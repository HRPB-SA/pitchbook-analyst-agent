"""Parse PitchBook tool output into Facts without loading it into context.

PitchBook profile and deal responses run to tens of kilobytes of markdown. The
harness persists anything large to disk, so the agent can call the tool, let it
spill to a file, and have this module lift the handful of fields that matter.
That keeps a full-universe backfill affordable.

    python3 -m engine pbextract <slug> <response.txt> [--kind profile|deals]

Everything produced carries tier T2 and the retrieval date, because that is what
a PitchBook figure is: a vendor's record, good but not primary.
"""
from __future__ import annotations

import datetime as _dt
import json
import os
import re
import sys

FIELD = r"\*\*{}:\*\*\s*([^\n_]+?)(?:\s*_\(|$)"


def _one(text, label, cast=None):
    m = re.search(FIELD.format(re.escape(label)), text)
    if not m:
        return None
    v = m.group(1).strip().rstrip("*").strip()
    if v in ("", "N/A", "-"):
        return None
    if cast is None:
        return v
    try:
        return cast(v)
    except (TypeError, ValueError):
        return None


def _money_m(text, label):
    """PitchBook writes money as '$188000.0M' or '188000.0M'."""
    raw = _one(text, label)
    if not raw:
        return None
    m = re.search(r"\$?\s*([\d,]+(?:\.\d+)?)\s*M", raw)
    if not m:
        m = re.search(r"\$?\s*([\d,]+(?:\.\d+)?)", raw)
    if not m:
        return None
    try:
        return float(m.group(1).replace(",", ""))
    except ValueError:
        return None


def _fact(value, as_of, source, tier="T2", decay=None, note=None, flags=None):
    f = {"value": value, "as_of": as_of, "source": source, "tier": tier}
    if decay:
        f["decay"] = decay
    if note:
        f["note"] = note
    if flags:
        f["flags"] = flags
    return f


def parse_profile(text: str, today: str = None) -> dict:
    """Lift the fields a model and a profile page actually need."""
    today = today or _dt.date.today().isoformat()
    src = "PitchBook profile"
    out = {"identity": {}, "valuation": {}, "financing": {}, "financials": {},
           "headcount": {}, "competition": {}}

    name = _one(text, "Company Name")
    legal = _one(text, "Legal Name")
    desc = _one(text, "Short Description") or _one(text, "Description")
    founded = _one(text, "Year Founded", int)
    hq = _one(text, "Headquarters")
    website = _one(text, "Website")
    status = _one(text, "Business Status")
    own = _one(text, "Ownership Status")
    cik = _one(text, "CIK Code")
    contact = _one(text, "Primary Contact")
    title = _one(text, "Title")

    if name:
        out["identity"]["name"] = _fact(legal or name, today, src, decay="PERMANENT")
    if desc:
        out["identity"]["description"] = _fact(desc[:500], today, src, decay="STABLE")
    if founded:
        out["identity"]["founded"] = _fact(founded, today, src, decay="PERMANENT")
    if hq:
        out["identity"]["hq"] = _fact(hq, today, src, decay="STABLE")
    if website:
        out["identity"]["website"] = _fact(website, today, src, decay="STABLE")
    if status:
        out["identity"]["business_status"] = _fact(
            f"{status}; {own}" if own else status, today, src, decay="STABLE")
    if cik:
        out["identity"]["cik"] = _fact(cik, today, src, decay="PERMANENT")
    if contact:
        out["identity"]["primary_contact"] = _fact(
            f"{contact}{', ' + title if title else ''}", today, src, decay="STABLE")

    emp = _one(text, "Employees", lambda x: int(float(x.replace(",", ""))))
    emp_as_of = _one(text, "Employee Count As Of") or today
    if emp:
        out["headcount"]["employees_ladder"] = [
            _fact(emp, emp_as_of, src, decay="QUARTERLY")]

    lkv = _money_m(text, "Last Known Valuation")
    lkv_date = _one(text, "Last Known Valuation Date") or today
    lkv_type = _one(text, "Last Known Valuation Deal Type")
    last_status = _one(text, "Last Financing Status")
    if lkv:
        note = f"Deal type {lkv_type}." if lkv_type else None
        if last_status and "Announced" in last_status:
            note = ((note or "") + " Round is Announced/In Progress, not completed — "
                    "house ruling R2: an unclosed round never anchors the base case.").strip()
        out["valuation"]["pb_last_known_valuation_bn"] = _fact(
            round(lkv / 1000, 3), lkv_date, "PitchBook Last Known Valuation field",
            decay="VOLATILE", note=note,
            flags=["VERIFY"] if (last_status and "Announced" in last_status) else None)

    raised = _money_m(text, "Total Raised")
    if raised:
        out["financing"]["total_raised_bn"] = _fact(
            round(raised / 1000, 3), today, "PitchBook Total Raised field", decay="STABLE")
    inv = _one(text, "Active Investors", lambda x: int(float(x.replace(",", ""))))
    if inv:
        out["financing"]["active_investors"] = _fact(inv, today, src, decay="QUARTERLY")
    fin_status = _one(text, "Financing Status")
    if fin_status:
        out["financing"]["status"] = _fact(fin_status, today, src, decay="STABLE")
    note_txt = _one(text, "Financing Status Note")
    note_date = _one(text, "Financing Status Note Date") or today
    if note_txt:
        out["financing"]["pb_status_note"] = _fact(
            note_txt[:700], note_date, "PitchBook financing status note", decay="VOLATILE")

    rev = _money_m(text, "Revenue")
    period = _one(text, "Fiscal Period")
    if rev:
        out["financials"]["pb_revenue_field_bn"] = _fact(
            round(rev / 1000, 3), today, f"PitchBook Revenue field, {period or 'period n/a'}",
            decay="QUARTERLY",
            note="Ruling R3: PitchBook's revenue field is a forward-window projection, "
                 "NOT a run-rate. Never used as a run-rate print.")

    comp = _one(text, "Market Information")
    if comp:
        out["competition"]["pb_competitor_set"] = _fact(
            comp[:600], today, "PitchBook competitor set", tier="T3", decay="STABLE")

    return {k: v for k, v in out.items() if v}


DEAL_BLOCK = re.compile(r"# Deal Profile:.*?(?=# Deal Profile:|\Z)", re.S)


def parse_deals(text: str, today: str = None) -> dict:
    """Turn the financing history into a dated valuation ladder and a deal list.

    This is the backfill that matters: a company's own funding history is the
    one long time series a private company reliably has.
    """
    today = today or _dt.date.today().isoformat()
    deals = []
    for block in DEAL_BLOCK.findall(text):
        d = {
            "deal_id": _one(block, "Deal ID"),
            "date": _one(block, "Deal Date"),
            "size_m": _money_m(block, "Deal Size"),
            "type": _one(block, "Deal Type"),
            "status": _one(block, "Deal Status"),
            "round": _one(block, "VC Round"),
            "pre_m": _money_m(block, "Pre-Money Valuation"),
            "post_m": _money_m(block, "Post-Money Valuation"),
            "rev_mult": _one(block, "Valuation/Revenue"),
            "debt_m": _money_m(block, "Debt Raised in Round"),
            "raised_to_date_m": _money_m(block, "Raised to Date"),
            "ceo": _one(block, "CEO"),
        }
        if d["date"]:
            deals.append(d)
    deals.sort(key=lambda d: d["date"])

    out = {"financing": {}, "valuation": {}}
    ladder = []
    for d in deals:
        if d["post_m"] and d["status"] and d["status"].lower().startswith("comp"):
            ladder.append(_fact(
                round(d["post_m"] / 1000, 3), d["date"],
                f"PitchBook deal {d['deal_id']} ({d['type']})", decay="STABLE",
                note=f"{d['round']}; deal size ${d['size_m']:,.0f}M" if d["size_m"] else d["round"]))
    if ladder:
        out["valuation"]["valuation_ladder_bn"] = ladder

    completed = [d for d in deals if (d["status"] or "").lower().startswith("comp")]
    if completed:
        last = completed[-1]
        out["financing"]["last_completed_deal"] = _fact(
            f"{last['type']} {('$%.0fM' % last['size_m']) if last['size_m'] else ''} "
            f"({last['round'] or 'round n/a'})".strip(),
            last["date"], f"PitchBook deal {last['deal_id']}", decay="STABLE")
        if last.get("raised_to_date_m"):
            out["financing"]["raised_to_date_bn"] = _fact(
                round(last["raised_to_date_m"] / 1000, 3), last["date"],
                f"PitchBook Raised to Date, deal {last['deal_id']}", decay="STABLE")

    if deals:
        out["financing"]["deal_history"] = _fact(
            "; ".join(f"{d['date']} {d['type']}"
                      + (f" ${d['size_m']:,.0f}M" if d["size_m"] else "")
                      + (f" @ ${d['post_m']/1000:,.1f}B post" if d["post_m"] else "")
                      for d in deals[-12:]),
            today, "PitchBook deal history", decay="STABLE",
            note=f"{len(deals)} tracked deals.")
    return {k: v for k, v in out.items() if v}


def merge_dicts(*parts) -> dict:
    """Combine parsed blocks, ladders concatenated rather than overwritten."""
    out = {}
    for p in parts:
        for cat, block in (p or {}).items():
            tgt = out.setdefault(cat, {})
            for k, v in block.items():
                if isinstance(v, list) and isinstance(tgt.get(k), list):
                    tgt[k].extend(v)
                else:
                    tgt[k] = v
    return out


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    slug, path = argv[0], argv[1]
    kind = "profile"
    if "--kind" in argv:
        kind = argv[argv.index("--kind") + 1]
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    text = text.replace("\\n", "\n")
    parsed = parse_profile(text) if kind == "profile" else parse_deals(text)
    n = sum(len(v) if isinstance(v, dict) else 1 for v in parsed.values())
    print(json.dumps(parsed, indent=1)[:400])
    print(f"... {n} field groups parsed for {slug} from {os.path.basename(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
