# Writing Styles Research: The Best Analytical Writing Styles to Incorporate (August 2026)

Prepared 2026-08-11 on branch `claude/analytical-writing-styles-5gu6r0`. A deep web sweep
of the writing traditions that produce the best analytical prose, run against the question
this repo has to answer: how should an analyst OS write initiation notes, deep dives, IC
memos, and morning notes that institutional readers act on.

Method: four parallel research streams (consulting and business frameworks; the
intelligence community's estimative standards; the investment-writing canon; prose science
and the empirical readability evidence), totaling roughly 45 web searches and 90
primary-source fetches on 2026-08-11. Quotes were verified against primary documents
wherever they are public (the ICD 203 PDF, Kent's 1964 CIA paper, the SEC Plain English
Handbook, the Amazon shareholder letters, the Hindenburg Nikola report, the journal
articles); anything that could not be confirmed at source is marked UNVERIFIED. The
house-style baseline is the WRITING MODE doctrine (harrison-core-craft v4.4), the repo's
standing constraints, and the live exemplar published this morning (Q2 2026 Global Unicorn
Tracker, PitchBook Institutional Research, 2026-08-11).

---

## The headline find

**The great traditions converge, and the house already runs most of the convergence.**
Consulting storylining, military BLUF, intelligence tradecraft, the CFA's report guidance,
and the admired investor letters all arrive at the same architecture: state the conclusion
first, make every heading a claim the body must prove, let the reader's next question
choose the next sentence, and treat candor about uncertainty as structure rather than
decoration. The current stack (the answer-first report protocol, declarative section and
chart titles, dated and named sources, the banned-phrase list, the em-dash gate that fails
the build) is that consensus independently reimplemented. This research validates more
than it corrects.

**The one genuinely unclaimed edge is estimative discipline.** The intelligence community
spent seventy years learning, at the cost of real failures, that probability words do not
transmit: Sherman Kent's own board read the signed phrase "serious possibility" as
anything from 20% to 80%, and a 2018 survey of about 1,700 readers found "likely"
interpreted anywhere from 55% to 90% and "real possibility" from roughly 20% to 80%
([Mauboussin and Mauboussin, HBR](https://hbr.org/2018/07/if-you-say-something-is-likely-how-likely-do-people-think-it-is)).
The fix is codified in [ICD 203](https://www.intelligence.gov/assets/documents/intelligence-community-directives/ICD_203.pdf):
a printed probability lexicon, numbers in parentheses after estimative words, and
confidence stated separately from likelihood. The research stream could not find a single
named investment firm that has formally adopted this standard in published research
(UNVERIFIED as an absence; Morningstar uncertainty ratings and bull/base/bear weights are
partial analogs). An analyst OS that prints the lexicon in every report and logs its
probability judgments for calibration would be visibly differentiated at the cost of one
methodology box.

**And writing quality is priced.** This is not a taste question. A one standard deviation
improvement in readability narrows closed-end fund discounts by 2.48%
([Hwang and Kim 2017](https://www.sciencedirect.com/science/article/abs/pii/S0304405X17300193)).
More readable sell-side reports draw larger trading-volume reactions across 356,463
reports ([De Franco et al. 2015](https://onlinelibrary.wiley.com/doi/10.1111/1911-3846.12062)).
Disclosure bloat predicts lower price efficiency
([Kim, Muhn, Nikolaev 2023](https://arxiv.org/abs/2306.10224)). The warning label for this
repo specifically: after a major AI research platform rolled out, analyst reports gained
about 40% more distinct sources and 34% more topical coverage while forecast errors rose
59% ([Xue, Zhang, Zhu, Dec 2025](https://arxiv.org/abs/2512.19705)). Breadth without
synthesis measurably degrades judgment. The writing discipline below is the antidote, and
it binds hardest on an agent that can generate breadth for free.

---

## The eight schools

Each school: where it comes from, the actual mechanics, the documented failure mode, and
what this shop should take. The schools divide cleanly by product: structure schools
(1, 8), depth schools (2, 5), uncertainty schools (3), and voice schools (4, 6, 7).

### 1. The pyramid: Minto and the consulting storyline

Barbara Minto, McKinsey's first female consultant, moved to London in 1966 to fix report
writing and produced the firm's structural doctrine
([The Minto Pyramid Principle](https://www.barbaraminto.com/); first-publication year is
muddled across sources, UNVERIFIED). Core axiom: ideas organized as a pyramid under a
single governing thought. Three rules: ideas at any level summarize the ideas below them;
ideas in a grouping are the same kind of idea; ideas in a grouping are logically ordered
(only three legal orders: time, structure, ranking). The load-bearing mechanic is the
vertical dialogue: "Any point you make must raise a question in the reader's mind, which
you must answer on the line below." SCQA (Situation, Complication, Question, Answer) is
the standard opener, and the plural-noun test is the QA check: a valid grouping can be
labeled with one plural noun ("drivers," "risks," "steps"). Minto on deduction:
"Deduction is a useful way to think, but a ponderous way to write."

The wider MBB toolkit adds action titles (full-sentence titles under about 15 words
stating the implication), the title test ("BCG consultants are trained to write slides
that allow someone to understand a presentation by only reading the titles,"
[Slideworks](https://slideworks.io/resources/bcg-approach-to-great-slides-practical-guide-from-former-consultant)),
dot-dash storyboarding before drafting, the day-one hypothesis, and Rasiel's elevator
test from The McKinsey Way (1999).

Failure modes: answer-first backfires with hostile audiences and in genuinely exploratory
work (premature closure), and Erin Meyer's The Culture Map documents that
principles-first cultures (Germany, France, Russia) read conclusion-first argument as
unearned ([erinmeyer.com](https://erinmeyer.com/the-art-of-persuasion-in-a-multi-cultural-world/)).
Assertion-driven decks whose proof is decorative are the degenerate form; the vertical
logic check exists because this fails constantly.

**Steal:** the title test as a mechanical QA pass (the ToC plus exhibit titles alone must
carry the thesis), the plural-noun test on every grouped section, dot-dash storyboards
before any 30+ page build, and SCQA as the initiation opener: situation is consensus,
complication is what the market misses, question is whether the asset is mispriced,
answer is the rating.

### 2. The narrative memo: Amazon

Bezos banned slide decks in a June 2004 email to the S-Team (subject line as widely
reproduced is UNVERIFIED at primary source): "the narrative structure of a good memo
forces better thought and better understanding of what's more important than what, and
how things are related." The system: six pages, full sentences, data appendices, read
silently for about 30 minutes at the start of the meeting ("study hall") because
executives bluff pre-reads; Bezos called it "probably the smartest thing we ever did"
([CNBC](https://www.cnbc.com/2019/10/14/jeff-bezos-this-is-the-smartest-thing-we-ever-did-at-amazon.html)).
The 2017 shareholder letter adds the scope doctrine: great memos are written, shared,
set aside, and re-edited with a fresh mind; "a great memo probably should take a week or
more" ([aboutamazon.com](https://www.aboutamazon.com/news/company-news/2017-letter-to-shareholders)).
The PR/FAQ (working backwards) writes the future press release and the hardest-questions
FAQ before any build; most PR/FAQs dying is the feature
([workingbackwards.com](https://workingbackwards.com/concepts/working-backwards-pr-faq-process/)).
The 1997 letter, re-attached to every subsequent letter, is the exemplar of a philosophy
stated in falsifiable prose: "When forced to choose between optimizing the appearance of
our GAAP accounting and maximizing the present value of future cash flows, we'll take the
cash flows."

Failure modes (practitioner consensus, no single canonical critic): heavyweight for
reversible low-stakes calls, gates influence on prose skill, and the narrative build sits
in structural tension with Minto's answer-first: Amazon memos often earn the conclusion
rather than opening with it.

**Steal:** the week-plus scope norm with a cooling-off re-edit for deep dives, study-hall
reading at IC, and the PR/FAQ as a pre-mortem for initiations: draft the future "what we
said and whether it held" retrospective and the FAQ of hardest objections before writing
the note.

### 3. The estimative tradition: Kent, ICD 203, Heuer, Tetlock

The deepest codified tradition of writing about uncertain futures for decision-makers,
and the section with the most unclaimed material for this shop.

**Kent (CIA, 1964).** After a policy reader asked what "serious possibility" meant in a
1951 estimate of a Soviet attack on Yugoslavia, Kent polled his own Board of National
Estimates: the authors of the same signed sentence meant anywhere from 20 to 80 percent
([Words of Estimative Probability](https://www.cia.gov/resources/csi/static/Words-of-Estimative-Probability.pdf)).
His response was a five-band odds table (almost certain 93%, probable 75%, chances about
even 50%, probably not 30%, almost certainly not 7%, each with a stated give-or-take) and
two rules that survive intact: the word "possible" must never be modified (no "serious
possibility," "distinct possibility," "might well"), and hedges must not stack, because
"we believe" at 3-to-1 inside "likely" at 3-to-1 silently compounds to worse than 3-to-2.
His weasel list ("apparently," "seemingly," unmodified "reportedly," which "carries no
evaluative weight whatsoever") reads like a modern AI-tell list. His close: "Let the
judgment be unmistakable and let it be unmistakably ours."

**ICD 203 (ODNI, 2015 revision).** The US intelligence community's binding analytic
standards, written after the Iraq WMD failure
([PDF](https://www.intelligence.gov/assets/documents/intelligence-community-directives/ICD_203.pdf)).
The nine tradecraft standards are a complete pre-publication rubric: describe source
quality and credibility; express and explain uncertainties; distinguish underlying
information from assumptions and judgments (with linchpin assumptions stated and the
implications if they fail); incorporate analysis of alternatives; demonstrate customer
relevance; use clear and logical argumentation with the main message up front; explain
change from or consistency with prior judgments; make accurate judgments ("should not
avoid difficult judgments in order to minimize the risk of being wrong"); use effective
visuals. The directive mandates a probability lexicon:

| almost no chance | very unlikely | unlikely | roughly even chance | likely | very likely | almost certain |
|---|---|---|---|---|---|---|
| remote | highly improbable | improbable | roughly even odds | probable | highly probable | nearly certain |
| 01-05% | 05-20% | 20-45% | 45-55% | 55-80% | 80-95% | 95-99% |

And the rule this document's recommendations lean on hardest: analysts "must not combine
a confidence level and a degree of likelihood, which refers to an event or development,
in the same sentence." Likelihood describes the event; confidence describes the evidence
base. "High confidence that X is likely" is a banned construction; the compliant form is
"We assess X is likely (55-80%). Confidence: moderate, because disclosure is thin."

**Heuer (Psychology of Intelligence Analysis, 1999).** Probability words "are empty
shells. The reader or listener fills them with meaning through the context," biased
toward what the reader already believes, so vague reports change no minds
([CIA PDF](https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf)).
His fix, stated as standard practice: put a numerical range in parentheses after every
estimative expression in key judgments. Two more findings that belong in any scenario
section: coherence is not correctness (a vivid chain of four 70% events feels about 70%
likely and is actually 24%, and every added plausible detail raises perceived probability
while lowering the real one), and analysis of competing hypotheses should proceed by
trying to disprove hypotheses, reporting the relative likelihood of all of them, with
indicators that would signal a different course.

**Tetlock (Superforecasting, 2015).** Granularity is information: Good Judgment Project
forecasters using ones (20/21/22%) beat those using fives, who beat those using tens, and
rounding superforecasters to the nearest 0.05 measurably worsens their Brier scores.
The vague-verbiage critique gives the writing rule: a forecast that lacks a defined
event, a date, and a number cannot be scored and therefore cannot be wrong, which is its
defect. Superforecasters also start from the outside view (the base rate for the
reference class) before adjusting on case specifics, because the first number anchors.

The misreading evidence is robust across settings: Wallsten et al. (1986) showed
probability words behave as wide, overlapping distributions with stable individual
dictionaries; 23 NATO officers assigned percentages to standard phrases spanning tens of
points (Barclay et al. 1977, reproduced as Heuer's Figure 18); and Irwin and Mandel's
NATO work (2019, 2023) finds even the adopted lexicons were never empirically validated.
The UK's [PHIA probability yardstick](https://www.gov.uk/government/publications/phia-common-analytical-standards)
improves on ICD 203 with deliberate unassigned gaps between bands (remote chance up to
about 5%, highly unlikely 10-20%, unlikely 25-35%, realistic possibility 40 to just under
50%, likely 55-75%, highly likely 80-90%, almost certain 95%+) so adjacent terms cannot
be argued onto the same number.

Failure mode of the whole tradition: numbers can imply false precision when the evidence
base is thin. The answer is already inside the standard: the confidence statement, kept
in its own sentence, is where thinness gets said.

**Steal:** everything in the Tier 1 recommendations below. This is the highest-value
section of the research.

### 4. The owner's letter: Buffett, Marks, and the fund-letter canon

**Buffett.** The best style guidance he ever gave is the preface to the
[SEC Plain English Handbook](https://www.sec.gov/pdf/handbook.pdf) (1998): "When writing
Berkshire Hathaway's annual report, I pretend that I'm talking to my sisters... My goal is
simply to give them the information I would wish them to supply me if our positions were
reversed. To succeed, I don't need to be Shakespeare; I must, though, have a sincere
desire to inform." And: "No siblings to write to? Borrow mine: Just begin with 'Dear
Doris and Bertie.'" The reversed-positions line is a completeness standard, not a tone
standard. The letters' repeatable mechanics: one named intelligent non-specialist as the
imagined reader, anticipated questions posed and answered, conversational connectives
(But, Yet, So) over "however/moreover," concrete verbs and analogies, and candor about
mistakes as a structural feature that buys credibility for the bullish sections.

**Marks.** One big idea per memo, stated in the title, developed essayistically; roughly
a decade of memos with no reader response before "bubble.com" (January 2000) landed
([Oaktree memos](https://www.oaktreecapital.com/insights/memos); CNBC 35-year
retrospective, 2025). The transferable devices: explicit epistemic sorting (the "I know"
school versus the "I don't know" school; what is knowable is current conditions and where
we stand in the cycle, what is not is forecasts), second-level thinking staged in the
text (consensus expects X; the edge is Y), and self-quotation with callbacks marking
where he was wrong or early. Buffett: "When I see memos from Howard Marks in my mail,
they're the first thing I open and read."

**The fund letters.** Nomad (Sleep and Zakaria, 2001-2014,
[free archive](https://igyfoundation.org.uk)) contributes destination analysis: judge the
business by where it will be in ten-plus years, developed serially across letters.
Fundsmith's letters run an identical skeleton every year, and the consistency is the
device. Greenlight's letters are admired for symmetric long and short theses, the
balanced counterweight to the short-seller genre below.

**Steal:** the reversed-positions completeness test as a review question, a
what-we-got-wrong section in every quarterly and annual review, the know/don't-know
block in verdict sections, and one-thesis-per-document discipline for memos.

### 5. The evidence-first paper: Mauboussin and Damodaran

**Mauboussin** (Credit Suisse, then Morgan Stanley Counterpoint Global;
[paper index](https://www.michaelmauboussin.com/writing)) is the sell-side gold standard
because of two moves. The base-rate move: every forecast is located inside the historical
distribution of what comparable companies actually achieved (The Base Rate Book, 2016),
so "20% growth for a decade" must first argue against the historical distribution
before it can rest on the company story. The expectations move: reverse the DCF and ask what must be true for today's
price to make sense, then handicap those embedded expectations. Paper architecture:
a one-page summary of numbered conclusions, a pedagogical body that teaches the tool
before applying it, an exhibit roughly every page that stands alone, and full academic
apparatus. No canonical self-stated writing rules were found (UNVERIFIED as doctrine;
the mechanics are inferred from the papers).

**Damodaran** (Narrative and Numbers, 2017) supplies the bridge discipline: every story
must pass the 3P test (possible, then plausible, then probable) and then convert into
explicit value drivers; every input must map back to a story sentence, and a growth rate
with no narrative justification is as suspect as a story with no number. His blog
practice adds the feedback loop: publish the valuation with the spreadsheet, state what
would change your mind, and revisit in public.

**Steal:** a base-rate table beside every multi-year forecast, a "what's priced in"
section before the thesis, the 3P gate in IC memos, and a two-column narrative-to-input
map in model sections (the operating model's sourced assumption column is already
halfway there).

### 6. The columnist's compression: The Economist, Lex, Alphaville, Levine

The Economist Style Guide's introduction is the register manual: "Clarity of writing
usually follows clarity of thought. So think what you want to say, then say it as simply
as possible," and "Do not be stuffy"
([12th edition PDF](https://cdn.static-economist.com/sites/default/files/pdfs/style_guide_12.pdf)).
It adopts Orwell's six rules from Politics and the English Language wholesale, including
the sixth: "Break any of these rules sooner than say anything outright barbarous"
([Orwell Foundation](https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/)).
FT Lex proves a view survives in about 300 words with a kicker (the word count is the
standard industry description, UNVERIFIED as a formal rule). Alphaville's contribution is
document-driven skepticism: pull the filing footnote everyone skipped (Wirecard is the
exemplar). Levine's Money Stuff mechanics, per the profiles: incentives-first explanation
(every scandal re-narrated as rational actors responding to a structure), assuming much
of the audience knows more than the writer, hypothetical dialogues, steelman-then-rebut
sequencing, and footnotes that carry the caveats so the main line stays clean.

Where it does not fit: the columnist voice depends on having no position, no target, and
no liability for a call. Snark corrodes rated research.

**Steal:** Orwell's six rules as the copy-edit checklist, a Lex-length view box atop
deep dives, footnote-forensics as a standing risks-section method, incentive-map
paragraphs for governance sections, and footnoted caveats to keep argument lines clean.

### 7. The prosecutor's brief: activist short research

The Hindenburg Nikola report (2020) is the anatomy lesson
([primary](https://hindenburgresearch.com/nikola/)): position disclosed first (bias
converted into stated stakes), thesis in one sentence, executive-summary bullets
quantifying each allegation before any narrative, then claim-evidence-exhibit chains
(allegation header, context, the document itself, corroboration, conclusion), paired
"Claim / Reality" subheads, radical quantification down to video timestamps, and a
closing list of 53 questions for management that pre-empts the rebuttal. Muddy Waters
runs the same forensic architecture. The calibration caution is structural: these are
advocacy documents written to move a price; effectiveness comes from evidence density,
not balance.

**Steal:** the evidence-chain discipline (every claim carries its exhibit), Claim/Reality
tables for bear cases, and a questions-for-management appendix, always paired with
Greenlight-style symmetry rather than the genre's one-sidedness.

### 8. The compression formats: BLUF, Smart Brevity, the one-pager

**BLUF** is codified in US Army Regulation 25-50: "Effective Army writing is understood
by the reader in a single rapid reading" with "the main point at the beginning of the
correspondence (bottom line up front)" and active voice
([armypubs PDF, 2020 edition](https://armypubs.army.mil/epubs/DR_pubs/DR_a/ARN31586-AR_25-50-000-WEB-1.pdf)).
ICD 203's "main analytic message up front" is BLUF for analysis.

**Smart Brevity** (VandeHei, Allen, Schwartz, 2022) is the four-part unit: a muscular
six-word headline, one strong lede sentence, a labeled "Why it matters" paragraph, and
optional "Go deeper." Doctrine: "Brevity is confidence. Length is fear." The critiques
are real: Colin Dickey in The New Republic argues the format cannot "preserve anything
like the complexity required to process deep, conceptual problems"
([review](https://newrepublic.com/article/167733/axios-guide-writing-well-neither-smart-brief-smart-brevity-book-review)),
and the Washingtonian notes readers learn to skip the repeated axiom headers. Both are
correct, and both are irrelevant to the morning-note use case.

**The P&G one-page memo** is the oldest member: president Richard Deupree returned long
memos with "Boil it down to something I can grasp," and the reco structure (idea,
background, how it works, benefits with support, next steps) still runs at P&G.

**Steal:** the tiering itself. Compression formats own the top of the funnel (morning
notes, alerts, screeners), pyramid structure owns published research, narrative memo
logic owns the point of decision. Same invariant at every tier: conclusion first, and
the first sentence of any section is its bottom line.

---

## The evidence that writing quality is priced

The empirical case, in one table. These are the studies to cite when someone calls prose
style a soft preference.

| Study | Setting | Finding |
|---|---|---|
| Li 2008, J. Accounting and Economics | 10-Ks, 1994-2004 | Mean 10-K Fog 19.4 (WSJ editorials run about 15.2); worse earnings come wrapped in harder, longer filings; complicated reports predict lower persistence of good earnings (obfuscation is informative) |
| Loughran and McDonald 2014, J. Finance | 10-Ks | The Fog index is misspecified for finance (polysyllables like "management" and "operations" are not hard); file size beats it as a readability proxy. Do not gate on Fog |
| Lawrence 2013, J. Accounting and Economics | Retail investors | Individuals invest more in firms with clear, concise disclosure; roughly 58-91 bp of return improvement per standard deviation of clearer, shorter text against a ~200 bp information disadvantage |
| De Franco, Hope, Vyas, Zhou 2015, Contemporary Accounting Research | 356,463 sell-side reports, 2002-2009 | Trading-volume reactions increase with report readability; higher-ability analysts write more readably. The direct commercial KPI of research writing |
| Hwang and Kim 2017, J. Financial Economics | Closed-end funds | One standard deviation of readability narrows the discount to NAV by 2.48%; title says it: "It pays to write well" |
| Kim, Muhn, Nikolaev 2023 | 10-Ks and LLM summaries | Good summaries are over 70% shorter with amplified information content; measured "bloat" predicts lower price efficiency and higher information asymmetry. Redundancy, not complexity, is the tax |
| Xue, Zhang, Zhu, Dec 2025 (arXiv) | Analyst reports post-AI adoption | About +40% distinct sources, +34% topical coverage, +25% advanced methods, and forecast errors up 59%. Breadth without synthesis degrades judgment |

The last row is the one this repo should pin above the desk. The failure mode of an AI
analyst is not too little material; it is unsynthesized material presented fluently.

---

## The sentence-level science

The micro-style with provenance, ordered by how much each rule is worth.

**Reader-expectation mechanics (Gopen and Swan, American Scientist, 1990;
[full text](https://cseweb.ucsd.edu/~swanson/papers/science-of-writing.pdf)).** The
highest-value sentence rules in the literature, and fully compatible with dense
technical content. Put the new information you want emphasized in the stress position
(the end of the sentence, the point of syntactic closure). Put the thing the sentence is
about in the topic position (the front), and make it old information that links backward:
"the misplacement of old and new information turns out to be the No. 1 problem in
American professional writing today." Follow a subject with its verb immediately
(anything long between them reads as an interruption). One point per unit of discourse,
at every scale. Their definition of overlong is structural, not numeric: a sentence is
too long when it has more candidates for stress than stress positions. They also defend
the passive when the paragraph's protagonist demands it, a corrective to blanket
active-voice rules.

**Classic style and the curse of knowledge (Thomas and Turner 1994; Pinker, The Sense of
Style, 2014).** Treat prose as a window: the writer has seen something and orients the
reader's gaze so the reader sees it too. The chief cause of bad writing is the curse of
knowledge (the difficulty of imagining not knowing what you know), and the only reliable
fixes are showing drafts to real readers and rereading cold. Pinker's cut list:
metadiscourse ("In this section we will examine..."), signposting, apologizing,
professional narcissism, zombie nouns, and compulsive qualifiers ("somewhat," "fairly,"
"to some extent," "I would argue"). His resolution on hedging: commit on the main claim,
and where uncertainty is real, state it as content (conditions, ranges, probabilities),
not verbal fuzz. Hyland's corpus work adds the caution in the other direction: boosters
("clearly," "obviously") are inverse weasels, and in a research note "clearly" usually
flags the least-supported claim.

**The SEC Plain English Handbook (1998, [PDF](https://www.sec.gov/pdf/handbook.pdf)).**
The most finance-native style document in existence, with before/after examples from
real filings. Its nine common problems: long sentences, passive voice, weak verbs,
superfluous words, jargon, numerous defined terms, abstract words, unnecessary detail,
unreadable design. The prescriptions that generalize: surface hidden verbs ("made an
application" becomes "applied"; "there is the possibility of prior Board approval"
becomes "the Board might approve in advance"); write in the positive ("not able" becomes
"unable"); kill the superfluous pairs ("in order to" becomes "to," "prior to" becomes
"before"); avoid "respectively" (it forces the reader to walk back and match); tabulate
if-then logic; and when a sentence still will not clarify, present the information as a
table.

**Numbers in prose (Heath and Starr, Making Numbers Count, 2022; CIA Style Manual, 8th
ed. 2011).** Round with enthusiasm in prose (readers keep 6, not 5.684; precision lives
in the exhibits), translate to human scale, and normalize per unit (per employee, per
user, per dollar raised) so magnitudes become judgeable. Always give the denominator and
the comparison. The CIA manual contributes two precision rules finance writing violates
constantly: ranges repeat units ("between $10 million and $20 million," never "between
$10 and $20 million"), and "increased to five times" is a fourfold increase while "five
times greater" is a fivefold one; pick the construction that matches the arithmetic. Its
register rule fits rated research exactly: intelligence is dispassionate; the
exclamation point "should rarely, if ever, be used."

**Sentence length, honestly stated.** The circulating numbers (15-20 word averages;
comprehension collapsing above 40 words) trace to plain-language advocacy with weak
accessible primary evidence; GOV.UK's 25-word editorial trigger is policy, not science.
Govern instead by Gopen and Swan's structural test plus a 25-word review trigger, and
manage total length and redundancy (the variable the finance studies actually price)
rather than a readability score (misspecified per Loughran and McDonald).

**The AI-tell list (Wikipedia's
[Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)).**
The negative space: inflated significance ("pivotal," "marking a shift"), bolted-on
participial analysis ("...highlighting the importance of"), vague attributions
("observers have cited," "industry reports suggest"), negative parallelisms, rule-of-three
filler, copula avoidance ("serves as," "boasts," "stands as" for "is"), synonym rotation,
em-dash overuse, and vocabulary density ("delve," "intricate," "tapestry," "underscore").
The deeper point: nearly every tell is a violation of an older rule (prefabricated
phrases per Orwell, nothing in the stress position per Gopen and Swan, gesturing instead
of showing per classic style), so enforcing the older rules largely immunizes the output.
The house banned-phrase list and em-dash gate are this insight already running in
production; the extension list is in Tier 1 below.

---

## Gap analysis against the house style

| Capability | Current coverage | Gap | Best fill |
|---|---|---|---|
| Answer-first architecture | Report protocol leads with sharpest data point; BLUF native in morning notes | None; convergent with Minto, AR 25-50, ICD 203 std 6 | Keep |
| Claim titles | Chart-title thesis rule; live report section heads are claims | ToC-level QA is manual | Title test as a build-time checklist item |
| Estimative language | Scenario probabilities appear in models; no word-number map in prose | Probability words uncalibrated; confidence and likelihood mixed | ICD 203 lexicon + parenthetical odds + confidence separation (Tier 1.1) |
| Fact vs assumption vs judgment | Sources dated and named; estimates labeled; TTM flag doctrine | Linchpin assumptions and their failure implications not standard | ICD 203 std 3 block in initiations (Tier 1.2) |
| Alternatives and falsifiers | Stress-test section; strongest-objection rule in scoring frameworks | No standing what-would-change-our-mind box with indicators and dates | Heuer ACH-lite + Tetlock kill criteria (Tier 1.2) |
| Base rates and priced-in | Benchmark table in quant mode; growth-adjusted comps | Not mandatory in report flow; no expectations section | Mauboussin pair of sections (Tier 1.3) |
| Publish gate | Two-pass review (critical/informational) | No novelty/examinability screen on the call itself | Valentine ENTER (Tier 1.4) |
| Prose gates | Em-dash build gate; banned-phrase list | Weasels, boosters, modified "possible," hedge stacks, range notation unscanned | Extend the docx scanner (Tier 1.5) |
| Candor devices | Validation log; verification caveats sections | No named-reader completeness check; no standing what-we-got-wrong section | Buffett reversed-positions + error ledger (Tier 1.6) |
| Change from prior note | Practiced (Q1 score non-comparability note) | Not codified | ICD 203 std 7 one-liner (Tier 1.6) |
| Scope and process | Validation-first build cadence | No cooling-off re-edit or cold-reader pass | Amazon scope doctrine + doc-coauthoring reader test (Tier 2) |
| Compression tier | Morning note under 300 words doctrine | Format not templated | Smart Brevity unit, small stable header set (Tier 2) |

---

## Recommendations

### Tier 1: adopt now

**1. The estimative-language package.** The single highest-value adoption, with seventy
years of IC precedent and no visible competitor in published investment research. Four
parts. (a) Print the ICD 203 probability lexicon (the table above, or PHIA-style bands
with gaps) as a methodology box in every report template. (b) In key-judgment sentences,
put a numerical range in parentheses after every estimative word: "a down round within
18 months is likely (55-80%)." Allow finer granularity where the evidence supports it;
Tetlock's data says fine gradations carry signal. (c) State confidence in its own
sentence, never fused with likelihood, and make the confidence sentence say why: "We
assess X is likely (60-70%). Confidence: moderate; the revenue figure is a T4 database
projection." This slots directly into the existing T1-T5 source-authority rubric, which
is already an ICD-grade sourcing standard waiting for its uncertainty twin. (d) Adopt
Kent's bans: never modify "possible," never stack hedges, one odds-bearing word per
sentence.

**2. Key Judgments with falsifiers.** Open every initiation and IC memo with a Key
Judgments block (three to six numbered judgments, each carrying its parenthetical odds
and one-line evidence basis), and close the thesis section with a falsifier box: the
linchpin assumptions, what breaks if each fails, the indicators that would move the
estimate, and Tetlock-style kill criteria with dates ("what observation, by what date,
counts as wrong"). The thesis-tracker workflow already holds catalysts and confidence;
this makes the falsifiers first-class in the published document. For contested calls,
add an ACH-lite table: the two or three live hypotheses against the evidence, scored by
what each piece would disconfirm, reporting the relative likelihood of all of them.

**3. The Mauboussin pair.** Two mandatory sections in every initiation: a base-rate
paragraph before the company story (where the forecast sits in the reference-class
distribution; the quant-mode benchmark table is the seed) and a "what's priced in"
section that reverses the valuation before arguing with it. The Damodaran 3P test
(possible, plausible, probable) becomes the IC-memo gate for any narrative that feeds a
model input, and the model's sourced-assumption column becomes a two-way map: every
input cites a story sentence, every story sentence lands on an input.

**4. The ENTER publish gate.** Before any note ships, the call itself passes Valentine's
screen: Expectational (forward-looking), Novel (the market does not already have it),
Thorough, Examinable (a trusted colleague could replicate the conclusion from the note),
Revealing (says where it could be wrong). Anything that fails Novel becomes a monitoring
line, not a publication. This is the writing-level twin of the validation spine.

**5. Extend the prose gates in the build.** The em-dash gate proves the pattern:
mechanical scans catch what tired editors miss. Add to the docx scan: Kent's weasels
("apparently," "seemingly," bare "reportedly," any modified "possible"), booster words
("clearly," "obviously," "undoubtedly"), hedge stacks (two estimative words in one
sentence), vague attributions ("observers note," "some argue," "industry reports
suggest"), the AI-vocabulary list, mixed range notation ("between $10 and $20 million"),
and "X times greater" arithmetic misuse. Keep them as warnings except the existing hard
fails; the scanner's job is to force a look, not to write.

**6. Candor as standing sections.** Three cheap, compounding devices: a "what changed
since our last note" line near the top of every update (ICD 203 standard 7; the Q1
non-comparability note in the unicorn report is the house already doing this once); a
what-we-got-wrong ledger in every quarterly review (Buffett; also ENTER's Revealing);
and the reversed-positions question added to the review checklist ("does this note give
the reader the information we would demand if positions were reversed?"), with a named
imagined reader per product (the IC member for memos, the LP for letters, the smart
non-specialist for media work).

### Tier 2: trial on the next report

- **Dot-dash storyboard before any 30+ page build**, reviewed at outline stage where
  changes are cheap; the storyline compiles into the section plan.
- **The title test as a formal QA step**: read the ToC plus every exhibit title in
  sequence and check that the argument reconstructs. `extract_toc.py` already harvests
  the Contents; extending it to emit the title-only storyline for review is a small step.
- **PR/FAQ pre-mortem for initiations**: draft the future retrospective and the
  hardest-questions FAQ before the note; surviving questions become the risks section.
- **Study hall and the cooling-off edit**: IC memos read silently in the meeting; deep
  dives get a set-aside day and a cold re-edit before render, plus a context-free
  reader pass (the doc-coauthoring skill's reader test is this exact gate).
- **A Lex-length view box** (about 300 words with a kicker) atop deep dives, written
  last, publishable standalone.
- **Claim/Reality tables and a questions-for-management appendix** for bear cases and
  governance-contested names, paired with symmetric bull treatment.
- **Calibration scoring**: log every parenthetical probability with its date and
  resolution criterion in the validation log; score quarterly. The estimative package
  only compounds if the numbers get graded.
- **Incentive-map paragraphs** in governance sections: who gets paid when what happens,
  in two sentences per actor.

### Skip, with reasons

| Candidate | Why skip |
|---|---|
| Fog/readability-score gates | Misspecified for finance (Loughran and McDonald 2014); manage bloat and word choice directly |
| Smart Brevity for research bodies | Dickey's critique is correct where reasoning chains matter; keep it to morning notes and alerts |
| Amazon's no-bullets absolutism and six-page cap | The house Key Takeaways bullet is a signature that works; deep dives legitimately run long. Take the scope doctrine, not the format dogma |
| The Levine voice in rated products | Depends on holding no position and no target; keep for teach-in sidebars only |
| Short-seller one-sidedness | Import the evidence chains, never the selection bias; Einhorn symmetry is the pairing rule |
| Hard 15-20 word sentence averages | Weak provenance; use the stress-position test and a 25-word review trigger instead |
| Kent's bare five-band table | Superseded; ICD 203's seven bands (or PHIA's gapped bands) are the modern standard |

---

## The reading list

The primary sources, in the order a new analyst should read them:

1. SEC, [A Plain English Handbook](https://www.sec.gov/pdf/handbook.pdf) (1998): the finance-native micro-style, with Buffett's preface.
2. ODNI, [ICD 203 Analytic Standards](https://www.intelligence.gov/assets/documents/intelligence-community-directives/ICD_203.pdf) (2015): the nine standards and the probability lexicon.
3. Sherman Kent, [Words of Estimative Probability](https://www.cia.gov/resources/csi/static/Words-of-Estimative-Probability.pdf) (1964): why the lexicon exists.
4. Gopen and Swan, [The Science of Scientific Writing](https://cseweb.ucsd.edu/~swanson/papers/science-of-writing.pdf) (1990): the sentence mechanics.
5. Heuer, [Psychology of Intelligence Analysis](https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf) (1999): chapters 8 and 12.
6. Minto, [The Pyramid Principle](https://www.barbaraminto.com/) (1996 edition): structure.
7. Bezos, [1997](https://www.aboutamazon.com/news/company-news/amazons-original-1997-letter-to-shareholders) and [2017](https://www.aboutamazon.com/news/company-news/2017-letter-to-shareholders) shareholder letters: falsifiable philosophy and the scope doctrine.
8. Orwell, [Politics and the English Language](https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/) (1946): the six rules.
9. [Berkshire letters](https://www.berkshirehathaway.com/letters/letters.html) and [Oaktree memos](https://www.oaktreecapital.com/insights/memos): the voice canon.
10. [Mauboussin's paper archive](https://www.michaelmauboussin.com/writing): base rates and expectations in practice.
11. Hindenburg, [the Nikola report](https://hindenburgresearch.com/nikola/) (2020): evidence-chain anatomy (read for structure, not for balance).
12. Mauboussin and Mauboussin, [If You Say Something Is "Likely"...](https://hbr.org/2018/07/if-you-say-something-is-likely-how-likely-do-people-think-it-is) (HBR 2018): the misreading evidence in one chart.
13. The Economist, [Style Guide introduction](https://cdn.static-economist.com/sites/default/files/pdfs/style_guide_12.pdf): register.
14. Hwang and Kim, [It pays to write well](https://www.sciencedirect.com/science/article/abs/pii/S0304405X17300193) (JFE 2017): the price of prose.
15. Wikipedia, [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing): the negative space.

---

## Verification caveats

Captured 2026-08-11. Verified against the hosted primary documents: ICD 203 (bands,
standards language, the confidence/likelihood rule), Kent 1964 (the Yugoslavia episode,
the odds table, the "possible" rule), Heuer 1999 (the empty-shells passage, parenthetical
numbers as standard practice, the 0.7^4 scenario math), AR 25-50 (the BLUF language),
the SEC handbook (Buffett preface, prescriptions and examples), Gopen and Swan (the
principles, quoted), Orwell (the six rules), the 2017 Amazon letter (the scope quotes),
the Hindenburg Nikola report (structure and specifics), and the CIA Style Manual 8th
edition scan (foreword, range and multiplier rules).

Known soft spots, all flagged in place: the Bezos 2004 email subject line and the exact
first-publication year of Minto's book; Zinsser and Thomas/Turner wording sourced from
book-note compilations rather than print pages; the Lex 300-word figure as industry
description rather than formal rule; Valentine's frameworks confirmed via his firm's
public materials (CASCADE has reportedly been superseded by a newer acronym in his
current training); the 15-20 word sentence-length numbers, whose provenance is
plain-language advocacy rather than accessible primary studies; morning-note conventions
as folk practice; and the claim that no investment firm has formally adopted an IC-style
lexicon, which is an absence of evidence after search, not proof of absence. Effect
sizes for the readability studies were taken from the papers or their SSRN/journal
abstracts as linked. The Xue, Zhang, Zhu study is a December 2025 arXiv preprint and
should be treated as not yet peer-reviewed.
