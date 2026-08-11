# Analyst Report Engine: agent runbook

This repo is an automated research-report factory. Deterministic Python
(`engine/`) handles storage, trends, charts, build, and QA; the agent (you)
handles research judgment, tiering, and prose. A report request goes in; a
gated, styled, validated docx/pdf comes out.

## The pipeline (run these stages in order for any report request)

```
0 INTAKE    read the request ("Report Automation/requests/queue/*.json" or the
            pasted prompt); create reports/<slug-or-topic>-<template>-<date>/
            with request.json. New company? python3 -m engine add <slug> "<Name>"
1 RESEARCH  FIRST ingest analyst-provided material: uploads/ (documents/ +
            links.md queue) and the company's companies/<slug>/<category>/
            drop folders; tier it like any source, file uploads into the right
            company folder, log links under Ingested. THEN live pull per
            company (protocol below). Write reports/<id>/research/snapshot.json
            as Fact dicts with tier+as_of
2 STORE     python3 -m engine snapshot <slug> <snapshot.json>
            (immutable snapshot + freeze-on-conflict merge into canonical)
3 TRENDS    python3 -m engine digest <slug>   -> what changed, what fired,
            what went stale; this digest DRIVES the report's Signal section.
            Then python3 -m engine export <slug> to refresh PROFILE.md
4 COMPOSE   pick report_template/<template>.json; write blocks/NN_name.json per
            section in the block grammar (engine/compose.py docstring),
            following style/STYLE.md + style/STYLE_PROFILE.md and the writing
            standard in README.md; auto sections via
            engine.compose.tracker_blocks / fact_sheet_blocks
5 CHARTS    write charts.json specs (types in engine/charts.py CHART_TYPES);
            python3 -m engine charts reports/<id>/charts.json
6 BUILD     python3 -m engine build reports/<id>   (docx + pdf + measured TOC;
            QA FAIL blocks the build and deletes the docx)
7 VALIDATE  write reports/<id>/validation_log.md: one ledger line per
            load-bearing claim (value, sources, tier, cross-check,
            confidence), conflicts frozen, embargo check, QA overrides,
            Report Ship gate checklist ticked
8 SHIP      git add the report dir + companies/ changes; commit; push. Move the
            request file from "Report Automation/requests/queue/" to
            "Report Automation/requests/archive/".
```

README.md at the repo root is the report-writing standard (structure, voice,
sourcing, gate); this runbook operationalizes it. On conflict, README wins on
editorial questions, this file on tooling.

A report is DONE only when the Report Ship gate in its validation log is all
true. Any false box = not done (fix and re-assert). Never leave TODOs.

Fresh container? Run `bash "Report Automation/scripts/setup.sh"` before stage 6 (installs
python-docx/matplotlib/openpyxl + libreoffice-writer + poppler-utils; without
the latter two the build ships docx-only and that gap must be flagged).

## Research protocol

Sources, in tier order:
- T1: SEC EDGAR (`https://data.sec.gov/submissions/CIK##########.json`),
  audited filings, 8-K/10-Q/S-1.
- T2: PitchBook Premium MCP (primary structured source) + company
  announcements. Key tools: `pitchbook_get_profile` (pbid in
  companies/universe.json), `pitchbook_get_company_deals`,
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
6. Em-dashes SPARINGLY: more than 2 per block warns, more than 8 per document
   fails the build. Never as a comma substitute or rhythm tic.
7. Report prose names sources by KIND + date (company disclosure, PitchBook
   deal record, SEC EDGAR, press reports); outlet names live only in the
   validation log.

## Style

Follow style/STYLE.md (prescriptive; embeds the five-rule pre-flight checklist
from style/Institutional_Research_Style_Guide.pdf and the adopted findings of
style/WRITING_STYLES_RESEARCH.md) + style/STYLE_PROFILE.md (measured).

VOICE: the Hemingway-analyst register. Short declarative core; subject, verb,
object; one fact or judgment per sentence; concrete subjects doing things.
The flow rule: each sentence opens from what the reader just learned and
closes on the new thing (stress position); the chain of sentences IS the
analysis, so connective filler is neither needed nor allowed. Long sentences
carry one evidence chain and earn a short declarative after. 25-word review
trigger. Depth goes below the waterline: exhibits, tables, the store.

ESTIMATIVE DISCIPLINE (ICD 203): key forward judgments carry lexicon words
with parenthetical ranges ("very likely (80-95%)"); confidence is a separate
sentence stating why; "possible" is never modified; one odds-bearing word per
sentence; reports making forward calls include the lexicon box
(engine.compose.lexicon_blocks). Log every parenthetical probability in the
validation log with date + resolution criterion.

Punchline first: every opening sentence and every takeaway lead IS the
finding with its metric, never a rhetorical hook. Delete emphasis adjectives,
insert the metric. Three-beat every analytical passage and tie every metric
to multiples, exit timelines, capital efficiency, or risk. Updates carry a
"what changed since our last note" line near the top. Verdict takes a
position and names the falsifier with dated kill criteria. The call passes
ENTER before ship (Expectational, Novel, Thorough, Examinable, Revealing);
a call failing Novel becomes a monitoring line, not a report. After every
shipped report, re-run
`python3 -m engine style` so the corpus keeps teaching the profiler, and drop
any externally produced reports into previous_reports/.

## Templates

The MASTER template is report_template/Vertical_Analyst_Note_10.docx
(analyst-provided), encoded as vertical_analyst_note.json and rendered by the
builder's `analyst_note` theme: production metadata sheet as page 1 (fill
every field in report.json "production"), Key takeaways (h2, bulleted, every
bullet carries a figure), 2-4 h2 sections with charts (captions <= 30 words;
build warns past it), numbered References rendered from report.json
"references" (outlets and URLs belong there, not in prose). Default template
unless the request says otherwise.

The other report_template/*.json contracts (initiation_note, company_update,
rush_note, earnings_note, one_pager, sector_overview) cover deep-dive and
specialty formats in the "house" theme. `required` entries are the editorial
contract; check each before ship. Custom section lists from a request are
legitimate; the engine renders whatever blocks exist.

## Tracker refresh (scheduled or on demand)

For each company in companies/universe.json (or the requested subset):
1. `pitchbook_get_profile` (+ targeted news query if the profile moved)
2. Write snapshot -> `python3 -m engine snapshot <slug> <file>`
3. `python3 -m engine digest <slug>`; update trigger statuses;
   `python3 -m engine export <slug>` to refresh the readable PROFILE.md
4. `python3 -m engine cohort` for the cross-company view
5. If a named trigger fired or a material field moved (valuation, mark
   status, run-rate print, S-1, leadership), START A REPORT REQUEST:
   write "Report Automation/requests/queue/<slug>-update-<date>.json"
   (template company_update, the trend digest as the idea) and process it, or
   surface it if the run is refresh-only. Commit companies/ changes either way
   with message "tracker: <date> refresh (<n> companies, <changes> changes)".

## Commits

Commit after every completed stage-8 ship and every tracker refresh. Never
commit a report whose build failed QA. Branch per standing instructions;
never force-push over history.
