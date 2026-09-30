#!/usr/bin/env python3
"""
CONTEXT: ANTHROPIC INTELLIGENCE DESK — reconcile the independent re-derivations against the draft record.
Reads agents/private/claims_master.json (draft values) and agents/outputs/verify-{capital,operating,prospectus,compute}.json (independent answers),
compares the numeric and date fields that carry a tolerance, classifies each claim and writes the validation ledger into data/claims_ledger.json
(merge.py embeds it in data/ledger.json; this script also patches an existing ledger.json in place).
Only fields with a tolerance in the claim are compared mechanically (amounts, dates, prices). Text fields (basis, definitions, notes) are never pass/fail: they are shown side by side.
Verdicts: MATCH (every compared number agrees) · MISMATCH (a compared number differs beyond tolerance; frozen, both values shown) · PARTIAL (only a date differs, or the sources themselves
          disagree and the draft matches one of them) · NOTED (an answer with sources exists but has no number to compare; shown side by side) · UNTRACEABLE (no usable independent answer).
Confidence: HIGH (MATCH, >= 2 independent origins, best source <= T2) · MEDIUM (MATCH on one origin, or NOTED with a T1-T3 source) · DISPUTED (MISMATCH) · VERIFY (PARTIAL, UNTRACEABLE, other).
Run: python3 scripts/reconcile.py
"""
import json, os, re
from datetime import datetime
from urllib.parse import urlparse
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)
TR = {"T1": 1, "T2": 2, "T3": 3, "T4": 4, "T5": 5}
DATE_FIELDS = {"date", "release_date"}

def dom(u):
    try: return urlparse(u).netloc.lower().replace("www.", "")
    except Exception: return ""

def pure_num(v):
    """A number, or a short string that is essentially only a number with an optional unit. Anything else is text and is not compared."""
    if v is None or isinstance(v, bool): return None
    if isinstance(v, (int, float)): return float(v)
    s = str(v).strip().lower().replace(",", "").replace("$", "").replace("~", "").replace("usd", "")
    s = re.sub(r"^(about|approximately|approx\.?|over|nearly|around|more than|roughly|up to)\s+", "", s).strip()
    m = re.fullmatch(r"(-?\d+(?:\.\d+)?)\s*(trillion|tn|t|billion|bn|b|million|mm|m|%|x)?(\s*per\s*mtok)?", s)
    if not m: return None
    x, u = float(m.group(1)), m.group(2)
    if u in ("trillion", "tn", "t"): x *= 1_000_000
    elif u in ("billion", "bn", "b"): x *= 1000
    return x

def pdate(s):
    try: return datetime.strptime(str(s)[:10], "%Y-%m-%d")
    except Exception: return None

def as_list(v): return v if isinstance(v, list) else [v]

def compare(field, exp, got, tol):
    """-> (ok | None, detail). None = not mechanically comparable (missing or text)."""
    if exp in (None, "", []) or got in (None, "", []): return None
    if field in DATE_FIELDS:
        a = pdate(exp); bs = [pdate(x) for x in as_list(got)]
        if not a or any(b is None for b in bs): return None
        best = min(abs((a - b).days) for b in bs)
        return best <= (tol or 3), f"{exp} vs {got} ({best} days apart)"
    a = pure_num(exp); bs = [pure_num(x) for x in as_list(got)]
    if a is None or any(b is None for b in bs): return None
    rel_tol = tol if tol is not None else 0.05
    best = min((abs(a - b) / max(abs(a), abs(b)) if (a or b) else 0.0) for b in bs)
    return best <= rel_tol, f"{exp} vs {got} ({best * 100:.1f}% apart)"

def load(fn):
    try: return json.load(open(fn))
    except Exception: return None

def draft_matches_a_conflict_side(field, exp, tol, conflicts):
    for cf in conflicts or []:
        r = compare(field, exp, [cf.get("value_a"), cf.get("value_b")], tol)
        if r and r[0]: return True
    return False

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
    hint = ((a or {}).get("verdict_hint") or "").upper()
    cmp_rows = []
    for f, exp in (c.get("expect") or {}).items():
        if f not in (c.get("tol") or {}): continue          # text fields are never pass/fail
        r = compare(f, exp, found.get(f), c["tol"].get(f))
        if r is not None: cmp_rows.append((f, r[0], r[1]))
    hard_fail = [x for x in cmp_rows if not x[1] and x[0] not in DATE_FIELDS]
    soft_fail = [x for x in cmp_rows if not x[1] and x[0] in DATE_FIELDS]
    sources_disagree = hint == "CONFLICT" or bool((a or {}).get("conflicts"))
    if not a or not srcs or hint == "UNTRACEABLE":
        verdict = "UNTRACEABLE"
    elif not cmp_rows:
        verdict = "PARTIAL" if hint == "CONFLICT" else "NOTED"
    elif hard_fail:
        # the draft matching one side of a disagreement between the sources themselves is a partial, not a mismatch
        side = sources_disagree and all(draft_matches_a_conflict_side(f, (c.get("expect") or {}).get(f), c["tol"].get(f), (a or {}).get("conflicts")) for f, _, _ in hard_fail)
        verdict = "PARTIAL" if side else "MISMATCH"
    elif soft_fail:
        verdict = "PARTIAL"
    else:
        verdict = "MATCH"
    doms_re = {dom(s["url"]) for s in srcs} - {""}
    doms_dr = {dom(u) for u in c.get("draft_sources", [])} - {""}
    indep = len(doms_re | doms_dr) if verdict == "MATCH" else len(doms_re)
    same_origin = bool(doms_re) and doms_re <= doms_dr
    if verdict == "MATCH": conf = "HIGH" if indep >= 2 and best_tier <= 2 and not same_origin and hint != "PARTIAL" else "MEDIUM"
    elif verdict == "MISMATCH": conf = "DISPUTED"
    elif verdict == "NOTED": conf = "MEDIUM" if hint == "FOUND" and best_tier <= 3 else "VERIFY"
    else: conf = "VERIFY"
    red = []
    if same_origin: red.append("Re-derivation landed on the same publisher as the draft: one origin, not two.")
    if sources_disagree and a: red.append("Re-deriver found sources that disagree: " + "; ".join(f"{x.get('value_a')} vs {x.get('value_b')}" for x in (a.get("conflicts") or [])[:2]))
    if verdict == "MISMATCH": red.append("Frozen: draft and re-derivation disagree beyond tolerance; neither is adopted.")
    if verdict == "PARTIAL" and soft_fail: red.append("Number agrees; the date differs beyond tolerance.")
    if verdict == "NOTED": red.append("No number to compare mechanically: draft and re-derived text shown side by side.")
    if verdict == "UNTRACEABLE": red.append("No independent answer; the draft figure stays flagged until one is found.")
    if found.get("notes"): red.append(str(found["notes"])[:240])
    rows.append({"claim_id": c["claim_id"], "group": c["group"], "kind": c["kind"], "claim": c.get("label") or c["question"][:90], "draft": json.dumps(c.get("expect"), ensure_ascii=False)[:160],
                 "rederived": json.dumps({k: v for k, v in found.items() if k != "notes"}, ensure_ascii=False)[:260] if found else "", "verdict": verdict,
                 "compared": [{"field": f, "ok": ok, "detail": d} for f, ok, d in cmp_rows], "tier": f"T{best_tier}" if best_tier < 9 else (c.get("draft_tier") or "T3"), "cross_check": indep,
                 "confidence": conf, "sources": [s["url"] for s in srcs][:4], "draft_sources": c.get("draft_sources", [])[:2], "red_team": " ".join(red), "event_id": c.get("event_id")})

order = {"MISMATCH": 0, "UNTRACEABLE": 1, "PARTIAL": 2, "NOTED": 3, "MATCH": 4}
rows.sort(key=lambda r: (order[r["verdict"]], r["claim_id"]))
summary = {k: sum(1 for r in rows if r["verdict"] == k) for k in order}
out = {"generated": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"), "summary": summary, "claims": rows}
json.dump(out, open(P("data", "claims_ledger.json"), "w"), indent=1, ensure_ascii=False)
lg = load(P("data", "ledger.json"))
if lg is not None:
    lg["claims"] = rows; lg["claims_summary"] = summary; json.dump(lg, open(P("data", "ledger.json"), "w"), indent=1, ensure_ascii=False)
answered = sum(1 for c in master if c["claim_id"] in answers)
print(f"claims {len(rows)} ({answered} answered by a re-deriver so far): {summary}")
for r in rows:
    if r["verdict"] == "MISMATCH": print("  MISMATCH", r["claim_id"], r["claim"][:70], "|", [c["detail"] for c in r["compared"] if not c["ok"]])
