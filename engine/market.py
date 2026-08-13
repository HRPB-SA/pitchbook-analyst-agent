"""Market and signal layer: the world around the coverage universe.

Two halves, because two different things go stale at two different speeds.

**Quotes** come from Morningstar, which is an agent tool rather than a Python
one, so the daily routine pulls them and hands them here through
`save_quotes()`. Each row keeps its retrieval timestamp; nothing is displayed
without one.

**Themes** are news feeds on the subjects that move this coverage — funding,
compute, regulation, listings, enterprise adoption, safety. Those are pure
Python and sweep on the same schedule as the company harvest.

The watchlist is deliberately the AI complex rather than the whole market: the
public names that are customers, suppliers, competitors or comparables for the
private companies being tracked. A reader should be able to look at this tab
and know what the listed proxies did today.
"""
from __future__ import annotations

import os

from . import evidence, harvest, store

MARKET = os.path.join(store.REPO, "market")
QUOTES = os.path.join(MARKET, "quotes.json")
THEMES = os.path.join(MARKET, "themes.json")

# Morningstar investment IDs, resolved once via the ID lookup tool.
WATCHLIST = [
    {"ticker": "NVDA", "name": "NVIDIA", "mid": "0P000003RE",
     "why": "Supplies the chips every AI company depends on."},
    {"ticker": "MSFT", "name": "Microsoft", "mid": "0P000003MH",
     "why": "Anthropic and OpenAI partner; Databricks reseller and rival."},
    {"ticker": "GOOGL", "name": "Alphabet", "mid": "0P000002HD",
     "why": "Frontier competitor and cloud supplier to several of the group."},
    {"ticker": "AMZN", "name": "Amazon", "mid": "0P000000B7",
     "why": "Largest cloud provider; Anthropic investor and compute partner."},
    {"ticker": "META", "name": "Meta", "mid": "0P0000W3KZ",
     "why": "Open-weight competitor; holds a large stake in Scale AI."},
    {"ticker": "CRWV", "name": "CoreWeave", "mid": "0P0001UXT9",
     "why": "In coverage, and the only one that files publicly."},
    {"ticker": "SNOW", "name": "Snowflake", "mid": "0P0001KOSA",
     "why": "The listed comparable for Databricks."},
    {"ticker": "PLTR", "name": "Palantir", "mid": "0P0001KOSE",
     "why": "The market's reference point for what enterprise AI is worth."},
    {"ticker": "AMD", "name": "AMD", "mid": "0P0000006A",
     "why": "The alternative to NVIDIA; a proxy for compute competition."},
    {"ticker": "TSM", "name": "TSMC", "mid": "0P000005AR",
     "why": "Manufactures nearly every advanced AI chip. A single point of failure."},
]

DATAPOINTS = {
    "ST157": "last_close", "PD003": "day_pct", "ST159": "market_cap_mm",
    "ST415": "price_to_sales", "OS603": "price_to_fair_value",
    "LT181": "moat", "ST569": "below_52w_high_pct",
}

# Themes worth a standing feed. One focus per query.
THEME_FEEDS = [
    ("funding", "AI startup funding round",
     "Where private capital is going this week."),
    ("compute", "AI data center compute chips shortage",
     "The supply side: chips, power and capacity."),
    ("regulation", "AI regulation policy law",
     "Rules that could change what these companies may sell."),
    ("listings", "AI company IPO filing",
     "The exit window, which is what a private mark ultimately depends on."),
    ("enterprise", "enterprise AI adoption spending",
     "Whether businesses are actually paying for this."),
    ("safety", "AI safety model evaluation risk",
     "Research and incidents that shape the regulatory mood."),
    ("markets", "stock market AI selloff rally technology shares",
     "How the listed proxies are trading."),
]


# -------------------------------------------------------------------- quotes

def save_quotes(rows: list) -> str:
    """Persist a Morningstar pull. `rows` is a list of dicts keyed by the names
    in DATAPOINTS, plus ticker and name."""
    os.makedirs(MARKET, exist_ok=True)
    payload = {"retrieved_at": evidence.now_utc(),
               "source": "Morningstar (last close; not live intraday)",
               "quotes": rows}
    store._write(QUOTES, payload)
    return QUOTES


def parse_morningstar(result: dict) -> list:
    """Turn the Morningstar data tool's response into watchlist rows."""
    by_mid = {w["mid"]: w for w in WATCHLIST}
    out = []
    for mid, blob in (result or {}).items():
        meta = by_mid.get(mid)
        if not meta:
            continue
        row = {"ticker": meta["ticker"], "name": meta["name"],
               "why": meta["why"], "mid": mid}
        for v in blob.get("values", []):
            key = DATAPOINTS.get(v.get("datapointId"))
            if not key:
                continue
            raw = v.get("value")
            try:
                row[key] = float(raw)
            except (TypeError, ValueError):
                row[key] = raw
        out.append(row)
    order = {w["ticker"]: i for i, w in enumerate(WATCHLIST)}
    out.sort(key=lambda r: order.get(r["ticker"], 99))
    return out


def load_quotes() -> dict:
    return store._read(QUOTES, {})


# -------------------------------------------------------------------- themes

def sweep_themes(quiet: bool = True) -> dict:
    """Pull each standing theme feed. Pure Python; runs with the harvest."""
    os.makedirs(MARKET, exist_ok=True)
    existing = store._read(THEMES, {})
    stamp = evidence.now_utc()
    out = {"retrieved_at": stamp, "themes": []}

    for key, query, why in THEME_FEEDS:
        url = harvest.google_news_url(query, query)
        status, body, err = harvest.fetch(url, timeout=20)
        prev = next((t for t in existing.get("themes", []) if t["key"] == key), {})
        seen = {i.get("title") for i in prev.get("items", [])}

        if status != 200 or not body:
            out["themes"].append({**prev, "key": key, "query": query, "why": why,
                                  "error": err or f"HTTP {status}",
                                  "checked_at": stamp})
            if not quiet:
                print(f"  ! {key:<12} {err or status}")
            continue

        items = harvest.parse_feed(body, key)[:24]
        fresh = sum(1 for i in items if i.get("title") not in seen)
        out["themes"].append({
            "key": key, "query": query, "why": why, "checked_at": stamp,
            "count": len(items), "new": fresh,
            "items": [{"title": i["title"], "url": i["url"],
                       "publisher": i["publisher"], "published": i["published"]}
                      for i in items],
        })
        if not quiet:
            print(f"  + {key:<12} {len(items)} items, {fresh} new")

    store._write(THEMES, out)
    return out


def load_themes() -> dict:
    return store._read(THEMES, {})


def summary() -> dict:
    """Headline numbers for the dashboard's market tab."""
    q = load_quotes()
    rows = q.get("quotes", [])
    movers = sorted([r for r in rows if isinstance(r.get("day_pct"), (int, float))],
                    key=lambda r: -abs(r["day_pct"]))
    up = [r for r in rows if isinstance(r.get("day_pct"), (int, float)) and r["day_pct"] > 0]
    themes = load_themes()
    return {
        "retrieved_at": q.get("retrieved_at"),
        "source": q.get("source"),
        "n": len(rows),
        "advancing": len(up),
        "declining": len(rows) - len(up),
        "biggest_move": movers[0] if movers else None,
        "themes_retrieved_at": themes.get("retrieved_at"),
        "n_themes": len(themes.get("themes", [])),
    }
