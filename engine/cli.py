"""CLI: python -m engine <command>

Commands:
    style                         profile reference reports -> style/
    snapshot <slug> <file>        add snapshot JSON + merge into canonical
    merge <slug> <snapshot.json>  merge an existing snapshot file by name
    trends <slug>                 recompute trends.json, print digest
    digest <slug>                 print tracker digest markdown
    cohort                        cross-company table
    staleness [slug]              stale/flagged facts (all companies if omitted)
    charts <charts.json> [outdir] render chart specs
    build <report_dir>            build report (docx + pdf + QA gate)
    qa <file.docx|blocks.json>    run QA gates on an artifact
    validate <blocks.json>        validate block grammar
"""
from __future__ import annotations
import json, sys
from . import store, trends, style, compose, charts, qa


def main(argv=None):
    argv = argv or sys.argv[1:]
    if not argv:
        print(__doc__)
        return 1
    cmd, args = argv[0], argv[1:]

    if cmd == "style":
        prof = style.run()
        print(json.dumps(prof["sentences"], indent=2))
        print("wrote style/style_profile.json + style/STYLE_PROFILE.md")

    elif cmd == "snapshot":
        slug, path = args
        with open(path, encoding="utf-8") as fh:
            payload = json.load(fh)
        name = store.add_snapshot(slug, payload)
        rep = store.merge_snapshot(slug, payload)
        print(f"snapshot {name} written; merge:")
        print(json.dumps(rep, indent=2))

    elif cmd == "merge":
        slug, name = args
        rep = store.merge_snapshot(slug, store.load_snapshot(slug, name))
        print(json.dumps(rep, indent=2))

    elif cmd == "trends":
        t = trends.company_trends(args[0])
        print(json.dumps(t, indent=2, default=str))

    elif cmd == "digest":
        print(trends.digest_md(args[0]))

    elif cmd == "cohort":
        rows = trends.cohort_view()
        w = "{:<14}{:>9}{:>7}{:>12}{:>7}{:>7}"
        print(w.format("company", "multiple", "CE", "$B/pt", "stale", "flags"))
        for r in rows:
            print(w.format(r["slug"], r["multiple"] or "-", r["ce"] or "-",
                           r["usd_per_pt_bn"] or "-", r["stale_facts"], r["flags"]))

    elif cmd == "staleness":
        slugs = args or [c["slug"] for c in store.universe()["companies"]]
        for slug in slugs:
            rep = store.staleness_report(slug)
            if rep["stale"] or rep["flagged"]:
                print(f"== {slug}")
                for s in rep["stale"]:
                    print(f"  STALE {s['field']} = {s['value']!r} "
                          f"({s['as_of']}, {s['age_days']}d, {s['decay']})")
                for f in rep["flagged"]:
                    print(f"  {f['flag']} {f['field']} = {f['value']!r}")

    elif cmd == "charts":
        out = charts.render_file(args[0], args[1] if len(args) > 1 else None)
        print("\n".join(out))

    elif cmd == "build":
        from . import build_docx
        res = build_docx.build_report(args[0])
        print(json.dumps({k: v for k, v in res.items() if k != "qa"}, indent=2))
        print(res["qa"])

    elif cmd == "qa":
        path = args[0]
        if path.endswith(".docx"):
            issues = qa.check_docx(path)
        else:
            with open(path, encoding="utf-8") as fh:
                issues = qa.check_blocks(json.load(fh), path)
        print(qa.format_report(issues))
        ok, _, _ = qa.gate(issues)
        return 0 if ok else 2

    elif cmd == "validate":
        compose.load_blocks(args[0])
        print("blocks valid")

    else:
        print(__doc__)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
