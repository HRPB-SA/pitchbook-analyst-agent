# Databricks — NEXUS Intelligence Profile

**Slug:** databricks · **Tier:** Frontier Five · **PBID:** 59199-40 · **HQ:** San Francisco, CA · **Founded:** 2013
**Sector:** AI-PLAT (AI Platform) · **Stage:** S5 · **Quality Tier:** Elite
**Profile compiled:** 2026-08-11, from the NEXUS Databricks bundle (source bundle dated through 2026-08-11) plus the company profile page, the July 7, 2026 reconciliation log, the Command Center deep-dive, and the AIBQ framework deep-dive.

> **Embargo notice:** NEXUS computes a cross-company quality-vs-valuation relationship across its coverage cohort. That relationship — including any coefficient describing its strength — is embargoed from publication and does not appear anywhere in this profile or its companion JSON. Where cited source material characterized Databricks' figures in cross-company comparative terms, this profile reports Databricks' own figures only (see §(b) and §(i)).

---

## (a) Overview

Databricks was founded in 2013 in San Francisco by Ali Ghodsi, Ion Stoica, Matei Zaharia, and other UC Berkeley AMPLab researchers, built around Apache Spark, which the founding team created. The company's stated mission was to unify data analytics, AI, and machine learning on a single platform — the "lakehouse" architecture it has since made into a category name. Ghodsi moved from VP Engineering/Product into the CEO role in 2016, with Stoica moving to Executive Chairman.

Within NEXUS's Frontier Five coverage (Databricks, Anthropic, OpenAI, xAI/SpaceX, SSI), Databricks is the only company carrying a positive free-cash-flow position and the only one that has never required a foundation-model training budget to compete — its AIBQ Compute Independence (CI) dimension is scored with a +1.0 "AI-PLAT" platform modifier specifically because it deploys customer workloads across clouds (AWS, Azure, GCP) rather than training frontier models itself. It holds the highest AIBQ composite score of the group (§b) and, on a nominal-dollar basis, the lowest valuation of the group ($134B canonical vs. Anthropic/OpenAI in the hundreds of billions) — two separate, independently-sourced facts that this profile reports without characterizing any relationship between them (see embargo notice above).

Core product line: the Databricks Data Intelligence Platform (Lakehouse), Unity Catalog (governance), Mosaic AI (model training/serving), Databricks SQL / DBSQL (data warehousing), Lakebase (a Postgres-compatible operational database for AI applications, GA'd 2026), and a fast-growing agentic product family launched through 2026 (Genie One, Genie Code, Agent Bricks, CustomerLake, LTAP). Open-source lineage: Apache Spark (co-created), Delta Lake (open-sourced 2020), MLflow (open-sourced, 1M+ downloads), and Apache Iceberg (acquired via Tabular, 2023).

Leadership: Ali Ghodsi (CEO since 2016), Ion Stoica (Executive Chairman, co-founder), Matei Zaharia (co-founder; won the ACM Computing Prize for AGI-adjacent work, announced April 8, 2026). Simon Davies was appointed SVP & GM for Asia Pacific & Japan (January 20, 2026). Lee Stockwell is logged as a recent (~90-day) key hire in the most recent company-financials refresh (extracted 2026-08-10). A CFO identity — David Conte, previously of Splunk — appears in NEXUS's own reconciliation log but is explicitly flagged there as **Medium confidence, unverified, to be confirmed before external citation**; this profile repeats that caveat rather than stating it as fact.

Headline scale metrics as of the most current disclosures (see §c for full detail and dating): **$6.9B annualized revenue run-rate (+80% YoY, as of June 16, 2026)**, gross margin 74% and guided lower, free-cash-flow positive for 12+ consecutive months, ~8,000–9,000 employees (sources disagree, see §i), 20,000+ organizations on the platform per NEXUS's most recent PitchBook-sourced count (legacy trackers still show a stale 10,000 figure — see §i), and a $134B closed valuation with a further $165–188B in reported-but-not-yet-closed/not-yet-ratified financing activity through mid-2026 (see §d).

---

## (b) Current scores — AIBQ Composite

NEXUS scores Databricks under the **AIBQ** framework (AI Business Quality), not PBQ — PBQ is a structurally-identical sibling framework used for companies outside AIBQ's sector coverage (it swaps the Compute Independence dimension for "Strategic Velocity"); nothing in the Databricks source material scores the company under PBQ.

### Current (canonical)

| Field | Value |
|---|---|
| **AIBQ Composite** | **8.81** (Elite) |
| **As of / ratified** | **July 7, 2026** (ad hoc ratification session; delegated ratification, not a routine Morning Digest cycle) |
| CE — Capital Efficiency | 8.9 |
| RQ — Revenue Quality | 9.0 |
| CI — Compute Independence | 8.0 |
| GO — Governance Optionality | 8.9 |
| MD — Moat Durability | 9.0 |
| CRA (Compounding Risk Adjustment) | 0 (no penalty triggered) |
| DAI (Data Availability Index) | HIGH |
| Confidence | High — Confirmed |
| Freshness | Current (as of ratification) |
| Prior composite | 8.92 (see below) |
| Composite change | −0.11 |
| Score gap to #2 in Frontier Five (Anthropic, 8.20) | 0.61 composite points |

Databricks' own $/AIBQ-point figure: **$15.2B per point** at the $134B canonical valuation (8.81 composite); **$19.3B per point** if computed against the unclosed $165–175B rumored round instead. These are reported here as Databricks-only metrics, per the embargo notice above — no comparison to any other company's $/point figure, and no characterization of how efficiently-priced this makes Databricks relative to peers, is made in this profile.

### Immediate prior (superseded)

| Field | Value |
|---|---|
| AIBQ Composite | 8.92 (Elite) |
| As of | May 27, 2026 (the reconciliation log's own baseline mark) |
| CE / RQ / CI / GO / MD | 9.0 / 9.0 / 8.0 / 9.0 / 9.0 |

### What moved between May 27 and July 7, 2026

- **CE (net −0.1, 9.0→8.9):** CE-1 (Efficiency Index) rose 9.0→9.5 on the June 16 DAIS disclosure ($6.9B run-rate, +80% YoY; Efficiency Index recomputed 0.52→0.56). CE-2 (gross-margin band) fell 9.0→8.0 on the same disclosure's 74% gross margin print (down from >80%), which dropped a full ratings band; a single-event cap capped the move at −1.0 raw. Net CE dimension effect, after S5 reweighting: −0.1.
- **GO (−0.1, 9.0→8.9):** GO-3 (IPO/Exit Readiness) moved 8.0→7.5 after CEO Ali Ghodsi ruled out a 2026 listing on Bloomberg TV (June 4, 2026: "2026 is a terrible year to go public"). This was adjudicated as a **half-cap** move (−0.5, not the full −1.0 initially proposed): NEXUS's own adjudication reasoning is that GO-3's bands are state-based (audits underway, bankers engaged, public-company-caliber CFO in place, SOX process underway) and that state was unchanged by the announcement — only the *intent timeline* moved, and even that was substituted with an active, still-open path to liquidity (the $165–175B round then in talks, plus active secondaries). The decomposition offered: the prior 8.0 was 7.5 "state floor" + 0.5 "imminence premium" tied to an H2-2026 S-1 expectation; the premium was removed and the floor held.
- **RQ, CI, MD (unchanged):** No qualifying events under NEXUS's "distinct pathway" / "second-order evidence" rules. The June 16 Panther acquisition (security-sector M&A) and a "Genie Ontology" product item were both explicitly held at Δ0 pending integration evidence.
- **Capital-basis correction (data correction, not a score-moving event):** The July 7 reconciliation also corrected the capital-raised basis from a blended $33.1B figure to $20.2B equity-only (see §d and §i) — NEXUS's own note is explicit that this "strengthens CE-4 at existing 9 and removes the 'capital quality, not the ratio' crutch from the CE narrative," i.e., it improved the analytical basis without itself moving a sub-score.

### Methodology note

Sub-score decompositions for the "same" 8.92 composite differ depending on which tracked table is consulted: a separate, earlier-vintage tracking lineage (informally labeled "v2.2" in the source data, run daily from February 27 through May 27, 2026) reached 8.92 via CE 9.0 / RQ 9.3 / CI 7.0 / GO 8.7 / MD 10.0 — a different five-way split than the CE 9.0/RQ 9.0/CI 8.0/GO 9.0/MD 9.0 breakdown the July 7 reconciliation cites as its own "May 27 canonical marks." The numeric composite is continuous across what appears to be a rubric rewrite; the sub-scores are not. This profile follows the reconciliation log's own framing (which the assigning brief for this profile designated as the single most authoritative source) for both the current and prior figures. Full detail in §(i) and in the companion JSON's `_meta.known_data_quality_flags`.

---

## (c) Financials

All figures dated; where the source disagrees with itself, both figures are shown (see also §i for a fuller data-quality discussion).

### Revenue / ARR ladder (company-wide annualized run-rate)

| As of | ARR | YoY growth | Source / tier |
|---|---|---|---|
| 2022A | ~$800M (est.) | — | PitchBook reconstruction, T2 |
| Jan 2023 | ~$1.0–1.2B | — | Crossed $1B ARR milestone |
| 2023A | ~$1.6B (est.) | — | PitchBook reconstruction, T2 |
| 2024A | ~$2.4B | — | PitchBook / Series L prep materials, T2 |
| ~Jan 2025 | $3.7B | — | Alongside a $100B valuation mark |
| Sep 2025 | $4.0B | +50% | Ladder rung, T2 |
| Dec 2025 | $4.8B | +55% | Ladder rung, T2 |
| **Feb 9, 2026** (Series L close) | **$5.4B** | **+65%** | Company press release / PitchBook, T2 — this was canonical until superseded below |
| **Jun 16, 2026** (DAIS keynote) | **$6.9B** | **+80%** | **CURRENT CANONICAL.** Ali Ghodsi on stage at Data + AI Summit; CNBC, Bloomberg-adjacent coverage; PitchBook. T2 |

Component breakdown at the June 16, 2026 print: **AI products $1.7B**; **DBSQL (Databricks SQL / data-warehousing line) $1.5B** (this line itself crossed a $1.0B run-rate milestone around January 2025 and is described as having "doubled" per Bloomberg's June 16 headline); **Lakebase** (the newer Postgres-for-AI-agents product, GA'd 2026) is reported "ramping at 2x DBSQL's pace at the same stage," without a standalone dollar figure disclosed.

**Do not confuse the $1.5B DBSQL sub-line with total company ARR** — a stale/miscalibrated daily tracker in the underlying data conflates the two; see §(i).

### Margins and cash generation

- **Gross margin: 74%**, down from an implicit >80% pre-disclosure level, **guided lower** by Ghodsi as agentic workloads multiply the number of underlying model queries per unit of customer intent (disclosed June 16–17, 2026, DAIS). NEXUS's own internal trigger: gross margin below 70% would break the "Efficiency-Index gate" (the FCF-positive / growth>40% / GM>70% combination that keeps Databricks in its top capital-efficiency scoring band) — armed but not tripped as of this profile's compile date.
- **Free cash flow: positive for 12+ consecutive months** as of Q1 2026 — Databricks is described across multiple sources as the only FCF-positive company in NEXUS's Frontier Five coverage. The actual FCF dollar figure is **not publicly disclosed**; NEXUS's own scoring model carries it at an analyst estimate of roughly 7.5% of revenue for index-calculation purposes, flagged to be firmed up at the next print.
- **Revenue multiple:** 19.4x (at $134B valuation ÷ $6.9B run-rate) — current; 24.8x was the prior figure (at $134B ÷ $5.4B) before the ARR correction. At the unclosed $165–175B rumor mark, the multiple would sit around 23.9–25.4x; NEXUS's own tracking separately notes the multiple is "effectively flat" across the run-rate correction because valuation and revenue moved together.

### Operating scale

| Metric | Value | As of / source |
|---|---|---|
| Employees | **9,000** | Per the July 7 reconciliation's Ops bullet (PitchBook, Jun 9, 2026) |
| Employees (alternate) | 8,000 | Multiple daily trackers, consistently through Aug 11, 2026 — see §(i) |
| NRR | **>140%** | Per the July 7 reconciliation's Ops bullet (PitchBook, Jun 9, 2026) |
| NRR (alternate) | 130% | Trackers dated ~Jun 1, 2026 |
| Organizations on platform | **20,000+** | Per the July 7 reconciliation's Ops bullet (PitchBook, Jun 9, 2026) |
| Customer count (alternate) | 10,000 | Daily tracker, as recently as the Aug 11, 2026 snapshot — see §(i) |
| Fortune 500 penetration | 70% | Jul 7 reconciliation Ops bullet |
| Customers with $1M+ ACV | 800+ | Jul 7 reconciliation Ops bullet |
| Customers with $10M+ ACV | 70+ | Jul 7 reconciliation Ops bullet |
| Enterprise revenue mix | 95% | Company-financials tracker |
| Customer concentration | ~5% (low) | Company-financials tracker |
| Revenue per employee | ~$771K | 2025E estimate, NEXUS Companies DB sync (Mar 2026) — dated prior to the ARR/headcount corrections below and not re-derived against $6.9B/9,000; treat as stale |

---

## (d) Valuation & funding history

**Methodology note (applied per this profile's house rule): capital-efficiency denominators use equity only. Debt is tracked separately below and informs risk, not the CE ratio.**

### Valuation status (as of profile compile date, 2026-08-11)

| Mark | Amount | Status | Source |
|---|---|---|---|
| Series L, closed | **$134B** post-money | **CANONICAL / closed** | PitchBook 59199-40; company press release; closed Feb 9, 2026 |
| 13th round, in talks | $165–175B | **Unclosed rumor — not adopted as canonical** | The Information, Jun 9, 2026 (T3); PitchBook status field 334745-56T |
| Further financing report | ~$188B post-money, ~$3B raised, Coatue-led | **Reported by multiple named outlets — NOT yet swept into NEXUS canonical figures** | Databricks' own newsroom press release, Bloomberg ("Coatue leads Databricks funding round at $188 billion valuation," Jul 17, 2026), TechCrunch (Jul 17, 2026); reported closing window ~Jul 16–17, 2026 |

On the $188B item specifically: this is reported through Databricks' own newsroom plus Bloomberg and TechCrunch — materially better-sourced than a rumor — but it **postdates** the July 7 reconciliation (not addressed there) and, as of the most recent NEXUS canonical-figures compile captured in this bundle (July 21, 2026), was **still tagged "T5 unconfirmed"** internally and flagged only as a "refresh trigger," not ratified. Clear Street, a secondary-market platform, is separately reported (July 31, 2026; CNBC) to have opened pre-IPO retail/accredited-investor access to Databricks shares referencing the $188B figure. This profile treats $134B as the canonical closed mark and reports the $165–175B and $188B figures as open, unratified signals — consistent with NEXUS's own stated discipline of never anchoring a base case to an unclosed round. See §(i) for the full open-item writeup.

### Equity funding round history

| Round | Date | Amount raised | Post-money | Lead / notable investors |
|---|---|---|---|---|
| Series A | 2013-09-24 | $14M | $47M | a16z |
| Series B | 2014-06-30 | $33M | $923M | NEA |
| Series C (down round) | 2016-12-15 | $60M | $560M | NEA; In-Q-Tel (US intelligence community) — a down round from the $923M Series B mark |
| Series D | 2018-09-25 | $140M | $985M | a16z |
| Series E | 2019-01-11 | $250M | $2.75B | a16z; Microsoft (strategic) |
| Series F | 2019-10-22 | $400M | $6.2B | a16z; Microsoft, Coatue, Tiger Global, T. Rowe Price, BlackRock |
| Series G | 2021-02-09 | $1.0B | $28B | Franklin Templeton; AWS, Salesforce, Microsoft, GIC, CPP Investments (26 investors) |
| Series H | 2021-08-31 | $1.6B | $38B | Counterpoint Global (Morgan Stanley) (31 investors) |
| Series I | 2023-11-13 | $685M | $43.2B | T. Rowe Price; NVIDIA, Capital One, AT&T (21 investors) |
| Series J | 2024-12-17 | $10.2B | $62B | Thrive Capital, GIC, Insight Partners, a16z, DST Global (32 investors incl. Meta, AT&T, QIA, Temasek) |
| Series K | ~Aug 2025 | $1.0B | $100B+ | — |
| **Series L** | **2026-02-09** | **$5.0B equity** (+ $2.0B debt capacity, $7.0B total infusion) | **$134B** ($129B pre) | Insight Partners, Fidelity, JPMAM (leads); Microsoft, a16z, BlackRock, Blackstone, Coatue, GIC, MGX, NEA, OTPP, JPMC Strategic Investment Group, Goldman Sachs Growth Equity, Glade Brook, QIA, T. Rowe Price, Temasek, Thrive Capital |
| 13th round | rumored, unclosed | — | $165–175B talked | The Information, Jun 9, 2026 |
| Further round (unratified) | ~Jul 16–17, 2026 | ~$3B | ~$188B | Coatue-led per Databricks newsroom / Bloomberg / TechCrunch |

**Cumulative equity raised (CANONICAL, ratified Jul 7, 2026): $20.2B.** PitchBook decomposition (59199-40): $13.9M (A) + $33.4M (B) + $60M (C) + $140M (D) + $250M (E) + $400M (F) + $1.0B (G) + $1.6B (H) + $684.6M (I) + $10.06B (J) + $1.0B (K) + $5.0B (L) ≈ $20.2B.

### Debt / credit facilities (tracked separately — never part of the capital-efficiency denominator)

| Facility | Amount | Date | Notes |
|---|---|---|---|
| Embedded in Series J | ~$0.17B | 2024 | Component of the J-round capital structure |
| Senior secured credit facility | $5.25B | 2025-01-14 | $2.25B term loan + $2.5B revolving credit + $500M delayed draw; lenders Ares, Blue Owl, Blackstone, New Mountain |
| Refinancing | $0.05B | ~Dec 2025 | — |
| New facility | $1.8B | 2026-01-23 | JPMorgan and Citi enter as new lenders |
| Series L debt tranche | $2.0B | 2026-02-09 | Attached to the Series L equity raise |
| **Total debt (canonical, Jul 7, 2026)** | **~$9.3B** | | Sum of the above (≈$9.27B) |

**PB total (equity + debt): $29.5B** ($20.2B equity + $9.3B debt). **Retired figures — no longer in use:** a prior $33.1B "cumulative raise" figure and a ~$38B "May 28 refresh" figure were both retired on July 7, 2026; NEXUS's own note is that "neither matches any PitchBook basis."

**Open discrepancy on the January 2026 debt facility:** a separate tracker (the daily company-financials feed) describes a "$5.45B debt (Jan 2026): $3.65B revolver + $1.15B revolver + $650M delayed draw term loan. On top of $2B debt from Series L" — a different amount and structure than the $1.8B JPM/Citi facility the canonical debt ladder above attributes to January 2026. The two do not reconcile in the source data; both are reported here rather than silently resolved (see §i).

### Capital efficiency (equity-only, per house methodology)

| | Numerator (ARR) | Denominator (equity raised) | Ratio |
|---|---|---|---|
| **Current (canonical, Jul 7, 2026)** | $6.9B | $20.2B | **0.34x** |
| Prior (blended, pre-correction) | $5.4B | $33.1B (blended equity+debt) | 0.16x |

The roughly 2x jump in the reported ratio (0.16x → 0.34x) reflects **two stacked corrections**, not one: the ARR numerator moved from the stale $5.4B print to the current $6.9B print, *and* the denominator moved from a blended $33.1B figure (which had silently combined equity and debt) to the $20.2B equity-only figure. Isolating each effect: revenue-only would have taken the ratio to roughly 0.21x ($6.9B/$33.1B); capital-basis-only would have taken it to roughly 0.27x ($5.4B/$20.2B). For reference only, and explicitly **not** the capital-efficiency metric under this profile's house rule: ARR against the debt-inclusive PB total of $29.5B would be 0.23x — debt informs risk, never capital efficiency.

---

## (e) Cap table & investors

**Board composition:** Ali Ghodsi, Ion Stoica, plus board seats held by a16z and NEA.

**Notable investor rights:** a16z and NEA each hold a full board seat. Standard Series L preferred liquidation preference structure. IPO ratchets are considered likely for late-stage investors who entered at the 2021 peak mark ($38B, Series H) given the subsequent down-then-up valuation path. FCF-positive status is noted (legacy tracker commentary) as removing forced-dilution risk relative to peers that must keep raising to fund losses.

**Investor roster across the company's history** (see §d for round-by-round detail): a16z (Series A, D, E, F lead across multiple rounds; board seat), NEA (Series B, C leads; board seat), In-Q-Tel (Series C — notable as a US-intelligence-community-affiliated investor), Microsoft (strategic, Series E onward), Coatue (Series F; also reported as leading the unratified ~$188B mid-2026 round), Tiger Global and T. Rowe Price (Series F, later T. Rowe also leads Series I), BlackRock (Series F), Franklin Templeton (Series G lead), AWS, Salesforce, GIC, CPP Investments (Series G), Counterpoint Global / Morgan Stanley (Series H lead), NVIDIA, Capital One, AT&T (Series I), Thrive Capital, Insight Partners, DST Global, Meta, QIA, Temasek (Series J — Thrive/GIC/Insight/a16z/DST co-leads), and the Series L syndicate: Insight Partners, Fidelity, and JPMAM (co-leads) plus Microsoft, a16z, BlackRock, Blackstone, Coatue, GIC, MGX, NEA, OTPP, JPMC Strategic Investment Group, Goldman Sachs Growth Equity, Glade Brook, QIA, T. Rowe Price, Temasek, and Thrive Capital.

Legacy tracker commentary separately names **Coatue as "leading investor"** in a general strategic-investor-stakes field (undated within that record, but consistent with Coatue's reported role leading the unratified July 2026 ~$188B round).

**Secondary market / retail access:** Clear Street, a private-market brokerage platform, is reported (per CNBC and other coverage, July 31, 2026) to have opened accredited-investor access to Databricks shares, referencing the $188B figure. A separate item (Benzinga, May 2026) notes a high-profile pre-IPO secondary position (reported "up 302%") as an illustration of retail/political-figure interest in pre-IPO Databricks exposure; included here as a market-color data point, not a cap-table fact.

---

## (f) Litigation & IP

**Litigation:**
- **DBRX training-data copyright lawsuit** — an ongoing lawsuit brought by authors alleging Databricks used copyrighted material to train its DBRX open-source model, first logged around April 29, 2026 and still described as "ongoing" as of a May 1, 2026 update, which characterizes the potential damages sought as **"extraordinary."** No resolution, ruling, or settlement is recorded in this bundle as of the profile compile date.
- **Abbott third-party security incident** — logged June 15, 2026: "Databricks platform accessed in Abbott security breach via compromised Microsoft Entra account." As sourced, this describes Databricks infrastructure being reached by an attacker who had already compromised a Microsoft Entra (Azure AD) credential at or for Abbott (the affected party) — i.e., the source material frames this as third-party credential compromise reaching into a Databricks-hosted environment, not a disclosed Databricks-side platform vulnerability. No NEXUS score impact is logged against this item, and no further detail (regulatory response, disclosure requirements, litigation) appears in this bundle.
- A low-importance, non-legal item logged July 13, 2026 mentions Databricks alongside other defense-adjacent technology companies in press coverage of Trump-family investment activity; included here for completeness but it is not a Databricks-specific legal or regulatory event.

**IP / open-source portfolio:**
- **Apache Spark** — co-created by the founding team; commercialized by Databricks.
- **Delta Lake** — open-sourced by Databricks in 2020; the storage layer (ACID transactions on data lakes) that underpins the "lakehouse" architecture category Databricks popularized.
- **MLflow** — open-sourced ML lifecycle platform; reached "1.0" in September 2020; cited at over 1 million downloads.
- **Apache Iceberg** — acquired into the Databricks portfolio via the 2023 Tabular acquisition (see §h); positioned against Snowflake's competing open-table-format strategy.

No trademark, patent, or additional IP-litigation items beyond the above appear in this bundle.

---

## (g) Active forecasts

NEXUS carries 18 open (unresolved, as of this bundle) forecast entries specific to Databricks — overwhelmingly concentrated on IPO-process timing. All probabilities below are as originally logged; none have resolved as of the profile compile date, and none should be read as updated for the July 2026 IPO-timeline correction (§b, §i) unless the forecast's own logged date is after June 4, 2026.

| Logged | Forecast | Test date | Probability | Status |
|---|---|---|---|---|
| 2026-04-16 | Databricks files S-1 before Anthropic accepts a primary round, by Jul 15, 2026 | 2026-07-15 | 0.65 | Unresolved |
| 2026-04-19 | Databricks files S-1 / confidential filing by May 15, 2026 | 2026-05-15 | 0.72 | Unresolved |
| 2026-04-21 | S-1 or banker selection reported by May 21, 2026 | 2026-05-21 | 0.55 | Unresolved |
| 2026-04-21 | IPO process formalized within 30–60 days | 2026-06-21 | 0.55 | Unresolved |
| 2026-04-22 | IPO banker selection reported within 30 days | 2026-05-22 | 0.50 | Unresolved |
| 2026-04-23 | S-1 filed or banker named by Jul 23, 2026 | 2026-07-23 | 0.65 | Unresolved |
| 2026-04-24 | S-1 filed or banker selection confirmed by Jul 24, 2026 | 2026-07-24 | 0.60 | Unresolved |
| 2026-04-26 | S-1 or banker mandate (Goldman/Morgan Stanley) confirmed by Jul 26, 2026 | 2026-07-26 | 0.65 | Unresolved |
| 2026-04-26 | Banker selection reported within 30–60 days | 2026-06-26 | 0.60 | Unresolved |
| 2026-05-03 | Lakebase ARR announcement positioning S-1 readiness | 2026-07-02 | 0.70 | Unresolved |
| 2026-05-03 | S-1 filed before Sep 1, 2026, at a $150–180B range | 2026-09-01 | 0.65 | Unresolved |
| 2026-05-05 | Databricks announces $6B+ ARR confirmation | 2026-07-05 | 0.55 | Unresolved |
| 2026-05-06 | Confidential S-1 filing for H2 2026 IPO | 2026-07-31 | 0.50 | Unresolved |
| 2026-05-09 | IPO roadshow or S-1 filing within 60 days | 2026-07-08 | 0.45 | Unresolved |
| 2026-05-12 | Databricks IPOs before Anthropic in 2026 (contrarian) | 2026-10-15 | 0.35 | Unresolved |
| 2026-05-13 | Confidential S-1 filing via Goldman/Morgan Stanley | 2026-07-13 | 0.55 | Unresolved |
| 2026-05-13 | S-1 submission (SEC EDGAR) | 2026-07-15 | 0.55 | Unresolved |
| 2026-05-20 | DAIS (Jun 15–18) features IPO-readiness signals | 2026-06-18 | 0.85 | Unresolved (DAIS did occur and did carry the $6.9B disclosure — see §h — but this bundle does not carry a formal resolution/Brier-score entry for the forecast itself) |

Every one of these forecasts predates Ghodsi's June 4, 2026 on-air statement ruling out a 2026 listing (§b, §h); most (all with test dates after June 4) are consequently very likely to resolve NO on a strict S-1-by-date reading, though several use OR conditions (banker selection, confidential filing) that could still resolve favorably even without a public listing in 2026. This bundle does not contain post-June-4 resolution data or updated Brier scores for any of them — flagged as an open item rather than adjudicated here.

---

## (h) Notable events (curated)

NEXUS's underlying event log carries **240 dated, Databricks-tagged entries** across two tracked tables: 25 in a curated "master events" seed table (2013–2025, fully verified, one row per underlying event) and 215 in a larger auto-ingested "timeline" table (2013–2027, extensively duplicated — the same underlying event is frequently logged multiple times with different headline phrasing from different aggregators, especially around the February 2026 Series L close, the June 2026 DAIS disclosures, and the July 2026 $188B reports). Four additional rows in the timeline table did not mention Databricks at all (Perplexity AI, an AI-leaderboard startup, and two unrelated SEC filers) and were excluded as out-of-scope rather than counted here; they are preserved, labeled, in the companion JSON's `_excluded_out_of_scope` array. **The full 240-entry log — every headline variant, all fields — is preserved in `databricks.json`.** What follows is a curated selection of roughly the top 35 by significance, one line per underlying event:

1. **2013-01-01** — Databricks founded by Ali Ghodsi, Ion Stoica, Matei Zaharia and other UC Berkeley AMPLab researchers, built around Apache Spark. *(Critical)*
2. **2013-09-24** — Series A: $14M led by a16z at $47M post-money — first external funding. *(High)*
3. **2016-01-01** — Ali Ghodsi becomes CEO; Ion Stoica moves to Executive Chairman. *(High)*
4. **2016-12-15** — Series C: $60M led by NEA at $560M post-money — a **down round** from the $923M Series B mark; In-Q-Tel (US intelligence community) invests. *(High)*
5. **2020-01-01** — Delta Lake open-sourced — becomes the foundation of the "data lakehouse" architecture. *(High)*
6. **2020-09-01** — MLflow reaches 1.0 — becomes an ML-lifecycle industry standard; 1M+ downloads. *(High)*
7. **2021-02-09** — Series G: $1.0B led by Franklin Templeton at $28B post-money; revenue growth 112% YoY. *(Critical)*
8. **2021-08-31** — Series H: $1.6B led by Counterpoint Global (Morgan Stanley) at $38B post-money. *(Critical)*
9. **2022-06-01** — Acquires MosaicML for ~$1.3B — positions Databricks as an end-to-end AI platform competing with OpenAI/Anthropic for enterprise AI workloads. *(Critical)*
10. **2023-01-01** — Crosses $1B ARR milestone. *(Critical)*
11. **2023-03-28** — Releases Dolly, a cheap-to-build (~$30 of compute) open-source instruction-following LLM — precursor to DBRX. *(High)*
12. **2023-09-26** — Acquires Tabular (the Apache Iceberg company) for ~$2B — secures open-table-format leadership against Snowflake. *(Critical)*
13. **2023-11-13** — Series I: $685M led by T. Rowe Price at $43.2B post-money; revenue $1.9B, +58% YoY. *(Critical)*
14. **2024-03-27** — Releases DBRX, a 132B-parameter open-source LLM trained for ~$10M, outperforming GPT-3.5/Llama 2/Mixtral on most benchmarks. *(High)*
15. **2024-12-17** — Series J: $10.2B led by Thrive Capital/GIC/Insight Partners/a16z/DST Global at $62B post-money — the largest round in company history to that point; revenue $3.0B (FY2024), FCF-positive for 12+ months. *(Critical)*
16. **2025-01-14** — $5.25B senior secured debt facility (Ares, Blue Owl, Blackstone, New Mountain). *(High)*
17. **~2025-08-01** — Series K: $1.0B at $100B+ valuation. *(Critical)*
18. **2026-01-23** — New $1.8B debt facility; JPMorgan and Citi enter as lenders. *(High)*
19. **2026-02-09** — **Series L closes: $5B equity + $2B debt capacity ($7B total) at $134B post-money**, led by Insight Partners/Fidelity/JPMAM. Revenue at close: $5.4B run-rate, +65% YoY, FCF-positive. *(Critical)*
20. **2026-03-11** — Genie Code launches — autonomous data agent, 2x benchmark performance vs. leading coding agents. *(High)*
21. **2026-03-15** — Acquires Quotient AI (AI evaluation tooling). *(Medium/High)*
22. **2026-03-17** — Accenture Databricks Business Group launches — 7th consecutive Partner-of-the-Year recognition. *(High)*
23. **2026-03-24** — Launches Lakewatch (agentic SIEM/security product); acquires Antimatter and SiftD.ai (Databricks' first and second security-sector M&A deals); Anthropic partnership deepens around Lakewatch. *(High)*
24. **2026-04-08** — Co-founder Matei Zaharia wins the ACM Computing Prize. *(High)*
25. **2026-04-16** — Customer-managed keys for model serving + ABAC reach general availability — read internally as an IPO-readiness signal. *(High)*
26. **2026-04-29** — Ongoing author copyright lawsuit over DBRX training data continues, with potential "extraordinary" damages reported. *(High)*
27. **2026-06-04** — **CEO Ali Ghodsi rules out a 2026 IPO on Bloomberg TV** ("a terrible year to go public") — 2026 listing explicitly off the table, 2027 earliest. *(Critical)*
28. **2026-06-09** — Databricks reported in talks to raise at a **$165–175B valuation** (The Information) — a 13th financing round, unclosed. *(High)*
29. **2026-06-15** — Databricks platform accessed in a third-party (Abbott) security breach via a compromised Microsoft Entra account. *(High)*
30. **2026-06-16** — **Data + AI Summit 2026: annualized revenue disclosed at $6.9B, +80% YoY; gross margin disclosed at 74%, guided lower** (Ghodsi, on stage; CNBC/Bloomberg coverage) — the single most consequential disclosure day in this profile's coverage window, driving the AIBQ CE-1/CE-2 moves detailed in §b. Same day: Panther (AI-native SOC, ~$1.4B last mark, terms undisclosed, clearance pending) announced as Databricks' third security-sector acquisition; Genie One (agentic "AI coworker"), CustomerLake (agentic CDP), and the LTAP architecture (unifying OLTP/OLAP) all launch; DBSQL/data-warehousing line separately confirmed past $1.5B annual run-rate. *(Critical)*
31. **2026-07-06/08** — Genie products shift to a pay-as-you-go pricing model (150 DBUs of free monthly LLM usage). *(Medium)*
32. **2026-07-07** — **NEXUS ratifies the AIBQ reconciliation: composite moves 8.92 → 8.81**; capital-raised basis corrected to $20.2B equity-only (+ ~$9.3B debt); full detail in §b/§i. *(Critical, internal/methodological — not a market event but the profile's own key correction date)*
33. **2026-07-16/17** — Reported ~$3B raised at an ~$188B valuation, Coatue-led (Databricks newsroom; Bloomberg; TechCrunch) — not yet ratified into NEXUS canonical figures as of this bundle's most recent compile (Jul 21, 2026). *(Critical per source tagging, but explicitly unverified in NEXUS's own pipeline — see §i)*
34. **2026-07-23** — Microsoft and Databricks extend their Azure partnership into the 2030s (including expanded custom-chip usage). *(High)*
35. **2026-07-31** — Clear Street opens a pre-IPO secondary-access platform for accredited investors referencing the $188B figure. *(High)*

Runner-up items excluded from the top-35 for space (all present in full in the JSON): the Series D/E/F equity rounds (2018–2019), the Redash acquisition (2021), MosaicML-adjacent product news, the ~20 monthly Databricks Runtime / platform release-note entries logged through 2026 (routine and low-importance), roughly a dozen partner-of-the-year and systems-integrator award announcements, the Australia/New Zealand $300M investment announcement (May 5, 2026), and a same-former-employee item (a former Databricks AI chief releasing an unrelated image-generation model, June 25, 2026 — talent-flow-adjacent but not a Databricks corporate action).

---

## (i) Open conflicts / disputes / corrections

The July 7, 2026 reconciliation log is the authoritative correction record for this profile. It documents seven canonical corrections in one pass (project-context v3.3 → v3.4), each shown here as **was → now**:

| # | Figure | Was (superseded) | Now (canonical, Jul 7 2026) | What changed it |
|---|---|---|---|---|
| 1 | Run-rate | $5.4B, +65% YoY (as of Jun 12, 2026 pull) | **$6.9B, +80% YoY** | Ghodsi at DAIS, Jun 16, 2026; CNBC — T2 |
| 2 | Revenue multiple | 24.8x | **19.4x** at $134B (24.6–25.4x range at the $170B rumor mark) | Derived from #1 |
| 3 | Cumulative capital raised | $33.1B [prior canonical] / ~$38B [a May 28 refresh figure] | **$20.2B equity-only**, $29.5B PB total incl. ~$9.3B debt | PitchBook 59199-40 deal-by-deal decomposition — both prior figures explicitly "retired," neither matched any PitchBook basis |
| 4 | Capital efficiency | 0.16x (blended) | **0.34x (equity-only)** | Derived from #1 and #3 together — see the stacked-correction breakout in §d |
| 5 | IPO timeline | H2 2026 (pipeline target) | **2027 earliest; 2026 explicitly ruled out** | Ghodsi, Bloomberg TV, Jun 4, 2026 |
| 6 | Gross margin | >80% (implicit, undisclosed exact figure) | **74%, guided lower** | DAIS, Jun 16–17, 2026 |
| 7 | Valuation | $134B | $134B **holds** as the canonical closed mark; a 13th-round rumor of $165–175B is tracked separately, unclosed | The Information, Jun 9, 2026 (T3) |

**Items this profile surfaced beyond the reconciliation log itself**, from cross-referencing the fuller data bundle (all detailed with dates and sourcing in the relevant section above; summarized here):

- **ARR field corruption in the daily company-financials tracker:** shows $5.4B collapsing to **$1.5B exactly on June 16, 2026** (the DAIS disclosure date) and never recovering through the most recent snapshot (Aug 11, 2026) — almost certainly a mis-extraction that grabbed the DBSQL product-line sub-figure ($1.5B) instead of the $6.9B total. Not adopted; flagged in the JSON metadata.
- **Gross margin shows 65%** in the same tracker family across snapshots dated May 27 – Aug 11, 2026, versus 80% on a May 18, 2026 snapshot and versus the DAIS-disclosed 74% — a third, unexplained figure matching neither the pre-DAIS nor post-DAIS canonical number.
- **Capital-raised field never swept:** the daily tracker still shows the retired $33.135B blended figure through the Aug 11, 2026 snapshot, three-plus weeks after the correction.
- **The Morning Digest scoreboard's "Databricks Composite" column shows 8.92 — not 8.81 — in every single daily digest from July 10 through August 10, 2026** (the most recent digest in this bundle), despite two digest entries on July 9 and July 10 explicitly noting "spec's static canonical table still shows pre-recompute 8.92, sweep needed." The sweep item is one of several unchecked boxes on the reconciliation log's own "sweep checklist" (which also includes the project-context v3.4 refresh, the Digest §1 talking points, an "NxtMove" signal reframe, and the $/pt ladder line) — none of which are marked complete as of the most recent data in this bundle.
- **IPO status text not updated:** a company-dossier record compiled July 21, 2026 — two weeks after the reconciliation — still reads "target H2 2026," not reflecting the June 4 correction.
- **January 2026 debt-facility size conflict:** the canonical debt ladder (§d) attributes $1.8B to a January 23, 2026 JPMorgan/Citi facility; a separate tracker describes a "$5.45B" January 2026 facility with a different structure (two revolvers + a delayed-draw term loan). Not reconciled in the source data; both figures reported.
- **Customer count gap:** 20,000+ organizations (reconciliation, PitchBook Jun 9) vs. 10,000 (daily tracker, as recently as Aug 11) — roughly 2x, unreconciled.
- **Headcount gap:** 9,000 (reconciliation, PitchBook Jun 9) vs. 8,000 (daily trackers, consistently through Aug 11) — plausibly just a later recount, not explicitly reconciled.
- **NRR gap:** >140% (reconciliation, PitchBook Jun 9) vs. 130% (trackers, ~Jun 1) — plausibly a later, higher print; not explicitly reconciled.
- **An unratified $188B valuation signal** (see §d) — well-sourced (company newsroom, Bloomberg, TechCrunch) but explicitly not yet processed through NEXUS's own canonicalization workflow as of the latest compile in this bundle (Jul 21, 2026). Flagged as the single most important open item for the next refresh cycle.
- **CI sub-score rubric-fit question**, raised by NEXUS's own analysts: literal application of the CI-2/CI-3 (infrastructure ownership / energy) thresholds — calibrated for frontier-training labs — would yield a CI score around 5.4 for Databricks, versus the applied canonical 8.0 once a platform-deployment interpretation and the +1.0 AI-PLAT modifier are used. Flagged as a methodology question for quarterly review, not changed as of July 7, 2026.
- **CFO identity** (David Conte, ex-Splunk) carried at Medium confidence / unverified in NEXUS's own open-items list.
- **Panther acquisition terms** undisclosed; regulatory clearance pending as of July 7, 2026.
- **FCF margin** not disclosed by the company; carried internally at an ~7.5% estimate for scoring purposes, to be firmed up at the next print.
- **Multiple parallel AIBQ scoring lineages** coexisted through the Feb–May 2026 window before consolidating around the "v3.0" rubric used in the July 7 reconciliation — see the Methodology note in §b and the full writeup in the companion JSON's `_meta.known_data_quality_flags`.

Per this profile's brief, an additional cross-company statistical relationship (quality score vs. valuation, across NEXUS's coverage cohort) exists in the source system. Consistent with the standing embargo, it is not stated, implied, or characterized anywhere in this profile; see the embargo notice at the top of this document.

---

## (j) Sources

- **External (non-Notion) source URLs referenced across the bundle: 181 distinct URLs**, spanning company blog/newsroom posts (databricks.com), PitchBook deal and profile pages (my.pitchbook.com, profile 59199-40), SEC/EDGAR, wire and trade press (Bloomberg, CNBC, Reuters, TechCrunch, The Information via secondary citation, Washington Post), release-note and documentation pages (docs.databricks.com, learn.microsoft.com), partner/customer press releases, and a long tail of AI-industry newsletters, aggregator sites, and Google News RSS pickups of varying reliability.
- **Source tiers represented:** T1 (SEC filings), T2 (PitchBook, company press releases, major wire services), T3 (The Information-sourced valuation-rumor coverage), and T4/T5 (unverified aggregator and social pickups — used only for the flagged, not-yet-ratified $188B item and similar open signals, never for canonical figures).
- **Internal NEXUS source-authority record:** databricks.com rated Authority Score 9/10 ("Tier 9 — official tracked-company sources + major wire services"), status Active, last reviewed 2026-07-21.
- **Structured NEXUS tables consulted:** 53 top-level sections of the source bundle (company registry, AIBQ daily-scores and score-tracker history, company snapshots, canonical figures, cap table, financial model inputs, forecasts, IPO pipeline, master events, timeline events, morning digests, and related tables) — full detail and row counts in the companion `databricks.json` and its `_meta` block.
- **Narrative context documents consulted:** the Databricks NEXUS profile page, the July 7, 2026 reconciliation + v3.0 re-score log (the authoritative source for the corrections in §i), the Command Center deep-dive, and the AIBQ framework deep-dive (both the May 27 vintage at composite 8.92 and an earlier May-vintage snapshot at composite 8.78, reflecting the same methodology-transition period discussed in §b).

---

*This profile and its companion `databricks.json` were produced from the NEXUS data bundle as supplied; no external sources were re-fetched. All figures carry their as-of dates; where the underlying data disagreed with itself, both figures are shown rather than one being silently preferred (see §i in particular). The one standing exception is the cross-company quality-vs-valuation relationship, which is embargoed and does not appear in either output file.*
