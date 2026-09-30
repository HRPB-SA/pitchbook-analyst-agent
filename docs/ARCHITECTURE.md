# Anthropic Intelligence Desk — Architecture & Operating Plan

**Status:** v1 · 2026-09-30 · Rigor 4 (external artifact feeding an IPO-window view)
**Owner:** Harrison Rolfes · **Built by:** the agent pipeline described here
**Repo:** `HRPB-SA/pitchbook-analyst-agent` · branch `claude/gifted-keller-ec8zdz`

---

## 0. The one-paragraph version

Capture everything Anthropic PBC has done since founding (Jan 2021) through today, as a
date-ordered, source-verified event record with structured extractions (capital, valuation,
revenue, compute, product, governance, moat, people, connected companies). Synthesize that record
by topic, drive a segment-level financial model and a compute-cost decomposition off it, reach a
bull/bear verdict with named thesis-breakers, and publish all of it in a single-page dashboard
whose last tab shows the agents that did the work — the real dispatch log, their messages to each
other, and the flags they raised when they found new or conflicting information.

**State of play at build time (calibrated 2026-09-30):** Anthropic is still private. Confidential
S-1 filed Jun 1 2026; Nasdaq selected; WSJ (Sep 18) reports a November listing target; prospectus
details leaked via Reuters/TechCrunch Sep 28–29; up to ~$100B raise at ~$2T (PitchBook note Sep 21,
T3). Run-rate >$65B at end-July (Bloomberg Aug 17, T2). Last priced round: Series H $65B at $965B
post (May 28 2026, PitchBook T2). Sonnet 5.5 shipped Sep 28. This dashboard is therefore a
pre-IPO reference, built to be refreshed when the public S-1 lands.

---

## 1. Objectives → deliverables

| # | User ask | Deliverable | Where |
|---|---|---|---|
| 1 | Capture as much information as possible, ordered by date, one-sentence summary, URL, extracted fields | `data/events.json` (master timeline) + Timeline tab | `data/`, `dashboard/` |
| 2 | Organized analysis by topic | `data/topics.json` + Topics tab | same |
| 3 | Financial model fed by the data | `data/model.json` (assumptions, 3 scenarios, outputs) + interactive Model tab; `scripts/model.py` recomputes | same |
| 4 | Bullish or bearish, with support | `data/thesis.json` + Bull/Bear tab (verdict, thesis-breakers with metric/threshold/date) | same |
| 5 | Compute costs and every aspect of revenue/cost/strategy at granularity | `data/compute.json` + Compute tab; segment build in Model tab | same |
| 6 | Public and private companies attached to Anthropic | `data/entities.json` + Network tab | same |
| 7 | Agents visible doing the work, communicating, raising a sign on new info | `data/agent_log.json` (real dispatch log) + Agents tab (office view, replay + live) | same |
| 8 | Full picture since the beginning | this plan, plus `docs/METHODOLOGY.md` and `docs/VALIDATION_LEDGER.md` | `docs/` |

---

## 2. Sources and the tier ladder

Every event carries the tier of its weakest load-bearing source (harrison-validation).

| Tier | What | Examples used here |
|---|---|---|
| T1 | Primary / audited | SEC filings (SpaceX S-1 for the Colossus contract; Anthropic S-1 when public), court dockets (Bartz v. Anthropic, Anthropic v. DoD), `anthropic.com/news`, model/system cards, pricing pages, partner press releases |
| T2 | Reputable / official | Bloomberg, Reuters, WSJ, FT, CNBC, official company statements, **PitchBook profile and deal fields** (pulled live: PBID 466959-97) |
| T3 | Single-source / specialist | The Information scoops, analyst estimates, PitchBook financing-status *notes* |
| T4 | Aggregator / secondary | Sacra, Wikipedia, IPO-tracker blogs — used to *find* primary sources, cited only when nothing better exists |
| T5 | Anonymous / social | never load-bearing |

**Live data pulled at build:** PitchBook profile, full financing history (deals), investor list
(305 active), financials (TTM series — treated as *forward projections*, per Methodology Ruling 4),
team members, and the PitchBook news index. **Bigdata.com is not called** (retired in the tool
registry Jun 15 2026; flagged per graceful degradation).

**Known traps screened on every figure:** forward TTM fields read as current run-rate ·
gross vs net revenue (Anthropic reports gross incl. cloud-partner resale) · "up to" commitments vs
funded amounts · announced vs closed rounds · debt counted as equity raised · one wire re-reported
by many logos counted as multiple sources.

---

## 3. Data model (one source of truth per entity)

```
data/
  events.json        master timeline, date-ordered, deduped   ← the record
  entities.json      companies/people/institutions attached to Anthropic, typed, public/private, ticker
  metrics.json       time series: valuation, run-rate, quarterly revenue, raised, headcount, compute $ / GW
  topics.json        per-topic synthesis (what happened → what it means → implications)
  model.json         assumptions + computed outputs, bull/base/bear
  compute.json       compute commitments by partner, chip mix, GW, $/yr, inference vs training, unit economics
  thesis.json        bull case, bear case, verdict, thesis-breakers, flip conditions
  agent_log.json     real agent activity: dispatches, searches, opens, finds, flags, messages
  ledger.json        validation ledger: one line per load-bearing claim
  raw/               PitchBook dumps and agent outputs as received
```

### Event schema
```json
{
  "id": "evt-20260528-series-h",
  "date": "2026-05-28", "date_precision": "day",
  "headline": "Series H: $65B at $965B post-money",
  "summary": "One sentence saying what this is about.",
  "category": ["funding","valuation"],
  "source": {"url": "…", "publisher": "…", "title": "…", "published": "2026-05-28", "tier": "T2", "opened": true},
  "corroboration": [{"url": "…", "publisher": "…", "tier": "T2"}],
  "extracted": {
    "amount_usd_m": 65000, "valuation_post_usd_m": 965000, "valuation_pre_usd_m": 900000,
    "revenue_run_rate_usd_m": null, "revenue_period_usd_m": null, "revenue_period": null,
    "margin_pct": null, "margin_type": null,
    "compute": {"partner": null, "chips": null, "gw": null, "usd_m": null, "term": null},
    "product": {"name": null, "type": null, "price_in_per_mtok": null, "price_out_per_mtok": null, "context_window": null},
    "governance": null, "moat": null, "strategy": null,
    "people": [], "entities": [{"name": "Dragoneer", "type": "investor", "public": false, "ticker": null}],
    "headcount": null, "customers": null, "other": {}
  },
  "confidence": "HIGH | MEDIUM | LOW | VERIFY | DISPUTED | CANONICAL",
  "notes": "period/methodology caveats",
  "agent": "desk-deals"
}
```

### Agent-log schema
```json
{"t": "2026-09-30T15:02:11Z", "agent": "scout-2026q3", "type": "flag",
 "text": "Nscale $45B cloud deal (CNBC Aug 26) is not in the canonical compute list",
 "url": "https://www.cnbc.com/…", "to": "desk-compute", "event_id": "evt-20260826-nscale"}
```
Types: `dispatch · search · open · found · flag · verify · message · note · done`. The Agents tab
renders `flag` as a raised sign, `message` as a line between desks, everything else as activity.

---

## 4. The agent roster and the waves

The bench rule: briefs are self-contained; checkers never see a producer's reasoning; producers
draft, nothing ships from a subagent; max 3 produce→check cycles per item.

### Wave 1 — Research (16 agents, parallel, independent slices)
| Agent | Slice | Min events |
|---|---|---|
| scout-2021-2022 | founding → Dec 2022 | 20 |
| scout-2023 | 2023 | 30 |
| scout-2024 | 2024 | 35 |
| scout-2025h1 | Jan–Jun 2025 | 35 |
| scout-2025h2 | Jul–Dec 2025 | 45 |
| scout-2026q1 | Jan–Mar 2026 | 35 |
| scout-2026q2 | Apr–Jun 2026 | 35 |
| scout-2026q3 | Jul 1 – Sep 30 2026 (post-training-cutoff; search-only) | 40 |
| desk-deals | every round, valuation, secondary, tender, debt, IPO process | 30 |
| desk-compute | every compute / chip / data-center / energy commitment, $ and GW | 30 |
| desk-product | every model, product, pricing change, benchmark claim | 45 |
| desk-revenue | every run-rate, quarterly revenue, margin, burn, customer count, projection | 30 |
| desk-governance | PBC, LTBT, board, RSP/ASL, safety, policy, government, international | 35 |
| desk-legal | litigation, settlements, regulatory actions, security incidents, controversies | 25 |
| desk-ecosystem | partners, customers, acquisitions, investments made, competitors, market share | 35 |
| desk-s1 | everything reported from the confidential/leaked prospectus and IPO structure | 20 |

Era scouts give coverage; topic desks give depth; overlap is intentional and resolved in Wave 2
(the same event found by two agents with independent sources is a cross-check, not a duplicate).

### Wave 2 — Merge and verify (script + 3 agents)
- `scripts/merge.py`: normalize, dedupe (date ± 3 days + fuzzy headline + same category), merge
  sources into `corroboration`, sort, emit `events.json`, `metrics.json`, `entities.json`, and
  `agent_log.json` (from every agent's log with real timestamps).
- **Source Re-deriver A (capital):** re-derives every round size, pre/post valuation, total
  raised (equity-only vs incl. debt), investor leads from PitchBook + T1/T2, from the claims list only.
- **Source Re-deriver B (operating):** re-derives run-rate series, quarterly revenue, margins,
  headcount, compute commitments ($, GW, term) from primary sources.
- **Canonical Reconciler:** compares the merged record against `harrison-project-context`
  canonical figures; every mismatch is frozen `[DISPUTED]` with both values, never chosen.

### Wave 3 — Analysis (6 agents)
- **Topic Analysts** (revenue · compute economics · product/moat · governance/regulatory · capital/IPO ·
  legal/risk): three-beat per topic — what happened (sourced) → mechanism → implications; second-order.
- **Financial Modeler:** builds `model.json` assumptions from the verified record (see §6).
- **Compute Economist:** builds `compute.json` (see §7).
- **Bull Analyst / Bear Analyst:** equal evidentiary standard; thesis-breakers with metric, threshold, date.
- **Judge:** verdict + what would flip it; checks against the House View (valuation–quality paradox,
  equalization ruling, IPO-absorption thesis).

### Wave 4 — Build and certify
- Dashboard build (dataviz + artifact-design + web-studio skills).
- **Certifier:** default NEEDS WORK; recomputes every composite shown; checks every KPI tile against
  `events.json`; screenshots as evidence; READY only on evidence.
- Commit, push, publish (Artifact link + Vercel-ready static).

---

## 5. Topic analysis frame (Topics tab)

Ten topics, each rendered as a card with: key metrics (linked to events), a three-beat analysis,
second-order implications, what to watch (dated), and the evidence list.

1. Capital & valuation (rounds, marks, secondaries, dilution, IPO structure)
2. Revenue & unit economics (run-rate curve, quarterly revenue, mix: API vs Claude Code vs
   subscriptions vs cloud-partner resale, NRR, customer counts, gross-vs-net basis)
3. Compute & infrastructure (commitments by partner, chip strategy, GW, ownership vs rental)
4. Product & models (release cadence, pricing curve, context, benchmarks, agents/Claude Code)
5. Moat & competition (coding share, enterprise share, switching costs, distribution via clouds,
   OpenAI/Google/xAI/DeepSeek/open-weights pressure)
6. Governance & safety (PBC, LTBT, board, RSP/ASL, super-voting proposal, dual-class)
7. Legal & regulatory (copyright, DoD dispute, BIS/export controls, state/federal policy)
8. Government & policy (contracts, positions, international expansion)
9. People & organization (founders, exec hires/departures, headcount, culture signals)
10. Ecosystem (investors, cloud partners, chip suppliers, customers, acquisitions, portfolio)

---

## 6. Financial model design (Model tab; `scripts/model.py` → `model.json`)

**Basis discipline first.** Anthropic reports revenue **gross** (incl. cloud-partner resale);
OpenAI reports net. Every comparable line states its basis; the equalization ruling (39.75%
gross-to-net haircut, canonical Jul 16 2026) is applied as a toggle, never silently.

**Revenue build (annual 2023A–2030E, quarterly 2025A–2026E):**
- Segments: API direct · Cloud-partner resale (Bedrock/Vertex/Azure Foundry) · Claude Code /
  developer tools · Enterprise seats (Team/Enterprise) · Consumer subscriptions (Pro/Max) ·
  Government/other. Each = customers × ARPU or tokens × price, with a growth decay curve.
- Anchors: run-rate series (T2), Q1'26 $4.73B / Q2'26 $11.5B, FY25 $9–10B [DISPUTED basis],
  PitchBook forward TTM $65B (4Q26) / $71B (4Q27) shown as *projection references only*.
- Price deflation curve from the pricing desk (per-token price by model generation).

**Cost build:**
- Cost of revenue: inference compute ($/M tokens served × tokens), cloud partner revenue share,
  hosting; → gross margin path (canonical: −94% → 40% → 63% (2027E) → 77% (2028E), source WSJ
  Apr 6 investor docs, T3).
- Training compute (capitalized vs expensed toggle), R&D headcount × cost, S&M, G&A, SBC.
- Operating income, two breakevens (excl-training 2025 / incl-training 2028 per WSJ docs), FCF with
  compute prepayment schedule, cumulative burn vs equity + debt raised.

**Valuation:** EV/run-rate and EV/NTM revenue vs the frontier comp set (OpenAI $852B / ~$25B net;
SPCX segment SOTP; Databricks $134B / $5.4B) on gross AND equalized bases; reverse-DCF stating what
growth/margin path a $965B, $1.5T (secondary), and $2T (IPO target) mark each require.
**Scenarios:** bull / base / bear with the swing drivers (price deflation, share of coding, gross
margin, compute cost/GW, IPO absorption). Sliders on the tab recompute live in the browser.

---

## 7. Compute decomposition (Compute tab; `compute.json`)

- **Commitments table:** partner · chip · $ · GW · term · start · status (announced/contracted/live)
  · source tier — AWS/Trainium (Project Rainier), Google TPU (up to 1M TPUs / >1GW), Microsoft Azure
  ($30B), Nvidia, SpaceX Colossus ($1.25B/mo, T1), Fluidstack ($50B DCs), Nscale ($45B, Aug 2026),
  AMD (talks), Broadcom (reported), others found by desk-compute. "Up to" vs contracted split.
- **Cost stack:** $/GW-year by chip class → $/M tokens served → gross margin bridge; inference vs
  training split; owned vs rented; prepayment vs pay-as-you-go; power contracts.
- **Strategy read:** multi-cloud hedging, chip diversification (TPU/Trainium/GPU), vendor financing
  (Nvidia/Microsoft/Amazon investing the money they get back as compute spend — circularity flagged),
  the $34.5B chip bonds, and what a 1GW → multi-GW path implies for capex and margins.

---

## 8. Dashboard design (single-page app, no build step)

`dashboard/index.html` (+ `app.js`, `styles.css`) reading `data/*.json`. Static hosting on Vercel
(`vercel.json`), also published as a Claude Artifact with the JSON as supporting files.

**Register:** institutional research desk — dense, calm, dark-and-light aware, numerals-forward,
one differentiator: the agents floor. Design system tokens on `:root`; charts follow the dataviz
skill (one categorical palette, sequential for time, direct labels, no chartjunk).

**Tabs**
1. **Overview** — KPI tiles (valuation, run-rate, Q2 revenue, raised equity vs debt, compute commitments,
   headcount, IPO status), verdict badge, valuation step chart, run-rate curve, latest flags.
2. **Timeline** — the record: filter by year/category/tier/confidence, full-text search, each row =
   date · summary · source · extracted chips · tier/confidence; click → detail drawer.
3. **Topics** — ten cards (§5) with linked evidence.
4. **Model** — assumptions panel with sliders, segment revenue build, cost stack, margin path,
   FCF, valuation bridge, scenario table, basis toggle (gross/equalized).
5. **Compute** — commitments table, $ and GW stacked by partner over time, cost stack, circularity map.
6. **Bull / Bear** — two columns, verdict, thesis-breakers table (metric · threshold · date · status).
7. **Network** — force graph of entities (investor / cloud / chip / customer / competitor /
   acquired / portfolio / regulator), public companies with tickers.
8. **Agents** — the office floor: desks by wave, status rings, live feed of the real log, animated
   messages between agents, flags raised as signs, counters, replay scrubber (play/pause/speed) and a
   Live mode that polls `agent_log.json`.
9. **Sources & Ledger** — validation ledger, tier distribution, open [VERIFY]/[DISPUTED] items,
   methodology notes, MNPI/COI disclosure.

**States:** loading / empty / error handled; responsive to phone width; keyboard-navigable tabs.

---

## 9. Validation and ship gates (Rigor 4)

- Gate 1–4 on every load-bearing figure (tier, cross-check, conflict-freeze, confidence tag).
- Gate 5 red-team run independently (Source Re-derivers + Certifier never see producer reasoning).
- Adversarial defensibility: for each attackable claim the defense is in the artifact (notes field,
  ledger line), not in my head.
- Ship decision: [VERIFY]/[DISPUTED] figures ship only with the flag visible in the UI.
- MNPI/COI: inputs are public web sources plus licensed PitchBook Premium content (not public; licence
  check before sharing). The S-1 is confidential: any figure from a leaked or reported prospectus is
  press-reported (T2/T3), labelled, and subject to the reader's compliance review. Portfolio disclosure
  (Anthropic 6% overweight, OpenAI 2% underweight in the model portfolio per project context dated
  Feb 27, to be re-verified) is shown on the Sources tab and is never used as evidence.

Gate checklist (asserted before "done"):
- [ ] `events.json` ≥ 300 deduped events, every one with an opened URL
- [ ] every KPI tile traces to an event id
- [ ] every model driver traces to a sourced figure (model.json `sources` map)
- [ ] scenario table + sensitivity present; reverse-DCF stated
- [ ] compute table reconciles to the commitments total shown on Overview
- [ ] bull/bear thesis-breakers each carry metric · threshold · date
- [ ] agent_log.json is the real log (no fabricated activity)
- [ ] Certifier verdict READY with evidence
- [ ] committed and pushed; Artifact published

---

## 10. Refresh path

- `scripts/refresh.py` (Wave 4) re-runs the roster briefs against the Claude API with web search,
  appends to `agent_log.json`, and re-merges. Intended cadence: weekly until the public S-1, then
  on every filing/event. Can be wired to a Claude Code Remote routine on request.
- On the public S-1: `desk-s1` re-runs against the primary document and every T3 prospectus-leak
  figure is re-tiered to T1 or cut.

---

## 11. Decisions and tradeoffs taken

- **Single-file static dashboard over a framework app.** Zero build step, deployable anywhere,
  Artifact-publishable. Tradeoff: no server-side auth; the data is public anyway.
- **Real agent log over a simulated one.** The Agents tab replays what actually happened this
  session; a Live mode covers future refresh runs. Tradeoff: the first replay is a fixed recording.
- **Model in the browser (JS) with a Python twin.** Sliders need client-side recompute; the Python
  script is the auditable reference and produces the shipped `model.json`. An `.xlsx` export is a
  follow-on, not in this pass.
- **Breadth via era scouts + depth via topic desks.** Duplicates cost merge effort but yield
  cross-checks for free; the alternative (one agent per topic only) misses the long tail.
