"""Evidence locker: the raw material behind every fact.

A Fact records what we believe. An evidence record keeps what we actually
read: the archived text, where it came from, the exact moment it was
retrieved, and a hash of the content so a later change is detectable.

    companies/<slug>/evidence/index.json     one row per record
    companies/<slug>/evidence/raw/<id>.txt   the archived text

Every record carries `retrieved_at` as a full UTC timestamp. That is
deliberately distinct from a Fact's `as_of`, which is the vintage of the
information itself. A figure dated 2026-02-09 may have been retrieved today;
both dates matter and the dashboard shows both.

Records are deduplicated on (url, content hash): re-reading an unchanged page
updates `last_seen` rather than storing a second copy.
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import os
import re

from . import store

KINDS = ("filing", "newsroom", "pricing", "careers", "blog", "docs",
         "press", "structured", "manual", "other")


def now_utc() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds")


def evidence_dir(slug: str) -> str:
    return os.path.join(store.company_dir(slug), "evidence")


def _index_path(slug: str) -> str:
    return os.path.join(evidence_dir(slug), "index.json")


def _raw_path(slug: str, eid: str) -> str:
    return os.path.join(evidence_dir(slug), "raw", f"{eid}.txt")


def load_index(slug: str) -> list:
    return store._read(_index_path(slug), [])


def save_index(slug: str, idx: list) -> None:
    os.makedirs(evidence_dir(slug), exist_ok=True)
    store._write(_index_path(slug), idx)


def text_hash(text: str) -> str:
    return hashlib.sha256((text or "").encode("utf-8")).hexdigest()[:16]


def make_id(slug: str, url: str, h: str) -> str:
    stem = re.sub(r"[^a-z0-9]+", "-", (url or "").lower()).strip("-")[-40:]
    return f"{stem or 'src'}-{h[:8]}"


def record(slug, *, url, source_name, kind="other", text="", title=None,
           as_of=None, note=None, status="ok") -> dict:
    """Archive one retrieval. Returns the evidence record.

    Re-recording identical text for the same URL touches `last_seen` and
    increments `seen_count` instead of duplicating the archive.
    """
    idx = load_index(slug)
    h = text_hash(text)
    stamp = now_utc()

    for row in idx:
        if row.get("url") == url and row.get("hash") == h:
            row["last_seen"] = stamp
            row["seen_count"] = int(row.get("seen_count", 1)) + 1
            save_index(slug, idx)
            return row

    eid = make_id(slug, url, h)
    os.makedirs(os.path.join(evidence_dir(slug), "raw"), exist_ok=True)
    with open(_raw_path(slug, eid), "w", encoding="utf-8") as fh:
        fh.write(text or "")

    row = {
        "id": eid,
        "url": url,
        "source_name": source_name,
        "kind": kind if kind in KINDS else "other",
        "title": title,
        "retrieved_at": stamp,
        "last_seen": stamp,
        "seen_count": 1,
        "hash": h,
        "chars": len(text or ""),
        "as_of": as_of,
        "note": note,
        "status": status,
    }
    idx.append(row)
    save_index(slug, idx)
    return row


def get(slug: str, eid: str):
    for row in load_index(slug):
        if row.get("id") == eid:
            return row
    return None


def raw_text(slug: str, eid: str) -> str:
    return store._read_text(_raw_path(slug, eid)) if hasattr(store, "_read_text") \
        else _read_text(_raw_path(slug, eid))


def _read_text(path: str) -> str:
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return ""


def find_span(slug: str, eid: str, needle: str):
    """Locate a quoted span inside an archived record.

    Returns (start, end) or None. This is the check that makes a stored number
    defensible: the span must still exist and still read the way it did.
    """
    text = _read_text(_raw_path(slug, eid))
    if not text or not needle:
        return None
    i = text.find(needle)
    if i < 0:
        squash = lambda s: re.sub(r"\s+", " ", s).strip()
        flat, target = squash(text), squash(needle)
        j = flat.find(target)
        return (j, j + len(target)) if j >= 0 else None
    return (i, i + len(needle))


def quote(slug: str, eid: str, start: int, end: int, pad: int = 0) -> str:
    text = _read_text(_raw_path(slug, eid))
    return text[max(0, start - pad):min(len(text), end + pad)]


def stats(slug: str) -> dict:
    idx = load_index(slug)
    kinds, latest = {}, None
    for row in idx:
        kinds[row.get("kind", "other")] = kinds.get(row.get("kind", "other"), 0) + 1
        ts = row.get("retrieved_at")
        if ts and (latest is None or ts > latest):
            latest = ts
    return {
        "records": len(idx),
        "chars": sum(int(r.get("chars", 0)) for r in idx),
        "kinds": kinds,
        "latest_retrieval": latest,
    }
