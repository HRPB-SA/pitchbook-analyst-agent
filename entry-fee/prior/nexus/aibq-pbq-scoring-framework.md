# AIBQ / PBQ Scoring Framework

The scoring system NEXUS uses to rate every company it tracks: AIBQ (AI
Business Quality) for AI-native companies, PBQ (Private Business Quality)
for the rest, sharing one rubric skeleton with the AI-specific
Compute Independence dimension swapped for Strategic Velocity. Mirrored
verbatim from the Notion "AIBQ/PBQ v3.0 Framework" pages, current as of
2026-08-11. This is the methodology; scored companies live in
`companies/`, and the full 666-row and 519-row score histories live in
the Excel workbook.

**Embargo note:** this framework computes a per-company AIBQ score and
tracks each company's valuation separately. A cross-company correlation
between the two is computed internally and is EMBARGOED — it appears
nowhere in this repository, in any chart, or in any company profile, and
should never be recomputed or published from the data here. See
`canon-and-governance.md` for the formal ruling.

## Contents

1. Canonical rubric — v3.0 (current, effective May 26, 2026)
2. PBQ variant rubric — v3.0
3. Weight configurations reference
4. Sector & stage classification
5. Event impact matrix (scoring lookup table)
6. Morningstar integration map
7. Version history — v2.2 (superseded), PBQ v1.0 (superseded), changelog

---

# 1. Canonical Rubric — AIBQ v3.0


# 🧮 AIBQ Scoring Rubric — v3.0 (Canonical)

**AIBQ Scoring Rubric — v3.0 (Canonical)**
**Effective: May 26, 2026 \| Supersedes v2.2 (May 12, 2026)**
**Composite = (CE × w₁) + (RQ × w₂) + (CI × w₃) + (GO × w₄) + (MD × w₅) − CRA**
---
## Principles
1. **No Δ without math.** Every score change shows its work.
2. **Single-event caps.** No one event moves a dimension more than 1.0 raw points.
3. **Daily caps.** No dimension moves more than 1.0 raw points per day.
4. **Aggregate event cap.** A single real-world event cannot move the composite more than ±0.50 in a single day.
5. **Confidence tags.** Every change tagged High / Medium / Low based on source tier.
6. **NEXUS log required.** Nothing becomes canonical until logged to the Daily Scores database.
7. **Precision.** Composites carry 0.01 precision. Dimensions carry 0.1 precision.
8. **Carry-forward.** Scores persist between events. No interpolation. No calendar-driven updates.
9. **24-hour cooling.** Before external citation of any score change.
10. **Distinct Pathway Test.** Multi-dimension events require different causal mechanisms per dimension.
11. **Second-order evidence rule.** Indirect effects require separate confirming evidence before adjustment.
---
## Three Weight Configurations
| Dimension | Code | Report Weight (Published) | Standard Weight (Quality) | Exit Weight (Returns) |
| --- | --- | --- | --- | --- |
| Capital Efficiency | CE | 20% | 15% | 20% |
| Revenue Quality | RQ | 25% | 30% | 25% |
| Compute Independence | CI | 15% | 10% | 10% |
| Governance Optionality | GO | 20% | 15% | 25% |
| Moat Durability | MD | 20% | 30% | 20% |
**Report Weights:** Original weights from "Ranking the AI Giants" (March 2026). Maintained for consistency with published research.
**Standard Weights:** Quality-focused. Emphasizes long-term business quality (RQ + MD = 60%). For research reports and quality rankings.
**Exit-Oriented Weights:** Return-focused. Emphasizes catalysts and execution risk (GO + CE = 45%). For investor allocation decisions.
---
## CE — Capital Efficiency (20%)
### Sub-Score Decomposition
| Sub-Score | Code | Weight | What It Measures | Applies to Stages |
| --- | --- | --- | --- | --- |
| Primary Efficiency Metric | CE-1 | 40% | Stage-appropriate capital conversion | All (S1–S5) |
| Gross Margin Quality | CE-2 | 25% | Unit economics health | S2–S5 |
| Burn Trajectory | CE-3 | 20% | Direction of capital efficiency improvement | S2–S4 |
| Capital Structure Health | CE-4 | 15% | Dilution, debt, runway adequacy | All (S1–S5) |
### CE-1: Stage-Gated Thresholds
| Stage | Label | Primary Metric | 1–2 | 3–4 | 5–6 | 7–8 | 9–10 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | Pre-Revenue | Cash runway (months) | <12mo | 12–18mo | 18–24mo | 24–36mo | >36mo |
| S2 | Early Revenue | Burn Multiple | >5x | 3–5x | 2–3x | 1–2x | <1x |
| S3 | Growth | Burn Multiple | >5x | 3–5x | 2–3x | 1–2x | <1x |
| S4 | Scale | Bessemer Efficiency Score | <0.5x | 0.5–1.0x | 1.0–1.5x | 1.5–2.0x | >2.0x |
| S5 | Pre-IPO | Efficiency Index | <0.20 | 0.20–0.35 | 0.35–0.50 | >0.50 | >0.50+FCF+ |
**Efficiency Index formula (S5 only):** Triggers when TTM FCF+, ARR growth \>40%, gross margin \>70%.
Index = (min(ARR_growth/100, 1.0) × 0.4) + (min(FCF/Revenue, 0.30) × 0.3) + (GrossMargin/100 × 0.3)
### CE-2: Gross Margin Thresholds
| Gross Margin | Score | Sector Adjustment |
| --- | --- | --- |
| <30% | 1–2 | AI-INFRA/AI-ACCEL: +1.0 if >50%. CLIMATE/SPACE: +1.0 if >40% |
| 30–50% | 3–4 | — |
| 50–65% | 5–6 | — |
| 65–75% | 7–8 | — |
| >75% | 9–10 | — |
### CE-3: Burn Trajectory Thresholds
| QoQ Change | Score |
| --- | --- |
| Worsening >50% | 1–2 |
| Worsening 10–50% | 3–4 |
| Flat (±10%) | 5–6 |
| Improving 10–50% | 7–8 |
| Improving >50% | 9–10 |
### CE-4: Capital Structure Health Thresholds
| Profile | Score |
| --- | --- |
| <12mo runway, >50% dilution, debt >2x ARR | 1–2 |
| 12–18mo runway, 30–50% dilution, moderate debt | 3–4 |
| 18–24mo runway, 20–30% dilution, manageable debt | 5–6 |
| >24mo runway, <20% dilution, minimal debt | 7–8 |
| Self-funding (FCF+), clean cap table, no distressed instruments | 9–10 |
---
## RQ — Revenue Quality (25%)
### Sub-Score Decomposition
| Sub-Score | Code | Weight | What It Measures | Applies to Stages |
| --- | --- | --- | --- | --- |
| Net Revenue Retention | RQ-1 | 30% | Expansion + contraction + churn | S3–S5 (S2: gross retention) |
| Customer Concentration Risk | RQ-2 | 20% | Revenue dependency on top accounts | S2–S5 |
| Enterprise Mix & ACV Quality | RQ-3 | 20% | Enterprise share + ACV distribution | S2–S5 |
| Revenue Durability | RQ-4 | 15% | Contract length, switching costs, recurring vs consumption | S2–S5 |
| Pricing Power | RQ-5 | 15% | Ability to raise prices without churn | S3–S5 |
### RQ-1: NRR Thresholds
| NRR | Score | S2 Alternative (Gross Retention) |
| --- | --- | --- |
| <90% | 1–2 | <70% |
| 90–105% | 3–4 | 70–80% |
| 105–120% | 5–6 | 80–85% |
| 120–140% | 7–8 | 85–90% |
| >140% | 9–10 | >90% |
### RQ-2: Customer Concentration Thresholds
| Profile | Score | Special Rule |
| --- | --- | --- |
| Top 1 customer >40% of revenue | 1–2 | — |
| Top 3 customers >50% of revenue | 3–4 | — |
| Top 10 customers 30–50% of revenue | 5–6 | — |
| Top 10 customers 15–30% of revenue | 7–8 | — |
| Top 10 <15%; no single >5% | 9–10 | Cloud partner >30% rev as investor+customer: −1.0 modifier |
### RQ-3: Enterprise Mix Thresholds
| Profile | Score |
| --- | --- |
| >80% consumer/self-serve, no enterprise motion | 1–2 |
| 50–80% consumer, early enterprise traction | 3–4 |
| Mixed: 40–60% enterprise, \$100K+ ACV emerging | 5–6 |
| Enterprise-dominant: >60% enterprise, 100+ at \$100K+ ACV | 7–8 |
| >80% enterprise, 100+ at \$1M+ ACV, Fortune 500 penetration | 9–10 |
### RQ-4: Revenue Durability Thresholds
| Profile | Score |
| --- | --- |
| Pure usage/consumption, no commitments, monthly billing | 1–3 |
| Mostly usage with some annual contracts; <50% committed | 4–5 |
| Majority annual contracts; 50–70% committed ARR | 6–7 |
| Multi-year contracts; >70% committed; high switching costs | 8–9 |
| Mission-critical platform; >80% committed; contractual minimums; regulatory lock-in | 10 |
### RQ-5: Pricing Power Thresholds
| Profile | Score | AI Signal |
| --- | --- | --- |
| Commodity pricing; customers easily substitute | 1–2 | — |
| Below-market pricing to win share | 3–4 | — |
| Market-rate; modest increases tolerated | 5–6 | — |
| Above-market; successful upsell/cross-sell | 7–8 | — |
| Premium pricing; demand exceeds supply | 9–10 | Maintained per-token revenue during 2025–26 compression = 8+ |
---
## CI — Compute Independence (15%)
### Sub-Score Decomposition
| Sub-Score | Code | Weight | What It Measures |
| --- | --- | --- | --- |
| Provider Diversification | CI-1 | 30% | Number and balance of compute sources |
| Infrastructure Ownership | CI-2 | 25% | Own DCs, racks, silicon |
| Energy Independence | CI-3 | 20% | Direct PPAs, energy security |
| Supply Chain Resilience | CI-4 | 15% | Chip sourcing diversity, TSMC dependency |
| Contractual Lock-in Risk | CI-5 | 10% | Exclusivity, minimums, exit costs |
**CI Sector Adjustments:**
- **AI-PLAT:** +1.0 modifier to CI composite (platform deployment, not frontier training)
- **AI-APP:** CI weight reduces to 10% (freed 5% to MD)
- **AI-ACCEL:** CI-4 weight increases to 30% (TSMC dependency is existential)
### CI-1: Provider Diversification Thresholds
| Profile | Score |
| --- | --- |
| Single provider, >90% from one source | 1–2 |
| Two providers, one dominant (>70%) | 3–4 |
| Three providers, no one >50% | 5–6 |
| Four+ providers, well-balanced | 7–8 |
| Own infra + 3+ cloud + shift workloads in <30 days | 9–10 |
### CI-2: Infrastructure Ownership Thresholds
| Profile | Score |
| --- | --- |
| Zero owned; fully renting cloud compute | 1–2 |
| Leased racks in colocation | 3–4 |
| Owned inference racks in partner DCs | 5–6 |
| Owned DCs + inference racks; custom ASIC in dev | 7–8 |
| Vertically integrated: own DCs + custom silicon GA + own power | 9–10 |
### CI-3: Energy Independence Thresholds
| Profile | Score |
| --- | --- |
| No energy strategy; dependent on cloud provider energy | 1–2 |
| Energy awareness but no direct contracts | 3–4 |
| 1–2 PPAs, <30% of needs | 5–6 |
| Major PPAs (>500MW), 30–70% of needs | 7–8 |
| >1GW direct energy; surplus available | 9–10 |
### CI-4: Supply Chain Resilience Thresholds
| Profile | Score |
| --- | --- |
| Single chip vendor, single foundry (TSMC) | 1–2 |
| Primary + secondary in evaluation | 3–4 |
| Multiple active (NVIDIA + AMD or custom) | 5–6 |
| Multiple + custom reducing dependency | 7–8 |
| Custom silicon from multiple foundries + commercial backup | 9–10 |
### CI-5: Contractual Lock-in Risk Thresholds
| Profile | Score |
| --- | --- |
| Exclusive agreement; exit penalties >\$1B | 1–2 |
| Exclusive training, non-exclusive inference | 3–4 |
| Non-exclusive; 6–12mo wind-down | 5–6 |
| Short-term (<2yr); low switching; portable workloads | 7–8 |
| No exclusivity; all portable; owned or month-to-month | 9–10 |
---
## GO — Governance Optionality (20%)
### Sub-Score Decomposition
| Sub-Score | Code | Weight | What It Measures |
| --- | --- | --- | --- |
| Board Quality & Independence | GO-1 | 25% | Composition, independence, expertise |
| Corporate Structure | GO-2 | 20% | Entity structure, cap table, voting rights |
| IPO / Exit Readiness | GO-3 | 20% | Banker mandate, audit readiness, S-1 indicators |
| Regulatory Landscape | GO-4 | 20% | Risk, compliance, government relationships |
| C-Suite Stability & Quality | GO-5 | 15% | Tenure, transitions, bench depth |
**Special Rules:**
- **Nonprofit-to-profit conversions:** −1.0 modifier to GO-2 until fully complete
- **Security clearance (FedRAMP High, IL5+):** +0.3 to GO-4
### GO-1: Board Quality & Independence Thresholds
| Profile | Score |
| --- | --- |
| No formal board; founder-controlled, no oversight | 1–2 |
| Board exists, <2 independent directors, no expertise | 3–4 |
| 2–3 independents; one with industry expertise | 5–6 |
| Majority independent; IPO-experienced director(s); audit committee | 7–8 |
| Majority independent, IPO veterans, domain experts, comp+audit committees, lead independent | 9–10 |
### GO-2: Corporate Structure Thresholds
| Profile | Score |
| --- | --- |
| Complex multi-entity; opaque cap table; extreme founder control; structural litigation | 1–2 |
| Messy cap table; ratchets/anti-dilution; unclear ownership | 3–4 |
| Clean single-entity; standard preferred/common; 409A current | 5–6 |
| Clean; standard preferences; ESOP managed; secondary active | 7–8 |
| IPO-ready: clean cap, no unusual provisions, convertibles resolved, transfer agent | 9–10 |
### GO-3: IPO / Exit Readiness Thresholds
| Profile | Score |
| --- | --- |
| No IPO prep; no audited financials; no banker relationships | 1–2 |
| Early IPO discussions; beginning audit prep | 3–4 |
| Audited financials (2+ years); banker conversations active | 5–6 |
| Banker mandate confirmed; CFO with public co experience; SOX underway | 7–8 |
| S-1 filed; quiet period; pricing imminent | 9–10 |
### GO-4: Regulatory Landscape Thresholds
| Profile | Score |
| --- | --- |
| Active investigations; pending existential litigation; regulatory gray zone | 1–2 |
| FTC/DOJ inquiries; class actions; compliance gaps | 3–4 |
| Moderate environment; compliant but no proactive engagement | 5–6 |
| Proactive engagement; ahead of requirements; favorable relationships | 7–8 |
| Regulatory tailwinds: gov contracts, favorable rulings, regulatory moat | 9–10 |
### GO-5: C-Suite Stability & Quality Thresholds
| Profile | Score |
| --- | --- |
| CEO/CFO departed trailing 12mo; no replacement; multiple C-suite exits | 1–2 |
| Recent transition (<6mo); new leader untested | 3–4 |
| Stable (2+ years); adequate bench; planned transitions only | 5–6 |
| CEO with prior exit; CFO from public company; deep VP bench | 7–8 |
| CEO with multiple exits; CFO with S-1 experience; full public pedigree | 9–10 |
---
## MD — Moat Durability (20%)
### Sub-Score Decomposition
| Sub-Score | Code | Weight | What It Measures |
| --- | --- | --- | --- |
| Technical Differentiation | MD-1 | 25% | Benchmarks, patents, technical novelty |
| Switching Costs & Lock-in | MD-2 | 25% | Integration depth, data gravity, workflow dependency |
| Talent Density & Retention | MD-3 | 20% | Research talent, attrition, hiring competitiveness |
| Data & Network Effects | MD-4 | 15% | Proprietary data, network effects, flywheel |
| Brand & Category Position | MD-5 | 15% | Recognition, category ownership, trust |
### MD-1: Technical Differentiation Thresholds
| Profile | Score |
| --- | --- |
| No differentiation; commodity/wrapper; no proprietary IP | 1–2 |
| Minor improvements over open-source | 3–4 |
| Meaningful; can't replicate within 12mo | 5–6 |
| Leading benchmarks; substantial patents | 7–8 |
| Category-defining; >5pp benchmark lead; 12+ months ahead; foundational patents | 9–10 |
### MD-2: Switching Costs & Lock-in Thresholds
| Profile | Score |
| --- | --- |
| Zero switching costs; drop-in replacement | 1–2 |
| Low; migration <1 week | 3–4 |
| Moderate; 1–3 month migration | 5–6 |
| High; 3–6 month migration; data migration; retraining | 7–8 |
| Very high; >6mo; regulatory recertification; embedded in critical workflows | 9–10 |
### MD-3: Talent Density & Retention Thresholds
| Profile | Score |
| --- | --- |
| >30% attrition; difficulty hiring; no notable researchers | 1–2 |
| 20–30% attrition; few notable researchers | 3–4 |
| <20% attrition; competitive; solid research team | 5–6 |
| <15% attrition; talent magnet; 5+ notable researchers | 7–8 |
| <10% attrition; recruits from competitors; world-class lab | 9–10 |
### MD-4: Data & Network Effects Thresholds
| Profile | Score |
| --- | --- |
| No proprietary data; no network effects | 1–2 |
| Small dataset; weak effects | 3–4 |
| Growing data asset; moderate network effects | 5–6 |
| Large proprietary data; strong effects; flywheel operational | 7–8 |
| Massive data moat; winner-take-most; compounds over time; unreplicable | 9–10 |
### MD-5: Brand & Category Position Thresholds
| Profile | Score |
| --- | --- |
| Unknown brand; undifferentiated | 1–2 |
| Niche recognition | 3–4 |
| Growing recognition; mentioned in analyses | 5–6 |
| Category leader in rankings; Fortune 500 trusted | 7–8 |
| Iconic; category creator or synonym; global recognition | 9–10 |
---
## Stage Classification System
| Stage | Label | Defining Characteristics | CE Primary Metric |
| --- | --- | --- | --- |
| S1 | Pre-Revenue | No GA product or <\$1M ARR | Cash runway |
| S2 | Early Revenue | \$1M–\$50M ARR | Burn Multiple |
| S3 | Growth | \$50M–\$500M ARR | Burn Multiple |
| S4 | Scale | \$500M–\$5B ARR | Bessemer Efficiency |
| S5 | Pre-IPO / Mega | >\$5B ARR or IPO-track | Efficiency Index |
### Stage Adjustments
| Stage | Adjustment | Rationale |
| --- | --- | --- |
| S1 | −1.0 to −0.5 | High mortality, minimal data |
| S2 | −0.5 to −0.25 | Real revenue but small sample |
| S3 | 0 | Baseline |
| S4 | 0 to +0.25 | Demonstrated durability |
| S5 | 0 to +0.5 | Near-public-grade disclosure |
---
## Sector Classification — Four-Question AIBQ vs PBQ Test
A company scores under AIBQ if YES to ≥2 of:
1. Does the company train or fine-tune its own foundation models (\>10B parameters)?
2. Does AI model performance directly determine core product differentiation?
3. Is compute infrastructure access a binding constraint on business continuity?
4. Does the company's revenue model primarily monetize AI capabilities?
### AIBQ Sector Codes
| Code | Label | CI Adjustment |
| --- | --- | --- |
| AI-INFRA | Infrastructure / Foundation Models | Standard |
| AI-PLAT | AI-Enabled Platform | +1.0 CI modifier |
| AI-APP | AI Application Layer | CI weight 10% (5% to MD) |
| AI-ACCEL | AI Hardware / Accelerators | CI-4 weight → 30% |
| AI-AUTO | AI Robotics / Automation | Standard |
| AI-BIO | AI for Life Sciences | Standard |
### PBQ Sector Codes
FINTECH, CYBER, INFRA-SW, HEALTH, CLIMATE, CONSUMER, DEFENSE, SPACE
---
## Compounding Risk Adjustment (CRA)
| Condition | Adjustment |
| --- | --- |
| 0–1 dimensions ≤ 3.0 | 0 |
| 2 dimensions ≤ 3.0 | −0.25 |
| 3 dimensions ≤ 3.0 | −0.75 |
| 4+ dimensions ≤ 3.0 | −1.50 |
---
## Data Availability Index (DAI)
| Level | DAI Score | What's Available |
| --- | --- | --- |
| D1 | 1–2 | PitchBook profile + press only |
| D2 | 3–4 | • investor deck or analyst estimates |
| D3 | 5–6 | • reported financials (unaudited) + board |
| D4 | 7–8 | • audited financials + public filings + analyst coverage |
| D5 | 9–10 | Full public-grade disclosure |
**Confidence Band** = ± (5 − DAI/2)
---
## Score Freshness
| Time Since Last Event | Label | DAI Modifier |
| --- | --- | --- |
| <30 days | Current | 0 |
| 30–90 days | Recent | −0.5 |
| 90–180 days | Aging | −1.0 |
| 180–365 days | Stale | −2.0 |
| >365 days | Expired | Flag "Under Review" |
---
## Double-Counting Rules
1. **Distinct Pathway Test:** each adjustment must cite a different causal mechanism.
2. **First-order effects** apply immediately; second-order require confirming evidence.
3. **Aggregate Event Cap:** single event cannot move composite more than ±0.50/day.
4. **Scoring memo required** when event triggers 3+ dimensions.
5. **Reversals** scored independently at resolution-appropriate magnitude.
---
## Scoring Protocol
1. Morning Digest identifies events from T1/T2 sources.
2. Apply rubric to each event; compute raw Δ per sub-score, then per dimension.
3. Apply single-event and daily caps.
4. Check Distinct Pathway Test for multi-dimension events.
5. Compute CRA based on current dimension scores.
6. Sum weighted Δ; compute new composite (0.01 precision).
7. Tag confidence (High/Medium/Low).
8. Write Daily Scores DB entry with all dimensions, sub-scores, composite, events, pathways, and rubric citations.
9. Only after NEXUS log: publish in digest as canonical.
10. Before external publication: 24-hour cooling-off period.
## Review Cadence
**Quarterly rubric review:** Are thresholds still calibrated? New event types needed?
**Annual recalibration:** If all five companies drift uniformly, the rubric is miscalibrated.
**Audit trail:** Every Daily Scores DB entry preserved indefinitely.
---
*v3.0 — Effective May 26, 2026 \| Owner: Harrison Rolfes \| PBQ variant at separate rubric page*


---

# 2. PBQ Variant Rubric — v3.0

# 🏢 PBQ Scoring Rubric — v3.0 (Canonical)

**PBQ Scoring Rubric — v3.0 (Canonical)**
**Effective: May 26, 2026 \| Supersedes v1.0**
**Composite = (CE × w₁) + (RQ × w₂) + (SV × w₃) + (GO × w₄) + (MD × w₅) − CRA**
PBQ is structurally identical to AIBQ with one substitution: **CI (Compute Independence) is replaced by SV (Strategic Velocity)** at the same weight. All other dimensions (CE, RQ, GO, MD), their sub-scores, thresholds, stage classifications, CRA, DAI, freshness rules, double-counting rules, and scoring protocol are identical to the AIBQ v3.0 rubric. Refer to the AIBQ v3.0 page for those shared sections.
This page documents SV and the PBQ-specific sector codes only.
---
## Principles
Identical to AIBQ v3.0. All 11 principles apply.
---
## Three Weight Configurations
| Dimension | Code | Report Weight (Published) | Standard Weight (Quality) | Exit Weight (Returns) |
| --- | --- | --- | --- | --- |
| Capital Efficiency | CE | 20% | 15% | 20% |
| Revenue Quality | RQ | 25% | 30% | 25% |
| Strategic Velocity | SV | 15% | 10% | 10% |
| Governance Optionality | GO | 20% | 15% | 25% |
| Moat Durability | MD | 20% | 30% | 20% |
---
## SV — Strategic Velocity (15%)
### Sub-Score Decomposition
| Sub-Score | Code | Weight | What It Measures |
| --- | --- | --- | --- |
| Product Cadence | SV-1 | 30% | Speed of shipping, release frequency |
| Geographic Expansion | SV-2 | 20% | Revenue-generating presence in new markets |
| Platform & Ecosystem | SV-3 | 25% | API adoption, integrations, ecosystem lock-in |
| M&A Execution | SV-4 | 15% | Acquisition velocity and integration success |
| Competitive Response Time | SV-5 | 10% | Speed of response to threats |
### SV-1: Product Cadence Thresholds
| Profile | Score |
| --- | --- |
| No product shipped; concept stage | 1–2 |
| Single product GA; cadence >12mo | 3–4 |
| 2–3 products GA; quarterly releases | 5–6 |
| Multi-product; monthly/continuous releases | 7–8 |
| Category-defining platform; continuous; new categories annually | 9–10 |
### SV-2: Geographic Expansion Thresholds
| Profile | Score |
| --- | --- |
| Single geography; single office | 1–2 |
| 2 geographies with revenue entities | 3–4 |
| 3–5 geographies; regional teams; localized | 5–6 |
| 5–10 major markets; localized sales+support+compliance | 7–8 |
| Global (10+); local regulatory; local partnerships | 9–10 |
### SV-3: Platform & Ecosystem Thresholds
| Profile | Score |
| --- | --- |
| No API; closed system | 1–2 |
| Basic API; <10 integrations | 3–4 |
| Public API; 10–50 integrations; growing community | 5–6 |
| Rich ecosystem; 50–200 integrations; marketplace | 7–8 |
| Industry standard; 200+; competitors build on you | 9–10 |
### SV-4: M&A Execution Thresholds
| Profile | Score |
| --- | --- |
| Acquisition stalled >180 days | 2–3 |
| No M&A (neutral) | 3 |
| 1–2 integrated in trailing 24mo | 5–6 |
| 3+ in 24mo with confirmed integrations | 7–8 |
| Every acquisition fills gap; <90 day integration; revenue retained | 9–10 |
### SV-5: Competitive Response Time Thresholds
| Profile | Score |
| --- | --- |
| Competitor shipped >6mo before response | 1–2 |
| Competitor first; responded 3–6mo | 3–4 |
| Parity; no consistent first-mover | 5–6 |
| Consistently first; competitors respond to you | 7–8 |
| Category creator; competitors can't match within 12mo | 9–10 |
---
## PBQ Sector Codes
| Code | Label |
| --- | --- |
| FINTECH | Financial Technology |
| CYBER | Cybersecurity |
| INFRA-SW | Infrastructure Software |
| HEALTH | Healthcare & Life Sciences |
| CLIMATE | Climate & Clean Tech |
| CONSUMER | Consumer Technology |
| DEFENSE | Defense & Government Tech |
| SPACE | Space & Aerospace |
---
## AIBQ vs PBQ Classification — Four-Question Test
A company scores under AIBQ if YES to ≥2 of:
1. Does the company train or fine-tune its own foundation models (\>10B parameters)?
2. Does AI model performance directly determine core product differentiation?
3. Is compute infrastructure access a binding constraint on business continuity?
4. Does the company's revenue model primarily monetize AI capabilities?
All other companies score under PBQ.
---
## Shared Sections (Refer to AIBQ v3.0)
The following sections are identical between AIBQ and PBQ. Refer to the AIBQ v3.0 rubric page for full thresholds:
- **CE — Capital Efficiency** (sub-scores CE-1 through CE-4, stage-gated thresholds)
- **RQ — Revenue Quality** (sub-scores RQ-1 through RQ-5)
- **GO — Governance Optionality** (sub-scores GO-1 through GO-5, special rules)
- **MD — Moat Durability** (sub-scores MD-1 through MD-5)
- **Stage Classification System** (S1–S5 with stage adjustments)
- **Compounding Risk Adjustment (CRA)**
- **Data Availability Index (DAI)**
- **Score Freshness**
- **Double-Counting Rules**
- **Scoring Protocol**
- **Review Cadence**
---
*v3.0 — Effective May 26, 2026 \| Owner: Harrison Rolfes \| AIBQ variant at separate rubric page*


---

# 3. Weight Configurations Reference

# ⚖️ Weights

## Three Configurations
| Dimension | Code | Report Weight | Standard Weight | Exit Weight |
| --- | --- | --- | --- | --- |
| Capital Efficiency | CE | 20% | 15% | 20% |
| Revenue Quality | RQ | 25% | 30% | 25% |
| Compute Independence / Strategic Velocity | CI/SV | 15% | 10% | 10% |
| Governance Optionality | GO | 20% | 15% | 25% |
| Moat Durability | MD | 20% | 30% | 20% |
| **Total** |  | **100%** | **100%** | **100%** |
---
## Report Weights (Published)
Original weights from "Ranking the AI Giants" (March 4, 2026). Maintained for consistency with published research and PitchBook platform display. These are the default weights for all external-facing scores.
## Standard Weights (Quality Focus)
Emphasizes long-term business quality. RQ + MD = 60% of composite. Used for research reports, quality rankings, and Morningstar-style analysis. Rationale: Revenue quality and moat durability are the strongest predictors of long-term business value.
## Exit-Oriented Weights (Return Focus)
Emphasizes catalysts and execution risk. GO + CE = 45% of composite. Used for investor allocation decisions, IPO readiness assessments, and deal-specific analysis. Rationale: For private market participants, governance and capital efficiency determine whether quality translates into investor returns.
---
## Why These Weights?
**RQ was underweighted at 25% (Report).** Revenue quality is the single best predictor of private company exit outcomes. Bessemer's Cloud Index shows NRR and revenue growth explain \>60% of variance in EV multiples. Standard config moves RQ to 30%.
**CI/SV was overweighted at 15% (Report).** Compute independence matters enormously for \~20 AI-INFRA companies but barely for the other 1,660 unicorns. Reduced to 10% with sector amplification.
**MD was underweighted at 20% (Report).** Morningstar's entire public equity framework is built on moat primacy. Wide Moat ETF outperformance is empirical evidence that moat deserves heavy weight. Standard config moves MD to 30%.
**GO needs two treatments.** For quality assessment, governance is background. For exit assessment, it's make-or-break. Dual config handles this.
---
## Backtesting Protocol
- Minimum sample: 50 companies with 12+ months history and 10+ exits before backtesting
- Method: Regress outcomes on dimension scores; compare coefficients to theoretical weights
- Cadence: Annual, with results in methodology update note
- Threshold: If regression weights diverge \>5pp on any dimension, investigate and consider adjustment


---

# 4. Sector & Stage Classification

# 🏷️ Sector & Stage Classification

## Four-Question AIBQ vs PBQ Classification Test
A company scores under **AIBQ** if YES to ≥2 of:
1. Does the company train or fine-tune its own foundation models (\>10B parameters)?
2. Does AI model performance directly determine core product differentiation?
3. Is compute infrastructure access a binding constraint on business continuity?
4. Does the company's revenue model primarily monetize AI capabilities?
All other companies score under **PBQ**.
---
## AIBQ Sector Codes
| Code | Label | CI Adjustment | Example Companies |
| --- | --- | --- | --- |
| AI-INFRA | Infrastructure / Foundation Models | Standard | Anthropic, OpenAI, SSI |
| AI-PLAT | AI-Enabled Platform | +1.0 CI modifier | Databricks |
| AI-APP | AI Application Layer | CI weight 10% (5% to MD) | Cursor, Jasper |
| AI-ACCEL | AI Hardware / Accelerators | CI-4 weight → 30% | Cerebras, Groq |
| AI-AUTO | AI Robotics / Automation | Standard | Figure AI, Physical Intelligence |
| AI-BIO | AI for Life Sciences | Standard | Recursion, Insitro |
---
## PBQ Sector Codes
| Code | Label | Example Companies |
| --- | --- | --- |
| FINTECH | Financial Technology | Stripe, Plaid, Chime |
| CYBER | Cybersecurity | Wiz, Snyk, Lacework |
| INFRA-SW | Infrastructure Software | Canva, Figma, Notion |
| HEALTH | Healthcare & Life Sciences | Tempus, Devoted Health |
| CLIMATE | Climate & Clean Tech | Redwood Materials, Commonwealth Fusion |
| CONSUMER | Consumer Technology | Discord, Reddit |
| DEFENSE | Defense & Government Tech | Anduril, Shield AI |
| SPACE | Space & Aerospace | SpaceX, Relativity Space |
---
## Stage Classification System
| Stage | Label | Defining Characteristics | CE Primary Metric | Stage Adjustment |
| --- | --- | --- | --- | --- |
| S1 | Pre-Revenue | No GA product or <\$1M ARR | Cash runway | −1.0 to −0.5 |
| S2 | Early Revenue | \$1M–\$50M ARR | Burn Multiple | −0.5 to −0.25 |
| S3 | Growth | \$50M–\$500M ARR | Burn Multiple | 0 (baseline) |
| S4 | Scale | \$500M–\$5B ARR | Bessemer Efficiency | 0 to +0.25 |
| S5 | Pre-IPO / Mega | >\$5B ARR or IPO-track | Efficiency Index | 0 to +0.5 |
---
## Classification Examples — Frontier Five
| Company | Q1 | Q2 | Q3 | Q4 | Count | Framework | Sector | Stage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Databricks | No | Yes | No | Yes | 2 | AIBQ | AI-PLAT | S5 |
| Anthropic | Yes | Yes | Yes | Yes | 4 | AIBQ | AI-INFRA | S5 |
| OpenAI | Yes | Yes | Yes | Yes | 4 | AIBQ | AI-INFRA | S5 |
| xAI | Yes | Yes | Yes | Yes | 4 | AIBQ | AI-INFRA | S4 |
| SSI | Yes | Yes | Yes | No | 3 | AIBQ | AI-INFRA | S1 |
---
*v3.0 — Effective May 26, 2026 \| Owner: Harrison Rolfes*


---

# 5. Event Impact Matrix

The scoring lookup table mapping event types to dimension impacts lives as a structured database (125 rows) rather than a prose page; see `NEXUS Intelligence/excel/` for the full table. Container page note:

# 📁 Event Catalog

Reference catalog of every possible event type, its valid Δ range, tier, sub-score target, and distinct pathway. This is the lookup table used during scoring.
<database url="https://app.notion.com/p/36c5e7ad9f7f81acba50c7f7f49e8d5f" inline="true" data-source-url="collection://c9df673a-b3ba-4148-b490-d7f911a9c66a"></database>

<!-- Extraction note: the inline database (AIBQ Event Impact Matrix, collection://c9df673a-b3ba-4148-b490-d7f911a9c66a) is extracted in full to event-impact-matrix.json in this directory. -->


---

# 6. Morningstar Integration Map

# ⭐ Morningstar Integration Map

## Purpose
Maps AIBQ/PBQ v3.0 framework outputs to Morningstar's equity research taxonomy. Enables publication of AIBQ-derived insights on the Morningstar platform using standard Morningstar language.
---
## MD → Morningstar Moat Rating
| MD Score | Morningstar Moat Rating | Rationale |
| --- | --- | --- |
| 9–10 | Wide Moat | Category-defining; >5pp benchmark lead; very high switching costs; world-class talent; massive data moat |
| 7–8 | Narrow Moat | Strong benchmarks; high switching costs; talent magnet; data flywheel operational |
| 5–6 | No Moat (Emerging) | Moderate differentiation; growing switching costs; competitive but not dominant |
| 1–4 | No Moat | Low differentiation; commodity product or wrapper; minimal switching costs |
### Moat Source Cross-Reference
| Morningstar Moat Source | AIBQ Sub-Score | Threshold for Attribution |
| --- | --- | --- |
| Intangible Assets | MD-1 (Technical Differentiation) | MD-1 ≥ 7 |
| Switching Costs | MD-2 (Switching Costs & Lock-in) | MD-2 ≥ 7 |
| Network Effect | MD-4 (Data & Network Effects) | MD-4 ≥ 7 |
| Cost Advantage | CE-2 (Gross Margin) + CI-2 (Infrastructure Ownership) | CE-2 ≥ 8 AND CI-2 ≥ 7 |
| Efficient Scale | RQ-2 (Concentration) + MD-5 (Brand) | RQ-2 ≥ 8 AND MD-5 ≥ 8 |
---
## Quality Tier Definitions
| Quality Tier | Composite Range | Description | Morningstar Equivalent |
| --- | --- | --- | --- |
| Elite | 8.5–10.0 | Best-in-class across all dimensions; IPO-ready or near-public quality | Exemplary Capital Allocation |
| Strong | 7.0–8.49 | Above-average across most dimensions; one weakness tolerated | Standard Capital Allocation |
| Adequate | 5.0–6.99 | Mixed; meaningful strengths offset by material gaps | Standard Capital Allocation |
| Developing | 3.0–4.99 | Below-average; structural issues in 2+ dimensions | Poor Capital Allocation |
| Distressed | 1.0–2.99 | Critical weakness across majority of dimensions; CRA likely applied | Poor Capital Allocation |
---
## DAI → Morningstar Uncertainty Rating
| DAI Score | Confidence Band | Morningstar Uncertainty |
| --- | --- | --- |
| 9–10 | ±0.0–0.5 | Low |
| 7–8 | ±1.0–1.5 | Medium |
| 5–6 | ±2.0–2.5 | High |
| 3–4 | ±3.0–3.5 | Very High |
| 1–2 | ±4.0–4.5 | Extreme |
---
## Publication Guidelines
When publishing AIBQ-derived content on Morningstar platforms:
1. Use Morningstar terminology (moat rating, uncertainty, capital allocation) in external-facing text.
2. Reference AIBQ scores and sub-scores in the supporting analysis section.
3. Always cite the AIBQ version (v3.0) and effective date.
4. Quality Tier maps to the headline assessment; sub-scores provide the supporting evidence.
5. DAI-derived confidence bands should be disclosed when the underlying data is D1–D3 (high uncertainty).
---
*v3.0 — Effective May 26, 2026 \| Owner: Harrison Rolfes*


---

# 7. Version History

## v2.2 (superseded May 26, 2026 by v3.0)

# 🧮 AIBQ Scoring Rubric — v2.2 (Historical)

**Canonical rubric for AIBQ dimension scoring \| v2.0 Effective May 12, 2026 \| Supersedes v1.0 (Apr 15)**
## Purpose
Every score change is reproducible, auditable, and quantified. Two analysts looking at the same event arrive at the same magnitude. The rubric is the source of truth. Scores not derived from this rubric are not canonical.
## Principles
1. No Δ without math. Every score change shows its work.
2. Single-event caps. No one event moves a dimension more than 1.0 raw points.
3. Daily caps. No dimension moves more than 1.0 raw points per day.
4. Confidence tags. Every change tagged High / Medium / Low based on source tier.
5. NEXUS log required. Nothing becomes canonical until logged to the AIBQ/PBQ Daily Scores database.
6. Precision. Composites carry 0.01 precision. Dimensions carry 0.1 precision.
7. Carry-forward. Scores persist between events. No interpolation. No calendar-driven updates.
8. 24-hour cooling. Before external citation of any score change.
---
## Dimension Weights
| Dim | Weight | What it measures |
| --- | --- | --- |
| CE | 20% | Capital Efficiency — ARR per dollar of capital raised |
| RQ | 25% | Revenue Quality — durability, concentration, pricing power |
| CI | 15% | Compute Independence — dependency on hyperscalers |
| GO | 20% | Governance Optionality — board, regulatory, IPO readiness |
| MD | 20% | Moat Durability — technical lead, switching costs, talent density |
**Composite = (CE × 0.20) + (RQ × 0.25) + (CI × 0.15) + (GO × 0.20) + (MD × 0.20)**
---
## CE — Capital Efficiency (20%)
**Base metric:** ARR / Cumulative capital raised (secondary tenders excluded)
**Quintile anchors:**
| Ratio | Score |
| --- | --- |
| <0.1x | 1–2 |
| 0.1–0.2x | 3–4 |
| 0.2–0.3x | 5–6 |
| 0.3–0.5x | 7–8 |
| >0.5x | 9–10 |
**v2.1 AMENDMENT — FCF+ Maturity Override:**
If ALL of the following are true: (1) Company is confirmed FCF+ for trailing 12 months, (2) ARR growth \>40% YoY, (3) Gross margin \>70% — then CE FLOOR = 7.0 regardless of ratio quintile. The ratio-based score serves as the binding metric only for pre-FCF companies.
**Event adjustments:**
| Event | Raw Δ |
| --- | --- |
| Ratio crosses quintile boundary (up) | +1.0 |
| Ratio crosses quintile boundary (down) | −1.0 |
| FCF+ for 4 consecutive quarters confirmed | +0.5 |
| Major writedown / impairment | −0.3 to −0.5 |
| Capital raise that decreases ratio >0.1x | −0.5 |
| Cap: ±1.0 per event, ±1.0 per day |  |
---
## RQ — Revenue Quality (25%)
**Components:** NRR, enterprise %, \$1M+ ACV count, customer concentration, pricing power.
**Quintile anchors:**
| Profile | Score |
| --- | --- |
| Mostly consumer, <110% NRR, high concentration | 1–3 |
| Mixed revenue, 110–120% NRR | 4–5 |
| Enterprise-leaning, 120–130% NRR, diversified | 6–7 |
| Enterprise-dominant, >130% NRR, Fortune 500 penetration | 8–9 |
| Dominant enterprise, >140% NRR, Fortune 10 penetration, strong pricing power | 10 |
**Event adjustments:**
| Event | Raw Δ |
| --- | --- |
| \$1M+ ACV count doubles in <90 days | +0.5 |
| \$1M+ ACV count grows >20% in 30 days | +0.3 |
| NRR confirmed above 140% | +0.3 |
| Successful usage-based or price-up migration | +0.3 |
| Major customer publicly churns or down-shifts | −0.5 |
| Bookings/ARR gap widens >20% | −0.3 |
| Customer concentration: top 10 >40% of revenue | −0.3 |
| Cap: ±1.0 per event, ±1.0 per day |  |
---
## CI — Compute Independence (15%)
**Components:** Cloud partner diversity, own inference infrastructure, custom silicon, direct PPAs.
**Quintile anchors:**
| Profile | Score |
| --- | --- |
| Single cloud partner, no silicon, no PPAs | 1–2 |
| 2 cloud partners, no silicon | 3–4 |
| 3+ cloud partners, silicon in development | 5–6 |
| Multi-cloud + own inference racks + silicon taped out | 7–8 |
| Vertically integrated (own silicon in GA + own DCs + PPAs) | 9–10 |
**Event adjustments:**
| Event | Raw Δ |
| --- | --- |
| New cloud partner signed (>\$5B commitment) | +0.3 |
| Lost compute site / deal with >\$3B impact | −0.3 to −0.5 |
| Custom silicon taped out | +0.5 |
| Custom silicon GA (shipping) | +1.0 |
| Direct PPA signed for >500 MW | +0.3 |
| Sole dependency on one hyperscaler exposed | −0.5 |
| Cap: ±1.0 per event, ±1.0 per day |  |
---
## GO — Governance Optionality (20%)
**Components:** Board composition, cap table, corporate structure, regulatory relationships, IPO readiness, C-suite stability.
**Quintile anchors (NEW — v2.0):**
| Profile | Score |
| --- | --- |
| Single founder control, no board, no structure, active litigation | 1–2 |
| Minimal board, opaque cap table, structural issues, regulatory friction | 3–4 |
| Adequate board, clean structure, some regulatory risk, pre-IPO prep underway | 5–6 |
| Strong board, clean cap table, IPO-ready structure, minimal regulatory risk | 7–8 |
| Best-in-class board, clean governance, active IPO mandate, regulatory tailwinds | 9–10 |
**Event adjustments:**
| Event | Raw Δ |
| --- | --- |
| IPO-veteran board add | +0.3 |
| Domain-expert board add | +0.2 |
| Independent director add | +0.1 |
| Key board member exit | −0.3 |
| C-suite departure (CEO/CFO/COO) | −0.3 to −0.5 |
| Public CEO/CFO disagreement surfaced | −0.3 |
| Government contract confirmed | +0.2 to +0.4 |
| Regulatory lawsuit filed | −0.2 |
| Regulatory lawsuit lost (major) | −0.5 |
| Regulatory lawsuit won (major) | +0.5 |
| Banker mandate confirmed (IPO) | +0.3 |
| Tender offer at flat/lower price | −0.2 |
| Tender offer at up-round | +0.2 |
| Cap: ±1.0 per event, ±1.0 per day |  |
---
## MD — Moat Durability (20%)
**Components:** Technical lead, switching costs, talent density, data moat, category dominance.
**Quintile anchors (NEW — v2.0):**
| Profile | Score |
| --- | --- |
| No technical differentiation, commodity product, zero switching costs | 1–2 |
| Narrow technical lead, low switching costs, limited talent bench | 3–4 |
| Moderate technical lead, growing switching costs, solid talent | 5–6 |
| Strong benchmark leadership, high switching costs, deep talent, data moat forming | 7–8 |
| Category-defining benchmark dominance, very high switching costs, talent magnet, deep data moat | 9–10 |
**Event adjustments:**
| Event | Raw Δ |
| --- | --- |
| Flagship model leads key benchmark >5pp | +0.5 |
| Flagship model loses benchmark leadership | −0.5 |
| Category expansion into new moated vertical | +0.3 |
| Major enterprise win (Fortune 50 validated) | +0.2 |
| Major enterprise loss (public) | −0.3 |
| Senior researchers poached (≥3 in 30 days) | −0.5 |
| Senior researchers hired (≥3 from competitor in 30 days) | +0.5 |
| Product quality complaints surge (≥3 T2+ in week) | −0.1 to −0.3 |
| Safety-based restriction framed positively | +0.2 |
| Open source closes <10% on key benchmark | −0.3 |
| Cap: ±1.0 per event, ±1.0 per day |  |
---
## Scoring Protocol
1. Morning Digest identifies events from T1/T2 sources.
2. Apply rubric to each event; compute raw Δ per dimension.
3. Apply single-event and daily caps.
4. Sum weighted Δ; compute new composite (0.01 precision).
5. Tag confidence (High/Medium/Low).
6. Write AIBQ/PBQ Daily Scores DB entry with all dimensions, composite, events, and rubric citations.
7. Only after NEXUS log: publish in digest as canonical.
8. Before external publication: 24-hour cooling-off period.
## Review Cadence
Quarterly rubric review: Are quintile anchors still calibrated? New event types needed?
Annual recalibration: If all five companies drift uniformly, the rubric is miscalibrated.
Audit trail: Every Daily Scores DB entry preserved indefinitely.
---
---
## v2.2 Amendments — Company Archetype Modifiers (May 12, 2026)
The base rubric assumes a single company type. In practice, the Frontier Five span five distinct archetypes with structurally different risk profiles. These modifiers adjust CE and CI to reflect those differences. All other dimensions use the standard rubric.
### Company Archetypes
| Archetype | Company | CE Treatment | CI Treatment |
| --- | --- | --- | --- |
| FCF+ Platform | Databricks | Efficiency Index | Platform Modifier (+1.0) |
| Pre-FCF Trainer, Diverse Compute | Anthropic | Standard ratio | Standard quintile |
| Pre-FCF Trainer, Dominant Partner | OpenAI | Standard ratio | Standard quintile |
| Vertically Integrated Compute | xAI/SpaceXAI | Standard ratio + Infrastructure Credit | Standard quintile (already 9-10) |
| Pure Research Lab | SSI | Standard ratio | Standard quintile |
### Amendment 2.2a — CE Efficiency Index (FCF+ Companies)
**Trigger:** Company confirms trailing-twelve-month FCF+, ARR growth \>40% YoY, and gross margin \>70%.
**Replaces:** The ratio-based quintile score for that company only. Pre-FCF companies remain on the ratio metric.
**Formula:** CE = round((NormalizedGrowth × 0.4) + (FCFMargin × 0.3) + (GrossMargin × 0.3), 1) × 10
Where NormalizedGrowth = min(ARR_growth_pct / 100, 1.0), FCFMargin = FCF/Revenue (capped at 0.30), GrossMargin = gross_margin_pct / 100.
**Quintile mapping of index output:**
| Index | CE Score |
| --- | --- |
| < 0.20 | 3-4 |
| 0.20 - 0.35 | 5-6 |
| 0.35 - 0.50 | 7-8 |
| > 0.50 | 9-10 |
**Rationale:** The ARR/total-raised ratio penalizes companies for having history. A company that raised \$100M in 2013 to build Spark and now generates \$5.4B ARR from AI products should not be scored on that 2013 capital. The efficiency index measures current operating quality: growth rate, cash conversion, and unit economics. These are what public-market investors actually price.
**Worked example — Databricks (May 12, 2026):**
ARR growth 65%, FCF margin \~8%, Gross margin 80%.
Index = (0.65 × 0.4) + (0.08 × 0.3) + (0.80 × 0.3) = 0.26 + 0.024 + 0.24 = 0.524.
0.524 \> 0.50 → CE = 9.
Event adjustments still apply from this base.
### Amendment 2.2b — CI Platform Deployment Modifier
**Trigger:** Company's primary compute exposure is multi-cloud workload deployment, NOT frontier model training. Company does not train models \>100B parameters in-house.
**Modifier:** +1.0 to CI base score.
**Rationale:** The CI rubric was designed for companies whose business continuity depends on access to GPU clusters for model training. A platform company like Databricks deploys customer workloads across AWS, Azure, and GCP. Its switching cost between cloud providers is a sales motion, not an engineering rebuild. For a model trainer, losing cloud access means a six-month retraining cycle. This structural difference in compute risk justifies a modifier.
**Applies to:** Databricks (CI 6 + 1.0 = 7).
**Does not apply to:** Anthropic, OpenAI, xAI (all train frontier models), SSI (pre-product).
### Amendment 2.2c — CE Infrastructure Asset Credit
**Trigger:** Company owns physical compute infrastructure (data centers, GPU clusters) with confirmed third-party monetization (leases, hosting contracts) generating or contracted to generate \>\$500M annually.
**Modifier:** +1.0 to CE base score (applied after ratio quintile, before FCF+ override).
**Rationale:** The CE ratio metric treats all capital as consumed. For companies that converted capital into physical assets that generate recurring revenue (e.g., data center leases), the ratio understates efficiency because the denominator includes infrastructure investment that the numerator (software ARR) doesn't capture. The credit applies only when the infrastructure is actively monetized, not merely owned.
**Applies to:** xAI/SpaceXAI (Colossus 1 leased to Anthropic, Colossus 2 operational). CE moves from ratio-based 2 to 3.
**Does not apply to:** Companies without owned, monetized infrastructure.
### Amendment 2.2d — MD Market Share Erosion (Clarification)
The existing rule "market share loss \>5pp in trailing 90 days: -0.5" applies to any confirmed, T1-sourced market share data. For products with public usage metrics (ChatGPT web traffic, app downloads, API share), the erosion is applied on the date the data is published by a T1 source, not the date the erosion began.
**Applied correction — OpenAI (April 2026):** ChatGPT web traffic share fell from 86.7% to 64.5% per Similarweb/Jefferies analysis published in April 2026. This is a \>22pp decline. MD: -0.5 applied April 15 (approximate publication date). OpenAI MD moves from 6.0 to 5.5.
### Recalculated Scores with v2.2
| Company | CE | RQ | CI | GO | MD | Composite | Change |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Databricks | 9.0 | 9.3 | 7.0 | 8.7 | 10.0 | **8.92** | +0.55 |
| Anthropic | 8.0 | 9.5 | 5.1 | 7.3 | 9.3 | **8.06** | — |
| OpenAI | 3.0 | 5.0 | 4.5 | 4.3 | 5.5 | **4.48** | -0.10 |
| xAI/SpaceXAI | 3.0 | 4.3 | 9.0 | 2.5 | 3.8 | **4.28** | -0.20 |
| SSI | 1.0 | 1.0 | 3.0 | 5.0 | 2.0 | **2.30** | — |
---
*v2.2 — Effective May 12, 2026 \| Owner: Harrison Rolfes \| PBQ variant at separate rubric page*


## PBQ v1.0 (superseded)

# 🏢 PBQ Scoring Rubric — v1.0 (Historical)

**Private Business Quality Framework — Canonical Rubric \| Effective May 12, 2026**
PBQ is structurally identical to AIBQ with one substitution: Compute Independence (CI) is replaced by Strategic Velocity (SV) at the same 15% weight. PBQ applies to all private companies outside the Frontier Five AI cohort. CE, RQ, GO, and MD dimensions use the same quintile anchors and event adjustment tables as AIBQ Rubric v2.0.
**PBQ Composite = (CE × 0.20) + (RQ × 0.25) + (SV × 0.15) + (GO × 0.20) + (MD × 0.20)**
---
## SV — Strategic Velocity (15%)
**What it measures:** The speed at which a company converts capability into market position. Product cadence, geographic expansion, category creation, partnership velocity, and time-to-market relative to competitors.
**Why it replaces CI:** Compute Independence is specific to AI-native companies whose economics depend on GPU access and hyperscaler relationships. For non-AI private companies, the binding strategic question is not compute access but execution speed: how fast does the company ship, expand, and compound its market position?
### Quintile Anchors
| Profile | Score |
| --- | --- |
| No product shipped; pre-revenue; single geography; concept stage | 1-2 |
| Single product GA; one market; release cadence >6 months; no API/platform | 3-4 |
| 2-3 products GA; 2+ geographies; quarterly releases; API available; growing partner ecosystem | 5-6 |
| Platform play; 3+ geographies; monthly or continuous releases; 10+ API integrations; active M&A for capability gaps | 7-8 |
| Category-defining platform; global presence (5+ major markets); continuous deployment; ecosystem standard-setter; competitors build on your platform | 9-10 |
### Event Adjustments
| Event | Raw Δ |
| --- | --- |
| New product category launch (net new TAM) | +0.3 |
| New top-10 geography expansion (revenue-generating office or entity) | +0.2 |
| Strategic platform partner signed (>\$100M implied commitment) | +0.3 |
| Platform opens to third-party developers (public API/SDK launch) | +0.3 |
| Industry standard adopted built on company technology | +0.5 |
| Acquisition closes that fills a capability gap (<90 days from announcement to integration) | +0.3 |
| Acquisition closes but integration stalls (>180 days, no product integration) | -0.2 |
| Product deprecated, discontinued, or sunset | -0.3 |
| Competitor launches equivalent product <6 months after company | -0.2 |
| Product quality regression (public, impacting >1 week of users) | -0.3 |
| Market share loss >5pp in trailing 90 days (confirmed by T1 source) | -0.5 |
| Key product launch delayed >90 days past announced date | -0.3 |
| Cap: ±1.0 per event, ±1.0 per day |  |
### Scoring Guidance
SV is the most judgment-intensive dimension. Two principles keep it defensible:
1. **Ship dates over announcements.** A product is GA when customers can buy it, not when a press release says it exists. Score based on confirmed GA dates, not roadmap slides.
2. **Revenue-weighted geography.** Opening a WeWork in London is not geographic expansion. A revenue-generating entity with local customers, local contracts, and local support infrastructure is. Score based on commercial presence, not office count.
### Worked Examples
**Databricks SV (if scored under PBQ):** 3+ products GA (Lakehouse, Lakebase, Agent Bricks, Genie), 30+ offices globally, continuous releases, Unity Catalog becoming an ecosystem standard, 20K+ customers across 5+ major markets. Score: 8-9 range.
**Stripe SV (hypothetical):** Global payments platform in 40+ countries, continuous deployment, developer-first API ecosystem with thousands of integrations, category standard for online payments, active M&A (Bridge, Paystack). Score: 9-10 range.
**Figure AI SV (hypothetical):** Single product (humanoid robot) still in development, pre-revenue, single geography, no API or partner ecosystem. Score: 2-3 range.
---
## Shared Dimensions (CE, RQ, GO, MD)
All four shared dimensions use identical quintile anchors and event adjustment tables as AIBQ Rubric v2.0 (Canonical). See the AIBQ rubric page for full specifications.
**CE v2.1 Amendment applies to PBQ:** The FCF+ maturity override (floor = 7.0 if FCF+ 12 months, ARR growth \>40%, gross margin \>70%) applies identically in PBQ scoring.
---
## Protocol
Identical to AIBQ:
1. Identify events from T1/T2 sources
2. Apply rubric to each event; compute raw Δ per dimension
3. Apply single-event cap (±1.0) and daily cap (±1.0 per dimension)
4. Sum weighted Δ; compute new composite (0.01 precision)
5. Tag confidence (High/Medium/Low)
6. Log to NEXUS AIBQ/PBQ Daily Scores database with Framework = "PBQ"
7. Canonical only after NEXUS log. 24-hour cooling before external citation.
---
## When to Use AIBQ vs PBQ
| Criterion | AIBQ | PBQ |
| --- | --- | --- |
| Company type | Frontier Five AI companies | All other private companies |
| Dimension 3 | Compute Independence (CI) | Strategic Velocity (SV) |
| Weight | 15% | 15% |
| Use case | AI-specific infrastructure dependency | General execution speed |
| Current coverage | Anthropic, OpenAI, Databricks, xAI/SpaceX, SSI | Any company scored on request |
*v1.0 — Effective May 12, 2026 \| Owner: Harrison Rolfes*


## Changelog

# 📓 Changelog

## v3.0 (May 26, 2026) — Current
- **Architect:** Harrison Rolfes
- **Changes:** Full rebuild with 24 sub-score decomposition across 5 dimensions. Added three weight configurations (Report/Standard/Exit). Added Compounding Risk Adjustment (CRA). Added Data Availability Index (DAI) with confidence bands. Added Score Freshness decay. Added Distinct Pathway Test and Aggregate Event Cap for double-counting prevention. Added stage classification (S1–S5) with stage-gated CE metrics. Added sector classification with four-question AIBQ vs PBQ test. Added 6 AIBQ sector codes and 8 PBQ sector codes. Populated 110 events in Event Impact Matrix. Created Source Registry, Company Financials, and Benchmarks databases. Scored all 5 Frontier Five with full sub-score decomposition.
- **Breaking changes:** Sub-scores are new; v2.2 dimension-level scores carry forward but sub-scores are decomposed from them (not independently validated yet).
## v2.2 (May 12, 2026)
- Added Company Archetype Modifiers: CE Efficiency Index for FCF+ companies, CI Platform Deployment Modifier, CE Infrastructure Asset Credit, MD Market Share Erosion clarification.
- Recalculated all 5 FF scores with amendments applied.
## v2.1 (May 2026)
- CE FCF+ Maturity Override: floor = 7.0 when FCF+, ARR growth \>40%, gross margin \>70%.
## v2.0 (May 12, 2026)
- Full rubric formalization with quintile anchors, event adjustment tables, caps, and scoring protocol. First canonical version.
## v1.0 (March 4, 2026)
- Original framework published in "Ranking the AI Giants: A New Framework for the Frontier Five" (108 pages). Introduced AIBQ concept, five dimensions, and initial scoring.


---
*Mirrored from Notion 2026-08-11. Framework owner: Harrison Rolfes.*
