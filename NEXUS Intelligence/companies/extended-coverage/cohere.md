# Cohere — NEXUS Intelligence Profile

**Coverage tier:** Extended Coverage (not Frontier Five) | **Sector:** Foundation Models | **Profile as of:** 2026-08-11

---

## Data quality note — read first

Cohere's raw `timeline_dated_events` extraction (208 rows) was reviewed row by row rather than trusting the pre-filter, per instruction, and that caution was warranted: **42 of 208 rows (~20%) are not genuinely about Cohere the AI company.** The contamination is broader than the single "Coherent Corp" collision flagged at task intake — six distinct non-Cohere-AI entities turned up:

| Colliding entity | What it actually is | Rows excluded |
|---|---|---|
| **Coherent Corp** (NYSE: COHR) | Unrelated public laser/photonics/optical-components manufacturer | 10 |
| **Cohere Health** | Separate, real Boston-based healthcare prior-authorization/revenue-cycle-management AI company — also founded 2019, which compounds the collision risk | 15 |
| **Cohere Technologies** | Separate telecom/5G waveform company — explicitly flagged as a known collision risk in this bundle's own internal dossier note | 2 |
| **Cohere Beauty** | Unrelated salon/cosmetics product-development business | 2 |
| **Cohera Commercial** (note spelling) | Unrelated commercial real-estate operating-services firm | 1 |
| **Borderless AI** | A different Toronto fintech/payroll startup, swept in from a shared source article | 3 |
| Unrelated mistagged noise (Arena, Dynatrace, Capital Clean Energy Carriers Corp, Coeur Mining/New Gold, Together AI, one Coherent-Corp-stock-page macro item) | No name relationship to Cohere at all | 9 |
| **Total excluded** | | **42** |

Five of the 42 excluded rows had already been self-flagged **"FALSE POSITIVE"** inside the bundle's own description field — but the other 37 carried no such flag despite being equally clearly not about Cohere the AI company (identical "Cohere Surface" claims-mining headlines sit right next to each other, some flagged and some not). This confirms the pre-filter is necessary but not sufficient. **166 genuine Cohere AI rows remain.** No genuinely-Cohere data point was dropped: every exclusion is individually justified and preserved — tagged, not deleted — in the full log inside `cohere.json`.

## (a) Overview

Cohere was founded in 2019 in Toronto by Aidan Gomez (a co-author of the original "Attention Is All You Need" Transformer paper and current CEO), Ivan Zhang, and Nick Frosst (ex-Google Brain). The company builds enterprise-focused LLM APIs differentiated from OpenAI by data privacy, multi-cloud and on-premise/VPC deployment, and customization — a positioning that has increasingly sharpened into a "sovereign AI" pitch to governments and regulated industries. It operates from Toronto (HQ), San Francisco, London, and New York, with 450 employees as of the most recent tracker refresh (up from 400).

Product line: Command R (2023, RAG-optimized) and Command R+ (2024), the Command A family with Reasoning and Vision variants (2025–2026), Command A+ (May 2026, the first fully open-weights flagship), the North agent platform (including North Mini Code coding models), Transcribe (open-source speech recognition, later extended with an Arabic model), and Aya (a translation/multilingual research model). Disclosed customers and partners span the enterprise and public sector: the University of Toronto, the Canadian federal government (Shared Services Canada / CanChat) and Quebec government, the UK government, Bell Canada, Saab (AI integration into Global Eye surveillance jets), HUMAIN (Saudi Arabia's AI champion, supplying compute), Oracle (cloud/OCI), Salesforce, Ensemble (a healthcare revenue-cycle-management partnership), Calian (military), and Carahsoft (US public-sector distribution). FedRAMP High authorization was achieved in May 2024.

CEO Aidan Gomez has said publicly that Cohere is looking to IPO "soon," and has advocated for sovereign AI at the G7 level, framing the choice as one between sovereign AI and "digital serfdom" (Fortune, June 2026).

## (b) Current scores

**No dated AIBQ (the primary five-dimension framework) composite exists for Cohere anywhere in the supplied data.** Unlike Mistral AI, there is no `framework/companies/cohere*.md` score page in the extract directory (confirmed by directory listing — none exists), and the unicorn-scores table holds exactly one row for Cohere, tagged framework **"PBQ,"** not "AIBQ." This is stated plainly as a genuine data gap rather than filled in with an estimate.

**PBQ composite: 5.63**, dated **2026-05-14**, confidence **High** — the only composite of any framework found for Cohere, so no prior score can be reported either.

| CE | RQ | SV | GO | MD |
|----|----|----|----|----|
| 3.0 | 5.0 | 5.5 | 6.0 | 5.5 |

*(CE = Capital Efficiency, RQ = Revenue Quality, SV = Strategic Vision — PBQ's substitute for AIBQ's Compute Independence dimension, GO = Governance Optionality, MD = Moat Durability.)*

The score's own rationale states: *"Rev $265M / Raised $1.64B = 0.16x (PitchBook verified). Val jumped from $6.3B to $20B in 7 months... Acquired Aleph Alpha..."* — this folds the announced-but-**not-yet-closed** Aleph Alpha/Schwarz Group transaction into the scoring input as if it were confirmed current valuation. This profile treats $6.8B (the standalone, ladder-tracked figure) as the base-case current valuation and the ~$20B figure as a pending forward signal — see (d) and (i).

## (c) Financials

As of the 2026-08-11 snapshot (a 115-point daily ladder tracked since 2026-03-23, cross-checked against the legacy dossier row):

| Metric | Value | Prior |
|---|---|---|
| ARR | $240M | $150M (~Jan 2025) |
| Gross margin | 55% | 52% |
| Gross profit | $132M | $82.5M |
| Burn rate | $25M/mo | $20M/mo |
| Headcount | 450 | 400 |
| Compute spend | $120M/yr | $100M/yr |
| Customers | 1,000 | 700 |
| Enterprise mix | 95% | 92% |
| NRR | 130% | 120% |
| Runway | 30 months | 24 months |
| Total capital raised | $1.64B | $1.6B |

$240M ARR traces to a specifically dated print ("Cohere reaches $240M ARR, exceeding $200M target," 2026-02-23) and is consistent with the ladder from late March 2026 onward. A less-precisely-dated PitchBook TTM estimate puts ARR slightly higher at $265M (carrying a different PitchBook ID than the one used elsewhere for Cohere — see (i)); shown as a secondary estimate, not the primary dated figure. ARR ÷ headcount at current values works out to roughly $533K/employee.

Two stored growth-rate fields disagree on scale for what should be the same metric: the legacy dossier's "Revenue Growth YoY %" reads 1.1 (prior period 0.7), while a separate valuations-snapshot field reads "ARR Growth YoY %": 70. A simple $150M→$240M computation implies roughly 60% growth, closer to the 70 figure — both stored values are shown rather than silently collapsed into one.

Total capital raised also shows real dispersion: **$1.64B** is the figure carried by the legacy dossier, the daily ladder, and the PBQ score rationale (the most current, highest-agreement number), but a PitchBook-sourced financial-model input separately tallies **$960M** as of an earlier point that predates the 2025–2026 raises, and one further aggregator-sourced timeline row cites "**~$1B** cumulative" with its own inconsistent round labeling. All three are shown rather than reconciled by invention.

**Partially corroborated, partially not — flagged rather than either fully adopted or fully discarded:** a single "Intel Notes" field (carrying a different PitchBook ID than the one used elsewhere for Cohere) claims Rev $265M, Val $20B, Raised $1.64B, 450 employees, "Former name: Secant," "82 active investors," "8 offices," "99th percentile growth," and "ACQUIRED Aleph Alpha (Apr 2026)." On investigation: the $1.64B raised and 450-employee figures check out exactly against the daily ladder; the Aleph Alpha transaction and ~$20B combined valuation are real and heavily corroborated — but as an **announced, not-yet-closed merger** (contemporaneous press explicitly notes it is "subject to regulatory and shareholder approval," and a forward-dated entry as far out as December 31, 2026 still describes it as merely "expected to close"), not a completed acquisition. "Former name: Secant" appears exactly once in the entire 208-row bundle, nowhere else corroborated, and is not presented as fact; "82 active investors," "8 offices," and "99th percentile growth" are likewise single-sourced and shown as unverified color only.

## (d) Valuation & funding history

| Date | Round | Amount | Post-money | Lead investors |
|---|---|---|---|---|
| 2021-05-28 | Series B | $40M | $215M | Index Ventures, OMERS Ventures |
| 2022-02 | Series C | $125M | $2.1B | Tiger Global, Radical Ventures |
| 2023-06-08 | Series D | $270M | $2.1B | Inovia Capital, Oracle |
| 2024-07-22 | Series E | $500M | $5.5B | PSP Investments, Salesforce Ventures |
| 2025-08 | Press-labeled "Series D" (post-dates the actual 2023 Series D) | $500M | $6.8B | — |
| 2025-09 | Press reconfirmation | — | ~$7B | (Intel Notes separately cites "$700M Series D1" at $6.3B, Radical/Kensington/Inovia — not reconciled) |
| 2026-02-23 | ARR print, not a funding round | — | — | ARR reaches $240M |
| 2026-04-24/25 | **Merger/acquisition of Aleph Alpha, anchored by Series E — ANNOUNCED, NOT closed** | $600M | ~$20B combined, if/when closed | Schwarz Group |
| 2026-05-01 | Standalone reference running in parallel with the merger story | — | $6.8B | — |
| 2026-06-02 | Single press mark, below the surrounding range | — | ~$5B (reported) | — |

The Series C ($125M, Feb 2022) and Series D ($270M, Jun 2023) rounds are both recorded at an identical "$2.1B post-money" in the primary verified events log despite the large difference in raise size — flagged as a likely duplication/reuse of the same figure rather than independently confirmed for each round. The most consequential open item is the **Aleph Alpha transaction**: heavily corroborated as a real, announced deal valuing the combined entity at roughly $20B and anchored by a $600M Series E from Germany's Schwarz Group, but explicitly not yet closed as of the most recent dated reference in the data. Consistent with treating unclosed financings as forward signals rather than the base case, this profile does not fold the $20B figure into current valuation.

**Current best-supported figures: $6.8B standalone valuation, $1.64B total raised, as of 2026-08-11.** The pending Aleph Alpha/Schwarz Group transaction (~$20B combined, if/when closed) is tracked separately.

## (e) Cap table & investors

No structured cap-table dataset exists in the supplied bundle (the relevant array is empty). The list below is reconstructed narratively from event and dossier fields and should be read as directional, not a verified formal cap table.

- **Series B:** Index Ventures, OMERS Ventures
- **Series C:** Tiger Global, Radical Ventures
- **Series D:** Inovia Capital, Oracle (also an OCI cloud deployment partner)
- **Series E:** PSP Investments, Salesforce Ventures
- **2025-09-era raise (labeling inconsistent — see (d)):** Radical Ventures, Kensington Capital Partners, Inovia Capital
- **Pending 2026 Series E, tied to the Aleph Alpha transaction, not closed:** Schwarz Group
- **Strategic stakeholders also referenced:** NVIDIA, Salesforce, Cisco, Oracle, Index Ventures

Aidan Gomez sits as CEO and board member; PSP Investments is reported to hold a board seat with lead rights and "a long investment horizon"; Oracle holds a Series D board seat per the dossier. Canadian domicile is flagged in the dossier as favorable for data-sovereignty positioning.

## (f) Litigation & IP

One confirmed, genuine litigation matter: a court **rejected Cohere's motion to dismiss a publishers' data-scraping lawsuit** (reported November 17, 2025) — the case was allowed to proceed against the company. This is single-sourced to a news aggregator at unverified tier, but it is a real and material litigation exposure and is flagged prominently despite the sourcing tier. No patent or trademark items were found (unlike Mistral AI, which had one patent-filing headline). Both structured litigation/IP arrays are empty. On the regulatory-adjacent side: FedRAMP High authorization (a compliance achievement, not enforcement) and German data-protection (BDSG)/air-gapped-deployment requirements for certain regulated customers are noted as governance considerations, not active actions.

## (g) Active forecasts

No structured forecast dataset exists for Cohere in the supplied bundle. Forward signals are press-reported only, not house forecasts with a stated methodology: CEO Aidan Gomez's statement that Cohere is looking to IPO "soon" (echoed by a December 2026-dated "anticipated IPO" timeline marker), and the pending Aleph Alpha merger close (~$20B combined valuation if/when it closes) — the dominant forward signal in the data, and one this profile does not adopt into the base case per standard practice on unclosed financings.

## (h) Notable events

The raw extraction contained **208 dated event rows**; after the contamination review detailed at the top of this document, **166 genuine rows remain**. Curated to the 29 most important below by importance; the complete raw log — all 208 rows, each tagged genuine or excluded with a stated reason, nothing deleted — ships in `cohere.json`.

1. **2019** — Founded in Toronto (Gomez, Zhang, Frosst)
2. **2021-05-28** — Series B $40M ($215M val)
3. **2022-02** — Series C $125M ($2.1B val)
4. **2023-01** — Command R released (enterprise RAG-optimized model)
5. **2023-05-02** — Joins the "Unicorn Club"
6. **2023-06-08** — Series D $270M ($2.1B val)
7. **2023-11** — Model integrated into Amazon Bedrock
8. **2024-03-11** — Command R+ released
9. **2024-05** — FedRAMP High authorization + Carahsoft distribution deal
10. **2024-07-22** — Series E $500M ($5.5B val)
11. **2024-12** — Canadian government provides $240M for sovereign AI data-center compute
12. **2025-01** — ARR reaches ~$150M
13. **2025-08** — $500M raise closes at ~$6.8B valuation
14. **2025-11-17** — Court denies motion to dismiss publishers' data-scraping lawsuit — case proceeds
15. **2026-02-23** — ARR reaches $240M, exceeding a $200M target
16. **2026-03-17** — Command A Vision (112B multimodal) launched
17. **2026-03/04** — Transcribe (open-source ASR) launched; Arabic model follows in July
18. **2026-03-23/24** — Saab partnership — AI integration into Global Eye surveillance jets
19. **2026-03-31** — Partnership with Ensemble on the first RCM-native LLM for healthcare orchestration
20. **2026-04-24/25** — Announces Aleph Alpha merger, ~$20B combined valuation, $600M Series E (Schwarz Group) — **announced, not closed**
21. **2026-05-01** — Command A+ released — first fully open-weights flagship model
22. **2026-05-01** — Aya (translation/multilingual) model released
23. **2026-05-01** — Partnerships announced with Canadian and UK governments
24. **2026-06-09** — Quebec government exploratory AI agreement
25. **2026-06-17** — CEO advocates for sovereign AI at G7 level (Fortune)
26. **2026-07-09/14** — HUMAIN (Saudi AI) compute-supply partnership
27. **2026-07-20** — University of Toronto multi-year enterprise AI partnership
28. **2026-07-30** — Carahsoft partnership for secure public-sector AI deployment
29. **2026-08-06** — CEO comments publicly on Google AI leadership shake-up (CNBC)

## (i) Open conflicts / disputes

1. **Entity-collision contamination in raw extraction (resolved by exclusion).** 42 of 208 raw rows (~20%) — full breakdown in the data-quality note at the top of this document.
2. **PitchBook ID mismatch.** Three different identifiers are attached to Cohere across the bundle: an internal slug, one ID underlying the well-corroborated $100–150M-ARR/~$960M-raised range, and a second ID underlying the PBQ score and the disputed $265M/$20B/"Secant" cluster.
3. **"Former name: Secant."** Appears exactly once in the entire bundle, uncorroborated anywhere else. Not presented as fact.
4. **Total capital raised spread.** $1.64B vs. $960M vs. "~$1B cumulative" — three sources, not reconciled by invention (detail in (c)).
5. **Identical valuation for two different-sized rounds.** Series C ($125M) and Series D ($270M) both recorded at "$2.1B post-money."
6. **Pending-vs-closed conflation.** Several scoring/intel fields treat the unclosed ~$20B Aleph Alpha/Schwarz Group transaction as current valuation; this profile keeps $6.8B as the base case and reports the merger separately.
7. **ARR precision spread.** $240M (specifically dated, ladder-consistent) vs. $265M (less-precisely-dated estimate, disputed PBID).
8. **Revenue-growth field unit inconsistency.** 1.1/0.7 (legacy dossier) vs. 70 (valuations snapshot) for what should be the same metric.
9. **Round-label/amount inconsistency, 2025 raise.** A 2025-08 raise is press-labeled "Series D" despite the real Series D having occurred in 2023; a separate note calls a Sep-2025 event "Series D1" with different amounts and investors. Not reconciled.
10. **EMBARGOED.** A cross-company quality-valuation relationship exists and is embargoed from publication. No coefficient, scatter, or fitted line relating AIBQ/PBQ score to valuation is stated, computed, or shown for Cohere.

## (j) Sources

Across the 166 genuine dated-event rows: **128 distinct source URLs** spanning **88 distinct domains**. The most-cited are Google News aggregation (22 hits), cohere.com (12, the company's own newsroom), TechCrunch (6), Wikipedia and BNN Bloomberg (5 each), and Tracxn, tech-insider.org, TipRanks, Manila Times, and CNBC (4 each). **8 of the 166 genuine rows (~5%) carry the primary system's "Verified: YES" tag**, tracing to the 8-row core events log; the remaining ~95% are harvested press/aggregator rows at unverified tier. Cohere's verified-tier share (~5%) is lower than Mistral AI's (~8%), and its contamination rate is far higher (~20% of raw rows vs. ~1.4% for Mistral) — both consistent with the bundle's own dossier note describing Cohere as a "thin-coverage name" with a known entity-collision problem; figures here warrant correspondingly more caution than Mistral AI's. Beyond the timeline, the profile draws on: the primary verified events log (8 rows), a company dossier stub (which itself flags the Cohere Technologies collision risk), four PitchBook-sourced financial-model-input lines, one flagship cross-company research report (in Data Collection status, names Cohere as a comparison company), and the 115-point daily snapshot ladder. The company's own domain (cohere.com) carries an internal source-authority score of 9/10.

---
*Full structured data, including the complete annotated 208-row dated-event log (contamination-filtered per the note above), ships in `cohere.json`.*
