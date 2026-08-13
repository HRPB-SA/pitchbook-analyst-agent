# Ten ideas for a fully automated research desk

*Design note. Written 2026-08-13. Companion to ARCHITECTURE.md, which describes
what exists; this describes what to build next and why.*

---

## The short version

The system already turns a finished set of facts into a handsome, gated
document. That half works. What is still done by hand is everything on either
side of it: finding the information in the first place, deciding what is worth
saying, checking that the words and the numbers agree, and making the writing
sound like a person rather than a machine.

So the honest summary of where we stand is this. **The bottleneck is not
writing. It is evidence, and it is judgment.** A language model can produce a
confident paragraph about a company in four seconds. What it cannot do
reliably, on its own, is know whether the number in that paragraph is true,
where it came from, whether it contradicts something on page nine, and whether
the point was worth making. Every idea below is aimed at one of those four
problems.

The ten ideas, in one line each:

| # | Idea | Fixes |
|---|---|---|
| 1 | **The Harvester** — a scheduled, repeatable sweep of a fixed source list per company | Research is ad hoc and unrepeatable |
| 2 | **The Evidence Locker** — archive the raw source text behind every fact | Numbers can't be traced or defended |
| 3 | **The Claim Ledger** — every number in the report is a pointer, not a typed digit | Prose, tables, charts and models disagree |
| 4 | **The Signal Engine** — the system proposes what to write about, and in what format | Report ideas depend on someone noticing |
| 5 | **The Analysis Library** — a menu of named analytical moves with required inputs | Analysis depth varies by luck |
| 6 | **The Voice Engine** — a measured fingerprint plus a critic that rewrites toward it | Style rules catch bad writing but don't produce good writing |
| 7 | **The Variety Planner** — forces a different structure than the last several reports | Everything starts to read the same |
| 8 | **The Exhibit Designer** — picks the chart that proves the specific claim | Charts are decoration chosen by habit |
| 9 | **The Model Factory** — one skeleton, four model types, built from the fact store | Financial models are hand-built one at a time |
| 10 | **The Red Team and the Learning Loop** — argue against the draft; learn from every edit | The system never gets better on its own |

Ideas 1 through 3 are the foundation. If only three get built, build those.

---

## Where the system stands today

Worth stating plainly, because the roadmap only makes sense against it.

**What is genuinely strong.** The fact store is unusually well designed. Every
value carries its date, its source, and a quality tier, and when two sources
disagree the system refuses to pick a winner silently — it freezes both and
flags the conflict. Templates are enforceable contracts rather than
suggestions. The build gate blocks a document that breaks the rules instead of
warning about it. The style profiler measures the existing body of work rather
than guessing at it. That is a better foundation than most desks have.

**What is still a person doing it by hand.** Research: a human or an agent
decides where to look, looks, and types up what it found. Idea generation:
someone notices that something moved. Verification that the report's own
numbers agree with each other: eyeballing. Financial models: one 647-line
script that only knows how to model one company. Voice: a list of banned
phrases, which prevents bad writing without causing good writing.

The gap, then, is not the document factory. It is the intelligence feeding it.

---

## How the finished system would run

Before the ten ideas, here is the shape they add up to. Read it as a day in
the life of the desk.

```
      OVERNIGHT, UNATTENDED
      ─────────────────────
  1.  HARVEST     sweep every source for every covered company
  2.  EXTRACT     pull candidate facts out of what came back
  3.  VERIFY      cross-check, tier, freeze conflicts, archive the raw text
  4.  DETECT      what changed? what fired? what went stale?
  5.  PROPOSE     rank what is worth writing; draft the request

      MORNING, WITH A HUMAN
      ─────────────────────
  6.  APPROVE     you pick from the ranked list (30 seconds)

      THEN, UNATTENDED AGAIN
      ─────────────────────
  7.  PLAN        choose the analytical moves and the structure
  8.  MODEL       build the workbook from the store
  9.  DRAFT       write, grounded only in stored facts
 10.  EXHIBIT     design the charts that prove each claim
 11.  CRITIQUE    voice pass, red team pass, number-agreement pass
 12.  BUILD       document, gate, validation log

      BEFORE IT GOES OUT
      ─────────────────────
 13.  REVIEW      you read it and edit
 14.  LEARN       your edits become rules
```

Two human touchpoints: thirty seconds in the morning to pick, and a real read
before it ships. Everything else runs on its own. The second touchpoint never
goes away, and should not — but the system should learn from it, which is
idea 10.

---

# The ten ideas

---

## 1. The Harvester: turn research into a repeatable sweep

**The problem.** Right now, research means an agent decides where to look and
then looks. Two runs a week apart may consult different sources and produce
different answers, and neither run leaves a record of what it chose not to
look at. You cannot audit a search that was improvised, and you cannot tell
the difference between "there was no news" and "nobody checked."

**The idea.** Replace improvisation with a fixed, per-company **source
matrix** — a written list of every place worth looking, and how often. The
harvester walks that list on a schedule and brings back everything, whether or
not it seems interesting. Deciding what matters happens later, and separately.

**How it works.** Each company gets a source manifest listing regulatory
filings, the structured data provider, company channels (blog, newsroom,
engineering posts, careers page, pricing page, documentation), a defined set
of trade press, executive social accounts, court and trademark records where
relevant, and job postings. Each source carries a check frequency and an
expected content type.

The sweep runs nightly. For each source it fetches, compares against what it
saw last time, and records one of three outcomes: unchanged, changed (with the
difference), or unreachable. That third outcome is the valuable one — an
unreachable source becomes a visible gap rather than a silent hole.

**Two details that make it work rather than merely run.**

*Watch the boring pages.* A company's pricing page, careers page, and
documentation change before its press releases do. Headcount by function,
pulled from job listings, is a leading indicator that arrives months before a
formal figure. Pricing changes tell you about competitive pressure directly.
These sources are unglamorous, machine-readable, and almost nobody watches
them systematically.

*Record absence.* "No filings this quarter" is a finding. "The newsroom has
not been updated in 90 days" is a finding. A system that only records what it
found cannot tell you about a silence.

**What gets built.** A `sources.json` manifest per company; `engine/harvest.py`
with a `harvest` command; a raw capture directory; a per-run report of
changed, unchanged, and unreachable.

---

## 2. The Evidence Locker: never store a number without its sentence

**The problem.** Today a fact records its source as a piece of text — a name, a
URL. That is enough to attribute a claim but not enough to defend it. If a
figure is challenged six months later, the underlying page may have changed or
disappeared, and nobody can reconstruct exactly what it said. Worse, a
language model reading a source and writing down a number is a step where
errors enter invisibly. Nothing in the current design catches a number that
was misread.

**The idea.** Under the fact store, add a layer that keeps **the raw material
itself**. Every fact points to an evidence record: the archived text, the URL,
the date it was retrieved, a content hash, and — this is the important part —
**the exact sentence or table cell the number was taken from.**

**How it works.** The harvester writes evidence records. Extraction reads them
and produces candidate facts, each carrying the identifier of its evidence and
the character range of the specific span it came from. A fact without a
resolvable evidence span cannot enter the store. That single rule makes an
entire category of error impossible: the system cannot record a number it did
not read somewhere.

**What this unlocks.**

*Verification becomes mechanical.* A checking pass re-reads the quoted span
and asks one narrow question: does this text support this value? That is a far
easier and far more reliable judgment than "is this true," and it catches
misreadings.

*Cross-checking gets real.* Two facts derived from two evidence records that
trace back to the same original announcement are one source, not two. With
evidence recorded properly, the system can detect that automatically — which
is exactly the rule the runbook already states but currently relies on a human
to apply.

*Claims become clickable.* Every figure in the finished report can carry a
hidden pointer back to the sentence that produced it. That is the difference
between a report that cites and a report that can be audited.

**What gets built.** `engine/evidence.py`; an `evidence/` store per company;
an extra required field on the Fact shape; a `verify` command that re-checks
spans and flags any that no longer support their value.

---

## 3. The Claim Ledger: numbers are pointers, not typed digits

**The problem.** A single figure can appear in five places in one report — the
summary bullets, the body text, a table, a chart, and the financial model. Each
is currently typed or generated independently. Nothing checks that they match.
This is the most likely way an embarrassing error reaches a reader, and it is
entirely preventable.

**The idea.** Writers stop typing numbers. Instead they write a **reference**,
and the build resolves it. `{{databricks.valuation.latest}}` becomes
"$188 billion" at build time, formatted per house style, and the exact same
resolution feeds the chart and the model.

**How it works.** The block grammar gains a reference token. At build time
every token resolves against the store; an unresolvable one fails the build.
Charts and models read the same references, so the three cannot drift apart.

Then a final sweep does something the system cannot do today: it collects every
number that appears anywhere in the finished document — resolved references,
chart labels, table cells, model outputs — and checks them against each other.
Same underlying fact, two different values? Build fails. A percentage change
that does not follow from its two endpoints? Build fails. A total that does not
equal its parts? Build fails.

**Why this matters more than it sounds.** Arithmetic that does not survive
scrutiny is the single most damaging error a research note can contain,
because it invites the reader to distrust everything else. It is also the
error most amenable to being solved permanently by a machine. A system that
can never contradict itself has an advantage no human desk has.

**What gets built.** Reference resolution in `engine/compose.py`; a numeric
extraction and consistency check in `engine/qa.py` promoted to FAIL; a claims
appendix in the validation log listing every figure, its source fact, and every
place it appeared.

---

## 4. The Signal Engine: the system proposes, you dispose

**The problem.** A report gets written when someone notices something. That
makes coverage depend on attention, which is finite and uneven. The tracker
refresh detects changes, but turning a change into "this deserves a note, of
this type, with this angle" is still a human judgment made from scratch each
time.

**The idea.** Score every detected change for how much it should matter, rank
them, and produce a short ranked list each morning with a drafted request
attached to each. Your job shrinks to picking.

**How it works.** Each change gets scored on a handful of plain dimensions:

- **Size** — how big is the move, relative to that company's own history?
- **Surprise** — does it contradict what we said last time? (A change that
  breaks our own prior view is worth more than one that confirms it.)
- **Confirmation** — how many independent sources, at what quality tier?
- **Reach** — how many other covered companies does this touch?
- **Freshness** — is this new, or are we late?
- **Silence** — has this company gone unusually quiet? (Absence scores too.)

The scores combine into a ranked list. For each item near the top, the system
drafts a complete request: which company, which template, the specific question
the note should answer, the facts already in hand, and the gaps that need
filling. You approve, adjust, or ignore.

**The design decision that matters.** Report *type* should be inferred from
the shape of the signal, not chosen by hand. A single dated event affecting
one company is a rush note. A trigger firing on an existing view is an update.
A pattern appearing across four companies at once is a sector piece. First
coverage of a company is an initiation. Encode that mapping and the system
picks its own format correctly almost every time.

**What gets built.** `engine/signal.py`; a scoring configuration; a
`propose` command writing candidate requests to the queue; a morning digest
of the ranked list.

---

## 5. The Analysis Library: name the moves and require their inputs

**The problem.** "Analyze the company" is not an instruction a machine can
follow well, and it is not really an instruction a junior analyst can follow
well either. Without a defined repertoire, the depth of analysis in any given
report depends on whether the writer happened to think of the right angle.

**The idea.** Write down the analytical moves the desk actually makes, as a
library. Each entry names the move, states what question it answers, lists the
inputs it requires, gives the arithmetic, and shows a worked example. The
planner picks three or four per report; the drafter executes them.

**A starting library.** Each of these is a distinct, teachable move:

1. **The base rate.** Before the company's own story, what usually happens to
   companies in this position? Establishes the outside view first, which is the
   single most effective guard against being talked into a narrative.
2. **What is already expected.** Work backward from the current valuation to
   the growth it implies, then ask whether that is achievable. Argue with the
   expectation, not with the price.
3. **Unit economics.** What does one customer cost to win, what do they pay,
   how long do they stay, what is left over? The engine of every subscription
   business, and where most stories break down.
4. **Capital efficiency.** How much value has been created per dollar of equity
   raised? (Equity only — the house ruling on this is fixed and must stay
   wired into the arithmetic.)
5. **Growth quality.** Is growth coming from new customers, from existing
   customers spending more, or from price increases? Same headline number,
   three completely different futures.
6. **The cost curve.** For businesses where the main input keeps getting
   cheaper, where does that leave margins in three years?
7. **Concentration.** How much depends on the largest few customers, the
   largest partner, or one product?
8. **The path to exit.** What has to be true, by when, for this to end well?
   And what does the record of similar companies say about how long that takes?
9. **The bear case at full strength.** The strongest honest argument against
   the view — written to convince, not to be knocked down.
10. **The falsifier.** The single published number that would change the
    answer, with a date attached.

**Why a library beats a prompt.** Each move has required inputs, so the system
knows in advance what to go find — the library becomes a research checklist as
well as a writing guide. Each move has fixed arithmetic, so the calculation is
deterministic rather than improvised. And a named move can be measured: over
time you learn which ones actually predicted well.

**What gets built.** `analysis/` with one specification per move;
`engine/plan.py` to select moves per report; required-input checks that feed
back into the harvester.

---

## 6. The Voice Engine: from banned words to a measured fingerprint

**The problem.** The current approach is subtractive. There is a list of
phrases that are not allowed, a list of machine-writing tells, and a list of
jargon. This is genuinely useful and unusually well built — but preventing bad
writing is not the same as producing good writing. A draft can pass every
check and still be flat, and still not sound like you.

**The idea.** Two additions. First, a **fingerprint**: a measured description
of how you actually write, richer than the current profile. Second, a
**critic**: a pass that reads the draft against the fingerprint, scores it, and
rewrites the parts that miss — before the build, not after.

### What the fingerprint should measure

The current profile measures sentence and paragraph length, evidence density,
and how sections are titled. Useful, and it should keep doing that. The
additions that would matter most:

- **Rhythm, not just average length.** The variance and the sequence of
  sentence lengths. Human analytical writing swings — a long chain of reasoning
  followed by a four-word verdict. Machine writing regresses to the mean. The
  measure that matters is how often length changes sharply, not what it
  averages.
- **How paragraphs open.** Machine writing opens paragraphs the same way over
  and over: with a summary sentence stating the topic. Human writing opens with
  an event, a number, a contradiction, a question, or a flat assertion. Count
  the distribution.
- **Where the verb sits.** Distance between subject and verb, and how often
  sentences open with a real actor doing something rather than an abstraction.
- **Metaphor and idiom rate.** How often you reach for an image, and which
  images. This is one of the most personal measurements available and almost
  nobody tracks it.
- **Judgment density.** How often the writing takes a position rather than
  reports a fact. This is the clearest divide between senior and junior work.
- **The words you use that others don't.** Compare your vocabulary against a
  general business-writing baseline. What is left is your signature.

### What the critic does

The critic reads the draft as a skeptical editor would, and it runs *before*
the document is built, so it can rewrite rather than merely complain. It scores
five things:

1. **Does this sound like the fingerprint?** Rhythm, openings, vocabulary.
2. **Is every paragraph earning its place?** A paragraph that restates the
   previous one, or that could be deleted without loss, gets cut. Bloat, more
   than complexity, is what makes research writing fail its reader.
3. **Does each sentence hand off to the next?** Each sentence should start from
   what the reader just learned and end on the new thing. When that chain is
   intact, connective filler becomes unnecessary — and its presence is the
   symptom that the chain is broken.
4. **Is there a judgment here, or only facts?** Every section needs at least
   one sentence that a reasonable person could disagree with.
5. **Would a senior analyst have written this?** Concretely: are hedges
   stacked; is uncertainty quantified rather than gestured at; are numbers used
   to make a point rather than to fill space; does the close face the reader's
   decision rather than trail off in summary.

Where a passage fails, the critic rewrites it and shows both versions in the
build log so the pattern is visible rather than silently corrected.

### On sounding human

The tells worth engineering against, in order of how much they give the game
away:

- **Trailing analysis bolted onto a sentence.** A statement, then a comma, then
  a clause explaining its significance. Once you see this you cannot unsee it,
  and it appears at several times the human rate. The fix is to split it: state
  the fact, then state the meaning in its own sentence. The gate already
  detects this; the critic should also fix it.
- **Uniform paragraph size.** Four to six sentences, every time. Real writing
  has one-sentence paragraphs where the point deserves the space.
- **Everything in threes.** Three examples, three adjectives, three clauses.
  Occasionally, on purpose, is rhetoric. Constantly is a habit.
- **"Not just X, but Y."** And its relatives. Almost always deletable.
- **Stacked hedging.** "May potentially suggest." Pick one, or quantify it.
- **Summary sentences that summarize nothing new.** The paragraph-closing
  restatement is the single largest source of bloat.

And the affirmative version, which matters more: **specificity is the strongest
signal of a human expert.** A machine writes "significant growth." A person
writes the number, names the quarter, and says what it cost to get. The house
rule to delete the emphasis adjective and insert the metric is exactly right,
and the critic should enforce it as an active rewrite.

**What gets built.** An expanded `engine/style.py`; `engine/critic.py`
running before build; the fingerprint stored as data; a before-and-after log.

---

## 7. The Variety Planner: stop the reports from converging

**The problem.** Templates produce consistency, which is the point, and
sameness, which is not. Read four notes in a row from a template-driven system
and the shape becomes visible — same section count, same opening move, same
rhythm of claim and evidence. The house style already calls for varying the
moves. Nothing enforces it, and nothing remembers what the last report did.

**The idea.** Give the planner a memory of the last several reports and require
it to differ.

**How it works.** Each report records its structural choices: how it opened,
which paragraph architectures it used and in what order, where the exhibits
sat, how it closed, which analytical moves it ran. Before drafting, the planner
reads the last several records and picks a combination that has not been used
recently.

**What actually varies.** Templates fix which sections exist. They do not fix:

- **The opening move.** Open on the event. Or on a number that seems wrong. Or
  on the history that explains the present. Or on a direct disagreement with
  the common view.
- **The order of argument.** Claim then evidence, or evidence accumulating to a
  claim. The second is slower and much more persuasive; it should not be rare.
- **Where the exhibits sit.** An early exhibit sets the terms of the argument.
  A late one settles it.
- **The closing move.** A dated falsifier. A single question. A comparison to
  what we said last time.
- **The section shapes.** A section that is one long argument reads differently
  from one that is three short observations, even at identical length.

**The constraint that keeps it honest.** Variety is a tiebreaker, not an
objective. If the material demands the same structure as last time, use it —
the planner should record the repetition and its reason rather than distorting
the argument to be different. Novelty at the expense of clarity is a worse
failure than sameness.

**What gets built.** A structure record per report; recency checks in
`engine/plan.py`; a variety line in the validation log naming what was chosen
and what was avoided.

---

## 8. The Exhibit Designer: charts that prove a specific claim

**The problem.** Chart specifications are hand-written, which means charts get
chosen by habit and familiarity rather than by what the particular argument
needs. The house chart factory is good — ten defined types, a fixed palette,
a hard embargo wired into code. The gap is upstream: nothing decides *which*
chart the claim requires.

**The idea.** Charts are generated from claims, not chosen from a list. The
drafter marks a claim as needing visual proof; the designer reads the claim,
identifies its logical shape, and selects the exhibit form that demonstrates
it.

**Claim shape to chart form.** The mapping is more mechanical than it looks:

| The claim is about | Show it as |
|---|---|
| Ranking — who is bigger | Horizontal bars, sorted, values labeled |
| Change over time | A line; bars only if the periods are few and discrete |
| Two quantities at different scales | Bars plus a line on a second axis |
| Composition changing | Stacked area or a small set of paired columns |
| A range of possible values | A football-field bar per method |
| Distribution across a group | Dots on a line, each labeled |
| One number against a threshold | A single labeled marker, not a gauge |
| Two variables related | A scatter — **except where embargoed, and the embargo here is absolute and enforced in code** |

**Conventions that separate professional exhibits from ordinary ones.**

- **The title is the finding, not the subject.** Not "Revenue by year" but
  "Revenue growth halved while headcount doubled." The reader who reads only
  the exhibit titles should get the argument.
- **Label the data directly.** Legends make the eye travel. Put the label on
  the line.
- **Annotate the moment that matters.** A small note on the chart at the point
  where something changed is worth a paragraph of explanation.
- **Every exhibit is referenced from the text that depends on it**, and the
  text says what to see in it.
- **Drop everything that is not data.** Gridlines, borders, background fills,
  and three-dimensional effects all reduce clarity. This is settled and
  uncontroversial.
- **Never truncate an axis on a bar chart.** Bar length encodes magnitude; a
  cut axis is a false statement. Lines may start above zero when the variation
  is the point, and should say so.

**The check worth adding.** The build should verify that every exhibit is
mentioned in the text, that its caption states a finding rather than a label,
and that the numbers it plots resolve to the same facts the prose uses — which
falls out of idea 3 for free.

**What gets built.** `engine/exhibit.py` mapping claims to chart types; a
caption generator that writes findings; a text-reference check in the gate.

---

## 9. The Model Factory: one skeleton, four models

**The problem.** There is exactly one financial model builder in the repo, it
is 647 lines, and it only knows how to model Databricks. The request
dashboard already has a checkbox asking for a model. Nothing consumes it.

**The finding that makes this tractable.** I examined all four uploaded
templates in detail. **They are the same building with different rooms.** Every
one follows the same skeleton:

```
Cover          title, contents, and automated model checks
Inputs         every assumption, in blue, each in its own labeled cell
Raw Data       historicals with the source written beside them
Model          the statements and their supporting schedules
Scenarios      best / base / worst, selected by one switch
Valuation      the method — discounted cash flow, comparables, or both
Outputs        the dashboard a reader looks at first
```

They also share their conventions exactly: **blue text for anything typed in,
black for anything calculated, green for a link to another sheet.** Accounting
number formats where zero shows as a dash and negatives sit in parentheses.
Percentages stored as fractions. Multiples shown as `0.0x`. Years carrying a
letter so the reader can see at a glance which are actual and which are
forecast — `2023A`, `2024F`. And a scenario switch driven from a single cell,
so one keystroke moves the whole model.

Because the skeleton is shared, it should be written once.

**How it works.** A model specification declares which archetype to build and
which drivers to use. The factory assembles the shared skeleton, then fills the
middle from the archetype:

- **Subscription operating model** — a monthly build of customers and recurring
  revenue: new customers, customers lost, existing customers spending more,
  average revenue per customer. This is the right default for a private
  software company, and the uploaded template is an excellent pattern for it.
- **Three-statement model** — profit and loss, cash flow, and balance sheet
  linked, with a working-capital schedule and a debt schedule.
- **Discounted cash flow** — the cash flow forecast, a cost-of-capital build
  from comparable companies, both terminal value methods, and a sensitivity
  grid.
- **Full valuation** — the above plus comparable companies, precedent
  transactions, sum-of-the-parts, and a summary of value by method.

**Every assumption comes from the fact store, or it is visible.** This is the
rule that makes an automated model trustworthy. Each blue input cell is either
a resolved reference to a stored fact — carrying its source and date in the
cell note — or it is explicitly marked as an assumption with its reasoning
written beside it. There is no third category. A model where you cannot tell
which numbers are known and which were invented is worse than no model.

**The gate.** A model ships only when: every formula evaluates without error;
the balance sheet balances in every period and every scenario; cash flow ties
to the change in cash; no formula contains a hardcoded number where an input
cell exists; the scenario switch moves every scenario-dependent output; and
the checks block on the cover page reads clean. All six are mechanical. The
uploaded templates already demonstrate the pattern — their cover pages carry a
checks block that renders plain answers like "Balance Sheet Unbalanced? No"
and shows ERROR for anything unexpected. Copy it exactly.

**One caution.** Private companies disclose little. A model built on four real
numbers and thirty assumptions is a speculation wearing a suit. The factory
should count how many inputs are sourced facts versus assumptions and print
that ratio on the cover. Below a threshold, it builds the workbook but labels
it clearly as illustrative. Being honest about this is what separates a
research model from a sales model.

**What gets built.** `engine/model.py` with the shared skeleton and four
archetypes; `model_templates/` holding the four reference workbooks;
`engine/model_qa.py` for the six checks; a `model` command; wiring for the
existing `extras.model` request flag.

---

## 10. The Red Team and the Learning Loop

Two ideas that belong together because both are about the system improving
rather than merely running.

### The Red Team

**The problem.** The ship gate requires that the strongest counter-argument be
addressed in the report. Today a human supplies that counter-argument. An
author checking their own argument is the weakest possible test of it.

**The idea.** A separate pass, with a different instruction, whose only job is
to attack the draft. It does not write the report and it does not see itself as
responsible for the conclusion.

**What it attacks.** Four things, in order:

1. **The load-bearing number.** Which single figure, if wrong, collapses the
   argument? How confident are we in it, really? What if it is stale?
2. **The alternative explanation.** What else would produce this same evidence?
   A growth figure could mean the product is winning, or it could mean one
   large customer signed, or it could mean the definition changed.
3. **The missing disconfirmation.** What evidence would we expect to see if
   this view were right, that we have not found? Absence of expected evidence
   is the most commonly ignored signal in research.
4. **The reversal test.** If the position were the opposite, which of our facts
   would support it? A view whose evidence cannot be read the other way is
   usually a view that has not been tested.

The attack goes into the draft's own record. The writer must answer each point
in the report itself or state in the validation log why it does not apply.
Unanswered attacks block the ship.

### The Learning Loop

**The problem.** Every time you edit a draft, you make a judgment about what
good looks like. Right now that judgment is applied once and then lost. The
system writes the next report exactly as naive as it wrote the last one.

**The idea.** Capture the edits. Compare what was drafted against what shipped,
classify the differences, and turn recurring patterns into rules.

**How it works.** The drafted version is kept. After you edit, a comparison
pass categorizes every change: a fact corrected, a sentence tightened, a hedge
removed, a structure reordered, a word swapped. Individual edits are noise.
Patterns are signal — the same word replaced three times is a vocabulary rule;
paragraphs consistently cut in half is a length rule; a section reordered the
same way twice is a structure rule.

Recurring patterns get proposed as additions to the style configuration for
your approval. The fingerprint updates from what you actually ship, not from
what the system guessed.

**The measurement that matters.** Track one number over time: **how much of
the shipped report survived from the draft unchanged.** If that rises quarter
over quarter, the system is genuinely learning. If it does not, the loop is
decorative and should be redesigned.

**What gets built.** `engine/redteam.py` running pre-build; draft archiving;
`engine/learn.py` for the comparison; a proposed-rules queue; the survival rate
tracked in the style profile.

---

# The craft reference

The ideas above are machinery. This section is the judgment the machinery is
supposed to encode. It is written for a reader who is smart but not a
specialist, which is also the right register for the reports themselves.

## What senior writing looks like

The difference between a junior and a senior research note is not vocabulary
and it is not length. It is four habits.

**A senior analyst takes a position.** A junior note assembles facts and lets
the reader conclude. A senior note says what it thinks and accepts that it
might be wrong. The test: could a reasonable person disagree with any sentence
here? If not, nothing has been said.

**A senior analyst quantifies uncertainty instead of gesturing at it.** "The
company will likely raise again" is a junior sentence. "The company very likely
(80–95%) raises again before the end of next year; the cash on hand covers
roughly six quarters at the current burn" is a senior one. The house practice
of using a fixed vocabulary of likelihood terms with numeric ranges attached is
the right one, and it is rare enough in this industry to be a genuine
distinction.

**A senior analyst leaves things out.** The junior instinct is to show all the
work. Depth belongs below the waterline — in exhibits, tables, and the fact
store — not in the body text. A note that includes everything found signals
that the writer could not tell what mattered.

**A senior analyst closes facing a decision.** The last paragraph of a junior
note summarizes. The last paragraph of a senior note tells the reader what
would change the answer, and by when.

## Grammar and rhythm

The mechanical rules that do the most work:

- **Subject, verb, object — and keep the subject and verb close together.**
  Distance between them is the main cause of sentences a reader has to read
  twice.
- **Put the new information at the end of the sentence.** Readers give the most
  weight to what sits in the final position. Start from what they already know
  and land on what you are adding. Chain sentences that way and the argument
  advances by itself, which is why good analytical writing needs so few
  connecting words.
- **One fact or one judgment per sentence.** When a sentence carries two, the
  reader remembers neither.
- **Concrete actors doing things.** "The company raised" beats "a capital raise
  was completed." The passive voice is not banned — it is correct when the
  actor is unknown or irrelevant — but a page of it means nobody is doing
  anything.
- **Prefer the verb to the noun made from a verb.** "Decided" over "made a
  decision." This alone removes a surprising amount of bulk.
- **Vary length deliberately.** A long sentence carrying one chain of evidence,
  followed by a short flat one. The short sentence after the long one is where
  the judgment goes.
- **Define a specialist term the first time it appears**, spell out a multiple
  in words on first use, and never use trading-floor slang. The reader is
  intelligent and busy, not a specialist in your specialty.

## The kinds of analysis worth doing

Restating the library from idea 5 in plain terms, because the choice of
analysis matters more than the quality of the prose:

Start with **what usually happens** to companies in this situation, before
looking at this company's story. Then ask **what the current price already
assumes**, and argue with that rather than with the price. Look at **what one
customer is worth against what one customer costs** — this is where most growth
stories either hold up or fall apart. Ask **where the growth came from**,
because new customers, existing customers spending more, and price increases
look identical in the headline number and mean entirely different things. Check
**how concentrated** the business is on its largest few relationships. Ask
**how much value has been created per dollar invested**. Then state **what has
to be true for this to end well, and by when** — and finally, **the one number
that would prove you wrong.**

## Visual conventions

Covered in idea 8, condensed here to the rules that matter most: the exhibit
title states the finding rather than naming the subject; labels sit on the data
rather than in a legend; the moment that matters gets annotated on the chart
itself; every exhibit is referred to from the text that depends on it; bar
charts always start at zero; and everything that is not data gets deleted.

---

# Build order

Sequenced by dependency and by how much each unlocks.

**Phase 1 — Trust the numbers.** Evidence Locker (2), then Claim Ledger (3),
then Harvester (1). This is the foundation: every number traceable to an
archived sentence, and no two parts of a report able to disagree. Nothing else
is worth much until a reader can trust the figures.

**Phase 2 — Fill the funnel.** Signal Engine (4) and Analysis Library (5).
Together these turn a request-driven system into one that proposes its own work
and knows what analysis that work requires.

**Phase 3 — Make it sound like you.** Voice Engine (6), Variety Planner (7),
Red Team (10a). The output stops reading as machine-generated.

**Phase 4 — The workbook.** Model Factory (9). Largest single build, and it
depends on the fact store being trustworthy, which is Phase 1.

**Phase 5 — Compounding.** Exhibit Designer (8) and Learning Loop (10b). The
system starts improving without being told to.

## What to measure

Six numbers, reviewed monthly:

1. **Traceability** — share of published figures resolving to an archived
   evidence span. Target: 100%. Anything less is a defect.
2. **Contradictions** — internal number conflicts reaching the build. Target:
   zero, permanently.
3. **Draft survival** — share of the draft that ships unedited. Should rise.
4. **Time to ship** — hours from signal to finished report. Should fall.
5. **Calibration** — of the forward judgments made with stated odds, how many
   came true, against what the odds implied. This is the only real measure of
   whether the analysis is any good, and it takes quarters to accumulate.
6. **Source coverage** — share of the source manifest successfully checked.
   Falling coverage is the leading indicator of a report going wrong.

The last two are the ones that matter most and the ones most likely to be
skipped. Calibration in particular is what separates a research operation from
a content operation: it is the willingness to write down a prediction with a
number attached, and then check.

---

## The honest caveats

Three things worth saying plainly.

**More sources is not more insight.** There is reasonable evidence that
research desks adopting automation ended up with more sources and broader
coverage while their forecast accuracy got *worse*. The mechanism is
straightforward — breadth without synthesis is noise, and a machine will
happily supply infinite breadth. Every idea here should be judged on whether it
improves judgment, not volume. Ideas 5, 6, and 10 exist for exactly this
reason.

**The human touchpoint should not be automated away.** Two remain: picking what
to write in the morning, and reading it before it ships. Both are cheap. Both
are where the responsibility for being right actually sits. A system that
removes them is not more automated, it is unaccountable.

**Private companies are not public companies.** Most of the technique in
published research assumes audited quarterly filings. The companies covered
here disclose when they feel like it. That makes the evidence layer, the
freeze-on-conflict rule, and the visible-vintage requirement more important
here than they would be on a public desk — not less. The right response to
thin information is to be scrupulous about what is known, not to fill the gap
with confident prose.
