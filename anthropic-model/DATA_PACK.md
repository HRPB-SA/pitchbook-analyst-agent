# Anthropic Data Pack — v1.0 (2026-08-19)

Feeds `01_Data` of the teaching build (`Anthropic_Model_v1.xlsx`). Every figure: value · as-of ·
basis · tier · tag · decay class. Tiers per validation spine (T1 primary → T5 rumor).
Rigor 3 build (internal/decision-supporting); promote to Rigor 4+ before anything ships externally.

**Basis rule (Ruling 5):** Anthropic reports revenue GROSS (incl. cloud partner sales).
Canonical equalization to net = **× 60.25%** (1 − 39.75%). Never compare a gross Anthropic line
to OpenAI net without equalizing. Equalization was gate-verified on the May-2026 mix — applying
it to later prints assumes mix stability (flag as est.).

---

## 1. Marks & funding history (STABLE decay) — PB deals file re-pulled 2026-08-19, profile last updated 2026-08-18

| Event | Date | Size | Pre → Post | Leads / notes | Tier |
|---|---|---|---|---|---|
| Series A | 2021-05-28 | $124M | → $461M | first institutional round | T2 (PB) |
| Series D | 2024-07-01 | $1.2B | $19.8B → $21B | Menlo (D-1/D-2/D-3) | T2 |
| Amazon round | 2024-11-22 | $8.0B | $46B pre | Amazon; $1.3B convertible → equity | T2 |
| Series E | 2025-03-03 | $3.5B | $58B → $61.5B | Lightspeed (E-1/E-3) | T2 |
| Revolver (debt) | 2025-05-16 | $2.5B | — | PB 295197-04T | T2 |
| Series F | 2025-09-02 | $13.0B | $170B → $183B | Lightspeed / Fidelity / ICONIQ; $750M conv. | T2 |
| Series G | 2026-02-12 | $30.0B | $350B → $380B | Coatue/GIC/ICONIQ/Dragoneer/SoftBank/D.E. Shaw/MGX/Founders Fund | T2 |
| Series H | 2026-05-28 | $65.0B | $900B → **$965B** | Dragoneer/Sequoia/Cloverdale/Greenoaks/Altimeter · $589.0095/sh · ~1,638mm implied shares · 17.33% acquired | T2 |
| Chip bonds (debt) | 2026-06-09 | $34.5B | — | tranched $6.0B Superpriority / $24.0B 1st Lien / $4.5B 2nd Lien; funds Alphabet-chip purchases (PB 334763-02T) | T2 |
| IPO (confidential S-1) | filed 2026-06-01 | exp. >$60B raise | — | expected Oct 2026, Nasdaq; GS/JPM/MS reported | T2 filing / T4 raise size & banks [VERIFY] |
| 11th round (upcoming) | — | — | — | "reportedly seeking venture funding from AMD as of Jul 22, 2026" (PB note) | T5 — round-in-talks, NOT closed |

**Capital totals [CANONICAL Jul 2, re-confirmed vs PB Aug 18]:** $124.3B equity-only + $37.0B debt
($34.5B chip bonds + $2.5B revolver) = **$161.254B total raised**. CE denominator = equity only (Ruling 1).

## 2. Revenue run-rate curve (VOLATILE — the model's spine)

| As-of | Run-rate (gross) | Tier / source |
|---|---|---|
| Dec 2024 | $1B | T2 (widely confirmed) |
| Jul 2025 | $4B | T2/T3 |
| Dec 2025 | $9B | T2 (multi-outlet; also PB FY2025 field — see conflict #1) |
| Feb 2026 | $14B | T3 |
| ~Apr 2026 | $30B | T2 company statement ("80x growth", VentureBeat) — date approx [VERIFY] |
| May 2026 | $47B | T2 company (prior canonical anchor, May 29) |
| **End-Jul 2026** | **$65B** | **T2 — company-to-investor update; CNBC / Bloomberg / Fortune / TechCrunch, Aug 17–18** |
| YE 2026 | $100–120B expected | T3 — investor expectation per CNBC, not company guidance |

**PROPOSED CANONICAL UPDATE:** $65B run-rate (end-Jul 2026) supersedes $47B (May), which was
flagged [VERIFY — STALE] in project-context v3.4. Same reporter chain (company → investors →
multiple T2 outlets); the outlets independently confirm the same company communication.
Equalized net run-rate ~$39.2B (est., mix-stability assumption).

**Derived multiples on the standing $965B mark (est.):**
- May: 20.5x gross / 34.1x equalized [matches Ruling 5]
- End-Jul: **14.8x gross / ~24.6x equalized (est.)** — ~28% multiple compression in 10 weeks on growth alone, no new mark.

## 3. Recognized revenue & P&L (QUARTERLY decay)

- FY2024: revenue $1.0B · net loss $5.3B (PB financials, T2/T4)
- FY2025: revenue $9.0B (PB) — **see conflict #1 (basis)**
- FY2026: no recognized figure yet. Integrating the run-rate curve implies ~$35–45B recognized (est., own derivation — LOW confidence until a reported figure lands)
- Gross margin path: −94% (2024) → 40% (2025A — lowered vs plan; The Information, T3) → 63% (2027E) → 77% (2028E) [CANONICAL]
- Q2 2026: first operating profit ~$559M (T3, CNBC) — **FCF-sweep flag still open in project-context; treat as unswept**
- Dual-P&L breakevens (WSJ Apr 2026 investor docs, T2): excl-training breakeven 2025 · incl-training 2028 (+$3B) · FCF trough −$25B (2027) · revenue basis GROSS
- NRR 140%+ · 80% enterprise · 300K+ business customers · 1,000+ at $1M+ ACV · Claude Code $2.5B ARR / 54% coding share [CANONICAL Jun 12]
- Employees 5,000 (PB, Apr 21, 2026)

## 4. Burn & cash (QUARTERLY decay)

- FY2025 burn: $5.6B (T3, The Information chain)
- FY2026 planned burn: ~$3B (T3, The Information — "hikes 2026 forecast 20%, delays cash-flow-positive")
- **Conflict #3 below:** −$25B FCF trough 2027 (WSJ scenario) vs ~$3B 2026 burn (Information) — different vintages AND definitions (FCF incl. training/compute prepays vs operating burn). Do not net them.

## 5. Company forecasts — vintage-stamped (all T3, The Information chain)

| Vintage | 2026E | 2027E | 2029E | Status |
|---|---|---|---|---|
| ~Jul 2025 | — | $34.5B base | — | superseded |
| ~Jan 2026 (hiked +20%) | up to $18B | $55B optimistic | $148B optimistic | **superseded by actuals** — Jul-2026 run-rate ($65B) already exceeds the 2027 optimistic case |

Teaching point: in hypergrowth, forecasts decay in weeks. Date-stamp every projection; never
average forecasts of different vintages.

## 6. Compute & obligations (STABLE)

- $80B+ compute commitments across 6 partners [CANONICAL Jun 12]
- SpaceX COLOSSUS deal: $1.25B/mo through May 2029 (~$45B total) · 90-day termination · Anthropic retains IP [T1, SpaceX S-1]
- $34.5B chip bonds fund Alphabet-developed chip purchases (see §1)

## 7. Comps marks (VOLATILE — refresh before valuation step)

- OpenAI: $852B (Mar 31, 2026) · ~$25B net ARR (est.) [STALE — re-pull at Step 8] · FY2025 audited leak: rev $13.07B / op loss $20.92B (T3, FT-verified)
- xAI-in-SPCX: SOTP implied ~$1.10–1.41T at the Jul-15 tape — **STALE: SPCX Q2 printed Aug 6, result not yet pulled [VERIFY — also the Basis Trade falsifier window]**
- Databricks: $134B [STALE, not re-pulled since ~Feb]

## 8. Frozen conflicts (Gate 3 — surfaced, not chosen)

1. **FY2025 revenue basis [DISPUTED].** PB carries FY2025 = $9.0B; the same $9B circulates as the
   *Dec-2025 exit run-rate*; the Jan-2026 guidance ("3–4x growth in 2026 to ~$18B") implies
   recognized FY2025 of ~$4.5–6B. Likely a period/methodology gap (run-rate-as-fiscal + gross
   basis), not a true conflict — but unresolved. Model both: run-rate row AND recognized row.
2. **PB revenue field = $71.0B, "TTM 4Q2027", period end 2027-12-31** (profile, Aug 18). Ruling 4
   trap, third firing (was $55B on Jul 16). Forward projection — NEVER cite as current revenue.
   Signal value only: PB's forward estimate moved $55B → $71B in ~5 weeks.
3. **Burn definitions.** $5.6B (2025) / ~$3B (2026 plan) operating burn vs WSJ −$25B 2027 FCF
   trough. Different definitions and vintages [DISPUTED — reconcile in Step 7 with an explicit
   bridge: operating burn → FCF incl. training compute & prepays].
4. **AMD round + Decart.** PB carries an upcoming 11th VC round (AMD, "reportedly", Jul 22) and
   Anthropic acquiring Decart for ~$6B (Aug 13, status Rumor/Speculation). Both T5 — track, do
   not model until closed.

## 9. Sources (load-bearing)

- CNBC / Bloomberg / Fortune / TechCrunch, Aug 17–18, 2026 — $65B run-rate, $100–120B YE expectation
- Anthropic (official): Series H announcement — $65B at $965B post
- PitchBook profile 466959-97 (last updated 2026-08-18) + full deals pull (2026-08-19, on file)
- The Information — gross-margin cut, burn, forecast hikes (T3 single-outlet chain)
- WSJ Apr 6, 2026 investor docs — dual-P&L breakevens, FCF trough
- SpaceX S-1 (May 20, 2026) — COLOSSUS contract [T1]
- Harrison project-context v3.4 (Jul 16, 2026) — canonical baseline this pack updates

*Full URLs in the session log; deals JSON cached at the session tool-results path.*
