# Analyst Report Engine

Automated research-report factory for the HRPB coverage universe. Type a
report idea into the dashboard; a Claude Code session on this repo runs the
pipeline in `CLAUDE.md`: live research (PitchBook Premium + news + EDGAR),
snapshot into a per-company tracker, trend and trigger review, composition in
the measured house style, house-factory charts, a gated docx/pdf build, and a
validation ledger. Deterministic Python does storage, math, charts, build,
and QA; the agent does research judgment, tiering, and prose.

## How to request a report

1. Open the dashboard (published artifact; source in `dashboard/index.html`).
2. Type the idea, pick template + companies + rigor.
3. Either **Copy launch prompt** and paste it into a new Claude Code session
   on this repo, or **Download request file** and commit it to
   `requests/queue/` for the scheduled runner. Details: `requests/SCHEMA.md`.

Every Monday a scheduled session re-pulls the tracked universe, diffs against
canonical, updates trigger states, and files an update request when something
material moved.

## Layout

```
CLAUDE.md          agent runbook: the pipeline, research protocol, rulings
engine/            deterministic core: store, trends, style profiler, charts,
                   docx builder, QA gates (python3 -m engine <cmd>)
templates/         report contracts (initiation, update, rush, earnings,
                   one-pager, sector) + TEMPLATE_SPEC.md
style/             STYLE.md (prescriptive voice) + measured style profile
data/              universe.json + per-company canonical profiles, immutable
                   snapshots, frozen conflicts, computed trends
requests/          dashboard request queue + schema
reports/           one directory per generated report: request, research
                   snapshot, blocks, charts, output (docx/pdf), validation log
dashboard/         the request dashboard (single file, also published)
reference_reports/ drop external .docx here to teach the style profiler
build/, charts/, output/, validation_log.md
                   the original hand-built July 2026 Databricks initiation
                   ("Brick by Brick") the engine was generalized from
```

## Engine quick reference

```bash
python3 -m engine style                  # re-profile the report library
python3 -m engine snapshot <slug> <f>    # add + merge a research snapshot
python3 -m engine digest <slug>          # tracker digest (trends/triggers)
python3 -m engine cohort                 # cross-company table
python3 -m engine staleness              # decay-class breaches, all companies
python3 -m engine charts <charts.json>   # render chart specs (house factory)
python3 -m engine build <report_dir>     # docx + pdf + measured TOC + QA gate
```

Dependencies: `pip install python-docx matplotlib openpyxl`; LibreOffice
(`libreoffice-writer`) + `poppler-utils` for pdf + measured Contents pages.

## Standing constraints (encoded in the engine and runbook; do not relax)

1. The quality-valuation coefficient is embargoed: the chart factory has no
   scatter type and refuses fitted lines against scores; the per-point ladder
   is the only cleared expression.
2. Unclosed or rumored financings never anchor a base case; they are
   analyzed, not adopted (flag `do-not-adopt` in the store).
3. Capital-efficiency denominators are equity-only.
4. PitchBook TTM revenue fields are forward-window projections, never
   run-rate sources.
5. Zero em-dashes; the QA gate fails the build.
6. Sources are dated and named by kind in report prose; outlet names live in
   validation logs. Estimates are labeled at the point of use; frozen
   conflicts ship both values or neither.

## Provenance

The engine generalizes the July 10, 2026 Databricks initiation note in
`build/` + `output/` (35 pp, 11 charts, seven-year operating model). That
report's structure became `templates/initiation_note.json`; its builder
became `engine/build_docx.py`; its chart code became the spec-driven factory
in `engine/charts.py`; its validation log became the seed for the Databricks
tracker profile. First engine-generated report:
`reports/databricks-update-2026-08-10/` (the $188B term-sheet update).
