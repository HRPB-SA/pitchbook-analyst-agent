# Anthropic Intelligence Desk

A source-verified record of everything Anthropic PBC has done since 2021, organized by date, analyzed by topic, fed into a financial model and a compute-cost
breakdown, and summarized in a bull/bear verdict. Built by a pipeline of research, verification and analysis agents whose real activity log is replayed on the
dashboard's **Agents floor** tab.

**State of the world at build time (2026-09-30):** Anthropic is private. Confidential S-1 filed Jun 1 2026. Listing timing is reported as October (PitchBook note) or
November (WSJ): treated as disputed. Last priced round: Series H, $65B at $965B post-money (May 28 2026). Re-run the pipeline when the public S-1 appears.

## What is in here

| Path | What |
|---|---|
| `index.html`, `assets/` | The dashboard: nine tabs, no build step (D3 from cdnjs, Google Fonts) |
| `data/events.json` | The record: deduped events in date order (one-sentence summary, source URL, tier, confidence, extracted fields) |
| `data/timeline.csv`, `data/anthropic_record.xlsx` | The same record as a spreadsheet, plus one sheet per desk table, conflicts and open items |
| `data/metrics.json`, `entities.json` | Time series and tables from the desks; the entity graph (public and private companies attached to Anthropic) |
| `data/topics.json`, `model.json`, `compute.json`, `thesis.json` | Topic analyses, three-scenario model, compute decomposition, bull/bear verdict |
| `data/ledger.json`, `claims_ledger.json`, `audit.json`, `health.json`, `certify.json` | Validation ledger, independent re-derivation of load-bearing claims, independent audit of a sample of the record, mechanical checks, ship gates |
| `data/agent_log.json` | The agents' own activity log (what the Agents floor replays) |
| `agents/outputs/` | Raw output of every agent, as received |
| `agents/briefs/` | The briefs each agent was given |
| `scripts/` | `merge.py`, `q.py`, `health.py`, `make_claims.py`, `reconcile.py`, `sample_audit.py`, `model.py`, `parity.cjs`, `build_analysis.py`, `certify.py`, `export_xlsx.py`, `build_artifact.py`, `shot.cjs` |
| `docs/` | `ARCHITECTURE.md` (design), `METHODOLOGY.md` (tiers, conflict rules, basis discipline, model conventions) |

## Run it locally

```bash
cd pitchbook-analyst-agent
python3 -m http.server 8080          # then open http://localhost:8080/
```

## Rebuild the data after agents add findings

```bash
cd pitchbook-analyst-agent
python3 scripts/merge.py             # dedupe + metrics + entities + agent log + timeline.csv
python3 scripts/health.py            # mechanical checks
python3 scripts/model.py             # recompute data/model.json from agents/outputs/analyst-model.json
python3 scripts/build_analysis.py    # topics.json, compute.json, thesis.json from analyst outputs
python3 scripts/export_xlsx.py       # spreadsheet export (pip install openpyxl)
```

Verification and gates (run in this order after the desks finish):

```bash
python3 scripts/make_claims.py       # claims_master (private) + question-only briefs for the independent re-derivers
#   ... re-derivers write agents/outputs/verify-capital.json and verify-operating.json ...
python3 scripts/reconcile.py         # MATCH / MISMATCH / PARTIAL / UNTRACEABLE ledger -> data/claims_ledger.json
python3 scripts/sample_audit.py      # draws the audit sample; after the auditors finish: python3 scripts/sample_audit.py --score
node scripts/parity.cjs              # model.py and computeModel() in app.js agree on every row
NODE_PATH=$(npm root -g) node scripts/shot.cjs   # headless QA of nine tabs x desktop/phone x light/dark
python3 scripts/certify.py           # mechanical ship gates -> data/certify.json (exit 1 on any FAIL)
```

## Deploy

Static site, nothing to build. From the repository root:

```bash
npm i -g vercel                      # once
vercel --cwd . --prod=false          # preview deployment; add --prod only when you want it public
```

The data files are public-facts derived from public sources and licensed PitchBook fields. **Check your PitchBook licence before publishing the site or the
repository**: `data/raw/` (raw PitchBook pulls) is git-ignored on purpose, but valuations, round sizes, investor names and team data derived from those pulls
appear in the dashboard.

To publish as a single-file page (for an artifact host): `python3 scripts/build_artifact.py` writes `dist/artifact.html` with CSS and JS inlined; publish it with the
`data/*.json` files alongside so the relative fetches keep working.

## Conventions you should know before quoting a number

- Tiers: T1 primary document, T2 Bloomberg/Reuters/WSJ/FT/CNBC/official/PitchBook field, T3 single-outlet scoop or estimate, T4 aggregator, T5 social.
- Anthropic reports revenue **gross** of cloud-partner resale; OpenAI reports **net**. The model shows both and applies a stated haircut, never silently.
- Run-rate is not recognized revenue. "Up to" is not contracted. Announced is not closed. Debt is not equity raised.
- PitchBook "TTM 4Q2026 / 4Q2027" revenue fields are forward projections, not current revenue.
- Conflicts between sources are frozen: both values are shown, neither is chosen.
- Timestamps on the Agents floor: each agent's start and finish are its own clock readings; actions inside a run are spread evenly between them.
