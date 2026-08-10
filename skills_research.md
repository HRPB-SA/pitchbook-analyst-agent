# Skills Research: The Best Agent Skills to Incorporate (August 2026)

Prepared 2026-08-10 on branch `claude/skills-research-jviof7`. A deep web sweep for
Agent Skills worth adding to the existing analyst OS (the harrison-* suite, the
official document skills, and the PitchBook / Morningstar / Bigdata.com / Notion /
Gmail / Microsoft 365 connectors).

Method: four parallel research streams (official Anthropic ecosystem; community
directories and marketplaces; power-user workflow collections; finance and analyst
domain), totaling roughly 45 web searches, 40 GitHub API lookups, and 70
primary-source fetches. Star counts and dates were captured live on 2026-08-10,
via the GitHub API wherever possible; anything that could not be confirmed at the
source is marked UNVERIFIED. Every recommendation is net-new relative to the
current stack unless noted.

---

## The headline find

**Anthropic now ships your job as a free, official skill marketplace.**
[anthropics/financial-services](https://github.com/anthropics/financial-services)
(34.2k stars, Apache-2.0, launched 2026-05-05 with the "Agents for financial
services" announcement, last commit 2026-08-04) contains seven vertical skill
bundles and ten agent plugins. Four verticals map directly onto this workflow:

- `financial-analysis`: 3-statement-model, dcf-model, lbo-model, comps-analysis,
  competitive-analysis, audit-xls, clean-data-xls, deck-refresh, ib-check-deck,
  xlsx-author, pptx-author
- `equity-research`: earnings-analysis, earnings-preview, initiating-coverage,
  model-update, morning-note, catalyst-calendar, thesis-tracker, idea-generation,
  sector-overview
- `private-equity`: ic-memo, dd-checklist, deal-screening, deal-sourcing,
  unit-economics, returns-analysis, portfolio-monitoring, value-creation-plan
- `investment-banking`: merger-model, cim-builder, teaser, buyer-list,
  strip-profile, datapack-builder, deal-tracker

The marketplace's connector layer is built around eleven financial data MCPs,
and two of the first-class ones are PitchBook and Morningstar, which are already
connected here. The skills are structured prompts plus templates (no bundled
data), which cuts in your favor: the data plane is already paid for.

Fit with the existing stack: harrison-core-craft and harrison-validation supply
method and rigor; these supply battle-tested deliverable TEMPLATES (IC memo,
initiation, morning note, thesis tracker, LBO, CIM). Complementary, not
duplicative. Trial `/ic-memo`, `/initiate`, `/earnings`, and `/comps` against the
house formats and keep whichever structure wins section by section.

Install:

    claude plugin marketplace add anthropics/financial-services
    claude plugin install financial-analysis@claude-for-financial-services
    claude plugin install equity-research@claude-for-financial-services
    claude plugin install private-equity@claude-for-financial-services

---

## Gap analysis

| Capability area | Current coverage | Gap | Best fill |
|---|---|---|---|
| Analyst method, validation, finance knowledge | harrison-* suite (deep) | None | Keep as-is |
| Finance deliverable templates | Built per-report | Ready-made IC memo / initiation / LBO / morning-note templates | financial-services verticals |
| Cross-session memory | harrison-project-context (manual rotation) | Automatic capture and recall across sessions | claude-mem (vetted), episodic-memory |
| Pre-work plan interrogation | Validation is post-work, on external claims | Adversarial grilling of plans BEFORE execution | mattpocock grill-me |
| Prose voice control | content-qa checks correctness; em-dash ban exists | Systematic AI-tell stripping | humanizer |
| Web deliverable verification | web-studio gates are asserted, not executed | A browser actually driving the shipped app | webapp-testing (official) |
| Free macro / market data | Paid MCPs are fundamentals-centric | FRED, VIX / options, screeners, transcripts, institutional holdings | gauss314/skills |
| Local SQL over datasets | xlsx + Python builds | SQL engine over CSV / parquet before Excel | duckdb-skills (official) |
| Market regime and timing | Fundamentals-centric stack | Breadth / regime detection, systematic screens, backtests | tradermonty/claude-trading-skills |
| Filings and earnings workflows | Bigdata.com / PitchBook transcript search (data) | Period-over-period filing deltas, guidance extraction (workflow) | OctagonAI/skills, edgar-change-interpreter |
| Long-horizon task state | harrison-execution waves (in-session) | Plan / task persistence across sessions and crashes | planning-with-files or beads |
| Engineering discipline | code-review, security-review | Systematic debugging, verification-before-completion, TDD gates | superpowers (selective) |
| Harness maintenance | update-config (manual) | Hooks from plain English, setup audit, CLAUDE.md hygiene | hookify, claude-code-setup, claude-md-management |
| Skill authoring at scale | skill-creator (hand-written) | Mint skills from vendor docs / PDFs automatically | Skill_Seekers |
| Skill supply-chain security | None | Scanning third-party skills before install | SkillSpector |

---

## Tier 0: prerequisite before installing anything community-built

**SkillSpector** ([NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector),
14.5k stars): scans third-party skills for prompt injection, data exfiltration,
and malicious patterns before install. This is not optional hygiene. A 2026 Snyk
audit flagged 13.4 percent of one large community registry's (ClawHub) skills as
critical, and a Koi Security scan found 341 of 2,857 scanned skills actively
exfiltrating data. Sourcing rules going forward:

1. Prefer the three official Anthropic marketplaces, verified partner repos, and
   [trailofbits/skills-curated](https://github.com/trailofbits/skills-curated)
   (security-reviewed community marketplace).
2. Scan everything else with SkillSpector, and read the SKILL.md plus any bundled
   scripts before enabling.
3. Treat hooks-based skills (memory layers especially) as privileged software:
   they see every session, which matters under the MNPI / COI rules in
   harrison-validation.
4. Note that several top community packs (superpowers, mattpocock-skills,
   bigdata-com) are mirrored in `claude-plugins-official`, which is the safer
   install path than random forks.

---

## Tier 1: install now

Ranked. Items 1 and 2 are official Anthropic; the rest are community with
traction verified 2026-08-10.

**1. Claude for Financial Services verticals** (see headline above). Official,
free, wired to connectors already paid for. The single highest-leverage add.

**2. Document-skills refresh plus two official skills you lack.** The upstream
docx / pptx / xlsx skills were updated 2026-07-16 (pdf on 2026-02-06); if local
copies predate July 2026, re-pull `document-skills@anthropic-agent-skills`. Then
add from the same repo: **webapp-testing** (Playwright toolkit that drives local
web apps, captures screenshots, reads console logs: the missing executable gate
for web-studio deliverables) and **frontend-design** (762K installs on skills.sh;
anti-generic aesthetic direction that complements the web-studio anti-slop
gates). [anthropics/skills](https://github.com/anthropics/skills), 167.5k stars.

**3. grill-me + handoff + research** from
[mattpocock/skills](https://github.com/mattpocock/skills) (212.5k stars, by Matt
Pocock of Total TypeScript; also on the official plugin directory). grill-me
runs a relentless adversarial interview on any plan before execution (about 800K
installs on skills.sh); it is the validation spine's ethos applied BEFORE work
instead of after. handoff compresses a session into a continuation document,
which generalizes to multi-day report builds. Install:
`npx skills add mattpocock/skills` (pick skills a la carte).

**4. humanizer** ([blader/humanizer](https://github.com/blader/humanizer), 34.7k
stars, by Siqi Chen). Strips AI writing tells: em-dash abuse, "delve", hedging
boilerplate, symmetric listicles. The repo's own zero-em-dash constraint is
already a hand-rolled humanizer rule; this systematizes the rest. Runs as a
final pass next to content-qa (content-qa owns correctness, humanizer owns
voice).

**5. claude-mem** ([thedotmack/claude-mem](https://github.com/thedotmack/claude-mem),
90.3k stars): the dominant persistent-memory layer. Hooks capture sessions, AI
compresses them, relevant context is re-injected later, with progressive
disclosure and private tags. Converts a stateless assistant into an actual
analyst OS that remembers projects, figures, and decisions, and automates what
harrison-project-context does by manual rotation today. CAVEAT: it is a
hooks-plus-database layer that sees everything; scan it, configure exclusions
for sensitive engagements, and keep harrison-project-context as the canonical
figures file (memory recalls; the context file remains the source of truth).
Local-first alternative if the hosted-ish footprint is unacceptable:
[obra/episodic-memory](https://github.com/obra/episodic-memory) (SQLite vector
index over transcripts, 462 stars).

**6. gauss314/skills** ([gauss314/skills](https://github.com/gauss314/skills),
181 stars, active 2026): 21 mostly keyless market-data skills: FRED (840k macro
series), SEC filings, Yahoo Finance, Finviz, Macrotrends, EarningsWhispers
transcripts, CBOE / VIX, Nasdaq institutional holdings. Fills the free
macro-and-options data layer the paid MCPs do not cover. Low stars but simple,
inspectable fetch skills; scan then adopt. Install: `npx skills add gauss314/skills`.

**7. duckdb-skills** ([duckdb/duckdb-skills](https://github.com/duckdb/duckdb-skills),
official DuckDB, 527 stars, announced March 2026): local SQL over CSV / parquet /
anything DuckDB reads. The right tool for comps tables, screens, and cohort math
before results go to Excel. Install:
`/plugin marketplace add duckdb/duckdb-skills` then
`/plugin install duckdb-skills@duckdb-skills`.

---

## Tier 2: high value, adopt when the workflow calls

- **karpathy-skills**
  ([multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills),
  201.2k stars): four behavioral rules (verify before claiming, minimal changes,
  no sycophancy, admit uncertainty) in one file at near-zero token cost. Largely
  redundant with harrison-kernel's calibration doctrine, but cheap enough to
  trial as a belt-and-suspenders guardrail.
- **Anthropic harness-maintenance trio** from
  [claude-plugins-official](https://github.com/anthropics/claude-plugins-official)
  (33.4k stars, 285 plugins): **hookify** (author hooks from plain-English
  rules; e.g. turn the em-dash ban into an enforced hook), **claude-code-setup**
  (audits a repo and recommends hooks / skills / automation), and
  **claude-md-management** (CLAUDE.md hygiene plus session-learning capture).
- **bigdata-com plugin** (official RavenPack entry in claude-plugins-official):
  the skills layer over the Bigdata.com MCP already connected; near-zero
  adoption cost, tightens search discipline and tearsheet workflows.
- **tradermonty/claude-trading-skills**
  ([repo](https://github.com/tradermonty/claude-trading-skills), 2.6k stars, the
  highest-traction finance-native pack): market breadth / regime detection,
  CANSLIM / VCP / value screeners, earnings-trade analysis, economic calendar,
  backtest expert, trade journaling. Adds a markets-and-timing dimension to a
  fundamentals-centric stack; tiered no-API starter path.
- **OctagonAI/skills** ([repo](https://github.com/OctagonAI/skills), 132 stars,
  vendor-maintained): 60+ research skills, strongest on earnings calls (13
  skills: guidance extraction, management sentiment) and SEC filings (15 skills:
  risk factors, MD&A, covenants). Workflow depth on top of the raw transcript
  access PitchBook and Bigdata.com already provide. Needs a free Octagon API key.
- **planning-with-files**
  ([OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files),
  26.1k stars): Manus-style persistent markdown plans (task_plan.md,
  findings.md, progress.md) that survive /clear, compaction, and crashes, with a
  deterministic completion gate. Direct upgrade for multi-wave report and model
  builds. Heavier alternative for many parallel workstreams:
  [steveyegge/beads](https://github.com/steveyegge/beads) (26.2k stars,
  git-backed dependency-graph issue tracker as agent memory). Start with
  planning-with-files; graduate to beads if workstream count demands it.
- **superpowers, selectively** ([obra/superpowers](https://github.com/obra/superpowers),
  270.2k stars, the most-starred skill framework): the full
  brainstorm-plan-execute loop overlaps harrison-execution, so skip wholesale
  adoption; but three sub-skills are best-in-class and worth extracting:
  **systematic-debugging** (4-phase root-cause process), 
  **verification-before-completion** (evidence-before-done gate, a code-side
  twin of the HARD VERIFICATION GATE doctrine), and **brainstorming** (Socratic
  design refinement with adversarial subagent review). Community consensus is
  genuinely split on the whole framework ("so much more productive" vs "not
  effective for me; don't believe it's a silver bullet"), which supports the
  cherry-pick approach.
- **Skill_Seekers**
  ([yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers),
  14.7k stars): converts documentation sites, repos, and PDFs into skills with
  conflict detection. Use it to mint house skills from vendor API docs
  (PitchBook, Morningstar endpoints) or reference material instead of
  hand-writing them.
- **doc-coauthoring** (official, in anthropics/skills): three-stage document
  workflow whose "reader testing" stage hands the draft to a context-free Claude
  to find blind spots. A genuinely novel QA gate for high-stakes memos; light
  overlap with the writing craft mode.
- **Deep-research pipelines**: current Claude Code builds reportedly bundle a
  `/deep-research` command (multi-agent, cited; check `/help`; not present in
  every environment). If absent, the best community options are
  [199-biotechnologies/claude-deep-research-skill](https://github.com/199-biotechnologies/claude-deep-research-skill)
  (975 stars; 8-phase pipeline with source-credibility scoring, which rhymes
  with the validation spine's tiering) and, for equity work specifically,
  [liangdabiao/Claude-Code-Stock-Deep-Research-Agent](https://github.com/liangdabiao/Claude-Code-Stock-Deep-Research-Agent)
  (361 stars; 8-stage DD framework fanning out 28 subagents with bull / bear
  balance).
- **vercel-labs/agent-skills** ([repo](https://github.com/vercel-labs/agent-skills),
  29.9k stars): web-design-guidelines (100+ auditable a11y / UX rules) and
  react-best-practices (57 performance rules). Auditable checklists that
  complement web-studio's method for the Next.js side of the house.
- **Browser automation**: official **webapp-testing** covers local apps (Tier
  1); for live-web work add
  [lackeyjb/playwright-skill](https://github.com/lackeyjb/playwright-skill)
  (3.0k stars; Claude writes and runs arbitrary Playwright scripts) or
  [obra/superpowers-chrome](https://github.com/obra/superpowers-chrome) (339
  stars; drives your real logged-in Chrome via CDP, useful for paywalled IR
  pages and dashboards). Vercel's
  [agent-browser](https://github.com/vercel-labs/agent-browser) (40.4k stars,
  652K installs) is the heavier-duty CLI option.

---

## Tier 3: situational watchlist

- **Carta plugins** (carta-cap-table, carta-investors, in claude-plugins-official):
  cap tables, 409A, waterfalls, investor benchmarks. High value the moment
  PE / VC cap-table work recurs.
- **edgar-change-interpreter**
  ([cmdrvl/edgar-change-interpreter](https://github.com/cmdrvl/edgar-change-interpreter),
  6 stars, MIT): flags material changes, vanished disclosures, and
  interpretation traps BETWEEN filing periods. Tiny traction, unique
  capability; inspect and adopt if filings-delta work recurs.
- **x2strategy** ([ALAGENT-HKU/x2strategy](https://github.com/ALAGENT-HKU/x2strategy),
  255 stars, HKU-affiliated): quant paper to validated Backtrader backtest.
  Nothing in the stack does replication; adopt if that becomes a workflow.
- **data@knowledge-work-plugins** (official,
  [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins),
  23.4k stars): validate-data, statistical-analysis, build-dashboard skills;
  validation-minded and free. Partner entries there worth noting: **daloopa**
  (institutional data skills, if credentials ever materialize) and **grasp**
  (deal-work workflows).
- **K-Dense scientific skills**
  ([K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills),
  33.1k stars, 140+ skills): cherry-pick the statistics / time-series /
  fred-economic-data subset; ignore the wet-lab majority.
- **Diagram production**: [tt-a1i/archify](https://github.com/tt-a1i/archify)
  (11.2k stars; animated self-contained HTML architecture diagrams) and
  [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill)
  (7.4k stars; natural language to EDITABLE draw.io files, 11 presets, exec-view
  compression). Editable source beats static SVG for client-grade figures.
- **EODHD skills**
  ([EodHistoricalData/eodhd-claude-skills](https://github.com/EodHistoricalData/eodhd-claude-skills),
  32 stars, vendor-official): global coverage (150k tickers, 70+ exchanges) and
  options analytics; another subscription (free tier 20 calls / day), so only if
  international coverage becomes a gap.
- **JoelLewis/finance_skills** ([repo](https://github.com/JoelLewis/finance_skills),
  164 stars): the wealth-management (Black-Litterman, factor investing, Monte
  Carlo VaR) and GIPS / compliance subsets are net-new; the core finance math
  duplicates harrison-finance-markets.
- **context-mode** ([mksglu/context-mode](https://github.com/mksglu/context-mode),
  19.8k stars): sandboxes tool output and persists session memory; consider if
  long sessions start dying to context rot.
- **makerskills** ([coreyhaines31/makerskills](https://github.com/coreyhaines31/makerskills),
  557 stars): decision frameworks, second-brain, scenario modeling; the closest
  philosophical cousin to a personal analyst OS, worth mining for patterns.
- **LangAlpha** ([ginlix-ai/langalpha](https://github.com/ginlix-ai/langalpha),
  1.6k stars): a competing full "Claude Code for financial markets" platform; a
  design reference for this repo's evolution, not an install.
- **agiprolabs/claude-trading-skills** ([repo](https://github.com/agiprolabs/claude-trading-skills),
  268 stars): ignore the crypto / DeFi half; the vectorbt / walk-forward /
  regime-detection / Kelly-sizing quant subset is reusable.

---

## Popular, but skip (already covered or poor fit)

| Skill | Traction | Why skip |
|---|---|---|
| quant-sentiment-ai/claude-equity-research | 687 stars | The house analyst suite is deeper; mine its report structure once, do not install |
| ECC (affaan-m/ECC) | 239.2k stars | Sprawling 183-skill harness; the useful ideas (memory, research-first) arrive via Tier 1 picks without the sprawl |
| ui-ux-pro-max-skill | 115.3k stars | web-studio owns design method; this is a reference corpus at best |
| ponytail | 100.1k stars | Aggressive YAGNI for codebases; wrong instinct for analytical deliverables |
| caveman | 97.3k stars | 65 percent output-token cut by stripping narration; fights the delivery contract. If cost ever bites, use caveman-micro (85 tokens) selectively |
| spec-kit (github/spec-kit) | 126.1k stars | Ceremony-heavy spec-driven dev; harrison-execution plus grill-me covers the need |
| marketingskills (coreyhaines31) | ~43.8k stars | CRO / SEO / copywriting; out of scope |
| i-have-adhd | 19.1k stars | Answer-first formatting; the kernel's delivery contract already enforces this |
| excel-analyst-pro-skill-md | 50 stars | Superseded by financial-analysis vertical plus official xlsx |
| brand-guidelines (official) | n/a | Anthropic's own brand; only useful as a template to fork into a personal brand skill |
| claude-scientific-writer, paper-search-mcp, notebooklm-py | various | Academic-publishing shaped; marginal for investment research |

---

## Ecosystem notes worth keeping

- **Where to watch**: [skills.sh](https://www.skills.sh/) (Vercel's
  install-telemetry leaderboard: the best real-usage signal, since stars can be
  gamed and installs less so),
  [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)
  (30.0k stars, best signal-to-noise list),
  [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)
  (72.2k stars, biggest list, vendor-run), [claude.com/plugins](https://claude.com/plugins)
  (Anthropic-verified badges), and
  [claudeskills.info/best/trading-skills](https://claudeskills.info/best/trading-skills/)
  for the finance long tail.
- **The standard is open and portable**: the Agent Skills spec
  ([agentskills.io](https://agentskills.io), repo 24.1k stars, Apache-2.0,
  originated at Anthropic) is adopted by ~45 clients including GitHub Copilot,
  Cursor, Codex, and Gemini CLI. Skills written for this OS are portable, and
  the `npx skills` CLI ([vercel-labs/skills](https://github.com/vercel-labs/skills),
  28.6k stars) is the de-facto cross-agent package manager.
- **Registry hygiene**: avoid installing from ClawHub and other raw-crawl
  registries without scanning (see Tier 0). SkillsMP and claudemarketplaces.com
  are uncurated crawls; fine for discovery, not for trust.
- **Consensus from heavy users**: "eight to twelve well-chosen skills cover most
  of a senior developer's day." The recommendation set above is deliberately a
  curation, not a hoard; prefer extending the harrison-* suite over installing
  overlapping frameworks.
- **Community sentiment anchors**: Simon Willison ("Claude Skills are awesome,
  maybe a bigger deal than MCP", 2025-10-16); Evan Schwartz's superpowers rave
  (2026-04-02) against the HN counter-view in the same thread; Anthropic's
  skills launch thread at 816 points on HN.

---

## Install quick reference

    # Tier 0
    npx skills add NVIDIA/SkillSpector          # then scan everything below

    # Tier 1
    claude plugin marketplace add anthropics/financial-services
    claude plugin install financial-analysis@claude-for-financial-services
    claude plugin install equity-research@claude-for-financial-services
    claude plugin install private-equity@claude-for-financial-services

    /plugin marketplace add anthropics/skills   # anthropic-agent-skills
    /plugin install document-skills@anthropic-agent-skills   # July 2026 refresh
    /plugin install example-skills@anthropic-agent-skills    # webapp-testing, frontend-design, doc-coauthoring

    npx skills add mattpocock/skills            # pick: grill-me, handoff, research
    npx skills add blader/humanizer
    npm install -g claude-mem && claude-mem install   # scan first; configure exclusions
    npx skills add gauss314/skills
    /plugin marketplace add duckdb/duckdb-skills
    /plugin install duckdb-skills@duckdb-skills

    # Tier 2 (as needed)
    /plugin marketplace add anthropics/claude-plugins-official
    /plugin install hookify@claude-plugins-official
    /plugin install claude-code-setup@claude-plugins-official
    /plugin install claude-md-management@claude-plugins-official
    /plugin install bigdata-com@claude-plugins-official
    npx skills add tradermonty/claude-trading-skills
    npx skills add OctagonAI/skills             # free API key required
    /plugin marketplace add OthmanAdi/planning-with-files
    /plugin marketplace add obra/superpowers-marketplace   # cherry-pick sub-skills

---

## Verification caveats

Captured 2026-08-10. GitHub star counts and last-push dates were checked via the
GitHub API by the research agents; install counts come from skills.sh telemetry
as displayed that day. Known soft spots: wshobson/agents repo-level stars,
grill-me per-skill install split, ECC's exact skill counts, the claude.ai
customize-surface merge date, and the paywalled thewenglab "100 Wall Street
analyst skills" pack (contents unverifiable) are all UNVERIFIED as labeled in
the underlying research. Before any install, re-check the repo (skills move fast
in 2026; one top skill changed owners this year: karpathy-skills now lives under
multica-ai after the original forrestchang repo went dark).
