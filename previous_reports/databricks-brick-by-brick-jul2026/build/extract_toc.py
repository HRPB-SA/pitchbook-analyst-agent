import subprocess, json, re, sys
SECTIONS = ["The AIBQ Breakdown: Business Quality, Scored and Decomposed",
"Executive Summary: The House That Data Built",
"The Foundation: What Databricks Is",
"The Bricks: Products and Services, Layer by Layer",
"The Mortar: How the Money Is Made",
"The Builders: Customers and What They Do",
"The Neighborhood: Competition on Three Fronts",
"The Blueprint: Strategy, Read Through Actions",
"The Ledger: The Financial Picture",
"The Appraisal: What the Business Is Worth",
"The Stress Test: What Would Change the Answer",
"The Verdict"]
pdf = sys.argv[1] if len(sys.argv) > 1 else "output/Databricks_BrickByBrick_Jul2026.pdf"
n = int(subprocess.run(["pdfinfo",pdf],capture_output=True,text=True).stdout.split("Pages:")[1].split()[0])
norm = {}
for p in range(1, n+1):
    out = subprocess.run(["pdftotext","-f",str(p),"-l",str(p),pdf,"-"],capture_output=True,text=True).stdout
    norm[p] = re.sub(r"\s+"," ", out)
toc_page = next(p for p in range(2,n+1) if "Exhibits" in norm[p] and "Contents" in norm[p])
pages = {}
raw = {}
for p in range(1, n+1):
    raw[p] = subprocess.run(["pdftotext","-f",str(p),"-l",str(p),pdf,"-"],capture_output=True,text=True).stdout
for s in SECTIONS:
    for p in range(2, n+1):
        if p != toc_page and any(l.strip() == s for l in raw[p].splitlines()):
            pages[s] = p; break
    else:
        for p in range(2, n+1):
            if p != toc_page and s in norm[p]:
                pages[s] = p; break
for f in range(1, 12):
    for p in range(2, n+1):
        if p != toc_page and f"Figure {f}." in norm[p]:
            pages[f"fig{f}"] = p; break
json.dump(pages, open("build/toc_pages.json","w"))
print("toc_page:", toc_page, "| total:", n)
print(json.dumps(pages))
