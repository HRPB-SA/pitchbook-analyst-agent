# Brick by Brick rewrite. Sections: The Blueprint (strategy), The Ledger (financials).
# No em-dashes. No news-outlet names. No author references.

BLOCKS = [

# =====================================================================
# 6. THE BLUEPRINT
# =====================================================================
("h1", "The Blueprint: Strategy, Read Through Actions"),

("p", "Strategy documents are cheap; wire transfers are not. This section reads Databricks' strategy through what it has actually paid for, signed, and declined to do: roughly nineteen acquisitions, a set of partnerships that would have been unthinkable three years ago, a debt structure built for a compute war, and a listing it keeps refusing to rush."),

("h2", "Acquisitions: buying the next brick, every time"),
("table", {
  "title": "The deals that built the stack",
  "header": ["Deal", "When / consideration", "What it became"],
  "rows": [
    ["MosaicML", "2023; ~$1.3B", "The AI platform layer: training, fine-tuning, serving. Now inside the company's largest product line ($1.7B run-rate, Jun 2026)"],
    ["Tabular", "2024; reported >$1B", "Detente in the format war: brought the Apache Iceberg founders in-house, making the lakehouse format-neutral and removing the last architectural adoption objection"],
    ["Neon", "2025; reported ~$1B", "Became Lakebase, the serverless Postgres for AI agents; thousands of customers within six months (company, Feb 9, 2026)"],
    ["Antimatter, SiftD.ai, Panther", "2024-2026; Panther announced Jun 16, 2026, terms undisclosed, clearance pending", "The security lakehouse: detection content, data security, and an agentic SOC surface (with Lakewatch, Mar 2026)"],
    ["~14 smaller deals", "2019-2026; mostly undisclosed", "Tuck-ins for connectors, governance, and talent; no visible integration failure across the program"],
  ],
  "align": "LLL",
  "source": "Company announcements and PitchBook, retrieved July 2026. Consideration figures are as reported at announcement; several were substantially stock.",
}),
("p", "The pattern deserves more credit than any single deal. Each major acquisition bought the seed of the next product layer roughly eighteen months before the market priced that layer as essential: Mosaic before enterprise AI training was a category, Neon before agent-provisioned databases existed as a phrase, Panther as agentic security operations is forming. The forward implication is that the M&A program is a leading indicator of the roadmap; the current security concentration (three of the last several deals) says clearly where management believes the next billion-dollar line sits."),

("h2", "Partnerships: the labs sell through the platform now"),
("table", {
  "title": "The alliance map",
  "header": ["Partner", "Deal", "What it means"],
  "rows": [
    ["OpenAI", "Multi-year partnership incl. a ~$100M commitment; frontier models made natively available on the platform and inside Agent Bricks (announced Sep 2025)", "The largest AI lab distributing through Databricks' governed estate rather than around it"],
    ["Anthropic", "Five-year alliance; Claude models native across all three clouds via SQL and model endpoints (announced Mar 2025)", "Model-agnosticism made real: the customer chooses the model, the platform keeps the workload"],
    ["Palantir", "Strategic product partnership joining Palantir's operational AI layer with the lakehouse (announced Mar 2025)", "Reach into defense and regulated operations where Databricks sells less directly"],
    ["SAP", "SAP Business Data Cloud ships with Databricks embedded (2025)", "The world's largest ERP estate flows toward the lakehouse by default"],
    ["Microsoft, AWS, Google", "First-party Azure Databricks; marketplace distribution on all three clouds; Microsoft participated in the Feb 2026 Series L close (PitchBook)", "The hyperscalers are simultaneously supplier, channel, competitor, and now investor"],
  ],
  "align": "LLL",
  "source": "Company announcements, 2025-2026; PitchBook deal record for the Series L close.",
}),
("p", "The analytical point: in 2023 the plausible bear case was that the frontier labs would commoditize Databricks from above while the hyperscalers squeezed it from below. The 2025-26 alliance map shows the opposite settlement. The labs concluded that the enterprise buys AI where its data is governed, and signed distribution into the platform; the deepest-pocketed hyperscaler wrote a check into the equity. Both are revealed-preference statements about where the durable position in the stack sits. The forward implication is a tailwind with a dependency: model partnerships make Databricks the neutral marketplace for frontier intelligence, but neutrality only stays valuable while no single model wins outright."),

("h2", "The capital blueprint: equity for ownership, debt for compute, flat marks by choice"),
("p", "The financing history is a strategy document in itself (Figure 3). Six marks in five years, from $28 billion (February 2021) to $134 billion (December 2025 and February 2026), each cleared by fundamentals that had roughly caught up with the prior mark. The composition matters more than the levels: roughly $20.2 billion of lifetime equity, over half of it in one round (the $10.2 billion Series J, December 2024) raised substantially to fund employee liquidity rather than operations, and roughly $9.3 billion of debt assembled between January 2025 and February 2026 (PitchBook deal records) to pre-fund compute commitments without dilution. A company that is free-cash-flow positive does not need either; it raised both to control its own timeline. The tell is the Series L: $134 billion held flat across two closes, a company declining a headline step-up it could have had, because it did not need the money enough to negotiate for vanity."),

("fig", "val_ladder.png",
 "Figure 3. Post-money valuation by round, Series G through L, with the reported June 2026 talks shown as unclosed. Sources: company announcements; PitchBook deal records."),

("h3", "The unclosed round: analyzed, not adopted"),
("p", "Press reports of June 9, 2026 describe discussions of a new round at $165 to 175 billion, a 23 to 31% step-up, with terms unsettled; PitchBook carried it as rumor with an estimated $170 billion post-money as of July 7, and no close had been reported as of July 10. Discipline first: an unclosed round anchors nothing in this report; every valuation statement here rests on the completed $134 billion mark. Analysis second, because the rumor is informative even while unadopted: the fundamentals-based valuation work in The Appraisal reaches $155 to 190 billion on a twelve-month view without referencing the round at all. Read against that, $165 to 175 billion is not an inflated present mark but a fair forward one, the price of the business a year from now bought today. If it closes in range, it confirms crossover demand for the eventual listing; if it dies or prices below, that is a genuine signal about appetite, and the multiple assumptions here would deserve revisiting. Either way the base case does not move, which is the point of the discipline."),

("h3", "The listing posture: waiting as strategy"),
("p", "No S-1 is on file (SEC EDGAR, CIK 1587468, verified July 10, 2026); the chief executive has publicly ruled out 2026 and pointed to 2027 at the earliest; prediction markets price no listing by end-2027 as a slight favorite. Meanwhile the two largest AI labs have reportedly filed paperwork, and the SpaceX listing (June 2026, $1.77 trillion, trading up roughly 23% since) has already tested the market's capacity for mega-scale AI paper (Figure 4). The strategic read: Databricks is the only name in the wave that can wait indefinitely, because it generates cash, and the only one that needs essentially no primary capital from a listing. Letting OpenAI and Anthropic price first outsources the experiment risk and hands Databricks a calibrated demand curve to price against. Waiting is not hesitancy here; it is the cheapest option the company owns."),

("fig", "absorption.png",
 "Figure 4. The AI mega-listing wave against the 2025 US IPO market (~$44-47B of proceeds, per major audit-firm annual reviews). SpaceX has already cleared; Databricks needs the least primary capital of any name in the queue."),

# =====================================================================
# 7. THE LEDGER
# =====================================================================
("h1", "The Ledger: The Financial Picture"),

("p", "Databricks publishes no financial statements, but it has published enough, four dated run-rate prints in ten months, a margin level and direction, retention, tier counts, and a complete financing record, to constrain a serious model. This section presents the disclosed skeleton and the seven-year three-statement model built on it; the full workbook (Inputs, Model, Valuation, with every assumption sourced) accompanies this report."),

("h2", "Revenue: acceleration at scale"),
("p", "What is disclosed: $4.0 billion annualized at +50% (September 2025), $4.8 billion at +55% (December 2025), $5.4 billion at +65% (February 9, 2026), $6.9 billion at +80% (June 16, 2026), all company statements (Figure 5). Four consecutive prints of accelerating growth while the base nearly doubled is behavior essentially without precedent at this scale; the drivers, decomposed in The Bricks, are the AI line compounding fastest, DBSQL doubling on workload migration, and the consumption meter converting agent adoption into revenue in real time. The model translates the ladder into fiscal years (ending January 31): roughly $2.6 billion in FY2025 and $4.1 billion in FY2026 as calibrated estimates, then a base case that deliberately decelerates, +77% in FY2027 to +24% by FY2031, landing at roughly $25 billion of revenue, consistent with a low-to-mid $20 billions run-rate entering calendar 2030. Nothing in the base case extrapolates the acceleration; it only asks the deceleration to be graceful, which retention above 140% alone nearly guarantees arithmetically."),

("fig", "acceleration.png",
 "Figure 5. Revenue run-rate and year-over-year growth, September 2025 to June 2026, per company disclosures. The rising growth line at rising scale is the core financial fact of the company."),

("h2", "Margins: 74%, guided lower, gated at 70"),
("p", "Gross margin is 74%, down from above 80%, and management has been unusually direct that agent-driven query volume will press it further. At the current run-rate each margin point is roughly $69 million of annualized gross profit, so the glide from the low 80s has already surrendered several hundred million dollars a year, a price paid deliberately to own the agentic workload while it forms. The quality framework in The Appraisal imposes a hard floor: a print below 70% breaks the efficiency gate and forces a re-score, and would recast the AI line from software revenue toward pass-through compute resale (Figure 6). The cushion is roughly four points. The base case holds margin in the 72.5 to 74% band through the forecast on serving efficiency and price/mix; the worst case in the model breaks the gate in FY2028 and is priced accordingly in the scenarios. The next disclosure, expected around September-October 2026, is the single most important data point for the thesis."),

("fig", "gate_gauge.png",
 "Figure 6. Gross margin (74%, June 2026, company disclosure) against the 70% efficiency-gate floor, with the prior >80% level marked."),

("h2", "Cash: the self-funding hypergrowth machine"),
("p", "The company states it is free-cash-flow positive on trailing-twelve-month and fiscal-2025 bases without giving magnitude (February 9, 2026). The model's estimate of what that understates: consumption prepayments mean customers fund growth in advance, so modeled free cash flow runs roughly $0.8 billion in FY2026 rising toward $6.7 billion by FY2031 at margins in the high teens to mid twenties, even while GAAP operating income only turns positive around FY2028 under the weight of stock compensation. Three balance-sheet consequences follow (all modeled, all labeled estimates in the workbook): cash of roughly $14 to 15 billion through the mid-forecast even after funding employee tenders and acquisitions; deferred revenue doubling to roughly $2 billion by FY2027 as commitments prepay; and debt steady at roughly $9.3 billion, comfortably serviced at a modeled ~$630 million of annual interest against gross profit two orders of magnitude larger by the forecast's end. Figure 7 places the resulting capital efficiency in its cohort: only Databricks and Anthropic convert equity into revenue at better than a third of a dollar per dollar raised, and only Databricks does it while generating cash."),

("fig", "ce_bars.png",
 "Figure 7. Run-rate revenue per dollar of lifetime equity raised, July 2026. Databricks from disclosures and PitchBook; peers are estimates from reported raises and run-rates. Debt excluded from all denominators."),

("h2", "The model on one page"),
("table", {
  "title": "Base case summary (USD millions; FY ends Jan 31; FY25A/FY26A calibrated estimates; companion workbook: Databricks_Operating_Model_Jul2026.xlsx)",
  "header": ["", "FY25A", "FY26A", "FY27E", "FY28E", "FY29E", "FY30E", "FY31E"],
  "rows": [
    ["Revenue", "2,550", "4,050", "7,168", "11,254", "15,756", "20,483", "25,399"],
    ["Growth", "59%", "59%", "77%", "57%", "40%", "30%", "24%"],
    ["Gross margin", "80.0%", "78.0%", "73.5%", "72.5%", "73.0%", "73.5%", "74.0%"],
    ["EBIT (GAAP est., incl. SBC)", "(255)", "(223)", "(179)", "169", "1,024", "2,253", "3,810"],
    ["Net income", "(195)", "(152)", "(55)", "106", "900", "1,860", "3,231"],
    ["Free cash flow", "244", "801", "1,442", "2,187", "3,510", "4,884", "6,675"],
    ["FCF margin", "9.6%", "19.8%", "20.1%", "19.4%", "22.3%", "23.8%", "26.3%"],
    ["Cash (closing)", "10,924", "15,379", "14,321", "14,508", "16,019", "18,903", "23,578"],
    ["Debt (closing)", "5,420", "7,274", "9,274", "9,274", "9,274", "9,274", "9,274"],
  ],
  "align": "LRRRRRRR",
  "source": "Model output, base case. Only the run-rate ladder, margin level/direction, FCF sign, retention, tier counts, and financing events are disclosed; every other line is an estimate with its source and logic stated in the workbook's Inputs sheet. Balance sheet balances in all years (check row in workbook).",
}),
("p", "How to read it: the disclosed facts pin the corners (revenue path, margin level and direction, FCF sign, the financing ladder), and the model fills the interior with sourced assumptions rather than hopes. The load-bearing estimates are three: sales efficiency improving as consumption expansion substitutes for sales headcount; stock compensation heavy now (an estimated low-20s percent of revenue, consistent with the scale of the company's employee tender programs) and declining; and working capital remaining a source of cash because commitments prepay. Flip any one and the earnings dates move; none of the three changes the direction. The scenario switch in the workbook flexes growth and gross margin to the Best and Worst paths shown in The Appraisal."),
]
