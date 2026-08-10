"""Report engine: deterministic half of the analyst automation.

Modules:
    schema      Fact shape, categories, tiers, decay classes
    store       snapshots + canonical profiles, freeze-on-conflict merge
    trends      ladders, deltas, derived metrics, staleness, triggers
    style       style profiler over the shipped report library
    compose     block grammar + auto-generated data-grounded sections
    charts      house chart factory (embargo-guarded)
    build_docx  template-driven docx/pdf builder with QA gate
    qa          em-dash / embargo / placeholder / banned-phrase gates

The judgment half (research, tiering decisions, prose) is executed by the
analyst agent per CLAUDE.md; this package makes that work reproducible.
"""
__all__ = ["schema", "store", "trends", "style", "compose", "charts",
           "build_docx", "qa"]
