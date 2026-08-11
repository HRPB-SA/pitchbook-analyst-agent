# Section 1: The AIBQ Breakdown (standalone, dimension-level only).
# Five dimensions; no sub-score decomposition. MD = Moat Durability.
# No em-dashes. No news-outlet names. No author references.

BLOCKS = [

("h1", "The AIBQ Breakdown: Business Quality, Scored and Decomposed"),

("p", "Before the story, the score. This section is deliberately standalone: it lays out the AI Business Quality (AIBQ) framework, works through each of the five dimensions behind Databricks' 8.81 composite, explains what moved since the prior score, and places the company in its cohort. A reader who stops at the end of this section will know exactly what is being claimed about business quality and exactly which published number would falsify it. The rest of the report then supplies the evidence underneath each dimension, layer by layer."),

("h2", "The framework in one page"),
("p", "AIBQ scores durable business quality, deliberately independent of valuation, across five weighted dimensions on a 0-to-10 scale, summed to a composite less a contextual risk adjustment (CRA): Composite = 0.20 CE + 0.25 RQ + 0.15 CI + 0.20 GO + 0.20 MD, minus CRA. Revenue Quality carries the largest weight because, across our coverage history, it best predicts which growth stories survive the transition to durable franchise. Each dimension aggregates a set of internal sub-scores that average within it; this report presents and defends the dimension level."),

("table", {
  "title": "Dimensions, weights, and the question each answers",
  "header": ["Dimension", "Weight", "The question"],
  "rows": [
    ["Capital Efficiency (CE)", "20%", "How much durable revenue does a dollar of equity buy, and does the business self-fund?"],
    ["Revenue Quality (RQ)", "25%", "Is the revenue diversified, retained, expanding mechanically, and honestly attributed?"],
    ["Compute Independence (CI)", "15%", "Who controls the cost curve and the capacity the business runs on?"],
    ["Governance Optionality (GO)", "20%", "Can the company access public markets on its own timetable, and would its governance survive the scrutiny?"],
    ["Moat Durability (MD)", "20%", "What does it cost the customer to leave, and is that cost rising?"],
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
    ["Moat Durability", "20%", "9.0", "1.800"],
    ["Weighted sum", "100%", "", "8.810"],
    ["Contextual Risk Adjustment", "", "", "0.000"],
    ["Composite", "", "", "8.81  (Elite)"],
  ],
  "align": "LRRR",
  "source": "July 2026 re-score. Reconciles exactly: 8.9(.20) + 9.0(.25) + 8.0(.15) + 8.9(.20) + 9.0(.20) = 8.81.",
}),

("h2", "Capital Efficiency: 8.9 (weight 20%)"),
("p", "CE asks one question: how much durable revenue does a dollar of equity buy? Databricks converts roughly $20.2 billion of lifetime equity (PitchBook 21-deal record, July 2026) into $6.9 billion of run-rate revenue, 0.34x, the best in the cohort save Anthropic, and it is the only cohort member whose marginal growth requires no new equity at all because the business self-funds: free cash flow is positive on trailing-twelve-month and fiscal-2025 bases (company, February 9, 2026), and the equity base has been static since February 2026 while growth accelerated. The discipline shows in behavior as much as in ratios. The $134 billion mark was held flat across two closes rather than chased upward, and the last several raises funded employee liquidity and flexibility rather than operations; a company that raises because it wants to, not because it must, is exhibiting the capital character this dimension exists to measure. What keeps the score at 8.9 rather than higher is the gate: all three legs are met, but the margin leg is binding at 74% against the 70% floor, guided lower on agent-driven compute (company disclosure, June 16, 2026). That roughly four-point cushion is why the next quarterly print is the single most important data point in this report."),

("h2", "Revenue Quality: 9.0 (weight 25%)"),
("p", "RQ carries the framework's largest weight, and Databricks posts the strongest RQ this framework has scored. The core mechanism is structural rather than commercial: consumption billing on compute and storage means expansion is a property of customer workloads, not of sales-force heroics, and net revenue retention above 140% is therefore mechanical rather than heroic. The base beneath that retention is a distribution, not a dependency: more than 20,000 organizations, over 60% of the Fortune 500, more than 800 customers above $1 million a year and more than 70 above $10 million (company, February 9, 2026). Growth is not merely fast but accelerating across four consecutive dated prints, +50% to +80% between September 2025 and June 2026, at a scale where software companies normally decelerate. And the mix is honestly attributed: the $1.7 billion AI line is incremental usage metered on the same platform, not relabeled core revenue. Two honest flags keep the score at 9.0 rather than higher: consumption revenue carries less downturn visibility than subscriptions, because usage can throttle without a contract breach, and the operating metrics above are five months old at publication; the September-October disclosure should refresh them."),

("h2", "Compute Independence: 8.0 (weight 15%)"),
("p", "CI is the honest notch in the radar (Figure 1) and the dimension a skeptic should attack first. Databricks owns no hyperscale infrastructure: it rides AWS, Azure, and Google Cloud, pays their economics, and competes with their first-party analytics while depending on their capacity. Three mitigants hold the score at 8.0 rather than lower. First, multi-cloud portability is real at Databricks in a way it is not for most vendors; when workloads can move across three clouds, three suppliers become three bidders. Second, the roughly $9.3 billion debt structure assembled between January 2025 and February 2026 (PitchBook deal records) exists substantially to pre-fund compute commitments without burning equity, a deliberate hedge credited here rather than in CE, and carried simultaneously as an obligation in the risk register. Third, the MosaicML lineage gives the company genuine training and serving engineering of its own, so AI unit economics are not purely a pass-through of someone else's GPU pricing. The offset is visible in the P&L and is why this dimension cannot score a 9: agents generating queries at machine speed is revenue, but at 74% and falling gross margin it is also proof that compute cost is a live constraint on the business."),

("h2", "Governance Optionality: 8.9 (weight 20%)"),
("p", "GO measures whether the company can access public markets on its own timetable, and whether its governance would survive the scrutiny when it does. Databricks scores 8.9, down from an effective 9.4: the 0.5-point imminence premium tied to a second-half-2026 filing has been removed, because no S-1 is on file (SEC EDGAR, CIK 1587468, verified July 10, 2026; Form D filings only) and the chief executive has publicly ruled 2026 out, with 2027 the earliest window (company, June 4, 2026). What remains is still exceptional. The company keeps a public-company disclosure cadence while private: four dated financial prints in ten months with consistent metric definitions, free cash flow disclosed on trailing and fiscal bases. The investor register already resembles a public one: Fidelity, Insight, J.P. Morgan Growth Equity, Microsoft and roughly 44 others in the final close alone, 148 active investors in total (PitchBook, July 2026), with no exotic control instruments disclosed. And critically, the company owns the luxury of choosing its window: waiting is a governance strength, not a weakness, when positive free cash flow means it never has to file into a bad market. The framework scores that optionality, not imminence."),

("h2", "Moat Durability: 9.0 (weight 20%)"),
("p", "MD is where the lakehouse architecture pays its rent, and the question is strictly the customer's: what does it cost to leave, and is that cost rising? The moat is data gravity. Once petabyte-scale estates sit in Delta Lake under Unity Catalog governance, with lineage, permissions, and audit history attached, the cost of leaving is not the storage bill, it is re-certifying every downstream pipeline, model, and compliance attestation an auditor ever signed. The paradox that makes the moat durable is that it was built on open formats: openness removed the adoption objection that kills proprietary platforms (reinforced by the 2024 Tabular acquisition, which brought the rival Iceberg format's founders in-house), while the switching cost quietly migrated up the stack into governance and workflow, where it is stickier than any file format. The moat also widens on its own evidence: more than 20,000 organizations and over 60% of the Fortune 500 sit on the platform, roughly nineteen acquisitions have been absorbed without visible integration failure, and the company named its category, so thoroughly that competitors now advertise in its vocabulary. Every new layer adopted, warehouse, AI, agents, security, raises the exit cost again, which is precisely the rising-cost trajectory a 9.0 requires. Hyperscaler co-opetition is deliberately scored under CI, not here; the moat question is customer exit cost, not supplier power."),

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
