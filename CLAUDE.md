# Analyst Report Engine: agent runbook

This repo is an automated research-report factory. Deterministic Python
(`engine/`) handles storage, trends, charts, build, and QA; the agent (you)
handles research judgment, tiering, and prose. A report request goes in; a
gated, styled, validated docx/pdf comes out.

## The pipeline (run these stages in order for any report request)

```
0 INTAKE    read the request (requests/queue/*.json or the pasted prompt);
            create reports/<slug-or-topic>-<template>-<date>/ with request.json
1 RESEARCH  live pull per company (see protocol below); write
            reports/<id>/research/snapshot.json as Fact dicts with tier+as_of
2 STORE     python3 -m engine snapshot <slug> <snapshot.json>
            (immutable snapshot + freeze-on-conflict merge into canonical)
3 TRENDS    python3 -m engine digest <slug>   -> what changed, what fired,
            what went stale; this digest DRIVES the report's Signal section
4 COMPOSE   pick templates/<template>.json; write blocks/NN_name.json per
            section in the block grammar (engine/compose.py docstring),
            following style/STYLE.md + style/STYLE_PROFILE.md; auto sections
            via engine.compose.tracker_blocks / fact_sheet_blocks
5 CHARTS    write charts.json specs (types in engine/charts.py CHART_TYPES);
            python3 -m engine charts reports/<id>/charts.json
6 BUILD     python3 -m engine build reports/<id>   (docx + pdf + measured TOC;
            QA FAIL blocks the build and deletes the docx)
7 VALIDATE  write reports/<id>/validation_log.md: one ledger line per
            load-bearing claim (value, sources, tier, cross-check,
            confidence), conflicts frozen, embargo check, QA overrides,
            Report Ship gate checklist ticked
8 SHIP      git add the report dir + data/ changes; commit; push. Move the
            request file from requests/queue/ to requests/archive/.
```

A report is DONE only when the Report Ship gate in its validation log is all
true. Any false box = not done (fix and re-assert). Never leave TODOs.

## Research protocol

Sources, in tier order:
- T1: SEC EDGAR (`https://data.sec.gov/submissions/CIK##########.json`),
  audited filings, 8-K/10-Q/S-1.
- T2: PitchBook Premium MCP (primary structured source) + company
  announcements. Key tools: `pitchbook_get_profile` (pbid in
  data/universe.json), `pitchbook_get_company_deals`,
  `pitchbook_get_company_financials`, `pitchbook_get_company_investors`,
  `pitchbook_get_news_analysis`, `pitchbook_search` (to resolve missing
  pbids; write them back to universe.json).
- T3: press via `pitchbook_get_news_analysis` and web search/fetch.
Cross-check every load-bearing figure with at least two independent sources
where possible; note when multiple outlets trace to one ultimate source
(that is ONE source, not several). One focus and one period per news query.

**Retired tools: Bigdata.com is retired. Never call it; substitute web
search/FMP and flag the substitution.** If any source is down, substitute a
named fallback and FLAG the gap in the validation log; never silently skip.

## Store rules (engine enforces shape; you enforce judgment)

- Every value is a Fact: `{value, as_of, source, tier, decay?, flags?, note?}`.
  Estimates carry flag `est.`; open checks `VERIFY`; frozen conflicts
  `DISPUTED` (both values ship or neither).
- Freeze-on-conflict: merge supersedes only when the challenger is BOTH newer
  and at least as strong a tier; otherwise the conflict is frozen into
  conflicts.json and surfaced. Never resolve a frozen conflict silently.
- Ladders (run-rate, growth, margin, headcount, valuation marks) are
  append-only lists of dated Facts; history is never edited.
- Decay classes: VOLATILE (~14d) valuations/tape/status; QUARTERLY (~100d)
  ARR/headcount/metrics; STABLE cap structure/deal terms; PERMANENT
  definitions/events. Stale facts are cited only with visible vintage.
- Trigger review is part of every run: update `triggers.named` statuses
  (armed/fired/expired with dates) by editing the profile after merge.

## Methodology rulings (hard-coded; never drift)

1. CE denominator = EQUITY ONLY. Debt informs risk, never CE.
2. Unclosed/rumored/announced-but-unsettled financings NEVER anchor the base
   case. Analyzed as forward signals, adopted only on completion.
3. PitchBook revenue "TTM" fields are forward-window projections, NOT
   run-rate. Ladders come from dated company/media prints.
4. Anthropic reports revenue GROSS, OpenAI NET: never compare raw. Canonical
   equalization 39.75% (both at 34.1x equalized; no multiple discount).
5. EMBARGO: the quality-valuation coefficient (r=-0.99) appears nowhere; no
   score-vs-valuation scatter or fitted line (chart factory refuses); the
   per-point ladder is the only cleared expression.
6. Zero em-dashes (U+2014) in any shipped artifact; QA fails the build.
7. Report prose names sources by KIND + date (company disclosure, PitchBook
   deal record, SEC EDGAR, press reports); outlet names live only in the
   validation log.

## Style

Follow style/STYLE.md (prescriptive) + style/STYLE_PROFILE.md (measured from
the shipped library). Lead with the sharpest signal; three-beat every
analytical passage (what happened -> what it means -> implication); metaphor +
colon + literal section titles, one metaphor family per report; verdict takes
a position and names the falsifier. After every shipped report, re-run
`python3 -m engine style` so the corpus keeps teaching the profiler, and drop
any externally produced reports into reference_reports/.

## Templates

templates/*.json define section order and binding obligations per report
type (initiation_note, company_update, rush_note, earnings_note, one_pager,
sector_overview). `required` entries are the editorial contract; check each
before ship. Custom section lists from a request are legitimate; the engine
renders whatever blocks exist.

## Tracker refresh (scheduled or on demand)

For each company in data/universe.json (or the requested subset):
1. `pitchbook_get_profile` (+ targeted news query if the profile moved)
2. Write snapshot -> `python3 -m engine snapshot <slug> <file>`
3. `python3 -m engine digest <slug>`; update trigger statuses
4. `python3 -m engine cohort` for the cross-company view
5. If a named trigger fired or a material field moved (valuation, mark
   status, run-rate print, S-1, leadership), START A REPORT REQUEST:
   write requests/queue/<slug>-update-<date>.json (template company_update,
   the trend digest as the idea) and process it, or surface it if the run is
   refresh-only. Commit data/ changes either way with message
   "tracker: <date> refresh (<n> companies, <changes> changes)".

## Commits

Commit after every completed stage-8 ship and every tracker refresh. Never
commit a report whose build failed QA. Branch per standing instructions;
never force-push over history.
