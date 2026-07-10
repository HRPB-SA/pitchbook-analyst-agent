# Brick by Brick rewrite. Sections: The Appraisal (valuation), The Stress Test, The Verdict.
# No em-dashes. No news-outlet names. No author references. No appendices.

BLOCKS = [

# =====================================================================
# 8. THE APPRAISAL
# =====================================================================
("h1", "The Appraisal: What the Business Is Worth"),

("p", "Valuation here proceeds in three passes, from quality to comparables to scenarios, and one rule binds all three: the base case anchors on the completed $134 billion mark (February 9, 2026) and lets the disclosed growth do the work. The reported $165 to 175 billion round remained unclosed as of July 10, 2026 and appears only as a reference line."),

("h2", "First pass: quality, measured"),
("p", "Our AI Business Quality (AIBQ) framework scores durable business quality independent of valuation: five dimensions on a 0-to-10 scale, weighted and summed, less any contextual risk adjustment. Revenue Quality carries the heaviest weight because, across our coverage, it best predicts which growth stories become durable franchises. One hard rule matters most here: at late stage, the framework's efficiency gate requires positive free cash flow, growth above 40%, and gross margin above 70% simultaneously; a print below 70% breaks the gate and forces a re-score regardless of everything else. Bands: Elite (8.50+), Strong (7.00-8.49), Developing (4.50-6.99), Distressed (below 4.50)."),

("table", {
  "title": "AIBQ scorecard: Databricks 8.81, Elite (the cohort's only Elite rating)",
  "header": ["Dimension", "Weight", "Score", "The one-line case"],
  "rows": [
    ["Capital Efficiency", "20%", "8.9", "0.34x run-rate per lifetime equity dollar; FCF positive; mark held flat by choice. Gate cushion ~4 margin points is what keeps this below 9"],
    ["Revenue Quality", "25%", "9.0", ">140% NRR, mechanical under consumption billing; 20,000+ orgs; four accelerating prints; AI line is genuine incremental usage"],
    ["Compute Independence", "15%", "8.0", "The honest notch: rents compute from three competitors. Mitigants: true multi-cloud portability, ~$9.3B debt ring-fenced for compute, Mosaic-derived serving efficiency"],
    ["Governance Optionality", "20%", "8.9", "Public-company disclosure cadence while private; crossover register; can list at will and chooses not to (2026 ruled out; no S-1 on file)"],
    ["Moat & Defensibility", "20%", "9.0", "Data gravity under Unity Catalog governance; open formats removed adoption friction while switching cost migrated up the stack; ~19 acquisitions absorbed cleanly"],
    ["Composite (less CRA of 0)", "100%", "8.81", "= 8.9(.20) + 9.0(.25) + 8.0(.15) + 8.9(.20) + 9.0(.20). Down from 8.92 on exactly two drivers: margin-band tightening and removal of a 0.5 listing-imminence premium; the unclosed round moved nothing"],
  ],
  "align": "LRRL",
  "source": "AIBQ framework, July 2026 re-score. Cohort composites: Anthropic 8.20 (Strong); OpenAI 4.53 and xAI 4.49 (Developing); SSI 2.30 (Distressed, pre-revenue by design). Lab scores reflect capital-efficiency and revenue-quality deficits, not research capability, which the framework does not score.",
}),

("fig", "radar.png",
 "Figure 8. AIBQ dimension scores, Databricks against the Frontier Five average (cohort dimension averages are estimates consistent with published composites). The compute-independence notch is the honest weakness; everything else scores near the top of the scale."),

("p", "Priced against that quality, the paradox from the Executive Summary sharpens: $15.2 billion per AIBQ point for the cohort's only Elite business, against $118 billion (Anthropic), $188 billion (OpenAI), and roughly $345 billion estimated (xAI). Part of the spread is rational, and the honest version of the counterargument deserves stating: the labs carry genuine option value on artificial general intelligence that no data platform participates in, and their marks re-rate upward mechanically because they must raise continuously while Databricks held its mark flat precisely because it needed nothing. But option value explains a premium, not an 8-to-23-fold premium per unit of quality over a business growing 80% with positive free cash flow. The residual is category confusion, and category confusion is exactly what a public listing prices out."),

("h2", "Second pass: comparables, growth-adjusted"),
("p", "The only clean public comparable is Snowflake: enterprise value roughly $89 billion (market capitalization ~$91 billion on July 7, 2026, less estimated net cash) against a raised FY2027 product-revenue guide of $5.84 billion, implying 31% growth (regulatory filing, May 27, 2026) at roughly 15.3x forward product revenue. Databricks at $134 billion on $6.9 billion is 19.4x, a higher sticker. But a buyer is buying growth, not a multiple, and per point of growth the ranking inverts: 0.24x per growth point for Databricks against 0.49x for Snowflake (Figure 9). Growth-adjusted, the private company trades at roughly half the price of its own best public comp, while outgrowing it nearly threefold and having already passed it in absolute revenue. Two fair objections and their answers: Snowflake's guide is audited and Databricks' prints are self-reported, which earns a haircut but not a halving, four dated disclosures in ten months constrain the exaggeration hypothesis; and growth-adjusted multiples flatter fast growers only while growth persists, which is why the durability case built across The Mortar and The Builders, not this arithmetic, is the report's load-bearing wall."),

("fig", "growth_adjusted.png",
 "Figure 9. Growth-adjusted multiples: Databricks (19.4x forward run-rate, +80%) versus Snowflake (15.3x forward product revenue, +31% guide). Iso-value rays mark equal price per point of growth; no fitted line is shown or implied."),

("h2", "Third pass: scenarios, anchored and gated"),
("table", {
  "title": "Twelve-month scenario architecture (anchored on $134B; the unclosed round is not an input)",
  "header": ["Scenario", "Operating path (workbook switch)", "Multiple", "Value", "What has to be true"],
  "rows": [
    ["Bear", "Growth halves toward 40-50%; margin breaks the 70% gate (Worst path: 69.5% FY28E)", "11-12.5x on ~$10.4B", "$115-130B", "Agentic margin drag proves structural; consumption throttling returns; quality re-scored out of Elite"],
    ["Base", "~$11.5B run-rate by mid-2027 (+65-70%); margin holds 72.5-74%", "14-16x", "$155-190B", "Graceful deceleration; gate holds; listing window opens 2027"],
    ["Bull", "~$12.5B+; margin stabilizes; DBSQL and Lakebase compound; listing re-anchors the category", "16.5-19x", "$205-240B+", "Acceleration proves durable; scarcity premium on the cleanest asset in the AI listing wave"],
  ],
  "align": "LLLLL",
  "source": "Estimates, July 10, 2026. Reference lines: $134B completed mark (Feb 9, 2026); $165-175B reported range (unclosed, press reports of Jun 9, 2026). Base multiple is a deliberate de-rate from today's 19.4x toward public hypergrowth-platform pricing.",
}),

("fig", "football_field.png",
 "Figure 10. Scenario ranges on a twelve-month view. The base case reaches the reported range on fundamentals alone, which reframes the rumor as a fair forward mark rather than an inflated current one, and is precisely why it must not be adopted as a present anchor: doing so would double-count the year of growth that justifies it."),

("p", "The sensitivity grid (Figure 11) exposes the machinery: value is forward run-rate times multiple, nothing else. Read it honestly in both directions. At $9.5 billion and 12x, the bear corner sits about 15% below the current mark; that is the real drawdown if margin breaks and growth halves together. At today's 19.4x on the base-case run-rate the grid reads roughly $223 billion, and the base case deliberately does not underwrite today's private multiple surviving a public order book. The margin of safety is not the multiple; it is quality bought at the cohort's lowest per-point price, with a mechanical gate that tells you when the thesis is wrong."),

("fig", "sensitivity.png",
 "Figure 11. Implied valuation across mid-2027 run-rate and multiple; base intersection highlighted. The same grid is live in the companion workbook's Valuation sheet."),

# =====================================================================
# 9. THE STRESS TEST
# =====================================================================
("h1", "The Stress Test: What Would Change the Answer"),

("p", "One line changes the rating mechanically: a gross-margin print below 70%. Everything else on this list is sized and survivable. Risks ranked by expected impact on the thesis, not by headline likelihood."),

("table", {
  "title": "Risk register",
  "header": ["#", "Risk", "Mechanism", "Watch item"],
  "rows": [
    ["1", "Margin gate break", "GM 74% and guided lower on agent compute (company, Jun 16, 2026). Below 70%, the efficiency gate breaks, the Elite rating re-scores, and the AI line reads as compute resale. Each point is ~$69M of annualized gross profit", "The ~Sep-Oct 2026 disclosure; cushion ~4 points"],
    ["2", "Growth deceleration", "The thesis leans on acceleration at scale. A fall through ~50% while margin compresses turns the story peaked; consumption billing cuts both ways when customers optimize, as 2022-23 showed industry-wide", "Sequential run-rate prints; NRR refresh; $10M+ tier count"],
    ["3", "Listing-window sequencing", "OpenAI and Anthropic reportedly filed first and will price first; a failed mega-listing shuts the window into 2028. Mitigant: FCF makes waiting costless, and the SpaceX listing (up ~23% since June) says the wall is scalable", "Lab IPO pricing and aftermarket, H1 2027"],
    ["4", "Hyperscaler squeeze", "Supplier, channel, competitor, and now investor at once; predation via egress pricing, marketplace terms, or bundling attacks margin and moat together. Mitigant: neutrality across three clouds is structurally uncopyable by any one of them", "Marketplace term changes; first-party warehouse win rates in $10M+ accounts"],
    ["5", "Leverage in a downside", "~$9.3B of debt is benign against 80% growth and positive FCF; against a broken gate and halved growth it turns disappointment into balance-sheet pressure", "Any new debt; covenant detail in an eventual S-1"],
    ["6", "Mark confusion", "Unclosed rounds and thin secondary trading can anchor expectations the fundamentals then have to chase; this report's do-not-adopt rule exists for that reason", "Close, repricing, or death of the $165-175B talks"],
    ["7", "AI leadership depth", "The AI line's founding leader departed September 2025 to a hardware venture (advisory role retained; company invested). Since then the AI line grew from ~$1.0B to $1.7B, which empirically retires most of the concern", "Senior AI-organization attrition; agent-product cadence"],
  ],
  "align": "CLLL",
  "source": "Ranking and sizing are judgments; items 1 and 2 are thesis-level, the rest are path-level.",
}),

("p", "What would strengthen the case: a margin print at or above 73% alongside a run-rate at or above $8 billion this autumn would confirm the agentic cost curve is being managed while the acceleration holds, and would retire most of the bear scenario's probability. What would end it, beyond the gate: evidence that DBSQL growth is bought with discounts rather than won on workload migration, or a hyperscaler term change proving the neutrality moat is rentable after all."),

# =====================================================================
# 10. THE VERDICT
# =====================================================================
("h1", "The Verdict"),

("p", "Brick by brick, the building holds. The foundation (an architecture that turned a universal enterprise tax into a platform), the bricks (five product layers, two already at billion-dollar scale, two more running the same proven play), the mortar (a billing model that converts customers' own growth into revenue and their prepayments into balance-sheet strength), the builders (a 20,000-organization pyramid whose top seventy accounts fund the platform's next act), and a blueprint (buy the next layer early, sign the labs as tenants, borrow for compute, never raise on need) together describe the most complete business in private technology."),

("p", "The appraisal says the market has not paid for that completeness. At $134 billion, Databricks costs $15.2 billion per point of measured quality against $118 to 345 billion for the labs it is filed next to; growth-adjusted, it costs half its own public comparable. The base case reaches $155 to 190 billion within twelve months on nothing more heroic than graceful deceleration and a de-rated multiple, and the reported next round, unclosed and unadopted here, happens to sit inside that corridor, which says sophisticated buyers are converging on the same arithmetic. The one number that breaks the case is published roughly quarterly and currently reads 74 against a floor of 70. Watch the autumn print, watch the $10 million tier count, and treat the eventual listing not as the risk but as the mechanism: the event that forces the market to underwrite the business brick by brick, the way this report just did."),

("p", "This report is for informational purposes only and is not investment advice. Databricks securities are unlisted and illiquid; private-market figures are negotiated marks, not market prices; all non-disclosed financial figures herein are estimates and are labeled as such. Quality-valuation correlation statistics are embargoed; the per-point spread is their only expression here. Prepared July 10, 2026."),
]
