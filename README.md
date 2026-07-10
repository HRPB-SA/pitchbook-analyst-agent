# Databricks: Brick by Brick (July 2026)

Institutional deep dive on Databricks, Inc. built around a single question:
what is each layer of the business, what does it earn, what does it mean now,
and what does it imply next. Companion seven-year three-statement operating
model in Excel. Prepared by Harrison Rolfes, Senior Research Director,
July 10, 2026.

## Deliverables

- `output/Databricks_BrickByBrick_Jul2026.docx` - the report (30 pages: cover,
  contents, ten sections, 11 embedded 300-DPI charts).
- `output/Databricks_Operating_Model_Jul2026.xlsx` - the model. Sheets mirror
  a standard 3-statement teaching structure: Cover (TOC + model checks),
  Outputs (dashboard + charts), Inputs (Best/Base/Worst driver switch, every
  assumption sourced in column M, estimated opening balance sheet), Model
  (income statement, cash flow, balance sheet + Schedules A-D: run-rate
  anchors, customer-cohort build, product-line split, funding ladder),
  Valuation (sensitivity grid, per-point table, growth-adjusted comparison).
- `output/Databricks_BrickByBrick_Jul2026.pdf` - rendered inspection copy.
- `validation_log.md` - the July 10, 2026 live re-verification log behind the
  figures (internal working document).

## Report structure

Executive Summary, The Foundation, The Bricks (products layer by layer),
The Mortar (how the money is made, incl. DBU price mechanics), The Builders
(customers and use cases), The Neighborhood (competition on three fronts),
The Blueprint (strategy read through acquisitions, partnerships, capital),
The Ledger (financials + model summary), The Appraisal (quality framework,
comparables, scenarios), The Stress Test, The Verdict.

## Model verification

`build/model_xlsx.py` computes the full base case in Python, asserts the
balance sheet balances in every year, writes the same arithmetic as live
Excel formulas, and the workbook has been independently recalculated
(formulas engine) to confirm formula outputs match to the dollar with a zero
balance check in all seven years. The Driver Switch (Inputs!E5) flexes revenue
growth and gross margin across Best / Base / Worst.

## Rebuild

```bash
pip install matplotlib python-docx openpyxl
python3 build/charts.py          # 11 charts -> charts/
python3 build/model_xlsx.py      # workbook -> output/ (+ prints base case)
python3 build/build_docx.py      # report -> output/ (uses build/toc_pages.json)
soffice --headless --convert-to pdf --outdir output output/Databricks_BrickByBrick_Jul2026.docx
python3 build/extract_toc.py     # measure Contents page numbers
python3 build/build_docx.py && soffice --headless --convert-to pdf --outdir output output/Databricks_BrickByBrick_Jul2026.docx
```

## Standing constraints (do not relax when editing)

1. The quality-valuation correlation coefficient is embargoed: no
   score-vs-valuation scatter, no fitted lines, no correlation statistic.
   The per-point ranked bar is the only cleared expression.
2. Unclosed or rumored financings (the reported $165-175B talks) never anchor
   the base case; they are analyzed, not adopted.
3. Capital-efficiency denominators are equity-only; debt informs compute
   independence and risk.
4. PitchBook TTM revenue is a forward-window projection, not a run-rate source.
5. Zero em-dashes (U+2014); the build scans the docx and fails loudly.
6. Sources are dated and named by kind (company disclosure, PitchBook,
   SEC EDGAR, public price lists, press reports); estimates are labeled.
