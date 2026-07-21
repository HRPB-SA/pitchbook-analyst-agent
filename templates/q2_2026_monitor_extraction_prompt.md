# Claude-in-Excel prompt: extract the Monitor file into report-ready tabs

For the Morningstar PitchBook Unicorn Monitor workbook
(`Unicorn_Monitor_Data_Q2_2026.lighter.hr_version.xlsx`). Paste below the line
into Claude working inside that file. It creates new `M-` tabs holding the
granular data this file uniquely provides for the Q2 2026 Global Unicorn Tracker,
each tied to a report exhibit and to the matching primary-tracker sheet, and it
reconciles this file against the primary tracker so the two bases are never
blended blindly. Read-only against source sheets; writes only to new `M-` tabs.

---

You are inside the Morningstar PitchBook Unicorn Monitor workbook (universe and
index data as of **6/30/2026**). This file is a SECOND source that complements
my primary Q2 2026 tracker database - and its universe is on a DIFFERENT basis
(this file: 1,556 active, $8,496.6B aggregate, $4,058B top-10; the primary
tracker: 1,743 active, $8,232.5B, top-10 36.8%). Your job is to extract the
granular data this file uniquely offers into new `M-` tabs, tie each to a report
exhibit, and RECONCILE the two bases - never silently merge them. Build with
live formulas referencing the source sheets. Do not modify, sort, or delete any
existing sheet.

## Why this file matters (what it has that the primary tracker lacked)

- **Index levels through 6/30/2026** (the primary tracker's trading data stopped
  at 3/31) - `Global Levels + Performance`, `Regional Levels + Performance`,
  `Industry Vertical Performance`. This fills the performance section and lets
  the correlation "validation test" run to quarter-end.
- **Secondary-market transactions** - `Secondary Markets` (trade date, PitchBook
  ID, volume; plus index constituent weights/MV).
- **True point-in-time universe snapshots** - `Global Unicorn History` (~47
  dated snapshots, per-company post-money + country + region + round date),
  which replaces the primary tracker's MAXIFS reconstruction and removes its
  survivorship bias.
- **Clean pre-computed universe / regional / vertical time series** - the
  `Overview` sheets and `Vertical MV and Count`.

Prioritize the data that is HERE and was MISSING there. Do not re-derive things
the primary tracker already has well (deal-level leaders, cap efficiency, PBQ).

## Ground rules

1. **Two bases, reconciled, never blended.** Every `M-` tab states at the top
   that it is on the Monitor basis. The `M-CROSSWALK` tab (below) reconciles the
   Monitor universe to the primary tracker's published figures and flags every
   difference. The report will choose one basis per exhibit; your job is to make
   the choice informed, not to average them.
2. **As-of 6/30/2026.** Universe snapshots and index levels both reach 6/30 in
   this file - state the exact last date on each tab (do not assume; read it).
3. **Never fabricate.** Anything this file cannot supply goes to `M-GAPS`
   (PBQ scores, per-IPO price paths, LP fund cashflows, MM100/Unicorn-30 if
   absent). No estimated numbers.
4. **Flag discrepancies.** Reuse the primary tracker's discrepancy discipline:
   log every anomaly to `M-DISCREPANCIES` (ID, severity, category, sheet, cell,
   rule, expected, actual, resolution) and highlight the offending extract cell.
   Nonexclusive verticals (a company in several) is a label, not an error.
5. **Live formulas, values preserved.** Computed cells reference source rows; do
   not paste hardcoded results.

## Step 0 - build `M-MAP` first, then stop

Profile every source sheet (name, grain, date coverage, key ID columns) and map
each required field below to its exact source sheet + column. State this file's
universe headline (active count, aggregate, top-10, new count) and the index
date range. Show me `M-MAP` before extracting.

## Tabs to create (each tied to a report exhibit + primary-tracker sheet)

**Universe & formation**
- `M-Universe TS` - annual (2014-2026) and quarterly (Q4'14-Q2'26) active count,
  new count, aggregate ($B), top-10 ($B), from `Overview Global`. Feeds report
  section 3.4 / 3.9; pairs with primary sheets 03 / 16.
- `M-Region TS` - US / Asia / Europe: active count, aggregate, top-10, new count
  by period, from `Overview Region`. Feeds 3.4; pairs with primary sheet 04.
- `M-PIT Universe` - from `Global Unicorn History`: at each of the ~47 dated
  snapshots, the active roster size, aggregate post-money, and top-10, PLUS
  derived formation (new PBIDs vs prior snapshot) and dormancy (share whose
  latest round date precedes the snapshot by >24 months). This is a TRUE
  point-in-time series - label it as the survivorship-clean alternative to the
  primary tracker's MAXIFS reconstruction (sheets 01 dormant / 07 / 21 / 22).
- `M-Country` - latest snapshot in `Global Unicorn History`: country, active
  count, aggregate ($B), sorted. Feeds 3.4; pairs with primary sheet 04.

**Verticals**
- `M-Vertical TS` - the 11 verticals in `Overview Industry Vertical`: active
  count, aggregate, top-10, new count by year 2021-2026. Feeds 3.12; pairs with
  primary sheets 05 / 34.
- `M-Vertical Snapshot` - `Vertical MV and Count`: each of the 12 vertical
  indexes, company count and latest aggregate ($B) as of 6/30. Note the total
  (1,793 co / $11,857.2B) EXCEEDS the universe because verticals are
  nonexclusive - label, do not flag. Feeds 3.12 / sheet 35.
- `M-Vertical Composition` - from `Vertical Unique Count` / `Pivot Vertical`:
  unique company count per vertical and cross-vertical overlap, so "AI share"
  can be stated on a disciplined basis. Feeds the sheet-34 AI-share
  decomposition (the 61.6% needs its basis pinned).

**Performance (this file's biggest contribution - data to 6/30/2026)**
- `M-Index Levels` - `Global Levels + Performance`: daily levels to 6/30 for
  every index present (Global Unicorn, Unicorn 20, and the public benchmarks),
  one date column + one column per index, plus the start/end/return/risk summary
  block. State the risk sampling frequency. Feeds 3.11; pairs with primary sheet
  30 and EXTENDS it from 3/31 to 6/30.
- `M-Regional Index` - `Regional Levels + Performance`: US / Asia / Europe
  Unicorn index levels to 6/30 + summary. Feeds 3.11.
- `M-Vertical Index` - `Industry Vertical Performance`: the 11 vertical index
  levels to 6/30 + return/risk. Feeds 3.11 / 3.12 (vertical performance).
- `M-Correlation` - compute rolling (state the window, e.g. 90-day) and
  full-window correlation between the US/Global Unicorn index and the public
  benchmark, through 6/30. This RESOLVES the primary tracker's D-033 (its 3/31
  data could not settle the +0.95 -> -0.63 inversion); report what the 6/30 data
  actually shows and footnote any window/frequency difference vs the Q1 figure.
  Feeds 3.11; pairs with primary sheet 31.

**Liquidity**
- `M-Secondaries` - `Secondary Markets`: secondary transaction volume and count
  by quarter (from the trade-level block), plus the index constituent weights /
  market values. State the trade-date range. Feeds 3.10; pairs with primary
  sheet 29 (fills its first half; LP contributions/distributions remain a gap).

**Reconciliation & back matter**
- `M-CROSSWALK` - the key one. Side by side, Monitor basis vs primary-tracker
  published basis, for: active count (1,556 vs 1,743), aggregate ($8,496.6B vs
  $8,232.5B), top-10 ($4,058B / 47.8% vs 36.8%), new-unicorn count (24 vs 84),
  and index total returns where both exist. Compute each difference, and for
  each row give a one-line likely cause (different constituent inclusion rules,
  index-universe vs full-universe, snapshot timing). Mark which basis the report
  should use for which exhibit.
- `M-GAPS` - what this file cannot supply (PBQ scores, per-IPO price paths, LP
  cashflows, and any index the report needs but is absent here, e.g. MM100 or
  Unicorn 30 if not present).
- `M-DISCREPANCIES` - the anomaly log for this workbook.

## Formatting (every M- tab)

Row-1 title; row-2 as-of + "Monitor basis" + source; header row bold on dark
fill; `Note:` block below; freeze header + first column; units in headers
(`Valuation ($B)`, `Return (%)`, `Level`); `#,##0.0` for $B, `0.0%` as fractions,
counts `#,##0`; negatives in parentheses, zeros as `-`; real dates one format;
banded rows; highlight the Q2 2026 / latest column; no merged cells in data; a
link back to `M-MAP`.

## Order and checkpoints

Build `M-MAP` first and stop for review. Then: (a) M-Universe TS, M-Region TS,
M-Country; (b) M-PIT Universe (the point-in-time engine); (c) the three vertical
tabs; (d) the four performance tabs incl. M-Correlation; (e) M-Secondaries;
(f) M-CROSSWALK + M-GAPS + M-DISCREPANCIES. Pause after each batch; report
formula-error count and any new discrepancies. The one I most want to see is
`M-CROSSWALK` - do not treat the two universes as interchangeable until it is
built.
