"""Desk dashboard: the whole coverage universe as one self-contained page.

`python3 -m engine dashboard` reads the universe, every company's fact store,
its evidence locker and harvest log, the report templates and the shipped
reports, and writes a single HTML file with all of it baked in. No server, no
network at view time.

    Overview   every company, coverage, staleness, armed triggers, live feed
    Company    key figures, timeline, ladders, every fact, sources, evidence
    Search     one box across every fact, source and note in the universe
    Request    compose a report request with the full option set
    Add        register a new company and start its harvest

Everything carries a date. Facts carry `as_of` (the vintage of the
information); evidence carries `retrieved_at` (the moment we read it). Both
are shown, because they answer different questions.

The page is a view, never a source. Regenerate after every refresh.
"""
from __future__ import annotations

import datetime as _dt
import glob
import html
import json
import os

from . import evidence, harvest, schema, store

ASSET = os.path.join(os.path.dirname(__file__), "assets", "desk.html")
OUT_DEFAULT = os.path.join(store.REPO, "Report Automation", "dashboard", "desk.html")

# Request-builder option set. Anything the composer can honour belongs here.
OPTIONS = {
    "rigor": [
        (1, "1 — Quick read"), (2, "2 — Light"), (3, "3 — Standard"),
        (4, "4 — Deep"), (5, "5 — Full initiation rigor"),
    ],
    "audience": [
        ("desk", "The desk (internal)"), ("lp", "LPs and investors"),
        ("founder", "Founders and operators"), ("public", "Public / media-safe"),
    ],
    "angle": [
        ("auto", "Let the engine choose"), ("valuation", "Valuation and what is priced in"),
        ("growth", "Growth quality and durability"), ("competition", "Competitive position"),
        ("capital", "Capital efficiency and burn"), ("exit", "Path to exit"),
        ("risk", "Risk and the bear case"),
    ],
    "chart_look": [("house", "House (navy / slate / green)"), ("pb", "Published (teal)")],
    "length": [("template", "Template default"), ("short", "Shorter than default"),
               ("long", "Longer than default")],
    "analysis": [
        ("base_rate", "Base rate — what usually happens"),
        ("priced_in", "What is already expected"),
        ("unit_econ", "Unit economics"),
        ("capital_eff", "Capital efficiency (equity only)"),
        ("growth_quality", "Growth quality — where growth came from"),
        ("concentration", "Concentration risk"),
        ("path_exit", "Path to exit"),
        ("bear", "Bear case at full strength"),
        ("falsifier", "Falsifier with dated kill criteria"),
    ],
}


# ----------------------------------------------------------------- utilities

def _iso(d):
    return d.isoformat() if hasattr(d, "isoformat") else (d or None)


def _fact_row(cat, path, f, today):
    return {
        "cat": cat, "field": path,
        "value": f.get("value"),
        "as_of": f.get("as_of"),
        "age": schema.fact_age_days(f, today),
        "tier": f.get("tier"),
        "decay": f.get("decay") or schema.CATEGORIES[cat][1],
        "source": f.get("source"),
        "flags": f.get("flags") or [],
        "note": f.get("note"),
        "stale": bool(schema.fact_is_stale(f, cat, today)),
    }


def _mark_ladder_staleness(facts):
    """Only the newest print in a ladder is staleness-checked; history is
    supposed to be old."""
    last = {}
    for r in facts:
        if "[" in r["field"]:
            base, idx = r["field"].rsplit("[", 1)
            last[(r["cat"], base)] = max(last.get((r["cat"], base), -1),
                                         int(idx.rstrip("]")))
    for r in facts:
        if "[" in r["field"]:
            base, idx = r["field"].rsplit("[", 1)
            if int(idx.rstrip("]")) < last[(r["cat"], base)]:
                r["stale"] = False
    return facts


def _ladders(profile):
    """Every list-of-Facts as a dated series, for sparklines."""
    out = {}
    for cat in schema.CATEGORIES:
        blk = profile.get(cat)
        if not isinstance(blk, dict):
            continue
        for field, v in blk.items():
            if not isinstance(v, list) or len(v) < 2:
                continue
            pts = [{"as_of": f.get("as_of"), "value": f.get("value"),
                    "tier": f.get("tier"), "source": f.get("source"),
                    "note": f.get("note")}
                   for f in v if schema.is_fact(f)
                   and isinstance(f.get("value"), (int, float))]
            if len(pts) >= 2:
                pts.sort(key=lambda p: p["as_of"] or "")
                out[f"{cat}.{field}"] = pts
    return out


def _identity(profile):
    """Flatten the descriptive fields a reader wants in the header."""
    out = {}
    for cat, fields in (("identity", ("hq", "ceo", "founded", "website", "status",
                                      "sector", "employees", "description")),
                        ("leadership", ("ceo", "cto", "cfo"))):
        blk = profile.get(cat)
        if not isinstance(blk, dict):
            continue
        for f in fields:
            v = blk.get(f)
            if schema.is_fact(v) and f not in out:
                out[f] = {"value": v.get("value"), "as_of": v.get("as_of"),
                          "tier": v.get("tier"), "source": v.get("source")}
    return out


HEADLINE_SPEC = [
    ("Valuation", "valuation", ("pb_last_known_valuation_bn", "post_money_bn",
                                "valuation_ladder_bn"), "$", "B"),
    ("Run-rate", "financials", ("run_rate_ladder_bn", "run_rate_bn"), "$", "B"),
    ("Growth YoY", "financials", ("growth_yoy_pct_ladder", "growth_yoy_pct"), "", "%"),
    ("Gross margin", "financials", ("gross_margin_pct_ladder", "gross_margin_pct"), "", "%"),
    ("Headcount", "headcount", ("employees_ladder", "employees"), "", ""),
    ("Equity raised", "financing", ("equity_raised_bn", "total_raised_bn"), "$", "B"),
    ("Net revenue retention", "customers", ("nrr_pct",), "", ""),
    ("Customers", "customers", ("orgs", "customers"), "", ""),
]


def _headline(profile):
    tiles = []
    for label, cat, fields, pre, suf in HEADLINE_SPEC:
        blk = profile.get(cat)
        if not isinstance(blk, dict):
            continue
        for field in fields:
            v = blk.get(field)
            if isinstance(v, list) and v:
                v = v[-1]
            if not schema.is_fact(v):
                continue
            val = v.get("value")
            tiles.append({
                "label": label, "value": val, "prefix": pre, "suffix": suf,
                "as_of": v.get("as_of"), "tier": v.get("tier"),
                "source": v.get("source"), "note": v.get("note"),
                "flags": v.get("flags") or [],
                "field": f"{cat}.{field}",
            })
            break
    return tiles


def _timeline(profile, trigs):
    """Events, deals, trigger fires and valuation marks on one dated spine."""
    items = []

    def add(date, kind, text, source=None, tier=None, note=None):
        if not date:
            return
        items.append({"date": str(date), "kind": kind, "text": text,
                      "source": source, "tier": tier, "note": note})

    ev = profile.get("events")
    if isinstance(ev, dict):
        for f in ev.get("stream") or []:
            if schema.is_fact(f):
                add(f.get("as_of"), "event", str(f.get("value")),
                    f.get("source"), f.get("tier"), f.get("note"))

    val = profile.get("valuation")
    if isinstance(val, dict):
        for f in val.get("valuation_ladder_bn") or []:
            if schema.is_fact(f):
                add(f.get("as_of"), "mark", f"Valuation mark ${f.get('value')}B",
                    f.get("source"), f.get("tier"), f.get("note"))

    fin = profile.get("financials")
    if isinstance(fin, dict):
        for f in fin.get("run_rate_ladder_bn") or []:
            if schema.is_fact(f):
                add(f.get("as_of"), "print", f"Run-rate ${f.get('value')}B",
                    f.get("source"), f.get("tier"), f.get("note"))

    for t in trigs:
        if t.get("fired_on"):
            add(t["fired_on"], "trigger", "Trigger fired: " + t["condition"][:130],
                t.get("source"), None, t.get("note"))

    items.sort(key=lambda x: x["date"], reverse=True)
    return items


def _triggers(profile):
    out = []
    blk = profile.get("triggers")
    if not isinstance(blk, dict):
        return out
    for item in blk.get("named") or []:
        if not schema.is_fact(item):
            continue
        v = item.get("value")
        if not isinstance(v, dict):
            continue
        out.append({"condition": v.get("condition", ""),
                    "status": (v.get("status") or "armed").lower(),
                    "fired_on": v.get("fired_on"), "as_of": item.get("as_of"),
                    "source": item.get("source"), "note": item.get("note")})
    return out


def _sources_index(facts):
    """Distinct sources behind the facts, with how much each carries."""
    agg = {}
    for f in facts:
        src = (f.get("source") or "").strip()
        if not src:
            continue
        row = agg.setdefault(src, {"source": src, "n": 0, "tiers": {},
                                   "latest": None, "earliest": None,
                                   "cats": set()})
        row["n"] += 1
        t = f.get("tier") or "?"
        row["tiers"][t] = row["tiers"].get(t, 0) + 1
        row["cats"].add(f["cat"])
        d = f.get("as_of")
        if d:
            if not row["latest"] or d > row["latest"]:
                row["latest"] = d
            if not row["earliest"] or d < row["earliest"]:
                row["earliest"] = d
    out = []
    for row in agg.values():
        row["cats"] = sorted(row["cats"])
        row["tier"] = sorted(row["tiers"].items(), key=lambda kv: kv[0])[0][0] \
            if row["tiers"] else "?"
        out.append(row)
    out.sort(key=lambda r: (-r["n"], r["source"]))
    return out


def _templates():
    out = []
    for path in sorted(glob.glob(os.path.join(store.REPO, "report_template", "*.json"))):
        try:
            with open(path, encoding="utf-8") as fh:
                t = json.load(fh)
        except Exception:
            continue
        out.append({
            "id": t.get("id") or os.path.basename(path)[:-5],
            "name": t.get("name") or os.path.basename(path)[:-5],
            "kicker": t.get("kicker"),
            "pages": t.get("length_pages"),
            "rigor": t.get("rigor"),
            "sections": [{"id": s.get("id"), "title": s.get("title_hint") or s.get("id"),
                          "auto": bool(s.get("auto"))}
                         for s in (t.get("sections") or [])],
        })
    order = ["vertical_analyst_note", "company_update", "initiation_note",
             "rush_note", "earnings_note", "one_pager", "sector_overview"]
    out.sort(key=lambda t: order.index(t["id"]) if t["id"] in order else 99)
    return out


def _reports_index():
    """Shipped reports, mapped to the companies they cover."""
    out = []
    for d in sorted(glob.glob(os.path.join(store.REPO, "reports", "*"))):
        if not os.path.isdir(d):
            continue
        rid = os.path.basename(d)
        req = store._read(os.path.join(d, "request.json"), {})
        rep = store._read(os.path.join(d, "report.json"), {})
        outs = [os.path.basename(p) for p in
                glob.glob(os.path.join(d, "output", "*")) if os.path.isfile(p)]
        meta = rep.get("meta") or {}
        out.append({
            "id": rid,
            "title": meta.get("title") or rep.get("title") or rid,
            "subtitle": meta.get("subtitle") or rep.get("subtitle"),
            "template": req.get("template") or rep.get("template"),
            "companies": req.get("companies") or [],
            "submitted": req.get("submitted"),
            "idea": req.get("idea"),
            "outputs": outs,
        })
    out.sort(key=lambda r: r.get("submitted") or "", reverse=True)
    return out


# ---------------------------------------------------------------- collection

def collect(today=None):
    today = today or _dt.date.today()
    uni = store.universe()
    entries = uni.get("companies", uni if isinstance(uni, list) else [])
    reports = _reports_index()
    companies, search, feed = [], [], []

    for ent in entries:
        slug = ent.get("slug")
        if not slug:
            continue
        try:
            profile = store.load_profile(slug)
        except Exception:
            profile = {}

        conflicts = []
        try:
            raw = store.load_conflicts(slug)
            conflicts = raw if isinstance(raw, list) else raw.get("conflicts", [])
        except Exception:
            pass

        facts, cats = [], {}
        for cat, path, f in schema.walk_facts(profile):
            row = _fact_row(cat, path, f, today)
            facts.append(row)
            cats[cat] = cats.get(cat, 0) + 1
        _mark_ladder_staleness(facts)

        trigs = _triggers(profile)
        man = harvest.load_manifest(slug)
        hlog = harvest.load_log(slug)
        last_run = hlog[-1] if hlog else None
        estats = evidence.stats(slug)
        eidx = evidence.load_index(slug)
        eidx_sorted = sorted(eidx, key=lambda r: r.get("retrieved_at") or "",
                             reverse=True)

        # cross-company feed: what the harvester actually saw move
        if last_run:
            for r in last_run.get("results", []):
                if r.get("outcome") in ("new", "changed"):
                    feed.append({
                        "slug": slug, "name": ent.get("name", slug),
                        "at": r.get("checked_at"), "source": r.get("name"),
                        "kind": r.get("kind"), "outcome": r.get("outcome"),
                        "url": r.get("url"), "evidence_id": r.get("evidence_id"),
                        "delta": r.get("delta_chars"),
                    })

        for f in facts:
            search.append({
                "slug": slug, "name": ent.get("name", slug),
                "cat": f["cat"], "field": f["field"],
                "value": f["value"], "as_of": f["as_of"], "tier": f["tier"],
                "source": f["source"], "note": f["note"],
                "stale": f["stale"], "flags": f["flags"],
            })

        n_stale = sum(1 for f in facts if f["stale"])
        n_flag = sum(1 for f in facts
                     if any(x in ("DISPUTED", "VERIFY") for x in f["flags"]))
        cov = min(100, round(100 * len(cats) / max(len(schema.CATEGORIES), 1)))

        companies.append({
            "slug": slug, "name": ent.get("name", slug),
            "group": ent.get("group", "coverage"), "sector": ent.get("sector"),
            "pbid": ent.get("pb_entity_id"),
            "domain": man.get("domain"), "cik": man.get("cik"),
            "updated": profile.get("_updated"),
            "identity": _identity(profile),
            "headline": _headline(profile),
            "ladders": _ladders(profile),
            "timeline": _timeline(profile, trigs),
            "triggers": trigs,
            "conflicts": conflicts,
            "facts": facts,
            "cats": cats,
            "sources_index": _sources_index(facts),
            "evidence": {
                "records": estats["records"], "chars": estats["chars"],
                "kinds": estats["kinds"], "latest": estats["latest_retrieval"],
                "recent": [{"id": r["id"], "source": r["source_name"],
                            "kind": r["kind"], "retrieved_at": r["retrieved_at"],
                            "last_seen": r.get("last_seen"), "chars": r.get("chars"),
                            "url": r["url"], "seen": r.get("seen_count", 1)}
                           for r in eidx_sorted[:40]],
            },
            "harvest": {
                "sources": [{"id": s.get("id"), "name": s.get("name"),
                             "kind": s.get("kind"), "url": s.get("url"),
                             "enabled": s.get("enabled", True),
                             "frequency": s.get("frequency")}
                            for s in (man.get("sources") or [])],
                "last_run": last_run.get("finished_at") if last_run else None,
                "counts": last_run.get("counts") if last_run else {},
                "results": last_run.get("results") if last_run else [],
                "runs": len(hlog),
            },
            "snapshots": [str(s) for s in (store.snapshots(slug) or [])],
            "reports": [r["id"] for r in reports if slug in (r["companies"] or [])],
            "n_facts": len(facts), "n_cats": len(cats), "n_stale": n_stale,
            "n_flagged": n_flag, "n_conflicts": len(conflicts),
            "n_armed": sum(1 for t in trigs if t["status"] == "armed"),
            "n_fired": sum(1 for t in trigs if t["status"] == "fired"),
            "coverage": cov,
        })

    companies.sort(key=lambda c: (c["group"] != "frontier_five", -c["n_facts"]))
    feed.sort(key=lambda f: f.get("at") or "", reverse=True)

    return {
        "generated": today.isoformat(),
        "generated_at": evidence.now_utc(),
        "categories": list(schema.CATEGORIES),
        "cat_labels": {k: k.replace("_", " ") for k in schema.CATEGORIES},
        "templates": _templates(),
        "options": {k: [{"id": str(a), "label": b} for a, b in v]
                    for k, v in OPTIONS.items()},
        "companies": companies,
        "reports": reports,
        "search": search,
        "feed": feed[:120],
    }


# --------------------------------------------------------------------- render

def render(data):
    with open(ASSET, encoding="utf-8") as fh:
        page = fh.read()
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"),
                         default=str).replace("</", "<\\/")
    cos = data["companies"]
    subs = {
        "__DATA__": payload,
        "__GEN__": html.escape(data["generated"]),
        "__GENAT__": html.escape(data["generated_at"] or ""),
        "__NCO__": str(len(cos)),
        "__NFACTS__": str(sum(c["n_facts"] for c in cos)),
        "__NSTALE__": str(sum(c["n_stale"] for c in cos)),
        "__NARMED__": str(sum(c["n_armed"] for c in cos)),
        "__NEV__": str(sum(c["evidence"]["records"] for c in cos)),
        "__NTHIN__": str(sum(1 for c in cos if c["n_cats"] <= 2)),
    }
    for k, v in subs.items():
        page = page.replace(k, v)
    return page


def build(out=None, today=None):
    out = out or OUT_DEFAULT
    data = collect(today)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(render(data))
    return out, data
