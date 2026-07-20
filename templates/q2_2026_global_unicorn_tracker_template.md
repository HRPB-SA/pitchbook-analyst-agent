# Q2 2026 Global Unicorn Tracker - Report Template

Working template for the second edition of the quarterly Global Unicorn Tracker
(data as of June 30, 2026; publish ~early August 2026). Built from a full review
of two sources:

- **Q1 2026 Global Unicorn Tracker** (PitchBook Late-Stage Company Research,
  published May 5, 2026) - the franchise skeleton this template extends.
- **J.P. Morgan Innovation Economy Update, H2 2025** - a structurally different
  report whose best display devices (dashboard page, cohort survival curves,
  valuation percentile dot plots, practitioner commentary) fill gaps in the
  Q1 format.

---

## 1. What the review found

### What the Q1 tracker does well (keep)

1. **A thesis, not a data dump.** Every section prosecutes one argument: the
   aggregate headline conceals a bifurcated market (5 companies = 77.6% of deal
   value; 844 dormant unicorns; 51.2% of the universe untested since Q1 2024).
   The strongest recurring analytical assets are:
   - Concentration framing (top 5 / top 10 share of deal value; top 10 share of
     aggregate valuation vs the 18.4% 2023 trough).
   - The **dormant-universe ledger** (844 companies, 4.3-year-old marks, the
     $3.3T of unverified valuation inside the $8.6T headline).
   - **RVVC** (venture value created per dollar invested) paired with step-ups -
     a genuinely proprietary metric worth franchising.
   - **PBQ / AIBQ** quality-vs-valuation rank divergence (Databricks 5th by
     valuation, 1st by quality; OpenAI 2nd by valuation, 4th by quality).
   - Capital-efficiency ladder (SpaceX 128.7x → OpenAI 4.7x order-of-magnitude
     spread).
   - Fallen-unicorn accounting with vintage-stress logic (2021 cohort, 3x vs 2x
     scenario math).
   - Morningstar PitchBook index divergence (US Unicorn +22.7% vs MM100 −3.6%,
     correlation flip +0.95 → −0.63).
2. **Forward hooks.** Q1 explicitly set up claims that Q2 must resolve (see §4
   Scoreboard). This is the single best retention device in the report - honor it.
3. **Editorial voice.** "The 0.7% is calculated with a denominator that omits
   the stressor," "a list of the most expensive companies, not the best ones."
   Keep the register: skeptical of headline aggregates, explicit about data
   limitations.

### What the Q1 tracker lacks (fix in Q2)

1. **No single-page quantitative summary.** Key takeaways are prose-only; a
   reader cannot scan the quarter in 15 seconds.
2. **No cohort survival view of dormancy.** Q1 asserts the 844 number but never
   shows *how* dormancy accumulates by cohort over months-since-last-round.
3. **No valuation percentile distributions.** Q1 reports medians (step-up 2.2x,
   Series C median $150M) but never shows the 25th/75th/90th spread, which is
   where the bifurcation story actually lives.
4. **No named practitioner voice.** All narration is the research group's own.
5. **Prediction accountability is implicit.** Q1 made testable calls; Q2 needs a
   formal mechanism for grading them or the hooks lose value.

### What to borrow from the J.P. Morgan deck

| JPM device | Where it lands in Q2 |
|---|---|
| 8-tile KPI dashboard (p.4: dollars, deals, IPO proceeds, M&A, down rounds - 6-year bars, current period highlighted) | New "Quarter dashboard" page inside Quick stats |
| Capital-concentration tiers + power-law curve (p.11: top 5/10/25/50/75/100 share, 5-year dot progression) | Market leaders - replaces one-off treemap-only view with a comparable time series |
| Follow-on survival curves by cohort (p.19–20: % with no follow-on at 6/12/…/60 months, split early/late, AI vs non-AI, SF vs rest) | Dormancy Watch - turns the 844 into a curve, and tests "AI retains an edge" on unicorn data |
| Valuation percentile dot plots with Δ vs 2021 (p.18: Series A–D, 25/50/75/90th pct) | Deals and fundraising - shows round-size/valuation inflation beyond the median |
| Time-between-rounds box/whisker percentiles (p.13) | Deals and fundraising - replaces single-median "1.5yr → 1.0yr" line |
| IPO day-1 vs current price dot-pairs (p.25) | Exits/Performance - ideal display for the SpaceX/China-class aftermarket story |
| Named practitioner commentary pages (Roddy p.10, Kapur p.24) | One half-page "Desk view" sidebar per issue (ECM or LP secondaries desk) |
| Secondaries volume-vs-count divergence (p.27) | Liquidity subsection - Q1 noted only 40 secondary transactions; JPM's framing (dollars up, count down, buyer-seller spread) is the right lens |
| Contributions vs distributions net-cashflow bars (p.27) | The vertical divide / repricing section - quantifies the 2028–2031 fund-cycle forcing function Q1 argued verbally |

**Do not borrow:** JPM's slide-deck fragmentation (5 sections, 28 slides, no
through-argument). The tracker's long-form thesis structure is the better
container; borrow displays, not architecture.

---

## 2. Recommended Q2 structure

Contents (target 26–30 pp., mirroring Q1's pacing):

| # | Section | Pages | Status vs Q1 |
|---|---|---|---|
| 1 | Introduction | 1 | Recurring |
| 2 | Key takeaways | 1 | Recurring |
| 3 | **Scoreboard: grading last quarter's calls** | 1 | **NEW** |
| 4 | Quick stats + **Quarter dashboard** | 3 | Upgraded (dashboard page added) |
| 5 | Market leaders | 3 | Recurring (adds concentration-tier time series) |
| 6 | **Spotlight: The SpaceX listing - the repricing event the private market ordered** | 3 | **NEW - rotating spotlight slot** |
| 7 | PBQ update: from 6 scores to the ranked universe | 3 | Upgraded (Q1 promised the ~1,200-company expansion) |
| 8 | Deals and fundraising | 3 | Recurring (adds percentile dot plots, time-between-rounds distribution) |
| 9 | Valuations and fallen unicorns + **Dormancy Watch** | 3 | Upgraded (standing 844-cohort tracker) |
| 10 | Exits | 3 | Recurring |
| 11 | Performance | 3 | Recurring |
| 12 | The vertical divide | 2 | Recurring |
| 13 | Looking ahead / Q3 setup | 1 | Recurring (explicit hooks for next Scoreboard) |

Design rule: the **rotating spotlight** (slot 6) replaces "one-off deep dive
crowding out the franchise." Q1's spotlight was effectively the PBQ launch; Q2's
is the SpaceX IPO; Q3's is pre-committed to Anthropic's listing + the OpenAI
setup; Q4's to the first wave of the repricing cycle. PBQ graduates from
spotlight to a standing 3-page update.

---

## 3. Section-by-section specification

### 3.1 Introduction (1 pp.)

Purpose: reframe the edition-one thesis ("rarity has returned as concentration")
against the quarter's defining event. If SpaceX listed in June as targeted,
Q2 2026 is the first quarter since 2012 in which the world's most valuable
private company left the private market. Frame: *the tracker spent Q1 arguing
private marks were untested; Q2 is the first quarter with a real test score.*

### 3.2 Key takeaways (1 pp.)

8–10 bullets, same register as Q1. Each bullet must be a claim with a number,
not a statistic with a caption. Draft the takeaways LAST.

### 3.3 Scoreboard: grading last quarter's calls (1 pp.) - NEW

The accountability device. Table: **Call made in Q1 | What happened | Grade
(Right / Early / Wrong) | What it changes.** Calls to grade:

1. SpaceX June listing at ~$2T raising ~$75B; "if it holds through lockup, it
   clears the runway" for OpenAI/Anthropic. (S-1 filed April 1 per Q1.)
2. Anthropic Q3 listing (~$60B raise; ARR >$30B run rate) - on track / slipped.
3. OpenAI Q4 IPO at ~$1T - status of CEO/CFO operational-readiness tensions.
4. Step-up environment "slightly above historical norms" (2.2x median vs 1.9x
   2016–2018 baseline) - did Q2 hold?
5. Formation pace (95 new unicorns in Q1; 60 of them AI) - sustained?
6. 2022 vintage stress "should have begun showing" - did fallen-unicorn count
   accelerate beyond the 32 recorded in 2025?
7. Repricing "begins in earnest late 2027" - any early markdowns among the 29
   estimate-below-mark companies (Motional, SHEIN, Amber Group, Kalshi,
   Saronic, 9fin) worth updating?
8. Private-public divergence (Unicorn Index vs MM100 correlation −0.63) -
   converged via public recovery, private markdown, or widened?

Grading is the point: an Early or Wrong grade with a paragraph of why is worth
more than ten Rights.

### 3.4 Quick stats + Quarter dashboard (3 pp.)

- Page 1 - **Quarter dashboard (NEW, JPM p.4 pattern):** eight tiles, six
  periods each (2021–2025 annual + Q2 2026, current highlighted): unicorn deal
  value / deal count / exit value / exit count / new unicorns / fallen
  unicorns / median step-up / dormant share (%). Every tile answerable from
  data already produced for Q1.
- Page 2 - recurring quarterly exit + deal activity bars (identical spec to Q1
  pp.5, for QoQ comparability).
- Page 3 - recurring universe charts: count + aggregate valuation stack,
  country map, vertical treemap, deal value by series. **Change from Q1:**
  aggregate-valuation chart gains a shaded band for "valuation carried on marks
  >24 months old" so the $8.6T → $X.XT headline visibly decomposes into
  tested vs untested value. If SpaceX ($1.25T) exited the universe mid-quarter,
  annotate the discontinuity - the headline will FALL for composition reasons
  and the chart must preempt the misread.

### 3.5 Market leaders (3 pp.)

Recurring: quarterly deal-value treemap (top deals vs remainder), top-10
capital-efficiency ladder, value-creation-per-year rankings.

Additions:
- **Concentration-tier table (JPM p.11 pattern):** top 5/10/25/50 deal share of
  unicorn deal value, shown for 2021→Q2 2026 so the 77.6% Q1 reading gets a
  trend line, not a snapshot.
- Post-SpaceX top-10 recomposition: who enters the top 10 when a $1.25T name
  leaves; what that does to top-10 share (41.3% in Q1) purely mechanically.
  Q1's warning that "the aggregate tells us more about frontier AI fundraising
  cadence than about the market" gets its natural experiment.

### 3.6 Spotlight: The SpaceX listing (3 pp.) - rotating slot

The most interesting available topic for Q2 by a wide margin: it is the
resolution of Q1's central epistemological complaint (private marks are
untested prices). Structure:

1. **The event.** Pricing vs the $2T target and $1.25T last private mark;
   proceeds vs the $75B target vs Aramco's $29.4B record; allocation and float
   mechanics (Q1 explicitly promised coverage of index inclusion, retail
   ownership, float management - deliver it here).
2. **The test read.** Day-1 through quarter-end trading vs the three scenarios
   Q1 laid out (holds → runway cleared; breaks issue → IPO-class freeze).
   Display: JPM p.25 dot-pair chart (offer / day-1 / current) with the recent
   US IPO class (CoreWeave +175.4%, Figma −85.7%, Gemini Space Station −86.3%)
   as context rows.
3. **Transmission.** What it did to: the IPO queue (Anthropic/OpenAI timing),
   the Morningstar US Unicorn Index (SpaceX weight exits the private index -
   quantify the mechanical drag), xAI's mark inside SpaceX, and secondary
   bid/ask for the next tier ($10B+ names, JPM's "44 private companies above
   $10B" framing).
4. If the listing slipped: the spotlight inverts to "the market that blinked" -
   why, what the delay signals for the $150B 2026 pipeline, and what it does to
   the 2028–2031 forcing function. Either outcome carries three pages.

### 3.7 PBQ update (3 pp.)

Q1 promised: "approximately 1,200 of the 1,680 active unicorns have enough data
for scoring on at least four dimensions... The output will be a PBQ-ranked
universe provided alongside the existing valuation-ranked universe." Q2 must
ship a first cut or explain the slippage (Scoreboard discipline applies to
ourselves).

- Recurring: 6-company scorecard table + radar strip (Databricks 8.7, Anthropic
  7.7, SpaceX 7.5, OpenAI 4.2, xAI 3.8, SSI 2.3), updated for the quarter -
  note SpaceX/xAI consolidation treatment post-merger, and whether a listed
  SpaceX exits the frame.
- New: **top-25 PBQ league table** (rank by quality vs rank by valuation,
  divergence column), plus a distribution histogram of scores across the scored
  universe. The single most differentiating asset the franchise owns; the
  valuation-rank-vs-quality-rank divergence is the recurring exhibit investors
  will cite.
- Discipline: dimension-level sub-scores stay in the table; no score-vs-
  valuation scatter or fitted correlation (consistent with the standing
  embargo in this repo's Databricks work).

### 3.8 Deals and fundraising (3 pp.)

Recurring: annual deal value/count bars with Q2 2026 partial-year bar; stage
composition (Series D+ share of value, 67.8% in Q1); investor-base contraction
(4,144 active, 6.1 investors/round); nontraditional participation (41.3%).

Additions (both JPM patterns):
- **Valuation percentile dot plots by series** (25/50/75/90th, with Δ vs 2021):
  unicorn-round versions of JPM p.18. Q1's Series C median tripling ($60M →
  $150M) needs its distribution shown - if the 75th/90th moved but the 25th
  didn't, "pricing discipline has loosened" resolves into "the top of the
  market is paying up."
- **Time-between-rounds distribution** (25/50/75th pct, JPM p.13 pattern)
  rather than the single median (1.0yr in Q1). The Q1 hospital line ("half its
  patients had left without being discharged") becomes a chart: the median
  compresses while the 75th percentile stretches.
- Seed-check inflation tracker: Q1 flagged $20M median seed for
  unicorn-trajectory companies (vs $7.5M a year earlier) as a monitoring item -
  one small recurring panel.

### 3.9 Valuations and fallen unicorns + Dormancy Watch (3 pp.)

Recurring: top-10 share of aggregate valuation time series; PitchBook estimates
vs last-round marks (629 covered; 80.8% above / 14.6% flat / 4.6% below);
marked-down company table; RVVC + step-up pairing (1.38 vs 0.74 baseline);
fallen-unicorn count and vertical mix.

New standing feature - **Dormancy Watch:**
- **Cohort survival curves (JPM pp.19–20 pattern applied to unicorns):** % of
  each unicorn-round cohort (H1 2021 … H2 2025) with no subsequent round at
  6/12/18/…/60 months. This is the chart Q1's whole 844-company argument was
  missing - it shows whether dormancy is a 2021-cohort artifact or a structural
  steady state, and whether AI unicorns re-raise faster (JPM found AI follow-on
  rates ~20pts better; test it at the unicorn tier).
- The quarterly ledger: dormant count (844 → ?), share >3yrs stale (658 → ?),
  average mark age (4.3yrs → ?), plus flows - how many dormant companies
  returned to market this quarter, at what median step-up, vs how many fell.
  Q1 predicted returners "either accept repricing or compete for limited exit
  capacity"; the flow table is the test.
- Scenario refresh: the 10%/20% dormant-failure overlay on the fallen count
  (~260 / ~345 implied) and the $500B–$1T 2027+ net-reduction call, updated.

### 3.10 Exits (3 pp.)

Recurring: quarterly exit bars, exit value/count share by type, time-to-exit
medians, China AI IPO performance table (update Z.ai +569.2%, Biren, MiniMax,
Iluvatar through quarter-end - did the Hong Kong class hold?).

Q2 angles:
- Base-vs-megadeal decomposition, recurring: Q1 stripped xAI ($250B of $343.1B)
  to get $93.1B "genuine recovery"; apply identically (SpaceX IPO will dominate
  Q2's headline the way xAI dominated Q1's).
- Unicorn-on-unicorn M&A and the acqui-hire question: Q1 counted 11 of 169 M&A
  exits with VC-backed acquirers, all distressed; JPM shows AI startups
  acquired earlier (6yrs median) and more often (32% of M&A). Test whether
  strategic (non-distressed) unicorn consolidation has started - post-merger
  SpaceX/xAI is itself the biggest data point.
- **Secondaries panel (JPM p.27 pattern):** volume vs count divergence, plus
  contributions-vs-distributions net cashflow as the LP-pressure gauge behind
  the 2028–2031 forcing function. Q1 mentioned 40 lifetime secondary
  transactions; make the "liquidity market that does not exist" claim a chart.

### 3.11 Performance (3 pp.)

Recurring: Morningstar PitchBook index chart (US Unicorn, Unicorn 30, MM100);
correlation read; IPO performance-spread tables (Day 7/30/90/120 vs Broad
Growth Extended, global + US); best/worst IPO table.

Q2 questions, pre-loaded by Q1:
- Did the +0.95 → −0.63 correlation inversion resolve, and in which direction
  (public recovery vs private markdown)? Q1 called this "the validation test";
  answer it with the SpaceX print as the arbiter.
- Does the "SaaS-pocalypse" (public SaaS repriced as AI-displacement risk while
  private AI sets records) extend a second quarter? One panel: public SaaS
  index vs private SaaS unicorn marks.
- US vs non-US IPO spread: Q1's US Day-120 median of −41.85 (trailing 12m) vs
  the Hong Kong AI class is the sharpest geographic contrast in the dataset.

### 3.12 The vertical divide (2 pp.)

Recurring: vertical treemap (SaaS 914/$5.6T, AI&ML 761/$4.9T, overlap caveat),
net formation by vertical, AI share of aggregate value (47.6% in Q1 - crossing
50% is a likely Q2 headline; pre-build the chart annotation).

Q2 angle: concentration-within-vertical, recurring from Q1's best line -
"'Space tech allocation' is SpaceX allocation; 'AI allocation' is OpenAI and
Anthropic allocation." Small table: each top vertical's aggregate value, share
held by its single largest company. If SpaceX listed, space tech's $1.31T
collapses to ~$61B - the cleanest demonstration the tracker will ever get that
vertical aggregates are proxies for single names.

### 3.13 Looking ahead (1 pp.)

Explicit, gradeable Q3 calls (feeds the Q3 Scoreboard): Anthropic listing
window/size; OpenAI Q4 go/no-go signal; formation run-rate; dormant-count
trajectory; AI value share vs 50%; step-up median band. 5–8 one-line
predictions, each with a falsifiable threshold.

---

## 4. Standing production rules

1. **Chart comparability:** recurring exhibits keep identical spec (axes,
   period windows, source lines "Source: PitchBook • Geography: Global • As of
   June 30, 2026") so QoQ flips are readable. New exhibits get introduced once
   and then frozen.
2. **As-of discipline:** market-data cutoffs match Q1 conventions (universe
   data as of quarter-end; trading performance may use a later stamped date,
   e.g. "As of July 24, 2026," as Q1 did with April 24).
3. **Decompose every headline:** any record number gets its xAI-style
   strip-out in the same paragraph (Q1's $343.1B → $93.1B move). Q2's version
   is the SpaceX IPO inside exit/deal aggregates and the headline aggregate
   valuation drop when SpaceX leaves the universe.
4. **Denominator honesty:** wherever a rate excludes the stressed population
   (down-round %, impairment %, median time-between-rounds), say what the
   denominator omits - this was Q1's signature move; it is now house style.
5. **Voice:** skeptical of aggregates, precise about coverage limits, no
   hedging on graded calls. Practitioner "Desk view" sidebar is clearly
   attributed and boxed, JPM-style, and does not carry the argument.
6. **Repo conventions carry over:** no em-dashes in built artifacts; estimates
   labeled and dated; rumored/unclosed financings analyzed, never adopted into
   base figures.

---

## 5. Why this template (summary judgment)

The Q1 tracker is the right chassis: it is the only report of the pair with a
falsifiable through-thesis (concentration + untested marks + a scheduled
repricing), and Q2 happens to be the quarter its biggest prediction - the
SpaceX listing - resolves. The JPM deck contributes the missing display layer:
a scannable dashboard, cohort survival curves that turn the dormancy claim into
a picture, percentile distributions that reveal the bifurcation medians hide,
and the IPO dot-pair chart purpose-built for the quarter's main event. The
three structural additions - Scoreboard, rotating Spotlight, Dormancy Watch -
convert Q1's one-off forward hooks into a repeatable quarterly franchise.
