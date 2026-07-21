# Brick by Brick rewrite. Sections: The Mortar (monetization), The Builders (customers).
# No em-dashes. No news-outlet names. No author references.

BLOCKS = [

# =====================================================================
# 4. THE MORTAR
# =====================================================================
("h1", "The Mortar: How the Money Is Made"),

("h3", "What it is"),
("p", "Databricks sells compute by the unit. The billing atom is the Databricks Unit (DBU), a normalized measure of processing capacity consumed per hour, with a price per DBU that varies by workload type, cloud, region, and tier. Customers either pay on demand or, far more commonly at enterprise scale, sign multi-year committed-use contracts: a prepaid pool of spend, drawn down as consumption occurs, at discounts that deepen with commitment size. Storage is billed by the underlying cloud provider; Databricks monetizes the compute and the software intelligence wrapped around it. There are no seats, no per-user licenses, and, in the traditional sense, no renewals: there is a commitment, a drawdown, and a bigger commitment."),

("table", {
  "title": "The price list, in one view (AWS, US regions, Premium tier; public price lists, retrieved July 2026)",
  "header": ["Workload (SKU)", "Rate per DBU", "What it meters"],
  "rows": [
    ["Jobs Light compute", "~$0.07", "Basic scheduled pipelines"],
    ["Jobs compute", "~$0.15", "Production data engineering and ETL"],
    ["All-purpose compute", "~$0.55", "Interactive analytics and notebooks"],
    ["SQL Serverless", "~$0.70", "Warehouse queries, infrastructure bundled"],
    ["Model serving", "~$0.08", "AI inference endpoints (scales with tokens/requests)"],
  ],
  "align": "LRL",
  "source": "Rates vary by cloud, region, and tier; Europe runs ~20-30% higher. The 10x span between the cheapest and richest SKU is the mix-shift engine: as customers move up the stack from pipelines to interactive AI, revenue per unit of underlying compute rises.",
}),

("h3", "What the analysis says"),
("p", "Three properties of this design do most of the work in the company's economics. First, expansion is mechanical. When a customer's data volume grows, when its analysts run more queries, and now when its AI agents run queries by themselves at machine speed, the meter turns without a salesperson in the room. Net revenue retention above 140% (company, February 9, 2026) is not a sales accomplishment; it is the billing model meeting the secular growth of data and AI workloads. Second, the committed-use structure converts consumption into visibility. Prepaid commitments sit on the balance sheet as deferred revenue and drain predictably; in the companion model, deferred revenue roughly doubles to about $2.0 billion by fiscal 2027 on the modeled path, funding growth with customers' own cash. Third, procurement friction is unusually low because Databricks sells through the cloud marketplaces: a Fortune 500 company can buy Databricks against its existing AWS, Azure, or Google Cloud spending commitment, which turns three trillion-dollar vendors' pre-negotiated budgets into Databricks' sales channel."),

("h3", "What it means now"),
("p", "The current implication is the quality of the revenue, and it shows up in three disclosed numbers read together: growth above 80%, NRR above 140%, and free cash flow positive. Subscription software can show any two of those; showing all three at once is the signature of consumption billing on top of a workload that customers cannot stop growing. It also carries an honest cost: consumption revenue has less downside protection than subscriptions, because customers can throttle usage without breaching a contract, as the industry learned painfully in the 2022-23 optimization cycle. The offset today is that the marginal workload is AI, and no enterprise in 2026 is optimizing its AI usage downward."),

("h3", "What it means next"),
("p", "Forward, the mortar sets the shape of the model. Because expansion is a product property, the arithmetic floor under growth is high: at NRR above 140%, the June 2026 installed base alone would reach roughly $9.7 billion of run-rate by June 2027 before a single new logo signs. Because the meter prices AI workloads in the same unit as everything else, the AI wave arrives as expansion revenue at enterprise-software margins rather than as a new low-margin business line, though the margin pressure from agent-driven query volume is real and is treated at length in The Ledger. And because commitments prepay, growth strengthens rather than strains the balance sheet, which is why the company can be simultaneously hypergrowth and self-funding, the combination that separates it from every frontier lab it is compared against."),

# =====================================================================
# 5. THE BUILDERS
# =====================================================================
("h1", "The Builders: Customers and What They Do"),

("h3", "What it is"),
("p", "The customer base is a pyramid of more than 20,000 organizations (company, February 9, 2026): a broad self-serve and departmental tail, a professional class of more than 800 customers spending over $1 million a year, and an apex of more than 70 customers spending over $10 million a year, with 70% of the Fortune 500 somewhere on the platform (company, July 16, 2026). Consumption economics make the pyramid dynamic by design: today's $200 thousand departmental workload is tomorrow's $2 million platform standard, and the disclosed tiers are snapshots of customers in transit between them."),

("table", {
  "title": "What the customers actually build (company-published case studies)",
  "header": ["Customer", "What they run on Databricks", "Why it matters"],
  "rows": [
    ["Comcast", "Voice-remote intelligence: petabyte-scale telemetry from video and voice applications, processed for instant response and viewer analytics", "Consumer-scale streaming workload; reported ~10x reduction in compute cost after consolidating on the platform"],
    ["Shell", "Predictive operations: more than 3 terabytes of real-time sensor data daily across energy infrastructure", "Industrial IoT at scale; the lakehouse as the operational nervous system, not just analytics"],
    ["Rivian", "Vehicle telemetry and battery/charge prediction models; a cybersecurity lakehouse migrated in under three months", "One customer, three strata: core platform, ML, and the security push, adopted in sequence"],
    ["HSBC", "Customer analytics and personalization across retail banking", "Regulated-industry proof: governance (Unity Catalog) is the purchase criterion, not an afterthought"],
    ["Fortune 500 broadly", "70% penetration (company, Jul 2026); use cases from fraud detection to genomics to supply-chain optimization", "The platform is horizontal; vertical depth comes from the data, which the customer already owns"],
  ],
  "align": "LLL",
  "source": "Company-published case studies and disclosures, retrieved July 2026. Case-study metrics are company-reported.",
}),

("h3", "What the analysis says"),
("p", "Two structural facts stand out from the base. First, concentration is meaningful but healthy: on the cohort arithmetic in the companion model, the roughly 70 largest customers at an average of roughly $30 million each account for about 30% of revenue, and the 800-plus million-dollar class for well over half; yet no single customer is disclosed or reputed to be material alone, and the tail of 20,000 organizations is a pipeline, not a rounding error. Second, the expansion motion is visible in the tiers themselves: the million-dollar class grew from the mid-hundreds to more than 800 in roughly a year (company disclosures), and the Rivian pattern, core platform first, then ML, then security, is the template the newest product layers are designed to repeat. The customer stories also explain the moat better than any architecture diagram: when a bank's regulatory reporting, a carmaker's battery models, and a media company's viewer experience all run on the same governed estate, the platform is no longer a vendor, it is infrastructure."),

("h3", "What it means now, and next"),
("p", "Now: the depth of the paid base is why revenue quality survives scrutiny. Expansion within existing customers alone sustains roughly 40%-plus growth before new business, which is the arithmetic backbone of the near-term forecast. Next: the pyramid's top tier is the leading indicator to watch. The modeled path takes the $10 million-plus class from roughly 70 customers toward 200 by fiscal 2031, at rising average spend, as AI agents move from pilots to production inside exactly these accounts; the disclosed count at the next update (expected around September-October 2026) will say whether that migration is on schedule. The risk symmetric to the opportunity: these are the same accounts where consumption throttling would appear first in a downturn, which is why the tier counts are a better early-warning system than the headline run-rate."),

# =====================================================================
# 6. THE NEIGHBORHOOD
# =====================================================================
("h1", "The Neighborhood: Competition on Three Fronts"),

("p", "Databricks fights on three fronts simultaneously, against different opponents with different weapons, and the state of each front explains a different part of the numbers."),

("h2", "Front one: the warehouse incumbents (winning, measurably)"),
("p", "What it is: the head-to-head against Snowflake and, secondarily, the legacy warehouse estates migrating to the cloud. Analysis: this is the only front with a public scoreboard, and it has flipped. Databricks passed Snowflake in absolute revenue during 2026; the gap ran roughly $0.5 billion in March and roughly $1.6 billion by June (derived from both companies' disclosures), and it is compounding, because Databricks is growing at 80% against Snowflake's guided 31%. The sharpest datapoint is DBSQL doubling to $1.5 billion inside Snowflake's core category, with management attributing the growth to workload migration. The 2024 Tabular acquisition mattered strategically here: by hiring the founders of Apache Iceberg, Snowflake's preferred open format, Databricks ended the format war and removed the last technical excuse not to consolidate on the lakehouse. Current implication: the competitive narrative that framed the two as peers is roughly two years stale; they are now different sizes growing at different speeds. Forward implication: Snowflake remains the price-setter for how public markets value the category, which matters enormously in The Appraisal, but it is no longer the constraint on Databricks' growth."),

("h2", "Front two: the hyperscalers (a stable, watchable truce)"),
("p", "What it is: Amazon, Microsoft, and Google are simultaneously Databricks' infrastructure suppliers, its distribution channel, its largest competitors (Redshift, Fabric, BigQuery), and, since Microsoft's participation in the February 2026 financing close (PitchBook), its investors. Analysis: the bear case writes itself, three trillion-dollar vendors controlling the compute beneath the platform and the marketplaces it sells through. The reason it has not happened is arithmetic: every Databricks workload monetizes hyperscaler compute underneath, so an ecosystem partner that drives consumption across all three clouds is worth more to each of them than a first-party product that only wins on its own cloud. Neutrality is also the one feature none of them can copy: no hyperscaler will ever be the trusted governance layer across its two rivals, and large enterprises are structurally multi-cloud. Current implication: the truce is profitable for everyone and priced into the quality score as its one visible notch (compute independence, 8.0 of 10). Forward implication: this is the front to monitor rather than the front to fear; the tell would be marketplace term changes or egress pricing aimed at cross-cloud platforms, which would show up in the $10 million-plus account win rates before it showed up anywhere else."),

("h2", "Front three: the AI labs (settled by treaty, for now)"),
("p", "What it is: the possibility that foundation-model companies capture the enterprise AI budget directly, making the data platform a commodity beneath them. Analysis: 2025-26 settled this front in Databricks' favor, at least for this cycle, and the evidence is the labs' own signatures: a multi-year OpenAI partnership with frontier models native on the platform, a five-year Anthropic alliance with Claude available across all three clouds through the platform's own interfaces (company announcements, 2025). The labs concluded that enterprises buy AI where their data is governed, not the reverse. Current implication: Databricks collects a distribution position on frontier intelligence without bearing frontier training costs, the inverse of the labs' economics. Forward implication: the treaty holds while no single model wins outright; a decisive frontier-capability breakaway would concentrate bargaining power in one lab and reopen the front. Model plurality is, quietly, a Databricks asset."),

("h3", "The moat, stated once"),
("p", "Across all three fronts the durable defense is the same: it costs an enterprise almost nothing to bring data onto the platform and a great deal to take it away, and the asymmetry deepens with every layer adopted. Open formats keep the front door frictionless; Unity Catalog governance, lineage, compliance attestation, and now agent workflows make the back door progressively more expensive, because leaving means re-certifying everything an auditor ever signed. Competitors can match any feature; none has demonstrated it can dissolve an installed governance layer. That is the moat a buyer of the company is underwriting, and it is why the competitive question in this report is not whether Databricks survives its neighborhood but what its neighborhood is worth."),
]
