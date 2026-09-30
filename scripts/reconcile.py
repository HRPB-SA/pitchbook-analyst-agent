#!/usr/bin/env python3
"""
CONTEXT: ANTHROPIC INTELLIGENCE DESK — reconcile the independent re-derivations against the draft record.
Reads agents/private/claims_master.json (draft values) and agents/outputs/verify-capital.json / verify-operating.json (independent answers),
compares field by field within tolerance, classifies each claim and writes the validation ledger rows into data/claims_ledger.json
(merge.py embeds them in data/ledger.json; this script also patches an existing ledger.json in place).
Verdicts: MATCH (all compared fields agree) · PARTIAL (some agree, some missing) · MISMATCH (a compared field differs beyond tolerance; frozen, both values shown)
          · UNTRACEABLE (no usable independent answer).
Confidence: HIGH (MATCH and >= 2 independent origins, one >= T2) · MEDIUM (MATCH, single origin or same origin as the draft) · DISPUTED (MISMATCH) · VERIFY (PARTIAL/UNTRACEABLE).
Run: python3 scripts/reconcile.py
"""
import json, os, re
from datetime import datetime
from urllib.parse import urlparse
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)
TR = {"T1": 1, "T2": 2, "T3": 3, "T4": 4, "T5": 5}

def dom(u):
    try: return urlparse(u).netloc.lower().replace("www.", "")
    except Exception: return ""

def num(v):
    if v is None or v == "" or isinstance(v, bool): return None
    if isinstance(v, (int, float)): return float(v)
    s = str(v).replace(",", "").replace("$", "")
    m = re.search(r"-?\d+(?:\.\d+)?", s)
    if not m: return None
    x = float(m.group(0))
    tail = s[m.end():m.end() + 12].lower()
    if re.match(r"\s*(t|trillion)", tail): x *= 1_000_000
    elif re.match(r"\s*(b|bn|billion)", tail): x *= 1000
    elif "%" in tail[:2]: pass
    return x

def pdate(s):
    try: return datetime.strptime(str(s)[:10], "%Y-%m-%d")
    except Exception: return None

def compare(field, exp, got, tol):
    if exp in (None, "", []) or got in (None, "", []): return None
    if field in ("date", "release_date"):
        a, b = pdate(exp), pdate(got)
        if not a or not b: return None
        return abs((a - b).days) <= (tol or 3), f"{exp} vs {got}"
    a, b = num(exp), num(got)
    if a is None or b is None:
        return (str(exp).lower().strip() in str(got).lower() or str(got).lower().strip() in str(exp).lower()), f"{exp} vs {got}"
    if a == 0 and b == 0: return True, "0 vs 0"
    rel = abs(a - b) / max(abs(a), abs(b))
    return rel <= (tol if tol is not None else 0.05), f"{exp} vs {got} ({rel*100:.1f}% apart)"

def load(fn):
    try: return json.load(open(fn))
    except Exception: return None

master = (load(P("agents", "private", "claims_master.json")) or {}).get("claims", [])
answers = {}
for g in ("capital", "operating", "prospectus", "compute"):
    d = load(P("agents", "outputs", f"verify-{g}.json"))
    for a in (d or {}).get("answers", []): answers[a.get("claim_id")] = a

rows = []
for c in master:
    a = answers.get(c["claim_id"]); found = (a or {}).get("found") or {}
    srcs = [s for s in (a or {}).get("sources", []) if isinstance(s, dict) and s.get("url") and s.get("opened") is not False]
    best_tier = min([TR.get(s.get("tier"), 9) for s in srcs], default=9)
    cmp_rows = []
    for f, exp in (c.get("expect") or {}).items():
        r = compare(f, exp, found.get(f), c["tol"].get(f))
        if r is not None: cmp_rows.append((f, r[0], r[1]))
    if not a or not srcs or a.get("verdict_hint") == "UNTRACEABLE":
        verdict = "UNTRACEABLE"
    elif not c.get("expect"):
        verdict = "PARTIAL"            # open-ended question: answer recorded, nothing to compare mechanically
    elif not cmp_rows:
        verdict = "PARTIAL"
    elif all(ok for _, ok, _ in cmp_rows):
        verdict = "MATCH"
    elif any(ok for _, ok, _ in cmp_rows):
        verdict = "MISMATCH"
    else:
        verdict = "MISMATCH"
    if a and a.get("conflicts") and verdict == "MATCH": verdict = "PARTIAL"   # the re-deriver itself found sources that disagree: not a clean match
    doms_re = {dom(s["url"]) for s in srcs} - {""}
    doms_dr = {dom(u) for u in c.get("draft_sources", [])} - {""}
    indep = len(doms_re | doms_dr) if verdict == "MATCH" else len(doms_re)
    same_origin = bool(doms_re) and doms_re <= doms_dr
    if verdict == "MATCH": conf = "HIGH" if indep >= 2 and best_tier <= 2 and not same_origin else "MEDIUM"
    elif verdict == "MISMATCH": conf = "DISPUTED"
    else: conf = "VERIFY"
    red = []
    if same_origin: red.append("Re-derivation landed on the same publisher as the draft: one origin, not two.")
    if a and a.get("conflicts"): red.append("Re-deriver found conflicting sources: " + "; ".join(f"{x.get('value_a')} vs {x.get('value_b')}" for x in a["conflicts"][:2]))
    if verdict == "MISMATCH": red.append("Frozen: draft and re-derivation disagree beyond tolerance; neither is adopted.")
    if verdict == "UNTRACEABLE": red.append("No independent answer; the draft figure stays flagged until one is found.")
    if found.get("notes"): red.append(str(found["notes"])[:200])
    rows.append({"claim_id": c["claim_id"], "group": c["group"], "kind": c["kind"], "claim": c.get("label") or c["question"][:90], "draft": json.dumps(c.get("expect"), ensure_ascii=False)[:160],
                 "rederived": json.dumps({k: v for k, v in found.items() if k != "notes"}, ensure_ascii=False)[:200] if found else "", "verdict": verdict,
                 "compared": [{"field": f, "ok": ok, "detail": d} for f, ok, d in cmp_rows], "tier": f"T{best_tier}" if best_tier < 9 else (c.get("draft_tier") or "T3"), "cross_check": indep,
                 "confidence": conf, "sources": [s["url"] for s in srcs][:4], "draft_sources": c.get("draft_sources", [])[:2], "red_team": " ".join(red), "event_id": c.get("event_id")})

order = {"MISMATCH": 0, "UNTRACEABLE": 1, "PARTIAL": 2, "MATCH": 3}
rows.sort(key=lambda r: (order[r["verdict"]], r["claim_id"]))
summary = {k: sum(1 for r in rows if r["verdict"] == k) for k in order}
out = {"generated": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"), "summary": summary, "claims": rows}
json.dump(out, open(P("data", "claims_ledger.json"), "w"), indent=1, ensure_ascii=False)
lg = load(P("data", "ledger.json"))
if lg is not None:
    lg["claims"] = rows; lg["claims_summary"] = summary; json.dump(lg, open(P("data", "ledger.json"), "w"), indent=1, ensure_ascii=False)
print(f"claims {len(rows)}: {summary}")
for r in rows:
    if r["verdict"] == "MISMATCH": print("  MISMATCH", r["claim_id"], r["claim"], "|", [c["detail"] for c in r["compared"] if not c["ok"]])
