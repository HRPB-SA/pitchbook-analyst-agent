#!/usr/bin/env python3
"""Deterministic Stage G check: fetch each cited URL raw and look for the quote.

Usage: python3 scripts/verify_links.py runs/<run_id>/pairs/<pair_id>

Reads verdict.json, writes verified_raw.json. Matching is on normalized text
(HTML stripped, entities unescaped, case/whitespace/quote-style/punctuation
folded). A quote containing "..." is split into fragments that must all appear,
in order. Statuses: found | not found | could not open. A "not found" on a page
that renders client-side is not conclusive; the verifier agent's result and the
orchestrator reconcile those.
"""
import html
import json
import re
import subprocess
import sys
from pathlib import Path

UA = "Mozilla/5.0 (compatible; dtf-link-verifier)"


def fetch(url):
    try:
        p = subprocess.run(["curl", "-sSL", "-m", "40", "-A", UA, "-w", "\n%{http_code}", url],
                           capture_output=True, timeout=60)
    except subprocess.TimeoutExpired:
        return None, "timeout"
    body, _, code = p.stdout.decode("utf-8", "replace").rpartition("\n")
    if p.returncode != 0 or not code.startswith("2"):
        return None, f"http {code or 'error'} rc={p.returncode}"
    return body, code


def norm(s):
    s = html.unescape(s)
    s = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", s) if "<" in s else s
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = s.lower().replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("–", "-").replace("—", "-").replace("₹", "rs ")
    s = re.sub(r"[^a-z0-9$%.]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def page_text(raw):
    # keep meta content attributes (og:description etc.) as page text too
    metas = " ".join(re.findall(r'content="([^"]{20,})"', raw))
    return norm(raw) + " " + norm(metas)


def check(text, quote):
    frags = [norm(f) for f in re.split(r"\.\.\.|…", quote) if norm(f)]
    pos = 0
    for f in frags:
        i = text.find(f.rstrip("."), pos)
        if i < 0:
            return False
        pos = i + len(f)
    return bool(frags)


def main():
    pair = Path(sys.argv[1])
    v = json.loads((pair / "verdict.json").read_text())
    cites = [c for c in v.get("evidence", []) if c.get("url")]
    cache, out = {}, []
    for c in cites:
        url = c["url"]
        if url not in cache:
            cache[url] = fetch(url)
        body, info = cache[url]
        if body is None:
            status = "could not open"
        else:
            q = c.get("quote", "")
            raw_hit = bool(q) and re.sub(r"\s+", " ", q.split("(")[0].strip()) in re.sub(r"\s+", " ", body)
            status = "found" if raw_hit or check(page_text(body), q) else "not found"
        out.append({"url": url, "quote": c.get("quote", ""), "tier": c.get("tier", ""),
                    "status": status, "note": info if body is None else ""})
    counts = {s: sum(o["status"] == s for o in out) for s in ("found", "not found", "could not open")}
    (pair / "verified_raw.json").write_text(json.dumps({"pair_id": v.get("pair_id"), "citations": out,
                                                        "counts": counts}, indent=2))
    print(pair.name, counts)


if __name__ == "__main__":
    main()
