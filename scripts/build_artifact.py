#!/usr/bin/env python3
"""
CONTEXT: ANTHROPIC INTELLIGENCE DESK — builds dist/artifact.html for publishing as a Claude Artifact.
The Artifact host wraps the file in its own document skeleton, so this strips <!doctype>/<html>/<head>/<body>,
keeps <title>, font links and the D3 script tag, and inlines assets/styles.css and assets/app.js.
The data/*.json files are published alongside as supporting files (relative fetch keeps working).
Run: python3 scripts/build_artifact.py
"""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html = open(os.path.join(ROOT, "index.html")).read()
css = open(os.path.join(ROOT, "assets", "styles.css")).read()
js = open(os.path.join(ROOT, "assets", "app.js")).read()
head = re.search(r"<head>(.*?)</head>", html, re.S).group(1)
body = re.search(r"<body>(.*?)</body>", html, re.S).group(1)
title = re.search(r"<title>.*?</title>", head, re.S).group(0)
links = "\n".join(m.group(0) for m in re.finditer(r"<link[^>]+>", head) if "styles.css" not in m.group(0))
d3 = re.search(r"<script src=\"https://cdnjs[^\"]+\"></script>", head).group(0)
body = body.replace('<script src="assets/app.js"></script>', "<script>\n" + js.replace("</script>", "<\\/script>") + "\n</script>")
out = f"{title}\n{links}\n<style>\n{css}\n</style>\n{d3}\n{body}"
os.makedirs(os.path.join(ROOT, "dist"), exist_ok=True)
open(os.path.join(ROOT, "dist", "artifact.html"), "w").write(out)
print("wrote dist/artifact.html", len(out), "bytes")
