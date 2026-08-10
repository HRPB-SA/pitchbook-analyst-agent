"""Trend engine: what changed, what accelerated, what went stale, what fired.

Consumes the canonical profile + snapshot history for each company and writes
data/companies/<slug>/trends.json plus a cohort view across the universe.

Methodology rulings are hard-coded here so no downstream artifact can drift:
  R1  CE denominator = EQUITY ONLY (debt informs risk, never CE).
  R4  PitchBook "TTM" revenue fields are forward-window projections, never
      adopted as run-rate; ladders come from dated company/media prints.
Derived values are computed fresh on every run and labeled "Derived".
"""
from __future__ import annotations
import datetime as _dt
from . import schema, store


def _num(fact_or_none):
    if not schema.is_fact(fact_or_none):
        return None
    v = fact_or_none["value"]
    return float(v) if isinstance(v, (int, float)) else None


def ladder_trend(ladder):
    """A ladder is a list of Facts whose values are numbers, sorted by as_of.
    Returns direction plus per-step deltas."""
    pts = [(f["as_of"], float(f["value"])) for f in ladder
           if schema.is_fact(f) and isinstance(f["value"], (int, float))]
    if len(pts) < 2:
        return None
    steps = []
    for (d0, v0), (d1, v1) in zip(pts, pts[1:]):
        pct = (v1 - v0) / abs(v0) * 100 if v0 else None
        steps.append({"from": d0, "to": d1, "delta": round(v1 - v0, 4),
                      "pct": round(pct, 1) if pct is not None else None})
    deltas = [s["delta"] for s in steps]
    if len(deltas) >= 2 and deltas[-1] > deltas[-2] > 0:
        direction = "accelerating"
    elif all(d > 0 for d in deltas):
        direction = "rising"
    elif all(d < 0 for d in deltas):
        direction = "falling"
    else:
        direction = "mixed"
    return {"points": len(pts), "first": pts[0], "last": pts[-1],
            "direction": direction, "steps": steps}


def derived_metrics(profile):
    """Multiple, CE (equity-only), $/AIBQ-pt. Missing inputs -> omitted, never guessed."""
    out = {}
    val = _num(profile.get("valuation", {}).get("post_money_bn"))
    fin = profile.get("financials", {})
    ladder = fin.get("run_rate_ladder_bn") or []
    rr = None
    if ladder and schema.is_fact(ladder[-1]):
        rr = _num(ladder[-1])
        rr_asof = ladder[-1].get("as_of")
    eq = _num(profile.get("financing", {}).get("equity_raised_bn"))
    aibq = _num(profile.get("scores", {}).get("aibq_composite"))
    if val and rr:
        out["ev_multiple"] = {"value": round(val / rr, 1),
                              "basis": f"${val:g}B / ${rr:g}B run-rate (as of {rr_asof})",
                              "label": "Derived"}
    if rr and eq:
        out["capital_efficiency"] = {"value": round(rr / eq, 2),
                                     "basis": f"${rr:g}B run-rate / ${eq:g}B EQUITY-ONLY (Ruling 1)",
                                     "label": "Derived"}
    if val and aibq:
        out["usd_per_aibq_pt_bn"] = {"value": round(val / aibq, 1),
                                     "basis": f"${val:g}B / {aibq:g} AIBQ",
                                     "label": "Derived"}
    return out


def trigger_review(profile):
    """Named triggers are Facts whose value is a dict:
       {condition, status: armed|fired|expired, fired_on?}. Surfaced every run."""
    out = []
    for t in profile.get("triggers", {}).get("named", []) or []:
        if schema.is_fact(t):
            out.append({"trigger": t["value"], "as_of": t.get("as_of"),
                        "source": t.get("source")})
    return out


def snapshot_delta(slug):
    """Field-level diff between the two most recent snapshots (or None)."""
    names = store.snapshots(slug)
    if len(names) < 2:
        return None
    a, b = store.load_snapshot(slug, names[-2]), store.load_snapshot(slug, names[-1])
    changes = []
    for cat in schema.CATEGORIES:
        ba, bb = a.get(cat) or {}, b.get(cat) or {}
        # Snapshots are partial pulls by design: a field absent from the latest
        # snapshot is "not re-pulled", never "removed". Only report fields
        # present in the latest pull that are new or carry a different value.
        for field in sorted(bb):
            fa, fb = ba.get(field), bb.get(field)
            va = fa.get("value") if schema.is_fact(fa) else fa
            vb = fb.get("value") if schema.is_fact(fb) else fb
            if isinstance(fa, list) or isinstance(fb, list):
                la = [x.get("value") for x in (fa or []) if schema.is_fact(x)]
                lb = [x.get("value") for x in (fb or []) if schema.is_fact(x)]
                new_items = [v for v in lb if v not in la]
                if new_items:
                    changes.append({"field": f"{cat}.{field}",
                                    "from": f"{len(la)} item(s)",
                                    "to": f"+{len(new_items)} new: {new_items!r:.90}"})
                continue
            if va != vb:
                changes.append({"field": f"{cat}.{field}", "from": va, "to": vb})
    return {"from": names[-2], "to": names[-1], "changes": changes}


def company_trends(slug, today=None):
    profile = store.load_profile(slug)
    fin = profile.get("financials", {})
    trends = {
        "slug": slug,
        "computed": (_dt.date.today()).isoformat(),
        "ladders": {},
        "derived": derived_metrics(profile),
        "snapshot_delta": snapshot_delta(slug),
        "staleness": store.staleness_report(slug, today),
        "open_conflicts": store.load_conflicts(slug)["open"],
        "triggers": trigger_review(profile),
    }
    for key in ("run_rate_ladder_bn", "growth_yoy_pct_ladder", "gross_margin_pct_ladder"):
        lt = ladder_trend(fin.get(key) or [])
        if lt:
            trends["ladders"][key] = lt
    hc = profile.get("headcount", {}).get("employees_ladder")
    lt = ladder_trend(hc or [])
    if lt:
        trends["ladders"]["employees"] = lt
    store._write(store.company_dir(slug) + "/trends.json", trends)
    return trends


def cohort_view():
    """Cross-company ranking on multiple, CE, $/pt + staleness counts."""
    rows = []
    for c in store.universe()["companies"]:
        slug = c["slug"]
        p = store.load_profile(slug)
        d = derived_metrics(p)
        st = store.staleness_report(slug)
        rows.append({
            "slug": slug, "name": c.get("name", slug),
            "multiple": d.get("ev_multiple", {}).get("value"),
            "ce": d.get("capital_efficiency", {}).get("value"),
            "usd_per_pt_bn": d.get("usd_per_aibq_pt_bn", {}).get("value"),
            "stale_facts": len(st["stale"]), "flags": len(st["flagged"]),
        })
    rows.sort(key=lambda r: (r["usd_per_pt_bn"] is None, -(r["usd_per_pt_bn"] or 0)))
    return rows


def digest_md(slug):
    """Analyst-readable digest of the current trends.json."""
    t = company_trends(slug)
    p = store.load_profile(slug)
    name = p.get("identity", {}).get("name", {})
    name = name.get("value") if schema.is_fact(name) else slug
    L = [f"# Tracker digest: {name} ({t['computed']})", ""]
    if t["derived"]:
        L.append("## Derived metrics")
        for k, v in t["derived"].items():
            L.append(f"- {k}: {v['value']} ({v['basis']})")
        L.append("")
    if t["ladders"]:
        L.append("## Ladders")
        for k, lt in t["ladders"].items():
            f0, f1 = lt["first"], lt["last"]
            L.append(f"- {k}: {f0[1]:g} ({f0[0]}) -> {f1[1]:g} ({f1[0]}), "
                     f"{lt['direction']} over {lt['points']} prints")
        L.append("")
    sd = t["snapshot_delta"]
    if sd and sd["changes"]:
        L.append(f"## Changed since prior snapshot ({sd['from']} -> {sd['to']})")
        for ch in sd["changes"]:
            L.append(f"- {ch['field']}: {ch['from']!r} -> {ch['to']!r}")
        L.append("")
    if t["staleness"]["stale"]:
        L.append("## Stale facts (decay-class breach; refresh before citing)")
        for s in t["staleness"]["stale"]:
            L.append(f"- {s['field']} = {s['value']!r} as of {s['as_of']} "
                     f"({s['age_days']}d old, {s['decay']})")
        L.append("")
    if t["open_conflicts"]:
        L.append("## Open conflicts (frozen; both values ship or neither)")
        for c in t["open_conflicts"]:
            L.append(f"- {c['field']}: held {c['held']['value']!r} "
                     f"({c['held']['tier']}, {c['held'].get('as_of')}) vs "
                     f"challenger {c['challenger']['value']!r} "
                     f"({c['challenger']['tier']}, {c['challenger'].get('as_of')})")
        L.append("")
    if t["triggers"]:
        L.append("## Named triggers")
        for tr in t["triggers"]:
            v = tr["trigger"]
            L.append(f"- [{v.get('status', 'armed').upper()}] {v.get('condition')}"
                     + (f" (fired {v['fired_on']})" if v.get("fired_on") else ""))
    return "\n".join(L) + "\n"
