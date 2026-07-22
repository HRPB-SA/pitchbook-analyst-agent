# Q2 2026 findings - answers computed from the three datasets

Sources: Unicorn 20 valuations+pricing (model marks daily; used at the 6/30/2026
Q2 close, file extends to 7/15/2026);
Unicorn 20 pricing; Unicorn Monitor lighter (universe/verticals/indexes/
secondaries, to 6/30/2026). Universe figures on the MONITOR BASIS (1,556 active
/ $8,496.6B), which differs from the primary tracker basis (1,743 / $8,232.5B).

Three marks per top-20 name: MODEL (Unicorn 20 daily), ROUND (Monitor
last-round post-money ~6/22), SECONDARY (Monitor implied = price x shares). All
as of 6/30/2026.

Data caveats: SpaceX absent from Monitor history (IPO/exit); Cerebras round mark
missing (IPO'd Q2); Monitor UnicornRoundDate = unicorn-qualifying date, NOT
latest-round date, so it overstates mark staleness; vertical index returns are a
6/16/2023-6/30/2026 window; "departed" companies conflate exits and falls (this
file cannot separate them - needs the curated fallen list).

## Market overview (leaders)

**Fresh vs stale vs secondary (the centerpiece).** Across the 18 top-20 names
with a round mark, MODEL totals $2,935.8B vs ROUND $2,549.6B = **model sits +15.1%
above last-round marks** in aggregate. But the SECONDARY tape sits BELOW the
model for every megacap, and far below the two largest at the quarter-end close:
SpaceX -32%, Anthropic -22%, OpenAI -9%, Databricks -7%, Revolut -7%. Reads:
- Model is most bullish; secondary corroborates the direction but not the
  magnitude - the June 30 model caught SpaceX post-IPO and Anthropic at a fresh
  round, marking the two largest 22-32% richer than where shares actually trade.
- Up-round pressure confirmed mid-cap: SECONDARY above ROUND for Applied
  Intuition +37%, Anysphere +30%, Anduril +22%, Revolut +16%, Ramp +6%,
  Databricks +4%, Anthropic +3%.
- Repricing already visible bottom-tier: all three marks down vs round for Ripple
  (model -53% vs round), Epic Games (-38%), Kraken (-38%, secondary -50%), Figure
  AI (-13%), Perplexity (-13%), Deel (-16%).
- Neuralink is a re-rate outlier: model $52.3B / secondary $42.8B vs a $9.7B 2021
  round (model +439%) - the round is ancient, not the company cheap.

**Value creation / YTD 2026 (model marks).** The 20 sum to $5,019B. YTD spread is
enormous: Cerebras +600%, Neuralink +284%, Anthropic +261%, SpaceX +146%,
OpenAI +67%, Ramp +50% - against outright decliners Ripple -22%, Kraken -17%,
Rippling -14%, Canva -14%, Perplexity -12%, Deel -6%. (Perplexity's apparent
+752% was a corrupt-data artifact: a bad 1/1/2026 holiday row; true YTD -11.5%.) Value creation is concentrated:
Anthropic (inception index $4.0B -> $1,272.1B) and SpaceX ($75B -> $2,026B) alone
added over $3.2T of model value; mature names (Stripe $121B -> $169B, Applied
Intuition flat) barely moved. **Value creation splits by mechanism** (Unicorn 20
share-structure): appreciation-driven (near-stable share base) vs issuance-driven.
Anthropic grew on a 1.26x share base (per-share appreciation); SpaceX (+6.2x
shares at IPO) and Perplexity (+10x) grew via issuance - their per-share price
FELL (SpaceX -61% YTD) even as valuation rose. Only 2 of the 20 are
issuance-driven; 17 appreciation-driven; 1 decline (Epic Games). Appreciation is
the higher-quality signal.

**AI: one-third of count, nearly half of value.** AI is 27.6% of unicorn count
(430/1,556) but 48.8% of value ($4,143.7B/$8,496.6B). Within AI, OpenAI +
Anthropic alone = ~51% of AI value on model marks (44% on round marks) - "AI
exposure" is exposure to two cap tables.

## Verticals

**Size ranking (Monitor, 6/30, nonexclusive tags).** AI $4,143.7B (430 co) >
Enterprise SaaS $2,389.9B (457) > FinTech $901.7B (198) > E-Commerce $578.6B >
Mobility $492.6B > HealthTech $348.1B > Supply Chain $308.4B > Climate $234.1B >
Cybersecurity $207.4B > BioPharma $60.1B > AgTech $58.4B. Tag total 1,793 co /
$11,857B exceeds the universe (nonexclusive) - do not sum to a total.

**The return layer (index ANNUALIZED return, 6/16/2023-6/30/2026; source
publishes annualized, not cumulative).** AI +58.1% ann / +302.6% cum (the runaway
leader) > Enterprise SaaS +34.2% / +144.6% > Cybersecurity +22.2% / +83.9% >
E-Commerce +16.1% > HealthTech +14.4% > BioPharma +13.3% > FinTech +12.9% >
Mobility +11.4% > Climate +8.7% > Supply Chain +8.5% > AgTech +5.9%. Benchmark
Global TME +19.6% ann / +72.4% cum. THREE verticals beat the public benchmark (AI,
SaaS, Cybersecurity); AI compounded at ~3.0x the public annualized rate. The rest
are large-ish but below benchmark. Size-vs-performance quadrant: AI and SaaS are
big AND compounding; FinTech is the third-largest vertical but a below-benchmark
laggard (+12.9%). Correction note: an earlier read treated the published vertical
returns as cumulative and the benchmark as a shorter window; verifying against the
index levels showed all figures are annualized on the same window, which raised
the AI/TME ratio to ~3.0x and the beat-count to three.

**AI as engine and risk.** AI is simultaneously the largest vertical, the
best-performing (+58%), and the highest-formation (60+ of recent new unicorns) -
the single name for both the growth case and the concentration risk.

**2021 vintage / 2028 outlook.** 618 unicorns minted in 2021 (matches published
formation; peak year, next-highest 195). Four+ years on, 465 remain active (75.2%);
153 have departed (still-private rate - includes exits, not only falls).
The 465 survivors carry marks largely set in the boom and now face 2028-2031
fund-cycle resolution.

## PBQ and valuations (top 20 = Unicorn 20 constituents)

**Why the table isn't a quality ranking.** Ranked by model valuation: SpaceX
$2,026B, Anthropic $1,272B, OpenAI $861B, Stripe $169B, Databricks $149B,
Revolut $94B, Anduril $77B... This is a most-expensive list. Full PBQ needs
invested-capital and operating metrics not in these files (-> data request);
what IS computable here is the estimate-integrity input.

**Estimate integrity from the three marks.** Names where MODEL, ROUND, and
SECONDARY agree tightly (Canva 0/0%, Stripe within 6%, Rippling within 5%) have
high mark reliability; names where they diverge widely (Neuralink +439%, Ripple
-51%, Kraken, with secondary far off) have low mark
reliability - a governance/valuation-quality flag. The megacaps sit in between:
model bullish, secondary 7-32% lower (widest at SpaceX and Anthropic).

## Valuations and fallen unicorns

**Where the value sits (top-10 share, Monitor basis).** 49.8% (2014) -> steady
de-concentration to an 18.3% trough in 2023 (the broad-based era) -> sharp
reconcentration to 26.2% (2025) and 47.8% (Q2 2026). Value has re-concentrated in
the megacaps to roughly its 2014 level.

**Latest valuation.** Aggregate $8,496.6B, up from $6,654B (Q4 2025) - but much of
the jump is the top 10 ($1,459B -> $4,058B), i.e. megacap mark appreciation and
composition, not broad-based gains. The middle 1,546 companies moved far less.

**Coverage gap.** 78.5% of current actives carry a unicorn-qualifying date >24
months old (71.9% >36 months) - a staleness proxy (overstated, since the field
is the qualifying date, not the latest round). Universe churn: 2,431 companies
ever reached the index, 1,556 remain, 875 have departed.

**Fallen / attrition.** This file cannot separate fallen from exited - 875 total
departures over 2014-2026 conflate both. The 2021 vintage alone accounts for 153
departures. A proper fallen count needs the curated list (primary tracker).
Formation trajectory for context: 2021 peak 618 -> 2023-24 trough 123 each ->
2025 recovery 179 -> 2026 H1 107 (annualizing ~214).

**Note on step-ups / RVVC.** Not computable here (no deal-level capital amounts);
these live in the primary tracker.
