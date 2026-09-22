#!/usr/bin/env python3
"""Wave 6 reconciliation + Wave 7 report for a DTF attribution run.

Usage: python3 scripts/compile_report.py runs/<run_id>

Stage G reconciliation: per pair, merges verified_raw.json (deterministic raw
check) with stageG_retry_results.json (WebFetch retry for pages curl could not
open) into verified.json. A Strong/Promising verdict with no citation "found"
is downgraded to Weak and flagged. Orchestrator notes come from
orchestrator_notes.json ({pair_id: note}).

Writes results.csv, ledger.csv, report.md, and prints the done-gate checks.
"""
import csv
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

GRADE_ORDER = {"Strong": 0, "Promising": 1, "Weak": 2, "Likely Incorrect": 3}
PCT_CONF = re.compile(r"\d+(\.\d+)?\s*%\s*(confiden|likel|probab|chance|certain)", re.I)


def load(p, default=None):
    p = Path(p)
    return json.loads(p.read_text()) if p.exists() else default


def domain(u):
    return urlparse(u).netloc.replace("www.", "") if u.startswith("http") else u.split("(")[0].strip()


def is_public(u):
    return u.startswith("http") and "pitchbook.com" not in u


def base_grade(g):
    g = (g or "").replace("(pending Stage G)", "").strip()
    for k in GRADE_ORDER:
        if g.startswith(k):
            return k
    return g


def md(s):
    return str(s if s is not None else "").replace("|", "\\|").replace("\n", " ")


def reconcile(run, pid, retry):
    pd = run / "pairs" / pid
    raw = load(pd / "verified_raw.json", {"citations": []})
    cites = []
    for c in raw["citations"]:
        c = dict(c)
        c["method"] = "raw-html"
        if c["status"] != "found":
            r = next((r for r in retry if r["pair_id"] == pid and r["url"] == c["url"]), None)
            if r and c["status"] == "could not open":
                c["status"], c["method"], c["note"] = r["status"], "webfetch-retry", r.get("note", "")
        if not is_public(c["url"]):
            c["status"], c["note"] = "not public", "PitchBook/MCP data pull - internal, not re-openable"
        c["tag"] = "" if c["status"] == "found" else "[VERIFY]"
        cites.append(c)
    counts = {s: sum(c["status"] == s for c in cites) for s in ("found", "not found", "could not open", "not public")}
    out = {"pair_id": pid, "citations": cites, "counts": counts}
    (pd / "verified.json").write_text(json.dumps(out, indent=2))
    return out


def main():
    run = Path(sys.argv[1])
    pairs = [json.loads(l) for l in (run / "pairs.jsonl").read_text().splitlines() if l.strip()]
    retry = load(run / "stageG_retry_results.json", [])
    notes = load(run / "orchestrator_notes.json", {})
    rows, ledger, sections, abandoned = [], [], [], []

    for p in pairs:
        pid = p["pair_id"]
        pd = run / "pairs" / pid
        files = ["universe.json", "patterns.json", "evidence.json", "redteam.json", "verdict.json"]
        if not p.get("full_engine") or not all((pd / f).exists() for f in files):
            abandoned.append((p, p.get("not_attempted_reason") or "stage files incomplete: " +
                              ", ".join(f for f in files if not (pd / f).exists())))
            continue
        u, ev, rt, v = (load(pd / f) for f in ("universe.json", "evidence.json", "redteam.json", "verdict.json"))
        ver = reconcile(run, pid, retry)
        grade = base_grade(v["grade"])
        recomputed = ""
        found_public = [c for c in ver["citations"] if c["status"] == "found"]
        if grade in ("Strong", "Promising") and not found_public:
            recomputed = f"{grade} -> Weak (no load-bearing citation verified in Stage G)"
            grade = "Weak"
        status_by = {(c["url"], c["quote"]): c for c in ver["citations"]}
        ev_cells = []
        for e in v.get("evidence", []):
            c = status_by.get((e.get("url"), e.get("quote")), {})
            tag = c.get("tag", "[VERIFY]")
            ev_cells.append(f"{e.get('url')} ({e.get('tier')}{' ' + tag if tag else ''})")
        competitor = rt.get("competitors", [{}])
        best = next((c for c in competitor if c.get("viable")), competitor[0] if competitor else {})
        exact = v["exact_fund"] if v.get("exact_fund_defensible") else "family only"
        rows.append({
            "Investor": u["investor"], "Company": u.get("company", p["company"]), "Date": u["deal_date"],
            "Lead Partner": u.get("lead_partner") or "unknown",
            "Predicted Fund/Family": v["family"], "Exact Fund if defensible": exact,
            "Key Signals": " ; ".join(v.get("key_signals", [])),
            "Competing Fund": v.get("runner_up") or best.get("family", ""),
            "Evidence/URLs": " ; ".join(ev_cells),
            "Confidence": grade + (" [orchestrator note]" if pid in notes else ""),
            "Rationale": v.get("rationale", ""), "What would change this": v.get("would_change", ""),
            "First investment?": v.get("first_investment") or ("Y" if u.get("is_first_investment") else "N"),
            "Eligible families (n)": v.get("eligible_families_n", len(u.get("eligible_families", []))),
            "DTF top candidate": v.get("dtf_top_candidate", "not supplied"),
            "MG hypothesis result": v.get("mg_result", "not supplied"),
            "_pid": pid, "_recomputed": recomputed,
        })
        # ledger: one line per load-bearing claim (each verdict citation)
        hits = ev.get("hits", []) + [e for c in rt.get("competitors", []) for e in c.get("evidence", [])]
        for e in v.get("evidence", []):
            claim = next((h.get("claim") for h in hits if h.get("url") == e.get("url") and h.get("claim")), "") \
                or e.get("claim", "") or e.get("quote", "")[:120]
            same = [h for h in ev.get("hits", []) if h.get("claim") == claim and domain(h.get("url", "")) != domain(e.get("url", ""))]
            c = status_by.get((e.get("url"), e.get("quote")), {})
            ledger.append({"pair_id": pid, "claim": claim, "source_url": e.get("url"), "tier": e.get("tier"),
                           "cross_check": "yes" if same else "single-source",
                           "confidence_tag": c.get("status", "unverified") + (" " + c.get("tag", "") if c.get("tag") else ""),
                           "red_team_note": best.get("why", "")[:300]})
        # section
        s = [f"### {u['investor']} → {u.get('company', p['company'])} ({u['deal_date']})",
             f"**Verdict: {grade}** — family **{v['family']}**; exact fund: {exact}; runner-up: {v.get('runner_up')}"
             + (f"  \n**Grade recomputed:** {recomputed}" if recomputed else "")
             + (f"  \n**Orchestrator note:** {notes[pid]}" if pid in notes else ""),
             "", f"First investment: {v.get('first_investment')} · Investor led: {u.get('investor_led')} · "
             f"Deal size (USD): {u.get('deal_size_usd')} · Flags: {', '.join(map(str, u.get('flags', []))) or 'none'}",
             "", "**Universe (all vehicles considered)**", "",
             "| Fund | Family | Type | First close | Existence | Inv. period | Reserve | Strategy | Size | Status | Reason |",
             "|---|---|---|---|---|---|---|---|---|---|---|"]
        for f in u["funds"]:
            g = f.get("gates", {})
            s.append("| " + " | ".join(md(x) for x in (f.get("fund_name"), f.get("family"), f.get("fund_type"),
                     f.get("first_close_date"), g.get("existence"), g.get("investment_period"), g.get("reserve"),
                     g.get("strategy"), g.get("size"), f.get("status_for_this_deal"), (f.get("reason") or "")[:220])) + " |")
        s += ["", "**Evidence cited in verdict**", "", "| Tier | URL | Quote | Verified |", "|---|---|---|---|"]
        for e in v.get("evidence", []):
            c = status_by.get((e.get("url"), e.get("quote")), {})
            s.append(f"| {md(e.get('tier'))} | {md(e.get('url'))} | {md(e.get('quote'))[:300]} | "
                     f"{md(c.get('status', 'unverified'))} ({md(c.get('method', ''))}) |")
        s += ["", "**Competing-fund analysis (red team)**", ""]
        for c in rt.get("competitors", []):
            s.append(f"- *{md(c.get('family'))}* ({md(c.get('type'))}) — viable: {c.get('viable')}. {md(c.get('why'))[:600]}")
        if v.get("disputed"):
            s += ["", "**[DISPUTED]**", ""] + [f"- {md(d if isinstance(d, str) else json.dumps(d))[:500]}" for d in v["disputed"]]
        s += ["", f"**What would change this:** {md(v.get('would_change'))}", "",
              f"<details><summary>Rationale</summary>\n\n{v.get('rationale', '')}\n\n</details>", ""]
        sections.append((GRADE_ORDER.get(grade, 9), s))

    rows.sort(key=lambda r: GRADE_ORDER.get(r["Confidence"].split(" [")[0], 9))
    cols = ["Investor", "Company", "Date", "Lead Partner", "Predicted Fund/Family", "Exact Fund if defensible",
            "Key Signals", "Competing Fund", "Evidence/URLs", "Confidence", "Rationale", "What would change this",
            "First investment?", "Eligible families (n)", "DTF top candidate", "MG hypothesis result"]
    with (run / "results.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    with (run / "ledger.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["pair_id", "claim", "source_url", "tier", "cross_check", "confidence_tag", "red_team_note"])
        w.writeheader()
        w.writerows(ledger)

    head = (run / "report_head.md").read_text() if (run / "report_head.md").exists() else ""
    tail = (run / "report_tail.md").read_text() if (run / "report_tail.md").exists() else ""
    L = [head, "## Results", "", "| Grade | Investor | Company | Date | Family | Exact fund | Runner-up | 1st inv. |",
         "|---|---|---|---|---|---|---|---|"]
    for r in rows:
        L.append("| " + " | ".join(md(r[k]) for k in ("Confidence", "Investor", "Company", "Date", "Predicted Fund/Family",
                                                      "Exact Fund if defensible", "Competing Fund", "First investment?")) + " |")
    L += ["", "## Per-pair detail", ""]
    for _, s in sorted(sections, key=lambda x: x[0]):
        L += s
    L += ["## Appendix A — pairs not run through the full engine", ""]
    for p, why in abandoned:
        L.append(f"- **{p['investor']} → {p['company']}** ({p.get('announce_date')}): {why}")
    L += ["", tail]
    (run / "report.md").write_text("\n".join(L))

    # done-gate
    ok = lambda b: "PASS" if b else "FAIL"
    full = [p for p in pairs if p.get("full_engine")]
    g1 = all(all((run / "pairs" / p["pair_id"] / f).exists() for f in
                 ("universe.json", "patterns.json", "evidence.json", "redteam.json", "verdict.json", "verified.json"))
             for p in full) and len(abandoned) == len(pairs) - len(full)
    g2 = all(any(c["status"] == "found" for c in load(run / "pairs" / r["_pid"] / "verified.json")["citations"])
             for r in rows if r["Confidence"].startswith(("Strong", "Promising")))
    g3 = all(r["What would change this"] for r in rows)
    g4 = all(f.get("status_for_this_deal") in ("eligible", "demoted", "eliminated") and f.get("reason") is not None
             for p in full for f in load(run / "pairs" / p["pair_id"] / "universe.json")["funds"])
    g5 = all(load(run / "pairs" / p["pair_id"] / "redteam.json").get("mg_hypothesis") is not None and
             load(run / "pairs" / p["pair_id"] / "redteam.json").get("dtf_top_candidate") is not None for p in full)
    txt = (run / "report.md").read_text() + (run / "results.csv").read_text()
    g6 = not PCT_CONF.search(txt)
    g7 = all(("[VERIFY]" in cell) or cell.split(" (")[0] in {c["url"] for c in load(run / "pairs" / r["_pid"] / "verified.json")["citations"] if c["status"] == "found"}
             for r in rows for cell in r["Evidence/URLs"].split(" ; ") if cell)
    g8 = len(ledger) >= sum(1 for _ in ledger) and len(ledger) > 0
    for name, g in [("all stage files or logged abandonment", g1), ("Strong/Promising cite >=1 found URL", g2),
                    ("every verdict has would-change", g3), ("every universe fund has status+reason", g4),
                    ("red-team MG/DTF result present", g5), ("no confidence percentages", g6),
                    ("no unverified URL without [VERIFY]", g7), ("ledger has claims", g8)]:
        print(f"{ok(g)}  {name}")
    for r in rows:
        if r["_recomputed"]:
            print("RECOMPUTED:", r["_pid"], r["_recomputed"])


if __name__ == "__main__":
    main()
