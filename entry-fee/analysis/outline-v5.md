# Outline v5.0: The $100 Billion Entry Fee: The Cost Architecture That Wall Street Isn't Pricing
Agent 2 (Analyst), 2026-09-09. Target for the Writer: 9,000-12,000 words, 18 exhibits (numbered E1-E18), each mapped to a workbook tab (A = report model `100B_Entry_Fee_v5.xlsx`; B = greenfield model `Greenfield_Entry_Cost_v5.xlsx`; tab list in `analysis/model-spec.md`). Every section is marked **unchanged / figures refreshed / argument changed / new** against the v4 map (`prior/v4-reconstruction.md` §3). Word targets are guidance; the argument map (`analysis/argument-map.md`) governs what each section may claim. No em-dashes anywhere in the report; ranges use hyphens; $14.2B not "14.2 billion"; 27.1x; +47% YoY; active voice.

Doctrine test applied before each section was admitted: is this already in secondary prices? Marks stood still (Anthropic $965B unchanged since May-28, L-005; OpenAI's Aug-10 tender at the unchanged $852B, L-067) while documented commitments more than doubled (L-138, L-135-L-137). The cost architecture is not in the prices. The sections below are analysis, not commentary, with two exceptions marked "context only".

Thesis to test, not assume: frontier AI cost architecture is structurally incompatible with investable return profiles. v5's answer (developed in §13): weaker at the operating-profit level, stronger at the commitment level, and the next mispricing is a specific incompatibility inside Anthropic's own plan (§5), not a general "costs are high" claim.

---

## Section plan

| § | Title | Mark vs v4 | Words | The point (one sentence) | Exhibits | Tab |
|---|---|---|---|---|---|---|
| 0 | The entry fee, restated | **argument changed** | 900 | $124.3B and $181.2B of equity bought two seats at the frontier; the seats now carry $324B and $480B of documented compute contracts (and a reported, unverified ~$200B Google leg), and the S-1s will show, for the first time, whether the contracts or the margins are real | E1 | A/08_Output |
| 1 | The 5-Layer Cost Stack: definition, placement rule, and the table | **figures refreshed** (definition printed for the first time) | 800 | Every seed figure sits in exactly one layer; layers 1-2 are commitments, 3-5 are consumption; most 2023A-2025A cells are holes the S-1s will fill | E2, E3 | A/00_Assumptions, A/03_Costs, A/09_Obligations |
| 2 | Revenue on a comparable basis: run-rate, recognized, forward; gross and net | **argument changed** | 900 | On today's run-rates the "no multiple discount" finding is not robust: the relative multiple flips sign inside the gross-to-net haircut range, so basis risk is now worth ~$190B of relative value | E4, E5 | A/02_Revenue, A/06_Valuation |
| 3 | The obligation stack: contracted, cash, cancellable | **argument changed** | 900 | The tallies in circulation are scopes, not numbers; documented-$ contracts are $324B and $480B; the largest single Anthropic item is terminable on 90 days' notice; 59% of the $1.15T OpenAI tally is unverifiable | E6, E7, E8 | A/09_Obligations |
| 4 | Training and inference: budgets, runs, and the Q2 prints | **argument changed** (v4 dual-P&L breakeven years CUT) | 700 | Annual training budgets and per-run costs are different objects; OpenAI's sworn $50B does not reconcile to the leaked split; Anthropic's Q2 positive adjusted operating income (non-GAAP, definition unpublished) implies a gross margin whose band depends on the reporting basis | E9 | A/03_Costs, A/04_PL |
| 5 | The margin-commitment incompatibility (the next mispricing) | **new** | 900 | On Anthropic's own 2028 plan the compute envelope is ~$66-68B/yr; priced commitments already run ~$53B; at the reported (unverified) ~$200B five-year value the Google leg alone pushes the 2028 stack to ~$93B, a $25-28B/yr excess; on the $/MW-yr proxy the contracted 5 GW exceeds the remainder by $30-50B/yr and the 2028 line of sight would take that to $125-175B/yr; the 77% margin, the $22B training budget and the take-or-pay status of the GW deals cannot all be true | E10 | A/09_Obligations, A/03_Costs, A/07_Sensitivity |
| 6 | Who holds the risk: vendor-backstopped financing | **new** (absorbs the financing half of v4 §7) | 700 | The labs' cost of capacity is being financed off their balance sheets at near-investment-grade rates because Nvidia, Broadcom, Google and AMD carry the tail; the subsidy is real, priced at 300-400 bp, has an accounting cost at the counterparties, and Huang says the equity leg may be over | E11 | A/10_Financing |
| 7 | Microsoft and OpenAI: the $24.1B anchor | **figures refreshed** | 500 | Microsoft's 10-K gives the only T1 cash numbers in the OpenAI stack ($24.1B of FY2026 revenue; $13.0B committed, $11.9B funded); the cap is single-outlet; the recap stake (27% / 26% / 47%) is T2 and the post-dilution stake and the percentage are documented silences | E12 | A/01_Data, A/09_Obligations |
| 8 | Capital efficiency on an equity-only denominator | **figures refreshed** | 500 | Equity-only denominators reproduce PitchBook exactly; the equalized CE advantage narrowed from 1.65x to 1.43x because OpenAI grew faster from a lower base; $15B of the Series H was previously committed strategic money | E13 | A/05_Cash_Fund |
| 9 | AIBQ: Capital Efficiency and Compute Independence re-run | **figures refreshed** (scores move; tiers do not) | 600 | Anthropic 8.20 → 8.15 (8.13 if the $15B facility closes; a method correction, not a downgrade); OpenAI 4.53 → 4.87 on T1 leases and custom silicon; the $/AIBQ-point ladder narrows from 1.60x to 1.48x; the coefficient stays embargoed | E14, E15 | A/11_AIBQ, A/06_Valuation |
| 10 | Outside view: reference classes and base rates for every forecast | **new** | 700 | In this ledger every revenue plan was beaten, every cost plan revised up, every margin plan missed and every dated milestone slipped; growth decay and margin paths now have sourced base rates (Bessemer endurance; the AWS margin path), IPO slippage does not; the SaaS decay rule applied to current growth lands above the company's own plan | E16 | A/13_OutsideView |
| 11 | Scenarios and sensitivities | **figures refreshed** | 500 | Three inputs move the answer: the haircut (27-39.75%), Anthropic's 2028 GM (60-77%), and OpenAI's revenue growth against a ~$175B/yr compute plan | E17 | A/07_Sensitivity |
| 12 | The greenfield entry fee: starting from zero in 2026 | **new** | 1,300 | Three ways in (lean fast-follower, full frontier, vertically integrated with custom silicon), line by line, time-phased over five years, checked against what xAI, SSI, Thinking Machines, Reflection, Mistral, Periodic, Humans& and Meta actually paid | E18 | B/07_Cash, B/08_Reference, B/09_Output |
| 13 | Where the thesis got weaker, where it got stronger, the verdict, and the falsifiers | **argument changed** | 800 | Three bullets each way, a verdict fenced by four dated falsifiers, and the two IPO windows stated as they stand on Sep-9 | (none; text) | A/08_Output |
| 14 | Frozen conflicts, methodology rulings, provenance | **new** (printed register) | 400 | Nine frozen conflicts rendered as frozen with their model switches; six rulings; the tier legend; the ten load-bearing figures with as-of dates | (table, unnumbered) | A/12_Conflicts, A/01_Data |
| | **Total** | | **~11,100** | | **18** | |

---

## Section-by-section structure

### §0 The entry fee, restated (argument changed; 900 words; E1)
1. Open on the two numbers the S-1s cannot change: $124,254M and $181,216.5M of equity raised (L-007, L-022). Then the two they will change: $65B gross and >$40B (L-032, L-065) run-rates that are company-to-investor communications until audited.
2. The v4 framing ("obligations exceed burn by an order of magnitude") is retired; v5's framing: the entry fee has three prices, burn-to-first-profit (~$15-25B for Anthropic, derived and flagged), capital raised to get there ($124B), and contracts signed to stay there ($324B documented, plus unpriced gigawatts).
3. State where the thesis moved (one paragraph each way) and name the next mispricing (§5) in one sentence.
4. E1 (A/08_Output): the at-a-glance table, both companies: mark, equity raised, run-rate (basis), Q2 recognized, Q2 operating result, documented-$ contracts, unpriced GW, IPO status on Sep-9.

### §1 The 5-Layer Cost Stack (figures refreshed; 800; E2, E3)
1. Print the definition (cost-stack-reconciliation §1) verbatim as E2, including the placement rule and the seed placement line. State that the v4 outline could not be located and this is the definition v5 uses.
2. E3 (A/03_Costs + A/09_Obligations): the layer × year × company table with provenance tags and HOLEs visible. Text walks one column (2026E) for each company and one row (L4) across years.
3. The structural finding (L-132, T1): neither lab owns a GPU fleet; capex sits with counterparties; both labs' compute is opex or lease with prepayments. This is why the S-1 balance sheets will look light and the commitments notes heavy.

### §2 Revenue on a comparable basis (argument changed; 900; E4, E5)
1. Ruling 4 first: every PB "TTM" field is a projection (E4 prints them in a separate column labelled "PB forward").
2. E4 (A/02_Revenue): dated ladders, three columns per company (run-rate, recognized, forward), every entry with basis and row.
3. E5 (A/02_Revenue, A/06_Valuation): the restatement at 39.75% and at ~27%, with multiples and CE at each, and OpenAI's C-16 switch. The finding: 24.6x vs 21.3x at 39.75% (Anthropic premium 15%); 20.3x vs 21.3x at 27% (discount 5%). The Jul-16 "both at 34.1x" is history.
4. The Q2-vs-run-rate tension (argument-map AM-16): Anthropic ahead on Q2 recognized on either basis, near parity on July run-rates; say what has to be true for both to hold. Quarterly ladder now T2 at every step: Q2-2025 $787M → Q1-2026 $4,730M → Q2-2026 >$11,500M (L-151).
5. The C-13 corollary (AM-33): a 39.75% partner payout cannot sit in cost of revenue beside the T4 $0.56 compute ratio (gross margin would be 4%); either the ratio contains the payouts or the effective share is lower. Both legs are T4; print as a flag, not a resolution.

### §3 The obligation stack (argument changed; 900; E6, E7, E8)
1. E6, E7 (A/09_Obligations): the two contracted / cash / cancellable tables from cost-stack-reconciliation §4, with the vendor-backstop attribute.
2. E8: the tally reconciliation (§5 of the reconciliation): four OpenAI scopes, five Anthropic scopes; which reconcile exactly and which are cut.
3. Four paragraphs: SpaceX's 90-day clause (L-046); the $34.5B reclassification and why PB's Total Raised fell $34.5B (C-01, L-044, L-006); the nine-vendor OpenAI list with Cerebras and SB Energy as the two primary-filing additions (L-149, L-061); the disclosure finding: Alphabet's 10-Q (zero Anthropic mentions; $811B of commitments not itemized), Google's release, Broadcom's 10-Q and Microsoft's 10-K disclose no dollar value for these contracts (L-153, L-154, L-156, L-157, L-121), so the only Google figure is a T3 [VERIFY] ~$200B over five years (L-155) that E8 carries as its own scope row and never adds to documented-$.

### §4 Training and inference (argument changed; 700; E9)
1. C-11 as a basis label: annual budgets (L-125, T4) beside per-run estimates (L-115, T3); never summed.
2. OpenAI's $50B (L-078, T2, sworn) and the $10.9B the leaked split does not explain.
3. Anthropic's Q2: revenue $11.5-11.6B (L-033; Q1 $4,730M, L-151), positive ADJUSTED operating income (L-151, T2; non-GAAP, definition unpublished; per T3 relays includes training cost and excludes SBC, L-152), projected at $559M ≈ 5.1% adjusted margin (L-152); the GM implied at $3-5B of quarterly opex (31-48% gross basis, 51-80% net basis) and the T4 compute ratio ($0.71 → $0.56 per revenue dollar, ~44% gross-basis if compute is all of cost of revenue). The point: the margin a reader will see in the S-1 depends on the revenue-recognition basis as much as on the business, and the profit a reader has already seen is a non-GAAP measure.
4. Inference: $8.4B → $14.1B (L-083, T3), 31-44% of FY2026E revenue; ads at $1.0B run-rate cover ~7% of it (L-081). The v4 free-tier arithmetic is gone; say so in a footnote, not the text.
5. E9 (A/03_Costs, A/04_PL): budgets vs runs; the $50B split; the Q2 GM cross-check grid.
6. Do not print breakeven years: the WSJ Apr-6 dual-P&L figures have no fresh row (argument-map AM-32). The only forward cash-flow datapoint is The Information's "positive cash flow $39B in 2030" (L-082, T3, Feb vintage).

### §5 The margin-commitment incompatibility (new; 900; E10)
1. Set up the triad on Anthropic's own plan: revenue $190-200B 2028 (L-036, T2), GM 77% (L-119, T4), training $22B (L-125, T4) → compute envelope ~$66-68B/yr (derived).
2. The priced commitment run in 2028: ~$53B (derived from L-072, L-074, L-046, L-135, L-048, L-136, L-137, L-044 with two stated term assumptions).
3. The Google leg, three branches: (a) reported ~$200B over five years = $40B/yr (L-155, The Information via Reuters, T3, page not opened, [VERIFY]); Alphabet's 10-Q, Google's release and Broadcom's 10-Q are silent on dollars and take-or-pay (L-153, L-154, L-156, T1); (b) proxy for the contracted 5 GW at the SPV-implied $9.3M per MW-yr (chips $6.9M from L-044 plus shell $2.4M from L-136) or the Volta/Nscale $12.5-16.3M (L-134): $46-62B/yr; (c) proxy with Broadcom's 10 GW 2028 line of sight (L-049): 15 GW, $140-188B/yr. AMD 2 GW (L-043) unpriced on top. Consistency: $200B / 5 yr / 5 GW = $8.0M per MW-yr, near the proxy; over 16 GW it would be $2.5M, below chips-only, so the reported figure fits ~5 GW.
4. The three exits: the margin path is lower than 77%; the training budget is higher than $22B; the GW deals are options or consumption-based, not take-or-pay. Each exit has a different valuation consequence; say which the S-1 commitments note will reveal.
5. E10 (A/09_Obligations vs A/03_Costs; band from A/07_Sensitivity): two lines (priced commitments per year; COGS + training envelope per year) with the Google band shaded under SW_GOOGLE_VALUE: reported $40B/yr [VERIFY], or the $/MW-yr proxy switchable at $9.3 / $12.5 / $16.3M and 5 or 15 GW. 2028 gaps: reported branch −$25-28B; proxy 5 GW −$30-50B; proxy 15 GW −$125-175B.
6. Rigor 5 flag in the text: the envelope rests on T4 margin and training rows and the reported Google value is a T3 [VERIFY] single-outlet figure whose page was not opened; the conclusion is conditional and the S-1 settles it.

### §6 Who holds the risk (new; 700; E11)
1. E11 (A/10_Financing): the ladder from cost-stack-reconciliation §6: T+1pt / 5.75% / 8.5% (SPV), 9.0-9.75% (neocloud notes), Nvidia RVG $105B, Nvidia holding the Lambda lease at Hut 8's Beacon Point (15-yr landlord lease, 704 MW, $19.6B base-term value, ≈ $1.86M per MW-yr powered shell, L-167 T1), AMD credit support, warrants for capacity.
2. The 300-400 bp spread as the price of the guarantee; the accounting cost at the counterparties (SB Energy $2.57B warrant charge, L-147; AMD $4.1B lease guarantees, L-146).
3. "OpenAI is not an investment-grade tenant" (L-061): the landlord's words; 20-year leases as quasi-debt.
4. Huang's "might be the last time" (L-075): the one ledger datapoint on persistence of the subsidy.

### §7 Microsoft and OpenAI (figures refreshed; 500; E12)
1. $24.1B FY2026, $6.0B receivable (L-054, T1); funding commitments $13.0B, $11.9B funded at Jun-30 (L-157, T1: reconciles PitchBook's $1B + $2B + $10B; $1.1B unfunded, within rounding of the $181.2B denominator, so the CE basis stays PitchBook's committed capital); the official Apr-27 terms (L-051, T1); the $38B cap (L-052, T3, single-outlet); percentage not confirmed (10-K silent, L-157; Bloomberg full text states no basis, L-158); stake ~27% / Foundation 26% / investors and employees 47% at the Oct-2025 recap (L-159, T2), post-dilution "decreased" and undisclosed (C-19 addendum).
2. RPO $678B, +25% ex-OpenAI (L-055); the $250B could not be verified (L-121; archive unreachable, L-159 notes). Say the silence: Microsoft, Alphabet, Google and Broadcom file no dollar value for these contracts (L-153, L-154, L-156, L-157).
3. E12 (A/01_Data, A/09_Obligations): the Microsoft anchor table with tiers.
4. The v4 breakeven-shift arithmetic is cut (no row). Say only what the cap does structurally: it bounds a cost line through 2030.

### §8 Capital efficiency (figures refreshed; 500; E13)
1. The reconciliation identity (L-007 + L-014 = L-006; L-022 + L-023 = L-021).
2. E13 (A/05_Cash_Fund): the CE walk Jul-16 → Sep-9 at gross / 39.75% / 27% for Anthropic and net / gross-case for OpenAI; the ratio 1.65x → 1.43x (base) / 1.73x (27%) / 2.37x (raw, forbidden).
3. New money: the Series H included $15B of previously committed hyperscaler money (L-038); AMD's $5B is contingent and not in the denominator (L-043).

### §9 AIBQ (figures refreshed; 600; E14, E15)
1. Lead with the baseline caveat (sub-scores were decomposed, not validated; this is the first rubric run).
2. E14 (A/11_AIBQ): the old → new → row → composite table from aibq-delta §1-§4, flags visible.
3. E15 (A/06_Valuation): the $/AIBQ-point ladder, old and new; the spread 1.60x → 1.48x (1.47x on the facility-closes branch). CE-4 is printed with both branches (7.5 default, facility not closed per L-160; 7.0 if it closes).
4. One sentence on the embargo. One paragraph listing the out-of-scope GO/RQ/MD events for the NEXUS scorer (aibq-delta §6) without scoring them.

### §10 Outside view (new; 700; E16)
1. E16 (A/13_OutsideView): one row per forecast the report makes (Anthropic revenue 2027-2030; OpenAI revenue 2027-2030; both GM paths; both training ramps; both burn paths; both IPO windows; obligation consumption; greenfield capital to milestones) with columns: reference class, base rate, source row or "analyst judgment", what is different here, by how much.
2. Ledger-supported base rates: plan-vs-actual (revenue up, cost up, margin down; L-120/L-032/L-036/L-082/L-065/L-078/L-062/L-083/L-119); milestone slippage (L-001/L-002/L-004/L-040/L-080/L-079); build-cost inflation +21% per MW (L-109); GPU residual values (H100 new $25-40K vs used $8-25K, L-103 T4); hyperscaler useful-life extension 15 → 25 years for DCs while GPUs stay short-lived (L-145).
3. Sourced base rates (new): growth endurance ~70% private / ~80% public (Bessemer, L-161, T3; SaaS dataset, not consumption-billed labs); the capex-heavy platform margin path (AWS operating margin 9.9% in 2014 → 25.4% in 2016 → 27-30% in 2018-2023 → 37.0% / 35.4% in 2024-2025, four Amazon 10-Ks, L-162, T1). Still analyst judgment (say so): IPO-window slippage; no filed-to-priced statistic exists (L-163); the one documented frontier-adjacent case is Cerebras (confidential file → cancel → refile → price ~9 months later) and PitchBook's Q2 colour is a 1.3x median step-up at listing.
4. "What is different here", with the arithmetic (AM-71): the SaaS decay rule applied to Anthropic's FY2026E growth (+476% on PitchBook's FY2025 $10B) gives +333% in 2027 and ~$249B of revenue, above the company's own $190-200B 2028 plan; the plan already embeds faster decay than the base rate, so the bear risk is a regime break, not base-rate decay. Costs also rose faster than any reference class. The AWS path says a capex-heavy platform can reach 25% operating margin in three years and plateau near 30% for six; Anthropic's plan asks for 77% GROSS margin by 2028, a different line and a different basis, and the report must not conflate them.

### §11 Scenarios and sensitivities (figures refreshed; 500; E17)
1. E17 (A/07_Sensitivity), three grids: (a) haircut 27 / 33 / 39.75% × OpenAI basis net / gross → relative multiple and CE ratio; (b) Anthropic 2028 revenue $150 / 175 / 200B × GM 60 / 70 / 77% → compute envelope vs priced commitments and vs the unpriced band; (c) OpenAI 2027-2030 revenue CAGR 40 / 70 / 100% × compute plan $600 / 750 / 900B → 2030 cash flow sign.
2. Bear / Base / Bull definitions stated once (model-spec §4); the 2029-2030 revenue tails use the Bessemer endurance shape (70% Bear and Base; 80% Bull) applied to each scenario's 2028 growth rate, with the arithmetic printed once.

### §12 The greenfield entry fee (new; 1,300; E18)
1. Frame: what the two incumbents' stacks say the price of a seat is, then price a seat from zero.
2. Three scenarios (model-spec §7): lean fast-follower (lease, 25-50k GPU-equivalents, one frontier-class run a year), full frontier (incumbent-scale annual training budgets by year 3, 1,500-3,000 staff), vertically integrated (own 1 GW-IT, custom ASIC program, own power contracts).
3. Line items with their anchors: chips by SKU (L-103, T4 index, ranges), lease vs buy with financing (L-104 T1, L-105 T3, L-106 T1), power (L-107 T3, L-108 T1), cooling and build vs colo (L-109 T2, L-110 T3, L-134, L-136, L-148, L-167 T1: Hut 8 Beacon Point ≈ $1.86M per MW-yr), network (L-111 T3), storage (L-112 CNV, flagged), training runs (L-115 T3, L-125 T4), inference serving (L-116, L-084 T1 list prices), people (L-165 T3 verbatim, supersedes L-092; L-093 T3 with L-166 could-not-verify; L-094 T2), serving throughput (L-164 T2: ~48M output tokens per GPU-hour on an efficient MoE model; 0.5-0.8M on dense 405B), data (L-113 T1, L-114 T4), safety (L-117 CNV, flagged), legal (L-086 T2, L-088 T4), GTM/G&A (L-118 T4).
4. Outputs (E18, B/07_Cash, B/09_Output): cumulative capital to first frontier-class model, to first $1B net revenue, to cash-flow breakeven, per scenario, with ranges. The Writer may now print a serving cost per million output tokens as an estimate, with the throughput, the GPU-hour rate and the utilization in the sentence: ~$0.22 (MoE, on-demand $10.50/GPU-hr, 100% utilization) to $0.05-0.08 (contracted $2.40-4.00); dense frontier-class ~$13-21 on-demand (L-164, L-104, L-105).
5. Reference-class check (B/08_Reference): xAI (accumulated deficit $41.3B; AI segment 2025 revenue $3.2B, operating loss $6.4B; Q2-26 $2.56B revenue, $1.26B loss; L-096, L-047), SSI ($7.0B raised, zero revenue, 40 staff; L-097), Thinking Machines ($2B seed; "a few hundred million" annualized; $40B round in talks; L-098), Reflection ($2.155B; $25B-pre round in progress; L-099), Mistral (€3B Series D; $7.49B raised; ~900 staff; L-100), Periodic ($300M; L-101), Humans& ($480M; L-102), Meta (capex $125-145B; $14.3B for 49% of Scale; packages to $100M/4 yrs; L-095, L-094).
6. Supply constraint: custom-silicon supply booked through 2028 by six incumbents (L-144, T1); an entrant buys merchant GPUs at merchant prices or waits.
7. The greenfield verdict in one sentence per scenario, each fenced by the reference class.

### §13 Weaker, stronger, verdict, falsifiers (argument changed; 800)
Weaker (three): Anthropic's positive adjusted operating income in Q2 at $11.5-11.6B of quarterly revenue, projected at $559M or ~5.1% of revenue on a non-GAAP measure that excludes SBC and whose definition the company has not published (L-034, L-151, L-152): real counter-evidence, and less than "first operating profit" implied; revenue beating every plan at both labs, with Anthropic's quarterly ladder now T2 at every step ($787M → $4,730M → >$11,500M; L-151, L-032, L-065, L-120, L-082); vendor-backstopped financing and custom silicon lowering unit cost (L-044, L-061, L-167, L-050, L-085), with current serving stacks already at ~$0.22 per million output tokens on efficient models (L-164).
Stronger (three): OpenAI's H1 operating loss at 1.74x revenue and widening, with the compute plan revised up twice (L-066, L-062, L-078, L-082); the §5 incompatibility inside Anthropic's own plan; margin plans missed at both labs while revenue plans were beaten (L-083, L-119).
Verdict: the thesis survives as a statement about commitments and margins, not about profits; the mispricing is basis risk plus the Anthropic triad, not a general "too expensive".
Falsifiers (dated): (1) Anthropic's public S-1 commitments note listing the GW deals as consumption-based or optional (kills §5's strongest exit); (2) an Anthropic FY2026 GM at or above 60% on a gross basis, or a GAAP operating profit for Q2 in the S-1 (kills the margin exit and restores the counter-evidence to full strength); (3) OpenAI's Q3 operating loss narrowing QoQ (weakens §4); (4) either lab pricing an IPO above the standing mark with the obligation table in the prospectus (tests §0's "not in the prices").
IPO status as of Sep-9: no public S-1 for either (L-001, L-002); Anthropic reported mid-October (L-040, T3); OpenAI "public company in 2027", possibly sooner (L-068).

### §14 Frozen conflicts, rulings, provenance (new; 400)
Printed register of the nine frozen conflicts with their switches (model-spec §5), including the C-12, C-14 and C-19 addenda; the six rulings; the tier legend; the ten load-bearing figures with as-of dates (argument-map §A); the provenance box (168 rows; confirmed 97, estimated 51, recalled 6, could-not-verify 14; Gate 1 passed twice); the note that the S-1s replace figures 1-6.

---

## Exhibit register

| # | Exhibit | Section | Workbook / tab / range (per model-spec §8) | Source rows |
|---|---|---|---|---|
| E1 | The entry fee at a glance (both companies) | 0 | A / 08_Output / A1:H14 | L-005, L-019, L-007, L-022, L-032, L-065, L-033, L-151, L-152, L-066, L-034, L-155 (reported, flagged), L-001, L-002 |
| E2 | The 5-Layer Cost Stack: definition and seed placement | 1 | A / 00_Assumptions / A40:F60 | cost-stack-reconciliation §1 |
| E3 | Layer × year × company, 2023A-2030E | 1 | A / 03_Costs / A5:K40 (L3-L5) and A / 09_Obligations / A60:K75 (L1-L2 annualized) | cost-stack-reconciliation §2-§3 |
| E4 | Revenue ladders: run-rate, recognized, forward (dated, with basis) | 2 | A / 02_Revenue / A5:K30 | L-139, L-037, L-032, L-033, L-151, L-035, L-036, L-009, L-010, L-063, L-065, L-066, L-024, L-025, L-069 |
| E5 | Gross-to-net restatement at 39.75% and ~27%; OpenAI basis switch | 2 | A / 02_Revenue / A35:H50 and A / 06_Valuation / A5:H20 | L-126, L-127, L-032, L-065, L-005, L-019, L-007, L-022 |
| E6 | Obligation stack, Anthropic: contracted / cash / cancellable / backstop | 3 | A / 09_Obligations / A5:J20 | cost-stack-reconciliation §4a |
| E7 | Obligation stack, OpenAI | 3 | A / 09_Obligations / A25:J40 | cost-stack-reconciliation §4b |
| E8 | Tally reconciliation: the numbers are scopes | 3 | A / 09_Obligations / A45:H58 | L-062, L-078, L-082, L-138, L-155 (Google leg, T3 [VERIFY]), L-153, L-154 (silences) |
| E9 | Training vs inference: annual budgets vs per-run; the $50B split; the Q2 GM cross-check | 4 | A / 03_Costs / A45:K60 and A / 04_PL / A30:H40 | L-125, L-115, L-078, L-083, L-033, L-034, L-151, L-152, L-081 |
| E10 | Anthropic: priced commitments per year vs the COGS + training envelope, with the Google band (reported $40B/yr [VERIFY] or the $/MW-yr proxy) | 5 | A / 09_Obligations / A80:K95 (chart data) | L-036, L-119, L-125, L-072, L-074, L-046, L-135, L-048, L-136, L-137, L-044, L-049, L-043, L-134, L-155, L-153, L-154 |
| E11 | Who holds the risk: financing ladder and backstops | 6 | A / 10_Financing / A5:H25 | L-044, L-045, L-059, L-061, L-106, L-137, L-167, L-146, L-147, L-148, L-145, L-095, L-075 |
| E12 | The Microsoft anchor | 7 | A / 01_Data (Microsoft block) and A / 09_Obligations / A25:J26 | L-054, L-157, L-051, L-052, L-159, L-158, L-055, L-121 |
| E13 | Capital efficiency walk, Jul-16 → Sep-9, equity-only, both bases | 8 | A / 05_Cash_Fund / A40:H55 | L-007, L-022, L-032, L-065, L-126, L-133 |
| E14 | AIBQ CE and CI: old → new → row → composite | 9 | A / 11_AIBQ / A5:L40 | aibq-delta §1-§5 |
| E15 | $/AIBQ-point ladder | 9 | A / 06_Valuation / A25:F32 | L-005, L-019, aibq-delta §5 |
| E16 | Outside view: reference classes and base rates for every forecast | 10 | A / 13_OutsideView / A5:H30 | L-161, L-162, L-163, L-120, L-032, L-036, L-082, L-065, L-078, L-062, L-083, L-119, L-001, L-002, L-004, L-040, L-080, L-079, L-109, L-103, L-145 |
| E17 | Sensitivity grids (three) | 11 | A / 07_Sensitivity / A5:H20, A25:H40, A45:H60 | model-spec §6 |
| E18 | Greenfield: three scenarios, line items, cumulative capital to milestones, reference-class check | 12 | B / 07_Cash / A5:H60, B / 08_Reference / A5:J20, B / 09_Output / A1:H25 | L-103 through L-118, L-134, L-136, L-148, L-167, L-164, L-125, L-084, L-086, L-088, L-093-L-102, L-165, L-166, L-047, L-144 |

Context-only material (permitted, not analysis): prediction-market odds (L-141, T4); the SpaceX Q2 print as a first public frontier-adjacent cost base (L-047, T2).

## Sections dropped from the v4 map and why
- v4 §3 "The free-tier subsidy": its arithmetic has no external source (argument-map AM-31); its surviving datapoints (users L-080, ads L-081, inference L-083) fold into §4.
- v4 §2 "The dual P&L" as a breakeven-year argument: the WSJ Apr-6 figures have no fresh row (AM-32); §4 keeps the training-vs-inference distinction without the years.
- v4 §7 "Microsoft: the revenue-share cap" as a cash-flow-bridge argument: the bridge figures have no row; §7 keeps the T1 anchor and the cap as a bound.
