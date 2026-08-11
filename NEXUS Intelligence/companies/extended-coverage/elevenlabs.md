# ElevenLabs — NEXUS Intelligence Profile

**Coverage tier:** Extended Coverage (not Frontier Five) · Internal labels seen in source data: "T3-Ecosystem" / "Tier 3 — Specialists"
**PitchBook ID:** 509315-23 · **Sector:** AI Applications (PitchBook industry: Multimedia and Design Software) · **Verticals:** AI/ML, AudioTech, SaaS
**As of:** 2026-08-11 · **Companion data file:** `elevenlabs.json` (full event log, all computed fields)

> **Embargo note:** This profile does not compute, state, or imply any cross-company quality-vs-valuation relationship. Score and valuation figures are reported in separate sections and are not cross-referenced against each other.

---

## (a) Overview

ElevenLabs was founded in 2022 by **Mati Staniszewski** (ex-Google) and **Piotr Dąbkowski** (ex-Palantir) on a mission to make content universally accessible through AI voice synthesis. The company is headquartered in **New York, NY**, with additional offices in **London, UK** and **Warsaw, Poland** per the canonical registry, plus two newer offices that surface only in the dated event log: **Madrid** (opened ~May 2026) and **Toronto** (Canada business launched 2026-07-07, general manager Max Lemmens, with plans to double the Canadian headcount).

Staniszewski remains CEO. The most recent notable hire is **Alexander Holt as Field CTO** (~April 2026, per the legacy registry's Key Hires field — no independent dated event exists for this specific hire in the timeline).

**Product line:** voice cloning and text-to-speech (core), Dubbing v2 / Dubbing API (29-language AI video dubbing), conversational voice agents, the **Eleven v3** model (transformer-based, contextual emotional register, 70+ languages — announced ~January 2026, general availability February–March 2026), **ElevenMusic** (AI music generation), a **Music Marketplace** letting creators monetize AI-generated tracks (~$11M paid to voice creators to date per one source), **ElevenReader** (a $11/month consumer audiobook app licensing 200,000 human-narrated titles, positioned against Audible), and a transcription model described by one source as ElevenLabs' "most accurate transcription model ever" (January 2026). One registry field claims ElevenLabs and Google "dominate" Artificial Analysis' speech-to-text benchmark, though no date is attached to that claim.

Two overview items worth flagging up front rather than burying: the registry notes ElevenLabs joined **Brazil's Permanent Programme to Combat Disinformation** ahead of the 2026 elections (no specific date given), and — the item this brief was specifically asked to fold in —

**UK Government / AI Safety Institute partnership (2026-06-11).** The UK Government formalized an **expanded** AI partnership with ElevenLabs and the UK AI Safety Institute (AISI) to improve accessibility of public services through AI-generated voice technology. This deepens (not launches) existing collaboration across three research tracks: how citizens perceive AI-generated voice, how well people identify when they're interacting with an AI system, and how that interaction shapes behavior, trust, and decision-making. The NEXUS Morning Digest (2026-06-12 edition) classifies this as Tier One sourcing — a named government contract with a named safety body — and frames it as a moat-building, switching-cost event: ElevenLabs, not OpenAI or Google DeepMind (both of which field voice products), is the named partner. The same digest notes that OpenAI's Head of Countries, George Osborne, said at Founders Forum the same day that most governments discussing AI adoption "have yet to actually deliver on implementation" — a juxtaposition the digest calls the sharpest signal of the week. This event is corroborated by an independent (harvested, unverified) dated timeline entry with the same date and subject.

No litigation/IP activity field is populated in the structured registry (empty string); everything on that front comes only from the dated event log — see section (f).

---

## (b) Current scores

Two distinct scoring frameworks appear for ElevenLabs in source data — **AIBQ** and **PBQ** — and they are not the same rubric (PBQ substitutes an "SV" dimension for AIBQ's "CI" dimension). They should not be blended.

### Canonical current AIBQ score

| Composite | Rating | As of | Confidence | Valuation rank at time |
|---|---|---|---|---|
| **5.20** | Adequate | **2026-05-12** | Low | 21 |

**Sub-scores:** CE 7.0 · RQ 5.0 · CI 5.0 · GO 4.0 · MD 5.0

**Rationale (verbatim):** "CE7: ~$350M raised, strong revenue growth. RQ5: developer + enterprise, usage-based, growing but early. CI5: own voice models but cloud-hosted inference. GO4: young company, early governance. MD5: voice synthesis leader but competitive (Amazon, Google, startups)."

This record cross-checks exactly against the standalone AIBQ score card (`extract/framework/companies/elevenlabs.md`: "ElevenLabs: AIBQ 5.20 (Adequate)," same five sub-scores) and is treated here as the corroborated canonical current score.

**Prior score:** None found. No earlier-dated AIBQ-labeled composite exists anywhere in the bundle to serve as a comparison point — 2026-05-12 is the only record explicitly tagged `Framework: AIBQ` with a composite value.

### Other dated composites — not reconciled with the canonical score

| Date | Framework | Composite | Confidence | Sub-scores |
|---|---|---|---|---|
| 2026-05-13 | *(not stated)* | 6.65 | High | CE 8 · RQ 7 · GO 8 · MD 7 · CI n/a |
| 2026-05-14 | PBQ | 5.43 | Low | CE 3 · RQ 5 · SV 6.5 · GO 6 · MD 6 |

The 2026-05-13 record omits Framework, PBID, HQ, Industry, and Rationale — thinly populated relative to its neighbors — and is one day removed from the AIBQ 5.20 print yet ~28% higher with no stated rationale. The 2026-05-14 record is explicitly a different framework (PBQ) with rationale: *"CE: Rev est ~$100M / Raised ~$300M = 0.33x, pre-FCF. RQ: Mix consumer + enterprise AI voice, growing enterprise. SV: Voice synthesis/cloning/dubbing/agents, global, rapid releases. GO: CEO Mati Staniszewski. MD: #1 AI voice quality, but OpenAI/Google/Amazon Polly/PlayHT competition. Low API switching costs."* Neither is presented as "the" current score; both are logged as open conflicts (section i).

A separate intelligence note (aibq_unicorn_intel, 2026-05-14 vintage) names key competitors as **OpenAI TTS, Google Cloud TTS, PlayHT, and Resemble AI**, and rates API switching costs "Low."

---

## (c) Financials

### Canonical current snapshot (2026-08-11)

| Metric | Value | Prior |
|---|---|---|
| ARR | $330M | $330M |
| Revenue growth YoY | 4.5% *(see conflict below)* | 4% |
| Gross margin | 65% | 62% |
| Gross profit | $214.5M | $65M |
| NRR | 160% | 150% |
| Headcount | 300 *(see conflict below)* | 200 |
| Burn rate | $15M/mo | $12M/mo |
| Compute spend | $60M/yr | $30M/yr |
| Runway | 36 months | 30 months |
| Customers | 1,000,000 | 500,000 |
| Enterprise mix | 50% | 40% |
| Customer concentration | 15% | — |
| Revenue/employee | $333K | $250K |
| Implied ARR multiple | 33.33x | 33x |
| Total capital raised | $850M | $781M |
| Profitability | Generating Revenue / Not Profitable | — |

The implied ARR multiple checks out arithmetically: $11B valuation ÷ $330M ARR = 33.3x, matching the stated field — unlike OpenEvidence (see that profile).

### Two data-quality items that belong in the financial picture, not buried in a footnote

**Revenue growth rate is very likely mis-scaled.** The registry's "Revenue Growth YoY %" field reads 4.5% (prior 4%). A separate same-day record (`aibq_company_comparisons`, also dated 2026-08-11) states **"ARR Growth YoY %": 400** for ElevenLabs — two orders of magnitude apart. ARR's own history (≈$100M in Aug 2024, verified, to $330M in 2026) is far more consistent with a triple-digit growth rate than with 4.5%. Both figures are reported here; neither is silently corrected.

**Headcount: canonical figure sits below third-party estimates dated earlier.** The canonical registry shows 300 employees as of Aug 2026 (up from 200 prior). Independent workforce-data provider Revelio Labs (LinkedIn-derived) reports **616 employees in December 2025** and **753 in March 2026** — both dated well before the "current" 300 figure, and both substantially higher. A third figure, 580 employees, appears in a May 2026 getlatka.com piece. A same-or-later-dated canonical figure showing *fewer* employees than earlier third-party counts is not explained anywhere in the source material.

### ARR ladder — every dated figure found (not just the canonical line)

| Date | ARR reported | Source / tier |
|---|---|---|
| 2024-08-01 | $100M | Verified — crosses $100M ARR, 1M+ API developers |
| 2025-01-31 | ~$100M | Verified (Series C event text) |
| 2025-12-31 | $350M | eu.36kr.com, unverified |
| 2025-12-31 | $330M | Forbes (Josipa Majic), unverified — **same day, different outlet, different number than the line above** |
| 2026-02-01 | $330M | CRV "best generative AI companies" list, unverified |
| Apr–May 2026 (cluster) | **$500M** | ~10 convergent unverified outlets (Pulse2, TechCrunch, CNBC interview, MSN, The AI Insider, CXO Digital Pulse, NewsBytes, Google News harvester rows) |
| 2026-05-05 | $450M | TechCrunch, attributed directly to CEO Staniszewski ("ARR ending Q1 2026 at approximately $450M") — a **third** distinct figure the same week |
| 2026-08-11 (canonical) | **$330M** | PitchBook-linked registry |

The $330M-vs-$500M gap is the single largest open conflict in this profile — see section (i).

---

## (d) Valuation & funding history

### Confirmed primary rounds

| Round | Date | Amount | Lead | Post-money | Verified |
|---|---|---|---|---|---|
| Pre-seed | 2023-01-24 | $2M | Credo Ventures, Concept Ventures | not stated | Yes |
| Seed | 2023-06-20 | $19M | a16z (Systrom & Krieger also invested) | $99M | Yes |
| Series B | 2024-01-22 | $80M | a16z, Sequoia | $1.1B *(first unicorn mark)* | Yes |
| Series C | 2025-01-31 | $250M | ICONIQ Growth | $3.3B *(ARR ~$100M at time of round)* | Yes |
| Series D | Reported Jan–Feb 2026 (Feb 4–5 per Tracxn); registry reflects it from the 2026-03-25 tracker refresh | $500M | Sequoia Capital (a16z ~4x'd its stake, ICONIQ ~tripled) | $11B *(more than tripled Series C)* | No — but ~15 independent unverified outlets converge on the same figures |

Two low-authority outlets (techbriefly.com, dataconomy.com) mislabel the Series D round "Series C" — almost certainly confusing it with the actual January 2025 Series C. The Series D announcement was bundled with the ElevenMusic and Music Marketplace product launches.

### Secondary / tender activity

| Date | Type | Detail |
|---|---|---|
| 2025-09-01 | Employee tender offer | Implied valuation $6.6B; staff with 1+ year tenure could sell shares |
| 2026-05-05/06 | Tender offer (closed) | $100M; described as the company's "second such transaction in roughly six months" — implying an unlisted ~$100M tender around Nov 2025 |
| 2026-07-02 | Tender offer talks (**not closed**) | Implied valuation $22B; early-stage employee-stock-sale discussions per Bloomberg/TechStartups. Per house methodology, unclosed financings never anchor a base case — this is a forward signal only |

### Valuation ladder

| Date | Valuation | Basis |
|---|---|---|
| 2023-06-20 | $99M | Seed post-money |
| 2024-01-22 | $1.1B | Series B post-money |
| 2025-01-31 | $3.3B | Series C post-money |
| 2025-09-01 | $6.6B | Employee tender offer |
| ~Feb 2026 | $11B | Series D post-money |
| 2026-07-30 | $13B *(one day only)* | Tracker anomaly — reverted to $11B the next day; no narrative event corroborates it |
| From 2026-07-02 | $22B *(talks, unclosed)* | Tender-offer discussions — see conflicts |

Capital-raised figures wobble similarly across the daily tracker: $851M (2026-03-25) → $781M (2026-04-25, a downward revision) → $850M (2026-07-30, coincident with the one-day $13B blip). The canonical current figure is $850M.

---

## (e) Cap table & investors

No structured cap table is present in source data (no ownership percentages, share classes, or option-pool detail). The investor list below is compiled from funding-round and investor-rights text fields, not a formal cap table.

**Named investors:** Sequoia Capital (Series D lead; earlier Series B co-lead) · Andreessen Horowitz/a16z (Seed lead; Series B co-lead; ~4x'd its Series D stake) · ICONIQ Capital/ICONIQ Growth (Series C lead; ~tripled its stake at Series D; board seat + lead investor rights) · Credo Ventures, Concept Ventures (pre-seed) · Kevin Systrom & Mike Krieger, Instagram co-founders (seed angels) · BlackRock, NVIDIA, Wellington (reported ~May 2026) · Jamie Foxx, Eva Longoria (celebrity investors, ~May 2026) · Robinhood Ventures Fund I (April 2026) · Poland/PFR ($11M, June 2026, tied to "AI Lab Poland") · Activate (April 2026, described as its "first global growth-stage AI bet").

**Investor rights (verbatim):** "ICONIQ Growth: board seat and lead investor rights. a16z: Series B board representation. Standard preferred liquidation preference. No strategic lock-up disclosed."

**Board:** Only Mati Staniszewski appears in the structured Board Composition field — not a full roster.

---

## (f) Litigation & IP

No structured litigation/IP tracker data exists; everything below comes from Legal/Regulatory-category dated events (5 found, none independently Verified).

| Date | Item | Detail |
|---|---|---|
| 2024-04-16 | Senator Hassan (Joint Economic Committee) inquiry | Formal letter to ElevenLabs + 3 other AI voice companies following FBI reports of $893M in AI-voice-related scam losses |
| 2025 (year only) | *Vacker v. ElevenLabs* settled | Unauthorized AI voice-cloning case; cited as an example of emerging voice-IP/consent exposure |
| 2026-04-16 | Senator Hassan repeats inquiry | Same $893M FBI figure; letters now also sent to LOVO, Speechify, VEED. Dated almost exactly one year after the item above — plausibly re-coverage or an annual follow-up rather than confirmed as a wholly separate inquiry |
| 2026-05-01 | "ElevenLabs announces application filing" | Source text itself is incomplete ("has applied for something — specific details not provided in the excerpt"); too thin to characterize further |
| 2026-05-12 | Class-action lawsuit (Illinois federal court) | Journalists and voice actors vs. ElevenLabs, Google, Meta, Microsoft, Nvidia — alleges unauthorized use of plaintiffs' voices to train AI models |

---

## (g) Active forecasts

**Not present.** `shared_forecasts` is empty for ElevenLabs in this bundle — no dated analyst forecast rows to report.

---

## (h) Notable events

**146 dated events** were found in the full timeline (from 1,393 raw rows seen before date-filtering). 9 of the 146 carry a Verified=Yes tag (the "seed" verified public-record subset); the remaining 137 are harvested/unverified. Only 3 of 146 rows don't literally mention "ElevenLabs" in title+description, and manual review confirms all three are still genuinely about the company (headcount-tracker rows and one model-name-only title) — **no systemic name-collision contamination was found for ElevenLabs**, unlike OpenEvidence (see that profile). The complete 146-row log ships in `elevenlabs.json` → `full_event_log`.

Curated top 28, chronological:

1. **2022-01-01** — Founded by Mati Staniszewski and Piotr Dąbkowski *(Verified)*
2. **2023-01-24** — $2M pre-seed (Credo Ventures, Concept Ventures) *(Verified)*
3. **2023-01-24** — Public beta launches; goes viral, 7M+ users in first months *(Verified)*
4. **2023-06-20** — $19M seed led by a16z; Instagram co-founders Systrom & Krieger invest *(Verified)*
5. **2023-09-01** — Commercial API launched for enterprise voice synthesis *(Verified)*
6. **2024-01-22** — $80M Series B (a16z/Sequoia) at $1.1B — first unicorn mark *(Verified)*
7. **2024-03-01** — AI dubbing studio launches, 29 languages *(Verified)*
8. **2024-04-16** — Senator Hassan sends first formal voice-scam inquiry
9. **2024-08-01** — Crosses $100M ARR; 1M+ API developers *(Verified)*
10. **2025 (dated 2025-01-01 in log)** — *Vacker v. ElevenLabs* settled
11. **2025-01-31** — $250M Series C (ICONIQ Growth) at $3.3B *(Verified)*
12. **2025-09-01** — Employee tender offer values the company at $6.6B
13. **2025-12-01** — Headcount reported at 616 (Revelio Labs)
14. **2025-12-31** — ARR reported crossing $330M for full-year 2025 (Forbes)
15. **~Feb 2026** — $500M Series D (Sequoia) at $11B; ElevenMusic + Music Marketplace launch
16. **2026-03-14** — Eleven v3 text-to-speech model reaches general availability
17. **2026-04-16** — Senator Hassan repeats the inquiry, now including LOVO, Speechify, VEED
18. **2026-05-05** — $100M tender offer closed (2nd in ~6 months); BlackRock/NVIDIA/Jamie Foxx/Eva Longoria join as investors; enterprise contracts signed with Deutsche Telekom, Revolut, Klarna
19. **2026-05-05** — Press reports ARR "hits $500M" alongside the Series D announcement *(conflicts with canonical $330M — see section i)*
20. **2026-05-01** — Madrid office opens
21. **2026-05-12** — Class-action lawsuit filed over unauthorized voice-training data use (with Google, Meta, Microsoft, Nvidia as co-defendants)
22. **2026-05-21** — Licenses 200K human-narrated audiobooks; powers Spotify's self-publishing audiobook tool
23. **2026-05-27** — Licenses Stan Lee's voice and likeness for commercial AI use
24. **2026-06-11** — UK Government + AI Safety Institute accessibility partnership formalized (see Overview)
25. **2026-06-17** — Poland invests $11M, ties to "AI Lab Poland"
26. **2026-07-02** — Early talks for a $22B tender offer (unclosed)
27. **2026-07-07** — Canada business launches; Toronto office opens
28. **2026-07-28** — DXC Technology strategic partnership announced

---

## (i) Open conflicts & disputes

1. **ARR: $330M canonical vs. ~$500M press cluster.** The registry's standing figure is $330M (as of 2026-08-11). A dense cluster of ~10 unverified articles dated late April–early May 2026 all report ElevenLabs "surpassing $500M ARR" the same week as the BlackRock/NVIDIA/Jamie Foxx news; a third figure ($450M, attributed to the CEO directly) also appears the same week. None carries a Verified tag. Unresolved.
2. **Valuation: $11B registry vs. $22B tender-offer signal.** The source system's own company-dossier notes state this explicitly: *"Signal feed carries a $22B tender-offer report vs $11B registry — unreconciled."* The $22B figure traces to July 2026 reporting of early-stage, unclosed secondary-sale talks.
3. **Likely date-extraction error on a second $22B mention.** One funding-category record describes "planning a share sale in September at a USD 22 billion valuation" but is timestamped **2024-09-01** — two years before the $22B narrative appears anywhere else (July 2026) and missing the "Year" field most other records carry. Far more plausibly September 2026; reported as-is rather than silently corrected.
4. **One-day valuation/capital-raised anomaly.** The daily tracker shows Valuation jumping to $13B and Capital Raised to $850M on 2026-07-30 only, reverting to $11B on 2026-07-31 (capital raised stayed at $850M). No narrative event corroborates a $13B mark that day.
5. **Series naming inconsistency.** Two low-authority outlets label the Feb-2026 $500M/$11B round "Series C" — the label already used for the real January 2025 round.
6. **Headcount: canonical 300 vs. third-party 580–753** (see Financials).
7. **Revenue Growth YoY %: 4.5% vs. 400%** (see Financials).
8. **Currency framing (not a real conflict).** One source frames the Series D valuation as "£8.7bn" — roughly consistent with $11B at plausible GBP/USD rates; noted for completeness, not treated as substantive.

---

## (j) Sources

- **146** dated timeline events drawing on **121 unique source URLs** across **84 unique domains** (from 1,393 raw rows seen before date-filtering)
- **9** Verified=Yes / **137** unverified-harvested dated events
- `canon_source_authority` registry: elevenlabs.io rated Authority Score 9 / Tier 9 ("official tracked-company sources + major wire services"), last reviewed 2026-07-21
- 2 NEXUS Morning Digest citations in `shared_morning_digests_db` (2026-08-05 v10.6; 2026-06-11 v7.0), plus the full 2026-06-12.md digest text used for the UK/AISI narrative
- AIBQ score card (`extract/framework/companies/elevenlabs.md`)
- PitchBook-linked internal registry rows: legacy company row, v2 company registry, 115-day daily snapshot series (2026-03-23 to 2026-08-11), company-comparisons record, 4 unicorn-score records, 1 unicorn-intel record, 1 company-dossier record

Representative domains: elevenlabs.io, techcrunch.com, bloomberg.com, cnbc.com, forbes.com, en.wikipedia.org, law360.com, musicbusinessworldwide.com, tracxn.com, reveliolabs.com, and 74 others (full list in `elevenlabs.json` → `sources.domain_list`).
