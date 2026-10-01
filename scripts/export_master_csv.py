#!/usr/bin/env python3
"""Build the master firm/fund/partner/focus CSV with an honest attribution classification.

Usage: python3 scripts/export_master_csv.py runs/vc-fund-database

Classifies each fund's lead_partners_source into:
  - Confirmed (named for this specific fund): a PitchBook team_members call on that exact fund ID,
    a fund-close press release, or a news article about that specific raise.
  - Prediction (firm's general roster, not confirmed for this fund): a firm team page, or a generic
    aggregator/profile page (Crunchbase org page, CB Insights investor profile, Wikipedia, PrivateEquityList,
    theorg.com, etc.) that describes the firm generally rather than naming a partner for one fund.
  - No partner data found: no lead_partners linked.
Also flags funds where a general roster was applied to a pre-2015 vintage (near-certain misattribution risk).
"""
import csv
import sqlite3
import sys
from pathlib import Path

GENERIC_AGGREGATORS = ("cbinsights.com/investor", "crunchbase.com/organization", "privateequitylist.com",
                       "signal.nfx.com/firms", "wellfound.com/company", "theorg.com/org", "rocketreach.co",
                       "vcsheet.com/fund", "vcsheet.com/who", "wikipedia.org", "fundingpost.com",
                       "investorlist.com", "startupintros.com")
GENERIC_PAGE_HINTS = ("/approach", "/about", ")", "(via search aggregation)")


def classify(src):
    if not src or src.startswith("PitchBook rate-limited"):
        return "no_data", ""
    if src == "pitchbook_team_members":
        return "confirmed", "PitchBook fund-level record (team_members called on this exact fund ID)"
    if src.startswith("web:firm-team-page:"):
        return "prediction", src[len("web:firm-team-page:"):]
    if src.startswith("web:fund-close-press:"):
        return "confirmed", src[len("web:fund-close-press:"):]
    if src.startswith("web:"):
        url = src[len("web:"):]
        if any(a in url for a in GENERIC_AGGREGATORS) or any(h in url for h in GENERIC_PAGE_HINTS):
            return "prediction", url
        return "confirmed", url
    return "prediction", src


def main():
    study = Path(sys.argv[1])
    con = sqlite3.connect(study / "database.db")
    cur = con.cursor()
    cur.execute("""
        SELECT firms.name, funds.fund_name, funds.vintage_year, funds.sector_focus, funds.sector_focus_specificity,
               funds.lead_partners_source, funds.id
        FROM funds JOIN firms ON firms.id = funds.firm_id
        ORDER BY firms.name, funds.vintage_year
    """)
    funds = cur.fetchall()
    cur.execute("SELECT fund_partners.fund_id, partners.name FROM fund_partners JOIN partners ON partners.id=fund_partners.partner_id")
    by_fund = {}
    for fid, name in cur.fetchall():
        by_fund.setdefault(fid, []).append(name)

    rows, counts = [], {}
    for firm, fund_name, vintage, focus, specificity, src, fid in funds:
        partners = sorted(set(by_fund.get(fid, [])))
        attribution, source_url = classify(src)
        if not partners:
            attribution = "no_data"
        counts[attribution] = counts.get(attribution, 0) + 1
        vintage_caution = ""
        if attribution == "prediction" and vintage and str(vintage).isdigit() and int(vintage) < 2015:
            vintage_caution = "ALSO: fund predates 2015 - this roster is almost certainly wrong for this fund"
        rows.append({
            "VC Firm": firm, "Fund Name": fund_name, "Vintage Year": vintage,
            "Fund Partner(s)": "; ".join(partners),
            "Attribution Type": {"confirmed": "Confirmed (named for this specific fund)",
                                 "prediction": "Prediction (firm's general roster, not confirmed for this fund)",
                                 "no_data": "No partner data found"}[attribution],
            "Source": source_url,
            "Fund Focus": focus,
            "Focus Specificity": "fund-specific" if specificity == "fund-specific" else "firm-level (general thesis)",
            "Additional Caution": vintage_caution,
        })

    print("Counts:", counts, "total:", sum(counts.values()))
    out = study / "exports" / "master_firm_fund_partner_focus.csv"
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["VC Firm", "Fund Name", "Vintage Year", "Fund Partner(s)",
                                          "Attribution Type", "Source", "Fund Focus", "Focus Specificity",
                                          "Additional Caution"])
        w.writeheader()
        w.writerows(rows)
    print("wrote", out)
    con.close()


if __name__ == "__main__":
    main()
