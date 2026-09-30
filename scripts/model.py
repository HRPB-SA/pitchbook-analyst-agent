#!/usr/bin/env python3
"""
CONTEXT: ANTHROPIC INTELLIGENCE DESK — financial model, Python twin of assets/app.js computeModel().
Reads agents/outputs/analyst-model.json (assumptions per scenario + sources + comps, written by the
Financial Modeler agent from the verified record), computes the annual build for each scenario with the
same formulas the dashboard uses live, and writes data/model.json (assumptions + outputs + audit).
Run: python3 scripts/model.py
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "agents", "outputs", "analyst-model.json")
OUT = os.path.join(ROOT, "data", "model.json")

def lerp(a, b, t): return a + (b - a) * t

def compute(A):
    years = A["years"]; segs = list(A["mix_2026"].keys())
    R, seg, rows = {}, {}, {}
    put = lambda k, y, v: rows.setdefault(k, {}).__setitem__(y, v)
    for y in years:
        act = A.get("actuals", {}).get(str(y)) or A.get("actuals", {}).get(y) or {}
        if act.get("revenue") is not None: R[y] = act["revenue"]
        elif y == 2026: R[y] = A["revenue_2026"]
        else: R[y] = R[y - 1] * (1 + A["growth"].get(str(y), A["growth"].get(y, 0)))
        t = min(1, max(0, (y - 2026) / 4))
        seg[y] = {s: R[y] * lerp(A["mix_2026"][s], A["mix_2030"][s], t) for s in segs}
    g = lambda d, y, default=0: d.get(str(y), d.get(y, default)) if isinstance(d, dict) else default
    for y in years:
        act = A.get("actuals", {}).get(str(y)) or A.get("actuals", {}).get(y) or {}
        rev = R[y]; put("revenue", y, rev)
        for s in segs: put(f"seg_{s}", y, seg[y][s])
        put("revenue_net", y, rev * (1 - A["equalization_haircut"]))
        gm = act.get("gross_margin") if act.get("gross_margin") is not None else g(A["gross_margin"], y)
        put("gross_margin", y, gm); gp = rev * gm; put("gross_profit", y, gp); put("cogs", y, rev - gp)
        infer = act.get("inference_share") if act.get("inference_share") is not None else A["inference_share_of_cogs"]
        put("cogs_inference", y, (rev - gp) * infer); put("cogs_other", y, (rev - gp) * (1 - infer))
        rnd = rev * g(A["opex"]["rnd"], y); sm = rev * g(A["opex"]["sm"], y); ga = rev * g(A["opex"]["ga"], y); sbc = rev * g(A["sbc_pct"], y)
        train = g(A["training_usd_m"], y, None); train = train if train is not None else rev * g(A.get("training_pct", {}), y)
        for k, v in (("rnd", rnd), ("sm", sm), ("ga", ga), ("sbc", sbc), ("training", train)): put(k, y, v)
        opex = rnd + sm + ga + sbc; put("opex", y, opex)
        oi_ex = gp - opex; put("op_income_ex_training", y, oi_ex); put("om_ex_training", y, oi_ex / rev if rev else 0)
        oi_all = gp - opex - train; oi = oi_ex - (train if A.get("expense_training") else 0)
        put("op_income", y, oi); put("op_income_incl_training", y, oi_all); put("om", y, oi / rev if rev else 0)
        tax = oi_all * A["tax_rate"] if oi_all > 0 else 0; put("tax", y, tax)
        capex = g(A["capex_usd_m"], y); put("capex", y, capex)
        fcf = oi_all - tax + sbc - capex; put("fcf", y, fcf); put("fcf_margin", y, fcf / rev if rev else 0)
    cum = 0
    for y in years:
        if y >= 2024: cum += rows["fcf"][y]
        put("cum_fcf", y, cum)
    r = A["discount_rate"]; base = 2025; pv = {}; pv_sum = 0
    for y in [y for y in years if y >= 2026]:
        pv[y] = rows["fcf"][y] / (1 + r) ** (y - base)
        if y < 2030: pv_sum += pv[y]
    tv = rows["fcf"][2030] * A["terminal_multiple_fcf"]; pv_tv = tv / (1 + r) ** (2030 - base)
    val = {"dcf_ev": pv_sum + pv[2030] + pv_tv, "pv_fcf": pv_sum + pv[2030], "pv_tv": pv_tv, "marks": []}
    for k, ev in A["marks"].items():
        req_fcf = (ev - pv_sum) * (1 + r) ** (2030 - base) / (A["terminal_multiple_fcf"] + 1)
        fm = rows["fcf_margin"][2030]; req_rev = req_fcf / fm if fm > 0 else None
        cagr = (req_rev / R[2026]) ** 0.25 - 1 if req_rev else None
        val["marks"].append({"key": k, "label": A.get("mark_labels", {}).get(k, k), "ev": ev, "ev_rev_2026": ev / R[2026], "ev_rev_2027": ev / R[2027],
                             "ev_net_2026": ev / rows["revenue_net"][2026], "ev_net_2027": ev / rows["revenue_net"][2027], "req2030rev": req_rev, "req_cagr": cagr, "vs_dcf": ev / val["dcf_ev"] - 1})
    return {"years": years, "rows": rows, "valuation": val}

def main():
    if not os.path.exists(SRC):
        print(f"missing {SRC}", file=sys.stderr); sys.exit(1)
    src = json.load(open(SRC))
    out = dict(src)
    out["outputs"] = {}
    for scen, A in src["assumptions"].items():
        A.setdefault("years", [2024, 2025, 2026, 2027, 2028, 2029, 2030])
        out["outputs"][scen] = compute(A)
    out["engine"] = "scripts/model.py == assets/app.js computeModel(); formulas identical; EV treated as equity value (net cash ignored); FCF = operating income incl. training − cash tax + SBC − compute capex/prepayments."
    json.dump(out, open(OUT, "w"), indent=1)
    for scen, o in out["outputs"].items():
        R = o["rows"]
        print(f"{scen:5s} 2026E rev {R['revenue'][2026]/1000:.1f}B GM {R['gross_margin'][2026]*100:.0f}% | 2028E rev {R['revenue'][2028]/1000:.1f}B FCFm {R['fcf_margin'][2028]*100:.0f}% | 2030E rev {R['revenue'][2030]/1000:.1f}B | DCF EV {o['valuation']['dcf_ev']/1e6:.2f}T | cum FCF trough {min(R['cum_fcf'].values())/1000:.0f}B")

if __name__ == "__main__":
    main()
