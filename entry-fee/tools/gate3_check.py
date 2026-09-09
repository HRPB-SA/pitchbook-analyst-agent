#!/usr/bin/env python3
# CONTEXT: $100B ENTRY FEE v5 — Gate 3 mechanical checks.
# (1) Every numeric figure in report/entry-fee-v5.md must appear in model/tie-out.md OR in the ledger
#     (as a value) — reports the misses for human review.
# (2) Old-draft figures that must not survive without a fresh row (from gate3-blind-derivation.md).
# (3) Frozen conflicts named in conflicts.md must be mentioned in the report (by figure), unless resolved.
# (4) Banned vocabulary / em-dash scan on the report text.
import re, sys, pathlib

BASE = pathlib.Path("/home/user/pitchbook-analyst-agent/entry-fee")
rep = (BASE / "report/entry-fee-v5.md").read_text(encoding="utf-8")
tie = (BASE / "model/tie-out.md").read_text(encoding="utf-8") if (BASE / "model/tie-out.md").exists() else ""
led = (BASE / "research/evidence-ledger.md").read_text(encoding="utf-8")
conf = (BASE / "research/conflicts.md").read_text(encoding="utf-8")

def norm(s):
    return s.replace(",", "").replace("~", "").replace("$", "").strip()

# --- (1) figure extraction ---
num_re = re.compile(r"(?<![\w.])(\$?\s?\d{1,3}(?:,\d{3})+(?:\.\d+)?|\$?\s?\d+(?:\.\d+)?)\s?(B|M|T|bn|mn|x|%|GW|MW|kW|MTok|/sh)?(?![\w])")
figs = set()
for m in num_re.finditer(rep):
    v, u = m.group(1), m.group(2) or ""
    v = norm(v)
    try:
        f = float(v)
    except ValueError:
        continue
    # skip years, small counts, section numbers, exhibit numbers
    if u == "" and (1900 <= f <= 2100 or f < 30):
        continue
    figs.add((v, u))

tie_n = norm(tie); led_n = norm(led)
miss = []
for v, u in sorted(figs, key=lambda t: (t[1], float(t[0]))):
    key = v
    if key not in tie_n and key not in led_n:
        miss.append(f"{v}{u}")
print(f"figures extracted from report: {len(figs)} · not found in tie-out OR ledger: {len(miss)}")
print("  ", ", ".join(miss[:200]))

# --- (2) must-not-survive list ---
forbidden = [
    (r"\$161\.3\s?B|\$161\.25\s?B|\$161,254", "Anthropic total raised $161.3B (superseded C-01)"),
    (r"34\.1x[^.\n]{0,40}(identical|both|same)", "'both at 34.1x' framing (dead on fresh prints)"),
    (r"1\.65x", "1.65x CE advantage (superseded)"),
    (r"\$100\s?B[^.\n]{0,30}(Nvidia|10\s?GW)|Nvidia[^.\n]{0,40}\$100\s?B", "Nvidia $100B LOI (retired, C-20)"),
    (r"3x cheaper", "Fast Mode 3x cheaper (reversed, C-07)"),
    (r"Co-Chief Executive|co-CEO", "Altman Co-CEO (PB artifact, resolved)"),
    (r"\$190\s?B", "OpenAI capex $190B 2026E (mis-tagged, L-124)"),
    (r"Superpriority|1st Lien|2nd Lien", "chip-bond tranche language (SPV debt, C-01)"),
]
print("\nforbidden-figure scan:")
bad = 0
for pat, label in forbidden:
    hits = [m.start() for m in re.finditer(pat, rep, flags=re.I)]
    if hits:
        bad += 1
        ctx = rep[max(0, hits[0]-80): hits[0]+120].replace("\n", " ")
        print(f"  HIT {label}: ...{ctx}...")
print("  none" if not bad else f"  {bad} pattern(s) hit — verify each is framed as history/superseded, else FAIL")

# --- (3) frozen conflicts mentioned ---
cids = re.findall(r"^\| (C-\d\d) \| ([^|]+) \|", conf, flags=re.M)
print("\nfrozen conflicts referenced in report (by ID or figure keyword):")
for cid, fig in cids:
    kw = fig.split("(")[0].strip()[:28]
    present = (cid in rep) or (kw.lower()[:18] in rep.lower())
    print(f"  {cid} {'ok ' if present else 'MISSING'} — {fig.strip()[:70]}")

# --- (4) style scan ---
banned = ["it's worth noting", "importantly", "going forward", "unlock", "dive into", "delve", "in conclusion", "at the end of the day", "synergy", "leverage "]
print("\nstyle scan:")
print("  em-dashes:", rep.count("—"), "· en-dashes:", rep.count("–"))
for b in banned:
    c = rep.lower().count(b)
    if c:
        print(f"  banned '{b}': {c}")
words = len(re.findall(r"\b\w+\b", rep))
print(f"  word count: {words}")
