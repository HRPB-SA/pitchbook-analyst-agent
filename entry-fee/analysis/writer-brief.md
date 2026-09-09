# Writer Brief: The $100 Billion Entry Fee v5
Agent 2 (Analyst) to Agent 3 (Writer), 2026-09-09. Read with `analysis/outline-v5.md` (structure and exhibits), `analysis/argument-map.md` (what may be claimed and at what tier), `analysis/cost-stack-reconciliation.md` (the shared tables) and `analysis/aibq-delta.md`. Figures below carry: value · ledger row · status (confirmed / estimated / recalled / could-not-verify) · tier · as-of · basis. Rigor dial 5: a figure resting on T3/T4 ships only with the flag in the sentence, not in a footnote. No em-dashes anywhere; hyphens for ranges. $14.2B, 27.1x, +47% YoY. Active voice.

---

## 1. Voice

You are a senior private-markets analyst who has been inside these two companies' numbers for three years and is preparing public-market investors for the moment the information asymmetry disappears at the S-1s. Evidence-heavy, not citation-heavy: one row reference per figure, in-line and short (e.g., "(L-054, Microsoft 10-K)"), never a paragraph of sourcing. Opinionated, not promotional: you have a view on both names and you say it, and you say what would make you wrong. You do not write "I was right" (doctrine note, April 2026): the market moved, Anthropic printed an operating profit, and the contrarian gap that v4 traded on has partly closed. You reframe around what the prices still do not carry (§2 basis risk, §5 the Anthropic triad, §6 who carries the tail) and you name it before the S-1s do.

House rules that bind every sentence: no PitchBook TTM field as a current figure (Ruling 4); no gross Anthropic number beside a net OpenAI number without the equalization stated (Ruling 5); no debt in any CE denominator (Ruling 1); the correlation coefficient does not appear in any form (Ruling 2); Anthropic's FCF stays "unswept" (Ruling 3): an operating profit is not free cash flow and you never write that it is.

## 2. Ten sentences the report must contain (in some form)

1. $124.3B and $181.2B of equity bought two seats at the frontier (L-007, L-022 · estimated, derived from PitchBook deal records · T2).
2. The seats carry $324B (Anthropic, eight counterparties) and $480B (OpenAI, four) of documented compute contracts, plus gigawatts nobody has priced in public (cost-stack §4).
3. Anthropic's $65B run-rate is gross and OpenAI's >$40B has no stated basis; on the internal 39.75% equalization Anthropic trades at 24.6x to OpenAI's 21.3x; on the ~27% the market's critics use, 20.3x: the sign of the relative multiple flips inside the dispute (L-032, L-065, L-126, C-13).
4. Anthropic reported its first quarterly operating profit in Q2-2026 on $11.5-11.6B of revenue; the $559M is a company projection and WSJ confirms only the sign (L-033, L-034 · T2).
5. OpenAI lost $12.3B at the operating line in Q2 on $6.7B of revenue, and the loss widened from $9.3B in Q1 (L-066 · T2).
6. On Anthropic's own 2028 plan, 77% gross margin, $22B of training and $190-200B of revenue leave ~$66-68B a year for compute; its priced contracts already take ~$53B of that in 2028; the contracted 5 GW of Google TPU alone needs $30-50B more, and Broadcom's 2028 line of sight would need $125-175B more (§5; T4 rows flagged).
7. The largest single item in Anthropic's stack, $1.25B a month to SpaceX through May 2029, can be cancelled by either side on 90 days' notice (L-046 · T1).
8. The $1.15T OpenAI obligation figure is 59% unverifiable: Azure $250B, Broadcom $350B and AMD $90B could not be confirmed at T1/T2 (L-121, L-122, L-123).
9. Microsoft booked $24.1B of FY2026 revenue from OpenAI arrangements, the only T1 cash figure in the stack (L-054).
10. Nvidia guarantees $105B of residual value on OpenAI's Ohio leases; the landlord's own filing says OpenAI is not an investment-grade tenant (L-061 · T1).

## 3. Section briefs

### §0 The entry fee, restated (900 words; E1)
- **Point.** The entry fee has three prices and v4 only counted one. Burn to first operating profit (Anthropic: ~$12-20B derived from FY2024 net loss −$5.3B or −$8.3B [L-012, C-05] plus FY2025 burn $5.6B [L-120 · recalled · T4] plus earlier years with no row; wide, T4 inputs; flag as derived), capital raised to reach it ($124.3B), contracts signed to keep the seat ($324B documented-$ plus unpriced GW). The S-1s will make the third price visible for the first time.
- **Numbers.** $124,254M (L-007 · estimated · T2 · 2026-05-28 · equity-only). $181,216.5M (L-022 · estimated · T2 · 2026-03-31 · equity-only). $65,000M (L-032 · confirmed · T2 · end-Jul-2026 · gross run-rate). >$40,000M (L-065 · confirmed · T2 · Jul-2026 · basis unstated).
- **Tension.** Anthropic's Q2 operating profit is a public counterexample to "structurally incompatible with returns". Say so in the second paragraph, not the last.
- **Do not say.** "Obligations exceed burn by an order of magnitude." That compares a spend plan with a burn plan (argument-map AM-25) and is cut.

### §1 The 5-Layer Cost Stack (800; E2, E3)
- **Point.** The definition is printed because the v4 outline could not be located; layers 1-2 are commitments, 3-5 are consumption, and the placement rule stops double counting.
- **Numbers.** Anthropic 2024A COGS $1,940M on $1,000M revenue (L-012 · T2; GM −94% L-119 · recalled · T4). OpenAI 2025A total COGS ≈ $8,777M (revenue $13,100M L-063 · T2 × (1 − 33%) L-083 · estimated · T3). Anthropic 2026E COGS $23-35B (derived; T3/T4 inputs). OpenAI 2026 compute $50,000M (L-078 · confirmed · T2 · sworn).
- **Tension.** Most 2023A-2025A cells are HOLEs; print them as HOLEs. A stack with visible holes is more credible than a filled one, and the S-1s will fill them within weeks.
- **Do not say.** Any Anthropic 2026 compute-spend number as a fact (L-128 could-not-verify). The "$19B" in circulation is a conflation with the April run-rate.

### §2 Revenue on a comparable basis (900; E4, E5)
- **Point.** The Jul-16 "no discount, both at 34.1x" result is not robust: on Sep-9 run-rates the relative multiple flips sign inside the haircut range, so the basis dispute is itself worth ~$190B of relative value (15% premium vs 5% discount on $965B).
- **Numbers.** Anthropic net run-rate $39,162M at 39.75% (L-032 × (1 − L-126 · recalled · T4, Ruling 5)) / $47,450M at ~27% (C-13 external branch, T4). Multiples 24.6x / 20.3x on $965,000M (L-005 · confirmed · T2). OpenAI 21.3x on $852,000M (L-019 · T2) / >$40,000M (L-065; if gross with a 20% share, T4, net $32,000M → 26.6x). Q2 recognized: Anthropic $11,600M gross → $6,989M / $8,468M net; OpenAI $6,700M (L-033, L-066 · T2).
- **Tension.** Q2 recognized says Anthropic is ahead on either basis; July run-rates say near parity on net. Both hold only if OpenAI's >20% July monthly growth (L-065) is real and sustained. Write the sentence that says which print you would bet on and why.
- **Do not say.** "34.1x" as a current multiple, or "Anthropic trades at a discount" without the haircut stated in the same sentence.

### §3 The obligation stack (900; E6, E7, E8)
- **Point.** The tallies are scopes; the documented-$ contracts are the only numbers that survive a filing; cancellability and backstops are attributes, not footnotes.
- **Numbers.** SpaceX $1,250M/month through May-2029, 90-day termination (L-046 · confirmed · T1 · 2026-05-03); contracted at any moment ≈ $3,750M. TPU lease SPV $34,500M, five-year lease, Broadcom-supported $30,000M (L-044 · estimated · T3 · 2026-08-12); this is why PB Total Raised fell from $161,254M to $126,754M (L-006, C-01). August neocloud deals: Riot $9,100M/20 yr/191 MW (L-136 · T2), Volta $10,000M/6 yr/133 MW (L-048 · T3), Nscale ~$45,000M/6 yr/~460 MW (L-135 · T2), Lambda $35,000M/~350 MW (L-137 · T2). OpenAI: Oracle $300,000M/5 yr from 2027 (L-064 · estimated · T2 press; Oracle discloses only RPO $638,000M, L-056 · T1), AWS ~$138,000M (L-064), CoreWeave $6,500M T1 / ~$22,400M press (L-058), Cerebras >$20,000M, 750 MW, plus a $1,000M loan from OpenAI to Cerebras (L-149 · T1).
- **Tension.** Cash paid to date is almost entirely undisclosed (only $24.1B at Microsoft, $50B plan, $1.0B Cerebras loan, ≤$2.56B SpaceX Q2, $1.5B settlement). Print the column with its HOLEs; do not estimate it.
- **Do not say.** "$1.15T across seven vendors" as a figure. Say "the $1.15T tally" and immediately decompose it ($480B documented-$, $690B could-not-verify).

### §4 Training and inference (700; E9)
- **Point.** Annual training budgets and per-run costs are different objects; the sworn $50B does not reconcile to the leaked split; the margin a reader sees depends on the recognition basis.
- **Numbers.** Training plan Anthropic $7,000 / $14,000 / $22,000M 2026-2028; OpenAI $25,000 / $60,000 / $112,000 / $120,000M 2026-2029 (L-125 · recalled · T4, "leaked doc", basis = annual budget). Per run: Grok 4 ~$500M; GPT-4.5 ~$200M pre-training; >$1B by 2027 (L-115 · estimated · T3). $50,000M − $25,000M − $14,100M = $10,900M unexplained (L-078, L-125, L-083). Inference $8,400M (2025) → $14,100M (2026E) (L-083 · T3); ads $1,000M run-rate (L-081 · T2 · 2026-08-31) ≈ 7% of 2026E inference.
- **Tension.** Anthropic's Q2 GM arithmetic: at $3-5B of quarterly opex (analyst judgment), gross-basis GM is 31-48% and net-basis 51-80% (L-034, L-033). Say the opex assumption in the sentence.
- **Do not say.** Any breakeven year ("excluding training 2026, including training 2030"), any FCF trough, any "cap moves breakeven forward a year": no fresh ledger row (AM-32). The only forward cash datapoint is "$39B positive cash flow in 2030" from a Feb-2026 plan (L-082 · T3).

### §5 The margin-commitment incompatibility (900; E10)
- **Point.** Anthropic's own plan contains three numbers that cannot all be true once the priced contracts and the unpriced gigawatts are laid against it. This is the next mispricing: the market prices the 77% margin and the 16 GW of TPU as if both are real.
- **Numbers.** Revenue 2028 $190,000-200,000M (L-036 · estimated · T2 · Reuters exclusive, company forecast to IPO investors). GM 77% 2028E (L-119 · recalled · T4). Training $22,000M 2028E (L-125 · recalled · T4). Envelope $65,700-68,000M (derived). Priced commitments 2028 ≈ $53,400M (derived from L-072, L-074, L-046, L-135, L-048, L-136, L-137, L-044; two term assumptions stated). Unpriced: Google 5 GW contracted (L-073 · T2) and Broadcom's 5 GW 2027 / 10 GW 2028 line of sight (L-049 · confirmed · T1 · 2026-09-02), AMD 2 GW (L-043 · T1); at $9.3M per MW-yr (SPV chips $6.9M from L-044 + shell $2.4M from L-136) or $12.5-16.3M (L-134 · T3), 5-10 GW costs $46-125B/yr.
- **Tension.** Every leg is a plan or a derivation; the conclusion is conditional. Write the three exits (margin lower; training higher; GW deals optional) and say which the commitments note in the S-1 will reveal and what each does to the multiple.
- **Do not say.** "Anthropic's margins are fake" or any verdict. Say "cannot all be true" and stop.

### §6 Who holds the risk (700; E11)
- **Point.** The subsidy is real, it is priced, it has an accounting cost at the counterparties, and it may not persist.
- **Numbers.** SPV tranches T+1pt / 5.75% / 8.5% (L-044 · T3); CoreWeave notes 9.00% / 9.75% / 9.625% (L-059 · confirmed · T1 · 2026-06-30); spread 300-400 bp. Nvidia RVG $105,000M on 4.25 GW-IT, option on 3.78 GW-IT, payable only at ready-for-service (L-061 · T1). Nvidia holds the Lambda lease (L-137 · T2). SB Energy warrant fair-value charge $2,573M H1-2026 (L-147 · T1). AMD DC lease guarantees $4,100M; $9,500M of new leases up to 16 years (L-146 · T1). Huang: the $30,000M "might be the last time" (L-075 · T2 · 2026-03-04).
- **Tension.** The same structures that lower the labs' cost of capacity are the ones a public investor cannot see on the labs' balance sheets. Say what line in an S-1 would show them (commitments and contingencies; related-party; variable-interest entities) and that you expect the disclosure to be thin.
- **Do not say.** That any backstop is an obligation of the lab. The RVG is Nvidia's contingent liability; the SPV debt is the lessor's.

### §7 Microsoft and OpenAI (500; E12)
- **Point.** One T1 number anchors the whole Microsoft relationship; everything else is single-outlet or undisclosed.
- **Numbers.** $24,100M FY2026 revenue from OpenAI arrangements incl. revenue share; A/R $6,000M (L-054 · confirmed · T1 · FY ended 2026-06-30). Revenue share through 2030 at the same percentage subject to a total cap; non-exclusive IP to 2032; any cloud (L-051 · confirmed · T1 · 2026-04-27). Cap $38,000M (L-052 · estimated · T3 · The Information via Reuters, single-outlet). Stake "below 27%" (L-054 T1 direction; L-053 · recalled · T4 level). RPO $678,000M, +25% ex-OpenAI (L-055 · T1).
- **Tension.** "$17.2B paid in FY2025" (L-054 notes · recalled · T4) is a calendar-year figure on a different basis; do not trend it against $24.1B.
- **Do not say.** "20%". The percentage is T4 only.

### §8 Capital efficiency (500; E13)
- **Point.** Equity-only denominators reproduce PitchBook exactly; the equalized advantage narrowed because OpenAI grew faster from a lower base; part of the Series H was old money.
- **Numbers.** $124,254M + $2,500M revolver = $126,754M PB Total Raised (L-007, L-014, L-006). $181,216.5M + $5,220M debt = $186,436.5M (L-022, L-023, L-021). CE: Anthropic 0.315x (39.75%) / 0.382x (27%) / 0.523x gross (forbidden raw); OpenAI 0.221x; ratio 1.43x / 1.73x / 2.37x; Jul-16 was 1.65x (L-133 · recalled · T4). Series H included $15,000M previously committed hyperscaler money incl. $5,000M Amazon (L-038 · confirmed · T1) and Google's $10,000M at a $350B valuation (L-073 · T2).
- **Tension.** CE improved on the data (0.228x → 0.315x) while the AIBQ CE score falls (§9). Pre-empt the confusion here.
- **Do not say.** Any CE figure with debt in the denominator, or the raw 2.37x as a comparison.

### §9 AIBQ (600; E14, E15)
- **Point.** First rubric-based validation of the CE and CI sub-scores; Anthropic's fall is a method correction, OpenAI's rise is T1 evidence; the ladder narrows; tiers do not change.
- **Numbers.** Anthropic CE 8.0 → 7.3 (CE-1 10.0 → 8.0: the prior 10.0 is not reproducible from the rubric without counting a projected operating profit as TTM FCF+); CI 5.05 → 5.55; composite 8.20 → 8.13. OpenAI CE 3.05 → 3.9 (CE-1 3.0 → 5.0 on 0.221x); CI 4.5 → 5.6 (CI-2 3.0 → 6.0 on L-061, L-050, L-149 · T1); composite 4.53 → 4.87. $/AIBQ-point: Anthropic $119B, OpenAI $175B; spread 1.60x → 1.47x.
- **Tension.** The composite moves exceed the rubric's daily caps; they are a re-baseline, logged as such, with the 24-hour cooling period.
- **Do not say.** Any correlation, r-value, or "inverse curve" language. The ladder is the only permitted expression.

### §10 Outside view (700; E16)
- **Point.** Before any forecast, name the reference class and the base rate; in this ledger the base rate is "revenue plans beaten, cost plans raised, margin plans missed, milestones slipped"; where no source exists, say "analyst judgment".
- **Numbers.** Anthropic Jan-2026 plan $18,000M 2026 / $55,000M 2027 / $102,000M 2028 (L-120 · recalled · T4) vs $65,000M run-rate by July (L-032) and $190,000-200,000M 2028 forecast by August (L-036). OpenAI compute plan $600,000M (May, L-078) → $750,000M (Jul, L-062); burn forecast +$111,000M (Feb, L-082). PB projections moved +29% (Anthropic FY27) and +38% (OpenAI FY26) in eight weeks (L-009, L-024). GM: OpenAI 33% vs 46% plan (L-083); Anthropic lowered (L-119). Milestones: no public S-1 by Sep-9 for either (L-001, L-002); ChatGPT 1B users seven months late (L-080 · T2); Abilene 1.2 GW from 2.1 GW (L-079 · T3). Build cost +21% per MW to $17.6M (L-109 · T2).
- **Tension.** "What is different here" cuts both ways: revenue beat plans by 2-4x within months (no software reference class does that) and so did cost. Do not resolve the tension; quantify it.
- **Do not say.** A base rate for hypergrowth growth decay or capex-heavy GM paths as if sourced. Label those "analyst judgment" in the sentence.

### §11 Scenarios and sensitivities (500; E17)
- **Point.** Three inputs move the answer; everything else is noise at this rigor level.
- **Numbers.** Haircut 27 / 33 / 39.75%; Anthropic 2028 GM 60 / 70 / 77% and revenue $150 / 175 / 200B; OpenAI 2027-2030 revenue CAGR 40 / 70 / 100% against a $600 / 750 / 900B compute plan. Bear / Base / Bull as defined in model-spec §4.
- **Tension.** Base case uses 39.75% (Ruling 5) although the external branch is lower; say why (gate-verified on the May-2026 mix; the external figure is adversarial and undocumented) and show both.
- **Do not say.** Point estimates without the grid they came from.

### §12 The greenfield entry fee (1,300; E18)
- **Point.** Price a seat from zero three ways and check each against what real entrants paid.
- **Numbers.** Contracted GPU-hours $2.40-4.00 (L-105 · estimated · T3) vs on-demand B200 $6.69-8.60, GB200 $10.50 per GPU (L-104 · confirmed · T1 · 2026-09-09); GB200 NVL72 rack $2-3M, GB300 $3-4M (L-103 · estimated · T4 index); all-in build $17.6M per MW, +21% since Q4-2024 (L-109 · T2); Texas industrial power 6.58 c/kWh, US 9.17 (L-108 · confirmed · T1 · Jun-2026); powered shell $1.76M (Core Scientific-AMD, L-148 · T1) to $2.4M per MW-yr (Riot, L-136); full-stack $12.5-16.3M per MW-yr (L-134 · T3); network 3-15% of GPU cost (L-111 · T3); storage 2-5% (L-112 · could-not-verify, flagged); frontier run ~$500M, >$1B by 2027 (L-115 · T3); incumbents' annual training budgets $7,000M / $25,000M (L-125 · T4); MTS base $1.12-1.38M (L-092 · T3); Meta packages to $100M over four years (L-094 · T2); retention $1.5M × ~1,000 (L-093 · T3); data licensing ~$50-70M per marquee source (L-113 · T1 Reddit S-1); expert data $1-3B/yr per lab (L-114 · T4); safety $55-115M (L-117 · CNV, flagged); copyright $1,500M paid, >$3,000M demanded (L-086 · T2); Broadcom supply booked through 2028 (L-144 · T1). Owning 1 GW-IT ≈ $36B up front (derived). Reference class: xAI accumulated deficit $41,311M, AI segment 2025 revenue $3,201M / operating loss $6,355M (L-096 · T1), Q2-26 $2,560M / −$1,260M (L-047 · T2); SSI $7,000M raised, zero revenue, 40 staff (L-097 · T2; C-08); Thinking Machines $2,000M seed, "a few hundred million" annualized, $40B-pre round in talks (L-098 · T2); Reflection $2,155M (L-099); Mistral €3,000M Series D, $7,492M raised, ~900 staff (L-100); Periodic $300M (L-101); Humans& $480M (L-102); Meta capex $125-145B, $14.3B for 49% of Scale (L-095 · T2).
- **Tension.** The reference class says $2-8B buys a credible model and almost no revenue; $40B+ of losses buys vertical integration and ~$3B of revenue; and the two incumbents raised $124B and $181B to get to $65B and $40B of run-rate. The greenfield numbers must be consistent with all three, or say why not.
- **Do not say.** A single "entry fee" number. Three scenarios, three milestones, ranges.

### §13 Weaker, stronger, verdict, falsifiers (800)
- **Point.** Answer the thesis honestly in both directions, then fence the verdict with dated falsifiers.
- **Numbers.** Weaker: $559M projected Q2 operating profit, sign confirmed (L-034 · T2); run-rate ladders $9B → $65B (L-139, L-032) and >$20B → >$40B (L-065); SPV at 5.75% (L-044), Fable 5.1 −25-45% cost per task (L-085 · T1 vendor), XPU "half the cost of a GPU" (L-050 · T1 vendor). Stronger: H1-26 operating loss $21,600M on $12,400M revenue, widening (L-066); $600B → $750B (L-078, L-062); the §5 triad; GM plans missed at both (L-083, L-119). IPO status: no public S-1 (L-001, L-002 · T1); Anthropic mid-October reported (L-040 · T3); OpenAI "2027" (L-068 · T2).
- **Tension.** The vendor claims that weaken the thesis (Fable 5.1 cost, XPU cost) are single-source vendor statements; say so in the same sentence you cite them.
- **Do not say.** "The thesis was right." The doctrine note forbids it and the Q2 print disproves it at one level.

### §14 Frozen conflicts, rulings, provenance (400)
- Print the nine frozen conflicts as frozen (§5 below), the six rulings, the tier legend, and the ten load-bearing figures with as-of dates (argument-map §A). One sentence: the S-1s will replace figures 1-6 with audited numbers; this report is the last one written before they do.

## 4. Frozen conflicts to render as frozen (both branches in the text; switch cell named)

| Conflict | Branch A | Branch B | How to render | Switch (Workbook A, 12_Conflicts) |
|---|---|---|---|---|
| C-02 (residual) | OpenAI IPO Q4-2026 "if our business continues to inflect" (L-068) | 2027 (L-068); PB's "September 2026" (L-004) is retired by L-002 and the 15-day rule | "The September window is closed by arithmetic; the live question is Q4-2026 versus 2027" | SW_IPO_OAI |
| C-03 | Anthropic FY2025 recognized $10,000M (PB, L-010) | ~$4,500-6,000M implied by the Jan-2026 guidance (L-120, T4); $9,000M is the exit run-rate (L-139) | "PitchBook's FY2025 field equals the December exit run-rate; recognized revenue is lower and undisclosed" | SW_A_FY25 |
| C-05 | FY2024 net loss −$5,300M (Jul-16 PB) | −$8,300M (PB deal records, L-012) | Print both with vintages | SW_A_FY24_NI |
| C-08 | SSI Apr-2025 round $6,000M, total $7,000M (PB) | $2,000M round, total $8,000M (press) | Reference class only; print both | SW_SSI (Workbook B) |
| C-12 | Anthropic "expects to lose ~$11B in 2026 and 2027" (Jan-2026, L-120 T4) | Q2-2026 first operating profit (L-034 T2); "2026 planned burn ~$3B" (T3 recalled) | "Definitions and vintages differ (GAAP loss incl. SBC and D&A; operating cash burn; operating profit); H2 training load could reconcile them; unresolved" | SW_A_2026_LOSS |
| C-13 | 39.75% equalization (Ruling 5, L-126) | ~27% (OpenAI CRO memo relay, adversarial, T4) | Base case 39.75% with both printed everywhere a net figure appears | SW_HAIRCUT |
| C-15 | Secondary at $925/share → $1.50T implied (T4) | "low-to-mid $800B" (T4) | One sentence: secondary prints disagree; the primary mark is $965B | display-only cell |
| C-16 | OpenAI >$40B is net of the Microsoft share (register convention) | Basis unstated; could be gross (Bloomberg caveat, L-065) | Base case net; gross case shown with a T4 20% haircut flagged | SW_OAI_BASIS |
| C-18 | Anthropic headcount 5,000 (PB, Apr-21, L-008) | ~4,020 (Revelio, Mar, L-091 T4) | Print both; neither company-stated | SW_A_HC |

Resolved and to be stated as resolved: C-01 (the $34.5B is lessor debt; equity-only unaffected), C-04 (PB −$42B is an artifact; neither used), C-06 (PB $20B is run-rate vintage; FY2025 = $13.1B), C-07 (Fast Mode is 2x standard; the "3x cheaper" claim is retired), C-11 (basis label), C-14 (scope table), C-19 ("below 27%"), C-20 (Nvidia LOI superseded), O-15 (Altman title was a PitchBook artifact from an Antimetal Co-CEO biography line; no OpenAI co-CEO structure; L-028, L-070, L-089).

## 5. The red-team bull case the text must answer (write it at full strength before you rebut it)

**The bull case.** (1) Run-rate growth is unprecedented and accelerating: Anthropic $9B → $65B in seven months (L-139, L-032), OpenAI >$20B → >$40B in the same window with July up more than 20% month on month (L-065) and enterprise run-rate up 50% quarter to date (L-069); every internal and third-party revenue plan in the ledger was beaten within months (L-120, L-082, L-009, L-024). (2) The unit economics have turned: Anthropic printed a quarterly operating profit at $11.6B of revenue (L-034), Fable 5.1 cuts cost per task by 25-45% (L-085), custom XPUs cost half a GPU (L-050), cache reads fell 75% (L-084), and Broadcom expects to ship $230B of AI silicon in FY2028 (L-144), so the supply curve is moving toward the labs. (3) The cost of capacity is being financed by vendors at investment-grade-like rates: 5.75% on Broadcom-supported SPV debt (L-044), a $105B Nvidia residual-value guarantee (L-061), Nvidia holding the Lambda lease (L-137), AMD credit support (L-148), warrants instead of cash (L-060, L-149); the labs' true cost of capital is lower than any cost-stack model that charges them 9-10% neocloud rates. (4) The commitments are options, not debts: SpaceX is cancellable on 90 days (L-046), AMD purchases vest by milestone (L-060), AWS is "up to" (L-064), Cerebras's second gigawatt is an option (L-149), Broadcom's gigawatts are "line of sight" (L-049); the obligation stack is a menu, not a bill. (5) On an equalized basis the multiples are ordinary for the growth: 24.6x and 21.3x (or 20.3x) on run-rates growing 100-600% a year, against a public comp set where Reuters says bankers cite Palantir at 53x 2026E revenue (L-036); the S-1s will show audited growth and the marks will look cheap. (6) The reference class of failure is small: no frontier lab with >$1B of revenue has failed; the entrants that raised $2-8B (SSI, Thinking Machines, Reflection, Mistral) are all up-rounding (L-097-L-100), so the "entry fee" is being paid willingly by the most sophisticated capital in the world.

**How the text answers it (one paragraph per point, in §13 or in the relevant section).** (1) Growth is real and the report says so; the base rate in the ledger is also that cost plans rise faster than revenue plans (L-062, L-078, L-082) and margin plans are missed (L-083, L-119). (2) The Q2 profit is one quarter, a projection for the amount, on a gross revenue basis whose margin band is 31-48% at plausible opex (L-034); vendor cost claims are single-source (L-085, L-050). (3) The subsidy is real and priced; it is also finite (Huang, L-075) and it lives on the vendors' books (L-147, L-146), which is exactly why it is not in the labs' prices today and why the S-1 will not show it. (4) Optionality cuts both ways: an option the lab does not exercise is capacity it does not have, and the growth case in (1) needs the capacity; the report's §5 asks which of margin, training or take-or-pay gives. (5) Equalized multiples depend on a haircut that is itself disputed by ~13 points (C-13); the report does not claim the marks are expensive, it claims the basis risk is unpriced. (6) The reference class also contains xAI ($41.3B of accumulated deficit for $3.2B of revenue, L-096) and the two incumbents themselves ($124B and $181B of equity for $65B and $40B of run-rate); up-rounds are prices, not returns.

## 6. Provenance box (print once, in §14)

Tiers: T1 primary/audited · T2 reputable/official/PitchBook fields · T3 single-outlet scoop or analyst estimate · T4 aggregator/secondary/internal prior · T5 rumor. Status: confirmed / estimated / recalled / could-not-verify. Decay: VOLATILE / QUARTERLY / STABLE / PERMANENT. Ledger: 149 rows, Gate 1 passed 2026-09-09 (confirmed 86, estimated 47, recalled 6, could-not-verify 10). Tool flags this run: NEXUS/Notion not available (prior extracts used as T4 only); Bigdata.com not exposed; Aiera not connected; cnbc.com, forbes.com, axios.com, theinformation.com, blogs.microsoft.com blocked to the fetcher (syndications and PitchBook news chunks used).
