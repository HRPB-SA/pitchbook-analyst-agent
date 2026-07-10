import subprocess, json, re, sys
SECTIONS = ["Disclosure and Basis of Preparation","Executive Summary and Investment Thesis",
"The AIBQ Rating: Full Breakdown","Business Model and the Lakehouse","Products and Services Deep Dive",
"AI Focus: Where the Models End and the Business Begins","Financials",
"Capital Structure and Capital Efficiency","The Upcoming Raise: Analyzed, Not Adopted",
"Competitive Position and the Moat","Market Implications and Category",
"The IPO as the Convergence Event","Valuation and Scenarios","Risks and What Would Change Our Mind",
"Management and Governance","Recommendation and Positioning","Appendix A: The AIBQ Framework",
"Appendix B: Sources and Tiering"]
pdf = "output/Databricks_Initiation_Note_Jul2026.pdf"
n = int(subprocess.run(["pdfinfo",pdf],capture_output=True,text=True).stdout.split("Pages:")[1].split()[0])
norm = {}
for p in range(1, n+1):
    out = subprocess.run(["pdftotext","-f",str(p),"-l",str(p),pdf,"-"],capture_output=True,text=True).stdout
    norm[p] = re.sub(r"\s+"," ", out)
toc_page = next(p for p in range(2,n+1) if "Exhibits" in norm[p] and "Contents" in norm[p])
pages = {}
for s in SECTIONS:
    for p in range(2, n+1):
        if p != toc_page and s in norm[p]:
            pages[s] = p; break
for f in range(1, 11):
    for p in range(2, n+1):
        if p != toc_page and f"Figure {f}." in norm[p]:
            pages[f"fig{f}"] = p; break
json.dump(pages, open("build/toc_pages.json","w"))
print("toc_page:", toc_page, "| total:", n)
print(json.dumps(pages))
