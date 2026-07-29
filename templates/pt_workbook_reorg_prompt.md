# Claude Excel prompt — reorganize the Q2 2026 Unicorn Tracker workbook for readability

Paste everything inside the fenced block below into Claude with the workbook attached.

---

```
Reorganize the attached workbook `Final__Q2_2026__Quarterly_Unicorn_Tracker_HR_Version.xlsx`
(56 sheets) into the most readable structure possible. This is a live analytical workbook
with 1,392 cross-sheet formula references — readability work must not disturb a single one.
Output a NEW file named `Q2_2026_Unicorn_Tracker_ORGANIZED.xlsx`. Do not modify the original.

=======================================================================
SECTION 0 — HARD CONSTRAINTS (violating any one of these fails the task)
=======================================================================

0.1  NEVER insert, delete, move, or shift any row or column on any sheet. Every change is
     formatting, tab order, tab colour, tab name (whitelist only), freeze panes, autofilter,
     zoom, gridlines, or writing into a cell that is currently EMPTY.

0.2  PRESERVE ALL FORMULAS. Load with openpyxl using data_only=False and save that object.
     Never save a workbook that was loaded with data_only=True — doing so silently converts
     all 1,392 formulas to static values and destroys the audit chain. If you need computed
     values for verification, open a SECOND read-only data_only=True handle purely to read.

0.3  DO NOT RENAME any sheet referenced by a formula. These 32 names are locked:
       Top Exits in Qtr, RVVC & Step Up Vertical Ranking, Aggregate unicorns,
       Unicorn market val x vertical, Uni Exits by Type, Top 10 Unicorns by PV,
       Step Up x series, Time Btwn Rnds x series, Top Deals in Qtr,
       Fallen Unicorns to Date, Active Unicorns, Unicorn down round activity,
       Rnds by Inv Count Bucket, Unicorn exit activity, MedAvg Uni Val Step Up,
       MedAvg Uni Time Between Rnds, MedAvg Uni RVVC, MedAvg Uni Time to Exit,
       Top Deals in Qtr by Val Step Up, Unicorn deal activity, AI Aggregate unicorns,
       PT-Universe, 2021 Uni Cohort, PT-Fallen, Top Investors, MedAvg Uni Post Value,
       PT-Exits, PT-Deals, Unicorn investors x Qtr, PT-StepUp-RVVC, PT-Vertical,
       MedAvg Uni Deal Size
     Renaming is permitted ONLY for the whitelist in 3.1.

0.4  DO NOT convert any range to an Excel Table / ListObject. Structured references would
     rewrite the A1-style ranges the formulas depend on.

0.5  DO NOT change any number VALUE, and do not add, remove, or rewrite any formula except
     the new hyperlink formulas explicitly requested in Section 4.

0.6  Leave the two veryHidden system sheets (PB_CACHE, PB_CACHE_JS) exactly as they are —
     still veryHidden, unrenamed, unmoved to the end of the book.

=======================================================================
SECTION 1 — THE LAYOUT FACTS YOU CAN RELY ON
=======================================================================

The 30 PitchBook-native export tabs are perfectly uniform. Every one of them:
  - rows 1-5 blank (A1 and B1 are empty on all 30 — free space for navigation)
  - row 6 = chart title, row 7 = column header, data begins row 8
  - column A is a 2.5-width cosmetic spacer; row labels live in column B
  - gridlines OFF, no freeze panes, no autofilter, zoom scattered from 55 to 114
Apply one single layout contract to all 30 rather than treating them individually.

The 11 analyst-built PT-* tabs use: row 1 title, row 2 source line, row 3 blank,
row 4 section header, content below, labels in column A (width 50).

The 9 section-audit tabs are INCONSISTENT and need normalizing (see 3.2).

=======================================================================
SECTION 2 — TARGET TAB ORDER AND COLOUR CODING
=======================================================================

Reorder to exactly this sequence, and set each tab's colour to its group colour. The colour
is what makes a 55-tab book navigable at a glance — one glance at the tab strip should tell
the reader whether they are in a control tab, a derived tab, or raw source data.

GROUP 0 · CONTROL & PROVENANCE — tab colour FFC000 (gold)
   1  SECTION BY SECTION AUDIT   -> rename per 3.1
   2  REPORT_SOURCE_MAP
   3  REPORT_AUDIT               (currently last at position 56 — promote it here)
   4  PT-CHECKS
   5  PT-GAPS
   6  PT-MAP
   7  PT-Crosswalk

GROUP 1 · SECTION-BY-SECTION AUDIT, in published report order — colour 9DC3E6 (light blue)
   8  Market Overview-5 financings
   9  Market Overview- who writes the
  10  Market Overview- three prices
  11  Market Overview- Median vs avg
  12  Market Overview- repriced quick
  13  Market Overview- AI three-fifth
  14  Verticals
  15  Business Quality
  16  Valuations and Fallen Uni

GROUP 2 · DERIVED ANALYSIS (PT-*) — colour 1F4E79 (navy)
  17  PT-Deals
  18  PT-Round-Dynamics
  19  PT-StepUp-RVVC
  20  PT-Vertical
  21  PT-Universe
  22  PT-Exits
  23  PT-Fallen

GROUP 3 · SOURCE — TRENDS & AGGREGATES — colour A9D18E (green)
  24  Aggregate unicorns
  25  AI Aggregate unicorns
  26  Unicorn deal activity
  27  Active unicorn deal activity
  28  Unicorn rounds by series
  29  Unicorn investors x Qtr
  30  Rnds by Inv Count Bucket
  31  Unicorn down round activity
  32  Unicorn exit activity
  33  Uni Exits by Type

GROUP 4 · SOURCE — MEDIANS & AVERAGES — colour C5E0B4 (pale green)
  34  MedAvg Uni Deal Size
  35  MedAvg Uni Post Value
  36  MedAvg Uni Val Step Up
  37  MedAvg Uni Time Between Rnds
  38  MedAvg Uni RVVC
  39  MedAvg Uni Time to Exit
  40  Uni med deal size x series
  41  Step Up x series
  42  Time Btwn Rnds x series

GROUP 5 · SOURCE — VERTICALS — colour F4B183 (orange)
  43  Unicorn market val x vertical
  44  RVVC & Step Up Vertical Ranking

GROUP 6 · SOURCE — COMPANY-LEVEL ROSTERS — colour BFBFBF (grey)
  45  Active Unicorns
  46  2021 Uni Cohort
  47  Top 10 Unicorns by PV
  48  Top Deals in Qtr
  49  Top Deals in Qtr by Val Step Up
  50  Top Exits in Qtr
  51  Uni Exits to Date
  52  Fallen Unicorns to Date
  53  Top Investors

GROUP 7 · SYSTEM — no colour, stays veryHidden, last
  54  PB_CACHE_JS
  55  PB_CACHE

DELETE `Sheet2` (position 14) — it is a single empty cell sitting in the middle of the PT
block. Confirm it is empty and unreferenced before deleting; if either check fails, keep it
and move it to Group 7 instead.

Final visible count must be 53, total 55.

=======================================================================
SECTION 3 — RENAMES AND HEADER NORMALIZATION
=======================================================================

3.1  Rename ONLY these 10 tabs. All are unreferenced by any formula, so the renames are safe.
     Three are truncated mid-word at the 31-char limit; the rest gain report-order prefixes.
       SECTION BY SECTION AUDIT         -> 0 START HERE
       Market Overview-5 financings     -> 1a Five financings
       Market Overview- who writes the  -> 1b Who writes the checks
       Market Overview- three prices    -> 1c Three prices
       Market Overview- Median vs avg   -> 1d Median vs average
       Market Overview- repriced quick  -> 1e Repriced quickly
       Market Overview- AI three-fifth  -> 1f AI three-fifths and exits
       Verticals                        -> 2 Verticals
       Business Quality                 -> 3 Business quality
       Valuations and Fallen Uni        -> 4 Valuations and fallen
     Verify each new name is <=31 chars and free of : \ / ? * [ ].

3.2  Normalize the 9 section-audit tabs to one shape. They currently disagree on both header
     row and column schema: tabs 1a/1b/1c put headers in row 2 with 6 columns
     (Figure | File | Tab | Cell | Calculation | Source), while 1e/1f/2/3/4 put headers in
     row 1 with 4 columns (Figure | File / Tab / Cell | How calculated | Source), and 1c/1d
     have prose in the header row instead of headers.
     Because rows cannot be inserted (0.1), do NOT try to move headers. Instead:
       - Bold + white text on 1F4E79 fill on whichever row is that tab's header row.
       - Freeze the row immediately below the header row.
       - Where a Figure row has blank File/Tab/Cell cells because the value continues from
         the row above (e.g. 1a rows 4-5, Verticals rows 3-6), fill the blank cells with
         "(as above)" in italic grey 808080. Writing into empty cells is permitted; this
         removes the single biggest source of misreading in these tabs.
       - Wrap text on the Calculation / How-calculated column, width 42, vertical align top.

3.3  On every one of the 30 native tabs, write a back-link into the empty cell B1:
       =HYPERLINK("#'0 START HERE'!A1","<< back to contents")
     Style it 9pt italic, font colour 1F4E79. Do the same in the first empty cell of row 1
     on the PT-* and control tabs (use C1 there, since column A holds long labels).

=======================================================================
SECTION 4 — REBUILD THE CONTENTS TAB
=======================================================================

`0 START HERE` currently holds only a 10-row plain-text list of the 9 report sections with
no hyperlinks and no coverage of the other 46 tabs. Rebuild it as a real index. Writing here
is unrestricted — nothing references this tab.

Layout: title in A1, generated-on note in A2, header row in A4, one row per visible sheet
from A5 down, in the Section 2 order. Columns:
   A  Group          (e.g. "0 · Control", "3 · Source — trends")
   B  Tab            =HYPERLINK("#'<tab>'!A1","<tab>")  — clickable
   C  What it holds  one plain-English line, e.g. for Aggregate unicorns:
                     "Active count + aggregate post-money value by year 2016-2026 and by
                      quarter; M8=1,743 count and M9=$8,232.5B are the headline universe."
   D  Layer          Control / Derived / Source
   E  Size           "1,746 x 17" style
   F  Locked name?   "Yes - formula-referenced" for the 32 in 0.3, else "Safe to rename"
   G  Header row     "6-7, data from 8" for native tabs; "4" for PT-*; per-tab for audit tabs

Freeze at A5. Autofilter A4:G57. Column widths A 18, B 32, C 72 (wrap), D 10, E 12, F 24,
G 20. Bold white-on-1F4E79 header row. Band the rows by group using the Section 2 group
colours at 25% tint in column A only, so the tab strip and the index use the same colour
language.

Add a legend block below the table explaining the seven tab colours, and a three-line
"How to read this book" note: control tabs prove the numbers, PT-* tabs derive them, source
tabs hold the raw PitchBook extract; every figure in the published report traces
report -> REPORT_SOURCE_MAP -> a PT-* tab -> a source tab cell.

=======================================================================
SECTION 5 — READABILITY CONTRACT FOR THE 30 NATIVE TABS
=======================================================================

Apply uniformly to all 30 (they share the row-6-title / row-7-header / data-row-8 layout):

5.1  FREEZE PANES — the single highest-value fix in this workbook. None of the 30 currently
     freeze anything, and the time-series tabs run 44-46 columns wide to AT, so scrolling
     right loses the row label and scrolling down loses the year header.
       - Time-series and summary tabs (labels in column B): freeze C8.
       - Roster tabs where column C is the company name (Active Unicorns, 2021 Uni Cohort,
         Top Deals in Qtr, Top Deals in Qtr by Val Step Up, Top Exits in Qtr,
         Uni Exits to Date, Fallen Unicorns to Date, Top 10 Unicorns by PV): freeze D8.
       - Top Investors: freeze C8.

5.2  HEADER STYLING — row 7 across the used range: bold, white text, 1F4E79 fill, wrap text,
     centre, row height 30. Row 6 title: bold 12pt, colour 1F4E79, no fill.

5.3  AUTOFILTER — apply to the 9 roster tabs listed in Group 6 only, anchored on row 7 and
     spanning the used range (e.g. Active Unicorns B7:Q1746). Do NOT filter the time-series
     or MedAvg tabs; they are pivot-shaped and a filter there is a footgun.

5.4  ZOOM AND GRIDLINES — set zoomScale to 100 on every tab (currently 55-114, wildly
     inconsistent). Turn gridlines ON for all source and PT-* tabs — they are currently off
     with no banding or borders, which makes wide rows very hard to track. Keep gridlines OFF
     on the Group 0 and Group 1 tabs, which read as documents.

5.5  BANDED ROWS — on the 9 roster tabs, apply a light F2F2F2 fill to every other data row
     across the used range. Do this with static fills, not a Table.

5.6  UNMERGE THE YEAR BANDS — `RVVC & Step Up Vertical Ranking` merges C7:G7 as "2025" and
     H7:L7 as "2026" over two repeated 5-column blocks, so a reader in column J cannot tell
     which year they are in. This is the most confusing layout in the book. Unmerge both,
     then write the year into each of the 10 header cells in row 8 as a prefix, so C8 reads
     "2025 Deal Count", D8 "2025 Avg RVVC", ... H8 "2026 Deal Count", J8 "2026 Median RVVC",
     etc. Row 8 currently holds the bare labels and is a header row, not data — data starts
     row 9 — so this is an in-place text edit of existing header cells, permitted under 0.1.
     Do the identical treatment on `Aggregate unicorns` row 44, which merges eight 4-column
     blocks (G44:J44, K44:N44, O44:R44, S44:V44, W44:Z44, AA44:AD44, AE44:AH44, AM44:AP44).

=======================================================================
SECTION 6 — NUMBER FORMAT DICTIONARY
=======================================================================

Formatting is currently half-applied: `Unicorn market val x vertical` has 26 formatted and
26 General numeric cells side by side, so $6.44T prints as 6.444788583990342 next to a
properly formatted neighbour. `RVVC & Step Up Vertical Ranking` has 152 numeric cells and
ZERO number formats. `Aggregate unicorns` is 161 General vs 75 formatted. Normalize:

   Company / deal counts .................. #,##0
   Values in $ millions ................... $#,##0
   Values in $ billions ................... $#,##0.0
   Values already scaled to $ trillions
     (col D of Unicorn market val x vertical) .. $#,##0.00"T"
   Valuation step-up multiples ............ 0.00"x"
   Time between rounds / time to exit ..... 0.00" yr"
   Share / percentage cells ............... 0.0%
   Dates .................................. yyyy-mm-dd
   RVVC ................................... 0.00   <-- see 6.1
   Text-in-numeric-column placeholders .... leave as General

6.1  RVVC TRAP — do not apply a percent format to RVVC. The source headers read
     "Avg RVVC (%)" and "Median RVVC (%)" but the stored values are ratios: AI 2026 median
     RVVC is 1.8368, which the published report prints as 1.84, not 183.7%. Format RVVC as
     0.00 and append " (ratio, not %)" to the RVVC header text so the mislabelled source
     header stops misleading readers. This applies to
     `RVVC & Step Up Vertical Ranking` columns D/E/J/K and `MedAvg Uni RVVC` rows 8-9.

6.2  Right-align all numerics, left-align all text, centre all date columns. Autofit every
     column to its content with a 10-char floor and 45-char ceiling; force wrap + width 45
     on the long-prose columns (Company Description on Top Deals in Qtr column E, Investors
     column J, and the Calculation columns on the audit tabs).

6.3  On REPORT_AUDIT, conditionally format column F: green fill C6EFCE for "Y", red fill
     FFC7CE for anything else, so a failed audit row is visible without reading. Do the same
     on PT-CHECKS column D for PASS / FAIL.

=======================================================================
SECTION 7 — VERIFICATION GATE (report the result of every check)
=======================================================================

Re-open the saved file and assert, printing a PASS/FAIL table:

 7.1  Sheet count = 55; visible = 53; PB_CACHE and PB_CACHE_JS still veryHidden.
 7.2  All 32 locked names from 0.3 still present, character-for-character.
 7.3  Total formula count = 1,392, and the per-sheet counts still match:
      REPORT_AUDIT 305, PT-Exits 290, PT-StepUp-RVVC 217, PT-Round-Dynamics 217,
      PT-Universe 131, PT-Vertical 57, PT-Fallen 43, PT-Deals 40, PT-CHECKS 33,
      REPORT_SOURCE_MAP 32, PT-MAP 17, PT-Crosswalk 9, Market Overview- repriced quick 5,
      Verticals 2, Unicorn down round activity 2, Unicorn deal activity 2,
      Valuations and Fallen Uni 1, Unicorn market val x vertical 1
      (the two renamed tabs in that list keep their counts under their new names).
      A count that DROPS means constraint 0.2 was violated — stop and re-do.
 7.4  Anchor values unchanged, read via a separate data_only handle:
        Aggregate unicorns          M8 = 1743          M9 = 8232.5063
        AI Aggregate unicorns       M8 = 702           M9 = 5076.4207
        Unicorn market val x vert.  C8 = 968           D8 = 6.4448
        RVVC & Step Up Vert. Rank.  J9 = 1.8368        L9 = 2.3684
        Top Exits in Qtr            G8 = 1690.2418
        PT-Exits                    B22 = 420.6574
        PT-Fallen                   B5  = 245
        PT-Deals                    C14 = 0.6244
        Top 10 Unicorns by PV       SUM(F8:F17) = 2886.65
 7.5  Every visible sheet has: a tab colour from the Section 2 palette, freeze panes set,
      zoomScale 100, and a working back-link in row 1.
 7.6  Every hyperlink on `0 START HERE` resolves to an existing sheet name.
 7.7  Zero Excel Tables exist in the workbook (constraint 0.4).

Then give me a short written summary: what moved, what was renamed, what was reformatted,
and anything you chose not to do because a constraint blocked it.
```

---

## Why the prompt is shaped this way

Findings from the scan of the attached file that drove each section:

| Observation | Prompt section |
|---|---|
| 1,392 cross-sheet formula refs; 32 sheets referenced by name | 0.3 lock list, 7.2, 7.3 |
| 1,024 formulas live on the PT-* and audit tabs; a `data_only=True` save would flatten all of them | 0.2, 7.3 |
| 56 tabs, three provenance layers, no visual separation, `REPORT_AUDIT` stranded at position 56 | Section 2 |
| `Sheet2` (1 empty cell) sits at position 14, mid-PT-block | Section 2 delete step |
| Zero freeze panes on all 30 native tabs, which run to column AT | 5.1 |
| Freeze panes on PT-* tabs set at cursor position, not headers (`PT-Vertical` at A58, below its 40 used rows) | 5.1, 3.2 |
| Zoom ranges 55–114 across tabs; gridlines off with no banding | 5.4, 5.5 |
| `RVVC & Step Up` merges C7:G7 "2025" / H7:L7 "2026" over repeated 5-col blocks; 152 numeric cells with zero formats | 5.6, 6.0 |
| `Unicorn market val x vertical`: 26 formatted vs 26 General numeric cells | Section 6 |
| Source headers say "RVVC (%)" but store ratios (1.8368 → report prints 1.84) | 6.1 |
| 9 section-audit tabs disagree on header row (1 vs 2) and schema (4 vs 6 cols); sparse fill-down | 3.2 |
| 3 tab names truncated mid-word at 31 chars | 3.1 |
| TOC is 10 rows of plain text, no hyperlinks, covers 9 of 56 tabs | Section 4 |
| All 30 native tabs uniform (rows 1–5 blank, row 6 title, row 7 header, data row 8, col A spacer 2.5) | Section 1, Section 5 |
| A1/B1 empty on all 30 native tabs | 3.3 back-links |
