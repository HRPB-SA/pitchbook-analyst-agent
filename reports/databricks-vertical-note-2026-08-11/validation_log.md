# Validation log: Q3 2026 Databricks Vertical Analyst Note

Author: Harrison Rolfes. Run date: August 11, 2026 (data as of August 10 pull).
Method: live PitchBook profile + financing note (59199-40) and PitchBook news
sweep cross-checked against company announcement coverage; canonical store
merge under freeze-on-conflict; derived figures recomputed by the engine at
build time. Register: Hemingway-analyst per STYLE.md; estimative language per
the ICD 203 adoption (lexicon box printed in the note).

## Ledger (load-bearing claims)

| Claim | Value | Sources | Tier | Cross-check | Confidence |
|---|---|---|---|---|---|
| Term sheet signed, Coatue lead | $188B post, Jul 17 | Company announcement; PB financing note Aug 7 (deal 334745-56T, Announced/In Progress) | T2 | Reuters syndication + TechCrunch + WSJ-via-CNA, all Jul 16-17 | High |
| Round size | ~$3B | Press reports (WSJ-sourced) | T3 | Multiple outlets trace to WSJ = ONE ultimate source; flagged est. | Moderate |
| Close timing | "later this summer" (company) | Company announcement | T2 | PB note Aug 7 consistent | High |
| Completed mark | $134B, Feb 9 | Company PR + PB deal 313367-68T | T2 | Held from July pack; PB re-verified Aug 10 | High |
| Run-rate | $6.9B, +80% YoY, Jun 16 | Company disclosure (analyst session) | T2 | Ladder re-verified from four dated prints | High |
| Gross margin | 74%, guided lower | Company disclosure Jun 16 | T2 | July pack confirmed | High |
| Multiples 19.4x / 27.2x | derived | $134B and $188B over $6.9B | Derived | Engine-computed at build | High |
| Growth-adjusted 0.34x vs 0.49x | derived | Comparable 8-K May 27 guide (+31%, 15.3x) | T1/Derived | July initiation figures re-checked | High |
| Per-point $15.2B / ~$21.3B / $118B / $188B / ~$279B | derived | Internal AIBQ marks + PB-confirmed peer marks | T2/Derived/est. | Engine-computed; xAI flagged est. | Moderate (xAI leg) |
| Headcount 9,000 | Jun 9 | PitchBook | T2 | Re-pulled Aug 10, unchanged | High |
| No S-1 on file | Jul 10 check | SEC EDGAR CIK 0001587468 | T1 | Stale 32d at publication; flagged in text ("at the last check") | High for the dated claim |

## Estimative judgments (calibration log)

| Judgment | Band | Date logged | Resolves | Criterion |
|---|---|---|---|---|
| Coatue round completes by October 31, 2026 | Very likely (80-95%) | 2026-08-11 | 2026-10-31 | PB deal 334745-56T status Completed, or company confirmation of funds received |

Confidence stated separately in the note: moderate; size and terms are
press-sourced (single ultimate source) and undisclosed by the company.

## Conflicts, staleness, embargo

- No frozen conflicts touched by this note.
- February-vintage operating metrics (FCF, NRR, org count) past QUARTERLY
  decay: cited with visible dates only; refresh expected Sep-Oct window.
- Embargo check: the quality-valuation coefficient appears nowhere; the
  per-point ranked bar is the only expression used. Chart factory scatter
  guard active.
- Em-dash count: 0 (budget 8).

## QA and copy-edit audit

- Build scanner: 0 FAIL / 0 WARN on the final build.
- Content-qa audit (stage 7, August 11): 7 findings, all fixed before ship.
  (1) "the step looks measured against the cohort" was ambiguous (measured =
  restrained vs. compared); rewritten "restrained by cohort standards".
  (2) "an engine that has run faster each time it has reported": engines do
  not report; rewritten "has grown faster with every report". (3)(4) Two
  comma-before-"because" constructions after positive main clauses; commas
  removed. (5) "until it prints": pronoun with a slippery antecedent;
  rewritten "until then". (6) "sits on the cohort floor by a factor of five"
  mixed the metaphor and the arithmetic; rewritten "prices at least five
  times below its nearest peer". (7) The close judgment and confidence
  sentence repeated near-verbatim (18 words) between takeaway 4 and the
  final section; the body's confidence sentence rewritten to vary.

## ENTER screen (the call)

- Expectational: yes; the note prices a pending close and sets the Sep-Oct print as the decider.
- Novel: yes; do-not-adopt discipline against the announced mark plus the two-price framing is not in circulating coverage.
- Thorough: tracker-verified store, four-print ladder, dual-mark math.
- Examinable: every figure re-derivable from the ledger above and the store.
- Revealing: kill criterion in the text (margin < 70% by the October disclosure forces a re-score); close-fails branch covered by the do-not-adopt anchor.

## Report Ship gate

- [x] Validation ledger complete (every load-bearing claim above)
- [x] Adversarial pass: the margin bear case is argued in the note at full strength; the close-fails branch is the standing anchor
- [x] No VERIFY/DISPUTED figure ships unflagged; stale metrics carry dates
- [x] Copyright-safe; zero TODOs; punchline-first; forward hooks dated
- [x] Verdict takes a position; falsifier named with date and criterion
- [x] ENTER passed (above); probability judgment logged for calibration
- [x] Template obligations met (metadata sheet full; lead bullets carry metrics; captions <= 30 words; lexicon box printed; references numbered)
