#!/usr/bin/env python3
"""Stage C pattern signals for the DTF attribution protocol.

Deterministic: reads inputs/sourced_dtf_history.csv and inputs/dtf_candidates.csv
(if present) plus the pair's universe.json, and writes patterns.json.

Usage: python3 scripts/patterns.py runs/<run_id>/pairs/<pair_id> [--inputs inputs]

When sourced history is missing, every sourced-pattern field is emitted with
status "not supplied" and the grade cap (Promising) is recorded in `caps`.
Optional fallback: if the pair directory holds pb_cadence.json (a list of
{"company", "deal_date", "fund_name"} rows from PitchBook investor investments),
its rows are reported under `pb_cadence` for cadence only and never counted as
sourced evidence.
"""
import argparse
import csv
import json
import sys
from collections import Counter
from datetime import date, timedelta
from pathlib import Path


def d(s):
    try:
        return date.fromisoformat(str(s)[:10])
    except (TypeError, ValueError):
        return None


def norm(s):
    return " ".join(str(s or "").lower().replace(",", " ").split())


def read_csv(path):
    if not path.exists():
        return None
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def by_fund(rows, key="fund_family"):
    c = Counter(r.get(key) or r.get("fund_name") or "unknown" for r in rows)
    return [{"fund": k, "count": v} for k, v in c.most_common()]


def window(rows, center, days):
    lo, hi = center - timedelta(days=days), center + timedelta(days=days)
    return [r for r in rows if (rd := d(r.get("deal_date"))) and lo <= rd <= hi]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pair_dir")
    ap.add_argument("--inputs", default="inputs")
    a = ap.parse_args()
    pair_dir = Path(a.pair_dir)
    inputs = Path(a.inputs)

    uni = json.loads((pair_dir / "universe.json").read_text())
    investor, company = uni.get("investor", ""), uni.get("company", "")
    deal_date = d(uni.get("deal_date"))
    deal_type = norm(uni.get("deal_type"))
    lead_partner = norm(uni.get("lead_partner"))
    if deal_date is None:
        sys.exit(f"{pair_dir}: universe.json has no valid deal_date")

    out = {"pair_id": uni.get("pair_id", pair_dir.name), "investor": investor,
           "company": company, "deal_date": deal_date.isoformat(), "caps": [],
           "inputs_used": []}

    hist = read_csv(inputs / "sourced_dtf_history.csv")
    if hist is None:
        na = {"status": "not supplied", "count": 0, "rows": []}
        for k in ("company_prior_funds", "period_deployment", "stage_pattern",
                  "partner_pattern", "candidate_first_deal"):
            out[k] = dict(na)
        out["caps"].append("sourced_dtf_history.csv missing -> grade capped at Promising")
    else:
        out["inputs_used"].append("sourced_dtf_history.csv")
        inv = [r for r in hist if norm(r.get("investor")) == norm(investor)]
        before = [r for r in inv if (rd := d(r.get("deal_date"))) and rd < deal_date]

        prior = [r for r in before if norm(r.get("company")) == norm(company)]
        out["company_prior_funds"] = {"status": "ok", "count": len(prior),
                                      "by_fund": by_fund(prior), "rows": prior}

        firsts = [r for r in inv if r.get("is_first_investment", "").upper() == "Y"]
        pdw = window(firsts, deal_date, 180)
        bf = by_fund(pdw)
        maj = bf[0]["fund"] if bf and bf[0]["count"] * 2 > len(pdw) else None
        out["period_deployment"] = {
            "status": "ok", "count": len(pdw), "by_fund": bf,
            "deployment_fund": maj,
            "summary": (f"{bf[0]['count']} of {len(pdw)} sourced first investments "
                        f"in +/-180d -> {bf[0]['fund']}") if bf else "no sourced first investments in window",
            "rows": pdw}

        stg = [r for r in window(inv, deal_date, 730) if norm(r.get("deal_type")) == deal_type]
        out["stage_pattern"] = {"status": "ok", "count": len(stg), "by_fund": by_fund(stg), "rows": stg}

        if not lead_partner:
            out["partner_pattern"] = {"status": "skipped: lead partner unknown", "count": 0, "rows": []}
        else:
            pp = [r for r in firsts if norm(r.get("lead_partner")) == lead_partner]
            pw = window(pp, deal_date, 730)
            out["partner_pattern"] = {"status": "ok", "all_time": {"count": len(pp), "by_fund": by_fund(pp)},
                                      "window_24m": {"count": len(pw), "by_fund": by_fund(pw)}, "rows": pp}

        cfd = {}
        for f in uni.get("funds", []):
            names = {norm(f.get("fund_name")), norm(f.get("family"))} - {""}
            dates = sorted(rd for r in inv if (rd := d(r.get("deal_date")))
                           and ({norm(r.get("fund_name")), norm(r.get("fund_family"))} & names))
            first = dates[0] if dates else None
            cfd[f.get("fund_name")] = {
                "earliest_sourced_deal": first.isoformat() if first else None,
                "has_sourced_deals_before_deal_date": bool(first and first < deal_date)}
        out["candidate_first_deal"] = {"status": "ok", "by_fund": cfd}

    cands = read_csv(inputs / "dtf_candidates.csv")
    if cands is None:
        out["dtf_rank"] = {"status": "not supplied", "rows": []}
    else:
        out["inputs_used"].append("dtf_candidates.csv")
        rows = [r for r in cands if norm(r.get("investor")) == norm(investor)
                and norm(r.get("company")) == norm(company)
                and (rd := d(r.get("deal_date"))) and abs((rd - deal_date).days) <= 45]

        def score(r):
            try:
                return float(r.get("dtf_score"))
            except (TypeError, ValueError):
                return float("-inf")
        rows.sort(key=score, reverse=True)
        out["dtf_rank"] = {"status": "ok" if rows else "no rows for this pair", "rows": [
            {"candidate_fund": r.get("candidate_fund"), "candidate_family": r.get("candidate_family"),
             "dtf_score": r.get("dtf_score"), "is_mg_first_investment_fund": r.get("is_mg_first_investment_fund"),
             "score_drivers": r.get("score_drivers")} for r in rows]}

    cad = pair_dir / "pb_cadence.json"
    if cad.exists():
        rows = json.loads(cad.read_text())
        out["pb_cadence"] = {"status": "PitchBook cadence only - not sourced DTF, not evidence",
                             "count_pm180d": len(window(rows, deal_date, 180)), "rows": rows}

    (pair_dir / "patterns.json").write_text(json.dumps(out, indent=2, default=str))
    print(f"{out['pair_id']}: patterns.json written; caps={out['caps'] or 'none'}")


if __name__ == "__main__":
    main()
