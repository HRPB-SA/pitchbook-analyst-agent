# Report requests

The dashboard (dashboard/index.html, published as an artifact) composes a
request and a launch prompt. Two ways a request reaches the agent:

1. **Paste** (interactive): the dashboard's "Copy launch prompt" button puts a
   complete instruction on the clipboard; paste it into a Claude Code session
   on this repo. The prompt embeds the request JSON; the agent runs the
   pipeline in CLAUDE.md end to end.
2. **Queue** (hands-off): drop the request JSON into `requests/queue/` (the
   dashboard's "Download request file" gives the file; commit it, or add it in
   the session). The weekly tracker Routine, and any session asked to
   "process the queue", picks up every queued file, runs the pipeline, and
   moves it to `requests/archive/`.

## Request JSON

```json
{
  "id": "slug-or-topic-template-YYYY-MM-DD",
  "submitted": "YYYY-MM-DD",
  "idea": "Free-text report idea: the question, the angle, what must be answered.",
  "template": "company_update | initiation_note | rush_note | earnings_note | one_pager | sector_overview | custom",
  "companies": ["slug", "..."],
  "sections": ["only for custom: ordered section briefs"],
  "rigor": 4,
  "deadline": null,
  "extras": {"charts": 3, "model": false, "notes": ""},
  "source": "dashboard | tracker | manual"
}
```

`companies` slugs come from data/universe.json; a company not yet tracked is
legitimate (the agent resolves it via pitchbook_search, adds it to the
universe, and seeds its profile on first research pass). `rigor` follows the
house 1-5 dial and scales validation depth. `extras.model = true` requests a
companion operating model workbook (engine support: build/model_xlsx.py
pattern from the July initiation; port per report).
