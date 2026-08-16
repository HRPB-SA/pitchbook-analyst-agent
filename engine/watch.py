"""Read what was reported, compare it to what we hold, and say so.

The desk had Databricks at $188B while fourteen outlets carried $190B. The
headline was sitting in the news store the whole time. Nothing read it.

That is the gap this module closes. It reads every harvested headline and
every archived document, pulls out the figures they claim, and checks each
one against the figure the desk currently stands behind. Where they differ it
raises a signal, with the link, the date, the publisher, and the size of the
disagreement.

What it deliberately does not do is change the store. Adopting a figure needs
tier judgment, a freeze-on-conflict check, and a view on whether a round has
actually closed. Those are the analyst's calls and the store rules exist to
stop them being made by accident. A detector that quietly rewrote the record
would replace a visible error with an invisible one.

So: this finds and flags. A person decides. The point is that nothing
reported can sit unnoticed.
"""

from __future__ import annotations

import datetime as _dt
import json
import os
import re

from . import briefing, evidence, schema, store

SIGNALS_FILE = "signals.json"

# ---------------------------------------------------------------- extraction

_SCALE = {"trillion": 1000.0, "t": 1000.0,
          "billion": 1.0, "bn": 1.0, "b": 1.0,
          "million": 0.001, "mn": 0.001, "m": 0.001}

# A money amount in text: $190 billion, $190B, $5.5bn, US$190 billion.
_MONEY = r"(?:US)?\$\s?([\d,]+(?:\.\d+)?)\s?(trillion|billion|million|bn|mn|[tbm])\b"

# Each claim type is a keyword and the ways a headline puts a number near it.
# Anchoring on the keyword is what keeps "raises $5 billion at $190 billion
# valuation" from filing the $5B as a valuation.
CLAIMS = [
    {"concept": "valuation_bn", "label": "valuation", "unit": "$B",
     "patterns": [
         # "valued at $190B", and also "value the company at $2 trillion",
         # where a short object sits between the verb and the price
         rf"valu\w*\s+(?:\w+\s+){{0,3}}?(?:at|of|to)\s+"
         rf"(?:about\s+|around\s+|nearly\s+|over\s+)?{_MONEY}",
         rf"{_MONEY}\s+(?:post-money\s+)?valuation",
         rf"valuation\s+(?:of|at|to|reaches?|tops?|hits?)\s+(?:about\s+|around\s+)?{_MONEY}",
         rf"at\s+a\s+{_MONEY}\s+(?:post-money|pre-money|valuation)",
         # a price paid for the whole company is a valuation of it; the buyer
         # guard keeps the acquirer's own page clear of the target's price
         rf"{_MONEY}\s+(?:all-stock\s+|all-cash\s+)?"
         rf"(?:acquisition|takeover|buyout)",
         rf"(?:acquir\w+|buy\w*|purchas\w+)\s+(?:\w+\s+){{0,4}}?for\s+{_MONEY}",
     ]},
    {"concept": "run_rate_bn", "label": "revenue run-rate", "unit": "$B",
     "patterns": [
         rf"(?:run[- ]?rate|annualized revenue|annualised revenue|ARR)\s*"
         rf"(?:of|at|tops?|hits?|reaches?|passes?|surpass\w*|crosses?)?\s*{_MONEY}",
         rf"{_MONEY}\s+(?:in\s+)?(?:annual\s+recurring\s+revenue|run[- ]?rate|ARR)",
     ]},
    {"concept": "round_size_bn", "label": "round size", "unit": "$B",
     "patterns": [
         rf"rais\w+\s+(?:about\s+|around\s+|nearly\s+|over\s+|up to\s+)?{_MONEY}",
         rf"clos\w+\s+(?:a\s+|on\s+|its\s+)?{_MONEY}\s+(?:round|financing|funding)",
         rf"{_MONEY}\s+(?:funding\s+round|round|financing|raise)\b",
     ]},
]

_HEADCOUNT = re.compile(
    r"(?:headcount|employees|staff|workforce)\s*(?:of|is|at|:|to|now)?\s*"
    r"(?:about\s+|around\s+|over\s+|nearly\s+)?([\d,]{3,})"
    r"|([\d,]{3,})\s+(?:employees|staff members|full-time)", re.I)

# "BBVA scaled ChatGPT Enterprise to 100,000 employees" is a customer story on
# OpenAI's own feed. The number counts the people a product reached, not the
# people who work there. Reach and staff are different measurements that
# happen to be counted in the same unit.
_REACH = re.compile(
    r"\b(?:to|across|for|reaching|serving|covering|among)\s*$", re.I)


def _to_bn(amount: str, scale: str) -> float | None:
    try:
        n = float(amount.replace(",", ""))
    except ValueError:
        return None
    mult = _SCALE.get((scale or "").lower())
    return None if mult is None else round(n * mult, 4)


# How close the company's name must sit to a figure inside a long document
# before the figure can be said to be about that company. A press release or
# a filing discusses customers, rivals and the wider market; "70,000
# employees" in an OpenAI post about the labour market is not OpenAI's
# headcount. A human never makes that mistake because they read the sentence.
# This is the machine's version of reading the sentence.
NEAR = 220


def _about_company(text: str, start: int, end: int, aliases) -> bool:
    if not aliases:
        return True
    window = text[max(0, start - NEAR):end + NEAR].lower()
    return any(a.lower() in window for a in aliases if a)


def extract(text: str, aliases=None, require_near=False) -> list[dict]:
    """Every figure a piece of text claims, with the phrase it came from.

    Set require_near for long documents, where the company must be named
    beside the figure. Headlines from a feed already filtered to this company
    need no such test: the company is the subject of the sentence.
    """
    if not text:
        return []
    out = []

    def keep(m, concept, label, unit, value):
        if require_near and not _about_company(text, m.start(), m.end(), aliases):
            return
        if concept == "valuation_bn" and _company_is_buyer(text, aliases, m.start()):
            return
        out.append({"concept": concept, "label": label, "unit": unit,
                    "value": value, "quote": _tidy(m.group(0))})

    for claim in CLAIMS:
        for pat in claim["patterns"]:
            for m in re.finditer(pat, text, re.I):
                val = _to_bn(m.group(1), m.group(2))
                if val is None or val <= 0:
                    continue
                keep(m, claim["concept"], claim["label"], claim["unit"], val)
    for m in _HEADCOUNT.finditer(text):
        raw = m.group(1) or m.group(2)
        try:
            n = int((raw or "").replace(",", ""))
        except ValueError:
            continue
        # a bare four-digit number next to "workforce" is far more often a year
        if 1900 <= n <= 2100 and "," not in (raw or ""):
            continue
        if m.group(2) and _REACH.search(text[max(0, m.start() - 24):m.start()]):
            continue                       # rolled out to N employees
        if 50 <= n <= 5_000_000:
            keep(m, "employees", "headcount", "", n)
    # one reading per (concept, value) per document
    seen, uniq = set(), []
    for c in out:
        key = (c["concept"], c["value"])
        if key not in seen:
            seen.add(key)
            uniq.append(c)
    return uniq


# When a company is the buyer, the valuation in the headline is the seller's.
# "Anthropic in talks to buy Decart for $6 billion" is not a reading of
# Anthropic. Six outlets carried that story and every one of them would have
# been filed as a 99% collapse in Anthropic's value.
_AS_BUYER = re.compile(
    r"\b(?:to\s+)?(?:acquir\w+|buy|buys|buying|bought|purchase[sd]?|"
    r"invest\w*\s+in|back\w*|take[sn]?\s+a\s+stake|eyes?|pursu\w+)\b", re.I)


def _company_is_buyer(text: str, aliases, upto: int) -> bool:
    """Whether the company is named as the acquirer ahead of this figure.

    The window runs forward from the company's name through to the figure,
    because the buying verb sits between the two and is often the first word
    of the matched phrase itself.
    """
    low = (text or "").lower()
    for a in (aliases or []):
        if not a:
            continue
        for m in re.finditer(r"(?<!\w)" + re.escape(a.lower()) + r"(?!\w)", low):
            if m.end() > upto:
                break
            if _AS_BUYER.search(low[m.end():min(upto + 40, m.end() + 90)]):
                return True
    return False


def _tidy(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip())[:140]


# ----------------------------------------------------------------- comparison

# A headline that says "about $190 billion" against a held 189.6 is the same
# figure loosely stated. Below this the two readings are one number.
ROUNDING = 0.005         # 0.5%
# Above this the two readings are telling different stories whatever their age.
MATERIAL = 0.02          # 2%


LADDERS = {"valuation_bn": ("valuation", "valuation_ladder_bn"),
           "run_rate_bn": ("financials", "run_rate_ladder_bn"),
           "growth_pct": ("financials", "growth_yoy_pct_ladder"),
           "gross_margin_pct": ("financials", "gross_margin_pct_ladder"),
           "employees": ("headcount", "employees_ladder")}


def _in_history(profile, concept, value):
    """Whether the desk already holds this figure as a past mark.

    An outlet writing about April's round in April is not disagreeing with
    August's price. Cursor's ladder carries $29B and $50B alongside the $60B
    it was bought for; all three are correct, each for its own date. Only a
    figure the record does not already contain is worth anyone's attention.

    Matching here is looser than the rounding test, because headlines round:
    a story saying "$29B" of a $29.3B mark is naming that mark. The looseness
    is safe in this direction. It can only quiet a figure the ladder already
    holds; a genuinely new number matches nothing and still fires.
    """
    cat, field = LADDERS.get(concept, (None, None))
    if not cat:
        return None
    for f in (profile.get(cat) or {}).get(field) or []:
        v = f.get("value")
        if not isinstance(v, (int, float)) or not v:
            continue
        if abs((value - v) / abs(v)) < MATERIAL:
            return {"value": v, "as_of": f.get("as_of"), "source": f.get("source")}
    return None


def _declined(profile, value):
    """Whether the desk has already seen this figure and refused it.

    Three of the first four valuation disagreements this module raised were
    rounds that had been announced but not closed, which house ruling R2 says
    never anchor anything. The desk had already looked at each and written it
    down as not-adopted. Reporting those as open questions would train a
    reader to ignore the panel. Having decided is different from not knowing.
    """
    for cat, blk in profile.items():
        if not isinstance(blk, dict):
            continue
        for field, v in blk.items():
            for f in (v if isinstance(v, list) else [v]):
                if not schema.is_fact(f) or not briefing.blocked(f):
                    continue
                fv = f.get("value")
                if not isinstance(fv, (int, float)) or not fv:
                    continue
                if abs((value - fv) / abs(fv)) < MATERIAL:
                    return {"path": f"{cat}.{field}", "value": fv,
                            "as_of": f.get("as_of"), "note": f.get("note"),
                            "flags": f.get("flags") or []}
    return None


def _held(profile, concept):
    """What the desk currently stands behind, if anything."""
    fact, path = briefing.preferred(profile, concept)
    if not schema.is_fact(fact) or not isinstance(fact.get("value"), (int, float)):
        return None
    return {"value": float(fact["value"]), "as_of": fact.get("as_of"),
            "tier": fact.get("tier"), "source": fact.get("source"), "path": path}


def _verdict(claimed, held, reported_on=None):
    """How a reported figure stands against the one on file.

    Size of gap is the obvious test and it is not sufficient. The failure that
    prompted this module was $188B held against $190B reported: a 1.1% gap,
    small enough for any sane materiality threshold to wave through, and wrong
    all the same. Two precise figures are not a rounding of each other. What
    made $190B the right number was not that it was far from $188B but that it
    came later, from a completed round.

    So date carries as much weight as size. A figure reported after the one on
    file, differing by more than a rounding, is a signal whatever its size.
    """
    if held is None or not held["value"]:
        return "unheld", 0.0
    gap = (claimed - held["value"]) / abs(held["value"])
    if abs(gap) < ROUNDING:
        return "confirms", gap
    if abs(gap) >= MATERIAL:
        return "disagrees", gap
    held_on = (held.get("as_of") or "")[:10]
    if reported_on and held_on and reported_on > held_on:
        return "newer", gap
    return "drifts", gap


# --------------------------------------------------------------------- sweep

def scan(slug: str, days: int = 120) -> dict:
    """Compare everything reported lately against everything the desk holds."""
    profile = store.load_profile(slug)
    cutoff = (_dt.date.today() - _dt.timedelta(days=days)).isoformat()
    aliases = _aliases(slug)

    docs = []
    for n in _news(slug):
        when = (n.get("published") or n.get("first_seen") or "")[:10]
        if when and when < cutoff:
            continue
        # a feed carries stories about the whole sector; only the ones tagged
        # to this company can speak for it
        if not n.get("relevant"):
            continue
        docs.append({"text": " ".join(x for x in (n.get("title"), n.get("summary")) if x),
                     "url": n.get("url"), "publisher": n.get("publisher") or "press",
                     "when": when, "kind": "news", "near": False})
    feeds = _feeds(slug)
    for r in _evidence(slug):
        when = (r.get("last_seen") or r.get("retrieved_at") or "")[:10]
        if when and when < cutoff:
            continue
        # An archived feed is fifty stories in one file, so any company named
        # anywhere in it sits within reach of every figure in it. That is how
        # seven other companies' funding rounds came to be read as Scale AI's.
        # The individual stories are already in the news store, each tagged to
        # its own subject, so the feed itself has nothing to add.
        if _is_feed(r, feeds):
            continue
        # the archived document itself, not just its title: a filing or a press
        # release states the figure in its body
        body = ""
        try:
            body = evidence.raw_text(slug, r.get("id") or "")[:200_000]
        except Exception:
            body = ""
        docs.append({"text": f"{r.get('title') or ''} {body}",
                     "url": r.get("url"), "publisher": r.get("source_name") or "",
                     "when": when, "kind": r.get("kind") or "document", "near": True})

    # group claims by (concept, value), because fourteen outlets carrying the
    # same number is one story reported widely, not fourteen findings
    groups = {}
    for d in docs:
        for c in extract(d["text"], aliases, require_near=d.get("near")):
            key = (c["concept"], c["value"])
            g = groups.setdefault(key, {**c, "reports": [], "publishers": set(),
                                        "first": None, "last": None})
            g["reports"].append({"url": d["url"], "publisher": d["publisher"],
                                 "when": d["when"], "kind": d["kind"],
                                 "quote": c["quote"]})
            if d["publisher"]:
                g["publishers"].add(d["publisher"])
            if d["when"]:
                g["first"] = min(g["first"] or d["when"], d["when"])
                g["last"] = max(g["last"] or d["when"], d["when"])

    signals = []
    for (concept, value), g in groups.items():
        held = _held(profile, concept) if concept != "round_size_bn" else None
        verdict, gap = _verdict(value, held, g["last"])
        historic = _in_history(profile, concept, value)
        if historic and verdict in ("disagrees", "newer", "drifts", "unheld"):
            verdict = "history"
        declined = (_declined(profile, value)
                    if verdict in ("disagrees", "newer", "drifts", "unheld",
                                   "context") else None)
        if declined:
            verdict = "declined"
        # A round size has nothing to compare against, so it is only news when
        # it is recent. Report it as context rather than a disagreement.
        if concept == "round_size_bn":
            verdict, gap = "context", 0.0
        g["reports"].sort(key=lambda r: r["when"] or "", reverse=True)
        signals.append({
            "concept": concept, "label": g["label"], "unit": g["unit"],
            "claimed": value, "verdict": verdict,
            "gap_pct": round(gap * 100, 1),
            "held": held,
            "n_reports": len(g["reports"]),
            "n_publishers": len(g["publishers"]),
            "publishers": sorted(g["publishers"])[:8],
            "first_reported": g["first"], "last_reported": g["last"],
            "already_held_as": historic,
            "already_declined": declined,
            "reports": g["reports"][:6],
        })

    signals.sort(key=lambda s: (_RANK.get(s["verdict"], 9),
                                -s["n_publishers"],
                                -(s["last_reported"] or "") .__len__()))
    open_items = [s for s in signals
                  if s["verdict"] in ("disagrees", "newer", "unheld", "drifts")]
    out = {"slug": slug, "scanned_at": _dt.datetime.now(_dt.timezone.utc)
           .isoformat(timespec="seconds"),
           "window_days": days, "documents": len(docs),
           "signals": signals, "open": len(open_items),
           "needs_attention": [s for s in signals
                               if s["verdict"] in ("disagrees", "newer")]}
    _write(slug, out)
    return out


_RANK = {"disagrees": 0, "newer": 1, "unheld": 2, "drifts": 3,
         "context": 4, "declined": 5, "history": 6, "confirms": 7}


def _is_feed(record, feeds):
    """Whether an archived document is a feed rather than a single story.

    Matching on URL alone is not enough: a manifest's news query changes when
    an alias is added, and the archived copy keeps the address it was fetched
    under. Name and host are checked as well so an old capture is still
    recognised for what it is.
    """
    url, name = record.get("url") or "", record.get("source_name") or ""
    if url in feeds["urls"] or name in feeds["names"]:
        return True
    return "news.google.com" in url or "/rss" in url or url.endswith(".xml")


def _feeds(slug):
    man = store._read(os.path.join(store.company_dir(slug), "sources.json"), {})
    srcs = [s for s in (man.get("sources") or []) if s.get("parser") == "feed"]
    return {"urls": {s.get("url") for s in srcs},
            "names": {s.get("name") for s in srcs if s.get("name")}}


def _aliases(slug):
    man = store._read(os.path.join(store.company_dir(slug), "sources.json"), {})
    out = list(man.get("aliases") or [])
    name = (man.get("name") or "").replace(", Inc.", "").replace(" Inc.", "").strip()
    if name and name.lower() not in [a.lower() for a in out]:
        out.append(name)
    return out


def _news(slug):
    path = os.path.join(store.company_dir(slug), "evidence", "news.json")
    data = store._read(path, [])
    return data if isinstance(data, list) else []


def _evidence(slug):
    idx = evidence.load_index(slug)
    return idx if isinstance(idx, list) else []


def _write(slug, payload):
    path = os.path.join(store.company_dir(slug), SIGNALS_FILE)
    store._write(path, payload)


def load(slug: str) -> dict:
    return store._read(os.path.join(store.company_dir(slug), SIGNALS_FILE), {})


def scan_all(days: int = 120) -> list[dict]:
    out = []
    for entry in store.universe()["companies"]:
        out.append(scan(entry["slug"], days=days))
    return out


# -------------------------------------------------------------------- report

def render(result: dict) -> str:
    """The scan as something a person reads in the terminal."""
    lines = [f"{result['slug']}: {result['documents']} documents, "
             f"{len(result['signals'])} figures found, {result['open']} open"]
    for s in result["signals"]:
        if s["verdict"] in ("confirms", "history", "declined"):
            continue
        held = s["held"]
        held_txt = (f"held {held['value']:g} ({held['as_of']}, {held['tier']})"
                    if held else "nothing on file")
        gap = f"{s['gap_pct']:+.1f}%" if held else ""
        lines.append(f"  [{s['verdict']:<9}] {s['label']:<16} "
                     f"reported {s['claimed']:g}{s['unit']} by "
                     f"{s['n_publishers']} outlet(s) — {held_txt} {gap}")
        if s["reports"]:
            r = s["reports"][0]
            lines.append(f"      {r['when']} {r['publisher']}: \"{r['quote']}\"")
    return "\n".join(lines)
