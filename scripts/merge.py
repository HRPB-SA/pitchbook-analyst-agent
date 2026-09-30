#!/usr/bin/env python3
"""
CONTEXT: ANTHROPIC INTELLIGENCE DESK — Wave 2 merge.
Reads every agent output in agents/outputs/*.json, validates, normalizes, dedupes
(cross-agent duplicates become corroboration, not noise), and emits:
  data/events.json      master timeline (ascending date)
  data/metrics.json     time series pulled from the record
  data/entities.json    entity graph
  data/agent_log.json   the real activity log with timestamps
  data/ledger.json      conflicts + open items + coverage stats
Run: python3 scripts/merge.py
"""
import glob, json, os, re, sys, math
from collections import defaultdict
from datetime import datetime, timedelta
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "agents", "outputs")
DATA = os.path.join(ROOT, "data")
os.makedirs(DATA, exist_ok=True)

TIER_RANK = {"T1": 1, "T2": 2, "T3": 3, "T4": 4, "T5": 5}
CONF_RANK = {"CANONICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3, "VERIFY": 4, "DISPUTED": 5}
CATS = {"funding","valuation","compute","product","model","pricing","governance","safety","legal",
        "regulatory","policy","government","people","partnership","customer","acquisition","investment",
        "international","revenue","financials","ipo","research","security","competition","debt","secondary","other"}
STOP = set("the a an of to in for on at by with and or from as is are was were be been its it this that anthropic claude company".split())

AGENT_META = {
  "scout-2021-2022": ("Timeline Scout · 2021–22", "scout"),
  "scout-2023": ("Timeline Scout · 2023", "scout"),
  "scout-2024": ("Timeline Scout · 2024", "scout"),
  "scout-2025h1": ("Timeline Scout · 2025 H1", "scout"),
  "scout-2025h2": ("Timeline Scout · 2025 H2", "scout"),
  "scout-2026q1": ("Timeline Scout · 2026 Q1", "scout"),
  "scout-2026q2": ("Timeline Scout · 2026 Q2", "scout"),
  "scout-2026q3": ("Timeline Scout · 2026 Q3", "scout"),
  "desk-deals": ("Deal Desk", "desk"),
  "desk-compute": ("Compute Desk", "desk"),
  "desk-product": ("Product Desk", "desk"),
  "desk-revenue": ("Revenue Desk", "desk"),
  "desk-governance": ("Governance & People Desk", "desk"),
  "desk-legal": ("Legal & Regulatory Desk", "desk"),
  "desk-ecosystem": ("Ecosystem Desk", "desk"),
  "desk-s1": ("Prospectus Desk", "desk"),
  "verify-capital": ("Source Re-deriver · Capital", "verify"),
  "verify-operating": ("Source Re-deriver · Operating", "verify"),
  "verify-prospectus": ("Source Re-deriver · Prospectus & Margins", "verify"),
  "verify-compute": ("Source Re-deriver · Compute & Prices", "verify"),
  "verify-audit-1": ("Record Auditor · 1", "verify"),
  "verify-audit-2": ("Record Auditor · 2", "verify"),
  "analyst-topic-capital": ("Analyst · Capital", "analysis"),
  "analyst-topic-revenue": ("Analyst · Revenue", "analysis"),
  "analyst-topic-compute": ("Analyst · Compute", "analysis"),
  "analyst-topic-product": ("Analyst · Product", "analysis"),
  "analyst-topic-moat": ("Analyst · Moat", "analysis"),
  "analyst-topic-governance": ("Analyst · Governance", "analysis"),
  "analyst-topic-legal": ("Analyst · Legal", "analysis"),
  "analyst-topic-government": ("Analyst · Policy", "analysis"),
  "analyst-topic-people": ("Analyst · People", "analysis"),
  "analyst-topic-ecosystem": ("Analyst · Ecosystem", "analysis"),
  "analyst-model": ("Financial Modeler", "model"),
  "analyst-compute": ("Compute Economist", "model"),
  "analyst-bull": ("Bull Analyst", "thesis"),
  "analyst-bear": ("Bear Analyst", "thesis"),
  "analyst-judge": ("Judge", "thesis"),
  "certifier": ("Certifier", "certify"),
  "orchestrator": ("Orchestrator", "orchestrator"),
}

def load_outputs():
    outs = {}
    for fn in sorted(glob.glob(os.path.join(OUT_DIR, "*.json"))):
        try:
            with open(fn) as f:
                d = json.load(f)
            aid = d.get("agent") or os.path.basename(fn)[:-5]
            outs[aid] = d
        except Exception as e:
            print(f"!! could not parse {fn}: {e}", file=sys.stderr)
    return outs

def parse_date(s):
    if not s: return None
    s = str(s).strip()
    for fmt in ("%Y-%m-%d", "%Y-%m", "%Y"):
        try: return datetime.strptime(s, fmt)
        except: pass
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", s)
    if m:
        try: return datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except: return None
    return None

def norm_url(u):
    if not u: return ""
    try:
        p = urlparse(u.strip())
        host = p.netloc.lower().replace("www.", "")
        path = p.path.rstrip("/")
        return f"{host}{path}".lower()
    except: return u.strip().lower()

def domain(u):
    try: return urlparse(u).netloc.lower().replace("www.", "")
    except: return ""

def tokens(s):
    s = re.sub(r"[^a-z0-9$%\. ]", " ", (s or "").lower())
    return {t for t in s.split() if t not in STOP and len(t) > 2}

def jaccard(a, b):
    if not a or not b: return 0.0
    return len(a & b) / len(a | b)

def num(x):
    try:
        if x is None or x == "": return None
        return float(x)
    except: return None

def normalize_event(e, agent):
    if not isinstance(e, dict):
        return None
    ev = dict(e)
    ev["agent"] = ev.get("agent") or agent
    d = parse_date(ev.get("date"))
    if not d:
        return None
    ev["date"] = d.strftime("%Y-%m-%d")
    ev.setdefault("date_precision", "day")
    cats = ev.get("category") or []
    if isinstance(cats, str): cats = [cats]
    cats = [c for c in cats if c in CATS] or ["other"]
    ev["category"] = cats
    src = ev.get("source") or {}
    if not isinstance(src, dict): src = {}
    src.setdefault("tier", "T4")
    if src.get("tier") not in TIER_RANK: src["tier"] = "T4"
    src["url"] = (src.get("url") or "").strip()
    if src["url"].startswith("file:"):
        # a licensed PitchBook extract held locally (git-ignored): keep the provenance, drop the local path
        m = re.search(r"deal ([0-9]+-[0-9]+T)", src.get("publisher") or "")
        src["local_extract"] = os.path.basename(src["url"]); src["url"] = f"pitchbook://deal/{m.group(1)}" if m else "pitchbook://licensed-extract"
    ev["source"] = src
    cor = ev.get("corroboration") or []
    ev["corroboration"] = [c for c in cor if isinstance(c, dict) and c.get("url")]
    ex = ev.get("extracted") or {}
    if not isinstance(ex, dict): ex = {}
    for k in ("amount_usd_m","valuation_post_usd_m","valuation_pre_usd_m","revenue_run_rate_usd_m","revenue_period_usd_m","margin_pct","headcount"):
        ex[k] = num(ex.get(k))
    ex.setdefault("compute", {}); ex.setdefault("product", {}); ex.setdefault("people", []); ex.setdefault("entities", []); ex.setdefault("other", {})
    if not isinstance(ex["entities"], list): ex["entities"] = []
    if not isinstance(ex["people"], list): ex["people"] = []
    ev["extracted"] = ex
    conf = (ev.get("confidence") or "MEDIUM").upper()
    ev["confidence"] = conf if conf in CONF_RANK else "MEDIUM"
    ev["headline"] = (ev.get("headline") or "").strip()[:140]
    ev["summary"] = (ev.get("summary") or "").strip()
    if not ev.get("id"):
        slug = re.sub(r"[^a-z0-9]+", "-", ev["headline"].lower())[:40].strip("-")
        ev["id"] = f"evt-{d.strftime('%Y%m%d')}-{slug}"
    return ev

class DSU:
    def __init__(self, n): self.p = list(range(n))
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]; x = self.p[x]
        return x
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b: self.p[b] = a

def is_dup(a, b):
    da, db = parse_date(a["date"]), parse_date(b["date"])
    dd = abs((da - db).days)
    ua, ub = norm_url(a["source"]["url"]), norm_url(b["source"]["url"])
    if ua and ua == ub and dd <= 45:
        return True
    if dd > 3: return False
    shared_cat = bool(set(a["category"]) & set(b["category"]))
    ta, tb = tokens(a["headline"] + " " + a["summary"]), tokens(b["headline"] + " " + b["summary"])
    j = jaccard(ta, tb)
    if j >= 0.45 and shared_cat: return True
    if j >= 0.30 and shared_cat:
        # same headline number (amount/valuation/run-rate) seals it
        for k in ("amount_usd_m", "valuation_post_usd_m", "revenue_run_rate_usd_m"):
            x, y = a["extracted"].get(k), b["extracted"].get(k)
            if x and y and abs(x - y) / max(x, y) < 0.02: return True
    if j >= 0.6: return True
    return False

def merge_cluster(members, conflicts_out):
    members = sorted(members, key=lambda e: (TIER_RANK[e["source"]["tier"]], CONF_RANK[e["confidence"]], -len(e["summary"])))
    prim = json.loads(json.dumps(members[0]))
    prim["agents"] = sorted({m["agent"] for m in members})
    prim["merged_ids"] = [m["id"] for m in members[1:]]
    seen = {norm_url(prim["source"]["url"])}
    cor = []
    for c in prim.get("corroboration", []):
        k = norm_url(c["url"])
        if k and k not in seen: seen.add(k); cor.append(c)
    for m in members[1:]:
        s = m["source"]
        k = norm_url(s.get("url"))
        if k and k not in seen:
            seen.add(k); cor.append({"url": s["url"], "publisher": s.get("publisher"), "title": s.get("title"), "tier": s.get("tier"), "agent": m["agent"]})
        for c in m.get("corroboration", []):
            k = norm_url(c["url"])
            if k and k not in seen: seen.add(k); cor.append(c)
    prim["corroboration"] = cor
    prim["category"] = sorted(set(sum([m["category"] for m in members], [])))
    # extracted: fill nulls in tier order; detect numeric conflicts
    ex = prim["extracted"]
    disputed = False
    for m in members[1:]:
        mex = m["extracted"]
        for k, v in mex.items():
            if k in ("compute", "product", "other") and isinstance(v, dict):
                ex.setdefault(k, {})
                for kk, vv in v.items():
                    if ex[k].get(kk) in (None, "", []) and vv not in (None, "", []): ex[k][kk] = vv
            elif k in ("people", "entities") and isinstance(v, list):
                have = {json.dumps(x, sort_keys=True) for x in ex.get(k, [])}
                for x in v:
                    if json.dumps(x, sort_keys=True) not in have: ex.setdefault(k, []).append(x)
            elif isinstance(v, (int, float)) and v is not None:
                cur = ex.get(k)
                if cur is None: ex[k] = v
                elif isinstance(cur, (int, float)) and cur and abs(cur - v) / max(abs(cur), abs(v)) > 0.10:
                    disputed = True
                    conflicts_out.append({"topic": f"{prim['headline']} · {k}", "value_a": cur, "source_a": prim["source"]["url"],
                                          "value_b": v, "source_b": m["source"]["url"], "note": f"cross-agent numeric mismatch ({prim['agent']} vs {m['agent']})", "event_id": prim["id"]})
            elif ex.get(k) in (None, "", []) and v not in (None, "", []):
                ex[k] = v
        if m.get("notes") and m["notes"] not in (prim.get("notes") or ""):
            prim["notes"] = ((prim.get("notes") or "") + " | " + m["notes"]).strip(" |")
    if disputed:
        prim["confidence"] = "DISPUTED"
    else:
        # independent corroboration upgrades confidence
        doms = {domain(prim["source"]["url"])} | {domain(c["url"]) for c in cor}
        doms.discard("")
        if len(doms) >= 2 and TIER_RANK[prim["source"]["tier"]] <= 2 and CONF_RANK[prim["confidence"]] > 1:
            prim["confidence"] = "HIGH"
    prim["independent_sources"] = len({domain(prim["source"]["url"])} | {domain(c["url"]) for c in cor} - {""})
    return prim

def build_events(outs, conflicts_out):
    raw = []
    for aid, d in outs.items():
        for e in d.get("events") or []:
            ne = normalize_event(e, aid)
            if ne: raw.append(ne)
    # sort by date for windowed comparison
    raw.sort(key=lambda e: e["date"])
    n = len(raw)
    dsu = DSU(n)
    for i in range(n):
        di = parse_date(raw[i]["date"])
        for j in range(i + 1, n):
            dj = parse_date(raw[j]["date"])
            if (dj - di).days > 45: break
            if is_dup(raw[i], raw[j]): dsu.union(i, j)
    clusters = defaultdict(list)
    for i in range(n): clusters[dsu.find(i)].append(raw[i])
    merged = [merge_cluster(ms, conflicts_out) for ms in clusters.values()]
    # ensure unique ids
    seen = {}
    for e in merged:
        base = e["id"]; k = base; i = 2
        while k in seen: k = f"{base}-{i}"; i += 1
        seen[k] = True; e["id"] = k
    merged.sort(key=lambda e: (e["date"], e["headline"]))
    return merged, n

def apply_corrections(events):
    """Apply agents/corrections.json (orchestrator corrections after the independent audit). Never edits agent outputs; records was/now on the event."""
    fn = os.path.join(ROOT, "agents", "corrections.json")
    if not os.path.exists(fn): return []
    try: cs = json.load(open(fn)).get("corrections", [])
    except Exception as ex:
        print("!! corrections.json unreadable:", ex, file=sys.stderr); return []
    alias = {}
    for e in events:
        alias[e["id"]] = e
        for mid in e.get("merged_ids", []): alias[mid] = e
    done = []
    # automatic rule: a valuation attached to an event that is not a financing is a reference mark (last round price, reported target), not that event's post-money
    fin = {"funding", "valuation", "debt"}
    for e in events:
        v = (e.get("extracted") or {}).get("valuation_post_usd_m")
        if v and not (fin & set(e["category"])):
            ex = e["extracted"]; ex.setdefault("other", {})["valuation_reference_usd_m"] = v; ex["valuation_post_usd_m"] = None
            chg = {"extracted.valuation_post_usd_m": {"was": v, "now": None}, "extracted.other.valuation_reference_usd_m": {"was": None, "now": v}}
            e.setdefault("corrections", []).append({"id": "R-VAL", "audit_id": None, "reason": "A valuation on an event that is not a financing is a reference mark (last round price or reported target), not this event's post-money. Moved to other.valuation_reference_usd_m.", "changed": chg})
            done.append({"id": "R-VAL", "audit_id": None, "event_id": e["id"], "headline": e["headline"], "reason": "Reference valuation moved out of the post-money field (event is not a financing).", "changed": list(chg)})
    for c in cs:
        e = alias.get(c.get("event_id"))
        if not e: print("!! correction", c.get("id"), "targets missing event", c.get("event_id"), file=sys.stderr); continue
        changed = {}
        for path, new in (c.get("set") or {}).items():
            cur = e; keys = path.split(".")
            for k in keys[:-1]:
                if not isinstance(cur.get(k), dict): cur[k] = {}
                cur = cur[k]
            changed[path] = {"was": cur.get(keys[-1]), "now": new}; cur[keys[-1]] = new
        if c.get("summary_replace"):
            a, b = c["summary_replace"]
            if a in e.get("summary", ""):
                changed["summary"] = {"was": e["summary"], "now": e["summary"].replace(a, b)}; e["summary"] = e["summary"].replace(a, b)
        e.setdefault("corrections", []).append({"id": c["id"], "audit_id": c.get("audit_id"), "reason": c.get("reason"), "changed": changed})
        done.append({"id": c["id"], "audit_id": c.get("audit_id"), "event_id": e["id"], "headline": e["headline"], "reason": c.get("reason"), "changed": list(changed)})
    return done

def build_metrics(events, outs):
    m = {"valuation": [], "run_rate": [], "period_revenue": [], "capital": [], "headcount": [], "compute": [], "pricing": [], "margins": [], "customers": []}
    for e in events:
        ex = e["extracted"]
        text = (e["headline"] + " " + e["summary"]).lower()
        talks = re.search(r"\b(in talks|talks to|reportedly seeking|seeking to raise|discussing|considering|weighs|could value|would value|target(s|ed)? valuation|secondary[- ]market|up to \$?\d+(\.\d+)? ?(b|t)\b.*(ipo|listing))\b", text)
        ipo_only = ("ipo" in e["category"]) and not ({"funding", "secondary"} & set(e["category"]))
        filing = re.search(r"\b(s-1|prospectus|confidential(ly)? (submit|fil))\b", text)
        if ex.get("valuation_post_usd_m") and not talks and not ipo_only and not filing and ({"funding", "valuation", "debt"} & set(e["category"])):   # a financing event; secondary-market marks live in the deals desk table
            m["valuation"].append({"date": e["date"], "usd_m": ex["valuation_post_usd_m"], "pre_usd_m": ex.get("valuation_pre_usd_m"), "label": e["headline"], "event_id": e["id"], "tier": e["source"]["tier"], "confidence": e["confidence"]})
        if ex.get("revenue_run_rate_usd_m") and e["source"]["tier"] in ("T1", "T2", "T3") and e["confidence"] in ("HIGH", "MEDIUM", "CANONICAL"):
            m["run_rate"].append({"date": e["date"], "usd_m": ex["revenue_run_rate_usd_m"], "event_id": e["id"], "tier": e["source"]["tier"], "confidence": e["confidence"], "source": e["source"]["url"]})
        if ex.get("headcount"):
            m["headcount"].append({"date": e["date"], "headcount": ex["headcount"], "event_id": e["id"], "tier": e["source"]["tier"]})
        if ex.get("amount_usd_m") and ({"funding", "debt"} & set(e["category"])) and not ({"compute", "acquisition", "investment", "legal"} & set(e["category"])):
            kind = "debt" if "debt" in e["category"] else "equity"
            m["capital"].append({"date": e["date"], "usd_m": ex["amount_usd_m"], "kind": kind, "label": e["headline"], "event_id": e["id"], "tier": e["source"]["tier"], "confidence": e["confidence"], "notes": e.get("notes")})
    # desk tables (richer, already structured)
    rv = outs.get("desk-revenue", {})
    m["run_rate_desk"] = rv.get("run_rate_series", [])
    m["period_revenue"] = rv.get("period_revenue", [])
    m["margins"] = rv.get("margin_and_loss", [])
    m["customers"] = rv.get("customer_metrics", [])
    m["mix"] = rv.get("mix", [])
    m["projections"] = rv.get("projections", [])
    m["comparables"] = rv.get("comparables", [])
    cp = outs.get("desk-compute", {})
    m["compute"] = (cp.get("compute_summary") or {}).get("rows", [])
    m["compute_totals"] = (cp.get("compute_summary") or {}).get("totals", {})
    m["compute_costs"] = (cp.get("compute_summary") or {}).get("cost_datapoints", [])
    pd_ = outs.get("desk-product", {})
    m["pricing"] = pd_.get("pricing_table", [])
    m["plans"] = pd_.get("plans_table", [])
    gv = outs.get("desk-governance", {})
    m["headcount_desk"] = gv.get("headcount_series", [])
    m["board"] = gv.get("board_history", [])
    m["ltbt"] = gv.get("ltbt", {})
    m["rsp"] = gv.get("rsp_versions", [])
    m["offices"] = gv.get("offices", [])
    m["people_moves"] = gv.get("people_moves", [])
    dl = outs.get("desk-deals", {})
    m["capital_summary"] = dl.get("capital_summary", {})
    lg = outs.get("desk-legal", {})
    m["cases"] = lg.get("cases", [])
    s1 = outs.get("desk-s1", {})
    m["prospectus_facts"] = s1.get("prospectus_facts", [])
    m["offering_structure"] = s1.get("offering_structure", {})
    m["risk_factor_themes"] = s1.get("risk_factor_themes", [])
    ec = outs.get("desk-ecosystem", {})
    m["market_share"] = ec.get("market_share", [])
    m["rounds"] = dl.get("rounds_table", [])
    for k in ("valuation", "run_rate", "headcount", "capital"):
        m[k].sort(key=lambda r: r["date"])
    # same valuation repeated within 200 days is a re-report of the same mark: keep the earliest
    dedup, last = [], {}
    for r in m["valuation"]:
        k = round(r["usd_m"] / 1000)
        prev = last.get(k)
        if prev and (parse_date(r["date"]) - parse_date(prev)).days <= 200:
            continue
        last[k] = r["date"]; dedup.append(r)
    m["valuation"] = dedup
    return m

def norm_name(n):
    n = re.sub(r"[^a-z0-9 ]", "", (n or "").lower())
    n = re.sub(r"\b(inc|corp|corporation|ltd|llc|plc|co|company|the|group|holdings|ventures|capital|management|partners)\b", "", n)
    return re.sub(r"\s+", " ", n).strip()

def build_entities(events, outs):
    ents = {}
    def add(name, types, public=None, ticker=None, note=None, event_id=None, amount=None, source=None, date=None, tier=None):
        if not name: return
        k = norm_name(name)
        if not k: return
        r = ents.setdefault(k, {"name": name.strip(), "types": set(), "public": None, "ticker": None, "notes": [], "event_ids": [], "amount_usd_m": None, "sources": [], "first_date": None, "tier": None})
        if len(name.strip()) < len(r["name"]) and name.strip(): r["name"] = name.strip()
        for t in (types or []): r["types"].add(t)
        if public is not None and r["public"] is None: r["public"] = bool(public)
        if ticker and not r["ticker"]: r["ticker"] = ticker
        if note and note not in r["notes"] and len(r["notes"]) < 4: r["notes"].append(note)
        if event_id and event_id not in r["event_ids"]: r["event_ids"].append(event_id)
        if amount and (r["amount_usd_m"] is None or amount > r["amount_usd_m"]): r["amount_usd_m"] = amount
        if source and source not in r["sources"] and len(r["sources"]) < 3: r["sources"].append(source)
        if date and (r["first_date"] is None or date < r["first_date"]): r["first_date"] = date
        if tier and (r["tier"] is None or TIER_RANK.get(tier, 9) < TIER_RANK.get(r["tier"], 9)): r["tier"] = tier
    ec = outs.get("desk-ecosystem", {})
    for r in ec.get("entities") or []:
        add(r.get("name"), r.get("types") or [], r.get("public"), r.get("ticker"), r.get("relationship_note"), None, num(r.get("amount_usd_m")), r.get("source_url"), r.get("first_date"), r.get("tier"))
        for eid in r.get("event_ids") or []: add(r.get("name"), [], event_id=eid)
    for e in events:
        for x in e["extracted"].get("entities") or []:
            if not isinstance(x, dict): continue
            t = x.get("type"); types = [t] if t else []
            add(x.get("name"), types, x.get("public"), x.get("ticker"), None, e["id"], None, e["source"]["url"], e["date"], e["source"]["tier"])
    out = []
    for k, r in ents.items():
        r["types"] = sorted(r["types"]) or ["partner"]
        r["degree"] = len(r["event_ids"])
        out.append(r)
    out.sort(key=lambda r: (-r["degree"], r["name"]))
    return out

def build_agent_log(outs, events):
    log = []
    agents = {}
    alias = {}
    for e in events:
        alias[e["id"]] = e["id"]
        for mid in e.get("merged_ids", []): alias[mid] = e["id"]
    def iso(dt): return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    all_start = None
    for aid, d in outs.items():
        st, fi = parse_iso(d.get("started")), parse_iso(d.get("finished"))
        if st and (all_start is None or st < all_start): all_start = st
    if all_start is None: all_start = datetime.utcnow()
    for aid, d in outs.items():
        role, wave = AGENT_META.get(aid, (d.get("role") or aid, "desk"))
        st, fi = parse_iso(d.get("started")), parse_iso(d.get("finished"))
        if not st: st = all_start
        if not fi or fi <= st: fi = st + timedelta(minutes=20)
        entries = d.get("log") or []
        n = max(len(entries), 1)
        span = (fi - st).total_seconds()
        agents[aid] = {"id": aid, "name": role, "wave": wave, "started": iso(st), "finished": iso(fi),
                       "stats": d.get("stats") or {}, "events": len(d.get("events") or []),
                       "conflicts": len(d.get("conflicts") or []), "open_items": len(d.get("open_items") or [])}
        log.append({"t": iso(st - timedelta(seconds=3)), "agent": "orchestrator", "type": "dispatch", "to": aid, "text": f"Dispatch {role}: brief issued, scope fenced, output contract attached."})
        for i, en in enumerate(entries):
            if not isinstance(en, dict): continue
            t = st + timedelta(seconds=span * (i + 1) / (n + 1))
            typ = (en.get("type") or "note").lower()
            if typ not in ("search", "open", "found", "flag", "verify", "message", "note"): typ = "note"
            eid = en.get("event_id")
            final = alias.get(eid) if eid else None
            rec = {"t": iso(t), "agent": aid, "type": typ, "text": (en.get("text") or "")[:300], "url": en.get("url"), "to": en.get("to"), "event_id": final or eid}
            if typ == "found" and final: rec["_final"] = final
            log.append(rec)
        s = d.get("stats") or {}
        parts = []
        if d.get("events"): parts.append(f"{len(d['events'])} events")
        if s.get("searches") is not None: parts.append(f"{s['searches']} searches")
        if s.get("pages_opened") is not None: parts.append(f"{s['pages_opened']} pages")
        if isinstance(d.get("topic"), dict) and d["topic"].get("evidence"): parts.append(f"{len(d['topic']['evidence'])} evidence ids cited")
        if s.get("claims_answered") is not None: parts.append(f"{s['claims_answered']} claims answered")
        if d.get("results"): parts.append(f"{len(d['results'])} items audited")
        if s.get("flags") is not None: parts.append(f"{s['flags']} flags")
        if d.get("conflicts"): parts.append(f"{len(d['conflicts'])} conflicts")
        log.append({"t": iso(fi), "agent": aid, "type": "done", "to": "orchestrator", "text": "Done: " + (", ".join(parts) or "output filed") + "."})
    for aid, (nm, wv) in AGENT_META.items():
        if aid not in agents and aid != "orchestrator":
            agents[aid] = {"id": aid, "name": nm, "wave": wv, "planned": True, "started": None, "finished": None, "stats": {}, "events": 0, "conflicts": 0, "open_items": 0}
    for r in log:
        if r.get("to") and r["to"] not in AGENT_META:
            r["to"] = "orchestrator"
    log.sort(key=lambda r: r["t"])
    seen_final = {}
    for i, r in enumerate(log):
        r["i"] = i
        f = r.pop("_final", None)
        if f:
            if f not in seen_final:
                seen_final[f] = r["agent"]; r["new"] = True        # first desk to put this event in the record
            else:
                r["new"] = False; r["confirms"] = seen_final[f]     # corroborates an event another desk already filed
    return {"generated": iso(datetime.utcnow()), "agents": agents, "log": log,
            "note": "Each entry is what the agent itself logged. Within one agent's run, timestamps are spread evenly between its recorded start and finish; start and finish are the agent's own clock readings."}

def write_timeline_csv(events):
    import csv
    cols = ["date", "headline", "summary", "source_url", "publisher", "source_tier", "confidence", "categories", "independent_sources",
            "amount_usd_m", "valuation_post_usd_m", "valuation_pre_usd_m", "revenue_run_rate_usd_m", "revenue_period_usd_m", "revenue_period",
            "margin_pct", "margin_type", "compute_partner", "compute_chips", "compute_gw", "compute_usd_m", "compute_term",
            "product_name", "product_type", "price_in_per_mtok", "price_out_per_mtok", "context_window",
            "governance", "moat", "strategy", "people", "entities", "headcount", "customers", "corroborating_urls", "notes", "found_by", "event_id"]
    with open(os.path.join(DATA, "timeline.csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f); w.writerow(cols)
        for e in sorted(events, key=lambda x: (x["date"], x["headline"])):
            x = e["extracted"]; cp = x.get("compute") or {}; pr = x.get("product") or {}
            w.writerow([e["date"], e["headline"], e["summary"], e["source"].get("url"), e["source"].get("publisher"), e["source"].get("tier"), e["confidence"],
                        "; ".join(e["category"]), e.get("independent_sources"), x.get("amount_usd_m"), x.get("valuation_post_usd_m"), x.get("valuation_pre_usd_m"),
                        x.get("revenue_run_rate_usd_m"), x.get("revenue_period_usd_m"), x.get("revenue_period"), x.get("margin_pct"), x.get("margin_type"),
                        cp.get("partner"), cp.get("chips"), cp.get("gw"), cp.get("usd_m"), cp.get("term"),
                        pr.get("name"), pr.get("type"), pr.get("price_in_per_mtok"), pr.get("price_out_per_mtok"), pr.get("context_window"),
                        x.get("governance"), x.get("moat"), x.get("strategy"),
                        "; ".join(f"{p.get('name')} ({p.get('role')}, {p.get('move')})" for p in x.get("people", []) if isinstance(p, dict)),
                        "; ".join(f"{p.get('name')}{' [' + p.get('ticker') + ']' if p.get('ticker') else ''} ({p.get('type')})" for p in x.get("entities", []) if isinstance(p, dict)),
                        x.get("headcount"), x.get("customers"), " | ".join(c.get("url", "") for c in e.get("corroboration", [])), e.get("notes"), ", ".join(e.get("agents", [e["agent"]])), e["id"]])

def parse_iso(s):
    if not s: return None
    try: return datetime.strptime(str(s)[:19], "%Y-%m-%dT%H:%M:%S")
    except: return None

def main():
    outs = load_outputs()
    if not outs:
        print("no agent outputs found"); return
    conflicts = []
    events, n_raw = build_events(outs, conflicts)
    applied = apply_corrections(events)
    metrics = build_metrics(events, outs)
    entities = build_entities(events, outs)
    alog = build_agent_log(outs, events)
    open_items, agent_conflicts = [], []
    for aid, d in outs.items():
        for c in d.get("conflicts") or []:
            c = dict(c); c["agent"] = aid; agent_conflicts.append(c)
        for o in d.get("open_items") or []:
            o = dict(o); o["agent"] = aid; open_items.append(o)
    tiers = defaultdict(int); confs = defaultdict(int); cats = defaultdict(int); years = defaultdict(int)
    for e in events:
        tiers[e["source"]["tier"]] += 1; confs[e["confidence"]] += 1; years[e["date"][:4]] += 1
        for c in e["category"]: cats[c] += 1
    ledger = {"generated": alog["generated"], "raw_events": n_raw, "merged_events": len(events),
              "tiers": dict(tiers), "confidence": dict(confs), "categories": dict(cats), "years": dict(sorted(years.items())),
              "opened_share": round(sum(1 for e in events if e["source"].get("opened")) / max(len(events), 1), 3),
              "cross_agent_conflicts": conflicts, "agent_conflicts": agent_conflicts, "open_items": open_items,
              "claims": [], "corrections": applied}
    id_map = {}
    for e in events:
        id_map[e["id"]] = e["id"]
        for mid in e.get("merged_ids", []): id_map[mid] = e["id"]
    json.dump(id_map, open(os.path.join(DATA, "id_map.json"), "w"), indent=0)
    def _load(fn):
        try: return json.load(open(os.path.join(DATA, fn)))
        except Exception: return None
    aud = _load("audit.json")
    if aud and aud.get("rows"):
        byid = {}
        for r in aud["rows"]:
            fid = id_map.get(r.get("event_id"), r.get("event_id"))
            byid[fid] = {k: r[k] for k in ("verdict", "note", "evidence", "figure_issues", "auditor", "audit_id", "orig_verdict") if r.get(k) not in (None, [], "")}
        for e in events:
            if e["id"] in byid: e["audit"] = byid[e["id"]]
    cl = _load("claims_ledger.json")
    if cl and cl.get("claims"):
        ledger["claims"] = cl["claims"]; ledger["claims_summary"] = cl.get("summary")
    write_timeline_csv(events)
    json.dump(events, open(os.path.join(DATA, "events.json"), "w"), indent=1, ensure_ascii=False)
    json.dump(metrics, open(os.path.join(DATA, "metrics.json"), "w"), indent=1, ensure_ascii=False)
    json.dump(entities, open(os.path.join(DATA, "entities.json"), "w"), indent=1, ensure_ascii=False)
    json.dump(alog, open(os.path.join(DATA, "agent_log.json"), "w"), indent=1, ensure_ascii=False)
    json.dump(ledger, open(os.path.join(DATA, "ledger.json"), "w"), indent=1, ensure_ascii=False)
    print(f"agents={len(outs)} raw={n_raw} merged={len(events)} entities={len(entities)} log={len(alog['log'])} "
          f"conflicts(cross)={len(conflicts)} conflicts(agent)={len(agent_conflicts)} open={len(open_items)}")
    print("tiers", dict(tiers)); print("confidence", dict(confs)); print("years", dict(sorted(years.items())))

if __name__ == "__main__":
    main()
