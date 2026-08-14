# Ten more recommendations

*Written 2026-08-13, after building the harvester, the intake router, the model
factory and the market layer, and running a full-universe backfill. Companion
to AUTOMATION_ROADMAP.md, which proposed the architecture; this one comes from
what actually broke while building it.*

---

## What this run taught us

Four numbers frame everything below.

**190 facts across 13 companies, up from 130.** The PitchBook backfill added
funding histories reaching back to 2018. Thin coverage fell from eight
companies to two.

**Zero of thirteen models are research-grade.** Every one is labelled
illustrative. The best, Databricks, is 37% sourced. Nine companies have no
revenue figure at all, so their models cannot project anything and their
mechanical gates correctly fail.

**One number was wrong by $2 billion for a day.** PitchBook carried $188B
while the company had announced $190B. Not an error in either source — a lag.

**Five identifiers were written to the store without being looked up.** Mine.
They happened to be right, which is worse than if they had been wrong, because
nothing would have caught them.

The roadmap's thesis was that the bottleneck is evidence and judgment rather
than writing. That was correct but incomplete. The sharper version:
**the bottleneck is revenue, provenance, and time.**

---

## 1. Solve revenue, or the models stay decorative

**The problem, stated plainly.** A financial model needs revenue. PitchBook
publishes valuations, deal terms, investors and headcount, and it publishes
revenue for almost nobody private. Nine of thirteen companies have no revenue
figure from any source. Their models are seventeen assumptions in a trench
coat.

**Why the current design cannot fix itself.** The factory correctly refuses to
invent a number, so it substitutes a placeholder and labels the workbook
illustrative. Honest, and useless. The gap does not close by trying harder at
the same sources.

**The recommendation: a revenue estimation discipline with three independent
routes, and a published spread rather than a point.**

- *Route one, disclosed fragments.* Companies leak revenue in pieces: a
  milestone in a funding announcement, a customer count times a published
  price, a segment figure in a partner's earnings call. Harvest the fragments
  and reconstruct.
- *Route two, headcount.* Revenue per employee is remarkably stable within a
  category. Databricks runs at $767k. Apply the category's observed range to a
  company's headcount, which PitchBook does publish, and you get a bounded
  estimate rather than a guess.
- *Route three, the round itself.* Investors price on a multiple. Given a
  post-money valuation and the multiple range comparable companies commanded
  in the same quarter, you can back out an implied revenue band.

Where the three agree, confidence is high. Where they disagree, the
disagreement is the finding. Every estimate carries the `est.` flag, its
method, and its range — and the model uses the midpoint while the cover states
the spread. This turns nine dead models into nine live ones with honest error
bars, which is the difference between no answer and a range.

---

## 2. No identifier enters the store without the lookup that produced it

**The problem.** I wrote five PitchBook IDs into `universe.json` having looked
up only five of ten. All five happened to be correct. That is the dangerous
outcome: nothing in the system would have detected it, and a wrong ID would
have silently pulled another company's funding history into a profile.

**The recommendation.** Treat an identifier as a Fact, not a string. Every
`pb_entity_id`, CIK, ticker or domain carries the same envelope as any other
value: the source that resolved it, the date, and the tier. A resolution
record looks like the lookup that produced it — the query used, the candidates
returned, and which was chosen.

Then add the check that would have caught me: **cross-field consistency at
write time.** A PitchBook profile returns a company name, website and
headquarters. If the resolved name does not fuzzy-match the universe entry, or
the website does not match the stored domain, the write fails. Anything the
system can verify about itself, it should.

This generalises. The store already refuses a Fact with no source. It should
equally refuse an identifier with no resolution record.

---

## 3. Model source lag explicitly, and stop treating recency as a scalar

**The problem.** PitchBook said $188B, "Announced/In Progress." The company
said $190B, closed. Both were accurate on their own terms. The merge rule
resolved it correctly, but only because a human noticed and reasoned about it.

**What is actually going on.** Sources have characteristic latencies. A company
announcement is instant and self-interested. Wire coverage follows within
hours. A structured data vendor takes days to weeks and adds verification. SEC
filings are slow, sparse and authoritative.

The current merge rule compares two dates and two tiers. It has no concept of
*expected* lag, so it cannot tell the difference between "PitchBook has not
caught up yet" and "PitchBook checked and disagrees."

**The recommendation.** Give every source a latency profile — typical days
behind an event, and whether it corrects itself. Then:

- When a faster source leads a slower one within the slower one's normal lag,
  adopt the fast value and mark the slow field *pending confirmation* rather
  than *disputed*. That is what happened here.
- When the slower source has had time to catch up and still disagrees, that is
  a real conflict and gets frozen.

The practical payoff is a dated to-do list: every pending-confirmation field
carries the date by which the slower source should have caught up, and the
daily run checks it. A vendor that fails to confirm is itself information.

---

## 4. Make persist-and-extract the standard tool pattern

**The problem.** PitchBook deal responses run 50 to 85 kilobytes. Pulling
thirteen companies through the conversation would have consumed the entire
context window and produced nothing durable.

**What worked.** Large responses spill to disk automatically. Calling the tool,
letting it spill, and parsing the file with a purpose-built extractor
(`engine/pb_extract.py`) kept context flat while capturing everything. The
whole backfill cost a few hundred tokens of conversation.

**The recommendation.** Promote this from an improvisation to the house
pattern, with three parts:

- **An extractor per source shape**, versioned alongside the source. Vendors
  change field labels; the extractor is where that change gets absorbed. This
  bit already: the first version looked for "Post Valuation" where PitchBook
  writes "Post-Money Valuation", and silently produced empty ladders. A parser
  that finds nothing should fail loudly, not return an empty result.
- **A raw response archive** keyed to the evidence locker, so a re-parse never
  needs a re-fetch. Vendor calls are metered; disk is not.
- **A parser test corpus** — one saved response per source shape, with expected
  output. Run it in the daily job. When a vendor changes its format, you learn
  from a failing test rather than from a quietly emptier store.

---

## 5. Verify by re-implementation, not by re-reading

**The problem.** LibreOffice cannot evaluate spreadsheets in this container —
it times out and then fails to load any workbook, including the analyst's own
templates. The model could not be recalculated, and an uncomputed model is an
unverified one.

**What worked.** `engine/model_check.py` recomputes the entire chain in Python
from the workbook's own inputs. It is a second implementation, not a re-read of
the first, so a disagreement between the formulas and the checker is itself the
finding. It caught two real flaws immediately: terminal value at 93% of
enterprise value, and two terminal methods disagreeing by six times.

**The recommendation.** Apply the pattern wherever an artifact carries
computation. A chart should be checkable against the numbers it claims to plot.
A report's arithmetic should be recomputed from the store rather than re-read
from the prose. The general rule: **anything the system computes for a reader,
it should be able to compute a second way and compare.**

And separate severity properly, which was the second half of that fix.
Mechanical faults block. Analytical cautions inform. A discounted cash flow
that cannot reach the market price is not a bug to be tuned away — it is the
analysis, and the system should say so in those words.

---

## 6. Publish the gap between the model and the price as a first-class output

**The observation.** The Databricks model values the business at roughly $45B
against a $190B mark. That ratio — 0.24x — is the single most interesting
number the system produced all day, and it currently lives only in a
verification log.

**Why it matters.** A DCF on defensible assumptions almost never reaches a
private AI valuation. That is not a failure of the model. It is a measurement
of how much of the price is growth expectation rather than discounted cash
flow. Tracked across a universe and over time, it becomes the desk's own
sentiment index — and unlike a survey, it is computed from stated assumptions
anyone can inspect.

**The recommendation.** Compute it for every company every time the store
moves, store it as a dated ladder, and show it on the dashboard. Then add the
inverse, which is the more useful question: **what would have to be true for
the model to reach the price?** Solve for the growth rate, the terminal margin
and the exit multiple that close the gap, and print those. "This price implies
55% compound growth for seven years and a 35% terminal margin" is a sentence a
reader can argue with. "$190 billion" is not.

**The embargo still binds.** This is a model-to-price comparison and involves
no quality score. It must never be joined to AIBQ.

---

## 7. Track staleness on narrative, not just on numbers

**The problem.** Decay classes govern facts. The briefings — the plain-English
explanations of what each business does — carry only an `updated` date and no
decay at all. They will drift silently, which is worse than a stale number
because prose does not look old.

**The recommendation.** Give narrative its own decay, driven by events rather
than the calendar. A briefing goes stale when the facts underneath it move: a
new funding round, a leadership change, a product line, a competitive shift.
The daily run compares each briefing's date against the facts it depends on and
flags any that now describe a company that has changed.

Then close the loop: the flag names *which* fact moved, so refreshing a
briefing is a five-minute edit rather than a rewrite. And record which facts a
briefing depends on when it is written, so the check is exact rather than
heuristic.

---

## 8. Give the news feed a memory longer than a month

**The problem.** Google News RSS returns roughly the last month. That is
excellent for "what happened today" and useless for "what happened this year."
The genuine year-long backfill came from PitchBook's deal history, not from
news, and deal history only covers financing events.

**The recommendation.** Add archival routes for the long look-back:

- **Company blogs and newsrooms have archives and paginated feeds.** The
  harvester currently reads page one. Walking the archive once per company
  yields years of dated, primary-source posts — product launches, customer
  announcements, the occasional revenue milestone. This is the highest-value
  unexploited source available.
- **The Wayback Machine** has a public API and holds dated snapshots of pricing
  pages, careers pages and homepages going back years. A pricing page from
  eighteen months ago, compared with today's, is a real finding about
  competitive pressure that no news article will report.
- **Regulatory archives** — full-text search over filings, not just the
  submissions index.

Depth matters more than breadth here. One archived pricing page is worth fifty
commentary articles.

---

## 9. Score the sources, and let the scores change behaviour

**The problem.** Tiering is assigned per fact by judgment. There is no record of
whether a source has historically been *right*. The Google News relevance
filter is the only automated source-quality signal in the system, and it only
measures topicality.

**The recommendation.** Keep a scorecard per source, accumulated automatically
from things the system already observes:

- **Confirmation rate.** When this source reported something, did a stronger
  source later confirm it? Contradict it?
- **Lead time.** How many days ahead of, or behind, the eventual confirmed
  value?
- **Precision.** Does it publish ranges and rumours, or settled figures?
- **Independence.** How often does it merely restate another source? The system
  can detect this from near-duplicate headlines it already collects.

Then let the scorecard do work. A source with a poor confirmation record gets
its default tier lowered. A source that reliably leads gets flagged as an early
indicator rather than dismissed as unconfirmed. Over a year this replaces a
static tier table with a measured one, and it is the only mechanism proposed
here that makes the system's judgment improve on its own.

---

## 10. Close the loop: record what the desk expected, then check

**The problem.** Every mechanism in this system runs one way. Facts arrive,
analysis is produced, reports ship. Nothing ever comes back to say whether the
analysis was right. The armed triggers are the closest thing, and they only
test whether an event occurred, not whether a judgment was sound.

**The recommendation.** Two ledgers, both cheap, both compounding.

**The prediction ledger.** Every parenthetical probability in every report —
the ICD 203 lexicon already requires them — gets logged with its resolution
date and criterion. When the date arrives, the daily run asks whether it
happened. After a year you can plot stated confidence against realised
frequency. If things called "very likely (80–95%)" happen 60% of the time, the
desk is overconfident by a measurable amount, and every future report can be
adjusted by a known correction.

**The assumption ledger.** Every model assumption — the 15-point growth decay,
the 8x exit multiple, the 4% capex — is currently a defensible guess with a
note. Log them, and when a company later discloses the real figure, record the
error. Assumptions that prove reliably wrong get replaced by the observed
distribution rather than by another guess.

This is the recommendation with the longest payback and the highest ceiling.
Everything else on this list makes the system faster or more careful. This is
the only one that makes it *better at being right*, and it costs almost nothing
beyond the discipline of writing predictions down before you know the answer.

---

## Where to start

If only three get built:

**Revenue estimation (1)** unblocks nine dead models and is the difference
between a model factory and a model-shaped-object factory.

**Identifier provenance (2)** closes the hole that let five unverified IDs into
the store, and it is a day's work.

**The prediction ledger (10)** costs nothing now and is worth more every
quarter it runs. It is also the only one that cannot be started retroactively —
you can backfill facts, but you cannot backfill a prediction you never wrote
down.
