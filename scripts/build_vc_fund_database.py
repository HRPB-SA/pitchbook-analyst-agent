#!/usr/bin/env python3
"""Consolidate per-firm VC fund/partner/sector JSON files into one SQLite database + CSV exports.

Usage: python3 scripts/build_vc_fund_database.py runs/vc-fund-database

Reads: data/*.json (schema per BRIEF.md: firm, funds[] with lead_partners[] and sector_focus).
Writes: database.db (firms, funds, partners, fund_partners) + exports/*.csv. Idempotent (rebuilds each run).
"""
import csv
import json
import sqlite3
import sys
from pathlib import Path


def main():
    study = Path(sys.argv[1])
    db_path = study / "database.db"
    db_path.unlink(missing_ok=True)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.executescript("""
    CREATE TABLE firms (id INTEGER PRIMARY KEY, name TEXT UNIQUE, firm_pbid TEXT, website TEXT,
        description TEXT, in_pitchbook INTEGER, n_funds INTEGER, gaps TEXT);
    CREATE TABLE funds (id INTEGER PRIMARY KEY, firm_id INTEGER, fund_name TEXT, fund_pbid TEXT,
        vintage_year TEXT, fund_type TEXT, status TEXT, sector_focus TEXT, sector_focus_specificity TEXT,
        sector_focus_source TEXT, lead_partners_source TEXT, UNIQUE(firm_id, fund_name));
    CREATE TABLE partners (id INTEGER PRIMARY KEY, name TEXT UNIQUE, person_pbid TEXT);
    CREATE TABLE fund_partners (fund_id INTEGER, partner_id INTEGER, title TEXT,
        PRIMARY KEY (fund_id, partner_id));
    """)

    n_files, n_funds, n_fp, errors = 0, 0, 0, []
    for f in sorted(study.glob("data/*.json")):
        try:
            r = json.loads(f.read_text())
        except json.JSONDecodeError as e:
            errors.append(f"{f.name}: {e}")
            continue
        n_files += 1
        funds = r.get("funds") or []
        cur.execute("INSERT OR IGNORE INTO firms (name, firm_pbid, website, description, in_pitchbook, "
                    "n_funds, gaps) VALUES (?,?,?,?,?,?,?)",
                    (r.get("firm", f.stem), r.get("firm_pbid", ""), r.get("website", ""),
                     r.get("firm_description", ""), int(bool(r.get("in_pitchbook"))), len(funds),
                     json.dumps(r.get("gaps", []))))
        cur.execute("SELECT id FROM firms WHERE name=?", (r.get("firm", f.stem),))
        firm_id = cur.fetchone()[0]
        for fund in funds:
            cur.execute("INSERT OR IGNORE INTO funds (firm_id, fund_name, fund_pbid, vintage_year, "
                        "fund_type, status, sector_focus, sector_focus_specificity, sector_focus_source, "
                        "lead_partners_source) VALUES (?,?,?,?,?,?,?,?,?,?)",
                        (firm_id, fund.get("fund_name", ""), fund.get("fund_pbid", ""),
                         str(fund.get("vintage_year") or ""), fund.get("fund_type", ""), fund.get("status", ""),
                         fund.get("sector_focus", ""), fund.get("sector_focus_specificity", ""),
                         fund.get("sector_focus_source", ""), fund.get("lead_partners_source", "")))
            n_funds += 1
            cur.execute("SELECT id FROM funds WHERE firm_id=? AND fund_name=?", (firm_id, fund.get("fund_name", "")))
            row = cur.fetchone()
            if not row:
                continue
            fund_id = row[0]
            for p in fund.get("lead_partners") or []:
                name = p.get("name")
                if not name:
                    continue
                cur.execute("INSERT OR IGNORE INTO partners (name, person_pbid) VALUES (?,?)",
                            (name, p.get("person_pbid", "")))
                cur.execute("SELECT id FROM partners WHERE name=?", (name,))
                partner_id = cur.fetchone()[0]
                cur.execute("INSERT OR IGNORE INTO fund_partners (fund_id, partner_id, title) VALUES (?,?,?)",
                            (fund_id, partner_id, p.get("title", "")))
                n_fp += 1
    con.commit()

    exports = study / "exports"
    exports.mkdir(exist_ok=True)
    for name, q in [
        ("firms", "SELECT * FROM firms"),
        ("funds", """SELECT funds.*, firms.name AS firm_name FROM funds
                     JOIN firms ON firms.id = funds.firm_id"""),
        ("fund_partners", """SELECT firms.name AS firm, funds.fund_name, funds.vintage_year, funds.sector_focus,
                              funds.sector_focus_specificity, partners.name AS partner, fund_partners.title,
                              funds.lead_partners_source, funds.sector_focus_source
                              FROM fund_partners
                              JOIN funds ON funds.id = fund_partners.fund_id
                              JOIN firms ON firms.id = funds.firm_id
                              JOIN partners ON partners.id = fund_partners.partner_id
                              ORDER BY firms.name, funds.vintage_year"""),
    ]:
        cur2 = con.execute(q)
        cols = [d[0] for d in cur2.description]
        with (exports / f"{name}.csv").open("w", newline="") as fo:
            w = csv.writer(fo)
            w.writerow(cols)
            w.writerows(cur2.fetchall())

    n_firms = cur.execute("SELECT COUNT(*) FROM firms").fetchone()[0]
    n_pb = cur.execute("SELECT COUNT(*) FROM firms WHERE in_pitchbook=1").fetchone()[0]
    n_partners = cur.execute("SELECT COUNT(*) FROM partners").fetchone()[0]
    n_funds_db = cur.execute("SELECT COUNT(*) FROM funds").fetchone()[0]
    n_funds_with_partner = cur.execute("SELECT COUNT(DISTINCT fund_id) FROM fund_partners").fetchone()[0]
    n_funds_with_sector = cur.execute("SELECT COUNT(*) FROM funds WHERE sector_focus != ''").fetchone()[0]
    print(f"firms={n_firms} (in_pitchbook={n_pb}) funds={n_funds_db} partners={n_partners} "
          f"fund_partner_links={n_fp} funds_with_>=1_partner={n_funds_with_partner} "
          f"funds_with_sector={n_funds_with_sector}")
    if errors:
        print(f"JSON errors ({len(errors)}): " + "; ".join(errors[:5]))
    print(f"DB: {db_path}\nCSV exports: {exports}")
    con.close()


if __name__ == "__main__":
    main()
