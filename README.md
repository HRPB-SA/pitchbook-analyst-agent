# Anthropic Intelligence Desk

A source-verified record of everything Anthropic PBC has done since 2021, organized by date, analyzed by topic, fed into a financial model and a compute-cost
breakdown, and summarized in a bull/bear verdict. Built by a pipeline of research, verification and analysis agents whose real activity log is replayed on the
dashboard's **Agents floor** tab.

**State of the world at build time (2026-09-30):** Anthropic is private. Confidential S-1 filed Jun 1 2026. Listing timing is reported as October (PitchBook note) or
November (WSJ): treated as disputed. Last priced round: Series H, $65B at $965B post-money (May 28 2026). Re-run the pipeline when the public S-1 appears.

## What the desk concluded (as of 2026-09-30)

**Call (Judge, 12-24 months after listing): BEARISH at the reported ~$2T IPO target, NEUTRAL near $1.5T, LEAN BULLISH only at or below about $1.07T (which includes Series H at $965B).**
The call is price-conditional: no IPO price range exists (no public S-1). Reasoning and what would flip it are on the Bull / Bear tab; thesis-breakers carry a metric, threshold and date.

| Model scenario (gross revenue basis) | 2026E | 2028E | 2030E | 2030E FCF margin | DCF EV (engine) |
|---|---|---|---|---|---|
| Bear | $50.0B | $95.4B | $127.2B | 15.9% | $0.18T |
| Base (follows the company plan; an inside-view anchor) | $55.8B | $195.5B | $328.1B | 28.4% | $1.19T |
| Bull | $60.0B | $257.6B | $447.9B | 36.2% | $2.64T |

At the base FCF margin the reverse-DCF needs 2030 revenue of $262B (Series H $965B, 47% a year from FY2026), $420B (secondary mark ~$1.5T, 66%) and $568B ($2T target, 79%). The outside view (top-1,000 firms above $25B, AWS, Nvidia data center) says growth persistence is weak: every scenario, including the bear, sits above it.

What the record cannot carry, stated plainly:
- No public S-1 exists. Every FY2024/FY2025 financial is press-reported from a leaked draft prospectus (Reuters readable; FT and NYT blocked). FY2024 revenue is implied from "+1,088%".
- Anthropic books revenue gross of cloud-partner resale. The desk's canonical 39.75% equalization haircut reproduces exactly from the Jul 16 marks (it is fitted, not measured); the record's own evidence is about 7.6% (platform fees) and PitchBook's 6-10%. Both are offered in the Model tab; the verdict is unchanged under either.
- Run-rate is not recognized revenue; year-end $100B+ run-rates and the $559M Q2 operating profit are projections; "up to" compute figures are not contracted ($592.1B announced, $217.9B on T1/T2 documents, about 80% of the $518B prospectus plan non-cancelable).
- Independent checks: a cold audit of 48 sampled events found every core fact supported but only 49% fully supported (8 corrections applied, logged); four independent re-derivers checked 121 load-bearing claims (72 match, 33 text-compared, 6 partial, 7 mismatches frozen with both values shown, 3 untraceable). An independent Certifier re-derived eight load-bearing facts from source before opening any deliverable, recomputed the model, and returned READY at commit 1fd56d1 with 0 blocking and 14 non-blocking notes (Sources tab). Mechanical gates: 14 pass, 1 warn (audit full-support rate below threshold, disclosed), 0 fail. Three later edits (a bounded "Signs raised" list, a non-affiliation line, and a corrected tier-ladder sentence that resolves the Certifier's note N-26) were checked by the browser smoke test only, not re-certified.

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
| `scripts/` | `merge.py`, `q.py`, `health.py`, `make_claims.py`, `reconcile.py`, `sample_audit.py`, `model.py`, `parity.cjs`, `build_analysis.py`, `certify.py`, `export_xlsx.py`, `build_artifact.py`, `build_summary.py`, `shot.cjs` |
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

Static site, nothing to build. From the repository root (`pitchbook-analyst-agent/`):

```bash
npm i -g vercel                      # once
vercel login                         # once
vercel                               # preview deployment; when asked: link to a new project, framework "Other", output directory "."
vercel --prod                        # only when you want it on the production URL
```

`.vercelignore` keeps `data/raw/`, `agents/`, `scripts/`, `docs/` and the spreadsheet out of the deployment; the site is `index.html`, `assets/` and `data/*.json`.

The data files combine public sources and licensed PitchBook fields. **Check your PitchBook licence before publishing the site or the
repository**: `data/raw/` (raw PitchBook pulls) is git-ignored on purpose, but valuations, round sizes, investor names and team data derived from those pulls
appear in the dashboard.

To publish as a single-file page (for an artifact host): `python3 scripts/build_artifact.py` writes `dist/artifact.html` with CSS and JS inlined; publish it with the
`data/*.json` files alongside so the relative fetches keep working.

The one-page decision board (the call, the model behind it, the evidence checks, in one scrollable page) is a second single file that fetches nothing: `python3 scripts/build_summary.py`
reads `data/*.json` and `agents/outputs/certifier.json`, fills `assets/summary.template.html` and writes `dist/summary.html`. Every figure on it is computed from those files;
only labels, captions and the disclosure wording are written by hand. Rebuild it after any change to the data, then publish `dist/summary.html` on its own (no data files needed).

## Conventions you should know before quoting a number

- Tiers: T1 primary document, T2 Bloomberg/Reuters/WSJ/FT/CNBC/official/PitchBook field, T3 single-outlet scoop or estimate, T4 aggregator, T5 social.
- Anthropic reports revenue **gross** of cloud-partner resale; OpenAI reports **net**. The model shows both and applies a stated haircut, never silently.
- Run-rate is not recognized revenue. "Up to" is not contracted. Announced is not closed. Debt is not equity raised.
- PitchBook "TTM 4Q2026 / 4Q2027" revenue fields are forward projections, not current revenue.
- Conflicts between sources are frozen: both values are shown, neither is chosen.
- Timestamps on the Agents floor: each agent's start and finish are its own clock readings; actions inside a run are spread evenly between them.
