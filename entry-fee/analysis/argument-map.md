# Argument Map: The $100 Billion Entry Fee v5
Agent 2 (Analyst), 2026-09-09. One row per claim the report makes. Each claim lists its supporting ledger rows, inherits the tier of its weakest load-bearing row, names what would falsify it, and carries a status: KEEP (T1/T2 throughout), KEEP-WITH-FLAG (a load-bearing row is T3/T4 or could-not-verify; the flag must be visible in the text, Rigor 5), or CUT (no ledger row, or superseded). Claims are grouped by the v5 section that carries them (`analysis/outline-v5.md`). No em-dashes; ranges use hyphens.

---

## A. The ten load-bearing figures the report turns on

| # | Figure | Value | As-of | Basis | Ledger row | Status | Tier | What turns on it |
|---|---|---|---|---|---|---|---|---|
| 1 | Anthropic annualized run-rate | $65.0B | end-Jul-2026 (reported Aug-17) | GROSS run-rate (incl. cloud-partner resale); company investor update via CNBC/Bloomberg/TechCrunch/Fortune | L-032 | confirmed | T2 | Every Anthropic multiple, CE ratio, the equalization, the AIBQ CE-1 move |
| 2 | OpenAI annualized run-rate | >$40.0B | July-2026 performance (reported Aug-13/14) | Basis NOT stated (register convention: NET of Microsoft share); Bloomberg via Yahoo; Friar +35% QTD Aug-19 | L-065, L-069 | confirmed | T2 | Every OpenAI multiple and CE ratio; C-16 switch |
| 3 | Anthropic equity-only capital raised | $124,254M | 2026-05-28 (Series H close) | Sum of ten PB equity rounds incl. converted convertibles; excludes $2.5B revolver and the $34.5B lease SPV | L-007 | estimated (derived) | T2 | CE denominator (Ruling 1); the "entry fee" headline |
| 4 | OpenAI equity-only capital raised | $181,216.5M | 2026-03-31 | Sum of PB equity rounds; excludes $5,220M debt and $1,030M grants | L-022 | estimated (derived) | T2 | CE denominator; the "entry fee" headline |
| 5 | Anthropic Q2-2026 revenue and first operating profit | $11.5-11.6B revenue; operating profit projected $559M, sign confirmed | Q2-2026 (reported Aug-14/17/19) | Recognized quarterly revenue, preliminary, GROSS presumed; profit is a company projection (pre-Aug-14), WSJ confirms "a small operating profit" without an amount | L-033, L-034 | confirmed | T2 | The strongest counter-evidence to the thesis; CE-3; the GM cross-check; C-12 |
| 6 | OpenAI Q2-2026 revenue and operating loss | $6.7B revenue (Q1 $5.7B); operating loss $12.3B incl. SBC (Q1 $9.3B) | Q2-2026 (WSJ Aug-19) | Recognized quarterly, NET presumed | L-066 | confirmed | T2 | The strongest evidence for the thesis; CE-3; the burn-vs-loss bridge |
| 7 | OpenAI compute spend, 2026 and through 2030 | $50B (2026); ~$750B (2026-2030 plan, up from ~$600B) | 2026-05-05 (sworn) / 2026-07-22 | Company statement in court; WSJ on the plan | L-078, L-062 | confirmed / estimated | T2 | The consumption side of the obligation stack; §3, §4, §11 |
| 8 | Microsoft revenue from OpenAI arrangements | $24.1B FY2026 (Jul-2025 to Jun-2026); A/R $6.0B | 2026-06-30 (10-K filed Jul-29) | Azure consumption plus revenue-sharing received, at Microsoft | L-054 | confirmed | T1 | The only T1 cash anchor in the OpenAI stack; §7 |
| 9 | SB Energy PORTS-Pike leases and Nvidia guaranty | 17 leases, ~8.0 GW-IT, 20-yr, OpenAI tenant; Nvidia RVG $105B on ~4.25 GW-IT; "OpenAI is not an investment-grade tenant" | 2026-08-17 (S-1 filed Sep-1) | Issuer filing | L-061 | confirmed | T1 | §6 (who holds the risk); CI-2; the quasi-debt argument |
| 10 | Anthropic 2028 revenue forecast to IPO investors | $190-200B | FY2028E (Aug-2026 vintage) | Company forecast per two sources familiar (Reuters exclusive; Business Times same wire); presumably GROSS | L-036 | estimated | T2 | §5 (the margin-commitment incompatibility) together with the T4 GM path (L-119) and T4 training plan (L-125) |

Frame constants inherited from the Rulings and the marks (not "figures the report turns on" but figures every figure is divided by): Anthropic $965B post (L-005/L-038 · confirmed · T2/T1 · 2026-05-28); OpenAI $852B post (L-019/L-020 · confirmed · T2 · 2026-03-31; re-affirmed by the Aug-10 tender at the same price, L-067); the 39.75% equalization (L-126 · recalled · T4 · Ruling 5) with the ~27% external branch (C-13).

Tier note: none of the ten is T1 except #8 and #9. The run-rates (#1, #2) are company-to-investor communications relayed by T2 outlets; the Q2 prints (#5, #6) are leaked to WSJ/Reuters; the equity sums (#3, #4) are derived from PitchBook deal records. The S-1s will replace #1-#6 with audited figures. The report must say so once, in the methodology box, and not apologize for it on every page.

---

## B. Claims by section

Status key: KEEP · KEEP-WITH-FLAG (KWF) · CUT. "Weakest" = tier of the weakest load-bearing row (colour rows do not count).

### §0 Executive summary

| ID | Claim | Rows | Weakest | Falsifier | Status |
|---|---|---|---|---|---|
| AM-01 | Standing at the frontier has cost $124.3B (Anthropic) and $181.2B (OpenAI) of equity, before any debt or lease; the two labs have signed documented compute contracts of $324B (Anthropic, eight counterparties) and $480B (OpenAI, four counterparties) on top | L-007, L-022, L-072, L-074, L-046, L-076, L-135, L-137, L-048, L-136, L-064, L-058, L-149 | T3 (Volta L-048 inside the $324B; press-valued Oracle/AWS inside the $480B at T2) | A public S-1 showing materially smaller purchase obligations in the commitments note | KWF (state "documented-$, scope in Exhibit 5") |
| AM-02 | The larger obligation tallies in circulation ($1.15T, $1.4T) are not verifiable at T1/T2: 59% of the $1.15T rests on could-not-verify rows (Azure $250B, Broadcom $350B, AMD $90B) | L-121, L-122, L-123, L-062, L-064, L-058, L-149 | T4 (the CNV rows themselves) | Microsoft/Broadcom/AMD disclosing the dollar values | KEEP (the claim is about verifiability, and the CNV status is T1-checked against the 10-K and the Broadcom call) |
| AM-03 | Revenue has beaten every plan in the ledger while gross margin has missed every plan in the ledger, at both labs | L-120 vs L-032/L-036 (Anthropic plan vs actual); L-082 vs L-065 (OpenAI plan vs actual); L-083 (OpenAI GM 33% vs 46% plan); L-119 (Anthropic GM lowered) | T4 (L-119, L-120 recalled) | A T2 disclosure that Anthropic's 2026 GM is at or above its January plan | KWF |
| AM-04 | The thesis is weaker than in v4 at the operating-profit level (Anthropic Q2) and stronger at the commitment level (both) | L-034, L-066, L-062, L-138 | T2 | Anthropic's H2-2026 or FY2026 operating result turning negative would restore v4; OpenAI's operating loss narrowing QoQ would weaken v5 | KEEP |
| AM-05 | The cost architecture is not reflected in secondary prices: marks stood still ($852B tender flat; $965B unchanged) while documented commitments more than doubled in 2026 | L-067, L-005, L-019, L-138, L-072-L-077, L-135-L-137 | T2 | A secondary print or IPO range below the standing marks that cites compute obligations | KEEP (doctrine test: analysis, not commentary) |

### §1 The 5-Layer Cost Stack

| ID | Claim | Rows | Weakest | Falsifier | Status |
|---|---|---|---|---|---|
| AM-06 | Neither lab owns a meaningful GPU fleet on its own balance sheet; the capex sits with Microsoft, Oracle, CoreWeave, SB Energy, AMD and Nvidia-backed SPVs; both labs' compute is lease or consumption opex with prepayments | L-132, L-044, L-061, L-057, L-146, L-145 | T1 | An S-1 balance sheet with material PP&E in GPUs | KEEP |
| AM-07 | Anthropic's 2024 COGS was $1.94B on $1.0B of revenue (GM −94%); 2025 GM ~40% | L-012, L-119 | T4 (L-119 recalled) | S-1 historical financials | KWF |
| AM-08 | Anthropic FY2026E gross recognized revenue is $58-63B on a linear ramp from the July run-rate to the $100-120B year-end expectation, $49B if flat from July; PB's $65B is a projection at the top of that range | L-032, L-033, L-035, L-129, L-010 | T3 (L-035 investor expectation) | The S-1's FY2026 revenue outside $49-65B | KWF (label "derived, investor expectation, not guidance") |
| AM-09 | OpenAI FY2026E net recognized revenue is $32-46B (H1 $12.4B plus a July >$40B run-rate at 0-20% monthly growth); PB's $41.3B is a projection inside that range | L-066, L-065, L-024 | T2 | An S-1 FY2026 figure outside the range | KEEP (label "derived") |
| AM-10 | OpenAI's 2026 compute spend of $50B does not reconcile to the T4 training ($25B) plus T3 inference ($14.1B) split: $10.9B is unexplained; the split is not a fact | L-078, L-125, L-083 | T4 | A disclosed 2026 R&D compute / COGS split | KWF |
| AM-11 | Anthropic's 2026 compute spend cannot be stated on a basis comparable with OpenAI's $50B; the only comparable object is the Q2 print and the derived COGS envelope ($23-35B) | L-128, L-078, L-034, L-119 | could-not-verify (L-128) | The S-1 cost of revenue and R&D lines | KWF (print the HOLE) |

### §2 Revenue on a comparable basis

| ID | Claim | Rows | Weakest | Falsifier | Status |
|---|---|---|---|---|---|
| AM-12 | Anthropic reports GROSS (cloud-partner resale counted as revenue, partner payouts as COGS); OpenAI reports NET; the two run-rates are never comparable raw | L-127, L-126, L-065 (Bloomberg methodology caveat) | T3 (Sacra) | Anthropic's S-1 revenue-recognition note showing agent (net) treatment | KWF |
| AM-13 | On the 39.75% equalization Anthropic's net run-rate is $39.2B, its multiple 24.6x and its equalized CE 0.315x; on the ~27% external branch: $47.5B, 20.3x, 0.382x. OpenAI: 21.3x, 0.221x | L-032, L-126, L-005, L-007, L-065, L-022, L-019 | T4 (39.75% and 27% are both T4; C-13) | The S-1 gross-to-net disclosure | KWF (Ruling 5 base case; both branches printed) |
| AM-14 | The Jul-16 "no multiple discount, both at 34.1x" finding is superseded: on the Sep-9 run-rates the sign of the relative multiple flips inside the haircut range (Anthropic at a 15% premium at 39.75%, a 5% discount at 27%); the "no discount" conclusion is not robust to the basis dispute | L-032, L-065, L-126, C-13 | T4 | Resolution of C-13 by the S-1 | KWF (this is the report's basis-risk headline) |
| AM-15 | Both multiples compressed on growth alone with no new marks: 34.1x/34.1x (Jul-16 basis) to 24.6x/21.3x | L-032, L-065, L-005, L-019, L-067 | T2 | A new primary round or IPO range | KEEP |
| AM-16 | On Q2-2026 recognized revenue Anthropic is ahead of OpenAI on either basis ($7.0-8.5B net vs $6.7B), while on July run-rates the two are near parity on a net basis ($39-47B vs >$40B); the two comparisons reconcile only if OpenAI's July jump (>20% MoM) is real and sustained | L-033, L-066, L-032, L-065 | T2 | Q3 prints | KEEP (state the tension) |
| AM-17 | Every PitchBook "TTM" revenue field on both profiles is a forward projection ($71B TTM 4Q2027 Anthropic; $41.3B TTM 4Q2026 OpenAI; PB FY2025 $20B OpenAI is run-rate-vintage) and must never be cited as current | L-009, L-010, L-024, L-025, C-06 | T2 | n/a (definitional, Ruling 4) | KEEP |
| AM-18 | Anthropic's run-rate ladder is now T1/T2 at every step: $9B (Dec-2025) → $30B (Apr-6) → $47B (May) → $65B (end-Jul) | L-139, L-037, L-032 | T2 | n/a | KEEP |

### §3 The obligation stack

| ID | Claim | Rows | Weakest | Falsifier | Status |
|---|---|---|---|---|---|
| AM-19 | The SpaceX contract is the largest cancellable item in either stack: $1.25B/month through May-2029 (≤ ~$45B) terminable by either party on 90 days' notice, so the contracted amount at any moment is ~$3.75B | L-046 | T1 | S-1 commitments note treating it as a firm purchase obligation | KEEP |
| AM-20 | The $34.5B TPU chip financing is lessor/SPV debt (Apollo-led, Broadcom- and Google-supported), not Anthropic-issued bonds; PitchBook removed it from Anthropic's Total Raised, which is why Total Raised fell from $161.254B to $126.754B; equity-only is unaffected | L-044, L-006, L-007, C-01 | T3 (Epoch) | Anthropic's S-1 showing the $34.5B as its own debt | KWF |
| AM-21 | Anthropic's August neocloud contracts (Riot $9.1B/20 yr, Volta $10B/6 yr, Nscale ~$45B/6 yr, Lambda $35B) added ~$99B of documented commitments in 27 days | L-136, L-048, L-135, L-137 | T3 (Volta) | Contract terms published showing options rather than commitments | KWF |
| AM-22 | Bloomberg's "at least $175B" reconciles exactly (Lambda + Nscale + Fluidstack + SpaceX at maximum); TechCrunch's "$61B" mixes an equity inflow with compute; the "$517B" tally is not reproducible | L-138 | T2 | n/a | KEEP (cite Bloomberg's components; do not cite the other two) |
| AM-23 | OpenAI's Oracle $300B and AWS ~$138B are press-valued; Oracle's own disclosure is total RPO of $638B (up from $138B) with no customer above 10% of revenue | L-064, L-056 | T2 | Oracle naming OpenAI or an S-1 purchase-obligation table | KEEP |
| AM-24 | The Nvidia "$100B / 10 GW" commitment no longer exists: Nvidia invested $30B in the March round, Huang said the rest is "probably not in the cards", and Nvidia instead guaranteed $105B of residual value on OpenAI's Ohio leases | L-075, L-061, C-20 | T2 | Nvidia funding further tranches | KEEP (C-20 resolved as supersession) |
| AM-25 | The four OpenAI tallies are four scopes: $665B (Feb spend plan), $600B → $750B (May → Jul compute-spend plan), $1.15T (obligations through 2035), $1.4T (headline commitments); they are never one number and never compared with a burn plan | L-082, L-078, L-062 | T3 (L-082) | n/a (definitional) | KEEP |
| AM-26 | Documented OpenAI commitments ($480B) are 12x the July run-rate; the vendor list is at least nine (Microsoft, Oracle, CoreWeave, AWS, Nvidia, AMD, Broadcom, Cerebras, SB Energy) | L-064, L-058, L-149, L-061, L-060, L-050, L-054, L-065 | T2 | n/a | KEEP |
| AM-27 | Cash paid to date is largely undisclosed; the only hard anchors are Microsoft's $24.1B FY2026, OpenAI's $50B 2026 plan, OpenAI's $1.0B loan to Cerebras, SpaceX's ≤$2.56B Q2 AI-segment revenue and Anthropic's $1.5B settlement | L-054, L-078, L-149, L-047, L-086 | T2 | n/a | KEEP (print the HOLE column) |

### §4 Training vs inference

| ID | Claim | Rows | Weakest | Falsifier | Status |
|---|---|---|---|---|---|
| AM-28 | The "leaked" training lines ($7B/$14B/$22B Anthropic; $25B/$60B/$112B/$120B OpenAI) are annual training-compute budgets; Epoch's per-run estimates (Grok 4 ~$500M; GPT-4.5 ~$200M pre-training) are a different basis; the two are shown side by side and never summed (C-11 resolved as a basis label) | L-125, L-115 | T4 (L-125) | Underlying documents located | KWF |
| AM-29 | OpenAI's 2028 training budget ($112B, T4) alone exceeds its July run-rate; the 2027-2030 compute plan averages ~$175B/yr against a run-rate of >$40B | L-125, L-062, L-065 | T4 | A revised plan | KWF |
| AM-30 | OpenAI's inference cost ($8.4B 2025 → $14.1B 2026E) is 31-44% of FY2026E revenue; the ads run-rate ($1.0B) covers ~7% of 2026E inference cost | L-083, L-081, L-066, L-065 | T3 | S-1 cost of revenue | KWF |
| AM-31 | The v4 "free-tier subsidy" arithmetic (~34% of inference, ~$2.86B, ~910M non-payers) has no external source | L-083 notes | n/a | n/a | CUT |
| AM-32 | The WSJ Apr-6 dual-P&L breakeven years (OpenAI excl-training 2026 / incl-training 2030→2029; Anthropic 2025 / 2028; FCF troughs −$110B / −$25B; cum. −$198B → −$99B; FCF 2030 +$30B → +$151B) have no fresh ledger row; only "cum. $198B" is referenced (L-125 notes, T4) | L-125 notes | T4 / none | n/a | CUT (replace with L-082's 2030 positive cash flow $39B, T3, and L-034) |
| AM-33 | Anthropic's Q2 operating profit implies gross-basis GM of 31-48% (net-basis 51-80%) for AJ quarterly opex of $3-5B: the GM band a reader sees depends on the reporting basis, not only on the business | L-034, L-033, L-126 | T2 (arithmetic; opex is AJ) | The S-1 income statement | KWF (label the opex assumption) |

### §5 The margin-commitment incompatibility (new)

| ID | Claim | Rows | Weakest | Falsifier | Status |
|---|---|---|---|---|---|
| AM-34 | On Anthropic's own 2028 plan (revenue $190-200B, GM 77%, training $22B) the annual compute envelope is ~$66-68B; priced commitments already run ~$53B in 2028; the unpriced Google TPU (5 GW contracted, 10 GW more in vendor line of sight) and AMD 2 GW deals are the largest items: the contracted 5 GW alone exceeds the remainder by $30-50B/yr at any plausible $/MW-yr, and the 2028 line of sight would take the excess to $125-175B/yr; one of {77% GM, $22B training, take-or-pay status of the GW deals} is untrue | L-036, L-119, L-125, L-072, L-074, L-046, L-135, L-048, L-136, L-137, L-044, L-049, L-043, L-134 | T4 (L-119, L-125) | The S-1 commitments note showing the GW deals as options or consumption-based; or a GM path below 77%; or a training budget above $22B | KWF (the report's "next mispricing"; present as a conditional with the three exits) |
| AM-35 | Full-stack GPU capacity prices at ~$12-16M per MW-yr (Nscale, Volta) versus ~$1.8-2.4M for powered shell (Core Scientific-AMD, Riot); the TPU SPV implies ~$6.9M per MW-yr for chips alone | L-134, L-135, L-048, L-148, L-136, L-044 | T3 (derived) | Published lease terms | KWF |
| AM-36 | Vendor guidance (Broadcom's "line of sight" to 10 GW in 2028) is demand signalling, not disclosed contract; the report treats it as unpriced and optional until a filing says otherwise | L-049, L-144 | T1 (the statement) | An Anthropic filing listing it as a firm commitment | KEEP |

### §6 Who holds the risk (new; absorbs v4 §7 financing)

| ID | Claim | Rows | Weakest | Falsifier | Status |
|---|---|---|---|---|---|
| AM-37 | The labs' cost of capacity is being financed off their balance sheets at investment-grade-like rates because vendors carry the tail: the TPU SPV prices at T+1pt / 5.75% / 8.5% with Broadcom and Google absorbing losses; Nvidia guarantees $105B of residual value on OpenAI's Ohio leases and holds Anthropic's Lambda lease; AMD provides credit support at Core Scientific | L-044, L-061, L-137, L-148, L-146, L-106 | T3 (L-044) | Any of these structures failing to close or being repriced | KWF |
| AM-38 | The spread between backstopped SPV debt (5.75%) and unbackstopped neocloud notes (9.0-9.75%) is 300-400 bp: the price of the guarantee | L-059, L-044, L-106 | T3 | n/a (arithmetic) | KWF |
| AM-39 | The subsidy has an accounting cost at the counterparties (SB Energy's $2.57B warrant fair-value charge; AMD's $4.1B lease guarantees; Microsoft's $6.5B recap gain reflects dilution, not cash) and Huang says the equity leg "might be the last time" | L-147, L-146, L-054, L-075 | T1/T2 | Nvidia or Broadcom announcing further lab equity | KEEP |
| AM-40 | "OpenAI is not an investment-grade tenant" is the landlord's own disclosure; 20-year leases signed by such a tenant are quasi-debt the CE-4 and CI-2 scores must carry | L-061 | T1 | A rating or an S-1 balance sheet contradicting it | KEEP |

### §7 Microsoft and OpenAI

| ID | Claim | Rows | Weakest | Falsifier | Status |
|---|---|---|---|---|---|
| AM-41 | Microsoft recorded $24.1B of FY2026 revenue from OpenAI arrangements including revenue sharing, with $6.0B receivable at June-30: the only T1 cash anchor in the OpenAI stack | L-054 | T1 | n/a | KEEP |
| AM-42 | The revenue share continues through 2030 at the same percentage subject to a total cap (official); the cap is $38B (single-outlet, T3); the percentage is not confirmed at T1/T2 | L-051, L-052 | T3 (the cap) | The S-1 related-party note | KWF (never print "20%") |
| AM-43 | Microsoft's stake is below 27% and undisclosed after the March round ("our proportionate ownership of OpenAI decreased") | L-054, L-053, C-19 | T4 (the 27%) | S-1 cap table | KWF (print "below 27%") |
| AM-44 | Microsoft's RPO of $678B grew 25% excluding OpenAI; the OpenAI component is large and undisclosed; the $250B Azure commitment could not be verified at T1/T2 | L-055, L-121 | T4 (the $250B) | Microsoft disclosing it | KEEP (as a verifiability statement) |
| AM-45 | "$17.2B paid to Microsoft in FY2025" is a calendar-2025 figure on a different basis from the $24.1B and must not be trended against it | L-054 notes | T4 (recalled) | n/a | KWF |

### §8 Capital efficiency on an equity-only denominator

| ID | Claim | Rows | Weakest | Falsifier | Status |
|---|---|---|---|---|---|
| AM-46 | Equity-only denominators reproduce PB Total Raised exactly when the disclosed debt is added back ($124,254 + $2,500 = $126,754; $181,216.5 + $5,220 = $186,436.5) | L-007, L-006, L-022, L-021 | T2 | PB revising a round | KEEP |
| AM-47 | The equalized CE advantage narrowed from 1.65x (Jul-16) to 1.43x (base) because OpenAI's run-rate grew faster from a lower base; on the 27% branch it is 1.73x; raw gross it is 2.37x and forbidden by Ruling 5 | L-032, L-065, L-007, L-022, L-126 | T4 (basis) | C-13 resolution | KWF |
| AM-48 | The Series H included $15B of previously committed hyperscaler investments ($5B Amazon; $10B Google at a $350B valuation); "new cash" in the round is at most $50B | L-038, L-072, L-073 | T1 | n/a | KEEP |
| AM-49 | AMD's "up to $5B" is a contingent, milestone-based commitment funded through FY2028 and not a priced round; it is not in capital raised | L-043, L-013 | T1 | AMD funding at a disclosed valuation | KEEP |

### §9 AIBQ

| ID | Claim | Rows | Weakest | Falsifier | Status |
|---|---|---|---|---|---|
| AM-50 | Re-run on the rubric, Anthropic CE moves 8.0 → 7.3 (composite −0.14) and CI 5.05 → 5.55 (+0.075); OpenAI CE 3.05 → 3.9 (+0.175) and CI 4.5 → 5.6 (+0.165); composites 8.20 → 8.13 and 4.53 → 4.87; tiers unchanged | `analysis/aibq-delta.md`; L-133 and rows therein | T4 (CE-2 GM; the prior sub-scores) | NEXUS re-score disagreeing on a logged event | KWF (flag the method-driven CE-1 move) |
| AM-51 | The $/AIBQ-point ladder narrows from 1.60x to 1.47x (OpenAI $175B/pt vs Anthropic $119B/pt) | L-005, L-019, aibq-delta §5 | T4 | New marks | KWF |
| AM-52 | The correlation coefficient is embargoed and not reported | Ruling 2 | n/a | n/a | KEEP (compliance) |

### §10 Outside view

| ID | Claim | Rows | Weakest | Falsifier | Status |
|---|---|---|---|---|---|
| AM-53 | Frontier-lab plan-vs-actual base rate in this ledger: revenue plans were exceeded in every observed case (Anthropic Jan-2026 $18B 2026 plan beaten by July; 2028 plan $102B → $190-200B in seven months; OpenAI $30B 2026 plan vs >$40B run-rate; PB projections +29% and +38% in eight weeks); cost plans were revised up in every observed case ($600B → $750B; burn +$111B); margin plans were missed in both observed cases | L-120, L-032, L-036, L-082, L-065, L-009, L-024, L-078, L-062, L-083, L-119 | T4 (L-120) | A plan revised down | KWF |
| AM-54 | Dated milestones in the ledger slipped in every observed case: no public S-1 for either lab by Sep-9 against September/October windows; ChatGPT's 1B-user milestone seven months late; Abilene capped at 1.2 GW from 2.1 GW; five Stargate sites clustered at Q4-2028 | L-001, L-002, L-004, L-040, L-080, L-079 | T3 | A milestone hit on time | KWF |
| AM-55 | Datacenter build cost rose 21% per MW since Q4-2024 to $17.6M per MW all-in | L-109 | T2 | Next year's guide | KEEP |
| AM-56 | Hypergrowth revenue-growth decay and capex-heavy GM paths have no base-rate source in the ledger; the base rates used are analyst judgment and labelled so | none | n/a | n/a | KWF (label "analyst judgment") |

### §11 Scenarios and sensitivities

| ID | Claim | Rows | Weakest | Falsifier | Status |
|---|---|---|---|---|---|
| AM-57 | The three inputs the answer turns on are: the gross-to-net haircut (27-39.75%), Anthropic's 2028 GM (60-77%), and OpenAI's revenue growth against a ~$175B/yr compute plan | L-126, L-119, L-062, L-065 | T4 | n/a | KWF |
| AM-58 | Relative value between the two names swings ~$190B on the haircut alone (15% premium to 5% discount on $965B) | L-032, L-065, L-126, L-005 | T4 | C-13 resolution | KWF |

### §12 Greenfield entry cost (new)

| ID | Claim | Rows | Weakest | Falsifier | Status |
|---|---|---|---|---|---|
| AM-59 | Contracted large-cluster GPU-hours price at $2.40-4.00 (B200/GB300), far below on-demand rack rates ($6.7-10.5); rack hardware is $2-4M per NVL72 rack; all point estimates are channel/index figures | L-105, L-104, L-103 | T4 (L-103) | Published Nvidia list prices | KWF |
| AM-60 | Owning 1 GW-IT of Blackwell-class capacity costs ~$36B up front (build $17.6B + chips ~$16.7B + network ~$1.7B + storage ~$0.5B) plus ~$0.4-0.6B/yr of power; leasing the same as full-stack capacity costs ~$12-16B/yr; leasing only the powered shell ~$1.8-2.4B/yr | L-109, L-103, L-107, L-111, L-112, L-108, L-134, L-148, L-136 | T4 (L-103, L-112) | Published TCO | KWF |
| AM-61 | A frontier final training run costs ~$500M today and >$1B by 2027 (2.4x/yr); annual frontier training budgets at the incumbents are 10-50x that ($7B; $25B) because they aggregate runs, experiments and post-training | L-115, L-125 | T4 | Epoch revision | KWF |
| AM-62 | Custom-silicon supply for a new entrant is fully booked through 2028 by six incumbent XPU customers (Broadcom AI revenue $58B → $115B → $230B, supply secured) | L-144, L-050 | T1 | Broadcom adding capacity | KEEP |
| AM-63 | The reference class says entry costs $2-8B to a credible model with little revenue (TML $2B seed → "a few hundred million" annualized; Mistral $7.5B → ~$1.2B projected; SSI $7B → zero revenue; Reflection $2.2B), and $40B+ of accumulated losses to a vertically integrated lab with ~$3B of revenue (xAI inside SpaceX) | L-098, L-100, L-097, L-099, L-096 | T2 | n/a | KEEP |
| AM-64 | Top-decile researcher packages price at $25-100M per year over four years at the extreme; base salaries for senior technical staff at Anthropic reach $1.1-1.4M | L-094, L-092 | T3 (L-092) | n/a | KWF |
| AM-65 | Copyright exposure is a real cost line: $1.5B paid by Anthropic; >$3B demanded by music publishers; NYT v. OpenAI pending without a damages figure | L-086, L-088 | T4 (L-088) | Rulings | KWF |

### §13 Verdict, weaker/stronger, falsifiers

| ID | Claim | Rows | Weakest | Falsifier | Status |
|---|---|---|---|---|---|
| AM-66 | OpenAI's IPO in September 2026 is arithmetically impossible (no public S-1 on EDGAR by Sep-9; 15-day public-filing rule); the live branches are Q4-2026-if-inflect and 2027 (Friar) | L-002, L-004, L-068, L-001 notes | T1 | A public S-1 appearing within days | KEEP (C-02 partially resolved: the September leg is retired; the switch keeps Q4-26 vs 2027) |
| AM-67 | Anthropic's public S-1 has not appeared as of Sep-9; the reported timetable has slipped from "after Labor Day" to "mid-October"; an October pricing still requires a public flip by roughly late September | L-001, L-039, L-003, L-040 | T3 (L-040) | The public flip | KWF |
| AM-68 | SpaceX's Q2 AI segment ($2.56B revenue, +247%; $1.26B operating loss; consolidated capex $18.4B) is the first public print of a frontier-adjacent cost base and shows the ramp of the Anthropic contract | L-047 | T2 | n/a | KEEP |
| AM-69 | Prediction-market colour (Kalshi 72% Anthropic lists first) is T4 and colour only | L-141 | T4 | n/a | KWF (colour) |

---

## C. Claims CUT (cannot be traced to a ledger row, or superseded by one)

| Old claim (v4 / Jul-16 register / DATA_PACK) | Why cut | Replacement |
|---|---|---|
| "$665B obligations vs $115B burn" | Mixes a Feb-2026 spend plan with a superseded burn vintage (L-082 notes) | §3 scope table (AM-25) |
| "$1.15T obligations across 7 vendors" as a single number | 59% rests on CNV rows (L-121, L-122, L-123); vendor count is now nine | AM-02, AM-26 |
| "~34% of inference COGS (~$2.86B) subsidizes ~910M non-payers" | Internal derivation not found externally (L-083 notes) | AM-30 |
| "SemiAnalysis 70%+ inference-infrastructure GM" | Could not verify; paywalled (L-116, L-119) | none |
| WSJ Apr-6 dual-P&L breakeven years, FCF troughs, cum. FCF bridge, "$38B cap moves breakeven 2030 → 2029 and FCF +$30B → +$151B" | No fresh ledger row (only "cum. $198B" is referenced at T4 in L-125 notes) | L-082 (2030 positive cash flow $39B, T3); L-034 (Anthropic Q2 operating profit) |
| "Microsoft revenue share = 20%" | T4 only (L-052 notes) | "same percentage, subject to a total cap" (L-051, T1) |
| "Azure $250B", "Broadcom $350B / 10 GW", "AMD $90B" as facts | Could-not-verify (L-121, L-122, L-123) | Appear only in the scope table, flagged CNV; prose uses GW and T1 terms |
| "Nvidia $100B / 10 GW commitment" | Superseded (L-075, C-20) | AM-24 |
| "OpenAI capex $190B 2026E (earnings call)" | Mis-tagged hyperscaler figure; no OpenAI earnings call (L-124) | L-078 ($50B compute spend) |
| "Anthropic total raised $161.254B incl. $37.0B debt" and "$34.5B chip bonds tranched $6.0B / $24.0B / $4.5B" | Superseded (L-006, L-044); tranches are A1/A2/B by rate | AM-20 |
| "Fast Mode ~3x cheaper (~$1.67 / $8.33)" | Direction reversed at T1 (L-084, C-07) | "Fast Mode at 2x standard pricing on Opus 5" |
| "Anthropic compute spend 2026 ~$19B" | T4 conflation with the April run-rate (L-128) | HOLE printed (AM-11) |
| "$80B+ compute commitments across 6 partners" | Superseded (L-138) | AM-21, AM-22 |
| "$517B" and "$61B" Anthropic tallies | Not reproducible / mixes equity (L-138) | AM-22 |
| "Anthropic secondary implies $1.50T at $925/share" or "low-to-mid $800B" | Two T4 sources contradict; neither verified (C-15) | "secondary prints disagree; the primary mark is $965B" |
| "NRR 140%+; 80% enterprise; Claude Code $2.5B ARR; 54% coding share" | No ledger row | >1,000 customers at >$1M annualized (L-139, T1) |
| "xAI raised $47.16B pre-merger" | Not reproducible from PB or the S-1 (L-096) | Accumulated deficit $41.3B; AI-segment P&L (L-096, T1) |
| "SSI $3B raised" | Superseded ($7.0B PB / $8B press, C-08) | L-097 with C-08 frozen |
| "OpenAI enterprise mix 15% vs 35-40%" | No ledger row | Enterprise run-rate +50% (L-069, T2) |
| "FY2025 net income −$42B" (either company, PB) | PB artifact (C-04) | none |
| "OpenAI FY2025 revenue $20B (PB)" as recognized | Run-rate vintage (C-06) | $13.1B (L-063, T2) |
| Any PB TTM field cited as current revenue | Ruling 4 | Labelled projections only |
| "Anthropic training $30B 2029E", "OpenAI training $90B 2030E" | No ledger row (L-125 stops at 2028 / 2029) | HOLE (scenario inputs) |
| "Georgia $30B+ DC (Jul-22)", "$500B Nvidia-backed DC deal (Jul-27)" | No ledger row | none |
| "Stargate UAE 1 GW / 5 GW" | Could not verify this run (L-130) | one line: "not verified" |
| "Anthropic 8.20 canonical vs 8.06 live" as a dispute the report adjudicates | Both are prior scores; the report applies deltas to the canonical base | aibq-delta §5 |
| "Morningstar FVE $780B"; "SPCX tape levels" | Outside the ledger; belongs to other notes | none |

---

## D. Frozen conflicts the argument map inherits (both branches live in the text)

C-02 (residual: Q4-2026 vs 2027 for OpenAI's IPO) · C-03 (Anthropic FY2025 recognized: PB $10B vs implied $4.5-6B) · C-05 (Anthropic FY2024 net loss −$5.3B vs −$8.3B) · C-08 (SSI round size) · C-12 (Anthropic 2026 loss/burn definitions and vintage) · C-13 (39.75% vs ~27%) · C-15 (secondary marks) · C-16 (OpenAI run-rate basis) · C-18 (Anthropic headcount 5,000 vs ~4,020). Resolved by the ledger and stated as resolved: C-01 (classification), C-04 (artifact; both figures dropped), C-06 (vintage), C-07 (T1 governs), C-09 (minor), C-10 (PB date artifact), C-11 (basis label), C-14 (scope table), C-17 (company statement governs), C-19 (range statement), C-20 (supersession), O-15 Altman title (PB artifact, L-028/L-070/L-089).
