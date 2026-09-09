# Model Spec: Workbook A (report model) and Workbook B (greenfield entry cost)
Agent 2 (Analyst) to Agent 4 (Model), 2026-09-09. Two openpyxl builds. Every input carries its ledger row, value, unit, as-of, basis, status and tier; every derived number is a formula chain from `01_Data`; every HOLE is a blue input with a Bear/Base/Bull triple and yellow fill; nothing is typed twice. Figures in $M unless stated. No em-dashes in any cell text or sheet name; hyphens for ranges.

---

## 0. House conventions (from `prior/models/Anthropic_Model_v1_ROADMAP.md`, locked)

- Blue font = hard-coded input; black = formula; green = output/KPI; yellow fill = placeholder / low confidence / analyst judgment (AJ).
- $M throughout model tabs ($65B = 65,000). `01_Data` stores figures as reported with a units column.
- Timeline tabs: years in columns D:K = 2023A, 2024A, 2025A, 2026E, 2027E, 2028E, 2029E, 2030E; typed once on `00_Assumptions` row 3 and linked everywhere.
- Column A = label; B = units; C = source / tier flag (format: `L-032 · confirmed · T2 · 2026-07-31 · GROSS`).
- One number, one home. Basis-tag every revenue line (GROSS / NET-39.75 / NET-27 / NET-unstated). Never hard-code a value used twice.
- Named ranges for every switch (§5) and for the ten load-bearing figures (§2, IDs LB01-LB10) so exhibits can reference names, not addresses.
- Provenance columns on `01_Data`: ID · item · value · unit · as-of · basis · status · tier · decay · ledger row · used-by (tab list).

---

## 1. Workbook A: `100B_Entry_Fee_v5.xlsx`, tab list (house numbering, extended)

| Tab | Purpose | Feeds exhibits |
|---|---|---|
| `00_Assumptions` | Timeline (row 3), scenario switch `SW_SCEN` (C4: 1 Bear / 2 Base / 3 Bull), every AJ driver grouped by module with Bear/Base/Bull triples, the printed 5-Layer definition (A40:F60) | E2 |
| `01_Data` | Facts only: one row per ledger anchor used anywhere (§2), with provenance columns; named ranges LB01-LB10 | E1, E12 |
| `02_Revenue` | Run-rate ladders (dated), recognized quarterly and annual, PB forward projections (separate block, labelled), FY2026E integrations, gross → net rows at both haircuts, OpenAI basis rows | E4, E5 |
| `03_Costs` | The 5-Layer stack consumption layers L3, L4, L5 by year, both companies; L1/L2 annualized links from `09_Obligations`; the training-vs-inference basis table; the Q2 GM cross-check grid | E3, E9 |
| `04_PL` | P&L rollup 2023A-2030E, both companies; dual view (excl-training / incl-training) built ONLY from ledger rows and AJ inputs (no WSJ Apr-6 breakeven years); H1-2026 actuals block | E9 |
| `05_Cash_Fund` | Burn walk (both vintages for OpenAI); capitalization (equity rounds, debt facilities, lease obligations shown separately); CE equity-only at every basis; the CE walk Jul-16 → Sep-9 | E13 |
| `06_Valuation` | Marks ladder; multiples at gross / 39.75% / 27% (Anthropic) and net / gross-case (OpenAI); $/AIBQ-point ladder (no correlation anywhere) | E5, E15 |
| `07_Sensitivity` | Three grids (§6) wired to the switches; scenario table | E17, E10 band |
| `08_Output` | One-page dashboard: E1 at-a-glance table; the ten load-bearing figures; verdict flags | E1 |
| `09_Obligations` | Contract schedule (one row per commitment: counterparty, layer, start, end, term, total, annual value, cancellability flag, backstop flag, tier); contracted / cash / cancellable tables; tally reconciliation; annualized priced run by year; the envelope-vs-commitments chart data | E3 (L1-L2), E6, E7, E8, E10 |
| `10_Financing` | Cost-of-capital ladder; backstop register; spread arithmetic | E11 |
| `11_AIBQ` | CE-1..CE-4 and CI-1..CI-5 old → new with rubric bands, weights, dimension and composite deltas, flags | E14 |
| `12_Conflicts` | Switch register: one row per frozen conflict with named switch cell, branch values, and the cells each gates; resolved conflicts listed with their resolution | §14 table |
| `13_OutsideView` | Reference classes and base rates per forecast, with row or "AJ" | E16 |

---

## 2. Workbook A inputs register (`01_Data`). Load-bearing figures are LB01-LB10.

| ID | Item | Value | Unit | As-of | Basis | Status | Tier | Decay | Row | Used by |
|---|---|---|---|---|---|---|---|---|---|---|
| LB01 | Anthropic run-rate | 65,000 | $M/yr | 2026-07-31 | GROSS run-rate | confirmed | T2 | QUARTERLY | L-032 | 02, 05, 06, 11 |
| LB02 | OpenAI run-rate | 40,000 (floor; ">40") | $M/yr | 2026-07 | unstated (NET assumed; SW_OAI_BASIS) | confirmed | T2 | QUARTERLY | L-065 | 02, 05, 06, 11 |
| LB03 | Anthropic equity-only raised | 124,254.0 | $M | 2026-05-28 | sum of ten PB equity rounds | estimated | T2 | STABLE | L-007 | 05, 11 |
| LB04 | OpenAI equity-only raised | 181,216.5 | $M | 2026-03-31 | sum of PB equity rounds | estimated | T2 | STABLE | L-022 | 05, 11 |
| LB05a | Anthropic Q2-2026 revenue | 11,600 (range 11,500-11,600) | $M | Q2-2026 | recognized, preliminary, GROSS presumed | confirmed | T2 | QUARTERLY | L-033 | 02, 03, 04 |
| LB05b | Anthropic Q2-2026 operating profit | 559 (projection; sign confirmed) | $M | Q2-2026 | operating profit, not FCF (Ruling 3) | confirmed | T2 | QUARTERLY | L-034 | 04, 11 |
| LB06a | OpenAI Q1 / Q2-2026 revenue | 5,700 / 6,700 | $M | H1-2026 | recognized, NET presumed | confirmed | T2 | QUARTERLY | L-066 | 02, 04 |
| LB06b | OpenAI Q1 / Q2-2026 operating loss incl. SBC | 9,300 / 12,300 | $M | H1-2026 | GAAP-style, incl. SBC | confirmed | T2 | QUARTERLY | L-066 | 04, 05, 11 |
| LB07a | OpenAI 2026 compute spend | 50,000 | $M | 2026-05-05 | company statement (sworn) | confirmed | T2 | QUARTERLY | L-078 | 03, 09 |
| LB07b | OpenAI compute plan through 2030 | 750,000 (600,000 May vintage; 665,000 Feb vintage) | $M | 2026-07-22 | consumption plan 2026-2030 | estimated | T2 | QUARTERLY | L-062, L-078, L-082 | 09, 07 |
| LB08 | Microsoft FY2026 revenue from OpenAI arrangements | 24,100 (A/R 6,000) | $M | FY ended 2026-06-30 | Azure consumption plus revenue share received | confirmed | T1 | STABLE | L-054 | 09, 10 |
| LB09 | SB Energy PORTS leases / Nvidia RVG | 8.0 GW-IT, 20 yr; RVG 105,000 on 4.25 GW-IT; Milam 753 MW, 15 yr | GW / $M | 2026-08-17 | issuer S-1 | confirmed | T1 | STABLE | L-061, L-147 | 09, 10, 11 |
| LB10 | Anthropic 2028 revenue forecast | 190,000-200,000 | $M | FY2028E (Aug-2026 vintage) | company forecast to IPO investors, GROSS presumed | estimated | T2 | QUARTERLY | L-036 | 02, 09, 07 |
| M01 | Anthropic post-money mark | 965,000 | $M | 2026-05-28 | Series H post | confirmed | T2/T1 | VOLATILE | L-005, L-038 | 06 |
| M02 | OpenAI post-money mark | 852,000 | $M | 2026-03-31 (tender at same price 2026-08-10) | Mar-2026 round post | confirmed | T2 | VOLATILE | L-019, L-067 | 06 |
| R01 | Equalization, internal | 39.75 | % | 2026-07-16 | Ruling 5 | recalled | T4 | PERMANENT | L-126 | 02, 05, 06, 11 (via SW_HAIRCUT) |
| R02 | Equalization, external | 27 | % | 2026-04 | OpenAI CRO memo relay, adversarial | recalled | T4 | STABLE | L-126, C-13 | same |
| R03 | Microsoft share (if OpenAI figure is gross) | 20 | % | n/a | T4 only; NEVER printed as a fact | recalled | T4 | STABLE | L-052 notes | 02 (gross case only) |
| A01 | Anthropic run-rate ladder | 9,000 (2025-12) · 30,000 (2026-04-06) · 47,000 (2026-05) · 65,000 (2026-07-31) | $M/yr | dated | GROSS | confirmed | T1/T2 | QUARTERLY | L-139, L-037, L-032 | 02 |
| A02 | Anthropic YE-2026 run-rate expectation | 100,000-120,000 | $M/yr | 2026-08-17 | investor expectation, not guidance | estimated | T3 | QUARTERLY | L-035 | 02 |
| A03 | Anthropic Q1-2026 revenue | ~5,000 | $M | Q1-2026 | derived (Q2 "more than doubled") | could-not-verify | T2 | QUARTERLY | L-129 | 02 |
| A04 | Anthropic PB revenue series | 10 · 100 · 1,000 · 10,000 · 65,000 · 71,000 (2022-2027) | $M | pulled 2026-09-09 | 2022-2025 recognized-estimate (basis unstated); 2026-2027 projections | estimated | T2 | n/a | L-010, L-009 | 02 (projection block only) |
| A05 | Anthropic FY2024 revenue / net loss | 1,000 / −8,300 (alt −5,300) | $M | FY2024 | PB deal-record financials | estimated | T2 | QUARTERLY | L-012, C-05 | 04 (SW_A_FY24_NI) |
| A06 | Anthropic FY2025 recognized revenue | 10,000 (PB) / 4,500-6,000 (implied) | $M | FY2025 | C-03 | estimated | T2 / T4 | QUARTERLY | L-010, L-120 | 04 (SW_A_FY25) |
| A07 | Anthropic GM path | −94 (2024) · 40 (2025) · 44-60 (2026) · 63 (2027E) · 77 (2028E) | % | 2026-01 vintage | The Information relay; register | recalled | T4 | QUARTERLY | L-119 | 03, 04, 07 |
| A08 | Anthropic training budget | 7,000 · 14,000 · 22,000 (2026-2028) | $M/yr | undated leaked docs | annual training-compute budget (C-11) | recalled | T4 | STABLE | L-125 | 03, 04, 09 |
| A09 | Anthropic Jan-2026 plan | rev 18,000 · 55,000 · 102,000 · 148,000 (2026-2029); loss ~11,000 (2026, 2027); server rentals ~180,000 through 2029; FY2025 burn 5,600 | $M | 2026-01 | superseded plan; C-12 | recalled | T4 | QUARTERLY | L-120 | 13, 12 (SW_A_2026_LOSS) |
| A10 | Anthropic headcount | 5,000 (PB) / ~4,020 (Revelio) | people | 2026-04-21 / 2026-03 | C-18 | confirmed / estimated | T2 / T4 | QUARTERLY | L-008, L-091 | 03 (SW_A_HC) |
| A11 | Anthropic debt facilities | revolver 2,500; expansion 15,000 nearing final | $M | 2025-05-16 / 2026-09-03 | facilities | confirmed / estimated | T2 / T3 | STABLE | L-014, L-042 | 05 (SW_15B_FACILITY) |
| A12 | TPU lease SPV | 34,500 (30,000 Broadcom-supported; 4,500 unsupported); 5-yr lease; tranches T+1pt / 5.75% / 8.5% | $M | 2026-06 | lessor debt, off-balance-sheet | estimated | T3 | STABLE | L-044 | 09, 10, 05 (SW_TOTAL_RAISED_VIEW) |
| A13 | Project-company debt (TPU sites) | 15,200 for 1.43 GW | $M | 2026-08-12 | off-balance-sheet | estimated | T3 | STABLE | L-045 | 09, 10 |
| A14 | Copyright | settlement 1,500 (approved 2026-07-20); music demands >3,000 | $M | 2026-07 | cash 2026; unreserved claims | confirmed | T2 | STABLE | L-086 | 03 (L5) |
| A15 | Comp anchors | MTS base 1.12-1.38 per person; T4 bands 0.30-0.76 | $M/yr | 2026 | base only / total comp | estimated | T3 / T4 | QUARTERLY | L-092 | 03 (L5, AJ) |
| A16 | Series H composition | 65,000 incl. 15,000 previously committed hyperscaler money (5,000 Amazon) | $M | 2026-05-28 | company statement | confirmed | T1 | STABLE | L-038 | 05 |
| A17 | Contingent equity inflows | Amazon up to 20,000; Google 30,000; AMD up to 5,000 | $M | 2026 | milestone-based; not in capital raised | confirmed | T1 / T2 / T1 | STABLE | L-072, L-073, L-043 | 05, 09 |
| A18 | List prices | Fable 5.1 10 / 50; Opus 5 5 / 25; Sonnet 5 2 / 10; Haiku 4.5 1 / 5; Fast Mode 2x; cache read 0.25 (Fable 5.1) | $ per MTok | 2026-09-09 | pricing page | confirmed | T1 | VOLATILE | L-084 | 03 (unit economics block) |
| O01 | OpenAI FY2025 revenue | 13,100 | $M | FY2025 | NET presumed; FT-verified 13,070 | confirmed | T2 | STABLE | L-063 | 02, 04 |
| O02 | OpenAI FY2025 operating loss / group loss | 20,920 / 60,350 (incl. 41,550 FV swing) | $M | FY2025 | FT-verified leak | recalled | T3 | STABLE | L-025/L-026 notes | 04 |
| O03 | OpenAI end-2025 run-rate | >20,000 | $M/yr | 2025-12 | Bloomberg relay | confirmed | T2 | QUARTERLY | L-065 | 02 |
| O04 | OpenAI PB revenue series | 2,000 · 6,000 · 20,000 · 41,300 (2023-2026); FY2024 NI −5,000; FY2026 NI −14,000 | $M | pulled 2026-09-09 | 2025 = run-rate vintage (C-06); 2026 = projection; NI rows T4 | estimated | T2 / T4 | n/a | L-025, L-026, L-024 | 02 (projection block only) |
| O05 | OpenAI burn plan | 2026 25,000 (Feb) / 27,000 (post-April); 2027 57,000 / 63,000; 2030 +39,000; end-2025 cash ~40,000; Q1-2026 burn 3,700 | $M | 2026-02 / 2026 | two vintages; cash basis | estimated | T3 | QUARTERLY | L-082, L-142 | 05 |
| O06 | OpenAI training budget | 25,000 · 60,000 · 112,000 · 120,000 (2026-2029) | $M/yr | undated | annual budget (C-11) | recalled | T4 | STABLE | L-125 | 03, 04 |
| O07 | OpenAI inference cost / GM | 8,400 (2025) · 14,100 (2026E); GM 33% (2025) vs 46% plan | $M / % | 2025 / 2026E | Sacra | estimated | T3 | QUARTERLY | L-083 | 03, 04, 11 |
| O08 | OpenAI headcount | 4,500 (2026-03-21); plan 8,000 end-2026 | people | 2026-03 | PB / Semafor | confirmed / estimated | T2 / T3 | QUARTERLY | L-027, L-090 | 03 (L5) |
| O09 | Retention bonuses | ~1.5 per person × ~1,000, >1,500 total over 2 yrs | $M | 2025-08 | The Information relay | estimated | T3 | STABLE | L-093 | 03 (L5) |
| O10 | OpenAI debt | 4,000 + 700 + 520 = 5,220 | $M | 2026-07-08 | facilities | confirmed | T2 | STABLE | L-023 | 05 |
| O11 | Microsoft terms | rev share through 2030 at same % subject to cap; cap 38,000 (T3); stake below 27%; RPO 678,000 (+25% ex-OpenAI); Azure 250,000 could-not-verify | mixed | 2026-04-27 / 2026-05-11 / 2026-06-30 | official / single-outlet / 10-K / CNV | mixed | T1 / T3 / T1 / T4 | STABLE | L-051, L-052, L-054, L-055, L-121 | 09, 10 |
| O12 | Users / ads | >1B active users; >2M businesses; ads run-rate 1,000 | users / $M | 2026-07-31 / 2026-08-31 | company / Digiday | confirmed | T2 | QUARTERLY | L-080, L-081 | 03 (context) |
| C01-C22 | Contract schedule rows (both companies) | see `09_Obligations` schedule in §3.9 | | | | | | | L-046, L-048, L-072-L-074, L-076, L-135-L-137, L-044, L-045, L-043, L-049, L-073, L-064, L-058, L-149, L-061, L-060, L-050, L-075, L-079, L-121-L-123 | 09 |
| F01-F09 | Financing ladder rows | see §3.10 | | | | | | | L-044, L-059, L-061, L-106, L-137, L-146, L-147, L-148, L-145, L-095, L-075 | 10 |
| Q01-Q18 | AIBQ prior sub-scores and new sub-scores | see `analysis/aibq-delta.md` | | May-27 / Sep-9 | rubric v3.0 | recalled / derived | T4 | PERMANENT (method) | L-133 | 11 |
| X01 | Neocloud lease economics | Nscale 16.3; Volta 12.5; Riot 2.4; Core Scientific-AMD 1.76; TPU SPV chips-only 6.9 | $M per MW-yr | 2026-08 | derived | estimated | T3 / T1 | VOLATILE | L-134, L-136, L-148, L-044 | 09 (SW_TPU_RATE), 07 |
| X02 | Broadcom TPU/XPU schedules | Anthropic 1 GW 2026, +5 GW 2027, +10 GW 2028; OpenAI 1.3 GW 2027, >5 GW 2028 | GW | 2026-09-02 | vendor call | confirmed | T1 | STABLE | L-049, L-050 | 09 |
| X03 | Reference / industry | Broadcom AI revenue 58,000 / 115,000 / 230,000 (FY26-28); Microsoft CY2026 capex ~175,000; Meta 125,000-145,000; C&W build 17.6 per MW (+21%); EIA power 6.58-10.10 c/kWh | mixed | 2026 | vendor / company / index / EIA | confirmed | T1 / T2 | QUARTERLY | L-144, L-145, L-095, L-109, L-108 | 13 |
| I01 | IPO status | no public S-1 either (EDGAR 2026-09-09); Anthropic confidential 2026-06-01, expected Oct (PB), mid-Oct reported; OpenAI confidential 2026-06-08, "2027" (CFO), PB Sep stale | status | 2026-09-09 | EDGAR / PB / press | confirmed / estimated | T1 / T2 / T3 | VOLATILE | L-001, L-002, L-003, L-004, L-039, L-040, L-068 | 08, 12 (SW_IPO_OAI) |

Do NOT enter (retired rows, listed so nobody re-adds them): L-011 / L-026 net income −42,000 (C-04); L-124 capex 190,000; L-121 / L-122 / L-123 values as facts (enter only in the tally block flagged CNV); the Jul-16 "Fast Mode 3x cheaper"; $161,254 Total Raised; $47.16B xAI pre-merger; any WSJ Apr-6 breakeven year.

---

## 3. Workbook A calculations, tab by tab (formulas in words)

### 3.1 `00_Assumptions`
- Row 3: years 2023A-2030E in D:K. C4 `SW_SCEN` = 1/2/3. Every AJ driver below has three columns (Bear/Base/Bull) and a live column = CHOOSE(SW_SCEN, Bear, Base, Bull).
- AJ drivers (yellow): Anthropic monthly run-rate ramp shape H2-2026 (linear to YE expectation low / mid / high: 100,000 / 110,000 / 120,000; Bear = flat from July); Anthropic 2027E revenue (Bear 120,000 / Base 145,000 / Bull 170,000; AJ interpolation, no row); Anthropic 2029E-2030E revenue growth (Bear +30% / Base +45% / Bull +60% YoY, AJ); Anthropic GM 2026 (44 / 52 / 60), 2029E-2030E GM (Bear 65 / Base 72 / Bull 77, AJ); Anthropic training 2029E-2030E (Bear 40,000 / Base 30,000 / Bull 25,000, AJ); Anthropic quarterly opex Q2-2026 for the GM cross-check (3,000 / 4,000 / 5,000); Anthropic average loaded cash comp per head (0.75 / 0.60 / 0.50 $M); Azure term (5 yrs, AJ); Lambda term (6 yrs, AJ); SpaceX ramp discount May-Jun 2026 (0.9 factor, AJ); Google TPU $/MW-yr proxy (via SW_TPU_RATE); OpenAI H2-2026 monthly growth (Bear 0% / Base 10% / Bull 20%); OpenAI 2027-2030 revenue CAGR (40 / 70 / 100%); OpenAI compute plan (900,000 / 750,000 / 600,000: Bear is the higher spend); OpenAI 2027-2030 opex ex-compute as % of revenue (Bear 40 / Base 30 / Bull 20, AJ); OpenAI 2030E training (Bear 120,000 / Base 90,000 / Bull 60,000; AJ, no row); SBC as % of operating loss for the burn bridge (AJ 25 / 20 / 15).
- A40:F60: the printed 5-Layer definition and placement rule (text from `analysis/cost-stack-reconciliation.md` §1), the source of E2.

### 3.2 `02_Revenue`
- Block A (A5:K30) ladders: Anthropic run-rate ladder A01 by date; OpenAI ladder (O03 end-2025, "~2,000 monthly at March" from L-063, LB02 July, +35% QTD Aug-19 from L-069 as text); recognized quarterly (A03, LB05a; LB06a); annual recognized (A05, A06 via SW_A_FY25; O01); PB forward block in its own rows, header "PB FORWARD PROJECTION (Ruling 4), never current".
- FY2026E integration, Anthropic: Q3 = July monthly (LB01/12) + Aug + Sep on the linear ramp to the YE expectation chosen by SW_SCEN; Q4 likewise; FY2026E = A03 + LB05a + Q3 + Q4. Check cell: must reproduce 57,850 / 62,850 (YE 100,000 / 120,000) and 49,100 (flat).
- FY2026E integration, OpenAI: monthly from LB02/12 compounding at the H2 growth driver; FY2026E = 5,700 + 6,700 + Q3 + Q4. Check: 32,400 / 38,119 / 45,500 at 0 / 10 / 20%.
- Gross → net rows (A35:H50): Anthropic net = gross × (1 − SW_HAIRCUT); OpenAI net = IF(SW_OAI_BASIS = "NET", LB02, LB02 × (1 − R03)) with R03 flagged T4. Both bases printed side by side in every exhibit that uses a net figure.
- Q2 comparison row: Anthropic Q2 net at both haircuts vs OpenAI Q2.

### 3.3 `03_Costs` (the 5-Layer stack, consumption layers)
- L3 rows: A08 / O06 by year; 2029E-2030E from AJ drivers; per-run reference block (L-115: 500 Grok 4; ~200 GPT-4.5 pre-train; 2.4x/yr) printed beside, never summed. Basis label in column C reads "annual budget (C-11)".
- L4 rows: Anthropic COGS = revenue (from `02_Revenue`, gross) × (1 − GM path A07 / AJ). OpenAI: 2025 total COGS = O01 × (1 − 33%); inference 2025-2026 from O07; 2027E+ = AJ % of revenue path (Bear 50 / Base 40 / Bull 30, declining, yellow).
- L5 rows: Anthropic comp = headcount (SW_A_HC) × comp driver; copyright A14 in 2026; data / safety / GTM as AJ lines with the L-113 / L-114 / L-117 / L-118 anchors in column C. OpenAI comp = headcount path (4,500 → 8,000 linear 2026, then AJ +20%/yr) × comp driver (AJ 0.8 / 0.7 / 0.6 $M); retention O09 split 2025-2026.
- L1-L2 annualized rows: links to `09_Obligations` §3.9 annual columns (no typing).
- The $50B split block: LB07a − O06(2026) − O07(2026) = 10,900 "unexplained" printed as a check, not allocated.
- Q2 GM cross-check grid (A45:K60 with `04_PL` A30:H40): rows opex 3,000 / 4,000 / 5,000; columns basis GROSS / NET-39.75 / NET-27; cell = (LB05b + opex) / Q2 revenue on that basis. Check: 31% / 51% at 3,000 gross / net-39.75.
- Unit-economics block: list prices A18 (display); no $/token COGS (L-116: none disclosed), cell reads "HOLE".

### 3.4 `04_PL`
- Both companies, D:K: revenue (gross and net rows for Anthropic), COGS (L4), gross profit, GM%, training (L3), other opex (L5), operating result excl-training and incl-training. 2023A-2025A cells link to the few ledger facts (A05, A06, O01, O02, LB06) and otherwise read HOLE. 2026E: Anthropic Q2 actual block (LB05a, LB05b) with H1 recognized ≈ 16,600 (A03 + LB05a); OpenAI H1 block (LB06a, LB06b).
- No breakeven-year cells. A note row: "WSJ Apr-6 dual-P&L breakevens not carried (no ledger row; argument-map AM-32)".

### 3.5 `05_Cash_Fund`
- Capitalization: Anthropic equity rounds (L-018, L-017, L-016, L-015 totals reproduce LB03), revolver A11, contingent inflows A17 (shown, not added), lease SPV A12 and project debt A13 in a separate "off-balance-sheet obligations" block toggled for display by SW_TOTAL_RAISED_VIEW; identity check LB03 + 2,500 = 126,754 (L-006). OpenAI: equity rounds reproduce LB04; debt O10; identity LB04 + 5,220 = 186,436.5 (L-021).
- CE (Ruling 1): numerator from `02_Revenue` net rows; denominator LB03 / LB04 only. Cells: Anthropic CE gross (display-only, red text "forbidden basis"), CE at SW_HAIRCUT, CE at the other haircut; OpenAI CE at SW_OAI_BASIS; ratio. Check: 0.315 / 0.382 / 0.523 and 0.221 → 1.43x / 1.73x / 2.37x.
- CE walk (A40:H55): Jul-16 (47,000 gross → 28,318 net; 25,000; 0.228 / 0.138 / 1.65x, all from L-133 recalled T4) → Sep-9 rows above.
- Burn walk: OpenAI O05 both vintages; bridge from operating loss (LB06b annualized) to burn = operating loss − SBC (AJ %) − vendor financing / prepayment timing (plug, yellow, labelled HOLE). Anthropic: C-12 block (SW_A_2026_LOSS) showing branch A (−11,000 GAAP loss, L-120) and branch B (Q2 operating profit trajectory, L-034); no plug.

### 3.6 `06_Valuation`
- Marks M01, M02; multiples: M01 / LB01 (gross, display), M01 / net at each haircut, M02 / LB02 (and gross case). Check: 14.8x / 24.6x / 20.3x; 21.3x / 26.6x. Jul-16 reference row 34.1x / 34.1x (L-133).
- $/AIBQ-point ladder (A25:F32): M01 / composite(new) and M02 / composite(new) from `11_AIBQ`; old row at 8.20 / 4.53. Check: 119 / 175 ($B per point); spread 1.47x (old 1.60x). No cell computes any correlation; sheet-level note: "Ruling 2: correlation embargoed".

### 3.7 `07_Sensitivity` (§6 grids)

### 3.8 `08_Output`
- E1 table (A1:H14): mark, equity raised, run-rate (basis tag), Q2 revenue, Q2 operating result, FY2026E derived range, documented-$ contracts (from `09_Obligations` totals), unpriced GW, IPO status (I01), both companies.
- Ten load-bearing figures with as-of and tier (names LB01-LB10). Verdict flags: §5 envelope gap at Base; relative multiple sign at each haircut; AIBQ composites.

### 3.9 `09_Obligations`
- Contract schedule (A100:N130), one row per commitment with: ID, company, counterparty, layer, start (date), end (date), term (yrs), total ($M, blank if unpriced), annual value ($M = total / term, or explicit monthly × 12), GW/MW, cancellability (text + flag: FULL 90-day / OPTION / MILESTONE / NONE-DISCLOSED), backstop (text), tier, row. Rows: A-AWS (L-072: 100,000 / 10 / 2026-2036), A-Azure (L-074: 30,000 / AJ 5 yrs), A-SpaceX (L-046: 1,250 × months; 2026 = 7 months × 0.9 ramp; 2027-2028 = 15,000; 2029 = 6,250; flag FULL 90-day), A-Fluidstack (L-076: 50,000; phasing HOLE; not in annual run), A-Nscale (L-135: 45,000 / 6 from late-2027: 2027 = 25% year), A-Lambda (L-137: 35,000 / AJ 6 yrs from 2027), A-Volta (L-048: 10,000 / 6 from H2-2026), A-Riot (L-136: 9,100 / 20 from 2028 AJ start; options 7,000 flagged OPTION), A-TPU-SPV (L-044: 34,500 / 5 from mid-2026; layer L1), A-Google-TPU (L-073, L-049: GW only; $ = GW × SW_TPU_RATE × 1,000, shown in the "unpriced proxy" column, never in documented-$), A-AMD (L-043: 2 GW from 2027; $ HOLE; equity 5,000 contingent in the inflow block), O-Oracle (L-064: 300,000 / 5 from 2027), O-AWS (L-064: 138,000 / 8 from 2026), O-CoreWeave (L-058: 22,400 / 6 to 2031; T1 tranche 6,500 noted), O-Cerebras (L-149: 20,000 / 4 from 2026; option 1.25 GW flagged OPTION), O-Azure (L-121: 250,000 CNV, flagged; annual = LB08 run 24,100 held flat as the priced proxy), O-SBE-PORTS (L-061: 8.0 GW-IT, 20 yrs from 2028; rent HOLE; proxy = 105,000 / 4.25 × 8.0 = 197,647 total value shown as proxy only), O-SBE-Milam (L-061: 753 MW, 15 yrs), O-AMD (L-060: 6 GW; 90,000 CNV flagged; MILESTONE), O-Broadcom (L-050: 1.3 GW 2027, >5 GW 2028; 350,000 CNV flagged), O-Nvidia (L-075: retired LOI; 30,000 equity inflow; RVG 105,000 in backstop column), O-Stargate (L-079: >9 GW; overlaps; excluded from sums).
- Contracted / cash / cancellable tables (A5:J20 Anthropic; A25:J40 OpenAI) are formulas over the schedule (SUMIFS by company and flag). Totals must reproduce: Anthropic documented-$ 324,100 (excl. SPV) and 358,600 (incl.); OpenAI documented-$ 480,400; recalled-$ 690,000; cancellable Anthropic ≈ 48,000 (SpaceX beyond 90 days + Riot options).
- Tally reconciliation (A45:H58): the L-062 / L-078 / L-082 / L-138 scopes with their component sums as formulas (Bloomberg 175,000 = Lambda + Nscale + Fluidstack + SpaceX-max; stepmark 99,100; TechCrunch 61,250 flagged "mixes equity").
- Annualized priced run by year (A60:K75): SUMIFS over the schedule by year and company, split L1 / L2; must reproduce Anthropic 2026 ≈ 28,158 (incl. SPV half-year) / 2027 ≈ 47,730 / 2028 ≈ 53,355 / 2029 ≈ 44,605 / 2030 ≈ 38,355 at the stated AJ terms; OpenAI 2027 ≈ 110,083.
- Envelope chart data (A80:K95): Anthropic COGS + training envelope by year from `03_Costs`; priced run from above; unpriced proxy = (Google unpriced GW by year: 2026 0 (the ~1 GW Ironwood sits inside the SPV), 2027 5 (contracted tranche, L-073/L-049), 2028 = SW_GW_2028 (5 = contracted tranche only / 15 = plus Broadcom's 10 GW line of sight, L-049)) × SW_TPU_RATE × 1,000 + AMD (2 GW from 2027 at the same rate, AJ). Gap row = envelope − priced − proxy. Check at Base (SW_TPU_RATE = 9.3, SW_GW_2028 = 5): 2028 gap ≈ −33,000; at SW_GW_2028 = 15: ≈ −126,000; at SW_TPU_RATE = 12.5 the two gaps are ≈ −49,000 and ≈ −174,000.

### 3.10 `10_Financing`
- Ladder rows F01-F09: instrument, lab, rate or terms, risk holder, row, tier (from `analysis/cost-stack-reconciliation.md` §6). Spread cell = 9.0-9.75% neocloud (L-059) minus 5.75% SPV A2 (L-044) = 325-400 bp; annual value on 34,500 = 1,121-1,380 (formula). Backstop register: Nvidia RVG 105,000 (L-061), Nvidia Lambda lease (L-137), Broadcom/Google SPV support 30,000 (L-044), Google project-debt support (L-045), AMD DC lease guarantees 4,100 and leases 9,500 (L-146), SB Energy warrant charge 2,573 (L-147), Microsoft recap gain 6,500 (L-054), Huang statement (L-075, text).

### 3.11 `11_AIBQ`
- Table exactly as `analysis/aibq-delta.md` §1-§4: sub-score, weight, old, new, rubric band text, rows, type, Δ raw, Δ dim = weight × Δ raw, flag (≥0.5). Dimension = SUMPRODUCT(weights, new). Composite Δ = 0.20 × ΔCE + 0.15 × ΔCI. New composite = canonical old (8.20 / 4.53) + Δ. Checks: Anthropic CE 7.30, CI 5.55, composite 8.13 (8.02 on the CI-5.8 base, shown); OpenAI CE 3.925, CI 5.60, composite 4.87 (4.79 gross case via SW_OAI_BASIS, which drives CE-1 = 5.0 / 4.0). Efficiency Index cells: Anthropic 0.55; OpenAI 0.50.

### 3.12 `12_Conflicts` (§5 below)

### 3.13 `13_OutsideView`
- One row per forecast: forecast, reference class, base rate, base-rate source (row or "AJ"), what is different here, magnitude, direction. Rows per `analysis/outline-v5.md` §10 and `writer-brief.md` §10.

---

## 4. Scenario definitions (Bear / Base / Bull), applied through `SW_SCEN`

| Driver | Bear | Base | Bull | Anchor |
|---|---|---|---|---|
| Anthropic YE-2026 run-rate | flat from July (65,000) | 110,000 | 120,000 | L-032, L-035 (T3) |
| Anthropic 2027E revenue | 120,000 | 145,000 | 170,000 | AJ (between L-035 and L-036) |
| Anthropic 2028E revenue | 150,000 | 190,000 | 200,000 | L-036 (T2); Bear is an AJ shortfall |
| Anthropic GM 2026 / 2027 / 2028 | 44 / 55 / 60 | 52 / 63 / 70 | 60 / 63 / 77 | L-119 (T4); Base 2028 is BELOW the 77% plan on purpose (the §5 finding); Bull = plan |
| Anthropic training 2026-2028 | 7,000 / 14,000 / 22,000 (plan) plus 25% | plan | plan less 15% | L-125 (T4) |
| Google TPU $/MW-yr proxy | 16.3 | 9.3 | 6.9 (chips only, shell inside AWS/other) | L-134, L-044, L-136 |
| OpenAI H2-2026 monthly growth | 0% | 10% | 20% | L-065 (July >20%) |
| OpenAI 2027-2030 revenue CAGR | 40% | 70% | 100% | AJ; L-069 (+35% QTD) as colour |
| OpenAI compute plan 2026-2030 | 900,000 | 750,000 | 600,000 | L-062, L-078 |
| OpenAI other opex % revenue | 40% | 30% | 20% | AJ (L-066 H1 ratio as ceiling) |
| Haircut | switch, not scenario (SW_HAIRCUT) | 39.75% | | Ruling 5 |

Base case rationale (print on `00_Assumptions`): 39.75% because Ruling 5 is gate-verified on the May-2026 mix and binds; Base 2028 GM 70% rather than 77% because both labs missed GM plans in every observed case (L-083, L-119) and the §5 envelope does not close at 77%; Base OpenAI compute plan 750,000 because it is the latest company-attributed vintage (L-062).

---

## 5. Frozen-conflict switch cells (`12_Conflicts`, column C, named ranges)

| Cell | Name | Conflict | Branch values | Default | Cells gated |
|---|---|---|---|---|---|
| C5 | SW_HAIRCUT | C-13 | 0.3975 / 0.27 (also 0.33 for grids) | 0.3975 | `02_Revenue` net rows; `05_Cash_Fund` CE; `06_Valuation` multiples; `11_AIBQ` CE-1 ratio; `07_Sensitivity` grid (a) |
| C6 | SW_OAI_BASIS | C-16 | "NET" / "GROSS" | NET | `02_Revenue` OpenAI net row (GROSS applies R03 = 20%, T4, flagged); `06_Valuation`; `11_AIBQ` CE-1 (5.0 / 4.0) |
| C7 | SW_IPO_OAI | C-02 (residual) | "Q4-2026" / "2027" | 2027 | `08_Output` IPO status text; `13_OutsideView` milestone row. "Sep-2026" is not a branch: retired by L-002 and the 15-day rule |
| C8 | SW_A_FY25 | C-03 | 10,000 (PB) / 5,250 (midpoint of the implied 4,500-6,000) | 10,000 | `02_Revenue` annual recognized 2025; `03_Costs` L4 2025; `04_PL` 2025 |
| C9 | SW_A_FY24_NI | C-05 | −5,300 / −8,300 | −8,300 (latest PB) | `04_PL` 2024 net result |
| C10 | SW_A_2026_LOSS | C-12 | "GAAP −11,000 (Jan plan)" / "Op-profit trajectory (Q2 print)" | Q2 print | `05_Cash_Fund` Anthropic 2026 burn block; `04_PL` 2026 note row |
| C11 | SW_A_HC | C-18 | 5,000 / 4,020 | 5,000 | `03_Costs` L5 comp |
| C12 | SW_TPU_RATE | (proxy choice, not a conflict) | 6.9 / 9.3 / 12.5 / 16.3 $M per MW-yr | 9.3 | `09_Obligations` unpriced proxy; E10 band |
| C16 | SW_GW_2028 | (scope choice: contracted vs line of sight, L-049) | 5 / 15 GW unpriced in 2028 | 5 | `09_Obligations` unpriced proxy; E10 band; grid (b) |
| C13 | SW_TOTAL_RAISED_VIEW | C-01 | "On-balance-sheet (126,754)" / "Incl. lease SPV (161,254)" | On-balance-sheet | `05_Cash_Fund` capitalization display block only; CE never changes (Ruling 1) |
| C14 | SW_15B_FACILITY | (L-042 not closed) | "Closes" / "Does not close" | Closes | `05_Cash_Fund` facilities; `11_AIBQ` CE-4 (7.0 / 8.0) |
| C15 | SW_SSI | C-08 | 7,000 (PB) / 8,000 (press) | 7,000 | Workbook B `08_Reference` (mirrored) |
| (display) | C-15 | secondary marks | 1,500,000 / ~800,000 (both T4) | none adopted | `06_Valuation` note cell only; no formula reads it |

Resolved conflicts listed on the same tab with their resolution text: C-01, C-04, C-06, C-07, C-09, C-10, C-11, C-14, C-17, C-19, C-20, O-15.

---

## 6. Sensitivity grids (`07_Sensitivity`)

(a) A5:H20 **Basis grid.** Rows: haircut 27% / 33% / 39.75%. Columns: OpenAI basis NET / GROSS (20% T4). Cells: Anthropic equalized multiple, OpenAI multiple, relative multiple (Anthropic ÷ OpenAI − 1), CE ratio. Expected corners: (39.75%, NET) 24.6x vs 21.3x, +15%, 1.43x; (27%, NET) 20.3x vs 21.3x, −5%, 1.73x; (39.75%, GROSS) 24.6x vs 26.6x, −7%, 1.78x.

(b) A25:H40 **Anthropic envelope grid (2028E).** Rows: revenue 150,000 / 175,000 / 200,000. Columns: GM 60% / 70% / 77%. Cell = revenue × (1 − GM) + training 22,000 − priced run 53,355 − unpriced proxy at SW_TPU_RATE × SW_GW_2028. Negative = the plan does not cover the commitments. Print a second panel with training at 30,000.

(c) A45:H60 **OpenAI 2030 cash-flow sign.** Rows: 2027-2030 revenue CAGR 40 / 70 / 100%. Columns: compute plan 600,000 / 750,000 / 900,000 (2027-2030 spend = plan − 50,000, phased AJ 15 / 22 / 28 / 35%). Cell = 2030E revenue − 2030E compute − other opex (% driver) ; sign and magnitude. Note row: The Information's own 2030 figure is +39,000 (L-082, T3, Feb vintage).

---

## 7. Workbook B: `Greenfield_Entry_Cost_v5.xlsx`

### 7.1 Tabs
`00_Assumptions` (scenario switch `SW_GF` C4: 1 Lean fast-follower / 2 Full frontier / 3 Vertically integrated with custom silicon; timeline Y1-Y5 in D:H, AJ drivers with ranges) · `01_Data` (greenfield anchors, §7.2) · `02_Compute` (chips by SKU and count; buy vs lease; financing) · `03_Facility` (power MW, $/MWh, utilization; cooling; build vs colocation by region; network; storage) · `04_Training` (runs by generation; compute-hours × cost; runs to a frontier result; failed-run allowance) · `05_Inference` (serving cost per million tokens at stated utilization; vs list) · `06_People_Other` (R&E headcount by band with comp; data licensing and labeling; safety/eval; legal/regulatory; GTM and G&A) · `07_Cash` (time-phased five years; cumulative; milestone triggers) · `08_Reference` (xAI, SSI, Thinking Machines, Reflection, Mistral, Periodic, Humans&, Meta) · `09_Output` (E18).

### 7.2 Inputs (`01_Data`), with anchors

| ID | Item | Value / range | Unit | Row · status · tier | Note |
|---|---|---|---|---|---|
| G01 | GPU purchase price by SKU | H100 new 25,000-40,000 (used 8,200-25,000); B200 30,000-40,000; DGX B200 (8) 300,000-500,000; GB200 NVL72 rack 2.0-3.0M (= 27,800-41,700 per GPU); GB300 NVL72 rack 3.0-4.0M (= 41,700-55,600 per GPU); DGX B300 ~400,000; B200 manufacturing cost ~6,400 | $ | L-103 · estimated · T4 | Index/channel figures; use ranges |
| G02 | GPU-hour on-demand | CoreWeave H100 6.16, H200 6.31, B200 8.60, GB200 10.50 per GPU; Lambda B200 6.69-6.99, H100 3.99; Nebius H100 3.85, H200 4.50, B200 7.15, B300 7.85; reserved up to 60% (CoreWeave) / 35% (Nebius) off; preemptible 44-55% off | $ per GPU-hr | L-104 · confirmed · T1 · 2026-09-09 | |
| G03 | GPU-hour contracted large cluster | B200 neocloud p25 2.40; hyperscaler p50 3.10; GB300 example 4.00 (5,184 GPUs); hyperscaler TCO 1.10-1.61x gold-tier neocloud; support 3-10% of bill | $ per GPU-hr | L-105 · estimated · T3 | The lease hinge |
| G04 | Cost of debt | neocloud unsecured 9.00 / 9.75 / 9.625% (2031-2032); vendor-backstopped SPV T+1pt / 5.75% / 8.5%; OEM equipment financing exists (rate not stated: AJ 7-8%) | % | L-059 · T1; L-106 · T1; L-044 · T3 | |
| G05 | Power per GPU | ~1.5 MW facility per 1,000 H100-class; ~2.0-2.2 MW per 1,000 GB200-class (rack 120-132 kW, ~1.2 kW per GPU) | MW | L-107 · estimated · T3 | Overhead (PUE) embedded |
| G06 | Electricity price | Texas 65.8; Washington 72.0; Arizona 77.3; Wyoming 87.5; Georgia 88.6; US industrial 91.7; Virginia 93.1; Ohio 98.9; Pennsylvania 101.0 | $ per MWh | L-108 · confirmed · T1 · Jun-2026 | Large-load tariffs differ; use as band |
| G07 | Utilization | training clusters 70-85%; inference 40-70% | % | AJ (no row) | yellow |
| G08 | Datacenter build | all-in greenfield 17.6M per MW (+21% since Q4-2024); AI-dense >20M (T4); shell-and-core 11.3M (JLL, T4); liquid-cooled infra 4.5-5.2M vs ~1.8M air per MW (T4); DLC premium 2,500-4,500 per kW (T4); powered land 584,000 per MW; power infra 21% of cost | $ | L-109 · confirmed · T2 | |
| G09 | Build lead time | 24-36 months greenfield; 9-18 months colocation fit-out | months | AJ (no row) | yellow |
| G10 | Colocation / powered shell | wholesale ~100-150 per kW-month triple-net; Core Scientific-AMD ≈ 147 per kW-month (= 1.76M per MW-yr, 2.5% escalators, 15 yrs); Riot ≈ 2.4M per MW-yr (20 yrs); retail 180-400 (T4) | $ per kW-month; $M per MW-yr | L-110 · T3; L-148 · T1; L-136 · T2 | |
| G11 | Full-stack GPU lease | Nscale ≈ 16.3M; Volta ≈ 12.5M per MW-yr (Vera Rubin vintage) | $M per MW-yr | L-134 · estimated · T3 (derived) | |
| G12 | Network fabric | 3-15% of GPU hardware cost at 1,024 GPUs (8.0% B200 BOM; 5.8% GB300; 21.2% MI300X); InfiniBand ~4,000 per GPU vs Ethernet 800-2,500 (T4) | % / $ per GPU | L-111 · estimated · T3 | Vendor-adjacent source |
| G13 | Storage | 2-5% of cluster capex; nodes 60,000-100,000 each, 4-8 per medium cluster; managed parallel FS 0.50-1.00 per GB-month | % / $ | L-112 · could-not-verify · T4 | FLAGGED; yellow |
| G14 | Training run cost (final run, compute) | GPT-4 ~78; Gemini Ultra ~191; Llama 3.1-405B ~170; Grok 4 ~500; GPT-4.5 ~200 pre-train + ~2 post; growth 2.4x/yr; >1,000 by 2027; cost shares: hardware 47-67%, R&D staff 29-49%, energy 2-6% | $M | L-115 · estimated · T3 | |
| G15 | Incumbent annual training budgets | Anthropic 7,000 / 14,000 / 22,000; OpenAI 25,000 / 60,000 / 112,000 / 120,000 | $M/yr | L-125 · recalled · T4 | Ceiling for scenario 2 |
| G16 | Runs to a frontier result | 2-4 full-scale runs per generation plus experiments; total development compute = 3-5x final-run compute | multiple | AJ (Epoch cost-share structure as colour, L-115) | yellow |
| G17 | Failed-run allowance | 30-50% of final-run compute per generation | % | AJ (no row) | yellow |
| G18 | Inference cost proxies | OpenAI inference 8,400 on 13,100 revenue (64%, 2025) → 14,100 (2026E); custom XPU "half the cost of a GPU" (vendor); Fable 5.1 −25-45% cost per task (vendor); no $/M-token COGS disclosure exists | mixed | L-083 · T3; L-050 · T1; L-085 · T1; L-116 | |
| G19 | List prices | Fable 5.1 10 / 50; Opus 5 5 / 25; Sonnet 5 2 / 10; Haiku 4.5 1 / 5; cache read 0.25-0.50; batch −50%; Fast Mode 2x | $ per MTok | L-084 · confirmed · T1 | Revenue-side ceiling |
| G20 | Tokens per GPU-hour at utilization | AJ by model class (no row): flag; model serving cost per MTok = (GPU-hr cost ÷ tokens per GPU-hr) × 1,000,000 | tokens | AJ | yellow; the Writer must not print a $/MTok COGS as fact |
| G21 | Researcher comp bands | top-decile leaders: 25-100M per year over 4 yrs at the extreme (Meta: "$100M over four years not inconceivable"; up to $300M/4 yrs reported); senior IC total comp 0.5-1.5M (T4); MTS base 1.12-1.38M (Anthropic H-1B); engineers total comp 0.30-0.76M (T4); other functions 0.23-0.50M | $M/yr | L-094 · T2; L-092 · T3 | |
| G22 | Retention | ~1.5M per person × ~1,000 over 2 yrs (>1,500 total) | $M | L-093 · estimated · T3 | |
| G23 | Data licensing | marquee text sources ~50-70 per source-year (Reddit $203M aggregate, 2-3 yrs; News Corp up to 250 over 5 yrs); ~20 publisher deals at OpenAI | $M | L-113 · confirmed · T1 (Reddit S-1 via TechCrunch) | Low single-digit $B at most |
| G24 | Expert data / labeling | 1-3B per year per lab at scale (Mercor $2B annualized, >90% from a handful of labs; Scale ~$1B; Surge ~$1B) | $M/yr | L-114 · estimated · T4 | |
| G25 | Safety / eval | 55-115 per year (T4 estimate); model as 3-8% of research headcount | $M/yr | L-117 · could-not-verify · T4 | FLAGGED; yellow |
| G26 | Legal / regulatory | copyright: Anthropic settlement 1,500 paid; music demands >3,000; NYT v. OpenAI pending, no figure; reserve AJ 500-1,500 over 5 yrs; compliance/policy AJ 20-50 per year | $M | L-086 · T2; L-088 · T4; AJ | |
| G27 | GTM and G&A | incumbent workforce mix Finance/Ops 34.9%, S&M 34.8%, Engineering 30.3% (T4); Lean AJ 20% of headcount; scenarios 2-3 AJ 40-60% | % | L-118 · estimated · T4 | |
| G28 | Custom-silicon supply | Broadcom AI revenue 58,000 (FY26) → 115,000 (FY27, supply secured) → 230,000 (FY28, line of sight); six XPU customers; entrant access AJ: none before 2029 | $M | L-144 · confirmed · T1 | Scenario 3 constraint |
| G29 | Custom ASIC program cost | NRE and team AJ 1,000-3,000 per year for 3-4 years to first GA; first-silicon risk allowance 30% | $M/yr | AJ (no row) | yellow |
| G30 | Reference class | see §7.5 | | L-096-L-102, L-047, L-094, L-095 | |

### 7.3 Scenario definitions (`00_Assumptions`, `SW_GF`), five years Y1-Y5

| Line item | 1 Lean fast-follower | 2 Full frontier | 3 Vertically integrated with custom silicon |
|---|---|---|---|
| Compute model | Lease contracted capacity from neoclouds (G03) | Lease at scale plus purchased clusters from Y2 (G01, G03); GPU-backed financing at G04 unsecured rates | Own 1 GW-IT by Y4 (G05: ~476,000 GB200-class GPUs at 2.1 MW per 1,000); custom ASIC program from Y1 (G29); merchant GPUs until ASIC GA (G28: no custom supply before 2029) |
| Chips by SKU and count (AJ, yellow) | 25,000-50,000 GPU-equivalents (B200/GB200) leased; Y1 25,000 → Y3 50,000 | 100,000 (Y1, leased) → 250,000 (Y3, half purchased GB300 at G01 rack price ÷ 72) → 400,000 (Y5) | 50,000 leased Y1; 240,000 purchased Y2 (500 MW); 476,000 by Y4 (1 GW); ASIC replaces 30% of merchant GPUs from Y5 at "half the cost" (G18 vendor claim, flagged) |
| Buy vs lease and financing | 100% lease at G03 (2.40-4.00 per GPU-hr) at G07 utilization; no debt | 50% purchased from Y2, financed 60% debt at G04 9.0-9.75% (unsecured) or 5.75% if a vendor backstop is obtained (switch `SW_GF_BACKSTOP`) | 80% purchased; project debt at G04 SPV rates if backstopped, else neocloud rates; equipment financing AJ 7-8% |
| Power | inside lease | inside lease for leased share; owned share: MW = GPUs × G05; $/MWh by region switch `SW_GF_REGION` (Texas / Virginia / Ohio / Norway AJ 40-60) | 1 GW × 8,760 h × G07 × $/MWh (Base Texas 65.8): 403-619 per year |
| Cooling and DC | inside lease | colocation powered shell at G10 (1.76-2.4M per MW-yr) for owned clusters; liquid-cooling premium inside | greenfield build at G08 17.6M per MW (AI-dense sensitivity 20M): 1 GW = 17,600-20,000 over Y1-Y4 (G09 lead time 24-36 months); DLC inside the all-in figure |
| Network | inside lease | G12: 8% of purchased GPU BOM | G12: 5.8-8% of GPU BOM ≈ 1,000-1,700 for 1 GW |
| Storage | inside lease | G13: 2-5% of cluster capex (flagged) | G13 ≈ 500 for 1 GW (flagged) |
| Training runs by generation | 1 frontier-class final run per year at G14 (500 in Y1, ×2.4/yr: 1,200 Y2, 2,900 Y3...) capped by cluster size; development multiple G16 low end (3x); failed-run allowance G17 30% | 2-3 generations over 5 years; annual training budget rising from 1,500 (Y1) to the Anthropic-2026 level 7,000 (Y3) and 14,000 (Y5) (G15 as ceiling); G16 4x; G17 40% | as scenario 2 for budget; compute-hours priced at owned-cost (depreciation 3 yrs AJ + power) rather than lease |
| Inference serving | cost per MTok from G20 at G07 40-70% utilization; revenue at G19 list less AJ 30-50% discounting; inference cost as % of revenue path 64% (Y1, G18 anchor) → 45% (Y3) → 35% (Y5) AJ | same path; 64% → 40% → 30% | same, with ASIC "half cost" from Y5 (flagged vendor claim) |
| R&E headcount by band | 100 (Y1) → 300 (Y5); 10% leaders at 5-25M, 40% senior IC at 0.5-1.5M, 50% engineers at 0.3-0.76M (G21) → ≈ 180-450 per year | 500 → 3,000; same bands; retention pool G22 from Y3 (≈ 750 per year) | 800 → 4,000 incl. DC ops and silicon team; ASIC team inside G29 |
| Data licensing and labeling | G23 50-200 per year; G24 100-300 | G23 300-1,000; G24 1,000-3,000 by Y3 | as scenario 2 |
| Safety / eval | G25: 3% of research headcount cost | 5% | 5% |
| Legal / regulatory | G26 reserve 100 per year; compliance 20 | reserve 300 per year; compliance 50 | as scenario 2 |
| GTM and G&A | G27 20% of headcount cost | 50% of headcount cost | 50% |

### 7.4 Formulas in words (`07_Cash`)
- Annual cash out (Y) = compute lease (GPUs leased × G03 rate × 8,760 × G07) + purchased chips (count × G01 price per GPU) + network (G12 × chips) + storage (G13 × cluster capex) + DC build or colocation (G08 or G10 × MW) + power (MW × 8,760 × G07 × G06) + training development premium (final-run compute × (G16 − 1) + G17 allowance; note final-run compute is already inside the compute lines, so this line adds only the AJ experiment and failure multiple on the lease/depreciation cost) + people (headcount × band comp) + data (G23 + G24) + safety (G25) + legal (G26) + GTM/G&A (G27) + ASIC program (G29, scenario 3) − revenue (from `05_Inference` at the chosen ramp).
- Debt service where financed: interest at G04 on drawn balance; principal straight-line over 4 years (AJ).
- Cumulative capital (Y) = running sum of annual net cash out plus debt principal outstanding (the equity-plus-debt "entry fee"); print equity-only as a second line (Ruling 1 spirit).
- Milestone triggers (green outputs): (i) first frontier-class model = end of the year the first final run at ≥ the current-year frontier cost (G14 path) completes (Lean Y2; Full Y2; Vertically integrated Y3 because the owned cluster lands Y2-Y3); (ii) first $1B net revenue = first year revenue ≥ 1,000 (Lean Y4 if achieved; Full Y3; Vertically integrated Y4) with an AJ probability column (Lean 30-50%; Full 60-80%; Vertically integrated 60-80%; reference: TML, Mistral, SSI); (iii) cash-flow breakeven = first year net cash out ≤ 0 (Lean: Y5 or never in Bear; Full: beyond Y5 in Base; Vertically integrated: beyond Y5).

Expected magnitudes at Base (the Model agent must reproduce within ±20% and print the ranges): Lean: Y1 1,000-1,500; cumulative to first frontier-class model 2,500-4,000; to $1B net revenue 5,000-8,000; to breakeven 8,000-15,000 or not reached. Full frontier: Y1 4,000-6,000; to first frontier model 12,000-18,000; to $1B net revenue 20,000-30,000; to breakeven 60,000-100,000+. Vertically integrated: Y1 5,000-8,000; Y2 15,000-25,000 (500 MW build 8,800 + 240,000 GPUs ≈ 8,400 + ASIC + people); to first frontier model 25,000-40,000; to $1B net revenue 40,000-60,000; to breakeven 80,000-150,000. Owning 1 GW-IT ≈ 36,400 up front at Base (17,600 build + 16,700 chips + 1,700 network + 500 storage) plus 400-620 per year of power; leasing the same as full-stack capacity ≈ 12,500-16,300 per year (G11); powered shell only ≈ 1,760-2,400 per year (G10). Crossover lease-vs-own at Base ≈ 2.5-3 years of full-stack lease, before residual-value risk (H100 used prices at 33-63% of new, G01).

### 7.5 Reference-class check (`08_Reference`): what entry actually cost

| Entrant | Capital raised / spent | Revenue | Headcount | Valuation | Resembles scenario | Rows · tier |
|---|---|---|---|---|---|---|
| xAI (inside SpaceX) | accumulated deficit 41,311 at 2026-03-31 (consolidated); AI-segment 2025 debt proceeds 16,055; pre-merger raise NOT reproducible (register 47,160 cut) | AI segment 2025 revenue 3,201, loss from operations (6,355); Q1-2026 818 / (2,469); Q2-2026 2,560 (+247%) / (1,260) operating loss; consolidated Q2 capex 18,400 | n/a | acquired at 250,000 (Feb-2026) | 3 (owned Colossus, ~200,000 GPUs, 300 MW phase 2 per L-107) | L-096 · T1; L-047 · T2 |
| SSI | 7,000 raised (PB) / 8,000 (press) incl. Nvidia 5,000 (Jul-2026) [SW_SSI] | zero | 40 | 32,000 | 1 (research-only) | L-097 · T2; C-08 |
| Thinking Machines Lab | 2,000 seed (Jun-2025) at 8,000 pre / 10,000 post (PB; press 12,000, C-09); seeking 1,000 at 40,000 pre (in talks) | "at least a few hundred million" annualized; PB 100 FY2026 projection | ~200 | 10,000-12,000 post (seed) | 1 | L-098 · T2 |
| Reflection AI | 2,155 raised; Series C 2,500 at ~25,000 pre in progress | n/a | ~200 | 8,000 post (Series B) | 1 | L-099 · T2 |
| Mistral AI | 7,492 raised incl. 830 debt; Series D EUR 3,000 (Sep-8-2026) | PB 1,167 FY2026 projection | ~900 | ~24,374 (EUR ~21B post) | 1 → 2 (first French datacenter) | L-100 · T2 |
| Periodic Labs | 300 seed at 1,000 pre; talks at ~7,000 | n/a | 48 | 1,300 post (seed) | 1 | L-101 · T2 |
| Humans& | 480 seed at 4,000 pre / 4,480 post | n/a | 20-30 | 4,480 | 1 | L-102 · T2 |
| Meta Superintelligence Labs | 2026 capex 125,000-145,000 (2025: 72,200); Scale AI 14,300 for 49%; packages to 100M over 4 yrs; 6 GW AMD deal | n/a (inside Meta) | n/a | n/a | 3 (hyperscaler-funded) | L-095 · T2; L-094 · T2; L-060 · T1 |
| Anthropic (incumbent, for scale) | equity 124,254; documented contracts 324,100 | run-rate 65,000 gross; Q2 11,600; first quarterly operating profit | 5,000 | 965,000 | beyond 2 | L-007, L-032, L-033, L-034, L-008, L-005 |
| OpenAI (incumbent, for scale) | equity 181,216.5; documented contracts 480,400 | run-rate >40,000; H1 12,400; H1 operating loss 21,600 | 4,500 → 8,000 | 852,000 | beyond 3 (leases, custom silicon) | L-022, L-065, L-066, L-027, L-019 |

Check rule for `09_Output`: each scenario's cumulative-capital-to-milestone must sit inside the reference band or the output cell prints "OUTSIDE REFERENCE CLASS: explain". Lean must land in the SSI / TML / Reflection / Mistral band (2,000-8,000 to a model with little revenue); Full frontier must land below Anthropic's equity-to-first-profit (124,254 raised; ~12,000-20,000 burned, derived and flagged) and near xAI's accumulated deficit (41,311) by Y4-Y5; Vertically integrated must land at or above xAI's deficit plus its 2025 AI-segment debt (~57,000) by Y5.

---

## 8. Exhibit ↔ tab ↔ range mapping

| Exhibit | Workbook / tab / range | Notes |
|---|---|---|
| E1 | A / 08_Output / A1:H14 | at-a-glance |
| E2 | A / 00_Assumptions / A40:F60 | printed definition |
| E3 | A / 03_Costs / A5:K40 and A / 09_Obligations / A60:K75 | L3-L5 and L1-L2 annualized |
| E4 | A / 02_Revenue / A5:K30 | ladders with PB forward block separate |
| E5 | A / 02_Revenue / A35:H50 and A / 06_Valuation / A5:H20 | restatement |
| E6 | A / 09_Obligations / A5:J20 | Anthropic stack |
| E7 | A / 09_Obligations / A25:J40 | OpenAI stack |
| E8 | A / 09_Obligations / A45:H58 | tallies |
| E9 | A / 03_Costs / A45:K60 and A / 04_PL / A30:H40 | budgets vs runs; $50B split; Q2 GM grid |
| E10 | A / 09_Obligations / A80:K95 | envelope chart data; band via SW_TPU_RATE |
| E11 | A / 10_Financing / A5:H25 | ladder and backstops |
| E12 | A / 01_Data (Microsoft block) and A / 09_Obligations / A25:J26 | Microsoft anchor |
| E13 | A / 05_Cash_Fund / A40:H55 | CE walk |
| E14 | A / 11_AIBQ / A5:L40 | AIBQ delta |
| E15 | A / 06_Valuation / A25:F32 | $/point ladder |
| E16 | A / 13_OutsideView / A5:H30 | base rates |
| E17 | A / 07_Sensitivity / A5:H20, A25:H40, A45:H60 | three grids |
| E18 | B / 07_Cash / A5:H60, B / 08_Reference / A5:J20, B / 09_Output / A1:H25 | greenfield |

---

## 9. Build checks (must pass before hand-off)

1. Identity checks: LB03 + 2,500 = 126,754; LB04 + 5,220 = 186,436.5 (L-006, L-021).
2. Reproduction checks (Base, defaults): Anthropic net run-rate 39,162; multiples 14.8x / 24.6x / 20.3x; OpenAI 21.3x; CE 0.315 / 0.382 / 0.221; ratio 1.43x; FY2026E integrations 57,850 / 62,850 / 49,100 and 32,400 / 38,119 / 45,500; documented-$ 324,100 / 358,600 / 480,400 / 690,000; Bloomberg tally 175,000; annualized Anthropic 2028 priced run ≈ 53,355; OpenAI 2027 priced run ≈ 110,083; AIBQ CE 7.30 / 3.925, CI 5.55 / 5.60, composites 8.13 / 4.87; $/pt 119 / 175; envelope 2028 65,700-68,000.
3. No cell on any timeline tab contains a typed number that also appears on `01_Data` (audit script: every numeric constant outside `00_Assumptions` and `01_Data` must be flagged).
4. Every yellow cell has a Bear/Base/Bull triple and a "AJ" tag in column C.
5. Every net figure has its haircut visible in an adjacent cell; every OpenAI net figure has SW_OAI_BASIS visible.
6. No sheet, name, note or cell computes or references a correlation between AIBQ and valuation (grep the workbook XML for "correl", "r=", "−0.99", "-0.99").
7. No PB TTM field feeds any cell labelled "current"; the projection block is the only home.
8. All 1,000-2,000 formulas evaluate without error under the `formulas` library (container LibreOffice was broken on the Aug-19 build); Bear/Base/Bull sweep and all switch combinations run clean.
9. Workbook B `09_Output` reference-class check prints PASS for all three scenarios or an explanation cell.
10. Sheet names contain no em-dash; cell text contains no em-dash.
