# Cerebras Systems — NEXUS Company Intelligence Profile

**PBID:** 163733-59 &nbsp;|&nbsp; **NEXUS coverage tier:** Extended Coverage &nbsp;|&nbsp; **Internal comp tier (legacy DB):** Tier 2 — Challengers
**Sector / industry labels in source:** AI Infrastructure (legacy DB) · Application Specific Semiconductors (AIBQ score rows) · Semiconductors (PBQ score rows)
**HQ:** DISPUTED across source tables — see Overview
**Profile compiled:** 2026-08-11 &nbsp;|&nbsp; **Most recent underlying data point:** 2026-08-11 (daily snapshot; values unchanged since 2026-05-11/12)

> **Coverage note.** Cerebras is the thinnest-data company in the 14-company core universe. Of the 49 list-type tables checked in the source bundle, 3 returned rows for this company (the legacy Companies database, the company-snapshots database, and the Unicorn Scores database); the other 46 — including the entire v2/AIBQ tracking layer and every canon, shared, framework, command-center, and timeline table — returned zero. Every section below reports only what was actually extracted. Where a standard profile section has no data, it says so rather than filling the gap with speculation. Full accounting in Section (j).

---

## (a) Overview

Cerebras Systems builds wafer-scale AI compute hardware, positioning itself as the primary challenger to NVIDIA in AI inference. Its core product, the Wafer-Scale Engine (WSE, now in its third generation as WSE-3), is fabricated as a single chip roughly 57–58x the area of a leading GPU die, packing 900,000+ cores with single-cycle on-chip SRAM access. The hardware ships as the CS-3, described in source as an "1.8-ton" turnkey appliance; multiple units cluster together via auxiliary interconnect devices, with the company's MemoryX architecture handling activation storage. Distribution runs two tracks: on-premise CS-3 sales, and cloud access via Amazon Web Services, added shortly after the company's large compute agreement with OpenAI (announced January 2026).

OpenAI is Cerebras's dominant commercial relationship: it accounted for more than 80% of FY2025 revenue and anchors the $24.6 billion in remaining performance obligations on the books (Section (c)). AWS is the second named partner, providing cloud distribution. Strategic priorities logged in source: AI inference chip development; compute/infrastructure; AI model training; IPO readiness and preparation; post-IPO profitability; scaling AI infrastructure; enterprise AI workloads.

Cerebras filed to go public in 2026: an S-1 in April, an amended S-1 (S-1/A) in May, and priced May 13–14, 2026 on Nasdaq under ticker CBRS. That followed a withdrawn 2024 IPO attempt, pulled during a CFIUS review of a G42 (UAE-based AI company) investment; clearance was received in May 2025. Full IPO and funding detail is in Section (d).

**HQ conflict, flagged rather than resolved:** the legacy Companies database lists the headquarters as Palo Alto, CA. All three Unicorn Score rows that carry a populated HQ field (one AIBQ, two PBQ) instead say Sunnyvale, CA/US. The two source tables disagree; both values are reproduced here rather than one being silently preferred.

No dedicated Leadership Team or Board Composition record exists in source for Cerebras (see Section (h)). CEO Andrew Feldman is named only incidentally — inside two scoring-rationale text fields and inside the Competitive Position narrative field — not inside a structured leadership record.

---

## (b) Current scores

Two distinct scoring frameworks appear for Cerebras in the Unicorn Scores database: **AIBQ** and an older, parallel rubric labeled **PBQ**. They use different dimension sets (AIBQ: CE, RQ, CI, GO, MD; PBQ: CE, RQ, SV, GO, MD) and are not placed on a common scale anywhere in source, so they are reported separately below rather than merged into a single "the" score. A sixth row in the same table cannot be attributed to either framework (see "Unattributed entry"). The `aibq_daily_scores` and `aibq_score_tracker` tables — which would carry an ongoing AIBQ time series — are both empty for this company.

### AIBQ

| Date | Composite | Band | Confidence | CE | RQ | CI | GO | MD | Batch | Post-money at scoring |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-05-12 | **4.50** | Developing | Medium | 3.0 | 3.0 | 9.0 | 4.0 | 5.0 | 1 | $23B |

This is the most recent full AIBQ read on Cerebras and it is cross-confirmed by two independent source records: the `aibq_unicorn_scores` row (Composite 4.5) and the dedicated AIBQ score page (`framework/companies/cerebras-systems.md`: "AIBQ 4.50 (Developing)"), which reproduces the identical CE/RQ/CI/GO/MD breakdown. Rationale logged with the score: capital-to-revenue ratio thin (roughly $1.1B+ raised against limited recurring revenue at the time), a hardware-sales model rather than SaaS-style recurring revenue, vertically integrated in-house chip manufacturing (the highest sub-score, CI 9.0), an IPO that was delayed with board and regulatory friction as of the scoring date (GO 4.0), and a wafer-scale technology the rationale calls genuinely differentiated but "niche" against NVIDIA's ecosystem dominance (MD 5.0).

A second AIBQ Batch 1 row exists in the same source table with no score fields populated at all — no Composite, no date, no dimensions — only HQ ("Sunnyvale, United States"), Post-Money ($23B), PBID, and Industry are filled in, and the Post-Money, PBID, and Industry values are identical to the scored row above (the HQ string differs only in phrasing: "Sunnyvale, United States" here versus "Sunnyvale, US" on the scored row). It reads as an incomplete or placeholder record, not a second AIBQ score, and is not counted separately.

### PBQ (legacy/parallel rubric)

| Date | Batch | Composite | Confidence | CE | RQ | SV | GO | MD | Valuation rank | Post-money at scoring | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-05-14 | 5 | 5.28 | Low | 3.5 | 5.0 | 6.5 | 5.5 | 6.0 | 110 | $4B | Original pass |
| 2026-05-14 | 8 | 5.28 | Low | 3.0 | 5.0 | 6.5 | 5.5 | 6.0 | 187 | $4B | Marked duplicate in source: "Keeping for reference" |
| 2026-05-14 | 17 | 5.28 | Low | 7.0 | 5.0 | 6.5 | 5.5 | 6.0 | 422 | $4B | Marked duplicate in source: "SKIP" |

All three rows share a date (2026-05-14) and a Composite (5.28). The source rationale on the Batch 8 and Batch 17 rows states directly that both are duplicates of Batch 5 rank 110, not fresh re-scores. The Valuation Rank field nonetheless climbs across the three passes — 110, then 187, then 422 — which reads as the comparison cohort growing between passes rather than Cerebras's own standing moving (a reading, not a confirmed fact). The CE sub-score is inconsistent across the three supposedly-duplicate rows (3.5 / 3.0 / 7.0) even though the Composite holds fixed at 5.28; reproduced as-is, not smoothed over.

More materially: the Batch 5 rationale prices Cerebras off much smaller figures than the legacy DB row carries for the same window — an estimated ~$100M revenue and ~$700M raised, against a $4B post-money — versus the $510M ARR, $4.62B raised, and $26.6B valuation the legacy DB row and the daily snapshot series report. That gap indicates the PBQ pass ran on materially older or unrefreshed inputs, not a fresher independent read. The rationale's one named leadership reference is CEO Andrew Feldman.

### Unattributed entry

| Date | Composite | Confidence | CE | RQ | GO | MD |
|---|---|---|---|---|---|---|
| 2026-05-13 | 7.65 | High | 6.0 | 7.0 | 8.0 | 7.0 |

This row falls chronologically between the AIBQ and PBQ entries above but carries no Framework, Batch, HQ, Industry, PBID, or rationale in source, and has neither an SV nor a CI dimension — so it does not cleanly match either rubric's dimension set. It cannot be confidently attributed to AIBQ or PBQ. It is not treated as the headline current score, but it is a genuine dated row in the source table and is reproduced here rather than dropped.

**Headline read:** the most recent fully attributed, cross-confirmed score is **AIBQ 4.50 ("Developing"), dated 2026-05-12, Medium confidence**. Nothing in the score tables has been refreshed since 2026-05-14 (PBQ), and nothing AIBQ-specific since 2026-05-12 — roughly three months of no re-scoring as of this profile's compile date.

---

## (c) Financials

*Source: legacy Companies database row, as-of 2026-05-11/2026-05-12 (Last Extracted / Last Refreshed). Every field below is carried unchanged across all 69 daily rows in the company-snapshots database from 2026-05-12 through 2026-08-11 — see the staleness note at the end of this section.*

**Revenue.** FY2025 ARR: **$510M**, up 76% year-over-year from an implied FY2024 figure of ~$290M. Source carries an explicit caveat on this figure, reproduced verbatim: "$510M is hardware/services revenue, not SaaS ARR — logged for comparability only." Cited sources: SEC S-1/A filing (Nasdaq, Apr–May 2026), SiliconAngle (May 4, 2026), a Cerebras press release (Feb 3, 2026), TechMarketBriefs' S-1/A analysis, and TechCrunch (Apr 18 and May 4, 2026). Revenue per employee is reported at approximately $1.275M, flagged **est.** in source. Customer concentration is severe: OpenAI is 80%+ of FY2025 revenue, and Enterprise Mix is logged at 100%.

**Remaining performance obligations.** The OpenAI compute agreement leaves **$24.6B** in remaining performance obligations on the books, of which roughly 15% is expected to be recognized in 2026–2027. Two source fields disagree on the resulting multiple of FY2025 revenue: one ("Benchmark Positions") states approximately 53x, another ("Top Line Trajectory") states approximately 48x for the same $24.6B/$510M pair (a direct calculation gives ~48.2x). Both are reproduced; neither is corrected here.

**Profitability and cash flow.** Non-GAAP net loss for FY2025 was **-$75.7M**. Operating cash flow swung from **+$452M** in FY2024 to **-$10M** in FY2025; source attributes the swing to the timing of the OpenAI agreement (source shorthand "MRA," not expanded in the extracted data). GAAP net income for FY2025 is **DISPUTED in source and reported here without adopting either figure**: $87.9M per SiliconAngle/Wikipedia, versus $237.8M per TechMarketBriefs, the latter inclusive of a $363.3M non-cash forward-contract gain. Source's own instruction, carried forward verbatim: "DO NOT attribute profitability without S-1 reconciliation." Burn rate is reported at approximately $6.3M/month, Non-GAAP, flagged **est.**

**Headcount and capital.** Headcount stands at **400**, versus a prior figure of **71** — a greater than 5x increase, though the prior figure carries no date in source, so the growth cannot be annualized from this data alone. Total capital raised is **$4,620M**, versus a prior figure of **$2,770M** (also undated). Source's own self-reported Data Confidence score for this row is **0.72**.

**Not captured in source:** gross margin, gross profit, cumulative losses, compute spend, customer count, revenue per customer, runway (months), implied ARR multiple, job posting score, media sentiment, and NRR are all null in the legacy DB row, and no fresher figures for any of them appear elsewhere in the bundle.

**Staleness flag.** All 69 daily rows in the company-snapshots database, spanning 2026-05-12 to 2026-08-11 (today), are field-for-field identical: same $510M ARR, same $26.6B valuation, same 400 headcount, same 76% growth, same 0.72 confidence score, every day, for three months. Nothing in this bundle indicates a re-pull happened in that window; the series reads as a carried-forward baseline rather than independently re-confirmed daily research.

---

## (d) Valuation & funding history

**Valuation ladder:**

| Date | Event | Valuation |
|---|---|---|
| undated (prior period) | — | $8.1B |
| 2026-02-03 | Series H close | $23B post-money |
| 2026-05-12 through 2026-08-11 (69 daily snapshots, unchanged) | S-1/A range and post-IPO mark | **$26.6B** |

The $26.6B figure first appears in the snapshot series on 2026-05-12 — one day before the stated IPO pricing window of May 13–14, 2026. Source data does not say explicitly whether $26.6B is the S-1/A-anticipated figure or a confirmed post-pricing mark; it sits inside the $26–27B target band disclosed in the S-1 (below), and it is the number every subsequent daily snapshot through 2026-08-11 carries forward unchanged. Separately, source logs an IPO pricing multiple: "51–53x 2025 trailing revenue at $135/share IPO range."

**Series H.** $1B raised, closed February 3, 2026, at a $23B post-money valuation, led by Tiger Global. AMD is named as a strategic investor in this round.

**IPO.** S-1 filed April 2026; amended (S-1/A) filed May 2026. Ticker CBRS on Nasdaq. Price range $125–135/share across roughly 28 million Class A shares, targeting a raise near $3.5B and a valuation of $26–27B. Priced May 13–14, 2026. The book was 20x oversubscribed: $10B+ of orders against the $3.5B offering. Lock-up covers approximately 171 million shares, roughly 5x the IPO share count. Class B shares carry 99.2% of post-IPO voting power, concentrated enough that source states founders can retain control with an economic stake as low as 5%; source characterizes public shareholders as having no meaningful vote on the board, executive compensation, change-of-control, or charter amendments. As a JOBS Act emerging growth company, Cerebras is not required to provide SOX 404(b) auditor attestation for up to five years. A first IPO attempt in 2024 was withdrawn during a CFIUS review triggered by a G42 (UAE) investment; clearance was received in May 2025, clearing the path to the 2026 filing.

**Debt.** An $850M revolving credit facility was secured April 16, 2026. Lead arrangers: Morgan Stanley, Citi, Barclays, UBS, Crédit Agricole, MUFG, Mizuho, TD Securities, and Silicon Valley Bank (First Citizens).

**Strategic investors and other notes.** OpenAI holds a $1B loan to Cerebras secured by warrants for 33M+ Cerebras shares. Several OpenAI leadership figures — Altman, Brockman, Sutskever, and D'Angelo — are named in source as angel investors in Cerebras. Source separately notes that OpenAI "previously considered acquisition" of Cerebras, citing a Musk lawsuit filing as the origin of that claim; this is reproduced as a sourced claim, not verified independently here. Abu Dhabi Growth Fund and G42 are named as early investors — the same G42 position that triggered the CFIUS review discussed above (now cleared). Total capital raised stands at $4,620M, versus $2,770M in the prior (undated) period.

**On the score tables' own valuation fields:** the AIBQ score rows in Section (b) carry a Post-Money figure of $23B (matching the Series H mark); the PBQ score rows carry $4B, which does not match any point on the ladder above and evidently reflects older or unrefreshed inputs to that scoring pass. Those figures describe the valuation on record at the moment each score was computed — they are not a restatement of this ladder, and are not repeated here.

---

## (e) Competitive positioning & product

Cerebras frames itself as the primary NVIDIA challenger in AI inference, built around the WSE-3: a single chip roughly 57–58x the die area of a leading GPU, with 900,000+ cores and single-cycle on-chip SRAM access. Source logs a claimed 15x inference-speed advantage over GPUs at a fraction of the power draw, and attributes to CEO Feldman the claim that Cerebras took OpenAI's fast-inference workload from NVIDIA. Hardware ships as the CS-3, a turnkey system source describes as an "1.8-ton" appliance, with multiple units linked into clusters via auxiliary interconnect devices and the MemoryX architecture handling activation storage. Distribution runs two tracks: on-premise CS-3 sales, and cloud access via AWS, added shortly after the OpenAI compute agreement (announced January 2026). The software stack is PyTorch-compatible, which source notes removes proprietary-framework lock-in as an adoption barrier — but source is direct that Cerebras has "no meaningful open developer ecosystem" as of May 2026, with OpenAI functioning as the company's primary enterprise reference customer.

Named competitors: NVIDIA, whose CUDA ecosystem source calls "the dominant" moat in the space, plus Tenstorrent, Groq, and SambaNova. Source frames the contest directly: Cerebras differentiates on latency and power, NVIDIA counters with software-ecosystem depth and breadth of model support. The bull case, per source: Cerebras "solved a genuine inference bottleneck." The bear case, per source: "the CUDA moat is sticky even where WSE-3 is technically superior."

Pricing runs three tracks: hardware sales (CS-3 systems), pay-as-you-go cloud access via AWS, and multi-year compute arrangements — the largest disclosed being the OpenAI agreement, a $10B+ arrangement covering 750MW of capacity through 2028 with an option to expand to 1.25GW and, by 2030, 2GW. (This is the agreement behind the $24.6B remaining performance obligations figure in Section (c).) Active product lines, as logged in source: HPC infrastructure, AI cloud infrastructure, AI compute infrastructure, and AI infrastructure services. Named customers and partners: OpenAI and Amazon (AWS).

---

## (f) Technology & IP

Core IP, per source: the wafer-scale integrated-circuit architecture spanning three generations (WSE, WSE-2, WSE-3); an on-chip SRAM memory hierarchy; an interconnect fabric for clustering multiple CS-3 units together; and the MemoryX storage architecture for AI model activations. Source describes the resulting moat as architecture-level, "not easily replicated on a standard GPU die without fundamental wafer-scale manufacturing capability." The manufacturing partner is TSMC — a 7nm process is disclosed for WSE-2, while WSE-3 process details are not disclosed in source.

One historical landmark is logged: the WSE-2 entered the Computer History Museum's permanent collection in August 2022, described there as an "epochal achievement in fabricating transistors."

---

## (g) Regulatory, governance & ownership

Two source fields independently cover the JOBS Act exemption and corroborate each other rather than conflicting: Regulatory Exposure states Cerebras is an emerging growth company under the JOBS Act with no SOX 404(b) auditor attestation required for up to five years; Investor Rights separately states the same five-year exemption.

Ownership is concentrated. Class B shares carry 99.2% of post-IPO voting power, and source states founders can retain control with an economic stake as low as 5%; public shareholders are described as having no meaningful vote on the board, executive compensation, change-of-control, or charter amendments (full detail in Section (d)).

Cerebras's first IPO attempt, in 2024, was withdrawn during a CFIUS review triggered by a G42 (Abu Dhabi-based AI company) investment; clearance was received in May 2025. Source also flags export controls on AI chips as a live risk to Cerebras's international customer base, and separately notes that AMD — named elsewhere as a Series H strategic investor — is simultaneously described as a chip-industry competitor/partner. Source flags this without resolving it further, and it is reproduced the same way here.

---

## (h) Leadership & organization

No data captured for Leadership Team or Board Composition as of extraction — both fields are null in the legacy DB row. Key Hires (90d) and Key Departures (90d) are also both null.

The one leadership data point available is incidental rather than structured: Andrew Feldman is named as CEO inside a PBQ scoring-rationale text field (Section (b)) and inside the Competitive Position narrative field (Section (e)), not inside a dedicated leadership record. It is reported here with that provenance caveat attached rather than presented as a verified leadership fact. Headcount (400, versus a prior undated 71) is reported in Section (c).

---

## (i) Recent activity, talent & events

No data captured for this section as of extraction. Recent Launches (90d), M&A Activity (12mo), Media Sentiment, and Job Posting Score are all null in the legacy DB row. The v2_talent_flow, v2_litigation_ip, v2_master_events, v2_event_timeline, v2_earnings_events, and v2_partnership tables all returned zero rows for this company.

---

## (j) Data coverage & known gaps

**Tables checked vs. populated.** 49 list-type tables were checked in the source bundle for Cerebras Systems. Three returned rows: `legacy_companies_row` (1), `aibq_company_snapshots` (69), and `aibq_unicorn_scores` (6). The remaining 46 returned zero rows, spanning the entire v2/AIBQ tracking layer (`v2_company_registry`, `v2_financial_history`, `v2_master_events`, `v2_event_timeline`, `v2_talent_flow`, `v2_litigation_ip`, `v2_earnings_events`, `v2_partnership`, `aibq_daily_scores`, `aibq_score_tracker`) and every `canon_*`, `shared_*`, `framework_*`, `command_center_*`, and `timeline_*` table in the bundle. A 50th table, `timeline_source_stats`, is a dict rather than a list and reports `total_rows_seen: 0`.

**Flags raised in this profile, collected:**

1. **DISPUTED — HQ.** Legacy DB: Palo Alto, CA. Unicorn-score rows: Sunnyvale, CA/US (all three populated instances). Not reconciled.
2. **DISPUTED — FY2025 GAAP net income.** $87.9M (SiliconAngle/Wikipedia) vs. $237.8M including a $363.3M non-cash forward-contract gain (TechMarketBriefs). Source instruction preserved: do not attribute profitability without S-1 reconciliation.
3. **Internal inconsistency — RPO multiple.** Source states both ~53x and ~48x FY2025 revenue for the same $24.6B RPO figure; direct calculation gives ~48.2x.
4. **Internal inconsistency — PBQ CE sub-score.** Three same-day, same-composite (5.28) PBQ rows report CE values of 3.5, 3.0, and 7.0 respectively.
5. **Observation — PBQ valuation-rank drift.** Rank climbs 110 → 187 → 422 across three same-day passes explicitly marked as duplicates in source; read as cohort growth, not a re-scored company.
6. **Observation — PBQ stale inputs.** The PBQ score rationale prices Cerebras off ~$100M revenue / ~$700M raised / $4B post-money, well below the legacy DB's contemporaneous $510M ARR / $4.62B raised / $26.6B valuation.
7. **Observation — undated headcount comparison.** Prior headcount (71) carries no date, so the jump to 400 cannot be annualized.
8. **Observation — duplicated prior-growth figure.** Prev Revenue Growth YoY % (0.76) is identical to the current-period value (0.76); likely an extraction artifact rather than an independently measured prior figure.
9. **Observation — static snapshot series.** All 69 daily snapshot rows (2026-05-12 to 2026-08-11) are field-for-field identical; no re-extraction appears to have occurred in three months.
10. **Gap — unattributed score row.** One unicorn-score row (Composite 7.65, Confidence High, dated 2026-05-13) has no Framework, Batch, HQ, Industry, or PBID and cannot be attributed to AIBQ or PBQ.

**Embargo check.** No cross-company quality-vs-valuation correlation, coefficient, scatter plot, or fitted-line appears anywhere in this profile or in the cleaned JSON. Nothing in the Cerebras-specific source bundle referenced that statistic in the first place, so nothing had to be withheld from it — this note exists to confirm the check was made, not because the material required redaction.

---

## Sources

**Named in the legacy DB row's ARR Source field:** SEC S-1/A filing (Nasdaq, Apr–May 2026); SiliconAngle (May 4, 2026); Cerebras Systems press release (Feb 3, 2026); TechMarketBriefs S-1/A analysis; TechCrunch (Apr 18 and May 4, 2026). GAAP net income figures additionally reference Wikipedia (one side of the disputed pair) and TechMarketBriefs (the other side).

**Internal NEXUS source pages:** legacy Companies DB row — `https://app.notion.com/p/35d5e7ad9f7f81be8256d1ff8f24faa1`; AIBQ score leaf page — `https://app.notion.com/p/3af5e7ad9f7f81eba801c1954baf35f4`. Each of the 6 Unicorn Score rows and each of the 69 daily snapshot rows carries its own Notion page URL in the source bundle and the cleaned JSON companion to this file; not enumerated individually here given Section (c) confirms the 69 snapshot rows are field-identical.

**Companion file:** `cerebras-systems.json` in this same directory — cleaned, structured version of every figure in this profile, plus the full data-quality-flag ledger and the exact list of empty source tables.
