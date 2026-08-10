"""QA gates. Encodes the standing constraints so no report ships without them.

Severities:
  FAIL  blocks the build (exit nonzero): em-dashes, embargoed expressions,
        placeholders, empty required fields.
  WARN  surfaced in the QA report and the validation log; ship only with a
        deliberate override noted in the log: banned phrases, outlet names in
        report prose, figure-dense paragraphs with no visible source cue.

House basis:
  - Zero em-dashes (U+2014) anywhere in a shipped artifact.
  - The quality-valuation correlation coefficient is EMBARGOED: no r=-0.99,
    no score-vs-valuation scatter or fitted line. Per-point spread only.
  - Report prose names sources by kind (company disclosure, PitchBook,
    SEC EDGAR, press reports), not by outlet name; outlets belong in the
    validation log, not the artifact.
  - Banned filler per house style.
"""
from __future__ import annotations
import re

EM_DASH = "—"

EMBARGO_PATTERNS = [
    r"r\s*=\s*[-−]\s*0?\.99",
    r"correlation\s+(?:coefficient|statistic)[^.]{0,80}(?:AIBQ|quality|valuation)",
    r"(?:AIBQ|quality)[^.]{0,60}correlat",
]

PLACEHOLDER_PATTERNS = [
    r"\bTODO\b", r"\bTKTK\b", r"\bTBD\b", r"\bFIXME\b", r"XXXX", r"\blorem\b",
    r"\[(?:PLACEHOLDER|FILL|INSERT)[^\]]*\]",
]

BANNED_PHRASES = [
    "it's worth noting", "it is worth noting", "importantly,", "synergy",
    "going forward", "unlock", "dive into", "delve", "in conclusion",
    "at the end of the day", "game-changer", "cutting-edge",
]

OUTLET_NAMES = [
    "CNBC", "Bloomberg", "Reuters", "The Information", "TechCrunch", "Axios",
    "Business Insider", "Forbes", "Fortune", "WSJ", "Wall Street Journal",
    "Financial Times", "The Verge", "Benzinga",
]

_FIGURE = re.compile(r"[$€£]\s?\d|\d+(?:\.\d+)?%|\d+(?:\.\d+)?x\b")
_SOURCE_CUE = re.compile(
    r"\((?:company|PitchBook|SEC|EDGAR|press|derived|internal|T[1-4]\b|est\.?"
    r"|source|per |as of|[A-Z][a-z]+ \d{1,2}, \d{4}|\d{4})", re.IGNORECASE)


def check_text(text, where="", prose=True):
    """Returns list of {severity, rule, where, detail}."""
    issues = []

    def add(sev, rule, detail):
        issues.append({"severity": sev, "rule": rule, "where": where,
                       "detail": detail[:220]})

    if EM_DASH in text:
        i = text.index(EM_DASH)
        add("FAIL", "em-dash", f"U+2014 at offset {i}: ...{text[max(0, i-40):i+40]}...")
    for pat in EMBARGO_PATTERNS:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            add("FAIL", "embargo", f"embargoed expression: {m.group(0)!r}")
    for pat in PLACEHOLDER_PATTERNS:
        m = re.search(pat, text)
        if m:
            add("FAIL", "placeholder", f"{m.group(0)!r}")
    low = text.lower()
    for ph in BANNED_PHRASES:
        if ph in low:
            add("WARN", "banned-phrase", repr(ph))
    if prose:
        for outlet in OUTLET_NAMES:
            if re.search(rf"\b{re.escape(outlet)}\b", text):
                add("WARN", "outlet-name",
                    f"{outlet!r} in report prose; name sources by kind, outlet stays in the validation log")
        figs = _FIGURE.findall(text)
        if len(figs) >= 3 and not _SOURCE_CUE.search(text):
            add("WARN", "unsourced-figures",
                f"{len(figs)} figures with no visible source cue: {text[:90]}...")
    return issues


def check_blocks(blocks, where=""):
    """QA over a blocks list (see engine.compose for the grammar)."""
    issues = []
    for i, b in enumerate(blocks):
        kind = b[0]
        loc = f"{where}#{i}:{kind}"
        if kind in ("h1", "h2", "h3", "p"):
            issues += check_text(b[1], loc, prose=(kind == "p"))
        elif kind == "bullets":
            for j, item in enumerate(b[1]):
                issues += check_text(item, f"{loc}[{j}]")
        elif kind == "table":
            spec = b[1]
            cells = [spec.get("title", "")] + list(map(str, spec.get("header", [])))
            for row in spec.get("rows", []):
                cells += [str(c) for c in row]
            cells.append(spec.get("source", ""))
            for c in cells:
                issues += check_text(c, loc, prose=False)
        elif kind == "fig":
            issues += check_text(b[2], loc, prose=False)
    return issues


def check_docx(path):
    """Full-document scan of a rendered .docx (body, tables, headers/footers)."""
    import docx as _docx
    d = _docx.Document(path)
    issues = []
    texts = [p.text for p in d.paragraphs]
    for t in d.tables:
        for row in t.rows:
            for c in row.cells:
                texts.append(c.text)
    for s in d.sections:
        for part in (s.header, s.footer, s.first_page_header, s.first_page_footer):
            if part is not None:
                texts += [p.text for p in part.paragraphs]
    blob = "\n".join(texts)
    if EM_DASH in blob:
        issues.append({"severity": "FAIL", "rule": "em-dash", "where": path,
                       "detail": "U+2014 present in rendered document"})
    for pat in EMBARGO_PATTERNS:
        m = re.search(pat, blob, re.IGNORECASE)
        if m:
            issues.append({"severity": "FAIL", "rule": "embargo", "where": path,
                           "detail": m.group(0)})
    for pat in PLACEHOLDER_PATTERNS:
        m = re.search(pat, blob)
        if m:
            issues.append({"severity": "FAIL", "rule": "placeholder",
                           "where": path, "detail": m.group(0)})
    return issues


def gate(issues):
    """(ok, fails, warns)."""
    fails = [i for i in issues if i["severity"] == "FAIL"]
    warns = [i for i in issues if i["severity"] == "WARN"]
    return (not fails), fails, warns


def format_report(issues):
    if not issues:
        return "QA: clean. 0 FAIL / 0 WARN.\n"
    ok, fails, warns = gate(issues)
    L = [f"QA: {len(fails)} FAIL / {len(warns)} WARN.", ""]
    for i in fails + warns:
        L.append(f"[{i['severity']}] {i['rule']} @ {i['where']}: {i['detail']}")
    return "\n".join(L) + "\n"
