#!/usr/bin/env python3
"""
CONTEXT: ANTHROPIC INTELLIGENCE DESK — Wave 2 claim list for the independent Source Re-derivers.
Selects the load-bearing figures the dashboard shows (rounds, debt, IPO facts, run-rate path, period revenue, margins, compute commitments,
prices, prospectus facts) from the desk tables and emits:
  agents/private/claims_master.json      claim + draft values + draft sources (for scripts/reconcile.py ONLY; re-derivers must never see it)
  agents/briefs/questions_capital.json   questions only (no answers, no sources) for verify-capital
  agents/briefs/questions_operating.json questions only for verify-operating
Run after the research desks finish: python3 scripts/make_claims.py
"""
import json, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M = json.load(open(os.path.join(ROOT, "data", "metrics.json")))
E = json.load(open(os.path.join(ROOT, "data", "events.json")))
PRIV, BRIEF = os.path.join(ROOT, "agents", "private"), os.path.join(ROOT, "agents", "briefs")
os.makedirs(PRIV, exist_ok=True)
claims = []

def add(group, kind, question, fields, expect, tol=None, draft_sources=(), draft_tier=None, label=None, event_id=None):
    cid = f"{'CAP' if group == 'capital' else 'OPS'}-{sum(1 for c in claims if c['group'] == group) + 1:03d}"
    claims.append({"claim_id": cid, "group": group, "kind": kind, "question": question, "fields": fields, "expect": expect, "tol": tol or {},
                   "draft_sources": [u for u in draft_sources if u], "draft_tier": draft_tier, "label": label, "event_id": event_id})

def usd(m):
    if m is None: return "n/a"
    return f"${m/1000:.1f}B" if m >= 1000 else f"${m:.0f}M"

def num(s):
    if s is None: return None
    if isinstance(s, (int, float)): return float(s)
    m = re.search(r"-?\d+(?:[.,]\d+)*", str(s).replace(",", ""))
    return float(m.group(0)) if m else None

# ---------------- capital ----------------
for r in M.get("rounds", []):
    if not r.get("round") or r.get("status") == "talks": continue
    add("capital", "round",
        f"Anthropic's '{r['round']}' financing: (1) announcement or close date; (2) amount raised in USD millions, and whether any part was debt, a convertible note or a secondary sale; (3) pre-money and post-money valuation in USD millions; (4) lead and co-lead investors as named by the company or a lead investor. Say whether the amount is announced or funded and whether the valuation is pre- or post-money.",
        ["date", "size_usd_m", "pre_usd_m", "post_usd_m", "leads", "notes"],
        {"date": r.get("date"), "size_usd_m": r.get("size_usd_m"), "pre_usd_m": r.get("pre_usd_m"), "post_usd_m": r.get("post_usd_m"), "leads": r.get("leads")},
        {"date": 3, "size_usd_m": 0.03, "pre_usd_m": 0.03, "post_usd_m": 0.03}, [r.get("source_url")], r.get("tier"),
        f"{r['round']}: {usd(r.get('size_usd_m'))} at {usd(r.get('post_usd_m'))} post ({r.get('date')})", r.get("event_id"))
cs = M.get("capital_summary") or {}
if cs.get("equity_only_usd_m"):
    add("capital", "total", "What is the total capital Anthropic has raised through Sep 30 2026 on an equity-only basis (priced rounds and strategic equity or convertible investments) versus including debt (revolvers, bonds)? List each component with its date and amount in USD millions, and say what PitchBook's 'Total Raised' field includes.",
        ["equity_only_usd_m", "debt_usd_m", "total_usd_m", "components"], {"equity_only_usd_m": cs.get("equity_only_usd_m"), "debt_usd_m": cs.get("debt_usd_m"), "total_usd_m": cs.get("total_usd_m")},
        {"equity_only_usd_m": 0.10, "debt_usd_m": 0.10, "total_usd_m": 0.10}, [], None, f"Total raised: {usd(cs.get('equity_only_usd_m'))} equity + {usd(cs.get('debt_usd_m'))} debt")
add("capital", "debt", "Anthropic debt financings: (1) the May 2025 revolving credit facility (size, banks); (2) the 2026 pre-IPO revolving credit facility (size, lead banks, date finalized); (3) whether Anthropic issued chip-purchase bonds in June 2026 (amount, tranches, issuer) or whether that description is wrong, and what the correct description is.",
    ["revolver_2025_usd_m", "revolver_2026_usd_m", "chip_bonds_usd_m", "chip_bonds_description", "notes"], {"revolver_2025_usd_m": 2500, "revolver_2026_usd_m": 15000}, {"revolver_2025_usd_m": 0.05, "revolver_2026_usd_m": 0.10}, [], None, "Revolvers ($2.5B May 2025; ~$15B pre-IPO) and the $34.5B chip-bond claim")
os_ = M.get("offering_structure") or {}
add("capital", "ipo", "Anthropic IPO as of Sep 30 2026: (1) has a public S-1 been filed (check SEC EDGAR) and when was the confidential draft submitted; (2) reported target raise and target valuation, and who reported them; (3) exchange; (4) reported timing (October vs November) with each outlet and date; (5) lead underwriters; (6) founder voting structure (class names, vote share).",
    ["public_s1", "confidential_submission_date", "target_raise_usd_m", "target_valuation_usd_m", "exchange", "timing_reports", "underwriters", "founder_vote_pct", "notes"],
    {"target_raise_usd_m": os_.get("target_raise_usd_m"), "target_valuation_usd_m": os_.get("target_valuation_usd_m"), "exchange": os_.get("exchange"), "founder_vote_pct": os_.get("founder_vote_pct")},
    {"target_raise_usd_m": 0.10, "target_valuation_usd_m": 0.10, "founder_vote_pct": 0.02}, os_.get("source_urls") or [], None, "IPO structure and timing")
for nm, q in (("Amazon", "Amazon's total investment in Anthropic through Sep 2026 (convertible notes vs equity; amounts and dates by tranche; carrying value in Amazon's latest filing) and Amazon's reported ownership range."),
              ("Google", "Google/Alphabet's total investment in Anthropic through Sep 2026 (amounts and dates by tranche; any 'up to' commitments) and reported ownership."),
              ("Microsoft and Nvidia", "The Nov 2025 Microsoft/Nvidia agreement: investment amounts ('up to' vs funded), the $30B Azure commitment, gigawatts, valuation cited, and what has been funded since.")):
    add("capital", "strategic", q, ["amount_usd_m", "funded_vs_up_to", "dates", "ownership_or_carrying_value", "notes"], {}, {}, [], None, f"{nm}: strategic investment")

# ---------------- operating ----------------
rr = [x for x in M.get("run_rate_desk", []) if x.get("run_rate_usd_m") and x.get("date")]
rr.sort(key=lambda x: x["date"]); seen_q = set(); pick = []
for x in rr:
    k = x["date"][:7] if x["date"] >= "2026-01" else x["date"][:4] + "Q" + str((int(x["date"][5:7]) - 1) // 3)
    if k in seen_q: continue
    seen_q.add(k); pick.append(x)
for x in pick:
    add("operating", "run_rate", f"What annualized revenue run-rate did Anthropic (company, CFO/CEO, investor documents or a named outlet citing sources) state for around {x['date'][:7]}? Give the figure in USD millions, the exact date it refers to, who stated it, and whether it is gross or net of cloud-partner resale. If several figures exist for that month, list each.",
        ["date", "run_rate_usd_m", "basis", "stated_by", "notes"], {"date": x["date"], "run_rate_usd_m": x["run_rate_usd_m"], "basis": x.get("basis")}, {"date": 20, "run_rate_usd_m": 0.12},
        [x.get("source_url")], x.get("tier"), f"Run-rate {usd(x['run_rate_usd_m'])} (~{x['date']})", x.get("event_id"))
for x in M.get("period_revenue", []):
    if x.get("usd_m") and re.search(r"actual|prelim", x.get("kind") or "", re.I):
        add("operating", "period_revenue", f"Anthropic revenue for {x['period']}: amount in USD millions, whether recognized, preliminary or run-rate, gross or net of cloud-partner resale, and who reported it (company, leaked prospectus, investor documents).",
            ["usd_m", "kind", "basis", "reported_by", "notes"], {"usd_m": x["usd_m"], "kind": x.get("kind"), "basis": x.get("basis")}, {"usd_m": 0.05}, [x.get("source_url")], x.get("tier"), f"Revenue {x['period']}: {usd(x['usd_m'])} ({x.get('kind')})")
for x in M.get("margins", [])[:14]:
    if x.get("metric") and x.get("value"):
        add("operating", "margin", f"Reported Anthropic {x['metric']} for {x.get('period')}: value, basis (before or after partner revenue share; before or after training compute; GAAP or adjusted), who reported it and when.",
            ["value", "basis", "reported_by", "notes"], {"value": x["value"], "basis": x.get("basis")}, {"value": 0.08}, [x.get("source_url")], x.get("tier"), f"{x['metric']} {x.get('period')}: {x['value']}")
for x in M.get("customers", [])[:8]:
    if x.get("metric") and x.get("value"):
        add("operating", "customer", f"Anthropic customer metric '{x['metric']}' around {x.get('date')}: value, date, and who stated it.", ["value", "date", "stated_by", "notes"], {"value": x["value"]}, {"value": 0.10}, [x.get("source_url")], x.get("tier"), f"{x['metric']}: {x['value']}")
comp = sorted([c for c in M.get("compute", []) if c.get("usd_m")], key=lambda c: -c["usd_m"])[:12]
for c in comp:
    add("operating", "compute", f"Anthropic's compute agreement with {c.get('partner')}: dollar value (USD millions) and whether 'up to' or contracted, gigawatts or MW, chip type, term, start, and who stated it and when. Is it a filed contract, a company announcement or a media report?",
        ["usd_m", "usd_basis", "gw", "chips", "term", "stated_by", "notes"], {"usd_m": c.get("usd_m"), "gw": c.get("gw"), "chips": c.get("chips")}, {"usd_m": 0.12, "gw": 0.15}, [c.get("source_url")], None, f"{c.get('partner')}: {usd(c.get('usd_m'))}" + (f", {c.get('gw')} GW" if c.get("gw") else ""), c.get("event_id"))
add("operating", "compute_total", "Totals reported for Anthropic's compute commitments as of Sep 2026: (1) the leaked prospectus total and the share that is non-cancelable, with the largest counterparties and amounts; (2) The Information's 'up to $517B / $531B in 11 months' figure and gigawatts; (3) any other total. State the basis (maximum contract value vs committed spend; years covered).",
    ["prospectus_total_usd_m", "non_cancelable_share", "information_total_usd_m", "information_gw", "notes"], {"prospectus_total_usd_m": 518000, "information_total_usd_m": 517000}, {"prospectus_total_usd_m": 0.05, "information_total_usd_m": 0.05}, [], None, "Compute commitment totals ($518B prospectus; $517B The Information)")
for p in M.get("pricing", []):
    if p.get("price_in_per_mtok") is not None and p.get("model") and re.search(r"opus|sonnet|haiku|fable|mythos", p["model"], re.I):
        add("operating", "price", f"Anthropic API list price for {p['model']} per million input and output tokens at launch, and any later changes, per Anthropic's own pricing or docs pages (state the date of the page).", ["price_in_per_mtok", "price_out_per_mtok", "release_date", "later_changes", "notes"],
            {"price_in_per_mtok": p["price_in_per_mtok"], "price_out_per_mtok": p["price_out_per_mtok"], "release_date": p.get("release_date")}, {"price_in_per_mtok": 0.02, "price_out_per_mtok": 0.02, "release_date": 3}, [p.get("source_url")], p.get("tier"), f"{p['model']}: ${p['price_in_per_mtok']}/${p['price_out_per_mtok']} per Mtok")
for f in M.get("prospectus_facts", [])[:14]:
    if f.get("metric") and f.get("value"):
        add("operating", "prospectus", f"What has been reported about Anthropic's draft IPO prospectus regarding '{f['metric']}' ({f.get('period_or_basis') or 'period not stated'}): value, who reported it (outlet, date), whether two outlets independently report it.", ["value", "reported_by", "date", "notes"],
            {"value": f["value"]}, {"value": 0.08}, [f.get("source_url")], f.get("tier"), f"Prospectus: {f['metric']} = {f['value']}")
if not any(c["group"] == "operating" and c["kind"] == "headcount" for c in claims):
    add("operating", "headcount", "Anthropic headcount: the most recent figure stated by the company or a named outlet, its date, and the trajectory over 2024-2026.", ["headcount", "date", "stated_by", "notes"], {}, {}, [], None, "Headcount")

json.dump({"claims": claims}, open(os.path.join(PRIV, "claims_master.json"), "w"), indent=1, ensure_ascii=False)
for g in ("capital", "operating"):
    qs = [{"claim_id": c["claim_id"], "question": c["question"], "fields_to_return": c["fields"]} for c in claims if c["group"] == g]
    json.dump({"auditor": f"verify-{g}", "as_of": "2026-09-30", "questions": qs}, open(os.path.join(BRIEF, f"questions_{g}.json"), "w"), indent=1, ensure_ascii=False)
    print(f"{g}: {len(qs)} questions")
