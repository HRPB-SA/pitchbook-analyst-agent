#!/usr/bin/env python3
"""Turn a sourced DTF history export into partner-study inputs.

Usage:
  python3 scripts/ingest_dtf_history.py inputs/sourced_dtf_history.csv runs/fund-partner-study \
      [--country-col investor_country --country "United States"] [--us-investors path.txt]
      [--label fund_family|fund_name] [--min-deals 15] [--min-funds 2]

Expected columns (DTF protocol §2): investor, investor_pbid (optional), company, company_pbid, deal_date,
deal_type, deal_size_usd, is_first_investment (Y/N), lead_partner, fund_name, fund_pbid, fund_family,
source_type, source_url. Column names are matched case-insensitively; extra columns are kept.

US filter: use --country-col if the export carries HQ country, else --us-investors (one investor name
or PBID per line, e.g. resolved from PitchBook investor profiles). With neither, no country filter.

Writes <study>/data/<firm>.deals.jsonl (all rows; follow-ons flagged) and <firm>.funds.json with one
entry per label. first_close is left EMPTY for enrichment from PitchBook fund profiles / Form D; the
earliest sourced deal per fund is recorded as `first_sourced_deal` only. It is not used as first_close,
because inferring fund start dates from the labels would leak the answer into the date rule.
Also writes <study>/data/_inventory.csv (per-firm counts) and prints a summary.
"""
import argparse
import csv
import json
import re
from collections import defaultdict
from pathlib import Path


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("study")
    ap.add_argument("--country-col")
    ap.add_argument("--country", default="United States")
    ap.add_argument("--us-investors")
    ap.add_argument("--label", default="fund_family", choices=["fund_family", "fund_name"])
    ap.add_argument("--min-deals", type=int, default=15)
    ap.add_argument("--min-funds", type=int, default=2)
    a = ap.parse_args()

    with open(a.csv, newline="", encoding="utf-8-sig") as f:
        rdr = csv.DictReader(f)
        rows = [{k.strip().lower(): (v or "").strip() for k, v in r.items()} for r in rdr]
    keep_names = None
    if a.us_investors:
        keep_names = {l.strip().lower() for l in open(a.us_investors) if l.strip()}

    by_firm = defaultdict(list)
    dropped = defaultdict(int)
    for r in rows:
        if a.country_col and r.get(a.country_col.lower(), "").lower() != a.country.lower():
            dropped["country"] += 1
            continue
        if keep_names is not None and r.get("investor", "").lower() not in keep_names \
                and r.get("investor_pbid", "").lower() not in keep_names:
            dropped["not in US investor list"] += 1
            continue
        lab = r.get(a.label) or r.get("fund_name")
        if not lab or not r.get("deal_date"):
            dropped["missing label or date"] += 1
            continue
        by_firm[r["investor"]].append(r)

    data = Path(a.study) / "data"
    data.mkdir(parents=True, exist_ok=True)
    inv = []
    for firm, rs in by_firm.items():
        labels = defaultdict(list)
        for r in rs:
            labels[r.get(a.label) or r["fund_name"]].append(r["deal_date"][:10])
        firsts = [r for r in rs if r.get("is_first_investment", "").upper() in ("Y", "YES", "TRUE", "1")]
        partners = {r.get("lead_partner") for r in firsts if r.get("lead_partner")}
        eligible = len(firsts) >= a.min_deals and len(labels) >= a.min_funds
        inv.append({"firm": firm, "rows": len(rs), "first_investments": len(firsts),
                    "with_partner": sum(bool(r.get("lead_partner")) for r in firsts),
                    "distinct_partners": len(partners), "labels": len(labels), "study_eligible": eligible})
        if not eligible:
            continue
        s = slug(firm)
        with (data / f"{s}.deals.jsonl").open("w") as f:
            for r in sorted(rs, key=lambda r: r["deal_date"]):
                f.write(json.dumps({"firm": firm, "investor_pbid": r.get("investor_pbid"), "company": r.get("company"),
                                    "company_pbid": r.get("company_pbid"), "fund_label": r.get(a.label) or r["fund_name"],
                                    "fund_name": r.get("fund_name"), "fund_pbid": r.get("fund_pbid"),
                                    "deal_date": r["deal_date"][:10], "deal_type": r.get("deal_type"),
                                    "deal_size_usd": r.get("deal_size_usd"), "lead_partner": r.get("lead_partner") or None,
                                    "followon": r.get("is_first_investment", "").upper() not in ("Y", "YES", "TRUE", "1"),
                                    "source_type": r.get("source_type"), "source_url": r.get("source_url")}) + "\n")
        fund_pbids = defaultdict(set)
        for r in rs:
            if r.get("fund_pbid"):
                fund_pbids[r.get(a.label) or r["fund_name"]].add(r["fund_pbid"])
        (data / f"{s}.funds.json").write_text(json.dumps([
            {"fund_label": k, "fund_pbids": sorted(fund_pbids[k]), "first_close": "", "type": "main",
             "first_sourced_deal": min(v), "n_sourced": len(v)} for k, v in sorted(labels.items(), key=lambda x: min(x[1]))], indent=1))
    inv.sort(key=lambda x: -x["first_investments"])
    with (data / "_inventory.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(inv[0].keys()) if inv else ["firm"])
        w.writeheader()
        w.writerows(inv)
    print(f"rows read {len(rows)}; firms {len(by_firm)}; study-eligible {sum(i['study_eligible'] for i in inv)}; dropped {dict(dropped)}")
    print("NEXT: fill first_close + type (main/opportunity/sector/geo) in each *.funds.json from PitchBook fund profiles, then run scripts/partner_study.py")


if __name__ == "__main__":
    main()
