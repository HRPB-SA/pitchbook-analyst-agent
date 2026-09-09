---
name: harrison-project-context
description: >
  Current project-specific data, canonical figures, and active configurations.
  THIS FILE ROTATES — update when projects close or figures change, and save a
  dated snapshot of every version to versions/YYYY-MM-DD.md.
  Zero craft protocols here — those live in harrison-domain-skills.md.
metadata:
  version: "3.4"
  last-updated: "2026-07-16"
---

# Harrison Project Context

All project-specific data lives here. When a project closes, archive its section.
When a figure is superseded, update it immediately and note the date.

**Versioning protocol (mandatory, effective 2026-06-12):** Every update to this file
saves a complete dated snapshot at `versions/YYYY-MM-DD.md` — one snapshot per update
date, never overwritten. The live `SKILL.md` carries only current state. Prior states
(including the full AIBQ v1 sub-score table) live in the snapshots. See VERSION LOG at
bottom. Container edits do not persist across sessions — after any update, the skill
folder must be re-packaged and re-uploaded.

**Source tiers:** T1 = SEC/audited · T2 = company-announced · T3 = media/single-source.
Tags: `[CANONICAL — date]` verified locked · `~ / (est.)` estimate · `[VERIFY]` open check.

---

## ACTIVE PROJECTS

### 1. Rush Note — "The xAI Tell" (In Production — ship Mon Jun 15)

6-page note: what SPCX's first print means for OpenAI and Anthropic.
**Thesis:** SPCX day-one tape is the public market's opening bid on a frontier lab;
xAI (AIBQ 4.49) is OpenAI's quality twin (4.53). SOTP residual on the AI segment
≈ $1.4–1.7T (est.) → ~$345B/AIBQ-pt (est.) → the first public print *extends* the
inverse quality–valuation curve rather than correcting it.
**Structure:** (1) day-one tape · (2) SOTP + sensitivity table · (3) $/pt ladder ·
(4) residual decomposition: scarcity / index / control / owned compute — what transfers
to OpenAI's pricing · (5) the Anthropic inversion (20.5x vs 34.1x) · (6) triggers.
**Pre-publication flags:**
- r=−0.99 EMBARGOED — use $/AIBQ-pt ladder only
- Anthropic bear-case FCF out of scope (correction sweep pending)
- [VERIFY] OpenAI $185.9B raised is equity-only before CE comparison prints
- Morningstar FVE $780B vs $2.1T close — coordinate internally before citing
- Franco Granda already quoted in Fortune on S-1 AI disclosure gaps — align, don't collide
**Named triggers:** SPCX 30-day VWAP vs $135 · 366-day lockup schedule · OpenAI roadshow
range vs $852B mark · Anthropic pricing multiple vs OpenAI first prints.

### 2. NEXUS Morning Digest v10.2 + IGNITION (Active — daily)

41 sections, 8 modules. Text = analyst document (dense, inline tables, numerals, tiers);
audio derived via TTS prep, never constrains text. Data Floor: every claim carries
figure/date/source. Three-Beat mandatory. §1 leads Frontier Five.
**Spec (authoritative):** Notion `37d5e7ad9f7f81d7b802f51dabd881d9` — per-section rules
live there, not here. [CONFLICT — surfaced, not chosen: memory carries §13 as both
"daily CFA vehicle" and "excludes all FF tickers incl SPCX"; resolve against Notion spec.]
**IGNITION intake floor:** 6–10 web searches + web_fetch full text of top 3–5 articles ·
Gmail both inboxes, full bodies of substantive newsletters · PitchBook news + get_profile
for any FF co with active event. *(Bigdata retired Jun 15 — sentiment step dropped pending a
designated replacement source; see TOOL REGISTRY.)* Then write all 41 sections,
auto-log all databases with Digest Date = today, archive. No questions — execute.
**Auto-log (every session):** Daily Scores DB `23e3c951-fb7a-4c66` (5 FF rows, full
composites) AND Score Tracker `3295e7ad-9f7f-8157` (dimension deltas) + Timelines,
FCL `eb782ae4`, Digests `448c36ae`, CFA `97f18666`. If relevant: FMI, Cost, Revenue,
Secondary, Valuation, Models, Talent, Litigation, Investors, Events, Media, Deals, Theses.

### 3. IPO Valuation Model — OpenAI + Anthropic (Active)

Goldman-standard 28-tab model. Built via Python/openpyxl, then rebuilt manually in
Excel cell-by-cell — **completed through Step 4**. Resume from Step 5.

### 4. Companion Reports (Published — sweep pending)

"An Eye on OpenAI" and "Anthropic: The S-1 Expected to Price AI" — both published
after multiple graded editorial passes.
**OPEN SWEEP:** Anthropic FCF-margin correction (bear case revised down significantly)
must be swept through ALL talking points and briefings before next media appearance.

### 5. Media Pipeline (Active)

BBC and Bloomberg appearances prepped (reporter briefs, talking points, interview prep
grounded in AIBQ + Anthropic companion report). Placements: Morningstar, Axios,
Bloomberg, Business Insider, Børsen, EFN.
**Before next appearance:** recompute r=−0.99 (embargoed until then) and confirm
FCF-correction sweep complete.

### 6. Trading Systems (Active)

- **Triforge** — autonomous intraday paper trading, Alpaca `PA3PVLIA2GP6`, VPS
  `134.122.123.51`, Next.js dashboard on Vercel. All three initial SPY strategies
  failed validation (negative expectancy, PBO). Pivoted to discretionary
  chart-analysis cycle trader with thesis/scorecard system.
- **Wheel Trader** — GitHub `HRPB-SA/wheel-trader`, local `~/Desktop/wheel-trader`,
  DigitalOcean VPS `134.122.123.51` (systemd), Alpaca paper `PA34V50DZ9AY`
  ($159K, Level 3 options), Tradier + yfinance data, Supabase + Notion + Telegram.
  Deploy: `./scripts/deploy.sh`. Target $100/day. Audited live; scheduler jobs (ET):
  6:30A premarket scan · 9:45A monitor/assignment/black swan · 10A trade session ·
  10:30A heartbeat · 1P midday · 3:45P closing · 4:30P summary · Sun 6P weekly + CEO audit.
- **Signal Nine** — 9-agent stock system, Alpaca $1K paper, VPS `134.122.123.51:5000`,
  paper trading since May 8. Queued: Jane Street shifts (cross-sectional ranking,
  IC validation, ML signals, portfolio optimization, alpha decay, risk decomposition,
  dynamic allocation) after Agent 9 audit review.

### 7. Unicorn Scores Project (Active)

475 companies scored across Batches 1–19. Intel DB `collection://891561be` (70 entries),
Scores DB `collection://6407d6b8`. 49 PB profiles pulled, 20+ PBIDs, ~42 public/acquired
discovered, ~60 duplicates flagged. **Next:** dedup cleanup → PB pulls
(Axonius/Cribl/Benchling/ClickHouse) → Batch 20+.

### 8. The $100 Billion Entry Fee (Report) — [STATUS VERIFY]

In production as of Feb 27 (`100B_Entry_Fee_Master.xlsx`, tabs 00_Assumptions–08_Sensitivity,
2023A–2030E). No activity logged since; likely superseded by the companion reports and the
28-tab IPO model. **Confirm: close/merge or resume.** Feb data corrections it carried —
OpenAI infra obligations $1.15T, OpenAI 2025 GM 33% — remain canonical (see OpenAI below).

### 9. Basis Trade note ('The Basis Trade: Why the Anthropic Discount Expires in August')

10pp - Rigor 5 - exhibits workbook v0.1 built Jul 2 - equalization 39.75% - falsifiers:
gross-accepted+coarse disclosure / OpenAI July flip / Q2 miss
**[Jul 16] PROMOTED TO CANONICAL — the 39.75% equalization is now Methodology Ruling 5 and governs every
artifact. Result: both names at 34.1x equalized; no discount exists; survivors are the 81% AIBQ-quality
premium and 1.65x CE. Falsifier status: "OpenAI July flip" — PB re-affirmed Sep on Jul 9, flip not yet
observed; "Q2 miss" — SPCX Q2 prints Aug 6, the first read in the window. Calendar conflict with Token
Trap (which anchors on Anthropic's Oct S-1) must be reconciled.**

### 10. Token Trap / 'Frontier AI Price Wars' companion (Rewrite in hand — NOT shipped)

Companion to *Waiting for a Trillion*. Doc dated Jul 10; project-context had it as an open pre-ship task
for the Jul 14 parent — **date conflict unresolved.** v2 rewrite complete (~9.5k words).
**Thesis (revised):** a 10x price sheet compresses into a **5.5-point implied-reliability band (87.6–93.1%)**
at 60k/12k and $17/failed attempt. Below the band the sticker decides; inside it nothing on the price sheet
does → the seat, not the sticker, is the moat. Opus 4.8 needs only **1.7 pts** over Gemini and **2.4 pts**
over the floor; measured agentic gaps are **7.2–15.0 pts** → the verdict is stronger than v1 claimed.
**Blockers:** Gate-2 benchmark sourcing · GPT-5.5-vs-5.6 version drift · $3.5T private-credit figure unsourced
· Google unscored · FCF sweep pending on the $559M (T3, CNBC) · COI disclosure (Anthropic 6% OW / OpenAI 2% UW).

---

## FRONTIER FIVE — CANONICAL [refreshed July 16, 2026]

**Refresh status (Jul 16):** Anthropic + OpenAI marks re-pulled from PB and CONFIRMED unchanged.
SPCX re-pulled live and MATERIALLY CHANGED (see below). Databricks, SSI, and both ARR lines
NOT re-pulled — flagged [VERIFY — STALE] below. AIBQ v3.0 scores are May 27 and unrefreshed.

| Company | Valuation | ARR / run-rate | Multiple | Equity raised | CE (equity-only) | AIBQ v3.0 |
|---|---|---|---|---|---|---|
| Anthropic | $965B post [CONFIRMED PB Jul 16, mark dated May 28] | $47B run-rate (T2, May) **[VERIFY — STALE, 2.5mo, QUARTERLY decay]** | 20.5x gross / **34.1x equalized** | $124.3B equity-only [CANONICAL Jul 2] (excl. $34.5B bonds + $2.5B revolver) | 0.38x gross / **0.228x equalized** | ~8.20 Strong / S5 / AI-INFRA |
| OpenAI | $852B [CONFIRMED PB Jul 16, mark dated Mar 31] | ~$25B net (est.) **[VERIFY — STALE]** | 34.1x | $181.2B equity-only [CANONICAL Jul 2 — UNCHANGED; Jul-8 $520M debt is excluded per Ruling 1] | 0.14x / **0.138x equalized** | 4.53 Developing / S5 / AI-INFRA |
| xAI (in SPCX) | **implied ~$1.10–1.41T (est., SOTP at the Jul 15 tape) — WAS $1.4–1.7T at the Jun 12 close** | $3.2B FY25 [T1 SEC] (**~$1.25B ex-X-ads**) | >400x implied (est.) | $47.16B pre-merger | 0.07x | 4.49 Developing / S4 / AI-INFRA |
| Databricks | $134B **[VERIFY — STALE, not re-pulled Jul 16]** | $5.4B / FCF+ **[VERIFY — STALE]** | 24.8x | $33.1B | 0.16x | 8.92 Elite / S5 / AI-PLAT |
| SSI | ~$30–32B **[VERIFY — STALE, not re-pulled Jul 16]** | $0 | ∞ | $3B | — | 2.30 Distressed / S1 / AI-INFRA |

**[CONFLICT — surfaced, not chosen | opened Jul 16] The CE column mixes bases.** Anthropic 0.38x is
computed on GROSS run-rate ($47B/$124.3B); OpenAI 0.14x on NET (~$25B/$181.2B). The raw ratio reads
2.71x. The Basis Trade equalization (39.75%) puts Anthropic net at ~$28.3B → CE 0.228x vs OpenAI
0.138x = **1.65x**, which is the figure the companion note ships. Ruling 1 governs the DENOMINATOR
(equity only) but is silent on the NUMERATOR basis. **Resolve the numerator basis, then sweep.**
Blast radius: every artifact citing CE or the 2.71x ratio.

**$/AIBQ-pt ladder [refreshed Jul 16]:** implied xAI **~$279B/pt (est., was ~$345B at the Jun 12
close)** · OpenAI $188B/pt · Anthropic $118B/pt · Databricks $15B/pt.
**The xAI rung fell ~19% on five weeks of SPCX tape — the inverse quality–valuation curve is partially
CORRECTING, which is the direct contradiction of "The xAI Tell" thesis. FCL + thesis-tracker event.** *(Public expression of the quality–valuation
spread. r=−0.99 itself EMBARGOED until recompute.)*

**AIBQ v3.0 scores dated May 27, 2026.** CRA=0 all. Key drags: Anthropic CE-2=4 (margin) ·
OpenAI GO-2=2 (conversion) · xAI CE-1=2 (CapEx 4x rev). Recent dimension moves: Anthropic
CI 5.1→5.8 (SpaceX compute deal) · xAI CE 3.0→2.5, GO 2.5→3.5, MD 3.8→4.3 (per SpaceX S-1).
Sub-score detail: Score Tracker `3295e7ad-9f7f-8157` + AIBQ rubric `36c5e7ad9f7f8199`.
v1 sub-score table preserved in `versions/2026-02-27.md`.

**Portfolio allocation [Feb 27 — verify against v3.0]:** Databricks 8% Core ·
Anthropic 6% Overweight · xAI 3% SpaceX Proxy · OpenAI 2% Underweight · SSI <1% Optionality.

### Anthropic [CANONICAL — June 12, 2026]

- $965B post — Series H $65B closed May 28 ($900B pre; leads Dragoneer/Sequoia/Greenoaks/Altimeter)
- $47B run-rate (T2 company-announced, May) · media carrying ~$44B — conflict surfaced, canonical = $47B
  **[VERIFY — STALE Jul 16: 2.5 months old, past QUARTERLY decay. Not re-pulled. Gross-basis reporter →
  20–40% SEC restatement exposure; a restatement lands it at $28.2–37.6B, and the 39.75% equalization
  lands at $28.3B — the bottom of that range.]**
- **[TRAP — NEW Jul 16] PB revenue field now reads $55B / Fiscal Period TTM 4Q2027 / period end 2027-12-31.
  This is a FORWARD PROJECTION to Dec-2027, NOT current run-rate. Ruling 4 fires. DO NOT ADOPT $55B.
  The Anthropic-ARR trap has now fired on both names (OpenAI $30B TTM 4Q2026; Anthropic $55B TTM 4Q2027).**
- Raised: $124.3B equity-only + $37.0B debt = $161.3B total [CANONICAL Jul 2]. Debt: $34.5B Jun-9 chip bonds, tranched $6.0B Superpriority / $24.0B 1st Lien / $4.5B 2nd Lien (PB 334763-02T, completed, T2) + $2.5B May-2025 revolver (PB 295197-04T). Prior $126.8B missed the revolver.
- Series H mechanics: $589.0095/sh, 17.33% acquired, investor ownership 62.66%, ~1,638mm implied shares (PB 329489-02T)
- PB financials: FY2024 rev $1.0B / net loss $5.3B; FY2025 rev $9.0B
- Ops: 140%+ NRR · 80% enterprise · 300K+ business customers · 1,000+ at $1M+ ACV
  · Claude Code $2.5B ARR (54% coding share)
- Margins: −94% → 40% → 63% (2027E) → 77% (2028E) · Q2 2026 first operating profit ~$559M (T3, CNBC-sourced)
- SpaceX compute deal [T1, SEC S-1 May 20]: $1.25B/mo through May 2029 at COLOSSUS/COLOSSUS II
  (~$45B total) · 90-day termination · Anthropic retains all IP
- Compute commitments: $80B+ across 6 partners (incl. SpaceX)
- Confidential S-1 filed Jun 1 · expected Oct 2026 (PB) **[CONFIRMED Jul 16 — PB financing note
  refreshed Jul 6 and still carries October; Alphabet-chip use of proceeds confirmed on the same note]**
- **Employees 5,000 (PB, Apr 21) — now ABOVE OpenAI's 4,500 (Mar 21). PB profile last-updated Jul 16.**
- **PB total raised $161.254B [CONFIRMED Jul 16] — matches canonical $161.3B.**

### OpenAI [CANONICAL — June 12, 2026]

- $852B (Mar 31) — $122B round at $730B pre
- ~$25B net ARR (est.) · PB $30B TTM 4Q2026 = forward projection — conflict surfaced, not chosen
- **Raised $186.4365B total (PB) [UPDATED Jul 16, was $185.9B] = $181.2B equity-only + $5.2365B debt
  ($4.0B Oct-24 + $0.7B embedded in Mar-26 round + **$520M Jul-8 2026, PB 338367-43T**); grants ($1.03B)
  already excluded by PB. **CE denominator UNCHANGED at $181.2B equity-only — Ruling 1 excludes the new
  debt, so CE 0.14x holds. This is the ruling doing its job.**
- MSFT revenue share capped at $38B through 2030 (cap binds mid-2028; shifts profitability
  2030→2029, FCF 2030 +$30B→+$151B, cum. neg FCF $198B→$99B) [model FINAL May 22]
- 2025 gross margin 33% (13pp miss vs 46% plan) · total infrastructure obligations $1.15T (7 vendors)
- Confidential S-1 filed Jun 8 (NOT May 22) · PB expected Sep 2026. **CONFLICT STILL FROZEN but MATERIALLY
  SHIFTED [Jul 16]: the PB financing note was REFRESHED Jul 9 and still carries September. The staleness
  objection ("note dated Jun 9, stale") is DEAD — PB re-affirmed September 13 days AFTER Bloomberg's Jun 26
  2027-lean. Both branches remain live; PB is no longer the stale leg. TRIGGER FIRED — this is the named
  trigger from The xAI Tell and it has moved. Sweep: Token Trap §5 assumes one branch.**
- **Business status "Generating Revenue/Not Profitable" (Jun 8) vs Anthropic's "Generating Revenue" — PB is
  encoding the profitability divergence in the status field itself.**

### Dual P&L breakevens (WSJ Apr 6 investor docs — reference)

- OpenAI: excl-training breakeven 2026 · incl-training 2030 · FCF trough −$110B (2028) · revenue NET of MSFT 20%
- Anthropic: excl-training breakeven 2025 · incl-training 2028 (+$3B) · FCF trough −$25B (2027) · revenue GROSS (incl. cloud partner sales)
- Basis differs (EBIT vs EBITDA; net vs gross revenue) — never compare raw lines without restating

---

## SPCX / SPACEX–xAI — CANONICAL [refreshed July 16, 2026 — MATERIALLY CHANGED]

**LIVE TAPE [Jul 15–16, 2026]: SPCX BROKE BELOW ITS $135 IPO PRICE FOR THE FIRST TIME on Jul 15
(CNBC, Yahoo — cross-confirmed, T2). ATH $225.64 on Jun 16 (four days post-IPO — never captured in
v3.3). Market cap ~$1.77–1.81T on 13.076B shares, vs ~$2.11T at the day-one close: ~$300–340B of
market cap gone in five weeks.**

**[DISPUTED — exact level] Investing.com: $135.27 (Jul 15), prev close $136.08, day range $132.15–139.34,
52wk $132.15–225.64. TradingView (Jul 16): mkt cap $1.81T, ATL $135.52 on Jul 14, +5.06% wk. CNN: opened
$140.95, −$0.81. Sources disagree ~6% on level and on the ATL date. THE EVENT (break below $135) is
cross-confirmed; THE LEVEL is not. Use "~$132–141, below the $135 IPO price" until a T1/T2 close is pulled.**

**NAMED TRIGGER FIRED: "SPCX 30-day VWAP vs $135" (from The xAI Tell). Spot is now through it.**

**NEW EVENTS not in v3.3:**
- **Nasdaq-100 inclusion Jul 7, 2026 — ~$4.3B forced QQQ buying into a 3–5% float [T4, VERIFY].
  v3.3 carried only "MSCI early inclusion Jun 9 · S&P declined fast-track."**
- **Q2 2026 earnings Aug 6, 2026 — the first public print since IPO, and the first frontier-AI-adjacent
  public earnings event in existence. Same date as the first lockup tranche. HARD CALENDAR ANCHOR.**
- **Lockup: ~911.5M shares; unlocks staged Aug 6 → Dec 2026 [T4, VERIFY]. This REFINES v3.3's flat
  "366-day lockup" — Aug 6 is the first date supply can actually move.**
- **Sell-side initiating: Piper Sandler Neutral · Evercore bullish · UBS buy-ahead-of-Starship [T4].**
- **Anysphere named as the Cursor parent in the $60B all-stock deal — dilution now a sell-side talking point.**
- **AI compute contracts ~$27.8B/yr incl. the $1.25B/mo Anthropic COLOSSUS contract [T4, VERIFY] —
  independent corroboration of the Anthropic deal from the SpaceX side.**

**Offer:** priced $135 Jun 11 · 555.6M shares · $75B raise · all-primary · largest IPO in history
**Day one (Jun 12):** open $150 (+11%) · high $176.52 (+31%) · close $161.11 (+19.3%)
· market cap ~$2.11T on 13.076B shares
**Structure:** float ~4.2% · Musk ~85% voting power · 366-day lockup
· MSCI early inclusion confirmed Jun 9 · S&P declined fast-track
**Consolidated FY2025 [T1 SEC]:** $18.7B revenue · −$4.9B net · $6.6B adj. EBITDA
**Segments FY2025:**
- Connectivity (Starlink): $11.4B rev · $7.17B segment adj. EBITDA (63%) · $4.42B op income
  · subs 8.9M (2025) → 10.3M (Q1 2026) · ARPU $99 (2023) → $66 (Q1 2026)
- Space (launch): $4.09B rev · −$660M op · ~80% of domestic payloads
- AI (xAI + X): $3.2B rev · −$6.36B op · capex $12.7B FY25
**Q1 2026:** Connectivity $3.257B rev / $2.087B EBITDA · AI $818M rev / −$2.47B op
· AI capex $7.7B (76% of group)
**True AI revenue ex-X-ads:** ~6.7% of company revenue (~$1.25B) [Fortune / Granda]
**SOTP residual (est., method in rush note) [RECOMPUTED Jul 16]:** Starlink $250–500B + Space $40–100B
+ $75B IPO cash → **implied AI segment ~$1.10–1.41T at the ~$1.77T Jul-15 tape (WAS ~$1.4–1.7T at the
$2.11T Jun-12 close). Same method, same segment marks, new tape. → xAI ~$279B/AIBQ-pt (est.), was ~$345B.**

**⚠️ THESIS HIT — "The xAI Tell" (shipped ~Jun 15) argued the first public print EXTENDS the inverse
quality–valuation curve rather than correcting it. Five weeks of tape have moved xAI's $/pt down ~19%
and the stock through its IPO price. The curve is PARTIALLY CORRECTING. Log to FCL + Thesis Registry
and decide: amend, retract, or hold with a dated update. Do not let a shipped thesis sit uncontested.**
**Morningstar FVE:** $780B (−63% vs close) — internal-coordination sensitivity
**xAI standalone history:** acquired all-stock Feb 2, 2026 at $250B (after $20B round
at $250B, Jan 2026 — Nvidia, Qatar SWF) · pre-merger raised $47.16B · accumulated losses $41.3B

---

## IPO PIPELINE & SEQUENCING [June 12, 2026]

| Company | Filed | Expected pricing | Note |
|---|---|---|---|
| SpaceX (SPCX) | priced Jun 11 | trading | first print, +19.3% day one |
| OpenAI | confidential S-1 Jun 8 | Sep 2026 (PB) · media: Q4 | **CONFLICT FROZEN, SHIFTED Jul 16: PB note REFRESHED Jul 9, still September — staleness objection dead. PB re-affirmed 13d after Bloomberg's Jun 26 2027-lean (Friar). Kalshi ~1-in-3 by Jan 1. Both branches live.** |
| Anthropic | confidential S-1 Jun 1 | Oct 2026 (PB) | filed first, may price second |
| Databricks | — | H2 2026 | no filing yet |

- PB sequencing (OpenAI Sep → Anthropic Oct) implies Anthropic prices against OpenAI's
  live tape — second mover inherits the first's print as ceiling or floor.
  **[Jul 16] This branch STRENGTHENED — PB re-affirmed Sep on a Jul 9 note. Any artifact asserting
  "Anthropic's Oct S-1 is the first/only frontier disclosure" is now on the weaker branch. Sweep.**
- **[Jul 16] SPCX Q2 earnings Aug 6 now sits AHEAD of both S-1s and is the first public frontier-AI-adjacent
  print. It, not either S-1, is the next hard datapoint. The Basis Trade's August catalyst and this are the
  same window — reconcile the two notes' calendars.**
- Combined pipeline ~$3.6T (Bloomberg est.) · combined raises >$240B vs ~$45B total 2025
  US IPO volume — absorption is the structural tail risk
- SEC review risk: gross-to-net revenue restatement could cut headline ARR 20–40% in one
  print (most exposed: gross-basis reporters)

---

## METHODOLOGY RULINGS & EMBARGOES [CANONICAL]

1. **CE denominator = EQUITY ONLY** (Jun 10, 2026). Debt — incl. Anthropic's $34.5B
   chip-purchase debt — excluded from CE; debt informs CI and risk, not CE.
2. **r=−0.99 EMBARGOED** until recompute. Public expression = per-point spread
   ($/AIBQ-pt ladder). Recompute required before next media appearance.
3. **FCF-margin correction sweep PENDING** — Anthropic bear case revised down; sweep all
   talking points/briefings before reuse.
4. **PitchBook TTM figures = forward projections, NOT current ARR** — always cross-reference.
5. **EQUALIZATION RULING (Jul 16, 2026).** Anthropic reports revenue GROSS (incl. cloud partner sales);
   OpenAI reports NET. NEVER compare the two raw. Canonical equalization = **39.75%** (Basis Trade,
   gate-verified workbook v0.1) → Anthropic net run-rate **~$28.3B** → **$965B/$28.3B = 34.1x, IDENTICAL
   to OpenAI's 34.1x. THERE IS NO MULTIPLE DISCOUNT.** What survives equalization: an **81% quality premium
   per AIBQ point** (8.20 vs 4.53) and a **1.65x capital-efficiency advantage** (0.228x vs 0.138x).
   Supersedes the "20.5x vs 34.1x Anthropic inversion" framing wherever it appears.
   **BLAST RADIUS — sweep required:** "The xAI Tell" §5 (the Anthropic inversion) · "Token Trap" §5 ·
   any talking point or media brief carrying 20.5x-vs-34.1x as a dislocation.
6. AIBQ v3.0: CE 20% · RQ 25% · CI 15% · GO 20% · MD 20% · Report/Standard/Exit weight
   configs · 24 sub-scores · Composite = weighted dims − CRA · stage-gated CE (S1–S5) ·
   PBQ swaps CI for SV. Hub `36c5e7ad9f7f815a`.

---

## OPEN [VERIFY] ITEMS

- **[ESCALATED Jul 16] Altman still listed 'Co-Founder, Co-Chief Executive Officer & Board Member' on a PB
  profile last-updated Jul 16. Persistent across 5+ weeks and a live refresh — the "transient artifact"
  hypothesis is now weak. Either PB has picked up a real governance change or it is a durable data error.
  A Co-CEO structure at OpenAI ahead of an S-1 is material. Resolve before any media appearance.**
- **[RESOLVED Jul 16] Sazabi $8M seed (Jun 25): CONFIRMED on BOTH profiles independently — it is the
  "Last Investment" field on Anthropic (466959-97) AND OpenAI (149504-14), $8.0M, Seed, Completed,
  2026-06-25. The co-investment is real. Anthropic and OpenAI are co-investors in the same seed round.**

---

## NEXUS (Pipeline + Schema — Active)

- **Schema:** 52 databases (May 5 spec). FMI uses "Latest Verified"/"xAI/SpaceX".
  12 Timeline Categories. Digest Date on AIBQ Tracker, FCL, 5 FF timelines.
  Pages: 🌍 State of Universe · 🏢 Company Profiles (5 FF) · 📖 Output Playbook.
  DBs incl. Earnings Calendar `d93289d9` · Media Tracker `0c2b8f65` · Thesis Registry
  `0f515343` · Weekly Rollup `920f9702` · HYPD Deal Pipeline `e82a7c2a` · CFA Progress `97f18666`.
- **Infra:** VPS `134.122.123.51` · GitHub Actions harvester (load_existing_hashes fixed)
  · `timeline_reader.py` → legacy Timeline DBs · SendGrid delivery · OpenAI TTS audio.
- **Coverage universe (13):** Anthropic · OpenAI · Databricks · xAI · SSI · Perplexity
  · Scale AI · CoreWeave · Cursor · Mistral · ElevenLabs · Cohere · OpenEvidence.
- **Conventions:** Notion via direct HTTP, `verify=False` (corporate SSL) · notion-client
  pinned **2.2.1** (3.0.0 breaks) · PowerShell `foreach ($c in @(...))` · two-pass
  extraction: authority≥8 → claude-sonnet, <8 → claude-haiku.
- Notion MCP connects to Archer/personal workspace — NEXUS operations use Python scripts.

---

## AI BENCHMARKS [partially refreshed July 16, 2026]

**LEGACY BLOCK [Feb 27 — a full generation stale, kept for history]:** Gemini 3.1 Pro leads ARC-AGI-2
(77.1%) and 13/16 benchmarks (Feb 19). Opus 4.6: #2 ARC-AGI-2 (68.8%) · #1 SWE-bench (80.8%) · #1 OSWorld
(72.7%) · #1 Arena Elo thinking (1,506). GPT-5.2 54.2% · Grok 4.1 40.0% ARC-AGI-2.

**CURRENT GEN [Jul 16 — Opus 4.8 vs Gemini 3.1 Pro, AGENTIC task class]:**

| Benchmark | Opus 4.8 | Gemini 3.1 Pro | Gap | Tier |
|---|---|---|---|---|
| SWE-bench Pro | 69.2% | 54.2% | +15.0 | T2 vendor |
| MCP-Atlas (Scale AI) | 82.2% | 73.9% | +8.3 | **T3 independent** |
| SWE-bench Verified | 88.6% | 80.6% | +8.0 | T2/T4 mixed harness |
| OSWorld-Verified | 83.4% | 76.2% | +7.2 | T2 vendor |
| GDPval-AA (ELO) | 1890 | 1314 | +576 | T2 vendor |
| HLE w/ tools | 57.9 | 51.4 | +6.5 | T2 vendor |

**⚠️ GATE 2 FAILS.** Every row except MCP-Atlas traces to **Anthropic's own system card (May 28, 2026)**,
re-reported by ~7 aggregators. *One wire, many logos.* **Google has not published matching agentic evals —
the Gemini numbers in circulation are Anthropic's measurements of Gemini.** Harness choice swings results
≥5 pts (GPT-5.5 Terminal-Bench: 78.2% default vs 83.4% on the Codex CLI harness).
**Direction HIGH confidence · magnitude LOW · [DISPUTED].**

**Version drift:** the circulating comparison set is Opus 4.8 / **GPT-5.5** / Gemini 3.1 Pro. The Token Trap
price sheet carries **GPT-5.6** Sol/Luna. **Do not pair a GPT-5.5 benchmark with a GPT-5.6 price.**

**Independent corroboration [T3, most valuable line here]:** Cursor reports Opus 4.8 completes CursorBench
tasks in **fewer steps** at a better result — token cost per task falls without a quality drop. Non-vendor,
production, and it is the Token Trap thesis measured. **Get the underlying data.**

**Product facts [T2, Jul 16]:** Opus 4.8 $5/$25 (unchanged from 4.7) · **Fast Mode ~3x cheaper** ·
**prompt caching up to 90% off** · **batch ~50%** · **effort controls (high/extra/max)** · **1M context**
(Gemini 3.1 Pro: 2M) · Anthropic claims ~4x less likely than 4.7 to let coding errors pass unremarked.
**Fast Mode (~$1.67/$8.33 est.) puts a frontier-family Anthropic model BELOW Gemini's $2/$12 — this kills
any "hollow middle / barbell" framing.**

---

## AI MARKET SIZING [Feb 2026]

Foundation Models $50B → $250B (2028E) · AI Infrastructure $120B → $400B (2028E)
· AI Applications $30B → $150B (2028E).

---

## KEY EVENTS [CANONICAL]

- xAI acquired by SpaceX: Feb 2, 2026 ($250B all-stock)
- Databricks Series L $7B: Feb 9, 2026 ($134B post)
- Anthropic Series G $30B: Feb 12, 2026 ($380B post)
- OpenAI $110B announcement: Feb 27, 2026 (announcement only; closed Mar 31 as $122B, PB 320989-60T. Do not double-count.)
- "Ranking the AI Giants" published: Mar 4, 2026
- OpenAI $122B round at $730B pre → $852B: Mar 31, 2026
- Archer Trading Desk archived: Apr 24, 2026
- Signal Nine paper trading start: May 8, 2026
- SpaceX S-1 public: May 20, 2026 (incl. Anthropic COLOSSUS deal disclosure)
- AIBQ v3.0 canonical scores: May 27, 2026
- Anthropic Series H $65B → $965B post: May 28, 2026
- Anthropic confidential S-1: Jun 1, 2026
- OpenAI confidential S-1: Jun 8, 2026
- Anthropic $34.5B chip debt (T3): Jun 9, 2026 · MSCI early inclusion confirmed for SPCX: Jun 9
- CE equity-only ruling: Jun 10, 2026
- SPCX priced $135: Jun 11, 2026 · first trade Jun 12, close $161.11 (+19.3%, ~$2.11T)
- Anthropic $34.5B tranched chip bonds: Jun 9, 2026
- Fable 5/Mythos 5 arc: launch Jun 9 / BIS directive Jun 12 / 18-day freeze / partial Mythos approval Jun 26 / lift Jun 30 / restoration + 50% credits through Jul 7: Jul 1
- SpaceX-Cursor $60B all-stock (8-K): Jun 16, 2026
- OpenAI audited FY2025 leak (FT-verified, T3): Jun 16, 2026. Rev $13.07B / op loss $20.92B / group loss $60.35B incl $41.55B FV swing on convertibles-warrants / $17.2B paid to MSFT
- **SPCX all-time high $225.64: Jun 16, 2026 (4 days post-IPO)**
- **SPCX Nasdaq-100 inclusion: Jul 7, 2026 (~$4.3B forced QQQ buying into a 3–5% float) [T4, VERIFY]**
- **Mythos/Fable restoration + 50% credits END: Jul 7, 2026 — three days before the Token Trap note date**
- **OpenAI $520M debt: Jul 8, 2026 (PB 338367-43T). Excluded from CE per Ruling 1.**
- **PB refreshed OpenAI financing note (still Sep 2026): Jul 9, 2026 — kills the "PB field is stale" objection**
- **Token Trap / "Frontier AI Price Wars" companion dated: Jul 10, 2026 [date conflicts with the Jul 14 parent ship — resolve]**
- **SPCX breaks below its $135 IPO price for the first time: Jul 15, 2026 (CNBC/Yahoo, T2). Named trigger fired.**
- **Canonical refresh v3.4: Jul 16, 2026 — Anthropic/OpenAI marks confirmed, SPCX materially changed, equalization ruling added**

---

## MEDIA & DISTRIBUTION RELATIONSHIPS

Business Insider (active) · Axios (quoted, OpenAI/Anthropic dynamics) · Bloomberg
(appearance prep) · BBC (appearance prep) · Morningstar (published; Tom Lauricella)
· Børsen · EFN/Swedish financial press.
Morningstar article: "From Private Conviction to Public Scrutiny: The AI Giants at the
IPO Gate" (~1,393 words).
Note: Franco Granda quoted in Fortune (May 28) on SpaceX S-1 AI disclosure gaps.

---

## WORK ENVIRONMENT

Windows laptop · corporate SSL inspection (`verify=False` for HTTP clients) ·
VS Code/Cursor · PowerShell · Claude Code at `C:\Users\harrison.rolfes\.local\bin`.

---

## ARCHIVED PROJECTS

- **Archer Trading Desk** — ARCHIVED Apr 24, 2026. Repo `~/archer-trading-desk`,
  nightly pipeline, 160-stock universe, 7 sector desks. First paper trades
  [CANONICAL — Mar 6, 2026]: MRVL $89.57→$113.46 · DDOG $125.75→$162.84
  · MSFT $408.96→$509.61. Superseded by Triforge/Wheel Trader/Signal Nine.
- **Q1 2026 Global Unicorn Tracker** — published (data 3/31/26): 1,680 active unicorns,
  $8.6T aggregate, AI = 622 cos/$4.1T (47.6%), Q1 exits $343.1B incl. xAI–SpaceX $250B.
  Known issues: EX4_AIBQ stale (pre-v2.2) · #REF! Q2–Q4 2026 structural · internal RVVC
  Snowflake SQL not in published.
- **TechCrunch Disrupt 2026** — submission removed May 25; not active.
- **AIBQ v1 scores/sub-scores (Feb 27)** — superseded by v3.0; full table in
  `versions/2026-02-27.md`.

---

## DATA GOVERNANCE

Every canonical figure in this file carries, going forward: value · last-verified date ·
decay class · dependents.

**Decay classes** (auto-flag stale when age exceeds the class threshold):
- **VOLATILE** — price / valuation / market data — stale in days–weeks
- **QUARTERLY** — ARR / run-rate / headcount — stale in ~a quarter
- **STABLE** — cap structure / deal terms / round details — stable until a new event
- **PERMANENT** — definitions / methodology rulings — do not decay

**Dependency graph:** note which artifacts cite which figure (report, digest §, model, talking point).

**Correction propagation:** when a canonical figure changes, compute the BLAST RADIUS — every
artifact that cited the old value — and drive the sweep before the change is "done." The FCF
correction sweep and the r=−0.99 recompute are instances of this; treat every figure change the same way.

---

## HOUSE VIEW (compounding theses — Notion DB)

A living, validated set of cross-cutting beliefs. Every Rigor ≥4 analysis is checked against
the house view (does it confirm, extend, or contradict a standing belief?) and deposits back
into it. Entries carry confidence + supporting evidence + last-tested date.

**Seed entries:**
- **Valuation–quality paradox** — the highest-valued frontier labs score lowest on AIBQ fundamentals.
  Public expression: the per-AIBQ-point spread (the r=−0.99 correlation stays embargoed).
  **[EXTENDED Jul 16] Restate on an equalized basis. The old expression — the market pays LESS for the
  higher-quality lab (20.5x vs 34.1x) — is a gross-vs-net artifact. The equalized expression is stronger:
  the market pays the IDENTICAL multiple (34.1x vs 34.1x) for assets differing by 81% on AIBQ quality and
  1.65x on capital efficiency. The paradox is not mispricing in Anthropic's favour — it is the market
  failing to price quality AT ALL. Survives the S-1 in a way the "discount" does not.**
  **[TESTED Jul 16 — partial fail] xAI's $/pt fell ~19% (~$345B → ~$279B) on five weeks of SPCX tape and
  the stock broke its IPO price. The curve is partially correcting. The paradox is not a constant.**
- **IPO absorption thesis** — the $3.6T pipeline vs ~$469B 2025 US IPO volume; can the market absorb it?
- **Sector valuation conventions don't transfer** — an 80% EBITDA margin on a rocket company is a
  category error (the SPCX/Morgan-Stanley tell).
- **CE methodology** — denominator is equity raised only; debt informs CI/risk, never CE.
- Cross-sector patterns from the industry layer deposit here as they recur.

---

## DEFECT LOG (the feedback loop — Notion DB "Output Defect Log")

One row per correction Harrison makes to a Claude output.

**Schema:** date · mode/layer · artifact · what was wrong · root-cause class · fix · recurring? (Y/N)
**Root-cause classes:** stale-data · bad-source · no-cross-check · calibration · craft-gap ·
execution-miss · industry-gap
**Open lines [written Jul 16]:**
| Date | Layer | Artifact | What was wrong | Root cause | Fix | Recurring? |
|---|---|---|---|---|---|---|
| 2026-07-16 | project-context L7 | FF canonical table | CE column compares Anthropic-on-gross to OpenAI-on-net; reads 2.71x where the equalized ratio is 1.65x | no-cross-check | Ruling 5 + numerator-basis resolution + sweep | **Y** — 3rd instance of the same basis error |
| 2026-07-16 | analyst | Token Trap §5 | 20.5x vs 34.1x published as a dislocation; it is the artifact the companion note dismantles | no-cross-check | deleted; four-basis table added | **Y** |
| 2026-07-16 | analyst | Token Trap §8 | Anthropic-over-Google edge called the "soft joint" at ~2pts; measured agentic gaps are 7.2–15.0 | stale-data | benchmark block refreshed | N |
| 2026-07-16 | analyst | Token Trap §3 | model-layer GM computed from output price only; input is >50% of revenue on the note's own task | craft-gap | blended-margin rebuild | N |
| 2026-07-16 | project-context L7 | AI BENCHMARKS | block 4.5mo stale and a full generation behind the price sheet under analysis | stale-data | current-gen table added; legacy retained | **Y** — decay class not enforced |

**Standing instruction:** whenever Harrison corrects an output, write one defect line before the
session ends. Monthly review — deepen the layer with the most recurring craft/industry gaps;
tighten the protocol with the most execution-misses. Converts "improve quality" into a measured loop.

---

## PRINCIPAL REGISTERS (owner doctrine, operational)

- **Portfolio / capital** — each active use of time & capital · expected return · marginal return of
  the next unit. Reallocation rule: feed winners; cut a use when its marginal ROIC drops below the best
  alternative. Reviewed on the operating cadence. Test before sustained effort: "is this the
  highest-returning slot for the next hour/dollar?"
- **Decision journal** — Type-1 (irreversible) decisions logged with the reasoning + EV AT THE TIME.
  Review later to separate decision quality from outcome quality.
- **Resilience register** — existential risks · single points of failure · "what kills this."
  Seed: the NEXUS harvester-timeout class (a job with no timeout took down the whole pipeline, Jun 2).
- **Leverage register** — what's systematized vs still manual. Any task done 3+ times triggers a leverage
  decision: do → document → systematize → delegate/automate → eliminate.
- **Operating cadence / KPI tree** — north-star + KPIs (reports shipped · media placements · prediction
  calibration [FCL] · AIBQ coverage breadth · HYPD pipeline · CFA readiness · output-defect rate).
  Rhythm: daily = digest · weekly = self-WBR (roll defect log + FCL + house view + capital register) ·
  monthly = deepen weakest layer + reallocate · quarterly = strategy + KPI review.

---

## TOOL REGISTRY (post-Bigdata)

- **LIVE:** PitchBook Premium · Gmail (hypdventures) · Notion · web_search/web_fetch
- **RECONNECT:** Aiera (events/transcripts) · Morningstar (analyst research / FVE)
- **ADD:** FMP (macro + fundamentals — Bigdata replacement) · Quartr (research/transcripts)
- **RETIRED:** Bigdata.com (subscription paused — removed from all protocols)
- **Gmail:** native MCP = one account; forward harrisonpbnews@gmail.com → hypdventures@gmail.com

*[VERIFY] Bigdata replacement does not cover sentiment (FMP = fundamentals/macro; Quartr/Aiera = transcripts).
The IGNITION intake floor's sentiment step was dropped on retirement — designate a sentiment source or
confirm removal.*

---

## VERSION LOG

| Date | Version | Summary |
|---|---|---|
| 2026-07-16 | 3.4 | **Canonical refresh.** Anthropic $965B + $161.254B raised CONFIRMED (PB, live); OpenAI $852B CONFIRMED, total raised $185.9B→$186.4365B (+$520M Jul-8 debt; CE denominator unchanged per Ruling 1). **SPCX materially changed** — broke below its $135 IPO price Jul 15 (named trigger fired), ~$1.77–1.81T vs $2.11T day-one, ATH $225.64 Jun 16, Nasdaq-100 Jul 7, Q2 prints Aug 6; xAI SOTP recut to ~$1.10–1.41T and $/AIBQ-pt to ~$279B (was ~$345B) — **partial fail on The xAI Tell thesis**. **Ruling 5 added (39.75% equalization → both names 34.1x; no discount)**. OpenAI S-1 conflict shifted (PB note refreshed Jul 9, still Sep — staleness objection dead). Sazabi co-investment RESOLVED; Altman Co-CEO ESCALATED. Benchmarks partially refreshed to Opus 4.8 vs Gemini 3.1 Pro (Gate 2 fails — one wire, many logos). NEW TRAP: PB Anthropic revenue field $55B TTM 4Q2027 = forward projection. Databricks/SSI/both ARR lines NOT re-pulled → [VERIFY — STALE]. Snapshot: `versions/2026-07-16.md` |
| 2026-07-02 | 3.3 | Capital-basis corrections (OpenAI equity-only $181.2B, CE 0.14x; Anthropic equity-only $124.3B, CE 0.38x; $2.5B revolver added to exclusions); chip-debt tranching T2; export-control arc; SpaceX-Cursor; OpenAI FY25 leak; Feb-27 dedupe; IPO conflict frozen; Basis Trade added as project 9. Snapshot: `versions/2026-07-02.md` |
| 2026-06-15 | 3.2 | Layer-7 additions: data governance (decay classes, dependency graph, correction propagation) · house view DB (seed theses) · output defect log · principal registers (portfolio/capital, decision journal, resilience, leverage, operating cadence/KPI tree) · tool registry post-Bigdata. Swept retired Bigdata ref out of IGNITION intake floor (§2). Additive — no canonical figures changed. Snapshot: `versions/2026-06-15.md` |
| 2026-06-12 | 3.1 | Full rotation: AIBQ v3.0 scores (May 27) replace v1 · valuations to Jun 10/12 anchors (Anthropic $965B/$47B, OpenAI $852B/~$25B, SPCX day-one tape) · SPCX canonical section added · IPO sequencing table · methodology rulings (CE equity-only, r=−0.99 embargo, FCF sweep) · rush note "The xAI Tell" added · Archer archived · dated-snapshot versioning protocol established. Snapshot: `versions/2026-06-12.md` |
| 2026-02-27 | 3.0 | Pre-rotation state (AIBQ v1, pre-Series-G/H valuations, Archer active). Snapshot: `versions/2026-02-27.md` |

---

## ARCHIVE TRIGGER

When a project closes or figures are superseded:
1. Save a dated snapshot of the CURRENT file to `versions/YYYY-MM-DD.md` (never overwrite prior snapshots)
2. Move closed sections to `## ARCHIVED PROJECTS` with close date and final status
3. Update any CANONICAL figures that changed; bump `last-updated` and add a VERSION LOG row
4. Re-package the skill folder and re-upload (container edits don't persist)
5. Never delete — archived context and snapshots may be referenced for historical comparison
