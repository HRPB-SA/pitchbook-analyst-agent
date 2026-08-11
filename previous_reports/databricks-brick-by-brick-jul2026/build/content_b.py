# Sections 5-9: Business model, Products, AI focus, Financials, Capital structure
# No em-dashes anywhere in this file.

BLOCKS = [

# =====================================================================
# SECTION 5 - BUSINESS MODEL AND THE LAKEHOUSE
# =====================================================================
("h1", "Business Model and the Lakehouse"),

("p", "Databricks sells one architectural idea, executed for thirteen years: the warehouse and the lake should be the same system. Before the lakehouse, enterprises ran two estates, a data warehouse for structured analytics (expensive, governed, SQL) and a data lake for everything else (cheap, ungoverned, ML-friendly), and paid an integration tax to shuttle data between them. The lakehouse collapses the two: open-format storage (Delta Lake) with warehouse-grade governance (Unity Catalog) and native machine-learning lifecycle (MLflow) on top. Founded in 2013 out of the UC Berkeley AMPLab by the creators of Apache Spark, headquartered in San Francisco with 46 additional offices and roughly 9,000 employees (PB, June 2026), the company has ridden that one idea from research project to $6.9 billion of run-rate revenue."),

("p", "The billing model is the underappreciated half of the machine. Databricks charges for consumption, metered in compute units and storage, not for seats or licenses. That single design choice produces most of the revenue quality documented in Section 4. Expansion requires no renewal event: when a customer's data volume grows, or its analysts run more queries, or, increasingly, its AI agents run queries by themselves, revenue expands mechanically. Net revenue retention above 140% (T2: February 9, 2026) is not a sales achievement, it is a property of the product meeting a secular trend in data volume. The same choice cuts the other way, and we do not hide it: consumption revenue has less downturn visibility than subscription revenue, because customers can throttle usage without breaching a contract. In 2022-23 this hurt consumption names across the industry. The offset today is that the marginal workload is AI, and no enterprise is throttling AI in 2026."),

("p", "Land-and-expand is therefore a property of the architecture, not a sales artifact. The land is often a single team's Spark or SQL workload. The expand is gravitational: data lands in Delta Lake, governance attaches in Unity Catalog, downstream teams build on what is already governed, and each new product layer (warehousing, model serving, agents, operational databases) monetizes the same estate again. More than 60% of the Fortune 500 is somewhere on that curve, with the deep end (70+ customers above $10 million a year; T2: February 2026) demonstrating where the rest of the base is headed. The forward implication is the one that matters for valuation: as long as data volumes and AI workloads compound, the installed base is a pre-sold pipeline, which is why we treat Databricks' growth as structurally persistent rather than cyclically fortunate."),

# =====================================================================
# SECTION 6 - PRODUCTS AND SERVICES DEEP DIVE
# =====================================================================
("h1", "Products and Services Deep Dive"),

("p", "The product surface is best read as four strata, each deepening the dependency on the one below. The foundational layer creates the gravity; analytics monetizes it against the warehouse incumbents; the AI layer monetizes it against the model era; and the newest agentic and security surface aims to make the platform the operating substrate for autonomous software. Revenue attribution, where disclosed: AI products roughly $1.7 billion run-rate and Databricks SQL roughly $1.5 billion (both T2: June 16, 2026, CNBC and Bloomberg respectively), implying a residual core platform of roughly $3.7 billion. Figure 3 (Section 7) charts the mix."),

("table", {
  "title": "Product surface, by stratum",
  "header": ["Stratum", "Products", "Function and evidence (dated)"],
  "rows": [
    ["Foundational", "Delta Lake, Unity Catalog, MLflow", "Open-format storage, governance and lineage, ML lifecycle. The gravity layer; not separately monetized, universally attached."],
    ["Analytics", "Databricks SQL", "Warehouse workloads on lakehouse storage; ~$1.5B run-rate, doubled YoY (T2: Bloomberg, Jun 16, 2026). The head-to-head Snowflake layer."],
    ["AI platform", "Model serving, vector search, Mosaic training and inference", "~$1.7B run-rate, largest and fastest line, from ~$1.0B Dec 2025 and $1.4B Feb 2026 (T2/T3)."],
    ["Agentic and operational", "Lakebase, Agent Bricks, Genie / Genie One / Ontology, Lakeflow", "Serverless Postgres for agents (thousands of customers in first six months, revenue growing ~2x the warehousing product's pace at equivalent stage; T2: Feb 9, 2026); production agent tooling; natural-language access."],
    ["Security and real-time", "Lakewatch (agentic SIEM, Mar 2026), Panther (announced Jun 16, 2026, clearance pending), CustomerLake, real-time engine (Reyden), Omnigent", "Security lakehouse build-out via third security acquisition; CDP and streaming surface (T2/T3, product-stage figures largely undisclosed)."],
  ],
  "align": "LLL",
  "source": "Sources as noted per row; strata are the author's organization. Undisclosed lines carry no revenue attribution.",
}),

("p", "Three observations carry analytical weight. First, Databricks SQL doubling to $1.5 billion (T2: Bloomberg, June 16, 2026) means the newest major assault on Snowflake's core is also one of the fastest-growing large product lines in software; Ghodsi attributes the growth partly to workload switching, which, if accurate, is share capture rather than market growth. Second, Lakebase is the one to watch for 2027: built on the Neon acquisition (2025, ~$1 billion reported, T3), it is an operational Postgres designed for agents to create and use databases programmatically, and the company reports it compounding at roughly twice the adoption pace DBSQL managed at the same age (T2: February 9, 2026). If agents become the dominant database customers, Databricks has pre-positioned the product they will provision. Third, the security push (Antimatter, SiftD.ai, then Panther, announced June 16, 2026 with terms undisclosed; Panther last privately marked at $1.4 billion in 2021, which is a reference point and not a purchase price) extends the same play into the SIEM market: security telemetry is the largest data volume in most enterprises, and pulling it into the lakehouse both grows consumption and deepens exit costs. That Anthropic is among Panther's customers (T2: company release) is a small but telling read on where AI-native buyers already sit."),

("p", "The roadmap logic is consistent and, from a moat perspective, slightly ruthless: every new layer is priced in consumption, lands on data already resident, and makes the layer below harder to leave. The forward implication is that product-count expansion functions as retention insurance; even if any single layer loses its head-to-head, the estate stays."),

# =====================================================================
# SECTION 7 - AI FOCUS
# =====================================================================
("h1", "AI Focus: Where the Models End and the Business Begins"),

("p", "Is Databricks an AI company or a data company? The honest answer is that it is a data-and-AI platform whose AI line is genuine incremental revenue on a profitable core, and the distinction matters for how it should be valued. The AI products line, at roughly $1.7 billion annualized, is now the largest single product line and the fastest-growing: roughly $1.0 billion in December 2025, $1.4 billion in February 2026, $1.7 billion in June (T2/T3 ladder; CNBC June 16, Tunguz June 2026). That is about 25% of total revenue, added in barely three years from the MosaicML acquisition, and it is growing faster than the corporate 80%."),

("p", "Positioning in the AI stack is the crux. Databricks does not compete with the frontier labs on model capability, and stopped pretending to after DBRX; the Mosaic lineage now feeds training, fine-tuning, serving, and evaluation infrastructure for whatever model the customer prefers, including the labs' own via API. Against the hyperscalers, Databricks occupies the governed-data layer they cannot easily replicate across each other's clouds: an enterprise running on all three clouds can have one catalog, one lineage graph, one agent platform. The strategic wager of the agentic surface (Agent Bricks for production agents, Genie and Ontology for natural-language access, Lakebase for agent-native storage, Lakewatch and Panther for agent-driven security operations) is that the durable profit pool of the AI era is not the model, it is the substrate where enterprise agents read, write, and are governed. Every credible competitor for that substrate either lacks the data estate (labs), lacks cross-cloud neutrality (hyperscalers), or lacks the AI-native tooling (legacy warehouses)."),

("p", "The cost of the wager is visible in the gross margin, and we treat it as the price of the prize rather than a defect: agents generate far more queries per human decision than humans do ('the agents are generating way more queries'; T2: Ghodsi, June 16, 2026), and serving that load compresses margin from above 80% to 74%, guided lower. The bull case is operating leverage on a much larger revenue base; the bear case is that agentic workloads permanently carry warehouse-era revenue at inference-era margins. The 70% gate (Section 8, Figure 5) is where we adjudicate that argument with data instead of adjectives."),

("fig", "fig03_composition.png",
 "Figure 3. Revenue composition by product line, June 2026 disclosed versus June 2027 desk estimate. Sources: AI line $1.7B (T2: CNBC, Jun 16, 2026); DBSQL $1.5B (T2: Bloomberg, Jun 16, 2026); core is the residual; forward split is a desk estimate."),

# =====================================================================
# SECTION 8 - FINANCIALS
# =====================================================================
("h1", "Financials"),

("h2", "Revenue: the acceleration is the story"),
("p", "Databricks disclosed a $6.9 billion annualized revenue run-rate growing more than 80% year over year on June 16, 2026 (T2: CNBC, from the Data + AI Summit analyst session). The level is remarkable; the second derivative is the thesis. Four consecutive public prints show growth accelerating at scale: $4.0 billion at +50% (September 2025), $4.8 billion at +55% (December 2025), $5.4 billion at +65% (February 9, 2026), $6.9 billion at +80% (June 2026), all company-announced (Figure 4). Software companies at multi-billion scale decelerate; this one added thirty points of growth rate in nine months while nearly doubling its base. The proximate drivers are attributable: the AI line compounding fastest, DBSQL doubling on workload switching, and consumption billing translating customer agent adoption directly into metered revenue."),

("fig", "fig04_acceleration.png",
 "Figure 4. Revenue run-rate and year-over-year growth, September 2025 to June 2026. Sources: company press releases (Sep 2025, Dec 2025, Feb 2026, T2) and CNBC from company disclosure (Jun 16, 2026, T2)."),

("p", "Forward build: we model graceful deceleration, not extrapolation of the acceleration. Base case: roughly $11.5 billion run-rate by mid-2027 (about +67%), roughly $16 billion in 2028, low-to-mid $20 billions by 2030, an unusually visible path given >140% NRR arithmetic alone sustains mid-40s growth before any new logo lands. A note of discipline on sources: PitchBook carries $6.9 billion labeled as TTM for a fiscal window ending December 2026 (PB financials field, retrieved July 10, 2026), which is a forward-window projection, not trailing actuals; we therefore use only the dated company prints above as run-rate evidence, per our cross-reference rule."),

("h2", "Margins: 74%, and the gate at 70"),
("p", "Gross margin is 74%, down from above 80%, and management has guided it lower as agentic compute grows in the mix (T2: June 16, 2026 disclosures). At $6.9 billion of run-rate, each point of gross margin is roughly $69 million of annualized gross profit, so the compression from the low 80s has already surrendered on the order of $400 to 500 million a year; this is a real cost, incurred deliberately, to own the agentic workload. The AIBQ efficiency gate sits at 70%: a print below that level breaks the gate, forces a re-score, and would in our judgment also reprice the private mark, because it would recast the AI line from high-quality software revenue toward pass-through inference resale. The cushion is roughly four points. Watch the September-October 2026 disclosure before anything else in this note (Figure 5). Our base case holds margin in the 71 to 74% band through 2027 as serving efficiency (Mosaic lineage) and pricing actions offset mix; we assign meaningful but minority probability, roughly a third, to a print in the 70-71% range that survives the gate while thinning the cushion to nothing."),

("fig", "fig05_gate_gauge.png",
 "Figure 5. Gross margin versus the 70% efficiency-gate floor. Sources: margin 74%, prior >80%, guided lower (T2: company disclosures via CNBC/MLQ, Jun 16, 2026); gate definition per desk AIBQ framework (Appendix A)."),

("h2", "Free cash flow: the differentiator"),
("p", "Databricks is free-cash-flow positive on both a trailing-twelve-month and a fiscal-2025 basis (T2: company, February 9, 2026; magnitude undisclosed). Against the Frontier Five this is the dividing line: the labs consume capital as a condition of existence, Databricks generates it as a byproduct of operations. The practical consequences compound quietly. The company raises when terms are attractive rather than when the treasury demands it (the flat $134 billion mark across two closes is the visible evidence); it funds compute commitments with debt priced against cash flows rather than equity priced against hope; and it can wait out a shut IPO window indefinitely. We flag the disclosure asymmetry honestly: FCF magnitude, GAAP operating loss, and stock-compensation load are all undisclosed and will only surface in an S-1. Positive FCF with heavy SBC is a weaker fact than it appears; we score what is disclosed and note what is not."),

("h2", "Unit economics and cohorts"),
("table", {
  "title": "Operating metrics (as of February 9, 2026 disclosure, five months old at publication)",
  "header": ["Metric", "Value", "Read"],
  "rows": [
    ["Net revenue retention", ">140%", "Expansion alone sustains ~40%+ growth; consumption billing makes it mechanical"],
    ["Organizations", ">20,000", "Breadth: the base is a distribution, not a whale list"],
    ["Fortune 500 penetration", ">60%", "Enterprise standard status; remaining 40% is pipeline, not TAM ceiling"],
    ["Customers >$1M/yr", ">800", "Up from 'more than 650' in stale mid-2025 coverage (T3); depth of the paid base"],
    ["Customers >$10M/yr", ">70", "The $10M+ tier is where lakehouse consolidation economics show first"],
    ["Gross retention", "Undisclosed", "We assume a mid-90s floor typical of governed data platforms; flagged as assumption"],
  ],
  "align": "LRL",
  "source": "Source: Databricks press release, Feb 9, 2026 (T2), except as noted. Next refresh expected ~Sep-Oct 2026.",
}),
("p", "The cohort math is the quiet engine of the valuation section: with >140% NRR, the June 2026 customer base alone reaches roughly $9.7 billion of run-rate by June 2027 with zero new logos. New business, DBSQL switching, and Lakebase attach are all additive to that floor. This is what 'letting growth do the work' means mechanically in Section 14."),

# =====================================================================
# SECTION 9 - CAPITAL STRUCTURE AND CAPITAL EFFICIENCY
# =====================================================================
("h1", "Capital Structure and Capital Efficiency"),

("p", "Databricks has raised approximately $29.5 billion in its lifetime (PB total-raised, retrieved July 10, 2026: $29,515.7 million across a 21-deal record), decomposing into roughly $20.2 billion of equity and $9.3 billion of debt. The decomposition matters because the AIBQ capital-efficiency ratio is computed on the equity denominator only: CE = $6.9 billion run-rate / $20.2 billion lifetime equity = 0.34x. The ruling is deliberate. Debt raised against a cash-generative business to pre-fund compute is a financing choice, not a claim on the equity engine's efficiency; it belongs in the compute-independence and risk assessments, where we duly count it as both hedge and obligation. Two figures carried in older internal versions ($33.1 billion and roughly $38 billion of total capital) had no clean deal-record basis and are retired; they appear here only so the reader knows why they appear nowhere else."),

("table", {
  "title": "The financing ladder (completed deals; PitchBook deal records, retrieved Jul 10, 2026)",
  "header": ["Date", "Round / instrument", "Size ($M)", "Class"],
  "rows": [
    ["Sep 2013", "Series A", "13.9", "Equity"],
    ["Jun 2014", "Series B", "33.4", "Equity"],
    ["Dec 2016", "Series C (3rd round)", "60.0", "Equity"],
    ["Sep 2018", "Series D", "140.0", "Equity"],
    ["Jan 2019", "Series E", "250.0", "Equity"],
    ["Oct 2019", "Series F", "400.0", "Equity"],
    ["Feb 2021", "Series G", "1,000.0", "Equity"],
    ["Aug 2021", "Series H", "1,600.0", "Equity"],
    ["Nov 2023", "Series I", "684.6", "Equity"],
    ["Dec 2024", "Series J (incl. ~$170M embedded debt)", "10,230.0", "Equity + debt"],
    ["Jan 2025", "Credit facility (JPMorgan-led)", "5,250.0", "Debt"],
    ["Sep 2025", "Series K", "1,000.0", "Equity"],
    ["Dec 2025", "Debt refinancing", "53.7", "Debt"],
    ["Jan 2026", "Debt addition (JPMorgan, Citi enter)", "1,800.0", "Debt"],
    ["Feb 2026", "Series L (two closes; $5,000 equity + $2,000 debt)", "7,000.0", "Equity + debt"],
    ["", "Lifetime total (excl. 5 secondaries)", "~29,516", "~$20.2B equity / ~$9.3B debt"],
  ],
  "align": "LLRL",
  "source": "Source: PitchBook entity 59199-40, 21-deal record incl. 5 secondary transactions not itemized above (T2). Series L: first close >$4B announced Dec 2025 at $134B (company, T2); Feb 9, 2026 close per PB deal 313367-68T, $5B equity led by Insight, J.P. Morgan Growth Equity, Fidelity, with Microsoft and ~44 others, plus $2B loan. Round-count note: the rumored next raise is the 13th equity round; PitchBook's deal count runs higher because debt deals and secondaries are tracked separately.",
}),

("p", "The cross-cohort comparison is the point of the exercise. On desk estimates from reported cumulative raises and run-rates, Anthropic converts equity to revenue at roughly 0.38x, Databricks at 0.34x, OpenAI at roughly 0.14x, xAI at roughly 0.07x (Figure 6). Two members of the cohort compound capital; the rest consume it. And the Databricks figure understates the gap in one respect: it is the only member of the four whose marginal growth requires no new equity at all, because the business self-funds. From here forward, the CE ratio improves automatically as the numerator compounds against a static denominator; on the base-case revenue path the ratio passes 0.55x by mid-2027 without a dollar raised. The labs' ratios, by construction, cannot do that while training costs scale."),

("fig", "fig06_ce_bars.png",
 "Figure 6. Capital efficiency across the Frontier Five: run-rate revenue per dollar of lifetime equity, July 2026. Databricks computed from disclosures (T2/PB); peers are desk estimates from reported raises and run-rates (est.). Debt excluded from denominators by AIBQ ruling."),

("p", "The debt book deserves its own honest paragraph. Roughly $9.3 billion of obligations at a private company is unusual, and it is collateralized, ultimately, against continued hypergrowth. We are comfortable for three reasons: the ladder is termed out and syndicate-broadening (JPMorgan-led 2025, Citi entering January 2026), the borrower is FCF-positive, and the use of proceeds (compute pre-funding, Series L liquidity structuring) substitutes directly for equity that would otherwise have diluted holders at the same moment the mark was being held flat. But the risk assessment in Section 15 carries it at full weight: in a downside where growth halves and margin breaks the gate, leverage converts a disappointment into a hard problem."),
]
