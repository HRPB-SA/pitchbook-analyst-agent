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

## Voice: the blended register (three sources, one voice)

The house voice fuses three things: the Hemingway-analyst skeleton (short
declarative core, concrete subjects doing things, depth below the waterline),
this desk's published cadence (mechanism sentences, named tells, the landed
observation), and the PitchBook-NVCA Venture Monitor's accessibility (the
flagship register every PitchBook reader already knows). Write so a smart
reader outside the coverage area follows every sentence on first pass.

What the Venture Monitor contributes, specifically:
- **Walk the reader through the counterintuitive.** When the data seems to
  contradict the environment, say so and resolve it: "At first glance, this
  expansion appears counterintuitive given the liquidity constraints.
  However, several factors explain the trend." Reasoning happens on the
  page, not behind it.
- **Natural connectives in moderation.** However, Although, While, Notably,
  Even so: at most one per paragraph, doing real logical work. The robotic
  set stays banned (Furthermore, Moreover, Additionally, In addition).
- **Name things plainly.** Companies get named (Anthropic, Snowflake), not
  wrapped in epithets ("the nearest frontier peer"). Specialist terms are
  defined at first use ("corporate venture capital firms (CVCs)"). Multiples
  are spelled out on first use ("19.4 times annualized revenue"), compressed
  after (19.4x).
- **Candor about the data.** When a figure is misleading or dated, the prose
  says so directly: "Some of these figures are misleading, particularly deal
  value." Candor is house PitchBook style, not a concession.
- **Forward views in plain form.** "We expect X to continue in 2026,
  particularly in deal count, as AI penetrates the economy": expectation,
  scope, driver, in one readable sentence, with the estimative odds where
  the judgment is load-bearing.

## Vocabulary: write for the PitchBook reader

No trading-desk slang. The reader allocates capital; the reader does not sit
on a trading floor. Banned terms and their plain replacements (QA flags the
banned column):

| Banned | Write instead |
|---|---|
| mark, the mark, marked at | valuation; the completed round valued the company at |
| print, the print | disclosure; reported figures; the company's next update |
| the tape | trading; market prices |
| re-rate, re-rates | re-price; put a higher price on |
| the book (demand sense) | investor demand |
| the Street | analysts; consensus |

Industry-standard PitchBook vocabulary stays, because the readership owns
it: deal value, deal count, dry powder, megadeal, markup, first financing,
post-money valuation, annualized revenue (preferred over bare "run rate").
The test for any remaining term: would the Venture Monitor print it without
a definition? If not, define it or replace it.

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

**The story (flow at report scale).** A note tells one story, and the
subtitle states its spine. Sections are movements, not bins: each section
closes by raising the question the next section answers, so the reader is
handed forward rather than restarted ("Whether the higher price is earned is
a question for the operating record, and the record has an answer."). Each
section earns one second-level insight: the sentence that says what the
pattern means, which the data alone does not ("Rumored rounds tend to shrink
on contact with a term sheet, because talks leak at their most hopeful
number. This one grew."). An insight is earned when the evidence for it sits
in the same section; an insight asserted before its evidence is a hook, and
hooks are banned. The verdict resolves the story it opened; it never
introduces a new theme.

**Grammar is absolute.** Zero defects ship. The traps that survive casual
review get hunted by name: ambiguous antecedents ("it", "this", "which" must
have one unmistakable referent; a sentential "which" is rewritten to name its
subject); bare-noun sentence openings ("Margin stands at" becomes "The margin
stands at"); danglers and misattached modifiers; elliptical constructions
that drop a needed word ("its guided 31%" becomes "guided growth of 31%");
false parallels in series; subject-verb distance. The content-qa audit runs
on every report before ship, and every ERROR-level finding is fixed, not
waived.

**Cadence limits.** No more than three consecutive sentences under 10 words;
no more than two consecutive over 30. Any sentence past 25 words gets re-read
on review and split unless it carries a single chain. A paragraph makes one
point and opens on its bottom line.

## Vary the moves (the anti-formula rules; one level above sentences)

Uniform moves read as machine writing even when every sentence is clean.
These rules govern the paragraph and the report, not the line.

1. **Rotate paragraph architectures.** A report uses at least three of these
   shapes, and no two consecutive paragraphs open with the same move:
   event-first ("On July 17, Databricks signed..."), history ("Databricks
   has been raising its own price for nineteen months."), assertion-then-
   mechanism ("The company does not need the money."), data-narrative
   ("Databricks reported $6.9 billion in June, and the announcement added
   nothing to it."), contrast-frame ("Where February's round brought in
   $7.0 billion, this one seeks $3 billion."). The copular pronouncement
   opener ("The X is Y.") appears at most twice per report; QA counts.
2. **Actors act.** Every paragraph keeps at least one concrete actor doing
   something in time: a company reports, an investor leads, management
   guides, a filing appears. If a paragraph's verbs are all states (is,
   stands, remains, sits, carries, reads), rewrite one sentence around an
   event. Analysis of abstractions is built on top of actors, not instead
   of them.
3. **Deliver insights; never label them.** "The price carries the first
   insight" announces analysis instead of doing it; so do "the durable fact
   in this note", "tells the same story", and "as covered above". The
   insight is the sentence itself. Desk machinery ("the basis for our
   analysis", "our standing rule") stays out of reader-facing prose; state
   the practice plainly ("a round that has not closed does not set the
   number we work from").
4. **One aphorism per report.** A crafted epigram every few paragraphs is
   performance; a single one, placed where it earns its keep, is voice.
5. **One symmetry per report.** The paired construction (two prices, two
   dates, either X) organizes at most one section. Elsewhere, vary the
   frame.
6. **The body outruns the takeaways.** Each body section contains material
   the takeaways do not: history, composition, structure, second-order
   effects, scenario work. A body paragraph that only re-words a takeaway
   gets deepened or cut.
7. **Close facing the reader.** The final section's last move turns to the
   person holding the report: what this means for the prices they see, the
   decisions in front of them, the spread worth watching. A note that ends
   inside its own coverage is unfinished.
8. **Watch the scaffolding words.** A load-bearing metaphor ("carries", "the
   story") or key noun repeated three or more times as connective tissue is
   a tic; the copy-edit pass hunts word-frequency echoes across the report.

## Sentence shapes (the anti-AI syntax rules)

Machine prose has a measurable grammar. Instruction-tuned models use present
participial clauses at 2 to 5 times the human rate and nominalizations at
1.5 to 2 times; they open sentence after sentence with the grammatical
subject; and they bolt analysis onto finished clauses instead of building
sentences around it. These shapes are banned or rationed by name.

1. **The bolt-on ban.** Never attach the analytic payload to a completed
   clause as a trailing modifier. Both forms are banned:
   - the participial bolt-on: "..., marking a shift", "..., highlighting the
     importance", "..., signaling demand" (the single strongest statistical
     tell; QA flags it);
   - the trailing appositive: "Databricks signed a term sheet at $188
     billion on July 17, 40% above its last completed mark." The delta
     dangles. Give the payload its own predicate ("...and the new price
     stands 40% above the mark it completed in February"), subordinate the
     event ("With the term sheet signed on July 17, ..."), or split into
     two sentences where the second does new work.
   Domain absolutes survive: "revenue of $6.9 billion, up 80% YoY" is
   analyst-standard shorthand, not a bolt-on. The test is whether the
   trailing element carries the sentence's ANALYSIS; data shorthand rides,
   analysis drives.
2. **Vary the opening.** Never three consecutive sentences opening with the
   same word (QA flags it), and each paragraph opens at least one sentence
   with something other than its subject: a time phrase ("On July 17, ..."),
   a subordinate clause ("Because no operating figure moved, ..."), a
   prepositional frame ("Under the house rule, ..."), or a contrast
   ("Where February's round raised $7.0 billion, this one seeks $3
   billion.").
3. **Verbs over nominalizations.** "Revenue accelerated" beats "the
   acceleration of revenue". If a sentence stacks two -tion/-ment nouns,
   rewrite it around a verb.
4. **Ration the machine's favorite figures.** Negative parallelism ("it is
   not X; it is Y"): one per report. Rule of three: vary list lengths so
   enumeration follows the content, not the meter. Decorative noun pairs
   ("growth and momentum") collapse to the stronger noun.
5. **The passive is legal.** Models underuse the agentless passive; humans
   use it whenever the paragraph's protagonist belongs in front ("The round
   was announced before the money moved"). Use it when topic position
   demands it.
6. **No that-clause subjects.** "That the round grew is telling" reads as
   machine syntax; write "The round grew, and the growth tells you
   something."

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
