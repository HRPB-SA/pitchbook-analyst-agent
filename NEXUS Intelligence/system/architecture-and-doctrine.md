# NEXUS Architecture & Operating Doctrine

How the NEXUS research system itself is built and run: its database
architecture (three generations, now consolidating into v2), the
deterministic legacy-to-v2 mapping, the standard output products it can
generate, and its daily/quarterly operating discipline. Mirrored from
Notion 2026-08-11.

## Contents

1. Architecture overview — why three generations of company stores exist
2. Legacy → v2 migration design (the deterministic mapping + sync-agent build log)
3. Reorg diagnosis — what prompted the migration
4. Output Playbook — the 12 standard analytical products and how to build each
5. Operating discipline — daily audit, analyst checklist, go-live validation, mentor doctrine
6. Guardian — the automation layer
7. Hub notes (Company Registry, Financial History, Event Timeline, Score History, Signal Processing, Research & Output, Operations & Meta)
8. Workspace root map

---

# 1. Architecture Overview

# 🏛️ NEXUS v2 — Clean Architecture

The single front door to every NEXUS v2 database. All company data routes through the Company Registry via relations; rollups auto-calculate event counts, latest scores, and financials. Legacy old-NEXUS databases remain intact for audit trail while the v2 sync agent mirrors them into the databases below.

---
## 🧭 Start here
- [🏢 Company Registry](https://app.notion.com/p/36d5e7ad9f7f81a5a0dfee52092a781e)
The spine. Every other database relates back to it. Holds AIBQ/PBQ composite, the five dimensions, tier, IPO status, valuation, ARR, and rollups.
## 📊 Scoring & quality
- [📊 Score History](https://app.notion.com/p/36d5e7ad9f7f8185af8fed94d5e5e24f)
[linked view: 📏 KPI Tracker database — https://app.notion.com/p/9d2bfc00801d4651b620a25a821ca81e (data source collection://07da58b6-e50c-4dc6-94eb-2dd90efd06c1)]
- [💰 Financial History](https://app.notion.com/p/36d5e7ad9f7f81b59e4ac47ae04f3011)
[linked view: 🔮 Prediction Log database — https://app.notion.com/p/0f23302017ee4d368e13047ab78c6621 (data source collection://53cb1beb-23f3-4b4a-836b-dc69b03f0255)]
## 💰 Financials & funding
The Signal Processing databases (live under that page): [🔗 Sources](https://www.notion.so/3285e7ad9f7f80b5a3e3d6e897156721), [⚡ Events](https://www.notion.so/3285e7ad9f7f80b68ecfe18839ceb7ab), [🌐 Master Events](https://www.notion.so/3295e7ad9f7f8131a872dee7ae283d6f), [⚠️ Review Queue](https://www.notion.so/3285e7ad9f7f801898ebfcdea222396f), [🏅 Benchmark Trends](https://www.notion.so/d9cfabe7c35b45fe974e9998962feea9), [⚖️ Regulatory Risk](https://www.notion.so/24629b3403db4b239a2e1a41b53777c1), [🏆 Customer Win/Loss](https://www.notion.so/9250681831894a30bff422cf178be35a), [🧑‍💼 Talent Flow](https://www.notion.so/bd4092f34ee448de84c0bc17bbaa182b), [⚖️ Litigation & IP](https://www.notion.so/5f68dc4aa3b441b9a4828f5d1e724196), [📅 Earnings & Events Calendar](https://www.notion.so/f04e6c866eb146ae90eb2682af06d580), [📌 Evidence Ledger](https://www.notion.so/2f8d6f2e6034456b9b6214b86f030dcd), [🏗️ Compute Infrastructure](https://www.notion.so/f0e7c27b68f742c6b76645a122892dbd), [🤝 Partnership & Alliance](https://www.notion.so/176f5fa2cd084050aa57839c60b3ff64).
[linked view: 💵 Funding Rounds database — https://app.notion.com/p/b3a7e06cd97b4b0d887ab216eaf34c59 (data source collection://e1934b65-324b-4b7d-be3c-18e6267fb2ce)]
## 📬 Output & research
## 🤖 Products
[linked view: 🤖 Model Registry database — https://app.notion.com/p/cdeb4545f769469289b3a9081a88db78 (data source collection://fb4446fc-f6a4-4da0-a14a-727411dca1ee)]
## ⚡ Activity & signals
- [⚡ Event Timeline](https://app.notion.com/p/36d5e7ad9f7f8149b4f5d2f6d045f9dd)
- [⚡ Signal Processing](https://app.notion.com/p/3575e7ad9f7f810c8adce9069858b2d3)
[📬 Morning Digests](https://www.notion.so/5aa8b1e40cf445d2a2660b5346f45e73) — canonical daily digest, one row per date.
[📊 Weekly Rollup](https://www.notion.so/5df2c01f4095438ea351fb27339aadc5)
- [📋 Research & Output](https://app.notion.com/p/36d5e7ad9f7f81be9e10e2a2233ba376)
## ⚠️ Pending cleanup (the sync agent will consolidate)
[📬 Morning Digest Archive](https://www.notion.so/3505e7ad9f7f812bbdf2eb922e337db6) — duplicate digest store; dedupe into Morning Digests.
[Format spec v5.0](https://www.notion.so/3445e7ad9f7f81b8b357c7db7a958848) and [v4.1](https://www.notion.so/3365e7ad9f7f81b181c0db3e25c26d35) — superseded by v7.0; demote to Historical.
Legacy old-NEXUS databases stay intact as audit trail until the ingestion repoint.

---

# 2. Legacy → v2 Migration Design

# 🔄 NEXUS Reorg — Sync Agent Design

Status: Design locked 2026-05-29. Two new databases created. Sync agent spec ready to build. Guardian VPS wiring NOT yet verified (cannot be checked from chat; Harrison runs the audit on the VPS).
## Decision (locked)
Approach: SYNC AGENT first (old NEXUS keeps scraping into old DBs via the live GitHub Actions pipeline; a new Guardian agent reads new/changed rows and UPSERTS them into v2). v2 becomes the clean source of truth / derived layer. Later, once v2 is proven, repoint ingestion directly into v2 and freeze the old DBs. The sync transform logic is reused at that cutover, so nothing is wasted.
## Core safety principle (the rule that prevents the duplication we already found)
Every synced record carries a stable Sync Key and the agent UPSERTS, never blind-inserts. On each run: compute key, look up existing v2 row by key, update if present, insert only if absent. Keys: Source = URL; Event = company\|date\|title_hash; Score = company\|date\|framework; Financial = company\|date\|metric; Model = company\|model\|release_date; Funding Round = company\|stage\|announced_date; Digest = date. The May-28 backfill duplicated digests precisely because it had no key and just created.
## Judgment vs determinism (correction to the original ask)
Organizational placement is DETERMINISTIC (fixed mapping rules below, decided once, here). Model-based judgment is allowed ONLY for fuzzy store-once fields (e.g. classifying a source's topic/sector, summarizing an event's significance) and the output is then persisted so it is stable across runs. The agent must never improvise where a row lives.
## v2 target inventory (what exists, do NOT recreate)
Core: Company Registry (coll a2b663e7-5ad9-4ddb-970d-0daf36715f82; \~14 companies incl FF + Cohere, Mistral, Perplexity, ElevenLabs, Scale, CoreWeave, Cursor, OpenEvidence), Event Timeline (coll a058291b-cc20-4f18-bb7e-b8cd2cc37c06), Score History (coll 557e8ac9-4300-48eb-adfe-4f79cfa0938b), Financial History (coll e0291a05-0918-4cb6-bc29-ef12b248c151), Research & Output, KPI Tracker (coll 07da58b6-e50c-4dc6-94eb-2dd90efd06c1), Prediction Log (coll 53cb1beb-23f3-4b4a-836b-dc69b03f0255), Publications (coll df3f414d-582b-4fa3-9141-21b57b5cafb4).
Signal Processing layer: Sources (coll 3285e7ad-9f7f-8015-b497-000bccb09a2c), Events (coll 3285e7ad-9f7f-8011-8682-000b88fe3d31), Review Queue, Master Events, Benchmark Trends (coll 7ee8254c-46db-43f5-8623-240d7b7aa78b), Regulatory Risk (coll 07988400-4611-4c37-b39a-de6a5eb3b62e), Customer Win/Loss (coll dfca1ba3-bae0-4e13-9826-6c77006c24d8), Talent Flow Tracker (coll f05024e4-f8fc-4437-ae25-d7f29df2faca), Litigation & IP (coll f45204fd-132b-4a19-9732-62f7c62a0395), Earnings & Events Calendar (coll d93289d9-740e-49ad-981c-66979c0202dc), Evidence Ledger (coll 6289e808-53cd-4a0c-a51a-28701f150959), Compute Infrastructure (coll 0f02b7db-50e2-4ce9-8b07-f418f87f25a0), Partnership & Alliance (coll f32a7d7c-558a-4164-ac47-c6622c0afc57).
Digests: Morning Digests DB (coll 448c36ae-83f9-4e1e-914d-c849eb661c09) = CANONICAL digest home. Schema: Date, Digest Version, per-FF composites, Lead Signal, Section Count, Status. One row per day.
## NEW databases created today (the only genuine gaps)
Model Registry (coll fb4446fc-f6a4-4da0-a14a-727411dca1ee) — model releases, modality, params, context window, key benchmark, significance. Related to Company Registry as 'Models'.
Funding Rounds (coll e1934b65-324b-4b7d-be3c-18e6267fb2ce) — round history, stage, amount, pre/post valuation, lead investors, PBID. Related to Company Registry as 'Funding Rounds'.
Decision NOT to create a new digest DB: Morning Digests already exists; a 4th store would worsen duplication. Talent NOT created: Talent Flow Tracker already exists.
## Deterministic mapping: old NEXUS -\> v2 (sync agent)
Old Sources -\> v2 Sources (key: URL). Resolve company name -\> Company Registry relation.
Old Events/Snapshots -\> v2 Event Timeline (key: company\|date\|title_hash); high-impact -\> Master Events.
Old Daily Scores/Score Tracker -\> v2 Score History (key: company\|date\|framework); update Registry latest composite + dimensions via rollup, not by overwrite.
Old FMI/Financials -\> v2 Financial History (key: company\|date\|metric).
Model-release sources/events -\> Model Registry (key: company\|model\|release_date).
Funding/deal rows + PitchBook -\> Funding Rounds (key: company\|stage\|announced_date).
Old Talent items -\> Talent Flow Tracker. Old regulatory -\> Regulatory Risk. Old litigation -\> Litigation & IP. Old benchmarks -\> Benchmark Trends / Model Registry. Old partnerships -\> Partnership & Alliance. Old compute -\> Compute Infrastructure. Old customer wins -\> Customer Win/Loss. Old earnings -\> Earnings Calendar.
Old Digests (DB + Archive page + loose pages) -\> Morning Digests (key: date); keep most complete version per date; redirect dupes.
Unmapped/ambiguous -\> Review Queue with a reason, never dropped, never guessed into a random DB.
## Company scope
Top 20 AI companies incl Frontier Five as T1/T2 Coverage Tier in Registry. Unicorns (the \~475 scored) live in Registry at T3/T4 with AIBQ or PBQ Framework flag and their composite in Score History. Sync must upsert companies into Registry by name (+ PBID when known) before attaching child rows, so nothing orphans.
## Guardian wiring — cannot verify from chat
Guardian runs on VPS 134.122.123.51 at /home/nexus-guardian. From Notion I can only infer: Registry partly populated toward top 20 (good), digests fragmented (digest agent not writing to one canonical home), so wiring is INCOMPLETE. Definitive audit checklist is in the build spec; Harrison must run it on the VPS.
## Session log
### 2026-05-29
Grounded the design against real v2 schemas. Created Model Registry and Funding Rounds. Designated Morning Digests as canonical. Declined to create duplicate Talent/Digest DBs. Wrote deterministic old-\>v2 mapping with upsert keys. Authored sync-agent build spec + VPS audit (delivered to Harrison as a paste-able file).
### 2026-05-29 (later) — Column mappings pinned
Sync agent built by Cursor: 283 tests passing (added 15), 4 spec tests green (upsert idempotency, alias resolution, digest dedup, orphan routing). Pinned live column mappings for the high-traffic domains: Score History (full 24 sub-scores CE-1..MD-5, Composite, CRA, Framework Version v2.2/v3.0, Weight Config, Quality Tier, key=company\|date\|frameworkversion), Financial History (full metric set, Source Type, Confidence, key=company\|date\|period-or-metric), Event Timeline (Category 17-option enum, Significance, Sentiment, Source Tier, plus existing "Migrated From" audit field, key=company\|date\|sha1(title)). Model Registry and Funding Rounds use their built-in Sync Key property. Remaining domains: agent self-fetches schema on --init into config/v2_schema_map.yaml and refuses --apply until confirmed. Still blank in config: master_events, review_queue, funding source IDs, digests_archive — fill before apply. Next: run --init, review generated schema map, then --domain digests --dry-run.
### 2026-05-29 (checkpoint) — Handoff to VPS
Agent at 292 tests passing. FIELD_MAPS pinned for scores/financials/events/models/funding with type coercion and select-validation→Review routing. init() generates config/v2_schema_map.yaml and blocks --apply on unconfirmed domains. Provided the two missing IDs: master_events = 3295e7ad-9f7f-8139-bdd7-000b2e1dd4f0, review_queue = 3285e7ad-9f7f-8066-b076-000b6cf7523e (both data source/collection IDs). Still to fill if used: funding source ID, digests_archive. 12 unpinned domains need confirm: sources, talent, regulatory, litigation, benchmarks, compute, partnerships, customers, earnings, digests, publications, kpi. NEXT (on VPS, needs NOTION_TOKEN): git pull → v2-sync --init (populates discovered_properties) → review schema map, confirm digests first → v2-sync --domain digests --dry-run. Watch digest insert count: \~20s = key works; 40-50 = key broken, do not apply. Then --apply --domain digests, verify one row per date, proceed domain by domain. Cron stays OFF until a clean full manual run.
### 2026-05-29 (config note) — Do NOT reconcile the two config blocks
config.yaml intentionally has TWO master_events / review_queue entries with different values. notion.v2.\* = the sync agent's WRITE targets. Legacy block (lines \~36-37) = the still-live old GitHub Actions pipeline's own IDs. They must stay different. Pointing legacy at v2 collections would silently perform the deferred repoint and merge the two systems before v2 is validated. Action taken: leave both as-is; recommended adding clarifying comments above each block so they are not "fixed" later. The duplicate-looking keys are correct, not a bug. Reconcile only at the eventual planned repoint, in a separate session, after v2 is proven. Also: offline empty MISSING_IDS confirms IDs are well-formed, NOT that they resolve — real resolution check happens on first VPS --init with token.
### 2026-05-29 (hub) — NEXUS v2 page rebuilt as the single front door
Reorganized the NEXUS v2 — Clean Architecture page into a complete grouped index linking every database: Start here (Company Registry), Scoring & quality (Score History, KPI Tracker, Prediction Log), Financials & funding (Financial History, Funding Rounds), Products (Model Registry), Activity & signals (Event Timeline, Signal Processing + its 13 sub-databases), Output & research (Morning Digests canonical, Weekly Rollup, Research & Output), and Pending cleanup (Morning Digest Archive duplicate + v5.0/v4.1 specs to demote). Chose front-door index over physical relocation: zero collection IDs touched, migration undisturbed, duplicates flagged rather than buried. Cleaned the doubled-emoji page title. Note: index is a static snapshot; shrink the Pending cleanup section after the sync consolidates digests.
### 2026-05-31 (\~3am) — RESUME HERE NEXT SESSION
Stopping for the night. State: v2-sync --init resolves all 23 targets (config IDs corrected, commit 05b4e0a). Digests domain applied (7 duplicates superseded, 1 undated row in Review). Eleven domains remain UNRUN: scores, financials, events, sources, talent, regulatory, litigation, benchmarks, compute, partnerships, customers. Sync cron still OFF by design.
NEXT SESSION, in this order:
1. FIRST confirm Guardian ingestion actually works before syncing. Check tomorrow's 4pm-UTC digest landed in Telegram, and that logs/monitor.log + logs/scorer.log have FRESH timestamps with real content. Tonight both staged 0 events, so source data may be stale/thin. Do not sync stale source data on a schedule.
2. Then run the 11 domains one at a time: for each, set confirmed:true in config/v2_schema_map.yaml (only after checking discovered_properties look right), run `nexus-guardian v2-sync --domain <name> --dry-run`, READ the insert/update/review/blocked counts, then `--apply`. Start with scores (most valuable, also most complex: 24 sub-scores). Do NOT batch-apply all 11.
3. Only after all 11 apply clean by hand: turn on the hourly v2-sync cron (add `40 * * * * $R v2-sync >> logs/v2-sync.log 2>&1` via the wrapper, same [run.sh](http://run.sh) pattern).
Open watch-item from Guardian revival: monitor staging 0 events — likely the unreliable DuckDuckGo web search. Chase if tomorrow's digest is thin.

---

# 3. Reorg Diagnosis

# 🔍 NEXUS Reorg — Diagnosis

Status: Diagnosis complete 2026-05-29. No migration actions taken yet. This page is the investigation output; execution is gated on Harrison's decisions below.
## Headline finding
The digests are not missing. They are duplicated and scattered across multiple competing homes. The original premise ("digests not saved, Guardian did not fill everything in") was inverted: Guardian filled things in, but into a second location, creating doubles. The real problem is collision, not absence. Charging in to backfill would have worsened the duplication.
## Evidence: digest storage is fragmented across 3+ homes
1. A database: "Morning Digests" (id 5aa8b1e4-0cf4-45d2-a266-0b5346f45e73).
2. A page-archive: "Morning Digest Archive" (id 3505e7ad-9f7f-812b-bdf2-eb922e337db6), described as one page per day, v6.0.
3. Loose individual pages at various parents.
## Evidence: confirmed duplicate digests
- May 12: 35e5e7ad-...(created May 12) AND 36e5e7ad-...-a517 (created May 28).
- May 13: 35f5e7ad-... (original) AND 3605e7ad-...-ade4 ("Backfill").
- May 14: 3605e7ad-...-b1b6 AND 3605e7ad-...-8343.
- May 6: 3585e7ad-...-b812 AND 3585e7ad-...-97ee.
- May 3: 3555e7ad-...-804f AND 36e5e7ad-...-85b2.
- April 26 and April 27 also appear in a May-28 backfill batch (36e5e7ad-...) alongside earlier copies.
The 36e5... cluster (all created 2026-05-28) is a backfill run that recreated digests that already existed elsewhere.
## Evidence: competing "canonical" format specs
Three specs each labeled Canonical: v4.1 (3365e7ad-...), v5.0 (3445e7ad-...), while the actual production format is v6.0/v7.0. Multiple canonical specs is a contradiction and should be resolved to one current + the rest marked Historical.
## Nexus v2 structure (the intended target)
"NEXUS v2 — Clean Architecture" (36d5e7ad-9f7f-81d6-848e-f18f305ae8c8) declares itself the new source of truth; legacy DBs kept intact for audit trail; everything connects through the Company Registry via relations with auto-rollups. Core v2 surfaces found: Company Registry (page 36d5e7ad-...-a0df; database 02b14c93-...), Financial History (page 36d5e7ad-...-9e4a; database e3723576-...), Signal Processing (3575e7ad-...-8adc), Sources DB (3285e7ad-...-a3e3). Note duplicate-looking Company Registry and Financial History entries (page vs database) that themselves need reconciling.
## The three jobs, re-scoped after diagnosis
1. Digest consolidation (NOT backfill). Pick ONE home (recommend the Morning Digest Archive page or the Morning Digests DB, not both), dedupe to one page per date keeping the most complete version, point the others to it. This is the biggest and most error-prone job.
2. Guardian finish-out. Genuinely incomplete items, separate from digests: filtered linked views for OpenAI/Databricks/xAI/SSI (Anthropic done), Gmail App Password cleanup, unicorn upload (2,508), Company Financials population. Some steps are manual-only (per-view filters the API cannot set).
3. Old-to-v2 dataflow. Decide what from the legacy 52-DB sprawl actually feeds v2's relational model vs stays frozen as audit trail. The v2 page already says legacy stays intact, so this is mostly classification, not migration.
## Decisions needed from Harrison before execution
A. Single digest home: Archive page, or Morning Digests DB?
B. Dedup rule when two copies differ: keep newest, keep most complete, or show diffs and ask per-conflict?
C. Which format spec is current canonical (assume v7.0) so the others can be demoted to Historical?
## Recommended order
Resolve the three decisions, then: digest consolidation first (highest pain, highest collision risk), Guardian finish-out second (well-defined), dataflow classification last (lowest urgency since legacy is already preserved).
## Session log
### 2026-05-29
Diagnosis run. Found duplication/collision rather than absence. Wrote this page. Execution gated on decisions A/B/C.

---

# 4. Output Playbook — The 12 Standard Products

# 📖 NEXUS Output Playbook

This page defines every structured output that NEXUS can produce, with exact instructions for which databases to query and how to assemble the result.

---
## Automated Analytical Products
### 1. Quarterly Company Briefing
Frequency: Quarterly (or ad hoc before media interviews)
Time to produce: 30-60 minutes using NEXUS data
Data sources to query:
- Company Profile page (snapshot section for current AIBQ/valuation/ARR)
- Company Timeline (filter: Date within quarter, sort by Date DESC)
- AIBQ Score Tracker (filter: Company + Date within quarter)
- Valuation History (filter: Company + Date within quarter)
- Forecast Calibration Log (filter: Company + resolved within quarter)
- Regulatory Risk Tracker (filter: Company + Status = Active)
- Talent Flow Tracker (filter: To Company or From Company = target)
- Litigation/IP Tracker (filter: Defendant = Company)
- Financial Model Inputs (filter: Company, sort by Year DESC)
- Investor/Cap Table (filter: Company)
- Benchmark Trends (filter: Company, latest results)
Output structure:
1. Executive Summary (1 paragraph: AIBQ score trajectory, valuation change, key event)
2. AIBQ Score Card (5 dimensions, quarter-over-quarter delta)
3. Key Events (top 5 from timeline, sorted by Importance)
4. Financial Position (ARR, valuation, capital raised, efficiency ratio)
5. Competitive Positioning (score vs peers, valuation vs peers)
6. Risk Profile (active regulatory risks, litigation exposure, governance concerns)
7. Forecast Track Record (forecasts resolved this quarter, hit rate)
8. Outlook (open forecasts, upcoming catalysts from Events Calendar)
Format: Markdown file or DOCX for distribution

---
### 2. Forecast Calibration Report
Frequency: Monthly (trailing 30 days) + Quarterly (trailing 90 days)
Time to produce: 15-30 minutes
Data sources:
- Forecast Calibration Log (all resolved forecasts in period)
- AIBQ Score Tracker (to correlate score changes with forecast accuracy)
Output structure:
1. Summary Stats (forecasts logged, resolved, hit rate, Brier score)
2. By Company (hit rate per company — systematic bias detection)
3. By Horizon (near vs mid vs contrarian accuracy)
4. By AIBQ Dimension (which dimensions do you predict best/worst)
5. Systematic Biases (overconfidence? underconfidence? directional bias?)
6. Calibration Curve (predicted probability vs actual outcome rate)
7. Publication Gate Status (trailing 90-day Brier vs 0.15 threshold)
Format: Markdown with embedded data tables

---
### 3. Thesis Health Check
Frequency: Quarterly
Time to produce: 45 minutes
Data sources:
- Thesis Registry (all active theses)
- AIBQ Score Tracker (evidence for/against each thesis)
- Company Timelines (events that support or undermine theses)
- Valuation History (for valuation-related theses)
- Forecast Calibration Log (forecasts derived from each thesis)
Output structure per thesis:
1. Thesis Statement (from Core Claim field)
2. Current Conviction (from Conviction field)
3. Supporting Evidence Since Last Review (new timeline events, score changes)
4. Challenging Evidence (events that cut against the thesis)
5. Falsification Status (has the falsification condition been met or approached?)
6. Conviction Update (maintain / strengthen / weaken / abandon)
7. Dependent Forecasts (open forecasts that rely on this thesis)
Format: Notion page update on each Thesis entry + summary document

---
### 4. Competitive Intelligence Matrix
Frequency: Monthly or before reports
Time to produce: 20 minutes
Data sources:
- AIBQ Score Tracker (latest composite + all 5 dimensions for each company)
- Valuation History (latest valuation per company)
- Financial Model Inputs (ARR, capital raised per company)
- Companies DB (sector, competitive position)
Output structure:
Single table: Company \| AIBQ \| Valuation \| ARR \| CE \| RQ \| CI \| GO \| MD \| \$/Quality Point \| IPO Readiness
Plus: r correlation recalculation
Format: Table in digest §3 scoreboard + standalone for reports

---
### 5. Risk Exposure Report
Frequency: Monthly
Time to produce: 15 minutes
Data sources:
- Regulatory Risk Tracker (all active/escalated risks)
- Litigation/IP Tracker (all active cases)
- Talent Flow Tracker (departures in last 90 days)
- Company Timelines (Legal/Regulatory + Security categories, last 90 days)
Output structure:
1. Aggregate Exposure (total \$ at risk across all companies)
2. By Company (risk count + exposure per company)
3. By Risk Type (regulatory vs litigation vs talent vs governance)
4. New Risks This Month
5. Risks Approaching Resolution
6. AIBQ Impact Assessment (which GO/MD scores are at risk)

---
### 6. Media Performance Tracker
Frequency: Monthly
Time to produce: 10 minutes
Data sources:
- Media & Outreach Tracker (all entries in period)
- Morning Digests (§9 and §16 outputs)
Output structure:
1. Pitches Sent vs Coverage Received (conversion rate)
2. By Outlet (which outlets respond, which don't)
3. AIBQ Framework Adoption (how often AIBQ is referenced in coverage)
4. LinkedIn Engagement (posts published, engagement trends)
5. Next Month Targets (outlets to prioritize, angles to pitch)

---
## Workflow Intelligence
### 7. Pre-Digest Briefing (Run Before Every Digest)
Query sequence:
1. FCL: Unresolved forecasts with Test Date in next 7 days
2. Events Calendar: Status = Upcoming, Date = today or this week
3. Financial Model Inputs: Last Verified Date \> 30 days ago (stale data)
4. Thesis Registry: Last Reviewed \> 30 days ago
5. Morning Digests: Check which companies appeared in §6 forecasts in last 3 sessions (rotation compliance)
6. AIBQ Score Tracker: Any dimension with 0 changes in last 30 days (coverage gap)
Output: Bullet list of items to check during intel gathering

---
### 8. Post-Digest Validation (Run After Every Digest)
Check sequence:
1. Every AIBQ delta from §3 has a matching row in AIBQ Score Tracker with today's Digest Date
2. Every §6 forecast has a matching row in FCL with today's Digest Date
3. Every §11 Next Move row has a matching row in FCL
4. Every E# event has a matching row in the relevant company Timeline
5. Digest archived to Morning Digests DB with all composite scores populated
6. §22 Contrarian thesis logged to Contrarian Log
7. Any financial figure updates pushed to Financial Model Inputs with today's Last Verified Date
Output: Pass/fail checklist. If any item fails, surface it before closing the session.

---
### 9. Weekly Rollup Auto-Population
Timing: Sunday evening or Monday morning
Query sequence:
1. AIBQ Score Tracker: All changes with Date of Change in last 7 days
2. FCL: All forecasts logged and resolved in last 7 days
3. Company Timelines (all 5 FF): Events with Date in last 7 days, Importance = Critical or High
4. Thesis Registry: Any conviction changes in last 7 days
5. Media & Outreach Tracker: All entries in last 7 days
6. Morning Digests: Count of digests completed, latest composite scores
7. Earnings Calendar: Events completed this week with Outcome Notes
Output: Populate one row in Weekly Rollup DB with all fields

---
## Cross-Database Intelligence
### 10. Signal Correlation Detection
Run during §4 Competitive Dynamics
Query: All 5 FF timelines for events in the same Category in the same week.
If 3+ companies have events in the same Category, flag as market-level signal.
Examples:
- 3 companies with Funding events = capital markets opening
- 3 companies with Legal/Regulatory events = regulatory wave
- 3 companies with Model Release events = capability race acceleration

---
### 11. Valuation-Quality Correlation Maintenance
Run monthly or when any AIBQ score or valuation changes
Query:
- Latest AIBQ composite for each FF company (from Score Tracker)
- Latest valuation for each FF company (from Valuation History)
- Calculate \$/quality-point for each
- Recalculate Pearson r
- Compare to baseline [VALUE EMBARGOED — see canon-and-governance.md Ruling 2]
If r weakens to below -0.90: flag as thesis risk in Thesis Registry
If r strengthens or holds: note in conviction history

---
### 12. IPO Readiness Assessment
Frequency: Monthly for Databricks and Anthropic
Data sources:
- Financial Model Inputs (revenue growth, margins, FCF trajectory)
- Regulatory Risk Tracker (active risks that could delay filing)
- Governance data from Companies DB
- Market conditions from digest §5 Market Watch
- Earnings Calendar (IPO milestone entries)
- Valuation History (primary vs secondary spread)
- Forecast Calibration Log (IPO-related forecasts)
Output: Structured assessment with go/no-go factors and estimated timeline

---
## Output Formats by Destination

| Output | Format | Destination |
| --- | --- | --- |
| Quarterly Briefing | DOCX or MD | PitchBook internal, Morningstar |
| Calibration Report | MD | Internal, eventually public |
| Thesis Health Check | Notion page updates | Internal |
| Competitive Matrix | Table in digest | Daily digest §3 |
| Risk Report | MD or DOCX | PitchBook internal |
| Media Performance | MD | Internal review |
| Pre-Digest Briefing | Inline in chat | Every digest session |
| Post-Digest Validation | Inline checklist | Every digest session |
| Weekly Rollup | Notion DB row | Weekly Rollup DB |
| IPO Assessment | DOCX | PitchBook reports |

---

# 5. Operating Discipline

## Daily Audit Dashboard

# ✅ Daily Audit Dashboard

**Purpose:** One-stop verification page. Visit each morning to confirm yesterday's digest was properly logged. If any check fails, the digest didn't happen — it's chat content, not analyst output.

---
## Daily Verification Checklist
Time: \~5 minutes every morning before writing the new digest.
- [ ] **Yesterday's AIBQ score changes** logged in [📈 AIBQ Score Tracker](https://www.notion.so/3295e7ad9f7f810b9d0ae72a1cf368f5) with full fields populated (Company, Dimension, Previous Score, New Score, Score Change, Direction, Date of Change, Triggering Event, Rubric Line, Source URL, Confidence, Analyst Rationale)
- [ ] **All Source URLs are clickable and resolve** (not blank, not 404). If a T1 source paywalled, cite the aggregator AND the original in Analyst Rationale.
- [ ] **Every row has a Rubric Line citation** referencing AIBQ Rubric v1.0 (e.g., 'CE §1 — quintile boundary cross +1.0'). No rubric line = ad-hoc scoring = invalid.
- [ ] **Verified By Claude checkbox** is TRUE. If FALSE, it's a proposal awaiting analyst verification, not a logged change.
- [ ] **Yesterday's forecasts** logged in [🔮 Forecast Calibration Log](https://www.notion.so/c31f1e52ecac4fac9fb65b7a5471c468) with Probability, Test Date, Binary Test, Invalidator, Supporting Evidence, Related AIBQ Dimension.
- [ ] **Any forecasts whose Test Date was yesterday** have Resolution set to Hit / Miss / Ambiguous, Actual Outcome populated (0 or 1), Brier Score computed, Post-Mortem written.
If all 6 pass: digest was properly logged. Proceed to today's.
If any fail: fix the log before writing today's digest. Enforcing this ordering is the only thing that makes the framework real.

---
## Weekly Review (Mondays, 10 min)
- [ ] Score Tracker: how many entries in the last 7 days? If fewer than 3, coverage is too light or digests aren't being logged.
- [ ] Forecast Calibration Log: how many forecasts logged last week? How many resolved? Running hit rate?
- [ ] Source-tier audit: what % of last 7 days' Triggering Events cite T1 sources? Target: \>70%.
- [ ] Rubric-citation audit: any entries without a Rubric Line? Fix retroactively.
- [ ] Cross-check Score Tracker Date of Change vs Digest Date — they should match for same-day logging.

---
## Monthly Review (first Monday, 30 min)
Per Mentor Doctrine §"Monthly doctrine review":
1. Read [🧭 Mentor Doctrine v1.0](https://www.notion.so/3445e7ad9f7f81e883f9f2d6a1d0f139) top-to-bottom; defend or revise each position.
2. Forecast Calibration: compute trailing-30-day hit rate and average Brier. Log to [🔮 Forecast Calibration Log](https://www.notion.so/c31f1e52ecac4fac9fb65b7a5471c468).
3. Check Q3/Q4 report slot status (Mentor Doctrine §2). Q3 named by April 30? Q4 named by July 31?
4. Extended-universe sweep completion rate: 4/4 Mondays?
5. Canonical data freshness: last full update date?
6. If hit rate \<50% two consecutive months, pause external forecast publication until recalibration.

---
## Views to bookmark
### AIBQ Score Tracker — daily audit view
**URL:** [AIBQ Score Tracker](https://app.notion.com/p/3295e7ad9f7f810b9d0ae72a1cf368f5)
Sort by Date of Change descending. Essential columns visible in Table view:
- Entry (headline summary)
- Company
- Dimension
- Previous Score → New Score
- Score Change
- Direction
- Date of Change
- Digest Date
- Triggering Event
- Rubric Line
- Source URL
- Confidence
- Verified By Claude
Existing views:
- **Default view** — all columns
- **Table** — sorted by Date of Change descending
- **Board** — grouped by Company (visual cadence check)
### Forecast Calibration Log — open positions view
**URL:** [Forecast Calibration Log](https://app.notion.com/p/c31f1e52ecac4fac9fb65b7a5471c468)
Use the database filters:
- Filter: Resolution = Unresolved
- Sort: Test Date ascending
- Essential columns: Forecast, Company, Horizon, Probability, Test Date, Binary Test, Invalidator
When Test Date ≤ today: resolve the forecast. Set Resolution (Hit / Miss / Ambiguous), Actual Outcome (0 or 1), compute Brier Score (probability − outcome)², write Post-Mortem.

---
## What a complete daily log looks like
Apr 16, 2026 reference example (logged today as schema test):

| Entry | Company | Dim | Prev → New | Δ | Trigger | Rubric | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Anthropic CE 7→8 | Anthropic | CE | 7 → 8 | +1.0 | ARR run-rate tripled \$9B→\$30B; \$1M+ ACV cohort doubled | CE §1 quintile up | Bloomberg/TechCrunch |
| Anthropic GO 4→5 | Anthropic | GO | 4 → 5 | +1.0 | CAISI testing Mythos + Narasimhan board add | GO §4 tacit bypass +0.5 + board add +0.5 | Politico |
| Anthropic Total 7.0→7.5 | Anthropic | Total | 7.0 → 7.5 | +0.5 | Composite rollup from CE + GO changes | Composite formula | Bloomberg |

And 3 forecasts logged: FCST-1 (Anthropic round \$550-700B by 5/31), FCST-2 (Databricks S-1 first by 7/15), FCST-3 (Mythos preview through Q3).

---
## The rule that actually enforces this
Per Morning Digest v5.0 Standing Rule §2: *'All AIBQ score changes logged to NEXUS before digest publication.'*
And per Mentor Doctrine §4: *'Every forecast in the Morning Digest is logged to the Forecast Calibration Log before publication.'*
The canonical order for every morning:
1. Pull intel (Gmail, web, MCP).
2. Draft the digest in markdown.
3. **Before publishing**: log all AIBQ score changes to Score Tracker, log all forecasts to Calibration Log, resolve any forecasts whose Test Date has passed.
4. Only after logging is confirmed: publish digest externally or share.
If step 3 is skipped, the digest is internal commentary, not analyst output.

---
*v1.0 — Effective April 16, 2026 \| Owner: Harrison Rolfes \| Bookmark this page — it's the compliance layer.*
## Linked Canon
- [📬 Morning Digest Format v5.0](https://www.notion.so/3445e7ad9f7f81b8b357c7db7a958848)
- [🧮 AIBQ Scoring Rubric v1.0](https://www.notion.so/3445e7ad9f7f81d1b052f1f935a50beb)
- [📈 Forecast Calibration Log v1.0 (doctrine)](https://www.notion.so/3445e7ad9f7f8141be5ee48975f4e80d) — methodology + scoring rules
- [🔮 Forecast Calibration Log (database)](https://www.notion.so/c31f1e52ecac4fac9fb65b7a5471c468) — where forecasts live
- [🎓 Analyst Discipline Checklist v1.0](https://www.notion.so/3445e7ad9f7f815e962bcec08deb33c6)
- [🧭 Mentor Doctrine v1.0](https://www.notion.so/3445e7ad9f7f81e883f9f2d6a1d0f139)
- [📈 AIBQ Score Tracker (database)](https://www.notion.so/3295e7ad9f7f810b9d0ae72a1cf368f5)

## Analyst Discipline Checklist

# 🎓 Analyst Discipline Checklist — v1.0

**Purpose:** Habits and disciplines that separate an analyst who's in-the-know from one who's running behind the news cycle. These are the practices that make coverage defensible in front of LPs, editors, and journalists — and that compound into real alpha over months.
Not all of these fit in the daily digest. Some are weekly, some monthly, some continuous background practices. Checklist-style — use what applies today.

---
## 1. Daily practices
### 1.1 Primary-source rotation
Read one primary document per day that isn't a news article. Rotating diet:
- Monday: 10-K or 10-Q of a hyperscaler (AMZN, MSFT, GOOGL, META, ORCL)
- Tuesday: S-1 or S-1/A of an AI-adjacent public filer (CoreWeave, Arm, Klarna, etc.)
- Wednesday: Central bank release (Fed H.4.1, BIS working paper, or ECB statement)
- Thursday: SEC comment letter or NT-10 — cheap signal, rarely read
- Friday: An AI lab paper or model card — read the actual paper, not the Twitter thread
**Why:** Most competitors only read news. Primary sources beat news by 2–4 weeks on average.
### 1.2 Source-tier audit
At the end of each digest, note what % of events came from T1/T2/T3. If T3 share is rising week-over-week, your info diet is degrading — re-prioritize T1 subscriptions.
### 1.3 Second-order discipline
Every digest must contain at least 2 'if X then Y' causal chains that go beyond the news. If you can't find two, you're reading too fast.
### 1.4 Counterfactual note
At the end of each digest — one sentence, in your own notes (not published): 'What would have to be true for my SIGNAL paragraph to be wrong?' Forces intellectual honesty without performing it.

---
## 2. Weekly practices
### 2.1 Extended Universe sweep (Monday)
Apply AIBQ Rubric v1.0 to the 8 extended-universe companies (Perplexity, Scale AI, CoreWeave, Cursor, Mistral, ElevenLabs, Cohere, OpenEvidence). Log in NEXUS. Some of your alpha is catching a company that should be scored up *before* it joins the Frontier Five.
### 2.2 Secondary market price tracker (Wednesday)
Pull weekly prints from:
- **Caplight** — bid/ask + implied valuations (Anthropic, OpenAI, Databricks, xAI, Perplexity, CoreWeave)
- **Forge Global** — same cohort, different liquidity pool
- **Hiive** — emerging company liquidity
- **EquityZen** — retail-accessible
Secondary prices are leading indicators of primary valuations. When secondaries gap \>20% above the last primary, a round is usually \<60 days out.
### 2.3 Wednesday mid-week intelligence scan \[MANDATORY — added Apr 19, 2026\]
**Why this exists:** On Apr 7, 2026, Bloomberg confirmed Anthropic's \$30B ARR. That figure sat unlogged in NEXUS for 12 days until the Apr 19 Sunday digest. That is a process failure, not an edge case. This rule closes the window from 7-day max lag to 4-day max lag.
**Minimum viable scan (15 minutes):**
1. Gmail pull `after:YYYY/MM/DD` — read T1/T2 threads only
2. Web search: `[company name] news [this week]` for each Frontier Five company
3. Any T1 event found (funding, ARR disclosure, model release, M&A, regulatory action): log to AIBQ Score Tracker + relevant company Timeline within 24 hours
No full digest required. Score Tracker and Timeline entries are sufficient. If nothing material is found, write one sentence in the NEXUS Run Log: 'Wed scan complete — no T1 events. \[date\]'
### 2.4 'The Ask' — one testable trade (Friday)
Every Friday, commit to one testable assertion that can be scored within 30 days. Logged to Forecast Calibration Log. Forces conviction discipline. If you can't produce one, you weren't rigorous enough this week.
### 2.5 Weekly KPI watchlist refresh
Beyond AIBQ, track these weekly:
- **NVIDIA DC revenue** (quarterly with monthly channel checks via Supermicro, Dell)
- **Hyperscaler capex guidance** (AMZN, MSFT, GOOGL, META)
- **Semiconductor lead times** (TSMC utilization, ASML order book)
- **Enterprise AI budget surveys** (Morgan Stanley CIO survey, Flexera State of the Cloud)
- **Power deal flow** (new PPAs, nuclear restarts, CCUS announcements)
- **LinkedIn job postings API** (headcount growth at Frontier Five and extended universe)
- **GitHub activity** (frontier lab open-source cadence)
- **Hugging Face model uploads** (signals on what labs are shipping pre-announcement)
These are the boring datasets that show the compute/labor pulse before it's in headlines.

---
## 3. Monthly practices
### 3.1 Thesis stress-test (first Monday)
Pick the 3 weakest parts of your AIBQ framework or \$100B Entry Fee report and actively search for counter-evidence. Not 'am I right' — 'what would make me wrong.'
Examples of things to stress-test:
- Is Anthropic's federal ban actually material, or is the Commerce CAISI workaround the pattern?
- Is OpenAI's CE collapse structural, or an accounting artifact of the \$110B round timing?
- Is Databricks's FCF+ truly sustainable, or does Lakehouse compete commoditize faster than expected?
Write one-paragraph findings per stress-test to NEXUS.
### 3.2 Forecast calibration ritual (first Monday)
As defined in Forecast Calibration Log v1.0. Compute hit rate + Brier, identify biases, publish to NEXUS.
### 3.3 Counterfactual journal (last Friday)
List 3 calls you made this month that turned out wrong (or ambiguous), and one sentence on *why* you were wrong. Most analysts skip this step. It's the single fastest learning loop you have.
### 3.4 Network hygiene
Touch base with 3 people who can see things you can't:
- One data-center developer or power-market specialist
- One hyperscaler procurement or capacity planner
- One SRE or infra engineer at a frontier lab
Even 20-minute calls generate more alpha per minute than any newsletter. Log learnings to NEXUS, not in a commonplace journal.
### 3.5 Media relationship refresh
Review your active media relationships (Axios, Business Insider, Morningstar, EFN). Have you produced anything citable in the last 30 days? If not, you're drifting from active analyst to passive one.

---
## 4. Quarterly practices
### 4.1 Rubric recalibration (AIBQ Rubric v1.0)
Per rubric itself: if all five companies drift uniformly, the rubric is miscalibrated, not the companies. Review quintile anchors and event adjustments.
### 4.2 Coverage universe refresh
Does the extended universe still contain the right 8 companies? A company that hasn't moved on any dimension in 90 days is probably not coverage-relevant anymore. Rotate in replacements.
### 4.3 Report cycle discipline
An institutional analyst should ship one meaningful report per quarter. AIBQ was Q1; \$100B Entry Fee is Q2. What's Q3? Q4? If you don't know, you're back-filling.
### 4.4 External-standard gate
From Forecast Calibration Log: only horizons with Brier \<0.15 in the trailing 90 days can be cited externally (LinkedIn, Morningstar, media). Defensibility gate.

---
## 5. Continuous background practices
### 5.1 The 'boring datasets' habit
- **EIA electricity data** — DC power demand by state, grid stress events
- **BLS tech employment** — layoff vs hiring pulse
- **PPI services, PPI information services** — pricing power in tech
- **Census Bureau Business Formation Statistics** — AI startup formation rate
- **FRED: real investment in software** — enterprise AI spending pulse
Even 5 minutes a week — these move before narratives do.
### 5.2 AI lab telemetry
Rotate across labs' public surfaces:
- Model cards + release notes
- GitHub commit cadence on public repos
- Hugging Face upload cadence
- Job postings by team
- Conference attendance patterns (NeurIPS, ICML, ICLR)
Changes in cadence predict product announcements by 2–8 weeks.
### 5.3 Analyst-voice discipline
When writing externally: zero hedging, zero filler, specific numbers, specific dates, specific invalidators. Cite AIBQ framework and specific E# in every external piece. Build the brand systematically.
### 5.4 Tools discipline
The tools multiply value only if they're used:
- **PitchBook MCP** — use it for every Frontier Five data point rather than quoting canonical figures
- **Morningstar MCP** — for public-company comps and sector data
- **Aiera MCP** — for earnings calls and analyst day transcripts
- [**Bigdata.com**](http://Bigdata.com)** MCP** — for sentiment and cross-reference on moves
If you notice yourself citing from memory when you have a tool that would verify — that's a discipline failure.

---
## 6. What NOT to do
- Don't publish forecasts externally until you have 90 days of calibration data.
- Don't cite canonical figures (e.g., '\$14B ARR') when live data contradicts them — update canonical or freeze the figure with a timestamp, never silently.
- Don't let secondary-market prices drive AIBQ score changes directly. Secondary prices are an *input signal*, not a dimension.
- Don't let news aggregators become your primary source. If an intel point only appears in newsletters, treat it as T3 until confirmed by a T1 primary source.
- Don't publish three articles that say the same thing. If two pieces share the same thesis, they're one piece.

---
*v1.0 — Effective April 16, 2026 \| Owner: Harrison Rolfes \| Pairs with Morning Digest v5.0 (**`3445e7ad9f7f81b8b357c7db7a958848`**), AIBQ Rubric v1.0 (**`3445e7ad9f7f81d1b052f1f935a50beb`**), and Forecast Calibration Log v1.0 (**`3445e7ad9f7f8141be5ee48975f4e80d`**)*

## Go-Live Validation Protocol (DSR/PBO)

# 🧪 Go-Live Validation Protocol (DSR / PBO) — set 2026-05-31

## Core principle
Confidence to switch Triforge to live capital must come from clearing **pre-set statistical bars**, not from a profitable-looking equity curve. The most validated finding in this field is that the majority of searched-and-selected strategies are overfit and lose money live (Bailey & López de Prado). Most strategy searches fail Gates 2–4 — finding that out on paper is the cheapest money available, and killing a strategy that can't clear these gates *is* the profitable outcome.
## Config-freeze status
**Freeze = stop editing parameters/strategies, NOT stop the process running.** Harrison opted not to freeze (2026-05-31). Consequence to keep in view: validation results are only valid for the *exact* configuration tested. Any tuning during or after the run (e.g. another threshold change) re-opens the multiple-testing problem and voids the DSR/PBO/holdout numbers. Either run the checks against a locked config or treat the results as noise.
## The protocol (in order)
1. **(Gate 1 — skipped by choice)** Freeze config.
2. **Pre-register targets** in writing before running anything else: required net-of-cost Sharpe, max acceptable drawdown, minimum trades, and the dollar loss that ends the experiment.
3. **Multiple-testing correction** on all 1,905 trial PnLs:
	- Deflated Sharpe Ratio (N = trial count; adjusts the best Sharpe for skew, fat tails, sample length, and number of trials).
	- Probability of Backtest Overfitting (PBO) via Combinatorially Symmetric Cross-Validation.
	- **PASS = DSR \> 0.95 AND PBO \< 0.20.** Fail = the search found noise → do not go live.
4. **Untouched holdout:** a time period (and ideally symbols) never used during the search or the 80→70 threshold tuning. Select strategies on the search data, then run once on the holdout. PASS = performance holds.
5. **Realistic costs:** re-run net of spread, slippage, latency, partial fills, and fees. PASS = edge survives conservative slippage. (Alpaca paper fills are optimistic; intraday edges are thin.)
6. **Forward paper-test** for a pre-set trade count — purpose is to confirm live signals, fills, and timing match the backtest (measure divergence), NOT to prove profit.
7. **Go live at minimum capital** with a P&L kill-switch that is independent of the Guardian / infra watchdog. (Uptime monitoring ≠ capital protection.)
**Decision rule:** advance only on a clean pass at each gate; a fail at any gate stops the process.
## Tooling built (2026-05-31)
`triforge_overfit_check.py` — implements DSR + PBO/CSCV in Python (numpy/scipy). Self-tested for correctness:
- Pure-noise strategy set → DSR 0.65, PBO 0.37 → correctly **FAILED**.
- Set containing one genuine-edge strategy → DSR 1.00, PBO 0.00 → correctly **PASSED**.
To run on real data, export the per-trial PnL matrix (T observations × N = 1,905 trials), the trial count, and the time-segment structure.
## Immediate next action
Run **Gate 3 (DSR / PBO)** on the existing 1,905-trial PnL matrix — computable now with no new data collection.
## 🚨 CRITICAL FINDING (2026-05-31): live gate is unvalidated by default
Traced the full selection→live wiring. The live order gate is **not** the validated set.
- `config/settings.py` → `_resolve_active_set_path()` returns `ACTIVE_SET_PAPER_TEST` whenever the `ACTIVE_SET_PATH` env var is unset.
- `active_set_paper_test.json` = **1,848 active strategies, ****`source: 'pattern'`****, ****`test_wr / test_pf / test_expectancy`**** all ****`None`****, 0 disabled** → zero out-of-sample validation. This was the "scanner-aligned paper gate" created to fix the pattern-name vs strategy-name mismatch; it lets the entire pattern universe through so the bot will trade.
- The validated set `active_set.json` (158 PASS, 1,892 correctly disabled — it even fails a 100%-WR / PF-10 tiny-sample combo) is used **only** if `ACTIVE_SET_PATH` is explicitly pointed at it.
- **Confirmed on the VPS (orchestrator PID 753): ****`ACTIVE_SET_PATH`**** unset → running on the 1,848 unvalidated set.** Paper account, so no capital lost — but the paper run to date validates nothing, and going live in this state would risk real money on strategies with null edge metrics.
Selection weaknesses in `scripts/backtest_strategies.py` (the actual selector, which writes `active_set.json`):
- Single chronological 70/30 split — **not** a rolling walk-forward, despite the label. The rolling engine (`backtest/walk_forward.py`) exists but does not feed live.
- Intraday OOS ≈ 2–3 weeks: yfinance caps 5m/15m at 60 days; PASS allowed on as few as 10 test trades.
- No transaction costs / slippage modeled; entry at bar close, exits at exact stop/target.
- Selection data is yfinance; live executes on Alpaca — different feed and fills.
- 158 PASS from \~2,050 trials with no multiple-testing correction.
### Required before live (revised, ordered)
1. **Config fix:** set `ACTIVE_SET_PATH=…/data/backtest/active_set.json` on the orchestrator (systemd) and restart, so the gate is the validated set, never the paper set.
2. **Re-validate the 158** with DSR + PBO (per timeframe), realistic transaction costs, consistent Alpaca intraday history (not yfinance's 60-day cap), and ideally the rolling `walk_forward.py` engine instead of the single split.
3. **Then** go live at minimum size with a P&L kill-switch independent of the Guardian/infra watchdog.
Tooling delivered 2026-05-31: `validate_active_set.py` (per-timeframe DSR/PBO on the regenerated per-trade OOS R-multiples, reusing the selector's own signal + simulation code).

## Mentor Doctrine

# 🧭 Mentor Doctrine — v1.0

**Purpose:** Mentor-layer pushback on Harrison's analyst practice — the hard calls that don't fit in daily workflow but compound over quarters. Review every first Monday alongside the Analyst Discipline Checklist.
This is not a checklist. It's a set of positions that should be actively defended or revised — not passively read.

---
## 1. Over-engineering framework, under-engineering calibration
**Position:** Harrison has two analytical frameworks (AIBQ, \$100B Entry Fee) and zero calibration data. That ordering is backwards.
**Why it matters:** An LP or Morningstar editor can dismiss a pretty rubric. They cannot dismiss 90 days of Brier \<0.15. Frameworks are worth what their forecasts score — nothing more.
**Rule:** No new analytical framework ships externally until the Forecast Calibration Log has 90 days of resolved forecasts and Brier \<0.15 for at least one horizon (near / mid / contrarian).
**Status:** Q1 2026 — calibration log created April 16, 2026. First eligibility date for external framework publication: July 15, 2026.

---
## 2. Publication rhythm discipline
**Position:** An institutional analyst who ships one meaningful report per quarter compounds brand. One who ships two a year doesn't. Each quarter must have a named, committed report topic.
**Cadence:**

| Quarter | Report | Status |
| --- | --- | --- |
| Q1 2026 | Ranking the AI Giants: A New Framework for the Frontier Five | Shipped March 4 |
| Q2 2026 | The \$100 Billion Entry Fee: The Cost Architecture That Wall Street Isn't Pricing | In production |
| Q3 2026 | **TBD — name by end of April 2026** | Unnamed |
| Q4 2026 | **TBD — name by end of July 2026** | Unnamed |

**Q3 2026 candidates (pick one by April 30):**
1. **The Compute Independence Gap: Why Frontier Model Owners Are Quietly Taping Out Silicon** — follows the AIBQ CI dimension into primary-source territory (10-Qs, job postings, patent filings). Leverages NEXUS.
2. **The Secondary Market as Leading Indicator: Three Frontier-Five Valuations Priced In 90 Days Early** — uses Caplight/Forge/Hiive weekly tracker (once 90 days of data exist) to show secondary-market predictive power. Directly demonstrates analyst edge.
3. **The Post-Mythos Cybersecurity Stack: Who Gets Paid When Defense = Token Spend** — second-order public-equity analysis (CRWD, PANW, ZS, S) tied to Mythos / Project Glasswing. High media value.
**Rule:** If Q3 topic isn't named by April 30, default to option 2 (Secondary Market) because it self-validates the calibration discipline.

---
## 3. Stop citing canonical figures from memory
**Position:** Canonical figures in `harrison-project-context.md` are as of Feb 27, 2026. By April 16 that's 7 weeks stale. Citing them when PitchBook MCP, Morningstar MCP, and [Bigdata.com](http://Bigdata.com) MCP exist is a discipline failure.
**Example of the failure mode:** Morning Digest v4.1 on April 16 cited Anthropic at \$14B ARR and 500+ \$1M ACV customers — stale. Live figures were \$30B run-rate and 1,000+. The digest became wrong at the source, and every downstream conclusion was compromised.
**Rule:** Before citing any Frontier Five data point (ARR, valuation, raised, NRR, employee count, benchmark score), run one MCP call to verify. If the MCP data contradicts canonical, update canonical **immediately** with a timestamp. Never cite both without reconciliation.
**Tool preference order:**
1. PitchBook MCP — primary for private-co data
2. Morningstar MCP — primary for public-co comps
3. Aiera MCP — primary for earnings-call transcripts
4. [Bigdata.com](http://Bigdata.com) MCP — primary for sentiment and cross-reference
5. Web search — only if none of the above covers it
6. Memory — never for numeric facts

---
## 4. Forecasts are a trap if they're not scored
**Position:** Every AI newsletter has a predictions section. Nobody tracks whether the pundit was right. A 'future of AI' paragraph without calibration math is content, not analysis, and it actively damages the analyst brand over time.
**Rule:**
- Every forecast in the Morning Digest is logged to the Forecast Calibration Log before publication.
- No forecast appears in external work (LinkedIn, Morningstar, media) until the relevant horizon has Brier \<0.15 over trailing 90 days.
- The Digest v5.0 spec contains this gate in Section 6 (Forecast) and Section 7 (Forecast Calibration).
**Anti-pattern to avoid:** A section titled 'AI Future Predictions' that isn't date-stamped, probability-tagged, and invalidator-specified. That's pundit content. It doesn't go in Harrison's work, internally or externally, regardless of quarter.

---
## 5. The contrarian alpha is decaying
**Position:** AIBQ's central finding was that Anthropic was undervalued and OpenAI was overvalued relative to fundamental quality. By April 16, the secondary market has priced in \~1.8x of that gap closure for Anthropic (\$688B Caplight vs \$380B Series G). The *contrarian* position is becoming consensus.
**Implication:** The Q2 \$100B Entry Fee report cannot just be 'I was right' — that report has negative asymmetry because the market has moved. It must either (a) reframe around OpenAI's continued mispricing (where the gap is still wide), or (b) name the next mispricing that isn't yet consensus.
**Rule:** Before shipping any section of the Q2 report externally, ask: 'Is this thesis already reflected in secondary market prices?' If yes, the section is commentary, not analysis — either kill it or find the next-order insight.

---
## 6. Under-using the extended coverage universe
**Position:** Frontier Five is marketing scope. Real alpha lives in the 8 extended-universe companies that might become Frontier Five next (Perplexity, CoreWeave, Cursor, etc.). AIBQ applied weekly to the extended universe, not just daily to Frontier Five, is where the next mispricing lives.
**Rule:** Monday extended-universe sweep is non-negotiable starting April 27, 2026. Results logged to NEXUS. If a company crosses into Frontier-Five scoring territory on rubric evidence, it becomes a roster-swap candidate.

---
## 7. The boring datasets matter more than news
**Position:** Most coverage surprises are visible in EIA power data / BLS tech employment / PPI services / LinkedIn job postings / GitHub commit cadence *before* they show up as news. Analysts who live on newsletters are structurally 2–8 weeks behind.
**Rule:** Five minutes a week minimum on each of: EIA electricity by state (DC power stress), BLS tech employment (layoff vs hiring pulse), PPI information services (tech pricing power), LinkedIn jobs API (headcount growth by company), Hugging Face upload cadence (pre-release product signal).
Log these in a NEXUS 'Weekly Signals' page starting week of April 20, 2026.

---
## Monthly doctrine review
First Monday of each month:
1. Read this page top to bottom.
2. Defend or revise each position. Is any position wrong? What changed?
3. Check status of Q3/Q4 report slots. Are they named?
4. Check Forecast Calibration Log status. Is Brier \<0.15 for any horizon yet?
5. Check canonical-data freshness. Last full update date?
6. Check extended-universe sweep completion rate. 4/4 Mondays last month?
If any answer is 'no' — that's the first thing to fix this month. Discipline before framework. Calibration before publication.

---
*v1.0 — Effective April 16, 2026 \| Owner: Harrison Rolfes \| Pairs with Morning Digest v5.0, AIBQ Rubric v1.0, Forecast Calibration Log v1.0, Analyst Discipline Checklist v1.0*

---

# 6. Guardian (Automation Layer)

# 🛡️ NEXUS Guardian

Status: Deployed and in production on the VPS. 248 passing tests. Several post-deploy fixes and open Notion-organization tasks outstanding.
## What it is
Multi-agent intelligence system on the VPS that reads from GitHub Actions-populated Notion databases and maintains the NEXUS Command Center. Built on top of the older NEXUS pipeline (HRPB-SA/nexus), which runs via GitHub Actions daily at 6am PT.
## Architecture \[CANONICAL\]
11 agents, 27 CLI commands, 248 passing tests. Installed on VPS at /home/nexus-guardian (NOT /home/harrison/nexus-guardian; wrong path broke cron once). Agents include: migrator, monitor (T1/T2/T3 tiers), batch_scorer, company_pages, digest, proof_chains, report_generator, research_tools, organizer. Cron schedule covers tiered monitoring (T1 four times daily, T2 Tue/Fri, T3 1st/15th), score-all after each T1, hub + company-page builds, morning digest (8am PST / 4pm UTC), unicorn batch scorer (Sun), tier refresh (Sun), weekly status (Mon). .env carries NOTION_TOKEN, two Gmail accounts ([hypdventures@gmail.com](mailto:hypdventures@gmail.com), [harrisonpbnews@gmail.com](mailto:harrisonpbnews@gmail.com)), Telegram, Anthropic key.
## Known issues / fixes on record
- Cron originally pointed at the wrong path and did not load .env; a sed fix attempt wiped the crontab once. Verify cron is correct and logs write to /home/nexus-guardian/logs/.
- Guardian did not fill in everything: filtered linked views were completed for Anthropic only; OpenAI, Databricks, xAI, SSI still need \~25 filtered views each (one-time manual filter step the API cannot do).
- Gmail App Passwords need cleanup (remove spaces in .env).
- Unicorn tracker upload (2,508 companies) pending.
- Past digests not yet written to Notion as pages.
- Company Financials not yet populated from PitchBook.
- Web search via DuckDuckGo unreliable; consider Google Custom Search API key.
## Relationship to old NEXUS
Guardian consumes the old pipeline's output (Sources DB, Companies DB, Timelines, Events, Snapshots, Trends). The broader reorganization task is to feed the old NEXUS system into NEXUS v2 cleanly. Tracked separately under the Notion Reorg work.
## Sources
Past chats: "AIBQ and PBQ rubric breakdown" (May 27), "Multi-agent company intelligence tracking system" (Mar 23).
## Session log
### 2026-05-29
Page created from past-chat synthesis. Captured the explicit list of what Guardian did not finish.
### 2026-05-30/31 (overnight) — ROOT CAUSE FOUND: Guardian was dormant 4 days; cron env bug fixed
Audit finding: Guardian had been effectively OFFLINE since \~May 27. Only monitor.log (May 27) and digest.log (May 28) existed; no scorer/freshness/validate/hub/pages/batch logs ever written. status showed 35 companies but only 5 (Frontier Five) with current scores, 0 staged events.
ROOT CAUSE: the crontab used `ENV=export $(cat .env | xargs)` then invoked `$ENV && ...` in each job. Cron does NOT re-evaluate the `$(...)` inside a variable; it string-splits and runs `export $(cat` etc, which errors ("not a valid identifier"). So .env never loaded under cron, every job died before authenticating, and wrote nothing. Agents worked fine when run manually (shell already had env), which masked it. Proved by reproducing the exact `$ENV &&` pattern and by env -i clean-shell tests.
FIX: created /home/nexus-guardian/[run.sh](http://run.sh) wrapper (cd; set -a; . .env; set +a; exec venv python -m nexus_guardian.cli "\$@"). Rewrote all 22 NEXUS cron jobs to call `$R <command>` (R=[run.sh](http://run.sh)) instead of the broken `$ENV && $VENV` chain. Triforge jobs + Sunday 2am /sbin/reboot left intact. Verified: crontab has 22 `$R` jobs; score-all and monitor run clean under `env -i` (cron-identical). System revived; jobs will fire from next scheduled slot.
NOTE confirmed (not bugs): cron daemon is enabled and survives the weekly reboot. The earlier "missing \$/typo" cron bugs I flagged were grep-wrapping artifacts, not real; full crontab was structurally fine apart from the \$ENV pattern.
OPEN / WATCH NEXT: monitor and score-all both report 0 staged events / 0 to score. Reviving cron makes the machinery RUN but the monitor may not be FINDING new intelligence to stage (possibly the known-unreliable DuckDuckGo web search). Next cycles or a manual monitor run during known news will reveal whether ingestion is actually working. This is the next thing to chase. Also still open from before: per-company filtered views (OpenAI/Databricks/xAI/SSI), Gmail App Password spaces, unicorn upload, Company Financials population.
Also tonight: v2 sync agent finally unblocked. Root cause of the 24x 404 was that config.yaml held Notion VIEW ids, not real database ids; corrected all 23 (commit 05b4e0a). The NEXUS integration (workspace "Nexus", bot id ...60bcd5) is correct and connected. v2-sync --init now resolves 23 targets. Ran digests domain: dedup works (7 SUPERSEDE within Morning Digests DB, 1 undated row to Review, 0 blind inserts) — applied. Other 11 domains (scores/financials/events/etc) still unconfirmed/unsynced. v2 sync cron still OFF by design until domains proven by hand.

---

# 7. Hub Notes

## Company Registry

# 🏢 Company Registry

Master list of every company. Current state, scores, financials, and all relations.

---
[linked view: 🏢 Company Registry database (main) — https://app.notion.com/p/02b14c9376f84097b373d1cb67aba7d8 (data source collection://a2b663e7-5ad9-4ddb-970d-0daf36715f82)]

---
## 🎯 Frontier Five Overview
*Filtered to T1 companies, sorted by composite score.*
[linked view: inline database — https://app.notion.com/p/36d5e7ad9f7f81a1bf91d1c097ef49c9 (data source collection://a2b663e7-5ad9-4ddb-970d-0daf36715f82)]

---
## 🔬 AIBQ Dimension Breakdown
*CE · RQ · CI · GO · MD side by side for Frontier Five.*
[linked view: inline database — https://app.notion.com/p/36d5e7ad9f7f81c082dbd9fa16f4f27d (data source collection://a2b663e7-5ad9-4ddb-970d-0daf36715f82)]

---
## 🏆 Quality Tier Distribution
*Companies grouped by Elite → Strong → Adequate → Developing → Distressed.*
[linked view: inline database — https://app.notion.com/p/36d5e7ad9f7f81279a8ef9ac0b18a710 (data source collection://a2b663e7-5ad9-4ddb-970d-0daf36715f82)]

---
## 📈 IPO Pipeline
*Companies grouped by filing status: S-1 Filed → Confidential → Pre-Filing → N/A.*
[linked view: inline database — https://app.notion.com/p/36d5e7ad9f7f817b8192dab591d1432b (data source collection://a2b663e7-5ad9-4ddb-970d-0daf36715f82)]

---
## 🃏 Company Cards
*Visual gallery view. Click any card to open full profile.*
[linked view: inline database — https://app.notion.com/p/36d5e7ad9f7f816db653ec00039481d3 (data source collection://a2b663e7-5ad9-4ddb-970d-0daf36715f82)]

## Financial History

# 💰 Financial History

Point-in-time financial snapshots — revenue, valuations, margins, compute.

---
[linked view: 💰 Financial History database (main) — https://app.notion.com/p/e37235761cc44a6fb29898d4ab0b9b49 (data source collection://e0291a05-0918-4cb6-bc29-ef12b248c151)]

---
## 💎 Valuation & Capital Timeline
*Primary valuations, secondary market prices, and cumulative capital raised over time.*
[linked view: inline database — https://app.notion.com/p/36d5e7ad9f7f817381e7eac7f9a69015 (data source collection://e0291a05-0918-4cb6-bc29-ef12b248c151)]

---
## 📈 Unit Economics & Profitability
*Gross margins, operating margins, FCF, NRR, and enterprise revenue mix.*
[linked view: inline database — https://app.notion.com/p/36d5e7ad9f7f81738ba4ced26fe0b581 (data source collection://e0291a05-0918-4cb6-bc29-ef12b248c151)]

---
## 🖥️ Compute & CapEx Tracker
*CapEx, compute spend, and compute obligations vs revenue. The cost architecture lens.*
[linked view: inline database — https://app.notion.com/p/36d5e7ad9f7f81a6a35fcd1524fa4a6b (data source collection://e0291a05-0918-4cb6-bc29-ef12b248c151)]

## Event Timeline

# ⚡ Event Timeline

Every event, signal, filing, and data point — chronological.

---
[linked view: ⚡ Event Timeline database (main) — https://app.notion.com/p/26886579a3c34b49b762c39050e5f701 (data source collection://a058291b-cc20-4f18-bb7e-b8cd2cc37c06)]

---
## 🔴 Critical & High Priority Events
*Filtered to Critical and High significance only. What demands attention now.*
[linked view: inline database — https://app.notion.com/p/36d5e7ad9f7f81e8af11f9d193d06c9a (data source collection://a058291b-cc20-4f18-bb7e-b8cd2cc37c06)]

---
## 📊 Events by Category
*Kanban: Funding · IPO/Filing · Model Release · Regulatory · Compute Deal · Partnership · and more.*
[linked view: inline database — https://app.notion.com/p/36d5e7ad9f7f81408cb6e136824cc7b6 (data source collection://a058291b-cc20-4f18-bb7e-b8cd2cc37c06)]

---
## 🟢🟡🔴 Sentiment Board
*Positive · Neutral · Negative. Instant read on news flow direction.*
[linked view: inline database — https://app.notion.com/p/36d5e7ad9f7f81f38f4ec22d5ec3eff7 (data source collection://a058291b-cc20-4f18-bb7e-b8cd2cc37c06)]

---
## 📅 Event Calendar
*Events plotted on a monthly calendar. Spots clustering and gaps.*
[linked view: inline database — https://app.notion.com/p/36d5e7ad9f7f8187858bfbe295847087 (data source collection://a058291b-cc20-4f18-bb7e-b8cd2cc37c06)]

## Score History

# 📊 Score History

Complete AIBQ/PBQ scoring record with all 24 sub-scores.

---
[linked view: 📊 Score History database (main) — https://app.notion.com/p/b18f2918f7144e00a897a5885ac38a3d (data source collection://557e8ac9-4300-48eb-adfe-4f79cfa0938b)]

---
## 🔬 Sub-Score Deep Dive
*All 24 sub-scores exposed: CE-1 through CE-4, RQ-1 through RQ-5, CI-1 through CI-5, GO-1 through GO-5, MD-1 through MD-5.*
[linked view: inline database — https://app.notion.com/p/36d5e7ad9f7f813f8978efb3463212b2 (data source collection://557e8ac9-4300-48eb-adfe-4f79cfa0938b)]

---
## 🏆 Score Entries by Quality Tier
*Scoring events grouped by tier at time of scoring. Shows tier migration over time.*
[linked view: inline database — https://app.notion.com/p/36d5e7ad9f7f81169be3f537f09f32dc (data source collection://557e8ac9-4300-48eb-adfe-4f79cfa0938b)]

## Signal Processing

# ⚡ Signal Processing

Event feeds, master events, sources, review queue, benchmark trends, regulatory risk, and customer win/loss tracking. The signal ingestion layer.

[linked view: 🔗 Sources database — https://app.notion.com/p/3285e7ad9f7f80b5a3e3d6e897156721 (data source collection://3285e7ad-9f7f-8015-b497-000bccb09a2c)]
[linked view: ⚡ Events database — https://app.notion.com/p/3285e7ad9f7f80b68ecfe18839ceb7ab (data source collection://3285e7ad-9f7f-8011-8682-000b88fe3d31)]
[linked view: ⚠️ Review Queue database — https://app.notion.com/p/3285e7ad9f7f801898ebfcdea222396f (data source collection://3285e7ad-9f7f-8066-b076-000b6cf7523e)]
[linked view: 🌐 Master Events database — https://app.notion.com/p/3295e7ad9f7f8131a872dee7ae283d6f (data source collection://3295e7ad-9f7f-8139-bdd7-000b2e1dd4f0)]
[linked view: 🏅 Benchmark Trends database — https://app.notion.com/p/d9cfabe7c35b45fe974e9998962feea9 (data source collection://7ee8254c-46db-43f5-8623-240d7b7aa78b)]
[linked view: ⚖️ Regulatory Risk Tracker database — https://app.notion.com/p/24629b3403db4b239a2e1a41b53777c1 (data source collection://07988400-4611-4c37-b39a-de6a5eb3b62e)]
[linked view: 🏆 Customer Win/Loss Tracker database — https://app.notion.com/p/9250681831894a30bff422cf178be35a (data source collection://dfca1ba3-bae0-4e13-9826-6c77006c24d8)]
[linked view: 🧑‍💼 Talent Flow Tracker database — https://app.notion.com/p/bd4092f34ee448de84c0bc17bbaa182b (data source collection://f05024e4-f8fc-4437-ae25-d7f29df2faca)]
[linked view: ⚖️ Litigation & IP Tracker database — https://app.notion.com/p/5f68dc4aa3b441b9a4828f5d1e724196 (data source collection://f45204fd-132b-4a19-9732-62f7c62a0395)]
[linked view: inline database (Regulatory Risk view) — https://app.notion.com/p/3575e7ad9f7f81658117c48f6db8206e (data source collection://07988400-4611-4c37-b39a-de6a5eb3b62e)]
[linked view: inline database (Talent Flow view) — https://app.notion.com/p/3575e7ad9f7f817cb09efa4876bcce21 (data source collection://f05024e4-f8fc-4437-ae25-d7f29df2faca)]
[linked view: inline database (Benchmark Trends view) — https://app.notion.com/p/3575e7ad9f7f811bb4dff56a82521a68 (data source collection://7ee8254c-46db-43f5-8623-240d7b7aa78b)]
[linked view: inline database (Litigation & IP view) — https://app.notion.com/p/3575e7ad9f7f8129aa95dec6f7c4e4ed (data source collection://f45204fd-132b-4a19-9732-62f7c62a0395)]
[linked view: 📅 Earnings & Events Calendar database — https://app.notion.com/p/f04e6c866eb146ae90eb2682af06d580 (data source collection://d93289d9-740e-49ad-981c-66979c0202dc)]
- [📌 Canonical Evidence Ledger](https://app.notion.com/p/35e5e7ad9f7f8144af58e92230136abd)
[linked view: 📌 Evidence Ledger database — https://app.notion.com/p/2f8d6f2e6034456b9b6214b86f030dcd (data source collection://6289e808-53cd-4a0c-a51a-28701f150959)]
[linked view: 🏗️ Compute Infrastructure Registry database — https://app.notion.com/p/f0e7c27b68f742c6b76645a122892dbd (data source collection://0f02b7db-50e2-4ce9-8b07-f418f87f25a0)]
[linked view: 🤝 Partnership & Alliance Registry database — https://app.notion.com/p/176f5fa2cd084050aa57839c60b3ff64 (data source collection://f32a7d7c-558a-4164-ac47-c6622c0afc57)]

## Research & Output

# 📋 Research & Output

Digests, reports, media interviews, publications.

---
[linked view: 📋 Research & Output database (main) — https://app.notion.com/p/6ec0ca6e6741422cbb5f5408384f9640 (data source collection://df3f414d-582b-4fa3-9141-21b57b5cafb4)]

---
## 📋 Research by Type
*Kanban: Morning Digest · Weekly Rollup · Research Report · Media Interview · LinkedIn Post · Article.*
[linked view: inline database — https://app.notion.com/p/36d5e7ad9f7f81c2a70bef1d1e52d70b (data source collection://df3f414d-582b-4fa3-9141-21b57b5cafb4)]

---
## 📌 Research Pipeline
*Kanban: Published · Draft · In Progress · Archived. Pipeline visibility.*
[linked view: inline database — https://app.notion.com/p/36d5e7ad9f7f81af8223e874a3c97415 (data source collection://df3f414d-582b-4fa3-9141-21b57b5cafb4)]

---
## 📅 Publication Calendar
*Publications plotted on a monthly calendar. Spots output velocity and gaps.*
[linked view: inline database — https://app.notion.com/p/36d5e7ad9f7f81dab091c929b0ede246 (data source collection://df3f414d-582b-4fa3-9141-21b57b5cafb4)]

---
## 🎤 Media Appearances
*Filtered to media interviews only. Outlet, reporter/contact, engagement metrics.*
[linked view: inline database — https://app.notion.com/p/36d5e7ad9f7f812cac81ec8caed18cc4 (data source collection://df3f414d-582b-4fa3-9141-21b57b5cafb4)]

## Operations & Meta

# 🔧 Operations & Meta

Run log, NEXUS trends, daily audit dashboard, analyst discipline checklist, and mentor doctrine. Platform operational tools.

[linked view: 📊 Run Log database — https://app.notion.com/p/3295e7ad9f7f81bab227cfb10e6c1236 (data source collection://3295e7ad-9f7f-811f-8929-000b973a6c40)]
[linked view: 📈 NEXUS Trends database (untitled in page body) — https://app.notion.com/p/32d5e7ad9f7f80deb393f5a8b54da3be (data source collection://32d5e7ad-9f7f-801d-b641-000bdf851879)]
- [✅ Daily Audit Dashboard](https://app.notion.com/p/3445e7ad9f7f81839302c6559cb34814)
- [🎓 Analyst Discipline Checklist — v1.0](https://app.notion.com/p/3445e7ad9f7f815e962bcec08deb33c6)
- [🧭 Mentor Doctrine — v1.0](https://app.notion.com/p/3445e7ad9f7f81e883f9f2d6a1d0f139)
- [📖 NEXUS Output Playbook](https://app.notion.com/p/3575e7ad9f7f81d28baef87bba3007dc)
[linked view: 📦 Build Prompt Backlog database — https://app.notion.com/p/f5b0bf66a6f04a75a49e745b838be152 (data source collection://db0f9ea8-5aaa-49a3-bfb7-43afd32c289d)]

## Continuity System

# 🗂️ Continuity System — Setup

Status: Active. Established 2026-05-29.
## Objective
Give Claude true cross-session continuity by storing project context as Notion pages under the Continuity Log hub, readable and writable via the Notion MCP connector.
## Why Notion and not a file
A README written to Claude's sandbox does not persist into Claude's context. The container resets between sessions and nothing on disk is fed back automatically. Notion pages are the only option Claude can read back across sessions without Harrison manually re-supplying them. Built-in Claude memory also runs in parallel and already carries core context, but it is auto-generated and not directly editable as structured project state.
## Architecture
Hub page: Continuity Log, under the Nexus main page (CLAUDE MEMORY section). Holds routing rules and the project index. One child page per active project. Claude reads the relevant page at session start, appends a dated entry at session end.
## Routing rule
Append to an existing project page when work continues that project's thread. Create a new page for a distinct objective, deliverable, or lifecycle. When ambiguous, Claude names the page it chose and why.
## Open decisions
1. Whether to back-fill dedicated pages for the known active projects (OpenAI S-1 coverage, NEXUS Guardian, Triforge, Unicorn Scores, AIBQ v3.0, CFA Level I) now, or create each lazily when first worked on. Current default: create lazily to avoid clutter.
## Session log
### 2026-05-29
Built the Continuity Log hub under NEXUS Command Center and this first project page. Confirmed Notion as the continuity mechanism over a sandbox README. Established the append-vs-new routing rule. Awaiting Harrison's call on lazy vs back-filled project pages.
### 2026-05-29 (later)
Consolidated the structure. Claude Memory is now the single hub: it holds the routing rules, lazy-creation policy, and project index. The separate Continuity Log page was retired (redirect only) since its role overlapped. This Setup page is now the first project page directly under Claude Memory. Hierarchy: Nexus \> Claude Memory \> \[project pages\].

# 🗄️ Continuity Log (retired — see Claude Memory)

> RETIRED. This page's role has been folded into its parent, the Claude Memory page. Routing rules and the project index now live there. Kept only as a redirect; do not maintain content here.

## Claude Memory (session continuity notes)

# 🧠 Claude Memory

> Home for Claude's persistent, cross-session memory. One page per project lives inside here. Claude reads the relevant project page at session start for cold-start context, and appends a dated entry at session end.
## What this is
A durable, MCP-readable record of what Harrison and Claude are building and where each thread left off. Unlike a sandbox file, Claude can read and write these pages across sessions through the Notion connector. This is the real continuity layer. Built-in Claude memory runs in parallel and already carries core context, but it is auto-generated and not directly editable as structured project state.
## How Claude uses it
Session start: pull the relevant project page for cold-start context. Session end: append a dated entry to that page. Entries are verdict-first and data-anchored. \[CANONICAL\] for verified figures, \~ for estimates, (est.) for projections. No em dashes.
## Routing rule: append vs new page
Append to an existing project page when the work continues that project's thread (same system, same deliverable, same thesis). Create a new project page under Claude Memory when the work has a distinct objective, a separate deliverable, or its own lifecycle that would clutter an existing page. When ambiguous, Claude states which page it chose and why, so Harrison can redirect.
## Project page creation: lazy by default
Project pages are created the first time a project is actually worked on in a session, not pre-stubbed. Reason: a page born from real work is accurate on day one, whereas back-filled stubs go stale immediately and clutter the hub.
## Project pages
- [🗂️ Continuity System — Setup](https://app.notion.com/p/3705e7ad9f7f812b92cad187314c7c1b)
- [📈 Signal Nine](https://app.notion.com/p/3705e7ad9f7f814fa113e9158177096a)
- [⚡ Triforge](https://app.notion.com/p/3705e7ad9f7f81099212df63a77cbfe5)
- [🛡️ NEXUS Guardian](https://app.notion.com/p/3705e7ad9f7f814fad73e6c158707b76)
- [🚀 HYPD Ventures](https://app.notion.com/p/3705e7ad9f7f810c98e2c2bdf1471ad2)
- [🔍 NEXUS Reorg — Diagnosis](https://app.notion.com/p/3705e7ad9f7f819fafc3ff858eb774e5)
- [🔄 NEXUS Reorg — Sync Agent Design](https://app.notion.com/p/3705e7ad9f7f817d8d78efe303044e73)
## Known active projects (no page until first worked on)
OpenAI S-1 coverage / An Eye on OpenAI; NEXUS Guardian; Triforge; Unicorn Scores Project; AIBQ v3.0 framework; CFA Level I.
- [🗄️ Continuity Log (retired — see Claude Memory)](https://app.notion.com/p/3705e7ad9f7f81f3bba3f6f34163da37)

---

# 8. Workspace Root Map

# Nexus

- [NEXUS v2 — Clean Architecture](https://app.notion.com/p/36d5e7ad9f7f81d6848ef18f305ae8c8)
- [NEXUS Command Center](https://app.notion.com/p/36d5e7ad9f7f81b58e5cdc4e8e9ed122)
[linked view: inline database — https://app.notion.com/p/3285e7ad9f7f804e919fcd2bcf2b141e (data source collection://3285e7ad-9f7f-8035-b0e0-000ba97cd145)]
- [📊 AIBQ Analytics](https://app.notion.com/p/3575e7ad9f7f8154a928ca135fd9f909)
- [🧮 AIBQ/PBQ v3.0 Framework](https://app.notion.com/p/36c5e7ad9f7f815aa453f19a160fb882)

---
<empty-block/>

## Personal Projects
- [🎓 CFA Level I — Study Rotation · December 2026](https://app.notion.com/p/3475e7ad9f7f81e990a2fcaad096733b)
[linked view: 🎓 CFA Progress Tracker database — https://app.notion.com/p/2c627c9f9e534bf891479d2796ca5fba (data source collection://97f18666-7087-4e57-aeca-adff5273df83)]
- [HYPD Ventures — VC Fund Formation Roadmap](https://app.notion.com/p/3505e7ad9f7f817ebc3bd0e31d08d174)
[linked view: 🚀 HYPD Deal Pipeline database — https://app.notion.com/p/b3dfadf09b6c415f8b86ffa33a9233f5 (data source collection://e82a7c2a-f7aa-4e5e-96cf-c36885d6e933)]
- [🔺 triforge](https://app.notion.com/p/3605e7ad9f7f81afa55be30553da363e)
[linked view: 💹 Second-Order Trade Tracker database — https://app.notion.com/p/9eacdf96930f4be594ea1c7c2213795a (data source collection://7fcbc908-b215-4de6-aa0c-67516def4b78)]

---
## Analytical Infrastructure
- [📅 Company Timelines](https://app.notion.com/p/3575e7ad9f7f81adaaa7eb9e5e153c3f)
- [💰 Financial Intelligence](https://app.notion.com/p/3575e7ad9f7f816f8a8cf8f5cc27c59b)
- [🔮 Forecasting & Calibration](https://app.notion.com/p/3575e7ad9f7f81b5bf62dbd5ae052d72)
- [📋 Research & Reports](https://app.notion.com/p/3575e7ad9f7f8139a8a5fe8cf6e0a0a6)
- [📬 Morning Digest](https://app.notion.com/p/3575e7ad9f7f81e29a74eb31b2767004)
- [🔧 Operations & Meta](https://app.notion.com/p/3575e7ad9f7f8102af47d580797ab97f)
- [🏢 Company Profiles](https://app.notion.com/p/3575e7ad9f7f81b39a1fe648007cb233)
- [🌍 State of the Universe](https://app.notion.com/p/3575e7ad9f7f814e8fdedf449407a433)
- [🔍 NEXUS Data Audit — May 6, 2026 (PitchBook + Multi-Source Reconciliation)](https://app.notion.com/p/3585e7ad9f7f812987dfe3c92e1e5eb3)

CLAUDE MEMORY
- [Claude Memory](https://app.notion.com/p/3705e7ad9f7f819fb868ea5d0c896e17)
- [🏛️ NEXUS Command Center](https://app.notion.com/p/3715e7ad9f7f81408da3fb62561b76eb)
- [🚀 HYPD Startup List](https://app.notion.com/p/3805e7ad9f7f817d9463db8c21046544)
- [Layer H Ventures — CRM](https://app.notion.com/p/38a5e7ad9f7f819d9b05fbebe1707d78)
- [Layer H Ventures — CRM (1)](https://app.notion.com/p/3a75e7ad9f7f82bfaa4b01c3c733ae58)
- [🏛️ NEXUS Canon](https://app.notion.com/p/3a45e7ad9f7f811486d1f9776aa3680e)

---

## Adjacent systems in this workspace (not company research)

Three other systems live in the same Notion workspace, sourced but kept
out of scope for this company-intelligence mirror since they are not
company research: **triforge**, a multi-agent trading system (build plan
with gated milestones, DSR/PBO validation checkpoints); **Signal Nine**,
a separate rules-based trading strategy playbook (best backtest: RSI(2)
mean-reversion on SPY); and the **HYPD Ventures fund-formation** materials
(AngelList mechanics, brand/website specs, ops manuals) alongside the
active HYPD deal pipeline, which *is* company-adjacent and lives in
`../hypd/`. Full extracts of all three are preserved in this repo's build
history for anyone who wants them; they are not reproduced here.

---
*Mirrored from Notion 2026-08-11.*
