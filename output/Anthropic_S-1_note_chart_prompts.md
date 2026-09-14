# Claude for Excel prompts: charts for "Q3 2026 Anthropic: what to look for in the S-1"

Prepared September 14, 2026. Paste each prompt into Claude for Excel with the target workbook open. Prompt 0 builds the workbook shell; Prompts 1 to 4 build the four charts the note references; Prompt 5 is optional (the note's metadata says "Chart count: 5" but the draft carries four CHART placeholders).

Conventions used in every prompt
- Palette (the desk's house palette from the Databricks note build; swap for the PitchBook chart template if editorial requires): Navy `#1F2A44`, Slate `#35506E`, Green `#1C5D46`, Grey `#6B7280`, Soft grey `#F2F5F9`, Warn red `#8F3421`, Ink `#2B3446`, gridline `#E4E9F0`.
- Chart size 6.5" wide by 3.9" tall, no chart border, white background, light horizontal gridlines only, legend below the plot, title bold navy 12 pt, subtitle grey 9 pt, source line italic grey 8 pt.
- Every data block carries a Source column so the "File / Tab / Cell" fields on the landing-page comment can be filled from the workbook.
- Figures are labelled by status: company-stated, reported (press), or computed (from the note's own assumptions). Nothing here is estimated by the workbook.

---

## Prompt 0: workbook shell

```
Set up this workbook for a PitchBook analyst note on Anthropic (chart as-of date: [fill in]).

1. Create these sheets in order and delete any default sheet: README, 1_RunRate, 2_AIBQ, 3_GrossProfit, 4_Sensitivity, 5_Multiple.
2. On README, put in A1 "Q3 2026 Anthropic: what to look for in the S-1 (chart workbook)", A2 "Chart as-of date:", B2 blank for me to fill, A3 "Geography: US", A4 "Author: Harrison Rolfes". In A6:B13 list the house palette as name/hex pairs: Navy #1F2A44, Slate #35506E, Green #1C5D46, Grey #6B7280, Soft #F2F5F9, Warn #8F3421, Ink #2B3446, Gridline #E4E9F0. Fill each B cell with its own color.
3. On every chart sheet, reserve A1:F20 for the data block and place the chart with its top-left corner at H2. Freeze nothing, no gridlines shown on the sheet (View > Gridlines off).
4. Use Calibri 10 for data blocks. Bold header rows. Number formats: $B figures as 0.0, percentages as 0%, multiples as 0.0"x".
Do not build any charts yet; I will give you one chart per prompt.
```

---

## Prompt 1: run-rate revenue, December 2025 to July 2026 (column chart)

Note reference: "CHART: Anthropic's run rate revenue from December 2025 to July 2026". Caption in the note: run rate has risen from about $9 billion to more than $65 billion in seven months.

```
On sheet 1_RunRate build a column chart of Anthropic's disclosed annualized run-rate revenue, December 2025 to July 2026.

Data block, A1:E10, headers in row 1: Month | Run-rate revenue ($B) | Disclosure date | Status | Source
Dec 2025 | 9 | Apr 6, 2026 | Company-stated, approximate ("approximately $9 billion at the end of 2025") | Anthropic, Google/Broadcom compute announcement, Apr 6, 2026; restated by Bloomberg via TechCrunch, Aug 17, 2026
Jan 2026 | (leave blank) | n/a | No disclosure found | n/a
Feb 2026 | 14 | Feb 12, 2026 | Company-stated | Anthropic, Series G release, Feb 12, 2026
Mar 2026 | 19 | Mar 3, 2026 | Reported (press); later cited by CEO | Bloomberg, "Anthropic Nears $20 Billion Revenue Run Rate", Mar 3, 2026; Amodei remarks reported by VentureBeat, May 8, 2026
Apr 2026 | 30 | Apr 6, 2026 | Company-stated | Anthropic, Apr 6, 2026 ("run-rate revenue has now surpassed $30 billion")
May 2026 | 47 | May 28, 2026 | Company-stated ("crossed $47 billion earlier this month") | Anthropic, Series H release, May 28, 2026
Jun 2026 | (leave blank) | n/a | No disclosure found | n/a
Jul 2026 | 65 | Aug 17, 2026 | Reported (press, citing investor update) | Bloomberg, Aug 17, 2026, as carried by TechCrunch, CNBC and Reuters ("surpassed $65 billion at the end of July")

Chart spec:
- Clustered column, one series (B2:B9), categories A2:A9. Show empty cells as gaps so Jan and Jun appear as labelled gaps on the axis, not zeros.
- Fill: Navy #1F2A44 for all columns; make the Jul 2026 column Green #1C5D46.
- Data labels above each column, format $0"B" (so they read $9B, $14B, ... $65B), 9 pt, Ink #2B3446, bold on the Jul 2026 label.
- Y axis: 0 to 70, major unit 10, number format $0"B", no axis title; light horizontal gridlines #E4E9F0; no vertical gridlines. X axis labels 9 pt grey. Gap width 60%.
- Title (bold navy 12 pt, left-aligned), matching the note's placeholder: "Anthropic's run-rate revenue from December 2025 to July 2026"
- Subtitle as a text box under the title (grey 9 pt): "Annualized run-rate revenue ($B) at each disclosure: from about $9B to more than $65B in seven months. No disclosure found for Jan or Jun 2026."
- Source line as a text box at the bottom of the chart (italic grey 8 pt): "Source: Anthropic company releases (Feb 12, Apr 6, May 28, 2026); Bloomberg (Mar 3 and Aug 17, 2026) as carried by TechCrunch, CNBC and Reuters. Run rate is the latest month's revenue annualized."
- Chart size 6.5" x 3.9", no border, no legend, anchored at H2.
Then tell me the chart's sheet and anchor cell so I can cite File / Tab / Cell.
```

---

## Prompt 2: AIBQ score (radar chart)

Note reference: "CHART: AIBQ Score". The composite is weighted, not a simple mean: 0.20 x 5.9 + 0.25 x 7.1 + 0.15 x 4.5 + 0.20 x 6.2 + 0.20 x 7.5 = 6.37 (a simple average would be 6.24). The weights are shown on the axis labels so a reader can reproduce the composite from the chart.

```
On sheet 2_AIBQ build a radar chart of Anthropic's AIBQ dimension scores.

Data block, A1:E7, headers in row 1: Dimension (weight) | Anthropic score | Weight | Contribution | Composite reference
Capital efficiency (20%) | 5.9 | 20% | =B2*C2 | 6.37
Revenue quality (25%) | 7.1 | 25% | =B3*C3 | 6.37
Compute independence (15%) | 4.5 | 15% | =B4*C4 | 6.37
Governance optionality (20%) | 6.2 | 20% | =B5*C5 | 6.37
Moat durability (20%) | 7.5 | 20% | =B6*C6 | 6.37
Row 7: A7 "Composite (weighted)", D7 =SUM(D2:D6) formatted 0.00 (it must show 6.37). A8 "Simple mean (not used)", B8 =AVERAGE(B2:B6) formatted 0.00.
A10 "Source: desk AIBQ framework, September 2026 score. Composite = 0.20 CE + 0.25 RQ + 0.15 CI + 0.20 GO + 0.20 MD, minus contextual risk adjustment (zero here). Bands: Elite 8.50+, Strong 7.00-8.49, Developing 4.50-6.99."

Chart spec:
- Radar chart (Excel "Radar with Markers"), categories A2:A6, in this clockwise order starting at the top: Capital efficiency, Revenue quality, Compute independence, Governance optionality, Moat durability.
- Series 1 "Anthropic (6.37 composite)" = B2:B6: line Green #1C5D46, 2.25 pt, circle markers size 6 in the same green. If you can set a fill, use the Filled Radar type for this series with Green at 80% transparency; if a per-series fill is not possible, keep it as a line radar.
- Series 2 "Composite reference (6.37)" = E2:E6: line Grey #6B7280, 1.25 pt, dashed, no markers. This draws the flat 6.37 pentagon so the reader sees which dimensions sit above or below the composite.
- Data labels on Series 1 only, value with one decimal, 9 pt bold green, positioned outside the line.
- Radial axis: minimum 0, maximum 10, major unit 2, labels 8 pt light grey (#B4BCC9); gridlines #E4E9F0. Category labels 9 pt Ink #2B3446.
- Legend below the plot, no legend border.
- Title (bold navy 12 pt, left-aligned): "Anthropic AIBQ score: 6.37 out of 10" (the note's placeholder reads "AIBQ Score"; if editorial wants a statement title, use "Revenue quality and moat lead; compute independence is the constraint")
- Subtitle text box (grey 9 pt): "AIBQ dimension scores (0-10, weights in parentheses), September 2026. Composite is weighted; a simple average would be 6.24."
- Source text box (italic grey 8 pt): "Source: desk AIBQ framework. Score is the analyst's; not externally verifiable by construction."
- Chart size 6.5" x 3.9", no border, anchored at H2.
Confirm D7 shows 6.37 before you finish.
```

Optional overlay (only if the note wants a cohort comparison; note the dates differ): add a third series "Databricks (8.81, Jul 2026)" with values 8.9, 9.0, 8.0, 8.9, 9.0 in F2:F6 as a Navy dashed line, and change the subtitle to say the Databricks scores are from the desk's July 2026 initiation.

---

## Prompt 3: $2T equals roughly 70x annualized gross profit (combo chart)

Note reference: "CHART: At a 44% gross margin, $2T equals roughly 70x annualized gross profit". All figures are computed from the note's own inputs: $65B run rate and a 44% gross-margin estimate. The chart flexes the margin so the reader sees how much margin expansion it takes to bring the multiple down.

```
On sheet 3_GrossProfit build a combination chart showing annualized gross profit and the implied $2T-to-gross-profit multiple across gross-margin assumptions.

Inputs, A1:B3: A1 "Run-rate revenue ($B)", B1 65; A2 "Valuation ($B)", B2 2000; A3 "Base-case gross margin", B3 44%.
Data block, A5:E10, headers in row 5: Gross margin | Annualized gross profit ($B) | $2T / gross profit (x) | $2T / revenue (x) | Case
Rows 6-10: gross margin 40%, 44%, 50%, 55%, 60%.
B = $B$1*A (gross profit), C = $B$2/B (multiple), D = $B$2/$B$1 (30.8x on every row, for the reference line), E = "Base case" on the 44% row, otherwise blank.
Expected values: 40% -> 26.0 / 76.9x; 44% -> 28.6 / 69.9x; 50% -> 32.5 / 61.5x; 55% -> 35.8 / 55.9x; 60% -> 39.0 / 51.3x.
A12 "Source: run rate per Bloomberg, Aug 17, 2026; 44% gross margin is the analyst's estimate; other margins are illustrative. Net presentation of cloud-partner sales (a 6%-10% revenue reduction) would raise the revenue multiple to roughly 32.7x-34.2x."

Chart spec:
- Combo chart. Series 1 "Annualized gross profit ($B)" = B6:B10 as clustered columns on the primary axis, fill Slate #35506E, with the 44% column recolored Green #1C5D46. Data labels above columns, format $0.0"B", 9 pt.
- Series 2 "$2T / gross profit (x)" = C6:C10 as a line with markers on the secondary axis, line Warn #8F3421 2 pt, circle markers size 6, data labels above points format 0"x", 9 pt bold in the same red; bold the 44% label and add the word "base" to it if labels can be edited (otherwise leave the value).
- Series 3 "$2T / revenue (30.8x)" = D6:D10 as a dashed grey line (#6B7280, 1.25 pt, no markers) on the secondary axis, so the gap between the revenue multiple and the gross-profit multiple is visible.
- Categories = A6:A10 formatted 0%. Primary Y axis 0 to 45, major unit 15, format $0"B"; secondary Y axis 0 to 90, major unit 30, format 0"x". Light horizontal gridlines from the primary axis only. Gap width 80%.
- Legend below the plot.
- Title (bold navy 12 pt), matching the note's placeholder: "At a 44% gross margin, $2T equals roughly 70x annualized gross profit"
- Subtitle text box (grey 9 pt): "Annualized gross profit on a $65B run rate and the implied $2T multiple, by gross-margin assumption. Model-training expense sits below gross profit."
- Source text box (italic grey 8 pt): use the text in A12.
- Chart size 6.5" x 3.9", no border, anchored at H2.
Verify C7 (44% row) rounds to 70x before finishing.
```

---

## Prompt 4: $2T requires both high margins and a premium 2028 multiple (clustered columns with target line)

Note reference: "CHART: $2T requires both high margins and a premium 2028 multiple". Inputs are the note's: $195B 2028 revenue midpoint, FCF margins of 25% to 35%, FCF multiples of 30x to 40x, discounted at 10% for 2.3 years (discount factor 0.803). The note's $1.37T-$1.64T central range is the 25%-30% margin pair at 35x.

```
On sheet 4_Sensitivity build a clustered column chart of the present value today of Anthropic under 2028 free-cash-flow margin and multiple assumptions, with a $2T target line.

Inputs, A1:B5: A1 "2028 revenue ($B)", B1 195; A2 "Discount rate", B2 10%; A3 "Years to 2028", B3 2.3; A4 "Discount factor", B4 =(1+B2)^-B3 (should show 0.803); A5 "Target valuation ($T)", B5 2.0.
Data block, A7:E10, headers in row 7: FCF margin | 30x | 35x | 40x | $2T target
Rows 8-10: margins 25%, 30%, 35%. Each cell = $B$1*margin*multiple*$B$4/1000, formatted $0.00"T". Column E = $B$5 on every row.
Expected values ($T): 25%: 1.17 / 1.37 / 1.57; 30%: 1.41 / 1.64 / 1.88; 35%: 1.64 / 1.92 / 2.19. Only the 35%-margin, 40x cell clears $2T.
Break-even block, A12:C14: A12 "FCF margin needed for $2T", B12 "at $195B", C12 "at $200B"; row 13 "35x": B13 =B5*1000/(35*B4)/B1, C13 =B5*1000/(35*B4)/200; row 14 "40x": B14 =B5*1000/(40*B4)/B1, C14 =B5*1000/(40*B4)/200; format 0.0%. Expected: 36.5% / 35.6% at 35x and 31.9% / 31.1% at 40x.
A16 "Source: 2028 revenue forecast of $190B-$200B as reported by The Information (2026); margins, multiples and discounting are the analyst's assumptions."

Chart spec:
- Clustered columns: categories A8:A10 (formatted 0%), three series 30x, 35x, 40x from B8:D10, fills Slate #35506E, Navy #1F2A44, Green #1C5D46 respectively. Data labels above every column, format $0.00"T", 8 pt. Gap width 60%, overlap -10%.
- Add series E8:E10 "$2T IPO valuation" as a line with no markers, Warn #8F3421, 1.5 pt dashed, and put one data label on its last point reading "$2T". The line will run from the first to the last category center; that is acceptable. If a full-width line is required, draw it instead as a dashed line shape at the $2.0T gridline and add a text box "$2T IPO valuation" at its right end.
- Y axis 0 to 2.5, major unit 0.5, format $0.0"T"; light horizontal gridlines only.
- Legend below the plot in the order 30x, 35x, 40x, $2T IPO valuation.
- Title (bold navy 12 pt), matching the note's placeholder: "$2T requires both high margins and a premium 2028 multiple"
- Subtitle text box (grey 9 pt): "Present value today ($T) at $195B of 2028 revenue, by FCF margin and FCF multiple; discounted at 10% for 2.3 years. Central case: 25%-30% margin at 35x = $1.37T-$1.64T."
- Source text box (italic grey 8 pt): use the text in A16.
- Chart size 6.5" x 3.9", no border, anchored at H2.
Check that C9 shows $1.64T and D9 shows $1.88T; those two figures appear in the note's text.
```

---

## Prompt 5 (optional): Series H to IPO, valuation is rising faster than revenue

Not referenced by a placeholder in the draft; use it only if the fifth chart slot in the metadata is real. It illustrates the paragraph on multiple expansion (20.5x at Series H to 30.8x at $2T).

```
On sheet 5_Multiple build a small bar chart comparing the change in Anthropic's run rate, valuation and revenue multiple between the May 2026 Series H and a $2T IPO.

Data block, A1:D4, headers in row 1: Metric | Series H (May 2026) | $2T IPO case (Jul 2026 run rate) | Change
Run-rate revenue ($B) | 47 | 65 | =C2/B2-1
Valuation ($B) | 965 | 2000 | =C3/B3-1
Revenue multiple (x) | =B3/B2 | =C3/C2 | =C4/B4-1
Expected: 20.5x and 30.8x; changes +38%, +107%, +50%.
A6 "Source: Anthropic Series H release, May 28, 2026 ($965B post-money; run rate crossed $47B earlier that month); Bloomberg, Aug 17, 2026 ($65B run rate at end of July); $2T is the reported IPO valuation target (Sep 11, 2026 reports of Nvidia anchor talks)."

Chart spec:
- Horizontal bar chart of D2:D4 (categories A2:A4), fills Slate #35506E for run rate, Warn #8F3421 for valuation, Navy #1F2A44 for multiple. Data labels at outside end formatted +0%. X axis hidden; no gridlines; gap width 50%.
- Title (bold navy 12 pt): "From Series H to $2T, the valuation is rising nearly three times as fast as revenue"
- Subtitle text box (grey 9 pt): "Change from the May 2026 Series H mark to a $2T valuation on the July 2026 run rate."
- Source text box (italic grey 8 pt): use A6.
- Chart size 6.5" x 2.6", no border, no legend, anchored at H2.
```

---

## Provenance summary for the chart data

| Figure | Value | Status | Source (opened and checked Sep 14, 2026) |
|---|---|---|---|
| Run rate, end-2025 | ~$9B | Company-stated, approximate | Anthropic announcement, Apr 6, 2026; TechCrunch (Bloomberg), Aug 17, 2026 |
| Run rate, Feb 2026 | $14B | Company-stated | Anthropic Series G release, Feb 12, 2026 |
| Run rate, Mar 2026 | $19B | Reported (press); CEO later cited "$19 billion in March" | Bloomberg, Mar 3, 2026; VentureBeat, May 8, 2026 |
| Run rate, Apr 2026 | $30B | Company-stated | Anthropic, Apr 6, 2026; VentureBeat, May 8, 2026 |
| Run rate, May 2026 | $47B | Company-stated | Anthropic Series H release, May 28, 2026 |
| Run rate, Jul 2026 | $65B | Reported (press, citing investor update) | Bloomberg, Aug 17, 2026, via TechCrunch; also CNBC, Reuters same day |
| Jan and Jun 2026 | none | No disclosure found | n/a; shown as gaps |
| AIBQ dimension scores | 5.9 / 7.1 / 4.5 / 6.2 / 7.5 | Analyst's framework | Note's AIBQ table; weights from the desk framework (Databricks note, Jul 2026) |
| 44% gross margin, 2028 revenue $190B-$200B, 10% discount, 2.3 years | as stated | Analyst's assumptions / reported forecast | Note text; The Information (2026) for the 2028 forecast |
| Series H mark and $2T target | $965B; $2T | Company-stated; reported | Anthropic Series H release; Sep 11, 2026 press reports |
