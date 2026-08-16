"""CLI: python -m engine <command>

Commands:
    style                         profile previous reports -> style/
    add <slug> "<Name>" [pbid]    register a company + scaffold its folders
    export [slug]                 write companies/<slug>/PROFILE.md (all if omitted)
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
    watch <slug>|--all            compare what was reported with what we hold
    refresh [slug|--all]          harvest, re-file, compare, rebuild the page
    dashboard [out.html]          render the desk dashboard from the store
    sources <slug> <domain> [cik] create/extend the harvest source manifest
    harvest <slug>|--all          sweep sources, archive evidence, log outcomes
    intake                        route uploads/ (links + documents) to companies
    model <slug> [type]           build the financial model workbook (2022-2032)
    modelcheck <workbook.xlsx>    recompute a built model and run its sanity gates
"""
from __future__ import annotations
import json, sys
from . import (store, trends, style, compose, charts, qa, desk, harvest,
               evidence, intake, model, model_check, watch)


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

    elif cmd == "add":
        slug, name = args[0], args[1]
        pbid = args[2] if len(args) > 2 else None
        path = store.add_company(slug, name, pb_entity_id=pbid)
        print(f"registered {slug} -> {path} (universe + category folders)")

    elif cmd == "export":
        slugs = args or [c["slug"] for c in store.universe()["companies"]]
        for slug in slugs:
            print("wrote", compose.export_profile_md(slug))

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

    elif cmd == "sources":
        slug = args[0]
        domain = args[1] if len(args) > 1 else None
        cik = args[2] if len(args) > 2 else None
        name = None
        for ent in store.universe().get("companies", []):
            if ent.get("slug") == slug:
                name = ent.get("name")
        harvest.ensure_manifest(slug, name=name, domain=domain, cik=cik)
        m = harvest.reprobe(slug)
        live = [s for s in m.get("sources") or [] if s.get("enabled", True)]
        print(f"{slug}: {len(live)}/{len(m.get('sources') or [])} sources reachable"
              + (f", CIK {m['cik']}" if m.get("cik") else ""))
        for s in m.get("sources") or []:
            mark = " " if s.get("enabled", True) else "x"
            print(f"  {mark} [{s['kind']:>9}] {s['id']:<12} {s['url']}")

    elif cmd == "harvest":
        if args and args[0] == "--all":
            runs = harvest.sweep_all(quiet=False)
            tot = {}
            for r in runs:
                for k, v in r["counts"].items():
                    tot[k] = tot.get(k, 0) + v
            print(f"\n{len(runs)} companies swept: "
                  + ", ".join(f"{k}={v}" for k, v in sorted(tot.items())))
        elif args:
            run = harvest.sweep(args[0], quiet=False)
            for r in run["results"]:
                mark = {"new": "+", "changed": "~", "unchanged": "=",
                        "unreachable": "!"}.get(r["outcome"], "?")
                print(f"  {mark} {r['id']:<16} {r['outcome']:<12}"
                      f"{r.get('error') or str(r.get('chars', '')) + ' chars'}")
        else:
            for row in harvest.status_all():
                print(f"{row['slug']:<14} sources={row['sources']:<3} "
                      f"last={row['last_run'] or 'never'}")

    elif cmd == "intake":
        res = intake.route_uploads()
        s_ = res["summary"]
        print(f"links {s_['links_filed']}/{s_['links']} filed · "
              f"documents {s_['documents_filed']}/{s_['documents']} filed")

    elif cmd == "model":
        slug = args[0]
        kind = args[1] if len(args) > 1 else "operating"
        info = model.build(slug, kind)
        print(f"wrote {info['path']}")
        print(f"  {info['years']} · {info['sourced']} sourced inputs, "
              f"{info['assumed']} assumptions ({info['ratio']:.0%} sourced) "
              f"-> {info['grade'].upper()}")

    elif cmd == "modelcheck":
        res = model_check.check(args[0])
        print(model_check.report(res))
        return 0 if res.get("ok") else 2

    elif cmd == "watch":
        slugs = ([e["slug"] for e in store.universe()["companies"]]
                 if (not args or args[0] == "--all") else [args[0]])
        total = 0
        for slug in slugs:
            res = watch.scan(slug)
            total += res["open"]
            if res["open"] or len(slugs) == 1:
                print(watch.render(res))
        print(f"\n{total} figures await a decision across {len(slugs)} companies")

    elif cmd == "refresh":
        # The whole chain in one command: read the world, re-file what came
        # back, compare it with what we hold, rebuild the page. Each stage
        # feeds the next, so a figure reported this morning reaches the
        # dashboard's attention panel by the end of this run.
        named = [a for a in args if not a.startswith("--")]
        slugs = named or [e["slug"] for e in store.universe()["companies"]]
        print(f"refreshing {len(slugs)} companies")
        swept = {"changed": 0, "new": 0, "unchanged": 0, "unreachable": 0}
        if "--no-fetch" not in args:
            for slug in slugs:
                try:
                    counts = harvest.sweep(slug, quiet=True).get("counts") or {}
                except Exception as exc:                        # a dead source
                    print(f"  {slug}: harvest failed ({exc})")  # is a gap, not a stop
                    continue
                for k, v in counts.items():
                    swept[k] = swept.get(k, 0) + v
        retag = [harvest.retag_news(s) for s in slugs]
        moved = sum(r["dropped"] for r in retag)
        stories = sum(r["now"] for r in retag)
        print(f"  harvest: {swept['changed']} sources changed, {swept['new']} new, "
              f"{swept['unreachable']} unreachable")
        print(f"  news: {stories} stories on file for these companies"
              + (f" · re-filing moved {moved}" if moved else ""))
        open_items = 0
        for slug in slugs:
            open_items += watch.scan(slug)["open"]
        print(f"  checked against the store: {open_items} figures await a decision")
        stale_models = model.stale(slugs)
        if stale_models:
            print(f"  models built on figures that have since moved: "
                  f"{', '.join(m['slug'] for m in stale_models)}")
        out, data = desk.build()
        print(f"  wrote {out}")
        if open_items:
            print(f"\nOpen the dashboard and settle {open_items} figure(s); "
                  f"run `python3 -m engine watch --all` for the detail.")

    elif cmd == "dashboard":
        out, data = desk.build(args[0] if args else None)
        cos = data["companies"]
        thin = [c["slug"] for c in cos if c["n_cats"] <= 2]
        print(f"wrote {out}")
        print(f"  {len(cos)} companies, {sum(c['n_facts'] for c in cos)} facts, "
              f"{sum(c['n_stale'] for c in cos)} stale, "
              f"{sum(c['n_armed'] for c in cos)} triggers armed")
        if thin:
            print(f"  thin coverage ({len(thin)}): {', '.join(thin)}")

    else:
        print(__doc__)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
