# Tie-out: Workbook A (entry-fee-v5.xlsx) and Workbook B (greenfield-entry-cost.xlsx)
Agent 4 (Model), 2026-09-09. Built with openpyxl from `analysis/model-spec.md` (patched per `analysis/ADDENDUM-PATCH.md`). Recalculated with LibreOffice (`recalc.py`), the digit-leading sheet names re-quoted in the saved XML (`build/requote.py`), cross-checked with the `formulas` library, audited for typed constants and embargoed strings. Scripts in `model/build/`. Copies of both workbooks in `/mnt/user-data/outputs/`. Values below are at Base defaults (SW_SCEN = 2; every switch at its spec default; SW_15B_FACILITY = "Does not close"; SW_GOOGLE_VALUE = "reported"). $M unless stated. No em-dashes anywhere in either workbook (XML scan clean).

## 0. Recalculation status

| File | Formulas | Named ranges | recalc.py | Cached-value error cells | Typed numeric constants outside 00/01 | Embargo grep (correl / -0.99 / r=) | Em-dash / en-dash |
|---|---|---|---|---|---|---|---|
| model/entry-fee-v5.xlsx (14 tabs) | 2,462 | 30 (SW_SCEN, SW_HAIRCUT, SW_OAI_BASIS, SW_IPO_OAI, SW_A_FY25, SW_A_FY24_NI, SW_A_2026_LOSS, SW_A_HC, SW_TPU_RATE, SW_GW_2028, SW_TOTAL_RAISED_VIEW, SW_15B_FACILITY, SW_GOOGLE_VALUE, SW_SSI; LB_01-LB_10 plus LB_05a, LB_05b, LB_06a, LB_06b, LB_07a, LB_07b; see section 2 item 11 for why the underscore) | status success, total_errors 0 | 0 | 13 (the 12_Conflicts selectors D5:D17, by design) | absent | absent |
| model/greenfield-entry-cost.xlsx (10 tabs) | 1,793 | 5 (SW_GF, SW_GF_BACKSTOP, SW_GF_REGION, SW_GF_MODELCLASS, SW_SSI) | status success, total_errors 0 | 0 | 0 | absent | absent |

Pipeline per file: `build_a.py` / `build_b.py` -> `recalc.py <file> 180` -> `requote.py <file>` -> `verify.py <file>` -> `dump_checks.py` (A). LibreOffice strips the quotes around sheet names that begin with a digit when it saves; `requote.py` restores `'01_Data'!` in every `<f>` and `<definedName>` without touching cached values (verified: openpyxl reloads formulas and values; the `formulas` library evaluates the file).

Formulas-library cross-check: see section 6 (`build/xcheck_formulas.json`).

## 1. Spec section 9 check table (Workbook A; 08_Output rows 45-140, linked PASS/FAIL cells; expected values typed once on 00_Assumptions rows 132-228)

97 check lines, 97 PASS, 0 FAIL at Base defaults (08_Output D141 "Count of FAIL cells" = 0). Table:

| Check | Expected | Computed | Where | Result |
|---|---|---|---|---|
| Identity LB03 + 2,500 = PB Total Raised (L-006) | 126,754 | 126,754 | 05_Cash_Fund D17 | PASS |
| Identity LB04 + 5,220 = PB Total Raised (L-021) | 186,436.5 | 186,436.5 | 05_Cash_Fund J17 | PASS |
| Anthropic net run-rate at 39.75% | 39,162 | 39,162.5 | 02_Revenue D38 | PASS |
| Multiples: Anthropic gross (display) / 39.75% / 27% | 14.8x / 24.6x / 20.3x | 14.85x / 24.64x / 20.34x | 06_Valuation D7 / D9 / D10 | PASS |
| OpenAI multiple NET / gross case | 21.3x / 26.6x | 21.30x / 26.63x | 06_Valuation D12 / D13 | PASS |
| CE Anthropic 39.75% / 27% / gross (forbidden, display) | 0.315 / 0.382 / 0.523 | 0.3152 / 0.3819 / 0.5231 | 05_Cash_Fund E44 / E45 / E46 | PASS |
| CE OpenAI | 0.221 | 0.2207 | 05_Cash_Fund G44 | PASS |
| CE ratio 39.75% / 27% / gross | 1.43x / 1.73x / 2.37x | 1.428 / 1.730 / 2.370 | 05_Cash_Fund H44 / H45 / H46 | PASS |
| FY2026E Anthropic at YE 100,000 / 120,000 / flat | 57,580 / 62,580 / 48,830 | 57,580 / 62,580 / 48,830 | 02_Revenue M55 / M56 / M57 | PASS |
| H1-2026 Anthropic; Q2/Q1 | 16,330; 2.45x | 16,330; 2.452x | 02_Revenue L54; E20 | PASS |
| FY2026E OpenAI at 0 / 10 / 20% | 32,400 / 38,119 / 45,500 | 32,400 / 38,118.7 / 45,499.7 | 02_Revenue M65 / M66 / M67 | PASS |
| Documented-$ Anthropic excl. / incl. SPV | 324,100 / 358,600 | 324,100 / 358,600 | 09_Obligations B18 / B19 | PASS |
| Reported-$ incl. Google leg [VERIFY] | 524,100 | 524,100 | 09_Obligations B20 (yellow) | PASS |
| Documented-$ OpenAI / recalled-$ | 480,400 / 690,000 | 480,400 / 690,000 | 09_Obligations B38 / B39 | PASS |
| Tallies: Bloomberg / stepmark / TechCrunch | 175,000 / 99,100 / 61,250 | 175,000 / 99,100 / 61,250 | 09_Obligations B46 / B48 / B47 | PASS |
| Cancellable Anthropic (approx. 48,000) | 48,000 (tol 500) | 48,250 | 09_Obligations E18 | PASS |
| Anthropic priced run 2026 / 2027 / 2028 / 2029 / 2030 | 28,158 / 47,730 / 53,355 / 44,605 / 38,355 | 28,158.3 / 47,730 / 53,355 / 44,605 / 38,355 | 09_Obligations G64:K64 | PASS |
| OpenAI priced run 2027 | 110,083 | 110,083.3 | 09_Obligations H68 | PASS |
| 2028 stack, reported branch | 93,355 | 93,355 | 09_Obligations I73 | PASS |
| Plan envelope 2027 low / high; 2028 low / high | 65,800 / 69,500; 65,700 / 68,000 | same | 09_Obligations H82:I83 | PASS |
| E10 gap 2027 reported low / high | -21,930 / -18,230 | -21,930 / -18,230 | 09_Obligations AI98 / AJ98 (and H88 / H89) | PASS |
| E10 gap 2028 reported low / high | -27,655 / -25,355 | -27,655 / -25,355 | 09_Obligations AK98 / AL98 (and I88 / I89) | PASS |
| E10 gap 2028 proxy 9.3 x 5 GW (midpoint, approx.) | -33,000 (tol 1,500) | -33,005 | 09_Obligations AM99 | PASS |
| E10 gap 2028 proxy 12.5 x 5 GW / 9.3 x 15 GW / 12.5 x 15 GW | -49,000 / -126,000 / -174,000 | -49,005 / -126,005 / -174,005 | 09_Obligations AM100 / AM101 / AM102 | PASS |
| Grid (b) at (200,000, 77%, reported) | -25,355 | -25,355 | 07_Sensitivity G40 | PASS |
| OpenAI $50B split unexplained | 10,900 | 10,900 | 03_Costs G49 | PASS |
| Q2 GM grid at opex 3,000: gross / net-39.75 | 31% / 51% | 30.7% / 50.9% | 03_Costs D54 / E54 | PASS |
| AIBQ Anthropic CE default / closes; CI | 7.375 / 7.30; 5.55 | 7.375 / 7.300; 5.550 | 11_AIBQ F10 / G10; D18 | PASS |
| AIBQ OpenAI CE; CI | 3.925; 5.60 | 3.925; 5.600 | 11_AIBQ D25; D33 | PASS |
| Composites Anthropic default / closes / canonical-CI base | 8.15 / 8.13 / 8.04 | 8.150 / 8.135 / 8.0375 | 11_AIBQ H37 / H38 / H39 | PASS |
| Composites OpenAI net / gross case | 4.87 / 4.79 | 4.870 / 4.790 | 11_AIBQ H41 / H42 | PASS |
| Efficiency Index Anthropic / OpenAI | 0.55 / 0.50 | 0.550 / 0.499 | 11_AIBQ C44 / F44 | PASS |
| $B per point Anthropic / OpenAI; closes branch | 118 / 175; 119 | 118.4 / 174.9; 118.6 | 06_Valuation C26 / E26; C27 | PASS |
| Ladder spread default / closes / old; old OpenAI $/pt; $B more per point | 1.48x / 1.47x / 1.60x; 188; 57 | 1.478 / 1.475 / 1.598; 188.1; 56.5 | 06_Valuation F26 / F27 / F25; E25; H26 | PASS |
| Bessemer tails Bear / Base / Bull 2029, 2030 | 176,250 / 197,841; 231,276 / 266,446; 286,000 / 354,640 | same (to the unit) | 02_Revenue J74:K76 | PASS |
| SPV vs neocloud spread bp low / high; annual value | 325 / 400; 1,121 / 1,380 | 325 / 400; 1,121.25 / 1,380 | 10_Financing B18:C19 | PASS |
| Jul-16 reference multiples; Jul-16 CE ratio | 34.1x; 1.65x | 34.08x / 34.08x; 1.652 | 06_Valuation D16:D17; 05_Cash_Fund H42 | PASS |
| AM-71: growth / decayed / implied 2027 revenue | +476% / +333% / 249,356 | +475.8% / +333.1% / 249,356 | 13_OutsideView D27:D29 | PASS |
| Grid (a) corners: relative multiple (39.75, NET) / (27, NET) / (39.75, GROSS); CE ratio (39.75, GROSS) | +15% / -5% / -7%; 1.78x | +15.7% / -4.5% / -7.5%; 1.785 | 07_Sensitivity G8 / G6 / G12; H12 | PASS |
| Google implied rate at 5 GW / 16 GW | 8.0 / 2.5 | 8.00 / 2.50 | 09_Obligations D95 / E95 | PASS |

Workbook B check cells (05_Inference I5:I8; 09_Output E36:E40): G20 serving cost MoE on-demand 0.218 (expected 0.22) PASS; dense on-demand 13.02 (expected 13) PASS and 21.14 (expected 21) PASS; owning 1 GW-IT 35,993 vs 36,400 PASS; power 403 (70%) / 576 (100%) vs 400-620 PASS; crossover 2.87 (Volta rate) / 2.21 (Nscale rate) vs 2.5-3 PASS.

## 2. Deviations from the spec's check values and modelling assumptions the spec left open

1. **Riot start date (spec section 3.9 vs its own check values).** The schedule row says "9,100 / 20 from 2028 AJ start", but the spec's 2027 priced run (47,730), the addendum's E10 2027 gap and cost-stack section 2 all count Riot's 455 in 2027. L-136 ("20 years through June 2048") implies a July-2028 start. The workbook carries the start as a yellow AJ date on 00_Assumptions row 70 (`RIOTSTART`, default 2027-01-01) so the check values reproduce exactly; with 2028-01-01 the 2027 run is 47,275 and the 2027 reported-branch gap -17,775 to -21,475; with 2028-07-01 the 2028 run is 53,127.5. The orchestrator should pick one for the report text.
2. **Anthropic composite on the facility-closes branch: 8.135, printed 8.13 in the spec.** The arithmetic is 8.20 - 0.140 + 0.075 = 8.135 (11_AIBQ H36); the check tolerance is 0.006 so it passes; the report should say 8.13 or 8.14 consistently (rounding half-up gives 8.14).
3. **Efficiency Index OpenAI = 0.499** (0.4 + 0 + 0.33 x 0.3), printed 0.50 in aibq-delta; within tolerance.
4. **Grid (a) corner values** are the rounded spec figures (+15% / -5% / -7%); the model gives +15.7% / -4.5% / -7.5% (tolerance 1 pt).
5. **OpenAI 2026E derived P&L (04_PL G29 = -6,106) vs the H1 actual operating loss annualized (43,200).** The spec builds L4 2026E from O07 inference only (14,100) and L5 bottom-up (comp + retention), which cannot reach the actual loss; the gap (04_PL F42 = HOLE, +37,094) is printed as a reconciliation row, not allocated. Same for 2025A (derived L4 + L5 8,777 + 750 vs the reported 20,920 operating loss).
6. **Grid (c) vs the OpenAI P&L 2030E.** Grid (c) uses the compute-plan phasing ((plan - 50,000) x 35% = 245,000 in 2030 at Base) and gives -22,140 at (70%, 750,000); the bottom-up P&L (COGS % path + training budget = 198,246) gives +24,614 (04_PL K29). Both are AJ views; the grid is the spec's definition of the cash-flow-sign exhibit.
7. **Scenario envelope vs plan envelope.** E10's check values use the company plan (GM 77%, training 22,000) = 65,700-68,000; the live Base scenario (GM 70%) gives 79,000 (09_Obligations I84, printed as its own row). The section-5 finding is stated on the plan envelope.
8. **Workbook B, Vertically integrated: two magnitudes outside the section 7.4 bands** (09_Output D21:E22): cumulative capital to the first frontier-class model 56,811 vs 25,000-40,000 (+42% over the top of the band) and to the first $1B net revenue 81,229 vs 40,000-60,000 (+35%). Cause: the spec's own VI line items sum above the band once phased by year. Through Y3 the build (14,960 of 17,600), purchased GPUs (11,111 + network / storage 1,250), the ASIC program at 2,000 x 1.3 x 3 years (7,800), the training development premium (4,049), people at 800 -> 2,400 heads (4,352 + retention 750), data (5,450) and GTM/G&A (2,175) already sum to ~51,000 before leased merchant GPUs (2,995) and debt service. The band would hold only if the build and GPUs were not both counted before Y3 or if people / data / GTM were excluded; the reference-class check (>= 57,366 by Y5) passes. Every VI driver is yellow on B/00_Assumptions and can be reset.
9. **Workbook B milestone rule (AJ, flagged).** The spec's literal test ("first final run at >= the current-year frontier cost, G14 path") cannot be met by any scenario after Y1 because the G14 path grows 2.4x per year while the stated budgets grow ~1.5x. Implemented: Lean is judged against a prior-generation class run (170, Llama 3.1-405B / GPT-4.5 per L-115; `LEAN_THRESH`), Full against the current-year G14, VI against G14 lagged one year (`TH_LAG` = 1: its cluster is bought in Y2 and lands Y2-Y3, so the Y3 run is judged against the frontier it was bought to train). With these the milestone years are the spec's (Lean Y2, Full Y2, VI Y3; $1B Lean Y4, Full Y3, VI Y4; breakeven beyond Y5 for all three). Full's Y2 budget is 5,500 (interpolated between the spec's 1,500 in Y1 and 7,000 in Y3) so that budget / (G16 + G17) = 1,250 >= the Y2 frontier 1,200.
10. **Workbook B Lean training is capped by cluster size** (spec section 7.3): the training premium is zero and the whole leased cluster is the R&D resource; Lean therefore never keeps pace with the frontier after Y2 (final-run-equivalent stays at 170 while G14 reaches 6,912), which is the spec's own Lean story.
11. **Named ranges LB_01-LB_10 instead of LB01-LB10.** `LB01`-`LB10` are syntactically cell references (column LB, rows 1-10); Excel refuses such defined names and the `formulas` library parsed `LB10` as a cell (the first cross-check showed 22,000 instead of 65,700 at 09_Obligations I82). LibreOffice tolerated them, so the recalc had passed. The build now writes `LB_01`-`LB_10` (and `LB_05a`, `LB_05b`, `LB_06a`, `LB_06b`, `LB_07a`, `LB_07b`) in every formula and definedName; exhibits should reference the underscore form. Cross-check after the rename: 0 mismatches on both files.

## 3. Exhibit register: E1-E18 with the values shown at Base defaults

| Exhibit | Workbook / tab / range (actual) | Values at Base defaults | Check |
|---|---|---|---|
| E1 at-a-glance | A / 08_Output / A2:H14 | marks 965,000 / 852,000; equity 124,254 / 181,216.5; run-rate 65,000 GROSS / 40,000 (NET assumed); net run-rate 39,162.5 (39.75%) / 40,000; Q2 revenue 11,600 / 6,700; Q2 result +559 ADJUSTED operating income (non-GAAP) / -12,300 operating loss incl. SBC; FY2026E 48,830-62,580 / 32,400-45,500 (live 60,080 / 38,119); documented-$ 324,100 (reported-$ 524,100 [VERIFY]) / 480,400 (recalled-$ 690,000); unpriced GW Google 5 + 10 line of sight, AMD 2 / SB Energy 8.75 GW-IT, AMD 6, Broadcom 1.3 -> >5; IPO status no public S-1, Anthropic Oct / mid-Oct, OpenAI SW_IPO_OAI = 2027; CE 0.315 / 0.221, ratio 1.43x | PASS (section 1 lines) |
| E2 5-Layer definition | A / 00_Assumptions / A40:F60 | five layer rows (L1 Silicon, L2 Capacity, L3 Training, L4 Inference, L5 People) with placement rule, seed placement and unit (text) | n/a |
| E3 layer x year | A / 03_Costs / A5:K41 (L3-L5 both companies) and A / 09_Obligations / A60:K75 (L1-L2 annualized) | Anthropic 2026E-2028E: L3 7,000 / 14,000 / 22,000; L4 COGS 28,838 / 53,650 / 57,000 (Base GM 52 / 63 / 70%); L5 9,085 / 8,710 / 10,116; L1 SPV 3,450 / 6,900 / 6,900; L2 24,708 / 40,830 / 46,455; envelope L3 + L4 35,838 / 67,650 / 79,000. OpenAI 2026E: L3 25,000; L4 14,100 (inference only, flagged); L5 5,125; L1 5,000; L2 45,083 (2026; 105,083 in 2027). Priced runs Anthropic 28,158 / 47,730 / 53,355 / 44,605 / 38,355; OpenAI 2027 110,083 | PASS |
| E4 revenue ladders | A / 02_Revenue / A5:K31 | Anthropic run-rate 9,000 (Dec-25) -> 30,000 (Apr-6) -> 47,000 (May) -> 65,000 (Jul-31), 7.2x; OpenAI >20,000 (Dec-25) -> 24,000 (~2,000 monthly, Mar) -> >40,000 (Jul), 2.0x; quarterly Anthropic 787 (Q2-25) / 4,730 / 11,600, Q2/Q1 2.45x; OpenAI 5,700 / 6,700 (+17.5%); annual Anthropic FY2024 1,000, FY2025 10,000 (SW_A_FY25); OpenAI FY2025 13,100; PB forward block rows 28-31 (Anthropic 10 / 100 / 1,000 / 10,000 / 65,000 / 71,000; OpenAI 2,000 / 6,000 / 20,000 / 41,300) labelled never current | PASS |
| E5 gross-to-net restatement | A / 02_Revenue / A35:H50 and A / 06_Valuation / A5:H20 | net run-rate 39,162.5 (39.75%) / 47,450 (27%); OpenAI NET 40,000 / gross case 32,000 (R03 20% T4, yellow); Q2 net 6,989 / 8,468 vs OpenAI 6,700; multiples 14.8x (gross, display) / 24.6x / 20.3x; OpenAI 21.3x / 26.6x; relative +15.7% (39.75%) / -4.5% (27%); Jul-16 34.1x / 34.1x; haircut visible beside every net figure | PASS |
| E6 obligation stack Anthropic | A / 09_Obligations / A5:J20 | 13 counterparties; documented-$ 324,100 (B18); incl. SPV 358,600 (B19); reported-$ 524,100 [VERIFY] (B20, yellow); cancellable 48,250 = SpaceX 41,250 beyond 90 days + Riot options 7,000 (E18, 14.9% of documented-$); contingent inflows 55,000 (E19); Google leg unpriced in every filing, reported 200,000 in its own scope cell; SPV cash bound <= 1,725; SpaceX cash bound <= 2,560 (L-047) | PASS |
| E7 obligation stack OpenAI | A / 09_Obligations / A25:J40 | 12 rows; documented-$ 480,400 (B38) = Oracle 300,000 + AWS 138,000 + CoreWeave 22,400 + Cerebras 20,000; recalled-$ 690,000 (B39, all could-not-verify, yellow); sum 1,170,400 vs the 1,150,000 canonical tally (+1.8%); CNV share 59.0% (B40); unpriced T1 leases 8.75 GW-IT (E38); cash anchors 78,800 (E40) | PASS |
| E8 tally reconciliation | A / 09_Obligations / A45:H58 | Bloomberg 175,000 (= Lambda + Nscale + Fluidstack + SpaceX max); TechCrunch 61,250 (mixes equity); stepmark 99,100; youngresearch 517,000 (not reproducible, CUT); register 80,000 (superseded); The Information Google leg 200,000 [VERIFY]; v5 stack 324,100 / 358,600 / 524,100; OpenAI 665,000 / 600,000 / 750,000 spend plans; obligation stack 1,150,000 vs reconstructed 1,170,400; headline 1,400,000; 2026 spend 50,000 | PASS |
| E9 training vs inference | A / 03_Costs / A45:K60 and A / 04_PL / A30:H40 | per-run reference Grok 4 500 / GPT-4.5 200 + 2 / GPT-4 78 / Gemini 191 / Llama 170, 2.4x per yr, >1,000 by 2027 (never summed); $50B split 50,000 - 25,000 - 14,100 = 10,900 unexplained; Q2 adjusted-GM grid at opex 3,000 / 4,000 / 5,000: gross 30.7% / 39.3% / 47.9%, net-39.75 50.9% / 65.2% / 79.5%, net-27 42.0% / 53.8% / 65.7%; A19 cross-check 1 - 0.56 = 44% (Q1 29%); with payouts beside compute 4.25% (39.75%) / 17% (27%) -> flag INCONSISTENT vs the 25.9% opex ratio; H1 block: Anthropic 4,730 / 11,600 / 16,330 (16,230 on the >11,500 print), 2.45x, adjusted margin 5.1% on 10,900 (4.8% on 11,600); OpenAI 5,700 / 6,700 / 12,400, loss 9,300 / 12,300 / 21,600, 1.74x, +32% QoQ | PASS |
| E10 envelope vs commitments | A / 09_Obligations / A80:K98 (chart data A80:K95; branch grid AF97:AR102) | plan envelope 2026 30,032-42,045; 2027 65,800-69,500; 2028 65,700-68,000; scenario envelope (Base) 35,838 / 67,650 / 79,000 / 94,757 / 104,605; priced run 28,158 / 47,730 / 53,355 / 44,605 / 38,355; Google leg in use (reported) 0 / 40,000 / 40,000 / 40,000 / 40,000; AMD proxy 0 / 18,600 / 18,600 / 18,600 / 18,600 (2 GW x 9.3); gap before AMD (plan) 2026 +1,874 to +13,886; 2027 -21,930 to -18,230; 2028 -27,655 to -25,355; after AMD 2027 -40,530 to -36,830, 2028 -46,255 to -43,955; branch grid: reported -21,930/-18,230 and -27,655/-25,355; proxy 9.3 x 5 GW 2028 -34,155 to -31,855 (mid -33,005); 12.5 x 5 GW -49,005; 9.3 x 15 GW -126,005; 12.5 x 15 GW -174,005; consistency 8.0 at 5 GW, 2.5 at 16 GW vs chips-only 6.9 | PASS |
| E11 financing ladder | A / 10_Financing / A5:H29 | F01-F10 (SPV T+1pt / 5.75% / 8.5% on 34,500; project debt 15,200; Nvidia holds the Lambda lease 35,000; RVG 105,000 on 4.25 GW-IT; warrants; neocloud 9.00 / 9.75 / 9.625%; shells 1.76 / 2.38; full-stack 16.3 / 12.5; hyperscaler capex 175,000; Beacon Point 1.86 per MW-yr = 19,600 / 704 / 15); spread 325-400 bp = 1,121-1,380 per year on 34,500; backstop register (105,000; 19,600 / 50,200; 30,000; 15,200; 4,100 / 9,500; 2,573; 6,500; Huang text) | PASS |
| E12 Microsoft anchor | A / 01_Data rows LB08, LB08_AR, O11_*, O13_* and A / 09_Obligations / A25:J26 | 24,100 FY2026 revenue from OpenAI arrangements incl. revenue share (T1); A/R 6,000; cap 38,000 (T3); stake ~27% (~135,000) at the Oct-2025 recap (T2), post-dilution undisclosed; funding commitments 13,000 / 11,900 funded (1,100 unfunded = 0.6% of LB04; CE 0.221 -> 0.222 if stripped, 05_Cash_Fund J20); no % in the 10-K; 250,000 could-not-verify | n/a |
| E13 CE walk | A / 05_Cash_Fund / A40:L50 | Jul-16: 47,000 gross -> 28,317.5 net; OpenAI 25,000; CE 0.228 / 0.138; ratio 1.65x. Sep-9: 0.315 (39.75%) / 0.382 (27%) / 0.523 (gross, forbidden, red) vs 0.221; ratios 1.43x / 1.73x / 2.37x; OpenAI gross case 0.177, ratio 1.78x; change +0.087 / +0.083 / -0.22 | PASS |
| E14 AIBQ delta | A / 11_AIBQ / A5:M44 | Anthropic CE 8.00 -> 7.375 (CE-1 10 -> 8, CE-2 4 -> 5, CE-3 9, CE-4 8 -> 7.5 default / 7.0 closes, both printed); CI 5.05 -> 5.55 (7 / 5 / 4 / 6 / 5; canonical 5.8, delta -0.25); OpenAI CE 3.05 -> 3.925 (5 / 3.5 / 3 / 3; gross case 3.525); CI 4.50 -> 5.60 (6 / 6 / 4 / 7 / 4.5); composites 8.20 -> 8.15 (8.135 closes; 8.0375 canonical base) and 4.53 -> 4.87 (4.79 gross); Efficiency Index 0.55 / 0.499; flags per aibq-delta | PASS |
| E15 $/AIBQ-point ladder | A / 06_Valuation / A25:H32 | old 117.7 / 188.1, spread 1.60x, 70.4 more; new 118.4 / 174.9, spread 1.48x, 56.5 more; closes branch 118.6 (119), 1.47x; canonical base 120.0; OpenAI gross case 177.9 | PASS |
| E16 outside view | A / 13_OutsideView / A5:H30 | 12 forecast rows + 7 ledger-supported base-rate rows; Bessemer 70% / 80% (L-161); AWS 9.9% -> 25.4% -> 27-30% -> 37.0% / 35.4% (L-162); IPO slippage = analyst judgment with the Cerebras case and the 1.3x step-up (L-163); AM-71 arithmetic +475.8% -> +333.1% -> 249,356 vs 190,000-200,000; PB moves +29% / +38% | PASS |
| E17 sensitivity grids | A / 07_Sensitivity / A5:J16, A25:H41, A45:H55 | (a) NET rows: 27% 20.3x vs 21.3x -4.5% 1.73x; 33% 22.1x +3.9% 1.55x; 39.75% 24.6x +15.7% 1.43x; GROSS rows: 20.3x vs 26.6x -23.6% 2.16x; 22.1x -16.9% 1.94x; 24.6x -7.5% 1.78x. (b) panel 1 (training 22,000, reported leg 40,000): revenue 150,000 / 175,000 / 200,000 (rows) x GM 60 / 70 / 77% (columns): -11,355 / -26,355 / -36,855; -1,355 / -18,855 / -31,105; +8,645 / -11,355 / -25,355; panel 2 (training 30,000) each +8,000; panel 3 (proxy 46,500 at 9.3 x 5 GW) each -6,500; expected cell -25,355. (c) CAGR 40 / 70 / 100% (rows) x compute plan 600,000 / 750,000 / 900,000 (columns; 2030 compute 192,500 / 245,000 / 297,500 at 35% phasing): 2030E revenue 146,437 / 318,371 / 609,899; cells -89,994 / -142,494 / -194,994; +30,360 / -22,140 / -74,640; +234,429 / +181,929 / +129,429; Base (70%, 750,000) -22,140 negative; The Information's own 2030 figure +39,000 (L-082) | PASS |
| E18 greenfield | B / 07_Cash / A5:H82 (Lean A5:H30, Full A31:H56, VI A57:H82), B / 08_Reference / A4:H20, B / 09_Output / A3:G44 | Lean: Y1 1,105; Y2 1,468; frontier Y2 at 2,523; $1B Y4 at 5,423 (AJ probability 40%); breakeven beyond Y5; cumulative Y5 6,156 (all equity). Full: Y1 4,430; Y2 12,933; frontier Y2 at 17,162; $1B Y3 at 30,706 (70%); breakeven beyond Y5; cumulative Y5 66,400 (equity 62,953; debt 3,447). VI: Y1 8,484; Y2 27,696; frontier Y3 at 56,811; $1B Y4 at 81,229 (70%); breakeven beyond Y5; cumulative Y5 100,773 (equity 95,744; debt 5,029). Section 7.4 checks: Lean 4 of 4 PASS; Full 4 of 4 PASS; VI Y1 and Y2 PASS, frontier and $1B OUTSIDE (section 2 item 8), breakeven not reached (band allows). Reference class: Lean PASS (2,523 in 2,000-8,000); Full PASS (Y4 46,955 / Y5 66,400 in 20,656-82,622 and below 124,254); VI PASS (100,773 >= 57,366). Own 1 GW 35,993 (17,600 + 16,534 + 1,323 + 536) + power 403-576; full-stack lease 12,531-16,304; shell 1,761-2,382; crossover 2.2-2.9 yrs. G20: MoE 0.218 on-demand, 0.050-0.083 contracted (0.36 / 0.083 at 60%); MoE server 1.00 / 0.23-0.38; dense 13.0-21.1 on-demand, 2.98-8.05 contracted | PASS except VI frontier and $1B magnitudes (explained) |

## 4. The ten load-bearing figures (Workbook A; named ranges LB_01-LB_10 on 01_Data column D; the spec's LB01-LB10 written with an underscore, section 2 item 11)

| # | Figure | Named range (cell) | Value | Unit | As-of | Tier / status | Also displayed |
|---|---|---|---|---|---|---|---|
| 1 | Anthropic run-rate | LB_01 ('01_Data'!$D$5) | 65,000 | $M/yr GROSS | 2026-07-31 | T2 confirmed | 02_Revenue E9, 08_Output C18 |
| 2 | OpenAI run-rate | LB_02 ($D$6) | 40,000 | $M/yr, basis unstated (NET assumed) | 2026-07 | T2 confirmed | 02_Revenue E13, 08_Output C19 |
| 3 | Anthropic equity-only raised | LB_03 ($D$7) | 124,254 | $M | 2026-05-28 | T2 estimated (derived) | 05_Cash_Fund D15 (sum of rounds ties), 08_Output C20 |
| 4 | OpenAI equity-only raised | LB_04 ($D$8) | 181,216.5 | $M | 2026-03-31 | T2 estimated (derived) | 05_Cash_Fund J15 (ties), 08_Output C21 |
| 5 | Anthropic Q2-2026 revenue / ADJUSTED operating income | LB_05a ($D$9) = LB05; LB05b ($D$11) | 11,600 / 559 | $M | Q2-2026 | T2 / T2-T3 | 04_PL D33 / D36 (label "adjusted operating income, non-GAAP"), 08_Output C22 / C28 |
| 6 | OpenAI Q2-2026 revenue / operating loss incl. SBC | LB_06a ($D$16) = LB06; LB06b ($D$18) | 6,700 / 12,300 | $M | Q2-2026 | T2 | 04_PL E33 / E36, 08_Output C23 / E28 |
| 7 | OpenAI compute spend 2026 / plan through 2030 | LB_07a ($D$19) = LB07; LB07b ($D$20) | 50,000 / 750,000 | $M | 2026-05-05 / 2026-07-22 | T2 | 03_Costs D49, 09_Obligations D58 / D56, 08_Output C24 / G28 |
| 8 | Microsoft revenue from OpenAI arrangements FY2026 | LB_08 ($D$23) | 24,100 | $M | FY ended 2026-06-30 | T1 | 09_Obligations C26 and schedule C16b annual value, 08_Output C25 |
| 9 | SB Energy PORTS leases | LB_09 ($D$25) with LB09_RVG ($D$27) | 8.0 GW-IT; RVG 105,000 | GW-IT / $M | 2026-08-17 | T1 | 09_Obligations schedule C17, 10_Financing G8 / B22, 08_Output C26 |
| 10 | Anthropic 2028 revenue forecast | LB_10 ($D$31) with LB10_high ($D$32) | 190,000-200,000 | $M | FY2028E (Aug-2026) | T2 estimated | 00_Assumptions E9 (Base 2028), 09_Obligations I82:I83, 08_Output C27 |

(Row numbers on 01_Data: LB01 D5 ... as registered by the build; verify with `python3 -c "from openpyxl import load_workbook; wb=load_workbook('model/entry-fee-v5.xlsx'); print({k:v.attr_text for k,v in wb.defined_names.items()})"`.)

## 5. Tab-by-tab notes, HOLEs and AJ placeholders beyond the spec

- **00_Assumptions.** Timeline row 2 numeric (typed once, D2 = 2023) and row 3 text labels; SW_SCEN C4. Scalar AJ drivers rows 7-38 with Bear/Base/Bull (yellow) and the live column G; contract timing rows 64-82; grid axes and unit constants rows 86-90 (12, 1,000, 4, 1,000, 5 ramp steps, 10,000 bp, 1,000 $ per $K); time-series drivers rows 95-125 (GM path, training, OpenAI COGS %, OpenAI training, headcount paths); spec check values rows 130-228. **Model-agent placeholders with no spec value (yellow, tagged HOLE):** Anthropic headcount growth 2027E+ (30 / 25 / 20%, row 17) and GTM + G&A as % of comp (60 / 50 / 40%, row 21); these feed only L5 and the P&L, no check value. Terms, dates and ramp factors that the spec states as single AJ values carry the same value in all three scenarios.
- **01_Data.** 412 rows (one per value), every one with the composite source string in column C. Retired rows not entered (C-04 -42,000; L-124; the 3x-cheaper Fast Mode; 161,254; 47,160; WSJ breakeven years). The three could-not-verify values 250,000 / 90,000 / 350,000 sit in a separate "tally-only" block (yellow) read only by the recalled-$ rows; A20 (200,000 reported Google) is yellow and read only by the REPORTED schedule row, the Google-leg switch and the reported-$ line, never by documented-$.
- **02_Revenue.** 2023A Anthropic and 2023A-2024A OpenAI revenue read HOLE (spec section 3.4); the PB series lives only in the projection block. Bessemer tails for all three scenarios are computed in rows 74-76 beside the live row 71.
- **03_Costs.** Anthropic L5 2023A-2025A and SBC are HOLE; OpenAI L4 2026E is inference-only (flagged); OpenAI L5 2027E+ "other" is the residual to the OAIOPEX % path. The A19 consistency flag prints INCONSISTENT at 39.75% (4.25% implied GM after payouts vs a 25.9% opex ratio), the datapoint against the C-13 internal branch.
- **04_PL.** No breakeven-year cells; the C-12 branch text is displayed (D17); the OpenAI 2026E reconciliation HOLE is F42.
- **05_Cash_Fund.** Rounds reproduce LB03 / LB04 exactly; the total-raised VIEW follows SW_TOTAL_RAISED_VIEW without touching CE; the burn plug (D61 = 7,560 at Base: 43,200 annualized loss - 8,640 SBC - 27,000 burn) is yellow HOLE; the revolver drawn / undrawn is HOLE; the 15,000 expansion shows 0 at the default (does not close).
- **06_Valuation / 11_AIBQ.** Ruling 2: no coefficient anywhere; the word itself is absent from the saved XML. CE-4 prints both facility branches (11_AIBQ F10 / G10, K8); OpenAI CE-1 follows SW_OAI_BASIS.
- **07_Sensitivity.** Grid (a) rows 6-8 NET, 10-12 GROSS; grid (b) three panels rows 25-38 with the expected cell G40; grid (c) rows 45-52.
- **09_Obligations.** Schedule A100:AD127 (25 rows; year values U:AB; cancellable AC); the E10 branch grid sits at AF97:AR102 so the schedule header at row 100 stays clear; Fluidstack (phasing HOLE), the Google GW rows, AMD, SB Energy (rent HOLE), the recalled rows, Nvidia and Stargate are flagged EXCL from the priced run. Landlord-lease columns for Lambda (15 yr, 704 MW, 19,600) are in AD106.
- **10_Financing, 12_Conflicts, 13_OutsideView, 08_Output** as the register above; 08_Output check table rows 45-140, FAIL count D141. 12_Conflicts: column C is the named live value (formula), column D the selector (blue), E:H the branch values linked from 01_Data; the retired "161,254" label text was not carried (the view computes 126,754 + 34,500 by formula).
- **Workbook B.** Every scenario driver is yellow on B/00_Assumptions rows 11-49 and 54-108 with its range; **placeholders beyond the spec:** leader share of headcount 10 / 3 / 2% (the spec's 10% at 100 heads cannot hold at 3,000), leader comp 15 (5-25), senior 1.0, engineer 0.53; the Y2 Full/VI budget 5,500; GPU fleet paths by year; revenue ramps; inference % paths; `LEAN_THRESH` 170; `TH_LAG` 0 / 0 / 1; debt share 60% for VI; power utilization 70%; Norway power 50 $/MWh (40-60). Storage (G13), safety (G25), the ASIC program (G29), the vendor "half cost" claim and the equipment-financing rate are yellow could-not-verify / vendor / AJ as the spec flags them.

## 6. Constants audit (verify.py)

Typed numeric constants outside 00_Assumptions and 01_Data: Workbook A 13 (the 12_Conflicts selectors D5:D17: 1 / 1 / 2 / 1 / 2 / 2 / 1 / 2 / 1 / 2 / 1 / 1 / 1, blue inputs by design); Workbook B 0. Numeric literals inside formulas: Workbook A only 0 (IFERROR / MAX guards and IF outputs), 1 (the unit in (1 - haircut), the +1 inclusive month count, the CHOOSE branch index) and one 2 (04_PL E42, halves per year in the H1 annualization); Workbook B only 0 (guards). Unit conversions are named cells (00_Assumptions row 90 in A; row 50 in B). Named ranges are quoted correctly after requote.py.

Formulas-library cross-check (build/xcheck_formulas.json): Appendix A; 52 cells on A and 20 on B, 0 mismatches after the LB_ rename.

## 7. Scenario and switch sweep (Workbook A; build/sweep_a.py, build/sweep_a.json)

Appendix B: 24 states (Base default; SW_SCEN 1 and 3; every other switch at each non-default branch, 15 states; six joint combinations incl. Bear and Bull with every switch on its alternative branch), each recalculated by LibreOffice on a temp copy: 0 error cells in every state; recalc status success throughout. The sweep ran on the file before the LB_ rename; LibreOffice evaluated the old names correctly (values identical to the renamed file at Base). Readings: the E10 gap (plan envelope, before AMD) at 2028 is -27,655 to -25,355 on the reported branch in every scenario (it depends on the Google switches, not SW_SCEN); proxy branch -34,155 to -31,855 at 9.3 x 5 GW; Bear with proxy 16.3 -69,155 to -66,855; Bull with proxy 6.9 -22,155 to -19,855; 12.5 x 15 GW -175,155 to -172,855; the all-alternative Bear state -232,155 (16.3 x 15 GW). The relative-multiple sign is + (+15.7%) at 39.75% / NET, - (-4.5%) at 27% / NET, - (-7.5%) at 39.75% / GROSS, - (-23.6%) at 27% / GROSS; the CE ratio 1.43x / 1.73x / 1.78x / 2.16x in the same four states. SW_15B_FACILITY = Closes moves the Anthropic composite 8.150 -> 8.135; SW_OAI_BASIS = GROSS moves OpenAI's 4.870 -> 4.790 and the six OpenAI-basis-dependent check lines to FAIL by construction (the check values are Base-basis). The scenario switch moves FY2026E Anthropic 48,830 (Bear) / 60,080 (Base) / 62,580 (Bull) and the live scenario envelope, not the plan-envelope gap.

## Appendix A. Formulas-library cross-check (build/xcheck_formulas.py; LibreOffice cached value vs the `formulas` library on the re-quoted file)


entry-fee-v5.xlsx: 52 cells compared, 0 mismatches (9 s).

| Cell | LibreOffice | formulas library | Match |
|---|---|---|---|
| 01_Data!D5 | 65000 | 65000 | yes |
| 02_Revenue!D38 | 39162.5 | 39162.5 | yes |
| 02_Revenue!M54 | 60080 | 60080.0 | yes |
| 02_Revenue!M55 | 57580 | 57580.0 | yes |
| 02_Revenue!M56 | 62580 | 62580.0 | yes |
| 02_Revenue!M57 | 48830 | 48830.0 | yes |
| 02_Revenue!M66 | 38118.7 | 38118.70000000001 | yes |
| 02_Revenue!J75 | 231275.862068966 | 231275.8620689655 | yes |
| 02_Revenue!K75 | 266445.743162901 | 266445.7431629013 | yes |
| 05_Cash_Fund!D17 | 126754 | 126754.0 | yes |
| 05_Cash_Fund!J17 | 186436.5 | 186436.5 | yes |
| 05_Cash_Fund!E44 | 0.315181000209249 | 0.3151810002092488 | yes |
| 05_Cash_Fund!E45 | 0.381879054195438 | 0.3818790541954384 | yes |
| 05_Cash_Fund!G44 | 0.220730452249105 | 0.22073045224910534 | yes |
| 05_Cash_Fund!H44 | 1.42789994311048 | 1.4278999431104833 | yes |
| 06_Valuation!D9 | 24.6409192467284 | 24.640919246728377 | yes |
| 06_Valuation!D10 | 20.3371970495258 | 20.337197049525816 | yes |
| 06_Valuation!D12 | 21.3 | 21.3 | yes |
| 06_Valuation!D13 | 26.625 | 26.625 | yes |
| 06_Valuation!C26 | 118.40490797546 | 118.40490797546013 | yes |
| 06_Valuation!E26 | 174.948665297741 | 174.9486652977413 | yes |
| 06_Valuation!F26 | 1.47754572246279 | 1.477545722462789 | yes |
| 09_Obligations!B18 | 324100 | 324100.0 | yes |
| 09_Obligations!B19 | 358600 | 358600.0 | yes |
| 09_Obligations!B20 | 524100 | 524100.0 | yes |
| 09_Obligations!B38 | 480400 | 480400.0 | yes |
| 09_Obligations!B39 | 690000 | 690000.0 | yes |
| 09_Obligations!B46 | 175000 | 175000.0 | yes |
| 09_Obligations!G64 | 28158.3333333333 | 28158.333333333332 | yes |
| 09_Obligations!H64 | 47730 | 47730.0 | yes |
| 09_Obligations!I64 | 53355 | 53355.0 | yes |
| 09_Obligations!J64 | 44605 | 44605.0 | yes |
| 09_Obligations!K64 | 38355 | 38355.0 | yes |
| 09_Obligations!H68 | 110083.333333333 | 110083.33333333333 | yes |
| 09_Obligations!I82 | 65700 | 65700.0 | yes |
| 09_Obligations!I83 | 68000 | 68000.0 | yes |
| 09_Obligations!I88 | -27655 | -27655.0 | yes |
| 09_Obligations!I89 | -25355 | -25355.0 | yes |
| 09_Obligations!AM99 | -33005 | -33005.0 | yes |
| 09_Obligations!AM101 | -126005 | -126005.0 | yes |
| 11_AIBQ!F10 | 7.375 | 7.375 | yes |
| 11_AIBQ!D17 | 5 | 5 | yes |
| 11_AIBQ!D24 | 3 | 3 | yes |
| 11_AIBQ!D31 | 7 | 7 | yes |
| 03_Costs!G49 | 10900 | 10900.0 | yes |
| 03_Costs!D54 | 0.306810344827586 | 0.30681034482758623 | yes |
| 03_Costs!E54 | 0.509228788095579 | 0.5092287880955788 | yes |
| 07_Sensitivity!G40 | -25355 | -25355.0 | yes |
| 10_Financing!B18 | 325 | 324.99999999999994 | yes |
| 13_OutsideView!D29 | 249355.948 | 249355.94800000003 | yes |
| 08_Output!D45 | PASS | PASS | yes |
| 08_Output!D142 | None | None | yes |

greenfield-entry-cost.xlsx: 20 cells compared, 0 mismatches (5 s).

| Cell | LibreOffice | formulas library | Match |
|---|---|---|---|
| 09_Output!C4 | 1105.495 | 1105.4950000000001 | yes |
| 09_Output!D4 | 4429.5775 | 4429.5775 | yes |
| 09_Output!E4 | 8484.2584 | 8484.258399999999 | yes |
| 09_Output!C7 | 2523.29856870229 | 2523.29856870229 | yes |
| 09_Output!D7 | 17162.2903009259 | 17162.290300925928 | yes |
| 09_Output!E7 | 56810.5064185185 | 56810.50641851852 | yes |
| 09_Output!C9 | 5423.42606870229 | 5423.426068702291 | yes |
| 09_Output!D9 | 30705.861478588 | 30705.861478587965 | yes |
| 09_Output!E9 | 81228.6713842593 | 81228.67138425926 | yes |
| 09_Output!C12 | 6155.71106870229 | 6155.7110687022905 | yes |
| 09_Output!D12 | 66400.2663194445 | 66400.26631944445 | yes |
| 09_Output!E12 | 100773.216625 | 100773.216625 | yes |
| 09_Output!C36 | 35992.8571428571 | 35992.85714285713 | yes |
| 09_Output!C40 | 2.87223 | 2.872229999999999 | yes |
| 05_Inference!D5 | 0.217889337118382 | 0.2178893371183824 | yes |
| 05_Inference!D7 | 13.0208333333333 | 13.020833333333334 | yes |
| 05_Inference!D8 | 21.1352657004831 | 21.135265700483092 | yes |
| 09_Output!C26 | PASS | PASS | yes |
| 09_Output!C27 | PASS | PASS | yes |
| 09_Output!C28 | PASS | PASS | yes |

## Appendix B. Scenario and switch sweep (build/sweep_a.py; each state recalculated by LibreOffice on a temp copy; Base defaults otherwise)

No error cells under any state (column 'errors'). 'fails' = the 08_Output FAIL count (the check table assumes Base defaults, so non-zero counts away from Base are expected and listed).

| State | recalc | errors | fails | scenario | FY2026E Anthropic | E10 gap 2028 low | high | Google leg 2028 | relative multiple (live) | sign | CE ratio | composite A | composite O |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BASE_DEFAULT | success | 0 | 0 | Base | 60,080 | -27,655 | -25,355 | 40,000 | +15.7% | + | 1.43x | 8.150 | 4.870 |
| SW_SCEN=1 | success | 0 | 0 | Bear | 48,830 | -27,655 | -25,355 | 40,000 | +15.7% | + | 1.43x | 8.150 | 4.870 |
| SW_SCEN=3 | success | 0 | 0 | Bull | 62,580 | -27,655 | -25,355 | 40,000 | +15.7% | + | 1.43x | 8.150 | 4.870 |
| SW_HAIRCUT=2 | success | 0 | 0 | Base | 60,080 | -27,655 | -25,355 | 40,000 | -4.5% | - | 1.73x | 8.150 | 4.870 |
| SW_OAI_BASIS=2 | success | 0 | 6 | Base | 60,080 | -27,655 | -25,355 | 40,000 | -7.5% | - | 1.78x | 8.150 | 4.790 |
| SW_IPO_OAI=1 | success | 0 | 0 | Base | 60,080 | -27,655 | -25,355 | 40,000 | +15.7% | + | 1.43x | 8.150 | 4.870 |
| SW_A_FY25=2 | success | 0 | 0 | Base | 60,080 | -27,655 | -25,355 | 40,000 | +15.7% | + | 1.43x | 8.150 | 4.870 |
| SW_A_FY24_NI=1 | success | 0 | 0 | Base | 60,080 | -27,655 | -25,355 | 40,000 | +15.7% | + | 1.43x | 8.150 | 4.870 |
| SW_A_2026_LOSS=1 | success | 0 | 0 | Base | 60,080 | -27,655 | -25,355 | 40,000 | +15.7% | + | 1.43x | 8.150 | 4.870 |
| SW_A_HC=2 | success | 0 | 0 | Base | 60,080 | -27,655 | -25,355 | 40,000 | +15.7% | + | 1.43x | 8.150 | 4.870 |
| SW_TPU_RATE=1 | success | 0 | 0 | Base | 60,080 | -27,655 | -25,355 | 40,000 | +15.7% | + | 1.43x | 8.150 | 4.870 |
| SW_TPU_RATE=3 | success | 0 | 0 | Base | 60,080 | -27,655 | -25,355 | 40,000 | +15.7% | + | 1.43x | 8.150 | 4.870 |
| SW_TPU_RATE=4 | success | 0 | 0 | Base | 60,080 | -27,655 | -25,355 | 40,000 | +15.7% | + | 1.43x | 8.150 | 4.870 |
| SW_TOTAL_RAISED_VIEW=2 | success | 0 | 0 | Base | 60,080 | -27,655 | -25,355 | 40,000 | +15.7% | + | 1.43x | 8.150 | 4.870 |
| SW_15B_FACILITY=1 | success | 0 | 0 | Base | 60,080 | -27,655 | -25,355 | 40,000 | +15.7% | + | 1.43x | 8.135 | 4.870 |
| SW_SSI=2 | success | 0 | 0 | Base | 60,080 | -27,655 | -25,355 | 40,000 | +15.7% | + | 1.43x | 8.150 | 4.870 |
| SW_GW_2028=2 | success | 0 | 0 | Base | 60,080 | -27,655 | -25,355 | 40,000 | +15.7% | + | 1.43x | 8.150 | 4.870 |
| SW_GOOGLE_VALUE=2 | success | 0 | 0 | Base | 60,080 | -34,155 | -31,855 | 46,500 | +15.7% | + | 1.43x | 8.150 | 4.870 |
| Bear+proxy16.3 | success | 0 | 0 | Bear | 48,830 | -69,155 | -66,855 | 81,500 | +15.7% | + | 1.43x | 8.150 | 4.870 |
| Bull+proxy6.9 | success | 0 | 0 | Bull | 62,580 | -22,155 | -19,855 | 34,500 | +15.7% | + | 1.43x | 8.150 | 4.870 |
| proxy+15GW+12.5 | success | 0 | 0 | Base | 60,080 | -175,155 | -172,855 | 187,500 | +15.7% | + | 1.43x | 8.150 | 4.870 |
| 27pct+GROSS | success | 0 | 6 | Base | 60,080 | -27,655 | -25,355 | 40,000 | -23.6% | - | 2.16x | 8.150 | 4.790 |
| Bear+all-alt | success | 0 | 6 | Bear | 48,830 | -232,155 | -229,855 | 244,500 | -23.6% | - | 2.16x | 8.135 | 4.790 |
| Bull+all-alt | success | 0 | 6 | Bull | 62,580 | -91,155 | -88,855 | 103,500 | -23.6% | - | 2.16x | 8.135 | 4.790 |

States run: 24; states with any error cell: 0; recalc non-success: none.
