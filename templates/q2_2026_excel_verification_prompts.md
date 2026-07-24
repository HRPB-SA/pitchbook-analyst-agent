# Claude-in-Excel verification prompts - Q2 2026 report

Run these in a live Claude-in-Excel session to locate every number used in the
report and confirm it against the source cell. Each prompt names the workbook, the
tab, and the figures, and writes them into a `REPORT_AUDIT` tab so you end with one
sheet that maps every report figure to its source and flags any mismatch.

## The three workbooks (open the one named at the top of each prompt)

- **PT** = `Final - Q2 2026 - Quarterly Unicorn Tracker - HR Version.xlsx` (deal-level primary tracker). Most figures.
- **MON** = `Unicorn Monitor Data Q2 2026 (lighter, HR version).xlsx`. Three-valuation comparison and vertical index returns.
- **U20** = `Morningstar PitchBook Unicorn 20 Valuations and Pricing Data (h version).xlsx`. Origin of the daily model valuations.

## Standing instruction (paste once at the start of each workbook)

> In this workbook, create a tab named `REPORT_AUDIT` if it does not exist, with the
> header row: `Report figure | Report value | Source tab | Source cell / logic |
> Extracted value | Match (Y/N)`. As I give you each prompt, find the value on the
> named tab, write one row per figure, put the actual cell address or range you read
> in "Source cell / logic", and set Match to Y only if the extracted value equals the
> report value (within rounding). Never overwrite existing rows; always append. After
> each prompt, tell me the extracted values and list any row where Match is N. Do not
> change any source tab; only write to `REPORT_AUDIT`.

---

# Workbook PT - Final Q2 2026 Quarterly Unicorn Tracker

## Prompt P1 - Aggregate universe (tab: `Aggregate unicorns`)

> On tab `Aggregate unicorns`, find the annual series (year headers in the top rows,
> data below). Read the 2026 column (as of 6/30/2026) and the 2025 column, and append
> these rows to `REPORT_AUDIT`:
> - Aggregate post-money 2026 = $8.23 trillion (expect 8,232.51 in $B)
> - Active unicorn count 2026 = 1,743
> - Aggregate post-money 2025 = $7,305.43B; compute YoY = 2026/2025 - 1 (expect ~13%)
> - Universe value gain = 2026 aggregate - 2025 aggregate (expect ~$927B / $0.93T)
> Report the four values and confirm each against the expected figure.

## Prompt P2 - AI sub-universe (tab: `AI Aggregate unicorns`)

> On tab `AI Aggregate unicorns`, read the 2026 and 2025 columns of the annual series
> and append to `REPORT_AUDIT`:
> - AI active count 2026 = 702; AI count share = 702 / 1,743 (expect 40.3%)
> - AI aggregate post-money 2026 = $5.08T (expect 5,076.42 $B); value share = 5,076.42 / 8,232.51 (expect 61.7%)
> - AI aggregate 2025 = $3.49T (expect 3,487.23); six-month change = 2026/2025 - 1 (expect +45.6%)
> - AI value added = 2026 - 2025 AI aggregate (expect ~$1,589B / $1.59T)
> - AI new unicorns 2026 = 109 (new-in-year row); report total new = 178 (from PT tab `Aggregate unicorns` new row, 2026) for the 109-of-178 claim.

## Prompt P3 - Deal concentration and deal sizes (tabs: `Top Deals in Qtr`, `Unicorn deal activity`, `MedAvg Uni Deal Size`)

> On tab `Top Deals in Qtr` (Q2 2026 deals, sorted by deal size), append to `REPORT_AUDIT`:
> - Sum of the five largest deal sizes = $87.1B
> - Largest deal: Anthropic, deal size $65B, post-money $965B
> - Second-largest: Prometheus, $12B into $41B
> - Also confirm Anduril $5B/$61B, ByteDance $3B/$370B, Isomorphic Labs $2.1B are in the top five
> - Sum of the ten largest / sum of all sized Q2 deals (expect top-10 = 68.9%)
> - Sum of the twenty-five largest / sum of all sized deals (expect top-25 = 78.5%)
> On tab `Unicorn deal activity`, read 2026 total deal value (expect $396.1B) and Q2 2026 quarterly deal value ($144.9B) and count (207). Compute Anthropic $65B / $396.1B (expect 16.4% of first-half financing).
> On tab `MedAvg Uni Deal Size`, read 2026 median and average deal size (expect $200M median, $1,142.76M average).

## Prompt P4 - Step-ups and RVVC by year (tabs: `MedAvg Uni Val Step Up`, `MedAvg Uni RVVC`)

> On tab `MedAvg Uni Val Step Up`, read the median step-up row and append:
> - 2026 median step-up = 2.20x (expect 2.201); 2025 = 2.05x (2.048); 2021 = 2.64x (2.641)
> On tab `MedAvg Uni RVVC`, read the median and average RVVC rows and append:
> - 2026 median RVVC = 1.42x (1.418); 2025 = 0.93x (0.9323); 2023 = 0.23x (0.2342)
> - pre-boom baseline = average of the 2016, 2017, 2018 medians (expect ~0.73)
> - 2026 average RVVC = 2.73x (2.729)

## Prompt P5 - RVVC and step-up by vertical (tab: `RVVC & Step Up Vertical Ranking`)

> On tab `RVVC & Step Up Vertical Ranking`, the verticals run down the rows with a 2025
> block and a 2026 block of columns (each: Deal Count, Avg RVVC, Median RVVC, Avg Step
> Up, Median Step Up). Read the 2026 block and append:
> - Artificial Intelligence: median RVVC 1.84x (1.837), median step-up 2.35x, deal count 249
> - SaaS: median RVVC 1.42x (1.423), median step-up 2.18x (2.183), deal count 176
> - Robotics and Drones: median RVVC 2.03x (2.025), average RVVC 5.66x (5.658)
> - CleanTech: median RVVC 3.30x (3.298), median step-up 2.77x (2.771)
> - Cryptocurrency/Blockchain: median RVVC 2025 = 2.62x (2.619) and 2026 = 1.11x
> - Cybersecurity: median RVVC 0.66x (0.662), median step-up 1.74x
> - E-Commerce: median RVVC 0.38x (0.3817), median step-up 2.13x (2.133)

## Prompt P6 - Round dynamics (tabs: `Unicorn down round activity`, `MedAvg Uni Time Between Rnds`, `Rnds by Inv Count Bucket`, `Unicorn investors x Qtr`)

> On tab `Unicorn down round activity`, read the annual series and append:
> - 2026 down-round count = 6 and value = $3.85B (3.846); 2025 count = 31; 2024 count = 34
> On tab `MedAvg Uni Time Between Rnds`, read the median row:
> - 2026 = 0.98yr (0.9808); 2025 = 1.21yr (1.205); 2024 = 1.45yr (1.445)
> On tab `Rnds by Inv Count Bucket`, compute the 6+-investor share of known-investor rounds:
> - 2026 = 60.9% (six-plus bucket / total known-investor rounds, 234 / 384); 2021 peak = 64% (0.6402)
> On tab `Unicorn investors x Qtr`, read participation counts:
> - Q3 2021 = 2,892; Q4 2023 = 895; Q1 2026 = 1,415; Q2 2026 = 995

## Prompt P7 - Verticals by tagged value (tab: `Unicorn market val x vertical`)

> On tab `Unicorn market val x vertical`, each row is a vertical with a unicorn count and
> a "Sum of latest post valuation ($T)". Multiply the $T value by 1,000 for $B and append:
> - SaaS = $6.44T (6,444.79 $B), 968 companies
> - Artificial Intelligence & ML = $6.02T (6,023.32 $B), 865 companies
> - FinTech = $2.02T (2,020.6 $B), 436 companies
> - Space Technology = $1.87T (1,868.3 $B), 34 companies
> - Mobility Tech = $0.83T (829.7 $B); CloudTech & DevOps = $0.74T (742.1); HealthTech = $0.45T (450.9)
> - SaaS + AI tagged value = $12.5T (12,468.11 $B)
> Note on the row: tags are nonexclusive, so these do not sum to the universe.

## Prompt P8 - Exits (tabs: `Uni Exits by Type`, `Unicorn exit activity`, `MedAvg Uni Time to Exit`, `Top Exits in Qtr`)

> On tab `Uni Exits by Type`, read the 2026 column and append:
> - Total exit value 2026 = $2,110.9B; Public Listing value = $1,802.91B; Public Listing share = 85% (0.8541)
> On tab `Top Exits in Qtr`, append: SpaceX IPO exit size = $1,690.24B; Cerebras IPO = $34.25B; Quantinuum IPO = $13.98B.
> - Compute ex-SpaceX 2026 exit value = 2,110.9 - 1,690.24 (expect $420.7B)
> On tab `MedAvg Uni Time to Exit`, read the median row: 2026 = 8.47yr; 2025 = 9.17yr (9.174).

## Prompt P9 - Active universe: dormancy, geography, latest financing dates (tabs: `Active Unicorns`, `MedAvg Uni Post Value`)

> On tab `Active Unicorns` (header row 7, data from row 8), column D is "Latest Round
> Close Date" and column Q is Country. Using an as-of date of 6/30/2026, append to `REPORT_AUDIT`:
> - Share with last financing > 24 months before 6/30/2026 = 47.6% (count / total active)
> - Share > 36 months = 37.1%
> - Count with last financing within the past 12 months = 614 (expect ~a third)
> - United States share of active = 54% (US count 945 / total); confirm US count = 945
> - Latest financing dates: Anthropic = 2026-05-28 (May 2026), OpenAI = 2026-03-31 (March 2026), ByteDance = 2026-05-16 (May 2026), Ant Group = 2020-08-09 (August 2020), SHEIN = 2024-01-01 (January 2024)
> On tab `MedAvg Uni Post Value`, read median and average post value:
> - 2026 median = $2.0B, average = $18.19B; ratio 9.1x; 2025 ratio = 3.1x (4.821/1.572); 2024 ratio = 2.8x (3.338/1.185)

## Prompt P10 - Top 10 by post value and concentration (tab: `Top 10 Unicorns by PV`)

> On tab `Top 10 Unicorns by PV`, read the ten companies and their most-recent post
> valuations and append:
> - Anthropic $965B, OpenAI $852B, ByteDance $370B, Stripe $159B, Databricks $134B, Waymo $126B, Ant Group $78.65B, Revolut $75B, SHEIN $66B, Anduril $61B
> - Top-2 (Anthropic + OpenAI) = $1.82T (1,817); as share of $8,232.51B = 22% (22.07%)
> - Sum of all ten = ~$2.9T (2,886.65); as share of $8,232.51B = 35% (35.06%)

## Prompt P11 - Fallen unicorns (tab: `Fallen Unicorns to Date`)

> On tab `Fallen Unicorns to Date` (header row 7, data from row 8), append:
> - Total fallen companies (count of rows) = 245
> - Median down-round post-money (the priced down-round column, excluding zero/blank) = $524.5M
> - Median markdown vs peak = down-round post / peak post - 1 = -67% (-0.6722)

## Prompt P12 - 2021 cohort (tab: `2021 Uni Cohort`)

> On tab `2021 Uni Cohort` (header row 7, data from row 8), column F is "Active Status".
> Count each status value and append:
> - Total = 635; Active = 470 (74%); Exited = 102 (16%); Fallen = 34; Fallen at Exit = 15; Bankrupt/Out of Business = 13

## Prompt P13 - Investors and step-up leaders (tabs: `Top Investors`, `Top Deals in Qtr by Val Step Up`)

> On tab `Top Investors`, read the deal-participation counts and append:
> - Sequoia Capital = 491; Tiger Global = 472; Andreessen Horowitz = 454; Accel = 382; Coatue Management = 344
> On tab `Top Deals in Qtr by Val Step Up`, read the top rows and append:
> - Hark = 151.4x step-up (post $6B); Blitzy = 30x (post $1.4B); SendCutSend = 30x (post $1.01B)

---

# Workbook MON - Unicorn Monitor Data Q2 2026

## Prompt M1 - Three-valuation comparison (tab: `Top20_Marks`)

> On tab `Top20_Marks`, each of the twenty companies has a Model $B, Round $B, and
> Secondary $B, plus gap columns. Append to `REPORT_AUDIT`:
> - Aggregate Model / Round premium for the round-marked names = +15.2% (0.1515)
> - Count of companies where Secondary < Model = 12
> - SpaceX: Model = $2,026.24B, Secondary = $1,376.55B, Secondary/Model = -32% (-0.3206); gap = ~$650B
> - Anthropic: Model = $1,272.09B, Secondary = $989.6B, Secondary/Model = -22% (-0.2221); gap = ~$282B
> - Secondary above Round (up-round): Applied Intuition +36% (0.3648), Anysphere +30% (0.304), Anduril +22% (0.2212), Revolut +16% (0.1608)
> - Neuralink: Model/Round = +441% (4.416)
> - Confirm Ripple, Epic Games, Kraken show all three valuations below their last round.

## Prompt M2 - Vertical index returns (tab: `Vertical_Returns`, or raw `Industry Vertical Performance`)

> On tab `Vertical_Returns` (3-year window 6/16/2023-6/30/2026, level-based), append the
> annualized and cumulative returns:
> - Artificial Intelligence = 58.1% annualized (0.5814), 302.6% cumulative (3.026)
> - Enterprise SaaS = 34.2% (0.3423); Cybersecurity = 22.2% (0.2221)
> - Global TME benchmark = 19.6% annualized (0.1963), 72.4% cumulative (0.7239)
> - FinTech = 12.9% (0.1291)
> - AI / TME annualized ratio = ~3x (0.5814 / 0.1963 = 2.96); confirm exactly three verticals beat TME.

## Prompt M3 - Coverage-gap proxy, superseded figure (tab: `Coverage_Gap`)

> On tab `Coverage_Gap`, read the qualifying-date staleness proxy and append:
> - Share of active companies with qualifying date > 24 months = 78.5% (0.7841)
> Note in the row: this is the OLD proxy the report cites as superseded; the report uses
> 47.6% from PT `Active Unicorns` latest-financing dates (Prompt P9). Both should appear.

---

# Workbook U20 - Unicorn 20 Valuations and Pricing (origin of model valuations)

## Prompt U1 - Model valuations at the Q2 close (tab: `U-Value Creation` or `Historical Valuations`)

> On tab `U-Value Creation` (or `U-Summary`), read the 6/30/2026 model valuations and append:
> - SpaceX = $2,026.24B; Anthropic = $1,272.09B; OpenAI = $861.4B; twenty-company total = $5,019.04B
> These are the model valuations that feed MON `Top20_Marks` (Prompt M1). Confirm SpaceX
> and Anthropic match the Model column there, so the two workbooks agree at the close.

---

# After running all prompts

Ask Claude-in-Excel:

> Review the `REPORT_AUDIT` tab across this workbook. List every row where Match = N,
> and give me a one-line count of rows checked, rows matched, and rows flagged. For any
> flagged row, show the report value and the extracted value side by side so I can see
> the size of the difference.

Do this in each of the three workbooks. Every figure in the report should resolve to a
Match = Y row; anything that does not is either a rounding display, a basis mismatch
(check you are on the right workbook), or a figure to correct in the report.
