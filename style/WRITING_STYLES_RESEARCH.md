# Writing Styles Research: The Best Analytical Writing Styles to Incorporate (August 2026)

Prepared 2026-08-11 (research branch `claude/analytical-writing-styles-5gu6r0`); adopted
into the house standard the same day. STYLE.md binds the Tier 1 recommendations; the QA
scanner in engine/qa.py enforces the mechanical ones; the Hemingway-analyst register in
STYLE.md is the voice they serve.

## The headline find

**The great traditions converge, and the house already runs most of the convergence.**
Consulting storylining, military BLUF, intelligence tradecraft, the CFA's report guidance,
and the admired investor letters all arrive at the same architecture: state the conclusion
first, make every heading a claim the body must prove, let the reader's next question
choose the next sentence, and treat candor about uncertainty as structure rather than
decoration.

**The one genuinely unclaimed edge is estimative discipline.** The intelligence community
learned that probability words do not transmit: Sherman Kent's own board read the signed
phrase "serious possibility" as anything from 20% to 80%, and a 2018 survey of about
1,700 readers found "likely" interpreted anywhere from 55% to 90% (Mauboussin and
Mauboussin, HBR 2018). The fix is codified in ICD 203: a printed probability lexicon,
numbers in parentheses after estimative words, and confidence stated separately from
likelihood. No named investment firm has formally adopted this standard in published
research (unverified as an absence). An analyst OS that prints the lexicon in every
report and logs its probability judgments for calibration is visibly differentiated at
the cost of one methodology box.

**And writing quality is priced.** One standard deviation of readability narrows
closed-end fund discounts by 2.48% (Hwang and Kim 2017, JFE). More readable sell-side
reports draw larger trading-volume reactions across 356,463 reports (De Franco et al.
2015). Disclosure bloat predicts lower price efficiency (Kim, Muhn, Nikolaev 2023). The
warning label for this repo: after a major AI research platform rolled out, analyst
reports gained about 40% more distinct sources and 34% more topical coverage while
forecast errors rose 59% (Xue, Zhang, Zhu, Dec 2025 arXiv preprint). Breadth without
synthesis measurably degrades judgment, and it binds hardest on an agent that can
generate breadth for free.

## The eight schools (mechanics worth stealing)

1. **The pyramid (Minto / consulting).** Ideas as a pyramid under one governing thought;
   any point raises a question the next line must answer (the vertical dialogue); SCQA
   openers; groupings pass the plural-noun test; action titles under ~15 words; the
   title test (ToC + exhibit titles alone must carry the thesis); dot-dash storyboards
   before long builds. "Deduction is a useful way to think, but a ponderous way to write."
2. **The narrative memo (Amazon).** Six pages of full sentences read silently at the
   meeting; a great memo takes a week and a fresh-mind re-edit; the PR/FAQ pre-mortem
   (write the future retrospective and the hardest-questions FAQ first). The 1997 letter
   is falsifiable philosophy in prose.
3. **The estimative tradition (Kent, ICD 203, Heuer, Tetlock).** The ICD 203 lexicon
   (bands below); numerical ranges in parentheses after estimative words; confidence
   stated in its own sentence, never fused with likelihood; never modify "possible";
   never stack hedges; granularity carries signal (Tetlock); a forecast without an
   event, a date, and a number cannot be scored, which is its defect; coherence is not
   correctness (four 70% events chained = 24%).
4. **The owner's letter (Buffett, Marks).** The reversed-positions completeness test
   ("the information I would wish them to supply me if our positions were reversed");
   one named intelligent non-specialist as imagined reader; what-we-got-wrong sections
   as credibility structure; know/don't-know sorting; one thesis per memo.
5. **The evidence-first paper (Mauboussin, Damodaran).** Base rates before the company
   story (locate every forecast in the reference-class distribution); reverse the
   valuation and state what's priced in before arguing with it; the 3P gate (possible,
   plausible, probable); every model input maps to a story sentence and back.
6. **The columnist's compression (Economist, Lex, Levine).** Orwell's six rules as the
   copy-edit pass; incentives-first explanation; footnotes carry caveats so the main
   line stays clean; the ~300-word standalone view box. The snark stays out of rated
   research.
7. **The prosecutor's brief (activist shorts).** Every claim carries its exhibit;
   Claim/Reality tables; a questions-for-management appendix; always paired with
   Greenlight-style long/short symmetry, never the genre's one-sidedness.
8. **The compression formats (BLUF, Smart Brevity, the P&G one-pager).** Conclusion
   first at every tier; the first sentence of any section is its bottom line; muscular
   short headline + one strong lede + "why it matters." Morning notes and alerts only;
   reasoning chains stay in full prose.

## The ICD 203 probability lexicon (the house estimative bands)

| almost no chance | very unlikely | unlikely | roughly even chance | likely | very likely | almost certain |
|---|---|---|---|---|---|---|
| remote | highly improbable | improbable | roughly even odds | probable | highly probable | nearly certain |
| 01-05% | 05-20% | 20-45% | 45-55% | 55-80% | 80-95% | 95-99% |

Kent's rules travel with it: "possible" is never modified (no "serious possibility,"
"distinct possibility"); hedges never stack ("we believe" inside "likely" silently
compounds); one odds-bearing word per sentence. Heuer: probability words "are empty
shells" that readers fill with what they already believe; the parenthetical number is
the fix. The confidence rule: likelihood describes the event, confidence describes the
evidence base, and they never share a sentence. Compliant form: "We assess X is likely
(55-80%). Confidence: moderate; the revenue figure is a database projection."

## The sentence-level science

- **Gopen and Swan (1990).** Put the new information you want emphasized at the stress
  position (sentence end); put the linking, old information at the front (topic
  position); keep subject and verb adjacent; one point per unit of discourse. The
  misplacement of old and new information is "the No. 1 problem in American
  professional writing." A sentence is too long when it has more candidates for stress
  than stress positions.
- **Classic style (Thomas and Turner; Pinker).** Prose as a window: the writer has seen
  something and orients the reader's gaze. The enemy is the curse of knowledge; the
  fixes are cold rereads and real readers. Cut metadiscourse, signposting, zombie
  nouns, compulsive qualifiers. Commit on the main claim; state real uncertainty as
  content (conditions, ranges, probabilities), not verbal fuzz. Boosters ("clearly,"
  "obviously") flag the least-supported claim.
- **SEC Plain English Handbook (1998).** Surface hidden verbs ("made an application" ->
  "applied"); write in the positive ("not able" -> "unable"); kill superfluous pairs
  ("in order to" -> "to," "prior to" -> "before"); avoid "respectively"; tabulate
  if-then logic; when a sentence will not clarify, make it a table.
- **Numbers in prose (Heath and Starr; CIA Style Manual).** Round with enthusiasm in
  prose; precision lives in exhibits. Always give the denominator and the comparison.
  Ranges repeat units ("between $10 million and $20 million," never "between $10 and
  $20 million"). "Increased to five times" is fourfold; "five times greater" is
  fivefold; match the construction to the arithmetic. No exclamation points.
- **Sentence length.** Govern by the stress-position test and a 25-word review trigger;
  manage total length and redundancy (the variable the finance studies price), not a
  readability score (Fog is misspecified for finance per Loughran and McDonald 2014).
- **The AI-tell list.** Inflated significance ("pivotal," "marking a shift"), bolted-on
  participial analysis ("...highlighting the importance of"), vague attributions
  ("observers have cited," "industry reports suggest"), copula avoidance ("serves as,"
  "boasts," "stands as" for "is"), rule-of-three filler, synonym rotation, em-dash
  overuse, vocabulary density ("delve," "intricate," "tapestry," "underscore"). Nearly
  every tell violates an older rule, so enforcing the older rules immunizes the output.

## The evidence that writing quality is priced

| Study | Setting | Finding |
|---|---|---|
| Li 2008 | 10-Ks 1994-2004 | Worse earnings come wrapped in harder filings; complexity predicts lower persistence of good earnings |
| Loughran and McDonald 2014 | 10-Ks | Fog is misspecified for finance; do not gate on readability scores |
| Lawrence 2013 | Retail investors | Clear, concise disclosure draws investment; ~58-91 bp per SD of clearer text |
| De Franco et al. 2015 | 356,463 sell-side reports | Trading-volume reactions increase with readability; the commercial KPI of research writing |
| Hwang and Kim 2017 | Closed-end funds | One SD of readability narrows the NAV discount 2.48%: "It pays to write well" |
| Kim, Muhn, Nikolaev 2023 | 10-Ks + LLM summaries | Bloat, not complexity, is the tax; redundancy predicts lower price efficiency |
| Xue, Zhang, Zhu 2025 (preprint) | Post-AI analyst reports | +40% sources, +34% coverage, forecast errors +59%: breadth without synthesis degrades judgment |

## Adopted (Tier 1, now binding; see STYLE.md and the QA scanner)

1. The estimative-language package: lexicon box in reports that make forward calls;
   parenthetical ranges after estimative words in key judgments; confidence in its own
   sentence with the reason; Kent's bans (no modified "possible," no hedge stacks).
2. Key Judgments with falsifiers: initiations and IC memos open with numbered judgments
   carrying odds; the thesis closes with linchpin assumptions, indicators, and dated
   kill criteria.
3. The Mauboussin pair: a base-rate paragraph before the company story and a "what's
   priced in" section before the thesis argues with the price.
4. The ENTER publish gate on the call itself: Expectational, Novel, Thorough,
   Examinable, Revealing. Fails Novel -> monitoring line, not a publication.
5. Extended prose gates in the build: Kent's weasels, boosters, hedge stacks, vague
   attributions, the AI-vocabulary list, mixed range notation, "times greater"
   arithmetic checks. Warnings that force a look, not writers.
6. Candor as standing sections: "what changed since our last note" near the top of
   updates; a what-we-got-wrong ledger in reviews; the reversed-positions question in
   the review checklist.

## Trial on the next report (Tier 2)

Dot-dash storyboard before 30+ page builds; the title test as formal QA; PR/FAQ
pre-mortem for initiations; the cooling-off re-edit and a context-free reader pass; a
~300-word standalone view box atop deep dives; Claim/Reality tables plus a
questions-for-management appendix for contested names, with symmetric bull treatment;
calibration scoring of every parenthetical probability, graded quarterly; incentive-map
paragraphs in governance sections.

## Skipped, with reasons

Fog/readability gates (misspecified); Smart Brevity for research bodies (correct
critique: cannot carry reasoning chains); Amazon's no-bullets absolutism (the Key
Takeaways bullet is a house signature); the Levine voice in rated products (depends on
holding no position); short-seller one-sidedness (import the evidence chains, never the
selection bias); hard 15-20 word sentence averages (weak provenance; use the
stress-position test and the 25-word trigger).

## The reading list

SEC Plain English Handbook (1998) · ICD 203 (2015) · Kent, Words of Estimative
Probability (1964) · Gopen and Swan, The Science of Scientific Writing (1990) · Heuer,
Psychology of Intelligence Analysis (1999), ch. 8 and 12 · Minto, The Pyramid Principle ·
Bezos 1997 and 2017 letters · Orwell, Politics and the English Language (1946) ·
Berkshire letters and Oaktree memos · Mauboussin's paper archive · Hindenburg's Nikola
report (structure, not balance) · Mauboussin and Mauboussin, HBR 2018 · The Economist
Style Guide introduction · Hwang and Kim 2017 · Wikipedia, Signs of AI writing.

## Addendum (August 11, 2026): the syntax layer

A follow-up sweep on sentence-level AI tells, run after the desk flagged the
"clause, comma, dangling analysis" pattern in a draft.

The empirical anchor is the PNAS Biber-feature study (Reinhart et al., "Do
LLMs write like humans? Variation in grammatical and rhetorical styles",
PNAS 2025): across parallel human/LLM corpora, instruction-tuned models used
present participial clauses at 2 to 5 times the human rate, nominalizations
at 1.5 to 2 times, favored "that" clauses as subjects and phrasal
coordination, and used the agentless passive at roughly half the human rate.
The tells are grammatical, not lexical, and they survive model scaling.
Corroboration: the Wikipedia "Signs of AI writing" catalogue (participial
bolt-ons, negative parallelisms, rule-of-three filler, copula avoidance,
synonym rotation) and community linters (vale-ai-tells) that codify the same
patterns.

The practical translation, now binding in STYLE.md ("Sentence shapes"): the
bolt-on ban (no analysis as a trailing participial or appositive; the
payload gets its own predicate), varied sentence openings (QA flags three
consecutive sentences opening on the same word), verbs over nominalizations,
rationed negative parallelism and rule-of-three, the passive restored where
topic position demands it, and no that-clause subjects. Domain absolutes
("$6.9 billion, up 80% YoY") stay: data shorthand rides, analysis drives.

Sources: pnas.org/doi/10.1073/pnas.2422455122 · en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing ·
github.com/tbhb/vale-ai-tells · cmu.edu/dietrich/news 2025 coverage of the PNAS study.
