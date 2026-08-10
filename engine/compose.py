"""Composition contract between the analyst agent and the builder.

Blocks grammar (JSON): a list of arrays, first element the kind:
    ["h1", "Section Title"]
    ["h2", "Subhead"]            ["h3", "Minor head"]
    ["p", "Paragraph text."]
    ["bullets", ["item", ...]]
    ["table", {"title": ..., "header": [...], "rows": [[...], ...],
               "align": "LRL...", "source": "...", "widths": [...](opt)}]
    ["fig", "chart_file.png", "Figure N. Caption with source and date."]

The agent writes prose blocks; auto-builders below generate data-grounded
blocks (fact sheets, tracker sections, sources) directly from the store so
every report carries a verified backbone regardless of who wrote the prose.
"""
from __future__ import annotations
import json, os
from . import schema, store

KINDS = {"h1": 2, "h2": 2, "h3": 2, "p": 2, "bullets": 2, "table": 2, "fig": 3}


def validate_blocks(blocks, where=""):
    errs = []
    if not isinstance(blocks, list):
        return [f"{where}: blocks must be a list"]
    for i, b in enumerate(blocks):
        loc = f"{where}#{i}"
        if not isinstance(b, list) or not b or b[0] not in KINDS:
            errs.append(f"{loc}: bad block {b!r:.80}")
            continue
        kind = b[0]
        if len(b) != KINDS[kind]:
            errs.append(f"{loc}: {kind} needs {KINDS[kind]} elements, got {len(b)}")
            continue
        if kind == "bullets" and not (isinstance(b[1], list) and all(isinstance(x, str) for x in b[1])):
            errs.append(f"{loc}: bullets payload must be list[str]")
        if kind == "table":
            spec = b[1]
            if not isinstance(spec, dict) or "header" not in spec or "rows" not in spec:
                errs.append(f"{loc}: table needs header+rows")
            else:
                n = len(spec["header"])
                for j, row in enumerate(spec["rows"]):
                    if len(row) != n:
                        errs.append(f"{loc}: row {j} has {len(row)} cells, header has {n}")
                a = spec.get("align")
                if a and len(a) != n:
                    errs.append(f"{loc}: align {a!r} length != {n}")
    return errs


def load_blocks(path):
    with open(path, encoding="utf-8") as fh:
        blocks = json.load(fh)
    errs = validate_blocks(blocks, os.path.basename(path))
    if errs:
        raise ValueError("invalid blocks:\n" + "\n".join(errs))
    return blocks


def _cite(f):
    """Render a Fact's provenance: 'source, as-of (tier)' + flags."""
    bits = [f.get("source", "unsourced"), str(f.get("as_of", "undated"))]
    s = ", ".join(bits) + f" ({f.get('tier', '?')})"
    flags = f.get("flags") or []
    if flags:
        s += " [" + ", ".join(flags) + "]"
    return s


def _val(f):
    v = f.get("value")
    if isinstance(v, float) and v == int(v):
        v = int(v)
    if isinstance(v, dict):
        s = " · ".join(f"{k} {x}" for k, x in v.items())
    else:
        s = str(v)
    if "est." in (f.get("flags") or []):
        s = f"~{s} (est.)"
    return s


def fact_sheet_blocks(slug, categories=None, title="Company fact sheet"):
    """One table per category: field / value / source-date-tier."""
    profile = store.load_profile(slug)
    blocks = []
    for cat in (categories or schema.CATEGORIES):
        block = profile.get(cat)
        if not isinstance(block, dict) or not block:
            continue
        label = schema.CATEGORIES[cat][0]
        rows = []
        for field, v in block.items():
            if schema.is_fact(v):
                rows.append([_label(field), _val(v), _cite(v)])
            elif isinstance(v, list) and v and all(schema.is_fact(x) for x in v):
                for item in v[-4:]:
                    rows.append([_label(field), _val(item), _cite(item)])
        if rows:
            blocks.append(["table", {
                "title": f"{title}: {label}" if title else label,
                "header": ["Metric", "Value", "Source, date (tier)"],
                "rows": rows, "align": "LLL",
            }])
    return blocks


def tracker_blocks(slug):
    """Tracker section: derived metrics, ladders, changes, staleness, conflicts."""
    from . import trends as _tr
    t = _tr.company_trends(slug)
    blocks = []
    if t["derived"]:
        rows = [[_label(k), str(v["value"]), v["basis"]] for k, v in t["derived"].items()]
        blocks.append(["table", {"title": "Derived metrics (computed this run)",
                                 "header": ["Metric", "Value", "Basis"],
                                 "rows": rows, "align": "LRL",
                                 "source": "Derived by the tracker at build time; inputs carry their own tiers."}])
    if t["ladders"]:
        rows = []
        for k, lt in t["ladders"].items():
            f0, f1 = lt["first"], lt["last"]
            rows.append([_label(k), f"{f0[1]:g} ({f0[0]})", f"{f1[1]:g} ({f1[0]})",
                         lt["direction"], str(lt["points"])])
        blocks.append(["table", {"title": "Tracked ladders",
                                 "header": ["Series", "First print", "Latest print", "Direction", "Prints"],
                                 "rows": rows, "align": "LLLLR"}])
    sd = t.get("snapshot_delta")
    if sd and sd["changes"]:
        rows = [[c["field"], _short(c["from"]), _short(c["to"])] for c in sd["changes"][:20]]
        blocks.append(["table", {"title": f"Changed since prior snapshot ({sd['from']} to {sd['to']})",
                                 "header": ["Field", "Prior", "Current"],
                                 "rows": rows, "align": "LLL"}])
    if t["staleness"]["stale"]:
        rows = [[s["field"], _short(s["value"]), f"{s['as_of']} ({s['age_days']}d, {s['decay']})"]
                for s in t["staleness"]["stale"]]
        blocks.append(["table", {"title": "Stale facts (decay-class breach; refreshed or flagged before use)",
                                 "header": ["Field", "Value", "As of (age, class)"],
                                 "rows": rows, "align": "LLL"}])
    if t["open_conflicts"]:
        rows = [[c["field"],
                 f"{_short(c['held']['value'])} ({c['held']['tier']}, {c['held'].get('as_of')})",
                 f"{_short(c['challenger']['value'])} ({c['challenger']['tier']}, {c['challenger'].get('as_of')})"]
                for c in t["open_conflicts"]]
        blocks.append(["table", {"title": "Open conflicts (frozen; both values stated, neither chosen)",
                                 "header": ["Field", "Held", "Challenger"],
                                 "rows": rows, "align": "LLL"}])
    return blocks


LABELS = {
    "ev_multiple": "Run-rate multiple",
    "capital_efficiency": "Capital efficiency (CE, equity-only)",
    "usd_per_aibq_pt_bn": "Valuation per AIBQ point ($B)",
    "run_rate_ladder_bn": "Run-rate ladder ($B)",
    "growth_yoy_pct_ladder": "YoY growth ladder (%)",
    "gross_margin_pct_ladder": "Gross margin ladder (%)",
    "employees": "Employees",
    "employees_ladder": "Employees",
    "nrr_pct": "Net revenue retention",
    "pb_ttm_field_note": "PitchBook TTM field (trap note)",
}


def _label(key):
    if key in LABELS:
        return LABELS[key]
    return key.replace("_bn", " ($B)").replace("_pct", " (%)").replace("_", " ").strip().capitalize()


def _short(v, n=48):
    s = str(v)
    return s if len(s) <= n else s[:n - 3] + "..."
