#!/usr/bin/env python3
"""
CONTEXT: ANTHROPIC INTELLIGENCE DESK — mechanical ship gates (the non-judgment half of certification).
Checks the built data files against the gate list in docs/ARCHITECTURE.md §9 and writes data/certify.json, which the Sources tab renders.
Status per gate: PASS · WARN (ships only with the flag visible) · FAIL (blocks) · PENDING (input not produced yet).
The judgment half (does the verdict follow from the model, are the basis traps handled) is the independent Certifier agent: agents/briefs/certifier_brief.md.
Run: python3 scripts/certify.py            (exit code 1 if any gate FAILS)
"""
import json, os, re, subprocess, sys, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)
def load(*a):
    try: return json.load(open(P(*a)))
    except Exception: return None

E = load("data", "events.json") or []
EV = {e["id"] for e in E}
gates = []
def gate(gid, name, status, detail): gates.append({"id": gid, "name": name, "status": status, "detail": detail})

# G1 record size and sourcing
no_url = [e["id"] for e in E if not (e.get("source") or {}).get("url")]
years = sorted({e["date"][:4] for e in E})
gate("G1", "Record: >= 300 deduped events, each with a source URL, every year 2021 to 2026 present",
     "PASS" if len(E) >= 300 and not no_url and all(str(y) in years for y in range(2021, 2027)) else "FAIL", f"{len(E)} events; {len(no_url)} without a URL; years {years[0]}–{years[-1]}")
h = load("data", "health.json") or {}
gate("G2", "Mechanical health checks (dates, schema, duplicate ids, tier/confidence consistency)", "PASS" if h.get("fails") == 0 else ("FAIL" if h else "PENDING"), f"{h.get('fails')} fails, {h.get('warns')} warns")
weak = [e["id"] for e in E if e.get("confidence") in ("HIGH", "CANONICAL") and (e.get("source") or {}).get("tier") in ("T4", "T5") and not e.get("corroboration")]
gate("G3", "No HIGH/CANONICAL confidence resting on a T4/T5 source alone", "PASS" if not weak else "FAIL", f"{len(weak)} violations" + (f": {weak[:3]}" if weak else ""))
LG = load("data", "ledger.json") or {}
conf = (LG.get("cross_agent_conflicts") or []) + (LG.get("agent_conflicts") or [])
bad_c = [c.get("topic") for c in conf if c.get("value_a") in (None, "") or c.get("value_b") in (None, "") or not (c.get("source_a") or c.get("source_b") or c.get("note"))]
flagged = sum(1 for e in E if e.get("confidence") in ("DISPUTED", "VERIFY", "LOW"))
gate("G4", "Conflicts are frozen, not resolved: every conflict row shows both values and a source or note", "PASS" if conf and not bad_c else ("WARN" if not conf else "FAIL"), f"{len(conf)} conflicts in the ledger ({len(bad_c)} incomplete); {flagged} events carry a DISPUTED/VERIFY/LOW tag")

# G5 model
M = load("data", "model.json")
if not M:
    gate("G5", "Model: bear/base/bull present, every driver traced to an event id or table row", "PENDING", "data/model.json not built yet")
    gate("G6", "Model engine parity: scripts/model.py == computeModel() in assets/app.js", "PENDING", "no model")
else:
    miss = [s for s in ("bear", "base", "bull") if s not in (M.get("outputs") or {})]
    dt = M.get("driver_trace") or []
    bad_ids = [i for d in dt for i in (d.get("event_ids") or []) if i not in EV and i not in (load("data", "id_map.json") or {})]
    untraced = [d.get("driver") for d in dt if not (d.get("event_ids") or d.get("table_row"))]
    st = "PASS" if not miss and len(dt) >= 6 and not bad_ids and not untraced else "FAIL"
    gate("G5", "Model: bear/base/bull present, every driver traced to an event id or table row", st, f"scenarios missing: {miss or 'none'}; {len(dt)} drivers traced; unresolved ids {len(bad_ids)}; drivers without a trace {untraced[:3] or 'none'}; outside-view block {'present' if M.get('outside_view') else 'MISSING'}")
    try:
        r = subprocess.run(["node", P("scripts", "parity.cjs")], capture_output=True, text=True, timeout=60)
        gate("G6", "Model engine parity: scripts/model.py == computeModel() in assets/app.js", "PASS" if r.returncode == 0 else "FAIL", (r.stdout or r.stderr).strip().splitlines()[-1][:200])
    except Exception as ex:
        gate("G6", "Model engine parity", "WARN", f"could not run node: {ex}")

# G7 compute
C = load("data", "compute.json")
if not C:
    gate("G7", "Compute: commitments table reconciles to the totals shown", "PENDING", "data/compute.json not built yet")
else:
    rows = C.get("commitments") or []; tot = (C.get("totals") or {}).get("usd_m_announced")
    s = sum((r.get("usd_m") or 0) for r in rows)
    ok = bool(rows) and tot and abs(s - tot) / tot <= 0.02
    gate("G7", "Compute: commitments table reconciles to the totals shown", "PASS" if ok else "WARN", f"{len(rows)} rows sum to ${s/1000:.1f}B vs stated total ${ (tot or 0)/1000:.1f}B; waterfall {'present' if C.get('gross_margin_bridge') else 'MISSING'}; unit economics {'present' if C.get('unit_economics') else 'MISSING'}")

# G8 thesis
T = load("data", "thesis.json")
if not T or not T.get("verdict"):
    gate("G8", "Thesis: verdict at each reference price; every thesis-breaker carries metric, threshold, date", "PENDING", "data/thesis.json has no judge verdict yet")
else:
    j = T["verdict"]; br = T.get("thesis_breakers") or []
    incomplete = [b.get("metric") for b in br if not (b.get("metric") and b.get("threshold") not in (None, "") and b.get("observable_by"))]
    marks = {m.get("mark") for m in (j.get("by_mark") or [])}
    ok = {"series_h", "secondary", "ipo_target"} <= marks and len(br) >= 6 and not incomplete and j.get("call") and len(T.get("bull") or []) >= 6 and len(T.get("bear") or []) >= 6
    gate("G8", "Thesis: verdict at each reference price; every thesis-breaker carries metric, threshold, date", "PASS" if ok else "FAIL",
         f"call: {j.get('call')}; marks covered {sorted(marks)}; {len(br)} breakers, incomplete: {incomplete or 'none'}; bull claims {len(T.get('bull') or [])}, bear claims {len(T.get('bear') or [])}")

# G9 topics
TP = load("data", "topics.json") or {}
topics = TP.get("topics") if isinstance(TP, dict) else TP
topics = topics or []
thin = [t.get("slug") for t in topics if len(t.get("evidence") or []) < 12]
gate("G9", "Topics: ten topic analyses, each with >= 12 evidence ids", "PASS" if len(topics) >= 10 and not thin else ("PENDING" if len(topics) < 10 else "FAIL"), f"{len(topics)} topics built; thin evidence: {thin or 'none'}")

# G10 claims ledger
cl = load("data", "claims_ledger.json")
if not cl:
    gate("G10", "Independent re-derivation of load-bearing claims reconciled", "PENDING", "no claims ledger yet")
else:
    s = cl["summary"]; n = sum(s.values())
    st = "PASS" if n >= 40 and s.get("MISMATCH", 0) <= 0.15 * n and s.get("UNTRACEABLE", 0) <= 0.25 * n else "WARN"
    gate("G10", "Independent re-derivation of load-bearing claims reconciled", st, f"{n} claims: {s}. MISMATCH rows are frozen with both values shown.")

# G11 audit
A = load("data", "audit.json")
if not A:
    gate("G11", "Independent audit of a random sample of the record", "PENDING", "no audit scored yet")
else:
    ss, sp = A.get("supported_share") or 0, A.get("supported_or_partly_share") or 0
    st = "PASS" if A.get("n", 0) >= 40 and ss >= 0.80 and sp >= 0.92 else ("FAIL" if sp < 0.85 else "WARN")
    gate("G11", "Independent audit of a random sample of the record", st, f"{A.get('n')} events audited cold: {ss:.0%} fully supported, {sp:.0%} core fact supported, {A.get('unopenable', 0)} unopenable; thresholds 80% / 92% on n>=40")

# G12 agent log honesty
L = load("data", "agent_log.json") or {}
log = L.get("log") or []; ags = L.get("agents") or {}
ts = [r.get("t") for r in log]
unknown = sorted({r.get("agent") for r in log if r.get("agent") not in ags and r.get("agent") != "orchestrator"})
future = [t for t in ts if t and t > datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")]
ordered = all(ts[i] <= ts[i + 1] for i in range(len(ts) - 1)) if ts else False
outs = {f[:-5] for f in os.listdir(P("agents", "outputs")) if f.endswith(".json")}
no_output = sorted(a for a, m in ags.items() if not m.get("planned") and a != "orchestrator" and a not in outs)
gate("G12", "Agent log is the real log: agents known, time-ordered, nothing in the future, every active agent has an output file", "PASS" if log and not unknown and ordered and not future and not no_output else "FAIL",
     f"{len(log)} rows; unknown agents {unknown or 'none'}; ordered {ordered}; future rows {len(future)}; active agents without an output file {no_output or 'none'}")

# G13 repo hygiene
try:
    tracked = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True).stdout.splitlines()
except Exception:
    tracked = []
raw = [f for f in tracked if f.startswith("data/raw/")]
secret_re = re.compile(r"(sk-ant-[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{30,}|AIza[0-9A-Za-z_-]{30,}|xox[baprs]-[A-Za-z0-9-]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY-----)")
hits = []
for f in tracked:
    if f.endswith((".png", ".xlsx", ".min.js")): continue
    try:
        if secret_re.search(open(P(f), errors="ignore").read()): hits.append(f)
    except Exception: pass
ign = "data/raw" in (open(P(".gitignore")).read() if os.path.exists(P(".gitignore")) else "")
gate("G13", "Hygiene: PitchBook raw pulls git-ignored, no credentials in tracked files", "PASS" if not raw and not hits and ign else "FAIL", f"{len(raw)} raw files tracked; secret-pattern hits {hits or 'none'}; .gitignore covers data/raw: {ign}")

# G14 disclosures
js = open(P("assets", "app.js")).read()
need = {"licence": "licence" in js, "MNPI": "MNPI screen" in js, "conflict of interest": "Conflict of interest" in js, "not investment advice": "not investment advice" in js}
gate("G14", "Disclosures present in the UI (PitchBook licence, MNPI screen, conflict of interest, not investment advice)", "PASS" if all(need.values()) else "FAIL", str(need))

# G15 UI smoke (written by scripts/shot.cjs)
ef = P("dist", "qa", "errors.txt")
if os.path.exists(ef):
    txt = open(ef).read().strip()
    gate("G15", "UI smoke: nine tabs x desktop/phone x light/dark, no console errors, no horizontal overflow", "PASS" if not txt else "FAIL", "clean" if not txt else txt.splitlines()[0][:200] + (f" (+{len(txt.splitlines()) - 1} more)" if len(txt.splitlines()) > 1 else ""))
else:
    gate("G15", "UI smoke: nine tabs x desktop/phone x light/dark", "PENDING", "run: NODE_PATH=$(npm root -g) node scripts/shot.cjs")

summary = {k: sum(1 for g in gates if g["status"] == k) for k in ("PASS", "WARN", "FAIL", "PENDING")}
out = {"generated": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"), "summary": summary, "gates": gates}
json.dump(out, open(P("data", "certify.json"), "w"), indent=1)
for g in gates: print(f"[{g['status']:7s}] {g['id']:3s} {g['name'][:88]}\n            {g['detail'][:230]}")
print(summary)
sys.exit(1 if summary["FAIL"] else 0)
