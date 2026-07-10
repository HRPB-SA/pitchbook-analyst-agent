# Sections 10-14: The raise, Competitive position, Market implications,
# IPO convergence, Valuation and scenarios. No em-dashes anywhere.

BLOCKS = [

# =====================================================================
# SECTION 10 - THE UPCOMING RAISE
# =====================================================================
("h1", "The Upcoming Raise: Analyzed, Not Adopted"),

("p", "What is reported: Databricks has discussed raising a round that would value it between $165 and 175 billion, first reported by The Information on June 9, 2026, echoed by Reuters the same day (T3). Follow-on reporting indicated the round could formally kick off within a month of that report, with terms still being finalized and even the treatment of new capital in the headline valuation unsettled (T3: Benzinga, Economic Times syndication, June 9). As of this note's July 10 verification, PitchBook carries the deal as Rumor/Speculation with an estimated $170 billion post-money (PB financing note dated July 7, 2026), and no close has been reported by any outlet. Status: in talks, unclosed. Under our do-not-adopt rule it contributes nothing to the base-case mark, which remains $134 billion."),

("h3", "The step-up math, and what the round is for"),
("p", "The rumored range implies a 23 to 31% step-up over the February 2026 mark, five to seven months later. If it closes, it would perform the three classic functions of a late pre-IPO round: set a reference mark for eventual listing conversations, provide employee and early-investor liquidity after thirteen years of private tenure (the deal record already shows five secondary transactions; PB, July 2026), and let crossover institutions build position before a prospectus exists. Note the distinction the coverage often blurs: a completed primary round at $170 billion would be a negotiated institutional mark; secondary-market chatter in the meantime is a sentiment reading from a thin market, and we weight it accordingly, which is to say barely."),

("h3", "The observation that reframes the rumor"),
("p", "Here is the analytically important part, and the reason this section exists rather than a disclaimer sentence. Our fundamentals-driven base case (Section 14) reaches $155 to 190 billion on a twelve-month view with no reference whatsoever to the rumor: it is simply the February anchor plus a year of disclosed-trajectory growth at a de-rated multiple. The rumored range sits inside that corridor. Read properly, then, $165 to 175 billion is not an inflated current mark, it is a fair forward mark: the price at which new money would be buying roughly the business we expect to exist in mid-2027, at roughly today's quality-adjusted discount. That is also precisely why it must not be adopted as a current anchor: adopting it would double-count the year of growth that justifies it. The discipline and the analysis point the same direction. If the round closes at or above the range, the correct update is to our conviction in the demand curve for the eventual listing, not to our estimate of present value; if it closes below, or dies, that is a genuinely bearish data point about crossover appetite and we would revisit the multiple, not the business quality."),

# =====================================================================
# SECTION 11 - COMPETITIVE POSITION AND THE MOAT
# =====================================================================
("h1", "Competitive Position and the Moat"),

("h2", "Snowflake: the comparison, done properly"),
("p", "The Snowflake comparison is usually done lazily (two logos, one 'data war' headline) and the lazy version misses the finding. Done properly: Snowflake carries an enterprise value of roughly $89 billion (market capitalization ~$91 billion on July 7, 2026, less estimated net cash) against forward product-revenue guidance of $5.84 billion for FY2027, raised on May 27, 2026 from $5.66 billion, implying 31% growth (T1: 8-K; Q1 actuals ran ~30-34%). That is roughly 15.3x forward product revenue. Databricks at $134 billion against $6.9 billion is 19.4x, a higher headline multiple. But the buyer is not buying a multiple, the buyer is buying growth, and per point of growth purchased the ranking inverts: Databricks costs 0.24x per growth point, Snowflake 0.49x (Figure 3). Growth-adjusted, Databricks is roughly half the price of its own best public comparable. Meanwhile the operational scoreboard has already flipped: Databricks passed Snowflake in revenue during 2026, and the gap, roughly $490 million in March, was roughly $1.6 billion by June (T3: Tunguz, June 2026), with Databricks' warehousing product, Snowflake's home turf, doubling year over year to $1.5 billion (T2: Bloomberg, June 16, 2026)."),

("fig", "fig03_growth_adjusted.png",
 "Figure 3. Growth-adjusted multiples: Databricks (19.4x / +80%) versus Snowflake (15.3x / +31% FY27 guide). Sources: Databricks per company disclosures (T2, Jun 16, 2026) and Feb 2026 mark; Snowflake per 8-K of May 27, 2026 (T1) and market data of Jul 7, 2026. Iso-value rays indicate equal price per growth point; no fitted line is shown."),

("p", "Two fair rebuttals, answered. First, Snowflake's 31% is public-market audited guidance and Databricks' 80% is self-reported; some haircut is warranted, though four independent dated prints in ten months constrain how large a haircut is plausible. Second, growth-adjusted multiples flatter the faster grower only while growth persists; that is true, and it is why the durability analysis of Sections 5 and 8 (consumption mechanics, >140% NRR, cohort floor) is the load-bearing wall of the whole note, not the multiple arithmetic."),

("h2", "The hyperscalers: co-opetition priced into the score"),
("p", "AWS, Azure, and Google Cloud are simultaneously Databricks' distribution channels, suppliers, and competitors, and this triple role is the single largest structural risk to the franchise, which is why compute independence scores 8.0 while everything else scores near 9. The bear mechanics are obvious: each hyperscaler sells first-party analytics (Redshift, Fabric/Synapse, BigQuery), controls the marketplace rails Databricks sells through, and prices the compute beneath it. The mitigants are equally concrete. Neutrality is a product feature the hyperscalers cannot copy: none of them will ever be the governance layer across the other two, and enterprises are structurally multi-cloud. Microsoft's participation in the Series L close (PB deal record, February 9, 2026) is the tell that partnership economics currently dominate predation economics: the hyperscalers monetize every Databricks workload through the compute beneath it, and an ecosystem partner driving consumption is worth more to them than a first-party product with single-cloud reach. That equilibrium is stable while Databricks drives more hyperscaler revenue than it displaces, which at current AI workload growth is not close to binding."),

("h2", "Data gravity: the durable moat"),
("p", "Strip the noise and the moat is one sentence: it costs an enterprise almost nothing to bring data to Databricks and a great deal to take it away, and the asymmetry deepens with every layer adopted. The open-format strategy makes this politically sustainable inside customer organizations (no vendor-lock objection at adoption time) while the switching cost quietly migrates up into Unity Catalog governance, lineage, compliance attestation, and now agent workflows, where re-platforming means re-certifying everything an auditor ever signed. Competitors can match features; nobody has demonstrated they can dissolve an installed governance layer. That, more than any single product, is what an acquirer of this note's thesis is buying."),

# =====================================================================
# SECTION 12 - MARKET IMPLICATIONS AND CATEGORY
# =====================================================================
("h1", "Market Implications and Category"),

("p", "Databricks sits at the intersection of two spend pools that are converging: the data platform market (warehousing, lakes, streaming, governance), a pool we estimate at $150 billion-plus annually growing low-teens (desk estimate), and AI infrastructure, the most violent capital cycle in technology history, with hyperscaler capex alone running in the hundreds of billions annually in 2026. The lakehouse thesis is that the second pool does not bypass the first but lands on top of it: models and agents are only as useful as the governed data beneath them, so every dollar of enterprise AI ambition drags a data-platform dollar behind it. Databricks' acceleration while margin compresses is precisely what that convergence looks like from inside the P&L: AI workloads arriving faster than pricing and efficiency can absorb them."),

("p", "The category read-through runs in both directions. Today, public data-platform names are priced off Snowflake's 31%-growth reality; a Databricks listing would insert an 80%-growth, FCF-positive datapoint at the top of the comp table and force a repricing of what 'best in category' is worth, likely dragging the whole complex upward, Snowflake included, in the way that best-of-breed listings historically re-anchor their categories. Until then, the read-through runs the other way and is a genuine risk to the thesis: Databricks' eventual public multiple will be set partly off Snowflake's, and Snowflake has halved from its highs into mid-2026 before recovering (T3: TIKR, July 2026). We size that risk in Section 14 by de-rating the base-case multiple to 14-16x rather than assuming today's 19.4x survives contact with a public order book. For private-market allocators, the more actionable implication is the per-point ladder itself: if the quality-cheapest asset in the cohort re-rates toward even a fraction of the labs' per-point pricing upon listing, the convergence gain accrues to pre-IPO holders; the labs' per-point pricing, by contrast, requires AGI-grade outcomes to defend."),

# =====================================================================
# SECTION 13 - THE IPO AS THE CONVERGENCE EVENT
# =====================================================================
("h1", "The IPO as the Convergence Event"),

("p", "The thesis needs a mechanism, and the mechanism is the listing. Private marks are negotiated among consenting institutions; the per-point spread between Databricks and the labs can persist indefinitely in that regime because nothing arbitrages it. A public order book is the arbitrage. On listing day, Databricks stops being priced against the private AI complex and starts being priced against software fundamentals, where 80% growth, 74% margin, positive FCF, and >140% NRR have well-understood, generous public precedents. Convergence does not require the labs to fall; it requires Databricks to be re-based against assets it dominates on fundamentals."),

("p", "Timing: 2026 is ruled out by the CEO in terms that leave no ambiguity ('a terrible year to go public'; T2: Bloomberg Television, June 4, 2026), 2027 is the earliest, no S-1 is on file (T1: EDGAR CIK 1587468, verified July 10, 2026, Form D filings only), and prediction markets price 'no IPO by end-2027' at 0.54 (T3: 24/7 Wall St, July 7, 2026), i.e., a coin flip skewed slightly long. We read the waiting as strength, not evasion: an FCF-positive company choosing its window is exercising the governance optionality we score at 8.9, and every quarter of waiting compounds the eventual entry point at 80% growth. The next raise, if it closes, buys another year of that optionality."),

("p", "Sequencing is the real risk, and 2026 has already run the experiment at both ends. The absorption wall (Figure 10): the AI mega-listing wave totals roughly $3.9 trillion of listing value against a US IPO market that absorbed only $44 to 47 billion of proceeds in all of 2025 (T2: Deloitte, EY). The first brick has cleared: SpaceX, carrying xAI after their February 2026 all-stock merger, listed in late June 2026 at a $1.77 trillion valuation and has rallied roughly 23% since (T3, July 2026), proof that the wall is scalable for a scarce, iconic asset. OpenAI and Anthropic have reportedly filed IPO paperwork (T3: Reuters/CNA syndication, June 9, 2026), targeting roughly $1 trillion and $965 billion respectively, with potential combined primary raises across the wave in the $240 billion range, more than five times a normal year's entire issuance. If those two price well, Databricks lists into a validated category with the cleanest financial profile of the wave and the smallest ask (it may need essentially no primary capital at all). If they price poorly or exhaust the demand pool, the window shuts into 2028, and Databricks' capacity to wait, uniquely in the cohort, is the hedge. Either way the labs go first and take the experiment risk; Databricks gets to price off their result. We would rather hold the asset that chooses than the assets that must."),

("fig", "fig10_absorption.png",
 "Figure 10. The absorption question: AI mega-listing values versus 2025 US IPO issuance. Sources: SpaceX listing and performance (T3, Jun-Jul 2026); OpenAI target and Anthropic mark (T2/T3, Mar-May 2026); raise estimates (T3, desk aggregation); 2025 US IPO proceeds $44-47B (Deloitte, EY, T2)."),

# =====================================================================
# SECTION 14 - VALUATION AND SCENARIOS
# =====================================================================
("h1", "Valuation and Scenarios"),

("p", "Three independent lenses, one discipline: the base case anchors on the completed $134 billion mark and lets disclosed growth do the work; the rumored round appears only as a reference line. First lens, quality-adjusted: at $15.2 billion per AIBQ point Databricks is the cheapest quality in the cohort by 7.8x against the nearest lab (Figure 1); this lens sets direction, not a target. Second lens, growth-adjusted comps: at 0.24x per growth point against Snowflake's 0.49x, parity pricing on Snowflake's growth-adjusted multiple would imply roughly $270 billion today; we treat that as an upper bound illustration, not a target, because a private mark should discount the public comp, not match it. Third lens, forward fundamentals, which is where the target lives: mid-2027 run-rate of roughly $11.5 billion (graceful deceleration from +80% to the mid-60s) at 14 to 16x run-rate, a deliberate de-rate from today's 19.4x toward what a public order book pays for hypergrowth data platforms, yields $161 to 184 billion; widening for execution variance gives the base corridor of $155 to 190 billion (Figures 7 and 8)."),

("table", {
  "title": "Scenario architecture (12-month view, anchored on $134B; rumor not adopted)",
  "header": ["Scenario", "Run-rate path", "Multiple", "Value", "What has to be true"],
  "rows": [
    ["Bear", "Growth halves to ~40-50%; GM prints <70%, gate breaks", "11-12.5x on ~$10.4B", "$115-130B", "Agentic margin drag is structural; consumption throttling returns; rating re-scored out of Elite"],
    ["Base", "~$11.5B by mid-2027 (+65-70%); GM holds 71-74%", "14-16x", "$155-190B", "Disclosed trajectory persists with graceful deceleration; gate holds; window opens 2027"],
    ["Bull", "~$12.5B+; GM stabilizes; DBSQL and Lakebase compound", "16.5-19x", "$205-240B+", "Acceleration proves durable; listing re-anchors category; scarcity premium on cleanest AI-wave asset"],
  ],
  "align": "LLLLL",
  "source": "Desk estimates, July 10, 2026. Reference lines: $134B completed mark (T2, Feb 9, 2026); $165-175B rumored range (T3, The Information, Jun 9, 2026; unclosed, not adopted).",
}),

("fig", "fig07_football_field.png",
 "Figure 7. Valuation football field, 12-month view. The base case reaches the rumored range on fundamentals alone; the rumor is a reference line, not an input. Sources: as tabled above."),

("p", "The sensitivity grid (Figure 8) makes the machinery inspectable: value is forward run-rate times multiple, and the base intersection ($11.5 billion at 14 to 16x) sits comfortably above the current mark even after a five-point multiple de-rate. Read the bear column honestly: at $9.5 billion (growth halving) and 12x, the implied $114 billion sits 15% below the current mark, which is what the position risks if the margin gate breaks and growth decelerates simultaneously. Read the discipline the other way too: today's 19.4x on the base-case run-rate would imply roughly $223 billion, and we are deliberately not underwriting today's private multiple surviving the listing. The margin of safety is not the multiple; it is the per-point spread and the cohort-worst price for cohort-best quality."),

("fig", "fig08_sensitivity.png",
 "Figure 8. Sensitivity: implied valuation across mid-2027E run-rate and multiple, base intersection highlighted. Desk estimates, July 10, 2026."),
]
