# House style (prescriptive)

The measured profile lives in `style_profile.json` / `STYLE_PROFILE.md` and is
regenerated from the shipped library (`python -m engine style`). This file is
the prescriptive layer: what the writing must do. When the two disagree, this
file wins; refresh the measured profile after every shipped report so the
corpus keeps teaching the system.

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

## Banned

Em-dashes (U+2014) anywhere; the build fails on them. "it's worth noting" ·
"importantly" · "leverage" as a verb · "synergy" · "going forward" · "unlock" ·
"dive into" · "delve" · "in conclusion" · "at the end of the day" ·
"game-changer" · "cutting-edge". Rhetorical questions as transitions. Author
self-reference in report prose ("I think", "we believe" is acceptable as house
voice sparingly in verdict sections only).

## Evidence density

Target the measured profile: roughly 8-10 parenthetical citations, 12+ money
figures, 1+ table or figure per 1,000 words. A page with no number on it is a
page that should not exist.

## Verdicts

Every report ends with a verdict section that takes a position: rating, band,
base case, or explicit pass. State the falsifier: the single published number
that would change the answer. "It depends" is not a verdict.
