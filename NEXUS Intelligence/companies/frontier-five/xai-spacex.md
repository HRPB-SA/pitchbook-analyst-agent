# xAI / SpaceX — NEXUS Intelligence Profile

**Tier:** Frontier Five &nbsp;|&nbsp; **Profile built:** 2026-08-11 &nbsp;|&nbsp; **Coverage:** combined entity (xAI's valuation is carried inside its listed parent, SpaceX)

> **Staleness notice.** The NEXUS Notion *profile* page for this entity was last fetched **2026-05-05** — one of the stalest company pages in the workspace — and still shows a flat "AIBQ Composite: 5.0 (structural)" snapshot. This document instead draws on the fresher linked databases bundled with it (daily AIBQ score series through 2026-07-06, canonical figures through 2026-07-16, event log through 2026-08-11, morning-digest index through 2026-08-10). Every figure below is date-stamped individually; where the bundle itself disagrees with itself, both readings are shown rather than one being silently adopted. Full machine-readable detail, including the complete raw event/score logs, is in the companion file `xai-spacex.json`.

---

## (a) Overview

xAI was incorporated in Nevada in March–April 2023 (X.AI Corp., est. 2023-03-09) by Elon Musk, days after he resigned from OpenAI's board. It launched publicly on 2023-07-12 with 11 researchers under the stated mission "understand the true nature of the universe," and shipped Grok-1 on 2023-11-04 exclusively to X Premium+ subscribers. Between January 2024 and January 2026 it raised through Series A–E plus a $5B debt facility, reaching a $230B valuation on a $20B Series E (2026-01-06) — at the time the largest private AI raise on record.

**Two structural changes reshaped the entity in 2026, and both are documented in the source material:**

1. **SpaceX acquisition (2026-02-02).** SpaceX acquired 100% of xAI in an all-stock transaction valuing xAI at **$250B** (combined entity $1.25T, at an exchange ratio of 0.1433 SpaceX shares per xAI share). xAI became a wholly owned SpaceX operating subsidiary; all prior xAI preferred stock converted or was cashed out; Elon Musk became the effective sole decision-maker for the subsidiary. (X Corp/Twitter had already become a wholly owned xAI subsidiary in 2025, so the SpaceX deal folded X in as well.) This event alone is independently logged nine separate times in the raw event tables — scraped from nine different outlets/aggregators — with no material disagreement on the $250B/$1.25T figures themselves.

2. **Dissolution into "SpaceXAI" (early May 2026).** Elon Musk subsequently dissolved xAI as a standalone company and folded it into "SpaceXAI" — a subsidiary brand rather than an independently governed entity. Musk was quoted publicly: *"xAI will no longer exist as a separate company. It will just be SpaceXAI."* The NEXUS digests disagree on the exact date: the 2026-05-12 digest dates the formal dissolution to **May 7**; the 2026-05-16 digest, quoting Musk directly, dates it to **May 6**. The same week, SpaceX leased xAI's *entire* Colossus 1 cluster (~220,000–222,000 NVIDIA GPUs, 300+ MW, Memphis) to rival Anthropic — xAI's own utilization of that cluster was reportedly only ~11% at the time, against a ~40%+ hyperscaler norm, and New Street Research estimated the lease would generate $3–5B/yr in cash profit for SpaceX. Musk separately referenced a "right to reclaim" clause over the leased compute in public posts, but that clause was absent from the formal press release and its status in the signed contract is unconfirmed. Co-founder-departure counts are internally inconsistent across sources (11/11 referenced 2026-05-05; 9/12 as of 2026-05-12; "all twelve"/"all except Musk" as of 2026-05-16) — preserved as-is rather than reconciled. On 2026-08-11 (this profile's own build date), the *New York Times* reported that named xAI co-founder Igor Babuschkin is building an independent open-source AI venture, "River AI" — consistent with, though not itself proof of, the exodus narrative.

**Valuation-carried-inside-parent caveat.** Since SpaceX's IPO (2026-06-11), xAI/SpaceXAI has had **no independently observable market valuation**. SpaceX now trades as one consolidated public company (Nasdaq: SPCX) reporting three segments — Starlink/Connectivity, Space/launch, and an "AI segment" carrying xAI, Grok, and X. Any "xAI valuation" quoted after 2026-06-11 is therefore necessarily either (a) the frozen historical $250B acquisition mark, which does not move with the market, or (b) an internally derived sum-of-the-parts (SOTP) residual — SPCX market cap minus estimated Starlink and Space segment value — which the source system itself rates **T4/unverified and VOLATILE**. See Section (d) for the full ladder.

Business description: foundation-model developer (Grok family), now the AI/compute segment of SpaceX, encompassing Grok, the X platform, and the Colossus 1 & 2 Memphis GPU clusters. HQ is listed variably as San Francisco/Palo Alto, CA; Memphis, TN is the primary compute site.

---

## (b) Current scores

### Headline: AIBQ Composite **4.49** ("Developing") — as of **2026-05-27**, reaffirmed unchanged 2026-06-12 and 2026-07-06

| Dimension | Score | Prior | Weight | Driver of latest change |
|---|---|---|---|---|
| CE — Capital Efficiency | 2.5 | 3.0 | 20% | SpaceX S-1 (2026-05-20): CapEx $12.7B vs. $3.2B revenue = ~4x burn |
| RQ — Revenue Quality | 4.3 | 4.3 | 25% | unchanged this cycle |
| CI — Compute Independence | 9.0 | 9.0 | 15% | unchanged this cycle (already best-in-cohort) |
| GO — Governance Optionality | 3.5 | 2.5 | 20% | S-1 IPO path activation (GO-3) |
| MD — Moat Durability | 4.3 | 3.8 | 20% | Cursor $60B option, 550M MAUs, Anthropic named as compute customer |

- **CRA (Conflict Risk Adjustment):** **0** as of 2026-05-27 onward. Before that date it was **-0.25** (raw weighted composite ~4.285, minus the 0.25 penalty applied whenever 2+ dimensions read ≤3.0 — both CE=3.0 and GO=2.5 triggered it pre-S-1). GO's rise to 3.5 on 2026-05-27 left only CE ≤3.0, which alone does not trigger CRA.
- **Confidence:** Medium (±3.0 confidence band) per the cross-cohort unicorn-score record dated 2026-05-26; the individual key metrics feeding the score (ARR, acquisition valuation, total raised, compute status) are each independently rated "Confirmed" in the AIBQ deep-dive's data-confidence map.
- **Source:** aibq_score_tracker "xAI — SpaceX S-1 Filed: GO Upgrade + CE Downgrade + MD Upgrade" (2026-05-27); canon_canonical_figures "xAI AIBQ v3.0 score 4.49" (Last Verified 2026-05-27, Status CANONICAL); daily-score row 2026-07-06 (unchanged, flagged "No").

### Conflicting / stale readings (do not treat any of these as "the" current score without the caveat attached)

| Reading | As of | What it is |
|---|---|---|
| **4.29** (asterisked) | 2026-08-10 | Most recent *dated* composite mention in the bundle — the 2026-08-10 morning-digest TL;DR line lists "xAI 4.29\*" with a noted **-0.20 delta vs. the May 27 canonical**, deferred to a "§17" not captured in this extract. Self-flagged by its own source as pending/unreconciled, not a confirmed new analyst-entered score change — no corresponding dimension-level row exists for early August. The same digest separately caught and corrected a ticker-collision error: a CXApp Inc. (ticker **CXAI**) earnings item had been misfiled under "xAI" by an automated feed. |
| **5.0** ("structural" / "v2, 5-dim") | 2026-05-05 (stale profile fetch) / 2026-05-28 (explicit score-tracker row) | A parallel scoring methodology, run alongside the v2.2/v3.0 track that produced 4.29/4.49. A canonical-figures note explains it uses a "structural composite" because "pure AIBQ formula output would be different due to the SpaceX compute offset." This is the figure the stale Notion profile page shows — coincidentally, not because the profile was updated. |
| **4.06** ("v3.0, May 28") | 2026-05-28 | A same-day row on the *same* v3.0 track as the 4.49 canonical, describing itself as a "carry-forward from May 27 baseline" but reading 4.06. The source system's own 2026-06-12 canonical-reconciliation row explicitly **re-asserts 4.49** and names this row as the erroneous/superseded "dual-batch divergence." The standalone AIBQ deep-dive document pulled for this profile (composite 4.06, CRA 0.25, ranked #9, most fields "Missing" in its confidence map) appears to trace to this same divergent batch rather than the reconciled canonical — treat that document's scorecard as superseded. |

A separate PBQ-framework track also carries SpaceX (not xAI specifically) at composite 8.2–8.8 as of 2026-05-13, pre-dating the IPO; included in the JSON for completeness but not comparable to the AIBQ reads above.

---

## (c) Financials

**First SEC-quality (T1) xAI financials arrived via the SpaceX Form S-1, filed 2026-05-20**, as an "AI segment" carve-out combining xAI, Grok, and X. Everything before that date is PitchBook/press estimate-tier (T2/T3) and is labeled as such below.

### Filed / audited-adjacent (SEC S-1, T1, filed 2026-05-20)

| Metric | FY2025 | Q1 2026 |
|---|---|---|
| Revenue | **$3,201M** | $818M (~$3.3B annualized) |
| Operating loss | **$(6,355)M** | $(2,469)M |
| Operating margin | **-199%** | — |
| CapEx | $12,727M | $7,723M (~$30.9B annualized) |
| Adjusted EBITDA | $(1,237)M | $(609)M |

CapEx-to-revenue for FY2025 runs ~4.0x ($12.7B / $3.2B) — cited directly as the driver of the 2026-05-27 CE score downgrade. A separate T3 estimate (Fortune, citing Granda) inside the same canonical-figures table suggests *true* AI revenue excluding X-platform advertising may be only ~6.7% of the disclosed segment total (~$1.25B of the $3.2B) — i.e., most of the disclosed "AI segment" revenue may be X ads/subscriptions rather than Grok-specific revenue. This is flagged as an estimate, not confirmed in the S-1 itself.

### Earlier estimate-tier figures (PitchBook / press, T2–T3, pre-S-1)

- ARR 2025A: **$3.2B** — labeled "[CANONICAL]" in the shared financial-model-inputs table, sourced to PitchBook (Grok API + enterprise contracts). ARR 2024 estimate: ~$200M (Medium confidence, pre-Grok-3 scale).
- A separate daily-snapshot series (aibq_company_snapshots) carries ARR flat at $3,200M through 2026-06-09, then steps to **$3,830M** from 2026-06-10 through the latest row (2026-08-11) — this step is *not* the S-1 figure and its only cited source is a Bloomberg article dated 2025-12-01; treat as a lower-tier, loosely-dated estimate layered on top of the S-1 number, not a replacement for it.
- Gross margin 20%; gross profit $640M; cumulative losses $13.0B; burn rate $800M/month; runway 18 months; NRR 1.1%; enterprise mix 25%; revenue per employee $1.6M.
- **Headcount: 4,900** (PitchBook-verified, as of 2026-02-24, carried flat through 2026-08-11) — this figure directly **contradicts Elon Musk's own sworn testimony** on 2026-04-30 (Musk v. Altman/OpenAI trial) that xAI had "a few hundred employees." The order-of-magnitude gap was itself cited as a Governance-dimension score driver (GO -0.5, logged 2026-05-05).
- Total capital raised: $42.1B pre-S-1, stepping to **$45.0B** in the 2026-08-05 snapshot onward (source/date for the step not independently corroborated elsewhere in this bundle).

### Context, not xAI's own financials

- **SpaceX (parent) consolidated FY2025:** revenue $18.7B, net income $(4.9)B, adjusted EBITDA $6.6B. Segments: Starlink/Connectivity $11.4B revenue (63% segment adj. EBITDA margin); Space/launch $4.09B revenue ($(660)M operating); AI segment (xAI) $3.2B revenue.
- **Anthropic Colossus compute deal (disclosed in the same S-1):** $1.25B/month through May 2029 (~$45B implied total), 90-day termination notice, Anthropic retains all IP, covering the full Colossus 1 cluster. Estimated to generate $3–4B/yr cash profit for SpaceX (New Street Research, T3). This is Anthropic's revenue arrangement, not xAI's, but is included here as directly relevant context since it runs through SpaceX-owned infrastructure that was built for xAI.

---

## (d) Valuation & funding history

| Date | Event | Valuation | Tier |
|---|---|---|---|
| 2024-01-11 | Series A, $135M (Glade Brook Capital, Principled Investments) | undisclosed | T2 |
| 2024-06-10 | Series B, $6B (Valor/Sequoia/a16z-led) | $24B | T2 |
| 2024-11-20 | Series C, $6B (MGX-led, 51 investors) | $50B | T2 |
| 2025-06-20 | Debt financing, $5B ($3B bonds + $2B term loans, Apollo/Vista/Diameter) | n/a | T2 |
| 2025-07-01 | Later-stage raise, $5B (SpaceX joins as investor) | $113B | T2 |
| 2026-01-06 | Series E, $20B (NVIDIA/Valor-led, 35 investors) | $230B | T1 Primary (PitchBook) |
| 2026-01-22 | SpaceX confidential S-1 filed | IPO target ~$1.75T | T1 Primary |
| **2026-02-02** | **SpaceX acquires xAI, all-stock** | **$250B** (combined entity $1.25T) | **T1 Primary — historical print, STABLE, does not decay** |
| 2026-05-20 | SpaceX *public* S-1 filed | target reaffirmed ~$1.75T | T1 SEC |
| 2026-06-11 | SpaceX IPO priced | **$135.00/share**, $75B raised, all-primary — largest US IPO in history | T1 SEC/audited |
| 2026-06-12 | SPCX Nasdaq debut | day-one close $161.11 (+19.3%), ~$2.11T market cap | T2, STABLE historical print |
| 2026-06-16 | — | SPCX all-time-high close $225.64/share | T2 |
| 2026-07-06 | SPCX added to Nasdaq-100 (effective Jul 7) | close $162.00 — explicitly flagged as "a flow event, not a fundamentals delta" | T2 |
| **2026-07-15** | **SPCX closes below its $135 IPO price for the first time** — named NEXUS trigger FIRED | exact level **DISPUTED**: $135.27 close/range $132.15–139.34 (Investing.com) vs. $135.52 intraday ATL (TradingView, Jul 14) vs. $140.95 open (CNN) — sources disagree ~6% | event T2 cross-confirmed (CNBC/Yahoo); level T3 |
| 2026-07-15/16 | — | SPCX market cap ~**$1.77–1.81T** — down ~$300–340B (14–16%) from the day-one close over five weeks | T3 media |

### xAI's implied valuation post-IPO (SOTP estimate — not a market quote)

Because SpaceX consolidated the AI segment into one public entity, xAI has no standalone quote. The bundle carries an internal sum-of-the-parts residual (SPCX market cap minus estimated Starlink value $250–500B, minus estimated Space value $40–100B, minus $75B IPO cash):

- As of the 2026-06-12 close: **~$1.4–1.7T** (est.)
- As of the 2026-07-15 tape: **~$1.10–1.41T** (est.) — rated **T4 unverified, Decay Class VOLATILE**
- On the same basis, implied revenue multiple is cited as **>400x** FY2025 AI-segment revenue — an extreme, low-confidence derived figure, not an observed market multiple.

### A conflicting, apparently-stale valuation field

A separate daily field ("Latest Valuation (USD B)" in the aibq_company_snapshots / legacy_companies_row tables) carries xAI at a flat-ish **$200–230B** band from 2026-03-23 straight through the most recent row in this bundle (**2026-08-11: $200B**) — i.e., it never picked up either the SpaceX IPO pricing or the post-IPO SOTP re-estimate above. The underlying "legacy" company row shows "Last Refreshed [by analyst]: 2026-05-04" against "Last Extracted [by scraper]: 2026-08-10" — confirming the scraper kept re-pulling a page whose analyst-entered content had not moved since early May. This reads as a stale, unreconciled field rather than a genuine third valuation opinion; it is shown here, not suppressed, per instruction.

---

## (e) Cap table & investors

The bundle's dedicated cap-table database is **empty (0 rows)** for this entity — no granular share-class/ownership table exists in the source system. This section is reconstructed from funding-round investor lists, the S-1, and score-tracker notes.

**Notable investors across xAI's pre-acquisition funding rounds:** NVIDIA, Valor Equity Partners, Sequoia Capital, a16z, Tesla, Fidelity, Coatue, Temasek, QIA, JPMorgan Chase, MGX (Abu Dhabi), AMD, KIA, BlackRock, Morgan Stanley, SpaceX (as an investor pre-acquisition, Jul 2025), Seven Seven Six, DBL Partners, Glade Brook Capital, Principled Investments, Gorilla Private Equity, Inflection Ventures, 1789 Capital, Kingdom Holding.

**Debt:** $5B facility (2025-06-20) — $3B senior secured bonds + $2B term loans, SOFR+725, led by Apollo, Vista Equity Partners, and Diameter Capital (UBS as placement agent).

**Post-acquisition structure (from 2026-02-02):** SpaceX controls 100% of xAI; all prior xAI preferred stock converted or was cashed out; Elon Musk is the effective sole decision-maker for xAI specifically. The subsidiary's board composition is recorded simply as "Elon Musk" — no independent directors disclosed for xAI itself (distinct from the SpaceX parent board).

**SpaceX parent cap structure, post-IPO (2026-06-11):** dual-class, 10:1 (Class B = 10 votes); Musk holds majority voting control; the S-1 explicitly claims the "controlled company" exemption from majority-independent-board rules. 555.6M shares offered at IPO; ~13.076B total shares outstanding; float ~4.2%. Headline lockup 366 days, refined by a separate NEXUS trigger to a staged unlock of ~911.5M shares beginning 2026-08-06 through December 2026 (T4, unverified schedule). Lead underwriters: Goldman Sachs, Morgan Stanley, BofA, Citi, JPMorgan. Named SpaceX board members: Elon Musk (Chair), Kimbal Musk, Luke Nosek, Steve Jurvetson (others undisclosed per one intelligence row).

**Cursor — option, not a completed acquisition.** Several lower-tier event records (mostly Feb-2026-dated aggregator rows) describe SpaceX/xAI as having "acquired Cursor." The T1 S-1 (2026-05-20) instead describes an **option**: $60B implied equity value, with a $1.5B termination fee plus an $8.5B deferred services fee if it lapses. The S-1's language is treated as authoritative here over the "acquisition" framing in lower-tier rows.

---

## (f) Litigation & IP

| Case | Filed | Jurisdiction | Status | Issue | AIBQ impact |
|---|---|---|---|---|---|
| xAI CSAM Incident Investigation | 2026-03-15 | Regulatory authorities | Monitoring | Grok implicated in mass CSAM-adjacent deepfake creation | GO |
| Tennessee Deepfake Class Action vs. xAI | 2026-03-16 | Tennessee state court | Active | Grok-generated deepfakes; right-of-publicity violations | GO -0.2 |
| Baltimore CSAM Lawsuit vs. xAI | 2026-03-31 | D. Md. (Baltimore) | Active | Grok-generated CSAM content; minor-protection violations | part of the Mar-31 GO cascade (-1.0/day cap) |
| Amsterdam Injunction vs. xAI/Grok | 2026-03-31 | Amsterdam District Court | Active | GDPR/EU data-protection, content safety | part of the same cascade |
| Musk v. Altman/OpenAI (distillation testimony) | 2024-02-29 (testimony 2026-04-30) | N.D. Cal. | Active | Musk alleges OpenAI breached founding agreement; own 2026-04-30 testimony admitted Grok was "partly" distilled from OpenAI models — a self-inflicted moat/credibility hit | GO -0.3, MD -0.3 |

**Additional legal/regulatory items from the broader event log (not in the core tracked-case table above):**

- **2026-05-11:** 46 unpermitted gas turbines at Colossus 2 (Clean Air Act exposure) reported; **NAACP/SELC lawsuit** follows. Drove GO 2.5 → 2.3 (2026-05-14). Also bundled with reports of Grok generating nonconsensual sexualized images.
- **~2026-06-01:** Pentagon CDAO (Chief Digital and AI Officer) files a suit involving xAI — single-outlet sourced (justsecurity.org) within this bundle, not independently corroborated here.
- **2026-08-01:** A Minnesota judge **denies** xAI's request to block the state's ban on AI "nudify" apps; xAI had sued on First Amendment grounds.
- **Regulatory inquiries (context, not tracked as case rows):** Ireland DPC large-scale inquiry, EU Commission inquiry, UK government inquiry, and French cybercrime prosecutors raiding X's offices — all referenced as supporting evidence inside a 2026-05-05 forecast log entry rather than tracked independently; lower confidence on verification within this bundle.

**Forward compliance targets (not yet-occurred events, included for completeness):** SpaceX will not fully remove Colossus's unpermitted turbines for "another year" per 2026-07-31 reporting; separate items cite a 2027-07-31 turbine-removal commitment and a 2027-12-31 target for removing 69 temporary turbines at a Southaven facility. All three are still pending as of this profile's 2026-08-11 build date.

---

## (g) Active forecasts

**21 forecasts** are logged against this entity in the Forecast Calibration Log, spanning 2026-05-03 to 2026-05-20 log dates. **18 of the 21 have already passed their stated test date** (relative to this profile's 2026-08-11 build date) **without an Actual Outcome/Resolution recorded** in this bundle — a maintenance gap in the source system, not adjudicated here. Selected examples:

| Test date | Forecast | P | Status vs. today |
|---|---|---|---|
| 2026-05-07 (passed) | SpaceX/xAI Cursor acquisition confirmed via T1 source within 14 days | 0.40 | Unresolved in log — but the 2026-05-20 S-1 describes an *option*, not a completed acquisition, so this appears to have effectively resolved NO |
| 2026-06-21 (passed) | IPO roadshow begins within 60 days (logged 2026-04-21) | 0.45 | Unresolved in log — but the roadshow did begin on schedule, 2026-06-08, per the events calendar |
| 2026-07-04 (passed) | Aggressive coding-team hire-out or acquisition within 60 days | 0.65 | Unresolved |
| 2026-08-01 (passed) | SpaceX files S-1/announces IPO intent as SpaceXAI by Aug 1 | 0.55 | Effectively resolved YES (S-1 filed 2026-05-20, well ahead of the window) but not marked resolved |
| 2026-08-04 (passed) | Grok 5 "early preview" on/before Aug 4 | 0.55 | Unresolved — no Grok 5 preview logged in this bundle as of 2026-08-11 |
| 2026-08-08 (passed, 3 days ago) | SEC EDGAR shows SpaceX confidential S-1 filing by Aug 8 | 0.55 | Effectively resolved YES much earlier (public S-1 filed 2026-05-20) but not marked resolved |
| **2026-09-30 (open)** | Grok 5 ships publicly before Sept 30, 2026 (CONTRARIAN) | 0.30 | Still open |
| **2026-09-30 (open)** | SpaceX/xAI IPO S-1 filing with combined-entity financials by Sept 30 | 0.45 | Already satisfied by the May 20 S-1, but test date not yet reached |
| **2026-12-31 (open)** | SpaceX IPO delayed past H2 2026 (CONTRARIAN) | 0.25 | Already falsified by the June 11 IPO, but test date not yet reached |

Full list of all 21 forecasts, with invalidators and binary tests, is in the JSON (`active_forecasts.forecasts`).

---

## (h) Notable events

The bundle contains **124 discrete event/announcement/litigation/score-change records** for this entity across its various logs (18 master events + 81 timeline events + 1 event-timeline row + 1 partnership + 2 earnings/calendar + 5 litigation + 13 material score-change events + 3 media-outreach items), **plus a 105-row daily AIBQ score-tracking series** layered on top (mostly flat carry-forward, material only on the ~18 dates called out in the score history). Nine of the timeline rows are independent re-reports of the single 2026-02-02 SpaceX–xAI acquisition from different outlets. The full raw log of all of the above is preserved in the companion JSON (`events.curated_top_events` for the curated list below, `raw_sections_reference` for everything). **36 events are curated below**, ordered chronologically, by importance:

1. **2023-03-09** — X.AI Corp. established / Musk resigns OpenAI board (High)
2. **2023-07-12** — xAI launches publicly with 11 researchers (Critical)
3. **2023-11-04** — Grok-1 launched exclusively to X Premium+ subscribers (Critical)
4. **2024-01-11** — $135M Series A, first external funding (High)
5. **2024-03-28** — Grok-1 open-sourced, 314B-parameter MoE, Apache 2.0 (Critical)
6. **2024-06-10** — $6B Series B at $24B valuation (Critical)
7. **2024-10-01** — Colossus Memphis completed, 100,000 NVIDIA H100 GPUs — world's largest cluster at launch (Critical)
8. **2024-11-20** — $6B Series C at $50B valuation (Critical)
9. **2025-06-20** — $5B debt financing (High)
10. **2025-07-01** — $5B raise at $113B valuation; SpaceX joins as an investor (Critical)
11. **2026-01-06** — $20B Series E at $230B valuation — largest private AI raise on record at the time (Critical)
12. **2026-02-02** — **SpaceX acquires xAI, $250B all-stock; combined entity $1.25T; xAI becomes SpaceX subsidiary** (Critical; independently reported 9+ times)
13. **2026-03-16** — Tennessee deepfake class action filed (High; GO -0.2)
14. **2026-03-26** — xAI-led $40B buyout/LBO of Aligned Data Centers, $11B associated debt (High; CI +0.2)
15. **2026-03-31** — GO cascade day: Baltimore CSAM suit + Amsterdam GDPR injunction + founder-exodus reporting hit simultaneously — GO 4.8→3.8, the maximum single-day cascade penalty (Critical)
16. **2026-04-30** — Musk testifies under oath that xAI "partly" distilled Grok from OpenAI models; separately claims "a few hundred employees" vs. PitchBook-verified 4,900 (Critical; GO -0.3, MD -0.3)
17. **2026-05-05** — Grok 4.3 launch (#1 on CaseLaw v2 and CorpFin benchmarks) + voice-cloning suite + X ad-stack integration (High; RQ +0.3)
18. **2026-05-06** — SpaceX leases xAI's *entire* Colossus 1 cluster (~220–222K GPUs, 300+ MW) to rival Anthropic; xAI's own utilization was ~11% pre-lease (Critical — "biggest single-day CI change in NEXUS history")
19. **2026-05-06/07** — Musk dissolves xAI as a standalone company, folds it into "SpaceXAI" (Critical; date and co-founder-count conflicts, see Overview)
20. **2026-05-11** — 46 unpermitted gas turbines at Colossus 2 reported; NAACP/SELC lawsuit follows (High; GO 2.5→2.3)
21. **2026-05-15** — Grok 4.1 Fast deprecated with under two weeks' notice, no migration path — developer backlash (High; MD 3.8→3.5)
22. **2026-05-20** — **SpaceX S-1 filed** — first SEC-quality xAI financials; Anthropic's $1.25B/mo Colossus deal disclosed; Cursor $60B option disclosed; 550M MAUs/117M Grok MAUs disclosed (Critical; AIBQ 4.29→4.49)
23. **~2026-06-01** — Pentagon CDAO files suit involving xAI (Medium; single-source)
24. **2026-06-08** — SpaceX IPO roadshow begins (Critical)
25. **2026-06-11** — SpaceX IPO priced $135.00/share, $75B raised — largest US IPO in history (Critical)
26. **2026-06-12** — SPCX Nasdaq debut, day-one close $161.11 (+19.3%), ~$2.11T market cap (Critical)
27. **2026-06-16** — SPCX all-time-high close, $225.64/share (High)
28. **2026-07-06** — SPCX added to Nasdaq-100; AIBQ composite reaffirmed unchanged at 4.49 (Medium)
29. **2026-07-08** — Grok 4.5 released — 1.5T-parameter "V9" model, coding/agentic focus, trained on NVIDIA GB300 GPUs, incorporates Cursor data; Musk called it "Opus-class" (High)
30. **2026-07-15** — **SPCX closes below its $135 IPO price for the first time** — named trigger fired; exact level disputed (Critical)
31. **2026-07-16** — SPCX market cap marks ~$1.77–1.81T, down 14–16% from day-one close; xAI SOTP-implied value recomputed to ~$1.10–1.41T (Critical)
32. **2026-07-31** — Reporting confirms unpermitted Colossus turbines won't be fully removed for "another year" (Medium)
33. **2026-08-01** — Judge denies xAI's First Amendment challenge to Minnesota's AI "nudify" app ban (Medium)
34. **2026-08-05** — xAI launches "Imagine" image/video generation product (Medium)
35. **2026-08-10** — Digest flags xAI composite at 4.29 (asterisked, pending reconciliation); same digest catches and corrects a CXApp/xAI ticker-collision miscue (Medium — data-quality item)
36. **2026-08-11** — NYT reports xAI co-founder Igor Babuschkin building independent venture "River AI" (Medium — most recent dated item in the bundle)

---

## (i) Open conflicts / disputes

Per instruction, both sides of every disputed figure are shown with dates and sources — none is silently resolved.

1. **AIBQ composite — which figure is "current."** 4.49 (2026-05-27, reaffirmed through 2026-07-06, canonical) vs. 4.29\* (2026-08-10, self-flagged unreconciled) vs. 5.0 (a different "structural"/v2-5-dim methodology, 2026-05-05/05-28) vs. 4.06 (2026-05-28, a divergent same-day batch explicitly superseded by the 2026-06-12 reconciliation). This profile's headline uses 4.49; all four are carried in Section (b).
2. **Valuation — which figure is "current."** $250B acquisition print (2026-02-02, historical, does not decay) vs. a $200–230B daily-snapshot field that appears never to have been reconciled to the IPO (flat through 2026-08-11) vs. ~$1.77–1.81T SPCX consolidated market cap (2026-07-15/16) vs. ~$1.10–1.41T xAI-specific SOTP estimate (2026-07-15 tape, T4/VOLATILE). All four are carried in Section (d); none is presented as sole "the" valuation.
3. **Dissolution announcement date:** May 7 (2026-05-12 digest) vs. May 6 (2026-05-16 digest, quoting Musk directly).
4. **Co-founder departure count:** "11/11" (referenced 2026-05-05) vs. "9/12" (2026-05-12) vs. "all twelve"/"all except Musk" (2026-05-16) — both the numerator and the denominator (11 vs. 12 total co-founders) shift across sources.
5. **SPCX Jul-15 break level:** $135.27 close/range $132.15–139.34 (Investing.com) vs. $135.52 intraday ATL (TradingView) vs. $140.95 open (CNN) — ~6% spread; the *event* (breaking below $135) is cross-confirmed T2, the *exact level* is not, and the source system itself carries this as "Frozen" / unresolved.
6. **PBID inconsistency:** 533035-45 (15 citations, dominant, treated as authoritative here) vs. 544397-05 (1 citation, in v2_company_registry) vs. 606742-48 (1 citation, in command_center_master_profiles) — the latter two look like isolated data-entry errors.
7. **Cursor — "acquisition" vs. "option."** Multiple Feb-2026 aggregator rows describe a completed acquisition; the T1 S-1 (2026-05-20) describes a $60B implied-equity option with termination/deferred-fee terms, not a closed deal. The S-1 language is treated as authoritative.
8. **Acquisition-event year typo.** The single v2_master_events row for the SpaceX–xAI acquisition itself carries `date:Date:start = 2025-02-02` (Year field: 2025), inconsistent with every other reference to the deal in this bundle (including its own PitchBook deal description, the S-1, and the nine timeline_dated_events rows), all of which place it in **February 2026** — logically required since the $20B Series E that preceded it closed 2026-01-06. Treated as a one-row data-entry typo (year only) rather than a genuine competing date; preserved verbatim in the JSON for audit.
9. **Embargoed cross-company relationship.** Source material (the system's own Ruling 2, and multiple digest entries) documents that this research system computes a cross-company AIBQ-quality-vs-valuation relationship. **A cross-company quality-valuation relationship exists and is embargoed from publication** — per explicit instruction, no coefficient, per-point dollar figure, or scatter/fitted-line framing appears anywhere in this profile or its companion JSON (both were checked and, where the raw source material contained it, it was redacted and disclosed here rather than dropped silently).

---

## (j) Sources count

**135 non-empty source citations** (Source / Source URL / Source Name / Domain fields) were found across this entity's records in the bundle, resolving to **85 distinct domains or named sources**. These span:

- **T1 SEC:** sec.gov (SpaceX Form S-1, CIK 1181412)
- **T1/T2 Primary:** PitchBook (profile 533035-45), Anthropic's and xAI's own corporate blogs/news pages
- **T2/T3 press:** TechCrunch, Bloomberg, Fortune, CNBC, Reuters, VentureBeat, Mississippi Today, the New York Times, and roughly 75 further outlets, aggregators, and single-source blogs (full list in the JSON `sources.distinct_domains_list`)
- **Internal NEXUS methodology labels** (e.g., "Derived: SOTP residual…," "AIBQ v3.0 canonical scores") which are not external sources but are counted and separately labeled in the JSON

Only one dedicated official-domain authority record exists in the bundle's source-authority table (xai.com, authority score 9/official company source, last reviewed 2026-07-21) — a thin base for the "official primary source" tier specifically, though the SEC S-1 substantially strengthens overall source quality for the financial figures.

---

*Full machine-readable detail — including the complete 105-row daily AIBQ score series, all 21 forecasts with binary tests and invalidators, the full 124-record event log, the two verbatim source digests (2026-05-12 and 2026-05-16) documenting the dissolution/Colossus-1 event, and every raw NEXUS database table this profile draws on — is in `xai-spacex.json` alongside this file.*
