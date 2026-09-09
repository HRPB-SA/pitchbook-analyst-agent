# Gate 3 record (orchestrator), 2026-09-09 — HARD VERIFICATION GATE (harrison-execution) plus the six validation gates

Status legend: PASS · PASS-WITH-FIX (defect found and corrected before ship) · PENDING was used while the Model agent's Workbook B and tie-out were outstanding; all rows are now asserted

## A. Report side

| Check | Method | Result |
|---|---|---|
| Blind re-derivation of the ten load-bearing figures | tools/gate3-blind-derivation.md written before any draft; report §14 table and body reconciled against it | PASS: all ten match (F8 restated as adjusted operating income per the addendum, as the derivation's own addendum requires) |
| Derived ratios | Net run-rate 39,162 / 47,450; multiples 24.6x / 20.3x / 21.3x; CE 0.315x / 0.382x / 0.221x; ratio 1.43x / 1.73x; documented-$ 324,100 / 480,400; 2028 priced run 53,355; Google leg 40,000/yr; FY2026E 57,580 / 62,580 / 48,830; H1 16.2-16.3B | PASS: every figure in the text equals the derivation |
| Sensitivity grids recomputed by hand | E17a (relative multiple and CE ratio at 27 / 33 / 39.75% × NET / GROSS), E17b (nine cells per panel), E17c (2030 compute 192.5 / 245 / 297.5; revenue 146.4 / 318.4 / 609.9; cash-flow signs), Bessemer tails (176.3 / 197.8; 231.3 / 266.4; 286.0 / 354.6) | PASS |
| Old-draft figures without a fresh row | tools/gate3_check.py forbidden-pattern scan: 5 hits | PASS: all five are framed as superseded history (Jul-16 reference row 1.65x; retired Nvidia LOI; retired "3x cheaper"; PB Co-CEO artifact; "$190B of relative value" is a false positive on the capex pattern) |
| Frozen conflicts rendered as frozen | All 20 conflict IDs referenced; §14 table carries nine frozen with both branches and switch names, plus the C-14 addendum and the $15B facility rule | PASS |
| Rulings | No PB TTM as current (Exhibit 4 separate block); gross never beside net without the equalization; equity-only CE; no correlation coefficient (scan 0); no breakeven year; "20%" only as the flagged gross-case input; Q2 result always "adjusted", never FCF | PASS |
| Red-team | §13 states the bull case at full strength (six points) and answers each; four dated falsifiers | PASS |
| Style | 0 em/en dashes; banned-word scan 0; body 11,997 words; 14 sections; 18 exhibits as 23 tables | PASS |
| docx | build from the .md via docx npm; validate.py "All validations PASSED"; PDF 57 pages with populated Contents (UNO index update); visual check of pages 3, 6, 28, 45 | PASS |
| Defects found and fixed | (1) §0 and Exhibit 1 note called the $324.1B stack "T1 and T2 rows" although Volta's $10B is T3; (2) §2 "twenty points of multiple" corrected to "twenty percentage points of relative multiple"; (3) MNPI/COI disclosure paragraph added to the §14 provenance box | PASS-WITH-FIX (rebuilt, re-validated, re-rendered) |

## B. MNPI / COI checkpoint (tools/gate3-mnpi-coi.md)

| Check | Result |
|---|---|
| Material non-public inputs | None: every ledger row cites a public or licensed source; leaked-document figures enter only as press reporting at the press tier; nothing from either confidential S-1 | PASS |
| Confidential S-1 contents | Not public (L-001, L-002); nothing used | PASS |
| Positions / interests | Disclosure paragraph added to §14: PitchBook model-portfolio allocation (Anthropic 6% OW / OpenAI 2% UW, Jul-16 register) stated; personal holdings, if any, to be disclosed under PitchBook research policy before external distribution | PASS (author to confirm the personal line before release) |
| Embargo (Ruling 2) | Report and Workbook A XML scanned: no correlation coefficient, no "-0.99" | PASS |
| Copyright | Quotations are short filing or article fragments; ledger sentences ≤40 words | PASS |

## C. Workbook side

| Check | Method | Result |
|---|---|---|
| Workbook A build | build_a.py: 2,462 formulas, 30 named ranges, 14 tabs | PASS |
| Recalculation | recalc.py (LibreOffice): status success, total_errors 0; requote.py restored quoted sheet names; verify.py: 0 cached errors; typed constants outside 00/01 are the 13 switch selectors only; literals in formulas only 0/1/2; XML scans clean | PASS |
| Spec §9 reproduction | dump_checks.py: every listed check PASS at Base defaults; live cells: FY2026E 57,580 / 62,580 / 48,830; OpenAI 32,400 / 38,119; documented-$ 324,100 / 358,600 / 524,100 / 480,400 / 690,000; 2028 gap −25,355 to −27,655; 2027 gap −21,930; envelope 65,700 / 68,000; CE 0.3152 / 0.2207 / 1.428x; multiples 24.64x / 21.3x; $/pt 118.4 / 174.9; spread 1.478x; Anthropic 2029-2030 231,276 / 266,446 | PASS: matches the report |
| Colour discipline | 2,462 formulas black, 0 blue; 675 numeric inputs blue, 0 not blue | PASS |
| Named ranges | all 14 switches present; LB_01-LB_10 present (renamed from LB01-LB10, which Excel reads as cell references; tie-out §2.11; report §14 header updated) with cached values matching the derivation (LB01 65,000; LB02 40,000; LB03 124,254; LB04 181,216.5; LB08 24,100) | PASS |
| Switch and scenario sweep | build/sweep_a.py: every scenario and switch state recalculated by LibreOffice on a temp copy (tie-out §7 and Appendix B); formulas-library cross-check 0 mismatches on both files (Appendix A); orchestrator re-run of tools/gate3_model_check.py: A 2,462 formulas / 0 errors, B 1,793 / 0 errors, XML embargo and dash scans 0, colour discipline A 2,462 black / 675 blue and B 1,793 black / 558 blue | PASS |
| Workbook B (greenfield) | build_b.py: 10 tabs; check cells G20 / 1 GW / power / crossover PASS; reference-class checks PASS for all three scenarios; VI cumulative to first frontier model 56,811 and to first $1B 81,229 fall outside the Analyst's pre-model bands (25,000-40,000; 40,000-60,000) because the spec's own line items sum above the band once phased by year (tie-out §2.8). Resolution: the report prints the workbook figures and states the superseded bands (Exhibit 18b, §12 verdict). Milestone rule and Lean training cap are AJ, flagged (tie-out §2.9-2.10). Riot start default 2027-01-01 stated as an assumption in §5 with the 2028 sensitivity (tie-out §2.1); AIBQ 8.135 printed as 8.13 with the unrounded value (tie-out §2.2) | PASS-WITH-FIX |
| tie-out.md (every exhibit ↔ range with values) | tie-out §3 maps E1-E18 to ranges with Base values; orchestrator re-run of tools/gate3_check.py with the tie-out present: 836 figures extracted, 95 not found by literal string; a tolerant re-match (units normalized, 0.6% tolerance) against tie-out, ledger, model-spec and the blind derivation leaves 3, all derived and traceable: 43,550 (65,000 net of the 33% grid midpoint), 33.4M (L-149's 33,445,026 warrant shares rounded), 31,500 (Exhibit 3's 2030 priced run from the Exhibit 6 terms) | PASS |

Gate 3 verdict: PASS. Report side PASS with three fixes; workbook side PASS with the Workbook B reconciliation applied to the report text (six edits: Exhibit 18b VI cells, §12 verdict sentence, §14 named-range header, §11 unrounded composite, §5 Riot start assumption). docx rebuilt and validated; PDF re-rendered (57 pages, contents populated); gate3_check.py re-run clean on dashes, rulings, conflicts and forbidden patterns.
