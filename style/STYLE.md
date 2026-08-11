# House style (prescriptive)

The measured profile lives in `style_profile.json` / `STYLE_PROFILE.md` and is
regenerated from the shipped library (`python -m engine style`). This file is
the prescriptive layer: what the writing must do. When the two disagree, this
file wins; refresh the measured profile after every shipped report so the
corpus keeps teaching the system.

## The pre-flight checklist (Institutional_Research_Style_Guide.pdf, binding)

Run every draft against these five before anything ships. Institutional
readers read to allocate capital and assess risk, not for pleasure.

1. **The Apex Principle (punchline first).** The opening sentence of the
   report, of every section, and of every takeaway bullet IS the single most
   important finding: what the market is misprices or what the data proves,
   with the metric in it. Never a rhetorical hook, never a scene-setter.
   A punchy aphorism without its number is a hook, not a takeaway
   ("...and the money is not in hand" fails; "27.2x the June run-rate,
   unsettled" passes).
2. **High signal-to-noise (eradicate adjectives).** Adjectives project
   uncertainty; the metric carries the emphasis. "Massive", "significant",
   "drastic" and kin get deleted and replaced with the number
   (QA flags them). AVOID: "Compute costs are seeing massive growth."
   DO: "Compute CapEx now consumes 65 cents of every top-line dollar."
3. **Rhythmic asymmetry.** Vary cadence aggressively: follow a complex,
   multi-clause valuation chain with a short declarative. No metronome.
4. **The "So what?" imperative.** Reporting states what happened; analysis
   states what it means. Every metric ties directly to valuation multiples,
   exit timelines, capital efficiency, or risk underwriting. A data point
   left hanging is unfinished work.
5. **No throat-clearing.** Never introduce what you are about to say. Banned
   on sight: "It is important to note", "Furthermore", "Delve", "Robust",
   "Paradigm shift" (plus the house list below).

## Voice

Signal, not story. Direct, dense, analyst register. No hedging filler, no
disclaimers that bury the finding. Certainty is stated plainly; uncertainty is
labeled explicitly (`~`, `(est.)`, tier tags), never smuggled in with "may" and
"could" (hedge budget: at or below the measured rate, currently ~4/1,000 words).

## Structure

1. Lead with the sharpest signal. The first paragraph of the report, and of
   every section, carries the finding. Never open with preamble, throat-
   clearing, or methodology.
2. Complicate the headline: the strongest counter-fact appears near the top,
   not buried.
3. Close with the implication and a forward hook: what to watch, dated, and
   which published number would falsify the claim.
4. Three-beat discipline on every analytical passage: WHAT HAPPENED (fact,
   sourced, tiered) -> WHAT IT MEANS (mechanism) -> IMPLICATION (do / watch /
   reprice). A finding without an implication is incomplete work.

## Section titling

Metaphor + colon + literal claim, sustained as a system across the report:
"The Mortar: How the Money Is Made" · "The Appraisal: What the Business Is
Worth". One metaphor family per report; never mix families.

## Sentence and paragraph geometry

Sentences average low-20s words with wide variance: short declaratives for
verdicts, long clause-stacked sentences for evidence chains. Paragraphs are
dense, single-topic, roughly 4 sentences / 120 words; no one-sentence
paragraphs in body prose. Bullets are rare in body sections; tables carry
enumerable facts instead.

## Figures and formatting

- `$14.2B` in tables, tiles, and captions. Prose may spell "billion" in full
  sentences; never mix styles inside one table.
- `27.1x` not "27.1 times" · `+47% YoY` with sign and period · `~$14B (est.)`
  for estimates · `[CANONICAL]` only in internal docs, never in shipped prose.
- Every load-bearing figure carries a parenthetical source of KIND + DATE:
  `(company disclosure, June 16, 2026)`, `(PitchBook deal record, Feb 9,
  2026)`, `(SEC EDGAR, July 10, 2026)`, `(derived)`. Outlet names (CNBC,
  Bloomberg, The Information) stay in the validation log; report prose says
  "press reports".
- Estimates are labeled at the point of use, not in a footnote.
- Disputed figures ship as both values with both dates, or not at all
  (freeze-on-conflict).

## Punctuation and banned language

Em-dashes sparingly: at most 2 in any block (WARN past that) and 8 in a
document (build FAILS past that). Used for a genuine interruption or
apposition, never as a comma substitute or a rhythm tic.

Banned: "it's worth noting" · "it is important to note" · "importantly" ·
"furthermore" · "leverage" as a verb · "synergy" · "going forward" ·
"unlock" · "dive into" · "delve" · "in conclusion" · "at the end of the day" ·
"game-changer" · "cutting-edge" · "paradigm shift" · "robust". Emphasis
adjectives ("massive", "significant", "drastic", ...) are flagged: delete the
adjective, insert the metric. Rhetorical questions as transitions. Author
self-reference in report prose ("I think"; "we believe" is acceptable as house
voice sparingly in verdict sections only).

## Evidence density

Target the measured profile: roughly 8-10 parenthetical citations, 12+ money
figures, 1+ table or figure per 1,000 words. A page with no number on it is a
page that should not exist.

## Verdicts

Every report ends with a verdict section that takes a position: rating, band,
base case, or explicit pass. State the falsifier: the single published number
that would change the answer. "It depends" is not a verdict.
