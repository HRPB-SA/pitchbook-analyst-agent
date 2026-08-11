# NEXUS Intelligence

A GitHub mirror of Harrison Rolfes's NEXUS private-market AI research
system — the Notion workspace that tracks the Frontier Five and the
broader AI/unicorn universe, scores them against a proprietary quality
rubric (AIBQ/PBQ), and produces the Morning Digest research feed.
Extracted, organized, and redacted for the workspace's one embargo
ruling on 2026-08-11.

This is a distinct system from the report engine's own coverage store at
the repo root (`companies/`) and from the (removed) Layer H Ventures
pipeline mirror. NEXUS is the research infrastructure this repo's own
methodology rulings were partly modeled on — its Canon rulings on CE
denominator, revenue equalization, and the quality-valuation embargo
match this repo's `CLAUDE.md` almost verbatim, because they came from
the same analyst.

## Embargo — read first

NEXUS computes a cross-company correlation between AIBQ quality score and
valuation. That coefficient is embargoed by the source system's own
Ruling 2 and has been redacted from every file in this mirror, including
the Excel workbook. See `system/canon-and-governance.md` for the full
ruling and what public expression remains permitted (the per-company
$-per-quality-point figure only).

## Structure

```
NEXUS Intelligence/
  README.md                      this file
  companies/
    frontier-five/                Anthropic, OpenAI, Databricks, xAI/SpaceX, SSI
    extended-coverage/             Perplexity, Scale AI, CoreWeave, Cursor,
                                    Cerebras Systems, ElevenLabs, OpenEvidence,
                                    Mistral AI, Cohere
    ecosystem-scored/              23 further companies scored by the v3.0
                                    framework but not under deep coverage
                                    (VAST Data, Ramp, Waymo, Deel, Notion,
                                    Harvey, and others)
  system/
    aibq-pbq-scoring-framework.md  the full rubric: dimensions, weights,
                                    thresholds, stage gates, sector codes
    canon-and-governance.md        canonical figures, methodology rulings,
                                    frozen conflicts, sweep tracker (embargo
                                    redaction applied)
    architecture-and-doctrine.md   how NEXUS itself is built and run: three
                                    generations of company stores, the
                                    legacy-to-v2 migration, the 12 standard
                                    output products, operating discipline
    data-source-map.md             every Notion database found (78),
                                    row counts, collection IDs, for a
                                    future refresh
  digests/
    INDEX.md                       chronological index
    <date>.md                      108 dated Morning Digest bodies,
                                    2026-04-19 through 2026-08-10
  markets-and-research/
    forecasts.md                   96 logged, tracked forecasts
    valuations.md                  valuation history across the universe
    ipo-pipeline.md                IPO readiness scoring
    research-reports.md            the report registry
    cost-architecture-and-capex.md cost, hyperscaler capex, secondary market
  hypd/
    deal-pipeline.md                early-stage venture scouting funnel
    startup-screening-memo.md       the dated Pursue/Watch/Pass memo
    fund-formation-README.md        pointer to fund-ops docs (not company data)
  excel/
    NEXUS_Master_Workbook.xlsx     17-sheet structured mirror of every
                                    database above, for filtering/pivoting
```

## Source

- Notion workspace: **Nexus** (`06b5e7ad-9f7f-81aa-8309-0003938a801b`)
- 78 databases catalogued across five architectural layers: a legacy
  master Companies store, a Command Center intermediate layer, the
  current v2 spine + Signal Processing databases, AIBQ Analytics
  (including a 666-row scored-unicorn universe), the v3.0 scoring
  framework, and the Canon governance layer.
- Extracted 2026-08-11 by a fleet of extraction and synthesis agents,
  reading every reachable page and database via Notion's view-mode query
  API (SQL mode avoided once the workspace's shared quota ran low).

## What did not make it into this mirror, and why

- **Raw per-company timeline feeds.** The "Company Timelines" hub holds
  one legacy harvester database per company running into the thousands
  of rows each (Anthropic and OpenAI alone exceeded 6,800 rows each and
  pagination did not fully complete even after multiple passes) — almost
  all undated auto-scraped news debris. The system's own migration design
  (`system/architecture-and-doctrine.md` §2) confirms this feed is
  superseded by the curated, deduplicated **v2 Event Timeline** and
  **Master Events** databases, which *are* mirrored here in full (238 +
  52 rows). Each company's dated, deduplicated event subset — 3,362
  events total — is mirrored in the Excel workbook's "Company Events
  (dated)" sheet and in each company profile's Notable Events section.
- **HYPD fund-formation operations.** AngelList mechanics, brand specs,
  and ops manuals for the HYPD Ventures fund vehicle itself — not
  portfolio-company data. Indexed but not reproduced in `hypd/`.
- **triforge and Signal Nine.** Two unrelated automated trading systems
  living in the same workspace. Noted in `system/architecture-and-doctrine.md`
  but out of scope for a company-intelligence mirror.
- **Layer H Ventures CRM.** A separate deal-pipeline workspace, already
  mirrored and then removed from this repo at the user's request; not
  re-included here.
- **The embargoed coefficient.** By design, everywhere. See above.

## Refreshing this mirror

1. Re-run the same page/database sweep against the `Nexus` Notion
   workspace (`system/data-source-map.md` has every collection ID).
2. Prefer `notion-query-data-sources` in **view mode** — it does not draw
   against the workspace's shared SQL quota, which this extraction ran
   into partway through.
3. Rebuild company profiles from the merged per-company data bundle
   (join by company name across the legacy store, v2 registry, AIBQ
   scores, and Canon dossier).
4. Re-apply the embargo redaction pass to every generated file and to the
   Excel workbook before committing — verify with a search for the
   embargoed figure (Ruling 2's `Value Numeric` in the Canon export;
   check every minus-glyph variant, not just ASCII hyphen — a prior
   refresh missed the digest archive this way) as a final check before
   shipping.
5. Commit with message `nexus: <date> intelligence mirror refresh`.
