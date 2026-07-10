# Sections 2-4: Disclosure, Executive Summary, AIBQ Rating
# Block DSL consumed by build_docx.py. No em-dashes anywhere in this file.

BLOCKS = [

# =====================================================================
# SECTION 2 - DISCLOSURE AND BASIS OF PREPARATION (page 2)
# =====================================================================
("h1", "Disclosure and Basis of Preparation"),

("box", "CONFLICT OF INTEREST DISCLOSURE",
 "Databricks, Inc. is a position in the author's managed book, held as a core allocation of 8% of portfolio value. The author therefore has a direct economic interest in the conclusions of this note. This is not a footnote consideration: readers should weight every judgment herein with that interest in mind. The position was established prior to the preparation of this note and no transaction in Databricks securities has been made, and none will be made, within five trading days of this note's distribution."),

("p", "This note initiates coverage of Databricks, Inc. for an institutional-investor and venture-capital audience. It is prepared as of July 10, 2026, on a canonical data pack designated v3.4 (compiled July 7 to 9, 2026), with every load-bearing figure re-verified against live primary sources on July 10, 2026. Where a figure could not be independently re-verified, it is labeled as such in the text. Where a company-announced figure and a media figure disagree, both are stated with their dates; we adopt the higher-tier source and do not average."),

("h3", "Figure provenance and tiering"),
("p", "Every material figure carries a dated source assigned to one of three tiers: T1, audited or regulatory (SEC EDGAR, exchange data); T2, company-announced (Databricks press releases, executive statements to named outlets); T3, media or single-source reporting. Databricks is private and publishes no audited financials; even its T2 figures are self-reported and would be restated in an S-1 under GAAP discipline. Estimates are labeled as estimates; figures that may be stale carry as-of dates. Appendix B tables every load-bearing claim with source, date, and tier."),

("h3", "Embargo discipline"),
("p", "The correlation coefficient linking business quality to valuation across our coverage cohort is embargoed and appears nowhere in this document, in text or in chart form. The only cleared public expression of the quality-valuation relationship is the dollar-per-AIBQ-point spread, presented as a ranked bar (Figure 1). No chart plots quality scores against valuations, and none carries a fitted line from which the embargoed statistic could be reconstructed."),

("h3", "Valuation basis"),
("p", "The base-case valuation anchors on the last completed financing mark of $134 billion (Series L, first close announced December 2025, additional close February 9, 2026; T2). The reported financing discussions at $165 to 175 billion (T3: The Information, June 9, 2026) remained unclosed as of July 10, 2026 and are excluded from the base case under our do-not-adopt rule; they are analyzed in Section 10. Capital-efficiency calculations use an equity-only denominator by methodological ruling; debt informs the compute-independence and risk assessments instead (Appendix A). This is research, not investment advice: Databricks securities are unlisted and illiquid, and private-peer figures are negotiated marks, not market prices."),

# =====================================================================
# SECTION 3 - EXECUTIVE SUMMARY AND INVESTMENT THESIS
# =====================================================================
("h1", "Executive Summary and Investment Thesis"),

("p", "The most expensive assets in private technology are the least proven businesses, and the cheapest is the best one. That is the paradox this note is built around. Databricks scores 8.81 on our AI Business Quality framework, the highest composite in the Frontier Five and the cohort's only Elite rating, and at its $134 billion mark it costs $15.2 billion per point of measured quality. Anthropic costs $118 billion per point. OpenAI costs $188 billion. xAI, on our estimate of its implied value inside the newly listed SpaceX, costs roughly $345 billion. The buyer of Databricks pays the least, by an order of magnitude, per unit of the thing an investor is supposed to be buying."),

("p", "This is where the models end and the business begins. The frontier labs are call options on artificial general intelligence, priced accordingly. Databricks is a cash-generative enterprise franchise: $6.9 billion of run-rate revenue growing more than 80% year over year (T2: CNBC, June 16, 2026), gross margin of 74% (T2, same disclosure), free-cash-flow positive on a trailing-twelve-month basis (T2: company, February 9, 2026), and net revenue retention above 140%. It is being priced, per unit of quality, as if it were the least proven asset in the room. The IPO, guided by the CEO to 2027 at the earliest (T2: Bloomberg Television, June 4, 2026), is the event that forces the market to reconcile the two."),

("h3", "The three legs"),
("bullets", [
  "Quality that survives scrutiny. Growth above 80% at $6.9 billion scale is not a small-base artifact; it is the fastest growth of any software company near this size, against CrowdStrike at 26% and Shopify at 34% (T3: Tunguz, June 2026). The growth is accelerating: +50% in September 2025, +55% in December, +65% in February 2026, +80% in June (Figure 4). Margin, cash generation, and retention all clear institutional bars simultaneously, which is precisely what the AIBQ efficiency gate tests.",
  "Growth funded from within. Databricks has raised roughly $20.2 billion of equity in its lifetime and converted it into $6.9 billion of run-rate revenue, a capital efficiency of 0.34x, against roughly 0.14x at OpenAI and 0.07x at xAI (desk estimates). Only Anthropic, at an estimated 0.38x, is comparable. Unlike the labs, Databricks generates cash rather than consuming it: the last raise was taken flat at $134 billion across two closes because the company did not need to reprice itself to fund operations.",
  "The price. At $15.2 billion per AIBQ point, the market charges less for Databricks quality than for any other asset in the cohort (Figure 1). Growth-adjusted against its nearest public comp, the discount repeats: Databricks trades at 0.24x forward revenue multiple per point of growth versus Snowflake at 0.49x (Figure 7). Two independent yardsticks, private and public, say the same thing.",
]),

("h3", "The honest counter"),
("p", "Part of the spread is rational. Some of the labs' premium is genuine option value on AGI outcomes that Databricks does not offer; if frontier models compound into something discontinuous, no data platform participates in that tail. Part of the spread is structural: the labs re-mark upward on every raise because they must raise continuously, while Databricks held its mark flat precisely because it did not need money, so the comparison partly reflects liquidity mechanics rather than mispricing. And category confusion cuts both ways: the market may be paying up for model companies not by error but because it believes platform economics are more contestable than they look. We take these seriously and answer them in Sections 11 and 14. The short version: option value explains a premium, not an 8x-to-23x per-point premium over a business growing 80% with positive free cash flow, and the flat mark is itself evidence of the discipline the labs cannot afford."),

("h3", "Rating and recommendation"),
("p", "AIBQ 8.81, Elite band, down from 8.92 on exactly two drivers: gross-margin compression from above 80% toward the 70% efficiency-gate floor, and removal of a 0.5-point governance imminence premium that was tied to an H2 2026 S-1 no longer expected. The rumored raise is not a rating driver in either direction. Recommendation: Core Holding at an 8% allocation (disclosed conflict, page 2). Base-case value of $155 to 190 billion on a twelve-month view, reached by letting growth do the work against the $134 billion anchor, not by adopting the rumored round."),

("h3", "What would change our mind"),
("bullets", [
  "A gross-margin print below 70% at the next disclosure (expected roughly September to October 2026) breaks the efficiency gate, forces a mechanical re-score, and removes the Elite band. This is the single line that changes the rating.",
  "Growth decelerating through 50% while margin is still compressing would convert the acceleration story into a peak-quarter story and compress the base case toward the bear range of $115 to 130 billion.",
  "An OpenAI or Anthropic listing that prices poorly and closes the IPO window into 2028 extends the private holding period and weakens the convergence mechanism, though it does not impair the business.",
  "Hyperscaler behavior that turns co-opetition into margin capture, for example punitive egress or preferential first-party bundling, would attack the compute-independence dimension where the company is already weakest (CI 8.0).",
]),

("fig", "fig01_per_point.png",
 "Figure 1. Valuation per AIBQ point across the Frontier Five, July 2026. Sources: marks per company announcements and PitchBook (T2); xAI implied value is a desk estimate inside listed SpaceX (T3/est.); AIBQ scores are this desk's framework. SSI (~$30-32B / 2.30) excluded as pre-revenue. The embargoed quality-valuation coefficient is not derivable from this ranked bar."),

# =====================================================================
# SECTION 4 - THE AIBQ RATING: FULL BREAKDOWN
# =====================================================================
("h1", "The AIBQ Rating: Full Breakdown"),

("p", "AIBQ scores durable business quality, deliberately independent of valuation, across five weighted dimensions on a 0-to-10 scale, less a contextual risk adjustment (CRA). Databricks composites to 8.81 with a CRA of zero: the only Elite rating in the Frontier Five, and the highest composite this desk has assigned. The full methodology, band definitions, and the equity-only capital-efficiency ruling are in Appendix A. This section decomposes all 24 sub-scores, because the rating is the analytical spine of the note and the reader is entitled to see every joint in it."),

("table", {
  "title": "AIBQ composite reconciliation",
  "header": ["Dimension", "Weight", "Score", "Contribution"],
  "rows": [
    ["Capital Efficiency (CE)", "20%", "8.9", "1.780"],
    ["Revenue Quality (RQ)", "25%", "9.0", "2.250"],
    ["Compute Independence (CI)", "15%", "8.0", "1.200"],
    ["Governance Optionality (GO)", "20%", "8.9", "1.780"],
    ["Moat and Defensibility (MD)", "20%", "9.0", "1.800"],
    ["Weighted sum", "100%", "", "8.810"],
    ["Contextual Risk Adjustment (CRA)", "", "", "0.000"],
    ["Composite", "", "", "8.81  (Elite)"],
  ],
  "align": "LRRR",
  "source": "Source: desk AIBQ framework, July 2026 re-score. Reconciles exactly: 8.9(.20) + 9.0(.25) + 8.0(.15) + 8.9(.20) + 9.0(.20) = 8.81.",
}),

("h2", "Capital Efficiency: 8.9 (weight 20%)"),
("p", "CE asks one question: how much durable revenue does a dollar of equity buy? Databricks is stage-gated S5 (late stage), where the bar is hardest: at S5 the framework demands the efficiency gate be met in full, meaning positive free cash flow, growth above 40%, and gross margin above 70% simultaneously. Databricks clears all three, with the margin leg now the binding one: 74% against the 70% floor leaves a cushion of roughly four points, worth about $280 million of annualized gross profit at the current run-rate. That cushion, and the company's own guidance that margins will decline further on agentic compute (T2: Ghodsi, June 16, 2026), is why CE is 8.9 and not higher, and why the next quarterly print is the single most important data point in this note."),
("table", {
  "title": "CE sub-scores (5)",
  "header": ["Sub-score", "Score", "Basis (dated)"],
  "rows": [
    ["Revenue per equity dollar", "9.0", "0.34x run-rate per lifetime equity dollar ($6.9B / ~$20.2B), Jul 2026; best-in-cohort save Anthropic"],
    ["FCF status and trajectory", "9.1", "FCF-positive TTM and FY2025 (T2: company, Feb 9, 2026); labs are deeply FCF-negative"],
    ["Cost of incremental growth", "8.5", "Growth accelerating while equity base static since Feb 2026; but agentic COGS rising (T2: Jun 16, 2026)"],
    ["Dilution discipline", "9.0", "Mark held flat at $134B across two closes (Dec 2025, Feb 2026); raised for flexibility, not survival"],
    ["Stage-gate compliance (S5)", "8.9", "Gate met on all three legs; margin leg cushion ~4 pts and guided lower"],
  ],
  "align": "LRL",
  "source": "Simple average 8.9. Denominator is equity-only ($20.2B) by AIBQ ruling; the ~$9.3B of debt is assessed under CI and risk instead.",
}),

("h2", "Revenue Quality: 9.0 (weight 25%)"),
("p", "RQ carries the largest weight in the framework because it is the best predictor of which growth stories become durable franchises. Databricks posts the strongest RQ this desk has scored. The core mechanism is structural: consumption billing on compute and storage means expansion is a property of customer workloads, not of sales-force heroics. When a customer's agents generate more queries, revenue rises without a renewal negotiation. Net revenue retention above 140% (T2: company, February 9, 2026) at a base of more than 20,000 organizations, with more than 800 customers above $1 million a year and more than 70 above $10 million, is a distribution of expansion, not a handful of whales. We flag that these operating metrics are as of February 2026 and are five months old at publication; the September-October disclosure should refresh them."),
("table", {
  "title": "RQ sub-scores (5)",
  "header": ["Sub-score", "Score", "Basis (dated)"],
  "rows": [
    ["Net revenue retention", "9.4", ">140% (T2: Feb 9, 2026); top decile at this scale, mechanical under consumption billing"],
    ["Billing-model quality", "9.2", "Consumption-based on compute and storage; expansion is a product property, not a sales artifact"],
    ["Customer diversification", "8.7", ">20,000 orgs; >60% of Fortune 500; 800+ at $1M+, 70+ at $10M+ (T2: Feb 9, 2026)"],
    ["Scale-adjusted growth durability", "9.3", "+80% at $6.9B, accelerating four consecutive prints (T2: Sep 2025 to Jun 2026)"],
    ["Mix genuineness", "8.4", "AI line ($1.7B) is incremental usage on the same platform, not relabeled core; but agent-driven usage is young (T2: Jun 16, 2026)"],
  ],
  "align": "LRL",
  "source": "Simple average 9.0. Consumption revenue is lower-visibility than subscription in downturns; scored within mix genuineness and durability.",
}),

("h2", "Compute Independence: 8.0 (weight 15%)"),
("p", "CI is the honest notch in the radar (Figure 2) and the dimension a skeptic should attack first. Databricks does not own hyperscale infrastructure; it rides AWS, Azure, and Google Cloud, pays their list economics, and competes with their first-party analytics services while depending on their capacity. Three mitigants keep the score at 8.0 rather than lower. First, multi-cloud is real at Databricks in a way it is not for most vendors: workloads are portable across all three hyperscalers, which converts suppliers into bidders. Second, the debt structure (roughly $9.3 billion across the January 2025 $5.25 billion facility, the January 2026 $1.8 billion addition, and the $2.0 billion Series L tranche) exists substantially to pre-fund compute commitments without burning equity, a deliberate hedge we credit here rather than in CE. Third, the MosaicML lineage gives Databricks genuine training and inference engineering of its own, so its AI unit economics are not purely a pass-through of someone else's GPU pricing. The offset is the new agentic cost curve: agents generating more queries is revenue, but at 74% and falling gross margin it is also the clearest evidence that compute cost is a live constraint."),
("table", {
  "title": "CI sub-scores (4)",
  "header": ["Sub-score", "Score", "Basis (dated)"],
  "rows": [
    ["Infrastructure ownership and leverage", "7.2", "No owned hyperscale capacity; rents from three competitors-suppliers"],
    ["Supplier diversification", "8.8", "True multi-cloud portability across AWS, Azure, GCP converts dependence into a bid process"],
    ["Unit-cost trajectory", "7.4", "GM 74%, down from >80%, guided lower on agentic compute (T2: Jun 16, 2026)"],
    ["Strategic hedges", "8.6", "~$9.3B debt capacity ring-fenced for compute; Mosaic-derived infra IP; stake in Rao hardware venture (T3: Bloomberg, Sep 12, 2025)"],
  ],
  "align": "LRL",
  "source": "Simple average 8.0. The CI-CE boundary is where the debt lives: it does not dilute the CE denominator, but it is scored here as both hedge and obligation.",
}),

("h2", "Governance Optionality: 8.9 (weight 20%)"),
("p", "GO measures whether the company can access public markets on its own timetable, and whether its governance would survive the scrutiny. Databricks scores 8.9, down from an effective 9.4 in the prior score: we have removed the 0.5-point imminence premium that was tied to an H2 2026 S-1, because no S-1 is on file (T1: EDGAR, CIK 1587468, checked July 10, 2026; Form D filings only) and the CEO has ruled 2026 out (T2: Bloomberg Television, June 4, 2026). What remains is still exceptional: audited-grade internal reporting implied by quarterly public run-rate disclosures, a board and investor register (Insight, Fidelity, J.P. Morgan Growth Equity, Microsoft and roughly 44 others in the last close alone; T2/PB, February 9, 2026) that already resembles a public registry, and, critically, the luxury of choosing its window. Waiting is a governance strength when free cash flow means the company never has to file into a bad tape."),
("table", {
  "title": "GO sub-scores (5)",
  "header": ["Sub-score", "Score", "Basis (dated)"],
  "rows": [
    ["Board and investor structure", "8.8", "Crossover-heavy register (Fidelity, Insight, JPM Growth, Microsoft; T2/PB Feb 2026); founder-led with institutional depth"],
    ["Reporting and audit readiness", "9.2", "Quarterly public run-rate cadence since 2025; FCF disclosed on TTM and FY basis (T2)"],
    ["Control and alignment", "8.4", "Founder control tempered by 148 active investors (PB, Jul 2026); no exotic instruments disclosed"],
    ["Disclosure cadence", "9.3", "Four dated public prints in ten months; conflicts rare and explainable"],
    ["Listing optionality", "8.8", "Can list at will; chooses not to; imminence premium (0.5) removed on 2027-earliest guidance (T2: Jun 4, 2026)"],
  ],
  "align": "LRL",
  "source": "Simple average 8.9. Prediction markets price 'no IPO by end-2027' at 0.54 (T3: 24/7 Wall St, Jul 7, 2026); optionality, not imminence, is what we score.",
}),

("h2", "Moat and Defensibility: 9.0 (weight 20%)"),
("p", "MD is where the lakehouse architecture pays its rent. The moat is data gravity: once petabyte-scale data lands in Delta Lake under Unity Catalog governance, with lineage, permissions, and ML lifecycle (MLflow) attached, the cost of moving is not the storage bill, it is re-certifying every downstream pipeline, model, and compliance attestation. The paradox that makes this durable is that Databricks built it on open formats. Delta Lake is open source; in principle a customer can walk. In practice openness removed the adoption objection that kills proprietary platforms, and the switching cost migrated up the stack into governance and workflow, where it is stickier. Each new layer (SQL warehousing, model serving, Lakebase, Agent Bricks) deepens the dependency of the layer below it. Nineteen-odd acquisitions (estimate, aggregated from company disclosures) have been absorbed without a visible integration failure, MosaicML being the proof case: bought for roughly $1.3 billion in 2023 (T3: Bloomberg), it now anchors a $1.7 billion revenue line (T2: June 16, 2026)."),
("table", {
  "title": "MD sub-scores (5)",
  "header": ["Sub-score", "Score", "Basis (dated)"],
  "rows": [
    ["Data gravity and switching costs", "9.5", "Petabyte-scale estates under Unity Catalog governance; migration cost is re-certification, not storage"],
    ["Open-format paradox", "8.9", "Open Delta/Iceberg posture removes adoption friction; lock-in migrates to governance layer"],
    ["Ecosystem breadth", "9.0", ">20,000 orgs, >60% of Fortune 500 (T2: Feb 2026); 46 offices; ~9,000 employees (PB, Jun 2026)"],
    ["Acquisition integration record", "8.8", "~19 deals (est.); MosaicML to $1.7B AI line; Neon to Lakebase; Tabular to format detente"],
    ["Category definition power", "8.8", "Coined and owns 'lakehouse'; competitors now advertise in its vocabulary"],
  ],
  "align": "LRL",
  "source": "Simple average 9.0. Hyperscaler co-opetition is deliberately scored under CI, not MD; the moat question is customer exit cost, not supplier power.",
}),

("h2", "The delta from 8.92, and the band"),
("p", "The prior composite was 8.92. Two drivers, and only two, account for the 0.11-point decline. First, CE moved from 8.95 to 8.9 as the gross-margin band tightened: 74% and guided lower is a different fact pattern from the stable low-80s the prior score rested on. Second, GO moved from 9.4 to 8.9 with the removal of the 0.5 imminence premium tied to an S-1 that is no longer expected in H2 2026. The rumored $165 to 175 billion raise is not a driver of the score in either direction: AIBQ is constructed independent of valuation, and a rumor is not a business fact. Reconciliation: prior 8.95(.20) + 9.0(.25) + 8.0(.15) + 9.4(.20) + 9.0(.20) = 8.92; current 8.9(.20) + 9.0(.25) + 8.0(.15) + 8.9(.20) + 9.0(.20) = 8.81."),
("p", "Band placement: 8.81 sits in the Elite band (8.50 and above). Anthropic at 8.20 is Strong. OpenAI at 4.53 and xAI at 4.49 sit in the Developing band, scores dominated by revenue-quality and capital-efficiency deficits rather than by any doubt about their research. SSI at 2.30 is Distressed on business dimensions for the uncomplicated reason that it is pre-revenue by design. The per-point ladder in Figure 1 prices these scores; the peer radar in Figure 2 shapes them."),

("fig", "fig02_radar.png",
 "Figure 2. AIBQ dimension scores, Databricks versus Frontier Five average, July 2026. Cohort dimension averages are desk estimates consistent with published composites (8.81 / 8.20 / 4.53 / 4.49 / 2.30). Source: desk AIBQ framework."),
]
