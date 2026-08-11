# Scale AI — NEXUS Intelligence Profile

**Coverage tier:** Extended Coverage (task-assigned; not Frontier Five). Bundle field `tier = "Extended Coverage"`. Note: NEXUS's own framework index flags an internal inconsistency here directly — Scale AI has an "AIBQ Profile" page under **AI Leaders** (#6-25 by valuation, standard 2x-weekly coverage) *and* a separate "AIBQ Score" leaf under **AI Ecosystem** (#26-100, biweekly, basic scorecard). Both pages agree on the score (3.70), so this is a tier-bucketing inconsistency rather than a data conflict, but it is carried here unresolved.

**PitchBook ID:** 163154-17 | **HQ:** San Francisco, CA (plus a Washington, DC government office) | **Founded:** 2016

**Generated:** 2026-08-11, from `bundles/scale-ai.json` plus both AIBQ v3.0 company deep-dive pages (`framework/companies/scale-ai-profile.md` and `scale-ai-score.md`) and surrounding framework/rubric documentation. Companion file: `scale-ai.json` (full structured data, including the complete raw event log and every conflict identified below).

**Embargo check:** This profile was built under the standing rule that the cross-company AIBQ/PBQ quality-vs-valuation correlation coefficient tracked elsewhere in NEXUS is never to be stated, implied, or charted. That figure was searched for across this company's bundle and every framework document reviewed for scoring context and was **not found** anywhere in the material gathered for Scale AI. Nothing below states or implies it, and no score-vs-valuation chart or fitted line appears in this profile or its companion JSON; the score section (b) and the valuation section (d) are written and sourced independently of one another.

---

## (a) Overview

Scale AI was founded in 2016 by a 19-year-old MIT dropout, Alexandr Wang, together with Lucy Guo, to sell human-powered data-labeling infrastructure for AI training — starting with autonomous-vehicle sensor data. It became the category leader in data labeling, RLHF, and model evaluation (its SEAL benchmarks) for frontier AI labs and the US government/defense sector. The business was destabilized through 2025-26 by Meta Platforms' $14.3B investment for a 49% non-voting stake, which pulled founder-CEO Alexandr Wang out of the company to become Meta's Chief AI Officer and — per the company's own internal notes — triggered customer defections among AI labs wary of a Meta-affiliated data vendor.

- **Leadership:** Francis deSouza, a Google Cloud executive, was named permanent CEO around 2026-07-30 (reaffirmed in coverage as late as 2026-08-10), ending an interim period under Jason Droege (CEO & CSO) that followed Wang's departure. See §i for the date conflict around exactly when Wang left.
- **Board:** the only board field on file still lists a single name, "Alexandr Wang" — stale, not updated for his departure or for Meta's 49% stake.
- **Headcount:** 1,000 per the current PitchBook-sourced pull (down from 1,200 in the prior pull) — see §i for a sharply conflicting ~5,800 estimate from other compiled sources.
- **Sector labels:** shown inconsistently as "AI Infrastructure," "AI-INFRA," and "Business/Productivity Software" / "Application Software" depending on which field is read.
- **Customers:** 500 reported, 85% enterprise mix — consistent with an enterprise/government-only business model (Scale does not otherwise report a consumer product).
- **Reported customer flight post-Meta-deal:** OpenAI and Google are both described as having cut ties; Microsoft and xAI are described as exploring alternative vendors. Google is separately noted to have pulled back a previously planned $200M 2025 spend.

## (b) Current scores

| Framework | Composite | Tier label | CE | RQ | CI / SV | GO | MD | Date | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| **AIBQ (canonical)** | **3.70** | Developing | 2.0 | 4.0 | 6.0 (CI) | 3.0 | 4.0 | 2026-05-13 | Medium |
| PBQ (alternate, non-canonical) | 6.25 | — | 3.0 | 8.0 | 7.0 (SV) | 6.0 | 7.0 | 2026-05-13 | High |
| Unlabeled framework (alternate, non-canonical) | 6.05 | — | 3.0 | 7.0 | — | 5.0 | 6.0 | 2026-05-13 | High |
| Stub entry | — (no composite recorded) | — | — | — | — | — | — | (undated) | Low |

CRA (Compounding Risk Adjustment) is stated as 0.00 on the profile page. The 3.70 AIBQ composite is the figure served by both of Scale AI's dedicated pages (Profile and Score) as fetched 2026-08-11. Under the rubric's carry-forward rule, this reading has apparently not moved since 2026-05-13. As with Perplexity, there is **no distinct prior score** on file — the shared 77-row AIBQ Score Tracker has zero entries for Scale AI (Frontier-Five-only coverage).

**Open score conflict:** mirrors Perplexity's pattern exactly. Two other rows exist, both dated the same day as the canonical entry (2026-05-13): a PBQ composite of 6.25 and an unlabeled-framework composite of 6.05, both materially higher than 3.70. Notably, Scale AI's own intel notes state plainly that it "does not train frontier models" and has "light compute needs relative to model trainers" — which arguably argues for PBQ classification under the framework's own four-question test — yet the persisted canonical score is the AIBQ read. Neither alternate reading has been adopted; both are preserved verbatim in the JSON.

## (c) Financials

*All figures dated 2026-08-11 unless noted; "prior" = the previous PitchBook pull on file.*

| Metric | Current | Prior |
|---|---|---|
| ARR | $2,000M | $2,000M |
| Gross margin | 50% | 48% |
| Headcount | 1,000 | 1,200 |
| Revenue growth YoY | 40% | 35% |
| Burn rate | $50M/mo | $40M/mo |
| Compute spend | $56.8M/yr | $50M/yr |
| Capital raised (cumulative) | $15,900M | $15,903M |
| NRR | 120% | 115% |
| Runway | 30 months | 24 months |
| Revenue per employee | $2,000K | $500K (internally inconsistent — see below) |
| NEXUS data-confidence score | 0.44 | 0.75 (sharply declining) |

The $2.0B ARR figure is stable across 113 of 115 tracked daily snapshots (98%) and is treated as the current anchor. **Multiple other revenue readings exist and are not adopted:** $760M (2023, Sacra-sourced), $1.5B (2024, Sacra, "97% YoY"), "ARR exceeds $1B" (verified, dated 2025-01-01), $4B (implied mid-2025, from a single low-tier source), and a **disputed $9.0B run-rate claim for December 2025** from the same single low-tier source (geekfence.com) — a figure inconsistent with both the PitchBook-anchored $2B and the qualitative customer-flight narrative reported elsewhere in this same bundle. It is not adopted here.

**Other flags:** "Prev Revenue per Employee" of $500K does not reconcile with "Prev ARR" ($2,000M) ÷ "Prev Headcount" (1,200) ≈ $1,667K — a roughly 3.3x internal mismatch, kept as-is. "Prev Valuation (USD B)" of 7.3 in the same record matches no other historical figure on file (nearest real marks are $13.8B in 2024 and $74.1B currently) and is flagged as unexplained.

## (d) Valuation & funding history

| Date | Round | Amount | Post-money | Lead |
|---|---|---|---|---|
| 2019-08-05 | Series C | $100M | $1.0B | Accel |
| 2021-04-13 | Series E | $325M | $7.3B | Tiger Global |
| 2023-05-23 | Growth round | $1,000M | $14.0B | Accel, Tiger Global |
| 2024-05-22 | Growth round (down round) | $1,000M | $13.8B | incl. Meta (strategic) |
| ~2025-06 (day-precision not on file) | Meta strategic investment | $14,300M | $74.1B | Meta Platforms (49% non-voting) |

The first four rows are PitchBook-sourced, analyst-verified event records. The 2025 Meta round — by far the largest and most consequential — is **not** a single dated master-event row in this bundle; it is reconstructed here from descriptive intel-note fields, and its exact day is not on file (see §i for a related date conflict on Wang's departure). It triggered Wang's move to Meta as Chief AI Officer and named Meta as Scale AI's preferred RLHF data partner, with preferred terms including data-supply agreements and right of first refusal on RLHF contracts.

**Disputed 2024 marks:** two unverified single-source claims — $29B (dated only to "2024," getlatka.com) and $25B (May 2024, techstackipo.com) — conflict with the verified $13.8B *down round* dated 2024-05-22. Neither is adopted.

**Current mark:** $74.1B is essentially undisputed as the current reading — 113 of 115 daily snapshots (98%); the only two exceptions are the first two days of tracking (2026-03-23/24), which show stale pre-refresh data matching the 2024 $13.8B mark.

**Unreconciled signal:** an intel note under "GO: IPO Signals" reads verbatim: *"Exploring tender offer/funding at $25B+ in 2026. IPO path unclear given Meta ownership structure."* The $25B+ figure sits well below the $74.1B headline post-money carried elsewhere in the same record. This could refer to a partial tender/secondary size rather than a full-company valuation, but that is not confirmed either way in the source — presented verbatim, not reconciled.

## (e) Cap table & investors

No dedicated cap-table database exists for Scale AI in NEXUS (0 matches in the shared cap-table registry); this section is built from narrative fields and round-by-round investor lists.

- **Board:** only "Alexandr Wang" is on file — stale (see §a, §i).
- **Meta stake:** 49% non-voting, ~$14.3B (2025), with strategic preferred terms (data-supply agreements, right of first refusal on RLHF contracts).
- **Named investors:** Meta, Accel (led multiple growth rounds), Index Ventures, Founders Fund, Coatue, Thrive Capital, Spark Capital, Tiger Global, and Y Combinator (seed).
- **Round-level leads:** see the funding table in §d.

## (f) Litigation & IP

**None on file.** No litigation or IP-dispute records exist for Scale AI anywhere in the tracked data — the company-specific litigation feed is empty, and the master 12-row litigation registry (which does carry a record for Perplexity) has zero rows mentioning Scale AI. The AIBQ profile page's "Litigation Ip" linked-view placeholder exists in the NEXUS UI but returned no extracted rows in this pull. Stated plainly rather than padded: this means NEXUS has not logged anything here, which is not the same claim as "no litigation exists in the real world" — only that none is present in the tracked data reviewed for this profile.

## (g) Active forecasts

No formal, dated forecast database rows exist for Scale AI anywhere in NEXUS (0 rows in both the bundle's own forecast slice and the 96-row shared forecasts registry). What is on file is qualitative:

- The unreconciled "$25B+ tender offer/funding" exploration signal for 2026 noted in §d.
- An explicit forward-risk framing in the intel notes: *"ARR trajectory may be declining in 2025-26 despite 2024 growth"* — tied to the customer-flight narrative, not a modeled number.
- A moat-risk forecast embedded in the competitive-position notes: core data-labeling is described as "increasingly commoditized by LLMs," with "LLMs approaching parity with human labelers for many tasks" flagged as an existential risk to the business.

## (h) Notable events

**44 dated event records were found** across the verified master-event feed (10 rows, all `Verified: YES`, PitchBook/company-sourced) and the broader timeline and talent-flow feeds (32 + 2 rows, all `Verified: NO`, press-sourced). Data quality on the 32-row timeline feed is markedly worse than Perplexity's: **24 of the 32 rows (75%) describe an entirely different company** — Nebius, D-Robotics, Anthropic's S-1, Character.ai, Bain/Google Cloud, Google's Gemini launch, Cathedral, EquiLibre, Cursor/xAI, Chai Discovery, Kalshi, Microsoft/Mistral, Etched (three near-duplicate rows), Cognizant/Anthropic, Wipro/Databricks, IFS, Saviynt, EY/SymphonyAI, Flyte/Volato, RAD Intel, Channelscaler, and a Supermicro/SpaceXAI data-center item — and were excluded below as source-tagging contamination, though every row is retained in the full JSON log. That leaves only 8 genuinely Scale-AI-specific rows in the entire 32-row timeline feed. Separately and worth flagging on its own: NEXUS's own 2026-06-22/23/24 morning digests self-identify a related conflation risk between Scale AI and an unaffiliated Santa Clara competitor called **Upscale AI**, explicitly noting *"the intelligence source conflates the two."* No Upscale-AI-titled row surfaced inside this company's 32-row feed, but the risk is noted here because it bears on how to read any Scale-AI-tagged item elsewhere in NEXUS.

Curated, in chronological order (this list is close to exhaustive of the genuine signal in the feed, given the contamination rate above):

- **2016** — Founded by Alexandr Wang (19, MIT dropout) and Lucy Guo; joins Y Combinator Summer 2016.
- **2019-08** — Series C, $100M at $1B (Accel) — youngest unicorn at the time; early customers Waymo, Lyft, OpenAI, Airbnb.
- **2021-04** — Ex-Amazon executive Jeff Wilke joins as advisor to the CEO. Series E, $325M at $7.3B (Tiger Global); Wang becomes (per source claim) the youngest self-made billionaire in history.
- **2022** — Wins major US Department of Defense data-labeling and evaluation contracts.
- **2023-05** — $1B raised at $14B post-money (Accel, Tiger Global); ~$500M ARR at the time.
- **2024-04** — Wang joins the US AI Safety Institute advisory board.
- **2024-05** — $1B raised including a Meta strategic stake, at $13.8B — a *down round* versus 2023.
- **2024-08** — Co-founder Lucy Guo departs; Wang consolidates as sole founder-leader.
- **2025-01** — ARR exceeds $1B; government/defense reaches ~40% of revenue.
- **~2025-06 / 2026-04 (disputed, see §i)** — Alexandr Wang departs for Meta as part of its $14.3B/49% investment.
- **2025-12 (disputed)** — Single-source claim of a $9B revenue run-rate.
- **2026-01** — Joelle Pineau (ex-VP AI Research, Meta FAIR) hired as Chief AI Officer.
- **2026-01** — UR AI Trainer (with Teradyne Robotics) launches at GTC 2026.
- **2026-07-30** — Francis deSouza (Google Cloud) named permanent CEO, ending the post-Wang leadership vacuum; independently reported by Bloomberg and Axios.
- **2026-08-10** — deSouza's CEO appointment reaffirmed in further coverage.

## (i) Open conflicts / disputes

1. **Score framework:** canonical AIBQ 3.70 (2026-05-13) vs. alternate PBQ 6.25 and unlabeled 6.05, both also dated 2026-05-13 — see §b.
2. **CEO / leadership chain:** Alexandr Wang (founder/CEO) → departure to Meta → Jason Droege (interim CEO & CSO, per a 2026-05-13 intel note) → Francis deSouza (permanent CEO from Google Cloud, appointed ~2026-07-30). The Board Composition field still lists only "Alexandr Wang" and has not been updated.
3. **Wang's departure date:** the talent-flow record (unverified) dates the move to Meta as **2026-04-01**; every other reference in the bundle (two separate intel notes, the legacy company row) describes it as **"June 2025."** A roughly 10-month discrepancy, not resolved — both dates are preserved.
4. **Headcount:** 1,000-1,200 (current PitchBook-sourced pulls) vs. **~5,800** in a separately compiled May-2026 estimate (Sacra/GetLatka/Contrary Research/Fueler.io/TLDL). Not reconciled; one speculative explanation offered in the JSON (different counting conventions — core FTEs vs. a broader contractor/labeling workforce) but not confirmed in source.
5. **Revenue level:** $2.0B (PitchBook-anchored, 98% of daily snapshots) vs. a single unverified $9.0B run-rate claim for December 2025 — see §c.
6. **2024 valuation:** verified $13.8B down round (2024-05-22) vs. two unverified single-source claims of $29B and $25B in the same year — see §d.
7. **NRR vs. customer-flight narrative:** quantitative NRR fields read 120-130%+ even in the same period that qualitative notes describe active defections by OpenAI and Google — a possible tension between a renewal-based metric and full logo/customer attrition, not resolved in source.
8. **Tier placement:** Scale AI carries both an "AI Leaders" profile page and an "AI Ecosystem" score page in NEXUS's own company index — flagged directly by the source extraction notes.
9. **"Scale AI" vs. "Upscale AI" conflation risk:** self-flagged by NEXUS's own morning digests as an open intelligence-tagging ambiguity with an unrelated competitor.
10. **IPO/tender signal:** a "$25B+" tender/funding exploration figure sits well below the $74.1B headline valuation in the same record — not reconciled.
11. **Prior-period valuation field:** "Prev Valuation (USD B)" = 7.3 matches no other historical figure on file.

## (j) Sources

**35 distinct source URLs across 29 distinct domains** were cited in the underlying event, timeline, and talent-flow records (this count includes the URLs behind the 24 contamination rows excluded from §h, since those URLs are real, just mis-tagged to this company — meaning genuine Scale-AI-specific sourcing is considerably thinner than the raw count implies). Most-cited domain: scale.com (10, company's own blog/site). No entry exists for scale.com in NEXUS's source-authority registry at all (0 rows) — unlike Perplexity, which carries a scored domain-authority record; this is itself a completeness gap worth noting. Full domain breakdown is in `scale-ai.json`.
