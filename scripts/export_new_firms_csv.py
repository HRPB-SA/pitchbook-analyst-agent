#!/usr/bin/env python3
"""Export the discovery-batch (non-PitchBook push) firms with a PitchBook-check column.

Usage: python3 scripts/export_new_firms_csv.py runs/vc-fund-database
Reads new_firms_merged.tsv, pb_check.tsv, data/*.json. Writes exports/new_firms_pitchbook_check.csv
(one row per fund; firms with no named fund get one 'no fund identified' row carrying any firm-level roster)
and exports/new_firms_excluded.csv. Reuses classify() from export_master_csv.py.
"""
import csv, json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from export_master_csv import classify

def norm(s): return re.sub(r"[^a-z0-9]", "", (s or "").lower())
LABEL = {"confirmed": "Confirmed (named for this specific fund)",
         "prediction": "Prediction (firm's general roster, not confirmed for this fund)",
         "no_data": "No partner data found"}

def names(lst):
    out = []
    for p in lst or []:
        out.append(p.get("name", "") if isinstance(p, dict) else str(p))
    return [x for x in out if x]

def main():
    root = Path(sys.argv[1])
    new = [l.split("\t")[0] for l in (root / "new_firms_merged.tsv").read_text().splitlines()[1:]]
    pb = {}
    for l in (root / "pb_check.tsv").read_text().splitlines()[1:]:
        c = l.split("\t") + [""] * 6
        pb[norm(c[0])] = (c[1], c[4] if len(c) > 4 else "", c[5] if len(c) > 5 else "")
    data = {}
    for f in root.glob("data/*.json"):
        try: r = json.loads(f.read_text())
        except json.JSONDecodeError: continue
        data[norm(r.get("firm", ""))] = r
    rows, excl, seen = [], [], set()
    for name in new:
        k = norm(name)
        if k in seen or k not in data: continue
        seen.add(k); r = data[k]
        gaps = [g for g in (r.get("gaps") or []) if isinstance(g, str)]
        ex = next((g for g in gaps if "excluded" in g.lower()), None)
        status = pb.get(k, ("not checked", "", ""))[0]
        if ex:
            excl.append({"VC Firm": name, "Reason": ex, "PitchBook check": status}); continue
        base = {"VC Firm": r.get("firm", name), "HQ (as found)": r.get("hq", ""), "Website": r.get("website", ""),
                "PitchBook check": status, "Discovery lane": r.get("discovery_lane", "")}
        roster = names(r.get("firm_team")) or names(r.get("firm_partners")) or names(r.get("firm_level_partners"))
        funds = r.get("funds") or []
        if not funds:
            rows.append({**base, "Fund Name": "(no fund identified)", "Vintage Year": "",
                         "Fund Partner(s)": "; ".join(roster),
                         "Attribution Type": "Prediction (firm-level roster only; no fund identified)" if roster else LABEL["no_data"],
                         "Source": r.get("firm_team_source", ""), "Fund Focus": r.get("firm_description", ""),
                         "Focus Specificity": "firm-level (general thesis)"})
            continue
        for fd in funds:
            ps = sorted(set(names(fd.get("lead_partners"))))
            att, src = classify(fd.get("lead_partners_source", ""))
            if not ps: att = "no_data"
            rows.append({**base, "Fund Name": fd.get("fund_name", ""), "Vintage Year": fd.get("vintage_year") or "",
                         "Fund Partner(s)": "; ".join(ps), "Attribution Type": LABEL[att], "Source": src,
                         "Fund Focus": fd.get("sector_focus", ""),
                         "Focus Specificity": "fund-specific" if fd.get("sector_focus_specificity") == "fund-specific" else "firm-level (general thesis)"})
    out = root / "exports"
    for fn, data_rows in (("new_firms_pitchbook_check.csv", rows), ("new_firms_excluded.csv", excl)):
        with (out / fn).open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(data_rows[0].keys())); w.writeheader(); w.writerows(data_rows)
    from collections import Counter
    print("firm rows", len(rows), "excluded", len(excl))
    print(Counter(r["PitchBook check"] for r in rows))
    print(Counter(r["Attribution Type"][:10] for r in rows))
    print("firms by status:", Counter(pb.get(norm(n), ("not checked",))[0] for n in new if norm(n) in data))

main()
