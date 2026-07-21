# AIBQ score inputs - every data point needed for the top 20 unicorns

The AIBQ (AI Business Quality) score adapts the PitchBook Business Quality (PBQ)
framework to frontier AI. Five weighted dimensions, each scored 1-10, composited
to a single 1-10. This is the complete input list to compute it for the top 20
unicorns (feeds report sheet 12 / section 3.7, currently gap-bound). For non-AI
names in the 20, dimension 3 (compute independence) is replaced with strategic
velocity.

## 0. Setup / identity
- Ranked top-20 list by latest post-money valuation
- AI vs non-AI flag per company (sets whether dim 3 = compute independence or
  strategic velocity)
- Peer/benchmark set for relative scoring
- Prior-quarter AIBQ scores (for the delta column)
- Per metric: source, as-of date, disclosed-vs-estimate flag

## 1. Capital efficiency - 20%
- Latest post-money valuation / enterprise value (mark, as-of, primary/secondary)
- Cumulative EQUITY capital raised since founding (equity-only denominator)
- Total debt raised (excluded from denominator; informs risk / compute indep.)
- Full round history: each round date, amount, pre/post
- Founding / first-round date
- Net cash (optional EV adjustment)

## 2. Revenue quality - 25%
- Revenue / ARR (annualized run-rate), as-of date
- Revenue history (multi-period) and YoY growth
- Net revenue retention (NRR); gross retention if available
- Gross margin: current level and multi-period trajectory
- Revenue mix: recurring/subscription vs usage/transactional vs services/licensing
- Customer concentration: revenue share of top customer and top 10
- Enterprise vs SMB/consumer mix
- Customer counts: total, and number of >$1M ACV accounts
- Contract structure: average length, committed vs on-demand

## 3a. Compute independence - 15% (AI companies)
- Third-party vs owned compute (% training/inference rented vs owned)
- Cloud-provider dependency and which hyperscaler(s)
- Committed compute spend / infrastructure obligations
- Owned compute assets: data centers, GPU fleet, custom silicon
- Strategic-investor entanglement with a compute provider
- Training-vs-inference infra split; multi-cloud vs single-provider
- Power/energy access and cost

## 3b. Strategic velocity - 15% (non-AI companies, replaces 3a)
- Product-release / shipping cadence
- New-market / geography expansion rate
- M&A / inorganic-expansion pace
- Observable proxies: capital efficiency, valuation trajectory, estimate
  integrity, investor composition

## 4. Governance optionality - 20%
- Corporate structure: C-corp / PBC / capped-profit / dual-class
- Founder voting control and super-voting share %
- Board composition: independent vs insider/investor seats
- Ownership concentration: founder %, largest-investor %, employee pool %
- Share-class structure (number and type)
- Investor rights: liquidation preferences, protective/control provisions
- Structural transitions underway
- Available exit paths and regulatory constraints on exit

## 5. Moat durability - 20%
- Market share / category leadership
- Competitive set: number and funding depth of rivals
- Switching costs / customer lock-in
- Network effects, data advantage, scale advantage
- Proprietary IP / patents / custom tech
- Brand and distribution advantage
- Barriers to entry / regulatory moat / licenses
- Differentiation vs commoditization risk

## 6. Scoring mechanics
- 1-10 rubric/anchors mapping raw metrics to each sub-score
- Weights: Capital efficiency 20% | Revenue quality 25% | Compute independence
  15% | Governance optionality 20% | Moat durability 20%
- Normalization method (percentile-within-peer-set vs absolute bands)
- Band definitions (score -> label)
- Composite = weighted sum of the five sub-scores

## Sourcing note
Dimension 1 and the valuation input are in the PitchBook data. Almost everything
in dimensions 2-5 is not: revenue/ARR, NRR, margins, customer concentration,
compute obligations, and governance structure come from company disclosures,
press, and analyst estimates; the 1-10 rubric is analyst-defined. This list is
the AIBQ portion of the data request (expands item 1 of the data-request list).
