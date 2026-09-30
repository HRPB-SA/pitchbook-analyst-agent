#!/usr/bin/env python3
"""
CONTEXT: ANTHROPIC INTELLIGENCE DESK — independent audit sample of the merged record.
Draws a stratified, seeded sample of events (numeric-claim events over-weighted), strips everything except what an independent auditor needs
(URL, date, headline, the one-sentence summary and the figures claimed), and writes two audit files for verify-audit-1 / verify-audit-2.
  python3 scripts/sample_audit.py            -> agents/briefs/audit_1.json, audit_2.json, agents/briefs/audit_key.json (id -> event id; do not show auditors)
  python3 scripts/sample_audit.py --score    -> reads agents/outputs/verify-audit-*.json, writes data/audit.json (precision by tier and category)
"""
import json, os, random, re, sys, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = lambda n: json.load(open(os.path.join(ROOT, "data", n)))
B, O = os.path.join(ROOT, "agents", "briefs"), os.path.join(ROOT, "agents", "outputs")
NUM = ("amount_usd_m", "valuation_post_usd_m", "valuation_pre_usd_m", "revenue_run_rate_usd_m", "revenue_period_usd_m", "margin_pct", "headcount")

def numeric(e):
    x = e["extracted"]; cp = x.get("compute") or {}; pr = x.get("product") or {}
    return any(x.get(k) for k in NUM) or cp.get("usd_m") or cp.get("gw") or pr.get("price_in_per_mtok") is not None

def claimed(e):
    x = e["extracted"]; out = {k: x[k] for k in NUM if x.get(k)}
    cp = x.get("compute") or {}; pr = x.get("product") or {}
    for k in ("partner", "usd_m", "gw", "term"):
        if cp.get(k): out[f"compute_{k}"] = cp[k]
    for k in ("name", "price_in_per_mtok", "price_out_per_mtok"):
        if pr.get(k) is not None: out[f"product_{k}"] = pr[k]
    return out

def sample():
    E = D("events.json"); rnd = random.Random(20260930)
    pool_num = [e for e in E if numeric(e) and e["source"].get("url")]; pool_txt = [e for e in E if not numeric(e) and e["source"].get("url")]
    def strat(pool, n, key):
        groups = collections.defaultdict(list)
        for e in pool: groups[key(e)].append(e)
        for g in groups.values(): rnd.shuffle(g)
        out, keys = [], sorted(groups)
        while len(out) < n and any(groups[k] for k in keys):
            for k in keys:
                if groups[k] and len(out) < n: out.append(groups[k].pop())
        return out
    picks = strat(pool_num, 28, lambda e: e["category"][0]) + strat(pool_txt, 20, lambda e: e["date"][:4])
    rnd.shuffle(picks)
    items, key = [], {}
    for i, e in enumerate(picks, 1):
        aid = f"A-{i:03d}"; key[aid] = e["id"]
        items.append({"audit_id": aid, "url": e["source"]["url"], "date": e["date"], "headline": e["headline"], "claimed_summary": e["summary"], "claimed_figures": claimed(e)})
    half = len(items) // 2
    for n, part in ((1, items[:half]), (2, items[half:])):
        json.dump({"auditor": f"verify-audit-{n}", "items": part}, open(os.path.join(B, f"audit_{n}.json"), "w"), indent=1, ensure_ascii=False)
    json.dump(key, open(os.path.join(B, "audit_key.json"), "w"), indent=1)
    print(f"sampled {len(items)} events ({sum(1 for p in picks if numeric(p))} with numeric claims); files: audit_1.json ({half}), audit_2.json ({len(items) - half})")

def score():
    E = {e["id"]: e for e in D("events.json")}; key = json.load(open(os.path.join(B, "audit_key.json")))
    rows = []
    for n in (1, 2):
        fn = os.path.join(O, f"verify-audit-{n}.json")
        if not os.path.exists(fn): continue
        for r in json.load(open(fn)).get("results", []):
            eid = key.get(r.get("audit_id"))
            if eid in E:
                v, note = r.get("verdict"), r.get("note") or ""
                orig = None
                if v == "SUPPORTED" and re.search(r"paywall|teaser|headline only|from the headline|could not (read|open)|body (is )?(not|un)", note, re.I):
                    orig, v = v, "UNOPENABLE"   # brief: a page whose body was not read cannot be rated SUPPORTED
                    note = "Orchestrator adjustment: auditor rated SUPPORTED without reading the body (paywall); counted as UNOPENABLE. Auditor note: " + note
                issues = [{"field": f.get("field"), "claimed": f.get("claimed"), "page_says": f.get("page_says"), "basis_note": f.get("basis_note")} for f in (r.get("figure_checks") or []) if f.get("match") is False]
                rows.append({"event_id": eid, "audit_id": r.get("audit_id"), "auditor": f"verify-audit-{n}", "tier": E[eid]["source"]["tier"], "category": E[eid]["category"][0], "verdict": v, "orig_verdict": orig, "note": note, "evidence": r.get("evidence"),
                             "figure_issues": issues, "figure_checks": r.get("figure_checks"), "url": E[eid]["source"]["url"], "headline": E[eid]["headline"]})
    c = collections.Counter(r["verdict"] for r in rows); opened = [r for r in rows if r["verdict"] != "UNOPENABLE"]
    ok = sum(1 for r in opened if r["verdict"] == "SUPPORTED"); part = sum(1 for r in opened if r["verdict"] == "PARTLY")
    by_tier = {t: {"n": sum(1 for r in opened if r["tier"] == t), "supported": sum(1 for r in opened if r["tier"] == t and r["verdict"] == "SUPPORTED")} for t in sorted({r["tier"] for r in opened})}
    out = {"n": len(rows), "verdicts": dict(c), "opened": len(opened), "supported_share": round(ok / len(opened), 3) if opened else None, "supported_or_partly_share": round((ok + part) / len(opened), 3) if opened else None,
           "by_tier": by_tier, "unopenable": c.get("UNOPENABLE", 0), "problems": [r for r in rows if r["verdict"] in ("NOT_SUPPORTED", "DATE_MISMATCH", "PARTLY")], "rows": rows,
           "sample_note": "Stratified seeded sample drawn from the merged record before the last four desks (deals, compute, revenue, S-1) had merged; numeric-claim events over-weighted (28 of 48). Precision here is for the record as sampled, not for events added later."}
    json.dump(out, open(os.path.join(ROOT, "data", "audit.json"), "w"), indent=1, ensure_ascii=False)
    print(json.dumps({k: out[k] for k in ("n", "verdicts", "opened", "supported_share", "supported_or_partly_share", "by_tier")}))

if __name__ == "__main__":
    score() if "--score" in sys.argv else sample()
