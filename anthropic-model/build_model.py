# Anthropic_Model_v1.xlsx builder — CFI-consistent formatting (Open Sans, FF3271D2 inputs,
# FFD9E5F7 banners, parens negatives, en-dash zeros, 0"A"/0"E" year headers)
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment

FNT = "Open Sans"
BLUE = "FF3271D2"; BANFILL = "FFD9E5F7"; TITLE_BLUE = "FF4472C4"; NAVY = "FF132E57"
ORANGE = "FFFA621C"; WHITE = "FFFFFFFF"
NUM  = r'_(#,##0_);\(#,##0\);_("–"_);_(@_)'
PCT  = r'_(#,##0.0%_);\(#,##0.0%\);_("–"_)_%;_(@_)_%'
MULT = r'_(0.0\x_);\(0.0\x\);_("–"_);_(@_)'
CHK  = r'#,##0_);[Red]\(#,##0\);\-'
YRA = '0"A"'; YRE = '0"E"'
thin = Side(style="thin"); hair = Side(style="hair"); med = Side(style="medium"); dbl = Side(style="double")
B_T   = Border(top=thin); B_TB = Border(top=thin, bottom=thin)
B_MTB = Border(top=med, bottom=med); B_HB = Border(bottom=hair); B_TDB = Border(top=thin, bottom=dbl)

YC = {2023:"D",2024:"E",2025:"F",2026:"G",2027:"H",2028:"I",2029:"J",2030:"K"}
FC = ["G","H","I","J","K"]          # forecast cols 2026-2030
FC27 = ["H","I","J","K"]            # 2027-2030

def put(ws, coord, v, sz=10, bold=False, italic=False, color=None, fill=None, nf=None,
        border=None, align=None):
    c = ws[coord]; c.value = v
    c.font = Font(name=FNT, size=sz, bold=bold, italic=italic, color=color)
    if fill:   c.fill = PatternFill("solid", fgColor=fill)
    if nf:     c.number_format = nf
    if border: c.border = border
    if align:  c.alignment = Alignment(horizontal=align)
    return c

def banner(ws, r, text):
    for col in range(1, 13):
        ws.cell(row=r, column=col).fill = PatternFill("solid", fgColor=BANFILL)
    put(ws, f"B{r}", text, sz=14, bold=True, color=BLUE, fill=BANFILL)

def unote(ws, r, text="All figures in USD millions unless stated"):
    put(ws, f"B{r}", text, sz=9, italic=True)

def yearrow(ws, r):
    for y, cl in YC.items():
        put(ws, f"{cl}{r}", f"='00_Assumptions'!{cl}$10", bold=True,
            nf=(YRA if y <= 2025 else YRE), border=B_MTB, align="center")

def driver(ws, r, title, cols, bear, base, bull, nf):
    put(ws, f"B{r}", title, bold=True)
    for j, cl in enumerate(cols):
        put(ws, f"{cl}{r}", f"=CHOOSE($D$7,{cl}{r+2},{cl}{r+3},{cl}{r+4})",
            bold=True, nf=nf, border=B_TB)
    for k, (lab, vals) in enumerate([("Bear", bear), ("Base", base), ("Bull", bull)]):
        rr = r + 2 + k
        put(ws, f"B{rr}", lab, color=BLUE)
        for j, cl in enumerate(cols):
            put(ws, f"{cl}{rr}", vals[j], color=BLUE, nf=nf,
                border=(B_HB if k == 2 else None))
    return r + 6

def mksheet(wb, name, widths=None, freeze="A2"):
    ws = wb.create_sheet(name)
    ws.sheet_view.showGridLines = False
    if freeze: ws.freeze_panes = freeze
    w = widths or {"A":2.5,"B":42,"C":13,"D":10.5,"E":10.5,"F":10.5,"G":10.5,"H":10.5,
                   "I":10.5,"J":10.5,"K":10.5,"L":2.5,"M":70}
    for cl, wd in w.items(): ws.column_dimensions[cl].width = wd
    return ws

wb = Workbook(); wb.remove(wb.active)
cover = mksheet(wb, "Cover", {"A":3,"B":3,"C":34,"D":12,"E":12,"F":3,"G":3,"H":46,"I":10,"J":3}, freeze=None)
A  = mksheet(wb, "00_Assumptions")
DT = mksheet(wb, "01_Data", {"A":2.5,"B":34,"C":13,"D":8,"E":12,"F":26,"G":6,"H":18,"I":34})
RV = mksheet(wb, "02_Revenue")
CO = mksheet(wb, "03_Costs")
PL = mksheet(wb, "04_PL")
CF = mksheet(wb, "05_Cash_Fund")
VA = mksheet(wb, "06_Valuation", {"A":2.5,"B":40,"C":13,"D":11,"E":11,"F":9,"G":26,"H":10.5,
                                  "I":10.5,"J":10.5,"K":10.5,"L":2.5,"M":70})
SN = mksheet(wb, "07_Sensitivity", {"A":2.5,"B":13,"C":11,"D":11,"E":11,"F":11,"G":11,"H":3,"I":40})
OU = mksheet(wb, "08_Output", {"A":2.5,"B":40,"C":3,"D":13,"E":13,"F":40,"G":10.5,"H":10.5,
                               "I":10.5,"J":10.5,"K":10.5,"L":2.5})

# ============================== 00_ASSUMPTIONS ==============================
banner(A, 3, "Scenario Control & Timeline")
unote(A, 5)
put(A, "B7", "Scenario Switch", bold=True)
put(A, "D7", 2, color=BLUE, align="center")
put(A, "F7", "1 = Bear · 2 = Base · 3 = Bull", sz=9, italic=True)
put(A, "B8", "Active Scenario", bold=True)
put(A, "D8", '=CHOOSE($D$7,"Bear","Base","Bull")', align="center")
put(A, "B10", "Timeline (typed once — every tab links here)", bold=True)
put(A, "D10", 2023, color=BLUE, nf=YRA, bold=True, border=B_MTB, align="center")
for y, cl in list(YC.items())[1:]:
    prev = chr(ord(cl) - 1)
    put(A, f"{cl}10", f"={prev}10+1", bold=True, nf=(YRA if y <= 2025 else YRE),
        border=B_MTB, align="center")

banner(A, 13, "Scalar Drivers (one value per scenario)")
for cl, lab in [("D","Bear"),("E","Base"),("F","Bull"),("G","Active")]:
    put(A, f"{cl}15", lab, bold=True, border=B_TB, align="center")
scalars = [
    (16, "2026E exit run-rate — gross ($M)", 95000, 110000, 125000, NUM),
    (17, "Discount rate", .22, .18, .15, PCT),
    (18, "Terminal growth (Gordon)", .025, .03, .035, PCT),
    (19, "Terminal exit multiple (x 2030E FCF)", 14, 18, 22, MULT),
]
for r, lab, b1, b2, b3, nf in scalars:
    put(A, f"B{r}", lab)
    for cl, v in [("D",b1),("E",b2),("F",b3)]:
        put(A, f"{cl}{r}", v, color=BLUE, nf=nf, align="center")
    put(A, f"G{r}", f"=CHOOSE($D$7,D{r},E{r},F{r})", bold=True, nf=nf, align="center")

put(A, "B21", "Constants (not scenario-flexed)", bold=True)
consts = [
    (22, "Equalization — net as % of gross (Ruling 5)", .6025, PCT,
     "1 − 39.75% (Ruling 5) · gate-verified on May-26 mix · mix-stability assumed at later prints (est.)"),
    (23, "Tax rate (post-NOL)", .18, PCT, "blended fed+state, simplified"),
    (24, "Interest rate on debt", .065, PCT, "chip bonds + revolver, blended (est.)"),
    (25, "Yield on cash", .04, PCT, "T-bill proxy"),
    (26, "Owned-infra capex (% of revenue)", .015, PCT, "most compute is opex/prepay, not capex"),
]
for r, lab, v, nf, note in consts:
    put(A, f"B{r}", lab)
    put(A, f"D{r}", v, color=BLUE, nf=nf, align="center")
    put(A, f"F{r}", note, sz=8, italic=True)

banner(A, 29, "Per-Year Drivers — forecast 2026E–2030E (bold row = active scenario)")
yearrow(A, 31)
r = 33
r = driver(A, r, "Exit run-rate growth (YoY, 2027E on)", FC27,
           [.10,.05,.03,.02], [.50,.32,.22,.15], [.80,.55,.40,.30], PCT)      # r33
r = driver(A, r, "Gross margin (gross-revenue basis)", FC,
           [.46,.52,.60,.62,.63], [.52,.63,.77,.78,.80], [.55,.67,.80,.81,.82], PCT)  # r39
r = driver(A, r, "R&D — training compute ($M)", FC,
           [11000,14000,16000,18000,20000], [13000,22000,30000,38000,45000],
           [15000,28000,40000,52000,65000], NUM)                               # r45
r = driver(A, r, "R&D — people & other ($M)", FC,
           [2800,4000,5500,7000,8500], [3000,5000,7000,9000,11000],
           [3200,6000,8500,11000,13500], NUM)                                  # r51
r = driver(A, r, "S&M (% of revenue)", FC,
           [.09,.08,.07,.065,.06], [.08,.07,.06,.055,.05], [.07,.06,.05,.045,.04], PCT)  # r57
r = driver(A, r, "G&A (% of revenue)", FC,
           [.035,.03,.025,.025,.025], [.03,.025,.02,.02,.02], [.03,.025,.02,.018,.015], PCT)  # r63
r = driver(A, r, "Prepaid compute & WC build (% of revenue)", FC,
           [.12,.07,.05,.045,.04], [.10,.05,.04,.035,.03], [.08,.04,.03,.025,.02], PCT)  # r69
put(A, "B75", "Base margin path 2027E 63% / 2028E 77% = company plan (T3, The Information). "
              "Blue = input · Black = formula · Bold driver row = active scenario via CHOOSE on D7.",
    sz=9, italic=True)
# ============================== 01_DATA ==============================
banner(DT, 3, "Funding & Marks (STABLE decay) — PB re-pulled 2026-08-19")
hdr = ["Metric / Event","Value","Units","As-of","Basis / Round","Tier","Tag","Source"]
for cl, h in zip(["B","C","D","E","F","G","H","I"], hdr):
    put(DT, f"{cl}5", h, bold=True, border=B_TB)

def drow(ws, r, label, val, units, asof, basis, tier, tag, src, nf=NUM):
    put(ws, f"B{r}", label)
    put(ws, f"C{r}", val, color=BLUE, nf=nf)
    put(ws, f"D{r}", units, sz=9)
    put(ws, f"E{r}", asof, sz=9)
    put(ws, f"F{r}", basis, sz=9)
    put(ws, f"G{r}", tier, sz=9, align="center")
    tagcol = ORANGE if any(k in tag for k in ("DISPUTED","VERIFY","STALE","rumor")) else None
    put(ws, f"H{r}", tag, sz=9, color=tagcol)
    put(ws, f"I{r}", src, sz=9)

fund = [
    (6,  "Series A", 124, "2021-05-28", "post $461M", "T2", "CANONICAL", "PitchBook"),
    (7,  "Series D (Menlo)", 1200, "2024-07-01", "$19.8B pre → $21B post", "T2", "CANONICAL", "PitchBook"),
    (8,  "Amazon round", 8000, "2024-11-22", "$46B pre · $1.3B conv.", "T2", "CANONICAL", "PitchBook"),
    (9,  "Series E (Lightspeed)", 3500, "2025-03-03", "$58B pre → $61.5B post", "T2", "CANONICAL", "PitchBook"),
    (10, "Revolver (debt)", 2500, "2025-05-16", "debt facility", "T2", "CANONICAL", "PB 295197-04T"),
    (11, "Series F (Lightspeed/Fidelity/ICONIQ)", 13000, "2025-09-02", "$170B pre → $183B post", "T2", "CANONICAL", "PitchBook"),
    (12, "Series G (Coatue/GIC/ICONIQ e.a.)", 30000, "2026-02-12", "$350B pre → $380B post", "T2", "CANONICAL", "PitchBook"),
    (13, "Series H (Dragoneer/Sequoia e.a.)", 65000, "2026-05-28", "$900B pre → $965B post · $589.0095/sh", "T2", "CANONICAL", "PB 329489-02T"),
    (14, "Chip bonds (debt)", 34500, "2026-06-09", "$6.0B SP / $24.0B 1L / $4.5B 2L · Alphabet chips", "T2", "CANONICAL", "PB 334763-02T"),
    (15, "Total equity raised", 124300, "2026-07-02", "equity-only (Ruling 1)", "T2", "CANONICAL", "project-context v3.4 · PB tie"),
    (16, "Total debt", 37000, "2026-07-02", "bonds + revolver", "T2", "CANONICAL", "project-context v3.4"),
    (17, "Total raised (PB)", 161254, "2026-08-18", "equity + debt", "T2", "CANONICAL", "PB profile 466959-97"),
]
for row in fund: drow(DT, row[0], row[1], row[2], "$M", row[3], row[4], row[5], row[6], row[7])

banner(DT, 19, "Run-Rate Curve (VOLATILE decay) — annualized, GROSS basis")
for cl, h in zip(["B","C","D","E","F","G","H","I"], hdr):
    put(DT, f"{cl}21", h, bold=True, border=B_TB)
curve = [
    (22, "Run-rate — Dec 2024", 1000, "2024-12", "exit run-rate", "T2", "CANONICAL", "multi-outlet"),
    (23, "Run-rate — Jul 2025", 4000, "2025-07", "run-rate", "T2/T3", "est.", "press"),
    (24, "Run-rate — Dec 2025", 9000, "2025-12", "exit run-rate", "T2", "CANONICAL", "multi-outlet · PB FY25 field"),
    (25, "Run-rate — Feb 2026", 14000, "2026-02", "run-rate", "T3", "est.", "press"),
    (26, "Run-rate — ~Apr 2026", 30000, "2026-04", "run-rate ('80x growth')", "T2", "VERIFY date", "VentureBeat/company"),
    (27, "Run-rate — May 2026", 47000, "2026-05", "run-rate (prior canonical)", "T2", "CANONICAL", "company"),
    (28, "Run-rate — end-Jul 2026", 65000, "2026-08-17", "run-rate, company-to-investors", "T2", "PROPOSED CANONICAL", "CNBC·Bloomberg·Fortune·TechCrunch"),
    (29, "YE-2026 run-rate, investor expectation", 110000, "2026-08-17", "midpoint of $100–120B range", "T3", "est.", "CNBC"),
]
for row in curve: drow(DT, row[0], row[1], row[2], "$M", row[3], row[4], row[5], row[6], row[7])

banner(DT, 31, "P&L, Margins, Burn, Ops (QUARTERLY decay)")
for cl, h in zip(["B","C","D","E","F","G","H","I"], hdr):
    put(DT, f"{cl}33", h, bold=True, border=B_TB)
ops = [
    (34, "FY2024 revenue (PB)", 1000, "$M", "FY2024", "matches Dec-24 run-rate", "T2/T4", "DISPUTED basis", "PitchBook"),
    (35, "FY2024 net loss (PB)", -5300, "$M", "FY2024", "reported", "T2/T4", "CANONICAL", "PitchBook"),
    (36, "FY2025 revenue (PB)", 9000, "$M", "FY2025", "matches Dec-25 run-rate; guide implies ~$4.5–6B recognized", "T2/T4", "DISPUTED basis", "PitchBook"),
    (37, "Gross margin 2025", .40, "%", "FY2025", "lowered vs plan · gross-rev basis", "T3", "est.", "The Information"),
    (38, "GM path 2027E / 2028E", .63, "%", "plan", "77% in 2028E · company plan", "T3", "CANONICAL path", "The Information / WSJ"),
    (39, "Q2 2026 operating profit", 559, "$M", "Q2 2026", "first op profit", "T3", "unswept (FCF flag)", "CNBC"),
    (40, "FY2025 cash burn", -5600, "$M", "FY2025", "operating burn", "T3", "est.", "The Information"),
    (41, "FY2026 planned burn", -3000, "$M", "plan (pre-beat)", "vintage ~Jan-26", "T3", "superseded vintage", "The Information"),
    (42, "WSJ FCF trough (2027, scenario)", -25000, "$M", "2026-04-06", "incl.-training FCF basis", "T2", "DISPUTED vintage/defn", "WSJ investor docs"),
    (43, "Net revenue retention", 1.40, "%", "2026", "140%+", "T2", "CANONICAL", "company"),
    (44, "Enterprise share of revenue", .80, "%", "2026", "", "T2", "CANONICAL", "company"),
    (45, "Claude Code ARR", 2500, "$M", "2026-05", "54% coding share", "T2", "CANONICAL", "company"),
    (46, "Employees", 5000, "count", "2026-04-21", "", "T2", "CANONICAL", "PitchBook"),
]
for r, lab, v, u, asof, basis, tier, tag, src in ops:
    drow(DT, r, lab, v, u, asof, basis, tier, tag, src, nf=(PCT if u == "%" else NUM))

banner(DT, 48, "Forecast Vintages · Comps · Open Items")
for cl, h in zip(["B","C","D","E","F","G","H","I"], hdr):
    put(DT, f"{cl}50", h, bold=True, border=B_TB)
misc = [
    (51, "2026 company guide (hiked +20%)", 18000, "$M", "~Jan-26", "recognized-rev basis", "T3", "superseded by actuals", "The Information"),
    (52, "2027 optimistic case", 55000, "$M", "~Jan-26", "already below Jul-26 run-rate", "T3", "superseded", "The Information"),
    (53, "2029 optimistic case", 148000, "$M", "~Jan-26", "", "T3", "stale vintage", "The Information"),
    (54, "PB revenue field — TRAP", 71000, "$M", "2026-08-18", "TTM 4Q2027 = FORWARD projection (Ruling 4, 3rd firing)", "T4", "DISPUTED — never cite as current", "PitchBook"),
    (55, "OpenAI mark", 852000, "$M", "2026-03-31", "$122B round", "T2", "CANONICAL", "PitchBook"),
    (56, "OpenAI net ARR", 25000, "$M", "~2026-06", "NET basis", "T3", "STALE — re-pull", "project-context"),
    (57, "Databricks mark", 134000, "$M", "2026-02-09", "Series L", "T2", "STALE — re-pull", "PitchBook"),
    (58, "SPCX Q2 print (Aug 6)", 0, "—", "2026-08-06", "Basis Trade falsifier window", "—", "VERIFY — unpulled", "—"),
    (59, "AMD round (11th, upcoming)", 0, "—", "2026-07-22", "'reportedly seeking'", "T5", "rumor — do not model", "PB note"),
    (60, "Decart acquisition (~$6B)", 6000, "$M", "2026-08-13", "status Rumor/Speculation", "T5", "rumor — do not model", "PB"),
]
for r, lab, v, u, asof, basis, tier, tag, src in misc:
    drow(DT, r, lab, v, u, asof, basis, tier, tag, src)
put(DT, "B62", "Facts only — every model input traces here or to a stated estimate. Tiers per validation spine (T1 primary → T5 rumor).",
    sz=9, italic=True)

# ============================== 02_REVENUE ==============================
banner(RV, 3, "Run-Rate Curve — annual exits (GROSS basis)")
unote(RV, 5)
yearrow(RV, 7)
put(RV, "B9", "Exit run-rate — gross ($M)", bold=True)
put(RV, "D9", 200, color=BLUE, nf=NUM)                      # est. YE-2023
put(RV, "E9", "='01_Data'!$C$22", nf=NUM)
put(RV, "F9", "='01_Data'!$C$24", nf=NUM)
put(RV, "G9", "='00_Assumptions'!$G$16", nf=NUM, border=B_TB, bold=True)
for cl in FC27:
    prev = chr(ord(cl) - 1)
    put(RV, f"{cl}9", f"={prev}9*(1+'00_Assumptions'!{cl}$33)", nf=NUM, border=B_TB, bold=True)
put(RV, "M9", "2023 exit = est. · 2024/2025 link 01_Data · 2026E = scenario scalar · 2027E+ = growth driver", sz=8, italic=True)
put(RV, "B10", "   YoY growth", italic=True)
for cl in ["E","F","G","H","I","J","K"]:
    prev = chr(ord(cl) - 1)
    put(RV, f"{cl}10", f"={cl}9/{prev}9-1", italic=True, nf=PCT)
put(RV, "B11", "Exit run-rate — net equalized ($M)")
for cl in YC.values():
    put(RV, f"{cl}11", f"={cl}9*'00_Assumptions'!$D$22", nf=NUM)

banner(RV, 13, "Recognized Revenue — derived (log-mean integration of the exit curve)")
unote(RV, 15)
yearrow(RV, 16)
put(RV, "B17", "Recognized revenue — gross ($M)", bold=True)
put(RV, "D17", 100, color=BLUE, nf=NUM, border=B_TB, bold=True)
for cl in ["E","F","G","H","I","J","K"]:
    prev = chr(ord(cl) - 1)
    put(RV, f"{cl}17", f"=IFERROR(({cl}9-{prev}9)/LN({cl}9/{prev}9),({cl}9+{prev}9)/2)",
        nf=NUM, border=B_TB, bold=True)
put(RV, "M17", "Recognized_t = (RR_t − RR_t-1)/ln(RR_t/RR_t-1) — exact integral of smooth exponential growth between exits", sz=8, italic=True)
put(RV, "B18", "   YoY growth", italic=True)
for cl in ["E","F","G","H","I","J","K"]:
    prev = chr(ord(cl) - 1)
    put(RV, f"{cl}18", f"={cl}17/{prev}17-1", italic=True, nf=PCT)
put(RV, "B19", "Recognized revenue — net equalized ($M)")
for cl in YC.values():
    put(RV, f"{cl}19", f"={cl}17*'00_Assumptions'!$D$22", nf=NUM)
put(RV, "B21", "PB reference: FY2024 $1.0B · FY2025 $9.0B — [DISPUTED basis: PB carries exit run-rates as fiscal revenue; see 01_Data rows 34/36]",
    sz=9, italic=True, color=ORANGE)
put(RV, "B23", "Derived 2025 recognized ≈ $3.6B vs $4.5–6B implied by the Jan-26 guide — gap is curve-shape uncertainty; both far below the $9.0B run-rate-as-fiscal print.",
    sz=9, italic=True)
# ============================== 03_COSTS ==============================
banner(CO, 3, "Gross Margin & COGS (inference compute + cloud rev-share)")
unote(CO, 5)
yearrow(CO, 7)
put(CO, "B9", "Gross margin % (gross-revenue basis)", bold=True)
for cl, v in [("D", -1.20), ("E", -0.94), ("F", 0.40)]:
    put(CO, f"{cl}9", v, color=BLUE, nf=PCT)
for cl in FC:
    put(CO, f"{cl}9", f"='00_Assumptions'!{cl}39", nf=PCT)
put(CO, "M9", "2023 est. · 2024 −94% [CANONICAL] · 2025 40% (T3) · forecast = scenario driver", sz=8, italic=True)
put(CO, "B10", "Revenue — gross ($M)")
for cl in YC.values():
    put(CO, f"{cl}10", f"='02_Revenue'!{cl}17", nf=NUM)
put(CO, "B11", "COGS ($M)")
for cl in YC.values():
    put(CO, f"{cl}11", f"={cl}10*(1-{cl}9)", nf=NUM)
put(CO, "B12", "Gross profit ($M)", bold=True)
for cl in YC.values():
    put(CO, f"{cl}12", f"={cl}10-{cl}11", bold=True, nf=NUM, border=B_TB)

banner(CO, 15, "Operating Expenses")
unote(CO, 17)
yearrow(CO, 18)
opex_hist = {"18": [1200, 4000, 6000], "19": [400, 800, 1500]}
put(CO, "B20", "R&D — training compute ($M)")
for cl, v in zip(["D","E","F"], opex_hist["18"]):
    put(CO, f"{cl}20", v, color=BLUE, nf=NUM)
for cl in FC:
    put(CO, f"{cl}20", f"='00_Assumptions'!{cl}45", nf=NUM)
put(CO, "M20", "hist. est. (calibrated to PB FY24 loss + WSJ dual-P&L) · forecast = driver · expensed, never capitalized", sz=8, italic=True)
put(CO, "B21", "R&D — people & other ($M)")
for cl, v in zip(["D","E","F"], opex_hist["19"]):
    put(CO, f"{cl}21", v, color=BLUE, nf=NUM)
for cl in FC:
    put(CO, f"{cl}21", f"='00_Assumptions'!{cl}51", nf=NUM)
put(CO, "B22", "S&M ($M)")
for cl, v in zip(["D","E","F"], [50, 150, 400]):
    put(CO, f"{cl}22", v, color=BLUE, nf=NUM)
for cl in FC:
    put(CO, f"{cl}22", f"='00_Assumptions'!{cl}57*'02_Revenue'!{cl}17", nf=NUM)
put(CO, "B23", "G&A ($M)")
for cl, v in zip(["D","E","F"], [50, 100, 250]):
    put(CO, f"{cl}23", v, color=BLUE, nf=NUM)
for cl in FC:
    put(CO, f"{cl}23", f"='00_Assumptions'!{cl}63*'02_Revenue'!{cl}17", nf=NUM)
put(CO, "B24", "Total opex ($M)", bold=True)
for cl in YC.values():
    put(CO, f"{cl}24", f"=SUM({cl}20:{cl}23)", bold=True, nf=NUM, border=B_T)
put(CO, "B26", "Training compute sits in R&D and is expensed in full (GAAP) — the dual-basis EBIT on 04_PL separates it, per the WSJ investor-doc framework.",
    sz=9, italic=True)

# ============================== 04_PL ==============================
banner(PL, 3, "P&L — Consolidated (GROSS revenue basis)")
unote(PL, 5)
yearrow(PL, 7)
put(PL, "B9", "Revenue — gross ($M)", bold=True)
for cl in YC.values(): put(PL, f"{cl}9", f"='02_Revenue'!{cl}17", bold=True, nf=NUM)
put(PL, "B10", "COGS")
for cl in YC.values(): put(PL, f"{cl}10", f"='03_Costs'!{cl}11", nf=NUM)
put(PL, "B11", "Gross profit", bold=True)
for cl in YC.values(): put(PL, f"{cl}11", f"={cl}9-{cl}10", bold=True, nf=NUM, border=B_T)
put(PL, "B12", "   Gross margin", italic=True)
for cl in YC.values(): put(PL, f"{cl}12", f"={cl}11/{cl}9", italic=True, nf=PCT)
put(PL, "B14", "R&D — training compute")
for cl in YC.values(): put(PL, f"{cl}14", f"='03_Costs'!{cl}20", nf=NUM)
put(PL, "B15", "R&D — people & other")
for cl in YC.values(): put(PL, f"{cl}15", f"='03_Costs'!{cl}21", nf=NUM)
put(PL, "B16", "S&M")
for cl in YC.values(): put(PL, f"{cl}16", f"='03_Costs'!{cl}22", nf=NUM)
put(PL, "B17", "G&A")
for cl in YC.values(): put(PL, f"{cl}17", f"='03_Costs'!{cl}23", nf=NUM)
put(PL, "B18", "Total opex", bold=True)
for cl in YC.values(): put(PL, f"{cl}18", f"=SUM({cl}14:{cl}17)", bold=True, nf=NUM, border=B_T)
put(PL, "B20", "EBIT", bold=True)
for cl in YC.values(): put(PL, f"{cl}20", f"={cl}11-{cl}18", bold=True, nf=NUM, border=B_TB)
put(PL, "B21", "   EBIT margin", italic=True)
for cl in YC.values(): put(PL, f"{cl}21", f"={cl}20/{cl}9", italic=True, nf=PCT)
put(PL, "B22", "EBIT excl. training compute")
for cl in YC.values(): put(PL, f"{cl}22", f"={cl}20+{cl}14", nf=NUM)
put(PL, "M22", "WSJ dual-basis: excl-training breakeven 2025, incl-training 2028 (Apr-26 vintage) — actuals beat plan (Q2-26 op profit $559M, T3)", sz=8, italic=True)
put(PL, "B24", "Interest income")
for cl in YC.values():
    put(PL, f"{cl}24", f"='05_Cash_Fund'!{cl}24*'00_Assumptions'!$D$25", nf=NUM)
put(PL, "M24", "beginning-of-year cash × yield — avoids circularity", sz=8, italic=True)
put(PL, "B25", "Interest expense")
put(PL, "D25", "=('05_Cash_Fund'!D23/2)*'00_Assumptions'!$D$24", nf=NUM)
for cl in ["E","F","G","H","I","J","K"]:
    prev = chr(ord(cl) - 1)
    put(PL, f"{cl}25", f"=(('05_Cash_Fund'!{prev}23+'05_Cash_Fund'!{cl}23)/2)*'00_Assumptions'!$D$24", nf=NUM)
put(PL, "B26", "EBT", bold=True)
for cl in YC.values(): put(PL, f"{cl}26", f"={cl}20+{cl}24-{cl}25", bold=True, nf=NUM, border=B_T)
put(PL, "B28", "NOL balance (BoY)")
put(PL, "D28", 700, color=BLUE, nf=NUM)
for cl in ["E","F","G","H","I","J","K"]:
    prev = chr(ord(cl) - 1)
    put(PL, f"{cl}28", f"={prev}28+MAX(0,-{prev}26)-{prev}29", nf=NUM)
put(PL, "M28", "pre-2023 accumulated losses est. $0.7B — schedule accretes losses, burns against profits", sz=8, italic=True)
put(PL, "B29", "NOL used")
for cl in YC.values(): put(PL, f"{cl}29", f"=MIN({cl}28,MAX(0,{cl}26))", nf=NUM)
put(PL, "B30", "Taxable income")
for cl in YC.values(): put(PL, f"{cl}30", f"=MAX(0,{cl}26-{cl}29)", nf=NUM)
put(PL, "B31", "Tax expense")
for cl in YC.values(): put(PL, f"{cl}31", f"={cl}30*'00_Assumptions'!$D$23", nf=NUM)
put(PL, "B33", "Net income", bold=True)
for cl in YC.values(): put(PL, f"{cl}33", f"={cl}26-{cl}31", bold=True, nf=NUM, border=B_TDB)
put(PL, "B34", "   Net margin", italic=True)
for cl in YC.values(): put(PL, f"{cl}34", f"={cl}33/{cl}9", italic=True, nf=PCT)
put(PL, "B36", "No D&A line: compute is rented/prepaid (opex), owned-infra capex is small — see 05_Cash_Fund. SBC not separable pre-S-1 (private); flag for the T1 upgrade.",
    sz=9, italic=True)
# ============================== 05_CASH_FUND ==============================
banner(CF, 3, "Free Cash Flow")
unote(CF, 5)
yearrow(CF, 7)
put(CF, "B9", "Net income")
for cl in YC.values(): put(CF, f"{cl}9", f"='04_PL'!{cl}33", nf=NUM)
put(CF, "B10", "Prepaid compute & WC build")
for cl in ["D","E","F"]: put(CF, f"{cl}10", 0, color=BLUE, nf=NUM)
for cl in FC:
    put(CF, f"{cl}10", f"=-('00_Assumptions'!{cl}69*'02_Revenue'!{cl}17)", nf=NUM)
put(CF, "B11", "Owned-infra capex")
for cl in ["D","E","F"]: put(CF, f"{cl}11", 0, color=BLUE, nf=NUM)
for cl in FC:
    put(CF, f"{cl}11", f"=-('00_Assumptions'!$D$26*'02_Revenue'!{cl}17)", nf=NUM)
put(CF, "B13", "Free cash flow", bold=True)
for cl in YC.values():
    put(CF, f"{cl}13", f"=SUM({cl}9:{cl}11)", bold=True, nf=NUM, border=B_TB)
put(CF, "B14", "Reported burn: FY2025 −$5.6B (T3) vs derived — triangulation gap documented on 01_Data row 40. Hist. prepay/capex set to 0 (est.).",
    sz=9, italic=True)

banner(CF, 16, "Financing & Cash Walk")
unote(CF, 18)
yearrow(CF, 19)
put(CF, "B21", "Equity raised ($M)")
for cl, v in zip(YC.values(), [2000, 9200, 16500, 95000, 0, 0, 0, 0]):
    put(CF, f"{cl}21", v, color=BLUE, nf=NUM)
put(CF, "M21", "2026 = Series G $30B + Series H $65B · pre-2023 $1.6B sits in opening cash · est. year-split, tied to $124.3B [CANONICAL] via check", sz=8, italic=True)
put(CF, "B22", "Debt raised ($M)")
for cl, v in zip(YC.values(), [0, 0, 2500, 34500, 0, 0, 0, 0]):
    put(CF, f"{cl}22", v, color=BLUE, nf=NUM)
put(CF, "B23", "Debt balance (EoY)")
put(CF, "D23", "=D22", nf=NUM)
for cl in ["E","F","G","H","I","J","K"]:
    prev = chr(ord(cl) - 1)
    put(CF, f"{cl}23", f"={prev}23+{cl}22", nf=NUM)
put(CF, "B24", "Cash — BoY")
put(CF, "D24", 700, color=BLUE, nf=NUM)
for cl in ["E","F","G","H","I","J","K"]:
    prev = chr(ord(cl) - 1)
    put(CF, f"{cl}24", f"={prev}25", nf=NUM)
put(CF, "M24", "opening cash = pre-2023 raises net of pre-2023 burn (est.)", sz=8, italic=True)
put(CF, "B25", "Cash — EoY", bold=True)
for cl in YC.values():
    put(CF, f"{cl}25", f"={cl}24+{cl}21+{cl}22+{cl}13", bold=True, nf=NUM, border=B_TB)
put(CF, "B27", "Check: cum. equity − $124.3B [CANONICAL]")
put(CF, "D27", "=1600+SUM(D21:K21)-124300", nf=CHK)
put(CF, "F27", "(0 = ties · red = broken)", sz=8, italic=True)

banner(CF, 29, "Capitalization & Efficiency")
cap = [
    (31, "Total equity raised (cum., $M)", "=1600+SUM(D21:K21)", NUM, "Ruling 1 denominator"),
    (32, "Total debt ($M)", "=K23", NUM, "chip bonds + revolver"),
    (33, "Net cash — EoY 2026E ($M)", "=G25-G23", NUM, "feeds the DCF bridge"),
    (34, "CE — Jul-26 run-rate ÷ equity", "='01_Data'!C28/C31", MULT, "gross basis (Ruling 1)"),
    (35, "CE — equalized net ÷ equity", "=('01_Data'!C28*'00_Assumptions'!$D$22)/C31", MULT, "comparable to OpenAI 0.138x"),
]
for r, lab, f, nf, note in cap:
    put(CF, f"B{r}", lab, bold=(r in (31, 33)))
    put(CF, f"C{r}", f, nf=nf, bold=True)
    put(CF, f"E{r}", note, sz=8, italic=True)

# ============================== 06_VALUATION ==============================
banner(VA, 3, "Marks Ladder — what each round paid per $ of run-rate")
put(VA, "B5", "USD millions · multiples on GROSS run-rate unless noted", sz=9, italic=True)
for cl, h in zip(["B","C","D","E","F","G"], ["Round","Date","Post-money","RR at mark","EV / RR","Note"]):
    put(VA, f"{cl}7", h, bold=True, border=B_TB)
marks = [
    (8,  "Series E", "Mar-25", 61500, 2000, "RR est. (T3)"),
    (9,  "Series F", "Sep-25", 183000, 5000, "RR ~Aug-25 (T2)"),
    (10, "Series G", "Feb-26", 380000, 14000, "RR Feb-26 (T3)"),
    (11, "Series H", "May-26", 965000, 47000, "RR May-26 (T2)"),
]
for r, rd, dt_, post, rr, note in marks:
    put(VA, f"B{r}", rd); put(VA, f"C{r}", dt_, sz=9)
    put(VA, f"D{r}", post, color=BLUE, nf=NUM)
    put(VA, f"E{r}", rr, color=BLUE, nf=NUM)
    put(VA, f"F{r}", f"=D{r}/E{r}", nf=MULT)
    put(VA, f"G{r}", note, sz=8, italic=True)
put(VA, "B12", "Series H mark vs Jul-26 RR", bold=True)
put(VA, "C12", "Aug-26", sz=9)
put(VA, "D12", "=D11", nf=NUM, bold=True)
put(VA, "E12", "='01_Data'!C28", nf=NUM, bold=True)
put(VA, "F12", "=D12/E12", nf=MULT, bold=True, border=B_TB)
put(VA, "G12", "compression on growth alone", sz=8, italic=True)
put(VA, "B13", "   same, equalized NET (Ruling 5)", italic=True)
put(VA, "E13", "=E12*'00_Assumptions'!$D$22", nf=NUM)
put(VA, "F13", "=D12/E13", nf=MULT, bold=True)
put(VA, "G13", "was 34.1x at the May close", sz=8, italic=True)

banner(VA, 15, "Comps — equalized basis only (Ruling 5: never gross vs net)")
for cl, h in zip(["B","C","D","E","F","G"], ["Company","", "EV / mark","Net RR","EV / net RR","Note"]):
    put(VA, f"{cl}17", h, bold=True, border=B_TB)
put(VA, "B18", "OpenAI");    put(VA, "D18", 852000, color=BLUE, nf=NUM)
put(VA, "E18", 25000, color=BLUE, nf=NUM); put(VA, "F18", "=D18/E18", nf=MULT)
put(VA, "G18", "[STALE — Mar-26 mark, ~Jun-26 ARR · re-pull]", sz=8, italic=True, color=ORANGE)
put(VA, "B19", "Anthropic (equalized)"); put(VA, "D19", "=D12", nf=NUM)
put(VA, "E19", "=E13", nf=NUM); put(VA, "F19", "=D19/E19", nf=MULT, bold=True)
put(VA, "G19", "identical basis to OpenAI row", sz=8, italic=True)
put(VA, "B20", "Databricks"); put(VA, "D20", 134000, color=BLUE, nf=NUM)
put(VA, "E20", 5400, color=BLUE, nf=NUM); put(VA, "F20", "=D20/E20", nf=MULT)
put(VA, "G20", "[STALE — Feb-26 · reports net]", sz=8, italic=True, color=ORANGE)
put(VA, "B21", "xAI-in-SPCX: SOTP stale, Q2 printed Aug-6 [VERIFY] — excluded until re-pulled", sz=9, italic=True, color=ORANGE)

banner(VA, 23, "DCF — valuation date 31-Dec-2026 · active scenario")
unote(VA, 25)
yearrow(VA, 26)
put(VA, "B28", "Free cash flow ($M)")
for cl in YC.values(): put(VA, f"{cl}28", f"='05_Cash_Fund'!{cl}13", nf=NUM)
put(VA, "B29", "Discount period (yrs)")
for cl, t in zip(FC27, [1, 2, 3, 4]): put(VA, f"{cl}29", t, color=BLUE, align="center")
put(VA, "B30", "PV of FCF")
for cl in FC27:
    put(VA, f"{cl}30", f"={cl}28/(1+'00_Assumptions'!$G$17)^{cl}29", nf=NUM)
dcf = [
    (32, "PV of explicit FCF 2027E–2030E", "=SUM(H30:K30)", NUM, True, None),
    (33, "Terminal value — Gordon", "=K28*(1+'00_Assumptions'!$G$18)/('00_Assumptions'!$G$17-'00_Assumptions'!$G$18)", NUM, False, None),
    (34, "   PV of terminal (Gordon)", "=C33/(1+'00_Assumptions'!$G$17)^4", NUM, False, None),
    (35, "Terminal value — exit multiple", "=K28*'00_Assumptions'!$G$19", NUM, False, None),
    (36, "   PV of terminal (multiple)", "=C35/(1+'00_Assumptions'!$G$17)^4", NUM, False, None),
    (37, "Net cash — EoY 2026E", "='05_Cash_Fund'!C33", NUM, False, None),
    (39, "Equity value — Gordon ($M)", "=C32+C34+C37", NUM, True, B_TB),
    (40, "Equity value — exit multiple ($M)", "=C32+C36+C37", NUM, True, B_TB),
    (42, "Terminal as % of operating EV (Gordon)", "=C34/(C32+C34)", PCT, False, None),
    (43, "vs Series H $965B — Gordon", "=C39/965000-1", PCT, True, None),
    (44, "vs Series H $965B — exit multiple", "=C40/965000-1", PCT, True, None),
    (46, "Reverse-DCF: implied 2030E FCF multiple at $965B", "=(965000-C37-C32)*(1+'00_Assumptions'!$G$17)^4/K28", MULT, True, None),
]
for r, lab, f, nf, bold, bd in dcf:
    put(VA, f"B{r}", lab, bold=bold)
    put(VA, f"C{r}", f, nf=nf, bold=bold, border=bd)
put(VA, "B48", "FCF is basis-invariant: gross vs net revenue presentation changes multiples, never cash. 4-yr explicit window ⇒ terminal dominates — Gordon at ~3% understates a business still compounding double-digit into 2030; the exit multiple carries persistence. The two bracket the question.",
    sz=9, italic=True)
# ============================== 07_SENSITIVITY ==============================
banner(SN, 3, "Equity Value ($B) — Discount Rate × Terminal Growth (Gordon)")
put(SN, "B5", "Rebuilds the DCF at each (r, g) from the active-scenario FCF stream + net cash", sz=9, italic=True)
gcols = ["C","D","E","F","G"]; gvals = [.02, .025, .03, .035, .04]
rvals = [.14, .16, .18, .20, .22]
put(SN, "B7", "r \\ g", bold=True, border=B_TB, align="center")
for cl, g in zip(gcols, gvals):
    put(SN, f"{cl}7", g, color=BLUE, nf=PCT, bold=True, border=B_TB, align="center")
for i, rr_ in enumerate(rvals):
    r = 8 + i
    put(SN, f"B{r}", rr_, color=BLUE, nf=PCT, bold=True, align="center")
    for cl in gcols:
        f = (f"=('06_Valuation'!$H$28/(1+$B{r})^1+'06_Valuation'!$I$28/(1+$B{r})^2"
             f"+'06_Valuation'!$J$28/(1+$B{r})^3+'06_Valuation'!$K$28/(1+$B{r})^4"
             f"+('06_Valuation'!$K$28*(1+{cl}$7)/($B{r}-{cl}$7))/(1+$B{r})^4"
             f"+'06_Valuation'!$C$37)/1000")
        put(SN, f"{cl}{r}", f, nf=NUM)
put(SN, "I8", "Base cell: r 18.0% × g 3.0% (Base scenario)", sz=9, italic=True)
put(SN, "I9", "$965B mark = Series H, May-26", sz=9, italic=True)

banner(SN, 15, "Equity Value ($B) — Multiple × 2027E Net Revenue")
put(SN, "B17", "x \\ $B", bold=True, border=B_TB, align="center")
nrev = [50000, 70000, 90000, 110000, 130000]
for cl, v in zip(gcols, nrev):
    put(SN, f"{cl}17", v/1000, color=BLUE, nf=NUM, bold=True, border=B_TB, align="center")
for i, m in enumerate([10, 15, 20, 25, 30]):
    r = 18 + i
    put(SN, f"B{r}", m, color=BLUE, nf=MULT, bold=True, align="center")
    for cl in gcols:
        put(SN, f"{cl}{r}", f"=({cl}$17*1000*$B{r}+'06_Valuation'!$C$37)/1000", nf=NUM)
put(SN, "B24", "Model 2027E net revenue (active scenario, $B):", italic=True)
put(SN, "D24", "='02_Revenue'!H19/1000", nf=NUM, bold=True)
put(SN, "B26", "The model computes one scenario at a time — flip 00_Assumptions!D7 to compare. Grids above are scenario-invariant only through the FCF stream they reference.",
    sz=9, italic=True)

# ============================== 08_OUTPUT ==============================
banner(OU, 3, "Dashboard — What Must Be True for $965B?")
put(OU, "B5", "USD millions unless noted · active scenario:", sz=9, italic=True)
put(OU, "D5", "='00_Assumptions'!D8", sz=9, bold=True)
kpi = [
    (7,  "Run-rate — end-Jul 2026 (gross)", "='01_Data'!C28", NUM, "T2 · CNBC/Bloomberg/Fortune, Aug 17–18"),
    (8,  "Mark ÷ run-rate — gross / equalized", "='06_Valuation'!F12", MULT, "equalized in E — was 20.5x / 34.1x in May"),
    (9,  "2026E recognized revenue", "='02_Revenue'!G17", NUM, "derived, log-mean of the exit curve"),
    (10, "2027E recognized revenue", "='02_Revenue'!H17", NUM, "every scenario floors high — usage momentum"),
    (11, "EBIT 2027E", "='04_PL'!H20", NUM, "margin plan 63% doing the lifting"),
    (12, "FCF 2027E", "='05_Cash_Fund'!H13", NUM, "vs WSJ −$25B trough (Apr-26 vintage) — re-based"),
    (13, "Equity value — Gordon", "='06_Valuation'!C39", NUM, "floor-ish: terminal ignores post-2030 compounding"),
    (14, "Equity value — exit multiple", "='06_Valuation'!C40", NUM, "growth-persistence case"),
    (15, "vs $965B — Gordon / exit multiple", "='06_Valuation'!C43", PCT, "exit-multiple case in E"),
    (16, "Reverse-DCF: implied 2030E FCF multiple", "='06_Valuation'!C46", MULT, "what the mark actually requires"),
    (17, "CE — equalized net RR ÷ equity", "='05_Cash_Fund'!C35", MULT, "OpenAI comp: 0.138x (Ruling 1)"),
]
for r, lab, f, nf, note in kpi:
    put(OU, f"B{r}", lab, bold=True)
    put(OU, f"D{r}", f, nf=nf, bold=True)
    put(OU, f"F{r}", note, sz=8, italic=True)
put(OU, "E8", "='06_Valuation'!F13", nf=MULT, bold=True)
put(OU, "E15", "='06_Valuation'!C44", nf=PCT, bold=True)
mbt = [
    "1 · GROWTH — YE-26 exit ~$110B, then +50/+32/+22/+15% (Base). Usage revenue is not contracted ARR: durability is the bet.",
    "2 · MARGINS — 40% (2025A) → 77% (2028E company plan) against price deflation, cloud rev-share, and inference-cost curves.",
    "3 · COMPUTE — training spend scales to ~$45B/yr by 2030E and operating leverage still shows through.",
    "4 · BASIS — a gross→net SEC restatement (Ruling 5: ×60.25%) moves multiples ~40%, and cash not at all.",
]
for i, t in enumerate(mbt):
    put(OU, f"B{19+i}", t, sz=9)

# ============================== COVER ==============================
put(cover, "C11", "Anthropic — Operating Model & Valuation", sz=20, bold=True, color=TITLE_BLUE)
put(cover, "C12", "Teaching build v1.0 · 2026-08-19 · data: anthropic-model/DATA_PACK.md · all facts tiered on 01_Data", sz=10)
put(cover, "C14", "Table of Contents", sz=14, bold=True, color=NAVY, border=Border(bottom=thin))
toc = ["00_Assumptions — drivers, scenario switch, timeline", "01_Data — facts only, tiered",
       "02_Revenue — run-rate curve → recognized revenue", "03_Costs — GM path, compute, opex",
       "04_PL — dual-basis P&L, NOL schedule", "05_Cash_Fund — FCF, cash walk, capitalization",
       "06_Valuation — marks ladder, comps, DCF", "07_Sensitivity — r × g and multiple grids",
       "08_Output — dashboard & charts"]
for i, t in enumerate(toc):
    put(cover, f"C{16+i}", t, sz=12)
put(cover, "H14", "Model Checks (0 = OK)", sz=14, bold=True, color=NAVY, border=Border(bottom=thin))
checks = [
    ("Cumulative equity ties to $124.3B [CANONICAL]?", "='05_Cash_Fund'!D27"),
    ("2026E recognized within run-rate bounds?", "=IF(AND('02_Revenue'!G17>='02_Revenue'!F9,'02_Revenue'!G17<='02_Revenue'!G9),0,1)"),
    ("Terminal < 95% of operating EV (Gordon)?", "=IF('06_Valuation'!C42<0.95,0,1)"),
    ("P&L identity: GP − opex − EBIT = 0 (2030E)?", "='04_PL'!K11-'04_PL'!K18-'04_PL'!K20"),
    ("Cash walk continuity (EoY30 = BoY23 + Σflows)?", "='05_Cash_Fund'!K25-('05_Cash_Fund'!D24+SUM('05_Cash_Fund'!D21:K21)+SUM('05_Cash_Fund'!D22:K22)+SUM('05_Cash_Fund'!D13:K13))"),
]
for i, (lab, f) in enumerate(checks):
    put(cover, f"H{16+i}", lab, sz=10)
    put(cover, f"I{16+i}", f, nf=CHK, bold=True, align="center")
put(cover, "H23", "Colour Key", sz=12, bold=True, color=NAVY)
put(cover, "H24", "Blue — hardcoded input (fact or belief)", sz=10, color=BLUE)
put(cover, "H25", "Black — formula (logic only)", sz=10)
put(cover, "H26", "Orange — flagged: DISPUTED / VERIFY / STALE / rumor", sz=10, color=ORANGE)
put(cover, "H27", "Bold driver rows — active scenario (switch: 00_Assumptions!D7)", sz=10, bold=True)
for cl in ["C","D","E","F","G","H","I"]:
    cover[f"{cl}31"].fill = PatternFill("solid", fgColor=TITLE_BLUE)
put(cover, "C31", "HYPD · Harrison Rolfes — educational estimate built from public/reported data; not investment advice.",
    sz=10, bold=True, color=WHITE, fill=TITLE_BLUE)

# ============================== CHARTS (08_Output) ==============================
from openpyxl.chart import BarChart, LineChart, Reference, Series
ch1 = BarChart(); ch1.type = "col"; ch1.style = 10
ch1.title = "Recognized Revenue vs EBIT ($M)"
cats = Reference(PL, min_col=4, max_col=11, min_row=7, max_row=7)
s_rev = Series(Reference(PL, min_col=4, max_col=11, min_row=9, max_row=9), title="Revenue (gross)")
s_ebit = Series(Reference(PL, min_col=4, max_col=11, min_row=20, max_row=20), title="EBIT")
ch1.append(s_rev); ch1.append(s_ebit); ch1.set_categories(cats)
ch1.series[0].graphicalProperties.solidFill = "3271D2"
ch1.series[1].graphicalProperties.solidFill = "132E57"
ch1.width = 15.5; ch1.height = 8.5
OU.add_chart(ch1, "B25")

ch2 = LineChart(); ch2.style = 10
ch2.title = "Exit Run-Rate Path — gross vs equalized net ($M)"
s_g = Series(Reference(RV, min_col=4, max_col=11, min_row=9, max_row=9), title="Gross run-rate")
s_n = Series(Reference(RV, min_col=4, max_col=11, min_row=11, max_row=11), title="Net (equalized)")
ch2.append(s_g); ch2.append(s_n); ch2.set_categories(cats)
ch2.series[0].graphicalProperties.line.solidFill = "3271D2"; ch2.series[0].graphicalProperties.line.width = 28000
ch2.series[1].graphicalProperties.line.solidFill = "FA621C"; ch2.series[1].graphicalProperties.line.width = 20000
ch2.width = 15.5; ch2.height = 8.5
OU.add_chart(ch2, "G25")

OUT = "/home/user/pitchbook-analyst-agent/anthropic-model/Anthropic_Model_v1.xlsx"
wb.save(OUT)
print("saved", OUT)
