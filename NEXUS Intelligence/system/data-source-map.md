# Data Source Map

Every Notion database (data source) discovered across the Nexus workspace
during the 2026-08-11 extraction sweep, grouped by architectural layer,
with row counts as captured and where each landed in this repo. Use this
to re-run a future refresh: pass the `collection://` id to
`notion-query-data-sources` in view mode.

Two databases could not be enumerated here because they returned no rows
under any extraction: `benchmark-trends`, `compute-infrastructure-registry`,
`customer-win-loss-tracker`, `events`, `evidence-ledger`, `regulatory`,
`score-history`, and `weekly-rollup` are all genuinely empty (verified
active + archived), not extraction failures — they are v2/shared
databases created ahead of the data that was meant to populate them.

## Company Timelines (legacy per-company, superseded by v2 Event Timeline)

| Database | Collection ID | Rows | Repo path |
| --- | --- | --- | --- |
| Anthropic — Timeline | `3285e7ad-9f7f-8130-ad84-000ba378c44b` | 6883 | `extract/timelines/anthropic.json` (staging) |
| Cohere — Timeline | `3285e7ad-9f7f-8143-8280-000b62fb6141` | 1559 | `extract/timelines/cohere.json` (staging) |
| CoreWeave — Timeline | `3285e7ad-9f7f-8185-ad52-000b0ddd3a23` | 4080 | `extract/timelines/coreweave.json` (staging) |
| Cursor — Timeline | `3285e7ad-9f7f-8147-97b6-000b3a7a865a` | 2389 | `extract/timelines/cursor.json` (staging) |
| Databricks — Timeline | `3285e7ad-9f7f-81a9-8685-000b146cf8b8` | 2000 | `extract/timelines/databricks.json` (staging) |
| ElevenLabs — Timeline | `3285e7ad-9f7f-8170-abb3-000b00ad0fc3` | 1393 | `extract/timelines/elevenlabs.json` (staging) |
| Mistral AI — Timeline | `3285e7ad-9f7f-81ce-8e6d-000b73882e07` | 2199 | `extract/timelines/mistral.json` (staging) |
| OpenAI — Timeline | `3285e7ad-9f7f-81fc-8629-000bfb3031e8` | 6875 | `extract/timelines/openai.json` (staging) |
| OpenEvidence — Timeline | `3285e7ad-9f7f-81b2-ba3a-000b596e7462` | 822 | `extract/timelines/openevidence.json` (staging) |
| Perplexity — Timeline | `3285e7ad-9f7f-8142-a1d2-000b55095ab4` | 700 | `extract/timelines/perplexity.json` (staging) |
| Safe Superintelligence — Timeline | `3285e7ad-9f7f-81a3-b842-000be49eed55` | 800 | `extract/timelines/ssi.json` (staging) |
| Scale AI — Timeline | `3285e7ad-9f7f-81d5-9948-000b41bfbcc5` | 700 | `extract/timelines/scale-ai.json` (staging) |
| xAI — Timeline | `3285e7ad-9f7f-815c-8a7c-000be9b2d0de` | 800 | `extract/timelines/xai-spacex.json` (staging) |

## v2 spine + Signal Processing

| Database | Collection ID | Rows | Repo path |
| --- | --- | --- | --- |
| benchmark-trends | `7ee8254c-46db-43f5-8623-240d7b7aa78b` | 0 | `extract/v2/benchmark-trends.json` (staging) |
| company-registry | `a2b663e7-5ad9-4ddb-970d-0daf36715f82` | 13 | `extract/v2/company-registry.json` (staging) |
| compute-infrastructure-registry | `0f02b7db-50e2-4ce9-8b07-f418f87f25a0` | 0 | `extract/v2/compute-infrastructure-registry.json` (staging) |
| customer-win-loss-tracker | `dfca1ba3-bae0-4e13-9826-6c77006c24d8` | 0 | `extract/v2/customer-win-loss-tracker.json` (staging) |
| event-timeline-v2 | `a058291b-cc20-4f18-bb7e-b8cd2cc37c06` | 52 | `extract/v2/event-timeline-v2.json` (staging) |
| events | `3285e7ad-9f7f-8011-8682-000b88fe3d31` | 0 | `extract/v2/events.json` (staging) |
| evidence-ledger | `6289e808-53cd-4a0c-a51a-28701f150959` | 0 | `extract/v2/evidence-ledger.json` (staging) |
| financial-history | `e0291a05-0918-4cb6-bc29-ef12b248c151` | 84 | `extract/v2/financial-history.json` (staging) |
| master-events | `3295e7ad-9f7f-8139-bdd7-000b2e1dd4f0` | 238 | `extract/v2/master-events.json` (staging) |
| partnership-alliance-registry | `f32a7d7c-558a-4164-ac47-c6622c0afc57` | 6 | `extract/v2/partnership-alliance-registry.json` (staging) |
| review-queue | `3285e7ad-9f7f-8066-b076-000b6cf7523e` | 200 | `extract/v2/review-queue.json` (staging) |
| score-history | `557e8ac9-4300-48eb-adfe-4f79cfa0938b` | 0 | `extract/v2/score-history.json` (staging) |
| sources | `3285e7ad-9f7f-8015-b497-000bccb09a2c` | 200 | `extract/v2/sources.json` (staging) |
| talent-flow-tracker | `f05024e4-f8fc-4437-ae25-d7f29df2faca` | 7 | `extract/v2/talent-flow-tracker.json` (staging) |

## AIBQ Analytics

| Database | Collection ID | Rows | Repo path |
| --- | --- | --- | --- |
| AIBQ/PBQ Daily Scores | `23e3c951-fb7a-4c66-bae9-d6a8003a3b33` | 519 | `extract/aibq/aibq-pbq-daily-scores.json` (staging) |
| Company Comparisons | `3295e7ad-9f7f-8103-ab46-000b452c302f` | 13 | `extract/aibq/company-comparisons.json` (staging) |
| Company Snapshots | `32c5e7ad-9f7f-8056-9f5b-000b3503de0d` | 1564 | `extract/aibq/company-snapshots.json` (staging) |
| Model Release Registry | `2debb0e6-fa0f-444f-b3a4-d30d48b561ca` | 15 | `extract/aibq/model-release-registry.json` (staging) |
| Unicorn Intel Database | `891561be-fa0a-41b6-8954-8c8d4e657db6` | 87 | `extract/aibq/unicorn-intel-database.json` (staging) |
| unicorn-scores | `6407d6b8-81ee-4ffa-afd0-ddeab063a6af` | 666 | `extract/aibq/unicorn-scores.json` (staging) |

## v3.0 Framework data layer

| Database | Collection ID | Rows | Repo path |
| --- | --- | --- | --- |
| AIBQ Event Impact Matrix | `c9df673a-b3ba-4148-b490-d7f911a9c66a` | 125 | `extract/framework/event-impact-matrix.json` (staging) |
| Benchmarks | `587eb11b-d7f4-4ea1-89a1-7e2d8f54dbff` | 7 | `extract/framework/benchmarks.json` (staging) |
| Company Financials | `73041ac9-2b45-4ebd-8bca-9f3966764730` | 17 | `extract/framework/company-financials.json` (staging) |
| Proof Chains | `c5cf02aa-843d-42ca-b58f-de6ed059efbb` | 0 | `extract/framework/proof-chains.json` (staging) |
| Source Registry | `0486aec7-0702-4567-b62d-3d6db5f14a8c` | 15 | `extract/framework/source-registry.json` (staging) |

## Shared financial/market/research trackers

| Database | Collection ID | Rows | Repo path |
| --- | --- | --- | --- |
| ai-financial-model | `32f5e7ad-9f7f-814b-a4c7-000b7b95fbb9` | 67 | `extract/shared/ai-financial-model.json` (staging) |
| AI_Cost_Intelligence | `32f5e7ad-9f7f-81ca-bfd3-000b0e4c8efb` | 70 | `extract/shared/ai-cost-intelligence.json` (staging) |
| aibq-scores | `3295e7ad-9f7f-8157-9b51-000b524abcc2` | 77 | `extract/shared/aibq-scores.json` (staging) |
| cap-table | `6320402a-0717-483c-a975-80d1cd2e63e4` | 14 | `extract/shared/cap-table.json` (staging) |
| Cost Architecture Tracker | `382c7c5d-bcab-4568-be44-348b5a89724c` | 16 | `extract/shared/cost-architecture.json` (staging) |
| events-calendar | `d93289d9-740e-49ad-981c-66979c0202dc` | 16 | `extract/shared/events-calendar.json` (staging) |
| financial-model-inputs | `3295e7ad-9f7f-8127-8d5b-000b878b6450` | 143 | `extract/shared/financial-model-inputs.json` (staging) |
| forecasts | `eb782ae4-66c6-4c8c-b5e6-cf2d9b070b27` | 96 | `extract/shared/forecasts.json` (staging) |
| Hyperscaler Capex Tracker | `d798f498-4c31-40f5-8a58-e69579ad12fe` | 10 | `extract/shared/hyperscaler-capex.json` (staging) |
| IPO Pipeline Tracker | `cf97d177-bb20-4695-8c27-87ee67c446dd` | 4 | `extract/shared/ipo-pipeline.json` (staging) |
| litigation | `f45204fd-132b-4a19-9732-62f7c62a0395` | 12 | `extract/shared/litigation.json` (staging) |
| media-outreach | `0c2b8f65-a545-41d4-931d-37ef618db9f0` | 9 | `extract/shared/media-outreach.json` (staging) |
| morning-digests-db | `448c36ae-83f9-4e1e-914d-c849eb661c09` | 95 | `extract/shared/morning-digests-db.json` (staging) |
| regulatory | `07988400-4611-4c37-b39a-de6a5eb3b62e` | 0 | `extract/shared/regulatory.json` (staging) |
| report-data-points | `3295e7ad-9f7f-8137-a72e-000b8b404d4a` | 29 | `extract/shared/report-data-points.json` (staging) |
| research-notes | `3295e7ad-9f7f-8119-8112-000b4dde917c` | 3 | `extract/shared/research-notes.json` (staging) |
| research-reports | `3295e7ad-9f7f-8154-814f-000b0b961d44` | 21 | `extract/shared/research-reports.json` (staging) |
| Revenue Decomposition | `d417c437-4e3a-4bd1-b527-1db656dde545` | 3 | `extract/shared/revenue-decomposition.json` (staging) |
| secondary-prices | `caf7af0b-cbba-46be-89c7-92f17b30c49d` | 1 | `extract/shared/secondary-prices.json` (staging) |
| thesis-registry | `0f515343-b25f-4bf8-a068-93b951504797` | 6 | `extract/shared/thesis-registry.json` (staging) |
| valuations | `5499d772-ec48-4778-b048-da32040718cb` | 18 | `extract/shared/valuations.json` (staging) |
| weekly-rollup | `920f9702-717c-4eef-9d3f-1be325e70034` | 0 | `extract/shared/weekly-rollup.json` (staging) |

## Canon (governance)

| Database | Collection ID | Rows | Repo path |
| --- | --- | --- | --- |
| Artifacts Registry | `996c8965-8689-42c6-9817-54e43f57b2b7` | 12 | `extract/canon/artifacts-registry.json` (staging) |
| Canonical Figures | `71a4735c-c2ba-44db-bece-0a05e824e923` | 62 | `extract/canon/canonical-figures.json` (staging) |
| Citations | `d6b88d4b-b0c4-4140-bb93-7c27b540942a` | 14 | `extract/canon/citations.json` (staging) |
| Company Dossiers | `51208b99-20dd-41e3-b84f-e453b97b12e9` | 15 | `extract/canon/company-dossiers.json` (staging) |
| Conflict Register | `ade8a2b2-15f0-4fac-ac8b-0898837771ed` | 6 | `extract/canon/conflict-register.json` (staging) |
| Database Registry | `fa97292e-53a4-43b9-af74-873f7510c5c8` | 12 | `extract/canon/database-registry.json` (staging) |
| Decision Journal | `17681dc8-46a2-481c-929a-4143071261e8` | 0 | `extract/canon/decision-journal.json` (staging) |
| Media CRM | `a28787dc-879c-4800-8893-f8f69f458120` | 0 | `extract/canon/media-crm.json` (staging) |
| Rulings & Embargoes | `274226ec-7c65-4180-8bd9-178efec3fd76` | 6 | `extract/canon/rulings-embargoes.json` (staging) |
| Source Authority Registry | `1ae57124-ef8c-4a43-abe9-0c4964a9ba5f` | 95 | `extract/canon/source-authority-registry.json` (staging) |
| Sweep Tracker | `2a96b85d-28a1-4d23-b4b4-58430854d770` | 2 | `extract/canon/sweep-tracker.json` (staging) |
| Trigger Registry | `2605ea25-56e4-46a0-b1c6-73bfec815e1e` | 7 | `extract/canon/trigger-registry.json` (staging) |

## Command Center

| Database | Collection ID | Rows | Repo path |
| --- | --- | --- | --- |
| Master Company Profiles | `2392a658-aa6d-4871-a5fc-ac5874e00f02` | 5 | `extract/command-center/master-company-profiles.json` (staging) |
| Master Intelligence Feed | `84ebba22-38b5-437e-a142-4cd7ca5ff4b5` | 12 | `extract/command-center/master-intelligence-feed.json` (staging) |

## Legacy master Companies DB

| Database | Collection ID | Rows | Repo path |
| --- | --- | --- | --- |
| legacy-companies | `3285e7ad-9f7f-8035-b0e0-000ba97cd145` | 15 | `extract/legacy-companies/companies.json` (staging) |

## HYPD pipeline

| Database | Collection ID | Rows | Repo path |
| --- | --- | --- | --- |
| HYPD Deal Pipeline | `e82a7c2a-f7aa-4e5e-96cf-c36885d6e933` | 3 | `extract/hypd/deal-pipeline.json` (staging) |
| HYPD LP Database | `1ca4f50d-ea4b-477b-abee-283b4dd9993b` | — | `extract/hypd/fund-formation--lp-database.json` (staging) |
| Second-Order Trade Tracker | `7fcbc908-b215-4de6-aa0c-67516def4b78` | 0 | `extract/hypd/second-order-trades.json` (staging) |

**78 databases catalogued, 36,004 total rows captured across all of them** (a company's own count of its dated/deduped events differs from these raw totals — see each company's profile).

---
*Built 2026-08-11 from the extraction manifest. Repo paths under `extract/` refer to this build's staging area, not a folder shipped in the final repo — the cleaned, redacted, organized versions are what ship under `companies/`, `system/`, `digests/`, `markets-and-research/`, and `excel/`.*
