# Claude Excel prompt: organize the Q2 2026 tracker data into a readable workbook

Paste everything below the line into the Claude Excel session that holds the
extracted data (`Q2_2026_Unicorn_Tracker_DATA.xlsx`). It does not re-extract or
change any numbers - it reorganizes and formats the existing objects into one
clean workbook a human can scan and navigate. Output is a NEW file so the raw
extraction stays intact.

---

You have the extracted workbook `Q2_2026_Unicorn_Tracker_DATA.xlsx` (objects
01-35 plus 00_Map, 98_Checks, 99_Gaps). Produce a reader-friendly companion,
`Q2_2026_Unicorn_Tracker_READABLE.xlsx`. Your job is presentation and
navigation only: do not alter any underlying value, and keep every live formula
live (reference the source cells, never paste hardcoded results over a formula).
Deliver a new file; do not overwrite the extraction.

## Ground rule: SpaceX is an active unicorn in Q2 2026

SpaceX counts as an active unicorn in the 6/30/2026 universe (post-money in the
snapshot). The **base case INCLUDES SpaceX** in every count, aggregate, and
share. Where an ex-SpaceX view genuinely aids reading (top-10 valuation share,
space-tech vertical, the exit-value strip-out), show it as a **secondary column
clearly labeled "ex-SpaceX (sensitivity)"** - never as the headline number, and
never remove SpaceX from the base. Update any note that previously called the
snapshot's SpaceX inclusion a defect.

## Workbook architecture (this exact tab order)

Front matter, then eight color-coded section groups, then back matter.

**Front matter**
1. `Cover` - report title, both as-of stamps (universe as of 6/30/2026; trading
   or index data as of its own cutoff, stated), a 3-4 line orientation, the
   SpaceX rule in one sentence, and a hyperlinked table of contents: every tab
   listed with a one-line plain-English description of what it shows.
2. `Highlights` - one screen, no scrolling. The ~12 headline numbers for Q2 2026
   with a prior-quarter and year-ago column and a change column: aggregate
   post-money valuation, active unicorn count, new unicorns, fallen unicorns,
   unicorn deal value, exit value, top-10 valuation share, AI share of value,
   dormant share, median step-up, and the SpaceX line (last private mark / IPO
   status). Big, clean, one metric per row. Use up/down formatting on the change
   column.

**Section groups** (keep the numbered objects as individual tabs - do not merge
them into mega-sheets - but rename them short and color the tab by group):

- Universe (blue tabs): 01 Dashboard, 02 Qtr Activity, 03 Universe, 04 Country,
  05 Vertical, 06 Series Mix, 07 Tested vs Untested
- Leaders (teal): 08 Deal Leaders, 09 Concentration, 10 Cap Efficiency,
  11 Value Creation
- Quality (grey): 12 PBQ
- Deals (green): 13 Val Percentiles, 14 Time Between Rounds, 15 Seed Size
- Valuations & Dormancy (amber): 16 Top10 Share, 17 Estimate vs Mark,
  18 Marked Down, 19 RVVC & Step-up, 20 Fallen Unicorns, 21 Dormancy Ledger,
  22 Cohort Survival
- Exits (orange): 23 Qtr Exits, 24 Exit by Type, 25 Time to Exit,
  26 Exit List, 27 China AI IPO, 28 Unicorn M&A
- Performance (purple): 29 Secondaries, 30 Index Levels, 31 Correlation,
  32 IPO Spreads, 33 Best & Worst IPO
- Verticals (blue-green): 34 AI Value Share, 35 Vertical Concentration

**Back matter**
- `Definitions` - every term used (unicorn, dormant, RVVC, step-up, tested vs
  untested, PBQ), both as-of dates, the SpaceX treatment, currency, and the unit
  convention. Plain sentences.
- `Gaps` - the cleaned 99_Gaps: object, field, why absent, where it lives
  instead (mark the cross-source items - secondaries volume/count, and the
  vertical/regional/TME indexes - as "in Monitor workbook," not "missing").
- `Checks` - the cleaned 98_Checks: each reconciliation as a row with a clear
  PASS / FAIL cell (green / red fill) and the tie-out difference.

## Consistent layout for every data tab

1. Row 1: sheet title in Arial 14 bold.
2. Row 2: as-of stamp + source line, e.g. `As of 6/30/2026  |  Source: PitchBook
   (Geography: Global)`. Grey italic.
3. Row 3: blank.
4. Row 4: the table header (bold white text on a dark fill), then data rows.
5. Below the table, one blank row, then a `Note:` block for definitions,
   denominator caveats, and the grain-compromise flags from 00_Map.
6. Top-left of every tab except Cover: a small `^ Cover` hyperlink back to the
   index.

## Formatting standards (apply everywhere)

- Font: Arial. Body 10, headers 11 bold, titles 14 bold. No other fonts.
- Numbers: valuations and dollars in $B as `#,##0.0`; very large dollars
  `#,##0`; percentages as `0.0%` and STORED AS FRACTIONS (0.476, not 47.6);
  multiples as `0.0"x"`; counts as `#,##0`; negatives in parentheses; zeros
  render as `-`. Always put the unit in the column header (`Valuation ($B)`,
  `Share (%)`, `Efficiency (x)`), never inline in the cell.
- Dates as real dates, one format throughout (`dd-mmm-yy` or `mmm yyyy` for
  period columns - pick one and hold it).
- Freeze panes so the header row and the first label column stay visible when
  scrolling.
- Banded rows for readability (light fill on alternate data rows).
- Highlight the current period: the Q2 2026 (or latest) column in every time
  series gets a distinct fill and bold, so the eye lands on "now" instantly.
- Column widths sized to content; wrap text in long description/notes columns so
  nothing is clipped; no cell content spills hidden.
- No merged cells inside any data range (a merged title block above the table is
  fine). Merged cells break sorting and reading.
- Right-align numbers, left-align text, center period headers.

## Integrity (do not skip)

- Preserve all formulas. If a value is computed, keep it as a formula pointing at
  its inputs; do not replace it with a static number while reformatting.
- Repair or clearly mark the three `#REF!` estimate columns: pull the intact
  estimates from UNI LIST if reachable, else blank the cell and note it - never
  leave a live `#REF!` in a reader file.
- After building, recalculate the workbook and confirm zero formula errors
  (no `#REF!`, `#NAME?`, `#VALUE!`). If anything errors, fix it before delivery.
- Sanity-check that reformatting did not move a number: spot-check five figures
  against the source workbook and confirm they match.

Deliver `Q2_2026_Unicorn_Tracker_READABLE.xlsx`. Start with the `Cover` and
`Highlights` tabs and show me those two before formatting the rest, so I can
confirm the headline layout reads the way I want.
