# Architecture

```
                     ┌─────────────────────────────┐
   idea typed  ───►  │  DASHBOARD (artifact/html)  │
                     │  request JSON + launch      │
                     └──────────┬──────────────────┘
                                │ paste prompt / commit to "Report Automation/requests/queue/"
                                ▼
                ┌────────────────────────────────────┐
                │  AGENT SESSION (Claude Code, this  │
                │  repo; CLAUDE.md = runbook)        │
                │                                    │
                │  research: PitchBook MCP · news ·  │
                │  web search · SEC EDGAR            │
                │  judgment: tiering, conflicts,     │
                │  prose in house style              │
                └───────┬────────────────────────────┘
                        │ Fact snapshots  · blocks.json · charts.json
                        ▼
   ┌────────────────────────────────────────────────────┐
   │  ENGINE (deterministic, python3 -m engine)         │
   │                                                    │
   │  store    append-only snapshots; freeze-on-conflict│
   │           canonical merge; decay staleness         │
   │  trends   ladders · deltas · derived (CE equity-   │
   │           only, multiples, $/pt) · trigger states  │
   │  style    measured profile from shipped library    │
   │  compose  block grammar + auto fact/tracker tables │
   │  charts   spec-driven house factory (embargo guard)│
   │  build    template-driven docx/pdf + measured TOC  │
   │  qa       em-dash · embargo · placeholder · source │
   │           discipline gates (FAIL blocks build)     │
   └───────┬────────────────────────────────────────────┘
           ▼
   reports/<id>/output/*.docx|pdf + validation_log.md (Report Ship gate)
   companies/<slug>/store/ updated tracker state + PROFILE.md export, committed
```

## Design decisions

- **Agent researches; engine enforces.** Web scraping frontier-company data
  with fixed scrapers breaks weekly and cannot tier sources. The agent uses
  PitchBook MCP + news + EDGAR with judgment, but writes only well-formed
  Facts (value, as-of, source, tier, decay, flags) that the engine validates,
  merges, decays, and diffs deterministically. Every derived number in a
  report is recomputed by the engine at build time, never hand-typed.
- **Freeze-on-conflict in code.** A challenger supersedes only when newer AND
  at least as strong a tier; anything else lands in conflicts.json and ships
  as both values or neither. The merge cannot silently choose.
- **Templates are contracts, not scaffolding.** `required` obligations per
  section are checked at review; the Report Ship gate in the validation log
  is asserted before any ship.
- **Style is measured, then prescribed.** The profiler quantifies the shipped
  library (sentence geometry, evidence density, citation patterns); STYLE.md
  prescribes on top. Each shipped report feeds the corpus back.
- **Embargoes are load-bearing code.** The chart factory has no scatter type;
  the QA scanner fails builds on embargoed expressions and em-dashes. House
  rules that used to live in memory now live where they cannot be forgotten.
- **Two entry paths, one pipeline.** Pasted launch prompt (interactive) and
  requests/queue/ (scheduled Monday tracker + queue processor) both run the
  same CLAUDE.md pipeline, so output quality does not depend on entry path.
```
