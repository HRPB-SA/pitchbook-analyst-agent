# OpenEvidence — NEXUS Intelligence Profile

**Coverage tier:** Extended Coverage (not Frontier Five) · Internal labels seen in source data: "T3-Ecosystem" / "Tier 3 — Specialists"
**PitchBook ID:** 512765-92 · **Sector:** AI Applications (PitchBook industry: Decision/Risk Analysis) · **Verticals:** AI/ML, HealthTech, Life Sciences, Mobile
**As of:** 2026-08-11 · **Companion data file:** `openevidence.json` (full event log, all computed fields)

> **Embargo note:** This profile does not compute, state, or imply any cross-company quality-vs-valuation relationship. Score and valuation figures are reported in separate sections and are not cross-referenced against each other.

> **Data-quality headline, read this before the rest of the profile:** of the 154 dated events found in OpenEvidence's raw timeline, **34 (≈22%) describe events about other companies**, not OpenEvidence — see section (h) for the full breakdown. This profile excludes those from the curated list and from every substantive section below, but retains all 154 rows (each tagged) in the companion JSON, per instruction to never drop a data point silently.

---

## (a) Overview

OpenEvidence was founded in 2022 to build AI-powered clinical decision support for physicians, built on custom domain-specific models trained on peer-reviewed medical literature, with a mission to give every physician an AI-powered research assistant. Two items in this Overview are conflicts significant enough that they belong here rather than only in section (i):

**Founder name conflict.** The one Verified master-events record for the founding is titled *"OpenEvidence founded — Eran Segal and team"* — but its own description text never actually names a founder, only the mission and Cambridge HQ. Separately, the canonical registry's Leadership Team field says **"Daniel Nadler - CEO and Cofounder,"** and an independent (unverified) dated event states plainly: "OpenEvidence was founded in 2022 by Daniel Nadler." Two named founders, not reconciled. Daniel Nadler is corroborated by two independent records; Eran Segal appears only in a title with no supporting body text.

**Headquarters conflict.** The canonical registry (both the legacy company row and the v2 company registry) lists HQ as **Cambridge, MA**. But both dated AIBQ score-tracker records instead say **Miami, United States**. Two dated events corroborate a relocation: "OpenEvidence Closes $250M Series D, Moves HQ from Cambridge to Miami" (~January 2026) and "OpenEvidence establishes Miami as strategic headquarters" (~May 2026). It reads as though a relocation happened and the score tracker picked it up while the primary company registry record did not. Not resolved in source data — both HQs are reported.

**Leadership-field data contamination.** The registry's "Key Departures (90d)" field for OpenEvidence lists **"Marc Winterhoff (interim CEO)"** and **"Peter Rawlinson (CEO)"**; "Key Hires (90d)" lists **"Napoli (CEO)."** These are not OpenEvidence people — they are **Lucid Motors** executives. Six of the eight dated events tagged Category=Leadership in OpenEvidence's own timeline are explicitly about Lucid Motors' CEO transition (Rawlinson's February 2025 resignation, Winterhoff's interim tenure, Silvio Napoli's April 2026 appointment), plus two more about Qualtrics and Hume AI leadership changes — none about OpenEvidence. No other record anywhere in the bundle corroborates a CEO change at OpenEvidence; Daniel Nadler is otherwise the consistently-named CEO. This is treated as a data-pipeline mis-attribution, not a real OpenEvidence event, and is the clearest single instance of the broader "Open*" name-collision problem described in section (h).

**Product line:** AI-powered medical search and evidence-based clinical decision support; EHR integrations (Epic, at Mount Sinai and other systems); guideline-integration partnerships with medical societies (NCCN oncology, AAO-HNSF, AUA urology, ACOG ob-gyn, GINA asthma, Society of Surgical Oncology/ASCO); content-licensing partnerships (Wiley, Springer Nature); an accredited continuing-education/MOC platform; and a physician billing-capture tool ("Coding Intelligence," ~March 2026).

**Business model:** described in source data as both (i) free for individual verified physicians with enterprise hospital contracts of $50K–$200K+/yr, and (ii) an ad-funded model carrying pharmaceutical advertising with CPMs reported in the $70–150+ range. Both descriptions appear; they are not necessarily contradictory (a freemium-plus-enterprise-plus-advertising blend is plausible) but are not reconciled into one clean model in source data.

**Adoption scale (2026):** reported at 40%+ of US physicians using the platform (multiple sources agree on this figure); monthly consultation volume is given as **~15 million** by one source and **~20 million** by another — not reconciled.

Regulatory exposure is flagged in the canonical registry as the **EU Artificial Intelligence Act** — directly consistent with a dated withdrawal-from-Europe event covered in section (f).

---

## (b) Current scores

### Canonical current AIBQ score

| Composite | Rating | As of | Confidence | Valuation rank at time |
|---|---|---|---|---|
| **3.80** | Developing | **2026-05-12** | Low | 18 |

**Sub-scores:** CE 3.0 · RQ 4.0 · CI 4.0 · GO 4.0 · MD 4.0

**Rationale (verbatim):** "CE3: limited financial data. RQ4: healthcare AI, potentially sticky but early. CI4: uses LLM infrastructure. GO4: limited public governance data. MD4: medical AI specialized but competitive market."

This cross-checks exactly against the standalone AIBQ score card (`extract/framework/companies/openevidence.md`: "OpenEvidence: AIBQ 3.80 (Developing)," same five sub-scores) and is treated as the corroborated canonical current score.

**Prior score:** None found. No earlier-dated AIBQ-labeled composite exists in the bundle — 2026-05-12 is the only fully-tagged record.

### Other dated composite — not reconciled with the canonical score

| Date | Framework | Composite | Confidence | Sub-scores |
|---|---|---|---|---|
| 2026-05-13 | *(not stated)* | 5.5 | Medium | CE 4 · RQ 5 · GO 5 · MD 5 · CI n/a |

This record omits Framework, PBID, HQ, Industry, and Rationale — the same thinly-populated pattern seen for ElevenLabs' 2026-05-13 record, suggesting a possible systemic batch artifact affecting multiple companies that day rather than something specific to OpenEvidence. It is ~45% higher than the canonical 3.80 print with no stated rationale. Not presented as the current score; logged as an open conflict.

Unlike ElevenLabs, no PBQ-framework record exists for OpenEvidence in this bundle, and `aibq_unicorn_intel` (which supplied extra competitor narrative for ElevenLabs) is empty here — no additional switching-cost or competitor detail beyond the rationale above.

---

## (c) Financials

### Canonical current snapshot (2026-08-11)

| Metric | Value | Prior |
|---|---|---|
| ARR | $30M *(see wide dispute below)* | $15M |
| Revenue growth YoY | 1% *(see conflict below)* | 1.5% |
| Gross margin | 70% | 68% |
| Gross profit | $21M | $10.2M |
| NRR | 140% | 130% |
| Headcount | 50 | 30 |
| Burn rate | $5M/mo | $4M/mo |
| Compute spend | $5M/yr | $3M/yr |
| Runway | 36 months | 24 months |
| Customers | 800,000 | 700,000 |
| Enterprise mix | 80% | 70% |
| Customer concentration | 20% | — |
| Revenue/employee | $600K | $400K |
| Implied ARR multiple | 133.33x *(does not reconcile — see below)* | 120x |
| Total capital raised | $100M *(see wide dispute below)* | $90M |
| Profitability | "Profitable" *(but see conflict below)* | — |

**Implied ARR multiple does not check out.** The registry's own $12B valuation ÷ $30M ARR = 400x — not the 133.33x stated in the same row. 133.33x would require either a ~$4B valuation or a ~$90M ARR base, and neither matches this row's own fields. A separate same-vintage record (`aibq_company_comparisons`) independently states **"Valuation / ARR (Multiple)": 400** — consistent with the 400x arithmetic, not with the registry's own 133.33x field. Contrast with ElevenLabs, whose equivalent field is internally consistent.

**Profitability status conflict.** The legacy registry field says **"Profitable."** The same-vintage `aibq_company_comparisons` record says **"Burning — Controlled."** Both dated 2026-08-11 / current. Not resolved.

**Revenue growth rate is very likely mis-scaled.** The registry's "Revenue Growth YoY %" field reads 1% (prior 1.5%) — but the **same record's own** Prev ARR ($15M) to current ARR ($30M) is a 100% increase. A separate same-day record (`aibq_company_comparisons`) independently states **"ARR Growth YoY %": 100** — consistent with the doubling, and two orders of magnitude apart from the registry's own 1% field.

### ARR ladder — every dated figure found (wide and unresolved)

| Date | ARR reported | Source / tier |
|---|---|---|
| 2025-01-01 | $30M | Verified — "hospital system enterprise contracts" |
| 2025-01-01 | $50M | Google News harvester row, unverified — "lean team of 83 employees" (a third, uncorroborated headcount figure) |
| Jan 2026 (cluster of ~5 convergent articles) | $100M | iatrox.com, rdworldonline.com and others, unverified but convergent — attributed to pharmaceutical-advertising revenue |
| 2026-07-25 | $150M | Forbes (Garth Friesen), unverified — attributed mainly to pharma/medical-device advertisers |
| 2026-08-11 (canonical) | **$30M** | PitchBook-linked registry — **unchanged since the Jan-2025 verified print**, sitting well below the $50M/$100M/$150M press figures across 2025–2026 |

**Total capital raised is similarly disputed.** Canonical registry: $100M. Yet multiple dated press events report far higher cumulative totals: "$700M in total capital" (January 2026, two independent sources), "$795.4M in total funding" (CNBC Disruptor 50, May 2026), "~$750M raised" (rdworldonline.com, January 2026). The $100M figure appears to track only the priced institutional rounds the registry counts (seed $15M + Series A $75M + roughly $10M other ≈ $100M), while the $700M+ figures likely fold in the disputed/duplicate $200M item and the 2026 $250M round on a different base. Not reconciled.

No credible independent headcount data point exists beyond the canonical 50 (current) / 30 (prior) — the one "headcount" event in the raw timeline ("500 employees") is confirmed contamination from an unrelated company (see section h).

---

## (d) Valuation & funding history

### Confirmed primary rounds

| Round | Date | Amount | Lead | Post-money | Verified |
|---|---|---|---|---|---|
| Seed | 2023-05-01 | $15M | a16z | not stated | Yes |
| Series A | 2024-01-01 | $75M | a16z | not stated in verified record | Yes |
| "Series D" per press *(naming conflict, see below)* | ~Jan 2025 (per pymnts.com: "third funding round in under a year") | $250M | not specified | not stated | No |
| Series B | 2025-07-01 | $210M | not specified | $3.5B | No |
| "Series D" (2026, most-cited label) | January 2026 (multiple convergent sources) | $250M | DST Global, Thrive Capital, + "5 other investors" per one Tracxn-sourced article | $12B | No — but ~6 independent outlets converge on $250M/$12B |

**Funding-round naming is a genuine conflict, not just press sloppiness.** The registry's own **"Last Funding Round" field says "Series C,"** while most 2026 press calls the same/most-recent round "Series D." A 2025 event (the $250M round above) is *also* called "Series D" by pymnts.com despite arriving barely a year after the Series A — with no "Series B" or "Series C" named yet at that point in the press record (Series B doesn't appear in this data until July 2025, priced lower at $3.5B). The naming does not sequence cleanly in either direction; reported as found, not resolved.

### Disputed or low-confidence rounds (excluded from the confirmed table above, not from this report)

| Claim | Dates seen | Source | Why it's disputed |
|---|---|---|---|
| $200M raised at $6B valuation "in October" | 2023-10-31 *(Year field: 2023)* and again referenced as "October of the same year" inside a 2024-03-31 record | findskill.ai (single low-tier blog, same claim twice with drifting year) | A $6B mark in Oct 2023 or Oct 2024 doesn't sequence against the verified $75M Series A (Jan 2024) or the $210M Series B priced at just $3.5B (July 2025) — a $6B valuation should not precede a later $3.5B one. Also conflicts with the Series B record's own "$300M total capital raised since founding" claim. |
| "$100M at $1B valuation, Series A, led by Sequoia Capital" | 2026-05-18 (two duplicate records) | causeartist.com | Directly conflicts with the already-established $75M/a16z Series A (2024) and the contemporaneous $12B valuation already reported by January 2026. Very likely a garbled or conflated article. |
| $200M raise considered at $20B valuation | 2026-07-19 / 2026-07-20 | pymnts.com, medicalbuyer.co.in | Explicitly reported as **under consideration**, and per the second source "unlikely to proceed... partly due to dilution concerns for founders and shareholders." Not a closed round — treated as a forward signal only. |

**Investor-name data-quality flag.** One Tracxn-sourced article (2026-01-21) states the $250M round was "led by DST Global, Thrive Capital, **Delta Sigma Theta** and 5 other investors." Delta Sigma Theta is a historically Black sorority, not a venture investor — almost certainly a scraping/parsing artifact (possibly a garbled expansion near the "DST" abbreviation). Reported verbatim rather than silently dropped; not treated as a real investor.

### Valuation ladder

| Date | Valuation | Basis |
|---|---|---|
| ~2024 | ~$1B | Per several 2026 retrospective articles citing "up from $1B a year prior" |
| 2025-07-01 | $3.5B | Series B post-money |
| 2025-10-20 | $6B | Target/reached valuation, 90-day-ahead framing (Tracxn) |
| Jan 2026 (most-cited) | $12B | "Series D" post-money — best-attested current figure |
| 2026-06-21 to 2026-07-09 | $13B *(≈3-week window)* | Daily tracker shows $13B instead of $12B for this window, then reverts. No narrative event corroborates it — the same $12B↔$13B wobble pattern also appears (as a one-day event) in ElevenLabs' tracker, suggesting a possible shared ingestion quirk rather than two unrelated coincidences |
| 2026-07-19/20 | $20B *(unclosed consideration only)* | Reportedly not proceeded with — see disputed rounds above |

---

## (e) Cap table & investors

No structured cap table is present (no ownership percentages, share classes, or option-pool detail). List compiled from funding-round and investor-rights text fields only.

**Named investors:** Andreessen Horowitz/a16z (Seed + Series A lead; board seat + lead rights) · GV/Google Ventures (per Strategic Investor Stakes field) · DST Global, Thrive Capital (per the Jan-2026 round coverage — see the "Delta Sigma Theta" artifact above from the same source) · Sequoia Capital, NVIDIA, Kleiner Perkins, Blackstone, Mayo Clinic (per a single iatrox.com blog post describing the ~$700M cumulative funding base — **not independently corroborated elsewhere in this bundle**; Mayo Clinic and Blackstone as direct investors are notable, unusual claims worth treating cautiously given the single-source sourcing).

**Investor rights (verbatim):** "a16z: board seat and Series A lead rights. Standard preferred liquidation preference. HIPAA compliance built into investment terms. Series B expected 2026 — likely a16z led."

**Board:** Board Composition field is null/not populated.

---

## (f) Litigation & IP

No structured litigation/IP tracker data exists. Ten Legal/Regulatory-category dated events were found; **two are excluded here as unrelated to OpenEvidence** (an EU e-Evidence cross-border data-request regulation, flagged as a probable "Evidence" name-collision, and a UK FCA "Open Finance" framework item, flagged as an "Open" name-collision — both retained with flags in the JSON).

| Date | Item | Detail |
|---|---|---|
| Late April 2026 *(5 near-duplicate reports across independent outlets converge on 2026-04-28/30)* | **OpenEvidence withdraws from the European Union and United Kingdom** | Cited reason across all five: regulatory uncertainty / difficulty meeting the EU AI Act's requirements for a system that may be classified high-risk. One source (a competitor's blog) states the exit happened "without announcing a replacement or providing a UK handoff plan." Signal: Negative in the harvester-sourced duplicates. |

This is a materially significant, negative strategic event — a geographic contraction — and the five-outlet convergence around the same week gives it reasonably high confidence despite no Verified=Yes tag.

The registry's Regulatory Exposure field ("EU Artificial Intelligence Act") is directly consistent with this withdrawal.

---

## (g) Active forecasts

**Not present.** `shared_forecasts` is empty for OpenEvidence in this bundle — no dated analyst forecast rows to report.

---

## (h) Notable events

**154 dated events** were found in the full timeline (from 822 raw rows seen before date-filtering). 7 of the 154 carry a Verified=Yes tag; the remaining 147 are harvested/unverified.

### The headline data-quality finding

**34 of 154 dated rows (≈22%) describe events about companies other than OpenEvidence.** This is overwhelmingly explained by substring/name-collision matching on companies whose names start with **"Open"** — OpenAI, OpenText, OpenObserve, OpenPolicy, Open Systems, and the UK's "Open Finance" banking framework — plus a separate cluster of generic CEO-transition harvester rows (Lucid Motors, Qualtrics, Hume AI, Napco Security Technologies) that appear to have been mis-attributed to OpenEvidence upstream. The clearest single proof point: one "Financial Milestone"-category row reads verbatim *"Open Systems had 500 employees as of March 2026"* — Open Systems being an unrelated managed-security/SD-WAN company — yet it was extracted under the title "Headcount decreased to 500 employees" with no company name in the title to signal the mismatch.

**Provenance.** Per `consolidate.py` (the bundle-build script), the shared cross-company reference databases (v2_master_events, the aibq_* tables, canon_*) are filtered by an explicit Company-name column match and come back clean — no contamination was found there. The raw per-company timeline file, by contrast, is loaded with **no company-name filter at all**, only a "has a date" + de-duplicate-by-URL pass. This means the contamination was already present in the upstream per-company timeline harvest before this bundle was built, not introduced during consolidation.

**Handling.** All 34 flagged rows are retained in `openevidence.json` → `full_event_log` (each carries a `_data_quality_flag` field identifying the unrelated company) rather than silently dropped. They are excluded from the curated list below and from the Litigation & Partnership readings elsewhere in this profile. A full itemized list of all 34, with a one-line reason for each, is in the companion JSON.

### Curated top 29 (excludes all 34 flagged rows), chronological

1. **2022-01-01** — Founded *(Verified; see founder-name conflict in Overview)*
2. **2022-09-01** — Beta launch of AI-powered medical search tool *(Verified)*
3. **2023-05-01** — $15M seed led by a16z *(Verified)*
4. **2023-11-01** — Reaches 100,000 physician users *(Verified)*
5. **2024-01-01** — $75M Series A led by a16z; 300,000+ physician users *(Verified)*
6. **2024-06-01** — Reaches 500,000 physician users (~half of all US physicians); 200+ hospital systems *(Verified)*
7. **2024-08-04** — Springer Nature partnership on clinical decision-support content integration
8. **2025-07-01** — $210M Series B at $3.5B valuation
9. **2025-10-20** — Targets/reaches a $6B valuation
10. **2025-12-01** — American Diabetes Association partnership
11. **2026-01-01** — $250M round announced at $12B valuation (best-attested 2026 round)
12. **2026-01-01** — Reaches $100M in annualized revenue *(conflicts with the $30M canonical ARR — see Financials)*
13. **2026-01-31** — HQ reportedly moves from Cambridge to Miami *(see Overview conflict)*
14. **2026-03-01** — Mount Sinai integrates OpenEvidence into Epic EHR enterprise-wide
15. **2026-03-03** — Wiley content-licensing partnership announced
16. **2026-03-10** — 1 million clinical consultations in a single day — described as a historic first
17. **2026-03-16** — AAO-HNSF clinical-practice-guideline partnership
18. **2026-04-02** — Tandem partnership for evidence-based prescribing / prior authorization
19. **2026-04-27** — NCCN oncology clinical-practice-guideline integration
20. **2026-04-28** — Withdraws from UK and EU markets citing AI Act regulatory uncertainty *(Negative signal — see Litigation & IP)*
21. **2026-05-01** — ACOG (Ob-Gyn) strategic collaboration
22. **2026-05-19** — CNBC Disruptor 50 listing; $795.4M total funding disclosed *(conflicts with $100M canonical total raised — see Financials)*
23. **2026-05-20** — Cedars-Sinai enterprise deployment
24. **2026-05-27** — Society of Surgical Oncology / ASCO guideline-integration partnership
25. **2026-06-01** — Nature Medicine benchmark study: OpenEvidence underperforms GPT-5.2, Gemini 3.1 Pro, and Claude Opus 4.6 on all three tested benchmarks
26. **2026-07-19** — Considers (but per follow-up reporting is unlikely to proceed with) a $200M raise at $20B valuation
27. **2026-07-25** — ~$150M annual revenue reported (Forbes) — another point widening the ARR spread
28. **2026-07-29** — NOHARM benchmark (Stanford/Harvard/ARISE): shared patient-harm flaw identified across OpenEvidence, OpenAI GPT-5.6 Sol, Anthropic Claude Fable 5, and Doximity's tool — 1,100 clinical cases, ~13,000 physician harm-scored annotations
29. **2026-08-06** — OneOncology partnership to improve cancer care

---

## (i) Open conflicts & disputes

1. **Founder name:** "Eran Segal" (verified event title only, unsupported by its own body text) vs. "Daniel Nadler" (registry Leadership field + a separate corroborating event).
2. **Headquarters:** Cambridge, MA (registry) vs. Miami, FL (score-tracker fields + two dated relocation events).
3. **Leadership-field contamination:** registry's Key Departures/Key Hires fields (Winterhoff, Rawlinson, Napoli) belong to Lucid Motors, not OpenEvidence.
4. **ARR: $30M canonical vs. a $50M–$150M press range** spanning 2025–2026, unchanged in the registry since the Jan-2025 verified print.
5. **Total capital raised: $100M canonical vs. $700M–$795M press range.**
6. **Revenue Growth YoY %: 1% stated vs. 100%** implied by the record's own Prev/Current ARR fields and independently stated elsewhere.
7. **Profitability status:** "Profitable" (registry) vs. "Burning — Controlled" (comparisons table), same as-of date.
8. **Implied ARR multiple:** 133.33x stated vs. 400x arithmetic from the row's own valuation/ARR fields.
9. **Funding-round naming:** registry says the latest round is "Series C"; most 2026 press calls it "Series D," and a 2025 round is also independently labeled "Series D" — the naming does not sequence cleanly.
10. **Disputed $200M-at-$6B round** (Oct 2023 vs. Oct 2024, single low-tier source, doesn't sequence against verified rounds).
11. **Disputed "Sequoia-led $100M Series A at $1B" claim** (May 2026) — conflicts with the established 2024 a16z-led Series A and the already-reported $12B valuation.
12. **"Delta Sigma Theta" investor-name artifact** — almost certainly a scraping error, not a real cap-table participant.
13. **Adoption scale:** ~15M vs. ~20M consultations/month, not reconciled.
14. **~3-week $13B valuation print** in the daily tracker (2026-06-21 to 2026-07-09) with no corroborating narrative event.
15. **Systemic timeline contamination:** 34 of 154 dated events (≈22%) are about unrelated companies — see section (h) for the full account. This is a data-quality issue about the source pipeline itself, not a factual dispute about OpenEvidence, but it is significant enough to log here as well.

---

## (j) Sources

- **154** dated timeline events drawing on **128 unique source URLs** across **83 unique domains** (from 822 raw rows seen before date-filtering)
- **7** Verified=Yes / **147** unverified-harvested dated events
- **34 of the 154** flagged as likely describing unrelated companies (see section h) — retained, not deleted, and excluded from all substantive counts and curated selections above
- `canon_source_authority` registry: openevidence.com rated Authority Score 9 / Tier 9 ("official tracked-company sources + major wire services"), last reviewed 2026-07-21
- 2 NEXUS Morning Digest citations in `shared_morning_digests_db` (2026-07-29 v10.6, NOHARM benchmark; 2026-06-09 v7.0, brief mention alongside a note that OpenEvidence's evidence items were still queued for AIBQ scoring as of that date)
- AIBQ score card (`extract/framework/companies/openevidence.md`)
- PitchBook-linked internal registry rows: legacy company row, v2 company registry, 115-day daily snapshot series (2026-03-23 to 2026-08-11), company-comparisons record, 3 unicorn-score records, 1 company-dossier record (`aibq_unicorn_intel` is empty for this company, unlike ElevenLabs)

Representative domains: openevidence.com, statnews.com, cnbc.com, forbes.com, nytimes.com, techcrunch.com, en.wikipedia.org, tracxn.com, reveliolabs.com, fortune.com, and 73 others (full list in `openevidence.json` → `sources.domain_list`).
