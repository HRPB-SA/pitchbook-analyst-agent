# Section 1: The AIBQ Breakdown (standalone). Self-contained: framework,
# composite, all 24 sub-scores, bands, gate, delta, cohort placement.
# No em-dashes. No news-outlet names. No author references.

BLOCKS = [

("h1", "The AIBQ Breakdown: Business Quality, Scored and Decomposed"),

("p", "Before the story, the score. This section is deliberately standalone: it lays out the AI Business Quality (AIBQ) framework, decomposes every one of the 24 sub-scores behind Databricks' 8.81 composite, explains what moved since the prior score, and places the company in its cohort. A reader who stops at the end of this section will know exactly what is being claimed about business quality and exactly which published number would falsify it. The rest of the report then supplies the evidence underneath each score, layer by layer."),

("h2", "The framework in one page"),
("p", "AIBQ scores durable business quality, deliberately independent of valuation, across five weighted dimensions on a 0-to-10 scale, summed to a composite less a contextual risk adjustment (CRA): Composite = 0.20 CE + 0.25 RQ + 0.15 CI + 0.20 GO + 0.20 MD, minus CRA. Revenue Quality carries the largest weight because, across our coverage history, it best predicts which growth stories survive the transition to durable franchise. Each dimension is built from named sub-scores (five for CE, RQ, GO, and MD; four for CI; 24 in total) that average simply within their dimension."),

("table", {
  "title": "Dimensions, weights, and the question each answers",
  "header": ["Dimension", "Weight", "The question"],
  "rows": [
    ["Capital Efficiency (CE)", "20%", "How much durable revenue does a dollar of equity buy, and does the business self-fund?"],
    ["Revenue Quality (RQ)", "25%", "Is the revenue diversified, retained, expanding mechanically, and honestly attributed?"],
    ["Compute Independence (CI)", "15%", "Who controls the cost curve and the capacity the business runs on?"],
    ["Governance Optionality (GO)", "20%", "Can the company access public markets on its own timetable, and would its governance survive the scrutiny?"],
    ["Moat and Defensibility (MD)", "20%", "What does it cost the customer to leave, and is that cost rising?"],
  ],
  "align": "LRL",
  "source": "CRA captures contextual risks not natively held by the dimensions; Databricks carries CRA 0 in the current score.",
}),

("p", "Three structural rules matter for reading what follows. First, the stage gate: CE is stage-gated S1 through S5 so seed-stage burn is not scored against late-stage discipline; Databricks is S5, where the bar is hardest. At S5 the efficiency gate applies in full and is a hard rule: positive free cash flow AND growth above 40% AND gross margin above 70%, simultaneously. A gross-margin print below 70% breaks the gate and forces a re-score regardless of the other legs; at 74% and guided lower, the cushion is roughly four points (the gauge in The Ledger, Figure 7, dramatizes this). Second, the equity-only ruling: CE denominators exclude debt, because termed debt against a cash-generative base is a financing choice, not a claim on the equity engine's efficiency; the roughly $9.3 billion of debt is instead scored inside Compute Independence as both hedge and obligation, and carried at full weight in the risk register. Third, the embargo: the correlation between AIBQ scores and market valuations across the cohort is embargoed; no exhibit in this report pairs scores with valuations in reconstructable form, and the dollar-per-point spread (Figure 2, next section) is the only cleared expression of the relationship."),

("table", {
  "title": "Composite reconciliation: 8.81, Elite",
  "header": ["Dimension", "Weight", "Score", "Contribution"],
  "rows": [
    ["Capital Efficiency", "20%", "8.9", "1.780"],
    ["Revenue Quality", "25%", "9.0", "2.250"],
    ["Compute Independence", "15%", "8.0", "1.200"],
    ["Governance Optionality", "20%", "8.9", "1.780"],
    ["Moat and Defensibility", "20%", "9.0", "1.800"],
    ["Weighted sum", "100%", "", "8.810"],
    ["Contextual Risk Adjustment", "", "", "0.000"],
    ["Composite", "", "", "8.81  (Elite)"],
  ],
  "align": "LRRR",
  "source": "July 2026 re-score. Reconciles exactly: 8.9(.20) + 9.0(.25) + 8.0(.15) + 8.9(.20) + 9.0(.20) = 8.81.",
}),

("h2", "Capital Efficiency: 8.9 (weight 20%)"),
("p", "CE asks one question: how much durable revenue does a dollar of equity buy? Databricks converts roughly $20.2 billion of lifetime equity (PitchBook 21-deal record, July 2026) into $6.9 billion of run-rate revenue, 0.34x, the best in the cohort save Anthropic, and it is the only cohort member whose marginal growth requires no new equity at all because the business self-funds. The gate is met on all three legs, with the margin leg binding: 74% against the 70% floor, guided lower on agent-driven compute (company disclosure, June 16, 2026). That cushion, roughly four points, is why CE is 8.9 rather than higher, and why the next quarterly print is the single most important data point in this report."),
("table", {
  "title": "CE sub-scores (5)",
  "header": ["Sub-score", "Score", "Basis (dated)"],
  "rows": [
    ["Revenue per equity dollar", "9.0", "0.34x run-rate per lifetime equity dollar ($6.9B / ~$20.2B), Jul 2026; best-in-cohort save Anthropic"],
    ["FCF status and trajectory", "9.1", "FCF positive on TTM and FY2025 bases (company, Feb 9, 2026); the frontier labs are deeply FCF-negative"],
    ["Cost of incremental growth", "8.5", "Growth accelerating while the equity base is static since Feb 2026; agent-driven cost of revenue rising (company, Jun 16, 2026)"],
    ["Dilution discipline", "9.0", "Mark held flat at $134B across two closes (Dec 2025, Feb 2026); raised for flexibility and liquidity, not survival"],
    ["Stage-gate compliance (S5)", "8.9", "Gate met on all three legs; margin cushion ~4 points and guided lower"],
  ],
  "align": "LRL",
  "source": "Simple average 8.9. Denominator is equity-only by AIBQ ruling; the ~$9.3B of debt is assessed under CI and in the risk register.",
}),

("h2", "Revenue Quality: 9.0 (weight 25%)"),
("p", "RQ carries the framework's largest weight, and Databricks posts the strongest RQ this framework has scored. The core mechanism is structural rather than commercial: consumption billing on compute and storage means expansion is a property of customer workloads, not of sales-force heroics. Net revenue retention above 140% at a base of more than 20,000 organizations, with more than 800 customers above $1 million a year and more than 70 above $10 million (company, February 9, 2026), is a distribution of expansion, not a handful of whales. One honest flag: those operating metrics are five months old at publication; the September-October disclosure should refresh them."),
("table", {
  "title": "RQ sub-scores (5)",
  "header": ["Sub-score", "Score", "Basis (dated)"],
  "rows": [
    ["Net revenue retention", "9.4", ">140% (company, Feb 9, 2026); top decile at this scale, and mechanical under consumption billing"],
    ["Billing-model quality", "9.2", "Consumption-based on compute and storage; expansion is a product property, not a sales artifact"],
    ["Customer diversification", "8.7", ">20,000 organizations; >60% of the Fortune 500; 800+ at $1M+, 70+ at $10M+ (company, Feb 9, 2026)"],
    ["Scale-adjusted growth durability", "9.3", "+80% at $6.9B, accelerating across four consecutive prints (company, Sep 2025 to Jun 2026)"],
    ["Mix genuineness", "8.4", "AI line ($1.7B) is incremental usage on the same platform, not relabeled core; agent-driven usage is young (Jun 16, 2026)"],
  ],
  "align": "LRL",
  "source": "Simple average 9.0. Consumption revenue is lower-visibility than subscription in downturns; that risk is scored inside mix genuineness and durability.",
}),

("h2", "Compute Independence: 8.0 (weight 15%)"),
("p", "CI is the honest notch in the radar (Figure 1) and the dimension a skeptic should attack first. Databricks owns no hyperscale infrastructure: it rides AWS, Azure, and Google Cloud, pays their economics, and competes with their first-party analytics while depending on their capacity. Three mitigants hold the score at 8.0. First, multi-cloud portability is real at Databricks in a way it is not for most vendors, which converts three suppliers into bidders. Second, the debt structure exists substantially to pre-fund compute commitments without burning equity, a deliberate hedge credited here rather than in CE. Third, the MosaicML lineage gives the company genuine training and serving engineering of its own, so AI unit economics are not purely a pass-through of someone else's GPU pricing. The offset is visible in the P&L: agents generating queries at machine speed is revenue, but at 74% and falling gross margin it is also proof that compute cost is a live constraint."),
("table", {
  "title": "CI sub-scores (4)",
  "header": ["Sub-score", "Score", "Basis (dated)"],
  "rows": [
    ["Infrastructure ownership and leverage", "7.2", "No owned hyperscale capacity; rents from three competitor-suppliers"],
    ["Supplier diversification", "8.8", "True workload portability across AWS, Azure, and GCP turns dependence into a bid process"],
    ["Unit-cost trajectory", "7.4", "Gross margin 74%, down from >80%, guided lower on agentic compute (company, Jun 16, 2026)"],
    ["Strategic hedges", "8.6", "~$9.3B debt capacity ring-fenced for compute (PitchBook, Jan 2025 to Feb 2026); Mosaic-derived serving efficiency; stake in the departed AI chief's hardware venture (Sep 2025)"],
  ],
  "align": "LRL",
  "source": "Simple average 8.0. The CI-CE boundary is where the debt lives: it does not dilute the CE denominator, but it is scored here as both hedge and obligation.",
}),

("h2", "Governance Optionality: 8.9 (weight 20%)"),
("p", "GO measures whether the company can access public markets on its own timetable, and whether its governance would survive the scrutiny when it does. Databricks scores 8.9, down from an effective 9.4: the 0.5-point imminence premium tied to a second-half-2026 filing has been removed, because no S-1 is on file (SEC EDGAR, CIK 1587468, verified July 10, 2026; Form D filings only) and the chief executive has publicly ruled 2026 out. What remains is still exceptional: a public-company disclosure cadence while private (four dated financial prints in ten months with consistent metric definitions), a crossover-heavy investor register that already resembles a public one, and, critically, the luxury of choosing the window. Waiting is a governance strength when free cash flow means the company never has to file into a bad market."),
("table", {
  "title": "GO sub-scores (5)",
  "header": ["Sub-score", "Score", "Basis (dated)"],
  "rows": [
    ["Board and investor structure", "8.8", "Crossover-heavy register: Fidelity, Insight, J.P. Morgan Growth Equity, Microsoft and ~44 others in the final close alone; 148 active investors (PitchBook, Jul 2026)"],
    ["Reporting and audit readiness", "9.2", "Quarterly public run-rate cadence since 2025; FCF disclosed on TTM and fiscal-year bases"],
    ["Control and alignment", "8.4", "Founder-led with institutional depth; no exotic control instruments disclosed"],
    ["Disclosure cadence", "9.3", "Four dated public prints in ten months; definitional conflicts rare and explainable"],
    ["Listing optionality", "8.8", "Can list at will and chooses not to; imminence premium (0.5) removed on 2027-earliest guidance (company, Jun 4, 2026)"],
  ],
  "align": "LRL",
  "source": "Simple average 8.9. Prediction markets price no listing by end-2027 as a slight favorite (Jul 7, 2026); the framework scores optionality, not imminence.",
}),

("h2", "Moat and Defensibility: 9.0 (weight 20%)"),
("p", "MD is where the lakehouse architecture pays its rent. The moat is data gravity: once petabyte-scale estates sit in Delta Lake under Unity Catalog governance, with lineage, permissions, and audit history attached, the cost of leaving is not the storage bill, it is re-certifying every downstream pipeline, model, and compliance attestation. The paradox that makes it durable is that Databricks built the moat on open formats: openness removed the adoption objection that kills proprietary platforms, while the switching cost migrated up the stack into governance and workflow, where it is stickier. Hyperscaler co-opetition is deliberately scored under CI, not here; the moat question is customer exit cost, not supplier power."),
("table", {
  "title": "MD sub-scores (5)",
  "header": ["Sub-score", "Score", "Basis (dated)"],
  "rows": [
    ["Data gravity and switching costs", "9.5", "Petabyte-scale estates under Unity Catalog governance; migration cost is re-certification, not storage"],
    ["Open-format paradox", "8.9", "Open Delta/Iceberg posture (Tabular, 2024) removes adoption friction; lock-in migrates to the governance layer"],
    ["Ecosystem breadth", "9.0", ">20,000 organizations; >60% of the Fortune 500 (company, Feb 2026); ~9,000 employees across 47 offices (PitchBook, Jun 2026)"],
    ["Acquisition integration record", "8.8", "~19 deals absorbed without visible failure; MosaicML (2023, ~$1.3B) now anchors the $1.7B AI line; Neon became Lakebase"],
    ["Category definition power", "8.8", "Coined and owns 'lakehouse'; competitors now advertise in its vocabulary"],
  ],
  "align": "LRL",
  "source": "Simple average 9.0.",
}),

("fig", "radar.png",
 "Figure 1. AIBQ dimension scores, Databricks against the Frontier Five average, July 2026. Cohort dimension averages are estimates consistent with published composites. The compute-independence notch is the one visible weakness; the other four dimensions score near the top of the scale."),

("h2", "The delta from 8.92, the band, and the cohort"),
("p", "The prior composite was 8.92. Two drivers, and only two, account for the 0.11-point decline. First, CE moved from 8.95 to 8.9 as the gross-margin band tightened: 74% and guided lower is a different fact pattern from the stable low-80s the prior score rested on. Second, GO moved from 9.4 to 8.9 with the removal of the 0.5 imminence premium tied to a 2026 filing that is no longer expected. The reported $165 to 175 billion financing talks moved nothing in either direction: AIBQ is constructed independent of valuation, and a rumor is not a business fact. Reconciliation: prior 8.95(.20) + 9.0(.25) + 8.0(.15) + 9.4(.20) + 9.0(.20) = 8.92; current 8.9(.20) + 9.0(.25) + 8.0(.15) + 8.9(.20) + 9.0(.20) = 8.81."),

("table", {
  "title": "Bands and cohort placement (July 2026)",
  "header": ["Band", "Range", "Cohort members"],
  "rows": [
    ["Elite", "8.50 - 10.00", "Databricks (8.81)"],
    ["Strong", "7.00 - 8.49", "Anthropic (8.20)"],
    ["Developing", "4.50 - 6.99", "OpenAI (4.53), xAI (4.49)"],
    ["Distressed", "< 4.50", "SSI (2.30; pre-revenue by design)"],
  ],
  "align": "LLL",
  "source": "Lab scores are dominated by capital-efficiency and revenue-quality deficits, not by research capability, which AIBQ deliberately does not score.",
}),

("h3", "What the score means, now and next"),
("p", "Now: 8.81 says the business clears every institutional quality bar simultaneously, growth, margin, cash generation, retention, governance readiness, and moat, with exactly one visible structural weakness (compute dependence) and exactly one binding constraint (the margin gate's four-point cushion). Next: the score is falsifiable on a schedule. A gross-margin print below 70% at the roughly quarterly disclosure breaks the gate mechanically and removes the Elite band; a print at or above 73% alongside a run-rate at or above $8 billion would instead confirm the agentic cost curve is being managed and would likely restore part of the CE decline. No other single number moves the composite as much, which is why the margin print, not the next valuation headline, is the event to watch. How the market prices each point of this score, and why Databricks' points are the cheapest in the cohort, is where the next section begins."),
]
