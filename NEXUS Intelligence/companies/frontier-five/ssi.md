# Safe Superintelligence (SSI) — NEXUS Intelligence Profile

Slug: `ssi` | Tier: Frontier Five | PBID: 606742-48 | HQ: Palo Alto, CA
Staged: 2026-08-11 | Source bundle: `bundles/ssi.json` (sha256 `e99d197f87545952...`)

> This profile is built entirely from the pre-consolidated NEXUS bundle and its
> linked source-page extracts. Several data-quality issues were found in the
> underlying tables during staging (contaminated commercial-metrics fields, a
> majority-noise event timeline, and internally-inconsistent score rows); all
> are disclosed in **(i) Open conflicts/disputes** and preserved, flagged, in
> the companion `ssi.json`. Nothing was dropped silently and nothing was
> invented to fill a gap.

---

## (a) Overview

Safe Superintelligence Inc. (SSI) is a stealth AI research lab founded June
19, 2024 in Palo Alto, California by Ilya Sutskever, OpenAI's former Chief
Scientist and a co-author of OpenAI's 2023 superintelligence-governance
recommendations. SSI's stated mandate is singular: build safe
superintelligence directly, without shipping intermediate commercial
products along the way — reported in mid-2026 as a "Straight Shot" strategy.
As of the most recent extraction the lab has published no models and has
zero commercial products in market.

SSI has raised approximately $3 billion in disclosed capital since founding
and carries a reported $32 billion valuation (reached April 2026, unchanged
through the most recent August 2026 tracker update). Its capital base is
backed by Greenoaks Capital as lead investor, with NVIDIA and Alphabet
(Google) holding strategic observer rights; a further NVIDIA commitment of
roughly $5 billion, tied to Vera Rubin GPU access, was reported and
formalized as a long-term strategic partnership between May and July 2026
(see (d) and (i) — this amount is not yet reflected in SSI's canonical
total-raised figure).

On PitchBook's AIBQ framework, SSI carries the lowest composite score among
the tracked Frontier Five (Anthropic, OpenAI, Databricks, xAI, SSI). Per the
framework's own scoring rationale, this reflects SSI's pre-revenue,
pre-product stage — not a judgment on team or technology quality. Governance
is SSI's comparatively strongest scored dimension for a company at this
stage; capital efficiency and revenue quality sit at the framework floor
because there is, by design, no revenue yet.

In April 2026, Meta reportedly offered approximately $30 billion to acquire
SSI outright; Sutskever refused. Daniel Gross, SSI's other named co-founder,
has since departed (departure date is disputed between two sources — see
(i)), leaving Sutskever as sole remaining co-founder and CEO.

---

## (b) Current scores — AIBQ composite and sub-scores

| Field | Value |
|---|---|
| Composite (pre-CRA) | **2.30** — "Distressed" tier |
| CRA (Composite Risk Adjustment) | **-1.50** (four dimensions ≤ 3.0 — CE, RQ, CI, MD — trigger the maximum penalty) |
| Composite (post-CRA) | **0.80** |
| Score date | 2026-05-27 (command_center_master_profiles "Last Updated"); independently cited as already 2.30 on 2026-04-19 (legacy row); reconfirmed unchanged in every daily tracker digest through **2026-08-10**, the latest in the bundle |
| Prior score | Flat at 2.30 for the entire observed window (at least 2026-04-19 through 2026-08-10). One unexplained single-day reading of 3.65 appears on 2026-05-13, bracketed by 2.30 readings the day before and every day after — treated as a transient scoring-run artifact, not a real move (it also fails to reconcile arithmetically against its own component scores; see (i) DQ-3) |
| Confidence | Categorical: **High** (canonical score row; framework deep-dive Data Confidence Map marks ARR/Valuation/Total Raised/Status/Founder all "Confirmed"). Numeric: the daily snapshot ladder's continuous confidence metric is noisier, ranging roughly 0.32–0.85 across 115 daily readings (mean ≈ 0.55–0.60; most recent readings 0.57–0.60) |
| Staleness flags | Tracker fired an SSI-specific staleness flag twice: 2026-06-15 ("SSI staleness flag fires (30d)") and 2026-07-09 ("Databricks + SSI dimension grids >7 days unrefreshed") |

**Sub-scores** (weights: RQ 25%, CE/GO/MD 20% each, CI 15% — this weighting
reproduces the 2.30 composite exactly):

| Dimension | Score | Sub-scores |
|---|---|---|
| CE — Capital Efficiency | 1.0 | CE-1 1.0 · CE-2 1.0 · CE-3 1.0 · CE-4 1.0 (all flagged — pre-revenue floor) |
| RQ — Revenue Quality | 1.0 | RQ-1 1.0 · RQ-2 1.0 · RQ-3 1.0 · RQ-4 1.0 · RQ-5 1.0 (all flagged — no customers) |
| CI — Cost & Infrastructure | 3.0 | CI-1 4.0 · CI-2 2.0 · CI-3 2.0 · CI-4 3.0 · CI-5 4.0 (all flagged — limited compute access relative to the 7.0 pass line) |
| GO — Governance | 5.0 | GO-1 6.0 · GO-2 6.0 · GO-3 2.0 (flagged — no IPO preparation) · GO-4 6.0 · GO-5 5.0 — SSI's strongest dimension |
| MD — Moat Durability | 2.0 | MD-1 2.0 · MD-2 1.0 · MD-3 4.0 · MD-4 1.0 · MD-5 2.0 (all flagged — no shipped product means no moat yet) |

Per the framework's own sub-score analysis: "SSI is not a bad business — it
is a pre-business. Low scores reflect pre-revenue status, not quality
judgment." The trigger identified for score improvement across CE, RQ, and
MD simultaneously is a first product/API launch, which as of extraction had
not occurred (see (h)).

*A note on source consistency:* two independent AIBQ deep-dive source pages
disagree slightly (0.80 vs. 0.82 post-CRA, GO 5.0 vs. 5.1) — both values are
preserved; see (i) DQ-5. `command_center_master_profiles`'s own CRA field
separately reads 0 rather than -1.50 for the same dated snapshot — treated
as an unpopulated field, not a real disagreement; see (i) DQ-4. One 2026-07-02
tracker note references an embargoed cross-company coefficient in passing
(unrelated to SSI's own score); per this project's standing embargo, no
value, sign, or cohort-wide characterization is reproduced here — see (i)
DQ-11.

---

## (c) Financials

**SSI is pre-revenue.** ARR is $0. There are no shipped commercial products
and no customers. This is stated identically and independently across every
narrative source in the bundle: the command-center current snapshot ("ARR:
$0 (Pre-revenue) — Confirmed"), both AIBQ deep-dive extracts, the
canonical `aibq_unicorn_scores` row ("$0 revenue, $3B raised. Pure research
lab."), and even the master-profile row's own free-text field ("$0 revenue.
Pure research organization. No products shipped.").

No structured financial-model tables are populated for SSI — financial
model inputs, cost architecture, and revenue decomposition are all empty in
this bundle, consistent with a company that has nothing yet to model.

A single lower-confidence source (the master-profile row, Data Confidence
0.6) offers rough operating estimates, not corroborated elsewhere: burn rate
approximately **$50 million/month** (up from a prior estimate of $30
million/month), compute spend approximately **$1 billion/year** (up from a
prior $500 million/year), headcount approximately **20**, and runway
approximately **48 months**. These are directionally consistent with a
capital-intensive, pre-revenue research lab and are not contradicted
elsewhere in the bundle, but they should be read as single-source estimates,
not confirmed figures.

**Flag:** that same master-profile row and the 115-day daily snapshot ladder
derived from it also carry a cluster of fields that flatly contradict the
pre-revenue status above — ARR $499 million (and, in an earlier stretch of
the ladder, $0.6 million), a shipped product called "Zuma," customers "Ramp"
and "Zapier," a "Microsoft Foundry" developer-ecosystem tag, 78% gross
margin, 102% YoY revenue growth, and an IPO signal claiming Goldman Sachs
and JPMorgan were hired as underwriters for a H2 2026 listing. None of this
is adopted. It contradicts the row's own other fields (its "Benchmark
Positions" text says "No published models. Full stealth since founding Jun
2024"; its own prior-period values for these same fields are $0/0%), it
contradicts four independent other sources in this bundle, and it is
almost certainly cross-company data contamination — full detail in (i)
DQ-1. Total capital raised (~$3B) and valuation ($32B) are unaffected by this
contamination and are corroborated across multiple independent sources; see
(d).

---

## (d) Valuation & funding history

| Date | Event | Amount | Post-money valuation | Notes |
|---|---|---|---|---|
| 2024-06-19 | Founded | — | — | Palo Alto, CA. Ilya Sutskever (ex-OpenAI Chief Scientist) with co-founder Daniel Gross. Corroborated by 5 near-duplicate source rows |
| 2024 (year only) | Seed round | ~$100M | — | Precise date not captured in source |
| 2024-09-04 | Early round / public unveiling | ~$1B | reported $4B–~$20B across contemporaneous accounts | Sources vary on the exact figure at this stage; Google (Alphabet) and NVIDIA reported as backers |
| 2025-02-17 | Funding round | — | $30B | |
| 2025-04-01 → 2025-06-15 | **Series B** (named) | $2B | — | Announced April 2025; completed/closed June 15, 2025 |
| 2026-03-15 | Additional raise | >$1B | $30B (reaffirmed) | |
| **2026-04-01** | — | **cumulative ~$3B raised** | **$32B** | Current canonical anchor — stable through the 2026-08-10/11 extraction |
| 2026-04-20 | Unconfirmed press reports | $2B "seed" round targeted (separately, a "$6B raise" headline same day) | — | **Not reflected** in the canonical $3B total in any later source; treated as unconfirmed per house methodology on unclosed/rumored financings |
| 2026-04-28 | Acquisition approach (not a funding event) | Meta reportedly offered ~$30B to acquire SSI outright | — | Refused by Sutskever |
| 2026-05-15 → 2026-07-31 | NVIDIA investment / Vera Rubin partnership | ~$5B (reported) | — | First reported 5/15; reiterated 7/1 (tied explicitly to Vera Rubin GPU access); formal long-term strategic partnership + platform access announced 7/27–28; financing announcement 7/31. Tracker flagged this as triggering "active capital review" (2026-07-29 digest). **Not reflected** in the canonical $3B total as of the 2026-08-10/11 extraction |

**Current canonical figures:** Total capital raised ≈ **$3 billion**; latest
valuation **$32 billion**; last *named* round is **Series B** ($2B, closed
June 2025) — one source field separately labels the same general period a
"Series C," which is unconfirmed elsewhere; see (i) DQ-8.

---

## (e) Cap table & investors

No structured cap-table records exist for SSI in this bundle
(`shared_cap_table` is empty). What follows is drawn entirely from a single
free-text field on the master-profile row and should be read as directional,
not exhaustive:

- **Lead investor:** Greenoaks Capital — board seat and lead investor rights
- **Strategic backers:** NVIDIA (strategic observer rights; the ~$5B 2026
  commitment above is reported but not yet reflected in canonical totals);
  Alphabet/Google (strategic observer rights, backing reported since
  September 2024)
- **Deal terms:** no commercial lock-up disclosed — SSI can reportedly
  remain a pure research organization indefinitely under its investor
  terms; no profit-cap structure disclosed (unlike some peers in the
  cohort)
- **Board:** Ilya Sutskever (CEO; sole remaining co-founder on the board
  per this data)
- **Departed co-founder:** Daniel Gross — departure date is disputed
  between two sources; see (i) DQ-6

---

## (f) Litigation & IP

No data captured for this section as of extraction. Both the litigation
table (`shared_litigation`) and the litigation/IP tracker
(`v2_litigation_ip`) are empty for SSI, and the master-profile row's IP
Activity field is blank. This reflects an absence of records in the
dataset, not a confirmed absence of litigation or IP activity.

---

## (g) Active forecasts

No structured forecast model is populated for SSI — `shared_forecasts`,
`canon_canonical_figures`, `shared_ai_financial_model`,
`shared_financial_model_inputs`, `shared_cost_architecture`, and
`shared_revenue_decomposition` are all empty for this company in the bundle.
There is no ARR, headcount, or valuation projection to report.

The only forward-looking items on record are qualitative:

1. **First model launch** — still at the "plan" stage as of the most recent
   extraction (2026-08-01 restatements), consistent with an original plan
   reported back in 2024-08-04. No model has shipped in the intervening two
   years.
2. **"Straight Shot" strategy** — reported May 2026: build directly toward
   safe superintelligence without an intermediate commercial product line.
3. **NVIDIA $5B financing** — announced/reiterated May–July 2026, pending
   confirmation in canonical capital-raised totals (see (d), (i) DQ-9).
4. SSI is named as a **supporting-analysis company** (not the primary
   subject) in one in-progress NEXUS flagship report, "The Price of the
   Frontier" (status: Data Collection, not yet published), which studies
   frontier-AI cost structure and compute independence across OpenAI,
   Anthropic, SSI, Mistral AI, Cohere, xAI, and Cursor.

---

## (h) Notable events

The underlying event timeline holds **117 raw rows**, and the source's own
pagination tracker reports this is a partial capture — 117 of 800
`total_rows_seen` upstream, `pagination_complete: false`. Of the 117 rows,
only **47 are genuinely about SSI** by title and description. **69 rows**
concern unrelated or confusingly similarly-named entities that appear to
have been swept in by loose keyword matching — most heavily "Recursive
Superintelligence" (a distinct, competing startup — 5 rows), Meta's internal
"Meta Superintelligence Labs" initiative (2 rows), and the unrelated public
micro-cap "Safe Pro Group" (3 rows), plus assorted unconnected market events
(Lambda, Ineffable Intelligence, Snap, Tencent, fusion power, a Google Pixel
launch, etc.). **1 row** is background context predating SSI's founding
(Sutskever's 2023 OpenAI-era superintelligence-governance paper). The full
117-row raw log — noise rows included, clearly flagged — is preserved
verbatim in the companion JSON so nothing is silently dropped; only the 47
SSI-relevant rows are curated below, grouped by underlying real-world event
and ranked by importance as tagged in the source.

- **2024-06-19 (Critical/High, corroborated by 5 source rows) — Founding.**
  SSI launches in Palo Alto, CA. Two of the five corroborating rows say
  "founded in UK," which contradicts Palo Alto HQ confirmed three other
  independent ways elsewhere in the bundle; treated as an error (see (i)
  DQ-7).
- **2024–2026-04 (High, multiple rows) — Funding trajectory to $32B.**
  Seed (~$100M) → ~$1B raised with early valuation estimates spanning
  $4B–~$20B across contemporaneous accounts → $30B valuation (Feb 2025) →
  named Series B, $2B, closed June 2025 → additional >$1B raised (March
  2026) → $32B valuation on ~$3B cumulative raised (April 2026, current
  canonical). Full tranche detail in (d).
- **2024-08-04 and 2026-08-01 (High, corroborated x3 in 2026) — First model
  plan.** SSI plans its first model release/launch; as of the most recent
  extraction this remains a plan, not a shipped product, roughly two years
  after it was first reported.
- **2026-04-20 (High, unconfirmed, 3 same-day rows) — Reported $2B "seed"
  target and separate "$6B raise" headline.** Neither figure is reflected
  in the canonical $3B total-raised figure in any later source; not
  adopted (see (i) DQ-9).
- **2026-04-28 (High, corroborated x2) — Meta acquisition approach.** Meta
  reportedly offered approximately $30 billion to acquire SSI outright;
  Ilya Sutskever refused.
- **2026-05-01 (High, corroborated x3) — "Straight Shot" strategy
  reported.** SSI is described as pursuing a direct path to safe
  superintelligence without shipping intermediate commercial products.
- **2025-07-01 or 2026-03-15 (High; date disputed, see (i) DQ-6) —
  Leadership transition.** Co-founder Daniel Gross departs; Ilya Sutskever
  becomes sole CEO and sole remaining co-founder. The underlying fact is
  well corroborated; only the date is in conflict between two sources,
  roughly eight months apart.
- **2026-05-15 → 2026-07-31 (Critical/High, 5 dated restatements) — NVIDIA
  relationship.** Initial $5B investment report (5/15) → reiterated
  commitment tied explicitly to Vera Rubin GPU access (7/1) → formal
  long-term strategic partnership with platform access announced (7/27–28)
  → financing announcement (7/31). The tracker's 2026-07-29 digest flags
  this as triggering "active capital review," and the 2026-07-30 digest
  names it a center-of-gravity item warranting "score-watch" — but SSI's
  composite remained unchanged at 2.30 through the most recent update, and
  the amount is not yet reflected in the canonical total-raised figure (see
  (d), (i) DQ-9).

---

## (i) Open conflicts / disputes

All items below are also logged as structured `data_quality_flags` entries
in the companion `ssi.json` (IDs referenced in brackets), with full source
quotations and arithmetic where relevant. Nothing here has been silently
resolved — where two sources disagree and neither clearly supersedes the
other, both values are presented.

1. **[DQ-1, high]** A cluster of commercial-metrics fields (ARR $499M/$0.6M,
   product "Zuma," customers "Ramp"/"Zapier," "Microsoft Foundry," 78% gross
   margin, 102% YoY growth, Goldman Sachs/JPMorgan IPO-underwriter signal)
   contradicts SSI's pre-revenue, pre-product, stealth status — corroborated
   by four independent other sources *and* by other fields in the very same
   row. Almost certainly cross-company data contamination. Not adopted.
2. **[DQ-1b, medium]** Burn rate, compute spend, headcount, and runway
   estimates are single-source (Data Confidence 0.6) and should be labeled
   as reported estimates, not confirmed fact.
3. **[DQ-2, high]** The 117-row event timeline is 59% noise (69 rows) by
   title/description screening — see (h) for detail and counts.
4. **[DQ-3, medium]** Two of three `aibq_unicorn_scores` rows carry
   dimension scores that do not arithmetically reconcile to their own
   stated composite under the disclosed dimension weights (2026-05-14 row:
   computes to 2.10, not the stated 2.30; 2026-05-13 row: computes to 2.50,
   not the stated 3.65). The command-center/framework pairing used in (b)
   reconciles exactly. The unicorn-scores row-level CE/GO/MD fields are not
   used here.
5. **[DQ-4, low]** `command_center_master_profiles`'s own CRA field reads 0
   rather than -1.50 for the same dated snapshot the framework deep-dive
   scores at CRA -1.50. Treated as an unpopulated field, not a genuine
   disagreement.
6. **[DQ-5, low]** Two AIBQ deep-dive source pages disagree slightly:
   composite 0.80 (GO 5.0, CRA -1.50, financials fully populated/Confirmed)
   vs. composite 0.82 (GO 5.1, CRA stated as 1.50, financials table entirely
   "Missing"). The second appears to predate financial-data population and
   also claims SSI ranks "#10 among the Frontier Five," which is
   arithmetically impossible for a five-member cohort — likely a
   template/copy artifact. The first (0.80) is treated as more current.
7. **[DQ-6, high]** Daniel Gross's departure / Sutskever's CEO transition is
   dated 2026-03-15 in the talent-flow table and 2025-07-01 (two
   High-importance rows) in the event timeline — roughly eight months
   apart. Frozen; both dates ship.
8. **[DQ-7, low]** "Founded in UK" appears in 2 of 5 near-duplicate
   founding-event rows, contradicting Palo Alto HQ confirmed four other
   independent ways. Treated as an error in those two rows.
9. **[DQ-8, medium]** Last funding round is named "Series B" in one
   master-profile field and "$2B Series C" in a sibling field of the same
   row; only "Series B" is corroborated by the event timeline.
10. **[DQ-9, high]** Two rounds of capital-raise headlines (April 2026's
    "$2B seed"/"$6B raise," and the May–July 2026 NVIDIA $5B financing) are
    not reflected in the canonical $3B total-raised figure as of the most
    recent extraction. Per house methodology, unclosed/rumored financings
    never anchor the base case — both are reported here as forward signals
    only.
11. **[DQ-10, info]** A command-center source page's claim that SSI ranks
    "#10 among the Frontier Five" is arithmetically impossible (the cohort
    has five members) and is not used.
12. **[DQ-11, info]** One 2026-07-02 tracker note references an embargoed
    cross-company quality-valuation coefficient in passing, in a shared
    cross-company digest row unrelated to SSI specifically. Per this
    project's standing embargo, a cross-company quality-valuation
    relationship exists and is embargoed from publication; no value, sign,
    or further characterization is reproduced here or anywhere in this
    profile.
13. **[DQ-12, info]** The tracker fired SSI-specific data-staleness flags
    twice (2026-06-15, 2026-07-09); noted as a freshness caveat on the
    current score, not evidence of a score change.
14. **[DQ-13, info]** Early (2024) valuation figures vary across
    contemporaneous restatements ($4B/$5B/~$20B-approach language) rather
    than converging on one number; presented as a range in (d), not a false
    single point value.

---

## (j) Sources count

- **98 distinct external Source URLs** cited across the 117-row event
  timeline (mainstream outlets — Bloomberg, TechCrunch, Axios, Fortune,
  Politico, NYT, GlobeNewswire, Google News wire links, etc. — alongside a
  handful of lower-tier "how to invest in pre-IPO stock" content-mill
  sites; sourcing quality varies row to row and was not independently
  re-verified during staging).
- **1 source-authority registry entry**: `ssi.inc` (Source Type: Official
  Company; Authority Score 9/10; Status: Active; last reviewed 2026-07-21).
- **0 of 2** talent-flow rows carry a populated Source URL (both blank).
- No entries in `framework_source_registry` or `canon_citations` for SSI
  specifically (both empty in this bundle).

Total distinct named sources referenced across the bundle: **≈ 99**
(98 timeline URLs + the `ssi.inc` authority-registry domain; no further
dedup was attempted between the two since they serve different roles —
one is a per-event citation list, the other is a domain-level authority
rating).
