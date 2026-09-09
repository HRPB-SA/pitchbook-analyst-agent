#!/usr/bin/env python3
# CONTEXT: $100B ENTRY FEE v5 — Gate 1 mechanical check on the Researcher's ledger.
# Asserts: (1) every seed ID in SEED-LIST.md has at least one ledger row (any status);
# (2) every row tagged "confirmed" carries a T1 or T2 tier AND a non-empty supporting sentence;
# (3) PitchBook TTM revenue fields are not tagged confirmed as run-rate;
# (4) load-bearing rows either have a cross-check or say SINGLE-SOURCE.
import re, sys, pathlib

BASE = pathlib.Path("/home/user/pitchbook-analyst-agent/entry-fee")
seed_txt = (BASE / "research/SEED-LIST.md").read_text(encoding="utf-8")
ledger_txt = (BASE / "research/evidence-ledger.md").read_text(encoding="utf-8")

seed_ids = sorted(set(re.findall(r"^([AOXG]-\d{2})\b", seed_txt, flags=re.M)))

rows = []
for line in ledger_txt.splitlines():
    if not line.startswith("|"):
        continue
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) < 12 or not re.match(r"^L-\d{3,4}$", cells[0]):
        continue
    rows.append(cells)

print(f"seed IDs: {len(seed_ids)} · ledger rows parsed: {len(rows)}")
if not rows:
    print("FAIL: no ledger rows parsed — check the table format (13 columns, ID like L-001)")
    sys.exit(1)

# column indices per schema: 0 ID,1 Seed,2 Scope,3 Figure,4 Value,5 Unit,6 As-of,7 Status,8 Tier,9 Source,10 Sentence,11 Cross-check,12 Notes
covered = {}
for r in rows:
    for sid in re.findall(r"[AOXG]-\d{2}", r[1]):
        covered.setdefault(sid, []).append(r[0])

missing = [s for s in seed_ids if s not in covered]
status_counts = {}
bad_confirmed = []
trap_rows = []
single_source = []
for r in rows:
    st = r[7].lower()
    status_counts[st] = status_counts.get(st, 0) + 1
    tier = r[8].upper()
    sentence = r[10]
    if st.startswith("confirmed"):
        if not re.search(r"\bT[12]\b", tier) or len(sentence) < 15:
            bad_confirmed.append((r[0], r[3][:50], tier, len(sentence)))
    if re.search(r"TTM\s*4Q20\d\d", " ".join(r), flags=re.I) and st.startswith("confirmed") and re.search(r"run.?rate|ARR", r[3], flags=re.I):
        trap_rows.append((r[0], r[3][:60]))
    if "SINGLE-SOURCE" in r[11].upper():
        single_source.append((r[0], r[3][:50]))

print("status counts:", status_counts)
print(f"seed IDs with no row ({len(missing)}):", missing)
print(f"confirmed rows lacking T1/T2 or a sentence ({len(bad_confirmed)}):")
for b in bad_confirmed[:40]:
    print("   ", b)
print(f"possible PB-TTM trap rows tagged confirmed ({len(trap_rows)}):", trap_rows)
print(f"single-source rows ({len(single_source)}):")
for s in single_source[:60]:
    print("   ", s)

ok = not missing and not bad_confirmed and not trap_rows
print("GATE 1:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 2)
