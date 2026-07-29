# Q2 2026 Global Unicorn Tracker - cell-level source map

Audited July 28, 2026 against the latest uploads. Every figure in the report body was
located at cell level and recomputed where derived.

File keys:
- **PT** = Final__Q2_2026__Quarterly_Unicorn_Tracker_HR_Version.xlsx
- **MON** = Unicorn_Monitor_Data_Q2_2026.lighter.hr_version.xlsx
- **MON-FULL** = Unicorn_Monitor_Data_Q2_2026.Full_Version.xlsx (raw tabs; same data vintage as MON)
- **U20** = Morningstar_PitchBook_Unicorn_20_Valuations_and_Pricing_Data_h_version.xlsx
  (daily Morningstar model prices; MON Top20_Marks joins them via Names_Map)
- **PANEL** = AIBQ_PBQ_Panel_asof_20260630.xlsx
- **HS1** = US_AI_ML_HandScored_1.xlsx (301-name roster/classification, no scores)
- **HS2** = US_AI_ML_HandScored_2.xlsx (301 hand-scored composites)
- **Q1-PDF** = q12026globalunicorntracker (published Q1 report; external reference)

## Market overview - Five financings

| Report figure | Source | Calculation |
|---|---|---|
| $87.1B top-5 rounds | PT / PT-Deals / B14 | SUM of 5 largest deal sizes, 'Top Deals in Qtr' col G |
| 62% of sized deal value | PT / PT-Deals / C14 = 0.6244 | B14 / B7 (sized total $139.494B) |
| Anthropic $65B into $965B | PT / PT-Deals / C23, D23 | top-15 table (source 'Top Deals in Qtr' row 84) |
| 5.4x next largest | calc | C23/C24 = 65/12 = 5.42 |
| 16.4% of first-half financing | calc | C23 / B51 = 65/396.1369 = 0.1641 |
| Prometheus $12B/$41B | PT / PT-Deals / C24, D24 | |
| Anduril $5B/$61B | PT / PT-Deals / C25, D25 | |
| ByteDance $3B/$370B | PT / PT-Deals / C26, D26 | |
| Isomorphic $2.1B | PT / PT-Deals / C27 | |
| four of five are AI | PT / PT-Deals / G23:G27 | vertical tags |
| under $2B by sixth company | PT / PT-Deals / C28 = 2.0 | rank-6 deal |
| top-10 68.9% / top-25 78.5% | PT / PT-Deals / C15, C16 | cohort sums / B7 |
| Q2 $144.9B; Q1 record $251.3B | PT / Unicorn deal activity / AR50, AQ50 | quarterly block; counts AR51=207, AQ51=237 |
| not 1,700 (1,743 active) | PT / Aggregate unicorns / M8 | also PT-Universe L6, B9 |

## Market overview - who writes the checks

| Report figure | Source | Calculation |
|---|---|---|
| 60.9% syndicates of 6+ | PT / PT-Round-Dynamics / B45 = 0.609375 | 6+ bucket / total known-investor rounds (row 42), from 'Rnds by Inv Count Bucket' |
| 2021 peak 64% | PT / PT-Round-Dynamics / B46 = 0.6402 | same, 2021 column (G43) |
| 2,892 Q3 2021 | PT / Unicorn investors x Qtr / Y9 | helper PT-Round-Dynamics D56 |
| 895 Q4 2023 | PT / Unicorn investors x Qtr / AH9 | helper E58 |
| 1,415 Q1 2026 | PT / Unicorn investors x Qtr / AQ9 | helper B61 |
| 995 Q2 2026 | PT / Unicorn investors x Qtr / AR9 | helper C61 |
| Sequoia 491 / Tiger 472 / a16z 454 / Accel 382 / Coatue 344 | PT / Top Investors / D8:D12 | financing counts since 2016 |

## Market overview - three ways to value / secondary gaps

All marks: MON / Top20_Marks. Cols: C=Model $B (from U20 daily prices via Names_Map),
D=Round $B (from Global Unicorn History latest snapshot), E=Secondary $B (from
Secondary Markets, marks as of 6/22/2026), F=Model/Round, G=Secondary/Round,
H=Secondary/Model.

| Report figure | Source | Calculation |
|---|---|---|
| 18 companies with a priced round | Top20_Marks D9=0, D22=0 flags | 20 minus SpaceX + Cerebras ('no round mark in history', I9/I22) |
| model +15.2% over round | Top20_Marks C29 = 0.1515 | aggregate SUM(C)/SUM(D)-1 over the 18 |
| 12 of 20 below model | Top20_Marks C30 = 12 | COUNT of H < 0 |
| SpaceX -32%, $2.03T model, ~$650B gap | C22=2026.2384, E22=1376.5462, H22=-0.3206 | gap = C22-E22 = 649.7 |
| Anthropic -22%, $1.27T, ~$282B | C5=1272.0931, E5=989.5575, H5=-0.2221 | gap = C5-E5 = 282.5 |
| Applied +36% / Anysphere +30% / Anduril +22% / Revolut +16% | G7=0.3648, G6=0.304, G4=0.2212, G19=0.1608 | secondary vs round |
| Ripple / Epic / Kraken all three down | rows 20, 12, 14 | F and G both negative |
| positions 22-32% above buyers | H5, H22 | the two largest names' secondary/model discounts |

## Market overview - median vs average

| Report figure | Source | Calculation |
|---|---|---|
| median $2.0B / average $18.19B | PT / MedAvg Uni Post Value / M8, M9 | 2026 column |
| 9.1-to-1; 3.1 (2025); 2.8 (2024) | calc | M9/M8; L9/L8 (4.8212/1.5725); K9/K8 (3.3377/1.1851) |
| $200M median / $1,143M average deal | PT / PT-Deals / D51, E51 | source 'MedAvg Uni Deal Size' M-col |
| widest in eleven years | PT / PT-Deals / F41:F51 | skew col; 2026 = 5.71 is max |

## Market overview - repriced quickly

| Report figure | Source | Calculation |
|---|---|---|
| step-up 2.20 / 2.05 / 2.64 peak | PT / MedAvg Uni Val Step Up / M8, L8, H8 | 2026 / 2025 / 2021 medians |
| interval 0.98 / 1.21 / 1.45 yr | PT / MedAvg Uni Time Between Rnds / M8, L8, K8 | |
| down rounds 6 / $3.85B; 31 (2025); 34 (2024) | PT / Unicorn down round activity / M9, M8, L9, K9 | |
| Hark 151x, post <$7B | PT / Top Deals in Qtr by Val Step Up / E8=151.43; G8+I8 = 0.7+5.3 = 6.0 | |
| Blitzy 30x, SendCutSend 30x | same / E9, E10 | posts: 0.2+1.2=1.4; 0.11+0.9=1.01 |

## Market overview - AI three-fifths

| Report figure | Source | Calculation |
|---|---|---|
| 702 of 1,743 = 40.3% | PT / AI Aggregate unicorns / M8; Aggregate unicorns / M8 | 702/1743 |
| $5.08T of $8.23T = 61.7% | AI Aggregate M9=5076.4207; Aggregate M9=8232.5063 | |
| $3.49T -> $5.08T, +45.6% | AI Aggregate L9, M9 | M9/L9 - 1 = 0.4557 |
| 109 of 178 new | AI Aggregate M10; Aggregate M10 | |

## Market overview - exits

| Report figure | Source | Calculation |
|---|---|---|
| $2.1T across 50 exits | PT / Unicorn exit activity / M8, M9 | helper PT-Exits L9, L14 |
| SpaceX $1.7T | PT / Top Exits in Qtr / G8 = 1690.2418 | helper PT-Exits B21 |
| ex-SpaceX $420.7B | PT / PT-Exits / B22 | M8 - B21 |
| four-fifths of exit value | PT / PT-Exits / B24 = 0.8007 | |
| listings 85% of value | PT / PT-Exits / L10 = 0.8541 | public-listing value L6 / total L9 |
| Cerebras $34B, Quantinuum $14B | PT / Top Exits in Qtr / G9=34.2454, G10=13.9782 | |
| aggregate peaked $8.7T, ended $8.23T | PT / Aggregate unicorns / AQ47=8699.6621, AR47=8232.5063 | quarterly series |
| TTE 8.47 / peak 9.17 (2025) | PT / MedAvg Uni Time to Exit / M8, L8 | helper PT-Exits B38, B39 |

## Verticals

| Report figure | Source | Calculation |
|---|---|---|
| SaaS $6.44T/968; AI $6.02T/865; FinTech $2.02T/436 | PT / Unicorn market val x vertical / D8,C8; D9,C9; D10,C10 | col D in $T |
| Space $1.87T/34; Mobility $0.83T/161; Cloud $0.74T/157; Health $0.45T/171 | same / D12,C12; D13,C13; D11,C11; D14,C14 | |
| leaders ~$12.5T; 1.5x universe | PT / PT-Vertical / B37=12468.11, B39=1.5145 | (D8+D9)x1000; /8232.5063 |
| SpaceX still in vertical; ex ~$180B | calc | D12x1000 - PT-Exits B21 = 1868.3-1690.2 = 178.1 |
| top-10 $2.9T = 35% | PT / Top 10 Unicorns by PV / SUM(F8:F17) = 2886.65 | /8232.5063 = 0.3506 |
| 614 raised within 12 months (a third) | PT / PT-Universe / B23, C23=0.3531 | from Active Unicorns col D vs 6/30/2026 |
| 54% US | PT / PT-Universe / B46=945, C46=0.5434 | Active Unicorns country counts |
| RVVC AI 1.84/2.35/249; SaaS 1.42/2.18/176 | PT / RVVC & Step Up Vertical Ranking / J9,L9,H9; J10,L10,H10 | 2026 medians |
| Robotics 2.03; CleanTech 3.30/2.77; Crypto 2.62->1.11; Cyber 0.66/1.74; Ecomm 0.38/2.13 | same / J15; J22,L22; E19->J19; J20,L20; J21,L21 | |
| AI 58.1%/302.6% cum; SW 34.2%; Cyber 22.2%; TME 19.6%/72.4%; FinTech 12.9% | MON / Vertical_Returns / C6,H6; C7; C14; D21,D20; C8 | level-based 3yr window 6/16/2023-6/30/2026 |
| 3 verticals beat TME | MON / Vertical_Returns / B22 | |
| AI ~3x public rate | MON / Vertical_Returns / B23 = 2.96 | |
| AI added $1.59T vs $0.93T universe gain | calc | AI Agg M9-L9 = 1589.19; Agg M9-L9 = 927.08 |
| 25% AI cut = $1.27T = 15.4% | calc | 0.25 x 5076.4207 = 1269.1; /8232.5063 = 0.1542 |
| 2021 cohort: 634 minted | PT / Aggregate unicorns / H10 | 2021 new-unicorn count |
| 470 active / 102 exited / 62 failed (34+15+13) | PT / 2021 Uni Cohort / col F rows 8-642 | COUNTIF statuses; 1 row has no status (635 data rows) |
| 74% / 16% / 10% | calc | 470/634, 102/634, 62/634 |

## Business quality and valuations

| Report figure | Source | Calculation |
|---|---|---|
| 5 dimensions + weights | PANEL / 2. Scoreboard / F3:J3 headers; 1. Methodology | CE 20 / RQ 25 / CI-SV 15 / GO 20 / MD 20 |
| 8 AIBQ / 12 PBQ | PANEL / 2. Scoreboard / col C rows 4-23 | COUNTIF (Key Findings tab says 11/9 - source-tab error) |
| tiers Elite >=8.0 ... Distressed <4.5 | PANEL / 1. Methodology | |
| ~15% of score variation | calc | R^2 of composite (M4:M23) on log10(valuation), 20 names = 0.145 |
| Databricks 8.19 Elite $134B | PANEL / Scoreboard / M4, N4, P4 | |
| Stripe 8.15 Elite $159B | PANEL / Scoreboard / M5, N5, P5 | |
| Anthropic 7.22 rank 7 at $965B | PANEL / Scoreboard / A10, M10, P10 | |
| OpenAI 6.30 rank 15 at $852B | PANEL / Scoreboard / A18, M18, P18 | |
| $2.2B/point Applied; $134B/point Anthropic; ~60x | calc | 15/6.91=2.17; 965/7.22=133.7; ratio 61.6 |
| 10 above-round avg 7.4 / 7 below avg 6.0 | MON Top20_Marks col G x PANEL composites | see FLAG 1 below |
| Anthropic -22% / OpenAI -9% vs model | MON / Top20_Marks / H5, H16 | |
| Figure AI 3.75, -23% vs round | PANEL M22; MON G13 = -0.2273 | |
| Neuralink 2.5, model +441% vs round | PANEL M23; MON F15 = 4.4164 | |
| secondary volume $562M Q2 / $1.33B Q1 (if added) | MON / Secondary Markets / L27, K27 ($M) | per-company pivot in MON-FULL rows 67-75 |
| 301 US AI companies | HS2 / 2. Hand-Scored AI Stack / rows 5-307; roster HS1 Sheet1 F54 | |
| median composite ~4.5 | HS2 / col P rows 5-307 | MEDIAN = 4.55 |
| five Strong or better | HS2 / col Q | 1 Elite + 4 Strong |
| 140 of 301 Distressed | HS2 / col Q | COUNTIF |

## Valuations and fallen unicorns

| Report figure | Source | Calculation |
|---|---|---|
| Anthropic $965B + OpenAI $852B = $1.82T = 22% | PT / Top 10 Unicorns by PV / F8, F9 | 1817/8232.5063 = 0.2207 |
| Anthropic valued May 2026 | PT / Active Unicorns / D91 = 2026-05-28 | |
| ByteDance May 2026 | PT / Active Unicorns / D234 = 2026-05-16 | |
| OpenAI March 2026 | PT / Active Unicorns / D1065 = 2026-03-31 | |
| Ant Group Aug 2020 | PT / Active Unicorns / D90 = 2020-08-09 | |
| SHEIN Jan 2024 | PT / Active Unicorns / D1268 = 2024-01-01 | |
| 47.6% >24mo / 37.1% >36mo | PT / PT-Universe / B18,C18; B19,C19 | months since Active Unicorns col D, denominator B14=1739 |
| RVVC 1.42 / 0.93 / 0.23 low / avg 2.73 | PT / MedAvg Uni RVVC / M8, L8, J8, M9 | |
| pre-boom baseline ~0.73 | PT / PT-StepUp-RVVC / B12 = 0.7306 | defined A12: 2016-2018 average of annual medians |
| 245 fallen | PT / PT-Fallen / B5 | curated 'Fallen Unicorns to Date' rows 8-252 |
| vs 175 reported in Q1 | Q1-PDF | published figure |
| rebuild: 160 since-2016 + 22 pre-2016 + 63 no-date | PT / PT-Fallen / B8, B9, B10 | |
| 2024 peak 34 falls | PT / PT-Fallen / B11 | COUNTIFS col I by year |
| median failing val $524.5M / -67% | PT / PT-Fallen / B15, B16 | 182 priced down rounds, col J |
| 15 fell at exit recorded as exits | PT / 2021 Uni Cohort / col F | COUNTIF 'Fallen at Exit' |

## What to watch

All figures repeat earlier citations (22% top-2 share, 62% top-5 share C14, 47.6% C18,
-22%/-32% H5/H22, three-fifths/two-fifths AI shares, $1.27T stress calc).

## Audit flags

1. **10-above vs 11-above (open item)**: Top20_Marks C31 counts **11** names with
   secondary > round. The report's "ten companies ... average 7.4" excludes Neuralink,
   whose +344% vs round (G15) is the stale-round artifact the same paragraph calls out.
   With Neuralink included: 11 names averaging 6.9. Recommend making the exclusion
   explicit or restating as 11/6.9.
2. **RVVC baseline window**: defined in-file as 2016-2018 average (A12/B12), not
   "pre-boom 2016-2020". Report wording ("roughly 0.73") is fine; the RVVC chart
   footnote was corrected to 2016-2018.
3. Space Technology vertical still carries SpaceX at final private valuation while the
   universe aggregate excludes it (report states this explicitly).
4. The 301-company score claims cite HS2 (scored); HS1 is roster-only.
5. "Q1's record $251.3B" is the current tracker's restated quarterly basis (AQ50);
   Q1-PDF printed $245.6B on its own extract.

## Addendum - post-review corrections (July 29, 2026)

- Median/average section reframed as financing-cohort figures: $2.0B/$18.19B are the
  'MedAvg Uni Post Value' deal-year series (M8/M9), NOT universe stats. Universe-wide:
  median active unicorn $1.65B (computed over Active Unicorns col G, n=1,155 with a
  stated post value), implied average $4.72B ($8,232.5B / 1,743). Downstream "$2.0B
  median company" references updated to ~$1.7B.
- SpaceX secondary rework: the Monitor's $1,376.5B SpaceX "secondary" is a pre-listing
  print (trade_date 2025-11-19) carried into the 6/22 snapshot. Public reality per
  PANEL Scoreboard row 8 note: day-one close ~$2.11T vs model $2.03T. All
  secondary-vs-model claims now scope to the 18 private names (11 below model =
  Top20_Marks H<0 excluding SpaceX); aibq_vs_secondary chart re-rendered with SpaceX
  at its day-one public close.
- "two-thirds of growth" corrected to three-fifths of new formation (109/178 = 61%).
- Above/below-round split restated: 11 of 18 above round (C31), text now states the
  Neuralink exclusion behind the 10-name 7.4 average.
- Added: weights disclosure, Elite/Distressed boundary convention, June 30 data cap
  (Databricks July round excluded per PANEL Methodology), 301-panel method note,
  R^2 n=20 caveat, secondary-source naming, xAI/Waymo index-exclusion note,
  865-tag vs 702-cohort reconciliation, secondary-volume sentence (MON Secondary
  Markets K27/L27), vertical-returns window note (3.039yr: 1.5814^3.039 = +302.6%).
- Body word count is now ~3,530 (corrections took precedence over the 3,250 target).

## Addendum - full-report audit (July 30, 2026), merged team draft

Everything computable from the data pack has now been independently recomputed.
New verifications (all exact unless noted): model-vs-round panel from U20 daily
valuations (9 above / 9 below, median +0.1%; every named premium incl. Ramp -13.8%,
Cursor 36.3->32.8, Kraken 11.8, Ripple 19.8); Cursor last trade 4/20; Q1-2024
volume baselines (top-5 45.7%, U20 45.4%); AI share of secondary volume 82.5% (Q4-25)
-> 53.1% (Q2-26) via Industry Vertical Constituents join; exit record 6.8x vs
Q4-2021 $262.7B; index Q2 +42.7% = strongest quarter since at least 2015; three
largest days 6/15 (+11.9%), 6/2 (+5.3%), 6/18 (+4.1%); ex-3-days +16.3% vs TME
+14.9%; 120d correlation +0.46 (2022-25 year-end avg +0.86 vs claimed +0.88);
regional US 50.8/26.3 ex-3, Asia 24.5/21.8, Europe 12.6/11.0; >6% days 2/0/0;
Cerebras final private mark $30.7B (U20 model 5/13); SpaceX $1.38T eve-of-listing
(U20 model 6/11, $1,379.1B); age-premium correlation -0.37 vs claimed -0.34.

Defects found this pass:
1. Mark-age WIDTH claim (12 pts young vs 30 pts old) REVERSES under reconstruction
   (~20 vs ~13 on tracker round dates) - verify against PrimVSec dates or cut.
2. Prometheus "past $18 billion of total funding" - HS2 shows $16.2B raised; no
   in-pack support for $18B.
3. "Nearly a third of the headline aggregate" (dormancy-by-value) - basis is the
   $6.06T disclosed-value subset; relabel like the adjacent sentence.
4. 2021 cohort "roughly a quarter would impair" - cohort base rates are 10% failed /
   16% exited; a quarter = resolved (exit+failure), not impaired. Reword.
5. Minor: "1% of deal count" is 1.4%; Europe Q2 prints 12.6% vs "12.7%".

Still unverifiable from the pack (needs FG's 'Uni IPOs' / 'IPO Performance' tabs or
endnotes): all IPO pop statistics (346/290/277 populations, medians by year, -0.86
in-quarter rank correlation, +0.42 issuance-lead), and external claims (71% of global
venture dollars, Forge $12.19B, Ripple $50B tender, Figma, Prometheus backers,
Anthropic/OpenAI listing-timing consensus).
