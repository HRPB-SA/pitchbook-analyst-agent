"""QA gates. Encodes the standing constraints so no report ships without them.

Severities:
  FAIL  blocks the build (exit nonzero): em-dash budget breach, embargoed
        expressions, placeholders.
  WARN  surfaced in the QA report and the validation log; ship only with a
        deliberate override noted in the log: banned phrases, adjective noise,
        outlet names in report prose, figure-dense paragraphs with no visible
        source cue.

House basis (README.md + style/Institutional_Research_Style_Guide.pdf):
  - Em-dashes (U+2014) SPARINGLY: more than 2 in one block is a WARN; more
    than EM_DASH_BUDGET in a document FAILs the build.
  - The quality-valuation coefficient is EMBARGOED: no r=-0.99, no
    score-vs-valuation scatter or fitted line. Per-point spread only.
  - Report prose names sources by kind (company disclosure, PitchBook,
    SEC EDGAR, press reports), not by outlet name; outlets belong in the
    References section and the validation log.
  - Throat-clearing and filler banned per the style guide; emphasis
    adjectives flagged: delete the adjective, insert the metric.
"""
from __future__ import annotations
import re

EM_DASH = "—"
EM_DASH_BUDGET = 8          # per document; "sparingly", not "never"
EM_DASH_BLOCK_LIMIT = 2     # per block; more reads as a tic

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
    "it's worth noting", "it is worth noting", "it is important to note",
    "importantly,", "furthermore", "synergy", "going forward", "unlock",
    "dive into", "delve", "in conclusion", "at the end of the day",
    "game-changer", "cutting-edge", "paradigm shift", "robust",
]

# Style guide rule 2: adjectives project uncertainty; the metric carries the
# emphasis. Flagged so the writer swaps the adjective for the number.
NOISE_ADJECTIVES = [
    "massive", "significant", "significantly", "drastic", "drastically",
    "huge", "enormous", "tremendous", "incredible", "remarkable",
    "impressive", "staggering", "explosive",
]

# Kent's weasels: words that carry no evaluative weight (WRITING_STYLES_RESEARCH.md).
WEASELS = ["apparently", "seemingly", "supposedly", "arguably"]

# Trading-desk slang; report prose writes for the PitchBook reader (STYLE.md
# vocabulary table). Word-boundary regexes keyed to the suggestion shown.
JARGON = [
    (re.compile(r"\bmarks?\b(?!\s+a\b)"), "'mark': write 'valuation' / 'the completed round valued the company at'"),
    (re.compile(r"\bprints?\b"), "'print': write 'disclosure' / 'reported figures' / 'update'"),
    (re.compile(r"\bthe tape\b"), "'the tape': write 'trading' / 'market prices'"),
    (re.compile(r"\bre-rat(?:e|es|ed|ing)\b"), "'re-rate': write 're-price' / 'put a higher price on'"),
    (re.compile(r"\bthe Street\b"), "'the Street': write 'analysts' / 'consensus'"),
]

# Boosters flag the least-supported claim (Hyland via Pinker).
BOOSTERS = ["clearly", "obviously", "undoubtedly", "of course", "needless to say"]

# Vague attributions: name the source kind and date instead.
VAGUE_ATTRIBUTIONS = [
    "observers note", "observers have", "some argue", "some say",
    "critics say", "many believe", "industry reports suggest",
    "it is widely", "widely seen as", "experts say", "sources say",
]

# AI-tell vocabulary (Signs of AI writing); each violates an older rule.
AI_TELLS = [
    "pivotal", "underscore", "underscores", "underscoring", "tapestry",
    "intricate", "serves as a", "stands as a", "boasts", "marking a shift",
    "highlighting the importance", "testament to", "poised to",
    "rapidly evolving", "ever-evolving", "landscape of",
]

# The strongest statistical AI tell: analysis bolted to a finished clause as
# a present-participial modifier (2-5x the human rate per the PNAS Biber-
# feature study). The payload gets its own predicate instead.
_PARTICIPIAL_BOLTON = re.compile(
    r",\s+(?:marking|signaling|signalling|highlighting|underscoring|reflecting|"
    r"demonstrating|showcasing|illustrating|emphasizing|cementing|solidifying|"
    r"positioning|reinforcing|suggesting|indicating|representing|signifying|"
    r"paving the way|setting the stage|making it)\b")
_TRAILING_APPOSITIVE = re.compile(
    r",\s+a\s+(?:move|sign|signal|shift|step|feat|milestone|testament|record|first)\s+that\b")
_TRAILING_DELTA = re.compile(
    r",\s+\d+(?:\.\d+)?%\s+(?:above|below|higher than|lower than)\b[^.;:]{0,60}[.;]")

# One odds-bearing word per sentence (Kent: hedges must not stack).
_ESTIMATIVE = re.compile(
    r"\b(?:likely|unlikely|probable|probably|possible|possibly|"
    r"almost certain(?:ly)?|roughly even|might|could well|perhaps)\b")
_MODIFIED_POSSIBLE = re.compile(
    r"\b(?:serious|distinct|real|strong|significant|very real|clear)\s+possibilit",
    re.IGNORECASE)
_BAD_RANGE = re.compile(
    r"\$\d[\d,.]*\s+(?:to|and)\s+\$?\d[\d,.]*\s*(?:million|billion|trillion)\b")
_TIMES_GREATER = re.compile(r"\b\d+(?:\.\d+)?\s*times\s+(?:greater|higher|larger)\b")
_TIMES_LESS = re.compile(r"\b(?:\d+(?:\.\d+)?|five|four|three|ten)\s*times\s+(?:less|lower|cheaper|smaller)\b")

# Insight-labeling and desk self-reference: the writer pointing at the
# analysis instead of delivering it (STYLE.md, Vary the moves).
META_LABELS = [
    "carries the first insight", "carries the second insight",
    "carries the second", "the durable fact", "tells the same story",
    "as covered above", "the basis for our analysis", "as noted above",
    "it is worth pausing",
]
# Copular pronouncement paragraph opener: "The X is/are/remains ..."
_COPULAR_OPENER = re.compile(r"^The\s+[a-z][\w\s-]{0,24}?\s(?:is|are|was|were|remains|stands)\b")
_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")

OUTLET_NAMES = [
    "CNBC", "Bloomberg", "Reuters", "The Information", "TechCrunch", "Axios",
    "Business Insider", "Forbes", "Fortune", "WSJ", "Wall Street Journal",
    "Financial Times", "The Verge", "Benzinga",
]

_FIGURE = re.compile(r"[$€£]\s?\d|\d+(?:\.\d+)?%|\d+(?:\.\d+)?x\b")
# A source cue is a kind+date parenthetical (house deep-dive style) OR an
# endnote marker [n] (analyst-note style).
_SOURCE_CUE = re.compile(
    r"\((?:company|PitchBook|SEC|EDGAR|press|derived|internal|T[1-4]\b|est\.?"
    r"|source|per |as of|[A-Z][a-z]+ \d{1,2}, \d{4}|\d{4})|\[\d+\]", re.IGNORECASE)


def check_text(text, where="", prose=True):
    """Returns list of {severity, rule, where, detail}."""
    issues = []

    def add(sev, rule, detail):
        issues.append({"severity": sev, "rule": rule, "where": where,
                       "detail": detail[:220]})

    n_em = text.count(EM_DASH)
    if n_em > EM_DASH_BLOCK_LIMIT:
        add("WARN", "em-dash-density",
            f"{n_em} em-dashes in one block (limit {EM_DASH_BLOCK_LIMIT}); sparing use only")
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
        if re.search(rf"\b{re.escape(ph)}", low):
            add("WARN", "banned-phrase", repr(ph))
    if prose:
        for adj in NOISE_ADJECTIVES:
            if re.search(rf"\b{adj}\b", low):
                add("WARN", "adjective-noise",
                    f"{adj!r}: delete the adjective, insert the metric (style guide rule 2)")
        for w in WEASELS:
            if re.search(rf"\b{w}\b", low):
                add("WARN", "weasel", f"{w!r} carries no evaluative weight (Kent)")
        for pat, hint in JARGON:
            if pat.search(text):
                add("WARN", "jargon", hint + " (write for the PitchBook reader)")
        for b in BOOSTERS:
            if re.search(rf"\b{re.escape(b)}\b", low):
                add("WARN", "booster", f"{b!r} flags the least-supported claim; show the evidence instead")
        for v in VAGUE_ATTRIBUTIONS:
            if v in low:
                add("WARN", "vague-attribution", f"{v!r}: name the source kind and date")
        for t in AI_TELLS:
            if re.search(rf"\b{re.escape(t)}", low):
                add("WARN", "ai-tell", f"{t!r}: state the fact plainly instead")
        m = _MODIFIED_POSSIBLE.search(text)
        if m:
            add("WARN", "modified-possible",
                f"{m.group(0)!r}: 'possible' is never modified (Kent); use a lexicon band with odds")
        m = _BAD_RANGE.search(text)
        if m:
            add("WARN", "range-units",
                f"{m.group(0)!r}: repeat units in ranges ('$10 million to $20 million')")
        m = _TIMES_GREATER.search(text)
        if m:
            add("WARN", "times-greater",
                f"{m.group(0)!r}: check the arithmetic ('to five times' is 4x; 'five times greater' is 5x)")
        m = _TIMES_LESS.search(text)
        if m:
            add("WARN", "times-less",
                f"{m.group(0)!r}: arithmetically fuzzy; write 'a fifth of' / 'one-quarter of'")
        for ph in META_LABELS:
            if ph in low:
                add("WARN", "insight-label",
                    f"{ph!r}: deliver the insight, do not label it (STYLE.md, Vary the moves)")
        m = _PARTICIPIAL_BOLTON.search(text)
        if m:
            add("WARN", "participial-bolt-on",
                f"{m.group(0).strip()!r}: the strongest AI tell; give the analysis its own "
                "sentence with a real subject and verb")
        m = _TRAILING_APPOSITIVE.search(text)
        if m:
            add("WARN", "trailing-appositive",
                f"{m.group(0).strip()!r}: analysis dangling off a finished clause; "
                "promote it to a predicate")
        m = _TRAILING_DELTA.search(text)
        if m:
            add("WARN", "trailing-delta",
                f"{m.group(0).strip()!r}: give the comparison its own verb "
                "('...and the new price stands 40% above the February mark')")
        sents = _SENT_SPLIT.split(text)
        openers = [s.split()[0].lower().strip('"“(') for s in sents if s.split()]
        for i in range(len(openers) - 2):
            if openers[i] == openers[i + 1] == openers[i + 2]:
                add("WARN", "monotone-openers",
                    f"three consecutive sentences open with {openers[i]!r}; vary the "
                    "opening (time phrase, subordinate clause, contrast)")
                break
        for sent in sents:
            hits = _ESTIMATIVE.findall(sent.lower())
            if len(hits) >= 2:
                add("WARN", "hedge-stack",
                    f"{len(hits)} estimative words in one sentence ({', '.join(hits)}): "
                    "one odds-bearing word per sentence (Kent)")
                break
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
        elif kind == "lead_bullets":
            for j, (lead, rest) in enumerate(b[1]):
                issues += check_text(lead + " " + rest, f"{loc}[{j}]")
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
    n_em = blob.count(EM_DASH)
    if n_em > EM_DASH_BUDGET:
        issues.append({"severity": "FAIL", "rule": "em-dash-budget", "where": path,
                       "detail": f"{n_em} em-dashes in document (budget {EM_DASH_BUDGET}); sparing use only"})
    elif n_em:
        issues.append({"severity": "WARN", "rule": "em-dash-count", "where": path,
                       "detail": f"{n_em} em-dash(es) in document (budget {EM_DASH_BUDGET})"})
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
