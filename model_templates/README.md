# Model templates: the reference workbooks and the shared skeleton

Four analyst-provided workbooks, kept as the format contract for the financial
models this repo produces. See `Report Automation/docs/AUTOMATION_ROADMAP.md`
idea 9 for the build plan that consumes them.

| File | Archetype | Shape |
|---|---|---|
| `SaaS_Operating_Model.xlsx` | Subscription operating model | 3 sheets; monthly customer and recurring-revenue build feeding an annual model |
| `Three_Statement_Model.xlsx` | Three-statement | 4 sheets; profit and loss, cash flow, balance sheet linked, with a circularity switch |
| `DCF_Valuation_Model.xlsx` | Discounted cash flow | 4 sheets; revenue and cost schedules, cost-of-capital build, both terminal value methods |
| `Full_Valuation_Model_AMZN.xlsx` | Full valuation | 18 sheets; statements, scenarios, discounted cash flow, comparables, precedents, sum-of-the-parts |

## The finding: all four are the same building

Sheet counts differ; the skeleton does not. Every workbook runs left to right
in the same order, and the model factory should implement this once.

```
Cover        title, contents, and an automated model-checks block
Inputs       every assumption, in blue, each in its own labeled cell
Raw Data     historicals with the source written beside them
Model        the statements and their supporting schedules
Scenarios    best / base / worst, selected from a single switch cell
Valuation    discounted cash flow, comparables, or both
Outputs      the dashboard a reader looks at first
```

The larger workbook splits these across more sheets (`Control Panel` is the
inputs sheet; `Financial Statements` is the model; valuation spreads across
`DCF`, `WACC`, `Comps`, `Precedents`, `SOTP`). The smaller ones combine them.
Same order, same roles.

## Conventions, measured from the files

**Colors.** Blue text for anything typed in — `3271D2` in three of the
workbooks, pure `0000FF` in the fourth. Black for anything calculated. Green
for a link to another sheet (`1F995B` / `00745A`). The rule a reader relies on:
if it is blue you may change it, if it is black do not touch it.

**Number formats.** Accounting style throughout, zero rendered as a dash and
negatives in parentheses:

| Use | Format |
|---|---|
| Currency | `_(#,##0_);\(#,##0\);_("–"_);_(@_)` |
| Currency with symbol | `"$"#,##0_);\("$"#,##0\);"-"` |
| Percent | `_(#,##0.0%_);\(#,##0.0%\);_("–"_)_%;_(@_)_%` or `0.0%` |
| Multiple | `0.0"x"` / `0.0\x` |
| Actual year | `0"A"` |
| Forecast year | `0"F"` (`0"E"` in the larger workbook) |
| Monthly date | `mmm-yy` |
| Check result | `"Yes";"ERROR";"No";"ERROR"` |

Two of these are worth copying deliberately. The year suffix formats let a
plain number render as `2023A` or `2024F`, so a reader can see at a glance
where history ends. The check format turns a boolean into a plain-English
answer and renders anything unexpected as `ERROR`.

**Scenario switching.** One cell drives the whole model. The larger workbook
resolves a named scenario through a lookup into a control number, then feeds
every scenario-dependent row through `CHOOSE(...)` across the live, base, bull,
and bear blocks. The others use a "Driver Switch" input above best / base /
worst rows. Either is fine; a single switch cell is the requirement.

**Model checks on the cover.** Each workbook carries a checks block on its
first sheet — "Balance Sheet Unbalanced?", "Two UFCF Methods Different?",
"Model Circularity" — reading clean before the file is fit to send. This is the
pattern the model gate should reproduce.

**Named ranges.** The larger workbook names its global assumptions
(`_Vdate`, `_WACC`, `_TaxRate`, `_LTGrowth`, `_CompanyName`) so formulas read
in English. Worth adopting.

## Rules for generated models

1. Every blue cell is either a reference to a stored fact, with source and date
   in the cell note, or an assumption marked as one with its reasoning beside
   it. No third category.
2. No hardcoded number inside a formula where an input cell exists.
3. Formulas consistent across every period in a row.
4. The cover states how many inputs are sourced facts versus assumptions.
   Below threshold, the workbook is labeled illustrative.
5. Recalculate before shipping; zero formula errors, and all six model checks
   clean.
