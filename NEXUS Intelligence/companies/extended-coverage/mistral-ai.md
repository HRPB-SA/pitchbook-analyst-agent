# Mistral AI — NEXUS Intelligence Profile

**Coverage tier:** Extended Coverage (not Frontier Five) | **Sector:** Foundation Models | **Profile as of:** 2026-08-11

---

## (a) Overview

Mistral AI was founded in April 2023 in Paris by Arthur Mensch (ex-DeepMind, CEO), Timothée Lacroix and Guillaume Lample (both ex-Meta FAIR; Lample co-created LLaMA). The company builds frontier language models under a stated mission of efficiency and openness, and has positioned itself as Europe's sovereign-AI champion — the only European frontier-adjacent lab in this coverage cohort. It operates from Paris (HQ), London, and San Francisco, and reports 687 employees as of the most recent tracker refresh (up from roughly 150 in March 2026 and roughly 100 a year prior).

The product line spans open-weight releases (Mistral 7B, Mixtral 8x7B, the Small family) and closed commercial models (Mistral Large/Large 2, Medium 3/3.5) sold through an API business, alongside Le Chat (consumer chat, plus Le Chat Enterprise), Forge (custom enterprise model training), Vibe (an agent and coding-agent platform), Voxtral (open-weight text-to-speech), OCR 4, Robostral Navigate (a robotics/physical-AI foundation model), and Shieldstral (an open-weight safety classifier). Disclosed enterprise customers include ABN Amro, BNP Paribas, and HSBC; the French government has deployed a Mistral assistant to its civil service and, per an AMIAD-piloted agreement, to military use; Morocco's Digital Transition Ministry, Singapore's HTX, TCS, and CI&T round out the named customer/partner list. A multibillion-dollar Microsoft Azure sovereign-cloud infrastructure deal was signed in July 2026.

Mistral is EU AI Act-aligned and GDPR-compliant by design per its own positioning; Italy separately required hallucination-warning disclaimers on the chat interface (reported February 2026, unverified tier). CEO Arthur Mensch has publicly pushed for an EU-wide levy on large AI operators to fund the cultural sector — a policy position, not a legal action against the company.

## (b) Current scores

Mistral AI carries **AIBQ composite 4.55 ("Developing")**, dated **2026-05-12**, confidence **Medium** — sourced from the AI Ecosystem score page (`framework/companies/mistral-ai.md`) and cross-matched to the underlying scoring row.

| CE | RQ | CI | GO | MD |
|----|----|----|----|----|
| 3.0 | 4.0 | 5.0 | 6.0 | 5.0 |

*(CE = Capital Efficiency, RQ = Revenue Quality, CI = Compute Independence, GO = Governance Optionality, MD = Moat Durability.)*

**No prior AIBQ score exists in the supplied data** — this 2026-05-12 print is the only dated AIBQ composite found for Mistral AI, so no trend can be reported; stated plainly rather than backfilled.

A companion "PBQ" framework (swaps CI for SV — Strategic Vision) logged three composites within 48 hours that disagree with each other and are not treated as canonical: 5.3 (2026-05-13, sparse, no rationale recorded), 4.75 (2026-05-13, fullest rationale, uses mid-2025-era inputs), and 6.1 (2026-05-14) — the last of which is explicitly marked **"DUPLICATE: Already scored + PB verified... SKIP"** in its own rationale field and carries the disputed financial cluster discussed in (i) below. Shown for completeness only.

## (c) Financials

As of the 2026-08-11 snapshot (a 115-point daily ladder tracked since 2026-03-23, cross-checked against the legacy dossier row):

| Metric | Value | Prior |
|---|---|---|
| ARR | $400M | $400M (unchanged in the ladder since tracking began) |
| Gross margin | 50% | 40% |
| Gross profit | $200M | $8M |
| Burn rate | $40M/mo | $25M/mo |
| Headcount | 687 | 150 |
| Compute spend | $200M/yr | $100M/yr |
| Customers | 5,000 | 2,000 |
| Enterprise mix | 70% | 60% |
| NRR | 140% | 130% |
| Runway | 24 months | 18 months |
| Total capital raised | $4.0B | $3.5B |

The $400M ARR figure has not moved anywhere in the daily ladder since tracking began, and traces to the Financial Times quoting CEO Arthur Mensch that annualized run-rate was "north of €400m ($400M+), compared with just €20mn a year ago" (~February 2026) — a real number, but likely a stale mark rather than a freshly re-verified one. Two stored fields don't hold up under their own arithmetic and are flagged rather than corrected: the stored "Revenue Growth YoY %" of 19% is inconsistent with the roughly 20x year-over-year growth the FT quote itself implies, and the stored "Revenue per Employee" of $2,880K implies a headcount near 139 — matching Mistral's headcount many months ago, not the current 687 (at which ARR ÷ headcount works out to roughly $582K/employee).

Separately and reliably corroborated (roughly 15 independent headline variants): a **~$830M (~€830M) debt financing** for a Paris-area (Bruyères-le-Châtel) data center provisioning **13,800 Nvidia GB300 chips**, announced around March 2026 and operational from June 30, 2026.

**Flagged, not used as fact:** a single "Intel Notes" field (tied to a different PitchBook ID than the one used everywhere else for Mistral) claims revenue of $1.15B, headcount of 860, and "Apple acquisition talks" in July 2025. None of the three appears anywhere in Mistral's 272-row genuine dated-event timeline — which otherwise tracks the company in granular day-by-day detail through August 2026 — and a companion scoring row explicitly marks the same cluster "DUPLICATE... SKIP." This reads as a mismatched-company data pull, structurally identical to a confirmed contamination case detailed in (h)/(i) below, and none of the three figures is used anywhere in this profile.

## (d) Valuation & funding history

| Date | Round | Amount | Post-money | Lead investors |
|---|---|---|---|---|
| 2023-06-08 | Seed | €105M (~$113M) | €260M | Lightspeed, Xavier Niel, Eric Schmidt |
| 2023-12-11 | Series A | €385M (~$415M) | $2.15B | a16z, Lightspeed |
| 2024-06-11 | Series B | €600M (~$645M) | $6B | General Catalyst, NVIDIA (+ Microsoft, strategic) |
| 2025-06-01 | Series C | €600M (~$645M) | ~$6.4B | General Catalyst, XTX Ventures |
| 2025-09 (dispersed reporting) | ASML-anchored capital event | ~€1.7-2B / ~$1.9B (range) | reported $11.7B–$14B across outlets | ASML |
| 2026-07-16 | Series D — **in talks, not closed** | — | — | EQT (reportedly) |
| 2026-07-22/23 | Strategic investment — **reported, not confirmed closed** | up to ~€1B (~$1.1B) | framed against ~€20B in some headlines | Samsung Electronics |
| 2026-08-05 | Single press print, **not ladder-confirmed** | ~$4B cumulative raised | $23B | — |

The 2023-2025 rounds above are independently verified in the primary events log. The 2025-09 ASML-anchored event shows real press dispersion — different outlets cite different amounts and valuations for what appears to be a single financing — and is presented as a range rather than one invented number. The tracked daily valuation ladder itself is noisy through 2026 (fluctuating $11.7B–$14B) before settling at **$13.2B on 2026-08-11**, alongside **$4.0B total capital raised**. A single August 5, 2026 press print puts the valuation at $23B after ~$4B raised — six days before the ladder still shows $13.2B — so that figure is treated as an unconfirmed recent outlier, not the base case, pending corroboration.

**Current best-supported figures: $13.2B valuation, $4.0B total raised, as of 2026-08-11.**

## (e) Cap table & investors

No structured cap-table dataset exists in the supplied bundle (the relevant array is empty). The list below is reconstructed narratively from event and dossier fields and should be read as directional, not a verified formal cap table.

- **Seed:** Lightspeed Venture Partners, Xavier Niel, Eric Schmidt
- **Series A:** a16z, Lightspeed
- **Series B:** General Catalyst, NVIDIA, Microsoft (strategic — the stake later drew EU antitrust review over potential forced divestiture)
- **Series C:** General Catalyst, XTX Ventures
- **2025-09 capital event:** ASML
- **2026, reported but not closed:** Samsung Electronics (strategic, up to ~€1B); EQT (Series D talks, via its Scaleup Europe Fund)
- **Strategic stakeholders also referenced:** BNP Paribas

Arthur Mensch sits as CEO and board member; General Catalyst is reported to hold a board seat with lead rights. The French government relationship is described in the dossier as creating "implicit governance influence" short of any formal ownership or board role.

## (f) Litigation & IP

No litigation matters — lawsuits, court actions, disputes — were found anywhere in the supplied data; the structured litigation arrays are empty and no lawsuit-related keyword turned up a genuine hit across 272 dated-event rows. The closest IP-adjacent item is a single, unverified headline: a patent filing for "code implemented tool calls" (June 30, 2026), with no further detail available — flagged as thin. On the regulatory-adjacent side: Italy's hallucination-warning disclaimer requirement (February 2026, unverified) and Mensch's own EU AI-levy advocacy (March 2026) are the only related items, and neither is litigation against the company.

## (g) Active forecasts

No structured forecast dataset exists for Mistral AI in the supplied bundle. The only forward signals are press-reported, not house forecasts with a stated methodology: a company-stated target of roughly $1B ARR by the end of 2026 (multiple mid-2025 reports, unverified tier), and an IPO outlook described in the dossier as "no timeline; European IPO market limited; US listing possible 2027+."

## (h) Notable events

The raw extraction contained **276 dated event rows**. Row-by-row review found **4 rows (~1.4%) that are not genuinely about Mistral AI** and excluded them:

- **2 rows** are the same real-world event: Ondas Holdings' 2024 acquisition of an unrelated drone/aerospace company that also happens to be named "Mistral" — for $175M, giving Ondas "prime contractor access to US Army and Special Operations contract vehicles." This is unambiguously not the French AI lab, and the bundle's own internal annotation independently flags it as a "likely false positive." That same false positive had been absorbed uncritically into a separate summary field's "M&A Activity" note, which is why that field is not used in this profile.
- **2 rows** are simple harvester noise about unrelated companies (Upp.ai, Pendo) with no name relationship to Mistral at all.

**272 genuine rows remain**, heavily duplicated (the same real event reported by many outlets). Curated to the ~28 most important below by importance; the complete raw log — all 276 rows, each tagged genuine or excluded with a stated reason, nothing deleted — ships in `mistral-ai.json`.

1. **2023-04** — Founded in Paris (Mensch, Lacroix, Lample)
2. **2023-06-08** — €105M seed (Lightspeed/Niel/Schmidt) — largest European AI seed round at the time
3. **2023-09-27** — Mistral 7B released (open source, Apache 2.0)
4. **2023-12-11** — €385M Series A ($2.15B val); Mixtral 8x7B released same day
5. **2024-02-26** — Mistral Large released (API-only) — pivot to closed commercial models, GPT-4-competitive
6. **2024-06-11** — €600M Series B (General Catalyst/NVIDIA/Microsoft, $6B val)
7. **2024-06-16** — French government deploys Mistral assistant to all civil servants
8. **2024-07-01** — Codestral released
9. **2024-09-17** — Mistral Small 3 and Large 2 released
10. **2025-06-01** — €600M Series C (General Catalyst/XTX, ~$6.4B val)
11. **2025-09** — ASML-anchored capital event; valuation prints $11.7B–$14B across outlets
12. **2025-10-22** — Sovereign AI assistant deployed for 10,000 French public-sector agents
13. **2025-12** — HSBC signs multi-year deal
14. **2026-01-08** — French military AI deployment agreement (AMIAD-piloted)
15. **2026-02-17** — Italy requires hallucination-warning disclaimers
16. **2026-03** — ~$830M debt financing for a Paris-area data center with 13,800 Nvidia GB300 chips
17. **2026-03-17/18** — Forge (enterprise custom-model training) launched
18. **2026-03-20/21** — CEO advocates for an EU AI content levy
19. **2026-03-23/26** — Voxtral (open-weight TTS) released
20. **2026-04-29** — Medium 3.5 released — 128B unified model
21. **2026-05-01/02** — Vibe agent platform and remote coding agents launched; €1.7bn round referenced
22. **2026-05-19** — Acquires Austrian AI company Emmi AI
23. **2026-06-30** — Bruyères-le-Châtel data center (13,800 GPUs) begins operations
24. **2026-07-01/08** — Robostral Navigate launched — first robotics/physical-AI foundation model
25. **2026-07-16** — EQT reportedly in talks to lead a Series D — **not closed**
26. **2026-07-21** — Multibillion-dollar Microsoft Azure sovereign-cloud deal signed
27. **2026-07-22/23** — Samsung reported investing up to ~€1B — **not confirmed closed**
28. **2026-08-04/05** — Shieldstral released; single press print of $23B valuation (unresolved vs. ladder — see (i))

## (i) Open conflicts / disputes

1. **PitchBook ID mismatch.** Two different PitchBook IDs are attached to Mistral across the bundle — one used consistently in the sourced financial-model inputs, a different one used in the scoring and "Intel Notes" rows (including the disputed cluster below). Not reconciled here; both noted.
2. **Name-collision contamination (resolved by exclusion).** Ondas Holdings' acquisition of an unrelated "Mistral" drone/aerospace company — see (h).
3. **Suspect financial cluster.** Rev $1.15B / 860 employees / "Apple acquisition talks" — contradicted by the 115-point ladder and absent from the 272-row genuine timeline; treated as likely contamination, not fact (full detail in (c)). By contrast, that same note's claims about the ~$830M/13,800-chip debt financing and the ~$11.7B Series C-era valuation independently check out and are treated as genuine.
4. **Valuation dispersion.** $11.7B–$14B across late 2025–mid 2026 press, plus a single unconfirmed $23B print on 2026-08-05 that the ladder does not reflect six days later.
5. **Revenue-growth field inconsistency.** Stored 19% YoY does not square with the FT-sourced ~20x growth narrative in the same bundle.
6. **Stale derived field.** Stored "Revenue per Employee" ($2,880K) implies a headcount of ~139, not the current 687.
7. **EMBARGOED.** A cross-company quality-valuation relationship exists and is embargoed from publication. No coefficient, scatter, or fitted line relating AIBQ/PBQ score to valuation is stated, computed, or shown for Mistral AI.

## (j) Sources

Across the 272 genuine dated-event rows: **179 distinct source URLs** spanning **121 distinct domains**. The most-cited domains are mistral.ai (24 hits, the company's own newsroom), Google News aggregation (12), aizolo.com and TechCrunch (9 each), tech.eu (8), PYMNTS (7), CIO.com, Forbes, Le Monde, and CNBC (6 each). **22 of the 272 genuine rows (~8%) carry the primary system's "Verified: YES" tag**, tracing to the 11-row core events log cross-checked against company/press sources; the remaining ~92% are harvested press/aggregator rows at unverified tier and are treated as directional color rather than load-bearing on their own. Beyond the timeline, the profile draws on: the primary verified events log (11 rows), a company dossier stub, four PitchBook-sourced financial-model-input lines, one flagship cross-company research report (in Data Collection status, names Mistral as a comparison company), the AI Ecosystem score page, and the 115-point daily snapshot ladder. The company's own domain (mistral.ai) carries an internal source-authority score of 9/10 ("official tracked-company sources + major wire services").

---
*Full structured data, including the complete annotated 276-row dated-event log, ships in `mistral-ai.json`.*
