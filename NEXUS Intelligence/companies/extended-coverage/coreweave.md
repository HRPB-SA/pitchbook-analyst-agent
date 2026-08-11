# CoreWeave — NEXUS Intelligence Profile

**Tier:** Extended Coverage (not Frontier Five) | **Sector:** AI Infrastructure (GPU cloud) | **PBID:** coreweave / 327267-64 | **HQ:** Livingston, NJ | **Ticker:** Nasdaq: CRWV
**Profile generated:** 2026-08-11 | **Companion data file:** `coreweave.json` (full 383-row event log, all structured tables)

> **Embargo confirmation.** This research system computes a cross-company quality-vs-valuation correlation
> coefficient. That figure is not stated, implied, charted, or fitted anywhere in this report. Nothing in the
> source bundle referenced it in connection with CoreWeave; no suppression was required beyond following the
> standing rule.

---

## (a) Overview

CoreWeave was founded in 2017 by Michael Intrator, Brian Venturo, and Brannin McBee, originally as a
cryptocurrency-mining operation (a Core Scientific spinout). It pivoted fully to GPU cloud infrastructure for
machine learning and rendering workloads in 2020, retaining its mining-era GPU inventory as the seed fleet.
NVIDIA became a strategic investor in 2022 ($50M, NVIDIA's first data-center cloud investment), and CoreWeave
built out anchor-customer relationships with Microsoft (2023), Cohere and Anthropic (2024), and a rapidly
expanding set of Meta and OpenAI commitments through 2025-2026. It IPO'd on Nasdaq as CRWV on 2025-03-28
(~$1.5B raised at $40/share) — the first major AI-infrastructure pure-play to go public — and now carries a
large, growing stack of equity, debt, and compute-linked financing (Magnetar Capital, BlackRock, Coatue, Jane
Street, MUFG) to fund data-center buildout. NEXUS/PitchBook coverage tags it "T2-AI Leaders" / "Tier 2 —
Challengers" in the AI-INFRA sector.

The single largest open question in this bundle is how stale the system's own internal valuation mark is
relative to CoreWeave's actual post-IPO trajectory. A $19.1B "Valuation" figure has been carried unchanged in
the daily internal tracker since 2026-03-27 (4.5+ months as of this profile's generation date), while a
separate score-tracker entry dated roughly seven weeks later (~2026-05-14) cites an enterprise value of
$67.4B — more than 3x higher — for a company that, in the intervening window, disclosed a $99.4B revenue
backlog, signed tens of billions of dollars in new hyperscaler commitments (Meta, Anthropic, Jane Street), and
drew a securities class-action lawsuit. Both figures are carried in this profile, unreconciled; see
**(i) Open conflicts**.

Business model in one line: CoreWeave rents specialized, latency-tuned GPU capacity to a small number of very
large AI customers (Microsoft, OpenAI, Meta, Anthropic) under multi-year, multi-billion-dollar contracts,
financed heavily with debt and compute-linked equity deals, at 60% customer concentration and roughly 72%
gross margin per the most recent stable internal read.

---

## (b) Current scores — AIBQ/PBQ composite

| | Composite | Confidence | MD | GO | CE | SV | RQ |
|---|---|---|---|---|---|---|---|
| **Current — 2026-05-14** | **5.18** | High | 5.5 | 6 | 3 | 6 | 5.5 |
| **Prior** | *none on record* | — | — | — | — | — | — |

- **Framework label conflict:** this score entry tags itself **"PBQ"**; the separate v2 company-registry row
  tags CoreWeave **"AIBQ"** for the same company. Both labels appear in source; not reconciled here.
- **"SV" is unexplained.** The fifth sub-dimension in this score entry is labeled "SV," not "CI" (Compute
  Independence), which is the fifth AIBQ dimension used everywhere else in NEXUS (RQ / CI / CE / MD / GO). No
  definition of "SV" was found anywhere in the bundle. Presented as-is rather than guessed.
- **No prior score exists in the bundle.** This 2026-05-14 entry is the *only* dated AIBQ/PBQ composite score
  for CoreWeave found anywhere in the data. The company-registry row's own "Score Changes" and "Latest Score
  Date" fields are both marked `<omitted />` in the source extraction — a deliberate redaction marker, not an
  empty value, meaning a score history likely exists upstream but was not included in this bundle.
- **Rationale (verbatim):** "PUBLIC COMPANY - NO LONGER UNICORN. IPO'd NASDAQ (CRWV) Mar 28 2025 at $18.6B.
  Rev $6.23B (TTM 1Q2026), GP $4.32B (69% GM), NI -$1.59B, EV $67.4B. Raised $31.1B total. Former name:
  Atlantic Crypto. OpenAI $22.4B contract per 10-K. Score retained for reference."
- Valuation rank: 127 (of the broader PitchBook/NEXUS universe this ranking draws from; scope of the ranking
  pool not specified in source).

---

## (c) Financials — ARR, growth, margin, headcount (all dated)

**Most recent internal snapshot (2026-08-11, effectively frozen since 2026-04-19):**

| Metric | Value | As of |
|---|---|---|
| ARR | $5.1B | 2026-08-11 (unchanged since 2026-04-04) |
| Headcount | 2,189 | 2026-03-25 onward (stable, consistent across all sources) |
| Gross margin | 72% | 2026-03-25 onward (stable) |
| Gross profit | $3.694B | 2026-08-11 |
| Cumulative losses | $1.2B | Static since 2026-03-27 |
| Burn rate | $200M/mo | Static |
| Customers | 50 (60% concentration) | Static |
| NRR | 200% | Static |
| Runway | 18 months | Static |
| Compute spend | $6.0B/yr | Fluctuates $5.0-7.0B/yr across the year, resting at $6.0B most days |

**A separate, later scoring entry (as-of ~2026-05-14) tells a materially different financial story:**
revenue $6.23B TTM (1Q2026), gross profit $4.32B (69% GM — vs. 72% in the frozen tracker), net income
**-$1.59B**, enterprise value **$67.4B**, total capital raised **$31.1B**.

**ARR ladder (dated, multiple sources — not fully reconciled):**

| Date | ARR / Revenue figure | Source |
|---|---|---|
| 2025-03-28 (IPO) | ~$1.9B TTM | v2_master_events IPO description |
| 2025-06-01 | ~$3B ARR | v2_master_events, **Verified** |
| 2025-01-01 *(bucketed date, likely imprecise)* | "$5B annual revenue," cited as fastest cloud platform in history to reach it | timeline; **note:** this date precedes the $1.9B/$3B figures above — flagged as a mis-bucketed date, not a real reversal |
| Q1 2026 (reported 2026-05-07) | $2.1B quarterly revenue, +112% YoY | shared_ipo_pipeline note citing a May 8 digest |
| ~2026-05-14 | $6.23B TTM revenue | aibq_unicorn_scores rationale |
| 2026-08-11 (tracker, static since 04-19) | $5.1B ARR | aibq_company_snapshots |

**Growth-rate figures in tension** (all found in the same bundle, none reconciled):

- **2%** — "Revenue Growth YoY %" field, identical and unchanged across every single daily snapshot, the v2
  registry, and the legacy company row. This is very likely a data/units error: it is flatly contradicted by
  every narrative growth figure below.
- **110%** — "CoreWeave Reports 110% Revenue Growth Amid 2025 Losses" (2026-05-05)
- **112%** — Q1 2026 quarterly print, YoY
- **170%+** — legacy row's own trajectory narrative: "$16M (2022) → $229M (2023) → $1.9B (2024) → $5.1B TTM
  4Q2025 (SEC actual)... 170%+ YoY"

**Debt context** (never counted toward Capital Efficiency, which is equity-only per house methodology; carried
here as risk context): $2.3B (2023, Magnetar/BlackRock) → $8.5B GPU-backed, A3-rated facility with MUFG
(closed 2026-03-30) → $3.5B convertible senior notes (2026-04-13, $5.75B combined with senior notes) → $3.1B
HPC/chip-backed loan (multi-stage process, 2026-04-30 through close on 2026-07-11, ~$19B in investor demand
reported) → $2.6B leveraged loan earmarked for Anthropic capacity expansion (2026-07-29). A 2026-04-29 entry
puts cumulative high-interest debt at **$40B+**.

---

## (d) Valuation & funding history

| Date | Event | Amount | Post-money valuation | Investors | Verified |
|---|---|---|---|---|---|
| 2022-04-04 | Strategic investment | $50M | — | NVIDIA | Yes |
| 2023-04-19 | Series A | $221M | $2.1B | Magnetar Capital (lead) | Yes |
| 2023-08-01 | Debt financing | $2.3B | — | Magnetar Capital, BlackRock | Yes |
| 2024-05-29 | Series C | $1.1B | $19B | Coatue, Magnetar Capital | Yes |
| 2025-03-28 | **IPO (Nasdaq: CRWV)** | $1.5B | **$18.6B** *(score-tracker)* **or ~$23B** *(verified event description)* — both carried, unresolved | Public markets, $40/share | Yes (core fact); valuation figure disputed |
| 2025-06-01 | Equity alongside compute deal | $1.0B | — | Jane Street | No |
| 2026-03-27 → 2026-08-11 | **Standing internal valuation mark** (held constant) | — | **$19.1B** | — | No — flagged stale |
| 2026-03-30 | GPU-backed financing facility (debt, A3-rated) | $8.5B | — | MUFG Bank (arranger) | No |
| 2026-04-13 | Convertible senior notes | $3.5B | — | — | No |
| 2026-04-15 | Equity investment | $1.0B | — | Jane Street, at $109/share | No |
| 2026-04-21 | Combined offering | $6.7B | — | Combined with Google-backed data-center financing | No |
| 2026-04-30 → 2026-07-11 | HPC/chip-backed leveraged loan (multi-stage) | $3.1B | — | ~$19B investor demand reported | No |
| 2026-07-29 | Leveraged loan (Anthropic capacity) | $2.6B | — | — | No |
| ~2026-05-14 (as-of) | *(not a funding event — enterprise value, for continuity)* | — | **$67.4B EV** | — | No |

**Total capital raised — three figures in tension, none reconciled in source:**

| Figure | As of | Note |
|---|---|---|
| $1.0B | 2026-04-17 onward (tracker) / 2026-08-11 (comparisons table) | Matches the size of a single recent round — likely a basis error where the cumulative field got overwritten with the latest round's amount |
| $25.264B | 2026-03-25 (tracker) / legacy row "Prev" | — |
| $31.1B | ~2026-05-14 (score rationale: "Raised $31.1B total") | Likely blends equity and debt financing |

---

## (e) Cap table & investors

Only **one** structured cap-table row exists in the bundle:

| Investor | Type | Round | Amount | Date | Special rights |
|---|---|---|---|---|---|
| Jane Street | Financial VC | Equity alongside $6B compute agreement | $1.0B | 2025-06-01 | $6B cloud compute agreement tied to the equity investment |

The fuller investor picture is reconstructed narratively from verified funding events and the legacy company
row (not from a structured cap table, so treat as directional):

- **NVIDIA** — strategic investor since 2022-04-04 ($50M); board **observer** seat per the legacy row.
- **Magnetar Capital** — Series A lead (2023), debt co-lender (2023), Series C co-investor (2024).
- **BlackRock** — debt co-lender (2023, $2.3B facility).
- **Coatue** — Series C lead (2024, $1.1B).
- **Jane Street** — equity investor June 2025 ($1B) and April 2026 (additional $1B at $109/share), both tied
  to compute agreements.

**Board composition (per legacy row):** Michael Intrator (CEO), NVIDIA (observer), Coatue.

---

## (f) Litigation & IP

The structured litigation tables (`shared_litigation`, `v2_litigation_ip`) are **empty** in the bundle. One
item surfaces through the event timeline:

- **2026-03-05** — Pomerantz Law Firm files a securities class-action lawsuit against CoreWeave, Inc.
  (appears as 4 near-identical harvested rows). **No case number, specific allegations, or resolution status
  found anywhere in the bundle.** Status: open/unknown.

The legacy company row's "IP Activity" field is blank. Adjacent but not litigation: CoreWeave began pursuing
FedRAMP authorization for U.S. government AI-cloud services in October 2025 (regulatory posture, not a legal
dispute).

---

## (g) Active forecasts

The structured forecast table (`shared_forecasts`) is **empty** in the bundle. The items below are
forward-dated entries found in the event timeline itself, not a formal forecast object:

| Target date | Forward-looking item | Financial impact cited |
|---|---|---|
| 2026-12-31 | Increases 2026 ARR target and capex forecast | $18.5B |
| 2026-12-31 | Two-thirds of ARR projected from Microsoft, OpenAI, and Meta by end-2026 (stated as a forward concentration-risk projection) | — |
| 2026-12-31 | Software, CPU, and networking businesses expected to exceed $100M ARR by end of year | $100M |
| 2027-12-31 | Revenue projected to reach $25B by end of 2027 | $25B |
| 2027-12-31 | 3.1GW of compute capacity coming online by end of 2027 | $20B |
| 2030-12-31 | Scottish data-centre completion — source title itself says "under investigation" (unclear whether this refers to a regulatory review or flags a data-quality issue with the entry) | — |

---

## (h) Notable events

**383 dated events found** in the raw timeline (4,080 total rows scanned before date-filtering; the
extraction's own `pagination_complete` flag is **null** — neither confirmed complete nor incomplete). Of the
383, only **20 carry an independent "Verified" tag** (Seed — Verified Public tier); the remaining **363** are
harvester-extracted from press/analyst sources and unverified. The raw log is heavily duplicated — the same
story is frequently harvested from multiple outlets on the same or adjacent dates (e.g., the April 2026 Meta
$21B deal and the March 2026 $8.5B financing close each appear 4-8 times with near-identical wording).

The curated list below (36 items — within the requested ~25-35 range) collapses those duplicates to one
representative line each, prioritizes Verified/Critical items, and spans the full 2017-2026 range across
funding, partnership, product, legal, and competitive categories. **The complete, unfiltered 383-row log is
in `coreweave.json` → `full_event_log`; nothing was deleted.**

| Date | Event | Verified |
|---|---|---|
| 2017-01-01 | Founded by Michael Intrator, Brian Venturo, Brannin McBee (crypto-mining origin, Core Scientific spinout) | Yes |
| 2020-01-01 | Pivots fully from crypto mining to GPU cloud infrastructure | Yes |
| 2022-04-04 | Raises $50M — NVIDIA's first data-center cloud investment | Yes |
| 2023-04-19 | Raises $221M Series A led by Magnetar Capital, $2.1B valuation | Yes |
| 2023-08-01 | Raises $2.3B debt financing (Magnetar Capital, BlackRock) | Yes |
| 2023-11-01 | Microsoft signs $2.9B multi-year compute agreement | Yes |
| 2024-01-01 | Signs landmark Cohere deal for enterprise AI inference at scale | Yes |
| 2024-04-10 | Announces multi-year AI cloud deal with Anthropic | No |
| 2024-05-29 | Raises $1.1B Series C led by Coatue/Magnetar, $19B valuation | Yes |
| 2024-12-18 | Joins DOE's "Genesis Mission" AI research initiative | No |
| 2025-03-28 | **IPOs on Nasdaq (CRWV)**, $40/share, ~$1.5B raised (valuation figure disputed — see (d)) | Yes |
| 2025-04-09 | Announces $21B AI cloud infrastructure deal with Meta (later expanded) | No |
| 2025-06-01 | Jane Street invests $1B in equity alongside a $6B compute agreement | No |
| 2025-06-01 | ARR reaches ~$3B; Microsoft/OpenAI anchor customers | Yes |
| 2025-09-01 | Meta signs a separate $14.2B AI-capacity deal through 2031 | No |
| 2025-10-01 | Launches CoreWeave Federal business unit; pursues FedRAMP authorization | No |
| 2025-12-31 | Revenue backlog reaches $66.8B | No |
| 2026-03-05 | Pomerantz Law Firm files securities class-action lawsuit | No |
| 2026-03-16 | Tops the MLPerf v6.0 inference benchmark | No |
| 2026-03-30 | Closes $8.5B investment-grade (A3), GPU-backed financing facility with MUFG | No |
| 2026-04-03 | Ends Poolside AI Texas partnership (financial-impact figure disputed between two duplicate rows: $14B vs. $4B) | No |
| 2026-04-09 | Expands Meta deal to $21B through 2032 | No |
| 2026-04-13 | Raises $3.5B in convertible senior notes | No |
| 2026-04-15 | Jane Street invests an additional $1B at $109/share, boosts stake with $6B compute deal | No |
| 2026-04-20 | Meta commits $48B in combined spending across CoreWeave and Nebius (two-provider figure) | No |
| 2026-04-22 | Launches CoreWeave Interconnect with Google Cloud | No |
| 2026-04-29 | Debt load disclosed at $40B+; OpenAI's missed internal revenue projections send CRWV down 6% | No |
| 2026-05-05 | Reports 110% revenue growth amid 2025 losses; secures $3.1B chip-backed loan (~$19B demand) | No |
| 2026-05-13 | Jensen Huang's foundation buys $108.3M of CoreWeave compute, donates to researchers | No |
| 2026-05-19 | Google and Blackstone announce $5B competing cloud-infrastructure investment aimed at CoreWeave | No |
| 2026-06-18 | Adds $32B to AI backlog | No |
| 2026-06-22 | Joins the Nasdaq-100 Index | No |
| 2026-07-01 | Meta discloses its own "Meta Compute" plans; SoftBank launches competing "SB Neo AI Cloud" | No |
| 2026-07-09 | Named a Visionary in the 2026 Gartner Magic Quadrant for Cloud AI Infrastructure | No |
| 2026-07-29 | Raises $2.6B leveraged loan to expand Anthropic compute capacity | No |
| 2026-08-15 *(scheduled)* | Q2 2026 earnings — next data-refresh point | — |

**Consolidated governance note** (not itemized individually above): recurring insider stock sales through 2026
by CEO Michael Intrator ($7.2M on 03-25, $23.284M/200K shares on 04-21, $32.87M on 06-23, largely via 10b5-1
plans) and CDO Brannin McBee (07-20), alongside 2025 executive compensation packages cited at $64.5M. Full
detail in `full_event_log`.

---

## (i) Open conflicts / disputes

1. **IPO valuation:** $18.6B post-money (score-tracker rationale, matches legacy row's "Prev Valuation") vs.
   ~$23B market cap (verified master-event description) for the *same* 2025-03-28 listing. Both carried.
2. **Standing valuation vs. enterprise value:** $19.1B (frozen since 2026-03-27) vs. $67.4B EV (~2026-05-14) —
   more than 3x apart.
3. **IPO pipeline status stale:** `shared_ipo_pipeline` still shows Filing Status "Pre-Filing" as of its own
   last-updated date of 2026-05-12 — over a year after the confirmed IPO. The bundle's own canon dossier
   explicitly flags this exact internal conflict.
4. **Total capital raised:** three figures, three vintages — $1.0B / $25.264B / $31.1B (see (d)).
5. **Revenue growth YoY:** a "2%" field recurs identically everywhere it appears, flatly contradicted by
   110% / 112% / 170%+ figures elsewhere in the same bundle.
6. **Gross margin:** 72% (registry/snapshot/legacy) vs. 69% (score rationale, TTM 1Q2026).
7. The 2026-08-15 scheduled earnings entry is labeled "First Full Quarter Public" — inconsistent with a
   March 2025 IPO (would be roughly the sixth-plus full quarter as a public company).
8. **Poolside AI Texas exit:** two duplicate rows for the same event carry different financial-impact
   figures — $14B in one, $4B in the other.
9. **Framework label:** the registry tags CoreWeave "AIBQ"; its own score entry tags itself "PBQ."
10. The fifth score sub-dimension is labeled "SV" with no definition found anywhere in the bundle (elsewhere
    in NEXUS the five AIBQ dimensions are RQ/CI/CE/MD/GO).
11. A 2024-06-22 entry has CoreWeave "joining Nasdaq-100" — nine months before its actual IPO and impossible
    as literally dated; almost certainly a duplicate/date error of the properly-corroborated 2026-06-22 event.
12. Numerous events are bucket-dated to YYYY-01-01/YYYY-MM-01 when the exact date was evidently unknown,
    occasionally producing apparent chronological inversions (see the "$5B revenue" ARR-ladder entry in (c)).
13. **Timeline completeness is unconfirmed:** `pagination_complete` is `null` against 4,080 rows seen and 383
    kept as dated.

---

## (j) Sources count

| Metric | Count |
|---|---|
| Total dated timeline events | 383 |
| — independently Verified | 20 |
| — unverified (harvested) | 363 |
| Distinct source URLs cited in the timeline | 247 |
| Distinct outlet domains in the timeline | 89 |
| Populated structured tables in the bundle | 14 |
| Total records across all populated tables | 520 |
| Source-authority score, coreweave.com | 9/9 — "Official Company," Tier 9, last reviewed 2026-07-21 |

**Extra checks performed per task instructions:**
- **Hyperscaler Capex Tracker** (`extract/shared/hyperscaler-capex.json`) checked for rows where Company
  contains "CoreWeave": **zero matches** out of 10 rows total (all 10 are Amazon/AWS, Microsoft/Azure,
  Google/GCP, or Meta), even though "CoreWeave" is a valid option in the underlying schema. Reported as an
  empty result, not skipped.
- `extract/framework/companies/` checked for a CoreWeave AI-Ecosystem score page: none exists (only Cursor and
  a handful of other companies have one); consistent with CoreWeave's score data living entirely inside its
  own bundle.

Representative outlet mix in the timeline: coreweave.com / investors.coreweave.com (primary), Reuters,
Bloomberg, CNBC, Forbes, Business Insider, PR Newswire, GlobeNewswire, SEC.gov, Fitch Ratings, HPCWire,
Data Center Dynamics, Tom's Hardware, Seeking Alpha, MarketBeat, and a long tail of smaller finance/crypto
trade sites (full list in `coreweave.json` → `sources.domain_list`).
