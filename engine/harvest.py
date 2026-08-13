"""Harvester: a repeatable sweep of a fixed source list per company.

Research stops being improvisation and becomes a walk down a written list.
Each company carries `companies/<slug>/sources.json`; the sweep fetches every
enabled entry, compares it against what was seen last time, and records one of
four outcomes per source:

    new         first time we have seen this source
    changed     content differs from the last retrieval
    unchanged   identical to last time
    unreachable could not be fetched (a visible gap, never a silent hole)

That last outcome is the point. A system that only records what it found
cannot tell you about a silence.

    python3 -m engine harvest <slug>     sweep one company
    python3 -m engine harvest --all      sweep the universe

The sweep is deterministic Python over public endpoints: SEC EDGAR's
submissions API and ordinary company pages. Structured providers and news
search run through the agent's tools in the scheduled session, and land in the
same evidence locker.
"""
from __future__ import annotations

import datetime as _dt
import json
import os
import re
import ssl
import urllib.error
import urllib.parse
import urllib.request

from . import evidence, store

UA = "HRPB Research Desk (harry5r14@gmail.com)"
TIMEOUT = 25
CA_BUNDLE = "/root/.ccr/ca-bundle.crt"

FREQ = ("daily", "weekly", "monthly")


# ------------------------------------------------------------------ manifest

def manifest_path(slug: str) -> str:
    return os.path.join(store.company_dir(slug), "sources.json")


def load_manifest(slug: str) -> dict:
    return store._read(manifest_path(slug), {})


def save_manifest(slug: str, m: dict) -> None:
    os.makedirs(store.company_dir(slug), exist_ok=True)
    store._write(manifest_path(slug), m)


# Candidate paths per source kind, tried in order. Sites disagree about where
# they put things; probing beats guessing once and logging 36 dead links.
CANDIDATES = [
    ("home", "other", ["/"]),
    ("newsroom", "newsroom", ["/news", "/newsroom", "/company/newsroom", "/press",
                              "/company/news", "/about/news", "/blog/category/news"]),
    ("blog", "blog", ["/blog", "/research", "/posts", "/news", "/blog/"]),
    ("pricing", "pricing", ["/pricing", "/plans", "/product/pricing", "/pricing/"]),
    ("careers", "careers", ["/careers", "/jobs", "/company/careers",
                            "/about/careers", "/careers/"]),
    ("about", "other", ["/about", "/company", "/about-us", "/company/about"]),
    ("docs", "docs", ["/docs", "/documentation", "/developers"]),
]


def _norm_domain(domain: str) -> str:
    d = (domain or "").strip().rstrip("/")
    if not d:
        return ""
    if not d.startswith("http"):
        d = "https://" + d
    return d


def default_sources(name: str, domain: str = None, cik: str = None,
                    probe: bool = False) -> list:
    """The starting source list. Boring pages first — pricing, careers and
    documentation move before press releases do.

    With probe=True each candidate path is fetched and only the first one that
    actually answers is kept, so a new company arrives with a working manifest
    instead of a page of dead links.
    """
    src = []
    if cik:
        c = str(cik).lstrip("CIK").lstrip("0").rjust(10, "0")
        src.append({"id": "sec-submissions", "name": "SEC EDGAR submissions",
                    "kind": "filing", "frequency": "daily", "enabled": True,
                    "url": f"https://data.sec.gov/submissions/CIK{c}.json",
                    "parser": "edgar"})
    d = _norm_domain(domain)
    if not d:
        return src

    for sid, kind, paths in CANDIDATES:
        chosen, ok = d + paths[0], not probe
        if probe:
            for p in paths:
                status, body, _ = fetch(d + p, timeout=12)
                if status == 200 and len(html_to_text(body)) > 400:
                    chosen, ok = d + p, True
                    break
        src.append({"id": sid, "name": f"{name} {sid}", "kind": kind,
                    "frequency": "daily", "enabled": bool(ok),
                    "url": chosen, "parser": "html"})
    return src


def reprobe(slug: str) -> dict:
    """Re-test an existing manifest's HTML sources and repoint or disable them."""
    m = load_manifest(slug)
    d = _norm_domain(m.get("domain"))
    if not d:
        return m
    by_id = {s.get("id"): s for s in (m.get("sources") or [])}
    fresh = default_sources(m.get("name") or slug, m.get("domain"),
                            m.get("cik"), probe=True)
    for s in fresh:
        old = by_id.get(s["id"])
        if old and old.get("parser") == "edgar":
            continue
        if old:
            old.update(url=s["url"], enabled=s["enabled"], kind=s["kind"])
        else:
            (m.setdefault("sources", [])).append(s)
    m["probed"] = evidence.now_utc()
    save_manifest(slug, m)
    return m


def ensure_manifest(slug: str, name: str = None, domain: str = None,
                    cik: str = None) -> dict:
    m = load_manifest(slug)
    if not m:
        m = {"slug": slug, "name": name or slug, "domain": domain, "cik": cik,
             "sources": default_sources(name or slug, domain, cik),
             "created": evidence.now_utc()}
        save_manifest(slug, m)
        return m
    changed = False
    for key, val in (("domain", domain), ("cik", cik), ("name", name)):
        if val and not m.get(key):
            m[key] = val
            changed = True
    if changed and not m.get("sources"):
        m["sources"] = default_sources(m.get("name") or slug, m.get("domain"),
                                       m.get("cik"))
    if changed:
        save_manifest(slug, m)
    return m


# --------------------------------------------------------------------- fetch

def _ctx():
    if os.path.exists(CA_BUNDLE):
        try:
            return ssl.create_default_context(cafile=CA_BUNDLE)
        except Exception:
            pass
    return ssl.create_default_context()


def fetch(url: str, timeout: int = TIMEOUT):
    """Returns (status, text, error). Never raises."""
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/json,application/xhtml+xml,*/*",
        "Accept-Encoding": "identity",
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=_ctx()) as r:
            raw = r.read(4_000_000)
            enc = r.headers.get_content_charset() or "utf-8"
            return int(r.status), raw.decode(enc, errors="replace"), None
    except urllib.error.HTTPError as e:
        return int(e.code), "", f"HTTP {e.code}"
    except Exception as e:
        return 0, "", f"{type(e).__name__}: {e}"


_TAG = re.compile(r"<[^>]+>")
_DROP = re.compile(r"<(script|style|noscript|svg)\b.*?</\1>", re.S | re.I)


def html_to_text(html: str) -> str:
    """Strip markup down to readable text. Good enough for change detection
    and for holding a quotable span; not a parser."""
    s = _DROP.sub(" ", html or "")
    s = re.sub(r"<br\s*/?>|</(p|div|li|h[1-6]|tr)>", "\n", s, flags=re.I)
    s = _TAG.sub(" ", s)
    for a, b in (("&nbsp;", " "), ("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"),
                 ("&quot;", '"'), ("&#39;", "'"), ("&rsquo;", "'")):
        s = s.replace(a, b)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n\s*\n+", "\n\n", s)
    return s.strip()


def edgar_to_text(payload: str) -> tuple:
    """Flatten an EDGAR submissions response to a filings list.
    Returns (text, latest_filing_date)."""
    try:
        d = json.loads(payload)
    except Exception:
        return payload[:20000], None
    rec = (d.get("filings") or {}).get("recent") or {}
    forms = rec.get("form") or []
    dates = rec.get("filingDate") or []
    docs = rec.get("primaryDocument") or []
    accs = rec.get("accessionNumber") or []
    lines = [f"{d.get('name', '')} — CIK {d.get('cik', '')}",
             f"SIC {d.get('sicDescription', '')}",
             f"{len(forms)} recent filings", ""]
    for i in range(min(len(forms), 60)):
        lines.append(f"{dates[i] if i < len(dates) else '?'}  {forms[i]}  "
                     f"{accs[i] if i < len(accs) else ''}  "
                     f"{docs[i] if i < len(docs) else ''}")
    return "\n".join(lines), (dates[0] if dates else None)


def resolve_cik(name: str):
    """Best-effort CIK lookup against EDGAR's company index."""
    status, body, _ = fetch("https://www.sec.gov/files/company_tickers.json")
    if status != 200 or not body:
        return None
    try:
        data = json.loads(body)
    except Exception:
        return None
    want = re.sub(r"[^a-z0-9]", "", (name or "").lower())
    if not want:
        return None
    for row in (data.values() if isinstance(data, dict) else data):
        title = re.sub(r"[^a-z0-9]", "", str(row.get("title", "")).lower())
        if title and (title == want or want in title or title in want):
            return str(row.get("cik_str", "")).rjust(10, "0")
    return None


# --------------------------------------------------------------------- sweep

def log_path(slug: str) -> str:
    return os.path.join(evidence.evidence_dir(slug), "harvest_log.json")


def load_log(slug: str) -> list:
    return store._read(log_path(slug), [])


def append_log(slug: str, run: dict, keep: int = 120) -> None:
    os.makedirs(evidence.evidence_dir(slug), exist_ok=True)
    log = load_log(slug)
    log.append(run)
    store._write(log_path(slug), log[-keep:])


def _last_hash(slug: str, url: str):
    best = None
    for row in evidence.load_index(slug):
        if row.get("url") == url:
            if best is None or (row.get("last_seen") or "") > (best.get("last_seen") or ""):
                best = row
    return best


def sweep(slug: str, only: str = None, quiet: bool = True) -> dict:
    """Walk one company's manifest. Returns the run record."""
    m = load_manifest(slug)
    started = evidence.now_utc()
    results = []

    for src in (m.get("sources") or []):
        if not src.get("enabled", True):
            continue
        if only and src.get("id") != only:
            continue
        url = src.get("url")
        if not url:
            continue

        status, body, err = fetch(url)
        row = {"id": src.get("id"), "name": src.get("name"), "kind": src.get("kind"),
               "url": url, "checked_at": evidence.now_utc(), "http": status}

        if err or status != 200 or not body:
            row.update(outcome="unreachable", error=err or f"HTTP {status}")
            results.append(row)
            continue

        as_of = None
        if src.get("parser") == "edgar":
            text, as_of = edgar_to_text(body)
        else:
            text = html_to_text(body)

        if not text.strip():
            row.update(outcome="unreachable", error="empty after extraction")
            results.append(row)
            continue

        prev = _last_hash(slug, url)
        h = evidence.text_hash(text)
        rec = evidence.record(slug, url=url, source_name=src.get("name") or url,
                              kind=src.get("kind") or "other", text=text,
                              title=src.get("name"), as_of=as_of)
        if prev is None:
            row.update(outcome="new")
        elif prev.get("hash") == h:
            row.update(outcome="unchanged")
        else:
            row.update(outcome="changed", previous_hash=prev.get("hash"),
                       previous_seen=prev.get("last_seen"),
                       delta_chars=len(text) - int(prev.get("chars", 0)))
        row.update(evidence_id=rec["id"], chars=len(text), as_of=as_of)
        results.append(row)

    counts = {}
    for r in results:
        counts[r["outcome"]] = counts.get(r["outcome"], 0) + 1
    run = {"slug": slug, "started_at": started, "finished_at": evidence.now_utc(),
           "sources": len(results), "counts": counts, "results": results}
    append_log(slug, run)
    if not quiet:
        print(f"{slug}: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    return run


def sweep_all(quiet: bool = False) -> list:
    runs = []
    uni = store.universe()
    entries = uni.get("companies", uni if isinstance(uni, list) else [])
    for ent in entries:
        slug = ent.get("slug")
        if not slug:
            continue
        if not load_manifest(slug):
            continue
        runs.append(sweep(slug, quiet=quiet))
    return runs


def status_all() -> list:
    """One row per company: manifest size and the most recent run."""
    out = []
    uni = store.universe()
    entries = uni.get("companies", uni if isinstance(uni, list) else [])
    for ent in entries:
        slug = ent.get("slug")
        if not slug:
            continue
        m = load_manifest(slug)
        log = load_log(slug)
        last = log[-1] if log else None
        out.append({
            "slug": slug,
            "sources": len([s for s in (m.get("sources") or []) if s.get("enabled", True)]),
            "has_manifest": bool(m),
            "last_run": last.get("finished_at") if last else None,
            "counts": last.get("counts") if last else {},
        })
    return out
