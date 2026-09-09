# The $100 Billion Entry Fee — v4.0 MAP (RECONSTRUCTED)

**Status: RECONSTRUCTION, not the original.** The v4.0 outline, the companion `100B_Entry_Fee_Master.xlsx`, and the 28-tab OpenAI+Anthropic IPO model could not be located in any store reachable from this session on Sep 9, 2026: not on any of the 22 branches of `hrpb-sa/pitchbook-analyst-agent`, not in `hrpb-sa/ai-analyst-bot` or `hrpb-sa/layer-h`, not in the Notion workspace the MCP is bound to (Layer H, not NEXUS), not in Gmail. What follows is assembled from five things that ARE reachable:

1. The orchestrator brief for this run (Harrison, Sep 9, 2026) — the authoritative statement of coverage, thesis, and the new greenfield section.
2. NEXUS extracts on branch `claude/automated-report-generation-zulv5p` (compiled Aug 11, 2026), which quote "The $100 Billion Entry Fee" editorial draft (data as of **2026-03-27**) and the Goldman-model OpenAI/Anthropic comparison note.
3. `harrison-project-context` v3.4 (canonical register, Jul 16, 2026) — snapshot copied to `prior/project-context-snapshot-2026-07-16.md`.
4. Anthropic `DATA_PACK.md` v1.0 (Aug 19, 2026) — the most recent internal figure refresh.
5. Prior workbooks: `NEXUS_Master_Workbook.xlsx` (Financial Model Inputs, Canonical Figures), `Anthropic_Model_v1.xlsx` (9-tab teaching build, Aug 19), `Anthropic_Operating_Model_2022-2032.xlsx`, `anthropic_model_2026-08-16.xlsx`.

Everything below is a MAP of what the report argued and which figures it leaned on. **No figure here is a source.** Every number is unverified until it has a fresh row in `research/evidence-ledger.md`.

---

## 1. Title, thesis, posture (as previously stated)

- **Title (Q2 2026 publication-rhythm table, NEXUS doctrine):** *The $100 Billion Entry Fee: The Cost Architecture That Wall Street Isn't Pricing.*
- **Thesis to test (orchestrator brief):** frontier AI cost architecture is structurally incompatible with investable return profiles. v5 tests it; it does not assume it.
- **Production history:** in production as of Feb 27, 2026 (`100B_Entry_Fee_Master.xlsx`, tabs `00_Assumptions`–`08_Sensitivity`, 2023A–2030E). Editorial draft data as of Mar 27, 2026. No activity logged after that in project-context; status "[STATUS VERIFY] — likely superseded by the companion reports and the 28-tab IPO model." Digest of May 24, 2026: "$100B Entry Fee: SpaceX deal adds new data point to cost stack."
- **Standing doctrine constraint (NEXUS architecture-and-doctrine §5, Apr 2026):** "The Q2 $100B Entry Fee report cannot just be 'I was right' — that report has negative asymmetry because the market has moved. It must either (a) reframe around OpenAI's continued mispricing (where the gap is still wide), or (b) name the next mispricing that isn't yet consensus." And: "Before shipping any section externally, ask: is this thesis already reflected in secondary market prices? If yes, the section is commentary, not analysis."
- **Audience posture (orchestrator brief):** a senior private-markets analyst who has been inside these numbers for three years, preparing public-market investors for the information asymmetry to disappear at the S-1s.

## 2. The 5-Layer Cost Stack — RECONSTRUCTED definition

No document reachable from this session defines the five layers. The definition below is reconstructed so that (a) every seed figure in the brief lands in exactly one layer, (b) each layer maps to a line a public investor will be able to see in an S-1, and (c) the obligation stack (contracted vs cash vs committed-but-cancellable) can be reconciled across layers. **The Analyst adopts this unless Harrison supplies the original; either way the definition must be printed in the report.**

| Layer | Name | What sits here | Old-draft figures that lived here (unverified) |
|---|---|---|---|
| L1 | Silicon and compute capacity | GPU/TPU/custom-ASIC purchases and leases; chip-purchase debt; custom-silicon programs; the multi-year vendor commitments (Nvidia, AMD, Broadcom, Google TPU, Trainium) | Anthropic $34.5B chip bonds (Jun 9) funding Alphabet-chip purchases; OpenAI Broadcom $350B, Nvidia $100B, AMD $90B (+160M-share warrants) |
| L2 | Power, datacenters, network | MW secured, PPAs, datacenter build vs colocation, cloud capacity contracts (Azure/AWS/GCP/Oracle/CoreWeave/SpaceX COLOSSUS), network fabric, storage | Anthropic AWS 5GW + Google 5GW (~8.5–10GW), SpaceX $1.25B/mo to May 2029 (~$45B), "$80B+ across 6 partners"; OpenAI Oracle/Stargate $300B, Azure $250B, AWS $38B, CoreWeave $22.4B; Brockman: ~$600B total commitments (May 5 testimony) |
| L3 | Training (R&D compute) | Training runs by generation; failed-run allowance; the "excl-training vs incl-training" dual P&L | Anthropic training $7B (2026E) → $14B → $22B → $30B (2029E); OpenAI $25B (2026E) → $60B → $112B → $120B (2029E, peak) → $90B (2030E) — WSJ Apr 6, 2026 investor docs, T3 |
| L4 | Inference (COGS, serving) | Inference COGS, unit cost per million tokens, utilization, gross margin, the free-tier subsidy | OpenAI FY2025 inference COGS $8.4B, ~34% (~$2.86B) subsidizing ~910M non-paying users (Mar-27 draft finding); OpenAI 2025 GM 33% vs 46% plan; Anthropic GM −94% (2023) → 40% (2025) → 63% (2027E) → 77% (2028E); SemiAnalysis "70%+ inference infra GM" (narrower measure) |
| L5 | People and everything else | Talent comp and SBC; data acquisition/licensing; safety and evals; legal/regulatory/policy (copyright reserves); GTM; G&A | Anthropic copyright exposure ~$4.5B ($1.5B authors settlement + ~$3B music-publisher demand, $1B base-case reserve in the Mar-27 draft); headcount 5,000 vs 4,500; OpenAI ~8,000 end-2026 target |

Cross-layer object: **the obligation stack** — every multi-year commitment classified as contracted / cash-paid-to-date / committed-but-cancellable, reconciled against cumulative burn. Old-draft framing: "$665B obligations vs $115B burn" (Mar 27 vintage) → later notes "$1.15T obligation stack across 7 vendors" (Feb 27 canonical, "fullest tally on record"). The two are different tallies of the same object at different dates; v5 must reconcile them, not pick one.

## 3. Sections the draft argued (inferred structure) and the number each leaned on

| # | Section (inferred) | The point it made | Figures it leaned on (old values, unverified) |
|---|---|---|---|
| 0 | Executive summary / the entry fee | The cost of standing at the frontier is now measured in hundreds of billions of committed dollars; the S-1s will make that visible for the first time | $161.3B / $186.4B raised; $1.15T obligations; $47B gross / ~$25B net run-rate |
| 1 | The stack, layer by layer, both companies, 2023A–2030E | Each layer has grown faster than revenue; the mix is shifting from opex-like cloud spend to balance-sheet-like commitments | WSJ Apr 6 dual P&Ls; training ramps; commitments |
| 2 | Training vs inference: the dual P&L | "Breakeven excluding training" is the number management will sell; "including training" is the one that matters | OpenAI excl-training breakeven 2026 / incl 2030→2029 (post-MSFT cap); Anthropic excl 2025 / incl 2028 (+$3B) |
| 3 | The free-tier subsidy | A third of OpenAI's inference bill serves users who pay nothing; the ads tier is a cost response, not a growth initiative | $8.4B inference COGS; ~$2.86B; ~910M non-payers |
| 4 | Gross vs net: the S-1 restatement risk | Anthropic reports gross (cloud-partner resale); OpenAI net of Microsoft's share; SEC review could cut a gross headline 20–40% | 39.75% equalization (Ruling 5); $47B → ~$28.3B; both at 34.1x |
| 5 | Capital efficiency on an equity-only denominator | Debt is not equity; CE compared on equalized net revenue | $124.3B vs $181.2B equity-only; 0.228x vs 0.138x = 1.65x |
| 6 | The obligation stack vs burn | Obligations exceed cumulative burn by an order of magnitude; what is contracted, what is cash, what is cancellable | $665B vs $115B (Mar) → $1.15T (later); Brockman ~$600B |
| 7 | Microsoft: the revenue-share cap | The $38B cap through 2030 moves OpenAI's incl-training breakeven forward a year and halves cumulative negative FCF | $38B cap (May 18); FCF 2030 +$30B → +$151B; cum −$198B → −$99B; $17.2B paid to MSFT in FY2025 |
| 8 | Compute independence and the AIBQ read | CI and CE sub-scores as the scored expression of the stack | Anthropic 8.20 (CE-2 4.0, CI-2 4.0); OpenAI 4.53 (CE-1 3.0, CE-4 2.5, CI-2 3.0) |
| 9 | Valuation and multiple equalization | On an equalized basis the market pays the same multiple for very different quality and efficiency | $965B / $852B; 34.1x both; $118B vs $188B per AIBQ point |
| 10 | Scenarios and sensitivities | What moves the answer: GM path, training ramp, gross-to-net haircut, the cap | `07/08_Sensitivity` grids |
| 11 | The verdict and the falsifiers | Calls fenced with what would prove them wrong | IPO windows (Sep/Oct 2026 vs 2027), SPCX tape as first print |
| NEW | Greenfield entry cost | What it costs, line by line, to start a frontier lab from zero today; three scenarios; reference class xAI / SSI / Thinking Machines / Reflection / 2025–26 raises | none in old draft |

## 4. Old figures most likely to be superseded (feed for `superseded.md`)

| Figure | Old value (source, date) | Why it is suspect on Sep 9, 2026 |
|---|---|---|
| Anthropic run-rate | $47B gross (company, May 2026) → $65B (DATA_PACK, Aug 17–18 T2 reports) | QUARTERLY decay; PB now shows $71B TTM 4Q2027 forward field (trap) |
| Anthropic total raised | $161.254B incl. $37.0B debt (Jul 16) | PB profile now reads $126.754B — a $34.5B drop; classification change or removal of the bonds |
| Anthropic debt | $34.5B bonds + $2.5B revolver | PB Sep 4 note: AMD round "supported by an estimated $10 billion of debt financing" |
| OpenAI net run-rate | ~$25B (est., Mar–Jun 2026) | Stale since Jun 12; PB forward field now $41.3B TTM 4Q2026 (trap) |
| OpenAI S-1 window | Sep 2026 (PB, Jul 9) vs 2027 (Friar/Bloomberg Jun 26) | Frozen; September has arrived — the branch resolves itself within weeks |
| Obligation stack | $1.15T (7 vendors, Feb 27) vs Brockman ~$600B (May 5) vs $665B (Mar 27 draft) | Three tallies; Georgia $30B+ DC (Jul 22) and a reported $500B Nvidia-backed DC deal (Jul 27) may have moved it |
| Altman PB title | "Co-Chief Executive Officer" (Jul 16) | PB Sep 8 refresh shows plain CEO — anomaly gone; needs a dated closure |
| SPCX / xAI reference | $2.11T day-one → ~$1.77–1.81T Jul 15; xAI implied $1.10–1.41T | Aug 6 Q2 print and lockups since; VOLATILE |
| AIBQ scores | May 27, 2026 vintage (unrefreshed) | Every CE/CI input has moved |

## 5. Frozen conflicts inherited (both branches stay live unless the ledger resolves them)

1. OpenAI S-1 timing — PB September 2026 vs Friar 2027 lean.
2. CE numerator basis — gross vs net (raw 2.71x vs equalized 1.65x).
3. OpenAI confidential filing date — May 22 vs Jun 8 (vs Jun 1 / Jun 9 single-source).
4. Feb 27, 2026 round — $730B vs $840B post; "Series F" vs "Series G" label; do not double-count with the Mar 31 $122B close.
5. Anthropic gross margin — ~40% GAAP-style (WSJ) vs 70%+ inference-infrastructure (SemiAnalysis, narrower).
6. Anthropic AIBQ composite — 8.20 canonical vs 8.06 live in the daily tracker.
7. OpenAI enterprise mix — 15% vs 35–40%.
8. Altman Co-CEO field — durable PB error vs real governance change (now apparently closed on PB's side; confirm).

## 6. Methodology rulings the report must obey (PERMANENT decay)

- Ruling 1: CE denominator = equity raised only.
- Ruling 2: the quality–valuation correlation coefficient is EMBARGOED; only the $/AIBQ-point ladder may be published.
- Ruling 3: Anthropic bear-case FCF-margin correction sweep is open — the ~$559M Q2 op profit (T3) is under review.
- Ruling 4: PitchBook TTM revenue fields are forward projections.
- Ruling 5: Anthropic gross → net equalization 39.75% (verified on the May 2026 mix; applying it to later prints assumes mix stability → est.).
- Ruling 6: AIBQ v3.0 weights CE 20 / RQ 25 / CI 15 / GO 20 / MD 20; 24 sub-scores; stage-gated CE.

## 7. AIBQ inputs as last scored (May 27, 2026 vintage) — for `aibq-delta.md`

- Anthropic 8.20 (Strong / S5): CE-1 10.0 · CE-2 4.0 · CE-3 9.0 · CE-4 8.0 · CI-1 6.0 · CI-2 4.0 · CI-3 5.0 · CI-4 5.0 · CI-5 5.0 (CI dimension later revised 5.1 → 5.8 on the SpaceX deal; sub-scores not re-issued).
- OpenAI 4.53 (Developing / S5): CE-1 3.0 · CE-2 3.5 · CE-3 3.0 · CE-4 2.5 · CI-1 5.5 · CI-2 3.0 · CI-3 4.0 · CI-4 6.0 · CI-5 4.0.
- Thresholds that matter: CE-2 GM bands (<30% 1–2; 30–50% 3–4; 50–65% 5–6; 65–75% 7–8; >75% 9–10; AI-INFRA +1.0 if >50%). CE-4 debt >2x ARR → 1–2 band. CI-1 provider count/balance; CI-2 ownership ladder (rent → colo → owned racks → owned DCs + ASIC in dev → vertically integrated); CI-3 PPAs (>500MW = 7–8; >1GW = 9–10); CI-4 chip-vendor diversity; CI-5 lock-in.

## 8. Old workbook structure (for `model-spec.md` continuity)

- `100B_Entry_Fee_Master.xlsx` (Feb 27): `00_Assumptions` · `01`–`07` (not enumerated in any reachable file) · `08_Sensitivity`; years 2023A–2030E.
- `Anthropic_Model_v1.xlsx` (Aug 19, teaching build): `00_Assumptions` (scenario switch 1/2/3) · `01_Data` (tiered anchors with as-of, basis, tier, decay) · `02_Revenue` (gross AND equalized-net rows) · `03_Costs` · `04_PL` (dual excl/incl-training) · `05_Cash_Fund` (burn walk, capitalization, CE) · `06_Valuation` · `07_Sensitivity` · `08_Output`. Conventions: blue input / black formula / green output; $M; years in columns D:K; column A label, B units, C source/tier.
- v5 keeps the house numbering and the D:K = 2023A–2030E timeline so exhibits can be cross-referenced to the older builds.

## 9. What v5 must add that v4 did not have

- The greenfield entry-cost section and Workbook B (three scenarios; cumulative capital to first frontier-class model, to first $1B net revenue, to cash-flow breakeven; reference-class check).
- A contracted / cash / cancellable reconciliation of the obligation stack.
- Frozen-conflict switch cells in Workbook A.
- An explicit "where the thesis got weaker" section: the doctrine note already warned in April that the contrarian gap was closing.
