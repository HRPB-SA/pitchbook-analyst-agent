# Q2 2026 - Excel build & provenance manual

How to organize the data so every number in the analysis traces to a named
source. For each destination tab: the source FILE, the source SHEET, the exact
COLUMNS, and the extraction STEPS. Column letters are the real spreadsheet
letters (column A is blank in most Monitor sheets; data starts at B).

## Files (short codes) and as-of

- **B** = Morningstar PitchBook Unicorn 20 Valuations and Pricing Data
  (3607983d). Daily MODEL valuations; used at the 6/30/2026 Q2 close (file
  extends to 7/15/2026).
- **C** = Unicorn Monitor Q2 2026 lighter (bc89fe92). Universe, verticals,
  indexes, secondaries, to 6/30/2026 (history snapshot 6/22).
- (File A, Unicorn 20 Pricing Data, is redundant - a pricing-only subset of B.
  Do not use.)

Universe figures are on the Monitor basis (1,556 active / $8,496.6B). Everything
is as of 6/30/2026 (model marks pulled at the 6/30 row; 6/22 is only the history
snapshot date). Single as-of.

## Step 0 - set up the consolidation and the join key

The three-way price comparison joins B (model) to C (round + secondary), so put
both in one workbook first.

1. In file B, sheet `Historical Valuations`: row 3 holds company-name headers
   (columns C onward: Anduril, Anthropic, Anysphere ...); column B holds the
   date; the LAST data row is 7/15/2026. Copy the 20 latest values (the last
   row, columns C:X) and their headers. Paste as VALUES into file C on a new tab
   `HELP_Model` (one row per company: name | model $B).
2. Build a name-map on `HELP_Model`: the Monitor secondary sheet calls Anysphere
   "Cursor", Figure AI "Figure", and SpaceX by its long share-class name. Add a
   column `MonitorName` so joins resolve.
3. The universal join key is the **PitchBook ID**. Pull it in the next step and
   carry it on every tab so nothing joins by name alone.

## Tab 1 - `Top20_Marks` (the fresh / round / secondary centerpiece)

Feeds analysis: "The top of the market" and "estimate integrity".

- **Col A Company**: the 20 canonical names.
- **Col B PBID** (join key): from **C** sheet `Secondary Markets`, constituent
  block rows 3-22, `ConstituentName` = col **F**, `pitchbook_id` = col **G**.
  MATCH company (via MonitorName) in F, return G.
- **Col C Model $B**: from `HELP_Model` (originally **B** `Historical
  Valuations`, last row 7/15/2026). VLOOKUP by name. Already in $B.
- **Col D Round $B**: from **C** sheet `Global Unicorn History`. Columns:
  `Date` (snapshot) = **F**, `UnicornRoundDate` = **G**, `ThirdPartyId` (company
  PBID) = **H**, `Post_Money_Valuation` = **I** (in $M). Steps: filter to the
  latest snapshot (F = 6/22/2026), then INDEX/MATCH `Post_Money` (I) on
  `ThirdPartyId` (H) = col B PBID. Divide by 1000 for $B.
- **Col E Secondary $B**: from **C** `Secondary Markets`, `Market Value ($M)` =
  col **N**, for the constituent (match PBID in G, return N). Divide by 1000.
  (N = secondary price [col J] x shares outstanding [col K], i.e. implied
  company value.)
- **Col F model/round gap** = C/D - 1. **Col G secondary/round** = E/D - 1.
  **Col H secondary/model** = E/C - 1.
- **Provenance header** (row 2): label each column with its file+sheet+column,
  e.g. D = "C!Global Unicorn History col I / 1000".
- **Flags**: SpaceX has no round mark in history (IPO/exit); Cerebras round mark
  is missing (IPO'd Q2). Mark both "n/a" and note.
- Read-outs it produces: model +15.1% over round in aggregate; secondary 7-32%
  below model for megacaps (widest SpaceX -32%, Anthropic -22% at the 6/30 close);
  up-round pressure mid-cap; repricing bottom-tier.

## Tab 2 - `Top20_Performance` (value creation, YTD)

Feeds: "Value creation at the top".

- Source: **B** `Historical Valuations` (per-name daily $B).
- **Latest $B**: last row (7/15/2026) under each name's column.
- **Jan-2026 $B**: the row dated 2026-01-01 (or first trading row of 2026).
- **Inception $B**: the first non-blank value in each name's column (index start
  3/23/2021).
- **YTD %** = Latest / Jan-2026 - 1. **Since-inception $ created** = Latest -
  Inception.
- Steps: use INDEX/MATCH on the date column (B) for the three rows, then compute.
- Read-outs: Anthropic+SpaceX = 65.7% of the 20; top 3 = 82.9%; YTD spread
  +600% (Cerebras) to -22% (Ripple); note Perplexity read -12%, not the
  +752% a corrupt 1/1/2026 holiday row implied.

## Tab 3 - `Universe_TS` (aggregate, top-10 share, formation)

Feeds: "The quarter that belonged to five companies", "Where value sits",
"Latest valuation".

- Source: **C** sheet `Overview Global`.
  - Annual block: row 6 = year headers (col C = Q4-2014 ... col O = 2026);
    row 7 = Active count; row 8 = Aggregate ($B); row 9 = Aggregate top-10 ($B);
    row 10 = New unicorn count.
  - Quarterly block: row 16 = quarter headers (to col AW = Q2 2026); row 17
    Active; row 18 Aggregate; row 19 Top-10; row 20 New.
- Steps: link the annual rows into a clean table; compute **Top-10 share** =
  row9 / row8 per year. Add an `ex-SpaceX` column for the latest period if
  needed (subtract SpaceX's mark).
- Read-outs: top-10 share 49.8% (2014) -> 18.3% (2023) -> 47.8% (Q2'26);
  aggregate $8,496.6B; new formation 618 (2021) -> 107 (H1'26).

## Tab 4 - `AI_Share`

Feeds: "AI: one-third of count, nearly half of value".

- Source: **C** sheet `Vertical MV and Count` (rows 3-18: col B index name, col
  C unicorn count, col D latest post-money $B). AI row = 430 / $4,143.7B.
- Universe totals from Tab 3 (1,556 / $8,496.6B).
- Steps: **count share** = AI count / universe count; **value share** = AI value
  / universe value. For within-AI concentration, take OpenAI + Anthropic model
  marks from Tab 1 and divide by the AI value.
- Cross-basis flag: this AI value is the AI-vertical index total; it differs
  from any all-ever or primary-tracker basis. State it.

## Tab 5 - `Vertical_Size`

Feeds: "SaaS and AI dominance", "the narrow investable universe".

- Source: **C** `Vertical MV and Count` (col B name, C count, D $B) for the
  ranked size table.
- For unique/dedup counts: **C** sheet `Vertical Unique Count` (PitchBook ID as
  dedup key) - count distinct IDs per vertical.
- Note the tag total (1,793 / $11,857B) exceeds the universe (nonexclusive) -
  label, do not sum.

## Tab 6 - `Vertical_Returns`

Feeds: "the vertical return layer".

- Source: **C** sheet `Industry Vertical Performance`. Index-name headers in
  row 2; the summary block on the right (columns ~Q-AB) holds, per vertical,
  `Start Date` (row 3 = 6/16/2023), `End Date` (row 4 = 6/30/2026),
  `Return (%)` (row 5), `Risk (%)` (row 6).
- Steps: transpose the Return/Risk rows into a per-vertical table beside Tab 5's
  size. To get a FULLER window than the 6/16/2023 summary, compute return
  directly from the daily level columns (level history starts 3/22/2021):
  last level / first level - 1. Always stamp the window on the cell.
- Read-outs (ANNUALIZED; source publishes annualized not cumulative): AI +58.1%
  ann / +302.6% cum, SaaS +34.2%, Cyber +22.2% - three beat the Global TME
  +19.6% ann / +72.4% cum benchmark; AI ~3.0x public; risk understated by mark
  smoothing (note it).

## Tab 7 - `Vintage_2021`

Feeds: "the 2021 vintage and 2028 outlook".

- Source: **C** `Global Unicorn History`. Columns F (snapshot Date), G
  (UnicornRoundDate), H (ThirdPartyId).
- Steps: (a) set of companies whose `UnicornRoundDate` (G) falls in 2021 =
  vintage; (b) of those, how many appear in the latest snapshot (F = 6/22/2026)
  = survivors; (c) departed = vintage minus survivors. Use COUNTIFS / a helper
  pivot on distinct ThirdPartyId.
- Read-outs: 618 minted, 465 active (75.2%), 153 departed.

## Tab 8 - `Coverage_Gap`

Feeds: "the coverage gap: stale vs fresh marks".

- Source: **C** `Global Unicorn History`, latest snapshot. Columns G
  (UnicornRoundDate), H (ThirdPartyId).
- Steps: for current actives, share whose G is >24 months / >36 months before
  6/30/2026. COUNTIFS on the date threshold over the latest-snapshot rows.
- CRITICAL caveat on the cell: G is the unicorn-QUALIFYING date, not the latest
  round, so this OVERSTATES staleness. The Post_Money (I) is more current. Label
  the figure a proxy.
- Read-outs: 78.5% >24mo, 71.9% >36mo (proxy).

## Tab 9 - `Fallen_Attrition`

Feeds: "fallen unicorns".

- Source: **C** `Global Unicorn History`. Column H (ThirdPartyId), F (snapshot).
- Steps: distinct IDs ever present (all snapshots) vs distinct IDs in the latest
  snapshot; departed = ever minus current. Cannot separate fallen from exited in
  this file - label the total "attrition (exits + falls)".
- Read-outs: 2,431 ever, 1,556 active, 875 departed (36%); 156 from 2021.
- To separate fallen from exited: requires the curated fallen list (primary
  tracker) - log as a cross-source dependency, do not fabricate.

## Tab 10 - `Index_Performance` (context)

Feeds: performance context.

- Source: **C** sheet `Global Levels + Performance`. Daily index levels; the
  summary block (cols E-G, rows 4-6) holds Start/End/Return/Risk for Global
  Unicorn vs the TME benchmarks.
- Read-outs: unicorn ~25% annualized vs TME ~12.5%; unicorn risk LOWER than
  public (smoothing artifact - note it).

## Tab 11 - `PBQ_Frame`

Feeds: PBQ section.

- The 20 ranked by model valuation (from Tab 1 col C).
- Estimate-integrity input: the three-price agreement from Tab 1 (cols F/G/H).
- The five PBQ dimensions and composite: NOT in these files - headers only, with
  the six Q1 analyst scores as the seeded rows (Databricks 8.7, Anthropic 7.7,
  SpaceX 7.5, OpenAI 4.2, xAI 3.8, SSI 2.3). Everything else -> `GAPS`. Do not
  invent scores.

## Tabs 12 - `SOURCES`, `CHECKS`, `GAPS`

- `SOURCES`: one row per tab - destination, source file, source sheet, source
  columns, and the transform applied. This is the provenance index; build it as
  you go so every number is traceable in one place.
- `CHECKS`: reconciliations as PASS/FAIL - top-10 + rest = aggregate; quarterly
  ties to annual; AI value ties to `Vertical MV and Count`; the four count bases
  and their deltas.
- `GAPS`: step-ups / RVVC (need deal amounts, not in these files), full PBQ
  (analyst), fallen-vs-exited split (curated list), per-IPO prices - each with
  where it lives instead.

## Provenance rule (apply everywhere)

Every extracted value keeps its PitchBook ID and carries, in the tab's row-2
header, the exact `File!Sheet!Column [transform]` it came from (e.g.
`Round $B = C!Global Unicorn History col I (Post_Money $M) / 1000, latest
snapshot, join on col H`). Any computed cell references the source cells with a
live formula, never a pasted number, except the one deliberate values-paste in
Step 0 (model marks crossing from file B into file C), which is labeled as such
on `HELP_Model`.
