#!/usr/bin/env python3
"""
CONTEXT: ANTHROPIC INTELLIGENCE DESK — mechanical health checks on the merged record (the Certifier's first pass).
Prints problems and writes data/health.json. Run: python3 scripts/health.py
"""
import json, os, re, collections
from datetime import datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = lambda n: json.load(open(os.path.join(ROOT, "data", n)))
E = D("events.json"); TODAY = "2026-09-30"
checks = []
def chk(name, bad, sev="WARN", sample=6):
    checks.append({"check": name, "count": len(bad), "severity": sev if bad else "OK", "sample": [str(b)[:160] for b in bad[:sample]]})

chk("event dated after today", [e["id"] for e in E if e["date"] > TODAY], "FAIL")
chk("event dated before 2021", [e["id"] for e in E if e["date"] < "2021-01-01"], "FAIL")
chk("no source URL", [e["id"] for e in E if not e["source"].get("url")], "FAIL")
chk("source URL not opened", [e["id"] for e in E if e["source"].get("opened") is False], "WARN")
chk("URL is not http(s) or a pitchbook:// field reference", [e["id"] for e in E if e["source"].get("url") and not e["source"]["url"].startswith(("http", "pitchbook://"))], "FAIL")
chk("source is a licensed PitchBook field with no public URL (not openable by a reader)", [e["id"] for e in E if e["source"].get("url", "").startswith("pitchbook://")], "INFO")
chk("summary missing or > 600 chars", [e["id"] for e in E if not e["summary"] or len(e["summary"]) > 600], "WARN")
chk("headline > 140 chars", [e["id"] for e in E if len(e["headline"]) > 140], "WARN")
chk("HIGH confidence but only T4/T5 source and no corroboration", [e["id"] for e in E if e["confidence"] == "HIGH" and e["source"]["tier"] in ("T4", "T5") and not e.get("corroboration")], "WARN")
chk("T1 source hosted on an aggregator domain", [e["id"] for e in E if e["source"]["tier"] == "T1" and re.search(r"wikipedia|crunchbase|sacra|forge|tipranks|kucoin", e["source"].get("url", ""))], "WARN")
chk("valuation present without an amount or round wording", [e["id"] for e in E if e["extracted"].get("valuation_post_usd_m") and not re.search(r"series|round|raise|valuation|tender|buyback|secondary|invest", (e["headline"] + e["summary"]).lower())], "WARN")
chk("run-rate above $150B (implausible)", [e["id"] for e in E if (e["extracted"].get("revenue_run_rate_usd_m") or 0) > 150000], "FAIL")
chk("PitchBook TTM 4Q2026/4Q2027 used as run-rate", [e["id"] for e in E if re.search(r"ttm 4q20(26|27)", (e["summary"] + (e.get("notes") or "")).lower()) and e["extracted"].get("revenue_run_rate_usd_m")], "WARN")
chk("DISPUTED events (frozen conflicts)", [e["id"] for e in E if e["confidence"] == "DISPUTED"], "INFO")
chk("VERIFY events (open checks)", [e["id"] for e in E if e["confidence"] == "VERIFY"], "INFO")
dup = collections.Counter(e["source"].get("url") for e in E if e["source"].get("url"))
chk("same URL is primary source of > 6 different events", [f"{u} x{n}" for u, n in dup.items() if n > 6], "INFO")
ids = collections.Counter(e["id"] for e in E)
chk("duplicate event ids", [i for i, n in ids.items() if n > 1], "FAIL")
chk("categories outside the schema", [e["id"] for e in E if not e["category"]], "FAIL")
by_year = collections.Counter(e["date"][:4] for e in E)
out = {"generated": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"), "events": len(E), "by_year": dict(sorted(by_year.items())), "checks": checks,
       "fails": sum(1 for c in checks if c["severity"] == "FAIL"), "warns": sum(1 for c in checks if c["severity"] == "WARN")}
json.dump(out, open(os.path.join(ROOT, "data", "health.json"), "w"), indent=1)
for c in checks:
    print(f"[{c['severity']:4s}] {c['count']:4d}  {c['check']}" + (f"   e.g. {c['sample'][:2]}" if c["count"] and c["severity"] in ("FAIL", "WARN") else ""))
print(f"fails={out['fails']} warns={out['warns']}")
