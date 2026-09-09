# tabs_a3.py: Workbook A: 05_Cash_Fund, 11_AIBQ, 06_Valuation, 07_Sensitivity, 10_Financing, 13_OutsideView, 08_Output.
from xlhelp import *
from tabs_a1 import ck, CHECKS


# ----------------------------------------------------------------------------------------------------
# 05_Cash_Fund
# ----------------------------------------------------------------------------------------------------
def build_05(sh):
    sh.put("A1", "05_Cash_Fund: capitalization (equity rounds reproduce LB03 / LB04; debt and lease obligations shown separately; identity checks), the CE walk Jul-16 -> Sep-9 equity-only at every basis (E13 A40:H55), burn walks, facilities block.", kind="note")
    sh.section(3, "CAPITALIZATION (Ruling 1: CE denominators are equity-only; the SPV and project debt are off-balance-sheet obligations, display only)", ncols=11)
    sh.header(4, ["Item", "Unit", "Source", "Anthropic ($M)", "Note", "", "OpenAI item", "Unit", "Source", "OpenAI ($M)", "Note"])
    ra = [("Series A", "ANT_R01"), ("Series B", "ANT_R02"), ("Series C", "ANT_R03"), ("Alphabet convertible-to-equity", "ANT_R04"), ("Series D", "ANT_R05"),
          ("Amazon round (incl. 1,300 convertible)", "ANT_R06"), ("Series E", "ANT_R07"), ("Series F (incl. 750 convertible)", "ANT_R08"), ("Series G", "ANT_R09"), ("Series H", "ANT_R10")]
    for i, (lab, k) in enumerate(ra):
        rr = 5 + i
        sh.put(f"A{rr}", lab); sh.put(f"B{rr}", "$M", kind="note"); sh.put(f"C{rr}", "L-018 / L-017 / L-016 / L-015 · confirmed · T2 · PB deal record", kind="note"); sh.put(f"D{rr}", f"={R(k)}", kind="formula", nf=NUM)
    sh.put("A15", "Sum of the ten equity rounds (must equal LB03)", bold=True); sh.put("D15", "=SUM(D5:D14)", kind="formula", nf=NUM, bold=True, key="EQ_SUM_A")
    sh.put("E15", f'=IF(ABS(D15-LB03)<{R("TOL_IDENT_A")},"ties to LB03 (124,254)","BROKEN")', kind="formula", bold=True)
    sh.put("A16", "Revolver (debt; in PB Total Raised, not equity)"); sh.put("C16", "L-014 · confirmed · T2 · 2025-05-16", kind="note"); sh.put("D16", f"={R('A11')}", kind="formula", nf=NUM)
    sh.put("A17", "Identity: LB03 + 2,500 = PB Total Raised 126,754 (L-006)", bold=True); sh.put("D17", "=LB03+D16", kind="formula", nf=NUM, bold=True, key="IDENT_A"); ck(sh, "E17", "D17", "IDENT_A")
    sh.put("F17", f"={R('PB_TOTAL_A')}", kind="formula", nf=NUM); sh.put("G17", "PB Total Raised (L-006)", kind="note")
    for i, (lab, k, src) in enumerate((("Contingent inflow: Amazon (milestones; up to)", "A17_amzn", "L-072 · T1"), ("Contingent inflow: Google (performance targets)", "A17_goog", "L-073 · T2"), ("Contingent inflow: AMD (through FY2028; up to)", "A17_amd", "L-043 · T1"))):
        rr = 18 + i
        sh.put(f"A{rr}", lab); sh.put(f"C{rr}", src, kind="note"); sh.put(f"D{rr}", f"={R(k)}", kind="formula", nf=NUM); sh.put(f"E{rr}", "shown, not added to capital raised", kind="note")
    sh.put("A21", "Contingent inflows, total (shown, not added)", bold=True); sh.put("D21", "=SUM(D18:D20)", kind="formula", nf=NUM, key="INFLOW_A")
    sh.put("A22", "Off-balance-sheet: TPU lease SPV (lessor debt, L-044; PB removed it from Total Raised, C-01)"); sh.put("C22", "L-044 · estimated · T3", kind="note"); sh.put("D22", f"={R('A12')}", kind="formula", nf=NUM)
    sh.put("A23", "Off-balance-sheet: project-company debt, five TPU sites (Google conditional support)"); sh.put("C23", "L-045 · estimated · T3", kind="note"); sh.put("D23", f"={R('A13')}", kind="formula", nf=NUM)
    sh.put("A24", "Total raised VIEW (SW_TOTAL_RAISED_VIEW; display only; CE never changes)", bold=True); sh.put("C24", "=SW_TOTAL_RAISED_VIEW", kind="formula")
    sh.put("D24", '=IF(SW_TOTAL_RAISED_VIEW="On-balance-sheet",D17,D17+D22)', kind="formula", nf=NUM, bold=True, key="TR_VIEW"); sh.put("E24", "On-balance-sheet = equity + revolver; Incl. lease SPV adds the 34,500 lessor debt (the retired PB 161,254 view)", kind="note")
    sh.put("A25", "Series H composition (L-038, T1): 65,000 incl. previously committed hyperscaler money, of which Amazon"); sh.put("D25", f"={R('A16')}", kind="formula", nf=NUM); sh.put("E25", f"={R('A16_prior')}", kind="formula", nf=NUM); sh.put("F25", f"={R('A16_amzn')}", kind="formula", nf=NUM); sh.put("G25", "new-cash relevance only", kind="note")
    ro = [("Microsoft (Jul-2019)", "OAI_R01"), ("Series A", "OAI_R02"), ("Jul-2021 round", "OAI_R03"), ("Microsoft (Jan-2023; paid over multiple years)", "OAI_R04"), ("Apr-2023 round", "OAI_R05"),
          ("Series B (Oct-2024)", "OAI_R06"), ("Series F (Mar-2025)", "OAI_R07"), ("Jan-2025 round", "OAI_R08"), ("Mar-2026 round, equity portion", "OAI_R09")]
    for i, (lab, k) in enumerate(ro):
        rr = 5 + i
        sh.put(f"G{rr}", lab); sh.put(f"H{rr}", "$M", kind="note"); sh.put(f"I{rr}", "L-022 · estimated · T2 · PB deal records", kind="note"); sh.put(f"J{rr}", f"={R(k)}", kind="formula", nf=NUM1)
    sh.put("G15", "Sum of the equity rounds (must equal LB04)", bold=True); sh.put("J15", "=SUM(J5:J13)", kind="formula", nf=NUM1, bold=True, key="EQ_SUM_O")
    sh.put("K15", f'=IF(ABS(J15-LB04)<{R("TOL_IDENT_O")},"ties to LB04 (181,216.5)","BROKEN")', kind="formula", bold=True)
    sh.put("G16", "Debt: 4,000 revolver + 700 + 520 term loan (O10)"); sh.put("I16", "L-023 · confirmed · T2", kind="note"); sh.put("J16", f"={R('O10')}", kind="formula", nf=NUM)
    sh.put("G17", "Identity: LB04 + 5,220 = PB Total Raised 186,436.5 (L-021)", bold=True); sh.put("J17", "=LB04+J16", kind="formula", nf=NUM1, bold=True, key="IDENT_O"); ck(sh, "K17", "J17", "IDENT_O")
    sh.put("G18", "Microsoft funding commitments (L-157, T1): committed / funded / unfunded"); sh.put("J18", f"={R('O13_commit')}", kind="formula", nf=NUM); sh.put("K18", f"={R('O13_funded')}", kind="formula", nf=NUM)
    sh.put("G19", "Unfunded at 2026-06-30 and as % of LB04 (0.6%)"); sh.put("J19", "=J18-K18", kind="formula", nf=NUM, key="MSFT_UNFUNDED"); sh.put("K19", "=J19/LB04", kind="formula", nf=PCT2)
    sh.put("G20", "OpenAI CE if the unfunded 1,100 were stripped from the denominator (0.221x -> 0.222x; PB committed basis kept)"); sh.put("J20", f"={R('NET_O_LIVE')}/(LB04-J19)", kind="formula", nf=MULT3, key="CE_O_STRIPPED")
    sh.put("G21", "Nvidia equity into OpenAI (Mar-2026 round; inflow, not cost)"); sh.put("J21", f"={R('C21_equity')}", kind="formula", nf=NUM)
    sh.put("G22", "OpenAI cash at end-2025 (~; L-082 T3)"); sh.put("J22", f"={R('O05_cash25')}", kind="formula", nf=NUM)

    sh.section(40, "CAPITAL EFFICIENCY WALK, JUL-16 -> SEP-9, EQUITY-ONLY, BOTH BASES (Exhibit E13; A40:H55). CE = net run-rate / equity-only raised (Ruling 1); haircut visible in column C (Ruling 5).", ncols=11)
    sh.header(41, ["Row", "Anthropic run-rate GROSS", "Haircut", "Anthropic net run-rate", "Anthropic CE (x)", "OpenAI net run-rate", "OpenAI CE (x)", "Ratio (A / O)", "OpenAI basis", "Check"])
    sh.put("A42", "Jul-16 register (L-133, recalled T4): 47,000 gross -> 28,318 net; OpenAI 25,000")
    sh.put("B42", f"={R('A01c')}", kind="formula", nf=NUM); sh.put("C42", f"={R('R01')}", kind="formula", nf=PCT2); sh.put("D42", "=B42*(1-C42)", kind="formula", nf=NUM, key="NET_A_J16")
    sh.put("E42", "=D42/LB03", kind="formula", nf=MULT3, key="CE_A_J16"); sh.put("F42", f"={R('J16_OAI_RR')}", kind="formula", nf=NUM); sh.put("G42", "=F42/LB04", kind="formula", nf=MULT3, key="CE_O_J16")
    sh.put("H42", "=E42/G42", kind="formula", nf=MULT2, key="CE_RATIO_J16"); sh.put("I42", "NET (register)", kind="note"); ck(sh, "J42", "H42", "J16_RATIO")
    sh.put("K42", f"=\"register carried \"&TEXT({R('J16_CE_A')},\"0.000\")&\" / \"&TEXT({R('J16_CE_O')},\"0.000\")", kind="formula")
    walk = [
        (43, "Sep-9 at SW_HAIRCUT (live)", "=LB01", "=SW_HAIRCUT", f"={R('NET_A_LIVE')}", "CE_A_LIVE", f"={R('NET_O_LIVE')}", "CE_O_LIVE", "CE_RATIO_LIVE", "=SW_OAI_BASIS", None),
        (44, "Sep-9 at 39.75% (R01, Ruling 5)", "=LB01", f"={R('R01')}", f"={R('NET_A_3975')}", "CE_A_3975", f"={R('NET_O_NETCASE')}", "CE_O_NET", "CE_RATIO_3975", "NET", "RATIO"),
        (45, "Sep-9 at 27% (R02, C-13 external)", "=LB01", f"={R('R02')}", f"={R('NET_A_27')}", "CE_A_27", f"={R('NET_O_NETCASE')}", None, "CE_RATIO_27", "NET", "RATIO27"),
        (46, "Sep-9 GROSS (display only: forbidden basis, Ruling 5)", "=LB01", "n/a", "=LB01", "CE_A_GROSS", f"={R('NET_O_NETCASE')}", None, "CE_RATIO_GROSS", "NET", "RATIOG"),
        (47, "Sep-9 at 39.75%, OpenAI GROSS case (LB02 x (1 - R03), T4)", "=LB01", f"={R('R01')}", f"={R('NET_A_3975')}", None, f"={R('NET_O_GROSSCASE')}", "CE_O_GROSS", "CE_RATIO_G_CE", "GROSS (R03 = 20%, T4)", "RATIO_G_CE"),
    ]
    for rr, lab, g, hc, net, keyA, oai, keyO, keyR, basis, chk in walk:
        sh.put(f"A{rr}", lab, kind=("flag" if rr == 46 else "label"))
        sh.put(f"B{rr}", g, kind="formula", nf=NUM)
        sh.put(f"C{rr}", hc, kind=("formula" if hc.startswith("=") else "note"), nf=PCT2)
        sh.put(f"D{rr}", net, kind="formula", nf=NUM)
        sh.put(f"E{rr}", f"=D{rr}/LB03", kind="formula", nf=MULT3, key=keyA, bold=True, color=(RED if rr == 46 else None))
        sh.put(f"F{rr}", oai, kind="formula", nf=NUM)
        sh.put(f"G{rr}", f"=F{rr}/LB04", kind="formula", nf=MULT3, key=keyO, bold=True)
        sh.put(f"H{rr}", f"=E{rr}/G{rr}", kind="formula", nf=MULT2, key=keyR, bold=True)
        sh.put(f"I{rr}", basis, kind=("formula" if basis.startswith("=") else "note"))
        if chk:
            ck(sh, f"J{rr}", f"H{rr}", chk)
    ck(sh, "K44", "E44", "CE_3975"); ck(sh, "K45", "E45", "CE_27"); ck(sh, "K46", "E46", "CE_G"); ck(sh, "L44", "G44", "CE_O")
    sh.put("A48", "Change Jul-16 -> Sep-9 (at 39.75%): Anthropic CE, OpenAI CE, ratio"); sh.put("E48", "=E44-E42", kind="formula", nf=MULT3); sh.put("G48", "=G44-G42", kind="formula", nf=MULT3); sh.put("H48", "=H44-H42", kind="formula", nf=MULT2)
    sh.put("A49", "Reading: the data improved (run-rate +38%, CE 0.228x -> 0.315x equalized, OpenAI 0.138x -> 0.221x) while the AIBQ CE score falls: the fall is a method correction (11_AIBQ).", kind="note")
    sh.put("A50", "Every OpenAI net figure shows SW_OAI_BASIS (column I); every Anthropic net figure shows its haircut (column C).", kind="note")

    sh.section(52, "BURN WALK: OpenAI (both vintages) and the bridge from operating loss to burn; Anthropic C-12 block (SW_A_2026_LOSS); facilities block (SW_15B_FACILITY)", ncols=11)
    sh.header(53, ["Item", "Unit", "Source", "Value", "Note"])
    burn = [
        (54, "OpenAI burn plan 2026, Feb vintage / post-April vintage (in E)", "$M", "L-082 · estimated · T3 (two vintages)", f"={R('O05_b26feb')}", f"={R('O05_b26apr')}"),
        (55, "OpenAI burn plan 2027, Feb vintage / post-April vintage (in E)", "$M", "L-082 · estimated · T3", f"={R('O05_b27feb')}", f"={R('O05_b27apr')}"),
        (56, "OpenAI 2030 positive cash flow (Feb vintage plan) / end-2025 cash (in E)", "$M", "L-082 · estimated · T3", f"={R('O05_cf2030')}", f"={R('O05_cash25')}"),
        (57, "OpenAI Q1-2026 cash burn (vs Q1 operating loss 9,300 incl. SBC)", "$M", "L-142 · estimated · T3", f"={R('O05_q1burn')}", f"={R('LB06b_Q1')}"),
        (58, "Bridge: H1-2026 operating loss incl. SBC annualized (average quarter x 4)", "$M", "L-066 · confirmed · T2", f"=AVERAGE({R('LB06b_Q1')},LB06b)*{R('QPY')}", None),
        (59, "less SBC (AJ % of operating loss, SBCP)", "$M", "AJ · SBCP", f"=D58*{R('SBCP')}", f"={R('SBCP')}"),
        (60, "less burn plan 2026 (post-April vintage)", "$M", "L-082 · T3", "=E54", None),
        (61, "residual: vendor financing / prepayment timing / capitalized items (PLUG; HOLE)", "$M", "HOLE · residual, flagged", "=D58-D59-D60", None),
    ]
    for rr, lab, unit, src, v, e in burn:
        sh.put(f"A{rr}", lab, bold=(rr == 61)); sh.put(f"B{rr}", unit, kind="note"); sh.put(f"C{rr}", src, kind="note")
        sh.put(f"D{rr}", v, kind=("hole" if rr == 61 else "formula"), nf=NUM, bold=(rr == 61), key=("BURN_PLUG" if rr == 61 else None))
        if e:
            sh.put(f"E{rr}", e, kind="formula", nf=(PCT if rr == 59 else NUM))
    sh.put("A63", "Anthropic 2026 loss / burn (C-12, frozen): branch A = GAAP-style plan loss (Jan-2026, L-120 T4); branch B = Q2 positive ADJUSTED operating income trajectory (L-034, L-151 T2; non-GAAP, definition unpublished, L-152), annualized display = LB05b x 4; no plug", bold=True)
    sh.put("A64", "Branch A: 'expects to lose ~11,000 in 2026' (GAAP-style)"); sh.put("C64", "L-120 · recalled · T4 · 2026-01", kind="note"); sh.put("D64", f"={R('A09_loss2026')}", kind="formula", nf=NUM)
    sh.put("A65", "Branch B: Q2 adjusted operating income x 4 (display of the trajectory; NOT a forecast)"); sh.put("C65", "L-034, L-151 · T2; L-152 · T3", kind="note"); sh.put("D65", f"=LB05b*{R('QPY')}", kind="formula", nf=NUM)
    sh.put("A66", "Selected branch (SW_A_2026_LOSS)", bold=True); sh.put("C66", "=SW_A_2026_LOSS", kind="formula"); sh.put("D66", '=IF(SW_A_2026_LOSS="GAAP -11,000 (Jan plan)",D64,D65)', kind="formula", nf=NUM, bold=True, key="A_2026_RESULT")
    sh.put("A67", "FY2025 burn (register) / Jan-2026 planned 2026 burn ~3,000 (T3 recalled, not carried as a row)"); sh.put("C67", "L-120 · recalled · T4", kind="note"); sh.put("D67", f"={R('A09_burn2025')}", kind="formula", nf=NUM)
    sh.put("A69", "Facilities block", bold=True)
    sh.put("A70", "Revolver 2,500 (May-2025); drawn / undrawn: HOLE"); sh.put("C70", "L-014 · confirmed · T2", kind="note"); sh.put("D70", f"={R('A11')}", kind="formula", nf=NUM); sh.put("E70", "HOLE (drawn amount undisclosed)", kind="hole")
    sh.put("A71", "Expansion to 15,000: shown only when SW_15B_FACILITY = Closes (default: Does not close, L-160)"); sh.put("C71", "=SW_15B_FACILITY", kind="formula"); sh.put("D71", f'=IF(SW_15B_FACILITY="Closes",{R("A11_exp")},{R("A21a")})', kind="formula", nf=NUM, key="FAC_15B")
    sh.put("E71", f"={R('A22')}", kind="hole"); sh.put("A72", "Facilities in view"); sh.put("D72", "=D70+D71", kind="formula", nf=NUM, key="FAC_TOTAL")
    sh.ws.freeze_panes = "A5"


# ----------------------------------------------------------------------------------------------------
# 11_AIBQ
# ----------------------------------------------------------------------------------------------------
def build_11(sh):
    sh.put("A1", "11_AIBQ: CE-1..CE-4 and CI-1..CI-5, old (May-27, L-133) -> new (Sep-9 re-run, aibq-delta.md sections 1-4) with rubric bands, weights, dimension and composite deltas, flags (E14 A5:L40). Ruling 2: no statistical coefficient between AIBQ and valuation is computed, referenced or named anywhere in this workbook.", kind="note")
    sh.put("A2", "Composite deltas use Report weights (CE 0.20, CI 0.15; RQ, GO, MD held at their May-27 values); new composite = canonical old (8.20 / 4.53) + delta. Flags at >= 0.5 sub-score or >= 0.1 composite.", kind="note")
    sh.header(4, ["Sub-score", "Weight", "Old (May-27)", "New (Sep-9)", "Rubric band / basis", "Rows", "Type", "Delta raw", "Delta dim (weight x delta)", "Flag (>= 0.5)", "Branch note", "Live switch"])

    def block(r0, title, items, dim_key_old, dim_key_new, dim_label, extra=None):
        sh.put(f"A{r0}", title, bold=True, fill=SUB)
        n = len(items)
        for i, (lab, wk, ok, nk, band, rows, typ, note, sw) in enumerate(items):
            rr = r0 + 1 + i
            sh.put(f"A{rr}", lab); sh.put(f"B{rr}", f"={R(wk)}", kind="formula", nf=PCT)
            sh.put(f"C{rr}", f"={R(ok)}", kind="formula", nf=DEC2)
            sh.put(f"D{rr}", nk, kind=("formula"), nf=DEC2, bold=True)
            sh.put(f"E{rr}", band, kind="note", wrap=False); sh.put(f"F{rr}", rows, kind="note"); sh.put(f"G{rr}", typ, kind="note")
            sh.put(f"H{rr}", f"=D{rr}-C{rr}", kind="formula", nf=DEC2); sh.put(f"I{rr}", f"=B{rr}*H{rr}", kind="formula", nf=DEC3)
            sh.put(f"J{rr}", f'=IF(ABS(H{rr})>={R("Q_flag")},"FLAG","")', kind="formula", bold=True)
            sh.put(f"K{rr}", note, kind="note")
            if sw:
                sh.put(f"L{rr}", sw, kind="formula")
        rd = r0 + 1 + n
        sh.put(f"A{rd}", dim_label, bold=True)
        sh.put(f"C{rd}", f"=SUMPRODUCT(B{r0+1}:B{r0+n},C{r0+1}:C{r0+n})", kind="formula", nf=DEC3, bold=True, key=dim_key_old)
        sh.put(f"D{rd}", f"=SUMPRODUCT(B{r0+1}:B{r0+n},D{r0+1}:D{r0+n})", kind="formula", nf=DEC3, bold=True, key=dim_key_new)
        sh.put(f"H{rd}", f"=D{rd}-C{rd}", kind="formula", nf=DEC3, bold=True, key=dim_key_new + "_D")
        sh.put(f"B{rd}", f"=SUM(B{r0+1}:B{r0+n})", kind="formula", nf=PCT)
        return rd

    ceA = [
        ("CE-1 Primary efficiency (Efficiency Index; pre-FCF fallback: ARR / equity raised)", "Q_wCE1", "Q_A_CE1_old", f"={R('Q_A_CE1_new')}",
         "Index 0.55 -> band '>0.50' = 7-8; 9-10 requires '+FCF+', which Ruling 3 keeps unswept; ratio cross-check 0.315x (7-8 band); only the forbidden gross 0.523x reaches 9-10", "L-032, L-007, L-126, L-034", "Method-driven: the prior 10.0 is not reproducible from the rubric without counting a projected non-GAAP adjusted result as TTM FCF+", "Alternative reading (count Q2 adjusted as FCF+): 9.0; weaker because the measure is non-GAAP and excludes SBC (L-152). At 27%: 0.382x, still 7-8", None),
        ("CE-2 Gross margin quality", "Q_wCE2", "Q_A_CE2_old", f"={R('Q_A_CE2_new')}",
         "2025 ~40% (3-4); 2026 T4 range 44-60% straddles; Q2 arithmetic implies 31-48% gross / 51-80% net; L-152 ratio implies ~44% gross if compute is all of COGS; scored at the lower edge of 50-65% net; AI-INFRA +1.0 NOT applied", "L-119 (T4), L-034, L-151, L-152, L-033, L-126", "Data-driven, weak tier", "FLAG (T4 input). Alternative: hold 4.0 pending the S-1", None),
        ("CE-3 Burn trajectory (QoQ): positive adjusted operating income, non-GAAP (L-151, L-152)", "Q_wCE3", "Q_A_CE3_old", f"={R('Q_A_CE3_new')}",
         "Q1 4,730 -> Q2 11,600 (2.45x) with the adjusted result turning positive and the T4 compute ratio falling 0.71 -> 0.56: 'Improving >50%' = 9-10 on direction", "L-034, L-151, L-152", "Confirmed (direction), flagged (measure)", "FLAG (adjusted measure; T3 definition); the GAAP trajectory is unknown", None),
        ("CE-4 Capital structure health (both facility branches printed)", "Q_wCE4", "Q_A_CE4_old", f'=IF(SW_15B_FACILITY="Closes",{R("Q_A_CE4_closes")},{R("Q_A_CE4_dnc")})',
         "Runway >24 months; dilution 17.33%; on-balance-sheet debt 2,500; the 15,000 expansion NOT closed (L-160, house rule); the lease stack (SPV 34,500 / 5 yr, Riot 20-yr, Nscale, Lambda, Volta) is why neither branch returns to 8.0", "L-042, L-160, L-044, L-136, L-135, L-137, L-015", "Data-driven, T3 inputs", f"=\"does not close \"&TEXT({R('Q_A_CE4_dnc')},\"0.0\")&\" (default) / closes \"&TEXT({R('Q_A_CE4_closes')},\"0.0\")", "=SW_15B_FACILITY"),
    ]
    sh.put("A5", "ANTHROPIC CAPITAL EFFICIENCY (CE, weight 20%)", bold=True, fill=SUB)
    rd = block(5, "ANTHROPIC CAPITAL EFFICIENCY (CE, weight 20%)", ceA, "CE_A_OLD", "CE_A_NEW", "CE dimension = SUMPRODUCT(weights, scores)")
    sh.put(f"K{rd}", f"=\"CE closes-branch = \"&TEXT({R('CE_A_CLOSES')},\"0.000\")&\"; does-not-close = \"&TEXT({R('CE_A_DNC')},\"0.000\")" if False else "", kind="note")
    # explicit both-branch CE dimension cells
    sh.put(f"E{rd}", "Both branches:", kind="note")
    sh.put(f"F{rd}", f"={R('Q_wCE1')}*{R('Q_A_CE1_new')}+{R('Q_wCE2')}*{R('Q_A_CE2_new')}+{R('Q_wCE3')}*{R('Q_A_CE3_new')}+{R('Q_wCE4')}*{R('Q_A_CE4_dnc')}", kind="formula", nf=DEC3, key="CE_A_DNC")
    sh.put(f"G{rd}", f"={R('Q_wCE1')}*{R('Q_A_CE1_new')}+{R('Q_wCE2')}*{R('Q_A_CE2_new')}+{R('Q_wCE3')}*{R('Q_A_CE3_new')}+{R('Q_wCE4')}*{R('Q_A_CE4_closes')}", kind="formula", nf=DEC3, key="CE_A_CLOSES")
    ck(sh, f"I{rd}", f"F{rd}", "CE_A"); ck(sh, f"J{rd}", f"G{rd}", "CE_A_CL"); sh.put(f"K{rd}", "F = does not close (7.375, default); G = closes (7.30)", kind="note")
    sh.put(f"L{rd}", f"=H{rd}*{R('Q_wCEdim')}", kind="formula", nf=DEC3, key="CE_A_COMPD"); sh.put(f"M{rd}", "composite impact (x 0.20)", kind="note")
    ciA = [
        ("CI-1 Provider diversification", "Q_wCI1", "Q_A_CI1_old", f"={R('Q_A_CI1_new')}", "Nine providers under contract (AWS, Google Cloud, Azure, SpaceX, Nscale, Lambda, Volta, Riot, Fluidstack): 'Four+, well-balanced' = 7-8; balance unverified, so 7.0", "L-072, L-073, L-074, L-046, L-135, L-136, L-137, L-048, L-076", "Data-driven, T1/T2", "FLAG (balance unverified)", None),
        ("CI-2 Infrastructure ownership", "Q_wCI2", "Q_A_CI2_old", f"={R('Q_A_CI2_new')}", "Fluidstack DC build (T1) + Riot powered shell + TPU systems leased from an SPV: between 3-4 and 5-6; no custom ASIC of its own", "L-076, L-136, L-044, L-132", "Data-driven, T1/T3", "FLAG (ownership structure of the Fluidstack sites undisclosed)", None),
        ("CI-3 Energy independence", "Q_wCI3", "Q_A_CI3_old", f"={R('Q_A_CI3_new')}", "No PPA attributable to Anthropic; power procured by partners: 'Energy awareness but no direct contracts' = 3-4; the prior 5.0 has no supporting row", "L-131 (could-not-verify, T3)", "Method / absence-driven", "FLAG (absence of evidence at T3)", None),
        ("CI-4 Supply-chain resilience", "Q_wCI4", "Q_A_CI4_old", f"={R('Q_A_CI4_new')}", "Four active chip families (Nvidia, Google TPU, Trainium, AMD MI450 from 2027): top of 5-6; not 7-8 because none is Anthropic's own and all are TSMC-fabbed", "L-043, L-049, L-072, L-135", "Data-driven, T1/T2", "FLAG (rubric interpretation)", None),
        ("CI-5 Contractual lock-in", "Q_wCI5", "Q_A_CI5_old", f"={R('Q_A_CI5_new')}", "Non-exclusive throughout; SpaceX 90-day (toward 7-8) offset by a 10-yr AWS minimum and a 20-yr Riot lease (toward 3-4): net unchanged", "L-046, L-072, L-136", "Confirmed", "none", None),
    ]
    rd2 = block(rd + 2, "ANTHROPIC COMPUTE INDEPENDENCE (CI, weight 15%)", ciA, "CI_A_OLD", "CI_A_NEW", "CI dimension (sub-score base 5.05; canonical 5.8 in K)")
    sh.put(f"K{rd2}", f"=\"canonical CI after the un-decomposed SpaceX revision = \"&TEXT({R('Q_A_CI_canon')},\"0.00\")&\"; delta vs canonical = \"&TEXT(D{rd2}-{R('Q_A_CI_canon')},\"0.000\")", kind="formula")
    sh.put(f"L{rd2}", f"=H{rd2}*{R('Q_wCIdim')}", kind="formula", nf=DEC3, key="CI_A_COMPD"); sh.put(f"M{rd2}", "composite impact (x 0.15) vs the sub-score base", kind="note")
    sh.put(f"F{rd2}", f"=D{rd2}-{R('Q_A_CI_canon')}", kind="formula", nf=DEC3, key="CI_A_D_CANON"); sh.put(f"E{rd2}", "delta vs canonical 5.8:", kind="note")
    ck(sh, f"I{rd2}", f"D{rd2}", "CI_A")
    ceO = [
        ("CE-1 Primary efficiency (ratio 0.221x -> 5-6 band; C-16 gross case 0.177x -> 3-4 band = 4.0)", "Q_wCE1", "Q_O_CE1_old", f'=IF(SW_OAI_BASIS="NET",{R("Q_O_CE1_net")},{R("Q_O_CE1_gross")})', "40,000 / 181,216.5 = 0.221x -> 5-6 (0.2-0.3x); prior 3.0 matched 25,000 / 181,216.5 = 0.138x; Index cross-check 0.50 (borderline 5-6 / 7-8)", "L-065, L-022", "Data-driven, T2", f"=\"NET 5.0 / GROSS 4.0; live = \"&SW_OAI_BASIS", "=SW_OAI_BASIS"),
        ("CE-2 Gross margin quality", "Q_wCE2", "Q_O_CE2_old", f"={R('Q_O_CE2_new')}", "33% (2025) = 3-4 band; 2026E inference 14,100 on 32,400-45,500 implies an improving GM but no GM datapoint exists", "L-083 (T3), L-066", "Unchanged", "none", None),
        ("CE-3 Burn trajectory", "Q_wCE3", "Q_O_CE3_old", f"={R('Q_O_CE3_new')}", "Operating loss worsened 32% QoQ (9,300 -> 12,300): 'Worsening 10-50%' = 3-4; confirmed at T2", "L-066", "Confirmed", "none", None),
        ("CE-4 Capital structure health", "Q_wCE4", "Q_O_CE4_old", f"={R('Q_O_CE4_new')}", "By the letter 7-8 (debt 5,220; runway >24 months; dilution 14.23%); the prior treated the obligation stack as debt-like (480,400 documented-$ = 12x run-rate; 20-yr leases as a non-investment-grade tenant): hold, credit the round: 3.0", "L-020, L-023, L-082, L-061", "Data-driven, interpretive", "FLAG (interpretation: commitments treated as debt-like)", None),
    ]
    rd3 = block(rd2 + 2, "OPENAI CAPITAL EFFICIENCY (CE, weight 20%)", ceO, "CE_O_OLD", "CE_O_NEW", "CE dimension")
    sh.put(f"L{rd3}", f"=H{rd3}*{R('Q_wCEdim')}", kind="formula", nf=DEC3, key="CE_O_COMPD"); ck(sh, f"I{rd3}", f"D{rd3}", "CE_O_AIBQ")
    sh.put(f"F{rd3}", f"={R('Q_wCE1')}*{R('Q_O_CE1_gross')}+{R('Q_wCE2')}*{R('Q_O_CE2_new')}+{R('Q_wCE3')}*{R('Q_O_CE3_new')}+{R('Q_wCE4')}*{R('Q_O_CE4_new')}", kind="formula", nf=DEC3, key="CE_O_GROSSCASE"); sh.put(f"E{rd3}", "gross case (CE-1 = 4.0):", kind="note")
    ciO = [
        ("CI-1 Provider diversification", "Q_wCI1", "Q_O_CI1_old", f"={R('Q_O_CI1_new')}", "Azure, Oracle, AWS, CoreWeave, Cerebras, SB Energy sites, any-cloud: five-plus; Microsoft ~48% of the 2026 compute plan (24,100 / 50,000), so 'no one >50%' just holds: 5-6, top", "L-051, L-054, L-078, L-058, L-064, L-149", "Data-driven, T1/T2", "none", None),
        ("CI-2 Infrastructure ownership", "Q_wCI2", "Q_O_CI2_old", f"={R('Q_O_CI2_new')}", "20-yr leases on 8.0 GW-IT + 15-yr on 753 MW as tenant (T1), self-build plans, custom ASIC with a dated 2027 deployment (T1), dedicated Cerebras capacity (T1): above 3-4, not 7-8 (SB Energy and Oracle own the sites; Nvidia guarantees residual value)", "L-061, L-050, L-149, L-132", "Data-driven, T1", "FLAG: three events (Cerebras May-11; SB Energy Aug-17; Broadcom Sep-2) or a re-baseline", None),
        ("CI-3 Energy independence", "Q_wCI3", "Q_O_CI3_old", f"={R('Q_O_CI3_new')}", "No OpenAI PPA in the ledger; power sits with Oracle campuses and SB Energy (terms undisclosed): 3-4; upside if the SB Energy leases bundle power", "L-079, L-061", "Unchanged", "none", None),
        ("CI-4 Supply-chain resilience", "Q_wCI4", "Q_O_CI4_old", f"={R('Q_O_CI4_new')}", "Nvidia + AMD 6 GW (T1) + Broadcom custom XPU on a dated schedule (T1) + Cerebras wafer-scale (T1): 'Multiple + custom reducing dependency' = 7-8, low end", "L-050, L-060, L-149", "Data-driven, T1", "FLAG", None),
        ("CI-5 Contractual lock-in", "Q_wCI5", "Q_O_CI5_old", f"={R('Q_O_CI5_new')}", "Exclusivity gone (T1) pulls up; minimums (Oracle 300,000; AWS ~138,000; 20-yr leases) with exit costs far above 1,000 pull down: net +0.5", "L-051, L-064, L-061", "Data-driven, offsetting", "none", None),
    ]
    rd4 = block(rd3 + 2, "OPENAI COMPUTE INDEPENDENCE (CI, weight 15%)", ciO, "CI_O_OLD", "CI_O_NEW", "CI dimension")
    sh.put(f"L{rd4}", f"=H{rd4}*{R('Q_wCIdim')}", kind="formula", nf=DEC3, key="CI_O_COMPD"); ck(sh, f"I{rd4}", f"D{rd4}", "CI_O")

    rc = rd4 + 2
    sh.put(f"A{rc}", "COMPOSITE IMPACT (Report weights; RQ, GO, MD held; deltas applied to the canonical old composites 8.20 / 4.53, L-133)", bold=True, fill=SUB)
    sh.header(rc + 1, ["Company / branch", "CE delta dim", "CE composite delta (x 0.20)", "CI delta dim", "CI composite delta (x 0.15)", "Total composite delta", "Old composite", "New composite", "Quality tier", "Check", "$B per point (06_Valuation)", "Note"])
    comp = [
        (rc + 2, "Anthropic (sub-score CI base 5.05; SW_15B_FACILITY = Does not close, default)", f"={R('CE_A_DNC')}-{R('CE_A_OLD')}", f"={R('CI_A_NEW_D')}", f"={R('AIBQ_OLD_A')}", "COMP_A_NEW", "COMP_A", "Strong (unchanged)"),
        (rc + 3, "Anthropic (same, facility closes)", f"={R('CE_A_CLOSES')}-{R('CE_A_OLD')}", f"={R('CI_A_NEW_D')}", f"={R('AIBQ_OLD_A')}", "COMP_A_CLOSES", "COMP_A_CL", "Strong"),
        (rc + 4, "Anthropic (canonical CI base 5.8; default facility branch)", f"={R('CE_A_DNC')}-{R('CE_A_OLD')}", f"={R('CI_A_D_CANON')}", f"={R('AIBQ_OLD_A')}", "COMP_A_CANON", "COMP_A_CANON", "Strong"),
        (rc + 5, "Anthropic (LIVE: CE-4 follows SW_15B_FACILITY)", f"={R('CE_A_NEW_D')}", f"={R('CI_A_NEW_D')}", f"={R('AIBQ_OLD_A')}", "COMP_A_LIVE", None, "Strong"),
        (rc + 6, "OpenAI (net case)", f"={R('CE_O_NEW')}-{R('CE_O_OLD')}", f"={R('CI_O_NEW_D')}", f"={R('AIBQ_OLD_O')}", "COMP_O_NEW", "COMP_O", "Developing (unchanged; <5.0)"),
        (rc + 7, "OpenAI (C-16 gross case, CE-1 = 4.0)", f"={R('CE_O_GROSSCASE')}-{R('CE_O_OLD')}", f"={R('CI_O_NEW_D')}", f"={R('AIBQ_OLD_O')}", "COMP_O_GROSS", "COMP_O_G", "Developing"),
        (rc + 8, "OpenAI (LIVE: CE-1 follows SW_OAI_BASIS)", f"={R('CE_O_NEW_D')}", f"={R('CI_O_NEW_D')}", f"={R('AIBQ_OLD_O')}", "COMP_O_LIVE", None, "Developing"),
    ]
    for rr, lab, ced, cid, old, key, chk, tier in comp:
        sh.put(f"A{rr}", lab); sh.put(f"B{rr}", ced, kind="formula", nf=DEC3); sh.put(f"C{rr}", f"=B{rr}*{R('Q_wCEdim')}", kind="formula", nf=DEC3)
        sh.put(f"D{rr}", cid, kind="formula", nf=DEC3); sh.put(f"E{rr}", f"=D{rr}*{R('Q_wCIdim')}", kind="formula", nf=DEC3)
        sh.put(f"F{rr}", f"=C{rr}+E{rr}", kind="formula", nf=DEC3, bold=True); sh.put(f"G{rr}", old, kind="formula", nf=DEC2)
        sh.put(f"H{rr}", f"=G{rr}+F{rr}", kind="formula", nf=DEC3, bold=True, key=key); sh.put(f"I{rr}", tier, kind="note")
        if chk:
            ck(sh, f"J{rr}", f"H{rr}", chk)
    sh.put(f"A{rc+9}", "Efficiency Index (rubric S5): min(growth/100, 1.0) x 0.4 + min(FCF/Rev, 0.30) x 0.3 + GM x 0.3", bold=True)
    sh.put(f"B{rc+9}", "Anthropic", kind="note"); sh.put(f"C{rc+9}", f"={R('EI_w1')}*{R('EI_growth')}+{R('EI_w2')}*{R('EI_fcf')}+{R('EI_w3')}*{R('EI_gm_A')}", kind="formula", nf=DEC3, key="EI_A"); ck(sh, f"D{rc+9}", f"C{rc+9}", "EI_A")
    sh.put(f"E{rc+9}", "OpenAI", kind="note"); sh.put(f"F{rc+9}", f"={R('EI_w1')}*{R('EI_growth')}+{R('EI_w2')}*{R('EI_fcf')}+{R('EI_w3')}*{R('EI_gm_O')}", kind="formula", nf=DEC3, key="EI_O"); ck(sh, f"G{rc+9}", f"F{rc+9}", "EI_O")
    sh.put(f"A{rc+10}", "CE-1 ratio cross-checks: Anthropic net run-rate / equity (live haircut) and at 27%; OpenAI net / equity; the raw gross ratio is displayed on 05_Cash_Fund as a forbidden basis")
    sh.put(f"C{rc+10}", f"={R('CE_A_LIVE')}", kind="formula", nf=MULT3); sh.put(f"D{rc+10}", f"={R('CE_A_27')}", kind="formula", nf=MULT3); sh.put(f"F{rc+10}", f"={R('CE_O_LIVE')}", kind="formula", nf=MULT3); sh.put(f"G{rc+10}", "=SW_HAIRCUT", kind="formula", nf=PCT2)
    sh.put(f"A{rc+11}", "Flags summary: Anthropic CE-1 (-2.0, method), CE-2 (+1.0, T4), CE-3 (0, adjusted measure), CE-4 (-0.5 default / -1.0, T3), CI-1 (+1.0), CI-2 (+1.0), CI-3 (-1.0, absence), CI-4 (+1.0), CE composite (-0.125 default / -0.14); OpenAI CE-1 (+2.0), CE-4 (+0.5, interpretive), CI-2 (+3.0), CI-4 (+1.0), CE composite (+0.175), CI composite (+0.165), total (+0.34: book as a re-baseline).", kind="note")
    sh.put(f"A{rc+12}", "Reading: the fall in Anthropic's CE is a method correction (-0.80 from re-applying the rubric to CE-1); the data-driven moves net to +0.175 at the default. Say 'adjusted' every time the Q2 result is named.", kind="note")
    sh.ws.freeze_panes = "B5"


# ----------------------------------------------------------------------------------------------------
# 06_Valuation
# ----------------------------------------------------------------------------------------------------
def build_06(sh):
    sh.put("A1", "06_Valuation: marks ladder and multiples at gross / 39.75% / 27% (Anthropic) and net / gross-case (OpenAI) (E5 A5:H20); the $/AIBQ-point ladder (E15 A25:F32). Ruling 2: the AIBQ-to-valuation coefficient is embargoed; no cell computes any such statistic.", kind="note")
    sh.section(3, "MARKS AND MULTIPLES (Exhibit E5; A5:H20); every net figure shows its haircut in column E", ncols=11)
    sh.header(4, ["Item", "Unit", "Source", "Value", "Haircut / basis visible", "Check", "Note"])
    rows = [
        (5, "Anthropic post-money mark (M01, Series H)", "$M", "L-005, L-038 · confirmed · T2/T1 · 2026-05-28", f"={R('M01')}", "n/a", NUM, None, None),
        (6, "OpenAI post-money mark (M02, Mar-2026; Aug-10 tender at the same price)", "$M", "L-019, L-067 · confirmed · T2 · 2026-03-31", f"={R('M02')}", "n/a", NUM, None, None),
        (7, "Anthropic mark / run-rate GROSS (display only; not comparable, Ruling 5)", "x", "derived", "=D5/LB01", "GROSS", MULT, "MULT_A_G", "MULT_G"),
        (8, "Anthropic mark / net run-rate at SW_HAIRCUT (equalized)", "x", "derived", f"=D5/{R('NET_A_LIVE')}", "=SW_HAIRCUT", MULT, "MULT_A_LIVE", None),
        (9, "Anthropic mark / net run-rate at 39.75% (Ruling 5)", "x", "derived", f"=D5/{R('NET_A_3975')}", f"={R('R01')}", MULT, "MULT_A_3975", "MULT_3975"),
        (10, "Anthropic mark / net run-rate at 27% (C-13 external)", "x", "derived", f"=D5/{R('NET_A_27')}", f"={R('R02')}", MULT, "MULT_A_27", "MULT_27"),
        (11, "OpenAI mark / net run-rate at SW_OAI_BASIS", "x", "derived", f"=D6/{R('NET_O_LIVE')}", "=SW_OAI_BASIS", MULT, "MULT_O_LIVE", None),
        (12, "OpenAI mark / run-rate, NET case (as reported)", "x", "derived", f"=D6/{R('NET_O_NETCASE')}", "NET", MULT, "MULT_O_NET", "MULT_O"),
        (13, "OpenAI mark / run-rate, GROSS case (LB02 x (1 - R03), T4 flagged)", "x", "derived", f"=D6/{R('NET_O_GROSSCASE')}", f"={R('R03')}", MULT, "MULT_O_GROSS", "MULT_OG"),
        (14, "Relative multiple: Anthropic (SW_HAIRCUT) / OpenAI (SW_OAI_BASIS) - 1", "fraction", "derived", "=D8/D11-1", "=SW_HAIRCUT", PCT, "RELMULT_LIVE", None),
        (15, "Relative multiple at 27% vs OpenAI NET", "fraction", "derived", "=D10/D12-1", f"={R('R02')}", PCT, "RELMULT_27", "REL_27"),
        (16, "Jul-16 reference: Anthropic mark / net run-rate at May 47,000 (34.1x)", "x", "L-133 · recalled · T4; L-037", f"=D5/{R('NET_A_J16')}", f"={R('R01')}", MULT, "MULT_A_J16", "J16_MULT"),
        (17, "Jul-16 reference: OpenAI mark / 25,000 (34.1x)", "x", "L-133 · recalled · T4", f"=D6/{R('J16_OAI_RR')}", "NET (register)", MULT, "MULT_O_J16", "J16_MULT"),
        (18, "Relative multiple at 39.75% vs OpenAI NET (+15%)", "fraction", "derived", "=D9/D12-1", f"={R('R01')}", PCT, "RELMULT_3975", "REL_3975"),
    ]
    for rr, lab, unit, src, f, hc, nf, key, chk in rows:
        sh.put(f"A{rr}", lab); sh.put(f"B{rr}", unit, kind="note"); sh.put(f"C{rr}", src, kind="note"); sh.put(f"D{rr}", f, kind="formula", nf=nf, bold=True, key=key)
        if hc.startswith("="):
            sh.put(f"E{rr}", hc, kind="formula", nf=(GEN if "BASIS" in hc else PCT2))
        else:
            sh.put(f"E{rr}", hc, kind="note")
        if chk:
            ck(sh, f"F{rr}", f"D{rr}", chk)
    sh.put("E13", f"={R('R03')}", kind="hole", nf=PCT); sh.put("G13", "R03 is T4 and never printed as a fact", kind="flag")
    sh.put("A19", "C-15 (display only; no formula reads this): secondary marks 1,500,000 implied at $925/share and 'low-to-mid 800,000' (both T4); none adopted; the primary mark is M01.", kind="note")
    sh.put("A20", "Ruling 2: the AIBQ-to-valuation coefficient is embargoed. Ruling 5: never gross vs net; the gross multiple (row 7) is display only.", kind="note")
    sh.section(23, "$/AIBQ-POINT LADDER (Exhibit E15; A25:F32): mark / composite; the only permitted valuation-quality expression (Ruling 2)", ncols=11)
    sh.header(24, ["Row", "Anthropic composite", "Anthropic $B per point", "OpenAI composite", "OpenAI $B per point", "Spread (OpenAI / Anthropic)", "Check", "Note"])
    lad = [
        (25, "Old (May-27 canonical, L-133)", f"={R('AIBQ_OLD_A')}", f"={R('AIBQ_OLD_O')}", "PPT_A_OLD", "PPT_O_OLD", "SPREAD_OLD", ("PPT_O_OLD", "SPREAD_OLD")),
        (26, "New (default: facility does not close; OpenAI net case)", f"={R('COMP_A_NEW')}", f"={R('COMP_O_NEW')}", "PPT_A_NEW", "PPT_O_NEW", "SPREAD_NEW", ("PPT_A", "PPT_O", "SPREAD")),
        (27, "New (facility-closes branch)", f"={R('COMP_A_CLOSES')}", f"={R('COMP_O_NEW')}", "PPT_A_CL", None, "SPREAD_CL", ("PPT_A_CL", "SPREAD_CL")),
        (28, "New (canonical CI 5.8 base)", f"={R('COMP_A_CANON')}", f"={R('COMP_O_NEW')}", "PPT_A_CANON", None, "SPREAD_CANON", None),
        (29, "New (OpenAI C-16 gross case, CE-1 = 4.0)", f"={R('COMP_A_NEW')}", f"={R('COMP_O_GROSS')}", None, "PPT_O_GROSS", "SPREAD_OGROSS", None),
        (30, "LIVE (both switches)", f"={R('COMP_A_LIVE')}", f"={R('COMP_O_LIVE')}", "PPT_A_LIVE", "PPT_O_LIVE", "SPREAD_LIVE", None),
    ]
    for rr, lab, ca, co, kA, kO, kS, chk in lad:
        sh.put(f"A{rr}", lab); sh.put(f"B{rr}", ca, kind="formula", nf=DEC3); sh.put(f"C{rr}", f"=$D$5/B{rr}/{R('MPERB')}", kind="formula", nf=CNT1, bold=True, key=kA)
        sh.put(f"D{rr}", co, kind="formula", nf=DEC3); sh.put(f"E{rr}", f"=$D$6/D{rr}/{R('MPERB')}", kind="formula", nf=CNT1, bold=True, key=kO)
        sh.put(f"F{rr}", f"=E{rr}/C{rr}", kind="formula", nf=MULT2, bold=True, key=kS)
    ck(sh, "G25", "F25", "SPREAD_OLD"); sh.put("H25", "=E25-C25", kind="formula", nf=CNT1); sh.put("I25", "$B more per point for OpenAI (old: ~70)", kind="note")
    ck(sh, "G26", "F26", "SPREAD"); sh.put("H26", "=E26-C26", kind="formula", nf=CNT1, key="MORE_PPT"); sh.put("I26", "$B more per point for OpenAI (new: ~57)", kind="note")
    ck(sh, "G27", "F27", "SPREAD_CL"); ck(sh, "H27", "C27", "PPT_A_CL")
    ck(sh, "G31", "C26", "PPT_A"); ck(sh, "H31", "E26", "PPT_O"); ck(sh, "I31", "E25", "PPT_O_OLD"); ck(sh, "J31", "H26", "MORE_PPT")
    sh.put("A31", "Checks: $/pt 118 / 175 (default), 119 on the closes branch, spread 1.48x (1.47x), old 188 and 1.60x, $57B more per point", kind="note")
    sh.put("A32", "The ladder narrows because OpenAI's CE and CI improved on ledger evidence while its mark stood still (Aug-10 tender at 852,000, L-067). No coefficient is computed or referenced (Ruling 2).", kind="note")
    sh.ws.freeze_panes = "A5"


# ----------------------------------------------------------------------------------------------------
# 07_Sensitivity
# ----------------------------------------------------------------------------------------------------
def build_07(sh):
    sh.put("A1", "07_Sensitivity: (a) basis grid A5:H20; (b) Anthropic 2028E envelope grid A25:H40 (three panels); (c) OpenAI 2030 cash-flow sign A45:H60 (Exhibit E17). Grids are wired to the switches and drivers; no typed constants.", kind="note")
    sh.section(4, "(a) BASIS GRID: haircut 27% / 33% / 39.75% x OpenAI basis NET / GROSS (R03 = 20%, T4): Anthropic equalized multiple, OpenAI multiple, relative multiple, CE ratio", ncols=11)
    sh.header(5, ["Haircut", "OpenAI basis", "Anthropic net run-rate", "Anthropic multiple", "OpenAI net run-rate", "OpenAI multiple", "Relative multiple (A / O - 1)", "CE ratio (A / O)", "Check"])
    hcs = [("R02", "27%"), ("HCUTMID", "33% (grid only)"), ("R01", "39.75%")]
    rr = 6
    for basis, oai in (("NET", "=LB02"), ("GROSS", f"=LB02*(1-{R('R03')})")):
        for k, lab in hcs:
            sh.put(f"A{rr}", f"={R(k)}", kind="formula", nf=PCT2); sh.put(f"B{rr}", basis, kind=("flag" if basis == "GROSS" else "label"))
            sh.put(f"C{rr}", f"=LB01*(1-A{rr})", kind="formula", nf=NUM); sh.put(f"D{rr}", f"={R('M01')}/C{rr}", kind="formula", nf=MULT, bold=True)
            sh.put(f"E{rr}", oai, kind="formula", nf=NUM); sh.put(f"F{rr}", f"={R('M02')}/E{rr}", kind="formula", nf=MULT, bold=True)
            sh.put(f"G{rr}", f"=D{rr}/F{rr}-1", kind="formula", nf=PCT, bold=True, key=f"GA_REL_{basis}_{k}"); sh.put(f"H{rr}", f"=(C{rr}/LB03)/(E{rr}/LB04)", kind="formula", nf=MULT2, bold=True, key=f"GA_CE_{basis}_{k}")
            rr += 1
        rr += 1
    # rows: NET 6,7,8 ; GROSS 10,11,12
    sh.put("A14", "Expected corners: (39.75%, NET) 24.6x vs 21.3x, +15%, 1.43x; (27%, NET) 20.3x vs 21.3x, -5%, 1.73x; (39.75%, GROSS) 24.6x vs 26.6x, -7%, 1.78x", kind="note")
    ck(sh, "I8", "G8", "REL_3975"); ck(sh, "I6", "G6", "REL_27"); ck(sh, "I12", "G12", "REL_G")
    ck(sh, "J8", "H8", "RATIO"); ck(sh, "J6", "H6", "RATIO27"); ck(sh, "J12", "H12", "RATIO_G_CE")
    sh.put("A15", "GROSS rows apply R03 (T4, L-052 notes) and are flagged; the 20% is never printed as a fact. The 33% row exists for the grid only (spec section 5).", kind="note")
    sh.put("A16", "Live switches: SW_HAIRCUT ="); sh.put("C16", "=SW_HAIRCUT", kind="formula", nf=PCT2); sh.put("D16", "SW_OAI_BASIS =", kind="note"); sh.put("E16", "=SW_OAI_BASIS", kind="formula")

    sh.section(24, "(b) ANTHROPIC 2028E ENVELOPE GRID: cell = revenue x (1 - GM) + training - priced run 53,355 - Google leg; negative = the plan does not cover the commitments (before AMD)", ncols=11)
    run28 = RY("RUN_A", 2028); gmk = ["GMA_BEAR|2028", "GMA_BASE|2028", "GMA_BULL|2028"]; revk = ["GRIDREV1", "GRIDREV2", "GRIDREV3"]

    def panel(r0, title, trn_ref, leg_ref, keyp):
        sh.put(f"A{r0}", title, bold=True, fill=SUB)
        sh.put(f"A{r0+1}", "2028E revenue \\ GM", kind="header")
        for j, gk in enumerate(gmk):
            sh.put(f"{'BCD'[j]}{r0+1}", f"={R(gk)}", kind="formula", nf=PCT, bold=True)
        sh.put(f"E{r0+1}", "Training", kind="header"); sh.put(f"F{r0+1}", "Priced run 2028", kind="header"); sh.put(f"G{r0+1}", "Google leg 2028", kind="header")
        for i, rk in enumerate(revk):
            rr = r0 + 2 + i
            sh.put(f"A{rr}", f"={R(rk)}", kind="formula", nf=NUM, bold=True)
            for j in range(3):
                col = "BCD"[j]
                sh.put(f"{col}{rr}", f"=$A{rr}*(1-{col}${r0+1})+$E${r0+2}-$F${r0+2}-$G${r0+2}", kind="formula", nf=NUM, key=f"{keyp}_{i}{j}")
        sh.put(f"E{r0+2}", trn_ref, kind="formula", nf=NUM); sh.put(f"F{r0+2}", f"={run28}", kind="formula", nf=NUM); sh.put(f"G{r0+2}", leg_ref, kind="formula", nf=NUM)
    panel(25, "Panel 1: training 22,000 (L-125), Google leg = live switch (SW_GOOGLE_VALUE)", f"={R('GRIDTRN1')}", f"={RY('GOOG_LEG', 2028)}", "GB1")
    panel(30, "Panel 2: training 30,000 (Base 2029 AJ), Google leg = live switch", f"={R('GRIDTRN2')}", f"={RY('GOOG_LEG', 2028)}", "GB2")
    panel(35, "Panel 3: training 22,000, Google leg = PROXY (SW_TPU_RATE x SW_GW_2028 x 1,000) regardless of SW_GOOGLE_VALUE", f"={R('GRIDTRN1')}", f"={RY('GOOG_PROXY', 2028)}", "GB3")
    sh.put("A40", "Expected at (200,000, 77%, reported): 46,000 + 22,000 - 53,355 - 40,000 = -25,355 (computed here with the reported leg irrespective of the switch):", kind="note")
    sh.put("G40", f"={R('GRIDREV3')}*(1-{R('GMA_BULL|2028')})+{R('GRIDTRN1')}-{run28}-{RY('GOOG_REP', 2028)}", kind="formula", nf=NUM, bold=True, key="GRIDB_CHK"); ck(sh, "H40", "G40", "GRIDB")
    sh.put("A41", "Live switches: SW_GOOGLE_VALUE / SW_TPU_RATE / SW_GW_2028 ="); sh.put("C41", "=SW_GOOGLE_VALUE", kind="formula"); sh.put("D41", "=SW_TPU_RATE", kind="formula", nf=CNT1); sh.put("E41", "=SW_GW_2028", kind="formula", nf=CNT)

    sh.section(44, "(c) OPENAI 2030 CASH-FLOW SIGN: rows = 2027-2030 revenue CAGR 40 / 70 / 100%; columns = compute plan 600,000 / 750,000 / 900,000 (2027-2030 spend = plan - 50,000, phased 15 / 22 / 28 / 35%); cell = 2030E revenue - 2030E compute - other opex (OAIOPEX live %)", ncols=11)
    sh.put("A45", "CAGR \\ compute plan", kind="header")
    plans = ["OAIPLAN_BULL", "OAIPLAN_BASE", "OAIPLAN_BEAR"]; cagrs = ["OAICAGR_BEAR", "OAICAGR_BASE", "OAICAGR_BULL"]
    for j, pk in enumerate(plans):
        sh.put(f"{'BCD'[j]}45", f"={R(pk)}", kind="formula", nf=NUM, bold=True)
    sh.put("E45", "2030E revenue", kind="header"); sh.put("F45", "Years 2027-2030", kind="header"); sh.put("G45", "Other opex %", kind="header"); sh.put("H45", "2030 phasing", kind="header")
    nyrs = f"({R('YR|2030')}-{R('YR|2026')})"
    for i, ckk in enumerate(cagrs):
        rr = 46 + i
        sh.put(f"A{rr}", f"={R(ckk)}", kind="formula", nf=PCT, bold=True)
        sh.put(f"E{rr}", f"={R('FY26O')}*(1+A{rr})^$F$46", kind="formula", nf=NUM)
        for j in range(3):
            col = "BCD"[j]
            sh.put(f"{col}{rr}", f"=$E{rr}-({col}$45-LB07a)*$H$46-$G$46*$E{rr}", kind="formula", nf=NUM, key=f"GC_{i}{j}")
    sh.put("F46", f"={nyrs}", kind="formula", nf=GEN); sh.put("G46", f"={R('OAIOPEX')}", kind="formula", nf=PCT); sh.put("H46", f"={RY('PH', 2030)}", kind="formula", nf=PCT)
    sh.put("A50", "2030E compute by plan (plan - 50,000) x 35%:");
    for j in range(3):
        sh.put(f"{'BCD'[j]}50", f"=({'BCD'[j]}45-LB07a)*$H$46", kind="formula", nf=NUM)
    sh.put("A51", "Sign at Base (70%, 750,000):"); sh.put("C51", "=C47", kind="formula", nf=NUM, bold=True, key="GC_BASE"); sh.put("D51", '=IF(C47>=0,"positive","negative")', kind="formula", bold=True, key="GC_BASE_SIGN")
    sh.put("A52", "Note: The Information's own 2030 figure is +39,000 (L-082, T3, Feb vintage):"); sh.put("C52", f"={R('O05_cf2030')}", kind="formula", nf=NUM)
    sh.put("A53", "Phasing 2027 / 2028 / 2029 / 2030:");
    for j, y in enumerate((2027, 2028, 2029, 2030)):
        sh.put(f"{'BCDE'[j]}53", f"={RY('PH', y)}", kind="formula", nf=PCT)
    sh.put("A54", "FY2026E OpenAI revenue used as the base (live scenario):"); sh.put("C54", f"={R('FY26O')}", kind="formula", nf=NUM)
    sh.put("A55", "Scenario definitions are stated once on 00_Assumptions (spec section 4); the 2029-2030 Anthropic tails use the Bessemer endurance shape with the arithmetic on 02_Revenue rows 74-76.", kind="note")
    sh.ws.freeze_panes = "A5"


# ----------------------------------------------------------------------------------------------------
# 10_Financing
# ----------------------------------------------------------------------------------------------------
def build_10(sh):
    sh.put("A1", "10_Financing: cost-of-capital ladder (F01-F10), spread arithmetic, backstop register (Exhibit E11; A5:H25; cost-stack section 6).", kind="note")
    sh.section(3, "FINANCING LADDER: who holds the risk", ncols=11)
    sh.header(4, ["F#", "Instrument / structure", "Lab", "Rate or terms", "Risk holder", "Row · tier", "Value ($M)", "Note"])
    lad = [
        ("F01", "TPU lease SPV, tranches A1 / A2 / B (five-year lease)", "Anthropic", f"={R('A12_A1')}&\" / \"&TEXT({R('A12_A2')},\"0.00%\")&\" / \"&TEXT({R('A12_B')},\"0.0%\")", "Apollo-led lenders; Broadcom and Google absorb losses if Anthropic or Fluidstack stops paying", "L-044 · T3; L-106 · T1", f"={R('A12')}", "30,000 Broadcom-supported + 4,500 unsupported"),
        ("F02", "Project-company debt, five TPU site companies (1.43 GW)", "Anthropic", "Google conditional support", "Project lenders; Google", "L-045 · T3", f"={R('A13')}", "off-balance-sheet"),
        ("F03", "Nvidia holds the Lambda datacenter lease", "Anthropic", "undisclosed", "Nvidia (lease), Hut 8 (developer)", "L-137 · T2", f"={R('C06_tot')}", "the Anthropic-Lambda term is undisclosed"),
        ("F04", "Nvidia residual-value guaranties, PORTS", "OpenAI", f"=\"guaranteed value on \"&TEXT({R('LB09_RVG_GW')},\"0.00\")&\" GW-IT; option on the remaining capacity; payable only at RFS\"", "Nvidia", "L-061 · T1", f"={R('LB09_RVG')}", "OpenAI 'not an investment-grade tenant'"),
        ("F05", "Warrants for capacity: AMD (160M sh at $0.01), SB Energy (3.99M sh at $0.01), Cerebras (33.4M Class N)", "OpenAI", "vest on purchase / milestone / market-cap targets", "Vendors dilute their own holders; SB Energy booked a 2,573 warrant FV charge in H1-2026", "L-060, L-061, L-149 · T1; L-147 · T1", f"={R('F_sbe_warrant')}", "value = SB Energy charge"),
        ("F06", "Neocloud unsecured notes (2031-2032 coupons)", "Reference", f"=TEXT({R('F_neo1')},\"0.00%\")&\" / \"&TEXT({R('F_neo2')},\"0.00%\")&\" / \"&TEXT({R('F_neo3')},\"0.000%\")", "Bondholders; CoreWeave accumulated deficit 4,000", "L-059 · T1", "n/a", "unbackstopped benchmark"),
        ("F07", "Powered-shell leases: Core Scientific-AMD; Riot", "Reference", f"=TEXT({R('X01_cs')},\"0.00\")&\" and \"&TEXT({R('X01_riot')},\"0.00\")&\" $M per MW-yr\"", "Landlord", "L-148 · T1; L-136 · T2", f"={R('F_cs_tot')}", "15-yr, 2.5% escalators; 20-yr"),
        ("F08", "Full-stack GPU leases: Nscale; Volta", "Anthropic", f"=TEXT({R('X01_nscale')},\"0.0\")&\" and \"&TEXT({R('X01_volta')},\"0.0\")&\" $M per MW-yr\"", "Neocloud (and its lenders)", "L-134 · T3 derived", f"={R('C05_tot')}+{R('C07_tot')}", "Vera Rubin vintage"),
        ("F09", "Hyperscaler own capex: Microsoft CY2026 ~175,000; Meta 125,000-145,000", "Reference", "DC leases reclassified to operating; useful lives 15 -> 25 yrs; ~two-thirds short-lived GPUs/CPUs", "Hyperscaler shareholders", "L-145 · T1; L-095 · T2", f"={R('F_msft_capex')}", "Meta range in 01_Data"),
        ("F10", "Beacon Point (Nueces County, TX) behind the Lambda deal: Hut 8 second 352 MW IT lease, 15-yr; tenant capacity 704 MW; base-term 19,600, 50,200 with renewals", "Anthropic (via Lambda)", f"=TEXT({R('X01_beacon')},\"0.00\")&\" $M per MW-yr (= 19,600 / 704 MW / 15 yr); ~155 per kW-month\"", "Tenant is Nvidia (Bloomberg; FT relay); Hut 8 landlord", "L-167 · T1; L-137 · T2", f"={R('C06_LL_val')}", "Anthropic-Lambda term undisclosed (AJ 6 yrs on 09_Obligations)"),
    ]
    for i, (fid, inst, lab, rate, risk, src, val, note) in enumerate(lad):
        rr = 5 + i
        sh.put(f"A{rr}", fid, bold=True); sh.put(f"B{rr}", inst); sh.put(f"C{rr}", lab, kind="note")
        sh.put(f"D{rr}", rate, kind=("formula" if rate.startswith("=") else "note")); sh.put(f"E{rr}", risk, kind="note"); sh.put(f"F{rr}", src, kind="note")
        sh.put(f"G{rr}", val, kind=("formula" if val.startswith("=") else "note"), nf=NUM); sh.put(f"H{rr}", note, kind="note")
    sh.put("A16", "SPREAD ARITHMETIC: neocloud unsecured 9.00-9.75% (L-059) minus the backstopped SPV A2 5.75% (L-044) = 325-400 bp; on the 34,500 SPV = 1,121-1,380 per year of interest the labs do not pay because vendors carry the tail", bold=True)
    sh.header(17, ["Item", "Low", "High", "Unit", "Check low", "Check high"])
    sh.put("A18", "Spread (bp)"); sh.put("B18", f"=({R('F_neo1')}-{R('A12_A2')})*{R('BPU')}", kind="formula", nf=CNT, bold=True, key="SPREAD_BP_LO"); sh.put("C18", f"=({R('F_neo2')}-{R('A12_A2')})*{R('BPU')}", kind="formula", nf=CNT, bold=True, key="SPREAD_BP_HI"); sh.put("D18", "bp", kind="note")
    ck(sh, "E18", "B18", "SPREAD_BP_LO"); ck(sh, "F18", "C18", "SPREAD_BP_HI")
    sh.put("A19", "Annual value on the 34,500 SPV ($M)"); sh.put("B19", f"=({R('F_neo1')}-{R('A12_A2')})*{R('A12')}", kind="formula", nf=NUM, bold=True, key="SPREAD_ANN_LO"); sh.put("C19", f"=({R('F_neo2')}-{R('A12_A2')})*{R('A12')}", kind="formula", nf=NUM, bold=True, key="SPREAD_ANN_HI"); sh.put("D19", "$M/yr", kind="note")
    ck(sh, "E19", "B19", "SPREAD_ANN_LO"); ck(sh, "F19", "C19", "SPREAD_ANN_HI")
    sh.put("A20", "BACKSTOP REGISTER", bold=True)
    sh.header(21, ["Backstop", "Value ($M)", "Holder", "Row · tier", "Note"])
    bs = [
        (22, "Nvidia residual-value guaranty (PORTS, 4.25 GW-IT)", f"={R('LB09_RVG')}", "Nvidia", "L-061 · T1", "nothing payable until ready-for-service"),
        (23, "Nvidia holds the Lambda lease at Beacon Point (landlord base-term value / with renewals in E)", f"={R('C06_LL_val')}", "Nvidia (tenant), Hut 8 (landlord)", "L-137 · T2; L-167 · T1", f"={R('C06_LL_renew')}"),
        (24, "Broadcom / Google SPV support (of the 34,500)", f"={R('A12_bcom')}", "Broadcom, Google", "L-044 · T3", "4,500 unsupported"),
        (25, "Google project-debt support (five TPU site companies)", f"={R('A13')}", "Google", "L-045 · T3", "conditional"),
        (26, "AMD DC lease guarantees (max) / new DC leases up to 16 yrs (in E)", f"={R('F_amd_guar')}", "AMD", "L-146 · T1", f"={R('F_amd_lease')}"),
        (27, "SB Energy warrant fair-value charge (H1-2026)", f"={R('F_sbe_warrant')}", "SB Energy shareholders", "L-147 · T1", "equity-for-capacity has a real accounting cost at the landlord"),
        (28, "Microsoft recap gain on OpenAI (FY2026)", f"={R('F_msft_gain')}", "Microsoft", "L-054 · T1", "net gains from investments in OpenAI"),
        (29, "Huang statement (the ledger's only evidence on whether the subsidy persists)", f"={R('F_huang')}", "Nvidia", "L-075 · T2", "text"),
    ]
    for rr, lab, v, holder, src, note in bs:
        sh.put(f"A{rr}", lab); sh.put(f"B{rr}", v, kind="formula", nf=NUM); sh.put(f"C{rr}", holder, kind="note"); sh.put(f"D{rr}", src, kind="note")
        sh.put(f"E{rr}", note, kind=("formula" if note.startswith("=") else "note"), nf=NUM)
    sh.put("A30", "Exhibit E11 spans A5:H29 (ladder A5:H14, spread A16:F19, backstops A21:E29).", kind="note")
    sh.ws.freeze_panes = "A5"


# ----------------------------------------------------------------------------------------------------
# 13_OutsideView
# ----------------------------------------------------------------------------------------------------
def build_13(sh):
    sh.put("A1", "13_OutsideView: one row per forecast the report makes: reference class, base rate, base-rate source (row or 'analyst judgment'), what is different here, magnitude, direction (Exhibit E16; A5:H30). Sourced base rates: B01 (Bessemer, T3, SaaS caveat), B02 (AWS operating margin, T1); IPO slippage stays analyst judgment (B03).", kind="note")
    sh.header(4, ["Forecast", "Reference class", "Base rate", "Base-rate source (row or 'analyst judgment')", "What is different here", "Magnitude", "Direction", "Note"])
    # AM-71 arithmetic block written first so the forecast rows can reference it
    sh.put("A26", "AM-71 ARITHMETIC (why the Bessemer rule shapes only the tails)", bold=True, fill=SUB)
    sh.put("A27", "FY2026E (at YE 100,000) / PB FY2025 10,000 - 1 = growth"); sh.put("D27", f"={R('FY26A_100')}/{R('A06')}-1", kind="formula", nf=PCT, bold=True, key="AM71_G"); ck(sh, "E27", "D27", "AM71_G")
    sh.put("A28", "x 0.70 endurance = decayed 2027 growth"); sh.put("D28", f"=D27*{R('B01_priv')}", kind="formula", nf=PCT, bold=True, key="AM71_D"); ck(sh, "E28", "D28", "AM71_D")
    sh.put("A29", "Implied 2027 revenue = FY2026E x (1 + decayed growth) vs the 190,000-200,000 2028 plan"); sh.put("D29", f"={R('FY26A_100')}*(1+D28)", kind="formula", nf=NUM, bold=True, key="AM71_R"); ck(sh, "E29", "D29", "AM71_R")
    sh.put("F29", "=LB10", kind="formula", nf=NUM); sh.put("G29", f"={R('LB10_high')}", kind="formula", nf=NUM); sh.put("H29", "the plan already embeds faster decay than the base rate", kind="note")
    b01 = f"=\"next year's growth = \"&TEXT({R('B01_priv')},\"0%\")&\" (private) / \"&TEXT({R('B01_pub')},\"0%\")&\" (public) of this year's\""
    aws = f"=TEXT({R('B02_2014')},\"0.0%\")&\" (2014) -> \"&TEXT({R('B02_2016')},\"0.0%\")&\" (2016) -> 27-30% (2018-2023) -> \"&TEXT({R('B02_2024')},\"0.0%\")&\" / \"&TEXT({R('B02_2025')},\"0.0%\")&\" (2024-2025)\""
    rows = [
        (5, "Anthropic revenue 2027E-2030E (145,000 / 190,000 / Bessemer tails)", "SaaS growth endurance (Bessemer; 200+ BVP portfolio companies)", b01, "L-161 · estimated · T3 (SaaS dataset, not consumption-billed labs)", "Revenue plans beaten 2-4x within months (Jan-2026 plan 18,000 / 55,000 / 102,000 vs 65,000 run-rate by July and 190,000-200,000 for 2028)", f"=\"AM-71: the rule on FY2026E growth gives \"&TEXT({R('AM71_R')},\"#,##0\")&\" of 2027 revenue, above the 2028 plan\"", "Plan embeds faster decay than the base rate; the bear risk is a regime break, not decay; base rate shapes only the 2029E-2030E tails", "L-120, L-032, L-036, L-161"),
        (6, "OpenAI revenue 2027E-2030E (CAGR 40 / 70 / 100%)", "SaaS growth endurance (Bessemer)", b01, "L-161 · T3; CAGR triple = analyst judgment", "Run-rate doubled end-2025 -> July; +35% QTD (L-069); PB FY2026 projection +38% in eight weeks", f"=\"PB FY2026 field moved \"&TEXT({R('PB_move_O')},\"+0%\")&\" in eight weeks\"", "Up vs plan; consumption revenue, not contracted ARR", "L-065, L-069, L-024"),
        (7, "Anthropic gross-margin path (52% 2026E -> 70% Base / 77% plan 2028E)", "Capex-heavy cloud platform OPERATING margin: AWS 2014-2025 (four Amazon 10-Ks)", aws, "L-162 · confirmed · T1 (operating margin, not gross margin)", "The plan asks for 77% GROSS margin by 2028: a different line and a different basis; both labs missed GM plans in every observed case (L-083, L-119)", "25% operating margin in three years; ~30% plateau for six years", "Down vs plan (Base 2028 GM 70%, not 77%)", "L-162, L-119, L-083"),
        (8, "OpenAI gross-margin path (33% 2025 -> AJ COGS % 40% -> 34%)", "Own record: 33% vs the 46% plan (13pp miss); AWS operating-margin path as the platform reference", f"=\"OpenAI 2025 GM \"&TEXT({R('O07_gm2025')},\"0%\")&\" vs plan \"&TEXT({R('O07_gmplan')},\"0%\")", "L-083 · estimated · T3; L-162 · T1", "Inference 8,400 on 13,100 (64% of revenue) in 2025", "13pp miss", "Down vs plan", "L-083"),
        (9, "Anthropic training ramp (7,000 -> 14,000 -> 22,000; T4 plan)", "Cost plans revised UP in every observed case in this ledger", "OpenAI compute plan 600,000 (May) -> 750,000 (Jul): +25% in 11 weeks; burn forecast +111,000 (Feb)", "L-078, L-062, L-082 (ledger-supported)", "Bear applies +25% to the plan; Bull -15%", f"=\"+\"&TEXT({R('LB07b')}/{R('LB07b_may')}-1,\"0%\")&\" plan revision in 11 weeks (OpenAI)\"", "Up vs plan", "L-125, L-062, L-078"),
        (10, "OpenAI training ramp (25,000 -> 120,000; T4 plan)", "Cost plans revised up (own record)", "as above", "L-078, L-062, L-082", "The T4 split (25,000 training + 14,100 inference) does not reconcile to the T2 50,000 total: 10,900 unexplained", f"=\"unexplained \"&TEXT({R('UNEXPL')},\"#,##0\")", "Up vs plan", "L-125, L-078, L-083"),
        (11, "Anthropic burn / loss path 2026 (C-12: GAAP -11,000 plan vs Q2 positive adjusted operating income)", "Plan-vs-actual: revenue up, cost up, margin down", "Jan-2026 plan superseded within seven months; definitions differ (GAAP incl. SBC vs non-GAAP adjusted)", "L-120, L-151, L-152 (frozen conflict, SW_A_2026_LOSS)", "The Q2 result is a non-GAAP projection whose definition is unpublished", f"=\"Q2 adjusted margin ~\"&TEXT(LB05b/{R('LB05b_base')},\"0.0%\")", "Better than plan on the adjusted measure; GAAP unknown", "L-034, L-151, L-152"),
        (12, "OpenAI burn path (25,000 / 27,000 -> 57,000 / 63,000 -> +39,000 in 2030)", "Burn forecasts raised (+111,000 cumulative, Feb-2026); two vintages within two months", "Feb -> post-April vintages: +8% (2026) / +11% (2027)", "L-082 · estimated · T3; L-142", "H1 operating loss 21,600 incl. SBC (1.74x revenue) vs a 25,000-27,000 burn plan: the bridge is a HOLE (SBC + vendor financing)", f"=TEXT({R('O05_b27apr')}/{R('O05_b27feb')}-1,\"+0%\")&\" (2027 plan, two vintages)\"", "Up vs plan", "L-082, L-066"),
        (13, "Anthropic IPO window (October 2026 per PB; mid-October reported)", "IPO-window slippage", "No filed-to-priced or withdrawal statistic exists (PB none; Renaissance paywall; SEC counts only): ANALYST JUDGMENT. Colour: median step-up 1.3x at listing (Q2-2026); Cerebras cancel -> refile -> price ~9 months", "analyst judgment (L-163 · could-not-verify; T2 colour)", "No public S-1 on EDGAR by Sep-9 (L-001); the 15-day rule needs a public flip by late September for an October pricing", f"=\"step-up \"&TEXT({R('B03_stepup')},\"0.0x\")&\"; Cerebras ~\"&TEXT({R('B03_cerebras')},\"0\")&\" months\"", "Slippage risk", "L-001, L-003, L-039, L-040, L-163"),
        (14, "OpenAI IPO window (SW_IPO_OAI)", "IPO-window slippage", "as above: analyst judgment; PB's 'September 2026' retired by L-002 and the 15-day rule", "analyst judgment (L-163); L-002, L-004, L-068", "CFO: 'public company in 2027', possibly sooner", "=SW_IPO_OAI", "Slipped (Sep-2026 -> Q4-2026 / 2027)", "L-002, L-004, L-068"),
        (15, "Obligation consumption 2028 (priced 53,355 + Google leg vs the 65,700-68,000 plan envelope)", "Take-or-pay vs consumption contracts; disclosure silence in every filing", "Alphabet 10-Q: zero Anthropic mentions, 811,000 commitments not itemized; Google release no $; Broadcom 10-Q no customer commitment; Microsoft 10-K no %", "L-153, L-154, L-156, L-157 · confirmed · T1 (silence); gap = analyst arithmetic", "One of three things is untrue: the 77% margin path, the 22,000 training budget, or the take-or-pay status of the GW deals; the public S-1 will say which", f"=\"2028 gap (reported branch) \"&TEXT({RY('GAP_LO', 2028)},\"#,##0\")&\" to \"&TEXT({RY('GAP_HI', 2028)},\"#,##0\")", "Conditional finding, not a verdict", "L-036, L-119, L-125, L-155"),
        (16, "Greenfield capital to milestones (Workbook B: Lean / Full / Vertically integrated)", "Entrants: SSI 7,000 raised, zero revenue; TML 2,000 seed; Reflection 2,155; Mistral 7,492; xAI accumulated deficit 41,311", "2,000-8,000 to a model with little revenue; ~41,000 accumulated deficit for an owned-cluster entrant", "L-097, L-098, L-099, L-100, L-096 · T2 / T1", "Custom-silicon supply booked through 2028 by incumbents (L-144): an entrant buys merchant GPUs or waits", "see B/09_Output reference-class check", "Fenced by the reference class", "L-096-L-102, L-144"),
        (18, "LEDGER-SUPPORTED BASE RATE: revenue plans beaten", "Plan-vs-actual", "Anthropic Jan-2026 plan 18,000 (2026) / 55,000 (2027) / 102,000 (2028) vs 65,000 run-rate by July and 190,000-200,000 (2028) by August", "L-120, L-032, L-036", f"=\"PB projections moved \"&TEXT({R('PB_move_A')},\"+0%\")&\" (Anthropic FY27) and \"&TEXT({R('PB_move_O')},\"+0%\")&\" (OpenAI FY26) in eight weeks\"", "2-4x within months", "Up", "L-009, L-024"),
        (19, "LEDGER-SUPPORTED BASE RATE: cost plans raised", "Plan-vs-actual", "OpenAI compute plan 600,000 -> 750,000; burn +111,000; Anthropic server rentals ~180,000 through 2029 (Jan vintage) already stale", "L-078, L-062, L-082, L-120", "n/a", "+25% in 11 weeks", "Up", ""),
        (20, "LEDGER-SUPPORTED BASE RATE: margin plans missed", "Plan-vs-actual", "OpenAI 33% vs 46% plan; Anthropic lowered its GM projection (The Information, Jan-2026)", "L-083, L-119", "n/a", "13pp (OpenAI)", "Down", ""),
        (21, "LEDGER-SUPPORTED BASE RATE: milestones slipped", "Milestone slippage", "No public S-1 for either by Sep-9; ChatGPT 1B users seven months late; Abilene 1.2 GW from a 2.1 GW plan", "L-001, L-002, L-004, L-040, L-080, L-079", "n/a", f"=TEXT({R('CHATGPT_late')},\"0\")&\" months late; Abilene \"&TEXT({R('ABIL_plan')},\"0.0\")&\" of \"&TEXT({R('ABIL_orig')},\"0.0\")&\" GW\"", "Slipped", ""),
        (22, "LEDGER-SUPPORTED BASE RATE: build-cost inflation", "Datacenter development cost", f"=\"+\"&TEXT({R('CW_infl')},\"0%\")&\" per MW since Q4-2024 to \"&TEXT({R('CW_build')},\"0.0\")&\" $M per MW\"", "L-109 · confirmed · T2", "n/a", "+21%", "Up", ""),
        (23, "LEDGER-SUPPORTED BASE RATE: GPU residual values", "Hardware residual value", f"=\"H100 new \"&TEXT({R('GPU_new_lo')}/{R('KPERUNIT')},\"0\")&\"-\"&TEXT({R('GPU_new_hi')}/{R('KPERUNIT')},\"0\")&\"K vs used \"&TEXT({R('GPU_used_lo')}/{R('KPERUNIT')},\"0.0\")&\"-\"&TEXT({R('GPU_used_hi')}/{R('KPERUNIT')},\"0\")&\"K: used at \"&TEXT({R('GPU_used_lo')}/{R('GPU_new_lo')},\"0%\")&\"-\"&TEXT({R('GPU_used_hi')}/{R('GPU_new_hi')},\"0%\")&\" of new\"", "L-103 · estimated · T4", "n/a", "33-63% of new", "Down", ""),
        (24, "LEDGER-SUPPORTED BASE RATE: useful-life extension", "Hyperscaler accounting", f"=\"Microsoft datacenter useful life \"&TEXT({R('MSFT_life_old')},\"0\")&\" -> \"&TEXT({R('MSFT_life_new')},\"0\")&\" years while GPUs stay short-lived (~two-thirds of capex)\"", "L-145 · confirmed · T1", "n/a", "+10 years (DCs)", "Mixed", ""),
    ]
    for rr, f_, rc, br, src, diff, mag, dirn, note in rows:
        sh.put(f"A{rr}", f_, bold=(rr < 17)); sh.put(f"B{rr}", rc, kind="note")
        sh.put(f"C{rr}", br, kind=("formula" if br.startswith("=") else "note")); sh.put(f"D{rr}", src, kind="note")
        sh.put(f"E{rr}", diff, kind=("formula" if diff.startswith("=") else "note")); sh.put(f"F{rr}", mag, kind=("formula" if mag.startswith("=") else "note"))
        sh.put(f"G{rr}", dirn, kind=("formula" if dirn.startswith("=") else "note")); sh.put(f"H{rr}", note, kind="note")
    sh.put("A30", "Do not say that the Bessemer or AWS base rates are AI-lab base rates ('SaaS' and 'a capex-heavy cloud platform'); label IPO slippage 'analyst judgment' and cite the Cerebras case (L-163).", kind="note")
    sh.ws.freeze_panes = "B5"


# ----------------------------------------------------------------------------------------------------
# 08_Output
# ----------------------------------------------------------------------------------------------------
def build_08(sh):
    sh.put("A1", "08_Output: E1 at-a-glance (A1:H14); the ten load-bearing figures (named ranges LB01-LB10); verdict flags; the spec section 9 check table (rows 44+).", kind="note")
    sh.header(2, ["Item (Exhibit E1)", "Unit", "Anthropic", "Basis / tier", "OpenAI", "Basis / tier", "Rows", "Note"])
    e1 = [
        (3, "Post-money mark", "$M", f"={R('M01')}", "Series H post · T2/T1 · 2026-05-28", f"={R('M02')}", "Mar-2026 round post · T2 · 2026-03-31 (tender Aug-10)", "L-005, L-038, L-019, L-067", "VOLATILE"),
        (4, "Equity-only capital raised (Ruling 1 denominator)", "$M", "=LB03", "sum of ten PB equity rounds · T2 · 2026-05-28", "=LB04", "sum of PB equity rounds · T2 · 2026-03-31", "L-007, L-022", "excl. revolver / debt / lease SPV"),
        (5, "Annualized run-rate", "$M/yr", "=LB01", "GROSS run-rate · T2 · 2026-07-31", "=LB02", f"=\"basis unstated (\"&SW_OAI_BASIS&\" assumed) · T2 · 2026-07\"", "L-032, L-065", "Ruling 5: never compared gross vs net"),
        (6, "Net run-rate at the haircut in use (haircut visible in D)", "$M/yr", f"={R('NET_A_LIVE')}", "=SW_HAIRCUT", f"={R('NET_O_LIVE')}", "=SW_OAI_BASIS", "L-126 (Ruling 5), C-13, C-16", "equalized"),
        (7, "Q2-2026 revenue (recognized, preliminary)", "$M", "=LB05a", "GROSS presumed · T2 · Q2-2026", "=LB06a", "NET presumed · T2 · Q2-2026", "L-033, L-151, L-066", "Anthropic Q1 4,730; OpenAI Q1 5,700"),
        (8, "Q2-2026 operating result", "$M", "=LB05b", "ADJUSTED operating income, non-GAAP (definition unpublished; excludes SBC per relays) · T2/T3 · projection, sign confirmed", "=-LB06b", "operating loss incl. SBC · T2", "L-034, L-151, L-152, L-066", "Ruling 3: not FCF, not an operating profit"),
        (9, "FY2026E recognized revenue, derived range (flat from July to YE 120,000 / 0% to 20% monthly growth)", "$M", f"=TEXT({R('FY26A_FLAT')},\"#,##0\")&\" - \"&TEXT({R('FY26A_120')},\"#,##0\")", "linear ramp integration · derived", f"=TEXT({R('FY26O_0')},\"#,##0\")&\" - \"&TEXT({R('FY26O_20')},\"#,##0\")", "compounding integration · derived", "L-151, L-033, L-032, L-035; L-066, L-065", f"=\"live scenario: \"&TEXT({R('FY26A')},\"#,##0\")&\" / \"&TEXT({R('FY26O')},\"#,##0\")"),
        (10, "Documented-$ compute contracts (excl. SPV) / reported-$ incl. the Google leg [VERIFY]", "$M", f"={R('DOC_A')}", f"=\"8 contracts · T1-T3; reported-$ \"&TEXT({R('REP_A')},\"#,##0\")&\" [VERIFY, T3]\"", f"={R('DOC_O')}", f"=\"4 contracts · T1-T2; recalled-$ \"&TEXT({R('REC_O')},\"#,##0\")&\" (CNV)\"", "09_Obligations", "scope lines mandatory (C-14)"),
        (11, "Unpriced gigawatts", "GW", f"=\"Google \"&TEXT({R('X02_a27')},\"0\")&\" GW contracted (reported value T3 only) + \"&TEXT({R('X02_a28')},\"0\")&\" GW line of sight; AMD \"&TEXT({R('C11_GW')},\"0\")&\" GW\"", "L-073, L-049, L-043, L-155", f"=\"SB Energy \"&TEXT({R('UNPRICED_GW_O')},\"0.00\")&\" GW-IT (T1 leases, rent undisclosed); AMD \"&TEXT({R('C19_GW')},\"0\")&\" GW; Broadcom \"&TEXT({R('X02_o27')},\"0.0\")&\" GW 2027 / >\"&TEXT({R('X02_o28')},\"0\")&\" GW 2028\"", "L-061, L-060, L-050", "09_Obligations", "no dollar value in any filing"),
        (12, "IPO status (EDGAR 2026-09-09: no public S-1 for either)", "status", f"=\"confidential \"&{R('I01_a_conf')}&\"; expected \"&{R('I01_a_exp')}&\" (PB); \"&{R('I01_a_press')}", "L-039 T1; L-003 T2; L-040 T3", f"=\"confidential \"&{R('I01_o_conf')}&\"; SW_IPO_OAI = \"&SW_IPO_OAI&\"; CFO: \"&{R('I01_o_cfo')}", "L-004 T2; L-068 T2; L-002 T1", "L-001, L-002", "=SW_IPO_OAI"),
        (13, "Scenario / haircut in use", "switch", f"={R('SCEN_LABEL')}", "SW_SCEN", "=SW_HAIRCUT", "SW_HAIRCUT", "00_Assumptions, 12_Conflicts", "switch register on 12_Conflicts"),
        (14, "CE (net run-rate / equity-only) and ratio", "x", f"={R('CE_A_LIVE')}", "=SW_HAIRCUT", f"={R('CE_O_LIVE')}", f"=\"ratio \"&TEXT({R('CE_RATIO_LIVE')},\"0.00x\")", "05_Cash_Fund", "Ruling 1"),
    ]
    for rr, lab, unit, a, ab, o, ob, rows, note in e1:
        sh.put(f"A{rr}", lab, bold=True); sh.put(f"B{rr}", unit, kind="note")
        nf = MULT3 if unit == "x" else (NUM if unit in ("$M", "$M/yr") else GEN)
        for col, v in (("C", a), ("D", ab), ("E", o), ("F", ob), ("H", note)):
            if isinstance(v, str) and v.startswith("="):
                sh.put(f"{col}{rr}", v, kind="output" if col in ("C", "E") else "formula", nf=(nf if col in ("C", "E") else (PCT2 if "SW_HAIRCUT" == v[1:] else GEN)))
            else:
                sh.put(f"{col}{rr}", v, kind="note")
        sh.put(f"G{rr}", rows, kind="note")
    sh.section(16, "THE TEN LOAD-BEARING FIGURES (argument-map section A; named ranges LB01-LB10 on 01_Data)", ncols=11)
    sh.header(17, ["#", "Figure", "Value", "Unit", "As-of", "Tier", "Status", "What turns on it"])
    lb = [
        (1, "Anthropic annualized run-rate (LB01)", "=LB01", "$M/yr", "2026-07-31", "T2", "confirmed", "every Anthropic multiple, CE ratio, the equalization, the AIBQ CE-1 move"),
        (2, "OpenAI annualized run-rate (LB02)", "=LB02", "$M/yr", "2026-07", "T2", "confirmed", "every OpenAI multiple and CE ratio; C-16 switch"),
        (3, "Anthropic equity-only capital raised (LB03)", "=LB03", "$M", "2026-05-28", "T2", "estimated (derived)", "CE denominator (Ruling 1); the 'entry fee' headline"),
        (4, "OpenAI equity-only capital raised (LB04)", "=LB04", "$M", "2026-03-31", "T2", "estimated (derived)", "CE denominator; the 'entry fee' headline"),
        (5, "Anthropic Q2-2026 revenue (LB05a) and first positive ADJUSTED operating income (LB05b; non-GAAP, definition unpublished)", "=LB05a", "$M", "Q2-2026", "T2 (T3 for the definition)", "confirmed (revenue, sign) / estimated (margin, definition)", "the strongest counter-evidence; CE-3; the GM cross-check; C-12"),
        (6, "OpenAI Q2-2026 revenue (LB06a) and operating loss incl. SBC (LB06b)", "=LB06a", "$M", "Q2-2026", "T2", "confirmed", "the strongest evidence for the thesis; CE-3; the burn-vs-loss bridge"),
        (7, "OpenAI compute spend 2026 (LB07a) and through 2030 (LB07b)", "=LB07a", "$M", "2026-05-05 / 2026-07-22", "T2", "confirmed / estimated", "the consumption side of the obligation stack"),
        (8, "Microsoft revenue from OpenAI arrangements FY2026 (LB08)", "=LB08", "$M", "FY ended 2026-06-30", "T1", "confirmed", "the only T1 cash anchor in the OpenAI stack"),
        (9, "SB Energy PORTS leases 8.0 GW-IT and the Nvidia 105,000 RVG (LB09)", "=LB09", "GW-IT", "2026-08-17", "T1", "confirmed", "who holds the risk; CI-2; the quasi-debt argument"),
        (10, "Anthropic 2028 revenue forecast to IPO investors (LB10: 190,000-200,000)", "=LB10", "$M", "FY2028E (Aug-2026 vintage)", "T2", "estimated", "the margin-commitment incompatibility with the T4 GM path and training plan"),
    ]
    for i, (n, fig, v, unit, asof, tier, status, turns) in enumerate(lb):
        rr = 18 + i
        sh.put(f"A{rr}", f"#{n}", kind="note", align="center"); sh.put(f"B{rr}", fig); sh.put(f"C{rr}", v, kind="output", nf=(CNT2 if unit == "GW-IT" else NUM)); sh.put(f"D{rr}", unit, kind="note")
        sh.put(f"E{rr}", asof, kind="note"); sh.put(f"F{rr}", tier, kind="note"); sh.put(f"G{rr}", status, kind="note"); sh.put(f"H{rr}", turns, kind="note")
    sh.put("A28", "Companion values: LB05b =", kind="note"); sh.put("C28", "=LB05b", kind="output", nf=NUM); sh.put("D28", "LB06b (loss) =", kind="note"); sh.put("E28", "=LB06b", kind="output", nf=NUM); sh.put("F28", "LB07b =", kind="note"); sh.put("G28", "=LB07b", kind="output", nf=NUM); sh.put("H28", f"=\"LB10 high = \"&TEXT({R('LB10_high')},\"#,##0\")&\"; RVG = \"&TEXT({R('LB09_RVG')},\"#,##0\")", kind="formula")
    sh.section(30, "VERDICT FLAGS", ncols=11)
    sh.header(31, ["Flag", "Value", "Reading", "Cells"])
    vf = [
        (32, "E10 gap 2028 at the plan envelope, Google leg in use (low / high; negative = plan does not cover commitments)", f"={RY('GAP_LO', 2028)}", f"=\"to \"&TEXT({RY('GAP_HI', 2028)},\"#,##0\")&\"; Google leg = \"&SW_GOOGLE_VALUE", "09_Obligations I88:I89"),
        (33, "E10 gap 2028 after the AMD proxy (low)", f"={RY('GAP_LO_AMD', 2028)}", '=IF(B33<0,"plan does not cover commitments","covers")', "09_Obligations I90"),
        (34, "Relative multiple at 39.75% (Anthropic equalized vs OpenAI NET)", f"={R('RELMULT_3975')}", '=IF(B34>0,"Anthropic richer (+)","Anthropic cheaper (-)")', "06_Valuation D18"),
        (35, "Relative multiple at 27%", f"={R('RELMULT_27')}", '=IF(B35>0,"Anthropic richer (+)","Anthropic cheaper (-)")', "06_Valuation D15"),
        (36, "Relative multiple at the live switches", f"={R('RELMULT_LIVE')}", '=IF(B36>0,"Anthropic richer (+)","Anthropic cheaper (-)")', "06_Valuation D14"),
        (37, "AIBQ composites, live (Anthropic / OpenAI in C)", f"={R('COMP_A_LIVE')}", f"={R('COMP_O_LIVE')}", "11_AIBQ composite block"),
        (38, "$B per AIBQ point, live (Anthropic / OpenAI in C; spread in D)", f"={R('PPT_A_LIVE')}", f"={R('PPT_O_LIVE')}", f"={R('SPREAD_LIVE')}"),
        (39, "CE ratio, live", f"={R('CE_RATIO_LIVE')}", '=IF(B39>1,"Anthropic more capital-efficient","OpenAI more capital-efficient")', "05_Cash_Fund H43"),
        (40, "Anthropic 2026 result branch in use (SW_A_2026_LOSS)", f"={R('A_2026_RESULT')}", "=SW_A_2026_LOSS", "05_Cash_Fund D66"),
        (41, "Scenario in use", f"={R('SCEN_LABEL')}", '=" Bear = flat July run-rate, GM 44/55/60, training plan +25%, OpenAI growth 0%/40%; Bull = YE 120,000, GM 60/63/77, plan -15%, 20%/100%"', "00_Assumptions C4"),
    ]
    for rr, lab, v, rd, cells in vf:
        sh.put(f"A{rr}", lab, bold=True)
        nf = NUM if rr in (32, 33, 40) else (PCT if rr in (34, 35, 36) else (DEC3 if rr == 37 else (CNT1 if rr == 38 else (MULT2 if rr == 39 else GEN))))
        sh.put(f"B{rr}", v, kind="output", nf=nf)
        sh.put(f"C{rr}", rd, kind="formula", nf=(DEC3 if rr == 37 else (CNT1 if rr == 38 else GEN)))
        sh.put(f"D{rr}", cells, kind=("formula" if cells.startswith("=") else "note"), nf=MULT2)
    sh.section(43, "SPEC SECTION 9 CHECK TABLE (expected values typed once on 00_Assumptions rows 132+; PASS/FAIL cells live on the tabs and are linked here)", ncols=11)
    sh.header(44, ["Check", "Expected", "Tolerance", "PASS / FAIL (linked)", "Where computed"])
    where = {"IDENT_A": "05_Cash_Fund D17", "IDENT_O": "05_Cash_Fund J17", "NETRR": "02_Revenue D38", "MULT_G": "06_Valuation D7", "MULT_3975": "06_Valuation D9", "MULT_27": "06_Valuation D10", "MULT_O": "06_Valuation D12", "MULT_OG": "06_Valuation D13",
             "CE_3975": "05_Cash_Fund E44", "CE_27": "05_Cash_Fund E45", "CE_G": "05_Cash_Fund E46", "CE_O": "05_Cash_Fund G44", "RATIO": "05_Cash_Fund H44", "RATIO27": "05_Cash_Fund H45", "RATIOG": "05_Cash_Fund H46",
             "FY26_100": "02_Revenue M55", "FY26_120": "02_Revenue M56", "FY26_FLAT": "02_Revenue M57", "H1A": "02_Revenue L54", "Q2Q1": "02_Revenue E20", "OAI_0": "02_Revenue M65", "OAI_10": "02_Revenue M66", "OAI_20": "02_Revenue M67",
             "DOC_A": "09_Obligations B18", "DOC_A_SPV": "09_Obligations B19", "REP_A": "09_Obligations B20", "DOC_O": "09_Obligations B38", "REC_O": "09_Obligations B39", "BBG": "09_Obligations B46", "STEP": "09_Obligations B48", "TC": "09_Obligations B47", "CANC_A": "09_Obligations E18",
             "RUN26": "09_Obligations G64", "RUN27": "09_Obligations H64", "RUN28": "09_Obligations I64", "RUN29": "09_Obligations J64", "RUN30": "09_Obligations K64", "RUNO27": "09_Obligations H68", "STACK28": "09_Obligations I73",
             "ENV28_LO": "09_Obligations I82", "ENV28_HI": "09_Obligations I83", "ENV27_LO": "09_Obligations H82", "ENV27_HI": "09_Obligations H83",
             "GAP28_REP_LO": "09_Obligations AK98:AL98", "GAP27_REP_LO": "09_Obligations AI98:AJ98", "GAP28_PROXY": "09_Obligations AM99", "GAP28_15GW": "09_Obligations AM101", "GAP28_125": "09_Obligations AM100", "GAP28_125_15": "09_Obligations AM102",
             "GRIDB": "07_Sensitivity G40", "UNEXPL": "03_Costs G49", "GM_GRID_G": "03_Costs D54", "GM_GRID_N": "03_Costs E54",
             "CE_A": "11_AIBQ CE dimension F", "CE_A_CL": "11_AIBQ CE dimension G", "CI_A": "11_AIBQ CI dimension D", "CE_O_AIBQ": "11_AIBQ OpenAI CE dimension D", "CI_O": "11_AIBQ OpenAI CI dimension D",
             "COMP_A": "11_AIBQ composite H", "COMP_A_CL": "11_AIBQ composite H (closes)", "COMP_A_CANON": "11_AIBQ composite H (canonical)", "COMP_O": "11_AIBQ composite H (OpenAI)", "COMP_O_G": "11_AIBQ composite H (gross case)", "EI_A": "11_AIBQ Efficiency Index C", "EI_O": "11_AIBQ Efficiency Index F",
             "PPT_A": "06_Valuation C26", "PPT_O": "06_Valuation E26", "PPT_A_CL": "06_Valuation C27", "SPREAD": "06_Valuation F26", "SPREAD_CL": "06_Valuation F27", "SPREAD_OLD": "06_Valuation F25", "PPT_O_OLD": "06_Valuation E25", "MORE_PPT": "06_Valuation H26",
             "TAIL_BEAR29": "02_Revenue J74", "TAIL_BEAR30": "02_Revenue K74", "TAIL_BASE29": "02_Revenue J75", "TAIL_BASE30": "02_Revenue K75", "TAIL_BULL29": "02_Revenue J76", "TAIL_BULL30": "02_Revenue K76",
             "SPREAD_BP_LO": "10_Financing B18", "SPREAD_BP_HI": "10_Financing C18", "SPREAD_ANN_LO": "10_Financing B19", "SPREAD_ANN_HI": "10_Financing C19", "J16_MULT": "06_Valuation D16:D17", "J16_RATIO": "05_Cash_Fund H42",
             "AM71_G": "13_OutsideView D27", "AM71_D": "13_OutsideView D28", "AM71_R": "13_OutsideView D29", "REL_3975": "07_Sensitivity G8", "REL_27": "07_Sensitivity G6", "REL_G": "07_Sensitivity G12", "RATIO_G_CE": "07_Sensitivity H12",
             "GOOG_RATE5": "09_Obligations D95", "GOOG_RATE16": "09_Obligations E95"}
    for i, (k, lab, v, tol) in enumerate(CHECKS):
        rr = 45 + i
        sh.put(f"A{rr}", lab); sh.put(f"B{rr}", f"={R('CHK_'+k)}", kind="formula", nf=GEN); sh.put(f"C{rr}", f"={R('TOL_'+k)}", kind="formula", nf=GEN)
        if has_key(f"PF_{k}"):
            sh.put(f"D{rr}", f"={R('PF_'+k)}", kind="output"); sh.put(f"E{rr}", where.get(k, ""), kind="note")
        else:
            sh.put(f"D{rr}", "not wired", kind="flag"); sh.put(f"E{rr}", where.get(k, ""), kind="note")
    rr = 45 + len(CHECKS)
    sh.put(f"A{rr}", "Count of FAIL cells above (0 = all pass at the current switch settings; checks assume Base defaults):", bold=True)
    sh.put(f"D{rr}", f'=COUNTIF(D45:D{rr-1},"FAIL*")', kind="output", nf=GEN, key="FAILCOUNT")
    sh.ws.freeze_panes = "A3"
