# SEED LIST — The $100 Billion Entry Fee v5 refresh
Run date: 2026-09-09. Every value in parentheses is the LAST-KNOWN value (project-context snapshot Jul 16, 2026; Anthropic DATA_PACK Aug 19, 2026; NEXUS extracts). ALL are unverified until re-pulled. Each ID must end with a ledger row (confirmed / estimated / recalled) or an explicit COULD-NOT-VERIFY row.

## Orchestrator pre-pull (PitchBook profiles, pulled 2026-09-09; profile "Last Updated" 2026-09-08). LOG THESE AND RE-VERIFY — do not treat as confirmed.
- PB Anthropic 466959-97: Total Raised $126,754.0M (was $161,254M on Jul 16 — the $34.5B chip bonds appear to have dropped out of the field: log as CONFLICT, find out why); Last Known Valuation $965,000M (2026-05-28, Later Stage VC); Ownership Status "In IPO Registration" (2026-06-01); Financing note dated 2026-09-04: confidential S-1 Jun 1, expected IPO October 2026, "reportedly seeking venture funding from Advanced Micro Devices as of July 22, 2026. The transaction will be supported by an estimated $10 billion of debt financing"; Revenue field $71,000M "TTM 4Q2027" period end 2027-12-31 = FORWARD PROJECTION (Ruling 4; do not use as run-rate); Employees 5,000 (as of 2026-04-21); investor-side "Last Investment" Decart $6,000M M&A 2026-08-10 status Failed/Cancelled (est.).
- PB OpenAI 149504-14: Total Raised $186,436.5M; Last Known Valuation $852,000M (2026-03-31); Ownership "In IPO Registration" (2026-06-08); Financing note dated 2026-07-09: confidential S-1 Jun 8, expected IPO September 2026, $520M debt Jul 8 2026; Revenue field $41,300M "TTM 4Q2026" period end 2026-12-31 = FORWARD PROJECTION; Employees 4,500 (2026-03-21); Business Status "Generating Revenue/Not Profitable"; Primary contact title NOW "Co-Founder, Chief Executive Officer and Board Member" (the Jul-16 "Co-Chief Executive Officer" anomaly is no longer displayed — log as resolved-on-PB-side with the date, then check whether any governance change was ever disclosed).
- Web (Sep 9): no public S-1 found for either company via search; Reuters late-June report that OpenAI is considering waiting until 2027. MUST be confirmed directly on EDGAR full-text search before it enters the ledger.

## A. ANTHROPIC
A-01 Post-money valuation ($965B post, Series H $65B, May 28, 2026; $900B pre)
A-02 Total raised ($161.25B incl. $34.5B chip bonds Jun 9 + $2.5B revolver May 2025; equity-only $124.3B) — reconcile to PB's new $126.754B
A-03 Revenue run-rate, GROSS basis ($47B May; $65B end-Jul per Aug 17-18 T2 reports; YE2026 $100-120B "investor expectation") — get the latest as of Sep 2026
A-04 Headcount (5,000, Apr 21)
A-05 S-1 status and target window (confidential Jun 1; October 2026; >$60B raise; GS/JPM/MS) — is it public yet?
A-06 Gross margin (−94% 2024 → 40% 2025 → 63% 2027E → 77% 2028E; SemiAnalysis "70%+ inference infra GM")
A-07 Cloud reseller revenue treatment — gross vs net; share of revenue via AWS Bedrock / Google Vertex / Azure; the 39.75% equalization basis
A-08 Compute commitments by provider (AWS $100B cumulative? / 5GW; Google 5GW TPU, $40B equity; Microsoft $5B equity + $30B Azure; SpaceX COLOSSUS $1.25B/mo to May 2029 ≈ $45B; Nvidia; "$80B+ across 6 partners")
A-09 2026 compute spend and capex ($5B infra buildout 2026E in NEXUS tracker)
A-10 Chip deals and custom silicon (Alphabet/TPU purchases funded by $34.5B bonds; Trainium; AMD talks)
A-11 Cost per training run, current generation (NEXUS tracker: $7B 2026E, $14B 2027E, $22B 2028E — "Leaked Doc")
A-12 Inference unit costs (cost per million tokens; list prices Opus 4.8 $5/$25; Fast Mode)
A-13 Talent comp benchmarks (researcher packages; retention)
A-14 Energy / datacenter lease commitments (Fluidstack $50B DC build? Texas/NY sites; any PPAs)
A-15 Recognized revenue FY2024 ($1.0B) and FY2025 ($9.0B), net loss FY2024 ($5.3B); any FY2026 disclosure
A-16 Burn and FCF (FY2025 burn $5.6B; 2026 planned ~$3B; WSJ scenario FCF trough −$25B 2027; Q2 2026 first operating profit ~$559M T3 CNBC — FCF-sweep flag open)
A-17 Debt stack ($34.5B bonds tranched $6.0B/$24.0B/$4.5B; $2.5B revolver; new ~$10B debt per PB Sep 4 note)
A-18 AMD round status (in talks since Jul 22) and any Series I / secondary marks since May 28
A-19 Copyright exposure ($1.5B authors settlement; ~$3B music publishers demand; total ~$4.5B)

## B. OPENAI
O-01 Valuation ($852B post, $122B round at $730B pre, closed Mar 31, 2026) — any newer mark, secondary, or IPO range
O-02 Total raised ($186.4365B; $181.2B equity-only; debt $4.0B Oct-24 + $0.7B + $520M Jul-8)
O-03 Net revenue run-rate (~$25B est. Mar 2026; "$2B/month") — latest as of Sep 2026, NET of Microsoft share
O-04 FY2025 revenue actual ($13.07B FT-verified leak; op loss $20.92B; group loss $60.35B incl $41.55B FV swing; $17.2B paid to MSFT)
O-05 S-1 status and window (confidential Jun 8 per PB vs May 22 per media; September 2026 PB vs Friar 2027 lean — FROZEN CONFLICT; Kalshi odds)
O-06 Cumulative burn vs obligation stack (old draft $665B obligations vs $115B burn; later $1.15T obligations across 7 vendors) — reconcile the two tallies
O-07 Microsoft revenue-share cap ($38B through 2030; 20% share) and the renegotiation; Microsoft stake (~27%?) post-PBC conversion
O-08 Oracle / Stargate commitment ($300B; ~$60B/yr from 2027)
O-09 CoreWeave commitment ($22.4B)
O-10 AMD commitment ($90B; warrants 160M shares at $0.01)
O-11 Nvidia commitment ($100B; 10GW)
O-12 Broadcom custom silicon ($350B; 10GW)
O-13 Microsoft Azure commitment ($250B)
O-14 AWS commitment ($38B)
O-15 Altman title anomaly on PB profile (was "Co-Chief Executive Officer" Jul 16; now plain CEO Sep 8) — resolved or governance change?
O-16 2026 compute spend ($50B, Brockman testimony May 5, 2026)
O-17 Capex ($190B 2026E in NEXUS tracker "Earnings Call" — verify what this is)
O-18 Gross margin 2025 (33% vs 46% plan)
O-19 Cost per training run current gen (NEXUS: $25B 2026E, $60B 2027E, $112B 2028E "Leaked Doc")
O-20 Inference COGS FY2025 ($8.4B; ~34% subsidizing 910M free users ≈ $2.86B) and inference unit costs
O-21 Talent comp benchmarks (Meta poaching offers; retention grants; SBC)
O-22 Energy / datacenter lease commitments (Stargate Abilene, Michigan, Texas, UAE; Crusoe; power MW)
O-23 Headcount (4,500 Mar 21; ~8,000 target end-2026)
O-24 Burn / FCF trajectory (WSJ Apr 6 investor docs: FCF trough −$110B 2028; cum −$198B → −$99B post-MSFT cap; breakeven excl-training 2026, incl-training 2030→2029)
O-25 Debt ($4B Oct-24; $520M Jul-8; any new facilities; Stargate project finance)
O-26 Corporate structure (PBC conversion; Foundation stake; Microsoft share)
O-27 Users and mix (subscribers 50M consumer / 9M business; enterprise mix 15% vs 35-40% conflict; ads tier)

## C. BOTH — CROSS-CUTTING
X-01 2026 compute spend — both, comparable basis
X-02 Capex vs opex treatment of compute (leases vs purchases)
X-03 Chip deals and custom silicon programs (Anthropic TPU/Trainium/Alphabet chips; OpenAI Broadcom/AMD/Nvidia)
X-04 Cost per training run for current-gen models — external estimates (Epoch AI) vs leaked plans
X-05 Inference unit costs — $/M tokens list vs cost; utilization
X-06 Talent comp benchmarks (AI researcher bands; Levels.fyi; reported packages)
X-07 Energy and datacenter lease commitments (MW, $/MWh, lease $/kW-mo)
X-08 The 39.75% gross-to-net equalization (Ruling 5) — the evidence for the basis; any S-1-era disclosure that changes it
X-09 AIBQ v3.0 inputs: Compute Independence (CI) and Capital Efficiency (CE) — the figures that feed them (Anthropic ~8.20; OpenAI 4.53; CE 0.228x vs 0.138x equalized)

## D. GREENFIELD ENTRY COST (new section) — reference-class data
G-01 Frontier-scale training cluster: buy cost by chip generation (H100/H200/B200/GB200 NVL72/GB300/Rubin) per GPU and per rack; DGX / HGX system prices
G-02 Lease rates $/GPU-hour by generation (CoreWeave, Lambda, Nebius, AWS, Azure, Oracle); reserved vs on-demand; financing terms (GPU-backed loans, rates)
G-03 Power: MW per 100k GPUs; $/MWh by region; PUE; utilization
G-04 Cooling (liquid vs air; $/MW)
G-05 Datacenter build vs colocation by region ($/MW build; $/kW-month colo; lead times)
G-06 Network fabric ($ per GPU for InfiniBand / Spectrum-X / NVLink)
G-07 Storage
G-08 Research and engineering headcount by band with comp (frontier lab: researcher / engineer / infra; reported packages)
G-09 Data acquisition and licensing (Reddit, News Corp, AP, Shutterstock, StackOverflow deals; Scale/Surge/Mercor labeling spend)
G-10 Safety and evals spend
G-11 Legal / regulatory / policy (copyright settlements as a cost line; compliance)
G-12 Go-to-market and G&A
G-13 Training runs by generation: compute-hours × cost; number of runs to a frontier result; failed-run allowance (Epoch AI model cost estimates; GPT-4 ~$78M; Gemini Ultra ~$191M; Grok 3/4; Llama 4; Claude Opus 4; GPT-5)
G-14 Inference serving cost per million tokens at stated utilization (SemiAnalysis / Epoch / provider disclosures)
G-15 Reference class — what "entry" actually cost: xAI (raised $47.16B pre-merger; accumulated losses $41.3B; $250B merger); SSI ($3B raised; $32B); Thinking Machines Lab ($2B seed at $12B 2025; any 2026 round); Reflection AI (2025 $2B at $8B?); Mistral; Periodic Labs; Humans&; any 2025–2026 frontier-lab raise ≥$1B; Meta Superintelligence Labs spend
