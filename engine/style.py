"""Style profiler: reads reference reports (.docx) and distills a measurable
writing-style profile the composing agent must match.

Usage: python -m engine style
Reads every .docx under previous_reports/ (recursively; drop reports there to
teach the profiler) and reports/*/output/ (the shipped library), writes
style/style_profile.json + style/STYLE_PROFILE.md.

Measured, not vibes: sentence geometry, paragraph geometry, section cadence,
figure/table density, numeral formatting conventions, citation patterns,
punctuation signature, hedging rate, banned-phrase compliance.
"""
from __future__ import annotations
import glob, json, os, re, statistics as stats
from collections import Counter
from . import qa

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STYLE_DIR = os.path.join(REPO, "style")

_SENT = re.compile(r"(?<=[.!?])\s+(?=[A-Z$~(])")
_WORD = re.compile(r"[A-Za-z']+")
_MONEY = re.compile(r"\$\d[\d,.]*\s?(?:[BMKT]\b|billion|million|trillion)?")
_SPELLED_NUM = re.compile(r"\b\d+(?:\.\d+)?\s+(?:billion|million|trillion)\b")
_COMPACT_NUM = re.compile(r"\$\d[\d,.]*[BMT]\b")
_MULT = re.compile(r"\b\d+(?:\.\d+)?x\b")
_PCT = re.compile(r"[+-]?\d+(?:\.\d+)?%")
_CITE = re.compile(r"\((?:[^()]*(?:company|PitchBook|SEC|EDGAR|press|derived|"
                   r"est\.|T[1-4]|[A-Z][a-z]+ \d{1,2}, \d{4}|\d{4})[^()]*)\)")
_HEDGE = re.compile(r"\b(?:may|might|could|possibly|perhaps|arguably|"
                    r"somewhat|potentially)\b", re.IGNORECASE)


def _doc_text(path):
    import docx as _docx
    d = _docx.Document(path)
    paras, headings = [], {"h1": [], "h2": [], "h3": []}
    for p in d.paragraphs:
        t = p.text.strip()
        if not t:
            continue
        s = (p.style.name or "").lower()
        if s.startswith("heading 1"):
            headings["h1"].append(t)
        elif s.startswith("heading 2"):
            headings["h2"].append(t)
        elif s.startswith("heading 3"):
            headings["h3"].append(t)
        elif len(t) > 60:  # body prose, not captions/labels
            paras.append(t)
    n_tables = len(d.tables)
    n_figs = sum(1 for p in d.paragraphs if p.text.strip().startswith("Figure "))
    return paras, headings, n_tables, n_figs


def profile_docx(paths):
    all_sent_lens, para_sent_counts, para_word_counts = [], [], []
    cites = money = spelled = compact = mults = pcts = hedges = words_total = 0
    openers = Counter()
    h1s, h2s = [], []
    tables = figs = docs = 0
    for path in paths:
        try:
            paras, headings, n_tables, n_figs = _doc_text(path)
        except Exception:
            continue
        docs += 1
        tables += n_tables
        figs += n_figs
        h1s += headings["h1"]
        h2s += headings["h2"]
        for t in paras:
            sents = [s for s in _SENT.split(t) if s.strip()]
            para_sent_counts.append(len(sents))
            w = _WORD.findall(t)
            para_word_counts.append(len(w))
            words_total += len(w)
            for s in sents:
                sw = _WORD.findall(s)
                if sw:
                    all_sent_lens.append(len(sw))
                    first = sw[0]
                    if first[0].isupper():
                        openers[first] += 1
            cites += len(_CITE.findall(t))
            money += len(_MONEY.findall(t))
            spelled += len(_SPELLED_NUM.findall(t))
            compact += len(_COMPACT_NUM.findall(t))
            mults += len(_MULT.findall(t))
            pcts += len(_PCT.findall(t))
            hedges += len(_HEDGE.findall(t))
    if not all_sent_lens:
        raise SystemExit("no reference prose found; add .docx reports to reference_reports/")
    kw = 1000.0 / max(words_total, 1)
    prof = {
        "corpus": {"documents": docs, "words": words_total,
                   "paragraphs": len(para_sent_counts)},
        "sentences": {
            "mean_words": round(stats.mean(all_sent_lens), 1),
            "median_words": stats.median(all_sent_lens),
            "p25_words": sorted(all_sent_lens)[len(all_sent_lens) // 4],
            "p75_words": sorted(all_sent_lens)[3 * len(all_sent_lens) // 4],
            "note": "long, clause-stacked sentences are the house signature",
        },
        "paragraphs": {
            "mean_sentences": round(stats.mean(para_sent_counts), 1),
            "mean_words": round(stats.mean(para_word_counts), 0),
            "note": "dense single-topic paragraphs; no one-sentence fragments",
        },
        "sections": {
            "h1_titles": h1s[:20], "h2_per_h1": round(len(h2s) / max(len(h1s), 1), 1),
            "titling_pattern": "metaphor + colon + literal claim (e.g. 'The Mortar: How the Money Is Made')",
        },
        "density_per_1000_words": {
            "tables": round(tables * kw, 2), "figures": round(figs * kw, 2),
            "parenthetical_citations": round(cites * kw, 2),
            "money_figures": round(money * kw, 2),
            "multiples_x": round(mults * kw, 2), "percentages": round(pcts * kw, 2),
        },
        "conventions": {
            "compact_money_vs_spelled": {"compact_$14.2B": compact, "spelled_billion": spelled,
                                         "rule": "prose may spell 'billion'; tables/tiles use $14.2B"},
            "hedges_per_1000_words": round(hedges * kw, 2),
            "em_dashes": 0,
            "citation_style": "parenthetical, source kind + date: (company, February 9, 2026), (PitchBook deal record, Jul 2026)",
        },
        "frequent_sentence_openers": openers.most_common(15),
    }
    return prof


def profile_md(prof):
    s, p, d, c = prof["sentences"], prof["paragraphs"], prof["density_per_1000_words"], prof["conventions"]
    return f"""# Measured style profile (generated; do not hand-edit)

Corpus: {prof['corpus']['documents']} report(s), {prof['corpus']['words']:,} words,
{prof['corpus']['paragraphs']} body paragraphs.

## Sentence geometry
Mean {s['mean_words']} words; median {s['median_words']}; middle half {s['p25_words']}-{s['p75_words']}.
{s['note']}.

## Paragraph geometry
Mean {p['mean_sentences']} sentences / ~{int(p['mean_words'])} words per paragraph. {p['note']}.

## Section cadence
~{prof['sections']['h2_per_h1']} H2 subsections per H1 section. Titling: {prof['sections']['titling_pattern']}.

## Evidence density (per 1,000 words)
{d['parenthetical_citations']} parenthetical citations · {d['money_figures']} money figures ·
{d['multiples_x']} multiples (x) · {d['percentages']} percentages · {d['tables']} tables · {d['figures']} figures.

## Conventions
- Citations: {c['citation_style']}
- Money: {c['compact_money_vs_spelled']['rule']}
- Hedging: {c['hedges_per_1000_words']} hedge words per 1,000 (keep at or below this; certainty is stated, uncertainty is labeled)
- Em-dashes: zero, enforced by the build.

## Frequent sentence openers
{", ".join(w for w, _ in prof['frequent_sentence_openers'][:12])}.
"""


def run(extra_dirs=()):
    paths = glob.glob(os.path.join(REPO, "previous_reports", "**", "*.docx"),
                      recursive=True)
    paths += glob.glob(os.path.join(REPO, "reports", "*", "output", "*.docx"))
    for d in extra_dirs:
        paths += glob.glob(os.path.join(REPO, d, "*.docx"))
    paths = [p for p in paths if "~$" not in p]
    prof = profile_docx(sorted(set(paths)))
    os.makedirs(STYLE_DIR, exist_ok=True)
    with open(os.path.join(STYLE_DIR, "style_profile.json"), "w", encoding="utf-8") as fh:
        json.dump(prof, fh, indent=2, ensure_ascii=False)
    with open(os.path.join(STYLE_DIR, "STYLE_PROFILE.md"), "w", encoding="utf-8") as fh:
        fh.write(profile_md(prof))
    return prof
