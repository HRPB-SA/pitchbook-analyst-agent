# Extraction prompts to accompany the Q2 2026 analysis outline

Two Claude-in-Excel prompts, one per data source. Each creates organized tabs
that supply a specific outline section. Run PROMPT 1 inside the Unicorn 20
valuations+pricing workbook (cross-referencing its pricing-only twin), and
PROMPT 2 inside the Unicorn Monitor lighter workbook. Both are read-only against
source sheets and write only to new tabs; both build a MAP first and pause, flag
discrepancies, never fabricate, and format for reading.

Shared conventions for both prompts:
- Two as-of stamps: universe/index 6/30/2026; Unicorn 20 daily marks 7/15/2026.
  State which each tab uses.
- "Top 20" = the Unicorn 20 index constituents, not the 20 largest by value.
  State this on every top-20 tab.
- Universe figures are on the Monitor basis (1,556 active / $8,496.6B); label
  them so they are never blended with another basis.
- No fabrication -> `X-GAPS`. Flag anomalies -> `X-DISCREPANCIES` (id, severity,
  sheet, cell, rule, expected, actual). Live formulas, values preserved.
- Formatting: row-1 title; row-2 as-of + source + outline section it feeds;
  bold dark header; `Note:` block; freeze header + first column; units in
  headers; `#,##0.0` for $B, `0.0%` fractions, `0.0"x"` multiples; negatives in
  parentheses; zeros as `-`; banded rows; latest column highlighted; link back
  to MAP.

================================================================================
PROMPT 1 - Unicorn 20 valuations + pricing workbook
================================================================================

You are inside the Morningstar PitchBook Unicorn 20 valuations+pricing workbook
(daily model share prices and valuations for 20 marquee private names,
methodology v3, to 7/15/2026). Create new `U-` tabs that supply the Leaders,
PBQ, and Valuations sections of the Q2 analysis. Build a `U-MAP` first (source
sheets, grain, date range, the 20 constituent names, latest date) and pause for
review. Then build:

- `U-Fresh vs Stale` - feeds Leaders "the top of the market" and Valuations "the
  coverage gap." For each of the 20: latest fresh model valuation ($B, 7/15
  date), the last primary-round post-money (stale mark), the $ and % gap, and a
  rank by gap. Flag the widest divergences both ways (repricing risk vs upside).
  If the last-round mark is not in this file, pull it in PROMPT 2 and join by
  PitchBook ID; note the dependency in `U-GAPS`.
- `U-Latest Marks` - feeds Valuations "latest valuation." The 20, latest fresh
  valuation and share price, sorted, with as-of date; QoQ and since-first-round
  change from the historical series.
- `U-Rebased Performance` - feeds Leaders "value creation at the top." Rebased
  price index (=10 or 100 at entry) per name to latest, plus total and
  annualized return since inception and since 1/1/2026; the trajectory that
  shows top compounders vs laggards.
- `U-Value Creation` - feeds Leaders "value creation at the top." Per name:
  fresh valuation, years since first round, and (where invested-capital is
  available or joined from PROMPT 2) value created per year and capital-
  efficiency multiple. Flag names missing invested-capital to `U-GAPS`.
- `U-Estimate Integrity` - feeds PBQ "secondary pricing as the estimate-
  integrity input." For each of the 20, assemble the three prices to be
  compared: daily model mark, last-round mark, and (joined from PROMPT 2's
  `M-Secondaries`) the secondary-implied price; compute pairwise gaps and a
  simple agreement score (tight three-way agreement = high mark reliability).
  Leave the secondary column keyed for the join if not present here.
- `U-PBQ Frame` - feeds PBQ scorecard. Headers for the 20 x five PBQ dimensions
  and composite; populate only capital-efficiency and the estimate-integrity
  proxy from data; log the analyst-sourced dimensions (revenue quality, compute
  independence, governance, moat) to `U-GAPS` referencing the AIBQ input
  checklist. Do not invent scores.
- Back matter: `U-GAPS`, `U-DISCREPANCIES`.

Checkpoints: U-MAP (pause), then Leaders tabs (U-Fresh vs Stale, U-Latest Marks,
U-Rebased Performance, U-Value Creation), then PBQ tabs (U-Estimate Integrity,
U-PBQ Frame), then back matter. Report formula-error count and new discrepancies
per batch.

================================================================================
PROMPT 2 - Unicorn Monitor lighter workbook
================================================================================

You are inside the Unicorn Monitor lighter workbook (full universe, verticals,
index levels, secondary trades, all to 6/30/2026; Monitor basis 1,556 active /
$8,496.6B). Create new `M-` tabs that supply the Leaders, Verticals, and
Valuations & fallen sections. Build `M-MAP` first (source sheets, grain, date
range, the universe headline, index date range) and pause. Then build:

Leaders & universe
- `M-Concentration` - feeds Leaders "the quarter that belonged to five
  companies." NOTE: this file has no deal-level capital-raised amounts, so
  deal-VALUE concentration is not computable here (it is a primary-tracker
  exhibit). Build VALUATION concentration instead: top-10 share of aggregate
  (47.8%), the top-5 names' share of aggregate value, and formation
  (new-unicorn count vs value contributed). Monitor basis stated.
- `M-Step Ups` - feeds Leaders "step-ups" and Valuations "step-ups and RVVC."
  First verify Global Unicorn History shows round-date variation per company; if
  it does, build a snapshot-derived median step-up by year (labeled
  snapshot-derived) vs the 2016-2018 baseline and 2021 peak. RVVC and
  down-round share of value need capital-invested amounts NOT in this file ->
  `M-GAPS` (primary-tracker exhibit). If there is only one round date per
  company, the step-up is not derivable either -> GAPS. State the denominator
  excludes the non-raising dormant population.
- `M-AI Share` - feeds Leaders "AI: one-third of count, nearly half of value"
  and Verticals "AI as growth engine." AI share of count and of value by year,
  the 50% crossing, and concentration inside AI (top-2/3 names' share). Tie the
  AI aggregate to `Vertical MV and Count` and use `Vertical Unique Count` for a
  dedup'd basis; state the basis.

Verticals
- `M-Vertical Size` - feeds "SaaS and AI dominance" and "the narrow investable
  universe." Per vertical: tagged count, unique/dedup count, aggregate ($B),
  top-10 ($B), ranked; note nonexclusive tagging and the total exceeding the
  universe.
- `M-Vertical Returns` - feeds "the vertical return layer." Each vertical
  index's total return, annualized return, and risk to 6/30 from `Industry
  Vertical Performance`, set beside its count and valuation, so size and
  performance sit in one view. State the risk sampling frequency.
- `M-Vintage 2021` - feeds "the 2021 vintage and 2028 outlook." Reconstruct the
  2021 cohort from `Global Unicorn History` round dates: survivors, share of
  valuation set before 2023 and never retested, and a 20% / 30% markdown
  scenario on the untested marks with the implied aggregate hit.

Valuations & fallen
- `M-Value Location` - feeds "where the value sits." Top-10 share of aggregate
  by year and the reconcentration trajectory; value by tier.
- `M-Coverage Gap` - feeds "the coverage gap." Share of aggregate on marks
  older than 24 months vs recent (mark ages from round dates), the block with no
  estimate, and the estimate-vs-mark direction (above/flat/below) as a static
  cross-section (note estimates are undated).
- `M-Secondaries` - feeds Leaders secondary-price validation and PBQ estimate
  integrity. From `Secondary Markets`: per-constituent secondary-implied price,
  index weight, and market value, plus secondary transaction volume and count by
  quarter from the trade block. This is the tab PROMPT 1 joins to for the
  three-way price comparison. State the trade-date range.
- `M-Fallen` - feeds "fallen unicorns." Fallen count per year and per vertical,
  median down-round post-money, Q2 additions (from the curated fallen list with
  fall dates), plus the cohort-survival read (share never re-raising at
  6/12/.../60 months, AI vs non-AI) from `Global Unicorn History`.

Back matter: `M-CROSSWALK` (Monitor basis vs any other universe basis the report
uses, with per-line differences), `M-GAPS`, `M-DISCREPANCIES`.

Checkpoints: M-MAP (pause), then Leaders/universe tabs, then Verticals tabs,
then Valuations/fallen tabs, then back matter. Report formula-error count and
new discrepancies per batch. The `M-Secondaries` tab is the join target for
PROMPT 1's estimate-integrity work - build it before or alongside that step.
