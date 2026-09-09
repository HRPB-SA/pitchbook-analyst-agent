# tabs_a2.py: Workbook A: 02_Revenue, 09_Obligations, 03_Costs, 04_PL.
from xlhelp import *
from tabs_a1 import ck


def hc_note(haircut_ref):
    return f"={haircut_ref}"


# ----------------------------------------------------------------------------------------------------
# 02_Revenue
# ----------------------------------------------------------------------------------------------------
def build_02(sh):
    sh.put("A1", "02_Revenue: run-rate ladders (dated), recognized quarterly and annual revenue, the PB forward projection block (Ruling 4, never current), the gross-to-net restatement (E5), the FY2026E integrations (check block), annual revenue paths 2023A-2030E.", kind="note")
    sh.header(3, ["Item", "Unit", "Source (row · status · tier · as-of · basis)", "Date / period", "Value", "Basis tag", "Note"])
    sh.section(5, "RUN-RATE LADDERS (DATED) AND RECOGNIZED REVENUE (Exhibit E4; A5:K31)", ncols=11)
    lad = [
        (6, "Anthropic run-rate, end-2025", "$M/yr", "L-139 · confirmed · T1 · 2025-12 · GROSS run-rate", "2025-12", f"={R('A01a')}", "GROSS", "RR_A_DEC25"),
        (7, "Anthropic run-rate, April 6 2026", "$M/yr", "L-139 · confirmed · T1 · 2026-04-06 · GROSS run-rate", "2026-04-06", f"={R('A01b')}", "GROSS", "RR_A_APR"),
        (8, "Anthropic run-rate, early May 2026", "$M/yr", "L-037 · confirmed · T1 · 2026-05 · GROSS run-rate", "2026-05", f"={R('A01c')}", "GROSS", "RR_A_MAY"),
        (9, "Anthropic run-rate, end-July 2026 (LB01)", "$M/yr", "L-032 · confirmed · T2 · 2026-07-31 · GROSS run-rate", "2026-07-31", "=LB01", "GROSS", "RR_A_JUL"),
        (11, "OpenAI run-rate, end-2025 ('>20,000')", "$M/yr", "L-065 · confirmed · T2 · 2025-12 · basis unstated", "2025-12", f"={R('O03')}", "unstated (NET assumed)", "RR_O_DEC25"),
        (12, "OpenAI run-rate, March 2026 (~2,000 monthly x 12)", "$M/yr", "L-063 · confirmed · T2 · 2026-03 · monthly revenue at the March round", "2026-03", f"={R('O03b')}*{R('MPY')}", "unstated (NET assumed)", "RR_O_MAR"),
        (13, "OpenAI run-rate, July 2026 (LB02; floor '>40')", "$M/yr", "L-065 · confirmed · T2 · 2026-07 · basis unstated (SW_OAI_BASIS)", "2026-07", "=LB02", "unstated (NET assumed; SW_OAI_BASIS)", "RR_O_JUL"),
        (14, "OpenAI run-rate growth quarter-to-date (CFO, Aug-19; colour)", "text", "L-069 · confirmed · T2 · 2026-08-19 · all-hands relay", "2026-08-19", f"={R('O03c')}", "text", None),
        (17, "Anthropic Q2-2025 revenue (comparator)", "$M", "L-151 · confirmed · T2 · Q2-2025 · recognized", "Q2-2025", f"={R('A03b')}", "GROSS presumed", "Q2A25"),
        (18, "Anthropic Q1-2026 revenue", "$M", "L-151 · confirmed · T2 · Q1-2026 · recognized, GROSS presumed", "Q1-2026", f"={R('A03')}", "GROSS presumed", "Q1A"),
        (19, "Anthropic Q2-2026 revenue, preliminary (LB05a)", "$M", "L-033 · confirmed · T2 · Q2-2026 · recognized, preliminary, GROSS presumed", "Q2-2026", "=LB05a", "GROSS presumed", "Q2A"),
        (21, "OpenAI Q1-2026 revenue", "$M", "L-066 · confirmed · T2 · Q1-2026 · recognized, NET presumed", "Q1-2026", f"={R('LB06a_Q1')}", "NET presumed", "Q1O"),
        (22, "OpenAI Q2-2026 revenue (LB06a)", "$M", "L-066 · confirmed · T2 · Q2-2026 · recognized, NET presumed", "Q2-2026", "=LB06a", "NET presumed", "Q2O"),
        (24, "Anthropic FY2024 revenue", "$M", "L-012 · estimated · T2 · FY2024 · PB deal-record financials", "FY2024", f"={R('A05_rev')}", "basis unstated", "FY24A"),
        (25, "Anthropic FY2025 recognized revenue (SW_A_FY25; C-03)", "$M", "L-010 / L-120 · estimated / recalled · T2 / T4 · FY2025 · PB field = exit run-rate vs implied 4,500-6,000", "FY2025", "=SW_A_FY25", "GROSS presumed; C-03 switch", "FY25A"),
        (26, "OpenAI FY2025 revenue", "$M", "L-063 · confirmed · T2 · FY2025 · NET presumed; FT-verified 13,070", "FY2025", f"={R('O01')}", "NET presumed", "FY25O"),
    ]
    for rr, lab, unit, src, per, f, basis, key in lad:
        sh.put(f"A{rr}", lab); sh.put(f"B{rr}", unit, kind="note"); sh.put(f"C{rr}", src, kind="note"); sh.put(f"D{rr}", per, kind="note", align="center")
        sh.put(f"E{rr}", f, kind="formula", nf=(GEN if unit == "text" else NUM), key=key); sh.put(f"F{rr}", basis, kind="note")
    sh.put("A10", "   Anthropic run-rate multiple, end-2025 to end-July"); sh.put("E10", "=E9/E6", kind="formula", nf=MULT, key="RR_A_MULT")
    sh.put("A15", "   OpenAI run-rate multiple, end-2025 to July"); sh.put("E15", "=E13/E11", kind="formula", nf=MULT)
    sh.put("A20", "   Anthropic Q2 / Q1 (check 2.45x)"); sh.put("E20", "=E19/E18", kind="formula", nf=MULT2, key="Q2Q1"); ck(sh, "G20", "E20", "Q2Q1")
    sh.put("A23", "   OpenAI Q2 / Q1 - 1 (+18% per WSJ)"); sh.put("E23", "=E22/E21-1", kind="formula", nf=PCT, key="QOQO")
    sh.put("F25", "=SW_A_FY25", kind="formula", nf=NUM); sh.put("G25", "switch value visible (C-03)", kind="note")
    sh.section(28, "PB FORWARD PROJECTION (Ruling 4), never current: PB TTM fields are recognized-estimates (2022-2025) and projections (2026-2027); no cell labelled current reads them", ncols=11)
    for i, y in enumerate(range(2022, 2028)):
        col = "DEFGHI"[i]
        sh.put(f"{col}29", str(y), kind="header", align="center")
    sh.put("A29", "PB series (year)", kind="header"); sh.put("C29", "L-010, L-009 (Anthropic); L-025, L-024 (OpenAI) · estimated · T2 · pulled 2026-09-09", kind="note")
    sh.put("A30", "Anthropic PB revenue series"); sh.put("B30", "$M", kind="note")
    for i, y in enumerate(range(2022, 2028)):
        sh.put(f"{'DEFGHI'[i]}30", f"={R(f'A04_{y}')}", kind="formula", nf=NUM)
    sh.put("A31", "OpenAI PB revenue series (2025 = run-rate vintage, C-06; 2026 = projection)"); sh.put("B31", "$M", kind="note")
    for i, y in enumerate(range(2023, 2027)):
        sh.put(f"{'EFGH'[i]}31", f"={R(f'O04_{y}')}", kind="formula", nf=NUM)
    sh.put("J30", "2026-2027 fields are FORWARD projections", kind="flag"); sh.put("J31", "PB NI rows (T4) not carried", kind="note")

    # Gross to net
    sh.section(33, "GROSS TO NET RESTATEMENT AT BOTH HAIRCUTS; OPENAI BASIS SWITCH (Exhibit E5; A35:H50). Every net figure shows its haircut in column E (Ruling 5).", ncols=11)
    sh.header(34, ["Item", "Unit", "Source / basis", "Value", "Haircut / basis visible", "Note"])
    gn = [
        (35, "Anthropic run-rate GROSS (LB01)", "=LB01", "GROSS", None, NUM),
        (36, "Haircut in use (SW_HAIRCUT; C-13)", "=SW_HAIRCUT", "=SW_HAIRCUT", "HC_LIVE", PCT2),
        (37, "Anthropic net run-rate at SW_HAIRCUT", "=LB01*(1-SW_HAIRCUT)", "=SW_HAIRCUT", "NET_A_LIVE", NUM),
        (38, "Anthropic net run-rate at 39.75% (R01, Ruling 5)", f"=LB01*(1-{R('R01')})", f"={R('R01')}", "NET_A_3975", NUM),
        (39, "Anthropic net run-rate at 27% (R02, C-13 external)", f"=LB01*(1-{R('R02')})", f"={R('R02')}", "NET_A_27", NUM),
        (40, "Anthropic net run-rate at the OTHER haircut (the one SW_HAIRCUT does not select)", f"=IF(SW_HAIRCUT={R('R01')},D39,D38)", f"=IF(SW_HAIRCUT={R('R01')},{R('R02')},{R('R01')})", "NET_A_OTHER", NUM),
        (41, "OpenAI run-rate as reported (LB02; basis unstated)", "=LB02", "unstated", None, NUM),
        (42, "OpenAI basis switch (SW_OAI_BASIS; C-16)", "=SW_OAI_BASIS", "=SW_OAI_BASIS", "OAI_BASIS_LIVE", GEN),
        (43, "OpenAI net run-rate at SW_OAI_BASIS (GROSS case applies R03 = 20%, T4, flagged)", f'=IF(SW_OAI_BASIS="NET",LB02,LB02*(1-{R("R03")}))', f'=IF(SW_OAI_BASIS="NET",0,{R("R03")})', "NET_O_LIVE", NUM),
        (44, "OpenAI net run-rate, NET case (LB02 as reported)", "=LB02", "0% (NET presumed)", "NET_O_NETCASE", NUM),
        (45, "OpenAI net run-rate, GROSS case (LB02 x (1 - R03); R03 is T4 and NEVER printed as a fact)", f"=LB02*(1-{R('R03')})", f"={R('R03')}", "NET_O_GROSSCASE", NUM),
        (46, "Anthropic Q2-2026 revenue GROSS (LB05a)", "=LB05a", "GROSS presumed", None, NUM),
        (47, "Anthropic Q2-2026 net at 39.75%", f"=LB05a*(1-{R('R01')})", f"={R('R01')}", "Q2A_NET3975", NUM),
        (48, "Anthropic Q2-2026 net at 27%", f"=LB05a*(1-{R('R02')})", f"={R('R02')}", "Q2A_NET27", NUM),
        (49, "OpenAI Q2-2026 revenue (LB06a; NET presumed)", "=LB06a", "NET presumed", None, NUM),
        (50, "Anthropic Q2 net (39.75%) / OpenAI Q2; at 27% in column F", "=D47/D49", f"={R('R01')}", "Q2_RATIO", MULT2),
    ]
    for rr, lab, f, hc, key, nf in gn:
        sh.put(f"A{rr}", lab); sh.put(f"B{rr}", "$M/yr" if rr < 46 else "$M", kind="note")
        sh.put(f"C{rr}", "L-032 / L-065 / L-126 / L-033 / L-066 (see 01_Data rows)", kind="note")
        sh.put(f"D{rr}", f, kind="formula", nf=nf, key=key, bold=True)
        if isinstance(hc, str) and hc.startswith("="):
            sh.put(f"E{rr}", hc, kind="formula", nf=(GEN if rr == 42 else PCT2))
        else:
            sh.put(f"E{rr}", hc, kind="note")
    sh.put("E45", f"={R('R03')}", kind="hole", nf=PCT); sh.put("F45", "T4 (L-052 notes)", kind="flag")
    sh.put("F50", "=D48/D49", kind="formula", nf=MULT2); sh.put("G50", "at 27%", kind="note")
    ck(sh, "F38", "D38", "NETRR")

    # FY2026E Anthropic integration
    sh.section(52, "FY2026E INTEGRATION, ANTHROPIC: linear monthly ramp from the July run-rate (LB01/12) to the YE expectation; Q3 = Jul+Aug+Sep; Q4 = Oct+Nov+Dec; FY2026E = Q1 (A03) + Q2 (LB05a) + Q3 + Q4", ncols=14)
    sh.header(53, ["Case", "YE run-rate", "Source", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Q3", "Q4", "H1 (A03 + LB05a)", "FY2026E", "Monthly step", "Check vs spec"])
    cases = [(54, "Live scenario (SW_SCEN via YE26 driver)", f"={R('YE26')}", "00_Assumptions YE26", "FY26A", None),
             (55, "Check: YE 100,000 (L-035 low)", f"={R('A02_low')}", "L-035 · estimated · T3", "FY26A_100", "FY26_100"),
             (56, "Check: YE 120,000 (L-035 high)", f"={R('A02_high')}", "L-035 · estimated · T3", "FY26A_120", "FY26_120"),
             (57, "Check: flat from July (LB01)", "=LB01", "L-032 · confirmed · T2", "FY26A_FLAT", "FY26_FLAT")]
    for rr, lab, ye, src, key, chk in cases:
        sh.put(f"A{rr}", lab); sh.put(f"B{rr}", ye, kind="formula", nf=NUM); sh.put(f"C{rr}", src, kind="note")
        sh.put(f"D{rr}", f"=LB01/{R('MPY')}", kind="formula", nf=NUM)
        sh.put(f"I{rr}", f"=B{rr}/{R('MPY')}", kind="formula", nf=NUM)
        sh.put(f"N{rr}", f"=(I{rr}-D{rr})/{R('RAMPSTEPS')}", kind="formula", nf=NUM)
        sh.put(f"E{rr}", f"=D{rr}+$N{rr}", kind="formula", nf=NUM); sh.put(f"F{rr}", f"=E{rr}+$N{rr}", kind="formula", nf=NUM)
        sh.put(f"G{rr}", f"=F{rr}+$N{rr}", kind="formula", nf=NUM); sh.put(f"H{rr}", f"=G{rr}+$N{rr}", kind="formula", nf=NUM)
        sh.put(f"J{rr}", f"=SUM(D{rr}:F{rr})", kind="formula", nf=NUM, key=(f"Q3A" if rr == 54 else None))
        sh.put(f"K{rr}", f"=SUM(G{rr}:I{rr})", kind="formula", nf=NUM, key=(f"Q4A" if rr == 54 else None))
        sh.put(f"L{rr}", f"={R('A03')}+LB05a", kind="formula", nf=NUM, key=("H1A" if rr == 54 else None))
        sh.put(f"M{rr}", f"=L{rr}+J{rr}+K{rr}", kind="formula", nf=NUM, bold=True, key=key)
        if chk:
            ck(sh, f"O{rr}", f"M{rr}", chk)
    sh.put("A58", "   H1-2026 check (16,330) and Q2/Q1 (2.45x)"); sh.put("L58", "=L54", kind="formula", nf=NUM); ck(sh, "O58", "L58", "H1A")
    sh.put("A59", "   H1-2026 on the '>11,500' print (L-151): A03 + LB05a_low"); sh.put("L59", f"={R('A03')}+{R('LB05a_low')}", kind="formula", nf=NUM, key="H1A_LOW")
    sh.put("A60", "   Q3 / Q4 in the live scenario as a share of FY2026E"); sh.put("J60", "=J54/M54", kind="formula", nf=PCT); sh.put("K60", "=K54/M54", kind="formula", nf=PCT)

    # FY2026E OpenAI integration
    sh.section(62, "FY2026E INTEGRATION, OPENAI: monthly from LB02/12 in July, compounding at the H2 monthly growth driver; FY2026E = Q1 + Q2 (L-066) + Q3 + Q4", ncols=14)
    sh.header(63, ["Case", "Monthly growth", "Source", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Q3", "Q4", "H1 (L-066)", "FY2026E", "", "Check vs spec"])
    ocases = [(64, "Live scenario (SW_SCEN via OAIG driver)", f"={R('OAIG')}", "FY26O", None),
              (65, "Check: 0% (Bear)", f"={R('OAIG_BEAR')}", "FY26O_0", "OAI_0"),
              (66, "Check: 10% (Base)", f"={R('OAIG_BASE')}", "FY26O_10", "OAI_10"),
              (67, "Check: 20% (Bull)", f"={R('OAIG_BULL')}", "FY26O_20", "OAI_20")]
    for rr, lab, g, key, chk in ocases:
        sh.put(f"A{rr}", lab); sh.put(f"B{rr}", g, kind="formula", nf=PCT); sh.put(f"C{rr}", "L-065 (T2) July >40,000; growth AJ", kind="note")
        sh.put(f"D{rr}", f"=LB02/{R('MPY')}", kind="formula", nf=NUM)
        for i, col in enumerate("EFGHI"):
            prev = "DEFGH"[i]
            sh.put(f"{col}{rr}", f"={prev}{rr}*(1+$B{rr})", kind="formula", nf=NUM)
        sh.put(f"J{rr}", f"=SUM(D{rr}:F{rr})", kind="formula", nf=NUM); sh.put(f"K{rr}", f"=SUM(G{rr}:I{rr})", kind="formula", nf=NUM)
        sh.put(f"L{rr}", f"={R('LB06a_Q1')}+LB06a", kind="formula", nf=NUM, key=("H1O" if rr == 64 else None))
        sh.put(f"M{rr}", f"=L{rr}+J{rr}+K{rr}", kind="formula", nf=NUM, bold=True, key=key)
        if chk:
            ck(sh, f"O{rr}", f"M{rr}", chk)

    # Annual paths
    sh.section(69, "ANNUAL REVENUE PATHS 2023A-2030E (feeds 03_Costs, 04_PL, 09_Obligations, 07_Sensitivity). 2029E-2030E Anthropic = Bessemer endurance on the 2028 growth rate (B01, L-161).", ncols=11)
    sh.yearhdr(70, label="Item")
    sh.put("B70", "Unit", kind="header"); sh.put("C70", "Source / basis", kind="header")
    tsrow(sh, 71, "REVA", "Anthropic revenue GROSS (2023 HOLE: PB 100 is a recognized-estimate in the projection block, not carried as an actual)", "$M", "L-012 (2024) / SW_A_FY25 (2025) / FY2026E integration / AJ 2027-2028 / B01 tails",
          {2023: "HOLE", 2024: f"={R('A05_rev')}", 2025: "=SW_A_FY25", 2026: "=M54", 2027: f"={R('REV27')}", 2028: f"={R('REV28')}",
           2029: f"=I71*(1+{R('ENDUR')}*(I71/H71-1))", 2030: f"=J71*(1+{R('ENDUR')}*(J71/I71-1))"}, bold=True)
    tsrow(sh, 72, None, "   growth YoY", "fraction", None, {y: f"=IFERROR({YC[y]}71/{YC[y-1]}71-1,\"n/a\")" for y in range(2025, 2031)}, nf=PCT)
    sh.put("A73", "   Bessemer tails by scenario (check block; the live row above uses the SW_SCEN scenario)", kind="note")
    tails = [(74, "Bear", "REV27_BEAR", "REV28_BEAR", "ENDUR_BEAR", "TAIL_BEAR29", "TAIL_BEAR30"),
             (75, "Base", "REV27_BASE", "REV28_BASE", "ENDUR_BASE", "TAIL_BASE29", "TAIL_BASE30"),
             (76, "Bull", "REV27_BULL", "REV28_BULL", "ENDUR_BULL", "TAIL_BULL29", "TAIL_BULL30")]
    for rr, lab, k27, k28, ke, c29, c30 in tails:
        sh.put(f"A{rr}", f"   {lab}: 2027 / 2028 / growth 2028 / 2029 / 2030"); sh.put(f"B{rr}", "$M", kind="note"); sh.put(f"C{rr}", "AJ 2027-2028; B01 endurance on the 2028 growth rate", kind="note")
        sh.put(f"H{rr}", f"={R(k27)}", kind="formula", nf=NUM); sh.put(f"I{rr}", f"={R(k28)}", kind="formula", nf=NUM)
        sh.put(f"G{rr}", f"=I{rr}/H{rr}-1", kind="formula", nf=PCT)
        sh.put(f"J{rr}", f"=I{rr}*(1+{R(ke)}*G{rr})", kind="formula", nf=NUM, key=f"TAIL29_{lab.upper()}")
        sh.put(f"K{rr}", f"=J{rr}*(1+{R(ke)}*(J{rr}/I{rr}-1))", kind="formula", nf=NUM, key=f"TAIL30_{lab.upper()}")
        ck(sh, f"L{rr}", f"J{rr}", c29); ck(sh, f"M{rr}", f"K{rr}", c30)
    tsrow(sh, 77, "REVAN", "Anthropic revenue NET at SW_HAIRCUT (haircut visible in C)", "$M", "=SW_HAIRCUT",
          {y: f"={YC[y]}71*(1-SW_HAIRCUT)" for y in range(2024, 2031)}, srckind="formula")
    sh.put("C77", "=SW_HAIRCUT", kind="formula", nf=PCT2)
    tsrow(sh, 78, "REVO", "OpenAI revenue (NET presumed): 2025 = O01; 2026 = FY2026E integration; 2027E+ compound at OAICAGR", "$M", "L-063 (2025) / L-066 + L-065 (2026) / AJ CAGR 40-100%",
          {2023: "HOLE", 2024: "HOLE", 2025: f"={R('O01')}", 2026: "=M64", 2027: f"=G78*(1+{R('OAICAGR')})", 2028: f"=H78*(1+{R('OAICAGR')})", 2029: f"=I78*(1+{R('OAICAGR')})", 2030: f"=J78*(1+{R('OAICAGR')})"}, bold=True)
    tsrow(sh, 79, None, "   growth YoY", "fraction", None, {y: f"=IFERROR({YC[y]}78/{YC[y-1]}78-1,\"n/a\")" for y in range(2026, 2031)}, nf=PCT)
    sh.put("A81", "Ruling 4: no PB TTM field feeds any cell labelled current; the projection block (rows 28-31) is its only home. Ruling 5: every net figure carries its haircut in the adjacent cell.", kind="note")
    sh.ws.freeze_panes = "D4"


# ----------------------------------------------------------------------------------------------------
# 09_Obligations
# ----------------------------------------------------------------------------------------------------
SCHED_START = 101
YCOLS = {2023: "U", 2024: "V", 2025: "W", 2026: "X", 2027: "Y", 2028: "Z", 2029: "AA", 2030: "AB"}


def build_09(sh):
    sh.put("A1", "09_Obligations: contract schedule (A100:AD127; one row per commitment), contracted / cash / cancellable tables (E6 A5:J20, E7 A25:J40), tally reconciliation (E8 A45:H58), annualized priced run by year (E3 A60:K75; SUMIFS over the schedule), envelope-vs-commitments chart data (E10 A80:K98). Every total/term/GW links 01_Data or 00_Assumptions; nothing typed here.", kind="note")
    mpy = R("MPY")
    S = SCHED_START
    # ---------------- schedule ----------------
    sh.section(99, "CONTRACT SCHEDULE (A100:AD127): ID · company · counterparty · layer · start · end · term · total · annual value · GW/MW · cancellability · flag · backstop · tier · row · scope · in priced run · first-year factor · month indices · annual values by year · cancellable $ · note", ncols=30)
    hdr = ["ID", "Company", "Counterparty", "Layer", "Start", "End", "Term (yrs)", "Total ($M)", "Annual value ($M)", "GW / MW", "Cancellability (text)", "Cancel flag", "Backstop (text)", "Tier", "Row",
           "Scope (DOC / SPV / REPORTED / UNPRICED / RECALLED / PROXY / INFLOW / OVERLAP)", "In priced run", "First-year factor", "Start idx", "End idx"]
    sh.header(100, hdr)
    for y in YEARS:
        sh.put(f"{YCOLS[y]}100", f"={R(f'YR|{y}')}", kind="link", bold=True, nf=GEN, align="center", border=B_TB)
    sh.put("AC100", "Cancellable $", kind="header"); sh.put("AD100", "Note", kind="header")
    # (id, company, counterparty, layer, start_key, term_expr, end_key, total_expr, annual_expr, gw, canc, flag, backstop, tier, row, scope, run, factor_expr, cancellable_expr, note)
    rows = [
        ("C01", "Anthropic", "AWS", "L2", "AWSSTART", f"={R('C01_term')}", None, f"={R('C01_tot')}", "=H{r}/G{r}", "up to 5 GW; ~1 GW Trainium by end-2026", "take-or-pay status not disclosed; treat as contracted", "NONE-DISCLOSED", "Amazon is investor and supplier; equity 13,000 invested, up to 20,000 more on milestones (inflow)", "T1", "L-072", "DOC", "RUN", 1, None, "straight-line 10,000 per year 2026-2035"),
        ("C02", "Anthropic", "Azure", "L2", "AZSTART", f"={R('AZTERM')}", None, f"={R('C02_tot')}", "=H{r}/G{r}", "up to 1 GW", "none disclosed", "NONE-DISCLOSED", "Microsoft equity up to 5,000 (funded; 3,200 gain at MSFT)", "T1", "L-074", "DOC", "RUN", 1, None, "term not stated; AJ 5 yrs from 2026"),
        ("C03", "Anthropic", "SpaceX COLOSSUS / COLOSSUS II", "L2", "SPACEXSTART", "=(T{r}-S{r}+1)/" + mpy, "C03_end", "=I{r}*G{r}", f"={R('C03_monthly')}*{mpy}", "MW not stated", "entire contract terminable by either party on 90 days' notice: contracted at any moment = 3 months", "FULL 90-day", "SpaceX bought ~2,000 of gas turbines for its DCs", "T1", "L-046", "DOC", "RUN", f"={R('RAMP')}", f"=H{{r}}-I{{r}}/{mpy}*{R('C03_notice_m')}", "2026 = 7 months x 0.9 ramp; 2027-2028 = 15,000; 2029 = 5 months"),
        ("C04", "Anthropic", "Fluidstack", "L2", None, None, None, f"={R('C04_tot')}", "HOLE", "site MW not disclosed", "spend commitment, not a customer contract; phasing beyond 2026 undisclosed (L-168: 'throughout 2026')", "NONE-DISCLOSED", "Google conditional support on project debt (L-045)", "T1", "L-076, L-168", "DOC", "EXCL", 1, None, "phasing HOLE: excluded from the annual priced run"),
        ("C05", "Anthropic", "Nscale", "L2", "NSCALESTART", f"={R('C05_term')}", None, f"={R('C05_tot')}", "=H{r}/G{r}", "~460 MW Vera Rubin", "terms not published [VERIFY]; 460 MW is T3/T4", "NONE-DISCLOSED", "not disclosed", "T2", "L-135", "DOC", "RUN", 1, None, "capacity from late-2027: 2027 = 25% year"),
        ("C06", "Anthropic", "Lambda (Beacon Point)", "L2", "LAMSTART", f"={R('LAMTERM')}", None, f"={R('C06_tot')}", "=H{r}/G{r}", "~350 MW; landlord lease 15 yr / 704 MW / 19,600 base-term (L-167)", "Anthropic-Lambda term HOLE (AJ 6 yrs, flagged); landlord lease 15 yr", "NONE-DISCLOSED", "Nvidia holds the datacenter lease (Bloomberg); Hut 8 landlord; tenant Nvidia per FT relay", "T2 / T1", "L-137, L-167", "DOC", "RUN", 1, None, "landlord-lease columns: see AD"),
        ("C07", "Anthropic", "Volta (Tydal, Norway)", "L2", "VOLTASTART", f"={R('C07_term')}", None, f"={R('C07_tot')}", "=H{r}/G{r}", "133 MW", "'reportedly': single chain", "NONE-DISCLOSED", "hydropower site (Bitdeer)", "T3", "L-048", "DOC", "RUN", 1, None, "H2-2026 start"),
        ("C08", "Anthropic", "Riot Platforms (Rockdale)", "L2", "RIOTSTART", f"={R('C08_term')}", None, f"={R('C08_tot')}", "=H{r}/G{r}", "191 MW powered shell", "two 5-yr extensions to 16,100: 7,000 optional", "OPTION", "none", "T2", "L-136", "DOC", "RUN", 1, f"={R('C08_ext')}-{R('C08_tot')}", "start date AJ (see 00_Assumptions RIOTSTART note)"),
        ("C09", "Anthropic", "TPU lease SPV ('AI XPV Platform')", "L1", "SPVSTART", f"={R('A12_term')}", None, f"={R('A12')}", "=H{r}/G{r}", ">1 GW TPU systems", "lease presumed non-cancellable (debt-serviced); PB deleted it from Total Raised (C-01)", "NONE-DISCLOSED", "Broadcom and Google absorb part of the losses if Anthropic or Fluidstack stops paying; tranches T+1pt / 5.75% / 8.5%", "T3", "L-044", "SPV", "RUN", 1, None, "principal only; coupons add interest"),
        ("C10a", "Anthropic", "Google Cloud (REPORTED value) [VERIFY]", "L2", "GOOGSTART", f"={R('A20_yrs')}", None, f"={R('A20')}", "=H{r}/G{r}", "5 GW over five years", "take-or-pay undisclosed; Alphabet 10-Q, Google release, Broadcom 10-Q silent on $ (L-153, L-154, L-156)", "NONE-DISCLOSED", "Google supports the SPV and the project debt", "T3 [VERIFY]", "L-155", "REPORTED", "EXCL", 1, None, "[VERIFY] The Information via Reuters, page not opened; enters ONLY the Google-leg switch and the reported-$ line, never documented-$"),
        ("C10b", "Anthropic", "Google TPU gigawatts (unpriced proxy)", "L1", None, None, None, None, "n/a", "5 GW contracted 2027 (L-073, L-049); +10 GW 2028 line of sight (L-049); 1 GW Ironwood 2026 inside the SPV", "GW only; $ HOLE; proxy = GW x SW_TPU_RATE x 1,000 in the envelope block", "NONE-DISCLOSED", "Google / Broadcom", "T2 / T1", "L-073, L-049", "UNPRICED", "EXCL", 1, None, "proxy computed in A80:K98"),
        ("C11", "Anthropic", "AMD (MI450 Helios)", "L1", "AMDSTART", None, None, None, "HOLE", "up to 2 GW from H1-2027", "$ HOLE; equity 5,000 contingent (inflow block); purchases on milestones", "MILESTONE", "AMD leases DC sites itself (9,500 over up to 16 yrs; guarantees 4,100)", "T1", "L-043, L-146", "UNPRICED", "EXCL", 1, None, "proxy 2 GW x SW_TPU_RATE in the envelope block (AJ)"),
        ("C12", "OpenAI", "Oracle", "L2", "ORCLSTART", f"={R('C12_term')}", None, f"={R('C12_tot')}", "=H{r}/G{r}", "~4.5 GW", "cancellability unknown; Oracle books 20,000-25,000 of customer prepayments in FY27 capex", "NONE-DISCLOSED", "Oracle raises ~40,000 debt+equity in FY27 to fund it", "T2 (press; Oracle discloses only RPO 638,000, L-056 T1)", "L-064, L-056", "DOC", "RUN", 1, None, "60,000 per year 2027-2031"),
        ("C13", "OpenAI", "AWS", "L2", "OAWSSTART", f"={R('C13_term')}", None, f"={R('C13_tot')}", "=H{r}/G{r}", "~2 GW Trainium", "'up to' language: the 100,000 expansion may be a ceiling", "NONE-DISCLOSED", "none disclosed", "T2 / T4", "L-064", "DOC", "RUN", 1, None, "38,000 + up to 100,000 over eight years"),
        ("C14", "OpenAI", "CoreWeave", "L2", "CWSTART", f"={R('CWTERM')}", None, f"={R('C14_tot')}", "=H{r}/G{r}", "n/a", "'committed to pay up to'; T1 tranche 6,500 through 2031-05-31", "NONE-DISCLOSED", "CoreWeave funds with 9.0-9.75% notes and OEM financing", "T1 (6,500) / T4 (22,400)", "L-058", "DOC", "RUN", 1, None, "22,400 / 6 straight-line to 2031"),
        ("C15", "OpenAI", "Cerebras", "L1", "CEREBSTART", f"={R('CEREBTERM')}", None, f"={R('C15_tot')}", "=H{r}/G{r}", "750 MW in tranches 2026-2028; option +1.25 GW", "option +1.25 GW by end-2030: optional; warrant to OpenAI vests on milestones", "OPTION", "n/a; OpenAI advanced Cerebras a 1,000 working-capital loan (use of cash)", "T1", "L-149", "DOC", "RUN", 1, None, "20,000 over 4 yrs, AJ phasing"),
        ("C16a", "OpenAI", "Microsoft Azure (register 250,000, could-not-verify)", "L2", None, None, None, f"={R('C16_cnv')}", "n/a", "n/a", "10-K silent; primaries 403; recalled-$ scope only (CNV)", "NONE-DISCLOSED", "Microsoft holds equity; recap gain 6,500; funding commitments 13,000 / 11,900 funded (L-157)", "T4 (CNV)", "L-121, L-054, L-157", "RECALLED", "EXCL", 1, None, "CNV: never a fact; tally scope only"),
        ("C16b", "OpenAI", "Microsoft Azure priced proxy (LB08 FY2026 run held flat)", "L2", "OAZSTART", f"={R('OAZTERM')}", None, "=I{r}*G{r}", "=LB08", "n/a", "proxy, not a contract value: FY2026 revenue at Microsoft from OpenAI arrangements incl. revenue share", "NONE-DISCLOSED", "revenue share through 2030 at the same % subject to a cap (L-051; cap 38,000 L-052 T3)", "T1 (anchor)", "L-054, L-051, L-052", "PROXY", "RUN", 1, None, "in the priced run as the Azure proxy; NOT in documented-$"),
        ("C17", "OpenAI", "SB Energy PORTS-Pike (Ohio)", "L2", "SBESTART", f"={R('LB09_term')}", None, None, "HOLE", "~8.0 GW-IT; 17 leases, 20-yr", "nothing payable until ready-for-service (2028); 'OpenAI is not an investment-grade tenant'", "NONE-DISCLOSED", "Nvidia residual-value guaranties 105,000 on the initial ~4.25 GW-IT; option on 3.78 GW-IT", "T1", "L-061", "UNPRICED", "EXCL", 1, None, "rent HOLE; scale proxy in AD (105,000 / 4.25 x 8.0)"),
        ("C18", "OpenAI", "SB Energy Milam County (Texas)", "L2", "SBESTART", f"={R('LB09_Milam_term')}", None, None, "HOLE", "~753 MW; 15-yr", "rent undisclosed; SB Energy booked a 2,573 warrant FV charge", "NONE-DISCLOSED", "SoftBank-affiliated landlord; OpenAI warrants 3,991,809 at $0.01", "T1", "L-061, L-147", "UNPRICED", "EXCL", 1, None, "rent HOLE"),
        ("C19", "OpenAI", "AMD (6 GW; register 90,000 could-not-verify)", "L1", None, None, None, f"={R('C19_cnv')}", "n/a", "up to 6 GW; first GW on MI450", "milestone-based purchases: effectively optional; warrant 160M shares at $0.01", "MILESTONE", "AMD credit support to neoclouds (Core Scientific)", "T1 (GW) / T4 ($)", "L-060, L-123", "RECALLED", "EXCL", 1, None, "CNV $"),
        ("C20", "OpenAI", "Broadcom (Jalapeno; register 350,000 could-not-verify)", "L1", None, None, None, f"={R('C20_cnv')}", "n/a", "1.3 GW 2027; >5 GW 2028", "vendor 'on track' language, not disclosed take-or-pay", "NONE-DISCLOSED", "Broadcom supply secured through FY2028 for six XPU customers", "T1 (GW) / T4 ($)", "L-050, L-122", "RECALLED", "EXCL", 1, None, "CNV $"),
        ("C21", "OpenAI", "Nvidia (LOI retired; equity 30,000 inflow; RVG 105,000 backstop)", "L1", None, None, None, None, "n/a", "10 GW LOI retired", "RVG is Nvidia's contingent liability, not OpenAI's", "n/a", "see C17", "T2 / T1", "L-075, L-061", "INFLOW", "EXCL", 1, None, "financing, not cost"),
        ("C22", "OpenAI", "Stargate US sites", "L2", None, None, None, None, "n/a", ">9 GW planned; Abilene 0.3 GW operational", "overlaps Oracle and SB Energy rows: excluded from sums", "n/a", "Oracle / Crusoe project finance off-balance-sheet", "T3", "L-079", "OVERLAP", "EXCL", 1, None, "excluded"),
    ]
    sched_row = {}
    for i, rowdef in enumerate(rows):
        r = S + i
        (id_, co, cp, layer, startk, term, endk, total, annual, gw, canc, flag, backstop, tier, rowid, scope, run, factor, cancel, note) = rowdef
        sched_row[id_] = r
        sh.put(f"A{r}", id_, bold=True); sh.put(f"B{r}", co); sh.put(f"C{r}", cp); sh.put(f"D{r}", layer, align="center")
        if startk:
            sh.put(f"E{r}", f"={R(startk)}", kind="formula", nf=DATEF)
            sh.put(f"S{r}", f"=YEAR(E{r})*{mpy}+MONTH(E{r})", kind="formula", nf=GEN)
        if endk:
            sh.put(f"F{r}", f"={R(endk)}", kind="formula", nf=DATEF)
            sh.put(f"T{r}", f"=YEAR(F{r})*{mpy}+MONTH(F{r})", kind="formula", nf=GEN)
        elif startk and term:
            sh.put(f"T{r}", f"=S{r}+G{r}*{mpy}-1", kind="formula", nf=GEN)
            sh.put(f"F{r}", f"=DATE(INT((T{r}-1)/{mpy}),T{r}-INT((T{r}-1)/{mpy})*{mpy},1)", kind="formula", nf=DATEF)
        if term:
            sh.put(f"G{r}", term.replace("{r}", str(r)), kind="formula", nf=CNT2)
        if total:
            sh.put(f"H{r}", total.replace("{r}", str(r)), kind="formula", nf=NUM, bold=True)
        if annual == "HOLE":
            sh.put(f"I{r}", "HOLE", kind="hole", align="center")
        elif annual == "n/a":
            sh.put(f"I{r}", "n/a", kind="note", align="center")
        else:
            sh.put(f"I{r}", annual.replace("{r}", str(r)), kind="formula", nf=NUM)
        sh.put(f"J{r}", gw, kind="note"); sh.put(f"K{r}", canc, kind="note"); sh.put(f"L{r}", flag, align="center"); sh.put(f"M{r}", backstop, kind="note")
        sh.put(f"N{r}", tier, kind="note"); sh.put(f"O{r}", rowid, kind="note"); sh.put(f"P{r}", scope, align="center"); sh.put(f"Q{r}", run, align="center")
        if isinstance(factor, str):
            sh.put(f"R{r}", factor, kind="formula", nf=DEC2)
        else:
            sh.put(f"R{r}", f"={R('MPY')}/{R('MPY')}", kind="formula", nf=DEC2)  # 1.0 without typing a constant
        dated = bool(startk and (term or endk))
        for y in YEARS:
            col = YCOLS[y]
            if dated and annual not in ("HOLE", "n/a"):
                yr = f"{col}$100"
                f = (f"=$I{r}*MAX(0,MIN({yr}*{mpy}+{mpy},$T{r})-MAX({yr}*{mpy}+1,$S{r})+1)/{mpy}"
                     f"*IF({yr}=YEAR($E{r}),$R{r},1)")
                sh.put(f"{col}{r}", f, kind="formula", nf=NUM)
            else:
                sh.put(f"{col}{r}", f"={R('A21a')}", kind="formula", nf=NUM)  # 0 from 01_Data (no typed constant)
        if cancel:
            sh.put(f"AC{r}", cancel.replace("{r}", str(r)), kind="formula", nf=NUM)
        sh.put(f"AD{r}", note, kind="note")
    last = S + len(rows) - 1
    # landlord lease info and PORTS proxy in AD for C06 / C17
    r6 = sched_row["C06"]; r17 = sched_row["C17"]
    sh.put(f"AD{r6}", f"=\"Landlord lease (L-167): \"&TEXT({R('C06_LL_term')},\"0\")&\" yrs, \"&TEXT({R('C06_LL_MW')},\"0\")&\" MW, base-term \"&TEXT({R('C06_LL_val')},\"#,##0\")&\", \"&TEXT({R('X01_beacon')},\"0.00\")&\" per MW-yr; Anthropic-Lambda term AJ 6 yrs\"", kind="formula")
    sh.put(f"AD{r17}", f"=\"Scale proxy only (not a disclosed rent): \"&TEXT({R('LB09_RVG')}/{R('LB09_RVG_GW')}*{R('LB09_GW')},\"#,##0\")&\" = 105,000 / 4.25 GW-IT x 8.0 GW-IT\"", kind="formula")
    sh.put(f"AE{r17}", f"={R('LB09_RVG')}/{R('LB09_RVG_GW')}*{R('LB09_GW')}", kind="formula", nf=NUM, key="PORTS_PROXY")
    sh.put(f"A{last+1}", "End of schedule. Year values: annual value x months active in the year / 12 x first-year ramp factor; month index = year x 12 + month; rows without dates carry 0 (linked to the 01_Data zero, A21a).", kind="note")
    rng = lambda col: f"${col}${S}:${col}${last}"

    def sumifs(col, co, scope=None, run=None, layer=None):
        parts = [f"{rng(col)},{rng('B')},\"{co}\""]
        if scope: parts.append(f"{rng('P')},\"{scope}\"")
        if run: parts.append(f"{rng('Q')},\"{run}\"")
        if layer: parts.append(f"{rng('D')},\"{layer}\"")
        return "=SUMIFS(" + ",".join(parts) + ")"

    # ---------------- E6 Anthropic table ----------------
    sh.section(3, "OBLIGATION STACK, ANTHROPIC: contracted / cash paid to date / cancellable-contingent-unpriced / backstop (Exhibit E6; A5:J20; cost-stack section 4a)", ncols=11)
    sh.header(4, ["Counterparty (layer)", "Contracted, documented ($M)", "Cash paid to date ($M; bounds)", "Cancellable / contingent / unpriced", "Vendor backstop", "Tier", "Rows", "Scope", "Layer", "Note"])
    def H(id_): return f"=H{sched_row[id_]}"
    e6 = [
        (5, "1 AWS (L2)", H("C01"), "HOLE (AWS does not disclose)", "take-or-pay not disclosed; Amazon up to 20,000 more equity (inflow)", "Amazon is investor and supplier", "T1", "L-072", "DOC", "L2"),
        (6, "2 Google Cloud (L2)", "unpriced in every filing", "HOLE", f"=\"5 GW contracted + 5-10 GW line of sight; reported \"&TEXT({R('A20')},\"#,##0\")&\" over five years [VERIFY]; Google 30,000 equity contingent (inflow)\"", "Google supports the SPV and the project debt", "T2 / T1 / T3", "L-073, L-049, L-153, L-154, L-156, L-155", "REPORTED / UNPRICED", "L2"),
        (7, "3 TPU lease SPV (L1)", H("C09"), f"=\"<= \"&TEXT(I{sched_row['C09']}/{mpy}*{R('C03_notice_m')},\"#,##0\")&\" (<= 3 months of the lease)\"", "lease presumed non-cancellable (debt-serviced)", "Broadcom and Google absorb part of the losses; tranches T+1pt / 5.75% / 8.5%", "T3", "L-044", "SPV", "L1"),
        (8, "4 Azure (L2)", H("C02"), "HOLE", "none disclosed", "Microsoft equity up to 5,000 (funded)", "T1", "L-074, L-055", "DOC", "L2"),
        (9, "5 SpaceX COLOSSUS (L2)", H("C03"), f"=\"<= \"&TEXT({R('SPCX_AI_Q2')},\"#,##0\")&\" in Q2-2026 (SpaceX AI-segment revenue, L-047)\"", f"=AC{sched_row['C03']}", "SpaceX bought ~2,000 of gas turbines", "T1", "L-046, L-047", "DOC", "L2"),
        (10, "6 Fluidstack (L2)", H("C04"), "HOLE (project companies raised 15,200 for 1.43 GW: a separate TPU-site program)", "spend commitment; phasing beyond 2026 undisclosed", "Google conditional support on project debt", "T1", "L-076, L-168, L-045", "DOC (phasing HOLE)", "L2"),
        (11, "7 Nscale (L2)", H("C05"), f"={R('A21a')}", "terms not published [VERIFY]", "not disclosed", "T2", "L-135", "DOC", "L2"),
        (12, "8 Lambda (L2)", H("C06"), f"={R('A21a')}", "Anthropic-Lambda term HOLE (AJ 6 yrs); landlord lease 15 yr, 704 MW, 19,600 base-term (L-167)", "Nvidia holds the datacenter lease; Hut 8 landlord", "T2 / T1", "L-137, L-167", "DOC", "L2"),
        (13, "9 Volta (L2)", H("C07"), "HOLE", "'reportedly': single chain", "hydropower site (Bitdeer)", "T3", "L-048", "DOC", "L2"),
        (14, "10 Riot Platforms (L2)", H("C08"), "HOLE", f"=AC{sched_row['C08']}", "none", "T2", "L-136", "DOC", "L2"),
        (15, "11 AMD (L1)", "unpriced", f"={R('A21a')}", "up to 2 GW; $ undisclosed; equity up to 5,000 contingent (inflow)", "AMD leases DC sites itself (9,500; guarantees 4,100)", "T1", "L-043, L-146", "UNPRICED", "L1"),
        (16, "12 Copyright (L5)", f"={R('A14')}", "payable 2026", f"={R('A14_music')}", "n/a", "T2", "L-086", "L5 (consumption)", "L5"),
        (17, "13 Debt facilities", f"={R('A11')}", "facility, not spend", f"=\"expansion \"&TEXT({R('A11_exp')},\"#,##0\")&\" NOT closed as of Sep-9 [VERIFY] (L-160)\"", "n/a", "T2 / T3 / T3", "L-014, L-042, L-160", "facility", "n/a"),
    ]
    for rr, lab, c, d, e, f, g, h, i, j in e6:
        sh.put(f"A{rr}", lab, bold=True)
        for col, v in (("B", c), ("C", d), ("D", e), ("E", f), ("F", g), ("G", h), ("H", i), ("I", j)):
            if isinstance(v, str) and v.startswith("="):
                sh.put(f"{col}{rr}", v, kind="formula", nf=NUM)
            elif v == "HOLE" or (isinstance(v, str) and v.startswith("HOLE")):
                sh.put(f"{col}{rr}", v, kind="hole")
            else:
                sh.put(f"{col}{rr}", v, kind="note")
    sh.put("A18", "TOTAL documented-$ (items 1, 4-10; scope DOC)", bold=True); sh.put("B18", sumifs("H", "Anthropic", scope="DOC"), kind="formula", nf=NUM, bold=True, key="DOC_A"); ck(sh, "C18", "B18", "DOC_A")
    sh.put("D18", "Cancellable within documented-$ (SpaceX beyond 90 days + Riot options):", kind="note"); sh.put("E18", f"=SUMIFS({rng('AC')},{rng('B')},\"Anthropic\")", kind="formula", nf=NUM, bold=True, key="CANC_A"); ck(sh, "F18", "E18", "CANC_A")
    sh.put("G18", "=E18/B18", kind="formula", nf=PCT); sh.put("H18", "share of documented-$", kind="note")
    sh.put("A19", "TOTAL documented-$ incl. the TPU SPV lease (scope DOC + SPV)", bold=True); sh.put("B19", f"=B18+{sumifs('H', 'Anthropic', scope='SPV')[1:]}", kind="formula", nf=NUM, bold=True, key="DOC_A_SPV"); ck(sh, "C19", "B19", "DOC_A_SPV")
    sh.put("D19", "Contingent equity inflows (Amazon + Google + AMD; shown, not added):", kind="note"); sh.put("E19", f"={R('A17_amzn')}+{R('A17_goog')}+{R('A17_amd')}", kind="formula", nf=NUM, key="INFLOWS_A")
    sh.put("A20", "REPORTED-$ (documented-$ + the Google leg at its reported ~200,000) [VERIFY, T3]", bold=True); sh.put("B20", f"=B18+{sumifs('H', 'Anthropic', scope='REPORTED')[1:]}", kind="hole", nf=NUM, bold=True, key="REP_A"); ck(sh, "C20", "B20", "REP_A")
    sh.put("D20", "[VERIFY] L-155 (T3, page not opened); incl. SPV:", kind="flag"); sh.put("E20", f"=B20+{sumifs('H', 'Anthropic', scope='SPV')[1:]}", kind="hole", nf=NUM)
    sh.put("F20", "Unpriced GW: Google 5 GW contracted (reported value T3 only) + 5-10 GW line of sight; AMD 2 GW", kind="note")
    sh.put("G20", f"={R('X02_a27')}+{R('C11_GW')}", kind="formula", nf=CNT1); sh.put("H20", "GW contracted and unpriced (Google 5 + AMD 2)", kind="note")

    # ---------------- E7 OpenAI table ----------------
    sh.section(24, "OBLIGATION STACK, OPENAI (Exhibit E7; A25:J40; cost-stack section 4b). Row 25-26 = the Microsoft anchor (Exhibit E12).", ncols=11)
    sh.header(25, ["Counterparty (layer)", "Contracted, documented ($M)", "Cash paid to date ($M)", "Cancellable / contingent / unpriced", "Vendor backstop", "Tier", "Rows", "Scope", "Layer", "Note"])
    e7 = [
        (26, "1 Microsoft Azure (L2)", f"=\"250,000 incremental commitment: could-not-verify (register); T1 facts: revenue share through 2030 at the same % subject to a cap; non-exclusive IP to 2032; any cloud\"", "=LB08", f"=\"cap \"&TEXT({R('O11_cap')},\"#,##0\")&\" (T3); % unconfirmed at T1/T2 (10-K silent, L-157/L-158); stake ~\"&TEXT({R('O11_stake')},\"0%\")&\" (~\"&TEXT({R('O11_stake_val')},\"#,##0\")&\") at the Oct-2025 recap (T2), post-dilution undisclosed\"", f"=\"Microsoft holds equity (recap gain \"&TEXT({R('F_msft_gain')},\"#,##0\")&\"); funding commitments \"&TEXT({R('O13_commit')},\"#,##0\")&\", of which \"&TEXT({R('O13_funded')},\"#,##0\")&\" funded at 2026-06-30 (T1)\"", "T4 / T1 / T3 / T2", "L-121, L-054, L-051, L-052, L-159, L-157, L-158", "RECALLED (CNV) + PROXY", "L2"),
        (27, "2 Oracle (L2)", H("C12"), "HOLE (Oracle does not name OpenAI)", "prepayments booked by Oracle; cancellability unknown", "Oracle raises ~40,000 debt+equity in FY27", "T2 (T1 bound: RPO 638,000)", "L-064, L-056, L-057", "DOC", "L2"),
        (28, "3 AWS (L2)", H("C13"), "HOLE", "'up to' 100,000 expansion may be a ceiling", "none disclosed", "T2 / T4", "L-064", "DOC", "L2"),
        (29, "4 CoreWeave (L2)", H("C14"), "HOLE", "'committed to pay up to'; T1 tranche 6,500", "CoreWeave funds with 9.0-9.75% notes and OEM financing", "T1 / T4", "L-058, L-059", "DOC", "L2"),
        (30, "5 Cerebras (L1)", H("C15"), f"=\"1,000 working-capital loan advanced BY OpenAI (a use of cash)\"", "option +1.25 GW by end-2030 (optional); warrant vests on milestones", "n/a", "T1", "L-149", "DOC", "L1"),
        (31, "6 SB Energy PORTS-Pike (L2)", "unpriced (rent undisclosed)", f"={R('A21a')}", f"=\"scale proxy only: \"&TEXT({R('PORTS_PROXY')},\"#,##0\")&\" (105,000 / 4.25 GW-IT x 8.0 GW-IT); not a disclosed rent\"", f"=\"Nvidia residual-value guaranties \"&TEXT({R('LB09_RVG')},\"#,##0\")&\" on ~4.25 GW-IT; option on 3.78 GW-IT; nothing payable until RFS\"", "T1", "L-061", "UNPRICED", "L2"),
        (32, "7 SB Energy Milam County (L2)", "unpriced (rent undisclosed)", f"={R('A21a')}", "rent undisclosed; warrant FV charge 2,573 at SB Energy", "SoftBank-affiliated landlord", "T1", "L-061, L-147", "UNPRICED", "L2"),
        (33, "8 AMD (L1)", "unpriced (90,000 is a press estimate, CNV)", "HOLE", "milestone-based purchases: effectively optional", "AMD credit support to neoclouds", "T1 (GW) / T4 ($)", "L-060, L-123", "RECALLED (CNV)", "L1"),
        (34, "9 Broadcom (L1)", "unpriced (350,000 / 10 GW is CNV)", "HOLE", "vendor 'on track' language, not disclosed take-or-pay", "Broadcom supply secured through FY2028", "T1 (GW) / T4 ($)", "L-050, L-122, L-144", "RECALLED (CNV)", "L1"),
        (35, "10 Nvidia (L1)", "LOI 100,000 / 10 GW RETIRED (C-20)", "n/a (30,000 equity inflow)", "RVG 105,000 is Nvidia's contingent liability, not OpenAI's", "see item 6", "T2 / T1", "L-075, L-061", "INFLOW", "L1"),
        (36, "11 Stargate US sites (L2)", ">9 GW planned; overlaps items 2 and 6-7 (do not add)", "Abilene operating", "five sites complete Q4-2028 (T3)", "Oracle / Crusoe project finance off-balance-sheet", "T3", "L-079", "OVERLAP", "L2"),
        (37, "12 Debt", f"={R('O10')}", "facilities", "no Stargate project debt at the OpenAI level found", "n/a", "T2", "L-023", "facility", "n/a"),
    ]
    for rr, lab, c, d, e, f, g, h, i, j in e7:
        sh.put(f"A{rr}", lab, bold=True)
        for col, v in (("B", c), ("C", d), ("D", e), ("E", f), ("F", g), ("G", h), ("H", i), ("I", j)):
            if isinstance(v, str) and v.startswith("="):
                sh.put(f"{col}{rr}", v, kind="formula", nf=NUM)
            elif v == "HOLE" or (isinstance(v, str) and v.startswith("HOLE")):
                sh.put(f"{col}{rr}", v, kind="hole")
            else:
                sh.put(f"{col}{rr}", v, kind="note")
    sh.put("J26", "Exhibit E12 row: the T1 cash anchor is LB08 (24,100 FY2026) with A/R 6,000; do not print '20%'", kind="note")
    sh.put("A38", "TOTAL documented-$ (items 2-5; scope DOC)", bold=True); sh.put("B38", sumifs("H", "OpenAI", scope="DOC"), kind="formula", nf=NUM, bold=True, key="DOC_O"); ck(sh, "C38", "B38", "DOC_O")
    sh.put("D38", "Unpriced T1 leases (GW-IT):", kind="note"); sh.put("E38", f"={R('LB09_GW')}+{R('LB09_Milam_MW')}/{R('MWPERGW')}", kind="formula", nf=CNT2, key="UNPRICED_GW_O")
    sh.put("A39", "RECALLED-$ (items 1, 8, 9; scope RECALLED; all could-not-verify)", bold=True); sh.put("B39", sumifs("H", "OpenAI", scope="RECALLED"), kind="hole", nf=NUM, bold=True, key="REC_O"); ck(sh, "C39", "B39", "REC_O")
    sh.put("D39", "Sum documented + recalled (vs the 1,150,000 'obligations through 2035' tally):", kind="note"); sh.put("E39", "=B38+B39", kind="formula", nf=NUM, key="SUM_O")
    sh.put("A40", "Share of the reconstructed tally resting on could-not-verify rows", bold=True); sh.put("B40", "=B39/E39", kind="formula", nf=PCT, bold=True, key="CNV_SHARE")
    sh.put("D40", "Cash anchors: LB08 24,100 FY26 to Microsoft (T1) + 50,000 2026 compute plan (T2) + 1,000 Cerebras loan (T1) + Q1-26 burn 3,700 (T3)", kind="note")
    sh.put("E40", f"=LB08+LB07a+{R('C15_loan')}+{R('O05_q1burn')}", kind="formula", nf=NUM)

    # ---------------- E8 tallies ----------------
    sh.section(44, "TALLY RECONCILIATION: the numbers are scopes, not one number (Exhibit E8; A45:H58; cost-stack section 5)", ncols=11)
    sh.header(45, ["Tally", "Value ($M)", "Scope / definition", "Vintage", "Row · status · tier", "Reconciles?", "Components (formula)", "Check"])
    r3 = sched_row["C03"]
    tal = [
        (46, "Bloomberg (Aug-31): 'at least 175,000'", f"=H{sched_row['C06']}+H{sched_row['C05']}+H{sched_row['C04']}+H{r3}", "Lambda + Nscale + Fluidstack + SpaceX at its 36-month maximum", "2026-08-31", "L-138 · estimated · T2", "Yes, exactly", "C06 + C05 + C04 + C03 (schedule totals)", "BBG"),
        (47, "TechCrunch (Aug-26): 'at least 61,000'", f"=H{sched_row['C05']}+H{sched_row['C07']}+{R('A17_amd')}+{R('C03_monthly')}", "Nscale + Volta + AMD 5,000 (equity, not compute) + SpaceX one month", "2026-08-26", "L-138 · estimated · T2", "Yes, but mixes an equity inflow with compute: do not cite", "C05 + C07 + A17_amd + C03_monthly", "TC"),
        (48, "stepmark (T4): '>99,000'", f"=H{sched_row['C07']}+H{sched_row['C08']}+H{sched_row['C05']}+H{sched_row['C06']}", "Volta + Riot + Nscale + Lambda (four neoclouds)", "2026-09-02", "L-138 · estimated · T4", "Yes", "C07 + C08 + C05 + C06", "STEP"),
        (49, "youngresearch (T4): '517,000'", f"={R('T_young')}", "not reproducible from ledger rows", "2026", "L-138 · estimated · T4", "No: CUT", "n/a", None),
        (50, "Register (Jun-12): '80B+ across 6 partners'", f"={R('T_register')}", "pre-dates Riot, Volta, Nscale, Lambda", "2026-06-12", "L-138 · recalled · T4", "Superseded: CUT", "n/a", None),
        (51, "The Information (May-5): Google leg '~200,000 over five years' [VERIFY]", f"={R('A20')}", "Google Cloud commitment only (5 GW from 2027); '>40%' of Google's backlog; not in any other tally", "2026-05-05", "L-155 · estimated · T3 [VERIFY]; L-153, L-154 · T1 silent", "Page not opened (503); if true it alone roughly doubles every published 2026 tally (C-14 addendum)", "A20", None),
        (52, "v5 ledger stack: documented-$ (8 contracts)", "=B18", "items 1, 4-10 of E6", "2026-09-09", "mixed T1-T3", "Print the components; never a single total without this scope line", "SUMIFS scope DOC", "DOC_A"),
        (53, "v5 ledger stack: documented-$ + TPU SPV lease", "=B19", "adds the 34,500 lessor-debt lease (L-044)", "2026-09-09", "T3 (SPV)", "as above", "DOC + SPV", "DOC_A_SPV"),
        (54, "v5 ledger stack: reported-$ incl. the Google leg [VERIFY]", "=B20", "documented-$ + 200,000 reported; never inside documented-$", "2026-09-09", "T3 [VERIFY]", "own scope row only", "DOC + REPORTED", "REP_A"),
        (55, "OpenAI spend plan (Feb) 665,000 / (May) 600,000 / (Jul) 750,000", f"={R('LB07b_feb')}", "P&L consumption 2026-2030 (three vintages; May and Jul in columns D-E of row 56)", "2026-02-21 / 05-05 / 07-22", "L-082 T3 / L-078 T2 / L-062 T2", "Same object, different vintages and definitions; never compared with the obligation stack", "01_Data LB07b_feb / LB07b_may / LB07b", None),
        (56, "   May vintage (sworn) / Jul vintage", f"={R('LB07b_may')}", "compute spending through 2030", "2026-05-05 / 2026-07-22", "L-078 · confirmed · T2; L-062 · estimated · T2", "+25% vs May in 11 weeks", "", None),
        (57, "OpenAI obligation stack 1,150,000 (register) vs reconstructed documented + recalled", "=E39", "contracts through ~2035 across vendors: 480,400 documented-$ + 690,000 recalled-$ (59% CNV)", "2026-02-27", "L-062 notes · recalled · T4", "Reconciles within 2% of the 1,150,000 canonical tally (register value in D)", "DOC_O + REC_O", None),
        (58, "OpenAI headline 1,400,000 (Altman) and 2026 spend 50,000", f"={R('T_headline')}", "includes optional and aspirational capacity; 2026 spend = first-year slice (LB07a in D)", "2026 / 2026-05-05", "L-062 T2 relay; L-078 T2", "Never mixed with a spend plan or the obligation stack", "T_headline; LB07a", None),
    ]
    for rr, lab, f, scope, vint, src, rec, comp, chk in tal:
        sh.put(f"A{rr}", lab); sh.put(f"B{rr}", f, kind=("hole" if rr in (49, 50, 51, 54) else "formula"), nf=NUM, bold=True)
        sh.put(f"C{rr}", scope, kind="note"); sh.put(f"D{rr}", vint, kind="note"); sh.put(f"E{rr}", src, kind="note"); sh.put(f"F{rr}", rec, kind="note"); sh.put(f"G{rr}", comp, kind="note")
        if chk:
            ck(sh, f"H{rr}", f"B{rr}", chk)
    sh.put("D56", "=LB07b", kind="formula", nf=NUM); sh.put("D57", f"={R('T_oblig')}", kind="hole", nf=NUM); sh.put("D58", "=LB07a", kind="formula", nf=NUM)
    sh.put("H57", "=E39/D57-1", kind="formula", nf=PCT); sh.put("I57", "reconstructed vs canonical", kind="note")
    sh.put("A59", "Rule: a spend plan (2026-2030 consumption) is never compared with an obligation stack (through 2035 contracts) or with a headline. The comparable pair is burn plan vs spend plan (both consumption).", kind="note")

    # ---------------- annualized priced run ----------------
    sh.section(60, "ANNUALIZED PRICED COMMITMENT RUN BY YEAR (Exhibit E3, layers L1-L2; A60:K75; SUMIFS over the schedule by company, layer and 'RUN' flag)", ncols=11)
    sh.yearhdr(61, label="Item")
    sh.put("B61", "Unit", kind="header"); sh.put("C61", "Basis", kind="header")

    def runrow(rr, key, label, co, layer, bold=False):
        sh.put(f"A{rr}", label, bold=bold); sh.put(f"B{rr}", "$M/yr", kind="note"); sh.put(f"C{rr}", "priced contracts only (scope DOC/SPV/PROXY, flag RUN)", kind="note")
        for y in YEARS:
            f = f"=SUMIFS({rng(YCOLS[y])},{rng('B')},\"{co}\",{rng('Q')},\"RUN\"" + (f",{rng('D')},\"{layer}\"" if layer else "") + ")"
            sh.put(f"{YC[y]}{rr}", f, kind="formula", nf=NUM, bold=bold, key=f"{key}|{y}")
    runrow(62, "RUN_A_L1", "Anthropic L1 (TPU SPV lease)", "Anthropic", "L1")
    runrow(63, "RUN_A_L2", "Anthropic L2 (cloud, neocloud, site)", "Anthropic", "L2")
    runrow(64, "RUN_A", "Anthropic priced run, L1 + L2", "Anthropic", None, bold=True)
    sh.put("A65", "   check vs spec (28,158 / 47,730 / 53,355 / 44,605 / 38,355)", kind="note")
    for y, k in ((2026, "RUN26"), (2027, "RUN27"), (2028, "RUN28"), (2029, "RUN29"), (2030, "RUN30")):
        ck(sh, f"{YC[y]}65", f"{YC[y]}64", k)
    runrow(66, "RUN_O_L1", "OpenAI L1 (Cerebras)", "OpenAI", "L1")
    runrow(67, "RUN_O_L2", "OpenAI L2 (Oracle, AWS, CoreWeave, Azure proxy)", "OpenAI", "L2")
    runrow(68, "RUN_O", "OpenAI priced run, L1 + L2", "OpenAI", None, bold=True)
    sh.put("A69", "   check vs spec (2027: 110,083)", kind="note"); ck(sh, "H69", "H68", "RUNO27")
    r10a = sched_row["C10a"]
    sh.put("A70", "Anthropic Google leg, REPORTED branch (40,000 per year 2027-2031, L-155) [VERIFY]"); sh.put("B70", "$M/yr", kind="note"); sh.put("C70", "T3 [VERIFY]; scope REPORTED; never documented-$", kind="flag")
    for y in YEARS:
        sh.put(f"{YC[y]}70", f"={YCOLS[y]}{r10a}", kind="hole", nf=NUM, key=f"GOOG_REP|{y}")
    sh.put("A71", "Anthropic Google leg, PROXY branch (unpriced GW x SW_TPU_RATE x 1,000)"); sh.put("B71", "$M/yr", kind="note"); sh.put("C71", "GW: 2026 0 (Ironwood inside the SPV); 2027 = 5 contracted; 2028+ = SW_GW_2028", kind="note")
    sh.put("A94", "Unpriced Google GW by year (2026 0; 2027 contracted 5; 2028+ SW_GW_2028)"); sh.put("B94", "GW", kind="note"); sh.put("C94", "L-073, L-049; SW_GW_2028", kind="note")
    gw = {2023: f"={R('A21a')}", 2024: f"={R('A21a')}", 2025: f"={R('A21a')}", 2026: f"={R('A21a')}", 2027: f"={R('X02_a27')}", 2028: "=SW_GW_2028", 2029: "=SW_GW_2028", 2030: "=SW_GW_2028"}
    for y in YEARS:
        sh.put(f"{YC[y]}94", gw[y], kind="formula", nf=CNT1, key=f"GOOG_GW|{y}")
        sh.put(f"{YC[y]}71", f"={YC[y]}94*SW_TPU_RATE*{R('MWPERGW')}", kind="formula", nf=NUM, key=f"GOOG_PROXY|{y}")
    sh.put("A72", "AMD proxy (2 GW from 2027 at SW_TPU_RATE; AJ)"); sh.put("B72", "$M/yr", kind="note"); sh.put("C72", "L-043 (GW T1); rate AJ = SW_TPU_RATE", kind="note")
    for y in YEARS:
        f = f"=IF({R(f'YR|{y}')}>=YEAR({R('AMDSTART')}),{R('C11_GW')}*SW_TPU_RATE*{R('MWPERGW')},{R('A21a')})"
        sh.put(f"{YC[y]}72", f, kind="formula", nf=NUM, key=f"AMD_PROXY|{y}")
    sh.put("A73", "Anthropic 2028 stack, reported branch (priced + Google leg reported; check 93,355)"); sh.put("I73", "=I64+I70", kind="formula", nf=NUM, key="STACK28_REP"); ck(sh, "J73", "I73", "STACK28")
    sh.put("A74", "Google leg in use (SW_GOOGLE_VALUE)"); sh.put("B74", "$M/yr", kind="note"); sh.put("C74", "=SW_GOOGLE_VALUE", kind="formula")
    for y in YEARS:
        sh.put(f"{YC[y]}74", f'=IF(SW_GOOGLE_VALUE="reported",{YC[y]}70,{YC[y]}71)', kind="formula", nf=NUM, key=f"GOOG_LEG|{y}")
    sh.put("A75", "Cross-check: 2026 priced run = L2 24,708 (AWS 10,000 + Azure 6,000 + SpaceX 7,875 + Volta 833) + L1 SPV 3,450 (cost-stack section 2)", kind="note")

    # ---------------- envelope chart data ----------------
    sh.section(80, "ENVELOPE VS COMMITMENTS, ANTHROPIC (Exhibit E10 chart data; A80:K98): plan envelope = revenue x (1 - plan GM) + training; priced run; Google leg (switch); AMD proxy; gaps (negative = plan does not cover commitments)", ncols=11)
    sh.yearhdr(81, label="Item")
    sh.put("B81", "Unit", kind="header"); sh.put("C81", "Basis", kind="header")
    env = [
        (82, "ENV_PLAN_LO", "Plan envelope, LOW (2026: FY at 100,000 x (1 - 60% GM) + 7,000; 2027: 140,000 x (1 - 63%) + 14,000; 2028: 190,000 x (1 - 77%) + 22,000)", "L-035 / AJ / L-036 revenue; L-119 GM (T4); L-125 training (T4)",
         {2026: f"={R('FY26A_100')}*(1-{R('A07_2026_high')})+{R('A08_2026')}", 2027: f"={R('ENV27LO')}*(1-{R('A07_2027')})+{R('A08_2027')}", 2028: f"=LB10*(1-{R('A07_2028')})+{R('A08_2028')}"}),
        (83, "ENV_PLAN_HI", "Plan envelope, HIGH (2026: FY at 120,000 x (1 - 44%) + 7,000; 2027: 150,000 x 37% + 14,000; 2028: 200,000 x 23% + 22,000)", "as above",
         {2026: f"={R('FY26A_120')}*(1-{R('A07_2026_low')})+{R('A08_2026')}", 2027: f"={R('ENV27HI')}*(1-{R('A07_2027')})+{R('A08_2027')}", 2028: f"={R('LB10_high')}*(1-{R('A07_2028')})+{R('A08_2028')}"}),
    ]
    for rr, key, lab, basis, cells in env:
        sh.put(f"A{rr}", lab); sh.put(f"B{rr}", "$M/yr", kind="note"); sh.put(f"C{rr}", basis, kind="note")
        for y in YEARS:
            if y in cells:
                sh.put(f"{YC[y]}{rr}", cells[y], kind="formula", nf=NUM, key=f"{key}|{y}")
            elif y >= 2029:
                sh.put(f"{YC[y]}{rr}", "HOLE", kind="hole", align="center")
    ck(sh, "L82", "I82", "ENV28_LO"); ck(sh, "L83", "I83", "ENV28_HI"); ck(sh, "M82", "H82", "ENV27_LO"); ck(sh, "M83", "H83", "ENV27_HI")
    sh.put("A84", "Scenario envelope, LIVE (03_Costs: COGS L4 + training L3 at SW_SCEN)"); sh.put("B84", "$M/yr", kind="note"); sh.put("C84", "03_Costs row 20", kind="note")
    for y in FYEARS:
        sh.put(f"{YC[y]}84", f"='03_Costs'!{YC[y]}$20", kind="formula", nf=NUM, key=f"ENV_LIVE|{y}")
    sh.put("A85", "Priced run (L1 + L2, row 64)"); sh.put("B85", "$M/yr", kind="note")
    sh.put("A86", "Google leg in use (SW_GOOGLE_VALUE; row 74)"); sh.put("B86", "$M/yr", kind="note"); sh.put("C86", '=IF(SW_GOOGLE_VALUE="reported","reported 40,000 per year [VERIFY] (L-155, T3)","proxy: GW x SW_TPU_RATE")', kind="formula")
    sh.put("A87", "AMD proxy (row 72)"); sh.put("B87", "$M/yr", kind="note")
    for y in YEARS:
        sh.put(f"{YC[y]}85", f"={YC[y]}64", kind="formula", nf=NUM); sh.put(f"{YC[y]}86", f"={YC[y]}74", kind="formula", nf=NUM); sh.put(f"{YC[y]}87", f"={YC[y]}72", kind="formula", nf=NUM)
    gaps = [(88, "GAP_LO", "Gap BEFORE AMD, plan low = envelope low - priced - Google leg", "=%s82-%s85-%s86"),
            (89, "GAP_HI", "Gap BEFORE AMD, plan high = envelope high - priced - Google leg", "=%s83-%s85-%s86"),
            (90, "GAP_LO_AMD", "Gap AFTER AMD, plan low", "=%s88-%s87"),
            (91, "GAP_HI_AMD", "Gap AFTER AMD, plan high", "=%s89-%s87"),
            (92, "GAP_LIVE", "Gap, scenario envelope (live) BEFORE AMD", "=%s84-%s85-%s86"),
            (93, "GAP_LIVE_AMD", "Gap, scenario envelope (live) AFTER AMD", "=%s92-%s87")]
    for rr, key, lab, tmpl in gaps:
        sh.put(f"A{rr}", lab, bold=(rr in (88, 89))); sh.put(f"B{rr}", "$M/yr", kind="note"); sh.put(f"C{rr}", "negative = the plan does not cover the commitments", kind="note")
        yrs = FYEARS if rr >= 92 else (2026, 2027, 2028)
        for y in yrs:
            c = YC[y]
            sh.put(f"{c}{rr}", tmpl.replace("%s", c), kind="formula", nf=NUM, bold=(rr in (88, 89)), key=f"{key}|{y}")
    sh.put("A95", "Consistency cell: reported 200,000 / 5 yr / 5 GW = $M per MW-yr (fits ~5 GW); at 16 GW; vs the SPV chips-only rate"); sh.put("B95", "$M per MW-yr", kind="note")
    sh.put("D95", f"={R('X01_goog5')}", kind="hole", nf=CNT2, key="GOOG_RATE5"); sh.put("E95", f"={R('X01_goog16')}", kind="hole", nf=CNT2, key="GOOG_RATE16"); sh.put("F95", f"={R('X01_spv')}", kind="formula", nf=CNT2)
    ck(sh, "G95", "D95", "GOOG_RATE5"); ck(sh, "H95", "E95", "GOOG_RATE16")
    sh.put("I95", "8.0 at 5 GW is close to the 9.3 proxy; 2.5 at 16 GW is below chips-only 6.9, so the reported figure fits ~5 GW and Broadcom's line of sight is additional capacity", kind="note")
    sh.section(96, "E10 BRANCH GRID at AF97:AP102 (computed from the 01_Data branch values, independent of the switches): 2027 and 2028 gaps before AMD; report language: reported '$25-28B/yr', proxy 5 GW '$30-50B/yr', proxy 15 GW '$125-175B/yr'", ncols=11)
    gw5 = R("X02_a27"); gw15 = f"({R('X02_a27')}+{R('X02_a28')})"; mw = R("MWPERGW")
    branches = [
        (98, "reported ~200,000 over five years = 40,000 per year (Base) [VERIFY]", f"={R('A20')}/{R('A20_yrs')}", f"={R('A20')}/{R('A20_yrs')}", ("GAP27_REP_LO", "GAP27_REP_HI"), ("GAP28_REP_LO", "GAP28_REP_HI", None), "T3 [VERIFY] (L-155); filings silent (L-153, L-154, L-156)"),
        (99, "proxy, contracted 5 GW at 9.3 per MW-yr", f"={gw5}*{R('X01_tpu_93')}*{mw}", f"={gw5}*{R('X01_tpu_93')}*{mw}", None, (None, None, "GAP28_PROXY"), "T3 derived (L-044, L-136, L-134)"),
        (100, "proxy, contracted 5 GW at 12.5 per MW-yr", f"={gw5}*{R('X01_tpu_125')}*{mw}", f"={gw5}*{R('X01_tpu_125')}*{mw}", None, (None, None, "GAP28_125"), "T3 derived"),
        (101, "proxy, 15 GW incl. Broadcom's 2028 line of sight at 9.3", f"={R('A21a')}", f"={gw15}*{R('X01_tpu_93')}*{mw}", None, (None, None, "GAP28_15GW"), "T1 GW (L-049), T3 rate"),
        (102, "proxy, 15 GW at 12.5", f"={R('A21a')}", f"={gw15}*{R('X01_tpu_125')}*{mw}", None, (None, None, "GAP28_125_15"), "T3"),
    ]
    # Branch grid placed at AF97:AP102 (columns beyond the schedule's AD) so rows 98-102 stay clear of the schedule header at row 100.
    cols = ["AF", "AG", "AH", "AI", "AJ", "AK", "AL", "AM", "AN", "AO", "AP"]
    sh.put("AF96", "E10 BRANCH GRID (see section header at A96)", kind="header")
    for j, h in enumerate(["Branch", "Google leg 2027", "Google leg 2028", "Gap 2027 low", "Gap 2027 high", "Gap 2028 low", "Gap 2028 high", "Gap 2028 midpoint", "Check 2027", "Check 2028", "Tier"]):
        sh.put(f"{cols[j]}97", h, kind="header")
    sh.put("A98", "Branch grid printed at AF97:AP102 (five branches); the row-98 cells below link its first row.", kind="note")
    for i, (rr0, lab, leg27, leg28, c27, c28, tier) in enumerate(branches):
        rr = 98 + i
        sh.put(f"AF{rr}", lab, kind=("hole" if i == 0 else "label"))
        sh.put(f"AG{rr}", leg27, kind=("hole" if i == 0 else "formula"), nf=NUM); sh.put(f"AH{rr}", leg28, kind=("hole" if i == 0 else "formula"), nf=NUM)
        sh.put(f"AI{rr}", f"=$H$82-$H$85-AG{rr}", kind="formula", nf=NUM); sh.put(f"AJ{rr}", f"=$H$83-$H$85-AG{rr}", kind="formula", nf=NUM)
        sh.put(f"AK{rr}", f"=$I$82-$I$85-AH{rr}", kind="formula", nf=NUM); sh.put(f"AL{rr}", f"=$I$83-$I$85-AH{rr}", kind="formula", nf=NUM)
        sh.put(f"AM{rr}", f"=AVERAGE(AK{rr},AL{rr})", kind="formula", nf=NUM, key=f"BR_MID28_{i}")
        if c27:
            ck(sh, f"AN{rr}", f"AI{rr}", c27[0]); sh.put(f"AN{rr}", f'=IF(AND(ABS(AI{rr}-{R("CHK_"+c27[0])})<={R("TOL_"+c27[0])},ABS(AJ{rr}-{R("CHK_"+c27[1])})<={R("TOL_"+c27[1])}),"PASS","FAIL")', kind="formula", bold=True, key=f"PF_{c27[0]}")
        if c28:
            lo, hi, mid = c28
            if lo:
                sh.put(f"AO{rr}", f'=IF(AND(ABS(AK{rr}-{R("CHK_"+lo)})<={R("TOL_"+lo)},ABS(AL{rr}-{R("CHK_"+hi)})<={R("TOL_"+hi)}),"PASS","FAIL")', kind="formula", bold=True, key=f"PF_{lo}")
            if mid:
                ck(sh, f"AO{rr}", f"AM{rr}", mid)
        sh.put(f"AP{rr}", tier, kind="note")
    sh.ws.freeze_panes = "B5"
    return sched_row


# ----------------------------------------------------------------------------------------------------
# 03_Costs
# ----------------------------------------------------------------------------------------------------
def build_03(sh):
    sh.put("A1", "03_Costs: the 5-Layer stack consumption layers L3 (training), L4 (inference / COGS), L5 (people and other) by year, both companies (E3 A5:K40); L1-L2 annualized links from 09_Obligations; per-run reference, the $50B split and the Q2 GM cross-check grid (E9 A45:K60); unit-economics block.", kind="note")
    sh.section(4, "CONSUMPTION LAYERS L3-L5 BY YEAR, ANTHROPIC (GROSS basis: L4 also carries cloud-partner payouts) (Exhibit E3; A5:K40)", ncols=11)
    sh.yearhdr(5, label="Item"); sh.put("B5", "Unit", kind="header"); sh.put("C5", "Basis / source", kind="header")
    rev = {y: f"='02_Revenue'!{YC[y]}71" for y in range(2024, 2031)}; rev[2023] = "HOLE"
    tsrow(sh, 6, "REVA3", "Revenue GROSS (02_Revenue row 71)", "$M", "02_Revenue", rev, bold=True)
    gm = {2024: f"={R('A07_2024')}", 2025: f"={R('A07_2025')}"}
    gm.update({y: f"={RY('GMA', y)}" for y in FYEARS}); gm[2023] = "HOLE"
    tsrow(sh, 7, "GM3", "Gross margin path (2024-2025 L-119; 2026E+ GMA driver)", "fraction", "L-119 · recalled · T4 · GROSS-basis margin; 2026E+ AJ", gm, nf=PCT)
    cogs = {y: f"={YC[y]}6*(1-{YC[y]}7)" for y in range(2024, 2031)}; cogs[2023] = "HOLE"
    tsrow(sh, 8, "COGSA", "L4 Inference / COGS = revenue x (1 - GM) (2024: 1,940; 2025: on SW_A_FY25)", "$M/yr", "derived; includes partner payouts on the GROSS basis", cogs, bold=True)
    trn = {y: f"={RY('TRNA', y)}" for y in FYEARS}; trn.update({2023: "HOLE", 2024: "HOLE", 2025: "HOLE"})
    tsrow(sh, 9, "TRNA3", "L3 Training (annual budget, C-11; 2026-2028 L-125 x factor; 2029-2030 AJ)", "$M/yr", "L-125 · recalled · T4 · annual budget (C-11)", trn, bold=True)
    comp = {y: f"={RY('HCA', y)}*{R('COMPA')}" for y in FYEARS}; comp.update({2023: "HOLE", 2024: "HOLE", 2025: "HOLE"})
    tsrow(sh, 10, "COMPA3", "L5 Comp = headcount (SW_A_HC path) x loaded cash comp per head (COMPA)", "$M/yr", "L-008 / L-091 (SW_A_HC); L-165 anchors; SBC HOLE", comp)
    cr = {y: f"={R('A21a')}" for y in FYEARS}; cr[2026] = f"={R('A14')}"; cr.update({2023: "HOLE", 2024: "HOLE", 2025: "HOLE"})
    tsrow(sh, 11, "COPYA3", "L5 Copyright cash (Bartz settlement 2026; music demands >3,000 unreserved, not carried)", "$M/yr", "L-086 · confirmed · T2 · cash 2026", cr)
    tsrow(sh, 12, "DATAA3", "L5 Data licensing (AJ; L-113 anchor)", "$M/yr", "AJ · L-113 (T1) marquee sources ~50-70 each", {y: f"={R('DATAA')}" for y in FYEARS})
    tsrow(sh, 13, "EXPA3", "L5 Expert data / labeling (AJ; L-114 anchor)", "$M/yr", "AJ · L-114 (T4) 1-3B per year per lab", {y: f"={R('EXPA')}" for y in FYEARS})
    tsrow(sh, 14, "SAFA3", "L5 Safety / eval (AJ; L-117 anchor)", "$M/yr", "AJ · L-117 (CNV, T4) 55-115", {y: f"={R('SAFA')}" for y in FYEARS})
    tsrow(sh, 15, "GTMA3", "L5 GTM + G&A (HOLE placeholder: % of comp; L-118 workforce mix)", "$M/yr", "HOLE · L-118 (T4) mix 35/35/30", {y: f"={YC[y]}10*{R('GTMA')}" for y in FYEARS})
    l5 = {y: f"=SUM({YC[y]}10:{YC[y]}15)" for y in FYEARS}; l5.update({2023: "HOLE", 2024: "HOLE", 2025: "HOLE"})
    tsrow(sh, 16, "L5A", "L5 People and everything else, total (2023-2025 HOLE: no ledger opex)", "$M/yr", "sum of rows 10-15", l5, bold=True)
    tsrow(sh, 17, "L1A3", "L1 Silicon, annualized priced (09_Obligations row 62)", "$M/yr", "09_Obligations (SPV lease)", {y: f"='09_Obligations'!{YC[y]}62" for y in YEARS})
    tsrow(sh, 18, "L2A3", "L2 Capacity, annualized priced (09_Obligations row 63)", "$M/yr", "09_Obligations (AWS, Azure, SpaceX, Nscale, Lambda, Volta, Riot)", {y: f"='09_Obligations'!{YC[y]}63" for y in YEARS})
    tsrow(sh, 19, "PRICEDA3", "L1 + L2 priced commitments", "$M/yr", "derived", {y: f"={YC[y]}17+{YC[y]}18" for y in YEARS}, bold=True)
    envc = {y: f"={YC[y]}8+{YC[y]}9" for y in FYEARS}
    tsrow(sh, 20, "ENVA", "Compute envelope = L3 + L4 (COGS + training) at SW_SCEN", "$M/yr", "derived; feeds 09_Obligations row 84 (E10 scenario envelope)", envc, bold=True)
    tsrow(sh, 21, "TOTA3", "Total consumption L3 + L4 + L5", "$M/yr", "derived", {y: f"={YC[y]}20+{YC[y]}16" for y in FYEARS}, bold=True)
    tsrow(sh, 22, "XCHKA", "Cross-layer check: envelope - priced commitments (before the Google leg and AMD; positive = priced sits inside the envelope)", "$M/yr", "cost-stack section 2 cross-layer row", {y: f"={YC[y]}20-{YC[y]}19" for y in FYEARS})
    sh.put("A23", "2026E: priced (L1 3,450 + L2 24,708) sits inside the derived COGS + training envelope (30,000-42,000): consistent. 2027E-2028E: consistent BEFORE the Google leg and AMD; the E10 block on 09_Obligations adds them.", kind="note")

    sh.section(25, "CONSUMPTION LAYERS L3-L5 BY YEAR, OPENAI (NET revenue basis)", ncols=11)
    sh.yearhdr(26, label="Item"); sh.put("B26", "Unit", kind="header"); sh.put("C26", "Basis / source", kind="header")
    revo = {y: f"='02_Revenue'!{YC[y]}78" for y in range(2025, 2031)}; revo.update({2023: "HOLE", 2024: "HOLE"})
    tsrow(sh, 27, "REVO3", "Revenue NET presumed (02_Revenue row 78)", "$M", "02_Revenue", revo, bold=True)
    cpct = {2025: f"=1-{R('O07_gm2025')}", 2026: f"=IFERROR({R('O07_inf2026')}/G27,0)"}; cpct.update({y: f"={RY('OCOGS', y)}" for y in range(2027, 2031)}); cpct.update({2023: "HOLE", 2024: "HOLE"})
    tsrow(sh, 28, "CPCTO", "COGS as % of revenue (2025 = 1 - 33% GM; 2026 = inference 14,100 / FY2026E, implied; 2027E+ OCOGS driver)", "fraction", "L-083 (T3); AJ path", cpct, nf=PCT)
    cogso = {2025: f"={R('O01')}*(1-{R('O07_gm2025')})", 2026: f"={R('O07_inf2026')}"}; cogso.update({y: f"={YC[y]}27*{YC[y]}28" for y in range(2027, 2031)}); cogso.update({2023: "HOLE", 2024: "HOLE"})
    tsrow(sh, 29, "COGSO", "L4 Inference / COGS (2025 total COGS = O01 x (1 - 33%) = 8,777; 2026 = O07 inference 14,100 only, flagged; 2027E+ = revenue x AJ %)", "$M/yr", "L-063, L-083 (T3); 2027E+ AJ", cogso, bold=True)
    tsrow(sh, 30, "INFO3", "   memo: inference cost 2025 (Sacra) and 2026E", "$M/yr", "L-083 · estimated · T3", {2025: f"={R('O07_inf2025')}", 2026: f"={R('O07_inf2026')}"})
    trno = {y: f"={RY('TRNO', y)}" for y in FYEARS}; trno.update({2023: "HOLE", 2024: "HOLE", 2025: "HOLE"})
    tsrow(sh, 31, "TRNO3", "L3 Training (annual budget, C-11; 2026-2029 L-125; 2030 AJ)", "$M/yr", "L-125 · recalled · T4 · annual budget (C-11)", trno, bold=True)
    compo = {y: f"={RY('HCO', y)}*{R('COMPO')}" for y in FYEARS}; compo.update({2023: "HOLE", 2024: "HOLE", 2025: "HOLE"})
    tsrow(sh, 32, "COMPO3", "L5 Comp = headcount path (4,500 -> 8,000 linear 2026, then +20%/yr) x comp per head (COMPO)", "$M/yr", "L-027, L-090; AJ 0.8 / 0.7 / 0.6", compo)
    ret = {2025: f"={R('O09_pp')}*{R('O09_n')}/{R('O09_yrs')}", 2026: f"={R('O09_pp')}*{R('O09_n')}/{R('O09_yrs')}"}; ret.update({y: f"={R('A21a')}" for y in range(2027, 2031)})
    tsrow(sh, 33, "RETO3", "L5 Retention bonuses (~1.5 x ~1,000 over 2 yrs, split 2025-2026)", "$M/yr", "L-093 · estimated · T3; L-166 · could-not-verify", ret)
    oth = {y: f"=MAX(0,{R('OAIOPEX')}*{YC[y]}27-{YC[y]}32-{YC[y]}33)" for y in range(2027, 2031)}; oth.update({2026: f"={R('A21a')}"})
    tsrow(sh, 34, "OTHO3", "L5 Other opex ex-compute (2027E+: residual so that L5 = OAIOPEX % of revenue; AJ)", "$M/yr", "AJ · OAIOPEX (Bear 40 / Base 30 / Bull 20%)", oth)
    l5o = {y: f"=SUM({YC[y]}32:{YC[y]}34)" for y in FYEARS}; l5o[2025] = "=F33"; l5o.update({2023: "HOLE", 2024: "HOLE"})
    tsrow(sh, 35, "L5O", "L5 People and everything else, total (2025 = retention only; comp HOLE)", "$M/yr", "sum of rows 32-34", l5o, bold=True)
    tsrow(sh, 36, "L1O3", "L1 Silicon, annualized priced (09_Obligations row 66)", "$M/yr", "09_Obligations (Cerebras)", {y: f"='09_Obligations'!{YC[y]}66" for y in YEARS})
    tsrow(sh, 37, "L2O3", "L2 Capacity, annualized priced (09_Obligations row 67)", "$M/yr", "09_Obligations (Oracle, AWS, CoreWeave, Azure proxy)", {y: f"='09_Obligations'!{YC[y]}67" for y in YEARS})
    tsrow(sh, 38, "PRICEDO3", "L1 + L2 priced commitments", "$M/yr", "derived", {y: f"={YC[y]}36+{YC[y]}37" for y in YEARS}, bold=True)
    tsrow(sh, 39, "ENVO", "Compute envelope = L3 + L4 (COGS + training) at SW_SCEN", "$M/yr", "derived", {y: f"={YC[y]}29+{YC[y]}31" for y in FYEARS}, bold=True)
    tsrow(sh, 40, "TOTO3", "Total consumption L3 + L4 + L5", "$M/yr", "derived", {y: f"={YC[y]}39+{YC[y]}35" for y in FYEARS}, bold=True)
    sh.put("A41", "2027E: priced commitments ~110,000 + training 60,000 (T4; part of the same compute) vs burn plan 57,000-63,000 (L-082): the revenue required to hold burn at ~60,000 is a multiple of the July run-rate (cost-stack section 3).", kind="note")

    sh.section(44, "TRAINING VS INFERENCE: per-run reference (never summed), the $50B split, the Q2 GM cross-check grid (Exhibit E9; A45:K60)", ncols=11)
    sh.put("A45", "Per-run reference (L-115, Epoch AI; final-run amortized compute; basis differs from the annual budgets above, C-11): printed beside, never summed", bold=True)
    sh.header(46, ["", "", "", "Grok 4", "GPT-4.5 pre-train", "GPT-4.5 post-train", "GPT-4", "Gemini Ultra", "Llama 3.1-405B", "growth (x per yr)", ">1,000 by 2027"])
    sh.put("A47", "Per-run compute cost ($M)"); sh.put("C47", "L-115 · estimated · T3", kind="note")
    for col, k, nf in (("D", "X04_grok4", NUM), ("E", "X04_gpt45", NUM), ("F", "X04_gpt45_post", NUM), ("G", "X04_gpt4", NUM), ("H", "X04_gemini", NUM), ("I", "X04_llama", NUM), ("J", "X04_growth", CNT1), ("K", "X04_1b", NUM)):
        sh.put(f"{col}47", f"={R(k)}", kind="formula", nf=nf, key=f"RUNREF_{k}")
    sh.put("A48", "Anthropic 2026 training budget 7,000 (L-125) is 14x Grok 4's ~500 final run: the budget aggregates all runs, experiments and post-training (C-11), so the two bases are shown side by side and never summed.", kind="note")
    sh.put("A49", "The $50B split (OpenAI 2026): compute spend 50,000 (LB07a, T2) less training budget 25,000 (L-125, T4) less inference 14,100 (L-083, T3) = unexplained (printed as a check, not allocated)", bold=True)
    sh.put("D49", "=LB07a", kind="formula", nf=NUM); sh.put("E49", f"=-{R('O06_2026')}", kind="formula", nf=NUM); sh.put("F49", f"=-{R('O07_inf2026')}", kind="formula", nf=NUM)
    sh.put("G49", "=D49+E49+F49", kind="formula", nf=NUM, bold=True, key="UNEXPL"); ck(sh, "H49", "G49", "UNEXPL"); sh.put("I49", "the T4 split does not reconcile to the T2 total", kind="note")
    sh.put("A51", "Q2-2026 GM cross-check grid: implied gross margin = (LB05b adjusted operating income + quarterly opex) / Q2 revenue on each basis. LB05b is a non-GAAP adjusted operating income (excludes SBC per relays; definition unpublished, L-151/L-152), so the implied GM is an ADJUSTED GM.", bold=True)
    sh.header(52, ["Quarterly opex (AJ)", "Unit", "Source", "GROSS", "NET-39.75", "NET-27", "Note"])
    sh.put("A53", "Q2 revenue on each basis"); sh.put("B53", "$M", kind="note"); sh.put("C53", "LB05a; R01; R02", kind="note")
    sh.put("D53", "=LB05a", kind="formula", nf=NUM); sh.put("E53", f"=LB05a*(1-{R('R01')})", kind="formula", nf=NUM); sh.put("F53", f"=LB05a*(1-{R('R02')})", kind="formula", nf=NUM)
    for i, (k, lab) in enumerate((("OPEXQ2_BEAR", "opex 3,000"), ("OPEXQ2_BASE", "opex 4,000"), ("OPEXQ2_BULL", "opex 5,000"))):
        rr = 54 + i
        sh.put(f"A{rr}", f"Implied adjusted GM at {lab}"); sh.put(f"B{rr}", "fraction", kind="note"); sh.put(f"C{rr}", f"={R(k)}", kind="formula", nf=NUM)
        for col in "DEF":
            sh.put(f"{col}{rr}", f"=(LB05b+$C{rr})/{col}$53", kind="formula", nf=PCT, key=(f"GMGRID_{col}" if i == 0 else None))
    ck(sh, "G54", "D54", "GM_GRID_G"); ck(sh, "H54", "E54", "GM_GRID_N"); sh.put("I54", "check 31% / 51% at 3,000 gross / net-39.75", kind="note")
    sh.put("A57", "Second cross-check from A19 (T4 compute-cost ratio, display only): 1 - 0.56 = gross-basis GM if compute is the whole of cost of revenue (Q1 in E)"); sh.put("D57", f"=1-{R('A19b')}", kind="hole", nf=PCT, key="A19_GM_Q2"); sh.put("E57", f"=1-{R('A19a')}", kind="hole", nf=PCT, key="A19_GM_Q1")
    sh.put("A58", "If partner payouts sat beside compute in cost of revenue: 1 - 0.56 - SW_HAIRCUT (live) / at 39.75% / at 27%"); sh.put("D58", f"=1-{R('A19b')}-SW_HAIRCUT", kind="hole", nf=PCT2, key="A19_GM_PAYOUT"); sh.put("E58", f"=1-{R('A19b')}-{R('R01')}", kind="hole", nf=PCT2); sh.put("F58", f"=1-{R('A19b')}-{R('R02')}", kind="hole", nf=PCT2)
    sh.put("A59", "Required opex ratio at opex 3,000 (opex / Q2 revenue) and the consistency flag"); sh.put("D59", f"={R('OPEXQ2_BEAR')}/LB05a", kind="formula", nf=PCT)
    sh.put("E59", '=IF(D58<D59,"INCONSISTENT: a positive adjusted result is impossible if partner payouts sit beside compute at this haircut; either the 0.56 already contains the payouts or the effective payout share is well below 39.75% (a datapoint against the C-13 internal branch; T4 on both legs)","consistent")', kind="flag", key="A19_FLAG")
    sh.put("A60", "Ruling 3: LB05b is not FCF and not an operating profit; every label reads 'adjusted'.", kind="note")
    sh.section(62, "UNIT-ECONOMICS BLOCK: list prices (display); $/token COGS = HOLE (L-116: none disclosed)", ncols=11)
    sh.header(63, ["Model", "Input $/MTok", "Output $/MTok", "Note"])
    for i, (lab, ki, ko) in enumerate((("Fable 5.1", "A18_f51_in", "A18_f51_out"), ("Opus 5", "A18_o5_in", "A18_o5_out"), ("Sonnet 5", "A18_s5_in", "A18_s5_out"), ("Haiku 4.5", "A18_h45_in", "A18_h45_out"))):
        rr = 64 + i
        sh.put(f"A{rr}", lab); sh.put(f"B{rr}", f"={R(ki)}", kind="formula", nf=CNT2); sh.put(f"C{rr}", f"={R(ko)}", kind="formula", nf=CNT2); sh.put(f"D{rr}", "L-084 · confirmed · T1 · 2026-09-09 · pricing page", kind="note")
    sh.put("A68", "Fast Mode (Opus 5) multiplier / cache read (Fable 5.1)"); sh.put("B68", f"={R('A18_fast')}", kind="formula", nf=CNT1); sh.put("C68", f"={R('A18_cache')}", kind="formula", nf=CNT2)
    sh.put("A69", "$ per token COGS"); sh.put("B69", "HOLE", kind="hole"); sh.put("D69", "L-116: no $/million-token COGS disclosure exists for either lab; Workbook B G20 derives a serving-cost ESTIMATE from throughput (L-164) and GPU-hour rates (L-104, L-105)", kind="note")
    sh.ws.freeze_panes = "D6"


# ----------------------------------------------------------------------------------------------------
# 04_PL
# ----------------------------------------------------------------------------------------------------
def build_04(sh):
    sh.put("A1", "04_PL: P&L rollup 2023A-2030E, both companies; dual view (excl-training / incl-training) built ONLY from ledger rows and AJ inputs; no breakeven-year cells; H1-2026 actuals block (A30:H40).", kind="note")
    sh.section(3, "ANTHROPIC P&L (GROSS revenue; every net figure shows its haircut in column C)", ncols=11)
    sh.yearhdr(4, label="Item"); sh.put("B4", "Unit", kind="header"); sh.put("C4", "Basis / source", kind="header")
    tsrow(sh, 5, "PLA_REV", "Revenue GROSS", "$M", "03_Costs row 6", {y: f"='03_Costs'!{YC[y]}6" for y in range(2024, 2031)} | {2023: "HOLE"}, bold=True)
    tsrow(sh, 6, "PLA_NET", "Revenue NET at SW_HAIRCUT", "$M", "=SW_HAIRCUT", {y: f"={YC[y]}5*(1-SW_HAIRCUT)" for y in range(2024, 2031)}, srckind="formula")
    sh.put("C6", "=SW_HAIRCUT", kind="formula", nf=PCT2)
    tsrow(sh, 7, "PLA_COGS", "COGS (L4)", "$M", "03_Costs row 8", {y: f"='03_Costs'!{YC[y]}8" for y in range(2024, 2031)} | {2023: "HOLE"})
    tsrow(sh, 8, "PLA_GP", "Gross profit", "$M", "derived", {y: f"={YC[y]}5-{YC[y]}7" for y in range(2024, 2031)}, bold=True)
    tsrow(sh, 9, "PLA_GM", "Gross margin", "fraction", "derived", {y: f"=IFERROR({YC[y]}8/{YC[y]}5,0)" for y in range(2024, 2031)}, nf=PCT)
    tsrow(sh, 10, "PLA_TRN", "Training (L3)", "$M", "03_Costs row 9", {y: f"='03_Costs'!{YC[y]}9" for y in FYEARS} | {2023: "HOLE", 2024: "HOLE", 2025: "HOLE"})
    tsrow(sh, 11, "PLA_L5", "Other opex (L5)", "$M", "03_Costs row 16", {y: f"='03_Costs'!{YC[y]}16" for y in FYEARS} | {2023: "HOLE", 2024: "HOLE", 2025: "HOLE"})
    tsrow(sh, 12, "PLA_OPX", "Operating result EXCL. training = GP - L5", "$M", "derived (dual view)", {y: f"={YC[y]}8-{YC[y]}11" for y in FYEARS}, bold=True)
    tsrow(sh, 13, "PLA_OPI", "Operating result INCL. training = GP - L5 - L3", "$M", "derived (dual view)", {y: f"={YC[y]}8-{YC[y]}11-{YC[y]}10" for y in FYEARS}, bold=True)
    tsrow(sh, 14, "PLA_NI24", "Net result FY2024A (SW_A_FY24_NI; C-05)", "$M", "L-012 · estimated · T2 · PB deal-record financials; switch visible in C", {2024: "=SW_A_FY24_NI"})
    sh.put("C14", "=SW_A_FY24_NI", kind="formula", nf=NUM)
    tsrow(sh, 15, "PLA_BURN25", "FY2025 burn (register; display)", "$M", "L-120 · recalled · T4", {2025: f"={R('A09_burn2025')}"})
    sh.put("A16", "WSJ Apr-6 dual-P&L breakevens not carried (no ledger row; argument-map AM-32). No breakeven-year cells on this tab.", kind="note")
    sh.put("A17", "C-12 note (2026E): SW_A_2026_LOSS ="); sh.put("D17", "=SW_A_2026_LOSS", kind="formula"); sh.put("A18", "2023A-2025A cells link only to ledger facts (A05, A06 via SW_A_FY25, O01, O02, LB06) and otherwise read HOLE.", kind="note")

    sh.section(20, "OPENAI P&L (NET revenue presumed; basis switch SW_OAI_BASIS applies to the run-rate rows on 02_Revenue)", ncols=11)
    sh.yearhdr(21, label="Item"); sh.put("B21", "Unit", kind="header"); sh.put("C21", "Basis / source", kind="header")
    tsrow(sh, 22, "PLO_REV", "Revenue NET presumed", "$M", "03_Costs row 27", {y: f"='03_Costs'!{YC[y]}27" for y in range(2025, 2031)} | {2023: "HOLE", 2024: "HOLE"}, bold=True)
    tsrow(sh, 23, "PLO_COGS", "COGS (L4)", "$M", "03_Costs row 29", {y: f"='03_Costs'!{YC[y]}29" for y in range(2025, 2031)} | {2023: "HOLE", 2024: "HOLE"})
    tsrow(sh, 24, "PLO_GP", "Gross profit", "$M", "derived", {y: f"={YC[y]}22-{YC[y]}23" for y in range(2025, 2031)}, bold=True)
    tsrow(sh, 25, "PLO_GM", "Gross margin", "fraction", "derived (2025 = 33%, L-083)", {y: f"=IFERROR({YC[y]}24/{YC[y]}22,0)" for y in range(2025, 2031)}, nf=PCT)
    tsrow(sh, 26, "PLO_TRN", "Training (L3)", "$M", "03_Costs row 31", {y: f"='03_Costs'!{YC[y]}31" for y in FYEARS} | {2023: "HOLE", 2024: "HOLE", 2025: "HOLE"})
    tsrow(sh, 27, "PLO_L5", "Other opex (L5)", "$M", "03_Costs row 35", {y: f"='03_Costs'!{YC[y]}35" for y in range(2025, 2031)} | {2023: "HOLE", 2024: "HOLE"})
    tsrow(sh, 28, "PLO_OPX", "Operating result EXCL. training = GP - L5", "$M", "derived (dual view)", {y: f"={YC[y]}24-{YC[y]}27" for y in FYEARS}, bold=True)
    tsrow(sh, 29, "PLO_OPI", "Operating result INCL. training = GP - L5 - L3", "$M", "derived (dual view)", {y: f"={YC[y]}24-{YC[y]}27-{YC[y]}26" for y in FYEARS}, bold=True)
    sh.section(30, "H1-2026 ACTUALS BLOCK (Exhibit E9 companion; A30:H40)", ncols=11)
    sh.header(31, ["Item", "Unit", "Source", "Anthropic", "OpenAI", "Note"])
    h1 = [
        (32, "Q1-2026 revenue", "$M", "L-151 · T2 / L-066 · T2", f"={R('A03')}", f"={R('LB06a_Q1')}", "recognized; Anthropic GROSS presumed, OpenAI NET presumed"),
        (33, "Q2-2026 revenue", "$M", "L-033 · T2 / L-066 · T2", "=LB05a", "=LB06a", "Anthropic preliminary (11,500-11,600)"),
        (34, "H1-2026 recognized", "$M", "derived", "=D32+D33", "=E32+E33", "Anthropic 16,330 (16,230 on the >11,500 print)"),
        (35, "Q2 / Q1", "x", "derived", "=D33/D32", "=E33/E32", "2.45x vs 1.18x"),
        (36, "Q2-2026 operating result: Anthropic = ADJUSTED operating income, non-GAAP (LB05b; definition unpublished; excludes SBC per relays); OpenAI = operating loss incl. SBC (LB06b)", "$M", "L-034, L-151, L-152 · T2/T3 / L-066 · T2", "=LB05b", "=-LB06b", "sign confirmed for Anthropic; amount is a projection"),
        (37, "Q1-2026 operating result (OpenAI operating loss incl. SBC)", "$M", "L-066 · T2", "HOLE", f"=-{R('LB06b_Q1')}", "no Anthropic Q1 result disclosed"),
        (38, "Adjusted operating margin: Anthropic on the 10,900 Reuters base (5.1%) and on 11,600 (in F); OpenAI H1 operating loss / H1 revenue (x)", "fraction", "L-152 (derived) / L-066", f"=LB05b/{R('LB05b_base')}", "=-(E36+E37)/E34", "OpenAI 1.74x loss-to-revenue, widening"),
        (39, "OpenAI operating loss QoQ change (Q1 9,300 -> Q2 12,300)", "fraction", "L-066 · T2", "n/a", f"=LB06b/{R('LB06b_Q1')}-1", "+32%: 'worsening 10-50%' band (AIBQ CE-3)"),
        (40, "H1-2026 on the '>11,500' print (Anthropic); OpenAI H1 operating loss incl. SBC", "$M", "L-151 / L-066", f"={R('A03')}+{R('LB05a_low')}", f"=-({R('LB06b_Q1')}+LB06b)", ""),
    ]
    for rr, lab, unit, src, a, o, note in h1:
        sh.put(f"A{rr}", lab); sh.put(f"B{rr}", unit, kind="note"); sh.put(f"C{rr}", src, kind="note")
        nf = PCT if unit == "fraction" else (MULT2 if unit == "x" else NUM)
        for col, v in (("D", a), ("E", o)):
            if v == "HOLE":
                sh.put(f"{col}{rr}", "HOLE", kind="hole")
            elif v == "n/a":
                sh.put(f"{col}{rr}", "n/a", kind="note")
            else:
                sh.put(f"{col}{rr}", v, kind="formula", nf=nf, bold=True)
        sh.put(f"F{rr}", note, kind="note")
    sh.put("F38", "=LB05b/LB05a", kind="formula", nf=PCT); sh.put("G38", "adjusted margin on 11,600", kind="note")
    sh.put("F34", "=D34", kind="formula", nf=NUM, key="H1A_PL"); ck(sh, "G34", "F34", "H1A")
    sh.put("F35", "=D35", kind="formula", nf=MULT2); ck(sh, "G35", "F35", "Q2Q1")
    sh.put("A41", "2025A OpenAI: reported operating loss 20,920 and group loss 60,350 incl. the 41,550 fair-value swing (O02, recalled T3) are displayed on 01_Data and not reconstructed here; 2023A-2024A read HOLE.", kind="note")
    sh.ws.freeze_panes = "D5"
