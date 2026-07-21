# Q2 2026 Global Unicorn Tracker - data still needed from the data team

Everything the report template requires that is NOT in the current working
dataset, or is present but materially incomplete. Compiled from the confirmed
GAPS objects plus discrepancy findings D-002 to D-022. Request everything
as-of 6/30/2026 to match the universe; market/trading series through the same
date. Each item names the sheet/exhibit it unblocks and the likely source.

## Tier 1 - Blocking (the exhibit cannot be built at all)

1. **PBQ / AIBQ quality scores - or the inputs to compute them.** Composite plus
   the five sub-scores (capital efficiency, revenue quality, compute
   independence / strategic velocity, governance optionality, moat durability)
   for at least the top ~25 by valuation. If scores are analyst-generated and
   not stored, request instead the underlying operating metrics: revenue / ARR,
   YoY growth, gross margin, net revenue retention, customer concentration, and
   FCF / burn. Unblocks: sheet 12, section 3.7 (the franchise's single most
   differentiating exhibit).

2. **Per-IPO post-listing daily price series.** Offer price, day-1 close, and
   daily close through quarter-end for every VC-backed IPO since 1/1/2025, plus
   the benchmark (Morningstar US Market Broad Growth Extended). Unblocks: sheets
   32 (Day 7/30/90/120 spreads), 33 (best/worst IPO), 27 (China AI IPO returns),
   and the SpaceX spotlight offer/day-1/current dot-pair. Sections 3.10, 3.11,
   3.6. Source: market data.

3. **Full Morningstar PitchBook index family through 6/30/2026.** Current index
   data stops 3/31/2026 and omits most series. Need daily levels to quarter-end
   for: US Unicorn, **Unicorn 30** (we only have Unicorn 20), Global Unicorn,
   US / Asia / Europe regional, all vertical indexes, and the public benchmarks
   (MM100 / US TME, Global TME). Unblocks: sheets 30, 31, section 3.11 - the
   correlation-inversion "validation test" cannot resolve without the 6/30 tail.

4. **Independent PitchBook valuation ESTIMATES, distinct from last-round marks,
   across the active universe.** Especially the 582 actives that carry no
   post-money mark (ByteDance, Ant Group, Stripe, Canva, and 578 others) and the
   marked-down set. This is the single biggest coverage hole: disclosed marks
   sum to $6,134B vs the published $8,232.5B, so $2,098B of aggregate value is
   currently un-decomposable. Unblocks: sheets 17, 18, 07, 03; sections 3.9 and
   3.4 (tested-vs-untested, estimate-vs-mark, the whole coverage-limits thesis).

## Tier 2 - Material coverage gaps (exhibit builds but understates / stays caveated)

5. **Cumulative equity capital raised since founding, per company**, for the top
   ~25 by valuation. Current equity figures cover 2016+ rounds only, which
   inflates capital-efficiency multiples (SpaceX reads 148x on $8.4B vs Q1's
   128.7x on ~$10B). Unblocks: sheets 10, 11 (D-021), section 3.5.

6. **Complete fallen-unicorn list with fall dates for all ~175 companies.** The
   Unicorn End Date field populates only 49 falls across 2021-2025; the curated
   fallen population is ~175. Need a fall date (and cause: markdown / shutdown /
   sub-$1B acquisition) for each. Unblocks: sheet 20 (D-012), section 3.9.

7. **The 17 missing Q2 2026 deals.** Row-level data yields 190 unicorn deals
   ($142.8B) vs the published 207 ($144.9B). Request the 17 missing records, or
   confirmation that 207 / $144.9B is the complete Q2 set. Sheet 08 (D-018).

8. **Investor-base metrics.** Total active unicorn-investor count (the analog to
   Q1's 4,144), median investors per round, and a nontraditional-investor
   classification flag (hedge fund / sovereign wealth / corporate / crossover).
   We currently have investor names on exits only, not counts or types. Section
   3.8.

9. **Secondary-market transaction data.** Volume and transaction count by
   quarter, plus bid/ask or implied-valuation spread. Present in the Monitor
   workbook but not in this working database - either load that extract or
   supply it. Sheet 29, section 3.10.

10. **LP fund cashflows.** VC-fund contributions, distributions, and net
    cashflow by year - the liquidity-pressure gauge behind the 2028-2031 forcing
    function. Not in any unicorn file; separate PitchBook fund-cashflow data.
    Sheet 29 (second half), section 3.10.

## Tier 3 - Data-quality reconciliations (resolve ambiguities the engine flagged)

11. **Identity of the 55-company gap** between the constituent list (1,688) and
    the published active count (1,743). D-002 / D-015.

12. **The $2,098B reconciliation** - the estimate values behind the difference
    between disclosed-marks total ($6,134B) and published aggregate ($8,232.5B).
    Same underlying ask as item 4, framed as a tie-out.

13. **Anthropic 5/28/2026 $965B round - deal type.** Confirm whether it is a
    primary priced round or a secondary / tender. It is corroborated by the
    Unicorn 20 file's $1,120.7B mark on 7/15/2026, so the $380B in the active
    list is stale; we need the deal type to decide whether $965B becomes the
    adjusted authoritative mark. D-019, sections 3.5 / 3.9.

14. **Primary-vs-secondary transaction flag on ALL deal records**, so
    tender/secondary prices do not contaminate round-based step-up and
    valuation-percentile analysis. Generalizes D-019. Sheets 13, 19.

15. **Latest authoritative mark + as-of date + primary/secondary flag, per top
    company** - a clean "current valuation" field, since the list, the top-10
    source sheet, and the deal history disagree for the frontier names.

16. **Vertical tags for the 64 untagged active unicorns.** D-011, sheet 05.

17. **Status of the 22 "active" unicorns carrying disclosed marks below $1B** -
    stale mark, or should-be-reclassified. D-016, sheet 20.

18. **True historical quarterly universe snapshots** (active roster + marks at
    each prior quarter-end). We are currently reconstructing point-in-time state
    via MAXIFS on round history, which carries survivorship bias; real snapshots
    would replace it. Unblocks the historical basis of sheets 01 (dormant row),
    07, 21, 22.

## Tier 4 - Enhancing (upgrades, not blockers)

19. **Founding dates for all active unicorns** (currently partial) - time-to-
    exit (25), value-creation-per-year (11), age analysis.

20. **Revenue / ARR and growth for the top 25** - revenue-multiple context and a
    second input path for PBQ.

21. **Lockup expiration dates for 2025-2026 IPOs**, SpaceX especially - the
    float / lockup mechanics promised in section 3.6.

22. **Down-round flags and down-round post-money across the universe** - the
    down-round-frequency metric (Q1 cited 4% of deal count). Section 3.8.

23. **SpaceX IPO mechanics** - final proceeds, float %, index-inclusion status,
    retail allocation - for the spotlight (mostly external / market data).

24. **Standardized round-series / stage labels (Seed / A / B / C / D+)** on every
    round; current labels required probing. Sheets 06, 13.

## Addendum - discovered in batches (d)-(e)

25. **Re-authenticate the workbook's PitchBook connection, or supply static
    exports, for the auth-gated (`#NOTAUTH`) fields.** Company names, acquirer
    names, and investor names/counts return `#NOTAUTH` in every source that
    carries them. Names/verticals/countries were rebuilt by PBID join, but
    acquirer names (sheets 26, 28) are unrecoverable and the M&A narrative needs
    them. This is an environment fix at source, not a per-quarter hand-repair.
    Tier 1/2. D-024, D-029.

26. **Clean re-exports fixing column-shift misalignment.** Two UNI LIST rows have
    PBIDs sitting in status fields; the VCE export's trailing columns are shifted
    +1 vs their headers (ticker actually at BX, price-per-share at CD). Corrected
    in-extract this quarter, but the source exports should be fixed. D-025,
    D-029.

27. **Estimate as-of dates.** The valuation-estimate DATE columns are `#REF!` /
    absent, so estimates cannot be aged - the 88%-above-mark reading has to stay
    a static cross-section. Supplying estimate dates would let us measure
    estimate staleness. Strengthens items 4 and 12. D-003.

28. **Reconcile the fourth active-count basis.** UNI LIST reports 1,738 actives
    (vs published 1,743, constituent-list 1,688, and exits-derived), and its
    per-company marks are the freshest in the workbook (it carries Anthropic at
    $965B). Confirm which basis is authoritative for current marks. D-027.

## Note on as-of alignment

Two cutoffs currently coexist: universe 6/30/2026, trading/index 3/31/2026. The
priority in this list is item 3 - pulling every market and index series forward
to 6/30/2026 - so the performance section shares the universe's as-of and the
report carries one consistent quarter-end.
