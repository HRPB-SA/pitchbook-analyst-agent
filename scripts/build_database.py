#!/usr/bin/env python3
"""Consolidate all fund-partner-study label/enrichment files into one SQLite database + CSV exports.

Usage: python3 scripts/build_database.py runs/fund-partner-study

Reads:
  labels/*.jsonl            raw T2 portfolio-tag labels (firm, fund_label, company, source_url, tier, verbatim, accessed)
  data/*.deals.jsonl        enriched deal rows (firm, company, fund_label, deal_date, lead_partner, ...)
  data/*.funds.json         enriched fund metadata (fund_label, first_close, type, ...)
  labels/s1_*.jsonl         S-1/prospectus T1 labels (firm, company, fund_entity, fund_family, director_partner, ...)
  labels/s1_*_funds.json    S-1-lane fund entity metadata

Writes: database.db (SQLite: firms, funds, companies, partners, investments) + firms.csv, funds.csv,
investments.csv, partners.csv under <study>/exports/. Idempotent: drops and rebuilds tables each run.
"""
import csv
import json
import sqlite3
import sys
from pathlib import Path


def get_or_create(cur, table, key_col, key_val, extra=None):
    cur.execute(f"SELECT id FROM {table} WHERE {key_col}=?", (key_val,))
    row = cur.fetchone()
    if row:
        return row[0]
    cols = [key_col] + list((extra or {}).keys())
    vals = [key_val] + list((extra or {}).values())
    cur.execute(f"INSERT INTO {table} ({','.join(cols)}) VALUES ({','.join('?' * len(cols))})", vals)
    return cur.lastrowid


def main():
    study = Path(sys.argv[1])
    db_path = study / "database.db"
    db_path.unlink(missing_ok=True)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.executescript("""
    CREATE TABLE firms (id INTEGER PRIMARY KEY, name TEXT UNIQUE, website TEXT, lane TEXT);
    CREATE TABLE funds (id INTEGER PRIMARY KEY, firm_id INTEGER, fund_label TEXT, fund_type TEXT,
        first_close TEXT, final_close TEXT, size_usd TEXT, first_close_source TEXT, tier TEXT,
        UNIQUE(firm_id, fund_label));
    CREATE TABLE companies (id INTEGER PRIMARY KEY, name TEXT, website TEXT, UNIQUE(name, website));
    CREATE TABLE partners (id INTEGER PRIMARY KEY, firm_id INTEGER, name TEXT, UNIQUE(firm_id, name));
    CREATE TABLE investments (id INTEGER PRIMARY KEY, firm_id INTEGER, fund_id INTEGER, company_id INTEGER,
        partner_id INTEGER, deal_date TEXT, followon INTEGER, source_url TEXT, tier TEXT, verbatim TEXT,
        accessed TEXT, evidence_lane TEXT);
    """)

    def firm_id(name, website="", lane=""):
        return get_or_create(cur, "firms", "name", name, {"website": website, "lane": lane})

    def fund_id(fid, label, **kw):
        cur.execute("SELECT id FROM funds WHERE firm_id=? AND fund_label=?", (fid, label))
        row = cur.fetchone()
        if row:
            if any(kw.values()):
                sets = ", ".join(f"{k}=COALESCE(NULLIF({k},''), ?)" for k in kw)
                cur.execute(f"UPDATE funds SET {sets} WHERE id=?", list(kw.values()) + [row[0]])
            return row[0]
        cur.execute("INSERT INTO funds (firm_id, fund_label, fund_type, first_close, final_close, size_usd, "
                    "first_close_source, tier) VALUES (?,?,?,?,?,?,?,?)",
                    (fid, label, kw.get("fund_type", ""), kw.get("first_close", ""), kw.get("final_close", ""),
                     kw.get("size_usd", ""), kw.get("first_close_source", ""), kw.get("tier", "")))
        return cur.lastrowid

    def company_id(name, website=""):
        return get_or_create(cur, "companies", "name", name or website or "unknown", {"website": website})

    def partner_id_of(fid, name):
        if not name:
            return None
        return get_or_create(cur, "partners", "name", name, {"firm_id": fid}) if False else \
            get_or_create_partner(fid, name)

    def get_or_create_partner(fid, name):
        cur.execute("SELECT id FROM partners WHERE firm_id=? AND name=?", (fid, name))
        row = cur.fetchone()
        if row:
            return row[0]
        cur.execute("INSERT INTO partners (firm_id, name) VALUES (?,?)", (fid, name))
        return cur.lastrowid

    n_lab, n_enr, n_s1 = 0, 0, 0

    # 1. Raw T2 portfolio-tag labels
    for f in sorted((study / "labels").glob("*.jsonl")):
        if f.name.startswith(("firms_", "s1_")):
            continue
        for line in f.read_text().splitlines():
            if not line.strip():
                continue
            r = json.loads(line)
            fid = firm_id(r["firm"], r.get("firm_website", ""), "label")
            fund = fund_id(fid, r["fund_label"], tier=r.get("tier", "T2"))
            cid = company_id(r.get("company"), r.get("company_website", ""))
            cur.execute("INSERT INTO investments (firm_id, fund_id, company_id, deal_date, source_url, tier, "
                        "verbatim, accessed, evidence_lane) VALUES (?,?,?,?,?,?,?,?,?)",
                        (fid, fund, cid, "", r.get("source_url"), r.get("tier"), r.get("verbatim"),
                         r.get("accessed"), "portfolio_tag"))
            n_lab += 1

    # 2. Enriched deal+fund files
    for ff in sorted((study / "data").glob("*.funds.json")):
        slug = ff.name.replace(".funds.json", "")
        dealf = study / "data" / f"{slug}.deals.jsonl"
        if not dealf.exists():
            continue
        funds = json.loads(ff.read_text())
        deals = [json.loads(l) for l in dealf.read_text().splitlines() if l.strip()]
        firm_name = deals[0]["firm"] if deals else slug
        fid = firm_id(firm_name, "", "label+enrich")
        for fmeta in funds:
            fund_id(fid, fmeta["fund_label"], fund_type=fmeta.get("type", ""),
                    first_close=fmeta.get("first_close") or "", final_close=fmeta.get("final_close") or "",
                    size_usd=str(fmeta.get("size_usd") or ""), first_close_source=json.dumps(fmeta.get("first_close_source", {})),
                    tier="T1" if fmeta.get("first_close") else "")
        for r in deals:
            fund = fund_id(fid, r["fund_label"])
            cid = company_id(r.get("company"))
            pid = get_or_create_partner(fid, r["lead_partner"]) if r.get("lead_partner") else None
            cur.execute("INSERT INTO investments (firm_id, fund_id, company_id, partner_id, deal_date, followon, "
                        "source_url, tier, verbatim, accessed, evidence_lane) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                        (fid, fund, cid, pid, r.get("deal_date") or "", int(bool(r.get("followon"))),
                         (r.get("lead_partner_source") or {}).get("url", ""),
                         (r.get("lead_partner_source") or {}).get("tier", ""),
                         (r.get("lead_partner_source") or {}).get("verbatim", ""), "", "enriched"))
            n_enr += 1

    # 3. S-1 lane (T1 filing labels)
    for f in sorted((study / "labels").glob("s1_*.jsonl")):
        for line in f.read_text().splitlines():
            if not line.strip():
                continue
            r = json.loads(line)
            fid = firm_id(r["firm"], "", "s1")
            fund = fund_id(fid, r.get("fund_family") or r.get("fund_entity"), tier="T1")
            cid = company_id(r.get("company"))
            pid = get_or_create_partner(fid, r["director_partner"]) if r.get("director_partner") else None
            for dp in r.get("dated_purchases") or [{"date": ""}]:
                cur.execute("INSERT INTO investments (firm_id, fund_id, company_id, partner_id, deal_date, "
                            "source_url, tier, verbatim, accessed, evidence_lane) VALUES (?,?,?,?,?,?,?,?,?,?)",
                            (fid, fund, cid, pid, dp.get("date", ""), r.get("filing_url"), "T1",
                             r.get("entity_verbatim") or r.get("partner_verbatim"), r.get("accessed"), "s1_filing"))
                n_s1 += 1

    con.commit()

    exports = study / "exports"
    exports.mkdir(exist_ok=True)
    for name, q in [
        ("firms", "SELECT * FROM firms"),
        ("funds", "SELECT funds.*, firms.name AS firm_name FROM funds JOIN firms ON firms.id=funds.firm_id"),
        ("partners", "SELECT partners.*, firms.name AS firm_name FROM partners JOIN firms ON firms.id=partners.firm_id"),
        ("investments", """SELECT investments.id, firms.name AS firm, funds.fund_label, companies.name AS company,
                            partners.name AS lead_partner, deal_date, followon, investments.tier AS tier, evidence_lane, source_url, verbatim
                            FROM investments
                            LEFT JOIN firms ON firms.id=investments.firm_id
                            LEFT JOIN funds ON funds.id=investments.fund_id
                            LEFT JOIN companies ON companies.id=investments.company_id
                            LEFT JOIN partners ON partners.id=investments.partner_id"""),
    ]:
        cur2 = con.execute(q)
        cols = [d[0] for d in cur2.description]
        with (exports / f"{name}.csv").open("w", newline="") as fo:
            w = csv.writer(fo)
            w.writerow(cols)
            w.writerows(cur2.fetchall())

    n_firms = cur.execute("SELECT COUNT(*) FROM firms").fetchone()[0]
    n_funds = cur.execute("SELECT COUNT(*) FROM funds").fetchone()[0]
    n_inv = cur.execute("SELECT COUNT(*) FROM investments").fetchone()[0]
    n_partners = cur.execute("SELECT COUNT(*) FROM partners").fetchone()[0]
    print(f"firms={n_firms} funds={n_funds} partners={n_partners} investments={n_inv} "
          f"(portfolio_tag={n_lab} enriched={n_enr} s1_filing={n_s1})")
    print(f"DB: {db_path}")
    print(f"CSV exports: {exports}")
    con.close()


if __name__ == "__main__":
    main()
