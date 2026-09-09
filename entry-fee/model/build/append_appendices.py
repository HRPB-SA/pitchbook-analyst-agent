import json
sw = json.load(open("sweep_a.json")); xc = json.load(open("xcheck_formulas.json"))
def f(v, fmt):
    try: return format(v, fmt)
    except Exception: return str(v)
out = ["\n## Appendix A. Formulas-library cross-check (build/xcheck_formulas.py; LibreOffice cached value vs the `formulas` library on the re-quoted file)\n"]
for path, o in xc.items():
    out.append(f"\n{path.split('/')[-1]}: {len(o['cells'])} cells compared, {o['mismatches']} mismatches ({o['seconds']} s).\n\n| Cell | LibreOffice | formulas library | Match |\n|---|---|---|---|")
    for r in o["cells"]:
        out.append(f"| {r['cell']} | {r['libreoffice']} | {r['formulas']} | {'yes' if r['match'] else 'NO'} |")
out.append("\n## Appendix B. Scenario and switch sweep (build/sweep_a.py; each state recalculated by LibreOffice on a temp copy; Base defaults otherwise)\n")
out.append("No error cells under any state (column 'errors'). 'fails' = the 08_Output FAIL count (the check table assumes Base defaults, so non-zero counts away from Base are expected and listed).\n")
out.append("| State | recalc | errors | fails | scenario | FY2026E Anthropic | E10 gap 2028 low | high | Google leg 2028 | relative multiple (live) | sign | CE ratio | composite A | composite O |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for k, r in sw.items():
    out.append(f"| {k} | {r['recalc_status']} | {r['cached_errors']} | {r['failcount']} | {r['scenario']} | {f(r['FY26A'], ',.0f')} | {f(r['gap28_lo'], ',.0f')} | {f(r['gap28_hi'], ',.0f')} | {f(r['google_leg28'], ',.0f')} | {f(r['relmult_live'], '+.1%')} | {r['relmult_sign']} | {f(r['CE_ratio'], '.2f')}x | {f(r['comp_A_live'], '.3f')} | {f(r['comp_O_live'], '.3f')} |")
errs = sum(1 for r in sw.values() if r["cached_errors"]); bad = [k for k, r in sw.items() if r["recalc_status"] != "success"]
out.append(f"\nStates run: {len(sw)}; states with any error cell: {errs}; recalc non-success: {bad or 'none'}.")
open("../tie-out.md", "a").write("\n".join(out) + "\n")
print("appended; states", len(sw), "errors", errs, "bad", bad)
for k, r in sw.items():
    print(f"{k:<26} err={r['cached_errors']} fails={r['failcount']} scen={r['scenario']} gap28={f(r['gap28_lo'],',.0f')}/{f(r['gap28_hi'],',.0f')} rel={f(r['relmult_live'],'+.1%')} CE={f(r['CE_ratio'],'.2f')} compA={f(r['comp_A_live'],'.3f')} compO={f(r['comp_O_live'],'.3f')}")
for path, o in xc.items(): print(path, "mismatches", o["mismatches"], [r["cell"] for r in o["cells"] if not r["match"]])
