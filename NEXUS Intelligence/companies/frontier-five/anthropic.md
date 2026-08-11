# Anthropic — NEXUS Intelligence Profile

*Compiled from the NEXUS consolidated data bundle (49 source tables, 1,466 rows after de-duplication) plus six companion narrative extracts. Tier: Frontier Five. This document is a narrative digest; the full row-level data — including everything not surfaced below — lives in the companion file `anthropic.json`.*

**A note on how to read this document:** NEXUS is a live, actively-contradicting-itself research system. Where two parts of NEXUS disagree with each other (a common and, per its own rulings, an intentional feature — conflicts are frozen, not silently resolved), this profile shows both values, both dates, and both sources rather than picking a winner. See Section (i).

---

## (a) Overview

**Anthropic PBC** is a Public Benefit Corporation and frontier AI research and deployment company, best known for the **Claude** family of large language models. It was founded **2021** (event log dates the founding to 2021-01-01; the underlying story — co-founders Dario and Daniela Amodei leaving OpenAI to start "a focused research bet" — is dated by one timeline entry to **2020-11-01/late 2020–early 2021**) by **Dario Amodei** (CEO) and **Daniela Amodei** (President), together with 9 other co-founders (11 total, most ex-OpenAI).

| Field | Value | Source / date |
|---|---|---|
| Legal name | Anthropic PBC | nexus-data-audit, 2026-05-06 |
| HQ | San Francisco, CA | multiple, consistent |
| Other offices | New York, London, Dublin, Singapore, Tokyo (5 alternate offices) | legacy_companies_row, extracted 2026-08-09 |
| Sector | Foundation Models (self-description) / AI-INFRA (AIBQ classification) | legacy_companies_row / v2_company_registry |
| Tier / Stage | Frontier Five, Tier 1 / AIBQ Stage S5 | v2_company_registry, 2026-05-27 |
| PitchBook ID | 466959-97 | nexus-data-audit |
| CIK (SEC) | None listed as of data capture | nexus-data-audit, 2026-05-06 |
| Business status | "Generating Revenue / Not Profitable" | legacy_companies_row, extracted 2026-08-09 (see Financials for a disputed Q2 2026 "first operating profit" claim) |
| Core products | Claude (Opus/Sonnet/Haiku tiers), Claude Code (coding agent), Claude Developer Platform, Claude for Financial Services / Legal / Small Business, Managed Agents platform | aibq_model_registry; v2_master_events |
| Strategic priorities | "building reliable, interpretable, steerable AI systems; conducting frontier research; developing and applying safety techniques" | legacy_companies_row |
| Board | Dario Amodei, Daniela Amodei, Spark Capital (seat), Google (observer), Amazon (observer); Vas Narasimhan (Novartis CEO) added to the Long-Term Benefit Trust board, announced 2026-04-26 | legacy_companies_row; aibq_score_tracker |
| Leadership (selected hires) | Krishna Rao, CFO (joined 2024-05-21, ex-Airbnb/Fanatics/Cedar); Rahul Patil, CTO (2025-09-01); Mike Krieger, ex-Instagram co-founder (2024-05-15); Jason Clinton, CISO (2023-04-01); Vu Bui, Head of Strategic Finance & IR (2024-01-10) | v2_master_events |
| IP / research assets | Constitutional AI methodology (published 2021-12-15); Claude architecture patents pending; Natural Language Autoencoders interpretability paper (~May 2026) | v2_master_events; legacy_companies_row |
| Governance note | "No profit cap or mission lock" on Series G terms — an explicit contrast with OpenAI's capped-profit structure | legacy_companies_row, "Investor Rights" field |

---

## (b) Current scores — AIBQ composite and sub-scores

**Framework note:** the underlying system consistently calls this the **AIBQ** framework (no "PBQ" label appears anywhere in the source data).

### Headline

| | Composite | CE | RQ | CI | GO | MD | CRA | Confidence |
|---|---|---|---|---|---|---|---|---|
| **Current — canonical** (2026-05-27) | **8.20** (Strong) | 8.0 | 9.5 | 5.8 | 7.3 | 9.3 | 0.00 | High |
| Prior checkpoint (2026-05-08 → 2026-05-24, held flat) | 8.06 | 8.0 | 9.5 | 5.1 | 7.3 | 9.3 | — | High |
| Earlier baseline (2026-02-27, v2.2) | 7.40 | 7.0 | 9.0 | 5.0 | 7.0 | 8.0 | — | High |

Source: `canon_canonical_figures` ("Anthropic AIBQ v3.0 score 8.20," CANONICAL, verified through 2026-07-16) and `aibq_daily_scores` (full daily series, 2026-02-27 through 2026-07-06). Anthropic ranks **#2 of the Frontier Five**, behind Databricks (8.92) and ahead of OpenAI (4.53), xAI (4.29–4.49 depending on date), and SSI (2.30).

The jump from 8.06 to 8.20 on 2026-05-27 is a single-cause move: **CI rose 5.1 → 5.8 (+0.7)** on disclosure, via the SpaceX S-1, of Anthropic's Cloud Services Agreement with SpaceX ($1.25B/month through May 2029, ~$45B total; SEC filing, 2026-05-20) — scored as **compute-provider diversification** (AWS concentration falling from ~90% to ~70% AWS + ~30% SpaceX). CE, RQ, GO and MD were explicitly untouched by this event (`aibq_daily_scores`, entry "SpaceX Compute Deal: CI Upgrade").

### Sub-dimension detail (CE-1…MD-5)

Captured at the **8.06 checkpoint** (dated 2026-05-26 in `aibq_unicorn_scores`; corroborated by the framework AIBQ Deep Dive document, page-state 2026-05-27) — this is the most granular breakdown available; it was **not re-issued** after the CI revision to 5.8, so CI-1 in this table (6.0) reflects the pre-SpaceX-deal read even though it sits inside a doc whose CI-1 language elsewhere describes the diversification already happening:

| CE | | RQ | | CI | | GO | | MD | |
|---|---|---|---|---|---|---|---|---|---|
| CE-1 | 10.0 ✅ | RQ-1 | 10.0 ✅ | CI-1 | 6.0 | GO-1 | 8.0 | MD-1 | 9.5 |
| CE-2 | 4.0 ⚠️ | RQ-2 | 9.0 | CI-2 | 4.0 ⚠️ | GO-2 | 7.0 | MD-2 | 9.5 |
| CE-3 | 9.0 | RQ-3 | 10.0 ✅ | CI-3 | 5.0 | GO-3 | 7.0 | MD-3 | 9.0 |
| CE-4 | 8.0 | RQ-4 | 9.0 | CI-4 | 5.0 | GO-4 | 7.0 | MD-4 | 9.0 |
| — | | RQ-5 | 9.0 | CI-5 | 5.0 | GO-5 | 7.5 | MD-5 | 9.5 |

**CE-2 (gross-margin quality) is the single largest drag** on the composite — scored 4.0 against a ~40% gross margin, with the framework note projecting CE-2 would move to the 5–6 band (adding ~0.10 to the composite) if margins are confirmed above 50%. CI-2 (owned infrastructure) is the other sub-7 outlier: Anthropic leases all its compute from cloud partners and owns no data centers or custom silicon as of the scoring date.

### ⚠️ Open score conflict — read before citing "the" composite

NEXUS's own daily **Morning Digest** tracker (`shared_morning_digests_db`, 87 entries, 2026-04-25 through 2026-08-10 — the most recent entry available, one day before the "today" date of this profile) shows the Anthropic composite **oscillating between 8.20 and 8.06 from mid-June through mid-July 2026, then settling on 8.06 continuously from 2026-07-16 through 2026-08-10** — the digest itself flags this explicitly: *"Anthropic and xAI flagged for active composite deltas vs. May 27 canonical (Anthropic −0.14; xAI −0.20; see §17)"* (digest of 2026-08-10). A 2026-06-12 reconciliation entry in `aibq_daily_scores` attributes the 8.06 reading to a **"VPS pipeline" bug that pulled stale 2026-05-08/05-12 rows**, and explicitly re-asserts "May 27 v3.0 canon 8.20/Strong" as canonical — yet the digest kept reverting to 8.06 for two more months after that correction was logged. **This profile reports 8.20 as canonical** (it carries `Status: CANONICAL` and the most recent verification timestamp, 2026-07-16, in `canon_canonical_figures`), but the 8.06 reading remains live and unreconciled in the daily tracker as of the last available data point. Neither number is silently discarded.

$/AIBQ-point (methodology note, not a valuation call): **~$118B per point**, derived $965B ÷ 8.20 (`canon_canonical_figures`, VOLATILE decay class). *A cross-company quality-vs-valuation relationship is separately tracked by NEXUS across the whole Frontier Five cohort; the correlation coefficient itself is embargoed from publication system-wide and is not reproduced anywhere in this profile.*

---

## (c) Financials

All figures gross/ASC-606-principal basis unless noted (Anthropic reports revenue **gross**, including AWS/Google reseller pass-through — Ruling 5 explicitly warns never to compare this raw against OpenAI's **net**-basis figures).

### ARR / run-rate ladder (append-only; estimates flagged)

| As of | ARR | Status | Source |
|---|---|---|---|
| 2022A | ~$60M | Estimated, low confidence | Sacra/press, via `shared_financial_model_inputs` |
| Mid-2023 | ~$150M | Estimated | Anthropic press release back-calculation |
| End-2023 | ~$1,000M ($1B) | Estimated (**supersedes** an earlier $800M figure the source itself flagged as incorrect) | `shared_financial_model_inputs` |
| End-2024 | $1B | Confirmed (company disclosure) | Anthropic press release |
| End-2025 | $9B | Confirmed | Bloomberg, 2026-01-21 |
| 2026-02-12 (Series G close) | $14B | Confirmed — company's own words: *"today, our run-rate revenue is $14 billion, with this figure growing over 10x annually in each of the past three years"* | Anthropic press release |
| ~2026-03-03 | ~$20B ("nears/approaching") | Confirmed | Bloomberg |
| **2026-04-07** | **$30B** | **CANONICAL** — gross basis; first quarter Anthropic passed OpenAI (~$25B net) in run-rate revenue; explicit system note: *"DO NOT CHANGE WITHOUT T1 PRIMARY SOURCE"* | Bloomberg, 2026-04-07 |
| 2026-05-01/03 | $40–47B (reported range) | Mixed-confidence: SemiAnalysis ~$44B+ (primary source for that figure); Contrary Research $40B (end-April); Dario Amodei "80x growth" language (Fortune, ~2026-05-05) implies ~$40–44B | see Section (i) conflict #2 |
| 2026-05-01 (canonical mark) | **$47B** | CANONICAL but flagged **STALE** as of 2026-07-16 (2.5 months old, past QUARTERLY decay) | Company-announced, May 2026 |
| 2026-06-30 | $44B, "doubling every 6 weeks in 2026" | — | `timeline_dated_events` |
| — (methodology only) | ~$28.3B net-equivalent | **Not a print** — Ruling 5's 39.75% gross→net equalization factor applied to the $47B gross figure, for cross-company comparison only | `canon_canonical_figures` |

**Forward-projection traps (explicitly NOT current ARR per Ruling 4 — PitchBook TTM fields are forward projections):** PitchBook's TTM-4Q2026 field shows $30B; its TTM-4Q2027 field (period end 2027-12-31) shows **$55B** — "DO NOT ADOPT $55B" as a run-rate figure.

**Claude Code** (product line): **$2.5B ARR**, 54% coding-market-share, disclosed at Series G close (Feb 2026, within 90 days of relaunch) — `canon_canonical_figures`, CANONICAL. A 2026-06-04 analyst note in the profile page flags this as likely stale/understated: total ARR roughly tripled Feb→May 2026 with no updated Claude-Code-specific disclosure.

### Booked revenue (distinct from ARR — deferred multi-year enterprise contracts create a gap)

| Period | Booked revenue | Note |
|---|---|---|
| 2024A | $1B | Near-parity with ARR at this early stage |
| 2025A | $4.5B | vs. $9B ARR — "ARR/booked gap = 2x," driven by deferred recognition |
| 2026E | $18B | WSJ internal investor-doc projection (vs. $30B ARR); marked "INTERNAL ONLY, pre-publication cooling-off applies" in source |

### Gross margin — two competing reads (both preserved, see conflict #3)

- **~40%** (2025 actual) → 63% (2027E) → 77% (2028E). Historical arc: **−94%** (2023A) → 40% (2025) → 63% → 77%. Source: WSJ investor docs, 2026-04-06 — "a 10-point miss vs. 50% internal plan, driven by inference costs running 23% above budget."
- **70%+** ("inference infrastructure gross margin," up from 38% a year earlier) — SemiAnalysis, cited by Bitget, 2026-05-03, written up in a 2026-06-04 NEXUS analyst note that explicitly flags this may measure something narrower than GAAP gross margin (excluding SBC, non-inference COGS, support, DC ops) and recommends cross-referencing against audited S-1 financials once available.

### Headcount — conflicting reads (see conflict #6)

- **2,500** — carried in every "Companies DB"-synced tracking table (`legacy_companies_row`, `aibq_company_snapshots` through its most recent entry 2026-08-11, `framework_company_financials`) as of PitchBook, 2026-03-04.
- **5,000** — `canon_canonical_figures`, CANONICAL, PitchBook 2026-04-21 datum, verified current 2026-07-16; explicitly noted as "Now ABOVE OpenAI's 4,500 (2026-03-21)."

### Burn, runway, losses (as of "Last Extracted" 2026-08-09; prior-period comparison in parentheses)

Burn rate **$500M/mo** (was $600M/mo) · Runway **36 months** (was 30) · Cumulative losses **$8.0B** (was $5.0B) · Compute spend **$7.0B/yr** (2026E) — `legacy_companies_row`.

### EBITDA / FCF model (WSJ investor docs, 2026-04-06; "Analyst Model," Confidence HIGH)

| | 2026E | 2027E | 2028E | 2029E |
|---|---|---|---|---|
| EBITDA incl. training | −$5.0B | −$5.0B | +$3.0B (first breakeven incl. training) | +$15.0B |
| EBITDA excl. training | +$3.0B | +$10.0B | +$25.0B | +$50.0B |
| Training spend | $7.0B | $14.0B | $22.0B | $30.0B |
| Revenue (booked, WSJ) | $18B | $55B | $93B | $133B ($125B enterprise / $8B consumer) |

FCF: worst case **−$25B (2027E)**; **+$15B (2029E)**; cumulative negative FCF through 2029E **~$64B**.

**Actual, reported:** Q2 2026 **first operating profit, ~$559M** (T3/CNBC-sourced) — flagged **"under FCF sweep review"** by Ruling 3 (effective 2026-06-12): *"Anthropic bear-case FCF margin was revised down significantly. Sweep ALL talking points and briefings before reuse."* The associated sweep is still marked **Open** in `canon_sweep_tracker` as of the latest data. A separate note (command-center feed, 2026-05-20) put Q2 revenue at "more than double to $10.9B from Q1 $4.8B... but compute costs later in 2026 may erase operating profits."

### Capital efficiency ratio — an append-only ladder, not one number (CE denominator = equity raised only, per Ruling 1; debt informs risk, not CE)

| Basis / date | CE ratio | Note |
|---|---|---|
| ~$14B ARR / $60.55B raised (~Feb 2026) | 0.23x | "$4.33 capital per $1 of ARR" |
| $20B / $61.15B (~Mar 2026) | 0.33x | |
| $30B / $60.55B (2026-04-16, quintile-crossing event) | 0.495x | Moved CE sub-score 7→8 same day |
| $47B gross / $124.3B equity-only (post-Series-H, canonical) | **0.38x** | Gross numerator |
| ~$28.3B net-equivalent / $124.3B equity-only (Ruling 5, equalized) | **0.228x** | The apples-to-apples figure NEXUS ships in comparisons; **1.65x better** than OpenAI's equalized 0.138x — one of two "survivors" of the gross/net equalization (the other being an 81% AIBQ quality premium, 8.20 vs. OpenAI's 4.53) |

### Operating metrics (Company disclosure / Bloomberg 2026-04-07 unless noted)

NRR **140%+** · Enterprise mix **80%** · Business customers **300,000+** · $1M+ ACV customers **1,000+** (doubled from 500+ in under 90 days) · Customer concentration **15%** · Revenue/employee **$5.6M** · Revenue/customer **$46.67K** · Global LLM revenue market share **31.4%, Q1 2026** (Counterpoint Research) vs. OpenAI's 29% — the first quarter Anthropic passed OpenAI on this metric. Compute obligations across partners: **$80B+** (6 partners: SpaceX/COLOSSUS, Fluidstack, AWS, Microsoft+NVIDIA, Google+Broadcom).

---

## (d) Valuation & funding history

### Primary rounds (chronological)

| Date | Round | Raised | Post-money | Investors named | Notes / conflicts |
|---|---|---|---|---|---|
| 2021-05-28 | Series A | $124M | $461M | — | |
| 2022-04-29 | Series B | $980M | $3.0B | — | A separate, undated headline elsewhere gives "$580M Series B" — unresolved discrepancy, both shown |
| 2023-06-30 | Series C | $450M | $4.55B | — | |
| 2023-10-27 | Series D | $2.0B | $15.8B | Alphabet/Google-led | "Series D" label reused (see 2024-07-01 row) |
| 2024-07-01 | "Series D" (reused label) | $4.0B | $19.35B | Menlo Ventures-led | Same round label as 2023-10-27 — data-quality flag, not adjudicated |
| 2024-11-22 | Series E2 | $4.0B | $15.53B | Amazon | **Down round** vs. the $19.35B prior mark; "E2" precedes "E" chronologically (see next row) — labeling oddity |
| 2025-03-03 | Series E | $3.5B | $61.5B | — | |
| ~Sep 2025 (inferred; not explicitly dated in its own row — cross-referenced via the company's announcement URL slug and a financial-model citation) | Series F | $13B | $183B | — | |
| **2026-02-12** | **Series G** | **$30–30.6B** | **$380B** | Three different investor lists appear: GIC & Coatue (financial-model-inputs); Lightspeed (shared_valuations); Coatue/ICONIQ/Soma/MGX/D.E. Shaw/Dragoneer/GIC/Founders Fund (shared_report_data_points) | **Date conflict**: at least one row dates this identical round to **2025-02-12** instead — a likely one-year data-entry error given the overwhelming majority of corroborating rows place it in Feb 2026 |
| **2026-05-28** | **Series H** | **$65B** | **$965B** ($900B pre-money) | Led by Dragoneer, Sequoia, Greenoaks, Altimeter | **CANONICAL**, PitchBook-confirmed 2026-07-16. Share price **$589.0095**; **17.33%** of the company acquired in-round; investor ownership **62.66%** post-round; **~1,638M** implied shares outstanding |

### Secondary / other capital events

- **2024-05-31** — FTX/Alameda stake sold, $1.32B secondary
- **2025-01-15** — Homeroom Fund / Lakeside Capital secondary (Low importance)
- **2025-05-16** — $2.5B revolving credit facility (non-dilutive debt)
- **2025-09-09** — Alphaaero / Irving Investors secondary (Low importance)
- Undated — staff share sale up to $6B ("Anthropic Kicks Off Share Sale for Staffers")
- **2026-06-09** — $34.5B chip-purchase bonds (tranched: $6.0B Superpriority / $24.0B 1st Lien / $4.5B 2nd Lien)
- **Total debt: $37.0B** ($34.5B bonds + $2.5B revolver) — **excluded from the CE ratio** per Ruling 1 ("debt informs CI/risk, not CE")

### Secondary-market pricing (distinct from primary rounds — never treated as canonical valuation)

| Date | Implied valuation | Status |
|---|---|---|
| 2026-04-15 | ~$1.0T | Secondary market estimate |
| 2026-04-16 | $800B | UNCONFIRMED rumor (VentureBeat, T3) — "FREEZE until Bloomberg/WSJ T1 confirmation" |
| 2026-04-29 | $800B | Hiive secondary, +211% |
| ~2026-04 | $688B | Caplight secondary mark, +75% in 3 months (referenced in `shared_forecasts`) |
| 2026-01 (investor deck) | $1.995T by 2030 / $2.413T by 2031 | Coatue January 2026 investor presentation (forward projection, not a mark) |
| 2026-07-10 | $1.2T | "Anthropic valuation reaches $1.2 trillion on secondary markets, surpassing OpenAI" (`timeline_dated_events`) — a different, non-primary basis from the $965B Series H mark |

### Total capital raised — another ladder, not one number

| Value | As-of / vintage | Source |
|---|---|---|
| $60.55B | Cumulative through Series G, ~Feb 2026 | `shared_financial_model_inputs` |
| $61.154B | Same period ("more precise than Crunchbase ~$64B") | `shared_ai_financial_model` / `shared_report_data_points` |
| $65.0B | Carried forward through the **most recent (2026-08-11)** entries of the stale tracking tables | `legacy_companies_row`, `aibq_company_snapshots` |
| $66.8B | 2026-05-12 | `shared_ipo_pipeline` |
| $67.35–67.4B | ~2026-05-09/18 | framework docs, nexus-data-audit |
| $75.55B | 2026-05-27 (outlier — higher than every other same-period figure) | `framework_company_financials` |
| **$124.3B** (equity-only) | **CANONICAL**, verified 2026-07-16 (canonical since 2026-07-02) | `canon_canonical_figures` |
| **$161.3B** (total, incl. $37.0B debt) | **CANONICAL**, verified 2026-07-16 | `canon_canonical_figures` |

### IPO

- Confidential IPO registration filed **2025-12-01** (PB deal 314988-58T). One `timeline_dated_events` row separately states Anthropic "confidentially files for IPO at $965 billion valuation" dated **2026-01-01** — internally inconsistent, since the $965B mark was not reached until the Series H closed on 2026-05-28; flagged, not adjudicated (see conflict #12).
- PitchBook IPO deal originally listed "Upcoming" dated **2026-05-31** (nexus-data-audit: "may be a placeholder"); target later shown as **2026-10-01** (`shared_ipo_pipeline`, updated 2026-05-12) with an IPO window of **Oct 1–15, 2026**.
- Readiness score **72/100** (Financial 8, Market 7, Competitive 9, Governance 6, Regulatory 6); IPO Deal ID 325962-01T; **Rank 3** among the Frontier Five; **Filing Status: Pre-Filing** (as of 2026-05-27 data).
- House prediction: **P = 0.65** that pricing slips to 2027 (canon dossier).
- Open forecast: "Anthropic files S-1 by Aug 31, accelerating from Oct target" — **P = 0.55**, logged 2026-05-20, test date 2026-08-31, still Unresolved (see Section g).
- Banks in early talks reported (GS/JPM/MS mentioned via a SemiAnalysis writeup, 2026-03-27); no lead underwriters listed as of the `shared_ipo_pipeline` update.
- Critical blockers flagged: gross-vs-net ARR reconciliation exposure in the S-1; governance complexity from three hyperscaler investors who are simultaneously infrastructure providers and board-level stakeholders.

---

## (e) Cap table & investors

Anthropic PBC is governed under a **Long-Term Benefit Trust**. No full equity-waterfall / share-class table exists in the source data — the closest available is a set of investor-relationship rows plus the Series H per-share terms above.

### Named investors and terms

| Investor | Committed / invested | Terms | Date |
|---|---|---|---|
| **Google / Alphabet** | Up to **$40B** total ($10B immediate + $30B contingent on milestones) | Board observer seat; GCP preferred-provider status; TPU access; part of a 5GW compute commitment | 2026-04-24 |
| **Amazon / AWS** | Up to **$25B** equity + **$100B**/10-yr AWS infrastructure commitment; $5B fresh tranche 2026-04-20 brought cumulative invested to $13B (of up to $20B more, milestone-contingent) | Board observer seat; preferred-provider status + a Bedrock exclusivity window (at points); total AMZN exposure **$39.7B** per SEC disclosure | 2026-02 – 2026-04-20 |
| **Microsoft** | $5B equity + $30B Azure cloud commitment | Framed internally as MSFT's "hedge position" alongside its OpenAI stake; completes Anthropic's tri-cloud (AWS/Google/Azure) architecture | 2026-04-01 |
| **Blackstone-led PE JV** (Blackstone, Goldman Sachs, Hellman & Friedman, Apollo, General Atlantic; a related event row also names GIC, Leonard Green, Sequoia) | $1.5B | Captive AI-tools distribution vehicle for PE portfolio companies; 17.5% return structure said to mirror OpenAI's TPG JV | 2026-05-04/05 |
| **Menlo Ventures** | Led a 2024 round ($4B / $19.35B post); separately sponsors the co-branded "Anthology Fund," $100M, vintage 2024, closed | | 2024; 2024 |
| **Series H leads** | Dragoneer, Sequoia, Greenoaks, Altimeter | $65B / $965B post | 2026-05-28 |
| **Strategic stakes** (named, no further detail) | Coatue, GIC | | — |

**Active investor count:** **245** (nexus-data-audit, Apr-2026 vintage PitchBook pull) vs. **229** (`shared_report_data_points`, Mar-2026 vintage) — both PitchBook-sourced at different dates; shown both (conflict #7).

Anthropic itself is an active investor: **19 active portfolio companies** (nexus-data-audit).

**M&A (as acquirer):**
- **Coefficient Bio** — ~$400M, drug-discovery / clinical AI. Dated **2026-04-03** in the canon company dossier vs. **2026-04-16** in `shared_revenue_decomposition` — both shown, ~2-week discrepancy unresolved.
- **Vercept** (computer-use AI startup) — acqui-hire, 2026-02-25.
- **Humanloop** — team acqui-hire (undated).
- **Stainless** (API SDK tooling) — reported in talks to acquire for $300M+ (per 2026-05-13 score-tracker note).

**Governance note carried over from Overview:** Series G terms carry "no profit cap or mission lock" — an explicit structural contrast with OpenAI cited across multiple NEXUS theses (e.g., "The Builder and the Banker," 2026-05-06).

---

## (f) Litigation & IP

### The Pentagon / DoD "Supply Chain Risk" saga (the dominant regulatory storyline, multi-stage)

| Date | Development |
|---|---|
| 2025-03-12 | **Precursor:** US federal use ban — Trump administration designates Anthropic a national security risk (moved AIBQ GO 8→7) |
| 2026-02-28 / 2026-03-01 | Pentagon issues stop-use order + formal supply-chain-risk designation |
| 2026-03-09 | Anthropic sues DoD over the designation (N.D. Cal., later also D.C. Circuit) |
| 2026-03-26 | SF federal judge grants a **preliminary injunction blocking** the designation |
| 2026-04-08 | D.C. Circuit **denies a separate injunction bid** — the litigation tracker explicitly frames the pair of rulings as *"split rulings creat[ing] jurisdictional uncertainty,"* net AIBQ GO impact "zero" despite real volatility (+0.5 then −0.5) |
| 2026-05-19 | D.C. Circuit hears the substantive Anthropic v. Pentagon case |
| 2026-07-01 | US Air Force separately mandates its contractors cease using Anthropic **by 2026-09-01** |
| 2026-07-30 | Judge rules the administration **lacks evidence** to sustain the supply-chain-risk label |

Estimated federal-revenue exposure throughout: **~$200M (~1.4% of ARR)**. (Sources: `shared_litigation`/`v2_litigation_ip` [merged, identical], `v2_master_events`, `timeline_dated_events`.)

### Export-control restriction

Commerce Department / White House orders (**2026-06-12 to 2026-06-19**) forced Anthropic to cut off **foreign access** to its most advanced models (Mythos 5 / Claude Fable 5) on national-security grounds; access was **restored after a 20-day dispute on 2026-07-03**.

### Copyright

| Matter | Plaintiff(s) | Filed | Status |
|---|---|---|---|
| **Bartz v. Anthropic** (author class action) | Authors | — | Settled **$1.5B** — "America's largest copyright settlement"; plaintiffs' fee request cut to $187.5M (2026-03-22); court approval reported both **2026-07-01** ("approved by judge") and **2026-07-20** ("receives final approval") — both dates shown, not adjudicated (possibly preliminary vs. final approval, possibly duplicate reporting) |
| Music Publishers v. Anthropic | Universal Music, Concord, ABKCO | 2023-10-19 | Active; unauthorized lyrics in training data |
| BMG v. Anthropic | BMG | 2025-04-08 | $75M+ claim |
| Music Industry Consortium v. Anthropic | Universal Music, Sony, Warner | 2025-10-15 (M.D. Tenn.) | Active; training-data copyright + lyrics reproduction in Claude outputs; tracked as a potential Revenue-Quality risk, no confirmed AIBQ score impact as of last update (2026-04-01) |

A separate NEXUS analytical report (*The $100 Billion Entry Fee*, draft dated 2026-03-27) references **"a $3 billion demand from music publishers Universal, Concord, and BMG filed March 2026,"** which combined with the $1.5B author settlement brings **total known copyright exposure to ~$4.5B**; that report models a **$1B base-case reserve** for the March-2026 demand. **The bundle does not explicitly state whether this $3B March-2026 demand is a new escalation of the 2023 Music Publishers matter, an aggregation of the BMG/Music-Industry-Consortium matters, or a separate action** — presented as given, not merged.

### Security / safety disclosures (not litigation, but IP/safety-adjacent)

- **2026-03-19** — three high-risk vulnerabilities disclosed in Claude.ai
- **2026-04-21/22** — unauthorized Discord access incident affecting Mythos Preview
- **2026-07-30** — Anthropic's own red-team testing reports **three Claude models breached real-world systems** in cybersecurity tests

### IP / research assets

Constitutional AI methodology (foundational safety paper, published 2021-12-15); Claude architecture patents pending; Natural Language Autoencoders paper for activation interpretability (~May 2026).

### Adjacent industry litigation (context only — Anthropic is **not** a party; retained here because it appears in the Anthropic-filtered data as competitive context)

Musk v. Altman/OpenAI (distillation testimony, Musk lost on statute of limitations, verdict 2026-05-18); NYT v. OpenAI/Microsoft; Canada mass-shooting-victims v. OpenAI.

---

## (g) Active forecasts

**All 31 forecasts in `shared_forecasts` remain formally "Unresolved"** (`Resolution: Unresolved`, `Actual Outcome: null`) as of the data capture. Notably, **30 of the 31 carry test/resolution dates that have already passed** relative to "today" (2026-08-11) with no outcome or post-mortem ever logged — a tracking-staleness pattern distinct from, but similar in character to, the AIBQ score staleness noted above. Sorted by test date:

| ID | Forecast | P | Logged | Test date | Falsifier / invalidator | Status |
|---|---|---|---|---|---|---|
| 43 | Jupiter model announced GA at Code with Claude conference, May 6 | 0.78 | 05-05 | 2026-05-09 | Jupiter stays in red-teaming; conference has no model drop | Past due, unresolved |
| 18 | Named Fortune 500 Managed Agents customer disclosed within 30 days of Apr 21 | 0.50 | 04-21 | 2026-05-21 | Anthropic maintains media silence ahead of IPO | Past due, unresolved |
| 7 | Named enterprise customer discloses Managed Agents deployment within 30 days | 0.60 | 04-26 | 2026-05-26 | Media silence ahead of IPO | Past due, unresolved |
| 10 | Named Fortune 100 Managed Agents customer disclosed | 0.65 | 04-26 | 2026-05-26 | Media silence ahead of IPO | Past due, unresolved |
| 1 | Anthropic accepts a primary round of $550–700B (not $800B) by May 31 | 0.70 | 04-16 | 2026-05-31 | Accepts ≥$800B, accepts <$550B, or no round closes | Past due — later data shows Series H closed at $900B pre/$965B post, **outside** this band |
| 78 | Closes $30–50B round at $850–950B pre-money by May 31 | 0.80 | 05-13 | 2026-05-31 | Board delay or lead investor pulls out | Past due, unresolved |
| 86 | Closes $30B+ at $900B–1T pre-money by May 31 | 0.80 | 05-06 | 2026-05-31 | Investor demand softens | Past due, unresolved |
| 23 | Formal post-mortem on Mythos breach within 14 days | 0.35 | 04-22 | 2026-05-06 | Details kept under NDA given Glasswing defense partnerships | Past due, unresolved |
| 59 | ≥$900B valuation round within 30 days (of May 6) | 0.70 | 05-06 | 2026-06-05 | Board delay to Q3, or valuation <$800B | Past due, unresolved |
| 35 | Anthropic–DoD settlement framework within 30 days | 0.40 | 05-03 | 2026-06-02 | Adverse D.C. Circuit ruling first | Past due, unresolved |
| 67 | Closes $50B round at ≥$900B valuation by Jun 9 | 0.72 | 05-09 | 2026-06-09 | Lead investor withdraws over Musk relationship or DoD designation | Past due — plausibly consistent with the eventual Series H close (May 28, ahead of this date) |
| 70 | Closes $50B round AND announces formal JV entity name | 0.72 | 05-09 | 2026-06-09 | Musk exercises Colossus reclaim, or DoD ruling upheld | Past due, unresolved |
| 32 | Replicates NEC trust-intermediary model in a second sovereign market within 60 days | 0.50 | 04-25 | 2026-06-25 | Anthropic focuses only on Japan | Past due, unresolved |
| 75 | Closes $900B+ Series H before Jun 15 | 0.68 | 05-12 | 2026-06-15 | VIX shock >28, or DoD designation escalates | Past due — Series H closed 2026-05-28, ahead of this date |
| 25 | CONTRARIAN: "too dangerous" Mythos framing is commercial positioning; general API release within 60 days | 0.30 | 04-22 | 2026-06-22 | Strict Glasswing-only access maintained past Jun 22 | Past due, unresolved |
| 16 | Amazon earnings reveal Anthropic contract drawdown milestone | 0.50 | 04-21 | 2026-06-21 | Amazon omits Anthropic from commentary | Past due, unresolved |
| 20 | Amazon Q2 earnings reveals $20B commitment drawdown figure | 0.45 | 04-21 | 2026-06-21 | Amazon keeps financials confidential | Past due, unresolved |
| 38 | Anthropic–White House-mediated DoD settlement (30–45d) | 0.40 | 05-03 | 2026-07-02 | Adverse D.C. Circuit ruling before settlement | Past due, unresolved |
| 88 | CONTRARIAN: D.C. Circuit rules FOR Pentagon on supply-risk label within 45 days | 0.25 | 05-20 | 2026-07-04 | Panel requests further briefing | Past due — later data (Jul 30 ruling against the administration) is inconsistent with this contrarian call resolving YES |
| 5 | Publicly announces IPO plans (banker selection or S-1) by Jul 15 | 0.55 | 04-19 | 2026-07-15 | $800B VC round materializes instead, or DoD designation blocks >25% of pipeline | Past due, unresolved |
| 62 | Announce ≥$900B valuation round | 0.70 | 05-06 | 2026-07-05 | Board delay to Q3, or valuation <$800B | Past due, unresolved |
| 46 | Jupiter GA announced at May 6 conference | 0.78 | 05-05 | 2026-07-05 | No model announcement at conference | Past due, unresolved |
| 30 | S-1 gross-to-net ARR reconciliation creates material valuation re-rating | 0.45 | 04-24 | 2026-07-24 | Hyperscaler revenue structured as principal under ASC 606, no material gap | Past due, unresolved |
| 33 | EU AI Act enforcement triggers agent-tier disclosure inquiry within 90 days of Managed Agents GA | 0.30 | 04-25 | 2026-07-25 | EU enforcement prioritizes other provisions first | Past due, unresolved |
| 81 | Signs term sheet for $30–50B round at $900B+ | 0.80 | 05-13 | 2026-07-13 | Lead investor fails to materialize at $900B+ floor | Past due, unresolved |
| 89 | [Next Move] $30B+ round closes at $900B+ pre-money | 0.80 | 05-12 | 2026-07-19 | CNBC narrative accelerant fails to materialize | Past due, unresolved |
| 44 | $50B round closes at $850–950B, most valuable private company | 0.71 | 05-05 | 2026-06-30 | WTI >$115 and VIX >25 for 5+ consecutive sessions | Past due — plausibly consistent with the Series H outcome |
| 45 | CONTRARIAN: White House AI vetting EO becomes structural moat for Anthropic | 0.22 | 05-05 | 2026-08-05 | EO blocked/never signed, or imposes a flat moratorium on all labs equally | Past due, unresolved |
| **95** | **Files S-1 by Aug 31, accelerating from Oct target** | **0.55** | 05-20 | **2026-08-31** | DC Circuit rules against Anthropic, forcing timeline reset | **Not yet due** |
| 34 | CONTRARIAN: ad-free positioning breaks within 36 months as consumer revenue pressure mounts | 0.30 | 04-25 | 2029-04-25 | Remains 100% enterprise/API through Apr 2029; IPO prospectus commits to no advertising | Not yet due (long horizon) |

*Where this table notes a forecast as "plausibly consistent with" a later event, that is this analyst's observation only — NEXUS's own tracker has not logged an Actual Outcome or Brier Score for any of these 31 forecasts, and none is treated as resolved here.*

---

## (h) Notable events

`v2_master_events` holds **86 rows** (50 dated, 36 undated — largely near-duplicate news-aggregator headlines of already-dated events) and `timeline_dated_events` holds **733 dated rows** (191 Critical / 391 High / 128 Medium / 22 Low / 1 unlabeled), spanning 2020-11-01 through scheduled events as far out as 2026-12-31. The curated list below (~38 events) is selected by Importance/Significance field and chronological coverage; **the full log of both tables lives in `anthropic.json`.**

| Date | Event |
|---|---|
| 2021-01-01 | Anthropic founded (Dario Amodei, Daniela Amodei + 9 co-founders) |
| 2021-05-28 | Series A closes — $124M, $461M post-money |
| 2021-12-15 | Constitutional AI research published (foundational safety paper) |
| 2022-04-29 | Series B closes — $980M, $3.0B post-money |
| 2023-03-14 | Claude 1 launches publicly |
| 2023-05-23 | Google invests $300M — strategic cloud partnership begins |
| 2023-06-30 | Series C closes — $450M, $4.55B post-money |
| 2023-07-11 | Claude 2 released (100K context) and Claude.ai consumer product launches |
| 2023-09-01 | Amazon invests $1.25B — AWS strategic partnership announced |
| 2023-10-19 | Music Publishers v. Anthropic filed (earliest litigation in the data) |
| 2023-10-27 | Series D closes — $2.0B (Alphabet), $15.8B post-money |
| 2023-11-06 | Amazon completes full $4B commitment |
| 2024-03-04 | Claude 3 family launches (Haiku/Sonnet/Opus) |
| 2024-06-20 | Claude 3.5 Sonnet released, surpasses Opus on most benchmarks |
| 2024-07-01 | $4.0B round (Menlo-led) — $19.35B post-money |
| 2024-11-22 | $4.0B round (Amazon) — $15.53B post-money, a down round |
| ~Sep 2025 | Series F — $13B raised, $183B post-money (inferred date; see Section d) |
| 2025-03-12 | US federal use ban — Trump administration designates Anthropic a national-security risk |
| 2025-04-08 | BMG sues Anthropic for copyright infringement, $75M+ claim |
| 2025-10-15 | Music Industry Consortium (Universal/Sony/Warner) sues Anthropic |
| 2025-11-01 | Timeline event states ARR "reaches $14B" — in tension with the $9B end-2025 print and the Feb-2026 Series G statement (see conflict #16) |
| 2025-12-01 | Confidential IPO registration filed |
| 2026-02-12 | Series G closes ($30–30.6B, $380B post-money); Claude Code launches (80.8% SWE-bench); Claude 3.7 Sonnet ships |
| 2026-02-25 | Vercept (computer-use AI startup) acquired, acqui-hire |
| 2026-03-09 | Anthropic sues DoD over Supply Chain Risk designation |
| 2026-03-26 | SF judge grants preliminary injunction blocking the Pentagon designation |
| 2026-04-03 / 04-16 | Coefficient Bio acquired, ~$400M (drug-discovery AI) — two dates in source, both shown |
| 2026-04-07 | $30B ARR confirmed (Bloomberg), passes OpenAI in run-rate revenue; Broadcom/Google 3.5GW compute deal confirmed; Claude Mythos Preview announced |
| 2026-04-08 | DC Circuit declines to block the Pentagon designation (split ruling vs. Mar 26) |
| 2026-04-16 | Claude Opus 4.7 GA release; VC offers reportedly reach $800B valuation (Anthropic resisting) |
| 2026-04-20 | Amazon invests fresh $5B, commits $100B AWS spend over 10 years |
| 2026-04-24 | Google commits up to $40B ($10B upfront + $30B contingent) |
| 2026-05-06 | SpaceX/Colossus 1 compute deal announced — entire 300MW/222K-GPU cluster, $1.25B/mo through May 2029 (~$45B total) |
| 2026-05-19 | D.C. Circuit hears the substantive Anthropic v. Pentagon case |
| 2026-05-27 | AIBQ composite moves to 8.20 canonical (SpaceX-deal CI upgrade) |
| 2026-05-28 | Series H closes — $65B raised, $965B post-money, eclipsing OpenAI's prior valuation mark |
| 2026-06-12 / 06-19 | Commerce Dept / White House forces Anthropic to cut off foreign access to Mythos 5 / Fable 5 |
| 2026-07-01 | US Air Force mandates contractors cease using Anthropic by Sep 1, 2026 |
| 2026-07-03 | Models restored after a 20-day export-control dispute |
| 2026-07-06 | Anthropic–TeraWulf 20-year lease (~$19B, ~$950M/yr, 401MW) — CI review opened |
| 2026-07-20 | $1.5B Bartz v. Anthropic copyright settlement receives final court approval |
| 2026-07-30 | Judge rules the administration lacked evidence for the supply-chain-risk designation; same day, Anthropic discloses three Claude models breached real-world systems in its own red-team tests |
| 2026-08-04 | Anthropic signs $10B deal with AI cloud startup Volta |

---

## (i) Open conflicts / disputes

Nothing below is silently resolved. Where NEXUS itself has frozen a conflict or opened a sweep, that status is carried through verbatim.

1. **AIBQ composite:** 8.20 canonical (2026-05-27, verified 2026-07-16) vs. **8.06**, the figure NEXUS's own daily digest tracker has shown continuously from 2026-07-16 through its most recent entry (2026-08-10), despite an internal 2026-06-12 note attributing 8.06 to a stale-pipeline bug and re-affirming 8.20. See Section (b).
2. **ARR/revenue:** PitchBook field $30B TTM vs. SemiAnalysis ~$44B+ (2026-05) vs. Contrary Research $40B (end-Apr) vs. canonical $47B (now flagged STALE, past its quarterly decay window) vs. Dario Amodei's "80x growth" language (~$40–44B implied). NEXUS's own May-2026 data audit recommended adopting ~$44B as a Tier-B working estimate while flagging PitchBook's $30B as the last Tier-A read.
3. **Gross margin:** ~40% (WSJ/company model, T2/"leaked doc") vs. **70%+** ("inference infrastructure gross margin," SemiAnalysis/Bitget) — different bases (possibly inference-only vs. fully-loaded GAAP), unresolved pending audited S-1 financials.
4. **Valuation:** stale tracking tables still show $380B (Series G) as "latest" through their most recent 2026-08-11 entries, vs. the canonical **$965B** Series H mark (closed 2026-05-28, confirmed 2026-07-16), vs. a **$1.2T** secondary-market print reported 2026-07-10 — three different numbers depending on which table and basis you read.
5. **Total capital raised:** pre-Series-H figures range $60.55B–$75.55B across different tables/dates (timing and rounding, not obviously a single error) vs. post-Series-H canonical $124.3B equity-only / $161.3B including $37.0B debt.
6. **Headcount:** 2,500 (stale tracking tables, through 2026-08-11) vs. **5,000** (canonical, PitchBook 2026-04-21 datum, verified 2026-07-16).
7. **Active investor count:** 245 (Apr-2026 vintage) vs. 229 (Mar-2026 vintage) — both PitchBook-sourced, different pull dates.
8. **Funding-round bookkeeping oddities** (data-quality flags, not adjudicated): the "Series D" label is applied to two different rounds (2023 $2B Alphabet round and 2024 $4B Menlo round); "Series E2" (Nov 2024) precedes "Series E" (Mar 2025) chronologically; the Series B amount appears as both $980M (dated row, $3B post) and $580M (undated headline) elsewhere; "who led Series G" is answered three different ways across three tables (GIC/Coatue; Lightspeed; an eight-name list).
9. **Series G date:** the overwhelming majority of rows date the $380B/$30.6B close to **2026-02-12**, but at least one row dates the identical round to **2025-02-12** — a likely one-year data-entry error, not adjudicated here.
10. **CE cross-company basis conflict** — **FROZEN** in `canon_conflict_register` (opened 2026-07-16): naively comparing Anthropic's gross-basis CE (0.38x on $47B) to OpenAI's net-basis CE (0.14x on ~$25B) yields a misleading 2.71x raw ratio; the equalized comparison (Ruling 5, 39.75% factor) is **1.65x** (0.228x vs. 0.138x). "Never compare raw."
11. **Revenue multiple:** 20.5x gross ($965B/$47B) vs. **34.1x equalized** — identical to OpenAI's 34.1x once netted. Ruling 5 explicitly supersedes a "20.5x vs. 34.1x dislocation" framing that had already shipped in at least one prior NEXUS report; the sweep to correct every instance of that framing is still marked **Open** in `canon_sweep_tracker`.
12. **IPO confidential-filing date/value:** one row states Anthropic "confidentially files for IPO at $965 billion valuation" dated **2026-01-01** — which predates the Series H close (2026-05-28) that produced the $965B mark; the registration itself is elsewhere dated **2025-12-01** (pre-Series-H). The $965B tag on an early-2026 filing date looks retroactively/erroneously applied.
13. **Pentagon litigation:** genuinely split rulings between the SF federal court (injunction granted 2026-03-26) and the D.C. Circuit (separate injunction bid denied 2026-04-08) — the source itself describes this as creating "jurisdictional uncertainty," not a data error.
14. **Copyright settlement final-approval date:** given as both **2026-07-01** and **2026-07-20** — both shown, not adjudicated.
15. **Coefficient Bio acquisition date:** given as both **2026-04-03** and **2026-04-16** — both shown.
16. **"$14B ARR" dated 2025-11-01** (`timeline_dated_events`) sits in tension with the confirmed **$9B** end-2025 print (Bloomberg, 2026-01-21) and the company's own Series G statement that $14B was the run-rate "today" as of **2026-02-12**.
17. **Bear-case FCF margin sweep — Open:** Ruling 3 (effective 2026-06-12) states the bear-case FCF margin "was revised down significantly" and calls for a sweep of all talking points before reuse; the sweep is still marked Open, and the ~$559M Q2 2026 operating-profit figure is explicitly tagged "under FCF sweep review."
18. **Embargo compliance (standing instruction):** NEXUS's broader canonical-figures store tracks a cross-company quality-vs-valuation relationship across the whole Frontier Five cohort. **The correlation coefficient itself is embargoed from publication and is withheld here in full — neither its value nor its sign appears anywhere in this profile or its companion JSON.** The only cleared public expression of that relationship is the per-company $/AIBQ-point ladder (Anthropic ≈ $118B/point).

---

## (j) Sources

The companion JSON (`anthropic.json`) aggregates **1,466 rows** across **49 distinct NEXUS database tables** (four confirmed exact-duplicate table pairs were merged during cleaning; zero within-table exact duplicates were found). Programmatically extracting every non-Notion `Source URL` / `Source` / `Source Name` / link field across that dataset yields **687 distinct external source citations**. By outlet (top domains): TechCrunch (69), Google News aggregator (62), Bloomberg (60), Axios (46), anthropic.com company blog (39), PitchBook (28 direct links, plus numerous "Source: PitchBook" text citations without a URL), NYTimes (27), CNBC (25), Reuters (24), Fortune (22), plus SEC EDGAR filings, WSJ, Forbes, The Information, Politico, Ars Technica, and specialist research outlets (SemiAnalysis, Contrary Research, Sacra) among others. Named non-URL source labels add 19 further distinct citation types (PitchBook, Bloomberg, Reuters, "Dario Amodei at Morgan Stanley TMT Conference," "SEC — SpaceX S-1 Registration Statement," etc.).

This narrative also draws directly on six companion extracts supplied for this task: the Anthropic profile page (`profiles/anthropic.md`), the Command Center deep-dive (`command-center/deep-dive-anthropic.md`), two versions of the Framework AIBQ deep-dive (`framework/anthropic-aibq-deep-dive.md`), the May 6, 2026 NEXUS Data Audit (`pages/nexus-data-audit-2026-05-06.md`), the "$100 Billion Entry Fee" editorial draft (`pages/hundred-b-entry-fee-draft.md`), and the full canonical-figures export (`canon/canonical-figures.json`, 62 rows across all Frontier Five companies, of which 18 are Anthropic-specific and are folded into `anthropic.json`).
