# Canon & Governance

The data-integrity layer NEXUS runs on top of its company trackers: a
canonical-figures ledger with tier and decay tracking, methodology
rulings, a frozen-conflict register, and a sweep tracker for propagating
corrections. Mirrored from the Notion "NEXUS Canon" databases, current as
of 2026-08-11.

## Embargo — read before using any figure in this file

**Ruling 2 embargoes the cross-company quality-valuation correlation
coefficient.** Its value does not appear anywhere in this repository —
not in this file, not in any company profile, not in the Excel workbook.
Where the source canonical-figures ledger carries that figure, the row is
listed below with its value withheld. The only cleared public expression
of the underlying relationship is the per-company $-per-AIBQ-point figure
already reported in each company's own profile; never reconstruct or
republish the coefficient from that ladder.

## Methodology Rulings

Ordered by ruling number; all currently Active.

### Ruling 1 — CE denominator is equity only

- **Type:** Methodology  **Status:** Active  **Effective:** 2026-06-10  **Recompute required:** no
- **Statement:** CE denominator = EQUITY RAISED ONLY. Debt — incl. Anthropic's $34.5B chip-purchase bonds, $2.5B revolver, and OpenAI's Jul-8 $520M — is excluded from CE; debt informs CI and risk, not CE.
- **Notes:** Ruling is silent on the NUMERATOR basis (gross vs net revenue) — that conflict is frozen in the Conflict Register, opened Jul 16.

### Ruling 2 — quality-valuation correlation embargoed until recompute

- **Type:** Embargo  **Status:** Active  **Effective:** 2026-06-12  **Recompute required:** yes
- **Statement:** The quality-valuation correlation [VALUE EMBARGOED — see Ruling 2] is EMBARGOED until recompute. Public expression = per-point spread ($/AIBQ-pt ladder) only. Recompute required before next media appearance.
- **Notes:** Jul-16 tape moved the xAI rung ~19% — the recompute is now also a thesis test, not just a refresh.

### Ruling 3 — Anthropic FCF-margin correction sweep pending

- **Type:** Methodology  **Status:** Active  **Effective:** 2026-06-12  **Recompute required:** yes
- **Statement:** Anthropic bear-case FCF margin was revised down significantly. Sweep ALL talking points and briefings before reuse; confirm sweep complete before the next media appearance.
- **Notes:** Tracked as the open 'Anthropic FCF-margin correction sweep' in the Sweep Tracker. Related: Q2 2026 first op profit ~$559M (T3, CNBC) under FCF-sweep review in Token Trap blockers.

### Ruling 4 — PitchBook TTM figures are forward projections

- **Type:** Trap Rule  **Status:** Active  **Effective:** 2026-06-12  **Recompute required:** no
- **Statement:** PitchBook TTM revenue fields are FORWARD PROJECTIONS, not current ARR — always cross-reference before adopting.
- **Notes:** Trap has fired on both names: OpenAI $30B TTM 4Q2026; Anthropic $55B TTM 4Q2027 (period end 2027-12-31, surfaced Jul 16). DO NOT ADOPT either as run-rate.

### Ruling 5 — Revenue equalization 39.75% (Anthropic gross->net)

- **Type:** Methodology  **Status:** Active  **Effective:** 2026-07-16  **Recompute required:** no
- **Statement:** Anthropic reports revenue GROSS (incl. cloud partner sales); OpenAI reports NET. NEVER compare the two raw. Canonical equalization = 39.75% (Basis Trade, gate-verified workbook v0.1) -> Anthropic net run-rate ~$28.3B -> $965B/$28.3B = 34.1x, IDENTICAL to OpenAI's 34.1x. THERE IS NO MULTIPLE DISCOUNT. Survivors: 81% quality premium per AIBQ point (8.20 vs 4.53) and 1.65x CE advantage (0.228x vs 0.138x). Supersedes the '20.5x vs 34.1x Anthropic inversion' framing wherever it appears.
- **Notes:** BLAST RADIUS — sweep required: The xAI Tell §5 (the Anthropic inversion) · Token Trap §5 · any talking point or media brief carrying 20.5x-vs-34.1x as a dislocation. See 'Ruling 5 equalization sweep' in the Sweep Tracker.

### Ruling 6 — AIBQ v3.0 weights

- **Type:** Methodology  **Status:** Active  **Effective:** 2026-05-27  **Recompute required:** no
- **Statement:** AIBQ v3.0: CE 20% · RQ 25% · CI 15% · GO 20% · MD 20%. Report/Standard/Exit weight configs · 24 sub-scores · Composite = weighted dims - CRA · stage-gated CE (S1-S5) · PBQ swaps CI for SV.
- **Notes:** Hub 36c5e7ad9f7f815a. Canonical scores dated May 27, 2026 and unrefreshed as of v3.4.

## Conflict Register (frozen, unresolved)

Per the store's freeze-on-conflict rule: neither branch is adopted until explicitly resolved. Both readings ship or neither.

| Conflict | Branch A | Branch B | Status | Opened | Last tested |
| --- | --- | --- | --- | --- | --- |
| Digest §13 spec — daily CFA vehicle vs excludes all FF tickers | §13 is the daily CFA vehicle. | §13 excludes all FF tickers incl. SPCX. | Frozen | 2026-06-12 | 2026-07-16 |
| Altman 'Co-CEO' field on PitchBook profile | Durable PB data error. | PB has picked up a real governance change — a Co-CEO structure at OpenAI ahead of an S-1 is material. | Frozen | 2026-06-12 | 2026-07-16 |
| CE numerator basis — Anthropic gross vs OpenAI net | Raw bases: Anthropic CE 0.38x on GROSS $47B vs OpenAI 0.14x on NET ~$25B -> ratio reads 2.71x. | Equalized (Ruling 5): Anthropic net ~$28.3B -> 0.228x vs 0.138x -> 1.65x, the figure the companion note ships. | Frozen | 2026-07-16 | 2026-07-16 |
| Token Trap date — Jul 10 doc vs Jul 14 parent ship | Companion doc is dated Jul 10, 2026. | Project-context carried it as an open PRE-SHIP task for the Jul 14 parent (Waiting for a Trillion). | Frozen | 2026-07-10 | 2026-07-16 |
| OpenAI S-1 timing — PB Sep 2026 vs Bloomberg 2027-lean | PB: September 2026 — financing note refreshed Jul 9, still carries September. | Bloomberg Jun 26 (Friar): 2027-lean · media: Q4 · Kalshi ~1-in-3 by Jan 1. | Shifted | 2026-07-02 | 2026-07-16 |
| SPCX exact break level (Jul 15) — ~6% source disagreement | Investing.com: $135.27 close Jul 15, prev close $136.08, day range $132.15-139.34, 52wk $132.15-225.64. | TradingView (Jul 16): mkt cap $1.81T, ATL $135.52 on Jul 14, +5.06% wk · CNN: opened $140.95, -$0.81. | Frozen | 2026-07-16 | 2026-07-16 |

**Digest §13 spec — daily CFA vehicle vs excludes all FF tickers** — Memory carries both readings. Resolve against the authoritative Notion spec 37d5e7ad9f7f81d7b802f51dabd881d9 — per-section rules live there, not in project-context.

**Altman 'Co-CEO' field on PitchBook profile** — ESCALATED Jul 16: 'Co-Founder, Co-Chief Executive Officer & Board Member' persists across 5+ weeks AND a live profile refresh (last-updated Jul 16) — the 'transient artifact' hypothesis is now weak. Resolve before any media appearance.

**CE numerator basis — Anthropic gross vs OpenAI net** — Ruling 1 governs the DENOMINATOR (equity only) but is silent on the numerator basis. Defect log: 3rd instance of the same basis error. Resolve the numerator basis, then sweep — blast radius is every artifact citing CE or the 2.71x ratio.

**Token Trap date — Jul 10 doc vs Jul 14 parent ship** — Date conflict unresolved. Related calendar conflict: Basis Trade anchors on the August catalyst window while Token Trap anchors on Anthropic's Oct S-1 — reconcile the two notes' calendars.

**OpenAI S-1 timing — PB Sep 2026 vs Bloomberg 2027-lean** — PB re-affirmed September 13 days AFTER Bloomberg's 2027-lean; the staleness objection ('note dated Jun 9') is DEAD. PB branch STRENGTHENED but both branches remain live. Named trigger from The xAI Tell has moved; Token Trap §5 assumes one branch — sweep.

**SPCX exact break level (Jul 15) — ~6% source disagreement** — Sources disagree ~6% on the level AND on the ATL date. THE EVENT (break below $135) is cross-confirmed T2 (CNBC/Yahoo); THE LEVEL is not. Use '~$132-141, below the $135 IPO price' until a T1/T2 close is pulled.

## Sweep Tracker

Tracks propagation of a correction across every artifact that cited the superseded figure.

- **Harrison**, opened 2026-07-16, status **Open**: Targets: The xAI Tell §5 (the Anthropic inversion) · Token Trap §5 · all media briefs / talking points carrying 20.5x-vs-34.1x as a dislocation. Replace with the equalized framing: both names 34.1x; survivors = 81% AIBQ quality premium + 1.65x CE advantage. May not close while any related citation is un-updated.
- **Harrison**, opened 2026-06-12, status **Open**: Bear case revised down significantly (Ruling 3). Targets: ALL talking points + briefings — must complete before the next media appearance. Related open check: FCF sweep pending on the ~$559M Q2 op profit (T3, CNBC) carried in Token Trap.

## Trigger Registry

| Trigger | Threshold | Status | Check frequency | Notes |
| --- | --- | --- | --- | --- |
| Anthropic $47B run-rate quarterly decay re-pull | Figure age exceeds one quarter without re-verification | Armed | Weekly | $47B is T2 May — 2.5mo old at the Jul-16 refresh, past QUARTERLY decay and flagged [VERIFY — STALE]. Beware the PB $55B TTM 4Q2027 trap on re-pull (Ruling 4). |
| PB financing-note refresh — OpenAI Sep vs 2027 branch | PB financing note moves off September 2026 | Armed | Weekly | PB note REFRESHED Jul 9, still September — staleness objection dead; PB re-affirmed 13 days after Bloomberg's Jun-26 2027-lean (Friar). Both branches live; PB branch strengthened. |
| OpenAI roadshow range vs $852B mark | Roadshow range prints above/below the $852B private mark | Armed | Weekly | Named trigger from The xAI Tell. S-1 timing itself is a frozen conflict (PB Sep vs Bloomberg 2027-lean, SHIFTED Jul 16). |
| SPCX Q2 earnings + first lockup tranche Aug 6 2026 | Aug 6, 2026 — first public print since IPO, same date as first lockup tranche | Armed | Event-Driven | First frontier-AI-adjacent public earnings event in existence. HARD CALENDAR ANCHOR — sits ahead of both S-1s. 'Q2 miss' is a Basis Trade falsifier; reconcile the two notes' calendars. |
| Anthropic Oct pricing vs OpenAI tape | Anthropic prices Oct 2026 against OpenAI's live tape | Armed | Event-Driven | PB sequencing (OpenAI Sep -> Anthropic Oct) implies the second mover inherits the first's print as ceiling or floor. October re-confirmed on the Jul-6 PB financing note (Alphabet-chip use of proceeds on the same note). |
| SPCX 30-day VWAP vs $135 | 30-day VWAP breaches the $135 IPO price | Fired | Daily | FIRED — SPCX broke below its $135 IPO price for the first time Jul 15 (CNBC/Yahoo cross-confirmed, T2); spot is through it. Exact level DISPUTED (~$132-141). Thesis hit: the inverse quality-valuation curve is partially correcting. |
| SPCX lockup unlock schedule Aug-Dec staged | ~911.5M shares unlock staged Aug 6 -> Dec 2026 [T4, VERIFY] | Armed | Event-Driven | Refines v3.3's flat '366-day lockup' — Aug 6 is the first date supply can actually move. Schedule itself is T4, VERIFY. |

## Canonical Figures Ledger

62 figures. Status counts: CANONICAL 53, STALE 5, TRAP 2, DISPUTED 1, EMBARGOED 1.

### Anthropic

| Figure | Value | Status | Tier | Decay class | Last verified | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Anthropic Series H share price $589.0095 | $589.0095/sh | CANONICAL | T2 company-announced | STABLE | 2026-07-02 | 17.33% acquired; investor ownership 62.66%; ~1,638mm implied shares. |
| Anthropic employees 5,000 | 5,000 (PB, Apr 21 datum) | CANONICAL | T2 company-announced | QUARTERLY | 2026-07-16 | Now ABOVE OpenAI's 4,500 (Mar 21). |
| Anthropic revenue multiple 34.1x equalized | 34.1x equalized | CANONICAL | T2 company-announced | VOLATILE | 2026-07-16 | $965B / ~$28.3B net (39.75% equalization). IDENTICAL to OpenAI's 34.1x — there is no multiple discount. |
| Claude Code ARR $2.5B | $2.5B ARR (54% coding share) | CANONICAL | T2 company-announced | QUARTERLY | 2026-06-12 | Ops context: 140%+ NRR; 80% enterprise; 300K+ business customers; 1,000+ at $1M+ ACV. |
| Anthropic revenue multiple 20.5x gross | 20.5x gross | CANONICAL | T2 company-announced | VOLATILE | 2026-07-16 | Ruling 5 supersedes the 20.5x-vs-34.1x DISLOCATION framing — equalized multiple is 34.1x, identical to OpenAI. Gross arithmetic itself remains valid; never compare raw to OpenAI's net. |
| Anthropic valuation $965B post | $965B post (Series H) | CANONICAL | T2 company-announced | VOLATILE | 2026-07-16 | Series H $65B closed May 28 ($900B pre; leads Dragoneer/Sequoia/Greenoaks/Altimeter). |
| Anthropic CE 0.38x gross | 0.38x CE (gross numerator) | CANONICAL | T2 company-announced | QUARTERLY | 2026-07-16 | CONFLICT (opened Jul 16): CE column mixes numerator bases — Anthropic gross vs OpenAI net reads 2.71x raw; equalized ratio is 1.65x (0.228x vs 0.138x), the figure the companion note ships. |
| Anthropic equity raised $124.3B (equity-only) | $124.3B equity-only | CANONICAL | T2 company-announced | STABLE | 2026-07-02 | Excludes $34.5B chip bonds + $2.5B revolver per Ruling 1. |
| Anthropic Q2 2026 first operating profit ~$559M | ~$559M first operating profit (Q2 2026) | CANONICAL | T3 media/single-source | QUARTERLY | 2026-06-12 | Under FCF sweep review in Token Trap blockers. Margin arc: -94% -> 40% -> 63% (2027E) -> 77% (2028E). |
| PB Anthropic revenue field $55B (TTM 4Q2027) | $55B / Fiscal Period TTM 4Q2027 (period end 2027-12-31) | TRAP | T2 company-announced | QUARTERLY | 2026-07-16 | FORWARD PROJECTION to Dec-2027, NOT current run-rate. Ruling 4 fires. DO NOT ADOPT $55B. The Anthropic-ARR trap has now fired on both names. |
| Anthropic run-rate $47B | $47B run-rate (May, gross basis) | STALE | T2 company-announced | QUARTERLY | 2026-05-01 | 2.5mo old, past QUARTERLY decay. Media carrying ~$44B — conflict surfaced, canonical = $47B. Gross-basis reporter: 20-40% SEC restatement exposure ($28.2-37.6B); 39.75% equalization lands ~$28.3B, the bottom of that range. |
| Anthropic total raised $161.3B | $161.3B total ($124.3B equity + $37.0B debt) | CANONICAL | T2 company-announced | STABLE | 2026-07-16 | CANONICAL Jul 2. Prior $126.8B figure missed the revolver. |
| Anthropic-SpaceX compute deal $1.25B/mo (~$45B) | $1.25B/mo through May 2029 (~$45B total) | CANONICAL | T1 SEC/audited | STABLE | 2026-05-20 | COLOSSUS/COLOSSUS II; 90-day termination; Anthropic retains all IP. Part of $80B+ compute commitments across 6 partners. Corroborated from the SpaceX side: AI compute contracts ~$27.8B/yr [T4, VERIFY]. |
| $/AIBQ-pt — Anthropic $118B/pt | $118B per AIBQ point | CANONICAL | T4 unverified | VOLATILE | 2026-07-16 |  |
| Anthropic AIBQ v3.0 score 8.20 | ~8.20 Strong / S5 / AI-INFRA | CANONICAL | T4 unverified | QUARTERLY | 2026-05-27 | Key drag: CE-2=4 (margin). CI 5.1->5.8 on SpaceX compute deal. Scores dated May 27 and unrefreshed as of v3.4. |
| Anthropic CE 0.228x equalized | 0.228x CE equalized | CANONICAL | T2 company-announced | QUARTERLY | 2026-07-16 | 1.65x capital-efficiency advantage over OpenAI's 0.138x — one of the two survivors of equalization. |
| Anthropic debt $37.0B ($34.5B chip bonds + $2.5B revolver) | $34.5B Jun-9 chip bonds + $2.5B May-2025 revolver | CANONICAL | T2 company-announced | STABLE | 2026-07-02 | Bonds tranched $6.0B Superpriority / $24.0B 1st Lien / $4.5B 2nd Lien. Excluded from CE per Ruling 1 — debt informs CI/risk, not CE. |
| Anthropic equalized net run-rate ~$28.3B | ~$28.3B net (equalized) | CANONICAL | T4 unverified | QUARTERLY | 2026-07-16 | Lands at the bottom of the 20-40% SEC restatement exposure range ($28.2-37.6B). |

### Databricks

| Figure | Value | Status | Tier | Decay class | Last verified | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Databricks equity raised $33.1B | $33.1B | CANONICAL | T2 company-announced | STABLE | 2026-06-12 |  |
| Databricks AIBQ v3.0 score 8.92 | 8.92 Elite / S5 / AI-PLAT | CANONICAL | T4 unverified | QUARTERLY | 2026-05-27 | Highest AIBQ in the Frontier Five. |
| Databricks valuation $134B | $134B post (Series L) | STALE | T2 company-announced | VOLATILE | 2026-06-12 | [VERIFY — STALE] flagged in v3.4 refresh. |
| $/AIBQ-pt — Databricks $15B/pt | $15B per AIBQ point | CANONICAL | T4 unverified | VOLATILE | 2026-07-16 |  |
| Databricks CE 0.16x | 0.16x CE | CANONICAL | T2 company-announced | QUARTERLY | 2026-06-12 |  |
| Databricks ARR $5.4B | $5.4B / FCF+ | STALE | T2 company-announced | QUARTERLY | 2026-06-12 | [VERIFY — STALE] flagged in v3.4 refresh. FCF positive. |
| Databricks revenue multiple 24.8x | 24.8x | CANONICAL | T2 company-announced | VOLATILE | 2026-06-12 | Both inputs [VERIFY — STALE] as of Jul 16. |

### Market / Macro

| Figure | Value | Status | Tier | Decay class | Last verified | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Foundation models market $50B -> $250B (2028E) | $50B -> $250B (2028E) | CANONICAL | T3 media/single-source | QUARTERLY | 2026-02-27 |  |
| AI applications market $30B -> $150B (2028E) | $30B -> $150B (2028E) | CANONICAL | T3 media/single-source | QUARTERLY | 2026-02-27 |  |
| AI infrastructure market $120B -> $400B (2028E) | $120B -> $400B (2028E) | CANONICAL | T3 media/single-source | QUARTERLY | 2026-02-27 |  |

### Methodology

| Figure | Value | Status | Tier | Decay class | Last verified | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Quality-valuation correlation [withheld] | [VALUE EMBARGOED — see Ruling 2] | EMBARGOED | T4 unverified | QUARTERLY | 2026-06-12 | Public expression = $/AIBQ-pt ladder ONLY. Recompute required before next media appearance. Jul-16 test: xAI rung fell ~19% — the curve is partially correcting; the paradox is not a constant. |
| Equalization factor 39.75% (Anthropic gross->net) | 39.75% | CANONICAL | T4 unverified | PERMANENT | 2026-07-16 | Anthropic net run-rate ~$28.3B -> 34.1x, identical to OpenAI. NO multiple discount. Survivors: 81% AIBQ quality premium + 1.65x CE advantage. Supersedes the 20.5x-vs-34.1x inversion framing everywhere it appears. |

### OpenAI

| Figure | Value | Status | Tier | Decay class | Last verified | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| $/AIBQ-pt — OpenAI $188B/pt | $188B per AIBQ point | CANONICAL | T4 unverified | VOLATILE | 2026-07-16 | Ladder is the public expression of the quality-valuation spread; [VALUE EMBARGOED — see Ruling 2] itself EMBARGOED until recompute. |
| OpenAI 2025 gross margin 33% | 33% (13pp miss vs 46% plan) | CANONICAL | T3 media/single-source | STABLE | 2026-02-27 |  |
| OpenAI CE 0.14x gross | 0.14x CE (net numerator) | CANONICAL | T2 company-announced | QUARTERLY | 2026-07-16 | Numerator is NET where Anthropic's 0.38x is GROSS — raw 2.71x ratio is a basis artifact; equalized ratio is 1.65x. |
| OpenAI equity raised $181.2B (equity-only) | $181.2B equity-only | CANONICAL | T2 company-announced | STABLE | 2026-07-16 | Jul-8 $520M debt excluded per Ruling 1, so CE 0.14x holds — the ruling doing its job. |
| OpenAI employees 4,500 | 4,500 (PB, Mar 21) | CANONICAL | T2 company-announced | QUARTERLY | 2026-03-21 | Now BELOW Anthropic's 5,000 (Apr 21). |
| OpenAI infrastructure obligations $1.15T | $1.15T across 7 vendors | CANONICAL | T3 media/single-source | STABLE | 2026-02-27 |  |
| OpenAI total raised $186.4365B | $186.4365B total ($181.2B equity + $5.2365B debt) | CANONICAL | T2 company-announced | STABLE | 2026-07-16 | Debt: $4.0B Oct-24 + $0.7B embedded in Mar-26 round + $520M Jul-8 2026 (PB 338367-43T). Grants ($1.03B) already excluded by PB. CE denominator unchanged at $181.2B per Ruling 1. |
| PB OpenAI revenue field $30B (TTM 4Q2026) | $30B TTM 4Q2026 | TRAP | T2 company-announced | QUARTERLY | 2026-06-12 | FORWARD PROJECTION, not current ARR. Ruling 4. DO NOT ADOPT — canonical net ARR remains ~$25B (est.). |
| OpenAI revenue multiple 34.1x | 34.1x | CANONICAL | T2 company-announced | VOLATILE | 2026-07-16 | OpenAI reports NET revenue — never compare raw to Anthropic's gross (Ruling 5). |
| OpenAI AIBQ v3.0 score 4.53 | 4.53 Developing / S5 / AI-INFRA | CANONICAL | T4 unverified | QUARTERLY | 2026-05-27 | Key drag: GO-2=2 (conversion). xAI (4.49) is OpenAI's quality twin. |
| OpenAI-MSFT revenue share cap $38B through 2030 | $38B cap through 2030 | CANONICAL | T3 media/single-source | STABLE | 2026-05-22 | Cap binds mid-2028; shifts profitability 2030->2029; FCF 2030 +$30B->+$151B; cumulative negative FCF $198B->$99B. |
| OpenAI net ARR ~$25B (est.) | ~$25B net (est.) | STALE | T3 media/single-source | QUARTERLY | 2026-06-12 | PB $30B TTM 4Q2026 is a forward projection, not current ARR — Ruling 4. Conflict surfaced, not chosen. |
| OpenAI CE 0.138x equalized | 0.138x CE equalized | CANONICAL | T2 company-announced | QUARTERLY | 2026-07-16 |  |
| OpenAI valuation $852B | $852B | CANONICAL | T2 company-announced | VOLATILE | 2026-07-16 | $122B round at $730B pre, closed Mar 31 (PB 320989-60T). The Feb 27 $110B announcement is the same round — do not double-count. |

### SPCX / SpaceX

| Figure | Value | Status | Tier | Decay class | Last verified | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| SPCX consolidated FY2025 revenue $18.7B | $18.7B rev / -$4.9B net / $6.6B adj. EBITDA | CANONICAL | T1 SEC/audited | STABLE | 2026-05-20 |  |
| SPCX IPO price $135 | $135.00 (priced Jun 11) | CANONICAL | T1 SEC/audited | STABLE | 2026-06-11 | 555.6M shares; $75B raise; all-primary; largest IPO in history. Float ~4.2%; Musk ~85% voting power; 366-day lockup. |
| SPCX Connectivity (Starlink) FY2025 revenue $11.4B | $11.4B rev / $7.17B seg. adj. EBITDA (63%) | CANONICAL | T1 SEC/audited | STABLE | 2026-05-20 | $4.42B op income; subs 8.9M (2025) -> 10.3M (Q1 2026); ARPU $99 (2023) -> $66 (Q1 2026). |
| SPCX market cap ~$1.77-1.81T (Jul 15-16) | ~$1.77-1.81T on 13.076B shares | CANONICAL | T3 media/single-source | VOLATILE | 2026-07-16 | ~$300-340B of market cap gone in five weeks vs the ~$2.11T day-one close. |
| SPCX Jul-15 break level ~$132-141 | ~$132-141, below the $135 IPO price (Jul 15) | DISPUTED | T3 media/single-source | VOLATILE | 2026-07-16 | THE EVENT (first break below $135) is cross-confirmed; THE LEVEL is not. Investing.com $135.27 close, range $132.15-139.34; TradingView ATL $135.52 on Jul 14; CNN open $140.95. Use '~$132-141, below the $135 IPO price' until a T1/T2 close is pulled. |
| SPCX all-time high $225.64 (Jun 16) | $225.64 ATH, Jun 16 | CANONICAL | T2 company-announced | STABLE | 2026-07-16 | Four days post-IPO. Never captured in v3.3. |
| SPCX day-one close $161.11 (~$2.11T cap) | $161.11 close Jun 12 (+19.3%), ~$2.11T cap | CANONICAL | T2 company-announced | STABLE | 2026-06-12 | Open $150 (+11%), high $176.52 (+31%); ~$2.11T on 13.076B shares. Historical print — does not decay. |
| SPCX Space (launch) FY2025 revenue $4.09B | $4.09B rev / -$660M op | CANONICAL | T1 SEC/audited | STABLE | 2026-05-20 | ~80% of domestic payloads. |

### SSI

| Figure | Value | Status | Tier | Decay class | Last verified | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| SSI equity raised $3B | $3B | CANONICAL | T2 company-announced | STABLE | 2026-06-12 |  |
| SSI AIBQ v3.0 score 2.30 | 2.30 Distressed / S1 / AI-INFRA | CANONICAL | T4 unverified | QUARTERLY | 2026-05-27 |  |
| SSI valuation ~$30-32B | ~$30-32B | STALE | T3 media/single-source | VOLATILE | 2026-06-12 | [VERIFY — STALE] flagged in v3.4 refresh. $0 revenue; multiple is infinite. |

### xAI

| Figure | Value | Status | Tier | Decay class | Last verified | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| xAI implied multiple >400x | >400x implied (est.) | CANONICAL | T4 unverified | VOLATILE | 2026-07-16 |  |
| xAI CE 0.07x | 0.07x CE | CANONICAL | T2 company-announced | QUARTERLY | 2026-06-12 |  |
| xAI FY2025 revenue $3.2B (AI segment) | $3.2B FY25 (~$1.25B ex-X-ads) | CANONICAL | T1 SEC/audited | STABLE | 2026-05-20 | True AI revenue ex-X-ads ~6.7% of company revenue (~$1.25B) [Fortune/Granda, T3]. Segment op loss -$6.36B; capex $12.7B FY25. |
| xAI implied valuation ~$1.10-1.41T (SPCX AI segment SOTP) | ~$1.10-1.41T (est., SOTP at the Jul-15 tape) | CANONICAL | T4 unverified | VOLATILE | 2026-07-16 | WAS $1.4-1.7T at the Jun-12 close. Starlink $250-500B + Space $40-100B + $75B IPO cash backed out of the ~$1.77T Jul-15 tape. Same method, same segment marks, new tape. |
| xAI AIBQ v3.0 score 4.49 | 4.49 Developing / S4 / AI-INFRA | CANONICAL | T4 unverified | QUARTERLY | 2026-05-27 | Key drag: CE-1=2 (CapEx 4x rev). Per SpaceX S-1: CE 3.0->2.5, GO 2.5->3.5, MD 3.8->4.3. |
| xAI pre-merger equity raised $47.16B | $47.16B pre-merger | CANONICAL | T2 company-announced | STABLE | 2026-06-12 | Acquired all-stock by SpaceX Feb 2, 2026 at $250B; accumulated losses $41.3B. |
| $/AIBQ-pt — xAI ~$279B/pt | ~$279B per AIBQ point (est.) | CANONICAL | T4 unverified | VOLATILE | 2026-07-16 | WAS ~$345B at the Jun-12 close — the rung fell ~19% on five weeks of SPCX tape. The inverse quality-valuation curve is PARTIALLY CORRECTING — direct contradiction of The xAI Tell thesis. FCL + thesis-tracker event. |

## Company Dossiers Index

The Canon keeps one compiled dossier row per coverage company. Full profiles live under `companies/`; this is the completeness index.

| Company | AIBQ | Valuation | ARR / run-rate | IPO status | Completeness | Last compiled |
| --- | --- | --- | --- | --- | --- | --- |
| OpenAI | 4.53 | $852B [PB-confirmed Jul 16] | ~$25B net (est.) [STALE — estimate carried since Jun 12; not re-pulled Jul 16; PB $30B TTM 4Q2026 field is a TRAP (forward projection, Ruling 4)] | Confidential S-1 filed with SEC 2026-05-22; registry: Confidential Filed, Rank 4, expected window Sep-Nov 2026, lead banks GS/MS/JPM; Sep-2026-vs-2027 timing conflict frozen (house P=0.55 of a public 2027 reaffirmation before Sep 30) | Complete | 2026-07-21 |
| Anthropic | 8.2 | $965B post [PB-confirmed Jul 16] | $47B run-rate (May 2026, gross basis) [STALE — 2.5mo old, past QUARTERLY decay; not re-pulled Jul 16; equalized net ~$28.3B] | Confidential IPO registration filed 2025-12-01 (PB deal 314988-58T); registry: Pre-Filing, Rank 3, timeline Late 2026/Early 2027; PB target 2026-10-01 (readiness 72), IPO window Oct 1-15 2026; house prediction P=0.65 pricing slips to 2027 | Complete | 2026-07-21 |
| xAI | 4.49 | $250B SpaceX acquisition mark (Feb 2, 2026, all-stock); AI-segment SOTP-implied ~$1.10–1.41T (T4 est., Jul-15 tape) | $3.2B FY2025 revenue (AI segment, S-1 T1); ~$1.25B ex-X-ads | Acquired by SpaceX Feb 2, 2026; public exposure via SPCX (Nasdaq) since Jun 11, 2026 — see SPCX / SpaceX dossier | Complete | 2026-07-21 |
| Databricks | 8.92 | $134B post (Series L, Feb 2026) [VERIFY — STALE]; Jul 2026 feed reports $188B round (+$3B, T5 unconfirmed) | $5.4B / FCF+ [VERIFY — STALE] | Pre-Filing — IPO Rank 1; target H2 2026 (Sep window; readiness 88) | Complete | 2026-07-21 |
| SPCX / SpaceX | None | Market cap ~$1.77–1.81T (Jul 15–16, on 13.076B sh); day-one close ~$2.11T (Jun 12) | FY2025 consolidated revenue $18.7B (S-1, T1): Starlink $11.4B + Space/launch $4.09B + xAI $3.2B; −$4.9B net / $6.6B adj. EBITDA | PUBLIC — Nasdaq: SPCX. IPO $135.00 priced Jun 11, 2026 ($75B all-primary, largest US IPO ever); Jul 15 first close below IPO price (level DISPUTED) | Complete | 2026-07-21 |
| SSI | 2.3 | ~$30–32B [VERIFY — STALE] | $0 — pre-revenue (multiple is infinite) | Not Applicable (S1 research lab; IPO Rank 5) | Partial | 2026-07-21 |
| 🌐 System / Cross-Company | None |  |  |  | Complete | 2026-07-21 |
| ElevenLabs | None | $11B (v2 registry, unverified against canon) | $0.33B (v2 registry, unverified against canon) |  | Stub | 2026-07-21 |
| Scale AI | None | $74.1B (v2 registry, unverified against canon) | $2B (v2 registry, unverified against canon) |  | Partial | 2026-07-21 |
| Perplexity | None | $20B (v2 registry, unverified against canon) | $0.5B (v2 registry, unverified against canon) |  | Stub | 2026-07-21 |
| Mistral AI | None | $13.6B (v2 registry, unverified against canon) | $0.4B (v2 registry, unverified against canon) |  | Stub | 2026-07-21 |
| OpenEvidence | None | $12B (v2 registry, unverified against canon) | $0.03B (v2 registry, unverified against canon) |  | Stub | 2026-07-21 |
| Cohere | None | $6.8B (v2 registry, unverified against canon) | $0.24B (v2 registry, unverified against canon) |  | Stub | 2026-07-21 |
| CoreWeave | None | $19.1B (v2 registry, unverified against canon; pre-dates Mar-2025 IPO) | $5.1B (v2 registry, unverified against canon) | Public — Nasdaq: CRWV (per v2 master events, IPO 2025-03-28; conflicting v2 rows — see page) | Stub | 2026-07-21 |
| Cursor | None | $50B (v2 registry, unverified against canon) | $3B (v2 registry, unverified against canon) |  | Partial | 2026-07-21 |

## Load-Bearing Citations Sample

14 tracked citation-to-artifact links in the registry; sample of load-bearing entries with update status:

| Citation | Location | Updated for current value | Notes |
| --- | --- | --- | --- |
| xAI implied valuation ~$1.10-1.41T (SPCX AI segment SOTP) → The xAI Tell §2 (SOTP + sensitivity table) | §2 (SOTP + sensitivity table) | no | Report shipped $1.4-1.7T at the $2.11T Jun-12 close; recomputed ~$1.10-1.41T at the ~$1.77T Jul-15 tape. Same method, new tape. |
| Anthropic revenue multiple 20.5x gross → The xAI Tell §5 | §5 | no | Shipped as 'the Anthropic inversion' dislocation — superseded by Ruling 5 (equalized 34.1x). In the equalization sweep. |
| $/AIBQ-pt — Anthropic $118B/pt → The xAI Tell §3 | §3 | yes | Rung unchanged at the Jul-16 refresh. |
| $/AIBQ-pt — xAI ~$279B/pt → The xAI Tell §3 | §3 | no | Report shipped the ~$345B rung (Jun-12 close); canonical is now ~$279B — the ~19% fall is the thesis hit. |
| Anthropic run-rate $47B → An Eye on OpenAI comparison sections | comparison sections | yes | Never compare raw to OpenAI's net — Ruling 5. |
| Anthropic run-rate $47B → Anthropic: The S-1 Expected to Price AI revenue section | revenue section | yes | Gross-basis reporter: 20-40% SEC restatement exposure noted. |
| $/AIBQ-pt — Databricks $15B/pt → The xAI Tell §3 | §3 | yes | Rung unchanged at the Jul-16 refresh. |
| $/AIBQ-pt — OpenAI $188B/pt → The xAI Tell §3 | §3 | yes | Rung unchanged at the Jul-16 refresh. |
| Equalization factor 39.75% (Anthropic gross->net) → The Basis Trade workbook v0.1 | workbook v0.1 | yes | Origin artifact — gate-verified workbook; promoted to Ruling 5 on Jul 16. |
| Equalization factor 39.75% (Anthropic gross->net) → Token Trap / Frontier AI Price Wars companion v2 §5 | §5 | yes | v2 four-basis table carries the equalized framing. |
| Anthropic run-rate $47B → NEXUS Morning Digest §1 (Frontier Five) | §1 (Frontier Five) | yes | Canonical value unchanged but [VERIFY — STALE] since Jul 16 — past QUARTERLY decay; re-pull trigger armed. |
| OpenAI revenue multiple 34.1x → Token Trap / Frontier AI Price Wars companion v2 §5 | §5 | no | Carried in the v2 four-basis table; confirm on ship. |
| Anthropic revenue multiple 20.5x gross → Token Trap / Frontier AI Price Wars companion v2 §5 | §5 | no | v1 published it as a dislocation; v2 deleted it and added the four-basis table. Sweep closes when v2 ships. |
| OpenAI revenue multiple 34.1x → The xAI Tell §5 | §5 | no | The other leg of the 20.5x-vs-34.1x framing superseded by Ruling 5. |

---
*Mirrored from Notion 2026-08-11. The embargo redaction above is enforced by this repository's own methodology ruling (CLAUDE.md), independent of and consistent with the source system's own Ruling 2.*
