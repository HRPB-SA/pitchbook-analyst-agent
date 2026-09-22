#!/usr/bin/env python3
"""Score whether the lead partner predicts the fund, beyond the date rule.

Usage: python3 scripts/partner_study.py runs/fund-partner-study

Inputs (per firm, under <study>/data/):
  <firm>.deals.jsonl  one line per labelled first investment:
      {"firm","company","fund_label","deal_date","lead_partner"(nullable),"deal_type","followon":false}
  <firm>.funds.json   [{"fund_label","first_close","type":"main|opportunity|sector|geo|other",
                        "investment_period_years"(optional)}]
Rules (leave-one-out within firm, first investments only):
  B0 date rule: newest main fund with first_close <= deal_date + 90d.
  B1 partner-majority: modal fund of the partner's OTHER labelled deals; fallback B0.
  B2 partner x window: modal fund of the partner's other deals within +/-18 months; fallback B0.
A deal is "contested" if >=2 funds were inside [first_close - 90d, first_close + period] on the date.
Writes <study>/results/scores.md and scores.json. Counts only, no percentages.
"""
import json
import sys
from collections import Counter, defaultdict
from datetime import date, timedelta
from pathlib import Path


def d(s):
    try:
        return date.fromisoformat(str(s)[:10])
    except (TypeError, ValueError):
        return None


def active(funds, dt):
    out = []
    for f in funds:
        fc = d(f.get("first_close"))
        if not fc:
            continue
        yrs = f.get("investment_period_years") or 5
        if fc - timedelta(days=90) <= dt <= fc + timedelta(days=int(365.25 * yrs)):
            out.append(f["fund_label"])
    return out


def b0(funds, dt):
    mains = [f for f in funds if f.get("type", "main") == "main" and d(f.get("first_close"))
             and d(f["first_close"]) <= dt + timedelta(days=90)]
    return max(mains, key=lambda f: d(f["first_close"]))["fund_label"] if mains else None


def modal(labels):
    if not labels:
        return None
    c = Counter(labels).most_common()
    return c[0][0] if len(c) == 1 or c[0][1] > c[1][1] else None  # ties -> no call


def score_firm(deals, funds):
    rows = []
    for i, r in enumerate(deals):
        dt = d(r["deal_date"])
        if dt is None:
            continue
        others = [o for j, o in enumerate(deals) if j != i and o.get("lead_partner")
                  and o.get("lead_partner") == r.get("lead_partner")]
        p0 = b0(funds, dt)
        p1 = modal([o["fund_label"] for o in others]) if r.get("lead_partner") else None
        win = [o["fund_label"] for o in others if d(o["deal_date"]) and abs((d(o["deal_date"]) - dt).days) <= 548]
        p2 = modal(win) if r.get("lead_partner") else None
        rows.append({**r, "b0": p0, "b1": p1 or p0, "b2": p2 or p0,
                     "b1_used_partner": p1 is not None, "b2_used_partner": p2 is not None,
                     "contested": len(active(funds, dt)) >= 2, "active_funds": active(funds, dt)})
    return rows


def counts(rows, key):
    ok = sum(r[key] == r["fund_label"] for r in rows)
    return f"{ok} of {len(rows)}"


def main():
    study = Path(sys.argv[1])
    data = study / "data"
    out = study / "results"
    out.mkdir(exist_ok=True)
    allrows, md = {}, ["# Partner → fund scoring", "", "Counts are correct calls / deals scored (first investments, leave-one-out).", "",
                       "| Firm | Deals | w/ partner | Contested | B0 date | B1 partner | B2 partner×window | B0 on contested | B2 on contested |",
                       "|---|---|---|---|---|---|---|---|---|"]
    purity = []
    for dealf in sorted(data.glob("*.deals.jsonl")):
        firm = dealf.name.replace(".deals.jsonl", "")
        funds = json.loads((data / f"{firm}.funds.json").read_text())
        deals = [json.loads(l) for l in dealf.read_text().splitlines() if l.strip()]
        deals = [r for r in deals if not r.get("followon") and r.get("fund_label")]
        rows = score_firm(deals, funds)
        allrows[firm] = rows
        con = [r for r in rows if r["contested"]]
        md.append(f"| {firm} | {len(rows)} | {sum(bool(r.get('lead_partner')) for r in rows)} | {len(con)} | "
                  f"{counts(rows, 'b0')} | {counts(rows, 'b1')} | {counts(rows, 'b2')} | "
                  f"{counts(con, 'b0') if con else '-'} | {counts(con, 'b2') if con else '-'} |")
        byp = defaultdict(list)
        for r in rows:
            if r.get("lead_partner"):
                byp[r["lead_partner"]].append(r["fund_label"])
        for p, labs in sorted(byp.items(), key=lambda x: -len(x[1])):
            c = Counter(labs)
            purity.append(f"| {firm} | {p} | {len(labs)} | " + ", ".join(f"{k}: {v}" for k, v in c.most_common()) + " |")
    md += ["", "## Partner spread across funds (labelled first investments)", "",
           "| Firm | Lead partner | Deals | By fund |", "|---|---|---|---|"] + purity
    md += ["", "## Where the partner changed the call (B2 ≠ B0)", "", "| Firm | Company | Date | Partner | Truth | B0 | B2 |", "|---|---|---|---|---|---|---|"]
    for firm, rows in allrows.items():
        for r in rows:
            if r["b2"] != r["b0"]:
                md.append(f"| {firm} | {r['company']} | {r['deal_date']} | {r.get('lead_partner')} | {r['fund_label']} | {r['b0']} | {r['b2']} |")
    (out / "scores.md").write_text("\n".join(md))
    (out / "scores.json").write_text(json.dumps(allrows, indent=1, default=str))
    print("\n".join(md[:6 + len(allrows)]))


if __name__ == "__main__":
    main()
