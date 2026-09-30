# Methodology

How the record is built, tiered, verified and turned into a model. Rigor 4 throughout
(external artifact); every load-bearing figure travels the six-gate validation spine.

## 1. Source tiers

| Tier | Definition | Typical sources in this record |
|---|---|---|
| T1 | Primary or audited document | SEC filings (SpaceX S-1/10-Q; Amazon 10-Q), court dockets and orders (Bartz, Concord, Anthropic v. DoD, US v. Bankman-Fried), anthropic.com announcements, model/system cards, pricing pages, arXiv papers, government releases |
| T2 | Reputable/official | Bloomberg, Reuters, WSJ, FT, CNBC, Axios; official partner statements; PitchBook profile and deal fields |
| T3 | Single-source/specialist | The Information scoops, PitchBook financing-status notes, analyst estimates, vendor benchmark claims |
| T4 | Aggregator/secondary | Sacra, Crunchbase, Wikipedia, IPO-tracker blogs (lead-finders only) |
| T5 | Anonymous/social | never load-bearing |

An event inherits the tier of its weakest load-bearing source. When two agents found the same
event from different origins, the second origin is recorded as corroboration and the event's
`independent_sources` count rises; the same wire re-reported by several outlets counts once.

## 2. Confidence tags

`CANONICAL` (verified, cross-checked, locked) · `HIGH` (T1/T2 with an independent second origin)
· `MEDIUM` (single good source) · `LOW` · `VERIFY` (open check; ships only with the flag visible)
· `DISPUTED` (frozen conflict; both values shown, neither chosen).

## 3. Freeze-on-conflict

Sources disagreeing by more than 10% at comparable tiers are frozen. Before calling something a
conflict the desk rules out: pre- vs post-money; announced vs closed; "up to" vs funded; run-rate
vs recognized revenue; gross vs net basis; calendar vs fiscal period. Cross-agent numeric mismatches
are detected mechanically in `scripts/merge.py` and listed on the Sources & ledger desk.

## 4. Known traps screened on every figure

- PitchBook "TTM 4Q2026 / 4Q2027" revenue fields are forward projections, not current run-rate.
- Anthropic reports revenue gross of cloud-partner resale; OpenAI reports net. The equalization
  haircut (39.75%, canonical Jul 16 2026) is applied as a labeled toggle in the model, never silently.
- Strategic "investments" are often notes with options ("up to $4B" = $1.25B note + option).
- Compute headlines mix cumulative multi-year contract value with annual spend and with "up to"
  capacity; the ledger records the basis of every dollar and gigawatt.
- Debt is never counted as equity raised; the capital summary shows both bases.

## 5. Dedupe rules (merge.py)

Two findings are the same event when they cite the same URL within 45 days, or fall within 3 days
with ≥45% token overlap and a shared category, or within 3 days with ≥30% overlap and the same
headline number. The higher-tier source becomes primary; the rest become corroboration.

## 6. Model conventions

- Annual build 2024A–2030E; segments interpolate linearly from the 2026 mix to the 2030 mix.
- Gross margin path is an input per year; inference is a stated share of cost of revenue.
- Two operating-income definitions (ex-training and incl.-training) mirror the breakevens in
  the April 2026 investor documents reported by the WSJ.
- FCF = operating income incl. training − cash tax + SBC − compute capex/prepayments.
- Reverse DCF: each mark's required 2030 revenue solves EV = PV(FCF 2026–29) +
  PV(2030 FCF × (1 + terminal multiple)) at the model's 2030 FCF margin.
- The browser engine (`assets/app.js`) and the Python twin (`scripts/model.py`) share formulas;
  the Python output is the shipped reference in `data/model.json`.

## 7. Agents

Briefs are self-contained (role, objective, inputs, fence, hard rules, output contract). Producers
draft; checkers never see a producer's reasoning; the Certifier defaults to NEEDS WORK. The
agent log shown on the Agents floor is the real dispatch log with real timestamps.

## 8. Disclosures

All inputs are public. Bigdata.com was not called (retired in the desk's tool registry).
Model-portfolio disclosure per project context: Anthropic 6% overweight, OpenAI 2% underweight.
