# Claude-in-Excel prompt: build the tracker sheets + flag every discrepancy

Paste below the line into the Excel session where `MAP` is approved. It builds
each output sheet with an explicit breakdown tied to a specific Q2 2026 tracker
template exhibit, and it runs a comprehensive discrepancy engine that logs every
data problem to a `DISCREPANCIES` register. Read-only against source sheets;
writes only to new sheets.

---

`MAP` is approved. Build the output sheets now. Two standing requirements govern
the whole build:

**(A) Every sheet has a specific breakdown tied to the template.** Each sheet
states, in row 2, the template exhibit it feeds (e.g. "Feeds: template §3.4
Quarter dashboard"), then shows exactly the rows and columns named below - no
more, no less. The data exists to build a named exhibit; if a column does not
serve one, do not add it.

**(B) Identify every discrepancy.** Nothing gets silently smoothed. Run the
discrepancy engine below across every sheet as you build it, flag offending
cells in place, and log each finding to a `DISCREPANCIES` register. A number
that looks wrong is a finding, not something to quietly adjust.

## The discrepancy engine

Create a `DISCREPANCIES` sheet with columns: ID, Severity
(Blocker / Warning / Note), Category, Sheet, Cell or Range, Rule that caught it,
Expected, Actual, Auto-fix applied?, Suggested resolution. Highlight every
flagged source cell (distinct fill) and attach a comment carrying the finding
ID. Scan for all ten categories:

- **A Referential/structural:** any `#REF!`, `#NAME?`, `#VALUE!`, `#DIV/0!`,
  broken link, or mislabeled sheet title. (Known: the estimate `#REF!` columns -
  repair from UNI LIST where reachable and log as auto-fixed; the mislabeled
  sheet title - correct and log.)
- **B Count reconciliation:** constituent-list count vs published aggregate
  (the 1,688 vs 1,743 = 55-company gap - quantify it, name the 55 if
  derivable); sum-of-parts vs total (country sum, series shares to 100%).
- **C Cross-sheet ties:** quarterly sums to annual; top-10 + rest = aggregate;
  each dashboard KPI equals its detail-sheet total.
- **D Temporal:** as-of mismatch (universe 6/30/2026 vs trading 3/31/2026 -
  flag on every performance sheet); any future date; deal/round date after the
  as-of; round date after exit date; founding date after exit date; end date
  before start date; negative durations.
- **E Value plausibility:** an "active unicorn" with a post-money < $1B;
  negative valuation, amount, or step-up; efficiency multiple that is null,
  infinite, or beyond a stated sanity bound; a share > 100%; an estimate that
  diverges from its mark beyond a set threshold (flag for review, do not
  change).
- **F Duplicates/keys:** duplicate company ID within a snapshot; duplicate deal
  ID; missing ID; same name mapped to two IDs, or two names to one ID.
- **G Definitional conflicts:** a company appearing in BOTH the active universe
  and the fallen list; a company in the universe whose last mark is < $1B; the
  SpaceX IPO-status conflict (base-case active per ruling - note it once, do
  not treat as an error).
- **H Coverage gaps:** field present but null; the known GAPS items; partial
  columns. Cross-reference each to the `GAPS` sheet.
- **I Unit/format:** a value in $M sitting in a $B column (or the reverse); a
  percentage stored as a whole number where fractions are expected; any currency
  that is not USD.
- **J Sign/logic:** exit size > post value; an "ex-SpaceX" figure >= its
  with-SpaceX base; shares within a group that do not sum; a top-N series that
  is not monotonic (top5 <= top10 <= top25 <= top50 <= 100%).

**Auto-fix policy:** apply ONLY unambiguous mechanical repairs (rebuild a
`#REF!` estimate from UNI LIST; fix a mislabeled title) and log them as
auto-fixed with before/after. Everything else is flagged and left as-is - never
silently overwrite a data value.

## Per-sheet breakdown (what each sheet shows + its own checks)

Fields per `MAP`. Below is the breakdown - the rows/columns and the one thing
each sheet must surface - plus the discrepancy checks specific to it.

**Front matter**
- `COVER` - feeds the report front. Title, both as-of stamps, the SpaceX rule in
  one line, and a hyperlinked contents list: each sheet, its one-line
  description, AND the template section it feeds. Also a live count of open
  Blockers/Warnings pulled from `DISCREPANCIES`.
- `HIGHLIGHTS` - feeds §3.2 key takeaways. One screen: the ~12 headline Q2 2026
  numbers with prior-quarter, year-ago, and change columns. Each number is a
  formula pointing at its detail sheet (never re-keyed). Check: every headline
  ties to its source cell (Category C) - flag any that does not.

**Universe (feeds §3.4 / §3.12)**
- `01 Dashboard` - 8 KPIs x 6 periods. Check: each KPI cell = its detail-sheet
  total (C); flag any break.
- `02 Qtr Activity` - deal value/count, exit value/count by quarter Q1'21-Q2'26.
  Check: quarterly sums tie to 03 annual (C); deals missing date or size (H).
- `03 Universe` - active/new count, aggregate, top-10 by year 2016-2026, with an
  `ex-SpaceX (sensitivity)` column on Q2 2026. Checks: active count = published
  1,743 not the 1,688 list (B, flag the 55 delta); top-10 + rest = aggregate
  ($8,232.5B) (C, J); ex-SpaceX < base (J).
- `04 Country` - country, active count, aggregate ($B), sorted. Check: country
  counts and valuations sum to the universe totals (B) - flag residual.
- `05 Vertical` - vertical, count, aggregate, top-10. Checks: verticals are
  nonexclusive so the sum EXCEEDS the total - label it, do not flag as error;
  flag any company with a null vertical (H).
- `06 Series Mix` - deal-value share by Seed/A/B/C/D+ by year. Check: each year
  sums to 100% +/- rounding (B) - flag years that do not.
- `07 Tested vs Untested` - aggregate split by mark age <=24 vs >24 months.
  Checks: tested + untested = aggregate (C); count companies with no round date
  that cannot be classified (H).

**Leaders (feeds §3.5)**
- `08 Deal Leaders` - every Q2'26 unicorn deal, sorted by size, with top-5/10/
  remainder flag. Checks: deal sizes sum to the 02 Q2 deal value (C); duplicate
  deal IDs (F); deals missing size/post (H).
- `09 Concentration` - top 5/10/25/50 share of deal value, 2021-Q2'26. Check:
  monotonic within each period (J) - flag inversions.
- `10 Cap Efficiency` - top ~15 by post-money: post, equity raised, multiple
  (post/equity, equity-only). Checks: equity null or 0 (A div/0, flag); negative
  (E); only-total-capital rows (H); multiple beyond sanity bound (E, review).
- `11 Value Creation` - value created since first round, years, value/yr. Checks:
  years > 0 (D); missing first-round date (H).

**Quality (feeds §3.7)**
- `12 PBQ` - headers only; PBQ scores are analyst-generated, not in this data.
  Log to `GAPS`. Check: flag if any score cell is populated (should be empty).

**Deals (feeds §3.8)**
- `13 Val Percentiles` - 25/50/75/90th pre-money by series, 2021 vs 2026 H1, %
  change. Checks: 25<=50<=75<=90 within each series (J); series with n below a
  stated minimum (E, thin-sample note).
- `14 Time Between Rounds` - 25/50/75th pct months between rounds by year.
  Checks: durations > 0 (D); state the denominator excludes non-re-raisers and
  count them (H).
- `15 Seed Size` - median seed size for later-unicorns by year. Check: companies
  with no seed round in history (H).

**Valuations & Dormancy (feeds §3.9)**
- `16 Top10 Share` - top-10, rest, share by year, with ex-SpaceX column. Checks:
  share <= 100% off matched denominators (J); ex-SpaceX < base (J).
- `17 Estimate vs Mark` - mark, estimate, above/flat/below, months since round;
  counts at top. Checks: repair estimate `#REF!` from UNI LIST (A, auto-fix);
  flag any remaining `#REF!` (A); above+flat+below = n (B); null mark/estimate
  (H).
- `18 Marked Down` - subset where estimate < mark, % markdown, sorted. Checks:
  is a strict subset of 17 (C); flag markdowns beyond -90% for review (E).
- `19 RVVC & Step-up` - median step-up and median RVVC by year. Checks: step-up
  > 0 (E); RVVC denominator guard (A); thin-n years (E).
- `20 Fallen Unicorns` - date fell = Unicorn End Date (spine), with Down Round
  Date + down-round post-money as extra columns; last valuation, vertical,
  country; counts per year and per vertical. Checks: a company in BOTH this list
  and the active universe (G, Blocker); End Date null but company off the active
  list (G).
- `21 Dormancy Ledger` - dormant count, >3yr stale, avg mark age; flows (raised
  again: n + median step-up; fell: n) for Q2'26 and prior quarter, via MAXIFS
  point-in-time. Checks: companies with no round date cannot be aged (H); state
  the survivorship caveat; prior vs current deltas plausible (E).
- `22 Cohort Survival` - no-follow-on share at 6..60 months per cohort H1'21-
  H2'25, AI vs non-AI. Checks: share is monotonic non-decreasing in months (J);
  AI + non-AI = cohort total (B); cohort size > 0.

**Exits (feeds §3.10)**
- `23 Qtr Exits` - exit value/count by quarter. Check: ties to 26 sums and 02
  (C).
- `24 Exit by Type` - value share and count share by IPO/M&A/buyout by year.
  Checks: each block sums to 100% per year (B); unclassified deal types (H).
- `25 Time to Exit` - median and average founding-to-exit years by year. Check:
  founding date after exit date = negative age (D, Blocker).
- `26 Exit List` - every Q2'26 exit with SpaceX flag and running ex-SpaceX
  cumulative. Checks: sum ties to 23 (C); exit size > post value (J); missing
  date/type (H).
- `27 China AI IPO` - company, IPO date, IPO price, current price, returns.
  Price/return columns to `GAPS` if absent. Check: flag any hardcoded return
  (fabrication guard, H).
- `28 Unicorn M&A` - VC-backed/unicorn acquirers; three-way proxy: below -10%
  distressed / +/-10% flat / above +10% strategic (labeled proxy). Checks: rows
  missing exit-post or last-mark cannot be classified -> "unclassified" (H);
  acquirer not resolvable as VC-backed (H).

**Performance (feeds §3.11) - trading data as of 3/31/2026**
- `29 Secondaries` - volume and count by period where present; fund
  contributions/distributions to `GAPS`. Flag the as-of on the sheet.
- `30 Index Levels` - only indexes present in this workbook, one column each,
  plus start/end/return/risk. Checks: as-of 3/31/2026 not 6/30/2026 (D, flag on
  sheet); vertical/regional/TME indexes absent -> `GAPS`.
- `31 Correlation` - US Unicorn vs public benchmark over a stated window. Check:
  flag if the window differs from Q1's (comparability, Note).
- `32 IPO Spreads` - Day 7/30/90/120 by year, global and US -> `GAPS` (no
  per-IPO price paths in this data). Build headers, log the gap.
- `33 Best & Worst IPO` - company, listing date, sector, country since 1/1/2025;
  performance column -> `GAPS`.

**Verticals (feeds §3.12)**
- `34 AI Value Share` - AI, non-AI, AI share by year. Checks: AI + non-AI =
  aggregate (C); share <= 100% (J); note the nonexclusive-vertical method (H).
- `35 Vertical Concentration` - per vertical: aggregate, largest company, its
  valuation, its share; space-tech shown with AND without SpaceX. Checks:
  largest-company share <= 100% (J); confirm SpaceX is the space-tech leader.

**Back matter**
- `DEFINITIONS` - every term, both as-of dates, SpaceX treatment, currency,
  units.
- `GAPS` - everything not extractable and where it lives instead (mark the
  cross-source Monitor-workbook items).
- `CHECKS` - the reconciliation tie-outs as PASS/FAIL rows (the Category B/C
  subset), each showing the tie-out difference. `DISCREPANCIES` holds the full
  exception log across all ten categories.

## Formatting

Per the standing standard: row-1 title, row-2 as-of + template ref + source,
header row (bold, dark fill), `Note:` block below, freeze header + first column,
units in headers, `#,##0.0` for $B / `0.0%` fractions / `0.0"x"` multiples,
negatives in parentheses, zeros as `-`, banded rows, current-period column
highlighted, no merged cells in data, a link back to `COVER`.

## Order and checkpoints

Build in batches, pausing after each so I can review: (a) COVER + HIGHLIGHTS,
(b) 01-07, (c) 08-15, (d) 16-22, (e) 23-28, (f) 29-35, (g) DEFINITIONS + GAPS +
CHECKS + DISCREPANCIES. After each batch, report: formulas evaluate with zero
errors, and the new `DISCREPANCIES` findings from that batch (count by
severity). Start with (a).
