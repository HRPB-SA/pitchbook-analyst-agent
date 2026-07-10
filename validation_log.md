# Phase One Validation Log — Databricks Initiation Note

Author: Harrison Rolfes, Senior Research Director
Validation window: July 10, 2026. Canonical pack: v3.4 (July 7-9, 2026).
Method: live re-verification of every load-bearing figure against primary sources (SEC EDGAR, Databricks newsroom, CNBC, Bloomberg, The Information via aggregators, Reuters syndication), PitchBook Premium MCP (entity 59199-40, profile last updated 2026-07-09), and web search. Conflicts frozen, not averaged.

## Priority items (per brief Section 1)

### 1. The upcoming raise — STATUS: STILL UNCLOSED. Do-not-adopt holds.
- PitchBook financing status note dated 2026-07-07: company "is in talks to raise venture funding on an undisclosed date, putting the company's post-money valuation at an estimated $170 billion." Deal 334745-56T carried as Rumor/Speculation, 13th Round, Later Stage VC. (T2/T3, PB research)
- The Information, June 9, 2026 (echoed by Reuters, CNA, Benzinga): talks at $165B-$175B; round "could kick off within the next month"; terms being finalized; unclear whether new capital will be included in the valuation. No closing reported through July 10.
- CONCLUSION: unclosed as of July 10, 2026. Excluded from base-case valuation; analyzed as forward signal.

### 2. IPO / S-1 status — CONFIRMED: no S-1 on file.
- SEC EDGAR submissions API, CIK 0001587468, checked July 10, 2026: only Form D / D/A filings (most recent 2025-12-31). No S-1, S-1/A, or other registration statement. (T1)
- CEO Ali Ghodsi, Bloomberg Television, June 4, 2026: 2026 is "a terrible year to go public"; 2027 earliest. Reaffirmed in June 9 reporting ("on track for an IPO, potentially as early as next year"). Holds.
- Prediction markets (24/7 Wall St, July 7, 2026): "No Databricks IPO by Dec 31, 2027" priced at 0.54.
- NEW vs pack: OpenAI and Anthropic have reportedly filed IPO paperwork (CNA/Reuters syndication, June 9, 2026). Sequencing risk is live, not hypothetical.

### 3. Run-rate and gross margin — CONFIRMED, no newer print.
- $6.9B annualized, +80% YoY: CNBC, June 16, 2026, from Data + AI Summit analyst session. (T2)
- Ladder re-verified from company press releases and CNBC: $4.0B/+50% (Sep 2025, PR), $4.8B/+55% (Dec 2025, PR), $5.4B/+65% (Feb 9, 2026, PR), $6.9B/+80% (Jun 16, 2026, CNBC). Acceleration confirmed.
- Gross margin 74%, down from >80%; Ghodsi guided margins to "decline further" on agent-driven compute ("the agents are generating way more queries"). Each GM point ≈ $69M annualized gross profit at $6.9B. (T2 via MLQ/CNBC coverage, June 16, 2026)
- FCF positive on TTM basis (company PR, Feb 9, 2026, T2). No newer disclosure; next print expected ~Sep-Oct 2026.
- PitchBook revenue field shows $6,900M labeled "TTM 4Q2026, period end 2026-12-31" — i.e., a forward-window figure, NOT current-period actuals. Guardrail 5 confirmed empirically; PB revenue not used as a run-rate source.

### 4. Snowflake comp — CONFIRMED with refresh.
- Market cap ~$91.1B (July 7, 2026, MacroTrends/companiesmarketcap); EV ~$89B after net cash (estimate). Shares $260.15 July 2, +18.6% YTD.
- FY27 product revenue guide $5.84B, +31%, raised from $5.66B/+27% at Q1 FY27 print May 27, 2026 (8-K, T1). Q1 actual product growth ~30-34% (Tunguz cites 34%).
- Multiple: ~$89B / $5.84B = 15.3x forward product revenue. Growth-adjusted: 0.49x per growth point vs Databricks 0.24x. Holds.
- Databricks revenue has overtaken Snowflake; gap ~$1.6B and widening (Tunguz, June 2026).

### 5. Leadership / Naveen Rao — CONFIRMED digested.
- Departure announced September 12, 2025 (Bloomberg): exit to found AI-hardware startup; advisory role retained; Databricks investing in the new venture. ~10 months old at publication; no new adverse developments found. Treated as digested with residual key-person watch on the AI line.

## Other load-bearing figures

| Figure | Pack v3.4 | Validation result | Tier |
|---|---|---|---|
| Current mark $134B | Series L | PB: deal 313367-68T, Feb 9 2026, $7.0B ($5B equity + $2B debt), post $134B; first close Dec 2025 >$4B at $134B (company PR). Held flat across closes. CONFIRMED | T2 |
| Total raised ~$29.5B | $20.2B equity + ~$9.3B debt | PB Total Raised $29,515.7M. 21 tracked deals: 12 completed equity rounds (A through L), 4 debt (Jan-25 $5.25B; Dec-25 $53.7M refi; Jan-26 $1.8B; Feb-26 $2.0B Series L tranche; plus ~$0.2B Series J embedded), 5 secondaries. Equity ≈ $20.2-20.4B. CONFIRMED within rounding | T2 |
| CE 0.34x | run-rate / equity-only | $6.9B / ~$20.2B = 0.34x. Reconciles | Derived |
| Round-count convention | 13th equity round | PB labels rumor "13th Round" on VC-round count; PB separately tracks debt deals. Stated precisely in note | T2 |
| AI products $1.7B | largest, fastest line | CNBC June 16 ($1.7B, up from $1.4B in Feb). Tunguz: ~25% of ARR, ~$1.0B six months prior. CONFIRMED | T2 |
| DBSQL ~$1.5B | Snowflake-competitive layer | Bloomberg, June 16, 2026: data warehousing at $1.5B run rate, doubled YoY. CONFIRMED | T2 |
| Lakebase pace | ~2x DBSQL at equivalent stage | Company PR Feb 9, 2026: thousands of customers in first six months, revenue growing at twice the pace of the DW product. CONFIRMED (company-stated) | T2 |
| NRR >140%, 800+ at $1M+, 70+ at $10M+, 20,000+ orgs, >60% F500 | Feb 2026 | Company PR Feb 9, 2026. AS-OF FEB 2026, five months old at publication; flagged in note | T2 |
| Employees ~9,000 | PB June 2026 | PB employee count 9,000 as of 2026-06-09. HQ SF, 46 alternate offices | T2 |
| Panther | ~$1.4B last mark, terms undisclosed, 3rd security deal | Confirmed June 16, 2026 announcement; $1.4B is Panther's 2021 Series B mark, NOT a purchase price; follows Antimatter and SiftD.ai; Anthropic among Panther customers; clearance pending | T2/T3 |
| Anthropic $965B / Series H | peer mark | CNBC May 28, 2026: $65B Series H at $965B (Altimeter, Dragoneer, Greenoaks, Sequoia); reported run-rate ~$47B; first operating profit expected Q2 2026 (~$559M). CONFIRMED | T2 |
| OpenAI $852B | peer mark | Confirmed: $852B after $122B round closed late March 2026 | T2/T3 |
| xAI implied $1.4-1.7T | inside SpaceX | MATERIAL UPDATE: SpaceX-xAI all-stock merger completed Feb 2026; SpaceX IPO'd late June 2026 at $1.77T and trades ~$2.43T (+23% since debut). xAI slice remains an implied ESTIMATE; per-point figure labeled est. Absorption framing updated: one of three mega-listings has already cleared, and it rallied | T3/est. |
| 2025 US IPO volume ~$45B | absorption denominator | EY $47.4B; Deloitte ~$44B; ~$45B midpoint used, both cited | T2 |
| Frontier Five pipeline ~$3.6T | absorption numerator | Updated: SpaceX ($1.77T) already listed; remaining pipeline OpenAI (~$1T target, paperwork filed), Anthropic ($965B, paperwork filed), Databricks. TechCrunch July 9: the three are "bigger than the last 25 years of tech exits" | T3 |

## Conflicts frozen (both values stated in the note)
1. Series L equity composition: Databricks PR (Dec 2025) ">$4B Series L at $134B" first close vs PB deal record (Feb 9, 2026) $7.0B total, $5B equity led by Insight/JPM Growth/Fidelity with Microsoft + 44 others, $2B debt. Treated as two closes of one round; both dated in note. Pack's "JPMorgan-led debt; Thrive, a16z, GIC, Temasek participation" reflects Dec close reporting; PB reflects the Feb close. Higher-tier (company PR + PB deal record) adopted.
2. AI-line trajectory: company $1.4B (Feb 2026) vs Tunguz "~$1.0B six months ago" (Dec 2025). Not a conflict on inspection (different dates); ladder used: ~$1.0B Dec-25, $1.4B Feb-26, $1.7B Jun-26.
3. Snowflake growth: 31% (FY27 guide, T1) vs ~34% (Q1 actual, T3). Guide used in multiple math (conservative for the thesis); actual noted.
4. $1M+ customers: 800+ (company, Feb 2026) vs "more than 650" (stale media). Company figure adopted.
5. 2025 US IPO proceeds: $47.4B (EY) vs ~$44B (Deloitte). Both stated; ~$45B midpoint used in chart.

## Unverifiable / labeled as estimates in the note
- AIBQ scores and sub-scores: proprietary internal framework (this desk). Not externally verifiable by construction; methodology disclosed in Appendix A.
- xAI implied valuation ($1.4-1.7T slice of SpaceX) and resulting ~$345B/pt: estimate, labeled.
- Peer CE ratios (Anthropic ~0.38x, OpenAI ~0.14x, xAI ~0.07x): desk estimates from reported cumulative raises and run-rates, labeled.
- Acquisition count (~19): aggregated from company disclosures and press coverage, labeled estimate.
- Snowflake EV ~$89B: market cap T1-derived, net-cash adjustment estimated.

## Retired figures (not used anywhere)
- $33.1B and ~$38B total-raised variants (no clean deal-record basis; superseded by PB 21-deal decomposition at $29.5B).

## Embargo check
- The correlation coefficient linking quality to valuation appears nowhere in this log, the note, or any chart. The only quality-valuation expression used is the dollar-per-AIBQ-point ranked bar.
