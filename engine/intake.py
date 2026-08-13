"""Intake: everything arriving from outside, filed to the right company.

Three doors into the store, one router behind them:

    uploads/links.md         URLs you paste, one per line
    uploads/documents/       PDFs, decks, notes you drop in
    Gmail                    newsletters and analyst mail

Each item is classified against the coverage universe by counting company
mentions, archived into that company's evidence locker with a retrieval
timestamp, and — when it reads as a story — added to its news feed.

Gmail is an agent tool, not a Python one, so the sweep is run by the agent and
handed here through `ingest_email()`. URLs and documents are handled end to end
by `route_uploads()`.

Nothing is deleted and nothing is guessed at. An item the router cannot place
lands in `uploads/unfiled/` with its scores recorded, so a human can look.
"""
from __future__ import annotations

import datetime as _dt
import json
import os
import re
import shutil

from . import evidence, harvest, store


def company_root(slug):
    """The company's own folder. store.company_dir() points at its
    machine store one level deeper; the analyst drop zones sit here."""
    return os.path.join(store.COMPANIES, slug)

UPLOADS = os.path.join(store.REPO, "uploads")
UNFILED = os.path.join(UPLOADS, "unfiled")
LINKS = os.path.join(UPLOADS, "links.md")
DOCS = os.path.join(UPLOADS, "documents")
LOG = os.path.join(UPLOADS, "intake_log.json")

MIN_SCORE = 2          # mentions needed before a document is filed with confidence
STRONG_LEAD = 2        # winner must beat the runner-up by this much


# ---------------------------------------------------------------- classifying

def aliases_by_slug() -> dict:
    """Company -> the names it actually appears under in prose."""
    out = {}
    uni = store.universe()
    for ent in uni.get("companies", []):
        slug = ent.get("slug")
        if not slug:
            continue
        man = harvest.load_manifest(slug)
        al = list(man.get("aliases") or [])
        name = ent.get("name") or slug
        al.append(name)
        # "Cursor (Anysphere)" -> "Cursor", "Anysphere"
        al.append(re.sub(r"\s*\(.*?\)", "", name).strip())
        for m in re.findall(r"\((.*?)\)", name):
            al.append(m.strip())
        al.append(slug.replace("-", " "))
        seen, clean = set(), []
        for a in al:
            a = (a or "").strip().lower()
            if len(a) > 2 and a not in seen:
                seen.add(a)
                clean.append(a)
        out[slug] = clean
    return out


def score(text: str, alias_map: dict = None) -> list:
    """Rank companies by how often each is named. Returns [(slug, hits), ...]."""
    alias_map = alias_map or aliases_by_slug()
    t = (text or "").lower()
    if not t:
        return []
    rows = []
    for slug, al in alias_map.items():
        hits = 0
        for a in al:
            # word-boundary count so "ssi" does not match "assist"
            hits += len(re.findall(r"(?<![a-z0-9])" + re.escape(a) + r"(?![a-z0-9])", t))
        if hits:
            rows.append((slug, hits))
    rows.sort(key=lambda r: -r[1])
    return rows


def classify(text: str, alias_map: dict = None) -> dict:
    """Decide where an item belongs.

    Returns {slug, confidence, scores}. `confidence` is high when one company
    clearly dominates, low when it is a close call, and None when nothing in
    the universe is mentioned at all.
    """
    rows = score(text, alias_map)
    if not rows:
        return {"slug": None, "confidence": None, "scores": []}
    top = rows[0]
    second = rows[1][1] if len(rows) > 1 else 0
    if top[1] >= MIN_SCORE and (top[1] - second) >= STRONG_LEAD:
        conf = "high"
    elif top[1] >= MIN_SCORE:
        conf = "medium"
    else:
        conf = "low"
    return {"slug": top[0], "confidence": conf, "scores": rows[:6]}


# -------------------------------------------------------------------- logging

def _log(entry: dict) -> None:
    os.makedirs(UPLOADS, exist_ok=True)
    rows = store._read(LOG, [])
    rows.append(entry)
    store._write(LOG, rows[-500:])


# ------------------------------------------------------------------ ingestion

def ingest_text(slug, *, title, text, url=None, source_name=None, kind="manual",
                published=None, as_news=True, summary=None) -> dict:
    """File one piece of outside material into a company's evidence, and
    optionally its news feed. Returns the evidence record."""
    rec = evidence.record(
        slug, url=url or f"manual:{title[:60]}",
        source_name=source_name or "manual intake",
        kind=kind, text=text or "", title=title,
        as_of=(published or "")[:10] or None,
    )
    if as_news:
        harvest.merge_news(slug, [{
            "title": title, "url": url, "publisher": source_name,
            "published": published or evidence.now_utc(),
            "summary": (summary or (text or "")[:300]) or None,
        }], harvest.load_manifest(slug).get("aliases"))
    return rec


def ingest_email(*, subject, sender, date, body, thread_id=None,
                 alias_map=None) -> dict:
    """One newsletter or analyst email. Classified on subject plus body.

    Newsletters name many companies, so this files against the dominant one and
    records the full ranking; a digest touching five names is filed once and
    found by search under any of them.
    """
    verdict = classify(f"{subject}\n{body}", alias_map)
    slug = verdict["slug"]
    entry = {"kind": "email", "subject": subject, "sender": sender,
             "date": date, "thread_id": thread_id,
             "slug": slug, "confidence": verdict["confidence"],
             "scores": verdict["scores"], "at": evidence.now_utc()}
    if not slug:
        entry["outcome"] = "unfiled — no covered company named"
        _log(entry)
        return entry

    url = f"https://mail.google.com/mail/u/0/#inbox/{thread_id}" if thread_id else None
    rec = ingest_text(slug, title=subject, text=body, url=url,
                      source_name=(sender or "email").split("<")[0].strip(),
                      kind="press", published=date, as_news=True)
    entry["outcome"] = "filed"
    entry["evidence_id"] = rec["id"]
    _log(entry)

    # a digest naming several companies is cross-filed as evidence for each
    for other, hits in verdict["scores"][1:]:
        if hits >= MIN_SCORE:
            ingest_text(other, title=subject, text=body, url=url,
                        source_name=(sender or "email").split("<")[0].strip(),
                        kind="press", published=date, as_news=False)
            entry.setdefault("also_filed", []).append(other)
    return entry


def ingest_url(url: str, alias_map=None) -> dict:
    """Fetch a link, work out who it is about, archive it."""
    status, body, err = harvest.fetch(url)
    entry = {"kind": "url", "url": url, "at": evidence.now_utc(), "http": status}
    if err or status != 200 or not body:
        entry["outcome"] = f"unreachable: {err or status}"
        _log(entry)
        return entry

    text = harvest.html_to_text(body)
    m = re.search(r"<title[^>]*>(.*?)</title>", body, re.S | re.I)
    title = (m.group(1).strip() if m else url)[:220]
    verdict = classify(f"{title}\n{text[:6000]}", alias_map)
    entry.update(title=title, slug=verdict["slug"],
                 confidence=verdict["confidence"], scores=verdict["scores"])
    if not verdict["slug"]:
        entry["outcome"] = "unfiled — no covered company named"
        _log(entry)
        return entry

    host = re.sub(r"^www\.", "", (re.search(r"https?://([^/]+)", url) or
                                  re.match("", "")).group(1)) if "://" in url else None
    rec = ingest_text(verdict["slug"], title=title, text=text, url=url,
                      source_name=host or "web", kind="press", as_news=True)
    entry.update(outcome="filed", evidence_id=rec["id"])
    _log(entry)
    return entry


def _read_document(path: str) -> str:
    """Best-effort text from a dropped file. PDFs go through pdftotext when it
    is installed; everything else is read as text."""
    ext = os.path.splitext(path)[1].lower()
    if ext == ".pdf":
        out = path + ".txt"
        if shutil.which("pdftotext"):
            os.system(f'pdftotext -q "{path}" "{out}" 2>/dev/null')
            if os.path.exists(out):
                with open(out, encoding="utf-8", errors="replace") as fh:
                    txt = fh.read()
                os.remove(out)
                return txt
        return ""
    if ext in (".txt", ".md", ".csv", ".json", ".html", ".htm"):
        with open(path, encoding="utf-8", errors="replace") as fh:
            raw = fh.read()
        return harvest.html_to_text(raw) if ext in (".html", ".htm") else raw
    return ""


CATEGORY_HINTS = [
    ("filings", ("10-k", "10-q", "8-k", "s-1", "form d", "prospectus", "sec ")),
    ("financials", ("income statement", "balance sheet", "cash flow", "arr",
                    "run-rate", "revenue", "gross margin", "ebitda")),
    ("valuation-and-deals", ("term sheet", "post-money", "pre-money", "cap table",
                             "series ", "valuation", "round")),
    ("customers", ("customer", "case study", "deployment", "logo")),
    ("competition", ("competitor", "versus", "vs.", "market share", "landscape")),
    ("people", ("appointed", "hire", "chief", "board", "resign", "departure")),
    ("products", ("launch", "release", "feature", "product", "roadmap", "pricing")),
]


def guess_category(text: str) -> str:
    t = (text or "").lower()[:20000]
    best, bestn = "notes", 0
    for cat, words in CATEGORY_HINTS:
        n = sum(t.count(w) for w in words)
        if n > bestn:
            best, bestn = cat, n
    return best


def ingest_document(path: str, alias_map=None) -> dict:
    """Classify a dropped file, move it into the right company folder, and
    archive its text as evidence."""
    name = os.path.basename(path)
    text = _read_document(path)
    entry = {"kind": "document", "file": name, "at": evidence.now_utc(),
             "chars": len(text)}

    verdict = classify(f"{name}\n{text[:8000]}", alias_map)
    entry.update(slug=verdict["slug"], confidence=verdict["confidence"],
                 scores=verdict["scores"])

    if not verdict["slug"] or verdict["confidence"] == "low":
        os.makedirs(UNFILED, exist_ok=True)
        shutil.move(path, os.path.join(UNFILED, name))
        entry["outcome"] = "unfiled — moved to uploads/unfiled/"
        _log(entry)
        return entry

    slug = verdict["slug"]
    cat = guess_category(text or name)
    dest_dir = os.path.join(company_root(slug), cat)
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, name)
    shutil.move(path, dest)
    entry.update(category=cat, moved_to=os.path.relpath(dest, store.REPO))

    if text.strip():
        rec = ingest_text(slug, title=name, text=text,
                          url=f"file:{os.path.relpath(dest, store.REPO)}",
                          source_name="analyst upload", kind="manual",
                          as_news=False)
        entry["evidence_id"] = rec["id"]
    entry["outcome"] = "filed"
    _log(entry)
    return entry


# --------------------------------------------------------------------- router

def read_links() -> list:
    """URLs from uploads/links.md — bare lines, markdown links, or bullets."""
    if not os.path.exists(LINKS):
        return []
    with open(LINKS, encoding="utf-8") as fh:
        body = fh.read()
    urls = re.findall(r"https?://[^\s)\]>\"']+", body)
    seen, out = set(), []
    for u in urls:
        u = u.rstrip(".,;")
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


def mark_links_done(done: list) -> None:
    """Move processed URLs under an Ingested heading rather than deleting them."""
    if not os.path.exists(LINKS) or not done:
        return
    with open(LINKS, encoding="utf-8") as fh:
        body = fh.read()
    keep = []
    for line in body.splitlines():
        if any(u in line for u in done) and not line.strip().startswith("- ["):
            continue
        keep.append(line)
    stamp = _dt.date.today().isoformat()
    block = [f"\n## Ingested {stamp}"] + [f"- [x] {u}" for u in done]
    with open(LINKS, "w", encoding="utf-8") as fh:
        fh.write("\n".join(keep).rstrip() + "\n" + "\n".join(block) + "\n")


def route_uploads(quiet: bool = False) -> dict:
    """Process everything sitting in uploads/. Returns a summary."""
    alias_map = aliases_by_slug()
    os.makedirs(DOCS, exist_ok=True)
    results = {"links": [], "documents": []}

    for url in read_links():
        r = ingest_url(url, alias_map)
        results["links"].append(r)
        if not quiet:
            print(f"  link  {r.get('outcome','?'):<40} {r.get('slug') or '-':<14} {url[:60]}")
    done = [r["url"] for r in results["links"] if r.get("outcome") == "filed"]
    mark_links_done(done)

    for name in sorted(os.listdir(DOCS)):
        p = os.path.join(DOCS, name)
        if not os.path.isfile(p) or name.startswith("."):
            continue
        r = ingest_document(p, alias_map)
        results["documents"].append(r)
        if not quiet:
            print(f"  doc   {r.get('outcome','?'):<40} {r.get('slug') or '-':<14} "
                  f"{r.get('category') or '':<22} {name[:40]}")

    results["summary"] = {
        "links": len(results["links"]),
        "links_filed": sum(1 for r in results["links"] if r.get("outcome") == "filed"),
        "documents": len(results["documents"]),
        "documents_filed": sum(1 for r in results["documents"] if r.get("outcome") == "filed"),
    }
    return results


def recent(n: int = 40) -> list:
    return store._read(LOG, [])[-n:][::-1]
