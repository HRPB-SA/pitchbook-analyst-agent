# Anthropic Operating Model — Teaching Build Roadmap

**Workbook:** `Anthropic_Model_v1.xlsx` (Harrison builds by hand, cell-by-cell; Claude instructs)
**Cadence:** step-gated — Harrison confirms before each advance.
**Scope:** fresh Anthropic-only teaching build. Complements (does not resume) the 28-tab
OpenAI+Anthropic IPO model parked at its Step 5.
**Data:** `DATA_PACK.md` (v1.0, 2026-08-19) — refresh VOLATILE figures at Steps 8–10.

## The question the model answers

**What must be true for $965B — and for an October IPO above it?** Reverse-engineer the Series H
mark and the IPO window against the live revenue curve ($65B run-rate, end-Jul), the canonical
margin path (40% → 77%), and the burn/funding record ($124.3B equity + $37.0B debt).

## Architecture (9 tabs, house numbering)

| Tab | Purpose |
|---|---|
| `00_Assumptions` | every driver, grouped by module · scenario switch (1=Bear/2=Base/3=Bull) · master timeline |
| `01_Data` | facts only — tiered anchors w/ as-of date, basis, tier, tag, decay class (validation ledger built in) |
| `02_Revenue` | monthly run-rate curve → recognized annual revenue → segment forecast to 2030E (gross AND equalized-net rows) |
| `03_Costs` | inference COGS → GM path · R&D incl. training compute · S&M · G&A · headcount |
| `04_PL` | P&L rollup 2023A–2030E · dual view: excl-training vs incl-training (WSJ framework) |
| `05_Cash_Fund` | burn walk → FCF bridge · capitalization (equity + debt tranches) · runway · CE (equity-only, Ruling 1) |
| `06_Valuation` | marks ladder · comps on equalized basis (Ruling 5) · DCF + reverse-DCF on the $965B mark |
| `07_Sensitivity` | growth × GM grid · scenario wiring · IPO pricing matrix |
| `08_Output` | one-page dashboard: thesis, key charts, headline multiples |

## Conventions (locked at Step 1)

- Blue = hardcoded input · Black = formula · Green = output/KPI · Yellow fill = placeholder/low-confidence
- $M throughout model tabs ($65B = 65,000); `01_Data` stores figures as-reported with a units column
- Years in columns D:K = 2023A–2030E on every timeline tab; typed once on `00_Assumptions`, linked everywhere else
- Column A = label · B = units · C = source/tier flag
- One number, one home. Never hardcode a value used twice. Basis-tag every revenue line (GROSS / NET-equalized)

## Syllabus

| # | Step | Craft taught | Status |
|---|---|---|---|
| 1 | Skeleton: workbook, tabs, timeline, conventions, scenario switch stub | facts vs beliefs · single source of truth · auditability | **ISSUED 2026-08-19** |
| 2 | `01_Data`: enter tiered anchors + funding table | source tiers · run-rate vs recognized · decay classes · frozen conflicts | queued |
| 3 | `02_Revenue` historical: run-rate curve → recognized 2023A–2026E · gross vs net | annualization math · integrating a growth curve · Ruling 5 equalization | queued |
| 4 | `02_Revenue` forecast: segment build (API/enterprise · Claude Code · consumer) to 2030E | driver trees · NRR + new-logo builds · growth decay · TAM sanity | queued |
| 5 | `03_Costs`: COGS/compute → GM path · opex blocks · headcount | AI-lab cost anatomy · margin bridge · operating leverage | queued |
| 6 | `04_PL`: rollup, dual excl/incl-training view, breakeven crossovers | statement articulation · why training compute is "R&D" · loss-as-strategy | queued |
| 7 | `05_Cash_Fund`: burn walk, FCF bridge, capitalization, runway, CE | burn vs FCF definitions · debt vs equity · dilution math via post-money | queued |
| 8 | `06_Valuation` comps: marks ladder, equalized multiples, peer cross-section | forward vs trailing · growth-adjusted multiples · private marks ≠ prices | queued |
| 9 | `06_Valuation` DCF: explicit FCF to 2035E, terminal, venture discount rate, reverse-DCF | TVM · terminal-value dominance · what $965B implies | queued |
| 10 | `07_Sensitivity` + `08_Output`: scenario wiring, grids, dashboard | what actually moves the answer · presenting a view | queued |

Each step: concepts → exact cell instructions → validation gates on every figure used.
VOLATILE data (run-rate, comps marks, SPCX tape) re-pulled at Steps 8–10 before valuation locks.

## Status log

- 2026-08-19 · Session 1: branch created, data pack v1.0 written (incl. $65B run-rate refresh,
  proposed canonical update), Step 1 issued. Awaiting Harrison's Step-1 completion + scope confirm.
