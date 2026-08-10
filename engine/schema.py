"""Company record schema: categories, source tiers, decay classes.

Every load-bearing value in the store is a Fact:
    {"value": ..., "as_of": "YYYY-MM-DD", "source": "...", "tier": "T1|T2|T3|T4",
     "decay": "VOLATILE|QUARTERLY|STABLE|PERMANENT", "flags": [...], "note": "..."}

Tiers (house convention): T1 = SEC/audited filings. T2 = company-announced /
PitchBook deal records. T3 = reputable media, single-source. T4 = weak/aggregator,
verify before use. Estimates carry flag "est.". Open checks carry flag "VERIFY".
Frozen conflicts carry flag "DISPUTED" and both values live in conflicts.json.
"""
from __future__ import annotations
import datetime as _dt

TIERS = ("T1", "T2", "T3", "T4")
DECAY = ("VOLATILE", "QUARTERLY", "STABLE", "PERMANENT")

# Days until a fact of each decay class is flagged stale. STABLE decays only on
# a new event (never auto-stale); PERMANENT never decays.
STALE_AFTER_DAYS = {"VOLATILE": 14, "QUARTERLY": 100}

# The category layout of profile.json. Order is presentation order.
# Each entry: key -> (label, default decay class for facts inside it).
CATEGORIES = {
    "identity":    ("Identity & Status", "STABLE"),
    "valuation":   ("Valuation & Marks", "VOLATILE"),
    "financing":   ("Capital Raised & Deals", "STABLE"),
    "financials":  ("Financials", "QUARTERLY"),
    "headcount":   ("Employees", "QUARTERLY"),
    "products":    ("Products & Revenue Lines", "QUARTERLY"),
    "customers":   ("Customers & Retention", "QUARTERLY"),
    "leadership":  ("Leadership & Key People", "STABLE"),
    "investors":   ("Investors", "STABLE"),
    "competition": ("Competitive Position", "QUARTERLY"),
    "deals_ma":    ("M&A / Acquisitions", "STABLE"),
    "ipo_status":  ("IPO / Listing Status", "VOLATILE"),
    "scores":      ("Internal Scores (AIBQ)", "QUARTERLY"),
    "events":      ("Dated Event Stream", "PERMANENT"),
    "triggers":    ("Named Triggers", "STABLE"),
}

REQUIRED_FACT_KEYS = {"value", "as_of", "source", "tier"}


def fact(value, as_of, source, tier, decay=None, flags=None, note=None):
    """Construct a well-formed Fact dict."""
    if tier not in TIERS:
        raise ValueError(f"bad tier {tier!r}")
    f = {"value": value, "as_of": as_of, "source": source, "tier": tier}
    if decay:
        if decay not in DECAY:
            raise ValueError(f"bad decay {decay!r}")
        f["decay"] = decay
    if flags:
        f["flags"] = list(flags)
    if note:
        f["note"] = note
    return f


def is_fact(obj) -> bool:
    return isinstance(obj, dict) and REQUIRED_FACT_KEYS.issubset(obj.keys())


def fact_age_days(f, today=None) -> int:
    today = today or _dt.date.today()
    try:
        return (today - _dt.date.fromisoformat(str(f["as_of"]))).days
    except (KeyError, ValueError):
        return 10 ** 6  # undated = maximally stale


def fact_is_stale(f, category_key, today=None) -> bool:
    decay = f.get("decay") or CATEGORIES.get(category_key, ("", "QUARTERLY"))[1]
    if decay in ("STABLE", "PERMANENT"):
        return False
    limit = STALE_AFTER_DAYS.get(decay)
    return limit is not None and fact_age_days(f, today) > limit


def tier_rank(t) -> int:
    """Lower is stronger. Unknown tiers rank weakest."""
    try:
        return TIERS.index(t)
    except ValueError:
        return len(TIERS)


def walk_facts(profile):
    """Yield (category, field_path, fact) for every Fact in a profile,
    descending into lists (ladders) and one level of nested dicts."""
    for cat in CATEGORIES:
        block = profile.get(cat)
        if not isinstance(block, dict):
            continue
        for field, v in block.items():
            if is_fact(v):
                yield cat, field, v
            elif isinstance(v, list):
                for i, item in enumerate(v):
                    if is_fact(item):
                        yield cat, f"{field}[{i}]", item
            elif isinstance(v, dict):
                for sub, sv in v.items():
                    if is_fact(sv):
                        yield cat, f"{field}.{sub}", sv
