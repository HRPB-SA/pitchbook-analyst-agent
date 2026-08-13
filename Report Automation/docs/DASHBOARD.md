# The desk dashboard

`python3 -m engine dashboard` renders the whole coverage universe into one
self-contained HTML file at `Report Automation/dashboard/desk.html`. Publish it
as an artifact and it is reachable from any device.

Live copy: https://claude.ai/code/artifact/dc39b74b-a2fc-41f2-8640-440492921c43

## What it shows

**Overview** — every company with fact count, category coverage, stale and
flagged counts, frozen conflicts, trigger states and evidence volume; plus a
live feed of what the harvester actually saw move on its last sweep.

**Company** — key figures as tiles, numeric ladders as sparklines, a dated
timeline of events, marks, prints and trigger fires, every stored fact grouped
by category and filterable, the sources behind those facts, the evidence
locker, harvest status per source, and the reports covering the company.

**Search** — one box across every fact, source and note in the universe, with
facets for tier, category and staleness. Ctrl/Cmd-K focuses it.

**Request a report** — company, format, sections, analytical moves, rigor,
audience, angle, length, chart style, chart count, deadline and extras. Emits
the request JSON and a launch prompt.

**Add a company** — emits the registration commands and a setup prompt that
registers the company, probes its sources, runs the first sweep and does a
first research pass.

## Two kinds of date, and why both

Facts carry **`as_of`**: the vintage of the information. Evidence carries
**`retrieved_at`**: the UTC moment we read it. A figure dated February can be
read today; the dashboard shows both, because "how old is this fact" and "when
did we last check" are different questions.

## The daily loop

A Routine fires at 11:12 UTC daily: sweep every source, triage what changed,
verify and store material moves, fix dead sources, rebuild and republish this
page, queue a report request if a trigger fired, then commit.

The scheduled session runs **without MCP connectors**, so PitchBook is not
available to it. It substitutes SEC EDGAR and web search and flags the
substitution; anything needing PitchBook is left flagged VERIFY for an
interactive session. To give the Routine PitchBook access, recreate it from the
claude.ai Routines interface, where connectors can be attached.

## Commands

    python3 -m engine dashboard              rebuild the page
    python3 -m engine sources <slug> <domain> [cik]
                                             probe and write a source manifest
    python3 -m engine harvest <slug>         sweep one company
    python3 -m engine harvest --all          sweep the universe
    python3 -m engine harvest                per-company sweep status

The page is a view, never a source. Edit the store, then regenerate.
