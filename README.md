# Databricks Institutional Initiation Note (July 2026)

Single-name initiation of coverage on Databricks, Inc. for an institutional-investor
and venture-capital audience. Author: Harrison Rolfes, Senior Research Director.
Prepared July 10, 2026 on canonical data pack v3.4, with Phase One live re-verification
of every load-bearing figure (see `validation_log.md`).

## Deliverable

- `output/Databricks_Initiation_Note_Jul2026.docx` - the note (39 pages, US Letter,
  19 sections, 10 embedded 300-DPI charts, Contents page with measured page numbers).
- `output/Databricks_Initiation_Note_Jul2026.pdf` - rendered inspection copy
  (LibreOffice; Word will re-render fonts natively).

## Repo layout

- `validation_log.md` - Phase One validation: what was checked, what moved vs the
  pack, conflicts frozen, items labeled unverifiable.
- `build/charts.py` - all 10 charts (matplotlib, 300 DPI, house palette). Figures are
  numbered in order of appearance in the document.
- `build/content_a.py` … `content_d.py` - document content as a block DSL
  (sections 2-4, 5-9, 10-14, 15-19 respectively).
- `build/build_docx.py` - python-docx assembly: styles, header/footer with
  page-x-of-y fields and the COI/embargo line, dual-width DXA tables with
  no-split rows and repeated headers, cover, Contents.
- `build/extract_toc.py` - measures section/figure page numbers from the rendered
  PDF into `build/toc_pages.json` (two-pass Contents fill).
- `charts/` - rendered PNGs.

## Rebuild

```bash
pip install matplotlib python-docx
python3 build/charts.py
python3 build/build_docx.py                      # uses build/toc_pages.json if present
soffice --headless --convert-to pdf --outdir output output/*.docx
python3 build/extract_toc.py                     # refresh TOC page numbers
python3 build/build_docx.py                      # second pass with real numbers
soffice --headless --convert-to pdf --outdir output output/*.docx
```

## Guardrails enforced (do not relax when editing)

1. The quality-valuation correlation coefficient is embargoed: no score-vs-valuation
   scatter, no fitted lines, no r anywhere. The dollar-per-AIBQ-point ranked bar is
   the only cleared expression.
2. COI disclosure block stays on page 2; COI/embargo line stays in the footer.
3. Unclosed/rumored financings (the $165-175B talks) never anchor the base case.
4. Capital-efficiency denominator is equity-only; debt is assessed under CI and risk.
5. PitchBook TTM revenue is a forward-window projection; only dated company prints
   are run-rate evidence.
6. Zero em-dashes (U+2014); `build_docx.py` scans the built docx and prints
   EMDASH-CHECK on every build.
7. Every load-bearing figure carries a dated T1/T2/T3 source; estimates labeled;
   conflicts frozen with both values, never averaged.
