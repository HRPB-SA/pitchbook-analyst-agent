# Vendored Skills Manifest

91 third-party Agent Skills vendored 2026-08-10 (branch `claude/skills-research-jviof7`),
selected per `skills_research.md` (Tier 1 + Tier 2). Every skill was fetched at the
pinned upstream commit below and security-reviewed before commit: a mechanical sweep
(network destinations, exec/eval, credential reads, obfuscation, injection phrases)
plus two full-file review passes reading every SKILL.md and every bundled script.
Two skills failed review and were dropped; one one-line patch was applied (documented
below). Companion agent definitions live in `.claude/agents/`.

Policy notes:

- Vendored files are byte-identical to upstream (except the one documented patch),
  including upstream punctuation. The repo's zero-em-dash rule applies to authored
  deliverables and the docx build scan; vendored third-party files are exempt so
  they stay diffable against upstream.
- License texts for redistribution are collected in `LICENSES/`. Anthropic
  example skills carry per-folder LICENSE.txt files; `doc-coauthoring` has no
  license file upstream (distributed via Anthropic's public example-skills
  plugin); Vercel packs and karpathy-guidelines and deep-research declare MIT in
  frontmatter or README only, with no license file upstream.
- To update a source: re-clone the repo, diff against the pinned commit, re-review,
  re-vendor. To prune a skill: delete its folder (each is self-contained).

## Sources

| Source repo | Commit | License | Skills vendored |
|---|---|---|---|
| anthropics/financial-services | 38652224c106 | Apache-2.0 | 31: 3-statement-model, ai-readiness, audit-xls, catalyst-calendar, clean-data-xls, competitive-analysis, comps-analysis, dcf-model, dd-checklist, dd-meeting-prep, deal-screening, deal-sourcing, deck-refresh, earnings-analysis, earnings-preview, ib-check-deck, ic-memo, idea-generation, initiating-coverage, lbo-model, model-update, morning-note, portfolio-monitoring, ppt-template-creator, pptx-author, returns-analysis, sector-overview, thesis-tracker, unit-economics, value-creation-plan, xlsx-author |
| anthropics/skills | f17010c9bb48 | Apache-2.0 (per-skill) | 3: webapp-testing, frontend-design, doc-coauthoring |
| mattpocock/skills | 84fdeffd12f2 | MIT | 4: grill-me, grilling, handoff, research |
| blader/humanizer | 523374dee72d | MIT | 1: humanizer |
| gauss314/skills | 5156f818420d | MIT | 19: earningswhispers, sec-data, fred-macro, backtesting, nasdaq-data, tradingview, barchart, cboe-data, investing, portfolio, google-finance, marketscreener, historyofmarket, macrotrends, finviz, yahoo-finance, option-pricing, marketwatch, companiesmarketcap |
| duckdb/duckdb-skills | 7feda8e01e22 | MIT | 8: attach-db, convert-file, duckdb-docs, install-duckdb, query, read-file, s3-explore, spatial |
| multica-ai/andrej-karpathy-skills | 2c606141936f | MIT (README claim) | 1: karpathy-guidelines |
| tradermonty/claude-trading-skills | c51ff27beeaf | MIT | 16: market-environment-analysis, breadth-chart-analyst, macro-regime-detector, us-market-bubble-detector, vcp-screener, stockbee-episodic-pivot-analyzer, dividend-growth-pullback-screener, institutional-flow-tracker, position-sizer, backtest-expert, economic-calendar-fetcher, earnings-calendar, sector-analyst, finviz-screener, scenario-analyzer, data-quality-checker (plus 2 agents: scenario-analyst, strategy-reviewer) |
| OthmanAdi/planning-with-files | e8f505a4f502 | MIT | 1: planning-with-files |
| obra/superpowers | 44c9b2d6e889 | MIT | 3: brainstorming, systematic-debugging, verification-before-completion |
| vercel-labs/agent-skills | 7c180d9044c9 | MIT (frontmatter claim) | 2: vercel-react-best-practices, vercel-composition-patterns |
| 199-biotechnologies/claude-deep-research-skill | f2f2c0fa4e76 | MIT (README claim) | 1: deep-research |
| lackeyjb/playwright-skill | bb7e920d3760 | MIT | 1: playwright-skill |

## Dropped at review

- `read-memories` (duckdb-skills): searches ALL local Claude Code session logs
  across every project on the machine. Privacy and MNPI/COI conflict; excluded.
- `web-design-guidelines` (vercel-labs): fetches its rule set live from GitHub at
  runtime, so reviewed bytes are not the bytes that run. Excluded; re-add only
  with a pinned local snapshot.
- `simplywallst` (gauss314): carried a 15 MB bundled CSV asset; marginal value
  for the weight.
- `skill-creator` (financial-services): duplicate of the account-level skill.

## Patches applied to vendored code

- `brainstorming/scripts/server.cjs` line 106: the visual companion page loaded a
  logo image from primeradiant.com, acting as a de facto usage beacon from the
  browser. URL replaced with an inline transparent data URI. No other behavior
  changed.

## Deliberately not vendored (install on your own machine instead)

- OctagonAI/skills (60+ earnings/filings skills): hard dependency on the Octagon
  MCP server plus API key. `npx skills add OctagonAI/skills` once keyed.
- hookify, claude-code-setup, claude-md-management, bigdata-com: full plugins
  (commands, hooks, agents), not plain skills. Install via
  `/plugin marketplace add anthropics/claude-plugins-official` then
  `/plugin install <name>@claude-plugins-official`.
- claude-mem: hooks plus local daemon; `npm install -g claude-mem` then
  `claude-mem install`. Scan first; configure exclusions for sensitive work.
- Document skills refresh (docx/pptx/xlsx/pdf): account-level Anthropic skills;
  update via `document-skills@anthropic-agent-skills`, not this repo.
- steveyegge/beads: a Go binary system, not a skill.
- Skill_Seekers, NVIDIA SkillSpector: local tooling (skill minting, skill
  scanning), not runtime skills.

## Known caveats (accepted at review)

- comps-analysis and lbo-model reference example workbooks
  (`examples/comps_example.xlsx`, `examples/LBO_Model.xlsx`) that do not exist
  upstream; the build methodology in each SKILL.md is complete without them.
  lbo-model and dcf-model also reference the claude.ai path
  `/mnt/skills/public/xlsx/recalc.py`; local equivalent is the account-level
  xlsx skill plus LibreOffice.
- Several financial-services skills assume claude.ai or Office-add-in tooling
  (`ask_user_question`, `create_file`, `/mnt/user-data`); all degrade to
  ordinary file workflows.
- API keys, all optional and sent only to their own vendors: FRED_API_KEY
  (fred-macro), FMP_API_KEY (macro-regime-detector, vcp-screener,
  stockbee-episodic-pivot-analyzer, dividend-growth-pullback-screener,
  institutional-flow-tracker, economic-calendar-fetcher, earnings-calendar),
  FINVIZ_API_KEY Elite (finviz-screener, dividend screener). Some FMP endpoints
  (13F, economic calendar) need a paid tier.
- sec-data hardcodes the author's email as the SEC EDGAR User-Agent; swap in
  your own per SEC fair-access policy before heavy use.
- ToS-gray scrapers (browser impersonation or unofficial endpoints): investing,
  marketscreener, google-finance, nasdaq-data, yahoo-finance, tradingview,
  barchart, macrotrends, finviz, marketwatch, companiesmarketcap. Fragile by
  nature and subject to source-site terms; weigh against harrison-validation
  source-tier rules before citing their output.
- gauss314 documentation is partly Spanish; skills work fine in English.
- grill-me is a trigger stub for grilling (both vendored). brainstorming's
  final step references the un-vendored writing-plans skill; treat that mention
  as inert. scenario-analyzer requires the two vendored agents in
  `.claude/agents/`.
- planning-with-files declares hooks in skill frontmatter (prompt/tool-time
  plan injection); on harnesses without skill-hook support it degrades to a
  normal skill. Its Stop gate is opt-in and capped.
- playwright-skill installs npm dependencies and Chromium into its own folder on
  first run; a `.gitignore` inside the folder keeps runtime artifacts out of
  git.
- initiating-coverage and earnings-analysis deliberately instruct maximal token
  spend (30-50 page outputs); invoke them intentionally, not casually.
- Context cost: 91 skill descriptions load into every session on this repo.
  Prune freely by deleting folders; this manifest is the record of what came
  from where.
