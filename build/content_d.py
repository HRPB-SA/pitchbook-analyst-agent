# Sections 15-19: Risks, Management, Recommendation, Appendices.
# No em-dashes anywhere in this file.

BLOCKS = [

# =====================================================================
# SECTION 15 - RISKS AND WHAT WOULD CHANGE OUR MIND
# =====================================================================
("h1", "Risks and What Would Change Our Mind"),

("p", "One line changes the rating: a gross-margin print below 70%. Everything else in this section is sized, dated, and survivable; that one is mechanical. The risks below are ranked by expected impact on the thesis, not by likelihood of headlines."),

("table", {
  "title": "Risk register, ranked",
  "header": ["#", "Risk", "Mechanism and evidence (dated)", "Trigger / watch item"],
  "rows": [
    ["1", "Gross-margin gate break (first order)", "GM 74%, down from >80%, guided lower on agentic compute (T2: Jun 16, 2026). Below 70% breaks the AIBQ efficiency gate, forces re-score out of Elite, and recasts the AI line toward inference resale economics. Each point is ~$69M of annualized gross profit.", "Next disclosure, ~Sep-Oct 2026. Cushion: ~4 points."],
    ["2", "Growth deceleration", "The thesis leans on acceleration at scale (Figure 2). A fall through ~50% while margin compresses converts the story to a peaked one; consumption billing cuts both ways in downturns (usage throttles without contract breach, as the 2022-23 cycle showed industry-wide).", "Sequential run-rate prints; NRR refresh; $10M+ tier count."],
    ["3", "Absorption / IPO-window risk", "~$3.9T of AI listings vs a $44-47B 2025 issuance market (T2: Deloitte/EY). OpenAI and Anthropic reportedly filed (T3: Jun 9, 2026) and go first; a failed mega-listing shuts the window into 2028. Mitigant: FCF means waiting is costless; SpaceX's June 2026 listing (+23%) says the wall is scalable.", "OpenAI/Anthropic pricing and aftermarket; window state H1 2027."],
    ["4", "Hyperscaler absorption", "AWS/Azure/GCP are supplier, channel, and competitor at once (CI 8.0, the cohort-visible notch). Predation via egress pricing, marketplace terms, or first-party bundling attacks the margin and the moat simultaneously. Mitigant: multi-cloud neutrality is structurally uncopyable by any single hyperscaler; Microsoft invested in the Feb 2026 close (PB).", "Cloud marketplace term changes; Fabric/BigQuery win rates in $10M+ accounts."],
    ["5", "Leverage in a downside", "~$9.3B of debt (PB ladder, Jul 2026) is benign against 80% growth and positive FCF; against a broken gate and halved growth it converts disappointment into balance-sheet pressure.", "Covenant disclosures in any S-1; further debt additions."],
    ["6", "Secondary-vs-primary mark confusion", "Headline valuations from thin secondary trading or unclosed rounds (the $165-175B talks; T3, unclosed as of Jul 10) can anchor expectations the fundamentals must then chase. Our do-not-adopt rule exists for this reason.", "Close/repricing/death of the rumored round."],
    ["7", "Key-person and AI-leadership depth", "AI chief Naveen Rao departed Sep 12, 2025 to found a hardware startup, retaining an advisory role, with Databricks investing (T3: Bloomberg). Ten months on, the AI line accelerated from ~$1.0B to $1.7B post-departure, which empirically retires most of the concern; residual watch on Mosaic-lineage retention.", "Senior AI-org attrition; DBRX-successor cadence."],
  ],
  "align": "CLLL",
  "source": "Ranking and sizing are the author's. Items 1 and 2 are thesis-level; 3 through 7 are path-level.",
}),

("p", "What would make us add: a gross-margin print at or above 73% alongside a run-rate at or above $8 billion in the autumn disclosure would confirm the agentic cost curve is being managed and the acceleration is intact, at which point the bear leg of the football field loses most of its probability mass. What would make us exit entirely, beyond the gate: evidence that DBSQL growth is discount-bought rather than switching-driven, or a hyperscaler term change that demonstrates the neutrality moat is rentable after all."),

# =====================================================================
# SECTION 16 - MANAGEMENT AND GOVERNANCE
# =====================================================================
("h1", "Management and Governance"),

("p", "Databricks is that rarity, a founder-led company at $134 billion where the founding team is still intact at the top: CEO Ali Ghodsi and co-founder and executive chairman Ion Stoica (PB, July 2026) lead a bench drawn from the original Berkeley AMPLab group that created Apache Spark. The management quality shows less in the biography than in three observable behaviors. First, disclosure discipline: four dated public financial prints in ten months, each with consistent metric definitions, a cadence indistinguishable from a public company's and the basis of our GO reporting-readiness sub-score of 9.2. Second, capital discipline: holding the $134 billion mark flat across two closes rather than chasing a headline step-up, and financing compute with debt rather than dilution. Third, timing discipline: ruling out a 2026 listing in public, unhedged language (T2: Bloomberg Television, June 4, 2026) while competitors filed, a decision that costs prestige and preserves optionality."),

("p", "Governance readiness (GO 8.9) rests on the crossover-heavy register documented in Section 9 (Fidelity, Insight, J.P. Morgan Growth Equity, Microsoft, and roughly 44 others in the final close alone; 148 active investors in total per PitchBook, July 2026), audit-grade internal reporting implied by the disclosure cadence, and the absence of disclosed exotic control instruments. What an S-1 would still have to answer: stock-compensation load, GAAP operating economics beneath the FCF line, and the precise founder-control structure, none of which are visible from outside and all of which we have flagged rather than assumed."),

("p", "The Naveen Rao departure deserves its proper size, no more. The architect of the AI line left in September 2025 to build AI hardware; Databricks kept him as an advisor and invested in the venture (T3: Bloomberg, September 12, 2025). In the ten months since, the AI products line grew from roughly $1.0 billion to $1.7 billion and the company shipped its broadest agentic product slate to date (June 2026 summit). The empirical verdict is that the AI organization survived its founder-figure's exit; the residual risk is bench depth in a market where every lab is hiring, and we carry it as a watch item, not a discount."),

# =====================================================================
# SECTION 17 - RECOMMENDATION AND POSITIONING
# =====================================================================
("h1", "Recommendation and Positioning"),

("p", "Core Holding. The author's managed book carries Databricks at an 8% core allocation (conflict disclosed on page 2), and this note's analysis supports maintaining that position in full. The rating is AIBQ 8.81, Elite, the cohort's best business at the cohort's lowest quality-adjusted price, with a defined convergence mechanism (the 2027-window listing) and a defined disqualifier (the 70% margin gate)."),

("bullets", [
  "Entry discipline: accumulation is rational at or below the $134B completed mark, and defensible up to ~$150B, the level at which the buyer starts paying today for growth the base case books over the coming year. Do not chase a closed round at $165-175B: at that price the forward return compresses toward the bull-case dependency.",
  "Exit discipline: a GM print below 70% exits the position mechanically alongside the rating; growth through 50% with margin still compressing halves the position. Neither trigger has fired.",
  "Sizing logic: 8% reflects conviction bounded by illiquidity and single-disclosure risk (the September-October print). The margin of safety is the per-point spread: at $15.2B per point against $118B for the nearest lab, the market must be catastrophically wrong about business quality, not merely optimistic about models, for this to be the expensive asset in the cohort.",
  "Horizon: the position is underwritten to the listing plus one lock-up cycle, roughly 2027-28, with the private optionality (FCF, debt capacity) funding indefinite patience if the window shuts.",
]),

("p", "Conviction: high on the business, moderate on the path. The business case survives every stress in this note except the margin gate; the path case (window timing, sequencing behind the labs) is genuinely uncertain and is why the position is 8% and not 15%. We are paid to hold exactly this asymmetry: a franchise priced below its quality with a dated, checkable list of things that would prove us wrong."),

# =====================================================================
# SECTION 18 - APPENDIX A: THE AIBQ FRAMEWORK
# =====================================================================
("h1", "Appendix A: The AIBQ Framework"),

("p", "AIBQ (AI Business Quality) scores durable business quality independent of valuation. Five dimensions, each 0 to 10, weighted and summed, less a contextual risk adjustment (CRA): Composite = 0.20 CE + 0.25 RQ + 0.15 CI + 0.20 GO + 0.20 MD, minus CRA. Revenue Quality carries the largest weight because, in our coverage history, it best predicts which growth stories survive the transition to durable franchise. Twenty-four sub-scores (5 CE, 5 RQ, 4 CI, 5 GO, 5 MD) average simply within each dimension; the full Databricks decomposition is in Section 4."),

("table", {
  "title": "Dimensions, weights, and the question each answers",
  "header": ["Dimension", "Weight", "The question"],
  "rows": [
    ["Capital Efficiency (CE)", "20%", "How much durable revenue does a dollar of equity buy, and does the business self-fund?"],
    ["Revenue Quality (RQ)", "25%", "Is the revenue diversified, retained, expanding mechanically, and honestly attributed?"],
    ["Compute Independence (CI)", "15%", "Who controls the cost curve and capacity the business runs on?"],
    ["Governance Optionality (GO)", "20%", "Can the company access public markets on its own timetable, and would its governance survive the scrutiny?"],
    ["Moat and Defensibility (MD)", "20%", "What does it cost the customer to leave, and is that cost rising?"],
  ],
  "align": "LRL",
  "source": "Desk framework. CRA captures contextual risks not natively held by the dimensions; Databricks carries CRA 0 in the current score.",
}),

("h3", "Stage gates and the efficiency gate"),
("p", "CE is stage-gated S1 through S5 so that seed-stage burn is not scored against late-stage discipline. Databricks is S5 (late stage), where the efficiency gate applies in full and is a hard rule: positive free cash flow AND growth above 40% AND gross margin above 70%, simultaneously. A gross-margin print below 70% breaks the gate and forces a re-score regardless of the other legs. This is the mechanical link between the next earnings print and the rating, dramatized in Figure 5. At 74% and declining, the cushion is roughly four points."),

("h3", "Bands"),
("table", {
  "title": "Band definitions and cohort placement",
  "header": ["Band", "Range", "Cohort members (Jul 2026)"],
  "rows": [
    ["Elite", "8.50 - 10.00", "Databricks (8.81)"],
    ["Strong", "7.00 - 8.49", "Anthropic (8.20)"],
    ["Developing", "4.50 - 6.99", "OpenAI (4.53), xAI (4.49)"],
    ["Distressed", "< 4.50", "SSI (2.30; pre-revenue by design)"],
  ],
  "align": "LLL",
  "source": "Desk framework. Lab scores are dominated by capital-efficiency and revenue-quality deficits, not by research capability, which AIBQ does not score.",
}),

("h3", "The capital-efficiency ruling"),
("p", "CE denominators are equity-only. Debt is excluded because it makes claims on cash flows, not on the equity engine whose efficiency the ratio measures; folding it in would penalize precisely the financing structure (termed debt against a cash-generative base) that late-stage discipline should reward. Debt is instead assessed in CI (as a compute hedge) and in the risk register (as an obligation). Applied to Databricks: $6.9B / $20.2B = 0.34x; the ~$9.3B of debt appears in CI sub-score 4 and risk item 5, at full weight in both."),

("h3", "The per-point expression and the embargo"),
("p", "The relationship between AIBQ scores and market valuations across the cohort is summarized publicly only as dollars of valuation per composite point, presented as a ranked bar (Figure 1). The underlying correlation coefficient is embargoed and is not disclosed, plotted, or derivable from any exhibit in this note; no exhibit pairs scores with valuations in a form that supports reconstruction. Per-point figures are computed on last completed marks (rumored rounds excluded) and on implied-value estimates only where labeled."),

# =====================================================================
# SECTION 19 - APPENDIX B: SOURCES AND TIERING
# =====================================================================
("h1", "Appendix B: Sources and Tiering"),

("p", "Tiering: T1 = audited or regulatory; T2 = company-announced; T3 = media or single-source. Conflicts are frozen and stated, not averaged; the higher tier is adopted. All sources re-verified live on July 10, 2026. The quality-valuation correlation coefficient is embargoed and appears nowhere in this note; the per-point ladder is its only cleared public expression."),

("table", {
  "title": "Load-bearing claims, sourced and dated",
  "header": ["Claim", "Value", "Source, date", "Tier"],
  "rows": [
    ["Revenue run-rate / growth", "$6.9B / >80% YoY", "CNBC from company disclosure, Jun 16, 2026 (Data + AI Summit)", "T2"],
    ["Run-rate ladder", "$4.0B/+50% Sep 25; $4.8B/+55% Dec 25; $5.4B/+65% Feb 9, 26", "Databricks press releases", "T2"],
    ["Gross margin", "74%, prior >80%, guided lower", "Company disclosure via CNBC/MLQ, Jun 16, 2026", "T2"],
    ["Free cash flow", "Positive, TTM and FY2025 (magnitude undisclosed)", "Databricks press release, Feb 9, 2026", "T2"],
    ["NRR / customers", ">140%; >20,000 orgs; >60% F500; 800+ >$1M; 70+ >$10M", "Databricks press release, Feb 9, 2026 (5 months old at publication)", "T2"],
    ["Current mark", "$134B, held flat across closes", "Company (Dec 2025); PB deal 313367-68T, Feb 9, 2026 ($5B equity + $2B debt)", "T2"],
    ["Lifetime capital", "$29.5B total: ~$20.2B equity, ~$9.3B debt, 21-deal record", "PitchBook entity 59199-40, retrieved Jul 10, 2026", "T2"],
    ["Rumored raise", "$165-175B, in talks, UNCLOSED as of Jul 10", "The Information, Jun 9, 2026; Reuters echo; PB note Jul 7, 2026", "T3"],
    ["S-1 status", "None on file; Form D filings only", "SEC EDGAR CIK 1587468, verified Jul 10, 2026", "T1"],
    ["IPO timing", "2026 ruled out ('terrible year'); 2027 earliest", "Ali Ghodsi, Bloomberg Television, Jun 4, 2026", "T2"],
    ["IPO odds", "'No IPO by end-2027' priced at 0.54", "Prediction markets via 24/7 Wall St, Jul 7, 2026", "T3"],
    ["AI products line", "$1.7B run-rate (from $1.4B Feb, ~$1.0B Dec)", "CNBC Jun 16, 2026; company Feb 9, 2026; Tunguz Jun 2026", "T2/T3"],
    ["Databricks SQL", "$1.5B run-rate, doubled YoY", "Bloomberg, Jun 16, 2026", "T2"],
    ["Lakebase pace", "Thousands of customers in 6 months; ~2x DW-product pace at stage", "Databricks press release, Feb 9, 2026", "T2"],
    ["Panther acquisition", "Announced Jun 16, 2026; terms undisclosed; last mark $1.4B (2021); 3rd security deal; clearance pending", "Company release; Benzinga; SiliconANGLE", "T2/T3"],
    ["Naveen Rao departure", "Sep 12, 2025; advisory role; DB investing in his startup", "Bloomberg", "T3"],
    ["Snowflake comp", "Mkt cap ~$91B Jul 7; EV ~$89B (est.); FY27 product guide $5.84B/+31% (May 27, 2026)", "8-K (T1); market data (T2); EV net-cash adj. is an estimate", "T1/T2/est."],
    ["Anthropic mark", "$965B (Series H, $65B); reported run-rate ~$47B", "CNBC, May 28, 2026", "T2"],
    ["OpenAI mark", "$852B after $122B round", "Media reports, late Mar 2026", "T2/T3"],
    ["SpaceX/xAI", "Merger completed Feb 2026; listed late Jun 2026 at $1.77T; ~+23% since; xAI slice est. ~$1.4-1.7T basis", "Media reports Jun-Jul 2026; implied slice is a desk estimate", "T3/est."],
    ["2025 US IPO proceeds", "$47.4B (EY) / ~$44B (Deloitte); ~$45B used", "EY, Deloitte 2025 reviews", "T2"],
    ["Peer CE ratios", "Anthropic ~0.38x; OpenAI ~0.14x; xAI ~0.07x", "Desk estimates from reported raises and run-rates", "est."],
    ["AIBQ scores", "8.81 / 8.20 / 4.53 / 4.49 / 2.30; sub-scores per Section 4", "Desk framework (proprietary; not externally verifiable)", "desk"],
    ["Employees / footprint", "~9,000; HQ SF + 46 offices", "PitchBook, as of Jun 9, 2026", "T2"],
    ["Acquisition count", "~19 to date (MosaicML 2023 pivotal; Neon 2025; Tabular 2024; Panther 2026)", "Aggregated company disclosures and press; count is an estimate", "T3/est."],
  ],
  "align": "LLLC",
  "source": "Retired figures not used anywhere in this note: $33.1B and ~$38B lifetime-capital variants (no clean deal-record basis). PitchBook's $6.9B revenue field is labeled TTM 4Q2026 (window ending Dec 31, 2026) and is treated as a forward projection, not a run-rate source, per the cross-reference rule.",
}),

("p", "End of note. Prepared by Harrison Rolfes, Senior Research Director, July 10, 2026. Confidential: for institutional recipients only; not for redistribution. Not investment advice."),
]
