#!/usr/bin/env python3
"""Word-level redline engine for the Anthropic S-1 note.
Produces (a) a marked-up docx (insertions bold red, deletions strikethrough) and
(b) a clean docx with all edits applied, then reports Word-style word counts."""
import copy, re, sys, difflib
from docx import Document
from lxml import etree

WNS = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
W = '{%s}' % WNS
def w(tag): return W + tag
XML_SPACE = '{http://www.w3.org/XML/1998/namespace}space'

RPR_ORDER = ['rStyle','rFonts','b','bCs','i','iCs','caps','smallCaps','strike','dstrike','outline',
             'shadow','emboss','imprint','noProof','snapToGrid','vanish','webHidden','color','spacing',
             'w','kern','position','sz','szCs','highlight','u','effect','bdr','shd','fitText','vertAlign',
             'rtl','cs','em','lang','eastAsianLayout','specVanish','oMath']

def set_rpr_child(rPr, tag, attrs=None):
    for el in rPr.findall(w(tag)):
        rPr.remove(el)
    el = etree.SubElement(rPr, w(tag))
    if attrs:
        for k, v in attrs.items():
            el.set(w(k), v)
    children = list(rPr)
    def key(c):
        t = c.tag.replace(W, '')
        return RPR_ORDER.index(t) if t in RPR_ORDER else len(RPR_ORDER)
    children.sort(key=key)
    for c in children: rPr.remove(c)
    for c in children: rPr.append(c)
    return el

def make_run(text, rPr, mode=None):
    r = etree.Element(w('r'))
    rp = copy.deepcopy(rPr) if rPr is not None else etree.Element(w('rPr'))
    if mode == 'ins':
        set_rpr_child(rp, 'b'); set_rpr_child(rp, 'bCs')
        set_rpr_child(rp, 'color', {'val': 'FF0000'})
    elif mode == 'del':
        set_rpr_child(rp, 'strike')
    if len(rp): r.append(rp)
    t = etree.SubElement(r, w('t'))
    t.text = text
    t.set(XML_SPACE, 'preserve')
    return r

def tokenize(s):
    out = []
    for t in re.findall(r'\s+|\S+', s):
        if t.isspace():
            out.append(t); continue
        m = re.match(r'^(\(*)(.*?)([.,;:)]*)$', t)
        lead, core, trail = m.group(1), m.group(2), m.group(3)
        if not core:
            out.append(t); continue
        if lead: out.append(lead)
        out.append(core)
        if trail: out.append(trail)
    return out

def is_word(t):
    return any(c.isalnum() for c in t)

def norm(tok):
    return tok.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')

def curly(s):
    # house style: curly apostrophes in inserted text
    return s.replace("'", '’')

def offsets(tokens):
    off = [0]
    for t in tokens: off.append(off[-1] + len(t))
    return off

def extract(p_el):
    atoms = []
    for ch in list(p_el):
        tag = ch.tag
        if tag == w('pPr') or tag == w('proofErr'):
            continue
        if tag == w('r'):
            rPr = ch.find(w('rPr'))
            for sub in ch:
                if sub.tag == w('rPr'):
                    continue
                if sub.tag == w('t'):
                    for c in (sub.text or ''):
                        atoms.append(('c', c, rPr))
                elif sub.tag == w('lastRenderedPageBreak'):
                    continue
                else:
                    nr = etree.Element(w('r'))
                    if rPr is not None: nr.append(copy.deepcopy(rPr))
                    nr.append(copy.deepcopy(sub))
                    atoms.append(('x', nr))
        else:
            atoms.append(('x', copy.deepcopy(ch)))
    return atoms

def smooth(ops, ot, max_words=2):
    ops = [list(o) for o in ops]
    for idx in range(1, len(ops) - 1):
        tag, i1, i2, j1, j2 = ops[idx]
        if tag == 'equal' and ops[idx-1][0] != 'equal' and ops[idx+1][0] != 'equal':
            words = sum(1 for t in ot[i1:i2] if is_word(t))
            if words <= max_words:
                ops[idx][0] = 'replace'
    merged = []
    for o in ops:
        if merged and o[0] != 'equal' and merged[-1][0] != 'equal':
            m = merged[-1]
            m[0] = 'replace'; m[2] = o[2]; m[4] = o[4]
        else:
            merged.append(o)
    return merged

def rebuild(p_el, new_text, mode):
    """mode: 'redline' or 'clean'"""
    atoms = extract(p_el)
    old_chars = [a for a in atoms if a[0] == 'c']
    old_text = ''.join(a[1] for a in old_chars)
    anchors = {}
    pos = 0
    for a in atoms:
        if a[0] == 'c': pos += 1
        else: anchors.setdefault(pos, []).append(a[1])
    ot = tokenize(old_text); nt = tokenize(new_text)
    sm = difflib.SequenceMatcher(None, [norm(t) for t in ot], [norm(t) for t in nt], autojunk=False)
    ops = smooth(sm.get_opcodes(), ot)
    oo = offsets(ot); no = offsets(nt)
    for ch in list(p_el):
        if ch.tag != w('pPr'):
            p_el.remove(ch)
    # build a char-level stream: list of (kind, char_or_el, rPr) kind in {'c','x'}; for clean mode we drop deleted chars
    stream = []
    def emit_old(c1, c2, flag):
        deferred = []
        seg = ''.join(old_chars[k][1] for k in range(c1, c2))
        if flag == 'del' and seg.isspace():
            flag = None  # whitespace-only deletion: leave unmarked in redline (dropped/collapsed in clean)
            if mode == 'clean':
                flag = 'del'
        for k in range(c1, c2):
            for el in anchors.get(k, []):
                if flag == 'del': deferred.append(el)
                else: stream.append(('x', el, None))
            ch, rPr = old_chars[k][1], old_chars[k][2]
            if flag == 'del' and mode == 'clean':
                continue
            stream.append(('c', ch, rPr, flag))
        return deferred
    def template_rpr(i1):
        if not old_chars: return None
        k = i1 - 1 if i1 > 0 else 0
        k = min(k, len(old_chars) - 1)
        return old_chars[k][2]
    for tag, i1, i2, j1, j2 in ops:
        c1, c2 = oo[i1], oo[i2]
        if tag == 'equal':
            emit_old(c1, c2, None)
        else:
            deferred = []
            if i2 > i1:
                deferred = emit_old(c1, c2, 'del')
            if j2 > j1:
                txt = curly(''.join(nt[j1:j2]))
                rp = template_rpr(i1)
                for ch in txt:
                    stream.append(('c', ch, rp, 'ins' if (mode == 'redline' and not txt.isspace()) else None))
            for el in deferred:
                stream.append(('x', el, None))
    for el in anchors.get(len(old_chars), []):
        stream.append(('x', el, None))
    if mode == 'clean':
        # collapse whitespace runs and strip trailing whitespace
        cleaned = []
        for item in stream:
            if item[0] == 'c' and item[1].isspace():
                if cleaned and cleaned[-1][0] == 'c' and cleaned[-1][1].isspace():
                    continue
                if not cleaned:
                    continue
            cleaned.append(item)
        while cleaned and cleaned[-1][0] == 'c' and cleaned[-1][1].isspace():
            cleaned.pop()
        stream = cleaned
    # emit runs, grouping consecutive chars with identical rPr identity and flag
    buf = ''; cur = None
    def flush():
        nonlocal buf, cur
        if buf:
            p_el.append(make_run(buf, cur[0], cur[1]))
            buf = ''
    for item in stream:
        if item[0] == 'x':
            flush(); p_el.append(item[1]); cur = None
        else:
            key = (item[2], item[3])
            if cur is not None and (key[0] is not cur[0] or key[1] != cur[1]):
                flush()
            cur = key; buf += item[1]
    flush()


def rebuild_full(p_el, new_text, mode):
    """Whole-paragraph replacement: strike the entire old text, then append the new text (redline),
    or replace outright (clean). Non-text runs (endnote refs) are kept at the end."""
    atoms = extract(p_el)
    old_chars = [a for a in atoms if a[0] == 'c']
    rp = old_chars[0][2] if old_chars else None
    xs = [a[1] for a in atoms if a[0] == 'x']
    for ch in list(p_el):
        if ch.tag != w('pPr'):
            p_el.remove(ch)
    if mode == 'redline':
        buf = ''; cur = None
        for c in old_chars:
            if cur is not None and c[2] is not cur and buf:
                p_el.append(make_run(buf, cur, 'del')); buf = ''
            cur = c[2]; buf += c[1]
        if buf: p_el.append(make_run(buf.rstrip() , cur, 'del'))
        p_el.append(make_run(' ', rp, None))
        p_el.append(make_run(curly(new_text), rp, 'ins'))
    else:
        p_el.append(make_run(curly(new_text), rp, None))
    for el in xs:
        p_el.append(el)

def para_text(p_el):
    return ''.join(a[1] for a in extract(p_el) if a[0] == 'c')

def wc(s): return len(s.split())

def body_count(doc):
    """Word-style count from the 'Key takeaways' heading (first Heading 2) to just before 'References' heading; plus whole-doc count."""
    from docx.table import Table
    from docx.text.paragraph import Paragraph
    total = 0; body = 0; started = False; ended = False
    for child in doc.element.body.iterchildren():
        tag = child.tag.replace(W, '')
        if tag == 'p':
            p = Paragraph(child, doc)
            txt = p.text; style = p.style.name
            if style.startswith('Heading') and txt.strip() == 'Key takeaways': started = True
            if style.startswith('Heading') and txt.strip() == 'References': ended = True
        elif tag == 'tbl':
            txt = ' '.join(c.text for r in Table(child, doc).rows for c in r.cells)
        else:
            continue
        n = wc(txt); total += n
        if started and not ended: body += n
    return body, total

def apply(edits, mode, src, dst):
    doc = Document(src)
    paras = doc.paragraphs
    log = []
    for idx, new in edits.get('paras', {}).items():
        p = paras[idx]
        old = para_text(p._p)
        if idx in edits.get('full', []):
            rebuild_full(p._p, new, mode)
        else:
            rebuild(p._p, new, mode)
        log.append((f"p{idx}", wc(old), wc(new)))
    for (ti, ri, ci), new in edits.get('cells', {}).items():
        cell = doc.tables[ti].rows[ri].cells[ci]
        p = cell.paragraphs[0]
        old = para_text(p._p)
        rebuild(p._p, new, mode)
        log.append((f"t{ti}r{ri}c{ci}", wc(old), wc(new)))
    for (ti, ri) in edits.get('delete_rows', []):
        row = doc.tables[ti].rows[ri]
        if mode == 'redline':
            for cell in row.cells:
                for p in cell.paragraphs:
                    rebuild(p._p, '', 'redline')
        else:
            row._tr.getparent().remove(row._tr)
        log.append((f"t{ti}r{ri} (row deleted)", None, None))
    for (ti, after_ri, texts) in edits.get('insert_rows', []):
        tbl = doc.tables[ti]
        src_row = tbl.rows[after_ri]
        new_tr = copy.deepcopy(src_row._tr)
        src_row._tr.addnext(new_tr)
        from docx.table import _Row
        new_row = _Row(new_tr, tbl)
        for cell, txt in zip(new_row.cells, texts):
            p = cell.paragraphs[0]
            for extra in cell.paragraphs[1:]:
                extra._p.getparent().remove(extra._p)
            atoms = extract(p._p)
            rp = next((a[2] for a in atoms if a[0] == 'c'), None)
            for ch in list(p._p):
                if ch.tag != w('pPr'): p._p.remove(ch)
            p._p.append(make_run(curly(txt), rp, 'ins' if mode == 'redline' else None))
        log.append((f"t{ti} row inserted after r{after_ri}", None, None))
    # paragraph deletions
    for idx in sorted(edits.get('delete_paras', []), reverse=True):
        p = paras[idx]
        if mode == 'redline':
            rebuild(p._p, '', 'redline')
        else:
            nxt = p._p.getnext()
            # remove following empty spacer paragraph too
            if nxt is not None and nxt.tag == w('p') and not para_text(nxt).strip():
                nxt.getparent().remove(nxt)
            p._p.getparent().remove(p._p)
        log.append((f"p{idx} (paragraph deleted)", wc(para_text(paras[idx]._p)) if mode == 'redline' else None, 0))
    doc.save(dst)
    return log

if __name__ == '__main__':
    from edits import EDITS
    src = 'orig.docx'
    log = apply(EDITS, 'redline', src, 'redline.docx')
    apply(EDITS, 'clean', src, 'clean.docx')
    clean = Document('clean.docx')
    body, total = body_count(clean)
    obody, ototal = body_count(Document(src))
    print(f"{'item':38s} {'old':>5s} {'new':>5s} {'delta':>6s}")
    dsum = 0
    for item, o, n in log:
        if o is not None and n is not None:
            dsum += n - o
            print(f"{item:38s} {o:5d} {n:5d} {n-o:6d}")
        else:
            print(f"{item:38s}")
    print(f"\nORIGINAL  body(Key takeaways->end, tables incl.)={obody}  whole doc={ototal}")
    print(f"CLEAN     body(Key takeaways->end, tables incl.)={body}  whole doc={total}   target body=2900  diff={body-2900:+d}")
