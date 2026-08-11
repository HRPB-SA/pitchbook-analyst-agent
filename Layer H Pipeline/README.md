# Layer H Pipeline

A GitHub mirror of the Layer H Ventures deal pipeline that lives in Notion.
Every company the sourcing system tracks is here, one Markdown file per
company, with the full structured extract alongside. This folder is a
snapshot for reading, diffing, and report research; Notion remains the
system of record. Edit there, then re-extract.

## What's here

```
Layer H Pipeline/
  README.md        this file
  INDEX.md         master index: counts, then one table per thesis pillar
  pipeline.json    the complete structured extract (104 companies, 121 people)
  companies/       one file per company, categorized:
                   quick facts, what they do, deal profile, pipeline
                   position, decision reasoning, people, access paths,
                   open questions, validation, tracking dates
```

## Source

- Notion workspace: **Layer H** (`b4977aec-d4eb-818f-ad86-000364b430d5`)
- Companies database: `89d77aec-d4eb-82ba-939e-01e4e259c624`
  (data source `collection://fe677aec-d4eb-83d4-a21e-07e7970f3dea`)
- People database (founder records linked from company rows):
  data source `collection://a3277aec-d4eb-82a4-89dd-070e13f80d21`
- Extracted: **2026-08-11**

The company pages in Notion carry no body content; the database properties
are the entire record, so nothing beyond properties was left behind. Founder
rows were joined through each company's `Founders` relation; only the 121
People rows linked to companies were mirrored, not the wider contacts book.

## Coverage and caveats

- 104 companies: 54 Vertical Intelligence, 23 Physical AI Enabling Layer,
  20 Agentic Commerce Infrastructure, 7 with the pillar call still open.
- Status: 53 Tracking, 17 Passed, 34 not yet staged. Decisions: 3 Pursue,
  49 Watch, 17 Pass.
- The Notion `LHTS score` property is a formula the API does not export,
  and the `LHTS` relation points at an empty database; neither is mirrored.
- `SPVs` and `Drive folder` were empty on every row at extraction time.
- Several records carry deliberate research flags (identity conflicts,
  unreconciled funding histories, pillar calls). They are preserved verbatim
  under **Open questions** / **Validation**; do not silently resolve them.

## This is not the coverage universe

`companies/` at the repo root is the report engine's coverage universe
(Databricks, Anthropic, OpenAI, and the rest of the frontier cohort) with
Fact stores and snapshot history. This folder is the venture pipeline:
early-stage deal flow with diligence state. The OpenEvidence file here is
the pipeline view of the same company covered at the repo root; keep both.

## Refreshing the mirror

1. Query the Companies data source (SQL mode, 100-row pages; page past
   `has_more` with a `WHERE Company COLLATE NOCASE > '<last>'` cursor).
2. Query the People data source `WHERE Company IS NOT NULL` for founder
   rows; join by the `Founders` relation ids. If the workspace SQL quota
   is exhausted, fetch the missing pages individually by URL.
3. Rebuild the files (a build script writes pipeline.json, INDEX.md, and
   companies/*.md from the merged rows), then commit with message
   `pipeline: <date> Layer H mirror refresh`.
