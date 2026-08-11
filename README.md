# How to write the report

These are the exact instructions for producing a high-level company report in
this repository. They are the same every time, for any company, at any time.
Follow them in order; do not skip, reorder, or improvise around them. The
automation (`CLAUDE.md` + `engine/`) executes these same instructions; this
file is the standard both humans and the agent are held to.

## 0. Intake: fix the question before anything else

Every report answers ONE question. Write it down first, from the request
(dashboard prompt or `Report Automation/requests/queue/`). Then fix three
settings:

1. **Template** from `report_template/`: initiation_note (full deep dive),
   company_update, rush_note, earnings_note, one_pager, or sector_overview.
   The template's `sections[].required` entries are binding obligations.
2. **Company or companies**, by slug from `companies/universe.json`. A company
   not yet tracked is never a blocker: `python3 -m engine add <slug> "<Name>"`
   scaffolds it, then research seeds it. Any company, any time.
3. **Rigor 1-5.** A shipped report is 4; anything public or money-moving is 5.

## 1. Research: gather before writing, in this order

1. **Analyst-provided material first**: everything in `uploads/` (documents +
   `links.md`) and in the company's own folders (`companies/<slug>/financials/`,
   `valuation-and-deals/`, `products/`, `people/`, `customers/`,
   `competition/`, `filings/`, `news-and-events/`, `notes/`). This material
   outranks nothing automatically; it is tiered like everything else.
2. **T1**: SEC EDGAR filings (submissions API by CIK); audited statements.
3. **T2**: PitchBook Premium (profile, deals, financials, investors, news)
   and dated company announcements.
4. **T3**: reputable press. Multiple outlets tracing to one ultimate source
   count as ONE source.

Rules that never bend: every figure is captured as value + as-of date +
source + tier; load-bearing figures need two independent sources where
possible; PitchBook "TTM" revenue fields are forward-window projections,
never run-rate; unclosed or rumored financings never anchor a base case.

Write the findings as a snapshot (`reports/<id>/research/snapshot.json`),
store it (`python3 -m engine snapshot <slug> <file>`), and read the tracker
digest (`python3 -m engine digest <slug>`). The digest's changes, fired
triggers, and staleness flags are the report's raw signal.

## 2. Structure: the shape of the high-level report

**Default shape: the Vertical Analyst Note** (the provided master template,
`report_template/Vertical_Analyst_Note_10.docx`). Page 1 is the production
metadata sheet with every field filled: data filepath, chart as-of date,
chart geography, research type, access level, chart and table counts,
credits, published date, contents, the landing page block (chart title,
caption of 30 words or fewer, header, body), and two report picks. Then: Key
takeaways (bulleted; every bullet carries its load-bearing figure and date),
two to four analytical sections with charts, and numbered References where
outlets and URLs live. Chart captions never exceed 30 words.

**Deep-dive shape** (initiation notes and long-form house reports):

Cover: kicker, company name, subtitle (metaphor + colon + literal claim),
one-paragraph dek, three hero tiles (quality metric, valuation with date,
verdict), snapshot table where every row carries source and date, byline.

Body, in template order. For the full deep dive that means: the scoring
breakdown; executive summary; what the company is; products layer by layer;
how the money is made; customers; competition; strategy read through actions;
financials (with the tracker's ladders and derived metrics); valuation
(completed marks only in the ladder; rumored rounds analyzed, never adopted);
the stress test; the verdict; the fact-sheet appendix generated from the
store. Shorter templates keep the same discipline over fewer sections.

Every section obeys the three-beat: WHAT HAPPENED (fact, sourced, dated,
tiered), WHAT IT MEANS (the mechanism), IMPLICATION (what to do, watch, or
reprice). A finding without an implication is unfinished work.

## 3. Writing rules (voice and format)

The binding pre-flight checklist is `style/Institutional_Research_Style_Guide.pdf`,
prescribed in full in `style/STYLE.md`: (1) punchline first: every opening
sentence IS the takeaway with its metric, never a rhetorical hook; (2) delete
emphasis adjectives, insert the metric; (3) vary cadence: long evidence chains
broken by short declaratives; (4) every metric ties to valuation multiples,
exit timelines, capital efficiency, or risk underwriting; (5) no
throat-clearing ("It is important to note", "Furthermore", "Delve", "Robust",
"Paradigm shift" banned).

The voice is the Hemingway-analyst register (STYLE.md, binding): short
declarative core, one fact or judgment per sentence, concrete subjects doing
things, and the flow rule: each sentence opens from what the reader just
learned and closes on the new thing, so the chain of sentences IS the
analysis. Depth lives below the waterline, in the exhibits and the store.
Forward-looking judgments follow the estimative discipline: lexicon bands
with parenthetical odds ("a close by October 31 is very likely (80-95%)"),
confidence stated in its own sentence with the reason, "possible" never
modified, one odds-bearing word per sentence. Full research basis:
`style/WRITING_STYLES_RESEARCH.md`.

- Lead with the sharpest signal. First paragraph of the report, and of every
  section, carries the finding. No preamble, no methodology throat-clearing.
- Sentences average low-20s words with variance: short for verdicts, long
  clause-stacked chains for evidence. Paragraphs are dense, single-topic,
  roughly four sentences. Follow the measured profile in
  `style/STYLE_PROFILE.md`; the prescriptive rules in `style/STYLE.md` win on
  conflict.
- Section titles: metaphor + colon + literal claim; ONE metaphor family per
  report.
- Figures: `$14.2B` in tables and tiles; `27.1x` not "27.1 times"; `+47% YoY`
  with sign and period; `~` and `(est.)` on every estimate at the point of
  use.
- Citations are endnotes: write [n] markers in the text; the builder renders
  superscripts tied to the numbered References section, where outlets, URLs,
  and dates live. No parenthetical citations in prose. Dates stay inline
  only where they carry analytical weight. Derived arithmetic needs no
  marker; the validation log holds the derivations.
- Disputed values ship as both figures with both dates, or not at all.
- Em-dashes sparingly: at most 2 per block and 8 per document (the build
  fails past the budget). Full banned-language list in style/STYLE.md.

## 4. Charts

House factory only (`python3 -m engine charts <charts.json>`): navy / slate /
green palette, 300 DPI, title as a claim plus a sourced subtitle, dated
caption under every figure. Estimates and announced-but-unsettled values are
hatched. The quality-valuation coefficient is embargoed: no scatter, no
fitted line against scores; the per-point ranked bar is the only cleared
expression (the factory refuses anything else).

## 5. Build, QA, and the gate

`python3 -m engine build reports/<id>` produces the docx + pdf with a
measured Contents page. QA runs automatically and a FAIL deletes the build:
em-dashes, embargoed expressions, placeholders. Fix and rebuild; never
hand-edit the output files.

Before shipping, write `reports/<id>/validation_log.md`: one ledger line per
load-bearing claim (value, sources, tier, cross-check, confidence), frozen
conflicts, the embargo check, any QA warnings with their override rationale,
every parenthetical probability logged with its date and resolution criterion
(for quarterly calibration scoring), and the Report Ship gate checklist,
every box asserted true:

- The call passes ENTER: Expectational, Novel (the market does not already
  have it), Thorough, Examinable (a colleague could replicate the conclusion
  from the note), Revealing (says where it could be wrong)

- Validation ledger complete
- Adversarial pass done (the strongest counter-argument addressed in the
  report itself)
- No VERIFY/DISPUTED figure ships unflagged; stale facts carry visible
  vintage
- Copyright-safe; zero TODOs; lead-with-signal; forward hook present
- Verdict takes a position and names the falsifier: the single published
  number that would change the answer

Any false box = not done. Then commit the report directory and the updated
`companies/` store, push, and archive the request file.

## Where everything lives

```
README.md            this standard (the editorial contract)
CLAUDE.md            the agent runbook that executes it (must stay at root)
Report Automation/   dashboard, request queue, scripts, architecture docs
companies/           one folder per company: category drop zones for your
                     documents + PROFILE.md (readable record) + store/ (machine
                     data: snapshots, conflicts, trends)
previous_reports/    drop past reports here; the style profiler learns from them
report_template/     the template contracts (drop new template material here)
uploads/             general drop zone: documents/ + links.md for URLs
reports/             one folder per generated report, outputs in output/
engine/, style/      the deterministic machinery and the measured voice
```
