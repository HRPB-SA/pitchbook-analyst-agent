# Claude-in-Excel prompt: build the Q2 2026 tracker sheets inside this workbook

For use with Claude working directly inside your Excel database (the live
workbook, not a file loaded elsewhere). Paste everything below the line. It
creates new, clean, organized sheets that extract and lay out every data object
the Q2 2026 Global Unicorn Tracker needs, sourcing from the sheets already in
this workbook. It does not change or delete any existing sheet.

---

You are working inside my live Excel workbook, which holds the raw PitchBook
data for the **Q2 2026 Global Unicorn Tracker** (universe as of **6/30/2026**).
Create a set of NEW sheets in this workbook that extract, compute, and organize
the data into a clean, readable structure. Build with Excel formulas that
reference the existing source sheets (SUMIFS, COUNTIFS, MAXIFS, INDEX/MATCH,
PERCENTILE, etc.) so the outputs stay live and auditable. Do not modify, sort,
or delete any existing sheet - read from them, write only to new sheets.

## Ground rules

1. **SpaceX is an active unicorn in Q2 2026.** It stays in the 6/30/2026
   universe (post-money in the snapshot). Every count, aggregate, and share is
   BASE = includes SpaceX. Only where it genuinely helps reading (top-10
   valuation share, space-tech vertical, exit-value strip-out) add a secondary
   column labeled "ex-SpaceX (sensitivity)" - never as the headline.
2. **Never fabricate.** If a field is not derivable from this workbook, leave it
   blank and log it on the `GAPS` sheet (object, field, why, where it lives
   instead). No estimated numbers.
3. **Definitions:** unicorn = active, venture-backed, post-money valuation >= $1B.
   Deal value = capital raised in unicorn VC rounds. Exit value = disclosed exit
   size. All aggregates as of 6/30/2026 unless a sheet states its own cutoff
   (trading/index data may end earlier - state it).
4. **Preserve identifiers.** Carry the PitchBook company/deal ID on every
   extracted row so sheets can be joined.
5. **Values live, not pasted.** Computed cells stay as formulas pointing at the
   source rows, not hardcoded results.
6. **Active-count source of truth:** use the published quarterly aggregate
   series for active/new counts, not a constituent list, wherever the two
   differ - note the difference on `MAP`.

## Step 0 - build `MAP` first, then stop and show me

Before creating data sheets, create a sheet named `MAP` that lists: every
existing source sheet (name, grain = what one row represents, date coverage, key
ID columns), and a table mapping each required field below to the exact source
sheet + column you will use. Flag any field with no source (goes to `GAPS`).
State the workbook's currency, unit convention, and both as-of dates. **Show me
`MAP` before extracting** so I can correct mappings.

## Sheets to create (after MAP is approved)

Create these in order, grouped. Keep one sheet per object; short names as shown.

**Front matter**
- `COVER` - title, both as-of stamps, a 3-line orientation, the SpaceX rule in
  one sentence, and a hyperlinked contents list (each sheet + a one-line
  description).
- `HIGHLIGHTS` - one screen: ~12 headline Q2 2026 numbers with prior-quarter and
  year-ago columns and a change column (aggregate valuation, active count, new
  unicorns, fallen unicorns, deal value, exit value, top-10 share, AI value
  share, dormant share, median step-up, plus the SpaceX line).

**Universe**
- `01 Dashboard` - 8 KPIs x 6 periods (2021-2025 annual + Q2 2026): deal value
  ($B), deal count, exit value ($B), exit count, new unicorns, fallen unicorns,
  median step-up (x), dormant share (%).
- `02 Qtr Activity` - by quarter Q1 2021-Q2 2026: deal value ($B), deal count,
  exit value ($B), exit count.
- `03 Universe` - by year 2016-2026: active count, new count, aggregate
  post-money ($B), aggregate top-10 ($B). Add `ex-SpaceX` column for Q2 2026.
- `04 Country` - as of 6/30/2026: country, active count, aggregate valuation
  ($B); sorted by valuation.
- `05 Vertical` - vertical, company count, aggregate valuation ($B), top-10
  ($B); note if verticals are nonexclusive.
- `06 Series Mix` - share of unicorn deal value by round series (Seed/A/B/C/D+)
  by year 2016-2026; each year sums to 100%.
- `07 Tested vs Untested` - aggregate valuation split into marks <=24 months old
  vs >24 months old, as of 6/30/2026 and by year where round dates allow.

**Leaders**
- `08 Deal Leaders` - every unicorn VC deal in Q2 2026: company, ID, deal date,
  series, deal size ($B), post-money ($B), investors, vertical, country; sorted
  by size; add a top-5 / top-10 / remainder flag.
- `09 Concentration` - per period 2021-Q2 2026: share of unicorn deal value in
  the top 5, top 10, top 25, top 50 deals.
- `10 Cap Efficiency` - top ~15 by post-money: company, post-money ($B), equity
  capital raised ($B), efficiency multiple (valuation / equity, x). Equity-only
  denominator; flag any company where only total capital is available.
- `11 Value Creation` - same set: valuation created since first round ($B),
  years since first round, value created per year ($B/yr).

**Quality**
- `12 PBQ` - if any quality/score fields exist in the workbook: company,
  composite, five sub-scores, valuation rank, quality rank, divergence. If no
  score fields exist, create headers only and log on `GAPS` that PBQ scores are
  analyst-generated, not in this data. Do not invent scores.

**Deals**
- `13 Val Percentiles` - per series (Seed/A/B/C/D+): 25/50/75/90th percentile
  PRE-money valuation for 2021 and 2026 H1, plus % change vs 2021.
- `14 Time Between Rounds` - months between consecutive unicorn rounds:
  25/50/75th percentile by year 2019-2026; note the denominator counts only
  companies that raised again.
- `15 Seed Size` - median seed round size for companies that later reached
  unicorn status, by year.

**Valuations & Dormancy**
- `16 Top10 Share` - by year 2016-2026: top-10 valuation ($B), rest ($B), top-10
  share (%).
- `17 Estimate vs Mark` - companies with both an updated estimate and a
  last-round mark: company, mark ($B), estimate ($B), above/flat/below, months
  since last round; counts of above/flat/below at the top.
- `18 Marked Down` - subset where estimate < mark: company, mark, estimate, %
  markdown, months since round, vertical; sorted by markdown.
- `19 RVVC & Step-up` - by year: median step-up (x) and median RVVC (new
  valuation created / capital invested); both series shown.
- `20 Fallen Unicorns` - company, date fell (use Unicorn End Date as the spine;
  keep Down Round Date + down-round post-money as extra columns), last
  valuation, vertical, country; plus counts per year and per vertical.
- `21 Dormancy Ledger` - as of 6/30/2026 and prior quarter: dormant count (no
  round >2 yrs), count stale >3 yrs, average mark age (yrs), and flows this
  quarter (dormant companies that raised again: n + median step-up; that fell:
  n). Reconstruct point-in-time via MAXIFS on round history; note the
  survivorship caveat.
- `22 Cohort Survival` - per unicorn-round cohort (H1 2021 ... H2 2025): share
  with NO later round at 6/12/18/24/30/36/48/60 months; AI cohort vs non-AI
  cohort side by side.

**Exits**
- `23 Qtr Exits` - by quarter 2021-Q2 2026: exit value ($B), exit count.
- `24 Exit by Type` - by year 2016-2026: share of exit VALUE and of exit COUNT
  split IPO / M&A / buyout.
- `25 Time to Exit` - by year: median and average years from founding to exit.
- `26 Exit List` - every unicorn exit in Q2 2026: company, exit date, type, exit
  size ($B), post value ($B), acquirer (if M&A), vertical, country; add a SpaceX
  flag and a running ex-SpaceX cumulative for the strip-out.
- `27 China AI IPO` - the China/Hong Kong AI listing cohort: company, IPO date,
  IPO price, current price, return since IPO (%), return to date (%); leave the
  price/return columns blank and log to `GAPS` if current prices are not in the
  workbook.
- `28 Unicorn M&A` - M&A exits where the acquirer is itself VC-backed / a
  unicorn: target, acquirer, date, size, and a three-way flag below mark
  (distressed) / within +/-10% (flat) / above mark (strategic), labeled a proxy.

**Performance**
- `29 Secondaries` - by year/quarter if present: secondary transaction volume
  ($B) and count; log fund contributions/distributions to `GAPS` if absent.
- `30 Index Levels` - index level series for every index in the workbook (US /
  Global Unicorn, Unicorn 20/30, regional, verticals, and public benchmarks);
  one date column, one column per index; plus a start/end/return/risk summary
  block. State the trading cutoff. Log any index not present to `GAPS`.
- `31 Correlation` - correlation between the US Unicorn index and the public
  benchmark over the window; state the window.
- `32 IPO Spreads` - median IPO performance spread vs a growth benchmark at
  Day 7/30/90/120 by year, global and US; log to `GAPS` if per-IPO price series
  are not in the workbook.
- `33 Best & Worst IPO` - best/worst VC-backed IPO performers since 1/1/2025:
  company, listing date, sector, country, performance to a stated date;
  performance column to `GAPS` if not sourceable here.

**Verticals**
- `34 AI Value Share` - by year 2016-2026: AI aggregate ($B), non-AI ($B), AI
  share (%).
- `35 Vertical Concentration` - per top vertical: aggregate ($B), largest
  company, its valuation, its share of the vertical (%); show the space-tech row
  both with and without SpaceX.

**Back matter**
- `DEFINITIONS` - every term (unicorn, dormant, RVVC, step-up, tested vs
  untested, PBQ), both as-of dates, the SpaceX treatment, currency, units.
- `GAPS` - everything not extractable, with where it lives instead.
- `CHECKS` - reconciliations as rows with a PASS/FAIL cell: quarterly figures in
  02/23 sum to the annual figures in 01/03; country (04) and vertical (05)
  valuations tie to the universe aggregate (03) within rounding. List any that
  do not tie and why.

## Formatting (apply to every new sheet)

- Row 1 title (bold, larger); row 2 as-of + source line (`As of 6/30/2026 |
  Source: PitchBook, Global`); blank row; then the header row (bold, dark fill,
  white text) and data; a `Note:` block below the table for caveats.
- Freeze the header row and the first label column.
- Units always in the column header (`Valuation ($B)`, `Share (%)`,
  `Efficiency (x)`); never inline in the cell.
- Number formats: $B as `#,##0.0`; percentages as `0.0%` stored as fractions;
  multiples as `0.0"x"`; counts `#,##0`; negatives in parentheses; zeros as `-`.
- Real dates, one format throughout.
- Banded alternate rows; highlight the current period (Q2 2026 / latest) column
  in every time series with a distinct fill + bold.
- No merged cells inside data ranges. Right-align numbers, left-align text.
- On each sheet put a small hyperlink back to `COVER`.

## How to work

Build `MAP` first and stop for my review. Then build in the order above, in
these batches, pausing after each so I can check: (a) COVER + HIGHLIGHTS,
(b) 01-07, (c) 08-15, (d) 16-22, (e) 23-28, (f) 29-35, (g) CHECKS + GAPS. After
each batch, confirm formulas evaluate with no errors and that reformatting moved
no numbers.
