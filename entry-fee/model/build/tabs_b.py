# tabs_b.py: Workbook B (greenfield-entry-cost.xlsx): 00_Assumptions, 01_Data, 02_Compute, 03_Facility, 04_Training, 05_Inference,
# 06_People_Other, 07_Cash, 08_Reference, 09_Output. Three scenarios (SW_GF: 1 Lean fast-follower / 2 Full frontier / 3 Vertically
# integrated) are computed side by side on every model tab (one block per scenario) so 09_Output prints all three; the live block follows SW_GF.
from xlhelp import *

YB = {1: "D", 2: "E", 3: "F", 4: "G", 5: "H"}
YRS = [1, 2, 3, 4, 5]
SC = {1: "D", 2: "E", 3: "F"}
SCEN = {1: "1 Lean fast-follower", 2: "2 Full frontier", 3: "3 Vertically integrated with custom silicon"}
register_names(["SW_GF", "SW_GF_BACKSTOP", "SW_GF_REGION", "SW_GF_MODELCLASS", "SW_SSI"])


def d(key, s):
    return R(f"{key}|{s}")


def dy(key, s, y):
    return R(f"{key}|{s}|{y}")


def L(name, s, y):
    return R(f"{name}|{s}|{y}")


def line(sh, r, name, s, label, unit, src, cells, nf=NUM, bold=False, kind="formula"):
    sh.put(f"A{r}", label, bold=bold)
    if unit:
        sh.put(f"B{r}", unit, kind="note")
    if src:
        sh.put(f"C{r}", src, kind="note")
    for y in YRS:
        v = cells.get(y) if isinstance(cells, dict) else cells
        if v is None:
            continue
        sh.put(f"{YB[y]}{r}", v, kind=kind, nf=nf, bold=bold, key=(f"{name}|{s}|{y}" if name else None))


def drvB(sh, row, key, label, unit, tag, lean, full, vi, nf=NUM, lo=None, hi=None, note=None, hole=False):
    kind = "hole" if hole else "aj"
    sh.put(f"A{row}", label); sh.put(f"B{row}", unit, kind="note"); sh.put(f"C{row}", tag, kind="note")
    for s, v in ((1, lean), (2, full), (3, vi)):
        sh.put(f"{SC[s]}{row}", v, kind=kind, nf=nf, key=f"{key}|{s}")
    sh.put(f"G{row}", f"=CHOOSE(SW_GF,D{row},E{row},F{row})", kind="formula", nf=nf, bold=True, key=key)
    if lo is not None:
        sh.put(f"H{row}", lo, kind=("formula" if isinstance(lo, str) and lo.startswith("=") else "aj"), nf=nf, key=f"{key}|lo")
    if hi is not None:
        sh.put(f"I{row}", hi, kind=("formula" if isinstance(hi, str) and hi.startswith("=") else "aj"), nf=nf, key=f"{key}|hi")
    if note:
        sh.put(f"J{row}", note, kind="note")


def drvB_ts(sh, row, key, label, unit, tag, lean, full, vi, nf=NUM, note=None, hole=False):
    kind = "hole" if hole else "aj"
    sh.put(f"A{row}", label, bold=True); sh.put(f"B{row}", unit, kind="note"); sh.put(f"C{row}", tag, kind="note")
    for s, vals in ((1, lean), (2, full), (3, vi)):
        rr = row + s
        sh.put(f"A{rr}", f"   {SCEN[s]}", kind="note")
        for y in YRS:
            v = vals.get(y) if isinstance(vals, dict) else vals
            if v is None:
                continue
            sh.put(f"{YB[y]}{rr}", v, kind=kind, nf=nf, key=f"{key}|{s}|{y}")
    for y in YRS:
        c = YB[y]
        sh.put(f"{c}{row}", f"=CHOOSE(SW_GF,{c}{row+1},{c}{row+2},{c}{row+3})", kind="formula", nf=nf, bold=True, key=f"{key}|live|{y}")
    if note:
        sh.put(f"J{row}", note, kind="note")
    return row + 5


# ----------------------------------------------------------------------------------------------------
# 01_Data (B)
# ----------------------------------------------------------------------------------------------------
def build_b01(sh):
    sh.put("A1", "01_Data (Workbook B): greenfield anchors G01-G30 (model-spec.md section 7.2) and the reference class (section 7.5). Column C = source string (row · status · tier · as-of · basis). Blue = typed input; black = derived; yellow = AJ / could-not-verify.", kind="note")
    sh.header(3, ["ID", "Item", "Source (row · status · tier · as-of · basis)", "Value", "Unit", "As-of", "Basis", "Status", "Tier", "Decay", "Ledger row", "Used by", "Note"])
    r = 4

    def sec(t):
        nonlocal r
        sh.section(r, t, ncols=13); r += 1

    def row(id_, item, value, unit, rowid, status, tier, asof, basis, decay="STABLE", used="", note="", nf=NUM, yellow=False):
        nonlocal r
        r = drow(sh, r, id_, item, value, unit, rowid, status, tier, asof, basis, decay, used, note, nf, "input", None, yellow)

    sec("G01 GPU purchase prices (index / channel; use ranges)")
    for k, lab, v in (("H100_new_lo", "H100 new, low", 25000), ("H100_new_hi", "H100 new, high", 40000), ("H100_used_lo", "H100 used, low", 8200), ("H100_used_hi", "H100 used, high", 25000),
                      ("B200_lo", "B200 unit, low", 30000), ("B200_hi", "B200 unit, high", 40000), ("GB200_rack_lo", "GB200 NVL72 rack, low", 2000000), ("GB200_rack_hi", "GB200 NVL72 rack, high", 3000000),
                      ("GB300_rack_lo", "GB300 NVL72 rack, low", 3000000), ("GB300_rack_hi", "GB300 NVL72 rack, high", 4000000), ("DGX_B300", "DGX B300 (~)", 400000), ("B200_mfg", "B200 manufacturing cost (~)", 6400)):
        row(k, f"G01: {lab}", v, "$", "L-103", "estimated", "T4", "2026-07-10", "GPU price index (no Nvidia list price for rack systems)", "VOLATILE", "00, 02", nf=CNT)
    row("GPUS_PER_RACK", "GPUs per NVL72 rack", 72, "GPUs", "L-103", "confirmed", "T2", "2026", "NVL72 = 72 GPUs", "PERMANENT", "00", nf=CNT)
    sec("G02 GPU-hour on-demand (provider price pages, T1) and G03 contracted large-cluster rates (T3)")
    for k, lab, v in (("CW_H100", "CoreWeave H100 per GPU-hr", 6.16), ("CW_H200", "CoreWeave H200", 6.31), ("CW_B200", "CoreWeave B200", 8.60), ("CW_GB200", "CoreWeave GB200 NVL72 per GPU-hr", 10.50),
                      ("LAM_B200", "Lambda B200 (8x)", 6.69), ("LAM_H100", "Lambda H100 SXM", 3.99), ("NEB_H100", "Nebius H100", 3.85), ("NEB_B200", "Nebius B200", 7.15), ("NEB_B300", "Nebius B300", 7.85)):
        row(k, f"G02: {lab}", v, "$ per GPU-hr", "L-104", "confirmed", "T1", "2026-09-09", "provider price page; on-demand", "VOLATILE", "05 (G20), 02", nf=CNT2)
    row("CW_res_disc", "G02: CoreWeave reserved discount ('up to')", 0.60, "fraction", "L-104", "confirmed", "T1", "2026-09-09", "price page", "VOLATILE", "02", nf=PCT)
    row("NEB_res_disc", "G02: Nebius reservation discount ('up to')", 0.35, "fraction", "L-104", "confirmed", "T1", "2026-09-09", "price page", "VOLATILE", "02", nf=PCT)
    row("NEO_P25", "G03: B200 cluster, neocloud 25th percentile", 2.40, "$ per GPU-hr", "L-105", "estimated", "T3", "2026-04-20", "SemiAnalysis ClusterMAX", "VOLATILE", "00, 02, 05", nf=CNT2)
    row("HYP_P50", "G03: B200 cluster, hyperscaler ~50th percentile", 3.10, "$ per GPU-hr", "L-105", "estimated", "T3", "2026-04-20", "SemiAnalysis", "VOLATILE", "00, 02, 05", nf=CNT2)
    row("GB300_EX", "G03: GB300 NVL72 example (5,184 GPUs)", 4.00, "$ per GPU-hr", "L-105", "estimated", "T3", "2026-04-20", "SemiAnalysis", "VOLATILE", "00, 05", nf=CNT2)
    row("TCO_lo", "G03: hyperscaler TCO vs gold-tier neocloud, low", 1.10, "x", "L-105", "estimated", "T3", "2026-04-20", "LLM pretrain", "VOLATILE", "09 (note)", nf=MULT2)
    row("TCO_hi", "G03: hyperscaler TCO vs gold-tier neocloud, high", 1.61, "x", "L-105", "estimated", "T3", "2026-04-20", "multimodal RL", "VOLATILE", "09 (note)", nf=MULT2)
    sec("G04 cost of debt; G05 power per GPU; G06 electricity; G08 datacenter build; G10 colocation; G11 full-stack lease")
    row("NEO1", "G04: CoreWeave 2031 senior notes", 0.09, "fraction", "L-059, L-106", "confirmed", "T1", "2026-06-30", "10-Q", "STABLE", "00", nf=PCT2)
    row("NEO2", "G04: CoreWeave 2031 senior notes (second)", 0.0975, "fraction", "L-059, L-106", "confirmed", "T1", "2026-06-30", "10-Q", "STABLE", "00", nf=PCT2)
    row("NEO3", "G04: CoreWeave 2032 senior notes", 0.09625, "fraction", "L-059, L-106", "confirmed", "T1", "2026-06-30", "10-Q", "STABLE", "00", nf=PCT2)
    row("NEO_MID", "G04: neocloud unsecured, midpoint of 9.00-9.75%", f"=AVERAGE({R('NEO1')},{R('NEO2')})", "fraction", "L-059", "confirmed", "T1", "2026-06-30", "derived", "STABLE", "00", nf=PCT2)
    row("SPV_A2", "G04: vendor-backstopped SPV tranche A2", 0.0575, "fraction", "L-044, L-106", "estimated", "T3", "2026-08-12", "Epoch AI; A1 = Treasuries + 1pt; B = 8.5%", "STABLE", "00", nf=PCT2)
    row("SPV_B", "G04: SPV tranche B", 0.085, "fraction", "L-044, L-106", "estimated", "T3", "2026-08-12", "Epoch AI", "STABLE", "00", nf=PCT2)
    row("EQUIP_lo", "G04: OEM equipment financing rate, low (AJ; exists, rate not stated)", 0.07, "fraction", "L-059 (existence)", "estimated", "AJ", "2026-06-30", "AJ 7-8%", "STABLE", "00", nf=PCT2, yellow=True)
    row("EQUIP_hi", "G04: OEM equipment financing rate, high (AJ)", 0.08, "fraction", "L-059 (existence)", "estimated", "AJ", "2026-06-30", "AJ 7-8%", "STABLE", "00", nf=PCT2, yellow=True)
    row("MW_H100", "G05: facility MW per 1,000 H100-class GPUs", 1.5, "MW", "L-107", "estimated", "T3", "2024-09", "Colossus rule of thumb; PUE embedded", "STABLE", "00", nf=CNT2)
    row("MW_GB200_lo", "G05: facility MW per 1,000 GB200-class GPUs, low", 2.0, "MW", "L-107", "estimated", "T3", "2026", "rack 120-132 kW; ~1.2 kW per GPU", "STABLE", "00", nf=CNT2)
    row("MW_GB200_hi", "G05: facility MW per 1,000 GB200-class GPUs, high", 2.2, "MW", "L-107", "estimated", "T3", "2026", "as above", "STABLE", "00", nf=CNT2)
    for k, lab, v in (("EIA_TX", "Texas", 65.8), ("EIA_WA", "Washington", 72.0), ("EIA_AZ", "Arizona", 77.3), ("EIA_WY", "Wyoming", 87.5), ("EIA_GA", "Georgia", 88.6), ("EIA_US", "US industrial average", 91.7), ("EIA_VA", "Virginia", 93.1), ("EIA_OH", "Ohio", 98.9), ("EIA_PA", "Pennsylvania", 101.0)):
        row(k, f"G06: industrial electricity price, {lab}", v, "$ per MWh", "L-108", "confirmed", "T1", "2026-06", "EIA Table 5.6.A; large-load tariffs differ", "QUARTERLY", "03", nf=CNT1)
    row("NOR_AJ", "G06: Norway (AJ 40-60; hydropower site per L-048)", 50, "$ per MWh", "AJ (no row)", "estimated", "AJ", "2026", "AJ", "QUARTERLY", "03", nf=CNT1, yellow=True)
    row("BUILD", "G08: all-in greenfield build cost", 17.6, "$M per MW", "L-109", "confirmed", "T2", "2026-09-03", "Cushman & Wakefield 2026 guide; +21% since Q4-2024", "STABLE", "00, 03", nf=CNT1)
    row("BUILD_AI", "G08: AI-dense build cost ('can exceed 20M')", 20, "$M per MW", "L-109", "estimated", "T4", "2026-09-03", "T4 note", "STABLE", "00 (range)", nf=CNT1)
    row("SHELL_CORE", "G08: shell-and-core (JLL)", 11.3, "$M per MW", "L-109", "estimated", "T4", "2026", "JLL 2026 outlook", "STABLE", "09 (note)", nf=CNT1)
    row("LAND", "G08: powered land", 584000, "$ per MW", "L-109", "confirmed", "T2", "2026", "primary US markets YTD 2026", "STABLE", "09 (note)", nf=CNT)
    row("POWER_SHARE", "G08: power infrastructure share of greenfield cost", 0.21, "fraction", "L-109", "confirmed", "T2", "2026", "C&W", "STABLE", "09 (note)", nf=PCT)
    row("WHOLESALE_lo", "G10: wholesale colocation, low", 100, "$ per kW-month", "L-110", "estimated", "T3", "2026", "triple-net hyperscale/AI leases", "STABLE", "09 (note)", nf=CNT)
    row("WHOLESALE_hi", "G10: wholesale colocation, high", 150, "$ per kW-month", "L-110", "estimated", "T3", "2026", "as above", "STABLE", "09 (note)", nf=CNT)
    row("CS_tot", "G10: Core Scientific-AMD base contracted revenue", 14000, "$M", "L-148", "confirmed", "T1", "2026-07-28", "15 yrs, 530 MW, 2.5% escalators", "STABLE", "00", nf=NUM)
    row("CS_MW", "G10: Core Scientific-AMD capacity", 530, "MW", "L-148", "confirmed", "T1", "2026-07-28", "five sites", "STABLE", "00", nf=CNT)
    row("CS_term", "G10: Core Scientific-AMD term", 15, "yrs", "L-148", "confirmed", "T1", "2026-07-28", "15-year agreements", "STABLE", "00", nf=CNT)
    row("BP_val", "G10: Hut 8 Beacon Point campus base-term contract value", 19600, "$M", "L-167", "confirmed", "T1", "2026-07-20", "15-yr, 704 MW; tenant Nvidia; 50,200 with renewals", "STABLE", "00", nf=NUM)
    row("BP_MW", "G10: Beacon Point tenant capacity", 704, "MW", "L-167", "confirmed", "T1", "2026-07-20", "Hut 8 release", "STABLE", "00", nf=CNT)
    row("BP_term", "G10: Beacon Point lease term", 15, "yrs", "L-167", "confirmed", "T1", "2026-07-20", "Hut 8 release", "STABLE", "00", nf=CNT)
    row("RIOT_tot", "G10: Riot powered-shell lease", 9100, "$M", "L-136", "confirmed", "T2", "2026-08-10", "20 yrs, 191 MW", "STABLE", "00", nf=NUM)
    row("RIOT_MW", "G10: Riot capacity", 191, "MW", "L-136", "confirmed", "T2", "2026-08-10", "Rockdale", "STABLE", "00", nf=CNT)
    row("RIOT_term", "G10: Riot term", 20, "yrs", "L-136", "confirmed", "T2", "2026-08-10", "through June 2048", "STABLE", "00", nf=CNT)
    row("CS_rate", "G10: Core Scientific-AMD powered shell (derived)", f"={R('CS_tot')}/{R('CS_MW')}/{R('CS_term')}", "$M per MW-yr", "L-148", "confirmed", "T1 (derived)", "2026-07-28", "= 14,000 / 530 / 15", "STABLE", "00, 09", nf=CNT2)
    row("BP_rate", "G10: Hut 8 Beacon Point powered shell (derived)", f"={R('BP_val')}/{R('BP_MW')}/{R('BP_term')}", "$M per MW-yr", "L-167", "confirmed", "T1 (derived)", "2026-07-20", "= 19,600 / 704 / 15 (~155 per kW-month)", "STABLE", "00, 09", nf=CNT2)
    row("RIOT_rate", "G10: Riot powered shell (derived)", f"={R('RIOT_tot')}/{R('RIOT_MW')}/{R('RIOT_term')}", "$M per MW-yr", "L-136", "confirmed", "T2 (derived)", "2026-08-10", "= 9,100 / 191 / 20", "STABLE", "00, 09", nf=CNT2)
    row("RETAIL_lo", "G10: retail colocation, low", 180, "$ per kW-month", "L-110", "estimated", "T4", "2026", "retail", "STABLE", "09 (note)", nf=CNT)
    row("RETAIL_hi", "G10: retail colocation, high", 400, "$ per kW-month", "L-110", "estimated", "T4", "2026", "retail", "STABLE", "09 (note)", nf=CNT)
    row("NSCALE_tot", "G11: Nscale full-stack deal", 45000, "$M", "L-135, L-134", "confirmed", "T2", "2026-08-26", "6 yrs, ~460 MW Vera Rubin", "STABLE", "00", nf=NUM)
    row("NSCALE_MW", "G11: Nscale capacity", 460, "MW", "L-135", "estimated", "T3", "2026-08-26", "relay", "STABLE", "00", nf=CNT)
    row("NSCALE_term", "G11: Nscale term", 6, "yrs", "L-135", "confirmed", "T2", "2026-08-26", "six years", "STABLE", "00", nf=CNT)
    row("VOLTA_tot", "G11: Volta full-stack deal", 10000, "$M", "L-048, L-134", "estimated", "T3", "2026-08-04", "6 yrs, 133 MW", "STABLE", "00", nf=NUM)
    row("VOLTA_MW", "G11: Volta capacity", 133, "MW", "L-048", "estimated", "T3", "2026-08-04", "Tydal", "STABLE", "00", nf=CNT)
    row("VOLTA_term", "G11: Volta term", 6, "yrs", "L-048", "estimated", "T3", "2026-08-04", "six years", "STABLE", "00", nf=CNT)
    row("FS_NSCALE", "G11: full-stack lease rate, Nscale (derived)", f"={R('NSCALE_tot')}/{R('NSCALE_MW')}/{R('NSCALE_term')}", "$M per MW-yr", "L-134", "estimated", "T3 (derived)", "2026-08", "= 45,000 / 460 / 6", "VOLATILE", "00, 09", nf=CNT2)
    row("FS_VOLTA", "G11: full-stack lease rate, Volta (derived)", f"={R('VOLTA_tot')}/{R('VOLTA_MW')}/{R('VOLTA_term')}", "$M per MW-yr", "L-134", "estimated", "T3 (derived)", "2026-08", "= 10,000 / 133 / 6", "VOLATILE", "00, 09", nf=CNT2)
    sec("G12 network; G13 storage (could-not-verify); G14 training runs; G15 incumbent budgets")
    row("NET_lo", "G12: network fabric share of GPU hardware cost, low", 0.03, "fraction", "L-111", "estimated", "T3", "2026-06-08", "Hedgehog (vendor-adjacent)", "STABLE", "00", nf=PCT)
    row("NET_hi", "G12: network fabric share, high", 0.15, "fraction", "L-111", "estimated", "T3", "2026-06-08", "Hedgehog", "STABLE", "00", nf=PCT)
    row("NET_B200", "G12: network share, B200 BOM at 1,024 GPUs", 0.08, "fraction", "L-111", "estimated", "T3", "2026-06-08", "Hedgehog", "STABLE", "00", nf=PCT)
    row("NET_GB300", "G12: network share, GB300", 0.058, "fraction", "L-111", "estimated", "T3", "2026-06-08", "Hedgehog", "STABLE", "00", nf=PCT)
    row("NET_MI300", "G12: network share, MI300X", 0.212, "fraction", "L-111", "estimated", "T3", "2026-06-08", "Hedgehog", "STABLE", "09 (note)", nf=PCT)
    row("IB_GPU", "G12: InfiniBand per GPU (T4)", 4000, "$ per GPU", "L-111", "estimated", "T4", "2026", "Spheron (T4)", "STABLE", "09 (note)", nf=CNT)
    row("STO_lo", "G13: storage share of cluster capex, low (could-not-verify)", 0.02, "fraction", "L-112", "could-not-verify", "T4", "2026", "aggregators only; FLAGGED", "STABLE", "00", nf=PCT, yellow=True)
    row("STO_hi", "G13: storage share of cluster capex, high (could-not-verify)", 0.05, "fraction", "L-112", "could-not-verify", "T4", "2026", "aggregators only; FLAGGED", "STABLE", "00", nf=PCT, yellow=True)
    row("STO_node_lo", "G13: parallel FS node, low", 60000, "$", "L-112", "could-not-verify", "T4", "2026", "WEKA-class node", "STABLE", "09 (note)", nf=CNT, yellow=True)
    row("STO_node_hi", "G13: parallel FS node, high", 100000, "$", "L-112", "could-not-verify", "T4", "2026", "as above", "STABLE", "09 (note)", nf=CNT, yellow=True)
    for k, lab, v in (("GPT4", "GPT-4 (~)", 78), ("GEMINI", "Gemini Ultra (~)", 191), ("LLAMA", "Llama 3.1-405B (~)", 170), ("GROK4", "Grok 4 (~)", 500), ("GPT45", "GPT-4.5 pre-training (~)", 200), ("GPT45_post", "GPT-4.5 post-training (~)", 2), ("BY2027", "largest runs by 2027 ('>1,000')", 1000)):
        row(k, f"G14: final-run compute cost, {lab}", v, "$M", "L-115", "estimated", "T3", "2024-06-03 / 2025-09-26", "Epoch AI; amortized hardware and energy for the final run", "STABLE", "00, 04", nf=NUM)
    row("GROWTH", "G14: final-run cost growth since 2016", 2.4, "x per yr", "L-115", "estimated", "T3", "2024-06-03", "Epoch AI", "STABLE", "04", nf=CNT1)
    for k, lab, v in (("SH_hw_lo", "hardware share, low", 0.47), ("SH_hw_hi", "hardware share, high", 0.67), ("SH_staff_lo", "R&D staff share, low", 0.29), ("SH_staff_hi", "R&D staff share, high", 0.49), ("SH_en_lo", "energy share, low", 0.02), ("SH_en_hi", "energy share, high", 0.06)):
        row(k, f"G14: development cost shares, {lab}", v, "fraction", "L-115", "estimated", "T3", "2024-06-03", "Epoch AI", "STABLE", "09 (note)", nf=PCT)
    for k, lab, v in (("ANT_T26", "Anthropic 2026E", 7000), ("ANT_T27", "Anthropic 2027E", 14000), ("ANT_T28", "Anthropic 2028E", 22000), ("OAI_T26", "OpenAI 2026E", 25000), ("OAI_T27", "OpenAI 2027E", 60000), ("OAI_T28", "OpenAI 2028E", 112000), ("OAI_T29", "OpenAI 2029E", 120000)):
        row(k, f"G15: incumbent annual training budget, {lab}", v, "$M/yr", "L-125", "recalled", "T4", "undated leaked docs", "annual training-compute budget (C-11); ceiling for scenario 2", "STABLE", "00, 04", nf=NUM)
    sec("G18 inference proxies; G19 list prices; G20 throughput (L-164); G21-G22 comp and retention; G23-G27 data, safety, legal, GTM; G28-G29 silicon")
    row("OAI_INF25", "G18: OpenAI inference cost 2025", 8400, "$M", "L-083", "estimated", "T3", "2025", "Sacra", "QUARTERLY", "00, 05", nf=NUM)
    row("OAI_REV25", "G18: OpenAI revenue 2025", 13100, "$M", "L-063", "confirmed", "T2", "FY2025", "NET presumed", "STABLE", "00, 05", nf=NUM)
    row("OAI_INF26", "G18: OpenAI inference cost 2026E", 14100, "$M", "L-083", "estimated", "T3", "2026E", "Sacra", "QUARTERLY", "05", nf=NUM)
    row("INF_SHARE25", "G18: OpenAI inference as % of revenue, 2025 (derived; the Y1 anchor of the % path)", f"={R('OAI_INF25')}/{R('OAI_REV25')}", "fraction", "L-083, L-063", "estimated", "T3 (derived)", "2025", "= 8,400 / 13,100", "QUARTERLY", "00", nf=PCT)
    row("XPU_HALF", "G18: custom XPU 'half the cost of a GPU' (vendor claim)", 0.5, "fraction", "L-050", "confirmed", "T1 (vendor)", "2026-09-02", "Broadcom call; FLAGGED vendor claim", "STABLE", "00, 05", nf=PCT, yellow=True)
    row("F51_lo", "G18: Fable 5.1 cost per task reduction, low (vendor)", 0.25, "fraction", "L-085", "confirmed", "T1 (vendor)", "2026-09-01", "vendor claim", "VOLATILE", "09 (note)", nf=PCT)
    row("F51_hi", "G18: Fable 5.1 cost per task reduction, high (vendor)", 0.45, "fraction", "L-085", "confirmed", "T1 (vendor)", "2026-09-01", "vendor claim", "VOLATILE", "09 (note)", nf=PCT)
    for k, lab, v in (("P_F51_in", "Fable 5.1 input", 10), ("P_F51_out", "Fable 5.1 output", 50), ("P_O5_in", "Opus 5 input", 5), ("P_O5_out", "Opus 5 output", 25), ("P_S5_in", "Sonnet 5 input", 2), ("P_S5_out", "Sonnet 5 output", 10), ("P_H45_in", "Haiku 4.5 input", 1), ("P_H45_out", "Haiku 4.5 output", 5), ("P_cache_lo", "cache read, low", 0.25), ("P_cache_hi", "cache read, high", 0.50), ("P_batch", "batch discount", 0.5), ("P_fast", "Fast Mode multiplier", 2)):
        row(k, f"G19: list price, {lab}", v, "$ per MTok", "L-084", "confirmed", "T1", "2026-09-09", "pricing page; revenue-side ceiling", "VOLATILE", "00, 05", nf=CNT2)
    row("MOE_OUT", "G20: SGLang on GB200 NVL72, DeepSeek V3/R1, output tokens per second per GPU", 13386, "tok/s/GPU", "L-164", "confirmed", "T2", "2025-09-25", "FP8 attention + NVFP4 MoE; 2,000-token inputs", "STABLE", "00, 05, 09", nf=CNT)
    row("MOE_IN", "G20: SGLang GB200 input (prefill) tokens per second per GPU", 26156, "tok/s/GPU", "L-164", "confirmed", "T2", "2025-09-25", "LMSYS", "STABLE", "05", nf=CNT)
    row("MOE_BF16", "G20: SGLang GB200 output at BF16/FP8", 9087, "tok/s/GPU", "L-164", "confirmed", "T2", "2025-09-25", "LMSYS", "STABLE", "05", nf=CNT)
    row("MLPERF_OFF", "G20: MLPerf v5.1 GB300 NVL72 DeepSeek-R1 offline", 5842, "tok/s/GPU", "L-164", "confirmed", "T2", "2025-09-09", "NVIDIA blog", "STABLE", "05", nf=CNT)
    row("MLPERF_SRV", "G20: MLPerf v5.1 GB300 NVL72 DeepSeek-R1 server", 2907, "tok/s/GPU", "L-164", "confirmed", "T2", "2025-09-09", "NVIDIA blog", "STABLE", "05", nf=CNT)
    row("DENSE_OFF", "G20: GB200 NVL72 Llama 3.1 405B offline", 224, "tok/s/GPU", "L-164", "confirmed", "T2", "2025-09-09", "dense-frontier proxy", "STABLE", "00, 05, 09", nf=CNT)
    row("DENSE_SRV", "G20: GB200 NVL72 Llama 3.1 405B server", 170, "tok/s/GPU", "L-164", "confirmed", "T2", "2025-09-09", "dense-frontier proxy", "STABLE", "05", nf=CNT)
    row("DENSE_INT", "G20: GB200 NVL72 Llama 3.1 405B interactive", 138, "tok/s/GPU", "L-164", "confirmed", "T2", "2025-09-09", "dense-frontier proxy", "STABLE", "05", nf=CNT)
    row("LEAD_lo", "G21: top-decile leader package, low ($M per year over 4 yrs)", 25, "$M/yr", "L-094", "confirmed", "T2", "2025-06-27", "Meta: '$100M over four years not inconceivable'", "STABLE", "00", nf=CNT1)
    row("LEAD_hi", "G21: top-decile leader package, high (up to 300 over 4 yrs)", 75, "$M/yr", "L-094", "confirmed", "T2", "2025-06-27", "Wired via TheFly: up to $300M over 4 years", "STABLE", "00", nf=CNT1)
    row("SEN_lo", "G21: senior IC total comp, low (T4)", 0.5, "$M/yr", "L-094 notes", "estimated", "T4", "2025", "T4 bands", "STABLE", "00", nf=CNT2)
    row("SEN_hi", "G21: senior IC total comp, high (T4)", 1.5, "$M/yr", "L-094 notes", "estimated", "T4", "2025", "T4 bands", "STABLE", "00", nf=CNT2)
    row("MTS_a", "G21: Anthropic MTS base salary (H-1B; verbatim relay)", 1.12, "$M/yr", "L-165", "estimated", "T3", "2026-06-28", "base only; supersedes L-092", "QUARTERLY", "09 (note)", nf=CNT2)
    row("MTS_b", "G21: Anthropic MTS base salary (H-1B)", 1.38, "$M/yr", "L-165", "estimated", "T3", "2026-06-28", "base only", "QUARTERLY", "09 (note)", nf=CNT2)
    row("ENG_lo", "G21: engineer total comp, low (T4)", 0.30, "$M/yr", "L-092 notes", "estimated", "T4", "2026", "aggregators", "QUARTERLY", "00", nf=CNT2)
    row("ENG_hi", "G21: engineer total comp, high (T4)", 0.76, "$M/yr", "L-092 notes", "estimated", "T4", "2026", "aggregators", "QUARTERLY", "00", nf=CNT2)
    row("RET_pp", "G22: retention bonus per person (~)", 1.5, "$M", "L-093, L-166", "estimated / could-not-verify", "T3", "2025-08", "The Information relay", "STABLE", "00", nf=CNT2)
    row("RET_n", "G22: retention bonus recipients (~)", 1000, "people", "L-093, L-166", "estimated / could-not-verify", "T3", "2025-08", "relay", "STABLE", "00", nf=CNT)
    row("RET_yrs", "G22: retention payout period", 2, "yrs", "L-093, L-166", "estimated / could-not-verify", "T3", "2025-08", "quarterly over two years", "STABLE", "00", nf=CNT)
    row("SRC_lo", "G23: marquee text source, low (per source-year)", 50, "$M/yr", "L-113", "confirmed", "T1", "2024-02-22", "Reddit S-1 via TechCrunch; ~20 publisher deals at OpenAI", "STABLE", "00", nf=NUM)
    row("SRC_hi", "G23: marquee text source, high", 70, "$M/yr", "L-113", "confirmed", "T1", "2024-02-22", "as above", "STABLE", "00", nf=NUM)
    row("REDDIT", "G23: Reddit aggregate contract value", 203, "$M", "L-113", "confirmed", "T1", "2024-01", "2-3 yr terms", "STABLE", "09 (note)", nf=NUM)
    row("NEWSCORP", "G23: News Corp-OpenAI ('up to' over five years)", 250, "$M", "L-113", "estimated", "T3", "2024-05", "Variety", "STABLE", "09 (note)", nf=NUM)
    row("LAB_lo", "G24: expert data / labeling per lab at scale, low", 1000, "$M/yr", "L-114", "estimated", "T4", "2026", "Mercor 2,000 annualized; Scale ~1,000; Surge ~1,000", "QUARTERLY", "00", nf=NUM)
    row("LAB_hi", "G24: expert data / labeling per lab at scale, high", 3000, "$M/yr", "L-114", "estimated", "T4", "2026", "as above", "QUARTERLY", "00", nf=NUM)
    row("SAFE_lo", "G25: safety / eval spend, low (could-not-verify)", 55, "$M/yr", "L-117", "could-not-verify", "T4", "2026", "FLAGGED", "STABLE", "09 (note)", nf=NUM, yellow=True)
    row("SAFE_hi", "G25: safety / eval spend, high (could-not-verify)", 115, "$M/yr", "L-117", "could-not-verify", "T4", "2026", "FLAGGED", "STABLE", "09 (note)", nf=NUM, yellow=True)
    row("SAFE_sh_lo", "G25: safety as share of research headcount, low (AJ)", 0.03, "fraction", "AJ (L-117 as colour)", "estimated", "AJ", "2026", "AJ", "STABLE", "00", nf=PCT, yellow=True)
    row("SAFE_sh_hi", "G25: safety as share of research headcount, high (AJ)", 0.08, "fraction", "AJ", "estimated", "AJ", "2026", "AJ", "STABLE", "00", nf=PCT, yellow=True)
    row("COPY_settle", "G26: Anthropic copyright settlement (paid)", 1500, "$M", "L-086", "confirmed", "T2", "2026-07-20", "Bartz", "STABLE", "00", nf=NUM)
    row("MUSIC", "G26: music-publisher demands ('>3,000')", 3000, "$M", "L-086", "confirmed", "T2", "2026-01-29", "unreserved", "STABLE", "09 (note)", nf=NUM)
    row("RES_lo", "G26: entrant legal reserve over 5 yrs, low (AJ)", 500, "$M", "AJ (L-086, L-088 as colour)", "estimated", "AJ", "2026", "AJ", "STABLE", "00", nf=NUM, yellow=True)
    row("RES_hi", "G26: entrant legal reserve over 5 yrs, high (AJ)", 1500, "$M", "AJ", "estimated", "AJ", "2026", "AJ", "STABLE", "00", nf=NUM, yellow=True)
    row("COMPL_lo", "G26: compliance / policy per year, low (AJ)", 20, "$M/yr", "AJ", "estimated", "AJ", "2026", "AJ", "STABLE", "00", nf=NUM, yellow=True)
    row("COMPL_hi", "G26: compliance / policy per year, high (AJ)", 50, "$M/yr", "AJ", "estimated", "AJ", "2026", "AJ", "STABLE", "00", nf=NUM, yellow=True)
    for k, lab, v in (("MIX_fin", "Finance / Ops", 0.349), ("MIX_sm", "Sales and Marketing", 0.348), ("MIX_eng", "Engineering", 0.303)):
        row(k, f"G27: incumbent workforce mix (Revelio, T4), {lab}", v, "fraction", "L-118", "estimated", "T4", "2026", "Anthropic workforce mix", "QUARTERLY", "00 (colour)", nf=PCT)
    row("GTM_lean", "G27: Lean GTM/G&A share of headcount cost (AJ)", 0.20, "fraction", "AJ (L-118 as colour)", "estimated", "AJ", "2026", "AJ", "STABLE", "00", nf=PCT, yellow=True)
    row("GTM_lo", "G27: scenarios 2-3 GTM/G&A share, low (AJ)", 0.40, "fraction", "AJ", "estimated", "AJ", "2026", "AJ", "STABLE", "00", nf=PCT, yellow=True)
    row("GTM_hi", "G27: scenarios 2-3 GTM/G&A share, high (AJ)", 0.60, "fraction", "AJ", "estimated", "AJ", "2026", "AJ", "STABLE", "00", nf=PCT, yellow=True)
    row("BCOM26", "G28: Broadcom AI revenue FY2026 (~)", 58000, "$M", "L-144", "confirmed", "T1", "2026-09-02", "six XPU customers", "QUARTERLY", "09", nf=NUM)
    row("BCOM27", "G28: Broadcom AI revenue FY2027 (supply secured)", 115000, "$M", "L-144", "confirmed", "T1", "2026-09-02", "vendor guidance", "QUARTERLY", "09", nf=NUM)
    row("BCOM28", "G28: Broadcom AI revenue FY2028 (line of sight)", 230000, "$M", "L-144", "confirmed", "T1", "2026-09-02", "vendor guidance", "QUARTERLY", "09", nf=NUM)
    row("ENTRANT_ASIC_YEAR", "G28: entrant custom-silicon access (AJ): none before", 2029, "year", "AJ (L-144)", "estimated", "AJ", "2026", "supply booked through 2028 by incumbents", "STABLE", "00, 09", nf=GEN, yellow=True)
    row("ASIC_lo", "G29: custom ASIC program (NRE and team) per year, low (AJ)", 1000, "$M/yr", "AJ (no row)", "estimated", "AJ", "2026", "3-4 years to first GA", "STABLE", "00", nf=NUM, yellow=True)
    row("ASIC_hi", "G29: custom ASIC program per year, high (AJ)", 3000, "$M/yr", "AJ (no row)", "estimated", "AJ", "2026", "as above", "STABLE", "00", nf=NUM, yellow=True)
    row("ASIC_risk", "G29: first-silicon risk allowance (AJ)", 0.30, "fraction", "AJ (no row)", "estimated", "AJ", "2026", "AJ", "STABLE", "00", nf=PCT, yellow=True)
    sec("G30 REFERENCE CLASS (section 7.5): what entry actually cost")
    row("XAI_deficit", "xAI (inside SpaceX): accumulated deficit at 2026-03-31 (consolidated)", 41311, "$M", "L-096", "confirmed", "T1", "2026-03-31", "SpaceX S-1", "STABLE", "08, 09", nf=NUM)
    row("XAI_debt25", "xAI: AI-segment 2025 debt proceeds", 16055, "$M", "L-096", "confirmed", "T1", "FY2025", "SpaceX S-1", "STABLE", "08, 09", nf=NUM)
    row("XAI_rev25", "xAI: AI-segment 2025 revenue", 3201, "$M", "L-096", "confirmed", "T1", "FY2025", "SpaceX S-1", "STABLE", "08", nf=NUM)
    row("XAI_oploss25", "xAI: AI-segment 2025 loss from operations (magnitude)", 6355, "$M", "L-096", "confirmed", "T1", "FY2025", "SpaceX S-1", "STABLE", "08", nf=NUM)
    row("XAI_q1rev", "xAI: Q1-2026 revenue", 818, "$M", "L-096", "confirmed", "T1", "Q1-2026", "SpaceX S-1", "QUARTERLY", "08", nf=NUM)
    row("XAI_q1loss", "xAI: Q1-2026 loss from operations (magnitude)", 2469, "$M", "L-096", "confirmed", "T1", "Q1-2026", "SpaceX S-1", "QUARTERLY", "08", nf=NUM)
    row("XAI_q2rev", "xAI: Q2-2026 AI-segment revenue (+247%)", 2560, "$M", "L-047", "confirmed", "T2", "Q2-2026", "SpaceX Q2 results", "QUARTERLY", "08", nf=NUM)
    row("XAI_q2loss", "xAI: Q2-2026 AI-segment operating loss (magnitude)", 1260, "$M", "L-047", "confirmed", "T2", "Q2-2026", "SpaceX Q2 results", "QUARTERLY", "08", nf=NUM)
    row("XAI_capexq2", "xAI: SpaceX consolidated Q2-2026 capex", 18400, "$M", "L-047", "confirmed", "T2", "Q2-2026", "SpaceX Q2 results", "QUARTERLY", "08", nf=NUM)
    row("XAI_acq", "xAI: acquired by SpaceX at (Feb-2026)", 250000, "$M", "L-096", "confirmed", "T2", "2026-02-03", "PB SpaceXAI profile", "STABLE", "08", nf=NUM)
    row("SSI_pb", "SSI: total raised (PB)", 7000, "$M", "L-097", "confirmed", "T2", "2026-07-28", "PB; C-08", "STABLE", "00 (SW_SSI), 08", nf=NUM)
    row("SSI_press", "SSI: total raised (press tallies)", 8000, "$M", "L-097, C-08", "estimated", "T2/T4", "2026-07-28", "press; C-08", "STABLE", "00 (SW_SSI), 08", nf=NUM)
    row("SSI_val", "SSI: valuation", 32000, "$M", "L-097", "confirmed", "T2", "2025-04-11", "PB LKV", "STABLE", "08", nf=NUM)
    row("SSI_hc", "SSI: headcount", 40, "people", "L-097", "confirmed", "T2", "2026-07-29", "PB", "QUARTERLY", "08", nf=CNT)
    row("TML_raised", "Thinking Machines Lab: seed raised", 2000, "$M", "L-098", "confirmed", "T2", "2025-06-20", "PB", "STABLE", "08, 09", nf=NUM)
    row("TML_post", "Thinking Machines Lab: seed post-money (PB; press 12,000, C-09)", 10000, "$M", "L-098", "confirmed", "T2", "2025-06-20", "PB", "STABLE", "08", nf=NUM)
    row("TML_pre_talks", "Thinking Machines Lab: pre-money sought (in talks)", 40000, "$M", "L-098", "estimated", "T3", "2026-09-03", "The Information", "VOLATILE", "08", nf=NUM)
    row("TML_hc", "Thinking Machines Lab: headcount (~)", 200, "people", "L-098", "confirmed", "T2", "2026-07-16", "PB", "QUARTERLY", "08", nf=CNT)
    row("TML_pbrev", "Thinking Machines Lab: PB revenue field FY2026 (projection)", 100, "$M", "L-098", "estimated", "T2", "2026", "PB projection; 'at least a few hundred million' annualized (The Information)", "VOLATILE", "08", nf=NUM)
    row("REF_raised", "Reflection AI: total raised", 2155, "$M", "L-099", "confirmed", "T2", "2026-09-07", "PB", "STABLE", "08, 09", nf=NUM)
    row("REF_post", "Reflection AI: Series B post-money", 8000, "$M", "L-099", "confirmed", "T2", "2026", "PB", "STABLE", "08", nf=NUM)
    row("REF_pre_c", "Reflection AI: Series C pre-money (in progress)", 25000, "$M", "L-099", "confirmed", "T2", "2026-05-12", "PB", "VOLATILE", "08", nf=NUM)
    row("REF_hc", "Reflection AI: headcount (~)", 200, "people", "L-099", "confirmed", "T2", "2026", "PB", "QUARTERLY", "08", nf=CNT)
    row("MIS_raised", "Mistral AI: total raised incl. 830 debt", 7492, "$M", "L-100", "confirmed", "T2", "2026-09-08", "PB", "STABLE", "08, 09", nf=NUM)
    row("MIS_debt", "Mistral AI: of which debt", 830, "$M", "L-100", "confirmed", "T2", "2026-03-30", "PB", "STABLE", "08", nf=NUM)
    row("MIS_val", "Mistral AI: valuation (~EUR 21B post)", 24374, "$M", "L-100", "confirmed", "T2", "2026-09-08", "PB LKV", "VOLATILE", "08", nf=NUM)
    row("MIS_hc", "Mistral AI: headcount (~)", 900, "people", "L-100", "confirmed", "T2", "2026", "PB", "QUARTERLY", "08", nf=CNT)
    row("MIS_pbrev", "Mistral AI: PB revenue field FY2026 (projection)", 1167, "$M", "L-100", "estimated", "T2", "2026", "PB projection", "VOLATILE", "08", nf=NUM)
    row("PER_raised", "Periodic Labs: seed", 300, "$M", "L-101", "confirmed", "T2", "2025-09-03", "PB", "STABLE", "08", nf=NUM)
    row("PER_post", "Periodic Labs: seed post-money (est.)", 1300, "$M", "L-101", "confirmed", "T2", "2025-09-03", "PB", "STABLE", "08", nf=NUM)
    row("PER_hc", "Periodic Labs: headcount", 48, "people", "L-101", "confirmed", "T2", "2026-03-25", "PB", "QUARTERLY", "08", nf=CNT)
    row("HUM_raised", "Humans&: seed", 480, "$M", "L-102", "confirmed", "T2", "2026-01-20", "PB", "STABLE", "08", nf=NUM)
    row("HUM_post", "Humans&: seed post-money", 4480, "$M", "L-102", "confirmed", "T2", "2026-01-20", "PB", "STABLE", "08", nf=NUM)
    row("HUM_hc", "Humans&: headcount (20-30; midpoint)", 25, "people", "L-102", "confirmed", "T2", "2026", "PB / TechCrunch", "QUARTERLY", "08", nf=CNT)
    row("META_capex_lo", "Meta: 2026 capex guidance, low", 125000, "$M", "L-095", "confirmed", "T2", "2026-04-29", "Fortune", "QUARTERLY", "08", nf=NUM)
    row("META_capex_hi", "Meta: 2026 capex guidance, high", 145000, "$M", "L-095", "confirmed", "T2", "2026-04-29", "Fortune", "QUARTERLY", "08", nf=NUM)
    row("META_scale", "Meta: Scale AI stake (49%)", 14300, "$M", "L-095", "confirmed", "T2", "2025-06", "CNBC via Fortune", "STABLE", "08", nf=NUM)
    row("META_pkg", "Meta: leader package over four years ('not inconceivable')", 100, "$M", "L-094", "confirmed", "T2", "2025-06-27", "TechCrunch", "STABLE", "08", nf=NUM)
    row("META_amd_GW", "Meta: AMD GPU agreement", 6, "GW", "L-060", "confirmed", "T1", "2026-02", "AMD 10-Q", "STABLE", "08", nf=CNT1)
    row("ANT_equity", "Anthropic (incumbent, for scale): equity-only raised", 124254, "$M", "L-007", "estimated", "T2", "2026-05-28", "sum of PB equity rounds", "STABLE", "08, 09", nf=NUM)
    row("ANT_contracts", "Anthropic: documented compute contracts", 324100, "$M", "cost-stack section 4a", "derived", "T1-T3", "2026-09-09", "Workbook A 09_Obligations B18", "STABLE", "08", nf=NUM)
    row("ANT_reported", "Anthropic: reported-$ incl. the unverified Google leg [VERIFY]", 524100, "$M", "L-155 + section 4a", "estimated", "T3 [VERIFY]", "2026-09-09", "Workbook A 09_Obligations B20", "STABLE", "08", nf=NUM, yellow=True)
    row("ANT_rr", "Anthropic: run-rate (GROSS)", 65000, "$M/yr", "L-032", "confirmed", "T2", "2026-07-31", "GROSS run-rate", "QUARTERLY", "08", nf=NUM)
    row("ANT_q1", "Anthropic: Q1-2026 revenue", 4730, "$M", "L-151", "confirmed", "T2", "Q1-2026", "recognized", "QUARTERLY", "08", nf=NUM)
    row("ANT_q2", "Anthropic: Q2-2026 revenue (preliminary)", 11600, "$M", "L-033", "confirmed", "T2", "Q2-2026", "recognized, preliminary", "QUARTERLY", "08", nf=NUM)
    row("ANT_adj", "Anthropic: Q2-2026 ADJUSTED operating income (non-GAAP; projection)", 559, "$M", "L-034, L-151, L-152", "confirmed (sign) / estimated", "T2 / T3", "Q2-2026", "non-GAAP adjusted; definition unpublished", "QUARTERLY", "08", nf=NUM)
    row("ANT_hc", "Anthropic: headcount (PB)", 5000, "people", "L-008", "confirmed", "T2", "2026-04-21", "PB", "QUARTERLY", "08", nf=CNT)
    row("ANT_val", "Anthropic: post-money mark", 965000, "$M", "L-005", "confirmed", "T2", "2026-05-28", "Series H post", "VOLATILE", "08", nf=NUM)
    row("ANT_burn_lo", "Anthropic: burn to the first positive adjusted result, low (derived, flagged)", 12000, "$M", "derived (cost-stack section 2; AM notes)", "estimated", "T4 (derived)", "2026-09-09", "~12,000-20,000 burned; flagged", "STABLE", "09", nf=NUM, yellow=True)
    row("ANT_burn_hi", "Anthropic: burn to the first positive adjusted result, high (derived, flagged)", 20000, "$M", "derived", "estimated", "T4 (derived)", "2026-09-09", "flagged", "STABLE", "09", nf=NUM, yellow=True)
    row("OAI_equity", "OpenAI (incumbent, for scale): equity-only raised", 181216.5, "$M", "L-022", "estimated", "T2", "2026-03-31", "sum of PB equity rounds", "STABLE", "08", nf=NUM1)
    row("OAI_contracts", "OpenAI: documented compute contracts", 480400, "$M", "cost-stack section 4b", "derived", "T1-T2", "2026-09-09", "Workbook A 09_Obligations B38", "STABLE", "08", nf=NUM)
    row("OAI_rr", "OpenAI: run-rate ('>40,000')", 40000, "$M/yr", "L-065", "confirmed", "T2", "2026-07", "basis unstated", "QUARTERLY", "08", nf=NUM)
    row("OAI_h1rev", "OpenAI: H1-2026 revenue", 12400, "$M", "L-066", "confirmed", "T2", "H1-2026", "5,700 + 6,700", "QUARTERLY", "08", nf=NUM)
    row("OAI_h1loss", "OpenAI: H1-2026 operating loss incl. SBC (magnitude)", 21600, "$M", "L-066", "confirmed", "T2", "H1-2026", "9,300 + 12,300", "QUARTERLY", "08", nf=NUM)
    row("OAI_hc", "OpenAI: headcount (PB)", 4500, "people", "L-027", "confirmed", "T2", "2026-03-21", "PB; plan 8,000 end-2026 (L-090)", "QUARTERLY", "08", nf=CNT)
    row("OAI_hc_plan", "OpenAI: headcount plan end-2026", 8000, "people", "L-090", "estimated", "T3", "2026-03-22", "Semafor", "QUARTERLY", "08", nf=CNT)
    row("OAI_val", "OpenAI: post-money mark", 852000, "$M", "L-019", "confirmed", "T2", "2026-03-31", "Mar-2026 round", "VOLATILE", "08", nf=NUM)
    sh.put(f"A{r+1}", "End of 01_Data (B).", kind="note")
    sh.ws.freeze_panes = "D4"


# ----------------------------------------------------------------------------------------------------
# 00_Assumptions (B)
# ----------------------------------------------------------------------------------------------------
def build_b00(sh):
    sh.put("A1", "00_Assumptions (Workbook B): timeline Y1-Y5 (D:H), scenario switch SW_GF (C4), switches SW_GF_BACKSTOP / SW_GF_REGION / SW_GF_MODELCLASS / SW_SSI, AJ drivers by scenario (yellow; columns D Lean / E Full / F VI; G live; H-I range), time-series drivers, unit constants, expected-magnitude bands (spec section 7.4) and reference-class bands (section 7.5).", kind="note")
    sh.put("A2", "Year index (numeric, typed once)", bold=True); sh.put("D2", 1, kind="input", nf=GEN, key="YB|1", align="center")
    for y in YRS[1:]:
        sh.put(f"{YB[y]}2", f"={YB[y-1]}2+1", kind="formula", nf=GEN, key=f"YB|{y}", align="center")
    sh.put("A3", "Timeline label", bold=True)
    for y in YRS:
        sh.put(f"{YB[y]}3", f'="Y"&{YB[y]}2', kind="formula", bold=True, align="center", key=f"YLB|{y}", border=B_TB)
    sh.put("A4", "Scenario switch SW_GF (1 Lean fast-follower / 2 Full frontier / 3 Vertically integrated with custom silicon)", bold=True)
    sh.put("C4", 2, kind="input", nf=GEN, name="SW_GF", key="SW_GF", align="center"); sh.put("D4", f'=CHOOSE(SW_GF,"{SCEN[1]}","{SCEN[2]}","{SCEN[3]}")', kind="formula", bold=True, key="GF_LABEL")
    sh.put("A5", "SW_GF_BACKSTOP: vendor backstop obtained for purchased clusters? (selector in D: 1 No / 2 Yes)", bold=True); sh.put("D5", 1, kind="input", nf=GEN, align="center"); sh.put("C5", '=CHOOSE(D5,"No","Yes")', kind="formula", bold=True, name="SW_GF_BACKSTOP", key="SW_GF_BACKSTOP"); sh.put("E5", "No = neocloud unsecured 9.0-9.75% (L-059); Yes = SPV A2 5.75% (L-044)", kind="note")
    sh.put("A6", "SW_GF_REGION: power price region for owned MW (selector: 1 Texas / 2 Virginia / 3 Ohio / 4 Norway AJ)", bold=True); sh.put("D6", 1, kind="input", nf=GEN, align="center"); sh.put("C6", '=CHOOSE(D6,"Texas","Virginia","Ohio","Norway")', kind="formula", bold=True, name="SW_GF_REGION", key="SW_GF_REGION"); sh.put("E6", "EIA industrial prices (L-108, T1); Norway AJ 40-60", kind="note")
    sh.put("A7", "SW_GF_MODELCLASS: serving model class for G20 (selector: 1 scenario default / 2 MoE-efficient / 3 dense-frontier)", bold=True); sh.put("D7", 1, kind="input", nf=GEN, align="center")
    sh.put("C7", '=IF(D7=1,CHOOSE(SW_GF,"MoE-efficient","dense-frontier","dense-frontier"),CHOOSE(D7-1,"MoE-efficient","dense-frontier"))', kind="formula", bold=True, name="SW_GF_MODELCLASS", key="SW_GF_MODELCLASS"); sh.put("E7", "Lean default MoE-efficient; Full and VI default dense-frontier (L-164 anchors)", kind="note")
    sh.put("A8", "SW_SSI (mirrored from Workbook A, C-08): SSI total raised (selector: 1 PB 7,000 / 2 press 8,000)", bold=True); sh.put("D8", 1, kind="input", nf=GEN, align="center"); sh.put("C8", f"=CHOOSE(D8,{R('SSI_pb')},{R('SSI_press')})", kind="formula", nf=NUM, bold=True, name="SW_SSI", key="SW_SSI")
    sh.header(10, ["AJ driver (scalar)", "Unit", "Tag (AJ · anchor)", "1 Lean", "2 Full", "3 VI", "Live (SW_GF)", "Range low", "Range high", "Note"])
    r = 11
    D = lambda *a, **k: drvB(sh, *a, **k)
    D(11, "GPU_PRICE", "Purchase price per GPU (Full: GB300 NVL72 mid rack / 72; VI: GB200 mid rack / 72)", "$ per GPU", "AJ · G01 (L-103, T4 index)", f"={R('A21z')}" if has_key("A21z") else 0, f"=AVERAGE({R('GB300_rack_lo')},{R('GB300_rack_hi')})/{R('GPUS_PER_RACK')}", f"=AVERAGE({R('GB200_rack_lo')},{R('GB200_rack_hi')})/{R('GPUS_PER_RACK')}", nf=CNT, lo=f"={R('GB200_rack_lo')}/{R('GPUS_PER_RACK')}", hi=f"={R('GB300_rack_hi')}/{R('GPUS_PER_RACK')}", note="Lean buys nothing")
    D(12, "LEASE_RATE", "Contracted GPU-hour rate (Lean/VI neocloud p25; Full hyperscaler p50)", "$ per GPU-hr", "AJ · G03 (L-105, T3)", f"={R('NEO_P25')}", f"={R('HYP_P50')}", f"={R('NEO_P25')}", nf=CNT2, lo=f"={R('NEO_P25')}", hi=f"={R('GB300_EX')}")
    D(13, "UTIL_CLUSTER", "Training-cluster utilization (G07)", "fraction", "AJ · G07 (no row): 70-85%", 0.75, 0.75, 0.75, nf=PCT, lo=0.70, hi=0.85)
    D(14, "UTIL_INF", "Inference utilization (G07)", "fraction", "AJ · G07 (no row): 40-70%", 0.55, 0.55, 0.55, nf=PCT, lo=0.40, hi=0.70)
    D(15, "DEBT_SHARE", "Debt share of purchased capex (Full 60%; VI AJ 60%)", "fraction", "AJ · spec section 7.3", 0, 0.60, 0.60, nf=PCT, lo=0.5, hi=0.7)
    D(16, "DEPR_YEARS", "GPU depreciation life (AJ)", "yrs", "AJ · spec section 7.3 (3 yrs)", 3, 3, 3, nf=CNT, lo=3, hi=5)
    D(17, "PRIN_YEARS", "Debt principal straight-line (AJ)", "yrs", "AJ · spec section 7.4 (4 yrs)", 4, 4, 4, nf=CNT, lo=4, hi=4)
    D(18, "NET_PCT", "Network fabric as share of purchased GPU BOM (G12)", "fraction", "AJ · G12 (L-111, T3): 5.8-8% Blackwell", 0, f"={R('NET_B200')}", f"={R('NET_B200')}", nf=PCT, lo=f"={R('NET_GB300')}", hi=f"={R('NET_hi')}")
    D(19, "STO_PCT", "Storage as share of cluster capex (G13, could-not-verify)", "fraction", "HOLE-class · G13 (L-112, CNV, T4): 2-5%", 0, 0.03, 0.03, nf=PCT, lo=f"={R('STO_lo')}", hi=f"={R('STO_hi')}", hole=True)
    D(20, "MW_PER_1000", "Facility MW per 1,000 GB200-class GPUs (G05)", "MW", "AJ · G05 (L-107, T3): 2.0-2.2", 2.1, 2.1, 2.1, nf=CNT2, lo=f"={R('MW_GB200_lo')}", hi=f"={R('MW_GB200_hi')}")
    D(21, "POWER_UTIL", "Power utilization of owned MW", "fraction", "AJ · G07", 0.70, 0.70, 0.70, nf=PCT, lo=0.70, hi=1.0)
    D(22, "COLO_RATE", "Powered-shell colocation rate for owned clusters (Beacon Point T1 as Base)", "$M per MW-yr", "AJ · G10 (L-167 T1; L-148 T1; L-136 T2): 1.76-2.4", f"={R('BP_rate')}", f"={R('BP_rate')}", f"={R('BP_rate')}", nf=CNT2, lo=f"={R('CS_rate')}", hi=f"={R('RIOT_rate')}")
    D(23, "BUILD_COST", "Greenfield build cost (G08)", "$M per MW", "AJ · G08 (L-109, T2); AI-dense 20 sensitivity", f"={R('BUILD')}", f"={R('BUILD')}", f"={R('BUILD')}", nf=CNT1, lo=f"={R('BUILD')}", hi=f"={R('BUILD_AI')}")
    D(24, "MW_TARGET", "Owned datacenter build target (VI: 1 GW-IT by Y4)", "MW", "AJ · spec section 7.3", 0, 0, 1000, nf=CNT, lo=1000, hi=1000)
    D(25, "G16", "Development multiple: total development compute = G16 x final-run compute", "x", "AJ · G16 (Epoch cost-share structure as colour, L-115): 3-5x", 3, 4, 4, nf=CNT1, lo=3, hi=5)
    D(26, "G17", "Failed-run allowance as share of final-run compute", "fraction", "AJ · G17 (no row): 30-50%", 0.30, 0.40, 0.40, nf=PCT, lo=0.30, hi=0.50)
    D(27, "LEAN_THRESH", "Frontier-class threshold for the Lean milestone: prior-generation class run (Llama 3.1-405B / GPT-4.5 pre-train, L-115); Full and VI use the current-year G14 path", "$M", "AJ · L-115 anchors; fast follower matches last generation", f"={R('LLAMA')}", 0, 0, nf=NUM, lo=f"={R('LLAMA')}", hi=f"={R('GPT45')}")
    D(28, "LIST_BLEND", "Blended list price realised on billed tokens (Opus 5 mix of input and output; G19)", "$ per MTok", "AJ · G19 (L-084, T1)", f"=AVERAGE({R('P_O5_in')},{R('P_O5_out')})/{R('UNIT15')}" if has_key("UNIT15") else f"=({R('P_O5_in')}+{R('P_O5_out')})/2", f"=({R('P_O5_in')}+{R('P_O5_out')})/2", f"=({R('P_O5_in')}+{R('P_O5_out')})/2", nf=CNT2, lo=f"={R('P_S5_in')}", hi=f"={R('P_F51_out')}", note="mid of Opus 5 input 5 and output 25 = 15; blended by a 1:1 token mix (AJ)")
    D(29, "DISC", "Discounting off list (enterprise, batch, cache)", "fraction", "AJ · spec section 7.3: 30-50%", 0.40, 0.40, 0.40, nf=PCT, lo=0.30, hi=0.50)
    D(30, "LEADER_SHARE", "Leaders as share of headcount (10% at 100 heads cannot hold at 3,000: AJ shrinks with scale)", "fraction", "AJ · spec section 7.3 (10% at Lean)", 0.10, 0.03, 0.02, nf=PCT, lo=0.02, hi=0.10)
    D(31, "LEADER_COMP", "Leader comp per head per year (G21: 5-25 typical; 25-100 at the extreme)", "$M/yr", "AJ · G21 (L-094, T2)", 15, 15, 15, nf=CNT1, lo=5, hi=25)
    D(32, "SENIOR_SHARE", "Senior IC share of headcount", "fraction", "AJ · spec section 7.3 (40%)", 0.40, 0.40, 0.40, nf=PCT, lo=0.30, hi=0.50)
    D(33, "SENIOR_COMP", "Senior IC total comp per head (G21 T4 band 0.5-1.5)", "$M/yr", "AJ · G21 (L-094 notes, T4)", 1.0, 1.0, 1.0, nf=CNT2, lo=f"={R('SEN_lo')}", hi=f"={R('SEN_hi')}")
    D(34, "ENG_COMP", "Engineer total comp per head (G21 T4 band 0.30-0.76)", "$M/yr", "AJ · G21 (L-092 notes, T4)", f"=AVERAGE({R('ENG_lo')},{R('ENG_hi')})", f"=AVERAGE({R('ENG_lo')},{R('ENG_hi')})", f"=AVERAGE({R('ENG_lo')},{R('ENG_hi')})", nf=CNT2, lo=f"={R('ENG_lo')}", hi=f"={R('ENG_hi')}")
    D(35, "SAFE_PCT", "Safety / eval as share of research headcount cost (G25)", "fraction", "AJ · G25 (L-117 CNV as colour): 3% / 5% / 5%", 0.03, 0.05, 0.05, nf=PCT, lo=f"={R('SAFE_sh_lo')}", hi=f"={R('SAFE_sh_hi')}")
    D(36, "LEGAL_RES", "Legal reserve per year (G26)", "$M/yr", "AJ · G26 (L-086, L-088 as colour): reserve 500-1,500 over 5 yrs", 100, 300, 300, nf=NUM, lo=f"={R('RES_lo')}/5", hi=f"={R('RES_hi')}/5")
    D(37, "LEGAL_COMP", "Compliance / policy per year (G26)", "$M/yr", "AJ · G26: 20-50", f"={R('COMPL_lo')}", f"={R('COMPL_hi')}", f"={R('COMPL_hi')}", nf=NUM, lo=f"={R('COMPL_lo')}", hi=f"={R('COMPL_hi')}")
    D(38, "GTM_PCT", "GTM and G&A as share of headcount cost (G27)", "fraction", "AJ · G27 (L-118 T4 mix as colour): Lean 20%; scenarios 2-3 40-60%", f"={R('GTM_lean')}", 0.50, 0.50, nf=PCT, lo=f"={R('GTM_lo')}", hi=f"={R('GTM_hi')}")
    D(39, "DATA_LIC", "Data licensing per year (G23)", "$M/yr", "AJ · G23 (L-113, T1): Lean 50-200; scenarios 2-3 300-1,000", 125, 650, 650, nf=NUM, lo=50, hi=1000)
    D(40, "ASIC_ANNUAL", "Custom ASIC program per year, NRE and team (G29; VI only)", "$M/yr", "AJ · G29 (no row): 1,000-3,000 for 3-4 yrs", 0, 0, 2000, nf=NUM, lo=f"={R('ASIC_lo')}", hi=f"={R('ASIC_hi')}")
    D(41, "ASIC_RISK", "First-silicon risk allowance on the ASIC program (G29)", "fraction", "AJ · G29", f"={R('ASIC_risk')}", f"={R('ASIC_risk')}", f"={R('ASIC_risk')}", nf=PCT, lo=0.30, hi=0.30)
    D(42, "ASIC_YEARS", "ASIC program years to first GA (G29: 3-4)", "yrs", "AJ · G29", 4, 4, 4, nf=CNT, lo=3, hi=4)
    D(43, "ASIC_SHARE", "Share of merchant GPUs replaced by the ASIC from Y5 (VI; vendor 'half cost' claim flagged)", "fraction", "AJ · spec section 7.3; G18 (L-050 vendor)", 0, 0, 0.30, nf=PCT, lo=0, hi=0.30)
    D(44, "ASIC_HALF", "ASIC cost relative to a GPU (vendor claim: half)", "fraction", "vendor claim · G18 (L-050, T1 vendor) · FLAGGED", f"={R('XPU_HALF')}", f"={R('XPU_HALF')}", f"={R('XPU_HALF')}", nf=PCT, lo=0.5, hi=1.0, hole=True)
    D(45, "ASIC_TEAM", "Share of VI headcount costed inside G29 (silicon team), excluded from the people line", "fraction", "AJ · spec section 7.3 ('ASIC team inside G29')", 0, 0, 0.10, nf=PCT, lo=0.05, hi=0.15)
    D(46, "PROB_1B", "AJ probability of reaching $1B net revenue by the milestone year", "fraction", "AJ · spec section 7.4: 30-50% / 60-80% / 60-80% (reference: TML, Mistral, SSI)", 0.40, 0.70, 0.70, nf=PCT, lo=0.30, hi=0.80)
    D(47, "REV1B", "Revenue milestone threshold ($1B net revenue)", "$M", "spec section 7.4", 1000, 1000, 1000, nf=NUM, lo=1000, hi=1000)
    D(48, "COST_DEBT", "Cost of debt for purchased clusters: SPV A2 5.75% if SW_GF_BACKSTOP = Yes, else neocloud unsecured midpoint 9.375% (VI: OEM equipment financing 7-8% shown as the range)", "fraction", "G04 (L-059 T1; L-044 T3; equipment AJ)",
      f'=IF(SW_GF_BACKSTOP="Yes",{R("SPV_A2")},{R("NEO_MID")})', f'=IF(SW_GF_BACKSTOP="Yes",{R("SPV_A2")},{R("NEO_MID")})', f'=IF(SW_GF_BACKSTOP="Yes",{R("SPV_A2")},{R("NEO_MID")})', nf=PCT2, lo=f"={R('SPV_A2')}", hi=f"={R('NEO2')}")
    sh.put("A50", "Unit constants: hours per year; $ per $M; seconds per hour; tokens per MTok; GPUs per 1,000; MW per GW; $ per $K; unit one; unit zero; 20% tolerance for the section 7.4 magnitude check; 'near' band for the xAI reference (0.5x-2x); 60% utilization for the G20 x1.67 line; 5% relative tolerance for the G20 checks", kind="note")
    for col, v, k in (("D", 8760, "HOURS"), ("E", 1000000, "MPERUSD"), ("F", 3600, "SECPERHR"), ("G", 1000000, "TOKPERMTOK"), ("H", 1000, "KGPU"), ("I", 1000, "MWPERGW"), ("J", 1000, "KPERUNIT"), ("K", 1, "UNITONE"), ("L", 0, "UNITZERO"), ("M", 0.20, "TOL20"), ("N", 0.5, "NEAR_LO"), ("O", 2.0, "NEAR_HI"), ("P", 0.6, "UTIL60"), ("Q", 0.05, "G20TOL")):
        sh.put(f"{col}50", v, kind="input", nf=GEN, key=k)

    sh.section(52, "TIME-SERIES AJ DRIVERS BY SCENARIO (live row = CHOOSE on SW_GF; scenario rows yellow)", ncols=10)
    sh.header(53, ["Driver", "Unit", "Tag", "Y1", "Y2", "Y3", "Y4", "Y5", "", "Note"])
    for y in YRS:
        sh.put(f"{YB[y]}53", f"={R(f'YLB|{y}')}", kind="link", bold=True, border=B_TB, align="center")
    r = 54
    r = drvB_ts(sh, r, "GPUS_LEASED", "GPUs leased (GB200/B200-class equivalents)", "GPUs", "AJ · spec section 7.3: Lean 25,000 -> 50,000; Full 100,000 -> 400,000 fleet with half purchased from Y2; VI merchant GPUs until the ASIC",
                {1: 25000, 2: 37500, 3: 50000, 4: 50000, 5: 50000}, {1: 100000, 2: 87500, 3: 125000, 4: 162500, 5: 200000}, {1: 50000, 2: 60000, 3: 80000, 4: 119000, 5: 119000}, nf=CNT)
    r = drvB_ts(sh, r, "GPUS_OWNED", "GPUs owned (cumulative; purchased at GPU_PRICE)", "GPUs", "AJ · spec section 7.3: Full 50% purchased from Y2; VI 240,000 in Y2 (500 MW), 476,000 by Y4 (1 GW-IT)",
                {y: 0 for y in YRS}, {1: 0, 2: 87500, 3: 125000, 4: 162500, 5: 200000}, {1: 0, 2: 240000, 3: 320000, 4: 476000, 5: 476000}, nf=CNT)
    r = drvB_ts(sh, r, "RUNS", "Lean: frontier-class final runs per year (capped by cluster size)", "runs", "AJ · spec section 7.3 (1 per year from Y2)", {1: 0, 2: 1, 3: 1, 4: 1, 5: 1}, {y: 0 for y in YRS}, {y: 0 for y in YRS}, nf=CNT)
    r = drvB_ts(sh, r, "BUDGET", "Full / VI: annual training budget (1,500 Y1 -> 7,000 Y3 = Anthropic 2026 -> 14,000 Y5; G15 ceiling)", "$M/yr", "AJ · spec section 7.3; G15 (L-125, T4)",
                {y: 0 for y in YRS}, {1: 1500, 2: 5500, 3: f"={R('ANT_T26')}", 4: 10500, 5: f"={R('ANT_T27')}"}, {1: 1500, 2: 5500, 3: f"={R('ANT_T26')}", 4: 10500, 5: f"={R('ANT_T27')}"}, nf=NUM,
                note="Y2 5,500 interpolated so the Y2 final-run-equivalent (budget / (G16 + G17)) reaches the current-year frontier (1,200), the spec's Full-frontier Y2 milestone")
    r = drvB_ts(sh, r, "REV", "Net revenue ramp (AJ; reference: TML 'a few hundred million' ~18 months in; Mistral 1,167 PB FY2026 ~3 yrs in)", "$M", "AJ · spec section 7.4 milestone years (Lean Y4 / Full Y3 / VI Y4 for $1B)",
                {1: 0, 2: 50, 3: 300, 4: 1000, 5: 2000}, {1: 0, 2: 200, 3: 1000, 4: 3000, 5: 6000}, {1: 0, 2: 100, 3: 500, 4: 1000, 5: 3000}, nf=NUM)
    r = drvB_ts(sh, r, "INFPCT", "Inference serving cost as % of revenue (64% Y1 anchor = OpenAI 2025, G18)", "fraction", "AJ · G18 (L-083, L-063): 64% -> 45% -> 35% (Lean); 64% -> 40% -> 30% (Full, VI)",
                {1: f"={R('INF_SHARE25')}", 2: f"={R('INF_SHARE25')}", 3: 0.45, 4: 0.40, 5: 0.35}, {1: f"={R('INF_SHARE25')}", 2: 0.55, 3: 0.40, 4: 0.35, 5: 0.30}, {1: f"={R('INF_SHARE25')}", 2: 0.55, 3: 0.40, 4: 0.35, 5: 0.30}, nf=PCT)
    r = drvB_ts(sh, r, "HC", "Research and engineering headcount (VI incl. DC ops; silicon team inside G29)", "people", "AJ · spec section 7.3: 100 -> 300; 500 -> 3,000; 800 -> 4,000",
                {1: 100, 2: 150, 3: 200, 4: 250, 5: 300}, {1: 500, 2: 1125, 3: 1750, 4: 2375, 5: 3000}, {1: 800, 2: 1600, 3: 2400, 4: 3200, 5: 4000}, nf=CNT)
    r = drvB_ts(sh, r, "RET", "Retention pool (G22: ~1,500 over two years = ~750 per year from Y3; scenarios 2-3)", "$M/yr", "AJ · G22 (L-093, L-166 T3/CNV)",
                {y: 0 for y in YRS}, {1: 0, 2: 0, 3: f"={R('RET_pp')}*{R('RET_n')}/{R('RET_yrs')}", 4: f"={R('RET_pp')}*{R('RET_n')}/{R('RET_yrs')}", 5: f"={R('RET_pp')}*{R('RET_n')}/{R('RET_yrs')}"},
                {1: 0, 2: 0, 3: f"={R('RET_pp')}*{R('RET_n')}/{R('RET_yrs')}", 4: f"={R('RET_pp')}*{R('RET_n')}/{R('RET_yrs')}", 5: f"={R('RET_pp')}*{R('RET_n')}/{R('RET_yrs')}"}, nf=NUM)
    r = drvB_ts(sh, r, "LABEL", "Expert data / labeling (G24: Lean 100-300; scenarios 2-3 1,000-3,000 by Y3)", "$M/yr", "AJ · G24 (L-114, T4)",
                {y: 200 for y in YRS}, {1: 500, 2: 1000, 3: 2000, 4: 2000, 5: 2000}, {1: 500, 2: 1000, 3: 2000, 4: 2000, 5: 2000}, nf=NUM)
    r = drvB_ts(sh, r, "BUILD_PH", "Greenfield build spend phasing (VI; 24-36 month lead time G09): first 500 MW by end-Y2, 1 GW by Y4", "fraction", "AJ · G09 (no row) · sums to 100%",
                {y: 0 for y in YRS}, {y: 0 for y in YRS}, {1: 0.10, 2: 0.50, 3: 0.25, 4: 0.15, 5: 0}, nf=PCT)
    sh.section(r + 1, "EXPECTED MAGNITUDES AT BASE (spec section 7.4; typed once; 09_Output checks within +/- 20%) and REFERENCE-CLASS BANDS (section 7.5)", ncols=10)
    sh.header(r + 2, ["Metric", "Unit", "Tag", "1 Lean low", "1 Lean high", "2 Full low", "2 Full high", "3 VI low", "3 VI high", "Note"])
    exp = [
        ("EXP_Y1", "Y1 cash out", 1000, 1500, 4000, 6000, 5000, 8000),
        ("EXP_Y2", "Y2 cash out (VI only stated)", None, None, None, None, 15000, 25000),
        ("EXP_FRONT", "Cumulative capital to the first frontier-class model", 2500, 4000, 12000, 18000, 25000, 40000),
        ("EXP_1B", "Cumulative capital to the first $1B net revenue", 5000, 8000, 20000, 30000, 40000, 60000),
        ("EXP_BE", "Cumulative capital to cash-flow breakeven", 8000, 15000, 60000, 100000, 80000, 150000),
        ("EXP_FRONT_Y", "Expected milestone year: first frontier-class model", 2, 2, 2, 2, 3, 3),
        ("EXP_1B_Y", "Expected milestone year: first $1B net revenue", 4, 4, 3, 3, 4, 4),
    ]
    rr = r + 3
    for k, lab, *vals in exp:
        sh.put(f"A{rr}", lab); sh.put(f"B{rr}", "$M" if not k.endswith("_Y") else "year", kind="note"); sh.put(f"C{rr}", "spec section 7.4", kind="note")
        for i, v in enumerate(vals):
            col = "DEFGHI"[i]
            if v is not None:
                sh.put(f"{col}{rr}", v, kind="input", nf=(NUM if not k.endswith("_Y") else GEN), key=f"{k}|{(i // 2) + 1}|{'lo' if i % 2 == 0 else 'hi'}")
        rr += 1
    sh.put(f"A{rr}", "Expected breakeven: Lean Y5 or never (Bear); Full beyond Y5 (Base); VI beyond Y5", kind="note"); rr += 1
    sh.put(f"A{rr}", "Reference-class band for Lean: entrants that raised 2,000-8,000 to a model with little revenue (TML seed / Reflection / SSI via SW_SSI / Mistral)"); sh.put(f"B{rr}", "$M", kind="note"); sh.put(f"C{rr}", "L-097, L-098, L-099, L-100", kind="note")
    sh.put(f"D{rr}", f"=MIN({R('TML_raised')},{R('REF_raised')},SW_SSI,{R('MIS_raised')})", kind="formula", nf=NUM, key="REF_LEAN_LO"); sh.put(f"E{rr}", f"=MAX({R('TML_raised')},{R('REF_raised')},SW_SSI,{R('MIS_raised')})", kind="formula", nf=NUM, key="REF_LEAN_HI"); rr += 1
    sh.put(f"A{rr}", "Reference-class band for Full frontier: below Anthropic's equity raised (124,254) and 'near' xAI's accumulated deficit (41,311) by Y4-Y5 (near = 0.5x-2x, AJ)"); sh.put(f"B{rr}", "$M", kind="note"); sh.put(f"C{rr}", "L-007, L-096; AJ near band", kind="note")
    sh.put(f"D{rr}", f"={R('XAI_deficit')}*{R('NEAR_LO')}", kind="formula", nf=NUM, key="REF_FULL_LO"); sh.put(f"E{rr}", f"=MIN({R('ANT_equity')},{R('XAI_deficit')}*{R('NEAR_HI')})", kind="formula", nf=NUM, key="REF_FULL_HI"); sh.put(f"F{rr}", f"={R('ANT_equity')}", kind="formula", nf=NUM, key="REF_FULL_CAP"); rr += 1
    sh.put(f"A{rr}", "Reference-class floor for Vertically integrated: at or above xAI's deficit plus its 2025 AI-segment debt by Y5"); sh.put(f"B{rr}", "$M", kind="note"); sh.put(f"C{rr}", "L-096", kind="note")
    sh.put(f"D{rr}", f"={R('XAI_deficit')}+{R('XAI_debt25')}", kind="formula", nf=NUM, key="REF_VI_MIN"); rr += 1
    sh.put(f"A{rr}", "Lease-vs-own expected (spec section 7.4): owning 1 GW-IT ~36,400 up front (17,600 build + 16,700 chips + 1,700 network + 500 storage) plus 400-620 per year of power; full-stack lease 12,500-16,300 per year; powered shell 1,760-2,400 per year; crossover ~2.5-3 years"); sh.put(f"B{rr}", "$M", kind="note"); sh.put(f"C{rr}", "spec section 7.4", kind="note")
    for col, v, k in (("D", 36400, "EXP_OWN"), ("E", 400, "EXP_POWER_LO"), ("F", 620, "EXP_POWER_HI"), ("G", 2.5, "EXP_CROSS_LO"), ("H", 3.0, "EXP_CROSS_HI")):
        sh.put(f"{col}{rr}", v, kind="input", nf=GEN, key=k)
    rr += 1
    sh.put(f"A{rr}", "G20 expected serving cost per million output tokens at 100% utilization (spec section 9): MoE on-demand 0.22; dense on-demand 13-21"); sh.put(f"C{rr}", "spec section 9", kind="note")
    for col, v, k in (("D", 0.22, "EXP_G20_MOE"), ("E", 13, "EXP_G20_DENSE_LO"), ("F", 21, "EXP_G20_DENSE_HI")):
        sh.put(f"{col}{rr}", v, kind="input", nf=GEN, key=k)
    sh.ws.freeze_panes = "D4"


# ----------------------------------------------------------------------------------------------------
# model tabs (one block per scenario)
# ----------------------------------------------------------------------------------------------------
BH = 22  # block height


def blockhdr(sh, r0, s, title):
    sh.section(r0, f"SCENARIO {SCEN[s]}: {title}", ncols=10)
    sh.put(f"A{r0+1}", "Line", kind="header"); sh.put(f"B{r0+1}", "Unit", kind="header"); sh.put(f"C{r0+1}", "Source / driver", kind="header")
    for y in YRS:
        sh.put(f"{YB[y]}{r0+1}", f"={R(f'YLB|{y}')}", kind="link", bold=True, border=B_TB, align="center")
    return r0 + 2


def build_b02(sh):
    sh.put("A1", "02_Compute: chips by SKU and count (leased vs owned), buy vs lease, financing (SW_GF_BACKSTOP), depreciation, the economic capacity cost used by 04_Training. One block per scenario; live block = SW_GF.", kind="note")
    for s in (1, 2, 3):
        r0 = 3 + (s - 1) * BH
        r = blockhdr(sh, r0, s, "compute fleet and financing")
        line(sh, r, "CMP_LEASED", s, "GPUs leased", "GPUs", "GPUS_LEASED", {y: f"={dy('GPUS_LEASED', s, y)}" for y in YRS}, nf=CNT)
        line(sh, r + 1, "CMP_OWNED", s, "GPUs owned (cumulative)", "GPUs", "GPUS_OWNED", {y: f"={dy('GPUS_OWNED', s, y)}" for y in YRS}, nf=CNT)
        line(sh, r + 2, "CMP_PURCH", s, "GPU purchases in the year", "GPUs", "derived", {y: (f"={YB[y]}{r+1}" if y == 1 else f"={YB[y]}{r+1}-{YB[y-1]}{r+1}") for y in YRS}, nf=CNT)
        line(sh, r + 3, "CMP_PRICE", s, "Price per GPU (G01)", "$", "GPU_PRICE", {y: f"={d('GPU_PRICE', s)}" for y in YRS}, nf=CNT)
        line(sh, r + 4, "CMP_CAPEX", s, "Purchased chips ($M)", "$M", "= purchases x price / 1e6", {y: f"={YB[y]}{r+2}*{YB[y]}{r+3}/{R('MPERUSD')}" for y in YRS}, bold=True)
        line(sh, r + 5, "CMP_NET", s, "Network fabric capex (G12 % of GPU BOM)", "$M", "NET_PCT", {y: f"={YB[y]}{r+4}*{d('NET_PCT', s)}" for y in YRS})
        line(sh, r + 6, "CMP_STO", s, "Storage capex (G13 % of cluster capex; could-not-verify)", "$M", "STO_PCT (flagged)", {y: f"=({YB[y]}{r+4}+{YB[y]}{r+5})*{d('STO_PCT', s)}" for y in YRS})
        line(sh, r + 7, "CMP_RATE", s, "Contracted lease rate (G03)", "$ per GPU-hr", "LEASE_RATE", {y: f"={d('LEASE_RATE', s)}" for y in YRS}, nf=CNT2)
        line(sh, r + 8, "CMP_UTIL", s, "Cluster utilization (G07)", "fraction", "UTIL_CLUSTER", {y: f"={d('UTIL_CLUSTER', s)}" for y in YRS}, nf=PCT)
        line(sh, r + 9, "CMP_LEASE", s, "Compute lease cost ($M) = leased x rate x 8,760 x utilization / 1e6", "$M", "spec section 7.4", {y: f"={YB[y]}{r}*{YB[y]}{r+7}*{R('HOURS')}*{YB[y]}{r+8}/{R('MPERUSD')}" for y in YRS}, bold=True)
        dep = {}
        for y in YRS:
            terms = [f"{YB[k]}{r+4}" for k in range(max(1, y - 2), y + 1)]
            dep[y] = f"=({'+'.join(terms)})/{d('DEPR_YEARS', s)}"
        line(sh, r + 10, "CMP_DEPR", s, "Depreciation of owned GPUs (3-yr straight line, economic cost; not a cash line)", "$M", "DEPR_YEARS", dep)
        asic = {y: f"={R('UNITONE')}" for y in YRS}
        if s == 3:
            asic[5] = f"={R('UNITONE')}-{d('ASIC_SHARE', s)}*({R('UNITONE')}-{d('ASIC_HALF', s)})"
        line(sh, r + 11, "CMP_ASICF", s, "ASIC cost factor on owned-cluster cost (VI Y5: 1 - 30% x (1 - 0.5); vendor claim flagged)", "factor", "ASIC_SHARE, ASIC_HALF", asic, nf=DEC2)
        line(sh, r + 12, "CMP_DRAW", s, "Debt drawn = (chips + network + storage) x debt share", "$M", "DEBT_SHARE", {y: f"=({YB[y]}{r+4}+{YB[y]}{r+5}+{YB[y]}{r+6})*{d('DEBT_SHARE', s)}" for y in YRS})
        prin = {}
        for y in YRS:
            terms = [f"{YB[k]}{r+12}" for k in range(max(1, y - 4), y)]
            prin[y] = (f"=({'+'.join(terms)})/{d('PRIN_YEARS', s)}" if terms else f"={R('UNITZERO')}")
        line(sh, r + 13, "CMP_PRIN", s, "Principal repayment (straight-line over 4 yrs from the year after drawdown)", "$M", "PRIN_YEARS", prin)
        line(sh, r + 14, "CMP_DEBT", s, "Debt outstanding (end of year)", "$M", "derived", {y: (f"={YB[y]}{r+12}-{YB[y]}{r+13}" if y == 1 else f"={YB[y-1]}{r+14}+{YB[y]}{r+12}-{YB[y]}{r+13}") for y in YRS}, bold=True)
        line(sh, r + 15, "CMP_RDEBT", s, "Cost of debt (SW_GF_BACKSTOP)", "fraction", "COST_DEBT", {y: f"={d('COST_DEBT', s)}" for y in YRS}, nf=PCT2)
        line(sh, r + 16, "CMP_INT", s, "Interest on the opening balance", "$M", "derived", {y: (f"={R('UNITZERO')}" if y == 1 else f"={YB[y-1]}{r+14}*{YB[y]}{r+15}") for y in YRS})
        line(sh, r + 17, "CMP_MW", s, "Owned facility MW = owned GPUs / 1,000 x MW per 1,000 (G05)", "MW", "MW_PER_1000", {y: f"={YB[y]}{r+1}/{R('KGPU')}*{d('MW_PER_1000', s)}" for y in YRS}, nf=CNT1)
        line(sh, r + 18, "CMP_CAP", s, "Economic capacity cost = lease + depreciation x ASIC factor + colocation + power (03_Facility)", "$M", "feeds 04_Training", {y: f"={YB[y]}{r+9}+{YB[y]}{r+10}*{YB[y]}{r+11}+'03_Facility'!{YB[y]}{3 + (s-1)*BH + 2 + 4}+'03_Facility'!{YB[y]}{3 + (s-1)*BH + 2 + 3}" for y in YRS}, bold=True)
    sh.put(f"A{3 + 3*BH}", "Owned-vs-leased: Full buys half its fleet from Y2 at the GB300 rack price; VI buys 80% at the GB200 rack price and builds; Lean leases everything (no debt).", kind="note")
    sh.ws.freeze_panes = "D3"


def build_b03(sh):
    sh.put("A1", "03_Facility: power (MW, $/MWh by SW_GF_REGION, utilization), colocation vs greenfield build (VI), lease-vs-own reference lines. One block per scenario.", kind="note")
    for s in (1, 2, 3):
        r0 = 3 + (s - 1) * BH
        r = blockhdr(sh, r0, s, "facility, power, build")
        cr = 3 + (s - 1) * BH + 2  # compute block first line row
        line(sh, r, "FAC_MW", s, "Owned facility MW (02_Compute)", "MW", "02_Compute", {y: f"='02_Compute'!{YB[y]}{cr+17}" for y in YRS}, nf=CNT1)
        line(sh, r + 1, "FAC_ELEC", s, "Electricity price by region (SW_GF_REGION; EIA T1; Norway AJ)", "$ per MWh", "G06 (L-108)", {y: f'=IF(SW_GF_REGION="Texas",{R("EIA_TX")},IF(SW_GF_REGION="Virginia",{R("EIA_VA")},IF(SW_GF_REGION="Ohio",{R("EIA_OH")},{R("NOR_AJ")})))' for y in YRS}, nf=CNT1)
        line(sh, r + 2, "FAC_PUTIL", s, "Power utilization of owned MW", "fraction", "POWER_UTIL", {y: f"={d('POWER_UTIL', s)}" for y in YRS}, nf=PCT)
        line(sh, r + 3, "FAC_POWER", s, "Power cost = MW x 8,760 x utilization x $/MWh / 1e6", "$M", "spec section 7.3", {y: f"={YB[y]}{r}*{R('HOURS')}*{YB[y]}{r+2}*{YB[y]}{r+1}/{R('MPERUSD')}" for y in YRS}, bold=True)
        cum = {y: f"={d('MW_TARGET', s)}*SUM({''.join([])}{YB[1]}{r+6}:{YB[y]}{r+6})" for y in YRS}
        line(sh, r + 4, "FAC_COLO", s, "Colocation powered shell for owned MW not yet in an own-built hall = MAX(0, owned MW - built MW) x rate (G10)", "$M", "COLO_RATE (Beacon Point 1.86)", {y: f"=MAX(0,{YB[y]}{r}-{YB[y]}{r+7})*{d('COLO_RATE', s)}" for y in YRS}, bold=True)
        line(sh, r + 5, "FAC_BUILD", s, "Greenfield build spend = MW target x build cost x phasing (VI)", "$M", "BUILD_COST, BUILD_PH", {y: f"={d('MW_TARGET', s)}*{d('BUILD_COST', s)}*{YB[y]}{r+6}" for y in YRS}, bold=True)
        line(sh, r + 6, "FAC_PH", s, "Build phasing", "fraction", "BUILD_PH", {y: f"={dy('BUILD_PH', s, y)}" for y in YRS}, nf=PCT)
        line(sh, r + 7, "FAC_BUILTMW", s, "Built MW (cumulative)", "MW", "derived", {y: f"={d('MW_TARGET', s)}*SUM($D{r+6}:{YB[y]}{r+6})" for y in YRS}, nf=CNT)
        line(sh, r + 8, "FAC_FSEQ", s, "Reference: full-stack lease equivalent of the owned MW (Volta 12.5 to Nscale 16.3 per MW-yr; midpoint)", "$M/yr", "G11 (L-134)", {y: f"={YB[y]}{r}*AVERAGE({R('FS_VOLTA')},{R('FS_NSCALE')})" for y in YRS})
        line(sh, r + 9, "FAC_SHELLEQ", s, "Reference: powered-shell-only equivalent of the owned MW", "$M/yr", "G10", {y: f"={YB[y]}{r}*{d('COLO_RATE', s)}" for y in YRS})
    sh.put(f"A{3 + 3*BH}", "Lead time (G09, AJ): 24-36 months greenfield, 9-18 months colocation fit-out: the VI build phases 10 / 50 / 25 / 15% over Y1-Y4 so the first 500 MW lands by end-Y2 and 1 GW by Y4.", kind="note")
    sh.ws.freeze_panes = "D3"


def build_b04(sh):
    sh.put("A1", "04_Training: runs by generation (G14 path), training demand vs cluster capacity, the development premium (experiments and failed runs bought beyond the cluster), the final-run-equivalent and the first frontier-class model milestone. One block per scenario.", kind="note")
    for s in (1, 2, 3):
        r0 = 3 + (s - 1) * BH
        r = blockhdr(sh, r0, s, "training runs and the frontier milestone")
        cr = 3 + (s - 1) * BH + 2
        line(sh, r, "TRN_G14", s, "Frontier final-run cost path (G14: Grok 4 ~500 in Y1, x 2.4 per year)", "$M", "G14 (L-115, T3)", {y: f"={R('GROK4')}*{R('GROWTH')}^({R(f'YB|{y}')}-{R('UNITONE')})" for y in YRS})
        if s == 1:
            th = {y: f"={d('LEAN_THRESH', s)}" for y in YRS}
        else:
            th = {y: f"={YB[y]}{r}" for y in YRS}
        line(sh, r + 1, "TRN_TH", s, "Frontier-class threshold for the milestone (Lean: prior-generation class 170, AJ; Full and VI: current-year G14)", "$M", "LEAN_THRESH / G14", th)
        if s == 1:
            line(sh, r + 2, "TRN_DEM", s, "Training demand = runs x threshold x (G16 + G17) (Lean; capped by cluster size below)", "$M", "RUNS, G16, G17", {y: f"={dy('RUNS', s, y)}*{YB[y]}{r+1}*({d('G16', s)}+{d('G17', s)})" for y in YRS})
        else:
            line(sh, r + 2, "TRN_DEM", s, "Training demand = annual training budget (Full / VI)", "$M", "BUDGET (G15 ceiling)", {y: f"={dy('BUDGET', s, y)}" for y in YRS})
        line(sh, r + 3, "TRN_INF", s, "Inference serving cost (05_Inference)", "$M", "05_Inference", {y: f"='05_Inference'!{YB[y]}{cr+6}" for y in YRS})
        line(sh, r + 4, "TRN_CAP", s, "Economic capacity cost of the cluster (02_Compute)", "$M", "02_Compute", {y: f"='02_Compute'!{YB[y]}{cr+18}" for y in YRS})
        line(sh, r + 5, "TRN_IN", s, "Training compute served inside the cluster = MIN(demand, MAX(0, capacity - inference))", "$M", "derived", {y: f"=MIN({YB[y]}{r+2},MAX(0,{YB[y]}{r+4}-{YB[y]}{r+3}))" for y in YRS})
        if s == 1:
            line(sh, r + 6, "TRN_PREM", s, "Training development premium bought beyond the cluster (Lean: none, capped by cluster size)", "$M", "spec section 7.3", {y: f"={R('UNITZERO')}" for y in YRS}, bold=True)
        else:
            line(sh, r + 6, "TRN_PREM", s, "Training development premium bought beyond the cluster = MAX(0, demand + inference - capacity)", "$M", "spec section 7.4", {y: f"=MAX(0,{YB[y]}{r+2}+{YB[y]}{r+3}-{YB[y]}{r+4})" for y in YRS}, bold=True)
        line(sh, r + 7, "TRN_FINAL", s, "Final-run-equivalent compute = (in-cluster + premium) / (G16 + G17)", "$M", "G16, G17", {y: f"=({YB[y]}{r+5}+{YB[y]}{r+6})/({d('G16', s)}+{d('G17', s)})" for y in YRS}, bold=True)
        if s == 3:
            oper = {y: (f"={R('UNITZERO')}" if y == 1 else f"=IF('02_Compute'!{YB[y-1]}{cr+1}>0,{R('UNITONE')},{R('UNITZERO')})") for y in YRS}
            line(sh, r + 8, "TRN_OPER", s, "Owned cluster operational (VI: purchased the year before; the cluster lands Y2-Y3)", "1/0", "spec section 7.4", oper, nf=GEN)
        else:
            line(sh, r + 8, "TRN_OPER", s, "Cluster available (leased capacity from Y1)", "1/0", "spec section 7.3", {y: f"={R('UNITONE')}" for y in YRS}, nf=GEN)
        line(sh, r + 9, "TRN_HIT", s, "Frontier-class run completed this year (final-run-equivalent >= threshold and cluster available)", "1/0", "derived", {y: f"=IF(AND({YB[y]}{r+7}>={YB[y]}{r+1},{YB[y]}{r+8}={R('UNITONE')}),{R('UNITONE')},{R('UNITZERO')})" for y in YRS}, nf=GEN)
        sh.put(f"A{r+10}", "First frontier-class model: year index (MATCH on the row above)", bold=True); sh.put(f"D{r+10}", f'=IFERROR(MATCH({R("UNITONE")},D{r+9}:H{r+9},0),"beyond Y5")', kind="output", nf=GEN, key=f"TRN_FIRST|{s}")
        sh.put(f"E{r+10}", "expected: Lean Y2; Full Y2; VI Y3 (spec section 7.4)", kind="note")
        sh.put(f"A{r+11}", "Runs per year (Lean) / budget path (Full, VI), for reference", kind="note")
        for y in YRS:
            sh.put(f"{YB[y]}{r+11}", (f"={dy('RUNS', s, y)}" if s == 1 else f"={dy('BUDGET', s, y)}"), kind="formula", nf=(CNT if s == 1 else NUM))
    sh.put(f"A{3 + 3*BH}", "Per-run reference (G14, L-115): GPT-4 ~78; Gemini Ultra ~191; Llama 3.1-405B ~170; Grok 4 ~500; GPT-4.5 ~200 pre-train + ~2 post-train; growth 2.4x/yr; >1,000 by 2027. Cost shares: hardware 47-67%, R&D staff 29-49%, energy 2-6%.", kind="note")
    sh.ws.freeze_panes = "D3"


def build_b05(sh):
    sh.put("A1", "05_Inference: net revenue ramp, billed tokens, serving cost as % of revenue (the driver at Base) and the G20 unit-cost cross-check (L-164 throughput x GPU-hour rate x utilization; never a disclosed COGS). One block per scenario; G20 table at the top.", kind="note")
    sh.section(3, "G20 SERVING COST PER MILLION OUTPUT TOKENS (estimate): rate / (tokens per second per GPU x 3,600 x utilization / 1e6)", ncols=10)
    sh.header(4, ["Model class / benchmark", "tok/s/GPU", "M tokens per GPU-hr", "$/MTok on-demand 10.50 (100%)", "$/MTok contracted 2.40 (100%)", "$/MTok contracted 4.00 (100%)", "$/MTok on-demand at 60% util", "$/MTok contracted 2.40 at 60%", "Check", "Source"])
    g20 = [(5, "MoE-efficient: SGLang GB200 NVL72 DeepSeek V3/R1 output", "MOE_OUT", "EXP_G20_MOE"), (6, "MoE server-mode: MLPerf v5.1 GB300 NVL72 DeepSeek-R1", "MLPERF_SRV", None),
           (7, "Dense-frontier: GB200 NVL72 Llama 3.1 405B offline", "DENSE_OFF", "EXP_G20_DENSE_LO"), (8, "Dense-frontier: GB200 NVL72 Llama 3.1 405B interactive", "DENSE_INT", "EXP_G20_DENSE_HI")]
    for rr, lab, k, chk in g20:
        sh.put(f"A{rr}", lab); sh.put(f"B{rr}", f"={R(k)}", kind="formula", nf=CNT); sh.put(f"C{rr}", f"=B{rr}*{R('SECPERHR')}/{R('TOKPERMTOK')}", kind="formula", nf=CNT2)
        sh.put(f"D{rr}", f"={R('CW_GB200')}/C{rr}", kind="formula", nf=CNT2, bold=True, key=f"G20_OD_{k}"); sh.put(f"E{rr}", f"={R('NEO_P25')}/C{rr}", kind="formula", nf=CNT2, key=f"G20_C24_{k}"); sh.put(f"F{rr}", f"={R('GB300_EX')}/C{rr}", kind="formula", nf=CNT2, key=f"G20_C40_{k}")
        sh.put(f"G{rr}", f"=D{rr}/{R('UTIL60')}", kind="formula", nf=CNT2); sh.put(f"H{rr}", f"=E{rr}/{R('UTIL60')}", kind="formula", nf=CNT2)
        if chk:
            sh.put(f"I{rr}", f'=IF(ABS(D{rr}-{R(chk)})<={R(chk)}*{R("G20TOL")},"PASS","FAIL: "&TEXT(D{rr},"0.00"))', kind="formula", bold=True, key=f"PF_{chk}")
        sh.put(f"J{rr}", "L-164 · confirmed · T2; rates L-104 T1 / L-105 T3", kind="note")
    sh.put("A9", "Frontier proprietary models are not benchmarked; the dense-405B case is the closer proxy for them (flag). Print any $/MTok as an ESTIMATE with the throughput, the rate and the utilization in the sentence.", kind="note")
    for s in (1, 2, 3):
        r0 = 12 + (s - 1) * BH
        r = blockhdr(sh, r0, s, "inference revenue and serving cost")
        line(sh, r, "INF_REV", s, "Net revenue (AJ ramp)", "$M", "REV", {y: f"={dy('REV', s, y)}" for y in YRS}, bold=True)
        line(sh, r + 1, "INF_LIST", s, "Blended list price (G19)", "$ per MTok", "LIST_BLEND", {y: f"={d('LIST_BLEND', s)}" for y in YRS}, nf=CNT2)
        line(sh, r + 2, "INF_DISC", s, "Discount off list", "fraction", "DISC", {y: f"={d('DISC', s)}" for y in YRS}, nf=PCT)
        line(sh, r + 3, "INF_NET", s, "Net price per MTok", "$ per MTok", "derived", {y: f"={YB[y]}{r+1}*({R('UNITONE')}-{YB[y]}{r+2})" for y in YRS}, nf=CNT2)
        line(sh, r + 4, "INF_TOK", s, "Billed tokens (billions) = revenue x 1e6 / net price / 1,000", "B tokens", "derived", {y: f"=IFERROR({YB[y]}{r}*{R('MPERUSD')}/{YB[y]}{r+3}/{R('KPERUNIT')},0)" for y in YRS}, nf=CNT)
        line(sh, r + 5, "INF_PCT", s, "Inference serving cost as % of revenue (AJ path; Y1 = OpenAI 2025 64%)", "fraction", "INFPCT", {y: f"={dy('INFPCT', s, y)}" for y in YRS}, nf=PCT)
        cr = 3 + (s - 1) * BH + 2
        line(sh, r + 6, "INF_COST", s, "Inference serving cost = revenue x % (VI Y5 x ASIC factor)", "$M", "derived", {y: f"={YB[y]}{r}*{YB[y]}{r+5}*'02_Compute'!{YB[y]}{cr+11}" for y in YRS}, bold=True)
        line(sh, r + 7, "INF_TOKS", s, "G20 throughput for the model class in use (SW_GF_MODELCLASS)", "tok/s/GPU", "L-164", {y: f'=IF(SW_GF_MODELCLASS="MoE-efficient",{R("MOE_OUT")},{R("DENSE_OFF")})' for y in YRS}, nf=CNT)
        line(sh, r + 8, "INF_UNIT", s, "G20 unit cost at the scenario contracted rate and inference utilization ($ per MTok)", "$ per MTok", "G20 x G03 x G07", {y: f"={d('LEASE_RATE', s)}/({YB[y]}{r+7}*{R('SECPERHR')}*{d('UTIL_INF', s)}/{R('TOKPERMTOK')})" for y in YRS}, nf=CNT2)
        line(sh, r + 9, "INF_G20COST", s, "Cross-check: serving cost implied by G20 = billed tokens x unit cost", "$M", "derived", {y: f"={YB[y]}{r+4}*{R('KPERUNIT')}*{YB[y]}{r+8}/{R('MPERUSD')}" for y in YRS})
        line(sh, r + 10, "INF_GM", s, "Cross-check: implied serving gross margin = 1 - unit cost / net price", "fraction", "derived", {y: f"=IFERROR({R('UNITONE')}-{YB[y]}{r+8}/{YB[y]}{r+3},0)" for y in YRS}, nf=PCT)
        line(sh, r + 11, "INF_FLAG1B", s, "Revenue at or above the $1B threshold (1/0)", "1/0", "REV1B", {y: f"=IF({YB[y]}{r}>={d('REV1B', s)},{R('UNITONE')},{R('UNITZERO')})" for y in YRS}, nf=GEN)
        sh.put(f"A{r+12}", "First $1B net revenue: year index", bold=True); sh.put(f"D{r+12}", f'=IFERROR(MATCH({R("UNITONE")},D{r+11}:H{r+11},0),"not by Y5")', kind="output", nf=GEN, key=f"INF_FIRST1B|{s}")
        sh.put(f"E{r+12}", f"={d('PROB_1B', s)}", kind="formula", nf=PCT); sh.put(f"F{r+12}", "AJ probability of achieving it (reference: TML, Mistral, SSI)", kind="note")
    sh.ws.freeze_panes = "D3"


def build_b06(sh):
    sh.put("A1", "06_People_Other: R&E headcount by band with comp (G21), retention (G22), data licensing and labeling (G23-G24), safety (G25), legal (G26), GTM and G&A (G27), the ASIC program (G29). One block per scenario.", kind="note")
    for s in (1, 2, 3):
        r0 = 3 + (s - 1) * BH
        r = blockhdr(sh, r0, s, "people and other opex")
        line(sh, r, "PPL_HC", s, "Headcount", "people", "HC", {y: f"={dy('HC', s, y)}" for y in YRS}, nf=CNT)
        line(sh, r + 1, "PPL_BLEND", s, "Blended comp per head = leader share x leader comp + senior share x senior comp + engineer share x engineer comp", "$M/yr", "G21 bands", {y: f"={d('LEADER_SHARE', s)}*{d('LEADER_COMP', s)}+{d('SENIOR_SHARE', s)}*{d('SENIOR_COMP', s)}+({R('UNITONE')}-{d('LEADER_SHARE', s)}-{d('SENIOR_SHARE', s)})*{d('ENG_COMP', s)}" for y in YRS}, nf=CNT2)
        line(sh, r + 2, "PPL_COST", s, "People cost = headcount x blended comp (VI: excluding the silicon team inside G29)", "$M", "derived", {y: f"={YB[y]}{r}*{YB[y]}{r+1}*({R('UNITONE')}-{d('ASIC_TEAM', s)})" for y in YRS}, bold=True)
        line(sh, r + 3, "PPL_RET", s, "Retention pool (G22)", "$M", "RET", {y: f"={dy('RET', s, y)}" for y in YRS})
        line(sh, r + 4, "PPL_DATA", s, "Data licensing (G23)", "$M", "DATA_LIC", {y: f"={d('DATA_LIC', s)}" for y in YRS})
        line(sh, r + 5, "PPL_LABEL", s, "Expert data / labeling (G24)", "$M", "LABEL", {y: f"={dy('LABEL', s, y)}" for y in YRS})
        line(sh, r + 6, "PPL_SAFE", s, "Safety / eval = people cost x share (G25)", "$M", "SAFE_PCT", {y: f"={YB[y]}{r+2}*{d('SAFE_PCT', s)}" for y in YRS})
        line(sh, r + 7, "PPL_LEGAL", s, "Legal reserve + compliance (G26)", "$M", "LEGAL_RES, LEGAL_COMP", {y: f"={d('LEGAL_RES', s)}+{d('LEGAL_COMP', s)}" for y in YRS})
        line(sh, r + 8, "PPL_GTM", s, "GTM and G&A = people cost x share (G27)", "$M", "GTM_PCT", {y: f"={YB[y]}{r+2}*{d('GTM_PCT', s)}" for y in YRS})
        line(sh, r + 9, "PPL_ASIC", s, "Custom ASIC program (G29; VI Y1-Y4) = annual x (1 + risk allowance)", "$M", "ASIC_ANNUAL, ASIC_RISK, ASIC_YEARS", {y: f"=IF({R(f'YB|{y}')}<={d('ASIC_YEARS', s)},{d('ASIC_ANNUAL', s)}*({R('UNITONE')}+{d('ASIC_RISK', s)}),{R('UNITZERO')})" for y in YRS})
        line(sh, r + 10, "PPL_TOTAL", s, "People and other, total", "$M", "sum", {y: f"={YB[y]}{r+2}+SUM({YB[y]}{r+3}:{YB[y]}{r+9})" for y in YRS}, bold=True)
    sh.put(f"A{3 + 3*BH}", "Leader share shrinks with scale (10% at 100 heads; 3% at 3,000; 2% at 4,000): the spec's '10% leaders at 5-25M' cannot hold at incumbent scale (OpenAI 4,500-8,000 heads at 0.6-1.0M average, Workbook A 03_Costs).", kind="note")
    sh.ws.freeze_panes = "D3"


def build_b07(sh):
    sh.put("A1", "07_Cash: time-phased five-year cash out by line, revenue, net cash out, debt drawn and serviced, equity-only and equity-plus-debt cumulative capital, milestone triggers (Exhibit E18; A5:H82: Lean A5:H30, Full A31:H56, VI A57:H82).", kind="note")
    BH7 = 26
    for s in (1, 2, 3):
        r0 = 5 + (s - 1) * BH7
        sh.section(r0, f"SCENARIO {SCEN[s]}: annual cash out ($M)", ncols=10)
        sh.put(f"A{r0+1}", "Line", kind="header"); sh.put(f"B{r0+1}", "Unit", kind="header"); sh.put(f"C{r0+1}", "Source tab", kind="header")
        for y in YRS:
            sh.put(f"{YB[y]}{r0+1}", f"={R(f'YLB|{y}')}", kind="link", bold=True, border=B_TB, align="center")
        r = r0 + 2
        cr = 3 + (s - 1) * BH + 2; ir = 12 + (s - 1) * BH + 2
        lines = [
            ("CSH_LEASE", "Compute lease", "02_Compute", lambda y: f"='02_Compute'!{YB[y]}{cr+9}"),
            ("CSH_CHIPS", "Purchased chips", "02_Compute", lambda y: f"='02_Compute'!{YB[y]}{cr+4}"),
            ("CSH_NET", "Network", "02_Compute", lambda y: f"='02_Compute'!{YB[y]}{cr+5}"),
            ("CSH_STO", "Storage (could-not-verify)", "02_Compute", lambda y: f"='02_Compute'!{YB[y]}{cr+6}"),
            ("CSH_BUILD", "DC build (greenfield)", "03_Facility", lambda y: f"='03_Facility'!{YB[y]}{cr+5}"),
            ("CSH_COLO", "Colocation powered shell", "03_Facility", lambda y: f"='03_Facility'!{YB[y]}{cr+4}"),
            ("CSH_POWER", "Power", "03_Facility", lambda y: f"='03_Facility'!{YB[y]}{cr+3}"),
            ("CSH_PREM", "Training development premium", "04_Training", lambda y: f"='04_Training'!{YB[y]}{cr+6}"),
            ("CSH_INF", "Inference serving cost", "05_Inference", lambda y: f"='05_Inference'!{YB[y]}{ir+6}"),
            ("CSH_PPL", "People", "06_People_Other", lambda y: f"='06_People_Other'!{YB[y]}{cr+2}"),
            ("CSH_RET", "Retention", "06_People_Other", lambda y: f"='06_People_Other'!{YB[y]}{cr+3}"),
            ("CSH_DATA", "Data licensing + labeling", "06_People_Other", lambda y: f"='06_People_Other'!{YB[y]}{cr+4}+'06_People_Other'!{YB[y]}{cr+5}"),
            ("CSH_SAFE", "Safety / eval", "06_People_Other", lambda y: f"='06_People_Other'!{YB[y]}{cr+6}"),
            ("CSH_LEGAL", "Legal / regulatory", "06_People_Other", lambda y: f"='06_People_Other'!{YB[y]}{cr+7}"),
            ("CSH_GTM", "GTM and G&A", "06_People_Other", lambda y: f"='06_People_Other'!{YB[y]}{cr+8}"),
            ("CSH_ASIC", "ASIC program", "06_People_Other", lambda y: f"='06_People_Other'!{YB[y]}{cr+9}"),
        ]
        for i, (k, lab, src, fn) in enumerate(lines):
            line(sh, r + i, k, s, lab, "$M", src, {y: fn(y) for y in YRS})
        n = len(lines)
        line(sh, r + n, "CSH_TOTAL", s, "Total cash out (gross)", "$M", "sum", {y: f"=SUM({YB[y]}{r}:{YB[y]}{r+n-1})" for y in YRS}, bold=True)
        line(sh, r + n + 1, "CSH_REV", s, "less revenue (05_Inference)", "$M", "05_Inference", {y: f"='05_Inference'!{YB[y]}{ir}" for y in YRS})
        line(sh, r + n + 2, "CSH_NET", s, "Net cash out (equity + debt funded)", "$M", "derived", {y: f"={YB[y]}{r+n}-{YB[y]}{r+n+1}" for y in YRS}, bold=True)
        line(sh, r + n + 3, "CSH_DRAW", s, "Debt drawn (02_Compute)", "$M", "02_Compute", {y: f"='02_Compute'!{YB[y]}{cr+12}" for y in YRS})
        line(sh, r + n + 4, "CSH_SVC", s, "Debt service (interest + principal)", "$M", "02_Compute", {y: f"='02_Compute'!{YB[y]}{cr+16}+'02_Compute'!{YB[y]}{cr+13}" for y in YRS})
        line(sh, r + n + 5, "CSH_EQ", s, "Equity cash out = net cash out - debt drawn + debt service", "$M", "derived", {y: f"={YB[y]}{r+n+2}-{YB[y]}{r+n+3}+{YB[y]}{r+n+4}" for y in YRS}, bold=True)
        line(sh, r + n + 6, "CSH_CUMEQ", s, "Cumulative equity capital", "$M", "running sum", {y: (f"={YB[y]}{r+n+5}" if y == 1 else f"={YB[y-1]}{r+n+6}+{YB[y]}{r+n+5}") for y in YRS}, bold=True)
        line(sh, r + n + 7, "CSH_DEBT", s, "Debt principal outstanding (02_Compute)", "$M", "02_Compute", {y: f"='02_Compute'!{YB[y]}{cr+14}" for y in YRS})
        line(sh, r + n + 8, "CSH_CUMCAP", s, "Cumulative capital, equity plus debt (the entry fee)", "$M", "derived", {y: f"={YB[y]}{r+n+6}+{YB[y]}{r+n+7}" for y in YRS}, bold=True, kind="output")
        line(sh, r + n + 9, "CSH_BEFLAG", s, "Cash-flow breakeven this year (net cash out <= 0)", "1/0", "derived", {y: f"=IF({YB[y]}{r+n+2}<={R('UNITZERO')},{R('UNITONE')},{R('UNITZERO')})" for y in YRS}, nf=GEN)
    sh.ws.freeze_panes = "D3"


def build_b08(sh):
    sh.put("A1", "08_Reference: what entry actually cost (spec section 7.5): xAI, SSI (SW_SSI), Thinking Machines, Reflection, Mistral, Periodic, Humans&, Meta, and the two incumbents for scale (Exhibit E18; A5:J20).", kind="note")
    sh.header(4, ["Entrant", "Capital raised / spent ($M)", "Revenue", "Headcount", "Valuation ($M)", "Resembles scenario", "Rows · tier", "Note", "", ""])
    rows = [
        (5, "xAI (inside SpaceX)", f"={R('XAI_deficit')}", f"=\"AI segment 2025 \"&TEXT({R('XAI_rev25')},\"#,##0\")&\" / op loss (\"&TEXT({R('XAI_oploss25')},\"#,##0\")&\"); Q2-2026 \"&TEXT({R('XAI_q2rev')},\"#,##0\")&\" / (\"&TEXT({R('XAI_q2loss')},\"#,##0\")&\")\"", "n/a", f"={R('XAI_acq')}", "3 (owned Colossus, ~200,000 GPUs, 300 MW phase 2)", "L-096 · T1; L-047 · T2", f"=\"accumulated deficit at 2026-03-31 (consolidated); 2025 AI-segment debt proceeds \"&TEXT({R('XAI_debt25')},\"#,##0\")&\"; pre-merger raise NOT reproducible (register 47,160 cut)\""),
        (6, "SSI", "=SW_SSI", "zero", f"={R('SSI_hc')}", f"={R('SSI_val')}", "1 (research-only)", "L-097 · T2; C-08", "7,000 (PB) / 8,000 (press) via SW_SSI; incl. Nvidia 5,000 (Jul-2026)"),
        (7, "Thinking Machines Lab", f"={R('TML_raised')}", f"=\"'at least a few hundred million' annualized; PB \"&TEXT({R('TML_pbrev')},\"#,##0\")&\" FY2026 projection\"", f"={R('TML_hc')}", f"={R('TML_post')}", "1", "L-098 · T2", f"=\"seed at 8,000 pre / 10,000 post (press 12,000, C-09); seeking 1,000 at \"&TEXT({R('TML_pre_talks')},\"#,##0\")&\" pre (in talks)\""),
        (8, "Reflection AI", f"={R('REF_raised')}", "n/a", f"={R('REF_hc')}", f"={R('REF_post')}", "1", "L-099 · T2", f"=\"Series C 2,500 at ~\"&TEXT({R('REF_pre_c')},\"#,##0\")&\" pre in progress\""),
        (9, "Mistral AI", f"={R('MIS_raised')}", f"=\"PB \"&TEXT({R('MIS_pbrev')},\"#,##0\")&\" FY2026 projection\"", f"={R('MIS_hc')}", f"={R('MIS_val')}", "1 -> 2 (first French datacenter)", "L-100 · T2", f"=\"incl. \"&TEXT({R('MIS_debt')},\"#,##0\")&\" debt; Series D EUR 3,000 (2026-09-08)\""),
        (10, "Periodic Labs", f"={R('PER_raised')}", "n/a", f"={R('PER_hc')}", f"={R('PER_post')}", "1", "L-101 · T2", "talks at ~7,000"),
        (11, "Humans&", f"={R('HUM_raised')}", "n/a", f"={R('HUM_hc')}", f"={R('HUM_post')}", "1", "L-102 · T2", "seed at 4,000 pre"),
        (12, "Meta Superintelligence Labs", f"=\"2026 capex \"&TEXT({R('META_capex_lo')},\"#,##0\")&\"-\"&TEXT({R('META_capex_hi')},\"#,##0\")&\"; Scale AI \"&TEXT({R('META_scale')},\"#,##0\")&\" for 49%\"", "n/a (inside Meta)", "n/a", "n/a", "3 (hyperscaler-funded)", "L-095 · T2; L-094 · T2; L-060 · T1", f"=\"packages to \"&TEXT({R('META_pkg')},\"#,##0\")&\" over 4 yrs; \"&TEXT({R('META_amd_GW')},\"0\")&\" GW AMD deal\""),
        (13, "Anthropic (incumbent, for scale)", f"={R('ANT_equity')}", f"=\"run-rate \"&TEXT({R('ANT_rr')},\"#,##0\")&\" gross; Q1 \"&TEXT({R('ANT_q1')},\"#,##0\")&\", Q2 \"&TEXT({R('ANT_q2')},\"#,##0\")&\"; first positive ADJUSTED operating income (non-GAAP) \"&TEXT({R('ANT_adj')},\"#,##0\")", f"={R('ANT_hc')}", f"={R('ANT_val')}", "beyond 2", "L-007, L-032, L-151, L-033, L-034, L-152, L-155, L-008, L-005", f"=\"documented contracts \"&TEXT({R('ANT_contracts')},\"#,##0\")&\" (reported-$ \"&TEXT({R('ANT_reported')},\"#,##0\")&\" incl. the unverified Google leg); burn to the first positive adjusted result ~\"&TEXT({R('ANT_burn_lo')},\"#,##0\")&\"-\"&TEXT({R('ANT_burn_hi')},\"#,##0\")&\" (derived, flagged)\""),
        (14, "OpenAI (incumbent, for scale)", f"={R('OAI_equity')}", f"=\"run-rate >\"&TEXT({R('OAI_rr')},\"#,##0\")&\"; H1 \"&TEXT({R('OAI_h1rev')},\"#,##0\")&\"; H1 operating loss \"&TEXT({R('OAI_h1loss')},\"#,##0\")", f"=TEXT({R('OAI_hc')},\"#,##0\")&\" -> \"&TEXT({R('OAI_hc_plan')},\"#,##0\")", f"={R('OAI_val')}", "beyond 3 (leases, custom silicon)", "L-022, L-065, L-066, L-027, L-019", f"=\"documented contracts \"&TEXT({R('OAI_contracts')},\"#,##0\")"),
    ]
    for rr, name, cap, rev, hc, val, res, src, note in rows:
        sh.put(f"A{rr}", name, bold=True)
        for col, v, nf in (("B", cap, NUM), ("C", rev, GEN), ("D", hc, CNT), ("E", val, NUM), ("H", note, GEN)):
            if isinstance(v, str) and v.startswith("="):
                sh.put(f"{col}{rr}", v, kind="formula", nf=nf)
            else:
                sh.put(f"{col}{rr}", v, kind="note")
        sh.put(f"F{rr}", res, kind="note"); sh.put(f"G{rr}", src, kind="note")
    sh.put("A16", "Reference bands (00_Assumptions): Lean must land in the 2,000-8,000 band (TML / Reflection / SSI / Mistral); Full frontier below Anthropic's 124,254 raised and near xAI's 41,311 accumulated deficit by Y4-Y5; Vertically integrated at or above xAI's deficit plus its 2025 AI-segment debt (~57,366) by Y5.", kind="note")
    sh.put("B17", f"={R('REF_LEAN_LO')}", kind="formula", nf=NUM); sh.put("C17", f"={R('REF_LEAN_HI')}", kind="formula", nf=NUM); sh.put("A17", "Lean band (low / high)", kind="note")
    sh.put("B18", f"={R('REF_FULL_LO')}", kind="formula", nf=NUM); sh.put("C18", f"={R('REF_FULL_HI')}", kind="formula", nf=NUM); sh.put("D18", f"={R('REF_FULL_CAP')}", kind="formula", nf=NUM); sh.put("A18", "Full band (near xAI: low / high) and the Anthropic cap", kind="note")
    sh.put("B19", f"={R('REF_VI_MIN')}", kind="formula", nf=NUM); sh.put("A19", "VI floor (xAI deficit + 2025 debt)", kind="note")
    sh.put("A20", "Supply constraint (G28, L-144 T1): custom-silicon supply booked through 2028 by six incumbents; an entrant buys merchant GPUs at merchant prices or waits (AJ: no custom supply before 2029).", kind="note")
    sh.ws.freeze_panes = "B5"


def build_b09(sh):
    sh.put("A1", "09_Output (Exhibit E18): the three scenarios side by side: Y1 / Y2 cash out, cumulative capital to each milestone, expected bands (spec section 7.4) with the +/- 20% check, the reference-class check (PASS or 'OUTSIDE REFERENCE CLASS: explain'), lease-vs-own, G20 serving cost. Live scenario (SW_GF) in column F.", kind="note")
    sh.header(3, ["Metric", "Unit", "1 Lean fast-follower", "2 Full frontier", "3 Vertically integrated", "Live (SW_GF)", "Note"])
    BH7 = 26

    def cash(s, name, y):
        return R(f"{name}|{s}|{y}")

    def cum_to(s, first_key):
        # INDEX over the cumulative-capital row by the milestone year index (text if not reached)
        r0 = 5 + (s - 1) * BH7; rr = r0 + 2 + 16 + 8
        return f'=IFERROR(INDEX(\'07_Cash\'!$D${rr}:$H${rr},{R(first_key)}),"not reached")'

    rows = []
    rows.append(("Y1 cash out (gross)", "$M", lambda s: f"={cash(s, 'CSH_TOTAL', 1)}", "OUT_Y1"))
    rows.append(("Y2 cash out (gross)", "$M", lambda s: f"={cash(s, 'CSH_TOTAL', 2)}", "OUT_Y2"))
    rows.append(("First frontier-class model (year index; 04_Training)", "year", lambda s: f"={R(f'TRN_FIRST|{s}')}", "OUT_FRONT_Y"))
    rows.append(("Cumulative capital (equity + debt) to the first frontier-class model", "$M", lambda s: cum_to(s, f"TRN_FIRST|{s}"), "OUT_FRONT"))
    rows.append(("First $1B net revenue (year index; 05_Inference) with the AJ probability in the note", "year", lambda s: f"={R(f'INF_FIRST1B|{s}')}", "OUT_1B_Y"))
    rows.append(("Cumulative capital to the first $1B net revenue", "$M", lambda s: cum_to(s, f"INF_FIRST1B|{s}"), "OUT_1B"))
    rows.append(("Cash-flow breakeven (first year net cash out <= 0; 07_Cash)", "year", lambda s: f'=IFERROR(MATCH({R("UNITONE")},\'07_Cash\'!$D${5+(s-1)*BH7+2+16+9}:$H${5+(s-1)*BH7+2+16+9},0),"beyond Y5")', "OUT_BE_Y"))
    rows.append(("Cumulative capital to breakeven", "$M", lambda s: cum_to(s, f"OUT_BE_Y|{s}"), "OUT_BE"))
    rows.append(("Cumulative capital (equity + debt) at Y5", "$M", lambda s: f"={cash(s, 'CSH_CUMCAP', 5)}", "OUT_CUM5"))
    rows.append(("Cumulative equity-only capital at Y5 (Ruling 1 spirit)", "$M", lambda s: f"={cash(s, 'CSH_CUMEQ', 5)}", "OUT_CUMEQ5"))
    rows.append(("Y5 net cash out (negative = cash generative)", "$M", lambda s: f"={cash(s, 'CSH_NET', 5)}", "OUT_NET5"))
    rows.append(("Y5 revenue", "$M", lambda s: f"={cash(s, 'CSH_REV', 5)}", "OUT_REV5"))
    for i, (lab, unit, fn, key) in enumerate(rows):
        rr = 4 + i
        sh.put(f"A{rr}", lab, bold=True); sh.put(f"B{rr}", unit, kind="note")
        for s in (1, 2, 3):
            col = "CDE"[s - 1]
            sh.put(f"{col}{rr}", fn(s), kind="output", nf=(NUM if unit == "$M" else GEN), key=f"{key}|{s}")
        sh.put(f"F{rr}", f"=CHOOSE(SW_GF,C{rr},D{rr},E{rr})", kind="formula", nf=(NUM if unit == "$M" else GEN), bold=True)
    sh.put("G8", f"=\"AJ probability: \"&TEXT({d('PROB_1B', 1)},\"0%\")&\" / \"&TEXT({d('PROB_1B', 2)},\"0%\")&\" / \"&TEXT({d('PROB_1B', 3)},\"0%\")", kind="formula")
    sh.put("G6", "expected Lean Y2 / Full Y2 / VI Y3", kind="note"); sh.put("G8", "expected Lean Y4 / Full Y3 / VI Y4", kind="note"); sh.put("G10", "expected Lean Y5 or never / Full beyond Y5 / VI beyond Y5", kind="note")
    sh.put("G9", f"=\"AJ probability of $1B: \"&TEXT({d('PROB_1B', 1)},\"0%\")&\" / \"&TEXT({d('PROB_1B', 2)},\"0%\")&\" / \"&TEXT({d('PROB_1B', 3)},\"0%\")", kind="formula")
    sh.section(17, "EXPECTED MAGNITUDES AT BASE (spec section 7.4) AND THE +/- 20% CHECK", ncols=10)
    sh.header(18, ["Metric", "Unit", "1 Lean: actual / expected / check", "2 Full: actual / expected / check", "3 VI: actual / expected / check", "", "Rule"])
    chk_rows = [(19, "Y1 cash out", "OUT_Y1", "EXP_Y1"), (20, "Y2 cash out", "OUT_Y2", "EXP_Y2"), (21, "Cumulative to the first frontier-class model", "OUT_FRONT", "EXP_FRONT"),
                (22, "Cumulative to the first $1B net revenue", "OUT_1B", "EXP_1B"), (23, "Cumulative to breakeven (or not reached)", "OUT_BE", "EXP_BE")]
    for rr, lab, ok, ek in chk_rows:
        sh.put(f"A{rr}", lab, bold=True); sh.put(f"B{rr}", "$M", kind="note")
        for s in (1, 2, 3):
            col = "CDE"[s - 1]
            if has_key(f"{ek}|{s}|lo"):
                lo, hi = R(f"{ek}|{s}|lo"), R(f"{ek}|{s}|hi")
                act = R(f"{ok}|{s}")
                f = (f'=IF(ISNUMBER({act}),TEXT({act},"#,##0")&" vs "&TEXT({lo},"#,##0")&"-"&TEXT({hi},"#,##0")&": "&IF(AND({act}>={lo}*({R("UNITONE")}-{R("TOL20")}),{act}<={hi}*({R("UNITONE")}+{R("TOL20")})),"PASS (within 20%)","OUTSIDE (explained in tie-out.md)"),'
                     f'{act}&" vs "&TEXT({lo},"#,##0")&"-"&TEXT({hi},"#,##0")&": "&IF({act}="not reached","PASS if the band allows not reached (Lean Y5-or-never; Full/VI beyond Y5)","n/a"))')
                sh.put(f"{col}{rr}", f, kind="formula", bold=True, key=f"PFB_{ok}|{s}")
            else:
                sh.put(f"{col}{rr}", "n/a (no expected band stated)", kind="note")
        sh.put(f"G{rr}", "within [0.8 x low, 1.2 x high] of the spec band", kind="note")
    sh.section(25, "REFERENCE-CLASS CHECK (spec section 7.5 rule): PASS or 'OUTSIDE REFERENCE CLASS: explain'", ncols=10)
    sh.put("A26", "1 Lean: cumulative capital to the first frontier-class model must sit in the SSI / TML / Reflection / Mistral band (2,000-8,000 to a model with little revenue)", bold=True)
    sh.put("C26", f'=IF(ISNUMBER({R("OUT_FRONT|1")}),IF(AND({R("OUT_FRONT|1")}>={R("REF_LEAN_LO")},{R("OUT_FRONT|1")}<={R("REF_LEAN_HI")}),"PASS","OUTSIDE REFERENCE CLASS: explain (see tie-out.md)"),"OUTSIDE REFERENCE CLASS: explain (milestone not reached)")', kind="output", key="RC_LEAN")
    sh.put("A27", "2 Full frontier: cumulative capital by Y4-Y5 must be below Anthropic's equity to its first positive adjusted result (124,254 raised; ~12,000-20,000 burned, flagged) and near xAI's accumulated deficit (41,311; near = 0.5x-2x)", bold=True)
    sh.put("C27", f'=IF(AND({R("OUT_CUM5|2")}<{R("REF_FULL_CAP")},OR(AND({cash(2, "CSH_CUMCAP", 4)}>={R("REF_FULL_LO")},{cash(2, "CSH_CUMCAP", 4)}<={R("REF_FULL_HI")}),AND({R("OUT_CUM5|2")}>={R("REF_FULL_LO")},{R("OUT_CUM5|2")}<={R("REF_FULL_HI")}))),"PASS","OUTSIDE REFERENCE CLASS: explain (see tie-out.md)")', kind="output", key="RC_FULL")
    sh.put("D27", f"=\"Y4 \"&TEXT({cash(2, 'CSH_CUMCAP', 4)},\"#,##0\")&\"; Y5 \"&TEXT({R('OUT_CUM5|2')},\"#,##0\")&\" vs band \"&TEXT({R('REF_FULL_LO')},\"#,##0\")&\"-\"&TEXT({R('REF_FULL_HI')},\"#,##0\")&\"; Anthropic burn to first adjusted result ~\"&TEXT({R('ANT_burn_lo')},\"#,##0\")&\"-\"&TEXT({R('ANT_burn_hi')},\"#,##0\")", kind="formula")
    sh.put("A28", "3 Vertically integrated: cumulative capital by Y5 must be at or above xAI's deficit plus its 2025 AI-segment debt (~57,366)", bold=True)
    sh.put("C28", f'=IF({R("OUT_CUM5|3")}>={R("REF_VI_MIN")},"PASS","OUTSIDE REFERENCE CLASS: explain (see tie-out.md)")', kind="output", key="RC_VI")
    sh.put("D28", f"=\"Y5 \"&TEXT({R('OUT_CUM5|3')},\"#,##0\")&\" vs floor \"&TEXT({R('REF_VI_MIN')},\"#,##0\")", kind="formula")
    sh.section(30, "LEASE VS OWN 1 GW-IT AT BASE (spec section 7.4): own ~36,400 up front + 400-620 per year power; full-stack lease 12,500-16,300 per year; powered shell 1,760-2,400 per year; crossover ~2.5-3 years", ncols=10)
    sh.header(31, ["Item", "Unit", "Value", "Expected", "Check", "", "Basis"])
    gw = R("MWPERGW")
    lvo = [
        (32, "Build 1 GW at 17.6 per MW", "$M", f"={gw}*{d('BUILD_COST', 3)}", None, "G08 (L-109)"),
        (33, "Chips: GPUs for 1 GW-IT (1,000 MW / 2.1 MW per 1,000) x GB200 price", "$M", f"={gw}/{d('MW_PER_1000', 3)}*{R('KGPU')}*{d('GPU_PRICE', 3)}/{R('MPERUSD')}", None, "G05, G01"),
        (34, "Network (8% of GPU BOM)", "$M", f"=C33*{d('NET_PCT', 3)}", None, "G12"),
        (35, "Storage (3%; could-not-verify)", "$M", f"=(C33+C34)*{d('STO_PCT', 3)}", None, "G13"),
        (36, "Owning 1 GW-IT up front (sum)", "$M", "=SUM(C32:C35)", "EXP_OWN", "spec 36,400"),
        (37, "Power per year at 70% utilization (Texas) / at 100% in F", "$M/yr", f"={gw}*{R('HOURS')}*{d('POWER_UTIL', 3)}*{R('EIA_TX')}/{R('MPERUSD')}", "EXP_POWER_LO", "G06 (L-108)"),
        (38, "Full-stack lease of 1 GW per year, low (Volta) / high (Nscale) in F", "$M/yr", f"={gw}*{R('FS_VOLTA')}", None, "G11 (L-134)"),
        (39, "Powered shell only per year, low (Core Scientific) / high (Riot) in F", "$M/yr", f"={gw}*{R('CS_rate')}", None, "G10 (L-148, L-136)"),
        (40, "Crossover lease-vs-own (years of full-stack lease that equal the up-front own cost), at the low / high lease rate in F", "yrs", "=C36/C38", "EXP_CROSS_LO", "before residual-value risk (H100 used at 33-63% of new, G01)"),
    ]
    for rr, lab, unit, f, exp, basis in lvo:
        sh.put(f"A{rr}", lab); sh.put(f"B{rr}", unit, kind="note"); sh.put(f"C{rr}", f, kind="output" if rr in (36, 40) else "formula", nf=(CNT2 if unit == "yrs" else NUM))
        if exp:
            sh.put(f"D{rr}", f"={R(exp)}", kind="formula", nf=GEN)
        sh.put(f"G{rr}", basis, kind="note")
    sh.put("F37", f"={gw}*{R('HOURS')}*{R('EIA_TX')}/{R('MPERUSD')}", kind="formula", nf=NUM); sh.put("F38", f"={gw}*{R('FS_NSCALE')}", kind="formula", nf=NUM); sh.put("F39", f"={gw}*{R('RIOT_rate')}", kind="formula", nf=NUM); sh.put("F40", "=C36/F38", kind="formula", nf=CNT2)
    sh.put("E36", f'=IF(ABS(C36-D36)<=D36*{R("TOL20")},"PASS (within 20%)","OUTSIDE")', kind="formula", bold=True, key="PFB_OWN")
    sh.put("E37", f'=IF(AND(C37>={R("EXP_POWER_LO")}*({R("UNITONE")}-{R("TOL20")}),F37<={R("EXP_POWER_HI")}*({R("UNITONE")}+{R("TOL20")})),"PASS (within 20%)","OUTSIDE")', kind="formula", bold=True, key="PFB_POWER")
    sh.put("E40", f'=IF(AND(F40>={R("EXP_CROSS_LO")}*({R("UNITONE")}-{R("TOL20")}),C40<={R("EXP_CROSS_HI")}*({R("UNITONE")}+{R("TOL20")})),"PASS (within 20%)","OUTSIDE")', kind="formula", bold=True, key="PFB_CROSS")
    sh.put("A42", "G20 serving-cost table: 05_Inference A3:J9 (MoE on-demand ~0.22; contracted 0.05-0.08; dense on-demand ~13-21; contracted 3.0-8.1; x 1.67 at 60% utilization). Live scenario:", kind="note"); sh.put("C42", f"={R('GF_LABEL')}", kind="formula", bold=True)
    sh.put("A43", "Switches in use: SW_GF_BACKSTOP / SW_GF_REGION / SW_GF_MODELCLASS / SW_SSI", kind="note"); sh.put("C43", "=SW_GF_BACKSTOP", kind="formula"); sh.put("D43", "=SW_GF_REGION", kind="formula"); sh.put("E43", "=SW_GF_MODELCLASS", kind="formula"); sh.put("F43", "=SW_SSI", kind="formula", nf=NUM)
    sh.put("A44", "Verdict fences (one sentence per scenario, from the checks above): Lean is a research shop that never reaches the current frontier and needs a step-up round to serve revenue; Full frontier reaches the frontier in Y2 on leased and half-purchased clusters and burns at incumbent scale by Y5; Vertically integrated pays the 1 GW build and the ASIC program before its cluster is operational and lands above xAI's deficit-plus-debt by Y5.", kind="note")
    sh.ws.freeze_panes = "C4"
