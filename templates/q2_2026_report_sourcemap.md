# Q2 2026 report - source traceability map

Every figure in `q2_2026_report.md` mapped to its source file, tab, and the exact
cell or computation. Three source files:

- **PT** = Final Q2 2026 Quarterly Unicorn Tracker (HR Version) - deal-level primary tracker
- **U20** = Morningstar PitchBook Unicorn 20 Valuations and Pricing Data (h version)
- **MON** = Unicorn Monitor Data Q2 2026 (lighter, HR version)

All figures as of 6/30/2026. "Derived" = arithmetic on cited cells, shown.

## Summary

| Figure | Source | Tab | Cell / logic |
|---|---|---|---|
| $8.23T aggregate / 1,743 active | PT | Aggregate unicorns (via PT-Universe) | 2026 col = 8,232.51; active 1,743 |
| +13% YoY | PT | PT-Universe | 8,232.51 / 7,305.43 - 1 = +12.69% |
| AI added $1.59T H1 | PT | AI Aggregate unicorns | 5,076.42 - 3,487.23 = 1,589.19 |
| universe gained $0.93T | PT | PT-Universe | 8,232.51 - 7,305.43 = 927.08 |
| non-AI lost ~$0.66T | PT | derived | 927.08 - 1,589.19 = -662.11 |

## Market overview

| Figure | Source | Tab | Cell / logic |
|---|---|---|---|
| Top-5 rounds $87.1B | PT | PT-Deals | Top-5 cohort = 87.1 |
| Anthropic $65B into $965B | PT | PT-Deals / Top Deals in Qtr | rank 1: deal 65, post 965 |
| 5.4x #2 (Prometheus $12B/$41B) | PT | PT-Deals | 65 / 12 = 5.42 |
| Anthropic 16.4% of H1 financing | PT | derived | 65 / 396.1 = 16.41% |
| Anduril $5B/$61B; ByteDance $3B/$370B; Isomorphic $2.1B | PT | PT-Deals | ranks 3-5 |
| Top-10 68.9% / Top-25 78.5% of sized deal value | PT | PT-Deals | 0.6889 / 0.785 (denominator = $139.5B sized) |
| Model +15.2% over round (aggregate) | U20+MON | Top20_Marks | 2,935.7 / 2,549.55 - 1 = 0.1515 |
| Secondary below model for 12 of 20 | U20+MON | Top20_Marks | count = 12 |
| SpaceX -32% ($2.03T model, $1.38T sec, ~$650B gap) | U20+MON | Top20_Marks | -0.3206; 2026.24 - 1376.55 = 649.69 |
| Anthropic -22% ($1.27T model, ~$282B gap) | U20+MON | Top20_Marks | -0.2221; 1272.09 - 989.6 = 282.49 |
| Applied Intuition +36% / Anysphere +30% / Anduril +22% / Revolut +16% (sec vs round) | U20+MON | Top20_Marks | 0.3648 / 0.304 / 0.2212 / 0.1608 |
| Ripple, Epic Games, Kraken reset lower | U20+MON | Top20_Marks | all three marks negative vs round |
| Median post $2.0B / avg $18.19B / 9.1x | PT | MedAvg Uni Post Value | median 2.0, avg 18.19, ratio 9.10 |
| 2025 3.1x / 2024 2.8x | PT | MedAvg Uni Post Value | 4.821/1.572=3.07; 3.338/1.185=2.82 |
| Median deal $200M / avg $1,143M | PT | MedAvg Uni Deal Size | 200 / 1,142.76 |
| Step-up 2.20x (2026), 2.05x (2025), 2.64x (2021 peak) | PT | PT-StepUp-RVVC | 2.201 / 2.048 / 2.641 |
| Time between rounds 0.98yr / 1.21 (2025) / 1.45 (2024) | PT | PT-Round-Dynamics | 0.9808 / 1.205 / 1.445 |
| Down rounds 6 / $3.85B (2026); 31 (2025); 34 (2024) | PT | PT-Round-Dynamics | count 6, value 3.846; 31; 34 |
| Hark 151.4x, Blitzy 30x, SendCutSend 30x (all <$7B) | PT | Top Deals in Qtr by Val Step Up | 151.4 / 30 / 30; posts 6.0 / 1.4 / 1.01 |
| AI 702 / 40.3% count / $5.08T / 61.7% value | PT | AI Aggregate unicorns | 702; 702/1743=40.3%; 5,076.42; /8,232.51=61.7% |
| AI $3.49T -> $5.08T / +45.6% | PT | AI Aggregate unicorns | 3,487.23 -> 5,076.42 = +45.57% |
| AI 109 of 178 H1 mints | PT | AI Aggregate (109) / PT-Universe (178) | new-in-year 2026 |
| AI tag 865; Monitor AI index 430 / $4,143.7B | PT / MON | PT-Vertical (865); AI_Share (430 / 4,143.69) | cross-basis note |

## Verticals

| Figure | Source | Tab | Cell / logic |
|---|---|---|---|
| SaaS $6.44T/968; AI $6.02T/865; FinTech $2.02T/436 | PT | PT-Vertical | 6,444.79/968; 6,023.32/865; 2,020.6/436 |
| Space $1.87T; Mobility $0.83T; Cloud $0.74T; Health $0.45T | PT | PT-Vertical | 1,868.3 / 829.7 / 742.1 / 450.9 |
| Top two ~$12.5T; ~1.5x universe | PT | PT-Vertical | 6,444.79 + 6,023.32 = 12,468.11; /8,232.51 = 1.514 |
| Space $1.87T / 34 / ~$55B each | PT | PT-Vertical | 1,868.3 / 34 = 54.95 |
| Ten largest ~$2.9T = 35%; median $2.0B | PT | Top 10 Unicorns by PV / MedAvg Post Value | 2,886.65 / 8,232.51 = 35.06%; median 2.0 |
| 614 companies (~a third) raised within past 12 months | PT | PT-Universe (dormancy buckets) | <=12mo bucket = 614 / 1,739 = 35.3% |
| 54% US-domiciled; 40% AI | PT | PT-Universe (country) / AI Aggregate | US 945/1,743 = 54.3%; AI 702/1,743 = 40.3% |
| Secondary-market pricing tracked for ~20 names | MON | Secondary Markets / Top20_Marks | constituent block = 20 names |
| AI RVVC 1.84x / step 2.35x / 249 deals | PT | RVVC & Step Up Vertical Ranking | 1.837 / 2.35 / 249 |
| SaaS 1.42x / 2.18x / 176 | PT | RVVC & Step Up Vertical Ranking | 1.423 / 2.183 / 176 |
| Robotics 2.03x (5.66x avg); CleanTech 3.30x / 2.77x | PT | RVVC & Step Up Vertical Ranking | 2.025 (5.658); 3.298 / 2.771 |
| Crypto RVVC 2.62x -> 1.11x | PT | RVVC & Step Up Vertical Ranking | 2025 median 2.619 -> 2026 median 1.11 |
| Cyber 0.66x; E-Commerce 0.38x (RVVC); step-ups 1.74x / 2.13x | PT | RVVC & Step Up Vertical Ranking | RVVC 0.662 / 0.3817; step-up 1.74 / 2.133 |
| AI +58.1%/yr (+302.6% cum); SaaS +34.2%; Cyber +22.2% | MON | Vertical_Returns | level-based annualized / cumulative |
| TME +19.6%/yr (+72.4% cum); 3 verticals beat; ~3x | MON | Vertical_Returns | 0.1963 ann / 0.7239 cum; beat-count 3; 0.5814/0.1963=2.96 |
| FinTech +12.9% (trails benchmark) | MON | Vertical_Returns | 0.1291 ann |
| AI $1.59T of $0.93T; 62% value; 4 of top-5; 61% mints | PT | AI Aggregate / PT-Deals | see above |
| 25% AI cut = $1.27T = 15.4% | PT | derived | 0.25 x 5,076.42 = 1,269.1; /8,232.51 = 15.4% |
| 2021 cohort 635: 470 active (74%), 102 exited (16%), 34 fallen, 15 fallen-at-exit, 13 bankrupt | PT | 2021 Uni Cohort | status col F value counts |
| Median time to exit 8.47yr | PT | MedAvg Uni Time to Exit / PT-Exits | 8.47 |

## Deal dynamics, capital, and exits

| Figure | Source | Tab | Cell / logic |
|---|---|---|---|
| Syndicate 6+ = 60.9% (2026); 64% (2021 peak) | PT | PT-Round-Dynamics | 0.6094 / 0.6402 |
| Participation 2,892 (Q3'21), 895 (Q4'23), 1,415 (Q1'26), 995 (Q2'26) | PT | PT-Round-Dynamics / Unicorn investors x Qtr | quarterly counts |
| Sequoia 491, Tiger 472, a16z 454, Accel 382, Coatue 344 | PT | Top Investors | 2016-YTD deal counts |
| Exit value $2,110.9B / 50 exits | PT | PT-Exits | 2,110.9; total count 50 |
| SpaceX IPO $1,690B | PT | PT-Exits / Top Exits in Qtr | 1,690.24 |
| Ex-SpaceX $420.7B | PT | PT-Exits | 420.7 |
| Public listings 85% of value | PT | PT-Exits | 0.8541 |
| Cerebras $34B; Quantinuum $14B | PT | Top Exits in Qtr | 34.25 / 13.98 |
| Median TTE 8.47yr; peak 9.17yr (2025) | PT | MedAvg Uni Time to Exit | 8.47 / 9.174 |

## Business quality (PBQ / AIBQ)

| Figure | Source | Tab | Cell / logic |
|---|---|---|---|
| Price ladder Anthropic/OpenAI/ByteDance/Stripe/Databricks/Waymo | PT | Top 10 Unicorns by PV | order by post-value |
| Two of top-10 on marks >1yr old | PT | Active Unicorns col D | Ant Group 2020-08-09; SHEIN 2024-01-01 |
| OpenAI #2 in universe by post-value | PT | Top 10 Unicorns by PV | Anthropic 965 > OpenAI 852 |
| Neuralink model +441% over round | U20+MON | Top20_Marks | 4.416 |
| Canva/Stripe/Rippling tight; Neuralink/Ripple/Kraken diverge | U20+MON | Top20_Marks | gap columns F/G/H |
| **Six PBQ composites (8.7 / 7.7 / 7.5 / 4.2 / 3.8 / 2.3)** | **NOT in these files** | prior-edition analyst source | flagged in text as external |

## Valuations and fallen unicorns

| Figure | Source | Tab | Cell / logic |
|---|---|---|---|
| Anthropic $965B + OpenAI $852B = $1.82T = 22% | PT | Top 10 Unicorns by PV | 1,817 / 8,232.51 = 22.07% |
| Ten largest ~$2.9T = 35% | PT | Top 10 Unicorns by PV | sum of 10 = 2,886.65; /8,232.51 = 35.06% |
| Anthropic May 2026 / ByteDance May 2026 / OpenAI Mar 2026 | PT | Active Unicorns col D | 2026-05-28 / 2026-05-16 / 2026-03-31 |
| Ant Group Aug 2020; SHEIN Jan 2024 | PT | Active Unicorns col D | 2020-08-09 / 2024-01-01 |
| 47.6% >24mo / 37.1% >36mo (latest-round dates) | PT | PT-Universe (dormancy) | 0.4761 / 0.3709 over 1,739 |
| 78.5% qualifying-date proxy | MON | Coverage_Gap | 0.7841 |
| RVVC 1.42x (2026), 0.93x (2025), 0.23x (2023), 0.73 baseline | PT | PT-StepUp-RVVC | 1.418 / 0.9323 / 0.2342 / 0.7306 |
| Avg RVVC 2.73x | PT | PT-StepUp-RVVC | 2.729 |
| 245 fallen | PT | Fallen Unicorns to Date / PT-Fallen | 245 rows |
| Median down-round post $524.5M; markdown 67% | PT | PT-Fallen | 524.5; -0.6722 |
| 15 fell at exit (2021 cohort) | PT | 2021 Uni Cohort | status = "Fallen at Exit" = 15 |

## What to watch

| Figure | Source | Tab | Cell / logic |
|---|---|---|---|
| 22%; top-5 62% of Q2 deal value; 47.6% untested | PT | Top 10 PV / PT-Deals / PT-Universe | 22.07%; 0.6244; 0.4761 |
| 20-30% below model (megacaps) | U20+MON | Top20_Marks | SpaceX -32%, Anthropic -22%, OpenAI -9% |
| AI 3/5 value on 2/5 names | PT | AI Aggregate | 61.7% / 40.3% |
| 25% AI cut = $1.27T | PT | derived | 0.25 x 5,076.42 |

## Analytical statements (not single-cell figures)

These are reasoned claims, not direct reads, and are labeled as such in the text:
- Fund-cycle maturity 2028-2031 (10-year life on 2021-vintage funds).
- "Investable set falls to a few dozen" once fresh-mark + size + secondary filters
  are stacked (illustrative funnel, not a computed count).
- "Exit value settles below the 2026 figure once the backlog empties" (inference
  from the 8.47yr time-to-exit and the SpaceX-dominated 2026 total).

## Basis rule

Universe / aggregate / dormancy / deal dynamics / exits / fallen / country -> PT.
Three-mark secondary validation of the top 20 -> U20 + MON. Vertical index 3-year
returns -> MON. The three bases are never blended (AI 702 vs 865 vs 430 kept
distinct; aggregates $8.23T PT vs $8.50T MON kept distinct).

## Addendum - final editorial pass (July 28, 2026)

Verified against the July 28 workbook uploads. The Unicorn 20 and Monitor files are
byte-identical to the previously verified versions; the Final Q2 tracker was re-verified
in full (all figures confirmed, including Q1 quarterly deal value $251.26B and the Q1
aggregate peak $8,699.66B on the 'Aggregate unicorns' quarterly block, col AR area).

- 301-company US AI claims (median composite 4.55, 1 Elite + 4 Strong, 140 Distressed):
  source is US_AI_ML_HandScored_2.xlsx tab '2. Hand-Scored AI Stack'. The separately
  supplied US_AI_ML_HandScored_1.xlsx is the roster/classification only (301 names:
  20 model / 35 infra / 246 application) and carries no scores - cite the _2 workbook.
- Source-data flag: 'Unicorn market val x vertical' (as of 6/30/2026) still carries
  SpaceX inside Space Technology ($1.868T / 34 names) while 'Active Unicorns' and the
  $8,232.5B aggregate exclude it post-IPO. Report text now states this explicitly.
- Basis note: "Q1's record $251.3 billion" is the current tracker's restated quarterly
  figure; the published Q1 report printed $245.6B on its own extract.
- Chart slots: q2_2026_aibq_vs_primary.png (after 'The scores against primary
  valuations'), q2_2026_aibq_vs_secondary.png and q2_2026_quality_for_size.png (after
  'The scores against the secondary market'). Quality-for-size uses the all-private
  roster (xAI/Waymo in place of SpaceX/Cerebras); on that roster valuation explains
  ~6% of score variance vs ~15% on the Unicorn 20 panel - caption should say so.
