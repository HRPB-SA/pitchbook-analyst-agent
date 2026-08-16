"""Company store: append-only snapshots + canonical profile with
freeze-on-conflict merging.

Layout (repo-relative):
    companies/universe.json                coverage universe
    companies/<slug>/store/profile.json    canonical current record, by category
    companies/<slug>/store/snapshots/YYYY-MM-DD[.n].json   immutable pulls
    companies/<slug>/store/conflicts.json  frozen conflicts (both values, never chosen)
    companies/<slug>/store/history.json    supersession log (old value, new value, why)
    companies/<slug>/store/trends.json     computed by engine.trends
    companies/<slug>/<category>/           analyst drop zones (documents, notes);
                                           research ingests them, tiered as provided
    companies/<slug>/PROFILE.md            readable export (engine.compose.export_profile_md)

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
COMPANIES = os.path.join(REPO, "companies")
DATA = COMPANIES  # legacy alias; universe.json lives at companies/universe.json

# Analyst-facing category subfolders scaffolded for every tracked company.
DROP_FOLDERS = ("financials", "valuation-and-deals", "products", "people",
                "customers", "competition", "filings", "news-and-events", "notes")


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
    return os.path.join(COMPANIES, slug, "store")


def add_company(slug, name, pb_entity_id=None, group="coverage", sector=None):
    """Register a company and scaffold its folder tree. Idempotent."""
    u = universe()
    if not any(c["slug"] == slug for c in u["companies"]):
        u["companies"].append({"slug": slug, "name": name,
                               "pb_entity_id": pb_entity_id, "group": group,
                               "sector": sector})
        _write(os.path.join(COMPANIES, "universe.json"), u)
    for folder in DROP_FOLDERS:
        d = os.path.join(COMPANIES, slug, folder)
        os.makedirs(d, exist_ok=True)
        keep = os.path.join(d, ".gitkeep")
        if not os.listdir(d):
            open(keep, "w").close()
    os.makedirs(company_dir(slug), exist_ok=True)
    return os.path.join(COMPANIES, slug)


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
    """Whether two stored values say the same thing.

    Exact equality freezes conflicts that are not conflicts. A refresh
    restating $4.01B as $4.0102B is the same figure carried to another
    decimal, and describing the same round as "Later Stage VC $500M (5th
    Round)" rather than "$500M Series D at $11.0B post" is the same deal in
    more words. Freezing those buries the real disagreements the mechanism
    exists to surface.

    Numbers match within a tenth of a percent. Text matches when one
    description contains the other's substance. Anything else is a genuine
    disagreement and freezes as before.
    """
    if isinstance(a, bool) or isinstance(b, bool):
        return a is b
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a == b:
            return True
        return bool(a) and abs((b - a) / abs(a)) < 0.001
    if isinstance(a, str) and isinstance(b, str):
        if a == b:
            return True
        ka, kb = _key_terms(a), _key_terms(b)
        # one description restating the other keeps every figure and name the
        # shorter one carried
        return bool(ka) and bool(kb) and (ka <= kb or kb <= ka)
    return json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)


def _key_terms(text):
    """The load-bearing tokens of a description: its figures and its names."""
    import re as _re
    out = set()
    for m in _re.finditer(r"\$?\d[\d,]*\.?\d*\s*[MBK]?\b", text):
        tok = m.group(0).strip().replace(",", "").rstrip(".")
        # a round ordinal ("5th") is phrasing; a money figure is substance
        if tok and not _re.fullmatch(r"\d{1,2}", tok):
            out.add(tok.upper())
    return out


def reconcile_conflicts(slug):
    """Re-test open conflicts and close the ones that were never conflicts.

    Freezing is deliberately hard to undo, which is right for a genuine
    disagreement and wrong for one opened by a rule that has since been
    corrected. Nothing is decided here: a conflict closes only when the two
    values turn out to say the same thing. Real disagreements stay frozen.
    """
    conflicts = load_conflicts(slug)
    profile = load_profile(slug)
    keep, closed = [], []
    for c in conflicts.get("open") or []:
        held, chal = c.get("held") or {}, c.get("challenger") or {}
        if _values_equal(held.get("value"), chal.get("value")):
            closed.append(c)
        else:
            keep.append(c)
    if not closed:
        return {"slug": slug, "closed": 0, "open": len(keep)}
    conflicts["open"] = keep
    conflicts.setdefault("closed", []).extend(
        dict(c, closed_on=_dt.date.today().isoformat(),
             why="not a disagreement: the two values state the same figure")
        for c in closed)
    still = {c["field"] for c in keep}
    for c in closed:
        cat, field = c["field"].split(".", 1)
        fact = (profile.get(cat) or {}).get(field)
        if schema.is_fact(fact) and c["field"] not in still:
            flags = [f for f in (fact.get("flags") or []) if f != "DISPUTED"]
            if flags:
                fact["flags"] = flags
            else:
                fact.pop("flags", None)
    save_profile(slug, profile)
    _write(os.path.join(company_dir(slug), "conflicts.json"), conflicts)
    return {"slug": slug, "closed": len(closed), "open": len(keep)}


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
