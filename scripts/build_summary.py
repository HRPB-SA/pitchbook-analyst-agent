#!/usr/bin/env python3
"""
CONTEXT: ANTHROPIC INTELLIGENCE DESK — the one-page decision board.
Reads data/*.json and agents/outputs/certifier.json, computes every figure the board shows, embeds the result as JSON in assets/summary.template.html
and writes dist/summary.html: a single file that fetches nothing at view time (fonts and nothing else load from the network).
Every number on the board comes from the files read here; the only text written by hand is labels, captions and the disclosure wording, which repeats
the Sources tab of the main dashboard. Anything that cannot be parsed from the data is left out rather than guessed.
Run: python3 scripts/build_summary.py [--standalone]   (publish dist/summary.html as a private artifact page; --standalone also writes dist/summary.standalone.html for opening locally)
"""
import datetime
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)

FULL_DASHBOARD_URL = os.environ.get("FULL_DASHBOARD_URL", "https://claude.ai/artifact/Kstc8FDf1x7RTTVxQYAogS")
REPO_URL = os.environ.get("REPO_URL", "https://github.com/HRPB-SA/pitchbook-analyst-agent/tree/claude/gifted-keller-ec8zdz")
CERTIFIED_COMMIT = os.environ.get("CERTIFIED_COMMIT", "1fd56d1")   # the commit the Certifier's final pass ran against (agents/outputs/certifier.json: certified_against)


def load(*a):
    with open(P(*a), encoding="utf-8") as f:
        return json.load(f)


def git(*args):
    try:
        return subprocess.check_output(["git", *args], cwd=ROOT, text=True, stderr=subprocess.DEVNULL).strip()
    except Exception:
        return ""


T, M, C, L, A, G = (load("data", f) for f in ("thesis.json", "model.json", "compute.json", "claims_ledger.json", "audit.json", "certify.json"))
CE, E, LG, AL, ENT = (load("data", f) for f in ("certification.json", "events.json", "ledger.json", "agent_log.json", "entities.json"))
CERT = load("agents", "outputs", "certifier.json")
V = T["verdict"]

evmap = {}
for e in E:
    evmap[e["id"]] = e
    for m in e.get("merged_ids") or []:
        evmap.setdefault(m, e)


def evref(i):
    e = evmap.get(i)
    if not e:
        return None
    s = e.get("source") or {}
    return {"id": e["id"], "date": e["date"], "headline": e["headline"], "publisher": s.get("publisher"), "tier": s.get("tier"), "url": s.get("url")}


def evrefs(ids):
    return [r for r in (evref(i) for i in ids or []) if r]


# ---- reference marks and the Judge's call at each ----------------------------------------------------------------------------------------------------------
labels = M["assumptions"]["base"].get("mark_labels", {})
marks = []
for bm in V["by_mark"]:
    k = bm["mark"]
    ret = re.search(r"base-case return (?:of |is )?about ([+-]?\d+)% a year", bm["why"])
    by_scen = {}
    for s in ("bear", "base", "bull"):
        mk = next(m for m in M["outputs"][s]["valuation"]["marks"] if m["key"] == k)
        by_scen[s] = {"req2030rev_usd_m": mk["req2030rev"], "req_cagr": mk["req_cagr"], "vs_dcf": mk["vs_dcf"]}
    marks.append({"key": k, "label": labels.get(k, k), "ev_usd_m": bm["ev_usd_m"], "call": bm["call"], "why": bm["why"], "return_pct_a_year": int(ret.group(1)) if ret else None,
                  "by_scenario": by_scen, "events": evrefs(bm.get("event_ids"))})
marks.sort(key=lambda m: m["ev_usd_m"])

rat = " ".join(V["rationale"])
m_adj = re.search(r"adjusted base of \$([\d.]+)T(?: \(([^)]*)\))?", rat)
m_bands = re.search(r"LEAN BULLISH to about \$([\d.]+)T, NEUTRAL to \$([\d.]+)T, LEAN BEARISH to \$([\d.]+)T", rat)
bands = {"lean_bullish_max_usd_m": float(m_bands.group(1)) * 1e6, "neutral_max_usd_m": float(m_bands.group(2)) * 1e6, "lean_bearish_max_usd_m": float(m_bands.group(3)) * 1e6} if m_bands else None

# ---- the model: three scenarios, as stored in data/model.json ------------------------------------------------------------------------------------------------
years = sorted(int(y) for y in M["outputs"]["base"]["rows"]["revenue"])
i26, i30 = years.index(2026), years.index(2030)
scen = {}
for s in ("bear", "base", "bull"):
    o = M["outputs"][s]
    rev = [o["rows"]["revenue"][str(y)] for y in years]
    scen[s] = {"revenue_usd_m": rev, "fcf_usd_m": [o["rows"]["fcf"][str(y)] for y in years], "fcf_margin_2030": o["rows"]["fcf_margin"]["2030"],
               "dcf_ev_usd_m": o["valuation"]["dcf_ev"], "cagr_2026_2030": (rev[i30] / rev[i26]) ** 0.25 - 1}

ov = M["outside_view"]
br = next((b for b in ov["base_rates"] if "30% or more" in b["stat"]), None)
rates = [{"horizon": h, "pct": float(p)} for p, h in re.findall(r"(\d+(?:\.\d+)?)% over (one|three|five|ten) years?", br["value"])] if br else []
m_med = re.search(r"Median real CAGR above \$25B: ([\d.]+)% \(one year\), ([\d.]+)% \(three\), ([\d.]+)% \(five\)", br["value"]) if br else None
outside = {"reference_class": ov.get("reference_class"), "stat": br["stat"] if br else None, "rates": rates, "median_5y_pct": float(m_med.group(3)) if m_med else None,
           "source_url": br["source_url"] if br else None, "tier": br["tier"] if br else None}

# ---- facts the Certifier re-derived before it opened any deliverable --------------------------------------------------------------------------------------
FACT_LABEL = {"F1": "Last priced round", "F2": "Revenue run-rate", "F3": "FY2025 financials", "F4": "IPO status", "F5": "Compute commitments", "F6": "Gross margin",
              "F7": "Revenue-basis haircut", "F8": "Bartz v. Anthropic settlement"}
FACT_BASIS = {"F1": "Two origins", "F2": "One investor update, several outlets", "F3": "Press-reported from a leaked draft; no filing", "F4": "Reported; no public S-1",
              "F5": "Reported from the leaked draft", "F6": "Basis-dependent; no GAAP figure", "F7": "No public ruling found; conflict frozen", "F8": "Court-authorized site"}


def lead(text, clauses=2, cap=380):
    """First clauses of a long sentence, cut at a ';' or '. ' outside brackets; the full text stays one click away on the board."""
    depth, cuts = 0, []
    for i, ch in enumerate(text):
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth = max(0, depth - 1)
        elif depth == 0 and (ch == ";" or (ch == "." and text[i + 1:i + 2] == " ")):
            cuts.append(i)
    out = text[:cuts[clauses - 1]] if len(cuts) >= clauses else text
    if len(out) > cap:
        out = out[:cap].rsplit(" ", 1)[0] + "…"
    return out.strip().rstrip(".;")


def sentences(text, n):
    """First n sentences of a note (split at '. ' outside quotes is good enough for the Certifier's notes)."""
    parts = re.split(r"(?<=[.;]) (?=[A-Z'\"])", text.strip())
    return " ".join(parts[:n]).strip()


facts = []
for r in CE["rederived"]:
    fid = r["fact"]
    facts.append({"id": fid, "label": FACT_LABEL.get(fid, fid), "basis": FACT_BASIS.get(fid, ""), "headline": lead(r["value"]), "full": r["value"], "as_of": r["as_of"],
                  "single_source": bool(r.get("single_source")), "sources": [{"url": s["url"], "publisher": s["publisher"], "tier": s["tier"]} for s in r.get("sources", [])[:3]]})

# ---- evidence quality ------------------------------------------------------------------------------------------------------------------------------------------
recomputed = CERT.get("recomputed") or []
passes = []
ca = CERT.get("certified_against") or {}
for key in ("first_pass_head", "second_pass_head", "third_pass_head"):
    m = re.match(r"(\w+) \(verdict (NEEDS WORK|READY)(?:, blocking ([^)]*))?\)", ca.get(key, ""))
    if m:
        passes.append({"head": m.group(1), "verdict": m.group(2), "blocking": m.group(3) or ""})
fm = re.match(r"(\w+) ", ca.get("git_head", ""))
passes.append({"head": fm.group(1) if fm else CERTIFIED_COMMIT, "verdict": CERT.get("verdict"), "blocking": ""})
head = git("rev-parse", "--short", "HEAD")
later = [{"sha": ln.split(" ", 1)[0], "subject": ln.split(" ", 1)[1] if " " in ln else ""} for ln in git("log", "--format=%h %s", f"{CERTIFIED_COMMIT}..HEAD").splitlines() if ln.strip()]

evidence = {
    "gates": {"summary": G["summary"], "items": [{"id": g["id"], "status": g["status"], "name": g["name"], "detail": g["detail"]} for g in G["gates"]]},
    "audit": {"n": A["n"], "verdicts": A["verdicts"], "supported_share": A["supported_share"], "supported_or_partly_share": A["supported_or_partly_share"],
              "corrections": sum(1 for c in LG["corrections"] if str(c.get("id", "")).startswith("K-"))},
    "claims": {"n": len(L["claims"]), "summary": L["summary"]},
    "certifier": {"verdict": CE["verdict"], "finished": CE["finished"], "stats": CE["stats"], "blocking": len(CE["blocking"]), "non_blocking": len(CE["non_blocking"]),
                  "facts_agree": sum(1 for r in CE["reconciliation"] if r.get("agrees")), "facts_total": len(CE["reconciliation"]),
                  "recomputed_total": len(recomputed), "recomputed_ok": sum(1 for r in recomputed if r.get("within_tolerance")), "passes": passes,
                  "certified_commit": CERTIFIED_COMMIT, "later_commits": later,
                  "open_notes": [{"id": n["id"], "where": n.get("where"), "issue": sentences(n.get("issue") or "", 2)} for n in CE["non_blocking"] if str(n.get("where", "")).lower().startswith("judge")]},
}

# ---- compute commitments by firmness ----------------------------------------------------------------------------------------------------------------------
tot = C["totals"]
segs = [("documented", "Documented at T1/T2", tot["usd_m_contracted_t1_t2_documented"]), ("s1", "Prospectus press coverage (T3)", tot["usd_m_contracted_s1_coverage"]),
        ("upto", "“Up to”: cancellable or conditional", tot["usd_m_up_to"]), ("unconfirmed", "Reported, unconfirmed", tot["usd_m_reported_unconfirmed"])]
assert abs(sum(v for _, _, v in segs) - tot["usd_m_announced"]) < 1, "compute segments do not sum to the announced total"
compute = {"announced_usd_m": tot["usd_m_announced"], "contracted_usd_m": tot["usd_m_contracted"], "segments": [{"key": k, "label": l, "usd_m": v} for k, l, v in segs],
           "gw_announced": tot["gw_announced"], "gw_up_to_ceiling": tot["gw_up_to_ceiling"], "s1_reference_usd_m": tot["usd_m_s1_reference"], "s1_non_cancelable_share": tot["s1_non_cancelable_share"],
           "commitments": len(C["commitments"])}

# ---- frozen conflicts ---------------------------------------------------------------------------------------------------------------------------------------------
mismatches = [{"claim_id": r["claim_id"], "claim": r["claim"], "compared": [{"field": c["field"], "detail": c["detail"]} for c in r["compared"] if not c["ok"]], "tier": r["tier"],
               "sources": r["sources"][:2]} for r in L["claims"] if r["verdict"] == "MISMATCH"]

# ---- the record ------------------------------------------------------------------------------------------------------------------------------------------------------
by_year, by_tier, by_conf = {}, {}, {}
for e in E:
    by_year[e["date"][:4]] = by_year.get(e["date"][:4], 0) + 1
    by_tier[e["source"]["tier"]] = by_tier.get(e["source"]["tier"], 0) + 1
    by_conf[e["confidence"]] = by_conf.get(e["confidence"], 0) + 1
ent_n = len(ENT if isinstance(ENT, list) else ENT.get("entities", ENT))
waves = {}
for a in AL["agents"].values():
    waves[a.get("wave")] = waves.get(a.get("wave"), 0) + 1
record = {"events": len(E), "raw_findings": LG["raw_events"], "entities": ent_n, "first": min(e["date"] for e in E), "last": max(e["date"] for e in E),
          "by_year": dict(sorted(by_year.items())), "by_tier": dict(sorted(by_tier.items())), "by_confidence": by_conf,
          "agents": len(AL["agents"]), "waves": waves, "logged_actions": len(AL["log"])}

# ---- thesis-breakers and the evidence behind the Judge's reasoning ---------------------------------------------------------------------------------------
breakers = [{k: b.get(k) for k in ("metric", "threshold", "observable_by", "current", "status")} for b in T["thesis_breakers"]]
D = {
    "asof": "2026-09-30", "built": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "commit": head,
    "verdict": {"call": V["call"], "one_liner": V["one_liner"], "horizon": V["horizon"], "rationale": V["rationale"], "rationale_events": [evrefs(ids)[:3] for ids in V.get("rationale_ids") or []],
                "what_flips": V["what_flips"], "what_flips_events": [evrefs(ids)[:3] for ids in V.get("what_flips_ids") or []], "unresolved": T["unresolved"]},
    "marks": marks, "bands": bands, "adjusted_base_usd_m": float(m_adj.group(1)) * 1e6 if m_adj else None, "adjusted_base_note": (m_adj.group(2) if m_adj and m_adj.group(2) else None),
    "model": {"years": years, "scenarios": scen, "default_scenario": M.get("default_scenario")}, "outside": outside, "scorecard": T["scorecard"], "breakers": breakers,
    "evidence": evidence, "facts": facts, "compute": compute, "mismatches": mismatches, "record": record,
    "links": {"full_dashboard": FULL_DASHBOARD_URL, "repo": REPO_URL},
}

payload = json.dumps(D, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
with open(P("assets", "summary.template.html"), encoding="utf-8") as f:
    tpl = f.read()
assert "__DATA__" in tpl, "template has no __DATA__ placeholder"
os.makedirs(P("dist"), exist_ok=True)
with open(P("dist", "summary.html"), "w", encoding="utf-8") as f:
    f.write(tpl.replace("__DATA__", payload))
if "--standalone" in sys.argv:
    # the artifact host wraps the page in a document skeleton; opening the file on its own needs the same wrapper (doctype, viewport, zero body margin)
    page = tpl.replace("__DATA__", payload)
    wrapped = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
               '<style>:root{color-scheme:light}body{margin:0;font:14px system-ui,sans-serif}[hidden]{display:none!important}</style></head><body>' + page + '</body></html>')
    with open(P("dist", "summary.standalone.html"), "w", encoding="utf-8") as f:
        f.write(wrapped)
    print("wrote dist/summary.standalone.html (open this one directly in a browser; dist/summary.html is the artifact page)")
print(f"wrote dist/summary.html {os.path.getsize(P('dist', 'summary.html'))} bytes · {len(E)} events · {len(facts)} facts · {len(mismatches)} frozen conflicts · "
      f"bands {'parsed' if bands else 'NOT parsed'} · adjusted base {'parsed' if m_adj else 'NOT parsed'} · rates {len(rates)} · HEAD {head or '?'}")
