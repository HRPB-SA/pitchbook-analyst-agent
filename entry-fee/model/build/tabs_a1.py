# tabs_a1.py: Workbook A foundation tabs: 01_Data (facts), 00_Assumptions (AJ drivers), 12_Conflicts (switches).
import datetime as dt
from xlhelp import *

SWITCHES = ["SW_SCEN", "SW_HAIRCUT", "SW_OAI_BASIS", "SW_IPO_OAI", "SW_A_FY25", "SW_A_FY24_NI", "SW_A_2026_LOSS",
            "SW_A_HC", "SW_TPU_RATE", "SW_GW_2028", "SW_TOTAL_RAISED_VIEW", "SW_15B_FACILITY", "SW_GOOGLE_VALUE", "SW_SSI"]
LBNAMES = ["LB01", "LB02", "LB03", "LB04", "LB05", "LB05a", "LB05b", "LB06", "LB06a", "LB06b", "LB07", "LB07a", "LB07b",
           "LB08", "LB09", "LB10"]
register_names(SWITCHES + LBNAMES)

D = dt.date


# ----------------------------------------------------------------------------------------------------
# 01_Data
# ----------------------------------------------------------------------------------------------------
def build_01(sh):
    sh.put("A1", "01_Data: facts only. One row per ledger anchor used anywhere in Workbook A. Column C = source string "
                 "(row · status · tier · as-of · basis). Values in column D are the single home of every figure (blue = typed input, "
                 "black = derived by formula from other rows, yellow = could-not-verify / AJ). Named ranges LB01-LB10 point here.",
           kind="note", wrap=False)
    sh.put("A2", "Provenance: research/evidence-ledger.md (168 rows; confirmed 97, estimated 51, recalled 6, could-not-verify 14). "
                 "Retired rows NOT entered: L-011/L-026 net income -42,000 (C-04); L-124 capex 190,000; the Jul-16 'Fast Mode 3x cheaper'; "
                 "the 161,254 Total Raised; the 47.16B xAI pre-merger raise; any WSJ Apr-6 breakeven year.", kind="note")
    sh.header(3, ["ID", "Item", "Source (row · status · tier · as-of · basis)", "Value", "Unit", "As-of", "Basis", "Status", "Tier",
                  "Decay", "Ledger row", "Used by", "Note"])
    r = 4

    def sec(title):
        nonlocal r
        sh.section(r, title, ncols=13)
        r += 1

    def row(id_, item, value, unit, rowid, status, tier, asof, basis, decay="STABLE", used="", note="", nf=NUM,
            name=None, yellow=False, kind="input", key=None):
        nonlocal r
        r = drow(sh, r, id_, item, value, unit, rowid, status, tier, asof, basis, decay, used, note, nf, kind, name, yellow, key)

    # ---- load-bearing ----
    sec("LOAD-BEARING FIGURES (argument-map section A; named ranges LB01-LB10)")
    row("LB01", "Anthropic annualized run-rate, end-July 2026", 65000, "$M/yr", "L-032", "confirmed", "T2", "2026-07-31",
        "GROSS run-rate (incl. cloud-partner resale)", "QUARTERLY", "02, 05, 06, 11", name="LB01")
    row("LB02", "OpenAI annualized run-rate, July 2026 (floor: '>40')", 40000, "$M/yr", "L-065", "confirmed", "T2", "2026-07",
        "basis unstated (NET assumed via SW_OAI_BASIS)", "QUARTERLY", "02, 05, 06, 11", name="LB02")
    row("LB03", "Anthropic equity-only capital raised", 124254, "$M", "L-007", "estimated", "T2", "2026-05-28",
        "sum of ten PB equity rounds", "STABLE", "05, 11", name="LB03")
    row("LB04", "OpenAI equity-only capital raised", 181216.5, "$M", "L-022", "estimated", "T2", "2026-03-31",
        "sum of PB equity rounds", "STABLE", "05, 11", nf=NUM1, name="LB04")
    row("LB05a", "Anthropic Q2-2026 revenue (preliminary; range 11,500-11,600)", 11600, "$M", "L-033", "confirmed", "T2", "Q2-2026",
        "recognized, preliminary, GROSS presumed", "QUARTERLY", "02, 03, 04", name="LB05a")
    sh.wb.defined_names["LB05"] = DefinedName("LB05", attr_text=REG["LB05a"])
    row("LB05a_low", "Anthropic Q2-2026 revenue, the '>11,500' print", 11500, "$M", "L-151", "confirmed", "T2", "Q2-2026",
        "recognized, preliminary, GROSS presumed", "QUARTERLY", "04")
    row("LB05b", "Anthropic Q2-2026 ADJUSTED operating income (projection; sign confirmed)", 559, "$M", "L-034, L-151, L-152",
        "confirmed (sign) / estimated (amount, definition)", "T2 / T3", "Q2-2026",
        "non-GAAP adjusted operating income; definition unpublished; per T3 relays includes training cost, excludes SBC; not an operating profit, not FCF (Ruling 3)",
        "QUARTERLY", "04, 11", name="LB05b")
    row("LB05b_base", "Anthropic Q2-2026 projected revenue base behind the 5.1% adjusted margin (Reuters)", 10900, "$M", "L-034, L-152",
        "estimated", "T2 / T3", "Q2-2026", "projected revenue 'at least 10,900'", "QUARTERLY", "04, 11")
    row("A03", "Anthropic Q1-2026 revenue", 4730, "$M", "L-151", "confirmed", "T2", "Q1-2026",
        "recognized, GROSS presumed (Bloomberg full text); replaces the derived ~5,000 (L-129)", "QUARTERLY", "02, 03, 04")
    row("A03b", "Anthropic Q2-2025 revenue (comparator)", 787, "$M", "L-151", "confirmed", "T2", "Q2-2025",
        "recognized comparator; supersedes L-143 (T4)", "QUARTERLY", "02")
    row("LB06a_Q1", "OpenAI Q1-2026 revenue", 5700, "$M", "L-066", "confirmed", "T2", "Q1-2026", "recognized, NET presumed", "QUARTERLY", "02, 04")
    row("LB06a", "OpenAI Q2-2026 revenue", 6700, "$M", "L-066", "confirmed", "T2", "Q2-2026", "recognized, NET presumed", "QUARTERLY", "02, 04", name="LB06a")
    sh.wb.defined_names["LB06"] = DefinedName("LB06", attr_text=REG["LB06a"])
    row("LB06b_Q1", "OpenAI Q1-2026 operating loss incl. SBC (magnitude)", 9300, "$M loss", "L-066", "confirmed", "T2", "Q1-2026",
        "GAAP-style, incl. SBC", "QUARTERLY", "04, 05, 11")
    row("LB06b", "OpenAI Q2-2026 operating loss incl. SBC (magnitude)", 12300, "$M loss", "L-066", "confirmed", "T2", "Q2-2026",
        "GAAP-style, incl. SBC", "QUARTERLY", "04, 05, 11", name="LB06b")
    row("LB07a", "OpenAI 2026 compute spend", 50000, "$M", "L-078", "confirmed", "T2", "2026-05-05", "company statement (sworn)",
        "QUARTERLY", "03, 09", name="LB07a")
    sh.wb.defined_names["LB07"] = DefinedName("LB07", attr_text=REG["LB07a"])
    row("LB07b", "OpenAI compute plan through 2030 (Jul-2026 vintage)", 750000, "$M", "L-062, L-078, L-082", "estimated", "T2", "2026-07-22",
        "consumption plan 2026-2030", "QUARTERLY", "09, 07", name="LB07b")
    row("LB07b_may", "OpenAI compute plan through 2030 (May-2026 vintage, sworn)", 600000, "$M", "L-078", "confirmed", "T2", "2026-05-05",
        "'roughly 600,000 in total compute spending through 2030'", "QUARTERLY", "00, 09")
    row("LB07b_feb", "OpenAI spend plan through 2030 (Feb-2026 vintage, 'training and operating')", 665000, "$M", "L-082", "estimated", "T3",
        "2026-02-21", "P&L consumption 2026-2030, broader definition", "QUARTERLY", "09")
    row("LB08", "Microsoft FY2026 revenue from OpenAI arrangements incl. revenue share", 24100, "$M", "L-054", "confirmed", "T1",
        "FY ended 2026-06-30", "Azure consumption plus revenue share received, at Microsoft", "STABLE", "09, 10", name="LB08")
    row("LB08_AR", "Microsoft accounts receivable from OpenAI at 2026-06-30", 6000, "$M", "L-054", "confirmed", "T1", "2026-06-30",
        "10-K", "STABLE", "09, 10")
    row("LB09_GW", "SB Energy PORTS-Pike leases, capacity (17 leases, 20-yr, OpenAI affiliate tenant)", 8.0, "GW-IT", "L-061, L-147", "confirmed", "T1",
        "2026-08-17", "issuer S-1", "STABLE", "09, 10, 11", nf=CNT2, name="LB09")
    row("LB09_term", "PORTS lease term", 20, "yrs", "L-061", "confirmed", "T1", "2026-08-17", "issuer S-1", "STABLE", "09", nf=CNT)
    row("LB09_RVG", "Nvidia residual-value guaranty on PORTS, aggregate guaranteed value", 105000, "$M", "L-061", "confirmed", "T1",
        "2026-08-17", "issuer S-1; nothing payable until ready-for-service", "STABLE", "09, 10, 11")
    row("LB09_RVG_GW", "RVG covered capacity (initial)", 4.25, "GW-IT", "L-061", "confirmed", "T1", "2026-08-17", "issuer S-1", "STABLE", "09", nf=CNT2)
    row("LB09_Milam_MW", "SB Energy Milam County leases (two buildings)", 753, "MW", "L-061, L-147", "confirmed", "T1", "2026-09-01", "issuer S-1", "STABLE", "09", nf=CNT)
    row("LB09_Milam_term", "Milam County lease term", 15, "yrs", "L-061", "confirmed", "T1", "2026-09-01", "issuer S-1", "STABLE", "09", nf=CNT)
    row("LB10", "Anthropic 2028 revenue forecast to IPO investors, low end", 190000, "$M", "L-036", "estimated", "T2", "FY2028E (Aug-2026 vintage)",
        "company forecast to IPO investors, GROSS presumed", "QUARTERLY", "02, 09, 07", name="LB10")
    row("LB10_high", "Anthropic 2028 revenue forecast to IPO investors, high end", 200000, "$M", "L-036", "estimated", "T2", "FY2028E (Aug-2026 vintage)",
        "company forecast to IPO investors, GROSS presumed", "QUARTERLY", "02, 09, 07")

    sec("MARKS, RULINGS AND THE JUL-16 REGISTER")
    row("M01", "Anthropic post-money mark (Series H)", 965000, "$M", "L-005, L-038", "confirmed", "T2/T1", "2026-05-28", "Series H post", "VOLATILE", "06")
    row("M02", "OpenAI post-money mark (Mar-2026 round; Aug-10 tender at the same price)", 852000, "$M", "L-019, L-067", "confirmed", "T2",
        "2026-03-31", "Mar-2026 round post", "VOLATILE", "06")
    row("R01", "Equalization haircut, internal (Ruling 5)", 0.3975, "fraction", "L-126", "recalled", "T4", "2026-07-16", "Ruling 5; gate-verified on the May-2026 mix",
        "PERMANENT", "02, 05, 06, 11 (via SW_HAIRCUT)", nf=PCT2)
    row("R02", "Equalization haircut, external (~27%)", 0.27, "fraction", "L-126, C-13", "recalled", "T4", "2026-04",
        "OpenAI CRO memo relay, adversarial", "STABLE", "same", nf=PCT2)
    row("R03", "Microsoft share applied if the OpenAI figure is gross (T4 only; NEVER printed as a fact)", 0.20, "fraction", "L-052 notes", "recalled",
        "T4", "n/a", "T4 only; gross case of SW_OAI_BASIS", "STABLE", "02 (gross case only)", nf=PCT, yellow=True)
    row("J16_OAI_RR", "OpenAI run-rate carried in the Jul-16 register (CE walk start)", 25000, "$M/yr", "L-133", "recalled", "T4", "2026-07-16",
        "NET run-rate, register", "PERMANENT", "05 (CE walk)")
    row("J16_CE_A", "Anthropic CE at Jul-16 (register)", 0.228, "x", "L-133", "recalled", "T4", "2026-07-16", "equalized net run-rate / equity", "PERMANENT", "05", nf=MULT3)
    row("J16_CE_O", "OpenAI CE at Jul-16 (register)", 0.138, "x", "L-133", "recalled", "T4", "2026-07-16", "net run-rate / equity", "PERMANENT", "05", nf=MULT3)

    sec("ANTHROPIC: REVENUE, PLAN, MARGINS, PEOPLE, FACILITIES")
    row("A01a", "Anthropic run-rate, end-2025", 9000, "$M/yr", "L-139", "confirmed", "T1", "2025-12", "GROSS run-rate, company statement", "QUARTERLY", "02")
    row("A01b", "Anthropic run-rate, 2026-04-06", 30000, "$M/yr", "L-139", "confirmed", "T1", "2026-04-06", "GROSS run-rate, company statement", "QUARTERLY", "02")
    row("A01c", "Anthropic run-rate, early May 2026 (Series H announcement)", 47000, "$M/yr", "L-037", "confirmed", "T1", "2026-05", "GROSS run-rate, company statement", "QUARTERLY", "02, 05")
    row("A02_low", "Anthropic YE-2026 run-rate expectation, low", 100000, "$M/yr", "L-035", "estimated", "T3", "2026-08-17",
        "investor expectation, not guidance (FT via TechCrunch)", "QUARTERLY", "00, 02")
    row("A02_high", "Anthropic YE-2026 run-rate expectation, high", 120000, "$M/yr", "L-035", "estimated", "T3", "2026-08-17",
        "investor expectation, not guidance", "QUARTERLY", "00, 02")
    for y, v in ((2022, 10), (2023, 100), (2024, 1000), (2025, 10000), (2026, 65000), (2027, 71000)):
        basis = "PB recognized-estimate (basis unstated)" if y <= 2025 else "PB FORWARD PROJECTION (Ruling 4), never current"
        row(f"A04_{y}", f"Anthropic PB revenue series, {y}", v, "$M", "L-010, L-009", "estimated", "T2", "pulled 2026-09-09", basis, "n/a", "02 (projection block only)")
    row("A05_rev", "Anthropic FY2024 revenue", 1000, "$M", "L-012", "estimated", "T2", "FY2024", "PB deal-record financials", "QUARTERLY", "04")
    row("A05_NI", "Anthropic FY2024 net loss (Sep-9 PB vintage)", -8300, "$M", "L-012", "estimated", "T2", "FY2024", "PB deal-record financials (C-05)", "QUARTERLY", "04 (SW_A_FY24_NI)")
    row("A05_NI_alt", "Anthropic FY2024 net loss (Jul-16 PB vintage)", -5300, "$M", "L-012, C-05", "recalled", "T4", "FY2024", "PB financials, Jul-16 register (C-05)", "QUARTERLY", "04 (SW_A_FY24_NI)")
    row("A06", "Anthropic FY2025 revenue, PB TTM 4Q2025 field", 10000, "$M", "L-010", "estimated", "T2", "FY2025", "PB field = December exit run-rate (C-03)", "QUARTERLY", "04 (SW_A_FY25)")
    row("A06_impl_low", "Anthropic FY2025 recognized revenue implied by the Jan-2026 guidance, low", 4500, "$M", "L-120", "recalled", "T4", "FY2025", "implied (C-03)", "QUARTERLY", "04 (SW_A_FY25)")
    row("A06_impl_high", "Anthropic FY2025 recognized revenue implied by the Jan-2026 guidance, high", 6000, "$M", "L-120", "recalled", "T4", "FY2025", "implied (C-03)", "QUARTERLY", "04 (SW_A_FY25)")
    for k, lab, v in (("A07_2024", "Anthropic gross margin 2024", -0.94), ("A07_2025", "Anthropic gross margin 2025", 0.40),
                      ("A07_2026_low", "Anthropic gross margin 2026 (T4 range, low)", 0.44), ("A07_2026_high", "Anthropic gross margin 2026 (T4 range, high)", 0.60),
                      ("A07_2027", "Anthropic gross margin plan 2027E", 0.63), ("A07_2028", "Anthropic gross margin plan 2028E", 0.77)):
        row(k, lab, v, "fraction", "L-119", "recalled", "T4", "2026-01 vintage", "The Information relay; register; GROSS-basis margin", "QUARTERLY", "00, 03, 04, 07", nf=PCT)
    for y, v in ((2026, 7000), (2027, 14000), (2028, 22000)):
        row(f"A08_{y}", f"Anthropic training-compute budget {y}E", v, "$M/yr", "L-125", "recalled", "T4", "undated leaked docs", "annual training-compute budget (C-11)", "STABLE", "00, 03, 04, 09")
    for k, lab, v in (("A09_rev2026", "Anthropic Jan-2026 plan: revenue 2026", 18000), ("A09_rev2027", "Anthropic Jan-2026 plan: revenue 2027", 55000),
                      ("A09_rev2028", "Anthropic Jan-2026 plan: revenue 2028", 102000), ("A09_rev2029", "Anthropic Jan-2026 plan: revenue 2029", 148000),
                      ("A09_loss2026", "Anthropic Jan-2026 plan: loss 2026 (GAAP-style)", -11000), ("A09_loss2027", "Anthropic Jan-2026 plan: loss 2027", -11000),
                      ("A09_rentals", "Anthropic Jan-2026 plan: server rentals through 2029", 180000), ("A09_burn2025", "Anthropic FY2025 burn (register)", 5600)):
        row(k, lab, v, "$M", "L-120", "recalled", "T4", "2026-01", "superseded plan; C-12", "QUARTERLY", "05, 12, 13")
    row("A10", "Anthropic headcount (PB)", 5000, "people", "L-008", "confirmed", "T2", "2026-04-21", "PB profile; C-18", "QUARTERLY", "03 (SW_A_HC)", nf=CNT)
    row("A10_alt", "Anthropic headcount (Revelio)", 4020, "people", "L-091", "estimated", "T4", "2026-03", "LinkedIn-derived; C-18", "QUARTERLY", "03 (SW_A_HC)", nf=CNT)
    row("A11", "Anthropic revolving credit facility", 2500, "$M", "L-014", "confirmed", "T2", "2025-05-16", "debt facility (in PB Total Raised; not equity)", "STABLE", "05")
    row("A11_exp", "Anthropic revolver expansion 'set to finalize'", 15000, "$M", "L-042", "estimated", "T3", "2026-09-03", "Bloomberg relay; not closed", "STABLE once closed", "05 (SW_15B_FACILITY)")
    row("A22", "$15B facility closing status", "NOT closed as of 2026-09-09 ('set to finalize' Sep-3; PB deal still Upcoming)", "status", "L-160",
        "could-not-verify", "T3", "2026-09-09", "house rule: [VERIFY] until closed", "STABLE once closed", "05, 11 (SW_15B_FACILITY default)", nf=GEN, yellow=True)
    row("A12", "TPU lease SPV ('AI XPV Platform'): lessor debt financing TPU systems leased to Anthropic", 34500, "$M", "L-044", "estimated", "T3", "2026-06",
        "lessor debt, off-balance-sheet; 5-yr lease", "STABLE", "09, 10, 05")
    row("A12_bcom", "SPV tranche with Broadcom support", 30000, "$M", "L-044", "estimated", "T3", "2026-06", "lessor debt", "STABLE", "10")
    row("A12_unsup", "SPV tranche without support", 4500, "$M", "L-044", "estimated", "T3", "2026-06", "lessor debt", "STABLE", "10")
    row("A12_term", "SPV lease term", 5, "yrs", "L-044", "estimated", "T3", "2026-06", "five-year lease", "STABLE", "09, 10", nf=CNT)
    row("A12_GW", "SPV-financed TPU capacity ('more than 1 GW')", 1, "GW", "L-044", "estimated", "T3", "2026-06", "floor", "STABLE", "09 (X01)", nf=CNT2)
    row("A12_A1", "SPV tranche A1 rate", "Treasuries + 1pt", "text", "L-044, L-106", "estimated", "T3 / T1", "2026-08-12", "Epoch AI", "STABLE", "10", nf=GEN)
    row("A12_A2", "SPV tranche A2 rate", 0.0575, "fraction", "L-044, L-106", "estimated", "T3 / T1", "2026-08-12", "Epoch AI", "STABLE", "10", nf=PCT2)
    row("A12_B", "SPV tranche B rate", 0.085, "fraction", "L-044, L-106", "estimated", "T3 / T1", "2026-08-12", "Epoch AI", "STABLE", "10", nf=PCT2)
    row("A13", "Project-company debt, five TPU site companies", 15200, "$M", "L-045", "estimated", "T3", "2026-08-12", "off-balance-sheet; Google conditional support", "STABLE", "09, 10")
    row("A13_GW", "Project-company critical IT capacity", 1.43, "GW", "L-045", "estimated", "T3", "2026-08-12", "Epoch AI", "STABLE", "09, 10", nf=CNT2)
    row("A14", "Copyright: Bartz settlement (final approval 2026-07-20)", 1500, "$M", "L-086", "confirmed", "T2", "2026-07-20", "cash 2026", "STABLE", "03 (L5)")
    row("A14_music", "Copyright: music-publisher demands ('>3,000'), unreserved", 3000, "$M", "L-086", "confirmed", "T2", "2026-01-29", "unreserved claims; Sony/Warner Chappell suit unquantified", "STABLE", "03")
    for k, lab, v, rid, st, tr, basis in (("A15a", "MTS base salary, high (H-1B)", 1.38, "L-165", "estimated", "T3", "base only (verbatim relay)"),
                                          ("A15b", "MTS base salary (H-1B)", 1.12, "L-165", "estimated", "T3", "base only (verbatim relay)"),
                                          ("A15c", "MTS base range, low", 0.134, "L-165", "estimated", "T3", "base only"),
                                          ("A15d", "MTS Manager base, to", 0.85, "L-165", "estimated", "T3", "base only"),
                                          ("A15e", "Technical Sales base, to", 0.50, "L-165", "estimated", "T3", "base only"),
                                          ("A15f", "Product Design Manager base, to", 0.385, "L-165", "estimated", "T3", "base only"),
                                          ("A15h", "Engineer total-comp band, low (aggregators)", 0.30, "L-092 notes", "estimated", "T4", "total comp (T4)"),
                                          ("A15i", "Engineer total-comp band, high (aggregators)", 0.76, "L-092 notes", "estimated", "T4", "total comp (T4)")):
        row(k, f"Anthropic comp anchor: {lab}", v, "$M/yr", rid, st, tr, "2026-06-28", basis, "QUARTERLY", "00, 03 (L5, AJ)", nf=CNT3)
    row("A15g", "Anthropic H-1B roles certified H1 FY2026", 80, "roles", "L-165", "estimated", "T3", "2026-06-28", "verbatim relay", "QUARTERLY", "03", nf=CNT)
    row("A16", "Series H raised", 65000, "$M", "L-038", "confirmed", "T1", "2026-05-28", "company statement", "STABLE", "05")
    row("A16_prior", "Series H: previously committed hyperscaler money included", 15000, "$M", "L-038", "confirmed", "T1", "2026-05-28", "company statement", "STABLE", "05")
    row("A16_amzn", "Series H: of which Amazon", 5000, "$M", "L-038", "confirmed", "T1", "2026-05-28", "company statement", "STABLE", "05")
    row("A17_amzn", "Contingent equity inflow: Amazon (milestone-based)", 20000, "$M", "L-072", "confirmed", "T1", "2026-04-20", "up to; not in capital raised", "STABLE", "05, 09")
    row("A17_goog", "Contingent equity inflow: Google (performance targets)", 30000, "$M", "L-073", "confirmed", "T2", "2026-04-24", "contingent; not in capital raised", "STABLE", "05, 09")
    row("A17_amd", "Contingent equity inflow: AMD (through FY2028)", 5000, "$M", "L-043", "confirmed", "T1", "2026-07-22", "up to; subject to contingencies", "STABLE", "05, 09")
    for k, lab, v in (("A18_f51_in", "Fable 5.1 input", 10), ("A18_f51_out", "Fable 5.1 output", 50), ("A18_o5_in", "Opus 5 input", 5), ("A18_o5_out", "Opus 5 output", 25),
                      ("A18_s5_in", "Sonnet 5 input", 2), ("A18_s5_out", "Sonnet 5 output", 10), ("A18_h45_in", "Haiku 4.5 input", 1), ("A18_h45_out", "Haiku 4.5 output", 5),
                      ("A18_fast", "Fast Mode multiplier (Opus 5)", 2), ("A18_cache", "Cache read (Fable 5.1)", 0.25)):
        row(k, f"List price: {lab}", v, "$ per MTok", "L-084", "confirmed", "T1", "2026-09-09", "pricing page", "VOLATILE", "03 (unit economics block)", nf=CNT2)
    row("A19a", "Anthropic compute cost per revenue dollar, Q1-2026", 0.71, "ratio", "L-152", "estimated", "T4", "Q1-2026", "T4 relay; display and cross-check only, never a driver", "QUARTERLY", "03, 11", nf=CNT2, yellow=True)
    row("A19b", "Anthropic compute cost per revenue dollar, Q2-2026 (projected)", 0.56, "ratio", "L-152", "estimated", "T4", "Q2-2026", "T4 relay; display and cross-check only, never a driver", "QUARTERLY", "03, 11", nf=CNT2, yellow=True)
    row("A20", "Google Cloud commitment, REPORTED value over five years [VERIFY]", 200000, "$M", "L-155", "estimated", "T3 [VERIFY]", "2026-05-05",
        "The Information via Reuters; page not opened; filings silent (L-153, L-154, L-156); never in documented-$", "STABLE", "09 (SW_GOOGLE_VALUE branch only)", yellow=True)
    row("A20_yrs", "Google Cloud reported commitment, term", 5, "yrs", "L-155", "estimated", "T3 [VERIFY]", "2026-05-05", "'over five years'", "STABLE", "09", nf=CNT, yellow=True)
    row("A21a", "Alphabet 10-Q (Q2-2026): mentions of Anthropic", 0, "count", "L-153", "confirmed", "T1", "2026-06-30", "disclosure check (silence)", "STABLE", "09, 13", nf=CNT)
    row("A21b", "Alphabet 10-Q: total purchase commitments and other contractual obligations", 811000, "$M", "L-153", "confirmed", "T1", "2026-06-30", "not itemized", "STABLE", "09, 13")
    row("A21c", "Alphabet 10-Q: of which short-term", 200700, "$M", "L-153", "confirmed", "T1", "2026-06-30", "not itemized", "STABLE", "09, 13")
    row("A21d", "Google Cloud release (2026-04-06): dollar value / take-or-pay", "none stated ('multiple gigawatts'; no $; no take-or-pay)", "text", "L-154", "confirmed", "T1", "2026-04-06", "disclosure check (silence)", "STABLE", "09, 13", nf=GEN)
    row("A21e", "Broadcom 10-Q (Q2 FY2026): top-five end customers share of revenue", 0.45, "fraction", "L-156", "confirmed", "T1", "2026-05-03", "no customer commitment named", "STABLE", "09, 13", nf=PCT)
    row("A21f", "Microsoft 10-K FY2026: revenue-share percentage / 250,000 Azure figure", "no percentage; no 250,000 (full-text check)", "text", "L-157", "confirmed", "T1", "2026-06-30", "disclosure check (silence)", "STABLE", "09, 13", nf=GEN)
    rounds_a = (("ANT_R01", "Series A", 124, "2021-05-28", "L-018"), ("ANT_R02", "Series B", 980, "2022-04-29", "L-018"), ("ANT_R03", "Series C", 450, "2023-06-30", "L-018"),
                ("ANT_R04", "Alphabet convertible-to-equity", 2000, "2023-10-27", "L-018"), ("ANT_R05", "Series D", 1200, "2024-07-01", "L-018"),
                ("ANT_R06", "Amazon round (incl. 1,300 convertible)", 8000, "2024-11-22", "L-018"), ("ANT_R07", "Series E", 3500, "2025-03-03", "L-018"),
                ("ANT_R08", "Series F (incl. 750 convertible)", 13000, "2025-09-02", "L-017"), ("ANT_R09", "Series G", 30000, "2026-02-12", "L-016"),
                ("ANT_R10", "Series H", 65000, "2026-05-28", "L-015"))
    for k, lab, v, d, rid in rounds_a:
        row(k, f"Anthropic equity round: {lab}", v, "$M", rid, "confirmed", "T2", d, "PitchBook deal record, Total Invested Equity", "STABLE", "05")
    row("PB_TOTAL_A", "Anthropic PB Total Raised (net capital injected)", 126754, "$M", "L-006", "confirmed", "T2", "2026-09-08", "PB profile; equity + revolver; SPV removed (C-01)", "STABLE", "05 (identity check)")

    sec("OPENAI: REVENUE, LOSSES, PLANS, PEOPLE, DEBT, MICROSOFT")
    row("O01", "OpenAI FY2025 revenue", 13100, "$M", "L-063", "confirmed", "T2", "FY2025", "NET presumed; FT-verified 13,070", "STABLE", "02, 04")
    row("O02_oploss", "OpenAI FY2025 operating loss (magnitude)", 20920, "$M loss", "L-025/L-026 notes", "recalled", "T3", "FY2025", "FT-verified leak", "STABLE", "04")
    row("O02_group", "OpenAI FY2025 group loss incl. fair-value swing (magnitude)", 60350, "$M loss", "L-025/L-026 notes", "recalled", "T3", "FY2025", "FT-verified leak", "STABLE", "04")
    row("O02_fv", "OpenAI FY2025 fair-value swing inside the group loss", 41550, "$M", "L-025/L-026 notes", "recalled", "T3", "FY2025", "FT-verified leak", "STABLE", "04")
    row("O03", "OpenAI end-2025 run-rate ('>20,000')", 20000, "$M/yr", "L-065", "confirmed", "T2", "2025-12", "Bloomberg relay; basis unstated", "QUARTERLY", "02")
    row("O03b", "OpenAI monthly revenue at the March-2026 round", 2000, "$M/month", "L-063", "confirmed", "T2", "2026-03", "WSJ; ~2,000 per month", "QUARTERLY", "02")
    row("O03c", "OpenAI run-rate growth quarter-to-date (CFO, Aug-19)", "+35% QTD; enterprise +50%", "text", "L-069", "confirmed", "T2", "2026-08-19", "all-hands relay (colour)", "QUARTERLY", "02", nf=GEN)
    for y, v in ((2023, 2000), (2024, 6000), (2025, 20000), (2026, 41300)):
        basis = {2023: "PB series (basis unstated)", 2024: "PB series (basis unstated)", 2025: "run-rate vintage, not recognized (C-06)", 2026: "PB FORWARD PROJECTION (Ruling 4)"}[y]
        row(f"O04_{y}", f"OpenAI PB revenue series, {y}", v, "$M", "L-025, L-024", "estimated", "T2", "pulled 2026-09-09", basis, "n/a", "02 (projection block only)")
    row("O04_NI2024", "OpenAI FY2024 net income (PB deal record)", -5000, "$M", "L-026", "estimated", "T4", "FY2024", "PB deal-record financials (T4)", "n/a", "02 (projection block only)")
    row("O04_NI2026", "OpenAI FY2026 net income projection (PB deal record)", -14000, "$M", "L-026", "estimated", "T4", "FY2026E", "PB projection (T4)", "n/a", "02 (projection block only)")
    for k, lab, v, asof in (("O05_b26feb", "OpenAI burn plan 2026 (Feb vintage)", 25000, "2026-02-21"), ("O05_b26apr", "OpenAI burn plan 2026 (post-April vintage)", 27000, "2026"),
                            ("O05_b27feb", "OpenAI burn plan 2027 (Feb vintage)", 57000, "2026-02-21"), ("O05_b27apr", "OpenAI burn plan 2027 (post-April vintage)", 63000, "2026"),
                            ("O05_cf2030", "OpenAI 2030 positive cash flow (Feb vintage plan)", 39000, "2026-02-21"), ("O05_cash25", "OpenAI cash at end-2025 (~)", 40000, "2025-12")):
        row(k, lab, v, "$M", "L-082", "estimated", "T3", asof, "The Information relay; cash basis", "QUARTERLY", "05, 07")
    row("O05_q1burn", "OpenAI Q1-2026 cash burn", 3700, "$M", "L-142", "estimated", "T3", "Q1-2026", "The Information headline", "QUARTERLY", "05")
    for y, v in ((2026, 25000), (2027, 60000), (2028, 112000), (2029, 120000)):
        row(f"O06_{y}", f"OpenAI training budget {y}E", v, "$M/yr", "L-125", "recalled", "T4", "undated", "annual training budget (C-11)", "STABLE", "00, 03, 04")
    row("O07_inf2025", "OpenAI inference cost 2025", 8400, "$M", "L-083", "estimated", "T3", "2025", "Sacra", "QUARTERLY", "03, 04, 11")
    row("O07_inf2026", "OpenAI inference cost 2026E", 14100, "$M", "L-083", "estimated", "T3", "2026E", "Sacra projection", "QUARTERLY", "03, 04, 11")
    row("O07_gm2025", "OpenAI gross margin 2025", 0.33, "fraction", "L-083", "estimated", "T3", "2025", "Sacra", "QUARTERLY", "03, 04, 11", nf=PCT)
    row("O07_gmplan", "OpenAI gross margin plan (missed)", 0.46, "fraction", "L-083 notes", "estimated", "T4", "2025 plan", "Sacra / register", "QUARTERLY", "13", nf=PCT)
    row("O08", "OpenAI headcount (PB)", 4500, "people", "L-027", "confirmed", "T2", "2026-03-21", "PB profile", "QUARTERLY", "03 (L5)", nf=CNT)
    row("O08_plan", "OpenAI headcount plan, end-2026", 8000, "people", "L-090", "estimated", "T3", "2026-03-22", "Semafor", "QUARTERLY", "03 (L5)", nf=CNT)
    row("O09_pp", "OpenAI retention bonus per person (~)", 1.5, "$M", "L-093, L-166", "estimated / could-not-verify", "T3", "2025-08", "The Information relay; verbatim not reachable (403)", "STABLE", "03 (L5)", nf=CNT2)
    row("O09_n", "OpenAI retention bonus recipients (~)", 1000, "people", "L-093, L-166", "estimated / could-not-verify", "T3", "2025-08", "The Information relay", "STABLE", "03 (L5)", nf=CNT)
    row("O09_yrs", "OpenAI retention bonus payout period", 2, "yrs", "L-093, L-166", "estimated / could-not-verify", "T3", "2025-08", "paid quarterly over two years", "STABLE", "03 (L5)", nf=CNT)
    row("O09_eng", "OpenAI retention structure (engineers 0.2-0.6; key researchers 'mid-single-digit millions')", "engineers 0.2-0.6; researchers mid-single-digit millions", "text", "L-166", "could-not-verify", "T3", "2025-08-07", "search-level relays", "STABLE", "03", nf=GEN, yellow=True)
    row("O10_a", "OpenAI revolver (Oct-2024)", 4000, "$M", "L-023", "confirmed", "T2", "2024-10-03", "unsecured revolver", "STABLE", "05")
    row("O10_b", "OpenAI revolver inside the Mar-2026 round", 700, "$M", "L-023", "confirmed", "T2", "2026-03-31", "debt", "STABLE", "05")
    row("O10_c", "OpenAI term loan (Jul-2026)", 520, "$M", "L-023", "confirmed", "T2", "2026-07-08", "term loan", "STABLE", "05")
    row("O10", "OpenAI debt stack (sum)", f"={R('O10_a')}+{R('O10_b')}+{R('O10_c')}", "$M", "L-023", "confirmed", "T2", "2026-07-08", "derived: 4,000 + 700 + 520", "STABLE", "05")
    row("PB_TOTAL_O", "OpenAI PB Total Raised", 186436.5, "$M", "L-021", "confirmed", "T2", "2026-09-08", "PB profile", "STABLE", "05 (identity check)", nf=NUM1)
    row("O11_cap", "Microsoft revenue-share cap (cumulative through 2030)", 38000, "$M", "L-052", "estimated", "T3", "2026-05-11", "single-outlet (The Information via Reuters)", "STABLE", "09, 10")
    row("O11_stake", "Microsoft stake in OpenAI at the Oct-2025 recap (~27%)", 0.27, "fraction", "L-159", "confirmed", "T2", "2025-10-28", "TechCrunch verbatim; post-dilution decreased, undisclosed (C-19)", "STABLE", "09, 10", nf=PCT)
    row("O11_stake_val", "Microsoft stake value at the recap (~)", 135000, "$M", "L-159", "confirmed", "T2", "2025-10-28", "TechCrunch verbatim", "STABLE", "09, 10")
    row("O11_found", "OpenAI Foundation stake at the recap", 0.26, "fraction", "L-159", "confirmed", "T2", "2025-10-28", "TechCrunch verbatim", "STABLE", "09", nf=PCT)
    row("O11_inv", "Investors and employees at the recap", 0.47, "fraction", "L-159", "confirmed", "T2", "2025-10-28", "TechCrunch verbatim", "STABLE", "09", nf=PCT)
    row("O11_RPO", "Microsoft commercial RPO", 678000, "$M", "L-055", "confirmed", "T1", "2026-06-30", "Q4 FY26 call", "STABLE", "09, 10")
    row("O11_RPO_ex", "Microsoft RPO growth excluding OpenAI", 0.25, "fraction", "L-055", "confirmed", "T1", "2026-06-30", "Q4 FY26 call", "STABLE", "09", nf=PCT)
    row("O11_pct", "Microsoft revenue-share percentage", "not in the 10-K; Bloomberg full text states no basis for the >40,000 (T4 20% never printed as a fact)", "text", "L-051, L-157, L-158",
        "confirmed / could-not-verify", "T1 / T2", "2026-04-27 / 2026-06-30 / 2026-08-13", "official post, 10-K, Bloomberg", "STABLE", "09, 10", nf=GEN)
    row("O13_commit", "Microsoft total funding commitments to OpenAI", 13000, "$M", "L-157", "confirmed", "T1", "2026-06-30", "10-K equity-method note", "STABLE", "05 (note), 09, 10")
    row("O13_funded", "Microsoft funding commitments funded at 2026-06-30", 11900, "$M", "L-157", "confirmed", "T1", "2026-06-30", "10-K equity-method note (= PB 1,000 + 2,000 + 10,000 less 1,100 unfunded)", "STABLE", "05 (note), 09, 10")
    row("O12_users", "OpenAI active users", "more than 1 billion active users", "text", "L-080", "confirmed", "T2", "2026-07-31", "company statement (AFP)", "QUARTERLY", "03 (context)", nf=GEN)
    row("O12_biz", "OpenAI business customers", "more than 2 million businesses", "text", "L-080", "confirmed", "T2", "2026-07-31", "company statement", "QUARTERLY", "03 (context)", nf=GEN)
    row("O12_ads", "OpenAI advertising run-rate", 1000, "$M/yr", "L-081", "confirmed", "T2", "2026-08-31", "Digiday", "QUARTERLY", "03 (context)")
    rounds_o = (("OAI_R01", "Microsoft (Jul-2019)", 1000, "2019-07"), ("OAI_R02", "Series A", 10, "n/a"), ("OAI_R03", "Jul-2021 round", 2000, "2021-07"),
                ("OAI_R04", "Microsoft (Jan-2023; paid over multiple years)", 10000, "2023-01"), ("OAI_R05", "Apr-2023 round", 300, "2023-04"),
                ("OAI_R06", "Series B (Oct-2024)", 6600, "2024-10-02"), ("OAI_R07", "Series F (Mar-2025)", 40000, "2025-03-31"),
                ("OAI_R08", "Jan-2025 round", 6.5, "2025-01"), ("OAI_R09", "Mar-2026 round, equity portion", 121300, "2026-03-31"))
    for k, lab, v, d in rounds_o:
        row(k, f"OpenAI equity round: {lab}", v, "$M", "L-022", "estimated", "T2", d, "PitchBook deal records (sum of equity rounds)", "STABLE", "05", nf=NUM1)

    sec("CONTRACT ANCHORS (C01-C22): totals, terms, GW; the 09_Obligations schedule links these cells")
    row("C01_tot", "A-AWS: commitment to AWS over ten years ('>100,000')", 100000, "$M", "L-072", "confirmed", "T1", "2026-04-20", "company statement; take-or-pay not disclosed", "STABLE", "09")
    row("C01_term", "A-AWS: term", 10, "yrs", "L-072", "confirmed", "T1", "2026-04-20", "'over the next ten years'", "STABLE", "09", nf=CNT)
    row("C01_GW", "A-AWS: capacity ('up to 5 GW')", 5, "GW", "L-072", "confirmed", "T1", "2026-04-20", "company statement", "STABLE", "09", nf=CNT2)
    row("C02_tot", "A-Azure: purchase commitment", 30000, "$M", "L-074", "confirmed", "T1", "2025-11-18", "company statement; term not stated (AJ 5 yrs)", "STABLE", "09")
    row("C02_GW", "A-Azure: capacity ('up to 1 GW')", 1, "GW", "L-074", "confirmed", "T1", "2025-11-18", "company statement", "STABLE", "09", nf=CNT2)
    row("C03_monthly", "A-SpaceX: monthly fee", 1250, "$M/month", "L-046", "confirmed", "T1", "2026-05-03", "SpaceX S-1; through May-2029; reduced fee May-Jun 2026", "STABLE", "09")
    row("C03_end", "A-SpaceX: last month of the fee", D(2029, 5, 31), "date", "L-046", "confirmed", "T1", "2026-05-03", "'through May 2029'", "STABLE", "09", nf=DATEF)
    row("C03_notice_m", "A-SpaceX: termination notice (90 days = 3 months)", 3, "months", "L-046", "confirmed", "T1", "2026-05-03", "either party, 90 days' notice", "STABLE", "09", nf=CNT)
    row("C04_tot", "A-Fluidstack: $50B US datacenter build (spend commitment, not a customer contract)", 50000, "$M", "L-076, L-168", "confirmed", "T1", "2025-11-12", "phasing 'throughout 2026' only; no $ or GW schedule", "STABLE", "09")
    row("C04_phasing", "A-Fluidstack: phasing", "HOLE: 'throughout 2026' only (L-168); excluded from the annual priced run", "text", "L-168", "confirmed", "T1", "2025-11-12", "partner statement", "STABLE", "09", nf=GEN, yellow=True)
    row("C05_tot", "A-Nscale: compute deal", 45000, "$M", "L-135", "confirmed", "T2", "2026-08-26", "'~45,000 over six years'; capacity from late-2027", "STABLE", "09")
    row("C05_term", "A-Nscale: term", 6, "yrs", "L-135", "confirmed", "T2", "2026-08-26", "six years", "STABLE", "09", nf=CNT)
    row("C05_MW", "A-Nscale: capacity (T3/T4 relay)", 460, "MW", "L-135", "estimated", "T3", "2026-08-26", "Forbes/search summaries", "STABLE", "09", nf=CNT)
    row("C06_tot", "A-Lambda: compute deal", 35000, "$M", "L-137", "confirmed", "T2", "2026-08-31", "term not stated (AJ 6 yrs, flagged)", "STABLE", "09")
    row("C06_MW", "A-Lambda: capacity (T4 relay)", 350, "MW", "L-137", "estimated", "T4", "2026-08-31", "relay", "STABLE", "09", nf=CNT)
    row("C06_LL_term", "Beacon Point landlord lease term (Hut 8; tenant Nvidia)", 15, "yrs", "L-167", "confirmed", "T1", "2026-07-20", "landlord-level lease, not the Anthropic-Lambda term", "STABLE", "09, 10", nf=CNT)
    row("C06_LL_MW", "Beacon Point tenant contracted capacity", 704, "MW", "L-167", "confirmed", "T1", "2026-07-20", "Hut 8 release", "STABLE", "09, 10", nf=CNT)
    row("C06_LL_val", "Beacon Point campus base-term contract value", 19600, "$M", "L-167", "confirmed", "T1", "2026-07-20", "Hut 8 release", "STABLE", "09, 10")
    row("C06_LL_renew", "Beacon Point contract value with renewals", 50200, "$M", "L-167", "confirmed", "T1", "2026-07-20", "Hut 8 release", "STABLE", "10")
    row("C07_tot", "A-Volta: compute deal (Norway)", 10000, "$M", "L-048", "estimated", "T3", "2026-08-04", "'reportedly'; single chain", "STABLE", "09")
    row("C07_term", "A-Volta: term", 6, "yrs", "L-048", "estimated", "T3", "2026-08-04", "six years", "STABLE", "09", nf=CNT)
    row("C07_MW", "A-Volta: capacity", 133, "MW", "L-048", "estimated", "T3", "2026-08-04", "Tydal, Norway", "STABLE", "09", nf=CNT)
    row("C08_tot", "A-Riot: powered-shell lease (through June 2048)", 9100, "$M", "L-136", "confirmed", "T2", "2026-08-10", "Bloomberg; 20-yr lease", "STABLE", "09")
    row("C08_term", "A-Riot: term", 20, "yrs", "L-136", "confirmed", "T2", "2026-08-10", "20 years through June 2048", "STABLE", "09", nf=CNT)
    row("C08_MW", "A-Riot: capacity", 191, "MW", "L-136", "confirmed", "T2", "2026-08-10", "Rockdale, Texas", "STABLE", "09", nf=CNT)
    row("C08_ext", "A-Riot: total with two 5-yr extensions", 16100, "$M", "L-136", "confirmed", "T2", "2026-08-10", "options", "STABLE", "09")
    row("C10_GW", "A-Google Cloud: capacity over five years ('5 GW'; $ undisclosed)", 5, "GW", "L-073", "confirmed", "T2", "2026-04-06", "TechCrunch; Google release says 'multiple gigawatts' (L-154)", "STABLE", "09", nf=CNT2)
    row("X02_a26", "Broadcom schedule, Anthropic: Ironwood deploying 2026", 1, "GW", "L-049", "confirmed", "T1", "2026-09-02", "vendor call; sits inside the SPV", "STABLE", "09", nf=CNT2)
    row("X02_a27", "Broadcom schedule, Anthropic: TPU v8i 2027 (contracted tranche)", 5, "GW", "L-049", "confirmed", "T1", "2026-09-02", "vendor call", "STABLE", "09, 12", nf=CNT2)
    row("X02_a28", "Broadcom schedule, Anthropic: 2028 'line of sight' (vendor guidance, not contract)", 10, "GW", "L-049", "confirmed", "T1", "2026-09-02", "vendor call", "STABLE", "09, 12", nf=CNT2)
    row("X02_o27", "Broadcom schedule, OpenAI: Jalapeno 2027", 1.3, "GW", "L-050", "confirmed", "T1", "2026-09-02", "vendor call", "STABLE", "09", nf=CNT2)
    row("X02_o28", "Broadcom schedule, OpenAI: 2028 ('>5 GW')", 5, "GW", "L-050", "confirmed", "T1", "2026-09-02", "vendor call", "STABLE", "09", nf=CNT2)
    row("C11_GW", "A-AMD: capacity ('up to 2 GW' MI450; first GW from H1-2027; $ undisclosed)", 2, "GW", "L-043", "confirmed", "T1", "2026-07-22", "AMD release / 10-Q", "STABLE", "09", nf=CNT2)
    row("C12_tot", "O-Oracle: cloud contract from 2027 (press)", 300000, "$M", "L-064", "estimated", "T2", "2026-07-22", "WSJ; Oracle discloses only RPO (L-056)", "STABLE", "09")
    row("C12_term", "O-Oracle: term", 5, "yrs", "L-064", "estimated", "T2", "2026-07-22", "five years from 2027", "STABLE", "09", nf=CNT)
    row("C12_GW", "O-Oracle: capacity (~)", 4.5, "GW", "L-064", "estimated", "T2", "2026-07-22", "press", "STABLE", "09", nf=CNT2)
    row("ORCL_RPO", "Oracle total RPO at 2026-05-31 (T1 upper bound)", 638000, "$M", "L-056", "confirmed", "T1", "2026-05-31", "10-K; OpenAI not named", "STABLE", "09")
    row("C13_base", "O-AWS: original agreement", 38000, "$M", "L-064", "estimated", "T2", "2026-07-22", "press", "STABLE", "09")
    row("C13_exp", "O-AWS: expansion ('up to' 100,000 over eight years)", 100000, "$M", "L-064", "estimated", "T2/T4", "2026-08-01", "press; 'up to' language", "STABLE", "09")
    row("C13_tot", "O-AWS: combined (derived)", f"={R('C13_base')}+{R('C13_exp')}", "$M", "L-064", "estimated", "T2/T4", "2026-08-01", "derived: 38,000 + 100,000", "STABLE", "09")
    row("C13_term", "O-AWS: term", 8, "yrs", "L-064", "estimated", "T2/T4", "2026-08-01", "eight years", "STABLE", "09", nf=CNT)
    row("C13_GW", "O-AWS: Trainium capacity (~)", 2, "GW", "L-064", "estimated", "T4", "2026-08-01", "press", "STABLE", "09", nf=CNT2)
    row("C14_tot", "O-CoreWeave: cumulative agreements (press)", 22400, "$M", "L-058", "confirmed", "T1 (tranche) / T4 (total)", "2026-06-30", "10-Q names the 6,500 order form; 22,400 cumulative per press", "STABLE", "09")
    row("C14_T1", "O-CoreWeave: Sept-2025 order form (T1 tranche, through 2031-05-31)", 6500, "$M", "L-058", "confirmed", "T1", "2026-06-30", "10-Q", "STABLE", "09")
    row("C14_end", "O-CoreWeave: end of the order form", D(2031, 5, 31), "date", "L-058", "confirmed", "T1", "2026-06-30", "10-Q", "STABLE", "09", nf=DATEF)
    row("C15_tot", "O-Cerebras: multi-year deal ('more than 20,000')", 20000, "$M", "L-149", "confirmed", "T1", "2026-05-11", "S-1/A", "STABLE", "09")
    row("C15_term", "O-Cerebras: tranche terms (3-4 yrs; AJ 4)", 4, "yrs", "L-149", "confirmed", "T1", "2026-05-11", "S-1/A", "STABLE", "09", nf=CNT)
    row("C15_MW", "O-Cerebras: committed capacity", 750, "MW", "L-149", "confirmed", "T1", "2026-05-11", "tranches 2026-2028", "STABLE", "09", nf=CNT)
    row("C15_opt_GW", "O-Cerebras: option for additional capacity by end-2030", 1.25, "GW", "L-149", "confirmed", "T1", "2026-05-11", "option (flag OPTION)", "STABLE", "09", nf=CNT2)
    row("C15_loan", "O-Cerebras: working-capital loan advanced BY OpenAI", 1000, "$M", "L-149", "confirmed", "T1", "2026-05-11", "a use of cash", "STABLE", "09")
    row("C19_GW", "O-AMD: capacity ('up to 6 GW'; first GW on MI450)", 6, "GW", "L-060", "confirmed", "T1", "Oct-2025", "AMD 10-Q; warrant 160M shares at $0.01", "STABLE", "09", nf=CNT2)
    row("C21_LOI", "O-Nvidia: LOI (Sep-2025), RETIRED", 100000, "$M", "L-075", "confirmed", "T2", "2026-03-04", "Huang: remaining ~70,000 'probably not in the cards'", "STABLE", "09")
    row("C21_equity", "O-Nvidia: equity invested in the Mar-2026 round (inflow, not cost)", 30000, "$M", "L-075", "confirmed", "T2", "2026-03-04", "financing inflow", "STABLE", "09, 10")
    row("C22_GW", "O-Stargate: planned US capacity ('>9 GW'; overlaps Oracle / SB Energy rows)", 9, "GW", "L-079", "estimated", "T3", "2026-04-17", "Epoch AI; excluded from sums", "STABLE", "09", nf=CNT2)
    row("SPCX_AI_Q2", "SpaceX AI-segment Q2-2026 revenue (upper bound on Anthropic's cash paid to SpaceX in the quarter)", 2560, "$M", "L-047", "confirmed", "T2", "Q2-2026", "SpaceX Q2 results; reduced fee May-June", "QUARTERLY", "09 (E6 cash column)")

    sec("TALLY-ONLY VALUES (could-not-verify; flagged CNV; used ONLY by the 09_Obligations recalled-$ block, never as facts)")
    row("C16_cnv", "O-Azure: incremental Azure commitment (register value)", 250000, "$M", "L-121", "could-not-verify", "T4", "2025-10-28",
        "10-K silent; primaries 403; recalled-$ scope only", "STABLE", "09 (tally, CNV)", yellow=True)
    row("C19_cnv", "O-AMD: dollar value (press estimate)", 90000, "$M", "L-123", "could-not-verify", "T4", "2025-10", "AMD 10-Q states no $; recalled-$ scope only", "STABLE", "09 (tally, CNV)", yellow=True)
    row("C20_cnv", "O-Broadcom: dollar value ('350,000 / 10 GW', press estimate)", 350000, "$M", "L-122", "could-not-verify", "T4", "2025-10", "Broadcom states no $; recalled-$ scope only", "STABLE", "09 (tally, CNV)", yellow=True)
    row("T_young", "youngresearch tally ('517,000', not reproducible)", 517000, "$M", "L-138", "estimated", "T4", "2026-08-31", "not reproducible from ledger rows; CUT", "VOLATILE", "09 (tally display)", yellow=True)
    row("T_register", "Register tally ('80B+ across 6 partners', superseded)", 80000, "$M", "L-138", "recalled", "T4", "2026-06-12", "pre-dates Riot, Volta, Nscale, Lambda; CUT", "VOLATILE", "09 (tally display)", yellow=True)
    row("T_oblig", "OpenAI obligation stack (register canonical, 'through ~2035')", 1150000, "$M", "L-062 notes", "recalled", "T4", "2026-02-27", "reconciles as 480,400 documented-$ + 690,000 recalled-$", "STABLE", "09 (tally)", yellow=True)
    row("T_headline", "OpenAI headline 'infrastructure commitments' (Altman)", 1400000, "$M", "L-062", "estimated", "T2 relay", "2026", "includes optional and aspirational capacity", "STABLE", "09 (tally)")

    sec("FINANCING LADDER ANCHORS (F01-F10) AND LEASE ECONOMICS (X01)")
    row("F_neo1", "CoreWeave 2031 senior notes coupon", 0.09, "fraction", "L-059", "confirmed", "T1", "2026-06-30", "10-Q", "STABLE", "10", nf=PCT2)
    row("F_neo2", "CoreWeave 2031 senior notes coupon (second)", 0.0975, "fraction", "L-059", "confirmed", "T1", "2026-06-30", "10-Q", "STABLE", "10", nf=PCT2)
    row("F_neo3", "CoreWeave 2032 senior notes coupon", 0.09625, "fraction", "L-059", "confirmed", "T1", "2026-06-30", "10-Q", "STABLE", "10", nf=PCT2)
    row("F_cs_tot", "Core Scientific-AMD: base contracted revenue ('>14,000')", 14000, "$M", "L-148", "confirmed", "T1", "2026-07-28", "Q2 call; 2.5% escalators", "STABLE", "10, 09")
    row("F_cs_MW", "Core Scientific-AMD: capacity", 530, "MW", "L-148", "confirmed", "T1", "2026-07-28", "five sites", "STABLE", "10", nf=CNT)
    row("F_cs_term", "Core Scientific-AMD: term", 15, "yrs", "L-148", "confirmed", "T1", "2026-07-28", "15-year agreements", "STABLE", "10", nf=CNT)
    row("F_amd_guar", "AMD datacenter lease guarantees (max)", 4100, "$M", "L-146", "confirmed", "T1", "2026-06-27", "AMD 10-Q", "STABLE", "10")
    row("F_amd_lease", "AMD new long-term DC leases (up to 16 yrs)", 9500, "$M", "L-146", "confirmed", "T1", "2026-06-27", "AMD 10-Q", "STABLE", "10")
    row("F_sbe_warrant", "SB Energy warrant fair-value charge (H1-2026)", 2573, "$M", "L-147", "confirmed", "T1", "2026-06-30", "S-1", "STABLE", "10")
    row("F_msft_gain", "Microsoft FY2026 net gains from OpenAI investments (recap dilution gain)", 6500, "$M", "L-054", "confirmed", "T1", "FY2026", "10-K", "STABLE", "10")
    row("F_msft_capex", "Microsoft CY2026 capex expectation", 175000, "$M", "L-145", "confirmed", "T1", "2026-07-29", "Q4 FY26 call", "QUARTERLY", "10, 13")
    row("F_meta_lo", "Meta 2026 capex guidance, low", 125000, "$M", "L-095", "confirmed", "T2", "2026-04-29", "Fortune", "QUARTERLY", "10, 13")
    row("F_meta_hi", "Meta 2026 capex guidance, high", 145000, "$M", "L-095", "confirmed", "T2", "2026-04-29", "Fortune", "QUARTERLY", "10, 13")
    row("F_w_amd", "Warrant to OpenAI: AMD shares (M) at $0.01", 160, "M shares", "L-060", "confirmed", "T1", "Oct-2025", "AMD 10-Q", "STABLE", "10", nf=CNT1)
    row("F_w_sbe", "Warrant to OpenAI: SB Energy shares (M) at $0.01", 3.991809, "M shares", "L-061", "confirmed", "T1", "2026-08-17", "S-1", "STABLE", "10", nf=CNT2)
    row("F_w_cer", "Warrant to OpenAI: Cerebras Class N shares (M)", 33.445026, "M shares", "L-149", "confirmed", "T1", "2026-05-11", "S-1/A", "STABLE", "10", nf=CNT2)
    row("F_huang", "Huang statement on vendor equity", "the 30,000 OpenAI investment 'might be the last time'; the 100,000 LOI 'probably not in the cards'", "text", "L-075", "confirmed", "T2", "2026-03-04", "TechCrunch / Benzinga", "STABLE", "10", nf=GEN)
    row("X01_nscale", "Full-stack lease rate: Nscale (45,000 / 460 MW / 6 yr)", f"={R('C05_tot')}/{R('C05_MW')}/{R('C05_term')}", "$M per MW-yr", "L-134, L-135", "estimated", "T3 (derived)", "2026-08", "derived", "VOLATILE", "09, 12, 07", nf=CNT2)
    row("X01_volta", "Full-stack lease rate: Volta (10,000 / 133 MW / 6 yr)", f"={R('C07_tot')}/{R('C07_MW')}/{R('C07_term')}", "$M per MW-yr", "L-134, L-048", "estimated", "T3 (derived)", "2026-08", "derived", "VOLATILE", "09, 12, 07", nf=CNT2)
    row("X01_riot", "Powered-shell rate: Riot (9,100 / 191 MW / 20 yr)", f"={R('C08_tot')}/{R('C08_MW')}/{R('C08_term')}", "$M per MW-yr", "L-136", "confirmed", "T2 (derived)", "2026-08-10", "derived", "VOLATILE", "09, 12, 10", nf=CNT2)
    row("X01_beacon", "Powered-shell rate: Hut 8 Beacon Point (19,600 / 704 MW / 15 yr)", f"={R('C06_LL_val')}/{R('C06_LL_MW')}/{R('C06_LL_term')}", "$M per MW-yr", "L-167", "confirmed", "T1 (derived)", "2026-07-20", "derived; tenant Nvidia", "VOLATILE", "10, 09", nf=CNT2)
    row("X01_cs", "Powered-shell rate: Core Scientific-AMD (14,000 / 530 MW / 15 yr)", f"={R('F_cs_tot')}/{R('F_cs_MW')}/{R('F_cs_term')}", "$M per MW-yr", "L-148", "confirmed", "T1 (derived)", "2026-07-28", "derived", "VOLATILE", "10", nf=CNT2)
    row("X01_spv", "Chips-only rate: TPU SPV (34,500 / 1,000 MW / 5 yr)", f"={R('A12')}/({R('A12_GW')}*1000)/{R('A12_term')}", "$M per MW-yr", "L-044", "estimated", "T3 (derived)", "2026-08-12", "derived; 1 GW = 1,000 MW", "VOLATILE", "09, 12", nf=CNT2)
    row("X01_tpu_69", "SW_TPU_RATE branch: 6.9 (chips only, shell inside AWS/other)", f"=ROUND({R('X01_spv')},1)", "$M per MW-yr", "L-044", "estimated", "T3 (derived)", "2026-08-12", "rounded to one decimal as the spec states it", "VOLATILE", "12", nf=CNT1)
    row("X01_tpu_93", "SW_TPU_RATE branch: 9.3 (SPV chips 6.9 + Riot shell 2.4)", f"=ROUND({R('X01_spv')},1)+ROUND({R('X01_riot')},1)", "$M per MW-yr", "L-044, L-136", "estimated", "T3 (derived)", "2026-08", "rounded components as the cost-stack states them", "VOLATILE", "12", nf=CNT1)
    row("X01_tpu_125", "SW_TPU_RATE branch: 12.5 (Volta full-stack)", f"=ROUND({R('X01_volta')},1)", "$M per MW-yr", "L-134", "estimated", "T3 (derived)", "2026-08", "rounded", "VOLATILE", "12", nf=CNT1)
    row("X01_tpu_163", "SW_TPU_RATE branch: 16.3 (Nscale full-stack)", f"=ROUND({R('X01_nscale')},1)", "$M per MW-yr", "L-134", "estimated", "T3 (derived)", "2026-08", "rounded", "VOLATILE", "12", nf=CNT1)
    row("X01_goog5", "Google reported value implied rate at 5 GW (200,000 / 5 yr / 5,000 MW)", f"={R('A20')}/{R('A20_yrs')}/({R('C10_GW')}*1000)", "$M per MW-yr", "L-155, L-073", "estimated", "T3 [VERIFY]", "2026-05-05", "consistency check", "VOLATILE", "09", nf=CNT2, yellow=True)
    row("X01_goog16", "Google reported value implied rate at 16 GW (1 + 5 + 10 line of sight)", f"={R('A20')}/{R('A20_yrs')}/(({R('X02_a26')}+{R('X02_a27')}+{R('X02_a28')})*1000)", "$M per MW-yr", "L-155, L-049", "estimated", "T3 [VERIFY]", "2026-05-05", "consistency check", "VOLATILE", "09", nf=CNT2, yellow=True)

    sec("PER-RUN REFERENCE (L-115), INDUSTRY REFERENCE (X03), OUTSIDE-VIEW ANCHORS")
    for k, lab, v in (("X04_grok4", "Grok 4 final run (~)", 500), ("X04_gpt45", "GPT-4.5 pre-training (~)", 200), ("X04_gpt45_post", "GPT-4.5 post-training (~)", 2),
                      ("X04_gpt4", "GPT-4 (~)", 78), ("X04_gemini", "Gemini Ultra (~)", 191), ("X04_llama", "Llama 3.1-405B (~)", 170)):
        row(k, f"Per-run compute cost: {lab}", v, "$M", "L-115", "estimated", "T3", "2024-06-03 / 2025-09-26", "Epoch AI; final-run amortized compute (different basis from annual budgets, C-11); never summed with L3", "STABLE", "03 (reference block)")
    row("X04_growth", "Per-run cost growth since 2016", 2.4, "x per yr", "L-115", "estimated", "T3", "2024-06-03", "Epoch AI", "STABLE", "03", nf=CNT1)
    row("X04_1b", "Largest runs '> 1,000 by 2027'", 1000, "$M", "L-115", "estimated", "T3", "2024-06-03", "Epoch AI", "STABLE", "03")
    row("BCOM_26", "Broadcom AI semiconductor revenue FY2026 (~)", 58000, "$M", "L-144", "confirmed", "T1", "2026-09-02", "vendor guidance", "QUARTERLY", "13")
    row("BCOM_27", "Broadcom AI semiconductor revenue FY2027 (supply secured)", 115000, "$M", "L-144", "confirmed", "T1", "2026-09-02", "vendor guidance", "QUARTERLY", "13")
    row("BCOM_28", "Broadcom AI semiconductor revenue FY2028 (line of sight)", 230000, "$M", "L-144", "confirmed", "T1", "2026-09-02", "vendor guidance", "QUARTERLY", "13")
    row("CW_build", "All-in greenfield datacenter build cost", 17.6, "$M per MW", "L-109", "confirmed", "T2", "2026-09-03", "Cushman & Wakefield 2026 guide", "STABLE", "13", nf=CNT1)
    row("CW_infl", "Build cost inflation since Q4-2024", 0.21, "fraction", "L-109", "confirmed", "T2", "2026-09-03", "Cushman & Wakefield", "STABLE", "13", nf=PCT)
    row("GPU_new_lo", "H100 new price, low", 25000, "$", "L-103", "estimated", "T4", "2026-07-10", "GPU price index", "VOLATILE", "13", nf=CNT)
    row("GPU_new_hi", "H100 new price, high", 40000, "$", "L-103", "estimated", "T4", "2026-07-10", "GPU price index", "VOLATILE", "13", nf=CNT)
    row("GPU_used_lo", "H100 used price, low", 8200, "$", "L-103", "estimated", "T4", "2026-07-10", "GPU price index", "VOLATILE", "13", nf=CNT)
    row("GPU_used_hi", "H100 used price, high", 25000, "$", "L-103", "estimated", "T4", "2026-07-10", "GPU price index", "VOLATILE", "13", nf=CNT)
    row("MSFT_life_old", "Microsoft datacenter useful life, before", 15, "yrs", "L-145", "confirmed", "T1", "2026-07-29", "Q4 FY26 call", "STABLE", "13", nf=CNT)
    row("MSFT_life_new", "Microsoft datacenter useful life, after", 25, "yrs", "L-145", "confirmed", "T1", "2026-07-29", "Q4 FY26 call", "STABLE", "13", nf=CNT)
    row("ABIL_op", "Abilene operational capacity", 0.3, "GW", "L-079", "estimated", "T3", "2026-04-17", "Epoch AI", "QUARTERLY", "13", nf=CNT2)
    row("ABIL_plan", "Abilene planned (capped from 2.1)", 1.2, "GW", "L-079", "estimated", "T3", "2026-04-17", "Epoch AI", "QUARTERLY", "13", nf=CNT2)
    row("ABIL_orig", "Abilene original plan", 2.1, "GW", "L-079 notes", "estimated", "T4", "2026-03-09", "Winbuzzer (T4)", "QUARTERLY", "13", nf=CNT2)
    row("CHATGPT_late", "ChatGPT 1B-user milestone lateness vs projection", 7, "months", "L-080", "confirmed", "T2", "2026-07-29", "The Information via PYMNTS", "QUARTERLY", "13", nf=CNT)
    row("PB_move_A", "PB Anthropic FY2027 projection move, Jul-16 to Sep-9 (55,000 to 71,000)", f"={R('A04_2027')}/55000-1", "fraction", "L-009", "estimated", "T2", "2026-09-09", "derived; Jul-16 field was 55,000", "QUARTERLY", "13", nf=PCT)
    row("PB_move_O", "PB OpenAI FY2026 projection move, Jul-16 to Sep-9 (30,000 to 41,300)", f"={R('O04_2026')}/30000-1", "fraction", "L-024", "estimated", "T2", "2026-09-09", "derived; Jul-16 field was 30,000", "QUARTERLY", "13", nf=PCT)

    sec("AIBQ v3.0 INPUTS (Q01-Q18): weights, May-27 sub-scores (L-133), Sep-9 re-run sub-scores (aibq-delta.md)")
    for k, lab, v in (("Q_wCE1", "CE-1 weight", 0.40), ("Q_wCE2", "CE-2 weight", 0.25), ("Q_wCE3", "CE-3 weight", 0.20), ("Q_wCE4", "CE-4 weight", 0.15),
                      ("Q_wCI1", "CI-1 weight", 0.30), ("Q_wCI2", "CI-2 weight", 0.25), ("Q_wCI3", "CI-3 weight", 0.20), ("Q_wCI4", "CI-4 weight", 0.15), ("Q_wCI5", "CI-5 weight", 0.10),
                      ("Q_wCEdim", "CE dimension weight (Report configuration, Ruling 6)", 0.20), ("Q_wCIdim", "CI dimension weight (Report configuration)", 0.15)):
        row(k, f"AIBQ rubric: {lab}", v, "weight", "L-133 (rubric v3.0)", "recalled", "T4", "2026-05-26", "rubric v3.0; Report weights CE 20 / RQ 25 / CI 15 / GO 20 / MD 20", "PERMANENT (method)", "11", nf=PCT)
    for k, lab, v in (("Q_A_CE1_old", "Anthropic CE-1 (May-27)", 10.0), ("Q_A_CE2_old", "Anthropic CE-2 (May-27)", 4.0), ("Q_A_CE3_old", "Anthropic CE-3 (May-27)", 9.0), ("Q_A_CE4_old", "Anthropic CE-4 (May-27)", 8.0),
                      ("Q_A_CI1_old", "Anthropic CI-1 (May-27)", 6.0), ("Q_A_CI2_old", "Anthropic CI-2 (May-27)", 4.0), ("Q_A_CI3_old", "Anthropic CI-3 (May-27)", 5.0), ("Q_A_CI4_old", "Anthropic CI-4 (May-27)", 5.0), ("Q_A_CI5_old", "Anthropic CI-5 (May-27)", 5.0),
                      ("Q_O_CE1_old", "OpenAI CE-1 (May-27)", 3.0), ("Q_O_CE2_old", "OpenAI CE-2 (May-27)", 3.5), ("Q_O_CE3_old", "OpenAI CE-3 (May-27)", 3.0), ("Q_O_CE4_old", "OpenAI CE-4 (May-27)", 2.5),
                      ("Q_O_CI1_old", "OpenAI CI-1 (May-27)", 5.5), ("Q_O_CI2_old", "OpenAI CI-2 (May-27)", 3.0), ("Q_O_CI3_old", "OpenAI CI-3 (May-27)", 4.0), ("Q_O_CI4_old", "OpenAI CI-4 (May-27)", 6.0), ("Q_O_CI5_old", "OpenAI CI-5 (May-27)", 4.0),
                      ("Q_A_CI_canon", "Anthropic CI canonical (after the un-decomposed SpaceX revision)", 5.8),
                      ("AIBQ_OLD_A", "Anthropic composite (May-27, canonical)", 8.20), ("AIBQ_OLD_O", "OpenAI composite (May-27, canonical)", 4.53)):
        row(k, f"AIBQ prior: {lab}", v, "score", "L-133", "recalled", "T4", "2026-05-27", "May-27 vintage (prior/v4-reconstruction section 7)", "PERMANENT (method)", "11, 06", nf=DEC2)
    for k, lab, v in (("Q_A_CE1_new", "Anthropic CE-1 (Sep-9)", 8.0), ("Q_A_CE2_new", "Anthropic CE-2 (Sep-9)", 5.0), ("Q_A_CE3_new", "Anthropic CE-3 (Sep-9)", 9.0),
                      ("Q_A_CE4_dnc", "Anthropic CE-4 (Sep-9), facility does NOT close (default)", 7.5), ("Q_A_CE4_closes", "Anthropic CE-4 (Sep-9), facility closes", 7.0),
                      ("Q_A_CI1_new", "Anthropic CI-1 (Sep-9)", 7.0), ("Q_A_CI2_new", "Anthropic CI-2 (Sep-9)", 5.0), ("Q_A_CI3_new", "Anthropic CI-3 (Sep-9)", 4.0), ("Q_A_CI4_new", "Anthropic CI-4 (Sep-9)", 6.0), ("Q_A_CI5_new", "Anthropic CI-5 (Sep-9)", 5.0),
                      ("Q_O_CE1_net", "OpenAI CE-1 (Sep-9), NET basis", 5.0), ("Q_O_CE1_gross", "OpenAI CE-1 (Sep-9), GROSS case (C-16)", 4.0), ("Q_O_CE2_new", "OpenAI CE-2 (Sep-9)", 3.5), ("Q_O_CE3_new", "OpenAI CE-3 (Sep-9)", 3.0), ("Q_O_CE4_new", "OpenAI CE-4 (Sep-9)", 3.0),
                      ("Q_O_CI1_new", "OpenAI CI-1 (Sep-9)", 6.0), ("Q_O_CI2_new", "OpenAI CI-2 (Sep-9)", 6.0), ("Q_O_CI3_new", "OpenAI CI-3 (Sep-9)", 4.0), ("Q_O_CI4_new", "OpenAI CI-4 (Sep-9)", 7.0), ("Q_O_CI5_new", "OpenAI CI-5 (Sep-9)", 4.5)):
        row(k, f"AIBQ re-run: {lab}", v, "score", "aibq-delta.md sections 1-4", "derived (AJ on rubric v3.0)", "T4", "2026-09-09", "Analyst re-run on the Sep-9 ledger; rubric bands in 11_AIBQ", "PERMANENT (method)", "11", nf=DEC2, yellow=True)
    row("EI_growth", "Efficiency Index input: min(growth/100, 1.0), both labs", 1.0, "fraction", "aibq-delta.md section 1, 3", "derived", "T4", "2026-09-09", "growth >100% capped at 1.0", "PERMANENT (method)", "11", nf=DEC2, yellow=True)
    row("EI_fcf", "Efficiency Index input: min(FCF/Rev, 0.30), both labs (no TTM FCF+; Ruling 3)", 0.0, "fraction", "aibq-delta.md section 1", "derived", "T4", "2026-09-09", "unswept", "PERMANENT (method)", "11", nf=DEC2, yellow=True)
    row("EI_gm_A", "Efficiency Index input: Anthropic GM (lower edge of 50-65% net basis)", 0.50, "fraction", "aibq-delta.md section 1", "derived", "T4", "2026-09-09", "rubric input", "PERMANENT (method)", "11", nf=DEC2, yellow=True)
    row("EI_gm_O", "Efficiency Index input: OpenAI GM", f"={R('O07_gm2025')}", "fraction", "L-083", "estimated", "T3", "2025", "Sacra 33%", "PERMANENT (method)", "11", nf=DEC2)
    for k, lab, v in (("EI_w1", "Efficiency Index weight on growth", 0.4), ("EI_w2", "Efficiency Index weight on FCF", 0.3), ("EI_w3", "Efficiency Index weight on GM", 0.3)):
        row(k, lab, v, "weight", "rubric v3.0 (S5)", "recalled", "T4", "2026-05-26", "Index = min(growth/100,1)*0.4 + min(FCF/Rev,0.3)*0.3 + GM*0.3", "PERMANENT (method)", "11", nf=PCT)
    row("Q_flag", "AIBQ flag threshold: sub-score delta at or above this is flagged (composite threshold 0.1)", 0.5, "score", "rubric v3.0", "recalled", "T4", "2026-05-26", "flag rule (aibq-delta.md)", "PERMANENT (method)", "11", nf=DEC2)

    sec("BASE RATES (B01-B03) AND IPO STATUS (I01)")
    row("B01_priv", "Growth endurance, private cloud companies (next year's growth = 0.7 x this year's)", 0.70, "fraction", "L-161", "estimated", "T3", "2021-09-21",
        "Bessemer; SaaS dataset, not consumption-billed labs", "PERMANENT", "00 (2029E-2030E tails), 13", nf=PCT)
    row("B01_pub", "Growth endurance, public cloud companies", 0.80, "fraction", "L-161", "estimated", "T3", "2021-09-21", "Bessemer; SaaS dataset", "PERMANENT", "00, 13", nf=PCT)
    for y, v in ((2014, 0.099), (2015, 0.191), (2016, 0.254), (2017, 0.248), (2018, 0.284), (2019, 0.263), (2020, 0.298), (2021, 0.298), (2022, 0.285), (2023, 0.271), (2024, 0.370), (2025, 0.354)):
        row(f"B02_{y}", f"AWS operating margin FY{y}", v, "fraction", "L-162", "confirmed", "T1", f"FY{y}", "Amazon 10-K segment tables; OPERATING margin, not gross margin", "PERMANENT", "13", nf=PCT)
    row("B03_stepup", "IPO colour: median step-up at listing (Q2-2026)", 1.3, "x", "L-163", "could-not-verify", "T2 (colour)", "2026-08-10", "PB Q2-2026 US VC Valuations", "STABLE", "13", nf=MULT)
    row("B03_cerebras", "IPO colour: Cerebras cancel -> refile -> price (~months)", 9, "months", "L-163", "could-not-verify", "T2 (colour)", "2026-08-10", "one documented frontier-adjacent case", "STABLE", "13", nf=CNT)
    row("B03_status", "IPO timing base rate", "no filed-to-priced or withdrawal statistic available (PB none; Renaissance paywall; SEC counts only): analyst judgment", "text", "L-163", "could-not-verify", "T2 (colour)", "2026-08-10", "status", "STABLE", "13", nf=GEN, yellow=True)
    row("I01_edgar", "Public S-1 status, both labs (EDGAR)", "no public S-1 for either as of 2026-09-09", "status", "L-001, L-002", "confirmed", "T1", "2026-09-09", "EDGAR full-text and company browse", "VOLATILE", "08, 12", nf=GEN)
    row("I01_a_conf", "Anthropic confidential S-1 submission", "2026-06-01", "date", "L-039", "confirmed", "T1", "2026-06-01", "company statement", "STABLE", "08, 12", nf=GEN)
    row("I01_a_exp", "Anthropic expected IPO window (PB)", "October 2026", "date", "L-003", "confirmed", "T2", "2026-09-04", "PB financing note", "VOLATILE", "08, 12", nf=GEN)
    row("I01_a_press", "Anthropic reported timetable (press)", "mid-October 2026 reported (Forbes headline); late Sep / early Oct (The Information)", "date", "L-040", "estimated", "T3", "2026-09-07", "press", "VOLATILE", "08, 12", nf=GEN)
    row("I01_o_conf", "OpenAI confidential S-1 submission", "2026-06-08", "date", "L-004", "confirmed", "T2", "2026-07-09", "PB financing note", "STABLE", "08, 12", nf=GEN)
    row("I01_o_cfo", "OpenAI IPO timing (CFO to employees)", "'will be a public company in 2027', possibly sooner", "date", "L-068", "confirmed", "T2", "2026-08-19", "CNBC", "VOLATILE", "08, 12", nf=GEN)
    row("I01_o_pb", "OpenAI expected IPO window (PB, stale)", "September 2026 (note dated 2026-07-09; retired by L-002 and the 15-day rule)", "date", "L-004", "estimated", "T3", "2026-07-09", "PB financing note, stale", "VOLATILE", "12", nf=GEN)

    sec("WORKBOOK B MIRROR (SW_SSI branches)")
    row("SSI_pb", "SSI total raised (PB)", 7000, "$M", "L-097", "confirmed", "T2", "2026-07-28", "PB profile; C-08", "STABLE", "12 (SW_SSI), B/08_Reference")
    row("SSI_press", "SSI total raised (press tallies)", 8000, "$M", "L-097, C-08", "estimated", "T2/T4", "2026-07-28", "press; C-08", "STABLE", "12 (SW_SSI), B/08_Reference")
    sh.put(f"A{r+1}", "End of 01_Data.", kind="note")
    sh.ws.freeze_panes = "D4"
    return r


# ----------------------------------------------------------------------------------------------------
# 00_Assumptions
# ----------------------------------------------------------------------------------------------------
LAYERS = [
    ("L1", "Silicon", "Chip-vendor counterparties: Nvidia, AMD, Broadcom, Google (TPU as chip via SPV), Cerebras; chip-lease SPVs; custom-silicon programs",
     "Chip purchases, chip-lease SPV obligations, GW-denominated chip agreements, ASIC programs, warrants issued to chip vendors", "contracted $, GW"),
    ("L2", "Capacity", "Cloud, neocloud, site and power counterparties: AWS, Google Cloud, Azure, Oracle, CoreWeave, SpaceX, Nscale, Lambda, Volta, Riot, Fluidstack, SB Energy",
     "Cloud consumption contracts, full-stack GPU leases, powered-shell leases, site leases, PPAs, network and storage inside those leases", "contracted $, GW/MW, $ per MW-year"),
    ("L3", "Training", "Annual compute consumed by training, experiments and post-training (R&D compute)",
     "Annual training-compute budgets; per-run compute estimates are a different basis (C-11) and are shown side by side, never summed", "$ per year"),
    ("L4", "Inference", "Annual compute consumed by serving (COGS); on Anthropic's GROSS basis this line also carries cloud-partner payouts",
     "Inference COGS, gross margin, $ per million tokens", "$ per year, %"),
    ("L5", "People and everything else", "All other annual opex", "Comp and SBC, data licensing and labeling, safety and evals, legal and regulatory, GTM, G&A", "$ per year"),
]
SEED_PLACEMENT = [
    "Placement rule: Layers 1-2 hold COMMITMENTS (what is contracted or leased, in $ and GW, by counterparty type). Layers 3-5 hold CONSUMPTION (what the P&L absorbs in a year). A figure is placed by its nature: a contract value goes to L1 or L2 exactly once; an annual spend goes to L3, L4 or L5 exactly once. The obligation stack (09_Obligations) is the cross-layer object that reconciles L1+L2 commitments against L3+L4 consumption and against cash.",
    "Seed placement, Anthropic: AWS >$100B/5 GW -> L2. Google 5 GW -> L2 (cloud counterparty); the $34.5B TPU lease SPV -> L1 (chip financing). Azure $30B -> L2. SpaceX $1.25B/mo -> L2. AMD 2 GW -> L1. Broadcom TPU schedule -> L1 (GW; $ undisclosed). Fluidstack $50B -> L2. Nscale/Lambda/Volta/Riot -> L2. Training plan $7B/$14B/$22B -> L3. GM path -> L4. List prices -> L4 (unit economics). Comp -> L5. Copyright -> L5.",
    "Seed placement, OpenAI: Oracle $300B -> L2. CoreWeave -> L2. Azure -> L2. AWS -> L2. AMD 6 GW -> L1. Nvidia -> L1 (the $30B equity is financing, not cost; the $105B RVG is a vendor backstop on an L2 lease). Broadcom -> L1. Cerebras -> L1 (chip-vendor counterparty delivering capacity). SB Energy leases and Stargate sites -> L2. 2026 compute $50B -> consumption anchor spanning L3+L4 (printed once, in L3, with the split shown). Training plan -> L3. GM and inference -> L4. Comp and headcount -> L5. Legal -> L5.",
    "Source: analysis/cost-stack-reconciliation.md section 1 (v5 adopts the reconstructed five-layer definition with the placement rule the reconstruction lacked). This block is Exhibit E2.",
]


def build_00(sh):
    sh.put("A1", "00_Assumptions: timeline (row 2 numeric, row 3 labels), scenario switch SW_SCEN (C4), AJ drivers (yellow, Bear/Base/Bull, live column G via CHOOSE), the printed 5-Layer definition (A40:F60), contract timing, grid axes, time-series drivers.", kind="note")
    sh.put("A2", "Year (numeric, typed once)", bold=True)
    sh.put("D2", 2023, kind="input", nf=GEN, key="YR|2023", align="center")
    for y in YEARS[1:]:
        prev = YC[y - 1]
        sh.put(f"{YC[y]}2", f"={prev}2+1", kind="formula", nf=GEN, key=f"YR|{y}", align="center")
    sh.put("A3", "Timeline label (text; every tab links here)", bold=True)
    for y in YEARS:
        sfx = '"A"' if y <= 2025 else '"E"'
        sh.put(f"{YC[y]}3", f"={YC[y]}2&{sfx}", kind="formula", bold=True, align="center", key=f"YL|{y}", border=B_TB)
    sh.put("B4", "Scenario switch SW_SCEN (1 Bear / 2 Base / 3 Bull)", bold=True)
    sh.put("C4", 2, kind="input", nf=GEN, name="SW_SCEN", key="SW_SCEN", align="center")
    sh.put("D4", '=CHOOSE(SW_SCEN,"Bear","Base","Bull")', kind="formula", bold=True, key="SCEN_LABEL")
    sh.put("E4", "Google leg and TPU rate are switches on 12_Conflicts (SW_GOOGLE_VALUE, SW_TPU_RATE, SW_GW_2028); the section-4 scenario mapping (Bear proxy 16.3 / Base reported / Bull proxy 6.9) is applied by setting those switches, printed in row 122.", kind="note")

    sh.header(6, ["AJ driver (scalar)", "Unit", "Tag (AJ · basis · Bear/Base/Bull)", "Bear", "Base", "Bull", "Live (SW_SCEN)", "Note"])
    r = 7
    d = lambda key, label, unit, tag, bear, base, bull, nf=NUM, note=None, hole=False: driver(sh, key_row[key], key, label, unit, tag, bear, base, bull, nf, None, note, hole)
    order = ["YE26", "REV27", "REV28", "ENDUR", "TRNF", "TRN29", "TRN30", "GM29", "OPEXQ2", "COMPA", "HCGA", "DATAA", "EXPA", "SAFA", "GTMA", "AZTERM",
             "LAMTERM", "RAMP", "OAIG", "OAICAGR", "OAIPLAN", "OAIOPEX", "OAITRN30", "OAICOGS0", "OAICOGSD", "OAIHCG", "COMPO", "SBCP", "ENV27LO", "ENV27HI", "HCUTMID", "CEREBTERM"]
    key_row = {k: 7 + i for i, k in enumerate(order)}
    d("YE26", "Anthropic YE-2026 run-rate (linear monthly ramp from July; Bear = flat from July)", "$M/yr", "AJ · L-035 investor expectation (T3), L-032 July (T2) · Bear/Base/Bull",
      f"={R('LB01')}", f"=AVERAGE({R('A02_low')},{R('A02_high')})", f"={R('A02_high')}", note="Bear = LB01 flat; Base = midpoint of L-035; Bull = L-035 high")
    d("REV27", "Anthropic 2027E revenue", "$M", "AJ · interpolation between L-035 and L-036, no row · Bear/Base/Bull", 120000, 145000, 160000, note="Bull 160,000 keeps the Bull path monotone (addendum)")
    d("REV28", "Anthropic 2028E revenue", "$M", "AJ · L-036 low end at Base (T2); Bear = AJ shortfall; Bull = AJ beat · Bear/Base/Bull", 150000, f"={R('LB10')}", 220000)
    d("ENDUR", "Bessemer growth endurance applied to the 2028 growth rate (2029E-2030E tails)", "fraction", "AJ · B01 (L-161, T3, SaaS caveat): 0.70 private (Bear, Base), 0.80 public post-IPO (Bull)",
      f"={R('B01_priv')}", f"={R('B01_priv')}", f"={R('B01_pub')}", nf=PCT)
    d("TRNF", "Anthropic training factor on the 2026-2028 plan (L-125)", "x plan", "AJ · plan plus 25% / plan / plan less 15% · Bear/Base/Bull", 1.25, 1.00, 0.85, nf=DEC2)
    d("TRN29", "Anthropic training 2029E", "$M/yr", "AJ · no ledger row (v4 map carried 30,000); range 25,000-40,000 · Bear/Base/Bull", 40000, 30000, 25000)
    d("TRN30", "Anthropic training 2030E", "$M/yr", "AJ · no ledger row; range 25,000-50,000 · Bear/Base/Bull", 40000, 30000, 25000)
    d("GM29", "Anthropic GM 2029E-2030E", "fraction", "AJ · beyond the L-119 plan horizon · Bear/Base/Bull", 0.65, 0.72, 0.77, nf=PCT)
    d("OPEXQ2", "Anthropic quarterly opex Q2-2026 (GM cross-check grid rows)", "$M", "AJ · opex ex-COGS, no row · Bear/Base/Bull", 3000, 4000, 5000)
    d("COMPA", "Anthropic average loaded cash comp per head", "$M/yr", "AJ · anchored by L-165 MTS base 1.12-1.38 and T4 bands 0.30-0.76 · Bear/Base/Bull", 0.75, 0.60, 0.50, nf=CNT2)
    d("HCGA", "Anthropic headcount growth 2027E+ (HOLE: cost-stack section 2 L5 2027E+ 'headcount growth x comp, AJ')", "fraction", "HOLE · Model-agent placeholder triple, no spec value · Bear/Base/Bull", 0.30, 0.25, 0.20, nf=PCT, hole=True,
      note="No spec or ledger value; placeholder so the L5 line computes; listed in tie-out.md")
    d("DATAA", "Anthropic data licensing", "$M/yr", "AJ · L-113 (T1): marquee sources ~50-70 each; total at most low single-digit $B · Bear/Base/Bull", 1500, 1000, 500)
    d("EXPA", "Anthropic expert data / labeling", "$M/yr", "AJ · L-114 (T4): 1-3B per year per lab at scale · Bear/Base/Bull", 3000, 2000, 1000)
    d("SAFA", "Anthropic safety / eval", "$M/yr", "AJ · L-117 (could-not-verify, T4): 55-115 per year · Bear/Base/Bull", 115, 85, 55)
    d("GTMA", "Anthropic GTM + G&A as % of comp (HOLE: no dollar disclosure; L-118 workforce mix 35/35/30)", "fraction", "HOLE · Model-agent placeholder triple, no spec value · Bear/Base/Bull", 0.60, 0.50, 0.40, nf=PCT, hole=True,
      note="Placeholder; listed in tie-out.md")
    d("AZTERM", "Azure commitment term (L-074 states no term)", "yrs", "AJ · 5 yrs, not scenario-flexed · Bear/Base/Bull", 5, 5, 5, nf=CNT)
    d("LAMTERM", "Lambda contract term (L-137 states no term; landlord lease is 15 yrs, L-167)", "yrs", "AJ · 6 yrs, flagged; not scenario-flexed · Bear/Base/Bull", 6, 6, 6, nf=CNT)
    d("RAMP", "SpaceX ramp discount factor for the 2026 months (reduced fee May-Jun 2026, L-046)", "factor", "AJ · 0.9, not scenario-flexed · Bear/Base/Bull", 0.9, 0.9, 0.9, nf=DEC2)
    d("OAIG", "OpenAI H2-2026 monthly run-rate growth", "fraction/month", "AJ · L-065 (July >20% MoM) · Bear/Base/Bull", 0.0, 0.10, 0.20, nf=PCT)
    d("OAICAGR", "OpenAI 2027-2030 revenue CAGR", "fraction", "AJ · L-069 (+35% QTD) as colour · Bear/Base/Bull", 0.40, 0.70, 1.00, nf=PCT)
    d("OAIPLAN", "OpenAI compute plan 2026-2030 (Bear is the higher spend)", "$M", "AJ · L-062 (750,000 Jul) at Base; L-078 (600,000 May) at Bull; 900,000 AJ at Bear · Bear/Base/Bull", 900000, f"={R('LB07b')}", f"={R('LB07b_may')}")
    d("OAIOPEX", "OpenAI 2027-2030 opex ex-compute as % of revenue", "fraction", "AJ · L-066 H1 ratio as ceiling · Bear/Base/Bull", 0.40, 0.30, 0.20, nf=PCT)
    d("OAITRN30", "OpenAI 2030E training", "$M/yr", "AJ · no row (L-125 stops at 2029) · Bear/Base/Bull", 120000, 90000, 60000)
    d("OAICOGS0", "OpenAI COGS as % of revenue, 2027E start of path", "fraction", "AJ · declining path; L-083 33% GM 2025 as anchor · Bear/Base/Bull", 0.50, 0.40, 0.30, nf=PCT)
    d("OAICOGSD", "OpenAI COGS % annual decline (points per year, 2028E+)", "fraction", "AJ · 'declining' per spec section 3.3 · Bear/Base/Bull", 0.02, 0.02, 0.02, nf=PCT)
    d("OAIHCG", "OpenAI headcount growth 2027E+ (after the 4,500 -> 8,000 linear 2026)", "fraction", "AJ · spec section 3.3: +20%/yr · Bear/Base/Bull", 0.20, 0.20, 0.20, nf=PCT)
    d("COMPO", "OpenAI average comp per head", "$M/yr", "AJ · spec section 3.3: 0.8 / 0.7 / 0.6 · Bear/Base/Bull", 0.8, 0.7, 0.6, nf=CNT2)
    d("SBCP", "SBC as % of operating loss (burn bridge)", "fraction", "AJ · spec section 3.1 · Bear/Base/Bull", 0.25, 0.20, 0.15, nf=PCT)
    d("ENV27LO", "Plan-envelope 2027E revenue, low (E10 plan envelope; no 2027 company figure)", "$M", "AJ · interpolation between the YE-2026 run-rate range and the 2028 forecast (cost-stack section 2) · same all scenarios", 140000, 140000, 140000)
    d("ENV27HI", "Plan-envelope 2027E revenue, high", "$M", "AJ · cost-stack section 2 · same all scenarios", 150000, 150000, 150000)
    d("HCUTMID", "Grid (a) haircut midpoint ('also 0.33 for grids')", "fraction", "AJ · spec section 5 · same all scenarios", 0.33, 0.33, 0.33, nf=PCT2)
    d("CEREBTERM", "Cerebras tranche phasing term (S-1/A: 3-4 yr terms; AJ 4)", "yrs", "AJ · L-149 · same all scenarios", 4, 4, 4, nf=CNT)

    # 5-Layer definition A40:F60
    sh.section(40, "THE 5-LAYER COST STACK: definition adopted for v5 (Exhibit E2; source cost-stack-reconciliation.md section 1)", ncols=8)
    sh.header(41, ["Layer", "Name", "Placement rule (counterparty or nature)", "What sits here", "Unit", "Note"])
    for i, (l, n, p, w, u) in enumerate(LAYERS):
        rr = 42 + i
        sh.put(f"A{rr}", l, bold=True); sh.put(f"B{rr}", n); sh.put(f"C{rr}", p, wrap=True); sh.put(f"D{rr}", w, wrap=True); sh.put(f"E{rr}", u)
        sh.put(f"F{rr}", "COMMITMENT layer" if l in ("L1", "L2") else "CONSUMPTION layer", kind="note")
        sh.ws.row_dimensions[rr].height = 48
    for i, t in enumerate(SEED_PLACEMENT):
        rr = 48 + i * 3
        sh.put(f"A{rr}", t, wrap=False, size=8)
    sh.put("A60", "End of the printed definition (A40:F60).", kind="note")

    # Contract timing (AJ, not scenario-flexed)
    sh.section(62, "CONTRACT TIMING AND OTHER AJ INPUTS (not scenario-flexed; same value in Bear/Base/Bull; feeds 09_Obligations)", ncols=8)
    sh.header(63, ["Input", "Unit", "Tag", "Bear", "Base", "Bull", "Live", "Note"])
    timing = [
        ("AWSSTART", "A-AWS start (deal 2026-04-20; straight-line from Jan-2026 per cost-stack)", D(2026, 1, 1), "AJ · L-072 · straight-line 10 yrs from 2026"),
        ("AZSTART", "A-Azure start", D(2026, 1, 1), "AJ · L-074 (deal 2025-11-18) · 5-yr AJ term from 2026"),
        ("SPACEXSTART", "A-SpaceX first full-fee month (ramp May-Jun 2026; 7 months in 2026 per cost-stack)", D(2026, 6, 1), "AJ · L-046 · 36 months Jun-2026 to May-2029"),
        ("NSCALESTART", "A-Nscale start (capacity from late-2027; 2027 = 25% year)", D(2027, 10, 1), "AJ · L-135"),
        ("LAMSTART", "A-Lambda start (AJ from 2027)", D(2027, 1, 1), "AJ · L-137"),
        ("VOLTASTART", "A-Volta start (H2-2026)", D(2026, 7, 1), "AJ · L-048"),
        ("RIOTSTART", "A-Riot start: spec section 3.9 text says '2028 AJ start' but its check values (2027 priced run 47,730) and cost-stack section 2 count Riot 455 in 2027; L-136 (20 yrs through Jun-2048) implies Jul-2028. Default 2027-01-01 reproduces the check values; see tie-out.md",
         D(2027, 1, 1), "AJ · L-136 · AMBIGUITY FLAGGED"),
        ("SPVSTART", "A-TPU-SPV lease start (mid-2026)", D(2026, 7, 1), "AJ · L-044 · 5-yr lease"),
        ("GOOGSTART", "A-Google leg start (capacity from 2027; reported 200,000 over five years from 2027)", D(2027, 1, 1), "AJ · L-073, L-155"),
        ("AMDSTART", "A-AMD first GW (H1-2027)", D(2027, 1, 1), "AJ · L-043"),
        ("ORCLSTART", "O-Oracle start (from 2027)", D(2027, 1, 1), "AJ · L-064"),
        ("OAWSSTART", "O-AWS start (from 2026)", D(2026, 1, 1), "AJ · L-064"),
        ("CWSTART", "O-CoreWeave start (six-year straight line to 2031; AJ)", D(2026, 1, 1), "AJ · L-058 · 22,400 / 6"),
        ("CEREBSTART", "O-Cerebras start (tranches 2026-2028)", D(2026, 1, 1), "AJ · L-149"),
        ("OAZSTART", "O-Azure priced-proxy start (LB08 FY2026 run held flat)", D(2026, 1, 1), "AJ · L-054 · proxy through 2030 (revenue share runs through 2030, L-051)"),
        ("SBESTART", "O-SB Energy PORTS ready-for-service (from 2028)", D(2028, 1, 1), "AJ · L-061"),
    ]
    for i, (k, lab, dv, tag) in enumerate(timing):
        rr = 64 + i
        sh.put(f"A{rr}", lab); sh.put(f"B{rr}", "date", kind="note"); sh.put(f"C{rr}", tag, kind="note")
        for col in "DEF":
            sh.put(f"{col}{rr}", dv, kind="aj", nf=DATEF)
        sh.put(f"G{rr}", f"=CHOOSE(SW_SCEN,D{rr},E{rr},F{rr})", kind="formula", nf=DATEF, bold=True, key=k)
    rr = 64 + len(timing)
    sh.put(f"A{rr}", "O-Azure priced-proxy horizon", ); sh.put(f"B{rr}", "yrs", kind="note"); sh.put(f"C{rr}", "AJ · L-051 revenue share through 2030 · same all scenarios", kind="note")
    for col in "DEF":
        sh.put(f"{col}{rr}", 5, kind="aj", nf=CNT)
    sh.put(f"G{rr}", f"=CHOOSE(SW_SCEN,D{rr},E{rr},F{rr})", kind="formula", nf=CNT, bold=True, key="OAZTERM")
    rr += 1
    sh.put(f"A{rr}", "O-CoreWeave straight-line term (2026-2031)"); sh.put(f"B{rr}", "yrs", kind="note"); sh.put(f"C{rr}", "AJ · L-058 · same all scenarios", kind="note")
    for col in "DEF":
        sh.put(f"{col}{rr}", 6, kind="aj", nf=CNT)
    sh.put(f"G{rr}", f"=CHOOSE(SW_SCEN,D{rr},E{rr},F{rr})", kind="formula", nf=CNT, bold=True, key="CWTERM")

    # Grid axes and phasing
    sh.section(84, "GRID AXES AND PHASING (07_Sensitivity); unit conversions", ncols=8)
    sh.header(85, ["Input", "Unit", "Tag", "Value 1", "Value 2", "Value 3", "Value 4", "Note"])
    sh.put("A86", "Compute-plan phasing 2027 / 2028 / 2029 / 2030 (share of plan less 2026)"); sh.put("B86", "fraction", kind="note"); sh.put("C86", "AJ · spec section 6(c): 15 / 22 / 28 / 35%", kind="note")
    for col, v, y in (("D", 0.15, 2027), ("E", 0.22, 2028), ("F", 0.28, 2029), ("G", 0.35, 2030)):
        sh.put(f"{col}86", v, kind="aj", nf=PCT, key=f"PH|{y}")
    sh.put("H86", f"=SUM(D86:G86)", kind="formula", nf=PCT); sh.put("I86", "sums to 100%", kind="note")
    sh.put("A87", "Grid (b) revenue axis: 150,000 (Bear 2028) / 175,000 (midpoint) / 200,000 (L-036 high)"); sh.put("B87", "$M", kind="note"); sh.put("C87", "AJ · spec section 6(b)", kind="note")
    sh.put("D87", f"={R('REV28_BEAR')}", kind="formula", nf=NUM, key="GRIDREV1"); sh.put("E87", f"=AVERAGE(D87,F87)", kind="formula", nf=NUM, key="GRIDREV2"); sh.put("F87", f"={R('LB10_high')}", kind="formula", nf=NUM, key="GRIDREV3")
    sh.put("A88", "Grid (b) GM axis: 60% / 70% / 77% (the 2028 GM triple)"); sh.put("B88", "fraction", kind="note"); sh.put("C88", "AJ · spec section 6(b)", kind="note")
    sh.put("A89", "Grid (b) training: 22,000 (L-125 2028) and 30,000 (Base 2029 AJ)"); sh.put("B89", "$M", kind="note"); sh.put("C89", "spec section 6(b)", kind="note")
    sh.put("D89", f"={R('A08_2028')}", kind="formula", nf=NUM, key="GRIDTRN1"); sh.put("E89", f"={R('TRN29_BASE')}", kind="formula", nf=NUM, key="GRIDTRN2")
    sh.put("A90", "Unit conversions used in formulas: months per year = 12; MW per GW = 1,000; quarters per year = 4; $M per $B = 1,000; monthly ramp steps July to December = 5; basis points per unit = 10,000", kind="note")
    sh.put("D90", 12, kind="input", nf=GEN, key="MPY"); sh.put("E90", 1000, kind="input", nf=GEN, key="MWPERGW"); sh.put("F90", 4, kind="input", nf=GEN, key="QPY"); sh.put("G90", 1000, kind="input", nf=GEN, key="MPERB")
    sh.put("H90", 5, kind="input", nf=GEN, key="RAMPSTEPS"); sh.put("I90", 10000, kind="input", nf=GEN, key="BPU"); sh.put("J90", 1000, kind="input", nf=GEN, key="KPERUNIT"); sh.put("K90", "$ per $K = 1,000", kind="note")
    sh.put("A91", "Greenfield (Lean / Full frontier / Vertically integrated) inputs live in Workbook B (greenfield-entry-cost.xlsx).", kind="note")
    build_00_checks(sh)

    # Time-series drivers
    sh.section(93, "TIME-SERIES AJ DRIVERS (live row = CHOOSE on SW_SCEN; Bear/Base/Bull rows yellow)", ncols=12)
    sh.yearhdr(94, label="Driver")
    r = 95
    gm = {y: None for y in FYEARS}
    r = driver_ts(sh, r, "GMA", "Anthropic gross margin path (GROSS basis)", "fraction", "AJ · L-119 (T4) plan at Bull 2028 and Base/Bull 2027; Base 2028 70% BELOW the 77% plan on purpose (section 5 finding)",
                  bear={2026: 0.44, 2027: 0.55, 2028: 0.60, 2029: f"={R('GM29_BEAR')}", 2030: f"={R('GM29_BEAR')}"},
                  base={2026: 0.52, 2027: f"={R('A07_2027')}", 2028: 0.70, 2029: f"={R('GM29_BASE')}", 2030: f"={R('GM29_BASE')}"},
                  bull={2026: 0.60, 2027: f"={R('A07_2027')}", 2028: f"={R('A07_2028')}", 2029: f"={R('GM29_BULL')}", 2030: f"={R('GM29_BULL')}"},
                  years=FYEARS, nf=PCT)
    r = driver_ts(sh, r, "TRNA", "Anthropic training (L3): 2026-2028 = plan (L-125) x factor; 2029-2030 AJ", "$M/yr", "AJ · L-125 (T4) x TRNF; 2029E-2030E from TRN29/TRN30",
                  bear={2026: f"={R('A08_2026')}*{R('TRNF_BEAR')}", 2027: f"={R('A08_2027')}*{R('TRNF_BEAR')}", 2028: f"={R('A08_2028')}*{R('TRNF_BEAR')}", 2029: f"={R('TRN29_BEAR')}", 2030: f"={R('TRN30_BEAR')}"},
                  base={2026: f"={R('A08_2026')}*{R('TRNF_BASE')}", 2027: f"={R('A08_2027')}*{R('TRNF_BASE')}", 2028: f"={R('A08_2028')}*{R('TRNF_BASE')}", 2029: f"={R('TRN29_BASE')}", 2030: f"={R('TRN30_BASE')}"},
                  bull={2026: f"={R('A08_2026')}*{R('TRNF_BULL')}", 2027: f"={R('A08_2027')}*{R('TRNF_BULL')}", 2028: f"={R('A08_2028')}*{R('TRNF_BULL')}", 2029: f"={R('TRN29_BULL')}", 2030: f"={R('TRN30_BULL')}"},
                  years=FYEARS, nf=NUM)
    r = driver_ts(sh, r, "OCOGS", "OpenAI COGS as % of revenue, 2027E-2030E (declining)", "fraction", "AJ · OAICOGS0 less OAICOGSD per year",
                  bear={2027: f"={R('OAICOGS0_BEAR')}", 2028: f"=H{r+1}-{R('OAICOGSD_BEAR')}", 2029: f"=I{r+1}-{R('OAICOGSD_BEAR')}", 2030: f"=J{r+1}-{R('OAICOGSD_BEAR')}"},
                  base={2027: f"={R('OAICOGS0_BASE')}", 2028: f"=H{r+2}-{R('OAICOGSD_BASE')}", 2029: f"=I{r+2}-{R('OAICOGSD_BASE')}", 2030: f"=J{r+2}-{R('OAICOGSD_BASE')}"},
                  bull={2027: f"={R('OAICOGS0_BULL')}", 2028: f"=H{r+3}-{R('OAICOGSD_BULL')}", 2029: f"=I{r+3}-{R('OAICOGSD_BULL')}", 2030: f"=J{r+3}-{R('OAICOGSD_BULL')}"},
                  years=[2027, 2028, 2029, 2030], nf=PCT)
    r = driver_ts(sh, r, "TRNO", "OpenAI training (L3): 2026-2029 = L-125; 2030 AJ", "$M/yr", "L-125 (T4) 2026-2029 (same all scenarios); 2030 = OAITRN30",
                  bear={2026: f"={R('O06_2026')}", 2027: f"={R('O06_2027')}", 2028: f"={R('O06_2028')}", 2029: f"={R('O06_2029')}", 2030: f"={R('OAITRN30_BEAR')}"},
                  base={2026: f"={R('O06_2026')}", 2027: f"={R('O06_2027')}", 2028: f"={R('O06_2028')}", 2029: f"={R('O06_2029')}", 2030: f"={R('OAITRN30_BASE')}"},
                  bull={2026: f"={R('O06_2026')}", 2027: f"={R('O06_2027')}", 2028: f"={R('O06_2028')}", 2029: f"={R('O06_2029')}", 2030: f"={R('OAITRN30_BULL')}"},
                  years=FYEARS, nf=NUM)
    r = driver_ts(sh, r, "HCA", "Anthropic headcount path (2026 = SW_A_HC; 2027E+ grows at HCGA)", "people", "AJ · L-008 / L-091 via SW_A_HC; growth = HCGA (HOLE placeholder)",
                  bear={2026: "=SW_A_HC", 2027: f"=G{r+1}*(1+{R('HCGA_BEAR')})", 2028: f"=H{r+1}*(1+{R('HCGA_BEAR')})", 2029: f"=I{r+1}*(1+{R('HCGA_BEAR')})", 2030: f"=J{r+1}*(1+{R('HCGA_BEAR')})"},
                  base={2026: "=SW_A_HC", 2027: f"=G{r+2}*(1+{R('HCGA_BASE')})", 2028: f"=H{r+2}*(1+{R('HCGA_BASE')})", 2029: f"=I{r+2}*(1+{R('HCGA_BASE')})", 2030: f"=J{r+2}*(1+{R('HCGA_BASE')})"},
                  bull={2026: "=SW_A_HC", 2027: f"=G{r+3}*(1+{R('HCGA_BULL')})", 2028: f"=H{r+3}*(1+{R('HCGA_BULL')})", 2029: f"=I{r+3}*(1+{R('HCGA_BULL')})", 2030: f"=J{r+3}*(1+{R('HCGA_BULL')})"},
                  years=FYEARS, nf=CNT)
    r = driver_ts(sh, r, "HCO", "OpenAI headcount path (2026 = average of 4,500 and the 8,000 plan; 2027E+ from 8,000 at OAIHCG)", "people", "AJ · L-027, L-090; +20%/yr per spec",
                  bear={2026: f"=AVERAGE({R('O08')},{R('O08_plan')})", 2027: f"={R('O08_plan')}*(1+{R('OAIHCG_BEAR')})", 2028: f"=H{r+1}*(1+{R('OAIHCG_BEAR')})", 2029: f"=I{r+1}*(1+{R('OAIHCG_BEAR')})", 2030: f"=J{r+1}*(1+{R('OAIHCG_BEAR')})"},
                  base={2026: f"=AVERAGE({R('O08')},{R('O08_plan')})", 2027: f"={R('O08_plan')}*(1+{R('OAIHCG_BASE')})", 2028: f"=H{r+2}*(1+{R('OAIHCG_BASE')})", 2029: f"=I{r+2}*(1+{R('OAIHCG_BASE')})", 2030: f"=J{r+2}*(1+{R('OAIHCG_BASE')})"},
                  bull={2026: f"=AVERAGE({R('O08')},{R('O08_plan')})", 2027: f"={R('O08_plan')}*(1+{R('OAIHCG_BULL')})", 2028: f"=H{r+3}*(1+{R('OAIHCG_BULL')})", 2029: f"=I{r+3}*(1+{R('OAIHCG_BULL')})", 2030: f"=J{r+3}*(1+{R('OAIHCG_BULL')})"},
                  years=FYEARS, nf=CNT)
    sh.put(f"A{r}", "Base case rationale (spec section 4): 39.75% because Ruling 5 is gate-verified on the May-2026 mix and binds; Base 2028 GM 70% rather than 77% because both labs missed GM plans in every observed case (L-083, L-119) and the section-5 envelope does not close at 77%; "
                    "Base OpenAI compute plan 750,000 because it is the latest company-attributed vintage (L-062); Base Google leg = the reported 40,000 per year because it is the only dollar figure in existence for that contract, flagged [VERIFY] on every cell that reads it (L-155), with the proxy branches printed beside it.", kind="note")
    sh.put(f"A{r+1}", "Scenario mapping for the Google leg (spec section 4, applied through the 12_Conflicts switches, not SW_SCEN): Bear = proxy at 16.3 per MW-yr (SW_GOOGLE_VALUE = proxy, SW_TPU_RATE = 16.3); Base = reported 40,000 per year [VERIFY] (SW_GOOGLE_VALUE = reported); Bull = proxy at 6.9 (chips only).", kind="note")
    sh.put(f"A{r+2}", "AM-71 note: the Bessemer rule applied to FY2026E growth (+476% on the PB FY2025 10,000) would give +333% in 2027 and ~249,356 of revenue, above the company's 2028 plan, which is why the base rate shapes only the 2029E-2030E tails (arithmetic on 13_OutsideView).", kind="note")
    sh.ws.freeze_panes = "D5"


CHECKS = [
    # key, label, expected, tolerance (absolute)
    ("IDENT_A", "Identity: LB03 + 2,500 = 126,754 (L-006)", 126754, 0.05),
    ("IDENT_O", "Identity: LB04 + 5,220 = 186,436.5 (L-021)", 186436.5, 0.05),
    ("NETRR", "Anthropic net run-rate at 39.75%", 39162, 0.5),
    ("MULT_G", "Anthropic multiple, gross (display)", 14.8, 0.05),
    ("MULT_3975", "Anthropic multiple at 39.75%", 24.6, 0.05),
    ("MULT_27", "Anthropic multiple at 27%", 20.3, 0.05),
    ("MULT_O", "OpenAI multiple (NET)", 21.3, 0.05),
    ("MULT_OG", "OpenAI multiple, gross case", 26.6, 0.05),
    ("CE_3975", "Anthropic CE at 39.75%", 0.315, 0.0005),
    ("CE_27", "Anthropic CE at 27%", 0.382, 0.0005),
    ("CE_G", "Anthropic CE gross (forbidden basis, display)", 0.523, 0.0005),
    ("CE_O", "OpenAI CE", 0.221, 0.0005),
    ("RATIO", "CE ratio at 39.75%", 1.43, 0.005),
    ("RATIO27", "CE ratio at 27%", 1.73, 0.005),
    ("RATIOG", "CE ratio, gross", 2.37, 0.005),
    ("FY26_100", "Anthropic FY2026E at YE 100,000", 57580, 0.5),
    ("FY26_120", "Anthropic FY2026E at YE 120,000", 62580, 0.5),
    ("FY26_FLAT", "Anthropic FY2026E flat from July", 48830, 0.5),
    ("H1A", "Anthropic H1-2026 recognized", 16330, 0.5),
    ("Q2Q1", "Anthropic Q2/Q1", 2.45, 0.005),
    ("OAI_0", "OpenAI FY2026E at 0% monthly growth", 32400, 0.5),
    ("OAI_10", "OpenAI FY2026E at 10%", 38119, 0.5),
    ("OAI_20", "OpenAI FY2026E at 20%", 45500, 0.5),
    ("DOC_A", "Anthropic documented-$ (excl. SPV)", 324100, 0.5),
    ("DOC_A_SPV", "Anthropic documented-$ incl. SPV", 358600, 0.5),
    ("REP_A", "Anthropic reported-$ incl. Google leg [VERIFY]", 524100, 0.5),
    ("DOC_O", "OpenAI documented-$", 480400, 0.5),
    ("REC_O", "OpenAI recalled-$", 690000, 0.5),
    ("BBG", "Bloomberg tally", 175000, 0.5),
    ("STEP", "stepmark tally", 99100, 0.5),
    ("TC", "TechCrunch tally (mixes equity)", 61250, 0.5),
    ("CANC_A", "Anthropic cancellable (approx.)", 48000, 500),
    ("RUN26", "Anthropic 2026 priced run (incl. SPV half-year)", 28158, 0.5),
    ("RUN27", "Anthropic 2027 priced run", 47730, 0.5),
    ("RUN28", "Anthropic 2028 priced run", 53355, 0.5),
    ("RUN29", "Anthropic 2029 priced run", 44605, 0.5),
    ("RUN30", "Anthropic 2030 priced run", 38355, 0.5),
    ("RUNO27", "OpenAI 2027 priced run", 110083, 0.5),
    ("STACK28", "Anthropic 2028 stack, reported branch (priced + 40,000)", 93355, 0.5),
    ("ENV28_LO", "Plan envelope 2028, low", 65700, 0.5),
    ("ENV28_HI", "Plan envelope 2028, high", 68000, 0.5),
    ("ENV27_LO", "Plan envelope 2027, low", 65800, 0.5),
    ("ENV27_HI", "Plan envelope 2027, high", 69500, 0.5),
    ("GAP28_REP_LO", "E10 gap 2028, reported branch, low", -27655, 0.5),
    ("GAP28_REP_HI", "E10 gap 2028, reported branch, high", -25355, 0.5),
    ("GAP27_REP_LO", "E10 gap 2027, reported branch, low", -21930, 0.5),
    ("GAP27_REP_HI", "E10 gap 2027, reported branch, high", -18230, 0.5),
    ("GAP28_PROXY", "E10 gap 2028, proxy 9.3 at 5 GW (approx. midpoint)", -33000, 1500),
    ("GAP28_15GW", "E10 gap 2028, proxy 9.3 at 15 GW (approx. midpoint)", -126000, 1500),
    ("GAP28_125", "E10 gap 2028, proxy 12.5 at 5 GW (approx. midpoint)", -49000, 1500),
    ("GAP28_125_15", "E10 gap 2028, proxy 12.5 at 15 GW (approx. midpoint)", -174000, 1500),
    ("GRIDB", "Grid (b) at (200,000, 77%, reported)", -25355, 0.5),
    ("UNEXPL", "OpenAI $50B split: unexplained", 10900, 0.5),
    ("GM_GRID_G", "Q2 GM grid at opex 3,000, GROSS", 0.31, 0.005),
    ("GM_GRID_N", "Q2 GM grid at opex 3,000, NET-39.75", 0.51, 0.005),
    ("CE_A", "AIBQ Anthropic CE (default)", 7.375, 0.0005),
    ("CE_A_CL", "AIBQ Anthropic CE (facility closes)", 7.30, 0.0005),
    ("CI_A", "AIBQ Anthropic CI", 5.55, 0.0005),
    ("CE_O_AIBQ", "AIBQ OpenAI CE", 3.925, 0.0005),
    ("CI_O", "AIBQ OpenAI CI", 5.60, 0.0005),
    ("COMP_A", "AIBQ Anthropic composite (default)", 8.15, 0.005),
    ("COMP_A_CL", "AIBQ Anthropic composite (facility closes)", 8.13, 0.006),
    ("COMP_A_CANON", "AIBQ Anthropic composite (canonical CI 5.8 base)", 8.04, 0.005),
    ("COMP_O", "AIBQ OpenAI composite", 4.87, 0.005),
    ("COMP_O_G", "AIBQ OpenAI composite, gross case", 4.79, 0.005),
    ("EI_A", "Efficiency Index Anthropic", 0.55, 0.005),
    ("EI_O", "Efficiency Index OpenAI", 0.50, 0.005),
    ("PPT_A", "$B per AIBQ point, Anthropic (default)", 118, 0.5),
    ("PPT_O", "$B per AIBQ point, OpenAI", 175, 0.5),
    ("PPT_A_CL", "$B per point, Anthropic (facility closes)", 119, 0.5),
    ("SPREAD", "Ladder spread (default)", 1.48, 0.005),
    ("SPREAD_CL", "Ladder spread (facility closes)", 1.47, 0.005),
    ("SPREAD_OLD", "Ladder spread (May-27)", 1.60, 0.005),
    ("PPT_O_OLD", "$B per point, OpenAI (May-27)", 188, 0.5),
    ("MORE_PPT", "$B more per point paid for OpenAI (new)", 57, 0.5),
    ("TAIL_BEAR29", "Bessemer tail Bear 2029", 176250, 0.5),
    ("TAIL_BEAR30", "Bessemer tail Bear 2030", 197841, 0.5),
    ("TAIL_BASE29", "Bessemer tail Base 2029", 231276, 0.5),
    ("TAIL_BASE30", "Bessemer tail Base 2030", 266446, 0.5),
    ("TAIL_BULL29", "Bessemer tail Bull 2029", 286000, 0.5),
    ("TAIL_BULL30", "Bessemer tail Bull 2030", 354640, 0.5),
    ("SPREAD_BP_LO", "SPV vs neocloud spread, low (bp)", 325, 0.5),
    ("SPREAD_BP_HI", "SPV vs neocloud spread, high (bp)", 400, 0.5),
    ("SPREAD_ANN_LO", "Annual value of the spread on 34,500, low", 1121, 0.5),
    ("SPREAD_ANN_HI", "Annual value of the spread on 34,500, high", 1380, 0.5),
    ("J16_MULT", "Jul-16 reference multiple (both)", 34.1, 0.05),
    ("J16_RATIO", "Jul-16 CE ratio", 1.65, 0.005),
    ("AM71_G", "AM-71: FY2026E growth on PB FY2025", 4.76, 0.005),
    ("AM71_D", "AM-71: decayed 2027 growth", 3.33, 0.005),
    ("AM71_R", "AM-71: implied 2027 revenue", 249356, 1),
    ("REL_3975", "Relative multiple at (39.75%, NET)", 0.15, 0.01),
    ("REL_27", "Relative multiple at (27%, NET)", -0.05, 0.01),
    ("REL_G", "Relative multiple at (39.75%, GROSS)", -0.07, 0.01),
    ("RATIO_G_CE", "CE ratio at (39.75%, GROSS)", 1.78, 0.01),
    ("GOOG_RATE5", "Google implied rate at 5 GW", 8.0, 0.05),
    ("GOOG_RATE16", "Google implied rate at 16 GW", 2.5, 0.05),
]


def build_00_checks(sh):
    r0 = 130
    sh.section(r0, "SPEC SECTION 9 CHECK VALUES (typed once here; every PASS/FAIL cell in the workbook compares against these; tolerance absolute)", ncols=8)
    sh.header(r0 + 1, ["Check", "Unit", "Tag", "Expected", "Tolerance", "", "", "Where computed"])
    for i, (k, lab, v, tol) in enumerate(CHECKS):
        rr = r0 + 2 + i
        sh.put(f"A{rr}", lab)
        sh.put(f"B{rr}", "as stated", kind="note")
        sh.put(f"C{rr}", "spec section 9 / section 3 check value (model-spec.md, patched 2026-09-09)", kind="note")
        sh.put(f"D{rr}", v, kind="input", nf=GEN, key=f"CHK_{k}")
        sh.put(f"E{rr}", tol, kind="input", nf=GEN, key=f"TOL_{k}")


def ck(sh, ref, actual, key):
    """PASS/FAIL cell comparing an actual cell/expression with the typed spec check value."""
    exp = R(f"CHK_{key}"); tol = R(f"TOL_{key}")
    sh.put(ref, f'=IF(ABS(({actual})-{exp})<={tol},"PASS","FAIL: "&TEXT(({actual})-{exp},"#,##0.000"))', kind="formula", bold=True, key=f"PF_{key}")


# ----------------------------------------------------------------------------------------------------
# 12_Conflicts
# ----------------------------------------------------------------------------------------------------
def build_12(sh):
    sh.put("A1", "12_Conflicts: frozen-conflict switch register. Column C = live switch value (named range; formula over the selector); column D = selector (blue, 1..n); columns E:H = branch values linked from 01_Data (no number typed twice). Change the selector, never column C.", kind="note")
    sh.put("A2", "Frozen conflicts (both branches live in the text; writer-brief section 4): C-02 residual, C-03, C-05, C-08, C-12 (+addendum), C-13, C-15 (display only), C-16, C-18, C-14 addendum (Google leg), the $15B facility.", kind="note")
    sh.header(4, ["Name (cell C)", "Conflict", "Live value", "Selector", "Branch 1", "Branch 2", "Branch 3", "Branch 4", "Branch labels (1 / 2 / 3 / 4)", "Default", "Cells gated"])
    rows = [
        (5, "SW_HAIRCUT", "C-13 equalization magnitude", 1, [f"={R('R01')}", f"={R('R02')}"], "0.3975 (Ruling 5, L-126) / 0.27 (OpenAI CRO memo relay, T4); 0.33 in grid (a) only", "0.3975", "02_Revenue net rows; 05_Cash_Fund CE; 06_Valuation multiples; 11_AIBQ CE-1 ratio; 07_Sensitivity grid (a)", PCT2),
        (6, "SW_OAI_BASIS", "C-16 OpenAI run-rate basis", 1, ['"NET"', '"GROSS"'], "NET / GROSS (GROSS applies R03 = 20%, T4, flagged)", "NET", "02_Revenue OpenAI net row; 06_Valuation; 11_AIBQ CE-1 (5.0 / 4.0)", GEN),
        (7, "SW_IPO_OAI", "C-02 (residual) OpenAI IPO window", 2, ['"Q4-2026"', '"2027"'], "Q4-2026 / 2027 ('Sep-2026' is not a branch: retired by L-002 and the 15-day rule)", "2027", "08_Output IPO status text; 13_OutsideView milestone row", GEN),
        (8, "SW_A_FY25", "C-03 Anthropic FY2025 recognized revenue", 1, [f"={R('A06')}", f"=AVERAGE({R('A06_impl_low')},{R('A06_impl_high')})"], "10,000 (PB field = exit run-rate) / 5,250 (midpoint of the implied 4,500-6,000)", "10,000", "02_Revenue annual recognized 2025; 03_Costs L4 2025; 04_PL 2025", NUM),
        (9, "SW_A_FY24_NI", "C-05 Anthropic FY2024 net loss", 2, [f"={R('A05_NI_alt')}", f"={R('A05_NI')}"], "-5,300 (Jul-16 PB vintage) / -8,300 (Sep-9 PB vintage, latest)", "-8,300", "04_PL 2024 net result", NUM),
        (10, "SW_A_2026_LOSS", "C-12 (with addendum) Anthropic 2026 loss / burn", 2, ['"GAAP -11,000 (Jan plan)"', '"Adjusted-operating-income trajectory (Q2 print; non-GAAP, definition unpublished, L-151/L-152)"'], "GAAP -11,000 (Jan-2026 plan, L-120 T4) / adjusted-operating-income trajectory (Q2 print, L-151 T2; L-152)", "Q2 print", "05_Cash_Fund Anthropic 2026 burn block; 04_PL 2026 note row", GEN),
        (11, "SW_A_HC", "C-18 Anthropic headcount", 1, [f"={R('A10')}", f"={R('A10_alt')}"], "5,000 (PB, L-008) / 4,020 (Revelio, L-091 T4)", "5,000", "03_Costs L5 comp; 00_Assumptions headcount path", CNT),
        (12, "SW_TPU_RATE", "proxy choice (not a conflict): Google TPU $M per MW-yr", 2, [f"={R('X01_tpu_69')}", f"={R('X01_tpu_93')}", f"={R('X01_tpu_125')}", f"={R('X01_tpu_163')}"], "6.9 (chips only, L-044) / 9.3 (chips + Riot shell, L-044 + L-136) / 12.5 (Volta, L-134) / 16.3 (Nscale, L-134)", "9.3", "09_Obligations unpriced proxy; E10 band; 07_Sensitivity grid (b) proxy panel", CNT1),
        (13, "SW_TOTAL_RAISED_VIEW", "C-01 Anthropic total raised (display only)", 1, ['"On-balance-sheet"', '"Incl. lease SPV"'], "On-balance-sheet (126,754 = equity + revolver) / Incl. lease SPV (adds 34,500 lessor debt); CE never changes (Ruling 1)", "On-balance-sheet", "05_Cash_Fund capitalization display block only", GEN),
        (14, "SW_15B_FACILITY", "$15B facility (L-042, L-160: not closed as of Sep-9)", 2, ['"Closes"', '"Does not close"'], "Closes / Does not close (house rule: [VERIFY] until closed)", "Does not close", "05_Cash_Fund facilities; 11_AIBQ CE-4 (closes 7.0 / does not close 7.5; neither returns to the prior 8.0 because the lease stack drives the score)", GEN),
        (15, "SW_SSI", "C-08 SSI total raised", 1, [f"={R('SSI_pb')}", f"={R('SSI_press')}"], "7,000 (PB, L-097) / 8,000 (press)", "7,000", "Workbook B 08_Reference (mirrored)", NUM),
        (16, "SW_GW_2028", "scope choice (not a conflict): unpriced Google GW in 2028", 1, [f"={R('X02_a27')}", f"={R('X02_a27')}+{R('X02_a28')}"], "5 (contracted 2027 tranche only, L-049/L-073) / 15 (plus Broadcom's 10 GW 2028 line of sight, L-049)", "5", "09_Obligations unpriced proxy; E10 band; grid (b)", CNT),
        (17, "SW_GOOGLE_VALUE", "C-14 addendum: Google leg value", 1, ['"reported"', '"proxy"'], "reported (40,000 per year 2027-2031, L-155 T3 [VERIFY]) / proxy (GW x SW_TPU_RATE, GW from SW_GW_2028)", "reported (Base)", "09_Obligations Google leg column and reported-$ total; E10 band; grid (b); never documented-$", GEN),
    ]
    for rr, name, conflict, sel, branches, labels, default, gated, nf in rows:
        sh.put(f"A{rr}", name, bold=True)
        sh.put(f"B{rr}", conflict)
        cols = ["E", "F", "G", "H"]
        for i, b in enumerate(branches):
            if b.startswith('="') or b.startswith('"'):
                sh.put(f"{cols[i]}{rr}", b.strip('"') if not b.startswith("=") else b, kind="input", nf=nf)
            else:
                sh.put(f"{cols[i]}{rr}", b, kind="formula", nf=nf)
        refs = ",".join(f"{cols[i]}{rr}" for i in range(len(branches)))
        sh.put(f"D{rr}", sel, kind="input", nf=GEN, align="center")
        sh.put(f"C{rr}", f"=CHOOSE(D{rr},{refs})", kind="formula", nf=nf, bold=True, name=name, key=name)
        sh.put(f"I{rr}", labels, kind="note")
        sh.put(f"J{rr}", default, kind="note")
        sh.put(f"K{rr}", gated, kind="note")
    sh.put("A18", "(display) C-15", bold=True); sh.put("B18", "Secondary marks (both T4): 1,500,000 implied at $925/share (Prime Unicorn Index) vs 'low-to-mid 800,000' (kucoin); none adopted; the primary mark stays 965,000 (M01). No formula reads this row.", kind="note")
    sh.put("A20", "RESOLVED CONFLICTS (stated as resolved; resolving row in brackets)", bold=True)
    resolved = [
        ("C-01", "Anthropic total capital raised", "The 34,500 is lessor/SPV debt with Broadcom and Google support, not Anthropic-issued bonds; PB removed it from Total Raised (161,254 -> 126,754); equity-only 124,254 is unaffected (L-006, L-007, L-044)."),
        ("C-04", "FY2025 net income on PB deal records", "An identical -42,000 sits on both companies' FY2025 records: a PB artifact; neither figure is used (L-011, L-026)."),
        ("C-06", "OpenAI FY2025 revenue", "PB's 20,000 matches the end-2025 exit run-rate, not recognized revenue; FY2025 = 13,100 (L-025, L-063, L-065)."),
        ("C-07", "Anthropic Fast Mode pricing", "Fast Mode is 2x standard pricing on the live pricing page; the Jul-16 '3x cheaper' claim is retired (L-084)."),
        ("C-09", "Thinking Machines seed post-money", "Basis gap (PB 10,000 post vs press 12,000); minor; PB carried (L-098)."),
        ("C-10", "Reflection AI Series B date", "PB date-field artifact (2026-07-01 vs press Oct-2025); flagged for PB correction (L-099)."),
        ("C-11", "Cost per training run", "Basis gap: annual training-compute budgets (L-125) vs single final-run amortized compute (L-115); labelled, never summed."),
        ("C-14", "Anthropic 2026 compute-commitment total", "Scope gap: tallies are different deal lists; components printed with scope on 09_Obligations (L-138); addendum: the Google leg (L-155) sits in its own scope row with [VERIFY]."),
        ("C-17", "Series H lead investors", "Minor labelling difference; the company statement governs (L-015, L-038)."),
        ("C-19", "Microsoft ownership of OpenAI", "~27% (~135,000) at the Oct-2025 recap is now T2 verbatim (L-159); post-dilution 'decreased' and undisclosed (10-K, L-054); funding commitments 13,000 / 11,900 funded (L-157)."),
        ("C-20", "Nvidia-OpenAI '100B / 10 GW' LOI", "Superseded: 30,000 equity invested plus a 105,000 residual-value guaranty; the remaining ~70,000 'probably not in the cards' (L-075, L-061)."),
        ("O-15", "Altman title on PB", "PB artifact from an Antimetal Co-CEO biography line; no OpenAI co-CEO structure (L-028, L-070, L-089)."),
    ]
    sh.header(21, ["Conflict", "Subject", "Resolution"])
    for i, (c, s, t) in enumerate(resolved):
        rr = 22 + i
        sh.put(f"A{rr}", c, bold=True); sh.put(f"B{rr}", s); sh.put(f"C{rr}", t, kind="note")
    sh.put("A36", "Six rulings carried: Ruling 1 CE denominators equity-only; Ruling 2 correlation embargoed; Ruling 3 adjusted operating income is not FCF (unswept); Ruling 4 PB TTM fields are forward projections, never current; Ruling 5 39.75% equalization with the ~27% branch; Ruling 6 Report weights CE 20 / RQ 25 / CI 15 / GO 20 / MD 20.", kind="note")
    sh.put("A37", "Provenance box: 168 ledger rows; confirmed 97, estimated 51, recalled 6, could-not-verify 14; Gate 1 passed twice (L-161 and L-165 tagged estimated/T3 by rule). The S-1s will replace load-bearing figures 1-6 with audited numbers.", kind="note")
