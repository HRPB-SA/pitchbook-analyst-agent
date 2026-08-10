# Validation log: Databricks Company Update, August 10, 2026

Author of record: Harrison Rolfes, Senior Research Director.
Produced by the report engine (run date 2026-08-10); prior pack: July 10, 2026
validation log (repo root). Method: live PitchBook Premium pull (profile
59199-40, last updated 2026-08-10) + PitchBook news cross-check
(PITCHBOOK_NEWS + THIRD_PARTY_NEWS, min_date 2026-07-10). Conflicts frozen,
not averaged. Outlet names appear here, never in report prose.

## Load-bearing claims

| Claim | Value | Sources | Tier | Cross-check | Confidence |
|---|---|---|---|---|---|
| Term sheet signed, $188B post, Coatue lead | Jul 17, 2026 announcement | Company statement (Reuters syndication, TechCrunch, CNA/WSJ); PB deal 334745-56T Announced/In Progress; PB financing note Aug 7 | T2 | 4+ independent outlets + PB record | HIGH |
| Round size ~$3B | press-reported, company did not disclose | WSJ via Reuters/CNA; TechCrunch ("other outlets"); PB news commentary | T3 | 3 outlets, all tracing to WSJ | MEDIUM (single ultimate source; labeled est./press in text) |
| Close expected "later this summer"; funds not in hand | company statement | Reuters syndication; TechCrunch quotes company | T2 | 2+ | HIGH |
| $134B remains last completed mark | Series L, Feb 9, 2026 | PB deal 313367-68T; company PR Dec 2025 | T2 | PB + company | HIGH |
| PB now states Series L pre-money $129B; 48 co-investors (was ~44) | PB revision | PB financing note Aug 7, 2026 | T2 | single source, flagged as PB-revision in text | MEDIUM |
| Active investors 148 -> 152 | PB profile field | PB profile Aug 10, 2026 vs Jul 9 pack | T2 | field-level diff | HIGH |
| Valuation ladder $62B (Dec 2024), $100B (Sep 2025), $134B (Feb 2026) | completed marks | TechCrunch round history; PB deal records for Feb 2026 | T2/T3 | press + PB for latest | HIGH on 134; MEDIUM on 62/100 (press-dated) |
| Run-rate $6.9B +80% YoY (Jun 16); no newer print | company disclosure | July 10 pack (re-verified then); no newer print found in news sweep | T2 | news sweep found no update | HIGH |
| Gross margin 74%, guided lower; 70% gate cushion 4 pts | company disclosure Jun 16 | July 10 pack | T2 | held from pack | HIGH |
| Employees 9,000 (Jun 9, 2026) | PB field | PB profile Aug 10 pull | T2 | unchanged vs pack | HIGH |
| PB revenue field $6,900M TTM 4Q2026 = forward window | PB profile | re-verified on this pull; Ruling 4 | T2 | empirical re-check | HIGH |
| No S-1 on file | as of Jul 10, 2026 EDGAR check | July pack (T1); news sweep found no filing since | T1 (dated) | news sweep | HIGH as of its date; flagged VOLATILE/31d in tracker tables |
| Multiple 19.4x / 27.2x | derived | $134B and $188B over $6.9B | Derived | arithmetic checked: 134/6.9=19.42; 188/6.9=27.25 | exact |
| Per-point $15.2B / ~$21.3B / $118B / $188B / ~$279B | derived | marks over AIBQ composites (8.81 / 8.20 / 4.53 / 4.49) | Derived | 134/8.81=15.21; 188/8.81=21.34; 965/8.20=117.7; 852/4.53=188.1; ~1250/4.49=278 (est.) | exact on completed; est. where marked |
| CE 0.34x -> ~0.30x on close | derived, equity-only | 6.9/20.2=0.342; 6.9/23.2=0.297 | Derived | Ruling 1 basis stated in text | exact given inputs; equity base ~ labeled est. |
| Growth-adjusted 0.34x vs comp 0.49x | derived | 27.2/80; 15.3/31 (comp guide, 8-K May 27) | Derived/T1 | arithmetic checked | HIGH |
| Comparable at 15.3x fwd product revenue +31% | from July pack | Snowflake 8-K (T1) + market cap ~$91B (Jul 7, T3) | T1/T3 | pack values; market cap 34d old, flagged VOLATILE in tracker | MEDIUM (mkt cap stale; flagged) |

## Conflicts and traps this run

1. PB deal date Jul 16 vs company announcement Jul 17: trivial timing skew
   (announcement after signing); both dates shown where relevant. Not frozen.
2. One aggregator body-text carried "$118 billion" for the round valuation
   against its own headline's $188B: typo in source, discarded; four
   independent confirmations of $188B.
3. PB revenue field remains a forward-window figure (TTM 4Q2026): Ruling 4
   applied; not adopted. Trap re-verified empirically this run.
4. Feb-2026 operating metrics (NRR, customer counts, FCF) past QUARTERLY
   decay: flagged in report Section 2 with vintages; not silently reused as
   current.

## Embargo check

The quality-valuation coefficient appears nowhere in this report or its
charts. The chart factory has no scatter type (guard raises on any attempt);
the only quality-valuation expression used is the per-point ranked bar
(Figure 3). Footer carries the standing embargo line. Build QA: 0 FAIL.

## QA overrides

Two WARN-level heuristic flags (figure-dense paragraphs without inline
parenthetical cues) reviewed and accepted: both are restatement paragraphs
whose figures are sourced at first use earlier in the report (trigger-review
paragraph; verdict paragraph). No new figures introduced there.

## Report Ship gate (Protocol 2)

- [x] Validation ledger complete (above)
- [x] Adversarial pass: the strongest counter (paying 27.2x for decelerating
      software) is addressed head-on: the ladder shows acceleration, and the
      falsifier (margin below 70%) is named in the verdict
- [x] No open sweep flags on Databricks artifacts
- [x] No [VERIFY]/[DISPUTED] figure ships unflagged (stale metrics carry
      vintages in text and tables)
- [x] Copyright-safe: no quotes; all facts restated
- [x] Zero TODOs/placeholders (QA scan enforced); lead-with-signal; forward
      hook (three dated watch items + falsifier)
- [x] MNPI/COI: public sources only; no position disclosure required in an
      internal-format update
