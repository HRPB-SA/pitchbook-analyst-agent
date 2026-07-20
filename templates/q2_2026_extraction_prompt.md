# Claude Excel prompt: Q2 2026 Global Unicorn Tracker — data extraction

Paste everything below the line into a new Claude session, attach the new
dataset, and (if the file has formulas/multiple sheets) let the xlsx skill load.
It tells Claude exactly which data objects the Q2 tracker needs, how each maps
to a report exhibit, and how to output them.

---

You are a data analyst preparing the underlying data for the **Q2 2026 Global
Unicorn Tracker** (PitchBook Late-Stage Company Research; universe data as of
**June 30, 2026**). I am attaching a large dataset. Your job is NOT to write the
report — it is to extract, compute, and lay out every data object the report's
exhibits require into one clean Excel workbook I can chart from.

## Rules (read first, they override convenience)

1. **Profile before you extract.** First pass: for every sheet, list its name,
   row/column count, header row, grain (one row = one deal? one company? one
   company-day?), date coverage, and key identifier columns (PitchBook company
   ID, deal ID). Produce a `00_Map` sheet that maps each required field below to
   the actual source column you will use. Do this before computing anything.
2. **Never fabricate.** If a required field is not derivable from the dataset,
   leave it blank and log it on a `99_Gaps` sheet (object, field, why missing,
   what external source would fill it). An empty cell with a gap note beats an
   estimate. Do not infer numbers the data does not support.
3. **Match Q1 definitions.** Unicorn = active, venture-backed company with a
   post-money valuation ≥ $1B. "Deal value" = capital raised in unicorn VC
   rounds. "Exit value" = disclosed exit size. All aggregates as of the stated
   as-of date. Where the dataset's definition differs, note it on `00_Map`.
4. **Preserve identifiers.** Carry PitchBook company/deal IDs on every extracted
   row so objects can be joined later. Keep company names exactly as in source.
5. **Values, not prose.** Every output is a tabular sheet: labeled columns,
   one record per row, numbers as numbers (not "$1.2B" text). Dollar figures in
   $B unless noted. Dates as real dates. No merged cells inside data ranges.
6. **Show the arithmetic.** For any computed cell (shares, medians, step-ups,
   CAGRs), use live Excel formulas referencing the source rows, not hardcoded
   results, so I can audit and reflow. Put raw inputs and the computed output on
   the same sheet.
7. **Flag the SpaceX discontinuity everywhere it matters.** SpaceX (last private
   mark ~$1.25T; IPO priced June 12, 2026) leaves the private universe
   mid-quarter. Any aggregate it distorts (total valuation, top-10 share, exit
   value, space-tech vertical) must be produced BOTH with and without SpaceX,
   in adjacent columns.
8. **As-of discipline.** Universe/valuation objects: as of 6/30/2026. Trading/
   performance objects may run to a later stamped date if the data extends there
   — state the exact cutoff in the sheet header.

## Data objects to produce (one sheet each, numbered as below)

Deliver a single workbook, `Q2_2026_Unicorn_Tracker_DATA.xlsx`, with these tabs.
If a source cannot support a whole object, produce the partial and log the rest
on `99_Gaps`. Do not silently drop an object.

### Dashboard & universe

- **01_Quarter_Dashboard** — 8 KPIs × 6 periods (2021, 2022, 2023, 2024, 2025
  annual + Q2 2026): unicorn deal value ($B), deal count, exit value ($B), exit
  count, new unicorn count, fallen-unicorn count, median valuation step-up (x),
  dormant share (%). One row per KPI, one column per period.
- **02_Quarterly_Activity** — by calendar quarter (Q1 2021 → Q2 2026): unicorn
  deal value ($B), deal count, exit value ($B), exit count. This is the QoQ
  time series behind the Quick stats bars.
- **03_Universe_Timeseries** — by year (2016 → 2026) AND by quarter where
  available: active unicorn count, new unicorn count, aggregate post-money
  valuation ($B), aggregate post-money valuation of top 10 ($B). Add a column
  `Aggregate ex-SpaceX` for the last period.
- **04_Universe_by_Country** — as of 6/30/2026: country, active unicorn count,
  aggregate post-money valuation ($B). Sort by valuation.
- **05_Universe_by_Vertical** — as of 6/30/2026: vertical, company count,
  aggregate post-money valuation ($B), aggregate top-10 valuation ($B). Note in
  a header cell that verticals are nonexclusive (a company can appear in
  several) if that is true of the source.
- **06_Deal_Value_by_Series** — share of unicorn deal value by round series
  (Seed / A / B / C / D+), by year 2016 → 2026. Percentages that sum to 100%
  per year.
- **07_Tested_vs_Untested** — decompose aggregate post-money valuation into
  value carried on marks ≤24 months old vs >24 months old, as of 6/30/2026,
  and the same split by year if round-date data allows. This powers the shaded
  "untested value" band.

### Market leaders & concentration

- **08_Q2_Deal_Leaders** — every unicorn VC deal closed in Q2 2026: company,
  PitchBook ID, deal date, round series, deal size ($B), post-money valuation
  ($B), lead/investor names, vertical, country. Sorted by deal size. Add a
  `Top-N flag` column (top 5 / top 10 / remainder).
- **09_Concentration_Tiers** — for each period 2021 → Q2 2026: share of total
  unicorn deal value captured by the top 5, top 10, top 25, top 50 deals. This
  is the concentration trend line.
- **10_Capital_Efficiency** — top ~15 unicorns by post-money valuation: company,
  post-money valuation ($B), cumulative equity capital raised ($B), capital-
  efficiency multiple (valuation ÷ equity raised, "x"). Equity-only denominator
  (exclude debt); note any company where only total-capital is available.
- **11_Value_Creation_Rate** — for the same top set: valuation created since
  first round ($B), years since first round, value created per year ($B/yr).

### Quality (PBQ) — may not be in this dataset

- **12_PBQ_Scores** — if the dataset carries any quality/score fields: company,
  PBQ/AIBQ composite, the five sub-scores (capital efficiency, revenue quality,
  compute independence/strategic velocity, governance optionality, moat
  durability), valuation rank, quality rank, rank divergence. If the dataset has
  NO score fields, create the sheet with headers only and log on `99_Gaps` that
  PBQ scores are analyst-generated, not in this source. Do not invent scores.

### Deals & fundraising

- **13_Valuation_Percentiles_by_Series** — for each series (Seed, A, B, C, D+):
  25th / 50th / 75th / 90th percentile pre-money (or post-money — state which)
  valuation, for 2021 and for the latest period, plus the % change vs 2021. Show
  the underlying deal list the percentiles are computed from on a helper sheet
  `13h_pctile_inputs`.
- **14_Time_Between_Rounds** — distribution of months between consecutive
  unicorn rounds: 25th / 50th / 75th percentile, by year 2019 → 2026. Note the
  denominator (only companies that DID raise again are counted) in the header.
- **15_Seed_Check_Inflation** — median seed round size for companies that later
  reached unicorn status, by year. Small panel.

### Valuations, fallen unicorns, dormancy

- **16_Top10_Valuation_Share** — by year 2016 → 2026: aggregate valuation of
  top 10 ($B), aggregate valuation of the rest ($B), top-10 share (%). The
  reconcentration chart (18.4% trough → present).
- **17_Estimate_vs_Mark** — companies where the dataset carries both an
  independent/updated valuation estimate and a last-round mark: company, last-
  round mark ($B), estimate ($B), estimate vs mark (above / flat / below),
  months since last round. Summarize counts (n above / flat / below) at top.
- **18_Marked_Down** — subset of 17 where estimate < mark: company, mark,
  estimate, % markdown, months since last round, vertical. Sorted by markdown.
- **19_RVVC_StepUp** — by year: median valuation step-up (x) and median RVVC
  (relative velocity of value creation = new valuation created ÷ capital
  invested). Show both series so the divergence is visible.
- **20_Fallen_Unicorns** — companies that lost unicorn status: company, date
  fell, last valuation, vertical, country. Plus a summary block: count per year
  and count per vertical.
- **21_Dormancy_Ledger** — as of 6/30/2026 and the prior quarter: total dormant
  count (no round in >2 yrs), count stale >3 yrs, average age of most recent
  mark (yrs), and FLOWS this quarter — dormant companies that raised again (n,
  median step-up), dormant companies that fell (n).
- **22_Cohort_Survival** — for each unicorn-round cohort (H1 2021 … H2 2025):
  share of the cohort with NO subsequent round at 6 / 12 / 18 / 24 / 30 / 36 /
  48 / 60 months after the cohort round. Produce two versions side by side: AI
  cohort vs non-AI cohort. This is the dormancy survival-curve object.

### Exits

- **23_Quarterly_Exits** — by quarter 2021 → Q2 2026: exit value ($B) and exit
  count. (May duplicate part of 02; keep for the Exits-section spec.)
- **24_Exit_Share_by_Type** — by year 2016 → 2026: share of exit VALUE and share
  of exit COUNT split by IPO / M&A(acquisition) / buyout. Two blocks.
- **25_Time_to_Exit** — by year: median and average years from founding to exit.
- **26_Exit_List_Q2** — every unicorn exit in Q2 2026 (and full-year context if
  cheap): company, exit date, exit type, exit size ($B), post value ($B),
  acquirer (if M&A), vertical, country. Add columns to support the base-vs-
  megadeal strip-out: a `SpaceX flag` and a running `ex-SpaceX cumulative`.
- **27_China_AI_IPO** — the Hong Kong / China AI listing cohort: company, IPO
  date, IPO price, current price, return since IPO (%), return to date (%).
- **28_Unicorn_on_Unicorn_MnA** — M&A exits where the acquirer is itself VC-
  backed or a unicorn: target, acquirer, date, size, distressed vs strategic
  flag if determinable.

### Secondaries & liquidity

- **29_Secondaries** — by year (and quarter if available): secondary transaction
  volume ($B) and transaction count. Plus, if present, VC fund contributions vs
  distributions ($B) and net cashflow by year.

### Performance

- **30_Index_Levels** — daily (or available frequency) index levels for every
  index the source carries: Morningstar PitchBook US Unicorn, Global Unicorn,
  Unicorn 30 / Unicorn 20, US/Asia/Europe regional, each vertical index, and the
  public benchmarks (Global TME, US TME / MM100). One date column, one column
  per index. Also a summary block: start/end level, total return (%), annualized
  return, risk (%) per index, over the window the source uses.
- **31_Index_Correlation** — rolling and full-window correlation between the US
  Unicorn index and the public MM100/US TME benchmark, so the +0.95 → −0.63
  inversion can be traced. State the window.
- **32_IPO_Perf_Spread** — median IPO performance spread (percentage points) vs
  a broad growth benchmark at Day 7 / 30 / 90 / 120, by year 2021 → Q2 2026,
  produced twice: global and US-only.
- **33_Best_Worst_IPO** — best and worst VC-backed IPO performers since
  1/1/2025: company, listing date, sector, industry, country, performance to the
  stamped date (%). Sorted best to worst.

### Vertical divide

- **34_AI_Value_Share** — by year 2016 → 2026: AI unicorn aggregate valuation
  ($B), non-AI aggregate ($B), AI share (%). Pre-builds the "crossing 50%"
  annotation.
- **35_Vertical_Concentration** — for each top vertical: aggregate valuation
  ($B), name of the single largest company, that company's valuation, and its
  share of the vertical (%). Produce the space-tech row both with and without
  SpaceX to show the aggregate collapse.

## Output & handoff

- One workbook, tabs named exactly as above, plus `00_Map` (field→source
  mapping) and `99_Gaps` (everything not extractable).
- On `00_Map`, state the dataset's as-of date, its unicorn definition, its
  currency, and any place its grain forced a definitional compromise.
- After building, run a self-check: for objects 01–07 confirm the totals
  reconcile (e.g., quarterly deal values in 02 sum to the annual figure; country
  and vertical valuations tie to the universe aggregate within rounding). Report
  the reconciliation on a `98_Checks` sheet — list any object that does NOT tie
  and why.
- Do not chart. Data only. I will build exhibits from these tabs.

Start by profiling the file and showing me `00_Map` before extracting, so I can
correct any column mapping before you compute.
