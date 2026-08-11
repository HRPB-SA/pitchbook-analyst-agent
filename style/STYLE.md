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

## Voice: the Hemingway-analyst register

Write like Hemingway working as a research analyst, in this desk's cadence.
The skeleton is declarative: subject, verb, object; concrete subjects doing
things (companies sign, margins fall, filings appear). The depth is the
iceberg: state the fact and what it means, and leave the machinery below the
waterline, in the exhibits, the tables, and the validation log. Trust the
reader.

**The blend (this is the desk's actual voice; a telegram is as wrong as a
metronome).** The analysis breathes through mechanism sentences: a 20-35 word
sentence is right when it walks one causal chain end to end, usually on
"because" or "so", and it earns a short declarative after it. The published
house exemplar: "That is exactly where the token-only view fails, because a
failed agentic attempt is not free. It burns reviewer time, breaks the
automation downstream, and erodes trust in the seat." Mechanism, then verbs
in series, then the landed point. Write to a sharp colleague, not to a wire
service. Name the tell. Meet the objection where the reader will raise it.
Let one dry observation land per section, at most ("Rumored rounds usually
shrink on contact with a term sheet; this one grew.").

**The flow rule (this is what "natural analytic flow" means).** Each sentence
opens from what the reader just learned and closes on the new thing. The new
thing at the end of one sentence becomes the familiar thing at the start of
the next. That chain is the analysis; when it holds, no connective filler is
needed and none is allowed. Two mechanics enforce it (Gopen and Swan): the
stress position (sentence end) carries the new information you want to land,
and the topic position (sentence front) carries the old information that
links backward. Keep subject and verb adjacent.

**Cadence limits.** No more than three consecutive sentences under 10 words;
no more than two consecutive over 30. Any sentence past 25 words gets re-read
on review and split unless it carries a single chain. A paragraph makes one
point and opens on its bottom line.

**Sentence surgery (SEC Plain English Handbook).** Surface hidden verbs
("made an application" becomes "applied"). Write in the positive ("not able"
becomes "unable"). Kill the pairs: "in order to" becomes "to", "prior to"
becomes "before". Never "respectively". When a sentence will not clarify,
make it a table.

**Citations are endnotes.** Prose carries no parenthetical citations. A
citation is a numbered marker written as [n] in the block text; the builder
renders it as a superscript tied to the numbered References section, where
the source, outlet, URL, and date live. Dates stay in the prose only where
they carry analytical weight ("signed on July 17"; "the February disclosure").
Derived arithmetic needs no marker; the validation log holds the derivations.
One marker per fact cluster, placed at the end of the clause it supports.

No hedging filler, no disclaimers that bury the finding. Certainty is stated
plainly; uncertainty is stated as content per the estimative rules below,
never smuggled in with "may" and "could".

## Estimative language (ICD 203 discipline; see WRITING_STYLES_RESEARCH.md)

Forward-looking judgments use the desk lexicon, and key judgments carry a
numerical range in parentheses: "a close by October 31 is very likely
(80-95%)". The bands: almost no chance (1-5%) · very unlikely (5-20%) ·
unlikely (20-45%) · roughly even chance (45-55%) · likely (55-80%) · very
likely (80-95%) · almost certain (95-99%). Reports that make forward calls
print the lexicon box (engine.compose.lexicon_blocks).

Confidence is stated in its own sentence, never fused with likelihood, and
the sentence says why: "Confidence: moderate; the size is press-sourced."
Likelihood describes the event; confidence describes the evidence base.

Kent's bans, absolute: "possible" is never modified (no "serious possibility",
"distinct possibility", "might well"); hedges never stack (one odds-bearing
word per sentence); "apparently", "seemingly", and bare "reportedly" carry no
evaluative weight and are flagged by QA. A forecast without an event, a date,
and a number cannot be scored, which is its defect; every named trigger
carries all three.

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

## Paragraph geometry

Paragraphs are single-topic, roughly three to five sentences, opening on
their bottom line. A one-sentence paragraph is legal once or twice per report
as a deliberate beat, never as a habit. Bullets are rare in body sections
(Key takeaways excepted); tables carry enumerable facts instead.

## Candor (standing devices)

Every update carries a "what changed since our last note" line near the top.
Every quarterly and annual review carries a what-we-got-wrong ledger. The
review checklist asks the reversed-positions question: does this note give
the reader the information we would demand if positions were reversed?
The imagined reader has a name: the IC member for memos, the LP for letters,
the intelligent non-specialist for media work.

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
