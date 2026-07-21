# Q2 2026 Global Unicorn Tracker - detailed analysis outline

Built from three datasets: the Morningstar PitchBook **Unicorn 20** pricing file
and valuations+pricing file (daily model-marked share prices and valuations for
20 marquee private names, methodology v3, through 7/15/2026, incorporating
secondary trades and public comps), and the **Unicorn Monitor** lighter
workbook (full universe, verticals, index levels, secondary trades, all to
6/30/2026).

Framing note carried throughout: **"top 20" = the Morningstar PitchBook
Unicorn 20 index constituents**, not the 20 largest unicorns by valuation. These
are the names that carry daily fresh marks and secondary data - which is exactly
what makes the fresh-vs-stale, secondary-validation, and PBQ-estimate-integrity
threads computable. Where the analysis uses a universe figure (counts,
aggregates, verticals), state whether it is on the Monitor basis (1,556 active /
$8,496.6B) so it is never blended with a different basis.

Two as-of stamps: universe and index data 6/30/2026; the Unicorn 20 daily marks
run to 7/15/2026 (state which is used where).

---

## Market overview (leaders)

### The quarter that belonged to five companies
- Q2 unicorn deal value concentrated in a handful of names: top 5 deals as a
  share of quarterly deal value, top 10 share, and the remainder. The headline
  number describes a fundraising cadence of a few frontier labs, not the market.
- Decompose the headline: strip the single largest deal/event to show the
  "genuine" broad-based figure underneath (the recurring xAI/SpaceX-style
  strip-out).
- Formation vs concentration: new-unicorn count for the quarter against how
  little of the value the new entrants represent.
- Source: Monitor `Overview Global` (quarterly deal/new-unicorn series);
  deal-leader ranking from the deal-level data.

### The top of the market: fresh prices, stale prices, and the gap between them [+ secondary-price validation]
- For each of the 20: the **fresh mark** (Morningstar daily model valuation,
  latest date) vs the **stale mark** (last primary-round post-money), and the
  percentage gap between them. This is the section the Unicorn 20 file was built
  for.
- **Secondary-price validation:** overlay actual secondary transactions
  (Monitor `Secondary Markets`: constituent secondary-implied price, index
  weight, market value, and dated trades) against both the fresh model mark and
  the stale round mark - does the secondary tape corroborate the model's fresh
  price, or sit closer to the stale round?
- Rank the 20 by fresh-vs-stale gap; flag names where the model mark and the
  last round diverge most (the repricing-risk and repricing-upside tails).
- Source: Unicorn 20 valuations file (`Historical Valuations`, `Historical
  Prices`, latest column); Monitor `Secondary Markets`.

### Value creation at the top, value stagnation everywhere else
- Value created since first round for the top names (fresh mark minus cumulative
  invested capital), and value created per year, showing the order-of-magnitude
  spread from the top compounder to the laggard.
- Contrast with the median unicorn: how little cumulative value the middle and
  bottom of the universe have created, and how much of total value creation the
  top 3 alone account for.
- Source: Unicorn 20 valuations (rebased series for trajectory); Monitor
  `Overview Global` / `Global Unicorn History` for the universe distribution.

### Step-ups: the active market is functioning
- Median valuation step-up for unicorn rounds this quarter and by year, against
  the 2016-2018 functioning-market baseline and the 2021 bubble peak - the
  read that pricing discipline has returned for companies actually raising.
- Pair step-ups with down-round frequency and the share of value flowing into
  down rounds, with an explicit note on what the denominator omits (the dormant
  population that is not raising at all).
- Source: Monitor round-history within `Global Unicorn History`; universe series
  in `Overview Global`.

### AI: one-third of count, nearly half of value
- AI as a share of unicorn count and of aggregate value, and the trajectory of
  both, with the crossing point where AI value share passes 50%.
- Concentration inside AI: how much of AI value sits in the top two or three
  names, so "AI exposure" is shown to be exposure to specific cap tables.
- Source: Monitor `Vertical MV and Count`, `Overview Industry Vertical`,
  `Vertical Unique Count` (for a disciplined, dedup'd AI-share basis).

---

## Verticals

### SaaS and AI dominance, and the steep drop-off after
- Company count and aggregate valuation by vertical, ranked: SaaS and AI at the
  top, then the steep fall to fintech, e-commerce, mobility, and the rest.
- Note the nonexclusive tagging (a company appears in several verticals) so the
  vertical total exceeds the universe - label, do not treat as error.
- Source: Monitor `Vertical MV and Count` (12 vertical indexes, count + latest
  aggregate), `Overview Industry Vertical`.

### The narrow investable universe
- What a vertical-blind portfolio of N names would actually hold given the
  count distribution - the concentration that the 1,793-tag figure disguises.
- Unique vs tagged counts per vertical (dedup) to show the true breadth.
- Source: Monitor `Vertical Unique Count`, `Pivot Vertical`.

### Count and valuation vs. performance: the vertical return layer [+ vertical index returns]
- Add the return dimension the count/valuation view lacks: each vertical index's
  total and annualized return and risk, so a vertical's size is set against how
  its constituents have actually performed.
- Which verticals are large but flat, and which are small but compounding -
  the size-vs-performance quadrant.
- Source: Monitor `Industry Vertical Performance` (11 vertical index levels to
  6/30 + return/risk block).

### AI as growth engine and concentration risk
- AI as the highest-formation, highest-value-growth, and highest-attrition
  vertical simultaneously - the single vertical that is both the growth engine
  and the concentration risk.
- The read that underweighting AI is a bet against the market's center of
  gravity, while overweighting it is exposure to two or three cap tables.
- Source: Monitor vertical series + `Industry Vertical Performance`.

### The 2021 vintage and 2028 outlook
- The 2021 boom cohort's survival and repricing status: how much of that
  vintage's valuation was set before 2023 and never retested, and the
  fund-cycle forcing function that lands 2028-2031.
- Scenario overlay: a 20% vs 30% markdown on the untested 2021 marks and the
  implied hit to the aggregate.
- Source: Monitor `Global Unicorn History` (round dates + marks for vintage
  reconstruction), `Overview Global`.

---

## PitchBook Business Quality (PBQ) and valuations (top 20)

### Why the valuation table isn't a quality ranking
- The valuation-rank vs quality-rank divergence: a list of the top 20 by
  valuation is a list of the most expensive companies, not the best ones.
  Show the capital-efficiency spread across the 20 to make the point (the
  order-of-magnitude gap from the top compounder to the capital-hungry name).
- Source: Unicorn 20 valuations (marks) + invested-capital inputs; PBQ scores
  are analyst-generated (see input checklist).

### Expanding PBQ across the top 20 unicorns [+ secondary pricing as the estimate-integrity input]
- Extend the PBQ/AIBQ five-dimension frame from the six scored frontier names to
  all 20, flagging which dimensions are computable from data vs analyst-supplied.
- **Secondary pricing as the estimate-integrity input:** use the gap between the
  daily model mark, the last-round mark, and the actual secondary tape as the
  observable proxy for estimate integrity / valuation freshness inside the PBQ
  governance-optionality and capital-efficiency dimensions - the names whose
  three prices agree score higher on mark reliability than those where they
  diverge.
- Source: Unicorn 20 valuations + Monitor `Secondary Markets`; PBQ rubric and
  dimensions 2-5 from the AIBQ input checklist (analyst/disclosure sourced).

### PBQ per $ of valuation
- Quality score divided by valuation rank (or per $B of post-money) - the
  ranked bar showing who delivers the most business quality per dollar of price
  paid. The single cleared expression of the quality-vs-price relationship.
- Source: PBQ composite (analyst) over Unicorn 20 marks.

### PBQ scorecard by company
- The per-company scorecard: composite plus the five sub-scores, with the
  radar/table layout, for the scored set, extended toward the full 20 as
  dimensions are populated.
- Source: PBQ composite + sub-scores (analyst); marks from Unicorn 20.

---

## Valuations & fallen unicorns

### Where the value sits
- Top-10 share of aggregate unicorn valuation and its trajectory - the
  reconcentration back toward the 2016 level after the 2017-2023 broad-based
  era. Where the value sits by tier and by vertical.
- Source: Monitor `Overview Global` (aggregate + top-10 series).

### Latest valuation
- The current aggregate and its quarter-over-quarter move, decomposed: how much
  of the change is genuine repricing vs composition (names entering/leaving,
  SpaceX's status), on the Monitor basis with the figure stated.
- The latest per-name marks for the 20 (fresh model valuations) as the leading
  edge of where marks are actually moving.
- Source: Monitor `Overview Global`; Unicorn 20 valuations latest column.

### The coverage gap: stale marks vs. fresh marks
- The universe's coverage problem: the share of aggregate value carried on marks
  older than 24 months vs recently tested, and the block of companies with no
  independent estimate at all. The 20 are the fresh-mark frontier; most of the
  universe is not.
- Estimate-vs-mark direction across the covered set (share estimated above,
  flat, below the last round) - the up-round-pressure read - explicitly noting
  that estimates are undated and so shown as a static cross-section.
- Source: Monitor `Global Unicorn History` (mark ages via round dates); Unicorn
  20 valuations (the fresh-mark exemplar).

### Step-ups and relative velocity of value creation (RVVC)
- Median step-up paired with RVVC (new valuation created per dollar invested) by
  year, so the two are read together: rounds can step up in price while
  destroying value per dollar if the raise is large relative to the increment.
- The recovery in RVVC off the 2023 trough against the 2016-2018 baseline, and
  what it implies for the next two years.
- Source: Monitor round history in `Global Unicorn History`.

### Fallen unicorns
- The fallen roster: count per year and per vertical, the median down-round
  post-money, and the Q2 additions, driven off the curated fallen list with fall
  dates.
- The shadow inventory: dormant companies carrying untested marks that have not
  yet been reclassified, and the scenario range if 10-20% resolve downward.
- Cohort-survival read: the share of each vintage's cohort that never re-raised,
  split AI vs non-AI, showing AI's follow-on edge at the unicorn tier.
- Source: Monitor `Global Unicorn History` (cohort reconstruction, dormancy);
  curated fallen list.
