"""Company store: append-only snapshots + canonical profile with
freeze-on-conflict merging.

Layout (repo-relative):
    data/universe.json                     coverage universe
    data/companies/<slug>/profile.json     canonical current record, by category
    data/companies/<slug>/snapshots/YYYY-MM-DD[.n].json   immutable pulls
    data/companies/<slug>/conflicts.json   frozen conflicts (both values, never chosen)
    data/companies/<slug>/history.json     supersession log (old value, new value, why)
    data/companies/<slug>/trends.json      computed by engine.trends

Merge doctrine (cardinal rule 2, freeze-on-conflict):
  same value        -> refresh as_of/source if newer
  new value, strictly stronger-or-equal tier AND newer as_of -> supersede, log to history
  new value, weaker tier OR not newer  -> FREEZE: both values into conflicts.json,
                                          canonical keeps old value + DISPUTED flag.
Nothing is ever chosen silently.
"""
from __future__ import annotations
import json, os, datetime as _dt
from . import schema

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(REPO, "data")


def _read(path, default):
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    return default


def _write(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


def universe():
    return _read(os.path.join(DATA, "universe.json"), {"companies": []})


def company_dir(slug):
    return os.path.join(DATA, "companies", slug)


def load_profile(slug):
    return _read(os.path.join(company_dir(slug), "profile.json"), {"slug": slug})


def save_profile(slug, profile):
    profile["_updated"] = _dt.date.today().isoformat()
    _write(os.path.join(company_dir(slug), "profile.json"), profile)


def load_conflicts(slug):
    return _read(os.path.join(company_dir(slug), "conflicts.json"), {"open": [], "resolved": []})


def snapshots(slug):
    d = os.path.join(company_dir(slug), "snapshots")
    if not os.path.isdir(d):
        return []
    return sorted(f for f in os.listdir(d) if f.endswith(".json"))


def load_snapshot(slug, name):
    return _read(os.path.join(company_dir(slug), "snapshots", name), {})


def add_snapshot(slug, payload, as_of=None):
    """Write an immutable snapshot; auto-suffix if one already exists today."""
    as_of = as_of or _dt.date.today().isoformat()
    d = os.path.join(company_dir(slug), "snapshots")
    os.makedirs(d, exist_ok=True)
    name, n = f"{as_of}.json", 1
    while os.path.exists(os.path.join(d, name)):
        name = f"{as_of}.{n}.json"
        n += 1
    payload = dict(payload)
    payload.setdefault("_snapshot_date", as_of)
    _write(os.path.join(d, name), payload)
    return name


def _values_equal(a, b):
    return json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)


def merge_snapshot(slug, snap):
    """Merge a snapshot's category blocks into the canonical profile.
    Returns a report dict: refreshed / superseded / frozen / added lists."""
    profile = load_profile(slug)
    conflicts = load_conflicts(slug)
    history = _read(os.path.join(company_dir(slug), "history.json"), {"superseded": []})
    report = {"added": [], "refreshed": [], "superseded": [], "frozen": []}
    today = _dt.date.today().isoformat()

    for cat in schema.CATEGORIES:
        block = snap.get(cat)
        if not isinstance(block, dict):
            continue
        pblock = profile.setdefault(cat, {})
        for field, new in block.items():
            # Lists (ladders, event streams): append entries not already present.
            if isinstance(new, list):
                cur = pblock.setdefault(field, [])
                for item in new:
                    if not any(_values_equal(item, c) for c in cur):
                        cur.append(item)
                        report["added"].append(f"{cat}.{field}[] {_summ(item)}")
                if all(schema.is_fact(x) for x in cur):
                    cur.sort(key=lambda f: str(f.get("as_of", "")))
                continue
            if not schema.is_fact(new):
                if field not in pblock:
                    pblock[field] = new
                    report["added"].append(f"{cat}.{field}")
                continue
            old = pblock.get(field)
            if old is None or not schema.is_fact(old):
                pblock[field] = new
                report["added"].append(f"{cat}.{field} = {_summ(new)}")
                continue
            if _values_equal(old["value"], new["value"]):
                if str(new.get("as_of", "")) >= str(old.get("as_of", "")):
                    old["as_of"], old["source"], old["tier"] = new["as_of"], new["source"], new["tier"]
                    old.pop("flags", None) if "STALE" in (old.get("flags") or []) else None
                report["refreshed"].append(f"{cat}.{field}")
                continue
            newer = str(new.get("as_of", "")) > str(old.get("as_of", ""))
            stronger_or_equal = schema.tier_rank(new["tier"]) <= schema.tier_rank(old["tier"])
            if newer and stronger_or_equal:
                history["superseded"].append({
                    "date": today, "field": f"{cat}.{field}",
                    "old": old, "new": new,
                    "why": f"newer as_of ({new['as_of']} > {old.get('as_of')}) at tier {new['tier']} vs {old['tier']}",
                })
                pblock[field] = new
                report["superseded"].append(
                    f"{cat}.{field}: {_summ(old)} -> {_summ(new)}")
            else:
                conflicts["open"].append({
                    "opened": today, "field": f"{cat}.{field}",
                    "held": old, "challenger": new,
                    "rule": "freeze-on-conflict: challenger not (newer AND >= tier); surfaced, not chosen",
                })
                flags = set(old.get("flags") or [])
                flags.add("DISPUTED")
                old["flags"] = sorted(flags)
                report["frozen"].append(
                    f"{cat}.{field}: held {_summ(old)} vs challenger {_summ(new)}")

    save_profile(slug, profile)
    _write(os.path.join(company_dir(slug), "conflicts.json"), conflicts)
    _write(os.path.join(company_dir(slug), "history.json"), history)
    return report


def staleness_report(slug, today=None):
    """Every fact past its decay-class threshold, plus standing DISPUTED/VERIFY
    flags. Ladder entries are a time series: only the LATEST print in a list is
    staleness-checked; history is supposed to be old."""
    profile = load_profile(slug)
    out = {"stale": [], "flagged": []}
    last_idx = {}
    for cat, path, f in schema.walk_facts(profile):
        if "[" in path:
            base = path.rsplit("[", 1)[0]
            idx = int(path.rsplit("[", 1)[1].rstrip("]"))
            last_idx[(cat, base)] = max(last_idx.get((cat, base), -1), idx)
    for cat, path, f in schema.walk_facts(profile):
        if "[" in path:
            base = path.rsplit("[", 1)[0]
            idx = int(path.rsplit("[", 1)[1].rstrip("]"))
            if idx < last_idx[(cat, base)]:
                continue
        if schema.fact_is_stale(f, cat, today):
            out["stale"].append({
                "field": f"{cat}.{path}", "as_of": f.get("as_of"),
                "age_days": schema.fact_age_days(f), "value": f.get("value"),
                "decay": f.get("decay") or schema.CATEGORIES[cat][1],
            })
        for fl in (f.get("flags") or []):
            if fl in ("DISPUTED", "VERIFY"):
                out["flagged"].append({"field": f"{cat}.{path}", "flag": fl,
                                       "value": f.get("value"), "as_of": f.get("as_of")})
    return out


def _summ(f):
    if schema.is_fact(f):
        return f"{f['value']!r} ({f['tier']}, {f.get('as_of')})"
    return repr(f)[:60]
