# Perplexity — NEXUS Intelligence Profile

**Coverage tier:** Extended Coverage (task-assigned; not Frontier Five). Bundle field `tier = "Extended Coverage"`. Note: within NEXUS's own three-band system, Perplexity's only dedicated company page lives under **AI Ecosystem** (companies ranked #26-100 by valuation, biweekly monitoring, basic scorecard) — even though its ~$20B valuation would nominally sit inside the #6-25 **AI Leaders** band occupied by peers such as Scale AI, Cursor, and Waymo. That placement is not reconciled anywhere in the source material and is flagged rather than resolved.

**PitchBook ID:** 517947-04 | **HQ:** San Francisco, CA | **Founded:** August 2022

**Generated:** 2026-08-11, from `bundles/perplexity.json` plus the AIBQ v3.0 company deep-dive page (`framework/companies/perplexity.md`) and surrounding framework/rubric documentation. Companion file: `perplexity.json` (full structured data, including the complete raw event log and every conflict identified below).

**Embargo check:** This profile was built under the standing rule that the cross-company AIBQ/PBQ quality-vs-valuation correlation coefficient tracked elsewhere in NEXUS is never to be stated, implied, or charted. That figure was searched for across this company's bundle and every framework document reviewed for scoring context and was **not found** anywhere in the material gathered for Perplexity. Nothing below states or implies it, and no score-vs-valuation chart or fitted line appears in this profile or its companion JSON; the score section (b) and the valuation section (d) are written and sourced independently of one another.

---

## (a) Overview

Perplexity was founded in August 2022 by Aravind Srinivas (CEO, ex-OpenAI/Google), Andy Konwinski (ex-Databricks/UC Berkeley), Denis Yarats (ex-Meta FAIR), and Johnny Ho, to build an AI-native "answer engine." The product line has since broadened well past search: a free Chromium-based browser (**Comet**), a general-purpose agent orchestrator (**Computer**, routing tasks across 20+ frontier models), and vertical configurations such as **Computer for Counsel** for legal teams. Monetization runs through freemium consumer Pro/Max subscriptions, an Enterprise Pro B2B tier, and a usage-based Agent API (expanded in August 2026 to include Claude Opus 4.7, GPT-5.5, and Grok 4.20).

- **Leadership:** Aravind Srinivas (CEO), Denis Yarats, Johnny Ho, Andy Konwinski. Recent churn: Peter Jackson departed within the last 90 days of the latest pull; Henry Jiménez and Anand Thangaraju joined.
- **Board:** Aravind Srinivas, a SoftBank observer, and an IVP seat.
- **Headcount:** 250 (up from 150 in the prior PitchBook pull).
- **Sector labels:** shown inconsistently across records as "AI Applications," "AI-APP," and "Business/Productivity Software" / "Application Software" depending on which PitchBook field is read.
- **Customers:** the bundle's "Customer Count" field reads 30,000,000 — at a 30% enterprise mix and a ~$10 revenue-per-customer figure, this is almost certainly monthly active/registered users, not paying accounts, and is presented here with that caveat rather than relabeled.
- **Domain authority:** perplexity.ai is scored 9/10 ("official tracked-company source") in NEXUS's own source-authority registry — the highest tier available.

## (b) Current scores

| Framework | Composite | Tier label | CE | RQ | CI / SV | GO | MD | Date | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| **AIBQ (canonical)** | **3.85** | Developing | 5.0 | 4.0 | 3.0 (CI) | 4.0 | 3.0 | 2026-05-12 | Medium |
| PBQ (alternate, non-canonical) | 6.30 | — | 7.0 | 5.5 | 7.0 (SV) | 6.0 | 5.0 | 2026-05-13 | High |
| Unlabeled framework (alternate, non-canonical) | 5.95 | — | 3.0 | 7.0 | — | 3.0 | 4.0 | 2026-05-13 | High |
| Stub entry | — (no composite recorded) | — | — | — | — | — | — | (undated) | Low |

The 3.85 AIBQ composite is the figure served by Perplexity's dedicated AIBQ Score page as fetched 2026-08-11 — the same 32-page framework crawl that covers all 32 AIBQ/PBQ v3.0 company pages. Under the rubric's carry-forward rule (scores persist between events; no interpolation), this reading has apparently not moved since 2026-05-12, three months prior. There is **no distinct prior score**: the shared 77-row AIBQ Score Tracker (the granular daily-change audit log) has zero entries for Perplexity — that log only covers the Frontier Five, consistent with Perplexity's lighter biweekly coverage tier.

**Open score conflict:** two other "Unicorn Scores" rows exist for Perplexity, both dated 2026-05-13 (one day after the canonical entry), scored under a *different* framework — PBQ substitutes Strategic Velocity (SV) for Compute Independence (CI) — and land materially higher (6.30 and 5.95 vs. 3.85). Perplexity's AIBQ-vs-PBQ classification is genuinely ambiguous under the framework's own four-question test (it does not clearly train its own >10B-parameter foundation models, but AI performance and compute access do bear on its product), which may explain why it was scored under both rubrics. Neither alternate reading has been adopted as canonical; both are preserved verbatim in the JSON.

## (c) Financials

*All figures dated 2026-08-11 unless noted; "prior" = the previous PitchBook pull on file.*

| Metric | Current | Prior |
|---|---|---|
| ARR | $450M | $450M |
| Gross margin | 40% | 35% |
| Headcount | 250 | 150 |
| Burn rate | $30M/mo | $25M/mo |
| Compute spend | $80M/yr | $50M/yr |
| Capital raised (cumulative) | $1,500M | $1,720M |
| NRR | 150% | 140% |
| Runway | 30 months | 24 months |
| Revenue per employee | $1,000K | $700K |
| NEXUS data-confidence score | 0.51 | 0.72 (declining) |

**ARR ladder (dated prints, company/press-sourced):** ~$50M (Oct 2024, at 100M MAU) → $100M (Dec 2024, Series D) → $200M (Sep 2025 Series E close, and again self-reported Jan 2026 at "4.7x YoY") → $450M (Mar 2026, "Perplexity Computer" launch, +50% in 30 days) → $500M (Apr 2026, claimed 335% YoY). The most recent five consecutive daily snapshots (through 2026-08-11) all read $450M, which is the value used here as current; $500M recurs on 40 of 115 tracked days and $450M on 57 — the two effectively alternate, read as noise around a $450-500M current run-rate rather than real week-to-week swings.

**Flagged, not adopted:** PitchBook's own profile carries a $1,000M revenue figure sourced explicitly as a "TTM (4Q2026)" field. NEXUS/PitchBook-analyst convention treats PitchBook TTM fields as forward-window projections, not a current run-rate — this figure is kept out of the ARR ladder above on that basis. Separately, the bundle's "Revenue Growth YoY %" field is stored as a bare **2** in both the current and prior pull, which is inconsistent with every dated narrative growth figure elsewhere in the same dataset (4.7x, 150%, 335% YoY at different points in 2026). Presented as-is; not reinterpreted.

## (d) Valuation & funding history

| Date | Round | Amount | Post-money | Lead |
|---|---|---|---|---|
| 2023-03-18 | Series A | $28.8M | $150M | Databricks Ventures, NEA |
| 2024-01-04 | Extension | $73.6M | $520M | Jeff Bezos (personal) |
| 2024-03-25 | Series B | $135M | $1.0B | IVP, Bezos, Daniel Gross |
| 2024-04-23 | Series C | $250M | $2.8B | Bessemer |
| 2024-12-16 | Series D | $500M | $9.0B | SoftBank, IVP |
| 2025-07-02 | Series E | $600M | $18.0B | Accel |
| 2025-09-11 | Extension (flat) | $200M | $20.0B | Glade Brook, Alpha |

Verified via PitchBook-sourced, analyst-confirmed event rows (12 of 12 marked `Verified: YES`); sums to ~$1.79B raised across rounds against a headline cumulative-capital field of $1.5B (small internal gap, not reconciled).

**Current mark — disputed.** No verified primary-source round beyond the September 2025 $20B flat extension exists in this bundle. Since January 2026, a wide set of independent but individually low-tier sources (Wikipedia, aggregator sites, a January 9 cluster of near-simultaneous reports) has repeatedly cited $21.21B, and a separate cluster cites $22.6B — the latter still being quoted as of July 2026 alongside a "45-50x revenue multiple, compressed from the 100x+ implied by the Sept-2025 round." None of these is backed by a dated primary deal record here. Perplexity's own PitchBook-linked profile (last refreshed 2026-05-04) still carries $20B, and across 115 days of internal daily tracking, $20B is the dominant reading (82/115 days, 71%) and the value returned on each of the last five consecutive days. **This profile anchors on $20B (as of 2026-08-11)** and carries $21.21B–$22.6B as an unresolved, recurring but unconfirmed higher mark — consistent with the analyst note on file: *"Flat round Sep 2025 suggests valuation reset. Additional raise likely 2026."*

## (e) Cap table & investors

No dedicated cap-table database exists for Perplexity in NEXUS (0 matches in the shared cap-table registry); this section is built from narrative fields and round-by-round investor lists.

- **Board:** Aravind Srinivas; SoftBank (observer); IVP (seat).
- **Strategic stakes:** Jeff Bezos, NVIDIA.
- **Investor rights:** SoftBank holds board-observer rights; Accel holds Series E board representation; standard preferred liquidation preference; the flat September 2025 round is read internally as a sign of investor pressure on growth trajectory.
- **Investors across the round history:** Databricks Ventures, NEA, Sequoia, Elad Gil, Andrej Karpathy, Jeff Dean, Yann LeCun (Series A); Jeff Bezos, Daniel Gross, IVP, NVIDIA (Series B); Bessemer, SK Telecom, SoftBank, T.Capital (Series C); SoftBank, IVP (Series D, 37 investors); Accel, NVIDIA, ServiceNow, QIA (Series E, 23 investors); Glade Brook, Alpha, Cristiano Ronaldo among 23 investors in the September 2025 close.

## (f) Litigation & IP

Three distinct matters plus one regulatory inquiry — a meaningfully active docket for a company this size:

1. **Perplexity User Data Sharing Class Action** (privacy/data, filed 2025-09-01, status Active). Alleges Perplexity sent user chats to Google and Meta without consent. Tagged to the Governance Optionality (GO) dimension.
2. **Amazon.com Services, LLC v. Perplexity AI** (CFAA / terms-of-service, concerning the Comet agentic-browsing/shopping tool). The 9th Circuit found Amazon "unlikely to succeed" on its CFAA claims — reasoning that the user, not Perplexity, is the principal directing the agent — and overturned an injunction (~June 2026). A second report dated 2026-08-05 ("Appeals Court Sides Against Amazon, Lifts Perplexity Ban") describes the same posture; this may be a later-stage reaffirmation of the same ruling rather than a fully separate event — not resolved, both dates kept.
3. **Reddit, Inc. v. Perplexity AI / SerpApi** (DMCA, data scraping for AI model development). Reddit advanced its claims July 31, 2026; a federal court denied the defendants' motion to dismiss on August 3, 2026, allowing the claims to proceed. NEXUS's own morning digest is explicit that this is *not* a liability finding — only that the claims are legally cognizable.
4. **Regulatory:** Italy's Competition Authority (AGCM) opened a consultation on Perplexity's contract terms (~July 2026), part of broader Italian scrutiny of digital service providers. Outcome not on file.

## (g) Active forecasts

No formal, dated forecast database rows exist for Perplexity anywhere in NEXUS (0 rows in both the bundle's own forecast slice and the 96-row shared forecasts registry). What is on file is qualitative:

- CEO Aravind Srinivas confirmed (CNBC, ~June 8-9, 2026) a **2028 IPO target**, explicitly independent of how OpenAI's or Anthropic's listings are received, framed around revenue-quality readiness rather than competitive timing pressure.
- Analyst note on file: *"Flat round Sep 2025 suggests valuation reset. Additional raise likely 2026."*
- Unverified press commentary (July 2026) frames the implied revenue multiple as having compressed from "100x+" at the September 2025 round to "45-50x" on the disputed $22.6B mark against $450-500M ARR.

## (h) Notable events

**94 dated event/litigation records were found** across the verified master-event feed (12 rows, all `Verified: YES`, PitchBook-sourced), the broader timeline feed (81 rows, all `Verified: NO`, press/aggregator-sourced), and the litigation register (1 row, mirrored across two feeds). Of the 81 timeline rows, **8 describe an entirely different company or an unrelated regulatory matter** (Samsara, OpenAI's own ARR, a Hitachi/Anthropic partnership, IREN's cloud ARR target ×2, a CFTC perpetual-contracts notice, a marketing vendor's namedrop of multiple AI engines, and an unrelated chip-startup raise) and were excluded below as source-tagging contamination, though they remain in the full JSON log. Two further rows carry what read as two-year date typos (2024 instead of 2026, given content that exactly matches well-corroborated 2026 events) and are likewise excluded from the curated list below but retained in the log. The full raw log, contamination set, and every row's original fields are preserved in `perplexity.json`.

Curated, in chronological order:

- **2022-08** — Founded by Srinivas, Konwinski, Yarats, Ho.
- **2022-12** — Public beta of the AI answer engine launches.
- **2023-03** — Series A, $28.8M at $150M (Databricks Ventures/NEA).
- **2023-11** — First AI platform to sign a direct GSA deal (government market entry).
- **2023-10** — Perplexity Pro subscription launches ($20/mo).
- **2024-01** — $73.6M raise led personally by Jeff Bezos at $520M — his first direct consumer-AI investment.
- **2024-03** — Series B, $135M at $1B — crosses the unicorn threshold.
- **2024-04** — Series C, $250M at $2.8B (Bessemer).
- **2024-10** — Enterprise Pro (B2B tier) launches.
- **2024-10** — 100M MAU / 1B queries per month milestone (~$50M ARR).
- **2024-12** — Series D, $500M at $9B (SoftBank/IVP).
- **2025-07** — Series E, $600M at $18B (Accel) — 2x valuation in 7 months.
- **2025-09** — User Data Sharing Class Action filed (privacy).
- **2025-09** — $200M flat extension at $20B (Glade Brook/Alpha).
- **2025-10** — Comet browser made free globally on desktop.
- **2026-01** — Valuation first reported at $21.21B, then $22.6B (both disputed marks, see §d; the $22.6B figure keeps recurring in press through at least July 2026).
- **2026-01/02** — "Computer," a general-purpose agent orchestrator, launches; later ships with Deep Research routing across 20+ models.
- **2026-03** — ARR surpasses $450M alongside the Computer launch.
- **2026-04** — ARR reaches $500M, claimed +335% YoY.
- **2026-06** — 9th Circuit overturns Amazon's CFAA injunction.
- **2026-06** — CEO announces 2028 IPO target, independent of OpenAI/Anthropic listings.
- **2026-06** — "Computer for Counsel" legal-vertical product launches.
- **2026-07** — Italy's AGCM opens a consultation on Perplexity's contract terms.
- **2026-07** — SPACE, a secure sandbox for AI agents, launches (1.25M sandbox creations, 11.9M reconnects in its first tracked week).
- **2026-07** — A former Comet engineer launches rival AI-browser startup Polar, raising a $5.7M seed round — a competitive talent-flow signal.
- **2026-07** — Reddit advances DMCA scraping claims against Perplexity and SerpApi.
- **2026-08** — Court denies motion to dismiss; Reddit's claims proceed.
- **2026-08** — Second appellate report describes Amazon's ban on Perplexity lifted (see litigation note on possible duplication).

## (i) Open conflicts / disputes

1. **Score framework:** canonical AIBQ 3.85 (2026-05-12) vs. alternate PBQ 6.30 and unlabeled 5.95, both dated 2026-05-13 — see §b.
2. **Valuation:** $20B canonical anchor vs. $21.21B–$22.6B recurring in unverified press since January 2026 — see §d.
3. **Revenue level:** PitchBook's TTM "$1,000M" field vs. the dated $200-500M ARR ladder — see §c.
4. **Revenue-growth field:** a bare "2" in the YoY-growth field is inconsistent with narrative figures of 4.7x/150%/335% found elsewhere in the same bundle.
5. **Tier placement:** task brief and bundle agree on "Extended Coverage," but Perplexity's $20B valuation would nominally sit inside NEXUS's own "AI Leaders" (#6-25) band; its only company page instead lives under "AI Ecosystem" (#26-100) — not reconciled in source material.
6. **Event dates:** two timeline rows (the $450M-ARR/agent-tool item and the Windows PC-agent-launch item) appear to carry 2-year date typos (2024 instead of 2026).
7. **Canon-layer coverage:** the highest-authority NEXUS "canon" dossier for Perplexity is an explicit stub — *"Unscored in v3.0 canon; no canonical figures, financial-history rows, or predictions"* (compiled 2026-07-21) — meaning every figure in this profile is drawn from the v2 registry / AIBQ tracker / timeline layers rather than the canon layer.

## (j) Sources

**82 distinct source URLs across 58 distinct domains** were cited in the underlying event, timeline, and litigation records (this count includes the URLs behind the 8 contamination rows excluded from §h, since those URLs are real, just mis-tagged to this company). Most-cited domains: perplexity.ai (7), my.pitchbook.com (6, PitchBook deal records), news.google.com (6), tracxn.com (5), techjacksolutions.com (4). Perplexity's own domain (perplexity.ai) carries a 9/10 authority score in NEXUS's source-authority registry — "official tracked-company source," the highest tier defined. Full domain breakdown is in `perplexity.json`.
