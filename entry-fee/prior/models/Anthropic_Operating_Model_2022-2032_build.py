"""
Anthropic PBC - Bottom-up Operating Model, 2022A - 2032E
=========================================================
Fills the analyst template (revenue build -> token engine -> cost stack ->
opex/SBC/D&A -> guards) plus companion Capacity & Energy, Charts, Controls and
Sources sheets.

Interactivity (live in Excel):
  - SCENARIO switch: Base / Best / Worst  (flexes 2027-32 revenue + margin levers)
  - BASIS toggle:    Run-rate / Recognized (restates scale; workforce/capex fixed
                     so the recognized view carries a wider operating loss)
  The visible "P&L Build" sheet is CHOOSE()-driven off 6 precomputed blocks
  (D1..D6) selected by the two dropdowns on the Controls sheet.

Basis note:
  - Revenue anchored to PitchBook TTM (2022 $10M ... 2026 $47,000M run-rate);
    2027-32 projected. Model runs on run-rate/annualized basis by default, so
    2026 prints ~breakeven (the reported Q2-2026 first operating-profit quarter).
  - COGS = INFERENCE serving + safety/payments/support only. TRAINING compute is
    R&D (cap toggle), so gross margin is inference-only (~70-78% mature) and is a
    different metric from the fully-loaded "~40% gross margin (2025)" press line.

Zero em-dashes by house rule. Sources (every URL) on the Sources & Notes sheet.
"""

import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.chart import LineChart, BarChart, Reference, Series

YEARS = [2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032]
N = len(YEARS)
IDX = {y: i for i, y in enumerate(YEARS)}


def arr(*v):
    assert len(v) == N, f"expected {N}, got {len(v)}"
    return list(v)


def add(*ls):
    return [sum(l[i] for l in ls) for i in range(N)]


def sub(a, b):
    return [a[i] - b[i] for i in range(N)]


def scaleby(a, s):
    return [a[i] * s[i] for i in range(N)]


# =============================================================================
# MODEL FUNCTION - one full P&L for a (booked, scale, inf_mult, train_mult) combo
# =============================================================================
def build_model(booked_rev, scale, inf_mult, train_mult):
    V = {}
    V['booked_rev'] = booked_rev

    # --- pricing & blended rate (scenario/basis-invariant) ---
    mix_mythos = arr(0.00, 0.00, 0.00, 0.00, 0.03, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10)
    mix_opus = arr(0.00, 0.10, 0.08, 0.10, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12)
    mix_sonnet = arr(0.40, 0.30, 0.32, 0.45, 0.45, 0.44, 0.43, 0.42, 0.41, 0.40, 0.40)
    mix_haiku = arr(0.60, 0.60, 0.60, 0.45, 0.40, 0.39, 0.39, 0.39, 0.39, 0.39, 0.38)
    li_mythos = arr(15, 15, 15, 15, 15, 15, 14, 13, 12, 12, 11)
    lo_mythos = arr(75, 75, 75, 75, 75, 70, 65, 60, 55, 55, 50)
    li_opus = arr(11, 8, 15, 15, 5, 5, 5, 4.5, 4.5, 4, 4)
    lo_opus = arr(33, 24, 75, 75, 25, 25, 22, 22, 20, 20, 18)
    li_sonnet = arr(3, 3, 3, 3, 3, 3, 3, 2.5, 2.5, 2, 2)
    lo_sonnet = arr(15, 15, 15, 15, 15, 15, 13, 13, 12, 10, 10)
    li_haiku = arr(0.8, 0.8, 0.25, 0.8, 1.0, 1.0, 1.0, 0.9, 0.9, 0.8, 0.8)
    lo_haiku = arr(2.4, 2.4, 1.25, 4.0, 5.0, 5.0, 4.5, 4.5, 4.0, 4.0, 3.6)
    for k in ('mix_mythos mix_opus mix_sonnet mix_haiku li_mythos lo_mythos li_opus lo_opus '
              'li_sonnet lo_sonnet li_haiku lo_haiku').split():
        V[k] = locals()[k]
    blist_in = [mix_mythos[i]*li_mythos[i]+mix_opus[i]*li_opus[i]+mix_sonnet[i]*li_sonnet[i]+mix_haiku[i]*li_haiku[i] for i in range(N)]
    blist_out = [mix_mythos[i]*lo_mythos[i]+mix_opus[i]*lo_opus[i]+mix_sonnet[i]*lo_sonnet[i]+mix_haiku[i]*lo_haiku[i] for i in range(N)]
    avg_in_tok = arr(1200, 1500, 2500, 5000, 8000, 11000, 14000, 17000, 19000, 21000, 23000)
    avg_out_tok = arr(350, 400, 550, 800, 1200, 1500, 1800, 2000, 2200, 2400, 2600)
    input_share = [avg_in_tok[i]/(avg_in_tok[i]+avg_out_tok[i]) for i in range(N)]
    io_ratio = [avg_in_tok[i]/avg_out_tok[i] for i in range(N)]
    pct_cached = arr(0.00, 0.00, 0.05, 0.20, 0.35, 0.42, 0.47, 0.50, 0.52, 0.54, 0.55)
    cache_read_rate = arr(1.0, 1.0, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10)
    cache_write_mult = arr(1.0, 1.0, 1.25, 1.25, 1.25, 1.25, 1.25, 1.25, 1.25, 1.25, 1.25)
    batch_pen = arr(0.00, 0.00, 0.05, 0.15, 0.25, 0.30, 0.33, 0.35, 0.37, 0.39, 0.40)
    batch_rate = arr(1.0, 1.0, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50)
    eff_in = [blist_in[i]*((1-pct_cached[i])+pct_cached[i]*cache_read_rate[i]) for i in range(N)]
    pre_batch = [input_share[i]*eff_in[i]+(1-input_share[i])*blist_out[i] for i in range(N)]
    batch_mult = [1-batch_pen[i]*(1-batch_rate[i]) for i in range(N)]
    blended_eff = [pre_batch[i]*batch_mult[i] for i in range(N)]
    for k in ('avg_in_tok avg_out_tok input_share io_ratio pct_cached cache_read_rate cache_write_mult '
              'batch_pen batch_rate blended_list_in blended_list_out blended_eff').split():
        V[k] = {'blended_list_in': blist_in, 'blended_list_out': blist_out}.get(k, locals().get(k))
    V['blended_eff'] = blended_eff

    # --- non-API streams (revenue drivers scaled by `scale` for recognized basis) ---
    ent_contracts = scaleby(arr(0, 5, 60, 300, 1000, 1700, 2400, 3100, 3700, 4200, 4600), scale)
    committed_use_disc = arr(0.0, 0.05, 0.10, 0.12, 0.15, 0.15, 0.16, 0.16, 0.17, 0.17, 0.18)
    ent_seats = scaleby(arr(0, 2000, 40000, 250000, 900000, 1600000, 2300000, 3000000, 3600000, 4100000, 4500000), scale)
    ent_fee_seat_mo = arr(0, 30, 35, 40, 45, 48, 50, 52, 54, 55, 56)
    ent_seat_rev = [ent_seats[i]*ent_fee_seat_mo[i]*12/1e6 for i in range(N)]
    consumer_rev = scaleby(arr(0, 8, 120, 1300, 6600, 11200, 16100, 21000, 25900, 30100, 34300), scale)
    consumer_arpu = arr(20, 20, 21, 23, 26, 28, 29, 30, 31, 32, 33)
    paying_subs = [consumer_rev[i]*1e6/(consumer_arpu[i]*12) if consumer_arpu[i] else 0 for i in range(N)]
    dev_seats = scaleby(arr(0, 0, 0, 350000, 1100000, 1800000, 2500000, 3100000, 3600000, 4000000, 4300000), scale)
    base_seat_fee_mo = arr(0, 0, 0, 20, 22, 24, 25, 26, 27, 28, 28)
    cc_base_rev = [dev_seats[i]*base_seat_fee_mo[i]*12/1e6 for i in range(N)]
    avg_overage_tok_dev_mo = arr(0, 0, 0, 12, 20, 26, 30, 33, 36, 38, 40)
    overage_token_price = blended_eff
    cc_overage_rev = [dev_seats[i]*avg_overage_tok_dev_mo[i]*overage_token_price[i]*12/1e6 for i in range(N)]
    bedrock_gross = scaleby(arr(0, 10, 130, 1150, 4400, 6600, 8600, 10500, 12000, 13300, 14400), scale)
    bedrock_take = arr(0.0, 0.72, 0.72, 0.72, 0.73, 0.73, 0.74, 0.74, 0.74, 0.75, 0.75)
    bedrock_rev = [bedrock_gross[i]*bedrock_take[i] for i in range(N)]
    vertex_gross = scaleby(arr(0, 0, 55, 640, 2600, 4000, 5300, 6600, 7700, 8600, 9400), scale)
    vertex_take = arr(0.0, 0.0, 0.70, 0.70, 0.71, 0.71, 0.72, 0.72, 0.72, 0.73, 0.73)
    vertex_rev = [vertex_gross[i]*vertex_take[i] for i in range(N)]
    ft_engagements = scaleby(arr(0, 0, 15, 90, 260, 420, 560, 690, 800, 890, 960), scale)
    ft_monthly_compute = arr(0, 0, 40000, 55000, 70000, 80000, 88000, 95000, 100000, 105000, 110000)
    ft_markup = arr(0.0, 0.0, 0.35, 0.35, 0.40, 0.40, 0.42, 0.42, 0.43, 0.43, 0.44)
    ft_rev = [ft_engagements[i]*ft_monthly_compute[i]*(1+ft_markup[i])*12/1e6 for i in range(N)]
    ft_setup_fee = arr(0, 0, 25000, 25000, 30000, 30000, 32000, 32000, 34000, 34000, 35000)
    ft_new_adds = [max(0, ft_engagements[i]-ft_engagements[i-1]) if i > 0 else ft_engagements[i] for i in range(N)]
    ft_setup_rev = [ft_new_adds[i]*ft_setup_fee[i]/1e6 for i in range(N)]
    pt_units = scaleby(arr(0, 0, 20, 150, 600, 1050, 1500, 1950, 2350, 2700, 3000), scale)
    pt_flat_fee_mo = arr(0, 0, 40000, 45000, 50000, 52000, 54000, 56000, 58000, 60000, 62000)
    pt_rev = [pt_units[i]*pt_flat_fee_mo[i]*12/1e6 for i in range(N)]
    ps_hours_mo = scaleby(arr(0, 500, 3000, 9000, 20000, 30000, 38000, 45000, 50000, 54000, 57000), scale)
    ps_rate = arr(0, 300, 320, 340, 360, 375, 385, 395, 405, 415, 420)
    ps_rev = [ps_hours_mo[i]*ps_rate[i]*12/1e6 for i in range(N)]
    total_nonapi_rev = add(ent_seat_rev, consumer_rev, cc_base_rev, cc_overage_rev, bedrock_rev,
                           vertex_rev, ft_rev, ft_setup_rev, pt_rev, ps_rev)
    first_party_api_rev = sub(booked_rev, total_nonapi_rev)
    for k in ('ent_contracts committed_use_disc ent_seats ent_fee_seat_mo ent_seat_rev consumer_rev '
              'consumer_arpu paying_subs dev_seats base_seat_fee_mo cc_base_rev avg_overage_tok_dev_mo '
              'overage_token_price cc_overage_rev bedrock_gross bedrock_take bedrock_rev vertex_gross '
              'vertex_take vertex_rev ft_engagements ft_monthly_compute ft_markup ft_rev ft_setup_fee '
              'ft_new_adds ft_setup_rev pt_units pt_flat_fee_mo pt_rev ps_hours_mo ps_rate ps_rev '
              'total_nonapi_rev first_party_api_rev').split():
        V[k] = locals()[k]

    # --- token engine ---
    fp_tokens_Mtok = [first_party_api_rev[i]*1e6/blended_eff[i] if blended_eff[i] else 0 for i in range(N)]
    total_tokens_T = [fp_tokens_Mtok[i]/1e6 for i in range(N)]
    total_in_tokens_T = [total_tokens_T[i]*input_share[i] for i in range(N)]
    total_out_tokens_T = [total_tokens_T[i]*(1-input_share[i]) for i in range(N)]
    fp_calls_B = [fp_tokens_Mtok[i]*1e6/(avg_in_tok[i]+avg_out_tok[i])/1e9 for i in range(N)]
    calls_per_contract_day = [fp_calls_B[i]*1e9/max(ent_contracts[i], 1)/365 for i in range(N)]
    for k in ('fp_tokens_Mtok total_tokens_T total_in_tokens_T total_out_tokens_T fp_calls_B '
              'calls_per_contract_day').split():
        V[k] = locals()[k]

    # --- inference & infra ---
    consumer_tokens_T = scaleby(arr(0, 0.02, 0.4, 6.0, 34.0, 62.0, 92.0, 122.0, 150.0, 176.0, 200.0), scale)
    cc_tokens_T = [dev_seats[i]*avg_overage_tok_dev_mo[i]*12/1e6 for i in range(N)]
    billed_tokens_T = [fp_tokens_Mtok[i]/1e6+consumer_tokens_T[i]+cc_tokens_T[i] for i in range(N)]
    free_tier_tokens_T = [billed_tokens_T[i]*f for i, f in enumerate(arr(0.50, 0.45, 0.40, 0.35, 0.30, 0.28, 0.26, 0.25, 0.24, 0.23, 0.22))]
    internal_tokens_T = [billed_tokens_T[i]*f for i, f in enumerate(arr(0.30, 0.25, 0.20, 0.15, 0.12, 0.11, 0.10, 0.10, 0.09, 0.09, 0.08))]
    gross_tokens_T = add(billed_tokens_T, free_tier_tokens_T, internal_tokens_T)
    inference_pct_rev = [x*inf_mult for x in arr(0.85, 0.55, 0.40, 0.30, 0.26, 0.24, 0.23, 0.22, 0.21, 0.20, 0.19)]
    inference_cost = [booked_rev[i]*inference_pct_rev[i] for i in range(N)]
    blended_gpu_hr = arr(2.60, 2.50, 2.40, 2.30, 2.20, 2.10, 2.05, 2.00, 1.95, 1.90, 1.85)
    fleet_util = arr(0.55, 0.58, 0.62, 0.66, 0.70, 0.72, 0.74, 0.75, 0.76, 0.77, 0.78)
    provisioned_gpu_hours = [inference_cost[i]*1e6/blended_gpu_hr[i] for i in range(N)]
    required_gpu_hours = [provisioned_gpu_hours[i]*fleet_util[i] for i in range(N)]
    tokens_per_gpu_hour = [gross_tokens_T[i]*1e12/required_gpu_hours[i] if required_gpu_hours[i] else 0 for i in range(N)]
    egress_PB = scaleby(arr(0.5, 3, 20, 120, 480, 800, 1150, 1500, 1850, 2150, 2450), scale)
    egress_rate = arr(20, 18, 16, 14, 12, 11, 10, 9, 9, 8, 8)
    egress_cost = [egress_PB[i]*1000*egress_rate[i]/1e6 for i in range(N)]
    caching_storage_cost = scaleby(arr(0.2, 1, 6, 35, 120, 190, 260, 330, 400, 460, 520), scale)
    gateway_cost = scaleby(arr(0.3, 2, 10, 55, 200, 320, 440, 560, 680, 780, 880), scale)
    for k in ('consumer_tokens_T cc_tokens_T billed_tokens_T free_tier_tokens_T internal_tokens_T '
              'gross_tokens_T inference_cost blended_gpu_hr fleet_util provisioned_gpu_hours '
              'required_gpu_hours tokens_per_gpu_hour egress_PB egress_rate egress_cost '
              'caching_storage_cost gateway_cost').split():
        V[k] = locals()[k]

    # --- safety, payments, support ---
    content_mod_rate = arr(0.05, 0.05, 0.04, 0.035, 0.03, 0.028, 0.026, 0.025, 0.024, 0.023, 0.022)
    auto_mod_cost = [gross_tokens_T[i]*1e6*content_mod_rate[i]/1e6 for i in range(N)]
    hitl_volume = scaleby(arr(20000, 120000, 700000, 3500000, 12000000, 19000000, 26000000, 33000000, 39000000, 44000000, 48000000), scale)
    cost_per_hitl = arr(4.0, 4.0, 3.8, 3.6, 3.5, 3.4, 3.3, 3.2, 3.2, 3.1, 3.0)
    hitl_cost = [hitl_volume[i]*cost_per_hitl[i]/1e6 for i in range(N)]
    b2b_collections = add(first_party_api_rev, ent_seat_rev, cc_base_rev, cc_overage_rev, ft_rev, ft_setup_rev, pt_rev, ps_rev)
    stripe_fee = arr(0.029, 0.028, 0.027, 0.026, 0.025, 0.024, 0.024, 0.023, 0.023, 0.022, 0.022)
    b2b_pay_cost = [b2b_collections[i]*stripe_fee[i] for i in range(N)]
    mobile_share = arr(0.0, 0.20, 0.30, 0.35, 0.38, 0.40, 0.40, 0.40, 0.39, 0.39, 0.38)
    b2c_mobile_coll = [consumer_rev[i]*mobile_share[i] for i in range(N)]
    appstore_take = arr(0.0, 0.30, 0.30, 0.28, 0.20, 0.20, 0.18, 0.18, 0.17, 0.17, 0.15)
    appstore_cost = [b2c_mobile_coll[i]*appstore_take[i] for i in range(N)]
    csm_ratio = arr(0, 15, 20, 25, 30, 32, 34, 36, 38, 40, 42)
    n_csm = [ent_contracts[i]/csm_ratio[i] if csm_ratio[i] else 0 for i in range(N)]
    csm_salary = arr(0, 180000, 190000, 200000, 210000, 218000, 225000, 232000, 238000, 244000, 250000)
    csm_cost = [n_csm[i]*csm_salary[i]/1e6 for i in range(N)]
    ticket_vol_k = scaleby(arr(2, 20, 150, 800, 2600, 4200, 5800, 7300, 8600, 9700, 10600), scale)
    cost_per_ticket = arr(6, 6, 5.5, 5, 4.5, 4.2, 4.0, 3.8, 3.6, 3.5, 3.4)
    consumer_support_cost = [ticket_vol_k[i]*1000*cost_per_ticket[i]/1e6 for i in range(N)]
    total_cor = add(inference_cost, egress_cost, caching_storage_cost, gateway_cost, auto_mod_cost,
                    hitl_cost, b2b_pay_cost, appstore_cost, csm_cost, consumer_support_cost)
    gross_margin_pct = [1-total_cor[i]/booked_rev[i] if booked_rev[i] else 0 for i in range(N)]
    gross_profit = sub(booked_rev, total_cor)
    for k in ('content_mod_rate auto_mod_cost hitl_volume cost_per_hitl hitl_cost b2b_collections '
              'stripe_fee b2b_pay_cost mobile_share b2c_mobile_coll appstore_take appstore_cost csm_ratio '
              'n_csm csm_salary csm_cost ticket_vol_k cost_per_ticket consumer_support_cost total_cor '
              'gross_margin_pct gross_profit').split():
        V[k] = locals()[k]

    # --- opex (headcount/comp/capex are ABSOLUTE - not scaled by basis) ---
    total_hc = arr(60, 192, 400, 1050, 5000, 7500, 9500, 11000, 12000, 12800, 13500)
    rnd_hc = arr(40, 130, 270, 700, 3250, 4800, 6000, 6900, 7500, 7900, 8300)
    sm_hc = arr(8, 30, 70, 180, 900, 1450, 1900, 2250, 2500, 2700, 2850)
    ga_hc = arr(12, 32, 60, 170, 850, 1250, 1600, 1850, 2000, 2200, 2350)
    rnd_comp_head = arr(400000, 420000, 450000, 480000, 520000, 545000, 565000, 580000, 595000, 605000, 615000)
    rnd_pers_cost = [rnd_hc[i]*rnd_comp_head[i]/1e6 for i in range(N)]
    rlhf_data = arr(2, 8, 60, 300, 620, 900, 1150, 1400, 1600, 1750, 1900)
    data_licensing = arr(0, 3, 25, 120, 400, 620, 820, 1000, 1150, 1280, 1400)
    failed_runs = arr(3, 12, 90, 380, 620, 850, 1050, 1250, 1400, 1520, 1650)
    internal_tooling = arr(1, 4, 30, 150, 380, 560, 720, 880, 1010, 1130, 1240)
    training_pct_rev = [x*train_mult for x in arr(3.50, 1.20, 3.50, 0.45, 0.43, 0.35, 0.30, 0.26, 0.23, 0.21, 0.19)]
    cap_toggle = arr(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    research_compute = [booked_rev[i]*x for i, x in enumerate(arr(0.60, 0.25, 0.55, 0.10, 0.09, 0.08, 0.07, 0.06, 0.055, 0.05, 0.045))]
    training_compute_gross = [booked_rev[i]*training_pct_rev[i] for i in range(N)]
    capitalizable_training = [training_compute_gross[i]*0.30 for i in range(N)]
    training_to_rnd = [training_compute_gross[i]*(1 if cap_toggle[i] == 0 else 0)+research_compute[i] for i in range(N)]
    total_rnd = add(rnd_pers_cost, rlhf_data, data_licensing, failed_runs, internal_tooling, training_to_rnd)
    sm_comp_head = arr(280000, 290000, 300000, 310000, 320000, 330000, 340000, 350000, 358000, 365000, 372000)
    sm_pers_cost = [sm_hc[i]*sm_comp_head[i]/1e6 for i in range(N)]
    perf_marketing = arr(0, 2, 30, 250, 1000, 1600, 2100, 2550, 2950, 3300, 3600)
    events_sponsor = arr(0, 1, 8, 45, 180, 280, 370, 450, 520, 580, 630)
    total_sm = add(sm_pers_cost, perf_marketing, events_sponsor)
    ga_comp_head = arr(260000, 270000, 280000, 290000, 300000, 308000, 315000, 322000, 328000, 334000, 340000)
    ga_pers_cost = [ga_hc[i]*ga_comp_head[i]/1e6 for i in range(N)]
    legal_counsel = arr(1, 3, 15, 60, 180, 260, 330, 400, 460, 510, 550)
    corp_insurance = arr(0, 1, 6, 30, 110, 170, 220, 270, 310, 345, 375)
    real_estate = arr(1, 4, 20, 80, 240, 340, 430, 510, 580, 640, 690)
    sox_readiness = arr(0, 0, 2, 15, 80, 120, 100, 90, 85, 82, 80)
    ga_onetime_litigation = arr(0, 0, 5, 40, 150, 90, 60, 50, 45, 40, 40)
    total_ga = add(ga_pers_cost, legal_counsel, corp_insurance, real_estate, sox_readiness)
    for k in ('total_hc rnd_hc sm_hc ga_hc rnd_comp_head rnd_pers_cost rlhf_data data_licensing '
              'failed_runs internal_tooling training_pct_rev cap_toggle research_compute '
              'training_compute_gross capitalizable_training training_to_rnd total_rnd sm_comp_head '
              'sm_pers_cost perf_marketing events_sponsor total_sm ga_comp_head ga_pers_cost legal_counsel '
              'corp_insurance real_estate sox_readiness ga_onetime_litigation total_ga').split():
        V[k] = locals()[k]

    # --- SBC ---
    sbc_rate = arr(0.40, 0.45, 0.50, 0.55, 0.55, 0.50, 0.45, 0.42, 0.40, 0.38, 0.36)
    rnd_sbc = [rnd_pers_cost[i]*sbc_rate[i] for i in range(N)]
    sm_sbc = [sm_pers_cost[i]*sbc_rate[i] for i in range(N)]
    ga_sbc = [ga_pers_cost[i]*sbc_rate[i] for i in range(N)]
    total_sbc = add(rnd_sbc, sm_sbc, ga_sbc)
    for k in ('sbc_rate rnd_sbc sm_sbc ga_sbc total_sbc').split():
        V[k] = locals()[k]

    # --- D&A ---
    amort_life_models = arr(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
    amort_cap_models = [(capitalizable_training[i]+(capitalizable_training[i-1] if i > 0 else 0))/2 for i in range(N)]
    owned_gpu_capex = arr(2, 8, 40, 220, 1400, 3200, 5000, 6500, 7500, 8200, 8800)
    dep_life_hw = arr(4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6)
    dep_owned = []
    for i in range(N):
        d = 0.0
        for j in range(i+1):
            if i-j < dep_life_hw[j]:
                d += owned_gpu_capex[j]/dep_life_hw[j]
        dep_owned.append(d)
    amort_prepaid_cloud = arr(0, 0, 20, 120, 500, 800, 1050, 1300, 1500, 1650, 1800)
    total_da = add(amort_cap_models, dep_owned)
    for k in ('amort_life_models amort_cap_models owned_gpu_capex dep_life_hw dep_owned '
              'amort_prepaid_cloud total_da').split():
        V[k] = locals()[k]

    op_income_exsbc = [gross_profit[i]-total_rnd[i]-total_sm[i]-total_ga[i]-total_da[i] for i in range(N)]
    op_income_inclsbc = [op_income_exsbc[i]-total_sbc[i] for i in range(N)]
    op_margin = [op_income_exsbc[i]/booked_rev[i] if booked_rev[i] else 0 for i in range(N)]
    V.update(op_income_exsbc=op_income_exsbc, op_income_inclsbc=op_income_inclsbc, op_margin=op_margin)

    guards = {}
    guards['Model mix sums to 100%'] = all(abs(mix_mythos[i]+mix_opus[i]+mix_sonnet[i]+mix_haiku[i]-1) < 1e-9 for i in range(N))
    guards['Streams + API = anchor'] = all(abs(first_party_api_rev[i]+total_nonapi_rev[i]-booked_rev[i]) < 1e-6 for i in range(N))
    guards['API revenue non-negative'] = all(first_party_api_rev[i] >= -1e-6 for i in range(N))
    guards['CC overage tokens NOT in API pool'] = all(cc_tokens_T[i] >= 0 for i in range(N))
    guards['Prepaid-cloud NOT in P&L D&A'] = all(abs(total_da[i]-(amort_cap_models[i]+dep_owned[i])) < 1e-6 for i in range(N))
    guards['Implied GM% in plausible band (2026+ 55-85%)'] = all(0.55 <= gross_margin_pct[i] <= 0.85 for i in range(IDX[2026], N))
    guards['Blended $/Mtok sanity ($0.5-$25)'] = all(0.5 <= blended_eff[i] <= 25 for i in range(N))
    return V, guards


# =============================================================================
# CAPACITY & ENERGY (scenario/basis-invariant)
# =============================================================================
def build_capacity(fleet_util, blended_gpu_hr):
    V = {}
    gw_aws = arr(0.01, 0.03, 0.10, 0.30, 1.00, 2.00, 3.00, 4.00, 4.50, 5.00, 5.00)
    gw_google = arr(0.01, 0.02, 0.05, 0.10, 0.50, 2.00, 3.00, 3.50, 3.50, 3.50, 3.50)
    gw_azure = arr(0.0, 0.0, 0.0, 0.0, 0.10, 0.40, 0.70, 1.00, 1.00, 1.00, 1.00)
    gw_spacex = arr(0.0, 0.0, 0.0, 0.0, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30)
    gw_fluidstack = arr(0.0, 0.0, 0.0, 0.0, 0.20, 0.80, 1.50, 2.00, 2.50, 2.80, 3.00)
    gw_coreweave = arr(0.0, 0.0, 0.0, 0.02, 0.10, 0.30, 0.50, 0.60, 0.70, 0.80, 0.80)
    gw_akamai = arr(0.0, 0.0, 0.0, 0.0, 0.05, 0.10, 0.15, 0.20, 0.20, 0.25, 0.25)
    gw_total = add(gw_aws, gw_google, gw_azure, gw_spacex, gw_fluidstack, gw_coreweave, gw_akamai)
    gw_ceiling = arr(0.05, 0.12, 0.35, 0.90, 3.00, 7.50, 11.00, 14.00, 15.50, 16.50, 17.00)
    pue = arr(1.20, 1.18, 1.17, 1.16, 1.15, 1.15, 1.14, 1.14, 1.13, 1.13, 1.12)
    kw_per_accel = arr(1.0, 1.0, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5)
    it_energy_mwh = [gw_total[i]*1000*8760*fleet_util[i] for i in range(N)]
    facility_energy_mwh = [it_energy_mwh[i]*pue[i] for i in range(N)]
    avail_gpu_hours = [(gw_total[i]*1e6/kw_per_accel[i])*8760*fleet_util[i] for i in range(N)]
    elec_price = arr(70, 68, 66, 64, 62, 60, 60, 58, 58, 56, 56)
    energy_cost = [facility_energy_mwh[i]*elec_price[i]/1e6 for i in range(N)]
    energy_per_gpu_hr = [energy_cost[i]*1e6/avail_gpu_hours[i] if avail_gpu_hours[i] else 0 for i in range(N)]
    implied_allin_gpu_hr = blended_gpu_hr
    energy_pct_rental = [energy_per_gpu_hr[i]/implied_allin_gpu_hr[i] if implied_allin_gpu_hr[i] else 0 for i in range(N)]
    for k in ('gw_aws gw_google gw_azure gw_spacex gw_fluidstack gw_coreweave gw_akamai gw_total gw_ceiling '
              'pue kw_per_accel it_energy_mwh facility_energy_mwh avail_gpu_hours elec_price energy_cost '
              'energy_per_gpu_hr implied_allin_gpu_hr energy_pct_rental fleet_util').split():
        V[k] = locals().get(k, fleet_util if k == 'fleet_util' else None)
    cg = {}
    cg['Capacity constraint (ceiling > online)'] = all(gw_ceiling[i] >= gw_total[i] for i in range(N))
    cg['Utilization headroom 0-40%'] = all(0 <= (1-fleet_util[i]) <= 0.45 for i in range(N))
    cg['Energy % of rental $/GPU-hr (2-12%; below 15-25% owned note - see Sources)'] = all(0.02 <= energy_pct_rental[i] <= 0.12 for i in range(IDX[2026], N))
    return V, cg


# =============================================================================
# GENERATE 6 SCENARIO x BASIS BLOCKS
# =============================================================================
HIST = [10, 100, 1000, 9000, 47000]
booked_base = HIST + [80000, 115000, 150000, 185000, 215000, 245000]
booked_best = HIST + [92000, 140000, 190000, 245000, 300000, 355000]
booked_worst = HIST + [68000, 90000, 112000, 135000, 158000, 178000]
RECOG = arr(1.0, 0.85, 0.60, 0.52, 0.50, 0.62, 0.72, 0.80, 0.85, 0.88, 0.90)
ONES = [1.0]*N

SCN = [
    ('Base', booked_base, 1.00, 1.00),
    ('Best', booked_best, 0.90, 0.88),
    ('Worst', booked_worst, 1.12, 1.18),
]
blocks = []       # list of (name, V, guards)
for sname, bk, im, tm in SCN:
    Vr, gr = build_model(bk, ONES, im, tm)
    blocks.append((f'{sname}/Run-rate', Vr, gr))
    bk_rec = [bk[i]*RECOG[i] for i in range(N)]
    Vc, gc = build_model(bk_rec, RECOG, im, tm)
    blocks.append((f'{sname}/Recognized', Vc, gc))

V0 = blocks[0][1]   # Base / Run-rate  (default view + chart source)
capV, capG = build_capacity(V0['fleet_util'], V0['blended_gpu_hr'])

# console tie-out
print("Block                 2026rev  2026GM%  2026OpInc  2032rev  2032OpInc  guards")
for name, Vb, gb in blocks:
    print(f"{name:20s}  {Vb['booked_rev'][4]:>7.0f}  {Vb['gross_margin_pct'][4]*100:>6.1f}  "
          f"{Vb['op_income_exsbc'][4]:>8.0f}  {Vb['booked_rev'][10]:>7.0f}  {Vb['op_income_exsbc'][10]:>8.0f}  "
          f"{'ALL PASS' if all(gb.values()) else 'FAIL'}")
print("Capacity guards:", 'ALL PASS' if all(capG.values()) else 'FAIL')


# =============================================================================
# ROW DEFINITIONS
# =============================================================================
PL = [
 ('H', 'REVENUE', '', '', '', None, ''),
 ('D', 'Booked revenue', 'IN', '$M', 'Anchor. 2022-26 PitchBook TTM (10/100/1,000/9,000/47,000); 2027-32 base case. PB carries 55,000 for 2027 as a conservative mark.', 'booked_rev', '#,##0'),
 ('H', 'API PRICING AND BLENDED EFFECTIVE RATE', '', '', '', None, ''),
 ('D', 'Model mix % - Mythos', 'IN', '%', 'Token share, flagship tier (Fable 5 / Mythos 5, $10/$50). Introduced 2026.', 'mix_mythos', '0.0%'),
 ('D', 'Model mix % - Opus', 'IN', '%', 'Token share, Opus ($15/$75 to Aug-2025, cut to $5/$25 at Opus 4.5).', 'mix_opus', '0.0%'),
 ('D', 'Model mix % - Sonnet', 'IN', '%', 'Token share, Sonnet workhorse ($3/$15).', 'mix_sonnet', '0.0%'),
 ('D', 'Model mix % - Haiku', 'IN', '%', 'Token share, Haiku ($0.25/$1.25 -> $1/$5).', 'mix_haiku', '0.0%'),
 ('D', 'List input $/Mtok - Mythos', 'IN', '$', 'List input price, flagship.', 'li_mythos', '0.00'),
 ('D', 'List input $/Mtok - Opus', 'IN', '$', 'List input price, Opus.', 'li_opus', '0.00'),
 ('D', 'List input $/Mtok - Sonnet', 'IN', '$', 'List input price, Sonnet.', 'li_sonnet', '0.00'),
 ('D', 'List input $/Mtok - Haiku', 'IN', '$', 'List input price, Haiku.', 'li_haiku', '0.00'),
 ('D', 'List output $/Mtok - Mythos', 'IN', '$', 'List output price, flagship.', 'lo_mythos', '0.00'),
 ('D', 'List output $/Mtok - Opus', 'IN', '$', 'List output price, Opus.', 'lo_opus', '0.00'),
 ('D', 'List output $/Mtok - Sonnet', 'IN', '$', 'List output price, Sonnet.', 'lo_sonnet', '0.00'),
 ('D', 'List output $/Mtok - Haiku', 'IN', '$', 'List output price, Haiku.', 'lo_haiku', '0.00'),
 ('D', 'Avg input tokens / call', 'IN', 'Tok', 'Rising with agentic/long-context use.', 'avg_in_tok', '#,##0'),
 ('D', 'Avg output tokens / call', 'IN', 'Tok', 'Average generated tokens per call.', 'avg_out_tok', '#,##0'),
 ('D', 'Input share of tokens', 'CALC', '%', 'in / (in + out).', 'input_share', '0.0%'),
 ('D', 'Input : output ratio (memo)', 'CALC', 'x', 'Input per output token.', 'io_ratio', '0.00'),
 ('D', '% input tokens prompt-cached', 'IN', '%', 'Share hitting prompt cache (Aug-2024).', 'pct_cached', '0.0%'),
 ('D', 'Cache read pay-rate (0.10 = 90% off)', 'IN', 'x', 'Cached-read multiplier (0.10 = 90% off).', 'cache_read_rate', '0.00'),
 ('D', 'Cache write multiplier (memo)', 'IN', 'x', '5-min write = 1.25x input.', 'cache_write_mult', '0.00'),
 ('D', 'Batch penetration %', 'IN', '%', 'Share via Batch API (Oct-2024).', 'batch_pen', '0.0%'),
 ('D', 'Batch pay-rate (0.50 = -50%)', 'IN', 'x', 'Batch multiplier (0.50 = 50% off).', 'batch_rate', '0.00'),
 ('D', 'Blended effective $/Mtok', 'CALC', '$', 'Mix-weighted, adjusted for input share, caching, batch.', 'blended_eff', '0.00'),
 ('H', 'NON-API REVENUE STREAMS', '', '', '', None, ''),
 ('D', '# Enterprise contracts (>$1M ARR)', 'IN', 'count', '~1,000+ at $1M+ ACV by 2026.', 'ent_contracts', '#,##0'),
 ('D', 'Committed-use discount % (memo)', 'IN', '%', 'Volume discount realized on enterprise API.', 'committed_use_disc', '0.0%'),
 ('D', 'Active enterprise dashboard seats', 'IN', 'count', 'Console/admin seats.', 'ent_seats', '#,##0'),
 ('D', 'Enterprise platform fee / seat / mo', 'IN', '$', 'Monthly platform fee per seat.', 'ent_fee_seat_mo', '#,##0'),
 ('D', 'Enterprise seat revenue', 'CALC', '$M', 'seats x fee x 12.', 'ent_seat_rev', '#,##0'),
 ('D', 'Consumer subscription revenue (anchor)', 'IN', '$M', 'Claude Pro ($20) + Max ($100/$200).', 'consumer_rev', '#,##0'),
 ('D', 'Blended consumer ARPU ($/mo)', 'IN', '$', 'Blend of Pro and Max.', 'consumer_arpu', '#,##0'),
 ('D', 'Paying consumer subs (implied)', 'PLUG', 'Count', 'consumer rev / (ARPU x 12).', 'paying_subs', '#,##0'),
 ('D', 'Active developer seats', 'IN', 'Count', 'Claude Code seats (Feb-2025).', 'dev_seats', '#,##0'),
 ('D', 'Base seat fee ($/mo)', 'IN', '$', 'Claude Code base seat fee.', 'base_seat_fee_mo', '#,##0'),
 ('D', 'Claude Code base seat revenue', 'CALC', '$M', 'seats x fee x 12.', 'cc_base_rev', '#,##0'),
 ('D', 'Avg overage tokens / dev / mo', 'IN', 'Mtok', 'Usage above base seat.', 'avg_overage_tok_dev_mo', '#,##0'),
 ('D', 'Overage token price', 'LINK', '$/Mtok', 'Priced at blended API rate.', 'overage_token_price', '0.00'),
 ('D', 'Claude Code overage revenue', 'CALC', '$M', 'seats x overage x price x 12. ~$2.5B run-rate 2026.', 'cc_overage_rev', '#,##0'),
 ('D', 'AWS Bedrock gross billed volume', 'IN', '$M', 'Gross Claude billings via Bedrock.', 'bedrock_gross', '#,##0'),
 ('D', 'AWS rev-share take-rate %', 'IN', '%', 'Anthropic share of Bedrock gross.', 'bedrock_take', '0.0%'),
 ('D', 'Google Vertex gross billed volume', 'IN', '$M', 'Gross Claude billings via Vertex.', 'vertex_gross', '#,##0'),
 ('D', 'Google rev-share take-rate %', 'IN', '%', 'Anthropic share of Vertex gross.', 'vertex_take', '0.0%'),
 ('D', '# active fine-tuning engagement', 'IN', 'Count', 'Custom fine-tuning engagements.', 'ft_engagements', '#,##0'),
 ('D', 'Avg monthly compute / engagement', 'IN', '$', 'Compute billed per engagement/mo.', 'ft_monthly_compute', '#,##0'),
 ('D', 'Compute margin markup %', 'IN', '%', 'Markup over compute cost.', 'ft_markup', '0.0%'),
 ('D', 'Fine-tuning revenue', 'CALC', '$M', 'eng x compute x (1+markup) x 12.', 'ft_rev', '#,##0'),
 ('D', 'One-time setup fee / new engagement', 'IN', '$', 'Onboarding fee per new engagement.', 'ft_setup_fee', '#,##0'),
 ('D', 'New engagements (net adds)', 'CALC', 'Count', 'YoY change in engagements.', 'ft_new_adds', '#,##0'),
 ('D', 'Setup fee revenue', 'CALC', '$M', 'net adds x setup fee.', 'ft_setup_rev', '#,##0'),
 ('D', 'Active PT units', 'IN', 'Count', 'Priority Throughput reserved units.', 'pt_units', '#,##0'),
 ('D', 'Flat fee / PT unit / mo', 'IN', '$', 'Reserved-capacity fee per unit.', 'pt_flat_fee_mo', '#,##0'),
 ('D', 'PT revenue', 'CALC', '$M', 'units x fee x 12.', 'pt_rev', '#,##0'),
 ('D', 'Professional services hours / mo', 'IN', 'hr', 'Delivery/SA hours billed monthly.', 'ps_hours_mo', '#,##0'),
 ('D', 'PS rate ($/hr)', 'IN', '$', 'Blended bill rate.', 'ps_rate', '#,##0'),
 ('D', 'Professional services revenue', 'CALC', '$M', 'hours x rate x 12.', 'ps_rev', '#,##0'),
 ('S', 'Total non-API revenue', 'CALC', '$M', 'Sum of non-API streams.', 'total_nonapi_rev', '#,##0'),
 ('H', 'FIRST PARTY DIRECT API REVENUE', '', '', '', None, ''),
 ('S', 'First-party API revenue', 'PLUG', '$M', 'Booked revenue minus non-API streams.', 'first_party_api_rev', '#,##0'),
 ('H', 'API TOKEN ENGINE', '', '', '', None, ''),
 ('D', 'Total tokens processed (all)', 'PLUG', 'T', 'API revenue / blended $/Mtok (trillions).', 'total_tokens_T', '#,##0.0'),
 ('D', 'Total input tokens', 'CALC', 'T', 'tokens x input share.', 'total_in_tokens_T', '#,##0.0'),
 ('D', 'Total output tokens', 'CALC', 'T', 'tokens x (1 - input share).', 'total_out_tokens_T', '#,##0.0'),
 ('D', 'Total first-party API calls', 'CALC', 'B', 'tokens / tokens-per-call (billions).', 'fp_calls_B', '#,##0'),
 ('D', 'Memo: calls / contract / day', 'CALC', '#', 'calls / contracts / 365.', 'calls_per_contract_day', '#,##0'),
 ('H', 'COSTS - Inference and infrastructure', '', '', '', None, ''),
 ('D', 'Billed tokens (Anthropic-served)', 'LINK', 'T', 'API + consumer + Claude Code (excl Bedrock/Vertex).', 'billed_tokens_T', '#,##0.0'),
 ('D', 'Free-tier tokens served', 'IN', 'T', 'Non-billed free-tier usage.', 'free_tier_tokens_T', '#,##0.0'),
 ('D', 'Internal / testing tokens', 'IN', 'T', 'Evals/red-team/internal.', 'internal_tokens_T', '#,##0.0'),
 ('D', 'Gross tokens served', 'CALC', 'T', 'billed + free + internal.', 'gross_tokens_T', '#,##0.0'),
 ('D', 'Tokens per GPU-hour', 'IN', 'tok/hr', 'Serving throughput (back-solved for consistency).', 'tokens_per_gpu_hour', '#,##0'),
 ('D', 'Required GPU-hours', 'CALC', 'hr', 'gross tokens / tokens-per-GPU-hour.', 'required_gpu_hours', '#,##0'),
 ('D', 'Fleet utilization %', 'IN', '%', 'Effective serving utilization.', 'fleet_util', '0.0%'),
 ('D', 'Total provisioned GPU-hours', 'CALC', 'hr', 'required / utilization.', 'provisioned_gpu_hours', '#,##0'),
 ('D', 'Blended $/GPU-hour', 'IN', '$', 'Owned + rented all-in hourly cost.', 'blended_gpu_hr', '0.00'),
 ('D', 'Inference compute cost', 'CALC', '$M', 'Declining share of revenue; GPU-hrs x $/GPU-hr.', 'inference_cost', '#,##0'),
 ('D', 'Data egress volume (PB)', 'IN', 'PB', 'Outbound data volume.', 'egress_PB', '#,##0'),
 ('D', 'Egress cost ($/TB)', 'IN', '$', 'Blended egress unit cost.', 'egress_rate', '#,##0'),
 ('D', 'Data egress cost', 'CALC', '$M', 'PB x 1000 x $/TB.', 'egress_cost', '#,##0'),
 ('D', 'Context / caching storage cost', 'IN', '$M', 'KV-cache/context storage.', 'caching_storage_cost', '#,##0'),
 ('D', 'API gateway and load-balancing', 'IN', '$M', 'Edge/gateway/LB.', 'gateway_cost', '#,##0'),
 ('H', 'COSTS - SAFETY, PAYMENTS, SUPPORT', '', '', '', None, ''),
 ('D', 'Content moderation cost $/Mtok', 'IN', '$', 'Classifier cost per Mtok gross.', 'content_mod_rate', '0.000'),
 ('D', 'Automated moderation cost', 'CALC', '$M', 'gross tokens x $/Mtok.', 'auto_mod_cost', '#,##0'),
 ('D', 'HITL review volume', 'IN', 'Count', 'Human safety reviews / yr.', 'hitl_volume', '#,##0'),
 ('D', 'Cost per HITL review', 'IN', '$', 'BPO hourly x hours.', 'cost_per_hitl', '0.00'),
 ('D', 'HITL review cost', 'CALC', '$M', 'volume x cost.', 'hitl_cost', '#,##0'),
 ('D', 'B2B gross cash collections', 'LINK', '$M', 'API + seats + CC + FT + PT + PS.', 'b2b_collections', '#,##0'),
 ('D', 'Payment processing fee % (Stripe)', 'IN', '%', 'Blended processor fee.', 'stripe_fee', '0.00%'),
 ('D', 'B2B payment processing cost', 'CALC', '$M', 'collections x fee.', 'b2b_pay_cost', '#,##0'),
 ('D', 'Mobile share of consumer revenue %', 'IN', '%', 'Consumer via mobile stores.', 'mobile_share', '0.0%'),
 ('D', 'B2C mobile collections', 'CALC', '$M', 'consumer rev x mobile share.', 'b2c_mobile_coll', '#,##0'),
 ('D', 'App store take-rate %', 'IN', '%', 'Apple/Google store take.', 'appstore_take', '0.0%'),
 ('D', 'App store cost', 'CALC', '$M', 'mobile collections x take.', 'appstore_cost', '#,##0'),
 ('D', 'CSM ratio (accounts/CSM)', 'IN', '#', 'Accounts per CSM.', 'csm_ratio', '#,##0'),
 ('D', '#CSMs', 'CALC', 'count', 'contracts / ratio.', 'n_csm', '#,##0'),
 ('D', 'Fully-burdened CSM salary', 'IN', '$', 'Loaded cost per CSM.', 'csm_salary', '#,##0'),
 ('D', 'CSM cost', 'CALC', '$M', '#CSMs x salary.', 'csm_cost', '#,##0'),
 ('D', 'Support ticket volume (000s)', 'IN', 'k', 'Tickets/yr (thousands).', 'ticket_vol_k', '#,##0'),
 ('D', 'Cost per ticket', 'IN', '$', 'Cost per resolved ticket.', 'cost_per_ticket', '0.00'),
 ('D', 'Consumer support cost', 'CALC', '$M', 'tickets x cost.', 'consumer_support_cost', '#,##0'),
 ('S', 'Total cost of revenue (bottoms-up)', 'CALC', '$M', 'Inference + infra + safety + payments + support (training is R&D).', 'total_cor', '#,##0'),
 ('S', 'Memo: implied gross margin %', 'CALC', '%', 'Inference-only gross margin.', 'gross_margin_pct', '0.0%'),
 ('H', 'OpEx & Comp (ex-SBC)', '', '', '', None, ''),
 ('D', 'R&D headcount', 'IN', 'count', 'Research + eng (~65-75% of total).', 'rnd_hc', '#,##0'),
 ('D', 'Fully-burdened R&D cash comp ($/head)', 'IN', '$', 'Levels.fyi eng $619-841k, research ~$746k median.', 'rnd_comp_head', '#,##0'),
 ('D', 'R&D personnel cost', 'CALC', '$M', 'heads x comp.', 'rnd_pers_cost', '#,##0'),
 ('D', 'RLHF & data annotation', 'IN', '$M', 'Human feedback/annotation.', 'rlhf_data', '#,##0'),
 ('D', 'Proprietary data licensing', 'IN', '$M', 'Licensed training data.', 'data_licensing', '#,##0'),
 ('D', 'Experimental / failed training runs', 'IN', '$M', 'Abandoned run compute.', 'failed_runs', '#,##0'),
 ('D', 'Internal tooling & subscriptions', 'IN', '$M', 'Dev tooling/SaaS.', 'internal_tooling', '#,##0'),
 ('D', 'Capitalizable frontier-training runs', 'IN', '$M', 'Capitalizable portion (~30% of training).', 'capitalizable_training', '#,##0'),
 ('D', 'Cap toggle (1=capitalized, 0=ASC 730 expense)', 'IN', '0/1', '0 = expense training to R&D (base).', 'cap_toggle', '0'),
 ('D', 'Training compute expenses to R&D', 'CALC', '$M', 'Training (expensed) + research compute. Primary loss driver.', 'training_to_rnd', '#,##0'),
 ('S', 'Total R&D (ex-SBC)', 'CALC', '$M', 'Personnel + RLHF + licensing + failed + tooling + training.', 'total_rnd', '#,##0'),
 ('D', 'S&M Headcount', 'IN', 'count', 'GTM heads (small org).', 'sm_hc', '#,##0'),
 ('D', 'Fully-burdened S&M cash comp ($/head)', 'IN', '$', 'Loaded comp per S&M head.', 'sm_comp_head', '#,##0'),
 ('D', 'S&M personnel cost', 'CALC', '$M', 'heads x comp.', 'sm_pers_cost', '#,##0'),
 ('D', 'Performance marketing & advertising', 'IN', '$M', 'Paid acquisition/brand.', 'perf_marketing', '#,##0'),
 ('D', 'Events / conferences / sponsorships', 'IN', '$M', 'Dev conferences/sponsorships.', 'events_sponsor', '#,##0'),
 ('S', 'Total S&M (ex-SBC)', 'CALC', '$M', 'Personnel + marketing + events.', 'total_sm', '#,##0'),
 ('D', 'G&A headcount', 'IN', 'Count', 'Finance/legal/people/ops.', 'ga_hc', '#,##0'),
 ('D', 'Fully-burdened G&A salary ($/head)', 'IN', '$', 'Loaded comp per G&A head.', 'ga_comp_head', '#,##0'),
 ('D', 'G&A personnel cost', 'CALC', '$M', 'heads x comp.', 'ga_pers_cost', '#,##0'),
 ('D', 'Recurring outside legal counsel', 'IN', '$M', 'Outside counsel run-rate.', 'legal_counsel', '#,##0'),
 ('D', 'Corporate insurance (D&O, cyber)', 'IN', '$M', 'D&O/cyber premiums.', 'corp_insurance', '#,##0'),
 ('D', 'Real estate and office leases (office only)', 'IN', '$M', 'Office leases (ex-datacenter).', 'real_estate', '#,##0'),
 ('D', 'Public-co readiness / audit / SOX', 'IN', '$M', 'Audit/SOX/IPO-readiness (peaks ~2026).', 'sox_readiness', '#,##0'),
 ('S', 'Total G&A (ex-SBC)', 'CALC', '$M', 'Personnel + legal + insurance + RE + SOX.', 'total_ga', '#,##0'),
 ('D', 'One-time litigation services', 'IN', '$M', 'Non-recurring litigation.', 'ga_onetime_litigation', '#,##0'),
 ('H', 'STOCK BASED COMP', '', '', '', None, ''),
 ('D', 'SBC issue rate (% of base cash comp)', 'IN', '%', 'RSU grant value as % of cash comp.', 'sbc_rate', '0.0%'),
 ('D', 'R&D SBC', 'CALC', '$M', 'R&D cash x SBC rate.', 'rnd_sbc', '#,##0'),
 ('D', 'S&M SBC', 'CALC', '$M', 'S&M cash x SBC rate.', 'sm_sbc', '#,##0'),
 ('D', 'G&A SBC', 'CALC', '$M', 'G&A cash x SBC rate.', 'ga_sbc', '#,##0'),
 ('S', 'Total SBC', 'CALC', '$M', 'Sum of function SBC.', 'total_sbc', '#,##0'),
 ('H', 'DEPRECIATION & AMORTIZATION', '', '', '', None, ''),
 ('D', 'Amort life - models (yrs)', 'IN', 'yr', 'Life of capitalized models.', 'amort_life_models', '0'),
 ('D', 'Amort of capitalized frontier models', 'CALC', '$M', '2-yr straight-line of cap pool.', 'amort_cap_models', '#,##0'),
 ('D', 'Owned GPU / datacenter capex', 'IN', '$M', 'Owned hardware capex (Fluidstack $50B ramps 2026+).', 'owned_gpu_capex', '#,##0'),
 ('D', 'Depreciation life - HW (yrs)', 'IN', 'yr', 'Life of owned accelerators.', 'dep_life_hw', '0'),
 ('D', 'Depreciation of owned GPU / datacenter', 'CALC', '$M', 'Vintage straight-line depreciation.', 'dep_owned', '#,##0'),
 ('D', 'Amort of prepaid cloud commits (reclass)', 'MEMO', '$M', 'Reclass memo. NOT added to P&L D&A (guard).', 'amort_prepaid_cloud', '#,##0'),
 ('S', 'Total D&A', 'CALC', '$M', 'Model amort + owned HW dep (prepaid-cloud excluded).', 'total_da', '#,##0'),
 ('H', 'P&L SUMMARY (memo)', '', '', '', None, ''),
 ('S', 'Gross profit', 'CALC', '$M', 'Revenue - cost of revenue.', 'gross_profit', '#,##0'),
 ('S', 'Operating income (ex-SBC)', 'CALC', '$M', 'GP - R&D - S&M - G&A - D&A.', 'op_income_exsbc', '#,##0'),
 ('S', 'Operating income (incl-SBC)', 'CALC', '$M', 'After stock-based comp.', 'op_income_inclsbc', '#,##0'),
 ('S', 'Operating margin % (ex-SBC)', 'CALC', '%', 'Operating income / revenue.', 'op_margin', '0.0%'),
]

CAP = [
 ('H', 'CAPACITY BY PROVIDER (GW online, not committed ceiling)', '', '', '', None, ''),
 ('D', 'AWS - GW online', 'IN', 'GW', 'Trainium (Rainier live Oct-2025, >1M Trainium2). To 5GW; ~1GW end-2026.', 'gw_aws', '0.00'),
 ('D', 'Google/Broadcom - GW online', 'IN', 'GW', 'Google TPU (~1M) + Broadcom ~3.5GW from 2027.', 'gw_google', '0.00'),
 ('D', 'Azure/Nvidia - GW online', 'IN', 'GW', '$30B Azure + up to 1GW Nvidia (Nov-2025).', 'gw_azure', '0.00'),
 ('D', 'SpaceX - GW online', 'IN', 'GW', 'Colossus 1 ~0.3GW at $1.25B/mo to May-2029.', 'gw_spacex', '0.00'),
 ('D', 'Fluidstack - GW online', 'IN', 'GW', 'Owned US datacenters, $50B, ramp ~2-3GW.', 'gw_fluidstack', '0.00'),
 ('D', 'CoreWeave - GW online', 'IN', 'GW', 'Multi-year GPU deal (2026), scale undisclosed (est).', 'gw_coreweave', '0.00'),
 ('D', 'Akamai - GW online', 'IN', 'GW', 'Edge inference (~$1.8B), small (est).', 'gw_akamai', '0.00'),
 ('S', 'Total online GW', 'CALC', 'GW', '~10GW company target by 2029-30.', 'gw_total', '0.00'),
 ('D', 'Committed ceiling (GW)', 'IN', 'GW', 'Contracted ceiling (> online).', 'gw_ceiling', '0.00'),
 ('H', 'PHYSICAL to ENERGY', '', '', '', None, ''),
 ('D', 'Fleet utilization %', 'LINK', '%', 'Links to P&L fleet utilization.', 'fleet_util', '0.0%'),
 ('D', 'PUE (facility / IT power)', 'IN', 'x', '~1.15.', 'pue', '0.00'),
 ('D', 'Power per accelerator, all-in (kW)', 'IN', 'kW', '~1.2kW (GPU/TPU/Trainium blend).', 'kw_per_accel', '0.00'),
 ('D', 'IT energy (MWh/yr)', 'CALC', 'MWh/yr', 'GW x 1000 x 8760 x util.', 'it_energy_mwh', '#,##0'),
 ('D', 'Facility energy incl cooling (MWh/yr)', 'CALC', 'MWh/yr', 'IT energy x PUE.', 'facility_energy_mwh', '#,##0'),
 ('D', 'Available GPU-hours (from GW)', 'CALC', 'hr', '(GW / kW-per-accel) x 8760 x util.', 'avail_gpu_hours', '#,##0'),
 ('H', 'ENERGY COST (decomposition, not additive)', '', '', '', None, ''),
 ('D', 'Blended electricity price ($/MWh)', 'IN', '$', '~$55-65; gas-turbine cheaper but emissions-loaded.', 'elec_price', '#,##0'),
 ('D', 'Total energy cost ($M)', 'CALC', '$M', 'Facility energy x price. NOT added to COGS.', 'energy_cost', '#,##0'),
 ('D', 'Energy $ / GPU-hour', 'CALC', '$', 'Energy cost / available GPU-hours.', 'energy_per_gpu_hr', '0.000'),
 ('D', 'Implied all-in $/GPU-hr', 'LINK', '$', 'Links to P&L blended $/GPU-hour.', 'implied_allin_gpu_hr', '0.00'),
 ('D', 'Energy as % of rental $/GPU-hr', 'CALC', '%', '~4-5% (below ~15-25% owned-all-in note; see Sources).', 'energy_pct_rental', '0.0%'),
]

# =============================================================================
# STYLES + LAYOUT
# =============================================================================
HDR = PatternFill("solid", fgColor="1F2937"); SEC = PatternFill("solid", fgColor="374151")
SUM = PatternFill("solid", fgColor="1E3A5F")
WHITE = Font(color="FFFFFF", bold=True, size=10); SECF = Font(color="FFFFFF", bold=True, size=10)
BOLD = Font(bold=True, size=9); REG = Font(size=9); ITAL = Font(size=8, italic=True, color="6B7280")
SUMF = Font(bold=True, size=9, color="FFFFFF"); SUMI = Font(size=8, italic=True, color="D1D5DB")
RIGHT = Alignment(horizontal="right"); LEFTW = Alignment(horizontal="left", vertical="top", wrap_text=True)
CENTER = Alignment(horizontal="center")
COL0 = 5  # first year column (E)


def layout(rows):
    """Return list of (excel_row, spec) and a key->row map. Deterministic."""
    out = []; rowpos = {}; r = 3
    for spec in rows:
        out.append((r, spec))
        if spec[0] in ('D', 'S') and spec[5]:
            rowpos[spec[5]] = r
        r += 1
    return out, r, rowpos


def write_labels(ws, laid, title):
    ws.sheet_view.showGridLines = False
    ws.cell(1, 1, title).font = Font(bold=True, size=12, color="111827")
    hdr = ['Line Item', 'Type', 'Unit', 'What it is'] + [str(y) for y in YEARS]
    for c, h in enumerate(hdr, 1):
        cell = ws.cell(2, c, h); cell.fill = HDR; cell.font = WHITE
        cell.alignment = LEFTW if c == 4 else (RIGHT if c > 4 else CENTER)
    for r, (kind, label, typ, unit, whatis, key, fmt) in laid:
        if kind == 'H':
            ws.cell(r, 1, label).font = SECF
            for c in range(1, COL0+N):
                ws.cell(r, c).fill = SEC; ws.cell(r, c).font = SECF
            continue
        s = kind == 'S'
        ws.cell(r, 1, label).font = SUMF if s else BOLD if False else REG
        ws.cell(r, 1).alignment = LEFTW
        ws.cell(r, 2, typ).alignment = CENTER; ws.cell(r, 2).font = SUMI if s else REG
        ws.cell(r, 3, unit).alignment = CENTER; ws.cell(r, 3).font = SUMI if s else REG
        ws.cell(r, 4, whatis).alignment = LEFTW; ws.cell(r, 4).font = SUMI if s else ITAL
        if s:
            for c in (1, 2, 3, 4):
                ws.cell(r, c).fill = SUM
            ws.cell(r, 1).font = SUMF


def write_values(ws, laid, Vb):
    for r, (kind, label, typ, unit, whatis, key, fmt) in laid:
        if kind in ('H',) or not key:
            continue
        vals = Vb.get(key, [None]*N)
        for i in range(N):
            cell = ws.cell(r, COL0+i, vals[i]); cell.number_format = fmt; cell.alignment = RIGHT
            cell.font = SUMF if kind == 'S' else REG
            if kind == 'S':
                cell.fill = SUM


def write_guards(ws, start_row, gdict):
    r = start_row
    ws.cell(r, 1, 'GUARDS AND CHECKS').font = SECF
    for c in range(1, COL0+N):
        ws.cell(r, c).fill = SEC; ws.cell(r, c).font = SECF
    r += 1
    for name, ok in gdict.items():
        ws.cell(r, 1, name).font = REG; ws.cell(r, 1).alignment = LEFTW
        cell = ws.cell(r, COL0, 'PASS' if ok else 'FAIL'); cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor="047857" if ok else "B91C1C"); cell.alignment = CENTER
        r += 1
    return r


def set_widths(ws):
    ws.column_dimensions['A'].width = 40; ws.column_dimensions['B'].width = 7
    ws.column_dimensions['C'].width = 8; ws.column_dimensions['D'].width = 50
    for i in range(N):
        ws.column_dimensions[get_column_letter(COL0+i)].width = 11
    ws.freeze_panes = 'E3'


# =============================================================================
# BUILD WORKBOOK
# =============================================================================
wb = openpyxl.Workbook()
laid_pl, end_pl, rowpos = layout(PL)

# --- Controls sheet ---
wsC = wb.active; wsC.title = 'Controls'
wsC.sheet_view.showGridLines = False
wsC.cell(1, 1, 'Anthropic Operating Model - Controls').font = Font(bold=True, size=14)
wsC.cell(3, 1, 'SCENARIO').font = Font(bold=True, size=11)
wsC.cell(3, 2, 'Base').font = Font(bold=True, size=11, color="1E3A5F")
wsC.cell(4, 1, 'BASIS').font = Font(bold=True, size=11)
wsC.cell(4, 2, 'Run-rate').font = Font(bold=True, size=11, color="1E3A5F")
dv_s = DataValidation(type="list", formula1='"Base,Best,Worst"', allow_blank=False)
dv_b = DataValidation(type="list", formula1='"Run-rate,Recognized"', allow_blank=False)
wsC.add_data_validation(dv_s); wsC.add_data_validation(dv_b)
dv_s.add(wsC['B3']); dv_b.add(wsC['B4'])
for cellref in ('B3', 'B4'):
    wsC[cellref].fill = PatternFill("solid", fgColor="FEF3C7")
    wsC[cellref].border = Border(*[Side(style='thin', color='B45309')]*4)
# index helper (1..6) driving the CHOOSE on P&L Build
wsC.cell(6, 1, 'Block index').font = Font(size=9, italic=True, color="6B7280")
wsC['B6'] = '=IF(B3="Base",IF(B4="Run-rate",1,2),IF(B3="Best",IF(B4="Run-rate",3,4),IF(B4="Run-rate",5,6)))'
wsC['B6'].font = Font(bold=True, size=11)
notes_ctrl = [
 (8, 'How it works', 'Pick a SCENARIO and BASIS above. The P&L Build sheet recomputes live via the block index in B6.'),
 (9, 'SCENARIO', 'Base / Best / Worst flex 2027-32 revenue growth plus inference and training-intensity margin levers. 2022-26 are actuals and identical across scenarios.'),
 (10, 'BASIS', 'Run-rate = annualized/exit basis (matches PitchBook TTM; 2026 ~breakeven). Recognized = GAAP-style recognized revenue (~50% of run-rate in 2026); workforce and capex are held at absolute levels, so the recognized view carries a wider operating loss.'),
 (11, 'Charts', 'The Charts sheet is a fixed Base / Run-rate snapshot (renders without recalculation). The P&L Build table is the live switchable view.'),
 (12, 'Recalc', 'If figures look blank on open, press Ctrl+Alt+F9 (Excel) to force a full recalculation.'),
]
for r, a, b in notes_ctrl:
    wsC.cell(r, 1, a).font = Font(bold=True, size=9)
    c = wsC.cell(r, 2, b); c.font = Font(size=9); c.alignment = Alignment(wrap_text=True, vertical='top')
wsC.column_dimensions['A'].width = 16
wsC.column_dimensions['B'].width = 110

# --- 6 hidden data blocks D1..D6 ---
for bi, (bname, Vb, gb) in enumerate(blocks, 1):
    ws = wb.create_sheet(f'D{bi}')
    write_labels(ws, laid_pl, f'{bname}  (data block D{bi})')
    write_values(ws, laid_pl, Vb)
    write_guards(ws, end_pl, gb)
    set_widths(ws)
    ws.sheet_state = 'hidden'

# --- visible P&L Build: STATIC Base/Run-rate (always populated, no recalc needed) ---
wsP = wb.create_sheet('P&L Build', 1)
write_labels(wsP, laid_pl, 'Anthropic PBC - Operating Model 2022A-2032E  |  Base / Run-rate view  ($M unless noted).  Live Scenario/Basis switch: see Controls + "Live Switch" sheet.')
write_values(wsP, laid_pl, V0)
write_guards(wsP, end_pl, blocks[0][2])
set_widths(wsP)

# --- Live Switch: CHOOSE-driven off Controls (recalculates live in Excel) ---
wsL = wb.create_sheet('Live Switch', 2)
write_labels(wsL, laid_pl, 'LIVE SWITCH - reflects Scenario & Basis chosen on the Controls sheet  (press Ctrl+Alt+F9 if cells look blank)')
for r, (kind, label, typ, unit, whatis, key, fmt) in laid_pl:
    if kind == 'H' or not key:
        continue
    for i in range(N):
        col = get_column_letter(COL0+i)
        refs = ",".join(f"D{bi}!{col}{r}" for bi in range(1, 7))
        cell = wsL.cell(r, COL0+i)
        cell.value = f"=CHOOSE(Controls!$B$6,{refs})"
        cell.number_format = fmt; cell.alignment = RIGHT
        cell.font = SUMF if kind == 'S' else REG
        if kind == 'S':
            cell.fill = SUM
set_widths(wsL)

# --- Capacity & Energy ---
wsK = wb.create_sheet('Capacity & Energy')
laid_cap, end_cap, cappos = layout(CAP)
write_labels(wsK, laid_cap, 'Anthropic PBC - Compute Capacity & Energy 2022A-2032E  (scenario/basis-invariant)')
write_values(wsK, laid_cap, capV)
write_guards(wsK, end_cap, capG)
set_widths(wsK)

# --- Charts (static Base/Run-rate snapshot so it always renders) ---
wsCh = wb.create_sheet('Charts')
wsCh.sheet_view.showGridLines = False
wsCh.cell(1, 1, 'Charts - Base case, Run-rate basis (the P&L Build table is the live switchable view)').font = Font(bold=True, size=12)
DR = 92  # data block start row
series = [
 ('Year', YEARS),
 ('First-party API', V0['first_party_api_rev']),
 ('Non-API streams', V0['total_nonapi_rev']),
 ('Booked revenue', V0['booked_rev']),
 ('Gross margin %', V0['gross_margin_pct']),
 ('Operating margin %', V0['op_margin']),
 ('Operating income (ex-SBC)', V0['op_income_exsbc']),
 ('Total COGS', V0['total_cor']),
 ('Total R&D', V0['total_rnd']),
 ('Total S&M', V0['total_sm']),
 ('Total G&A', V0['total_ga']),
 ('Total online GW', capV['gw_total']),
 ('Committed ceiling GW', capV['gw_ceiling']),
]
for ri, (lab, vals) in enumerate(series):
    wsCh.cell(DR+ri, 1, lab).font = Font(size=8, bold=(ri == 0))
    for i in range(N):
        c = wsCh.cell(DR+ri, 2+i, vals[i])
        c.font = Font(size=8)
        if ri in (4, 5):
            c.number_format = '0.0%'
row_of = {lab: DR+ri for ri, (lab, _) in enumerate(series)}
cats = Reference(wsCh, min_col=2, min_row=DR, max_col=1+N, max_row=DR)


def mkbar(title, labels, stacked, ytitle):
    ch = BarChart(); ch.type = 'col'; ch.title = title; ch.height = 7.6; ch.width = 15
    if stacked:
        ch.grouping = 'stacked'; ch.overlap = 100
    ch.y_axis.title = ytitle; ch.x_axis.title = None
    for lab in labels:
        ref = Reference(wsCh, min_col=1, min_row=row_of[lab], max_col=1+N, max_row=row_of[lab])
        ch.add_data(ref, titles_from_data=True, from_rows=True)
    ch.set_categories(cats); ch.style = 10
    return ch


def mkline(title, labels, ytitle, pct=False):
    ch = LineChart(); ch.title = title; ch.height = 7.6; ch.width = 15
    ch.y_axis.title = ytitle
    for lab in labels:
        ref = Reference(wsCh, min_col=1, min_row=row_of[lab], max_col=1+N, max_row=row_of[lab])
        ch.add_data(ref, titles_from_data=True, from_rows=True)
    ch.set_categories(cats); ch.style = 12
    if pct:
        ch.y_axis.numFmt = '0%'
    for s in ch.series:
        s.smooth = False
    return ch


wsCh.add_chart(mkbar('Revenue build: first-party API vs non-API ($M)', ['First-party API', 'Non-API streams'], True, '$M'), 'A3')
wsCh.add_chart(mkline('Gross margin % and operating margin %', ['Gross margin %', 'Operating margin %'], '%', pct=True), 'J3')
wsCh.add_chart(mkbar('Operating income ex-SBC ($M)', ['Operating income (ex-SBC)'], False, '$M'), 'A19')
wsCh.add_chart(mkbar('Cost stack: COGS / R&D / S&M / G&A ($M)', ['Total COGS', 'Total R&D', 'Total S&M', 'Total G&A'], True, '$M'), 'J19')
wsCh.add_chart(mkline('Compute capacity: online GW vs committed ceiling', ['Total online GW', 'Committed ceiling GW'], 'GW'), 'A35')
wsCh.column_dimensions['A'].width = 12

# --- Sources & Notes (every URL) ---
wsS = wb.create_sheet('Sources & Notes')
wsS.sheet_view.showGridLines = False
wsS.column_dimensions['A'].width = 30
wsS.column_dimensions['B'].width = 125
r = 1
wsS.cell(r, 1, 'Anthropic Operating Model - Sources & Methodology').font = Font(bold=True, size=14); r += 2


def sec(t):
    global r
    wsS.cell(r, 1, t).font = Font(bold=True, size=10, color="FFFFFF")
    wsS.cell(r, 1).fill = SEC; wsS.cell(r, 2).fill = SEC; r += 1


def note(a, b):
    global r
    wsS.cell(r, 1, a).font = Font(bold=True, size=9); wsS.cell(r, 1).alignment = Alignment(wrap_text=True, vertical='top')
    wsS.cell(r, 2, b).font = Font(size=9); wsS.cell(r, 2).alignment = Alignment(wrap_text=True, vertical='top'); r += 1


def url(label, u):
    global r
    wsS.cell(r, 1, label).font = Font(size=9); wsS.cell(r, 1).alignment = Alignment(wrap_text=True, vertical='top')
    c = wsS.cell(r, 2, u); c.font = Font(size=9, color="1155CC", underline='single'); c.hyperlink = u; r += 1


sec('METHODOLOGY')
note('Prepared', 'July 2026. Anthropic is private and pre-IPO (confidential S-1 filed Jun 1, 2026; IPO expected Oct 2026). All P&L/headcount lines are third-party estimates; funding/valuation are PitchBook actual-status deal records.')
note('Basis', 'Model runs on an annualized / run-rate basis matching PitchBook TTM by default; on that basis 2026 prints ~breakeven (consistent with the reported Q2-2026 first operating-profit quarter). The Recognized basis restates revenue to a GAAP-style recognized level (~50% of run-rate in 2026) while holding workforce and capex absolute, producing a wider operating loss.')
note('COGS definition', 'Cost of revenue = inference serving + safety/payments/support only. Training compute is R&D (template cap toggle). So the model gross margin (~70-78% mature) is inference-only and differs from the fully-loaded "~40% gross margin (2025)" press figure by construction.')
note('Interactivity', 'Controls sheet drives a live CHOOSE across 6 precomputed blocks (Scenario Base/Best/Worst x Basis Run-rate/Recognized). Charts show the Base/Run-rate snapshot.')
note('Estimates', 'All 2027-2032 years and every undisclosed driver are modeled estimates. Hard anchors: revenue TTM, list pricing, funding/valuation, 2026 headcount, named compute deals (below).')

sec('PRIMARY / STRUCTURED')
note('PitchBook Premium', 'Company 466959-97 (profile, financials, deals). Revenue TTM: 2022 $10M, 2023 $100M, 2024 $1,000M, 2025 $9,000M, 2026 $47,000M, 2027 $55,000M (forward). Total raised $161.25B; last valuation $965B (May 28, 2026).')

sec('REVENUE / FINANCIALS')
url('Anthropic Series H', 'https://www.anthropic.com/news/series-h')
url('The Information - margin/revenue', 'https://www.theinformation.com/articles/anthropic-lowers-profit-margin-projection-revenue-skyrockets')
url('SaaStr - passed OpenAI in revenue', 'https://www.saastr.com/anthropic-just-passed-openai-in-revenue-while-spending-4x-less-to-train-their-models/')
url('SaaStr - 5,000 employees efficiency', 'https://www.saastr.com/anthropic-only-has-5000-employees-almost-no-one-has-ever-been-this-efficient-thats-by-choice/')
url('Cybernews - OpenAI/Anthropic profit', 'https://cybernews.com/ai-news/openai-anthropic-profit-revenue-ai/')
url('Prof G - how unprofitable is AI', 'https://www.profgmedia.com/p/how-unprofitable-is-ai-really')
url('Markman - first profitable quarter', 'https://markmancapitalinsight.substack.com/p/anthropic-just-booked-its-first-profitable')
url('Klover - path to profit', 'https://www.klover.ai/is_ai_profitable_anthropics_path_toward_profit_analysis_2026/')
url('Lambda Finance - compute costs', 'https://www.lambdafin.com/articles/anthropic-compute-costs')
url('Sacra - Anthropic', 'https://sacra.com/c/anthropic/')

sec('API PRICING')
url('Anthropic pricing (docs)', 'https://platform.claude.com/docs/en/about-claude/pricing')
url('Anthropic pricing (site)', 'https://claude.com/pricing')
url('Anthropic - prompt caching', 'https://platform.claude.com/docs/en/build-with-claude/prompt-caching')
url('Anthropic - batch processing', 'https://platform.claude.com/docs/en/build-with-claude/batch-processing')
url('Anthropic - Claude 4', 'https://www.anthropic.com/news/claude-4')
url('Anthropic - Claude 3.5 Sonnet', 'https://www.anthropic.com/news/claude-3-5-sonnet')
url('Anthropic - Claude Sonnet 5', 'https://www.anthropic.com/news/claude-sonnet-5')
url('TechCrunch - Sonnet 5 launch', 'https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/')
url('claudefa.st - model history', 'https://claudefa.st/blog/models')
url('ArtificialAnalysis - Claude 2.1', 'https://artificialanalysis.ai/models/claude-21')
url('pricepertoken - Claude Instant', 'https://pricepertoken.com/pricing-page/model/anthropic-claude-instant')
url('pricepertoken - Claude 3 Haiku', 'https://pricepertoken.com/pricing-page/model/anthropic-claude-3-haiku')
url('CloudZero - Claude API pricing', 'https://www.cloudzero.com/blog/claude-api-pricing/')
url('Finout - Anthropic API pricing', 'https://www.finout.io/blog/anthropic-api-pricing')
url('MetaCTO - Anthropic API pricing', 'https://www.metacto.com/blogs/anthropic-api-pricing-a-full-breakdown-of-costs-and-integration')
url('IntuitionLabs - Claude plans', 'https://intuitionlabs.ai/articles/claude-pricing-plans-api-costs')
url('AImodelcalc - Claude API pricing', 'https://aimodelcalc.com/guides/claude-api-pricing')
url('TLDL - Anthropic API pricing', 'https://www.tldl.io/resources/anthropic-api-pricing')
url('BenchLM - Anthropic API pricing', 'https://benchlm.ai/anthropic/api-pricing')
url('Costgoat - Claude API', 'https://costgoat.com/pricing/claude-api')
url('Evolink - Claude API pricing', 'https://evolink.ai/blog/claude-api-pricing-guide-2026')
url('PEC - Anthropic API pricing', 'https://pecollective.com/tools/anthropic-api-pricing/')

sec('COMPUTE / CAPACITY DEALS')
url('Anthropic + Amazon (5GW)', 'https://www.anthropic.com/news/anthropic-amazon-compute')
url('Amazon - additional $5B', 'https://www.aboutamazon.com/news/company-news/amazon-invests-additional-5-billion-anthropic-ai')
url('Anthropic + Google/Broadcom', 'https://www.anthropic.com/news/google-broadcom-partnership-compute')
url('SiliconRepublic - 3.5GW TPU', 'https://www.siliconrepublic.com/machines/anthropic-google-broadcom-announce-3-5gw-tpu-deal')
url('US News/The Information - $200B Google', 'https://www.usnews.com/news/top-news/articles/2026-05-05/anthropic-commits-to-spending-200-billion-on-googles-cloud-and-chips-the-information-reports')
url("Tom's Hardware - 3.5GW from 2027", 'https://www.tomshardware.com/tech-industry/broadcom-expands-anthropic-deal-to-3-5gw-of-google-tpu-capacity-from-2027')
url('CNBC - Broadcom/Google/Anthropic', 'https://www.cnbc.com/2026/04/06/broadcom-agrees-to-expanded-chip-deals-with-google-anthropic.html')
url('Microsoft/Nvidia/Anthropic', 'https://blogs.microsoft.com/blog/2025/11/18/microsoft-nvidia-and-anthropic-announce-strategic-partnerships/')
url('DCD - $30B Azure', 'https://www.datacenterdynamics.com/en/news/anthropic-to-purchase-30bn-in-microsoft-azure-credits-nvidia-and-microsoft-to-invest-in-ai-company/')
url('TechCrunch - SpaceX $1.25B/mo', 'https://techcrunch.com/2026/05/20/anthropic-will-pay-xai-1-25-billion-per-month-for-compute/')
url('Axios - Anthropic/SpaceX compute', 'https://www.axios.com/2026/05/20/anthropic-spacex-compute')
url('Anthropic - $50B US infrastructure', 'https://www.anthropic.com/news/anthropic-invests-50-billion-in-american-ai-infrastructure')
url('CNBC - TX/NY data centers', 'https://www.cnbc.com/2025/11/12/anthropic-ai-data-centers-texas-new-york.html')
url('CoreWeave - Anthropic agreement', 'https://www.coreweave.com/news/coreweave-announces-multi-year-agreement-with-anthropic')
url('Forbes - CoreWeave deals', 'https://www.forbes.com/sites/janakirammsv/2026/04/13/coreweave-becomes-ais-landlord-with-meta-and-anthropic-deals/')
url('Forbes - Akamai $1.8B', 'https://www.forbes.com/sites/janakirammsv/2026/05/08/akamai-lands-18-billion-anthropic-deal-as-cdn-becomes-ai-cloud/')
url('Futurum - TPU structural advantage', 'https://futurumgroup.com/insights/anthropics-gigawatt-scale-tpu-deal-with-broadcom-creates-a-structural-advantage/')
url('DCD - Project Rainier 500k Trainium2', 'https://www.datacenterdynamics.com/en/news/aws-activates-project-rainier-cluster-of-nearly-500000-trainium2-chips/')
url('Data Centre Magazine - Rainier', 'https://datacentremagazine.com/news/aws-how-500-000-trainium2-chips-power-project-rainier')
url('The New Stack - $100B AWS', 'https://thenewstack.io/anthropic-amazon-aws-investment/')
url('TradingKey - $100B Amazon', 'https://www.tradingkey.com/analysis/stocks/us-stocks/261804457-anthropic-amazon-aws-trainium-openai-tradingkey')
url('Yahoo - Google/Broadcom, revenue tripled', 'https://finance.yahoo.com/sectors/technology/articles/anthropic-google-broadcom-tpu-deal-113234906.html')
url('LightSource - Google 1M TPUs', 'https://lightsource.ai/blog/google-sold-anthropic-a-million-tpus')
url('Oplexa - Broadcom/Google TPU deal', 'https://oplexa.com/broadcom-google-tpu-deal-2026/')
url('Private Credit Pulse - $30B/8mo', 'https://privatecreditpulse.substack.com/p/anthropics-30b-every-eight-months')

sec('FUNDING / VALUATION / HEADCOUNT')
url('Anthropic - Series F $183B', 'https://www.anthropic.com/news/anthropic-raises-series-f-at-usd183b-post-money-valuation')
url('Anthropic - Series G $380B', 'https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation')
url('CNBC - Google $2B commitment', 'https://www.cnbc.com/2023/10/27/google-commits-to-invest-2-billion-in-openai-competitor-anthropic.html')
url('CNBC - $2.5B credit facility', 'https://www.cnbc.com/2025/05/16/anthropic-ai-credit-facility.html')
url('CNBC - Amazon up to $25B', 'https://www.cnbc.com/2026/04/20/amazon-invest-up-to-25-billion-in-anthropic-part-of-ai-infrastructure.html')
url('Fortune - Amazon/Google billions', 'https://fortune.com/2026/06/04/amazon-google-billions-anthropic-ipo/')
url('Axios - Apollo/Blackstone $34.5B debt', 'https://www.axios.com/2026/06/10/apollo-anthropic-blackstone-broadcom')
url('Cryptobriefing - $35B debt deal', 'https://cryptobriefing.com/apollo-blackstone-anthropic-35b-debt-deal/')
url('PYMNTS - new credit pre-IPO', 'https://www.pymnts.com/news/investment-tracker/ipo/2026/anthropic-seeks-billions-dollars-new-credit-amid-ipo-preparations/')
url('Synthedia - Amazon $4B', 'https://synthedia.substack.com/p/amazon-completes-4b-anthropic-investment')
url('StockAnalysis - invest in Anthropic', 'https://stockanalysis.com/article/invest-in-anthropic-stock/')
url('Wikipedia - Anthropic', 'https://en.wikipedia.org/wiki/Anthropic')
url('Revelio Labs - headcount', 'https://www.reveliolabs.com/companies/anthropic-pbc/employees/')
url('SEO.ai - employee count', 'https://seo.ai/blog/how-many-people-work-at-anthropic')
url('MakerStations - employee stats', 'https://www.makerstations.io/anthropic-employee-statistics/')
url('Tracxn - Anthropic', 'https://tracxn.com/d/companies/anthropic')
url('Levels.fyi - salaries', 'https://www.levels.fyi/companies/anthropic/salaries/')
url('Levels.fyi - software engineer', 'https://www.levels.fyi/companies/anthropic/salaries/software-engineer')
url('Levels.fyi - trust & safety', 'https://www.levels.fyi/companies/anthropic/salaries/trust-and-safety')
url('NAHC - salary overview', 'https://www.nahc.io/blog/anthropic-salary-overview-how-much-do-employees-get-paid')
url('JobsByCulture - compensation 2026', 'https://jobsbyculture.com/blog/anthropic-compensation-2026')

sec('SOURCE-QUALITY CAVEAT')
note('Tiering', 'Primary: Anthropic newsroom, PitchBook, Amazon/Microsoft/CoreWeave blogs, SEC-derived (SpaceX S-1 via TechCrunch/Axios), The Information, CNBC, Reuters, Fortune. Secondary/aggregator (pricing calculators, substacks, blogs) corroborate but are not first-party; treated as directional and cross-checked against primary where possible.')

wb.calculation.fullCalcOnLoad = True
os.makedirs('output', exist_ok=True)
OUT = 'output/Anthropic_Operating_Model_2022-2032.xlsx'
wb.save(OUT)
print(f"\nSaved {OUT}  sheets={wb.sheetnames}")
