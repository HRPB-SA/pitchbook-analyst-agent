# Anthropic S-1 note: 2,900-word redline

Reproduces the September 14, 2026 length edit of "Q3 2026 Anthropic: what to look for in the S-1".

- `edits.py` holds the replacement text per paragraph index and table cell, the deleted table row, the inserted Lambda row, and the deleted paragraph.
- `redline.py` applies a word-level diff to the original docx, marking insertions bold red and deletions strikethrough while preserving run formatting and endnote references; it also writes a clean copy and reports Word-style counts.

Run from a folder containing the original as `orig.docx`:

```bash
pip install python-docx lxml
python3 redline.py    # writes redline.docx and clean.docx, prints counts
```

Target: 2,900 words from the "Key takeaways" heading through the final body paragraph, tables and chart captions included, front matter and references excluded.
