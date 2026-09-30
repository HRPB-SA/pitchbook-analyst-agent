#!/usr/bin/env python3
"""
CONTEXT: ANTHROPIC INTELLIGENCE DESK — compact query helper over the merged record, used by the analyst agents.

  python3 scripts/q.py --cat governance,safety [--from 2021-01-01] [--to 2026-09-30] [--q text] [--tier T1,T2]
                       [--conf HIGH,MEDIUM] [--limit 200] [--full]          # list events, one compact line each
  python3 scripts/q.py --ids evt-a,evt-b                                  # full JSON for specific events
  python3 scripts/q.py --table board_history|people_moves|rsp|offices|cases|pricing|plans|rounds|run_rate_desk|period_revenue|margins|customers|mix|projections|comparables|compute|compute_costs|market_share|prospectus_facts|offering_structure|risk_factor_themes|capital_summary
  python3 scripts/q.py --conflicts [--q text]                             # frozen conflicts
  python3 scripts/q.py --open [--q text]                                  # open [VERIFY] items
  python3 scripts/q.py --entities [--type investor] [--public]            # entity graph rows
Event ids are stable: an id that was merged into another event still resolves (data/id_map.json).
"""
import argparse, json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = lambda n: json.load(open(os.path.join(ROOT, "data", n)))

def compact_ex(x):
    out = []
    for k in ("amount_usd_m", "valuation_post_usd_m", "valuation_pre_usd_m", "revenue_run_rate_usd_m", "revenue_period_usd_m", "revenue_period", "margin_pct", "margin_type", "headcount", "customers"):
        if x.get(k) not in (None, "", []): out.append(f"{k}={x[k]}")
    cp = x.get("compute") or {}
    if any(cp.get(k) for k in ("partner", "usd_m", "gw")): out.append("compute=" + "/".join(str(cp.get(k)) for k in ("partner", "chips", "usd_m", "gw", "term") if cp.get(k)))
    pr = x.get("product") or {}
    if pr.get("name"): out.append("product=" + str(pr.get("name")) + (f" ${pr.get('price_in_per_mtok')}/{pr.get('price_out_per_mtok')}" if pr.get("price_in_per_mtok") is not None else ""))
    for k in ("governance", "moat", "strategy"):
        if x.get(k): out.append(f"{k}={str(x[k])[:140]}")
    return "; ".join(out)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cat"); ap.add_argument("--from", dest="dfrom"); ap.add_argument("--to", dest="dto"); ap.add_argument("--q")
    ap.add_argument("--tier"); ap.add_argument("--conf"); ap.add_argument("--limit", type=int, default=300); ap.add_argument("--full", action="store_true")
    ap.add_argument("--ids"); ap.add_argument("--table"); ap.add_argument("--conflicts", action="store_true"); ap.add_argument("--open", action="store_true")
    ap.add_argument("--entities", action="store_true"); ap.add_argument("--type"); ap.add_argument("--public", action="store_true")
    a = ap.parse_args()
    E = D("events.json"); idm = D("id_map.json"); byid = {e["id"]: e for e in E}
    if a.ids:
        for i in a.ids.split(","):
            e = byid.get(idm.get(i.strip(), i.strip()))
            print(json.dumps(e, indent=1, ensure_ascii=False) if e else f"# unknown id {i}")
        return
    if a.table:
        M = D("metrics.json"); key = {"pricing": "pricing", "rsp": "rsp", "margins": "margins", "customers": "customers"}.get(a.table, a.table)
        v = M.get(key)
        if v is None: print(f"# no table {a.table}; have: {', '.join(sorted(M))}"); return
        print(json.dumps(v, indent=0, ensure_ascii=False)); return
    if a.conflicts or a.open:
        L = D("ledger.json")
        rows = (L["cross_agent_conflicts"] + L["agent_conflicts"]) if a.conflicts else L["open_items"]
        for r in rows:
            s = json.dumps(r, ensure_ascii=False)
            if not a.q or a.q.lower() in s.lower(): print(s)
        return
    if a.entities:
        for r in D("entities.json"):
            if a.type and a.type not in r["types"]: continue
            if a.public and not r.get("public"): continue
            print(json.dumps({k: r.get(k) for k in ("name", "types", "public", "ticker", "amount_usd_m", "first_date", "degree")}, ensure_ascii=False) + "  " + "; ".join(r.get("notes", [])[:1]))
        return
    cats = set(a.cat.split(",")) if a.cat else None
    tiers = set(a.tier.split(",")) if a.tier else None
    confs = set(a.conf.split(",")) if a.conf else None
    n = 0
    for e in E:
        if cats and not (cats & set(e["category"])): continue
        if a.dfrom and e["date"] < a.dfrom: continue
        if a.dto and e["date"] > a.dto: continue
        if tiers and e["source"]["tier"] not in tiers: continue
        if confs and e["confidence"] not in confs: continue
        blob = (e["headline"] + " " + e["summary"] + " " + (e.get("notes") or "")).lower()
        if a.q and a.q.lower() not in blob: continue
        ex = compact_ex(e["extracted"])
        print(f"{e['date']} | {e['id']} | {e['source']['tier']}/{e['confidence']} | {e['headline']} — {e['summary']}" + (f" | {ex}" if ex else "") + (f" | notes: {e['notes'][:200]}" if a.full and e.get("notes") else "") + (f" | {e['source'].get('url')}" if a.full else ""))
        n += 1
        if n >= a.limit: print(f"# limit {a.limit} reached"); break

if __name__ == "__main__":
    main()
