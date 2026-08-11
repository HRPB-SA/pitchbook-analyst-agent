# Report Automation

The machinery behind the report factory. You normally only touch the
dashboard and the request queue; the rest runs itself.

- `dashboard/index.html` the request dashboard (published as a claude.ai
  artifact). Type the idea, pick template + companies, copy the launch
  prompt into a Claude Code session on this repo, or download the request
  file into `requests/queue/`.
- `requests/` the queue: `queue/` (pending, picked up by any session asked to
  process the queue and by the weekly Monday run), `archive/` (done),
  `SCHEMA.md` (request format).
- `scripts/setup.sh` run once in a fresh container before building (installs
  the docx/pdf toolchain). `scripts/seed_store.py` is the one-time store seed
  from the July 2026 canonical pack.
- `docs/ARCHITECTURE.md` how the pieces fit.

The agent's operating runbook is `CLAUDE.md` at the repository root. It has
to stay there under that exact name: Claude Code auto-loads it from the root
on every session, which is what makes a fresh session immediately know the
whole pipeline. Treat root `CLAUDE.md` + root `README.md` (the writing
standard) as part of this automation even though they cannot live inside
this folder.

A scheduled Routine ("Weekly tracker refresh + report queue") fires every
Monday 10:30 UTC: processes the queue, re-pulls every tracked company,
updates trends and triggers, and files a company update when something
material moved. Manage it from the claude.ai Routines UI.
