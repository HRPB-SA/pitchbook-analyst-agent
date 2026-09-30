#!/usr/bin/env python3
"""
CONTEXT: ANTHROPIC INTELLIGENCE DESK — Wave 3 assembler.
Turns analyst agent outputs into the dashboard's analysis files, resolving every event id through data/id_map.json and
dropping (and counting) any id that does not exist. Tolerates missing inputs.
  agents/outputs/analyst-topic-*.json  -> data/topics.json
  agents/outputs/analyst-compute.json  -> data/compute.json
  agents/outputs/analyst-bull|bear|judge.json -> data/thesis.json
Run: python3 scripts/build_analysis.py
"""
import glob, json, os, re
from datetime import datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT, DATA = os.path.join(ROOT, "agents", "outputs"), os.path.join(ROOT, "data")
ORDER = ["capital", "revenue", "compute", "product", "moat", "governance", "legal", "government", "people", "ecosystem"]

def load(fn):
    try: return json.load(open(fn))
    except Exception: return None

IDM = load(os.path.join(DATA, "id_map.json")) or {}
EVS = {e["id"] for e in (load(os.path.join(DATA, "events.json")) or [])}

def fix(ids, st):
    out = []
    for i in ids or []:
        j = IDM.get(i) or (i if i in EVS else None)
        if j:
            if j not in out: out.append(j)
        else: st["dropped"] += 1
    return out

def items(lst, st):
    res = []
    for x in lst or []:
        if isinstance(x, str): res.append({"t": x, "e": []})
        elif isinstance(x, dict): res.append({"t": x.get("t") or x.get("text") or "", "e": fix(x.get("e") or x.get("event_ids"), st)})
    return res

def topics():
    rows, val = [], {}
    for fn in sorted(glob.glob(os.path.join(OUT, "analyst-topic-*.json"))):
        d = load(fn)
        if not d or not d.get("topic"): continue
        t = dict(d["topic"]); st = {"dropped": 0}
        t["slug"] = t.get("slug") or os.path.basename(fn)[len("analyst-topic-"):-5]
        t["evidence"] = fix(t.get("evidence"), st)
        km = []
        for k in t.get("key_metrics") or []:
            k = dict(k); k["event_id"] = (fix([k.get("event_id")], st) or [None])[0] if k.get("event_id") else None; km.append(k)
        t["key_metrics"] = km
        for f in ("what", "means", "implications"): t[f] = items(t.get(f), st)
        t["analyst"] = d.get("agent"); t["finished"] = d.get("finished")
        rows.append(t); val[t["slug"]] = {"evidence": len(t["evidence"]), "dropped_ids": st["dropped"]}
    rows.sort(key=lambda t: ORDER.index(t["slug"]) if t["slug"] in ORDER else 99)
    json.dump({"generated": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"), "topics": rows, "validation": val}, open(os.path.join(DATA, "topics.json"), "w"), indent=1, ensure_ascii=False)
    print(f"topics: {len(rows)} ({', '.join(t['slug'] for t in rows)}); dropped ids: {sum(v['dropped_ids'] for v in val.values())}")

def compute():
    d = load(os.path.join(OUT, "analyst-compute.json"))
    if not d:
        print("compute: no analyst-compute.json yet"); return
    st = {"dropped": 0}
    for c in d.get("commitments") or []:
        if c.get("event_id"): c["event_id"] = (fix([c["event_id"]], st) or [None])[0]
    if d.get("narrative"):
        for f in ("what", "means", "implications"): d["narrative"][f] = items(d["narrative"].get(f), st)
    d.pop("log", None)
    d["generated"] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"); d["validation"] = {"dropped_ids": st["dropped"]}
    json.dump(d, open(os.path.join(DATA, "compute.json"), "w"), indent=1, ensure_ascii=False)
    print(f"compute: {len(d.get('commitments') or [])} commitments; dropped ids: {st['dropped']}")

def thesis():
    bull, bear, judge = (load(os.path.join(OUT, f"analyst-{n}.json")) for n in ("bull", "bear", "judge"))
    if not (bull or bear or judge):
        print("thesis: no bull/bear/judge yet"); return
    st = {"dropped": 0}
    def case(d):
        out = []
        for c in (d or {}).get("case") or []:
            c = dict(c); c["event_ids"] = fix(c.get("event_ids"), st); out.append(c)
        return out
    T = {"generated": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"), "bull": case(bull), "bear": case(bear),
         "bull_at_price": (bull or {}).get("at_price", []), "bear_at_price": (bear or {}).get("at_price", []),
         "bull_outside_view": (bull or {}).get("outside_view"), "bear_outside_view": (bear or {}).get("outside_view"),
         "bull_concedes": (bull or {}).get("concedes"), "bear_concedes": (bear or {}).get("concedes")}
    if judge:
        vd = judge.get("verdict") or {}
        if vd.get("rationale_ids"): vd["rationale_ids"] = [fix(x, st) for x in vd["rationale_ids"]]
        for bm in vd.get("by_mark") or []:
            if bm.get("event_ids"): bm["event_ids"] = fix(bm["event_ids"], st)
        for wf in vd.get("what_flips_ids") or []: pass
        T["verdict"] = vd; T["scorecard"] = judge.get("scorecard", []); T["consensus"] = judge.get("consensus"); T["unresolved"] = judge.get("unresolved", [])
        br = []
        for b in judge.get("thesis_breakers") or []:
            b = dict(b); b["event_id"] = (fix([b.get("event_id")], st) or [None])[0] if b.get("event_id") else None; br.append(b)
        T["thesis_breakers"] = br
    json.dump(T, open(os.path.join(DATA, "thesis.json"), "w"), indent=1, ensure_ascii=False)
    print(f"thesis: bull {len(T['bull'])} bear {len(T['bear'])} verdict {'yes' if judge else 'pending'}; dropped ids: {st['dropped']}")

if __name__ == "__main__":
    topics(); compute(); thesis()
