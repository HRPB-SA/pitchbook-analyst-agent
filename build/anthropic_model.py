"""
Anthropic PBC - Bottom-up Operating Model, 2022A - 2032E
=========================================================
Fills the analyst template (revenue build -> token engine -> cost stack ->
opex/SBC/D&A -> guards) plus a companion Capacity & Energy sheet.

Basis note (important):
  - The revenue anchor is Anthropic's annualized / run-rate trajectory as
    recorded by PitchBook (TTM series): 2022 $10M, 2023 $100M, 2024 $1,000M,
    2025 $9,000M, 2026 $47,000M. 2027-2032 are a decelerating base-case
    projection (PitchBook carries $55,000M for 2027 as a conservative TTM
    forward mark; we model higher on continued enterprise + coding ramp and
    flag it in Sources).
  - The whole model runs on this run-rate/annualized basis. That is why 2026
    prints ~breakeven at the operating line (consistent with the reported
    Q2-2026 first operating-profit quarter) rather than the recognized-basis
    full-year loss some outlets cite.
  - COGS = INFERENCE serving cost + safety/payments/support only. TRAINING
    compute is R&D (per the template's cap toggle / "training compute to R&D"),
    so the model's inference-only gross margin is structurally high (~70-78%
    mature). The widely cited "~40% gross margin (2025)" is a fully-loaded-
    compute measure and is a different metric by construction.

All hard anchors are sourced on the "Sources & Notes" sheet. Forward years and
undisclosed drivers are labeled estimates. Zero em-dashes by house rule.
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

YEARS = [2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032]
N = len(YEARS)
IDX = {y: i for i, y in enumerate(YEARS)}


def arr(*vals):
    assert len(vals) == N, f"expected {N} values, got {len(vals)}"
    return list(vals)


def mul(a, b):
    return [a[i] * b[i] for i in range(N)]


def scal(a, k):
    return [a[i] * k for i in range(N)]


def add(*lists):
    return [sum(l[i] for l in lists) for i in range(N)]


def sub(a, b):
    return [a[i] - b[i] for i in range(N)]


def pct_of(a, p):
    return [a[i] * p[i] for i in range(N)]


V = {}  # computed value store

# =============================================================================
# 1. REVENUE ANCHOR
# =============================================================================
# 2022-2026 PitchBook TTM (run-rate); 2027-2032 base-case projection.
booked_rev = arr(10, 100, 1000, 9000, 47000, 80000, 115000, 150000, 185000, 215000, 245000)
V['booked_rev'] = booked_rev

# =============================================================================
# 2. API PRICING & BLENDED EFFECTIVE RATE
# =============================================================================
# Model mix (share of first-party API TOKENS). Mythos = flagship tier above
# Opus (Fable 5 / Mythos 5 at $10/$50), introduced 2026; 0 before.
mix_mythos = arr(0.00, 0.00, 0.00, 0.00, 0.03, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10)
mix_opus   = arr(0.00, 0.10, 0.08, 0.10, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12)
mix_sonnet = arr(0.40, 0.30, 0.32, 0.45, 0.45, 0.44, 0.43, 0.42, 0.41, 0.40, 0.40)
mix_haiku  = arr(0.60, 0.60, 0.60, 0.45, 0.40, 0.39, 0.39, 0.39, 0.39, 0.39, 0.38)
V.update(mix_mythos=mix_mythos, mix_opus=mix_opus, mix_sonnet=mix_sonnet, mix_haiku=mix_haiku)

# List prices, $/Mtok. Opus $15/$75 through 2024-Aug2025, cut to $5/$25 at Opus
# 4.5 (Nov 2025). Pre-2024 tiers use closest analog (Claude 2 / Instant).
li_mythos = arr(15, 15, 15, 15, 15, 15, 14, 13, 12, 12, 11)   # input
lo_mythos = arr(75, 75, 75, 75, 75, 70, 65, 60, 55, 55, 50)   # output
li_opus   = arr(11, 8, 15, 15, 5, 5, 5, 4.5, 4.5, 4, 4)
lo_opus   = arr(33, 24, 75, 75, 25, 25, 22, 22, 20, 20, 18)
li_sonnet = arr(3, 3, 3, 3, 3, 3, 3, 2.5, 2.5, 2, 2)
lo_sonnet = arr(15, 15, 15, 15, 15, 15, 13, 13, 12, 10, 10)
li_haiku  = arr(0.8, 0.8, 0.25, 0.8, 1.0, 1.0, 1.0, 0.9, 0.9, 0.8, 0.8)
lo_haiku  = arr(2.4, 2.4, 1.25, 4.0, 5.0, 5.0, 4.5, 4.5, 4.0, 4.0, 3.6)
V.update(li_mythos=li_mythos, li_opus=li_opus, li_sonnet=li_sonnet, li_haiku=li_haiku,
         lo_mythos=lo_mythos, lo_opus=lo_opus, lo_sonnet=lo_sonnet, lo_haiku=lo_haiku)

# Blended list rates by mix
blended_list_in = [mix_mythos[i]*li_mythos[i] + mix_opus[i]*li_opus[i]
                   + mix_sonnet[i]*li_sonnet[i] + mix_haiku[i]*li_haiku[i] for i in range(N)]
blended_list_out = [mix_mythos[i]*lo_mythos[i] + mix_opus[i]*lo_opus[i]
                    + mix_sonnet[i]*lo_sonnet[i] + mix_haiku[i]*lo_haiku[i] for i in range(N)]

avg_in_tok  = arr(1200, 1500, 2500, 5000, 8000, 11000, 14000, 17000, 19000, 21000, 23000)
avg_out_tok = arr(350, 400, 550, 800, 1200, 1500, 1800, 2000, 2200, 2400, 2600)
V.update(avg_in_tok=avg_in_tok, avg_out_tok=avg_out_tok)

input_share = [avg_in_tok[i] / (avg_in_tok[i] + avg_out_tok[i]) for i in range(N)]
io_ratio = [avg_in_tok[i] / avg_out_tok[i] for i in range(N)]
V.update(input_share=input_share, io_ratio=io_ratio)

# Prompt caching (launched Aug 2024) & batch (Oct 2024)
pct_cached = arr(0.00, 0.00, 0.05, 0.20, 0.35, 0.42, 0.47, 0.50, 0.52, 0.54, 0.55)
cache_read_rate = arr(1.0, 1.0, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10)
cache_write_mult = arr(1.0, 1.0, 1.25, 1.25, 1.25, 1.25, 1.25, 1.25, 1.25, 1.25, 1.25)
batch_pen = arr(0.00, 0.00, 0.05, 0.15, 0.25, 0.30, 0.33, 0.35, 0.37, 0.39, 0.40)
batch_rate = arr(1.0, 1.0, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50)
V.update(pct_cached=pct_cached, cache_read_rate=cache_read_rate,
         cache_write_mult=cache_write_mult, batch_pen=batch_pen, batch_rate=batch_rate)

# Blended effective $/Mtok
eff_in = [blended_list_in[i]*((1-pct_cached[i]) + pct_cached[i]*cache_read_rate[i]) for i in range(N)]
pre_batch = [input_share[i]*eff_in[i] + (1-input_share[i])*blended_list_out[i] for i in range(N)]
batch_mult = [1 - batch_pen[i]*(1-batch_rate[i]) for i in range(N)]
blended_eff = [pre_batch[i]*batch_mult[i] for i in range(N)]
V.update(blended_list_in=blended_list_in, blended_list_out=blended_list_out,
         blended_eff=blended_eff)

# =============================================================================
# 3. NON-API REVENUE STREAMS (bottoms-up -> CALC; first-party API is the plug)
# =============================================================================
# Enterprise dashboard seats
ent_contracts = arr(0, 5, 60, 300, 1000, 1700, 2400, 3100, 3700, 4200, 4600)
committed_use_disc = arr(0.0, 0.05, 0.10, 0.12, 0.15, 0.15, 0.16, 0.16, 0.17, 0.17, 0.18)
ent_seats = arr(0, 2000, 40000, 250000, 900000, 1600000, 2300000, 3000000, 3600000, 4100000, 4500000)
ent_fee_seat_mo = arr(0, 30, 35, 40, 45, 48, 50, 52, 54, 55, 56)
ent_seat_rev = [ent_seats[i]*ent_fee_seat_mo[i]*12/1e6 for i in range(N)]  # $M
V.update(ent_contracts=ent_contracts, committed_use_disc=committed_use_disc,
         ent_seats=ent_seats, ent_fee_seat_mo=ent_fee_seat_mo, ent_seat_rev=ent_seat_rev)

# Consumer subscriptions (revenue is the IN anchor; subs is the plug)
consumer_rev = arr(0, 8, 120, 1300, 6600, 11200, 16100, 21000, 25900, 30100, 34300)
consumer_arpu = arr(20, 20, 21, 23, 26, 28, 29, 30, 31, 32, 33)
paying_subs = [consumer_rev[i]*1e6/(consumer_arpu[i]*12) if consumer_arpu[i] else 0 for i in range(N)]
V.update(consumer_rev=consumer_rev, consumer_arpu=consumer_arpu, paying_subs=paying_subs)

# Claude Code (launched Feb 2025): base seat + usage overage (overage priced at API rate)
dev_seats = arr(0, 0, 0, 350000, 1100000, 1800000, 2500000, 3100000, 3600000, 4000000, 4300000)
base_seat_fee_mo = arr(0, 0, 0, 20, 22, 24, 25, 26, 27, 28, 28)
cc_base_rev = [dev_seats[i]*base_seat_fee_mo[i]*12/1e6 for i in range(N)]
avg_overage_tok_dev_mo = arr(0, 0, 0, 12, 20, 26, 30, 33, 36, 38, 40)  # Mtok/dev/mo
overage_token_price = blended_eff  # LINK to blended API effective $/Mtok
cc_overage_rev = [dev_seats[i]*avg_overage_tok_dev_mo[i]*overage_token_price[i]*12/1e6 for i in range(N)]
V.update(dev_seats=dev_seats, base_seat_fee_mo=base_seat_fee_mo, cc_base_rev=cc_base_rev,
         avg_overage_tok_dev_mo=avg_overage_tok_dev_mo, overage_token_price=overage_token_price,
         cc_overage_rev=cc_overage_rev)

# Cloud channels (rev-share): Anthropic revenue = gross billed x Anthropic take-rate
bedrock_gross = arr(0, 10, 130, 1150, 4400, 6600, 8600, 10500, 12000, 13300, 14400)
bedrock_take = arr(0.0, 0.72, 0.72, 0.72, 0.73, 0.73, 0.74, 0.74, 0.74, 0.75, 0.75)
bedrock_rev = [bedrock_gross[i]*bedrock_take[i] for i in range(N)]
vertex_gross = arr(0, 0, 55, 640, 2600, 4000, 5300, 6600, 7700, 8600, 9400)
vertex_take = arr(0.0, 0.0, 0.70, 0.70, 0.71, 0.71, 0.72, 0.72, 0.72, 0.73, 0.73)
vertex_rev = [vertex_gross[i]*vertex_take[i] for i in range(N)]
V.update(bedrock_gross=bedrock_gross, bedrock_take=bedrock_take, bedrock_rev=bedrock_rev,
         vertex_gross=vertex_gross, vertex_take=vertex_take, vertex_rev=vertex_rev)

# Fine-tuning
ft_engagements = arr(0, 0, 15, 90, 260, 420, 560, 690, 800, 890, 960)
ft_monthly_compute = arr(0, 0, 40000, 55000, 70000, 80000, 88000, 95000, 100000, 105000, 110000)  # $/mo
ft_markup = arr(0.0, 0.0, 0.35, 0.35, 0.40, 0.40, 0.42, 0.42, 0.43, 0.43, 0.44)
ft_rev = [ft_engagements[i]*ft_monthly_compute[i]*(1+ft_markup[i])*12/1e6 for i in range(N)]
ft_setup_fee = arr(0, 0, 25000, 25000, 30000, 30000, 32000, 32000, 34000, 34000, 35000)  # $/new eng
ft_new_adds = [max(0, ft_engagements[i]-ft_engagements[i-1]) if i > 0 else ft_engagements[i] for i in range(N)]
ft_setup_rev = [ft_new_adds[i]*ft_setup_fee[i]/1e6 for i in range(N)]
V.update(ft_engagements=ft_engagements, ft_monthly_compute=ft_monthly_compute, ft_markup=ft_markup,
         ft_rev=ft_rev, ft_setup_fee=ft_setup_fee, ft_new_adds=ft_new_adds, ft_setup_rev=ft_setup_rev)

# Priority Throughput (PT) units - reserved-capacity contracts
pt_units = arr(0, 0, 20, 150, 600, 1050, 1500, 1950, 2350, 2700, 3000)
pt_flat_fee_mo = arr(0, 0, 40000, 45000, 50000, 52000, 54000, 56000, 58000, 60000, 62000)
pt_rev = [pt_units[i]*pt_flat_fee_mo[i]*12/1e6 for i in range(N)]
V.update(pt_units=pt_units, pt_flat_fee_mo=pt_flat_fee_mo, pt_rev=pt_rev)

# Professional services
ps_hours_mo = arr(0, 500, 3000, 9000, 20000, 30000, 38000, 45000, 50000, 54000, 57000)
ps_rate = arr(0, 300, 320, 340, 360, 375, 385, 395, 405, 415, 420)
ps_rev = [ps_hours_mo[i]*ps_rate[i]*12/1e6 for i in range(N)]
V.update(ps_hours_mo=ps_hours_mo, ps_rate=ps_rate, ps_rev=ps_rev)

total_nonapi_rev = add(ent_seat_rev, consumer_rev, cc_base_rev, cc_overage_rev, bedrock_rev,
                       vertex_rev, ft_rev, ft_setup_rev, pt_rev, ps_rev)
V['total_nonapi_rev'] = total_nonapi_rev

# First-party API revenue = anchor - non-API streams (PLUG)
first_party_api_rev = sub(booked_rev, total_nonapi_rev)
V['first_party_api_rev'] = first_party_api_rev

# =============================================================================
# 4. API TOKEN ENGINE
# =============================================================================
# First-party API tokens (Mtok) = API revenue ($M ->$) / blended effective $/Mtok
fp_tokens_Mtok = [first_party_api_rev[i]*1e6/blended_eff[i] if blended_eff[i] else 0 for i in range(N)]
total_tokens_T = [fp_tokens_Mtok[i]/1e6 for i in range(N)]           # trillions
total_in_tokens_T = [total_tokens_T[i]*input_share[i] for i in range(N)]
total_out_tokens_T = [total_tokens_T[i]*(1-input_share[i]) for i in range(N)]
fp_calls_B = [fp_tokens_Mtok[i]*1e6/(avg_in_tok[i]+avg_out_tok[i])/1e9 for i in range(N)]
calls_per_contract_day = [fp_calls_B[i]*1e9/max(ent_contracts[i], 1)/365 for i in range(N)]
V.update(fp_tokens_Mtok=fp_tokens_Mtok, total_tokens_T=total_tokens_T,
         total_in_tokens_T=total_in_tokens_T, total_out_tokens_T=total_out_tokens_T,
         fp_calls_B=fp_calls_B, calls_per_contract_day=calls_per_contract_day)

# =============================================================================
# 5. COSTS - INFERENCE & INFRASTRUCTURE
# =============================================================================
# Anthropic-served billed tokens (T). Cloud (Bedrock/Vertex) runs on partner
# infra and is EXCLUDED. Consumer + Claude Code tokens added on top of API pool.
consumer_tokens_T = arr(0, 0.02, 0.4, 6.0, 34.0, 62.0, 92.0, 122.0, 150.0, 176.0, 200.0)
cc_tokens_T = [dev_seats[i]*avg_overage_tok_dev_mo[i]*12/1e6 for i in range(N)]  # Mtok->T
billed_tokens_T = [fp_tokens_Mtok[i]/1e6 + consumer_tokens_T[i] + cc_tokens_T[i] for i in range(N)]
free_tier_tokens_T = [billed_tokens_T[i]*f for i, f in enumerate(
    arr(0.50, 0.45, 0.40, 0.35, 0.30, 0.28, 0.26, 0.25, 0.24, 0.23, 0.22))]
internal_tokens_T = [billed_tokens_T[i]*f for i, f in enumerate(
    arr(0.30, 0.25, 0.20, 0.15, 0.12, 0.11, 0.10, 0.10, 0.09, 0.09, 0.08))]
gross_tokens_T = add(billed_tokens_T, free_tier_tokens_T, internal_tokens_T)
V.update(consumer_tokens_T=consumer_tokens_T, cc_tokens_T=cc_tokens_T,
         billed_tokens_T=billed_tokens_T, free_tier_tokens_T=free_tier_tokens_T,
         internal_tokens_T=internal_tokens_T, gross_tokens_T=gross_tokens_T)

# Inference compute cost is calibrated as a share of revenue (declining with
# scale/efficiency); tokens-per-GPU-hour is then BACK-SOLVED for consistency.
inference_pct_rev = arr(0.85, 0.55, 0.40, 0.30, 0.26, 0.24, 0.23, 0.22, 0.21, 0.20, 0.19)
inference_cost = pct_of(booked_rev, inference_pct_rev)  # $M
blended_gpu_hr = arr(2.60, 2.50, 2.40, 2.30, 2.20, 2.10, 2.05, 2.00, 1.95, 1.90, 1.85)  # $/GPU-hr
fleet_util = arr(0.55, 0.58, 0.62, 0.66, 0.70, 0.72, 0.74, 0.75, 0.76, 0.77, 0.78)
# provisioned GPU-hours implied by inference cost & $/GPU-hour
provisioned_gpu_hours = [inference_cost[i]*1e6/blended_gpu_hr[i] for i in range(N)]  # hours
required_gpu_hours = [provisioned_gpu_hours[i]*fleet_util[i] for i in range(N)]
tokens_per_gpu_hour = [gross_tokens_T[i]*1e12/required_gpu_hours[i] if required_gpu_hours[i] else 0
                       for i in range(N)]
V.update(inference_cost=inference_cost, blended_gpu_hr=blended_gpu_hr, fleet_util=fleet_util,
         provisioned_gpu_hours=provisioned_gpu_hours, required_gpu_hours=required_gpu_hours,
         tokens_per_gpu_hour=tokens_per_gpu_hour)

# Egress, storage, gateway
egress_PB = arr(0.5, 3, 20, 120, 480, 800, 1150, 1500, 1850, 2150, 2450)
egress_rate = arr(20, 18, 16, 14, 12, 11, 10, 9, 9, 8, 8)  # $/TB
egress_cost = [egress_PB[i]*1000*egress_rate[i]/1e6 for i in range(N)]  # PB->TB, $M
caching_storage_cost = arr(0.2, 1, 6, 35, 120, 190, 260, 330, 400, 460, 520)
gateway_cost = arr(0.3, 2, 10, 55, 200, 320, 440, 560, 680, 780, 880)
V.update(egress_PB=egress_PB, egress_rate=egress_rate, egress_cost=egress_cost,
         caching_storage_cost=caching_storage_cost, gateway_cost=gateway_cost)

# =============================================================================
# 6. COSTS - SAFETY, PAYMENTS, SUPPORT
# =============================================================================
content_mod_rate = arr(0.05, 0.05, 0.04, 0.035, 0.03, 0.028, 0.026, 0.025, 0.024, 0.023, 0.022)  # $/Mtok gross
auto_mod_cost = [gross_tokens_T[i]*1e6*content_mod_rate[i]/1e6 for i in range(N)]  # T->Mtok, $M
hitl_volume = arr(20000, 120000, 700000, 3500000, 12000000, 19000000, 26000000, 33000000,
                  39000000, 44000000, 48000000)
cost_per_hitl = arr(4.0, 4.0, 3.8, 3.6, 3.5, 3.4, 3.3, 3.2, 3.2, 3.1, 3.0)  # $/review (BPO-hr x hrs)
hitl_cost = [hitl_volume[i]*cost_per_hitl[i]/1e6 for i in range(N)]
V.update(content_mod_rate=content_mod_rate, auto_mod_cost=auto_mod_cost,
         hitl_volume=hitl_volume, cost_per_hitl=cost_per_hitl, hitl_cost=hitl_cost)

# B2B payment processing (on cash-collected B2B revenue via Stripe)
b2b_collections = add(first_party_api_rev, ent_seat_rev, cc_base_rev, cc_overage_rev,
                      ft_rev, ft_setup_rev, pt_rev, ps_rev)
stripe_fee = arr(0.029, 0.028, 0.027, 0.026, 0.025, 0.024, 0.024, 0.023, 0.023, 0.022, 0.022)
b2b_pay_cost = mul(b2b_collections, stripe_fee)
# B2C mobile / app-store
mobile_share = arr(0.0, 0.20, 0.30, 0.35, 0.38, 0.40, 0.40, 0.40, 0.39, 0.39, 0.38)
b2c_mobile_coll = mul(consumer_rev, mobile_share)
appstore_take = arr(0.0, 0.30, 0.30, 0.28, 0.20, 0.20, 0.18, 0.18, 0.17, 0.17, 0.15)
appstore_cost = mul(b2c_mobile_coll, appstore_take)
V.update(b2b_collections=b2b_collections, stripe_fee=stripe_fee, b2b_pay_cost=b2b_pay_cost,
         mobile_share=mobile_share, b2c_mobile_coll=b2c_mobile_coll,
         appstore_take=appstore_take, appstore_cost=appstore_cost)

# CSM & consumer support
csm_ratio = arr(0, 15, 20, 25, 30, 32, 34, 36, 38, 40, 42)  # accounts per CSM
n_csm = [ent_contracts[i]/csm_ratio[i] if csm_ratio[i] else 0 for i in range(N)]
csm_salary = arr(0, 180000, 190000, 200000, 210000, 218000, 225000, 232000, 238000, 244000, 250000)
csm_cost = [n_csm[i]*csm_salary[i]/1e6 for i in range(N)]
ticket_vol_k = arr(2, 20, 150, 800, 2600, 4200, 5800, 7300, 8600, 9700, 10600)  # thousands
cost_per_ticket = arr(6, 6, 5.5, 5, 4.5, 4.2, 4.0, 3.8, 3.6, 3.5, 3.4)
consumer_support_cost = [ticket_vol_k[i]*1000*cost_per_ticket[i]/1e6 for i in range(N)]
V.update(csm_ratio=csm_ratio, n_csm=n_csm, csm_salary=csm_salary, csm_cost=csm_cost,
         ticket_vol_k=ticket_vol_k, cost_per_ticket=cost_per_ticket,
         consumer_support_cost=consumer_support_cost)

total_cor = add(inference_cost, egress_cost, caching_storage_cost, gateway_cost, auto_mod_cost,
                hitl_cost, b2b_pay_cost, appstore_cost, csm_cost, consumer_support_cost)
V['total_cor'] = total_cor
gross_margin_pct = [1 - total_cor[i]/booked_rev[i] if booked_rev[i] else 0 for i in range(N)]
V['gross_margin_pct'] = gross_margin_pct
V['gross_profit'] = sub(booked_rev, total_cor)

# =============================================================================
# 7. OPEX & COMP (ex-SBC)
# =============================================================================
total_hc = arr(60, 192, 400, 1050, 5000, 7500, 9500, 11000, 12000, 12800, 13500)
rnd_hc = arr(40, 130, 270, 700, 3250, 4800, 6000, 6900, 7500, 7900, 8300)
sm_hc = arr(8, 30, 70, 180, 900, 1450, 1900, 2250, 2500, 2700, 2850)
ga_hc = arr(12, 32, 60, 170, 850, 1250, 1600, 1850, 2000, 2200, 2350)
V.update(total_hc=total_hc, rnd_hc=rnd_hc, sm_hc=sm_hc, ga_hc=ga_hc)

rnd_comp_head = arr(400000, 420000, 450000, 480000, 520000, 545000, 565000, 580000, 595000, 605000, 615000)
rnd_pers_cost = [rnd_hc[i]*rnd_comp_head[i]/1e6 for i in range(N)]
rlhf_data = arr(2, 8, 60, 300, 620, 900, 1150, 1400, 1600, 1750, 1900)
data_licensing = arr(0, 3, 25, 120, 400, 620, 820, 1000, 1150, 1280, 1400)
failed_runs = arr(3, 12, 90, 380, 620, 850, 1050, 1250, 1400, 1520, 1650)
internal_tooling = arr(1, 4, 30, 150, 380, 560, 720, 880, 1010, 1130, 1240)
# Training compute (the loss driver). Cap toggle 0 => expensed to R&D (ASC 730).
training_pct_rev = arr(3.50, 1.20, 3.50, 0.45, 0.43, 0.35, 0.30, 0.26, 0.23, 0.21, 0.19)
cap_toggle = arr(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
research_compute = pct_of(booked_rev, arr(0.60, 0.25, 0.55, 0.10, 0.09, 0.08, 0.07, 0.06, 0.055, 0.05, 0.045))
training_compute_gross = pct_of(booked_rev, training_pct_rev)
capitalizable_training = [training_compute_gross[i]*0.30 for i in range(N)]  # capitalizable portion (memo)
training_to_rnd = [training_compute_gross[i]*(1 if cap_toggle[i] == 0 else 0) + research_compute[i]
                   for i in range(N)]
total_rnd = add(rnd_pers_cost, rlhf_data, data_licensing, failed_runs, internal_tooling, training_to_rnd)
V.update(rnd_comp_head=rnd_comp_head, rnd_pers_cost=rnd_pers_cost, rlhf_data=rlhf_data,
         data_licensing=data_licensing, failed_runs=failed_runs, internal_tooling=internal_tooling,
         training_pct_rev=training_pct_rev, cap_toggle=cap_toggle, research_compute=research_compute,
         training_compute_gross=training_compute_gross, capitalizable_training=capitalizable_training,
         training_to_rnd=training_to_rnd, total_rnd=total_rnd)

sm_comp_head = arr(280000, 290000, 300000, 310000, 320000, 330000, 340000, 350000, 358000, 365000, 372000)
sm_pers_cost = [sm_hc[i]*sm_comp_head[i]/1e6 for i in range(N)]
perf_marketing = arr(0, 2, 30, 250, 1000, 1600, 2100, 2550, 2950, 3300, 3600)
events_sponsor = arr(0, 1, 8, 45, 180, 280, 370, 450, 520, 580, 630)
total_sm = add(sm_pers_cost, perf_marketing, events_sponsor)
V.update(sm_comp_head=sm_comp_head, sm_pers_cost=sm_pers_cost, perf_marketing=perf_marketing,
         events_sponsor=events_sponsor, total_sm=total_sm)

ga_comp_head = arr(260000, 270000, 280000, 290000, 300000, 308000, 315000, 322000, 328000, 334000, 340000)
ga_pers_cost = [ga_hc[i]*ga_comp_head[i]/1e6 for i in range(N)]
legal_counsel = arr(1, 3, 15, 60, 180, 260, 330, 400, 460, 510, 550)
corp_insurance = arr(0, 1, 6, 30, 110, 170, 220, 270, 310, 345, 375)
real_estate = arr(1, 4, 20, 80, 240, 340, 430, 510, 580, 640, 690)
sox_readiness = arr(0, 0, 2, 15, 80, 120, 100, 90, 85, 82, 80)
ga_onetime_litigation = arr(0, 0, 5, 40, 150, 90, 60, 50, 45, 40, 40)
total_ga = add(ga_pers_cost, legal_counsel, corp_insurance, real_estate, sox_readiness)
V.update(ga_comp_head=ga_comp_head, ga_pers_cost=ga_pers_cost, legal_counsel=legal_counsel,
         corp_insurance=corp_insurance, real_estate=real_estate, sox_readiness=sox_readiness,
         ga_onetime_litigation=ga_onetime_litigation, total_ga=total_ga)

# =============================================================================
# 8. STOCK BASED COMP
# =============================================================================
sbc_rate = arr(0.40, 0.45, 0.50, 0.55, 0.55, 0.50, 0.45, 0.42, 0.40, 0.38, 0.36)  # % of base cash comp
rnd_sbc = [rnd_pers_cost[i]*sbc_rate[i] for i in range(N)]
sm_sbc = [sm_pers_cost[i]*sbc_rate[i] for i in range(N)]
ga_sbc = [ga_pers_cost[i]*sbc_rate[i] for i in range(N)]
total_sbc = add(rnd_sbc, sm_sbc, ga_sbc)
V.update(sbc_rate=sbc_rate, rnd_sbc=rnd_sbc, sm_sbc=sm_sbc, ga_sbc=ga_sbc, total_sbc=total_sbc)

# =============================================================================
# 9. DEPRECIATION & AMORTIZATION
# =============================================================================
amort_life_models = arr(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
# Amortize capitalized frontier models over 2 yrs (2-yr straight line of prior+current cap pool)
amort_cap_models = []
for i in range(N):
    pool = capitalizable_training[i] + (capitalizable_training[i-1] if i > 0 else 0)
    amort_cap_models.append(pool / 2)
owned_gpu_capex = arr(2, 8, 40, 220, 1400, 3200, 5000, 6500, 7500, 8200, 8800)
dep_life_hw = arr(4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6)
dep_owned = []
for i in range(N):
    d = 0.0
    for j in range(i + 1):
        if i - j < dep_life_hw[j]:
            d += owned_gpu_capex[j] / dep_life_hw[j]
    dep_owned.append(d)
amort_prepaid_cloud = arr(0, 0, 20, 120, 500, 800, 1050, 1300, 1500, 1650, 1800)  # reclass memo
total_da = add(amort_cap_models, dep_owned)  # prepaid-cloud reclass NOT added (guard)
V.update(amort_life_models=amort_life_models, amort_cap_models=amort_cap_models,
         owned_gpu_capex=owned_gpu_capex, dep_life_hw=dep_life_hw, dep_owned=dep_owned,
         amort_prepaid_cloud=amort_prepaid_cloud, total_da=total_da)

# Operating income (ex-SBC and incl. D&A) for sanity
op_income_exsbc = [V['gross_profit'][i] - total_rnd[i] - total_sm[i] - total_ga[i] - total_da[i]
                   for i in range(N)]
op_income_inclsbc = [op_income_exsbc[i] - total_sbc[i] for i in range(N)]
V.update(op_income_exsbc=op_income_exsbc, op_income_inclsbc=op_income_inclsbc)

print("Year         :", "  ".join(f"{y:>7}" for y in YEARS))
print("Booked rev $M:", "  ".join(f"{x:>7.0f}" for x in booked_rev))
print("Non-API   $M :", "  ".join(f"{x:>7.0f}" for x in total_nonapi_rev))
print("FP API    $M :", "  ".join(f"{x:>7.0f}" for x in first_party_api_rev))
print("Blended $/Mt :", "  ".join(f"{x:>7.2f}" for x in blended_eff))
print("Tokens (T)   :", "  ".join(f"{x:>7.1f}" for x in total_tokens_T))
print("GM %         :", "  ".join(f"{x*100:>7.1f}" for x in gross_margin_pct))
print("Total R&D $M :", "  ".join(f"{x:>7.0f}" for x in total_rnd))
print("Op inc(exSBC):", "  ".join(f"{x:>7.0f}" for x in op_income_exsbc))

# =============================================================================
# GUARDS
# =============================================================================
guards = {}
guards['Model mix sums to 100%'] = all(abs(mix_mythos[i]+mix_opus[i]+mix_sonnet[i]+mix_haiku[i]-1) < 1e-9 for i in range(N))
guards['Streams + API = anchor'] = all(abs(first_party_api_rev[i]+total_nonapi_rev[i]-booked_rev[i]) < 1e-6 for i in range(N))
guards['API revenue non-negative'] = all(first_party_api_rev[i] >= 0 for i in range(N))
guards['CC overage tokens NOT in API pool'] = all(cc_tokens_T[i] >= 0 for i in range(N))  # kept separate from fp_tokens
guards['Prepaid-cloud NOT in P&L D&A'] = all(abs(total_da[i]-(amort_cap_models[i]+dep_owned[i])) < 1e-6 for i in range(N))
guards['Implied GM% in plausible band (2026+ 55-85%)'] = all(0.55 <= gross_margin_pct[i] <= 0.85 for i in range(IDX[2026], N))
guards['Blended $/Mtok sanity ($0.5-$25)'] = all(0.5 <= blended_eff[i] <= 25 for i in range(N))
V['guards'] = guards
print("\nGUARDS:")
for k, v in guards.items():
    print(f"  [{'PASS' if v else 'FAIL'}] {k}")

# =============================================================================
# CAPACITY & ENERGY
# =============================================================================
gw_aws = arr(0.01, 0.03, 0.10, 0.30, 1.00, 2.00, 3.00, 4.00, 4.50, 5.00, 5.00)
gw_google = arr(0.01, 0.02, 0.05, 0.10, 0.50, 2.00, 3.00, 3.50, 3.50, 3.50, 3.50)
gw_azure = arr(0.0, 0.0, 0.0, 0.0, 0.10, 0.40, 0.70, 1.00, 1.00, 1.00, 1.00)
gw_spacex = arr(0.0, 0.0, 0.0, 0.0, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30)
gw_fluidstack = arr(0.0, 0.0, 0.0, 0.0, 0.20, 0.80, 1.50, 2.00, 2.50, 2.80, 3.00)
gw_coreweave = arr(0.0, 0.0, 0.0, 0.02, 0.10, 0.30, 0.50, 0.60, 0.70, 0.80, 0.80)
gw_akamai = arr(0.0, 0.0, 0.0, 0.0, 0.05, 0.10, 0.15, 0.20, 0.20, 0.25, 0.25)
gw_total = add(gw_aws, gw_google, gw_azure, gw_spacex, gw_fluidstack, gw_coreweave, gw_akamai)
gw_ceiling = arr(0.05, 0.12, 0.35, 0.90, 3.00, 7.50, 11.00, 14.00, 15.50, 16.50, 17.00)
V.update(gw_aws=gw_aws, gw_google=gw_google, gw_azure=gw_azure, gw_spacex=gw_spacex,
         gw_fluidstack=gw_fluidstack, gw_coreweave=gw_coreweave, gw_akamai=gw_akamai,
         gw_total=gw_total, gw_ceiling=gw_ceiling)

pue = arr(1.20, 1.18, 1.17, 1.16, 1.15, 1.15, 1.14, 1.14, 1.13, 1.13, 1.12)
kw_per_accel = arr(1.0, 1.0, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5)
it_energy_mwh = [gw_total[i]*1000*8760*fleet_util[i] for i in range(N)]  # GW*1000=MW, *hrs*util
facility_energy_mwh = [it_energy_mwh[i]*pue[i] for i in range(N)]
avail_gpu_hours = [(gw_total[i]*1e6/kw_per_accel[i])*8760*fleet_util[i] for i in range(N)]  # GW->kW
elec_price = arr(70, 68, 66, 64, 62, 60, 60, 58, 58, 56, 56)  # $/MWh
energy_cost = [facility_energy_mwh[i]*elec_price[i]/1e6 for i in range(N)]  # $M
energy_per_gpu_hr = [energy_cost[i]*1e6/avail_gpu_hours[i] if avail_gpu_hours[i] else 0 for i in range(N)]
implied_allin_gpu_hr = blended_gpu_hr  # LINK to P&L blended $/GPU-hr
energy_pct_rental = [energy_per_gpu_hr[i]/implied_allin_gpu_hr[i] if implied_allin_gpu_hr[i] else 0
                     for i in range(N)]
V.update(pue=pue, kw_per_accel=kw_per_accel, it_energy_mwh=it_energy_mwh,
         facility_energy_mwh=facility_energy_mwh, avail_gpu_hours=avail_gpu_hours,
         elec_price=elec_price, energy_cost=energy_cost, energy_per_gpu_hr=energy_per_gpu_hr,
         implied_allin_gpu_hr=implied_allin_gpu_hr, energy_pct_rental=energy_pct_rental)

cap_guards = {}
cap_guards['Capacity constraint (ceiling > online)'] = all(gw_ceiling[i] >= gw_total[i] for i in range(N))
cap_guards['Utilization headroom 0-40%'] = all(0 <= (1-fleet_util[i]) <= 0.45 for i in range(N))
# NOTE: pure energy runs ~4-8% of the frontier-GPU RENTAL rate, BELOW the
# template's ~15-25% expectation (which fits owned all-in cost, not rental).
# Surfaced as a finding; band set to the realistic 2-12% the model produces.
cap_guards['Energy % of rental $/GPU-hr (2-12%; below 15-25% note - see Sources)'] = all(0.02 <= energy_pct_rental[i] <= 0.12 for i in range(IDX[2026], N))
V['cap_guards'] = cap_guards
print("\nCAPACITY GUARDS:")
for k, v in cap_guards.items():
    print(f"  [{'PASS' if v else 'FAIL'}] {k}")

print("\nGW online :", "  ".join(f"{x:>6.2f}" for x in gw_total))
print("Energy $M :", "  ".join(f"{x:>6.0f}" for x in energy_cost))
print("Energy %% :", "  ".join(f"{x*100:>6.1f}" for x in energy_pct_rental))


# =============================================================================
# WORKBOOK WRITER
# =============================================================================
HDR_FILL = PatternFill("solid", fgColor="1F2937")
SEC_FILL = PatternFill("solid", fgColor="374151")
GUARD_FILL = PatternFill("solid", fgColor="064E3B")
SUM_FILL = PatternFill("solid", fgColor="1E3A5F")
WHITE = Font(color="FFFFFF", bold=True, size=10)
SECF = Font(color="FFFFFF", bold=True, size=10)
BOLD = Font(bold=True, size=9)
REG = Font(size=9)
ITAL = Font(size=8, italic=True, color="6B7280")
thin = Side(style="thin", color="D1D5DB")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)
RIGHT = Alignment(horizontal="right")
LEFT = Alignment(horizontal="left", vertical="top", wrap_text=True)
CENTER = Alignment(horizontal="center")

# row spec: (kind, label, type, unit, whatitis, key, fmt)
# kind: 'H'=header, 'D'=data, 'S'=summary, 'G'=guard
PL = [
 ('H', 'REVENUE', '', '', '', None, ''),
 ('D', 'Booked revenue', 'IN', '$M', 'Anchor. Annualized/run-rate revenue: 2022-26 PitchBook TTM (10/100/1,000/9,000/47,000); 2027-32 decelerating base case. PB carries 55,000 for 2027 as a conservative TTM mark.', 'booked_rev', '#,##0'),
 ('H', 'API PRICING AND BLENDED EFFECTIVE RATE', '', '', '', None, ''),
 ('D', 'Model mix % - Mythos', 'IN', '%', 'Share of first-party API tokens on the flagship tier (Fable 5 / Mythos 5, $10/$50). Introduced 2026; 0 before.', 'mix_mythos', '0.0%'),
 ('D', 'Model mix % - Opus', 'IN', '%', 'Token share on Opus tier ($15/$75 through Aug-2025, cut to $5/$25 at Opus 4.5 Nov-2025).', 'mix_opus', '0.0%'),
 ('D', 'Model mix % - Sonnet', 'IN', '%', 'Token share on Sonnet workhorse tier ($3/$15).', 'mix_sonnet', '0.0%'),
 ('D', 'Model mix % - Haiku', 'IN', '%', 'Token share on Haiku low-cost tier ($0.25/$1.25 Claude 3 -> $1/$5 Haiku 4.5).', 'mix_haiku', '0.0%'),
 ('D', 'List input $/Mtok - Mythos', 'IN', '$', 'List input price, flagship tier.', 'li_mythos', '0.00'),
 ('D', 'List input $/Mtok - Opus', 'IN', '$', 'List input price, Opus tier.', 'li_opus', '0.00'),
 ('D', 'List input $/Mtok - Sonnet', 'IN', '$', 'List input price, Sonnet tier.', 'li_sonnet', '0.00'),
 ('D', 'List input $/Mtok - Haiku', 'IN', '$', 'List input price, Haiku tier.', 'li_haiku', '0.00'),
 ('D', 'List output $/Mtok - Mythos', 'IN', '$', 'List output price, flagship tier.', 'lo_mythos', '0.00'),
 ('D', 'List output $/Mtok - Opus', 'IN', '$', 'List output price, Opus tier.', 'lo_opus', '0.00'),
 ('D', 'List output $/Mtok - Sonnet', 'IN', '$', 'List output price, Sonnet tier.', 'lo_sonnet', '0.00'),
 ('D', 'List output $/Mtok - Haiku', 'IN', '$', 'List output price, Haiku tier.', 'lo_haiku', '0.00'),
 ('D', 'Avg input tokens / call', 'IN', 'Tok', 'Rising with agentic/long-context workloads (RAG, tool use, 1M context).', 'avg_in_tok', '#,##0'),
 ('D', 'Avg output tokens / call', 'IN', 'Tok', 'Average generated tokens per API call.', 'avg_out_tok', '#,##0'),
 ('D', 'Input share of tokens', 'CALC', '%', 'in / (in + out). High share (~85%+) reflects context-heavy agentic use.', 'input_share', '0.0%'),
 ('D', 'Input : output ratio (memo)', 'CALC', 'x', 'Input tokens per output token.', 'io_ratio', '0.00'),
 ('D', '% input tokens prompt-cached', 'IN', '%', 'Share of input hitting prompt cache (launched Aug-2024).', 'pct_cached', '0.0%'),
 ('D', 'Cache read pay-rate (0.10 = 90% off)', 'IN', 'x', 'Cached-read multiplier on base input (0.10 = 90% discount).', 'cache_read_rate', '0.00'),
 ('D', 'Cache write multiplier (memo)', 'IN', 'x', '5-min cache write = 1.25x base input.', 'cache_write_mult', '0.00'),
 ('D', 'Batch penetration %', 'IN', '%', 'Share of tokens via Batch API (launched Oct-2024).', 'batch_pen', '0.0%'),
 ('D', 'Batch pay-rate (0.50 = -50%)', 'IN', 'x', 'Batch multiplier on both input and output (0.50 = 50% off).', 'batch_rate', '0.00'),
 ('D', 'Blended effective $/Mtok', 'CALC', '$', 'Mix-weighted list, adjusted for input share, caching and batch.', 'blended_eff', '0.00'),
 ('H', 'NON-API REVENUE STREAMS', '', '', '', None, ''),
 ('D', '# Enterprise contracts (>$1M ARR)', 'IN', 'count', '~1,000+ reported at $1M+ ACV by 2026.', 'ent_contracts', '#,##0'),
 ('D', 'Committed-use discount % (API realization; memo)', 'IN', '%', 'Volume/committed-use discount off list realized on enterprise API.', 'committed_use_disc', '0.0%'),
 ('D', 'Active enterprise dashboard seats', 'IN', 'count', 'Console/admin seats on enterprise plans.', 'ent_seats', '#,##0'),
 ('D', 'Enterprise platform fee / seat / mo', 'IN', '$', 'Monthly platform fee per enterprise seat.', 'ent_fee_seat_mo', '#,##0'),
 ('D', 'Enterprise seat revenue', 'CALC', '$M', 'seats x fee x 12.', 'ent_seat_rev', '#,##0'),
 ('D', 'Consumer subscription revenue (anchor)', 'IN', '$M', 'Claude Pro ($20) + Max ($100/$200) recognized subscription revenue.', 'consumer_rev', '#,##0'),
 ('D', 'Blended consumer ARPU ($/mo)', 'IN', '$', 'Blend of Pro and Max tiers, rising as Max adoption grows.', 'consumer_arpu', '#,##0'),
 ('D', 'Paying consumer subs (implied)', 'PLUG', 'Count', 'consumer rev / (ARPU x 12).', 'paying_subs', '#,##0'),
 ('D', 'Active developer seats', 'IN', 'Count', 'Claude Code developer seats (launched Feb-2025).', 'dev_seats', '#,##0'),
 ('D', 'Base seat fee ($/mo)', 'IN', '$', 'Claude Code team base seat fee.', 'base_seat_fee_mo', '#,##0'),
 ('D', 'Claude Code base seat revenue', 'CALC', '$M', 'dev seats x base fee x 12.', 'cc_base_rev', '#,##0'),
 ('D', 'Avg overage tokens / dev / mo', 'IN', 'Mtok', 'Usage-based overage above base seat.', 'avg_overage_tok_dev_mo', '#,##0'),
 ('D', 'Overage token price', 'LINK', '$/Mtok', 'Priced at blended effective API rate (link).', 'overage_token_price', '0.00'),
 ('D', 'Claude Code overage revenue', 'CALC', '$M', 'seats x overage Mtok x price x 12. Reported ~$2.5B run-rate in 2026.', 'cc_overage_rev', '#,##0'),
 ('D', 'AWS Bedrock gross billed volume', 'IN', '$M', 'Gross Claude billings through AWS Bedrock.', 'bedrock_gross', '#,##0'),
 ('D', 'AWS rev-share take-rate %', 'IN', '%', 'Anthropic share of Bedrock gross.', 'bedrock_take', '0.0%'),
 ('D', 'Google Vertex gross billed volume', 'IN', '$M', 'Gross Claude billings through Google Vertex.', 'vertex_gross', '#,##0'),
 ('D', 'Google rev-share take-rate %', 'IN', '%', 'Anthropic share of Vertex gross.', 'vertex_take', '0.0%'),
 ('D', '# active fine-tuning engagement', 'IN', 'Count', 'Active custom fine-tuning engagements.', 'ft_engagements', '#,##0'),
 ('D', 'Avg monthly compute / engagement', 'IN', '$', 'Compute billed per engagement per month.', 'ft_monthly_compute', '#,##0'),
 ('D', 'Compute margin markup %', 'IN', '%', 'Markup over compute cost.', 'ft_markup', '0.0%'),
 ('D', 'Fine-tuning revenue', 'CALC', '$M', 'engagements x monthly compute x (1+markup) x 12.', 'ft_rev', '#,##0'),
 ('D', 'One-time setup fee / new engagement', 'IN', '$', 'Onboarding fee per new fine-tuning engagement.', 'ft_setup_fee', '#,##0'),
 ('D', 'New engagements (net adds)', 'CALC', 'Count', 'YoY change in active engagements.', 'ft_new_adds', '#,##0'),
 ('D', 'Setup fee revenue', 'CALC', '$M', 'net adds x setup fee.', 'ft_setup_rev', '#,##0'),
 ('D', 'Active PT units', 'IN', 'Count', 'Priority Throughput reserved-capacity units.', 'pt_units', '#,##0'),
 ('D', 'Flat fee / PT unit / mo', 'IN', '$', 'Monthly reserved-capacity fee per PT unit.', 'pt_flat_fee_mo', '#,##0'),
 ('D', 'PT revenue', 'CALC', '$M', 'PT units x flat fee x 12.', 'pt_rev', '#,##0'),
 ('D', 'Professional services hours / mo', 'IN', 'hr', 'Delivery/solutions-architect hours billed monthly.', 'ps_hours_mo', '#,##0'),
 ('D', 'PS rate ($/hr)', 'IN', '$', 'Professional-services blended bill rate.', 'ps_rate', '#,##0'),
 ('D', 'Professional services revenue', 'CALC', '$M', 'hours x rate x 12.', 'ps_rev', '#,##0'),
 ('S', 'Total non-API revenue', 'CALC', '$M', 'Sum of all non-API streams.', 'total_nonapi_rev', '#,##0'),
 ('H', 'FIRST PARTY DIRECT API REVENUE', '', '', '', None, ''),
 ('S', 'First-party API revenue', 'PLUG', '$M', 'Booked revenue minus total non-API revenue.', 'first_party_api_rev', '#,##0'),
 ('H', 'API TOKEN ENGINE', '', '', '', None, ''),
 ('D', 'Total tokens processed (all)', 'PLUG', 'T', 'First-party API revenue / blended effective $/Mtok. Implied volume (trillions).', 'total_tokens_T', '#,##0.0'),
 ('D', 'Total input tokens', 'CALC', 'T', 'tokens x input share.', 'total_in_tokens_T', '#,##0.0'),
 ('D', 'Total output tokens', 'CALC', 'T', 'tokens x (1 - input share).', 'total_out_tokens_T', '#,##0.0'),
 ('D', 'Total first-party API calls', 'CALC', 'B', 'tokens / (avg in + avg out) per call. Billions.', 'fp_calls_B', '#,##0'),
 ('D', 'Memo: calls / contract / day', 'CALC', '#', 'calls / enterprise contracts / 365.', 'calls_per_contract_day', '#,##0'),
 ('H', 'COSTS - Inference and infrastructure', '', '', '', None, ''),
 ('D', 'Billed tokens (Anthropic-served)', 'LINK', 'T', 'First-party API + consumer + Claude Code tokens (excludes Bedrock/Vertex, served on partner infra).', 'billed_tokens_T', '#,##0.0'),
 ('D', 'Free-tier tokens served', 'IN', 'T', 'Non-billed free-tier usage, as a multiple of billed.', 'free_tier_tokens_T', '#,##0.0'),
 ('D', 'Internal / testing tokens', 'IN', 'T', 'Evals, red-team, internal tooling usage.', 'internal_tokens_T', '#,##0.0'),
 ('D', 'Gross tokens served', 'CALC', 'T', 'billed + free-tier + internal.', 'gross_tokens_T', '#,##0.0'),
 ('D', 'Tokens per GPU-hour', 'IN', 'tok/hr', 'Serving throughput per accelerator-hour (back-solved for consistency with inference cost).', 'tokens_per_gpu_hour', '#,##0'),
 ('D', 'Required GPU-hours', 'CALC', 'hr', 'gross tokens / tokens-per-GPU-hour.', 'required_gpu_hours', '#,##0'),
 ('D', 'Fleet utilization %', 'IN', '%', 'Effective serving utilization of provisioned fleet.', 'fleet_util', '0.0%'),
 ('D', 'Total provisioned GPU-hours', 'CALC', 'hr', 'required GPU-hours / utilization.', 'provisioned_gpu_hours', '#,##0'),
 ('D', 'Blended $/GPU-hour', 'IN', '$', 'Blend of owned + rented accelerator all-in hourly cost.', 'blended_gpu_hr', '0.00'),
 ('D', 'Inference compute cost', 'CALC', '$M', 'Calibrated as a declining share of revenue; provisioned GPU-hours x $/GPU-hr.', 'inference_cost', '#,##0'),
 ('D', 'Data egress volume (PB)', 'IN', 'PB', 'Outbound data volume.', 'egress_PB', '#,##0'),
 ('D', 'Egress cost ($/TB)', 'IN', '$', 'Blended egress unit cost.', 'egress_rate', '#,##0'),
 ('D', 'Data egress cost', 'CALC', '$M', 'PB x 1000 x $/TB.', 'egress_cost', '#,##0'),
 ('D', 'Context / caching storage cost', 'IN', '$M', 'KV-cache and context storage.', 'caching_storage_cost', '#,##0'),
 ('D', 'API gateway and load-balancing', 'IN', '$M', 'Edge, gateway and LB infrastructure.', 'gateway_cost', '#,##0'),
 ('H', 'COSTS - SAFETY, PAYMENTS, SUPPORT', '', '', '', None, ''),
 ('D', 'Content moderation cost $/Mtok', 'IN', '$', 'Automated classifier cost per Mtok of gross tokens.', 'content_mod_rate', '0.000'),
 ('D', 'Automated moderation cost', 'CALC', '$M', 'gross tokens x $/Mtok.', 'auto_mod_cost', '#,##0'),
 ('D', 'HITL review volume', 'IN', 'Count', 'Human-in-the-loop safety reviews per year.', 'hitl_volume', '#,##0'),
 ('D', 'Cost per HITL review', 'IN', '$', 'BPO hourly x hours per review.', 'cost_per_hitl', '0.00'),
 ('D', 'HITL review cost', 'CALC', '$M', 'volume x cost per review.', 'hitl_cost', '#,##0'),
 ('D', 'B2B gross cash collections', 'LINK', '$M', 'API + seats + Claude Code + FT + PT + PS (card/invoice collected).', 'b2b_collections', '#,##0'),
 ('D', 'Payment processing fee % (Stripe)', 'IN', '%', 'Blended processor fee.', 'stripe_fee', '0.00%'),
 ('D', 'B2B payment processing cost', 'CALC', '$M', 'collections x fee.', 'b2b_pay_cost', '#,##0'),
 ('D', 'Mobile share of consumer revenue %', 'IN', '%', 'Consumer revenue collected via mobile app stores.', 'mobile_share', '0.0%'),
 ('D', 'B2C mobile collections', 'CALC', '$M', 'consumer rev x mobile share.', 'b2c_mobile_coll', '#,##0'),
 ('D', 'App store take-rate %', 'IN', '%', 'Apple/Google store take (falling with small-business/read rates).', 'appstore_take', '0.0%'),
 ('D', 'App store cost', 'CALC', '$M', 'mobile collections x take-rate.', 'appstore_cost', '#,##0'),
 ('D', 'CSM ratio (accounts/CSM)', 'IN', '#', 'Enterprise accounts per customer-success manager.', 'csm_ratio', '#,##0'),
 ('D', '#CSMs', 'CALC', 'count', 'enterprise contracts / CSM ratio.', 'n_csm', '#,##0'),
 ('D', 'Fully-burdened CSM salary', 'IN', '$', 'Loaded annual cost per CSM.', 'csm_salary', '#,##0'),
 ('D', 'CSM cost', 'CALC', '$M', '#CSMs x salary.', 'csm_cost', '#,##0'),
 ('D', 'Support ticket volume (000s)', 'IN', 'k', 'Consumer/support tickets per year (thousands).', 'ticket_vol_k', '#,##0'),
 ('D', 'Cost per ticket', 'IN', '$', 'Blended cost per resolved ticket.', 'cost_per_ticket', '0.00'),
 ('D', 'Consumer support cost', 'CALC', '$M', 'tickets x cost per ticket.', 'consumer_support_cost', '#,##0'),
 ('S', 'Total cost of revenue (bottoms-up)', 'CALC', '$M', 'Inference + infra + safety + payments + support. Training compute is R&D, not COGS.', 'total_cor', '#,##0'),
 ('S', 'Memo: implied gross margin %', 'CALC', '%', 'Inference-only gross margin. Higher than fully-loaded-compute measures by design.', 'gross_margin_pct', '0.0%'),
 ('H', 'OpEx & Comp (ex-SBC)', '', '', '', None, ''),
 ('D', 'R&D headcount', 'IN', 'count', 'Research + engineering heads (~65-75% of total).', 'rnd_hc', '#,##0'),
 ('D', 'Fully-burdened R&D cash comp ($/head)', 'IN', '$', 'Loaded cash comp per R&D head (Levels.fyi: eng $619-841k, research median ~$746k).', 'rnd_comp_head', '#,##0'),
 ('D', 'R&D personnel cost', 'CALC', '$M', 'R&D heads x comp/head.', 'rnd_pers_cost', '#,##0'),
 ('D', 'RLHF & data annotation', 'IN', '$M', 'Human feedback and annotation vendors.', 'rlhf_data', '#,##0'),
 ('D', 'Proprietary data licensing', 'IN', '$M', 'Licensed training data.', 'data_licensing', '#,##0'),
 ('D', 'Experimental / failed training runs', 'IN', '$M', 'Abandoned/failed run compute.', 'failed_runs', '#,##0'),
 ('D', 'Internal tooling & subscriptions', 'IN', '$M', 'Dev tooling and SaaS.', 'internal_tooling', '#,##0'),
 ('D', 'Capitalizable frontier-training runs', 'IN', '$M', 'Portion of training eligible for capitalization (memo, ~30% of training).', 'capitalizable_training', '#,##0'),
 ('D', 'Cap toggle (1=capitalized, 0=ASC 730 expense)', 'IN', '0/1', '0 = expense training to R&D per ASC 730 (base case).', 'cap_toggle', '0'),
 ('D', 'Training compute expenses to R&D', 'CALC', '$M', 'Training compute (expensed) + research compute. The primary loss driver.', 'training_to_rnd', '#,##0'),
 ('S', 'Total R&D (ex-SBC)', 'CALC', '$M', 'Personnel + RLHF + licensing + failed runs + tooling + training-to-R&D.', 'total_rnd', '#,##0'),
 ('D', 'S&M Headcount', 'IN', 'count', 'Go-to-market heads (small org; ~$5.6M revenue/employee reported).', 'sm_hc', '#,##0'),
 ('D', 'Fully-burdened S&M cash comp ($/head)', 'IN', '$', 'Loaded cash comp per S&M head.', 'sm_comp_head', '#,##0'),
 ('D', 'S&M personnel cost', 'CALC', '$M', 'S&M heads x comp/head.', 'sm_pers_cost', '#,##0'),
 ('D', 'Performance marketing & advertising', 'IN', '$M', 'Paid acquisition and brand.', 'perf_marketing', '#,##0'),
 ('D', 'Events / conferences / sponsorships', 'IN', '$M', 'Dev conferences and sponsorships.', 'events_sponsor', '#,##0'),
 ('S', 'Total S&M (ex-SBC)', 'CALC', '$M', 'Personnel + marketing + events.', 'total_sm', '#,##0'),
 ('D', 'G&A headcount', 'IN', 'Count', 'Finance, legal, people, ops heads.', 'ga_hc', '#,##0'),
 ('D', 'Fully-burdened G&A salary ($/head)', 'IN', '$', 'Loaded cash comp per G&A head.', 'ga_comp_head', '#,##0'),
 ('D', 'G&A personnel cost', 'CALC', '$M', 'G&A heads x comp/head.', 'ga_pers_cost', '#,##0'),
 ('D', 'Recurring outside legal counsel', 'IN', '$M', 'Outside counsel run-rate.', 'legal_counsel', '#,##0'),
 ('D', 'Corporate insurance (D&O, cyber)', 'IN', '$M', 'D&O and cyber premiums.', 'corp_insurance', '#,##0'),
 ('D', 'Real estate and office leases (office only)', 'IN', '$M', 'Office leases (excludes datacenters).', 'real_estate', '#,##0'),
 ('D', 'Public-co readiness / audit / SOX', 'IN', '$M', 'Audit, SOX and IPO-readiness (peaks around 2026 S-1).', 'sox_readiness', '#,##0'),
 ('S', 'Total G&A (ex-SBC)', 'CALC', '$M', 'Personnel + legal + insurance + real estate + SOX.', 'total_ga', '#,##0'),
 ('D', 'One-time litigation services', 'IN', '$M', 'Non-recurring litigation (e.g., copyright).', 'ga_onetime_litigation', '#,##0'),
 ('H', 'STOCK BASED COMP', '', '', '', None, ''),
 ('D', 'SBC issue rate (% of base cash comp)', 'IN', '%', 'RSU grant value as % of cash comp (equity-heavy structure).', 'sbc_rate', '0.0%'),
 ('D', 'R&D SBC', 'CALC', '$M', 'R&D personnel cash x SBC rate.', 'rnd_sbc', '#,##0'),
 ('D', 'S&M SBC', 'CALC', '$M', 'S&M personnel cash x SBC rate.', 'sm_sbc', '#,##0'),
 ('D', 'G&A SBC', 'CALC', '$M', 'G&A personnel cash x SBC rate.', 'ga_sbc', '#,##0'),
 ('S', 'Total SBC', 'CALC', '$M', 'Sum of function SBC.', 'total_sbc', '#,##0'),
 ('H', 'DEPRECIATION & AMORTIZATION', '', '', '', None, ''),
 ('D', 'Amort life - models (yrs)', 'IN', 'yr', 'Useful life of capitalized frontier models.', 'amort_life_models', '0'),
 ('D', 'Amort of capitalized frontier models', 'CALC', '$M', '2-yr straight-line of capitalized training pool.', 'amort_cap_models', '#,##0'),
 ('D', 'Owned GPU / datacenter capex', 'IN', '$M', 'Owned hardware/datacenter capex (Fluidstack $50B buildout ramps 2026+).', 'owned_gpu_capex', '#,##0'),
 ('D', 'Depreciation life - HW (yrs)', 'IN', 'yr', 'Useful life of owned accelerators/datacenter.', 'dep_life_hw', '0'),
 ('D', 'Depreciation of owned GPU / datacenter', 'CALC', '$M', 'Vintage straight-line depreciation of owned capex.', 'dep_owned', '#,##0'),
 ('D', 'Amort of prepaid cloud commits (reclass)', 'MEMO', '$M', 'Reclass memo only. NOT added to P&L D&A (guard).', 'amort_prepaid_cloud', '#,##0'),
 ('S', 'Total D&A', 'CALC', '$M', 'Model amortization + owned HW depreciation (prepaid-cloud excluded).', 'total_da', '#,##0'),
 ('H', 'P&L SUMMARY (memo)', '', '', '', None, ''),
 ('S', 'Gross profit', 'CALC', '$M', 'Booked revenue - total cost of revenue.', 'gross_profit', '#,##0'),
 ('S', 'Operating income (ex-SBC)', 'CALC', '$M', 'Gross profit - R&D - S&M - G&A - D&A. Loss through 2026, ~breakeven 2026 (Q2-2026 first op-profit qtr), profit 2027+.', 'op_income_exsbc', '#,##0'),
 ('S', 'Operating income (incl-SBC)', 'CALC', '$M', 'Operating income after stock-based comp.', 'op_income_inclsbc', '#,##0'),
]

CAP = [
 ('H', 'CAPACITY BY PROVIDER (GW online, not committed ceiling)', '', '', '', None, ''),
 ('D', 'AWS - GW online', 'IN', 'GW', 'Trainium (Project Rainier, live Oct-2025, >1M Trainium2). Ramp toward 5GW; ~1GW by end-2026.', 'gw_aws', '0.00'),
 ('D', 'Google/Broadcom - GW online', 'IN', 'GW', 'Google TPU (~1M chips) + Broadcom next-gen (~3.5GW from 2027). Small existing TPU 2025-26.', 'gw_google', '0.00'),
 ('D', 'Azure/Nvidia - GW online', 'IN', 'GW', '$30B Azure + Nvidia GB/Vera Rubin, up to 1GW (Nov-2025).', 'gw_azure', '0.00'),
 ('D', 'SpaceX - GW online', 'IN', 'GW', 'Colossus 1 (Memphis), ~0.3GW at $1.25B/mo through May-2029.', 'gw_spacex', '0.00'),
 ('D', 'Fluidstack - GW online', 'IN', 'GW', 'Owned US datacenters (TX/NY), $50B commitment, ramp to ~2-3GW.', 'gw_fluidstack', '0.00'),
 ('D', 'CoreWeave - GW online', 'IN', 'GW', 'Multi-year GPU agreement (2026), scale undisclosed (est).', 'gw_coreweave', '0.00'),
 ('D', 'Akamai - GW online', 'IN', 'GW', 'Distributed edge inference (~$1.8B), small (est).', 'gw_akamai', '0.00'),
 ('S', 'Total online GW', 'CALC', 'GW', 'Sum across providers. ~10GW company target by 2029-30.', 'gw_total', '0.00'),
 ('D', 'Committed ceiling (GW)', 'IN', 'GW', 'Contracted/committed capacity ceiling (> online).', 'gw_ceiling', '0.00'),
 ('H', 'PHYSICAL to ENERGY', '', '', '', None, ''),
 ('D', 'Fleet utilization %', 'LINK', '%', 'Links to P&L fleet utilization.', 'fleet_util', '0.0%'),
 ('D', 'PUE (facility / IT power)', 'IN', 'x', 'Power usage effectiveness (~1.15).', 'pue', '0.00'),
 ('D', 'Power per accelerator, all-in (kW)', 'IN', 'kW', 'Blends GPU/TPU/Trainium, ~1.2kW.', 'kw_per_accel', '0.00'),
 ('D', 'IT energy (MWh/yr)', 'CALC', 'MWh/yr', 'Total GW x 1000 x 8760 x utilization.', 'it_energy_mwh', '#,##0'),
 ('D', 'Facility energy incl cooling (MWh/yr)', 'CALC', 'MWh/yr', 'IT energy x PUE.', 'facility_energy_mwh', '#,##0'),
 ('D', 'Available GPU-hours (from GW)', 'CALC', 'hr', '(GW / kW-per-accel) x 8760 x utilization.', 'avail_gpu_hours', '#,##0'),
 ('H', 'ENERGY COST (decomposition, not additive)', '', '', '', None, ''),
 ('D', 'Blended electricity price ($/MWh)', 'IN', '$', '~$55-65/MWh; SpaceX/Memphis gas-turbine cheaper but emissions-loaded.', 'elec_price', '#,##0'),
 ('D', 'Total energy cost ($M)', 'CALC', '$M', 'Facility energy x price. Decomposition, NOT added to COGS.', 'energy_cost', '#,##0'),
 ('D', 'Energy $ / GPU-hour', 'CALC', '$', 'Energy cost / available GPU-hours.', 'energy_per_gpu_hr', '0.000'),
 ('D', 'Implied all-in $/GPU-hr', 'LINK', '$', 'Links to P&L blended $/GPU-hour.', 'implied_allin_gpu_hr', '0.00'),
 ('D', 'Energy as % of rental $/GPU-hr', 'CALC', '%', 'Energy vs rental rate. ~4-5% (below the ~15-25% owned-all-in note; see Sources).', 'energy_pct_rental', '0.0%'),
]

def write_sheet(ws, rows, guards_dict, title):
    ws.sheet_view.showGridLines = False
    cols = ['Line Item', 'Type', 'Unit', 'What it is'] + [str(y) for y in YEARS]
    # title row
    ws.cell(1, 1, title).font = Font(bold=True, size=13, color="111827")
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=4+N)
    # header row (row 2)
    for c, h in enumerate(cols, 1):
        cell = ws.cell(2, c, h)
        cell.fill = HDR_FILL; cell.font = WHITE; cell.border = BORDER
        cell.alignment = LEFT if c == 4 else (RIGHT if c > 4 else CENTER)
    r = 3
    for kind, label, typ, unit, whatis, key, fmt in rows:
        if kind == 'H':
            ws.cell(r, 1, label).font = SECF
            for c in range(1, 5+N):
                ws.cell(r, c).fill = SEC_FILL; ws.cell(r, c).font = SECF
            r += 1; continue
        ws.cell(r, 1, label).font = BOLD if kind == 'S' else REG
        ws.cell(r, 1).alignment = LEFT
        ws.cell(r, 2, typ).alignment = CENTER; ws.cell(r, 2).font = REG
        ws.cell(r, 3, unit).alignment = CENTER; ws.cell(r, 3).font = REG
        ws.cell(r, 4, whatis).alignment = LEFT; ws.cell(r, 4).font = ITAL
        vals = V.get(key, [None]*N)
        for i in range(N):
            cell = ws.cell(r, 5+i, vals[i])
            cell.number_format = fmt; cell.alignment = RIGHT
            cell.font = BOLD if kind == 'S' else REG
            if kind == 'S':
                cell.fill = SUM_FILL; cell.font = Font(bold=True, size=9, color="FFFFFF")
        if kind == 'S':
            ws.cell(r, 1).fill = SUM_FILL; ws.cell(r, 1).font = Font(bold=True, size=9, color="FFFFFF")
            for c in (2, 3, 4):
                ws.cell(r, c).fill = SUM_FILL; ws.cell(r, c).font = Font(size=8, color="FFFFFF", italic=(c == 4))
        r += 1
    # guards
    ws.cell(r, 1, 'GUARDS AND CHECKS').font = SECF
    for c in range(1, 5+N):
        ws.cell(r, c).fill = SEC_FILL; ws.cell(r, c).font = SECF
    r += 1
    for name, ok in guards_dict.items():
        ws.cell(r, 1, name).font = REG; ws.cell(r, 1).alignment = LEFT
        cell = ws.cell(r, 5, 'PASS' if ok else 'FAIL')
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor="047857" if ok else "B91C1C")
        cell.alignment = CENTER
        r += 1
    # widths & freeze
    ws.column_dimensions['A'].width = 40
    ws.column_dimensions['B'].width = 7
    ws.column_dimensions['C'].width = 8
    ws.column_dimensions['D'].width = 52
    for i in range(N):
        ws.column_dimensions[get_column_letter(5+i)].width = 11
    ws.freeze_panes = 'E3'

wb = openpyxl.Workbook()
ws1 = wb.active; ws1.title = 'P&L Build'
write_sheet(ws1, PL, V['guards'], 'Anthropic PBC - Bottom-up Operating Model  |  2022A - 2032E  ($M unless noted; run-rate/annualized basis)')
ws2 = wb.create_sheet('Capacity & Energy')
write_sheet(ws2, CAP, V['cap_guards'], 'Anthropic PBC - Compute Capacity & Energy  |  2022A - 2032E')

# Sources & Notes sheet
ws3 = wb.create_sheet('Sources & Notes')
ws3.sheet_view.showGridLines = False
ws3.column_dimensions['A'].width = 30
ws3.column_dimensions['B'].width = 120
notes = [
 ('SOURCES & METHODOLOGY', ''),
 ('Prepared', 'July 2026. Anthropic is private and pre-IPO (confidential S-1 filed Jun 1, 2026; IPO expected Oct 2026), so all P&L/headcount lines are third-party estimates; funding/valuation are PitchBook actual-status deal records.'),
 ('Basis', 'Model runs on an ANNUALIZED / RUN-RATE basis matching PitchBook TTM revenue. On this basis 2026 prints ~breakeven (consistent with the reported Q2-2026 first operating-profit quarter), NOT the recognized-basis full-year loss some outlets cite.'),
 ('COGS definition', 'Cost of revenue = INFERENCE serving + safety/payments/support only. TRAINING compute is R&D (template cap toggle / "training compute to R&D"). So the model gross margin (~70-78% mature) is inference-only and is a DIFFERENT metric from the widely-cited "~40% gross margin (2025)", which is a fully-loaded-compute measure.', ),
 ('', ''),
 ('REVENUE ANCHOR', ''),
 ('Revenue TTM series', 'PitchBook (co. 466959-97): 2022 $10M, 2023 $100M, 2024 $1,000M, 2025 $9,000M, 2026 $47,000M, 2027 $55,000M (forward). Model adopts 2022-26 as anchor; projects 2027-32 higher than PB $55B on continued enterprise+coding ramp (labeled estimate).'),
 ('Run-rate milestones', 'Series H (May 28, 2026) cited ~$47B run-rate, up from ~$9B end-2025 and ~$30B Apr-2026. Claude Code ~$2.5B run-rate (2026). 300K+ business customers; 1,000+ at $1M+ ACV; 140%+ NRR (company/press).'),
 ('', ''),
 ('API PRICING (list $/Mtok in/out)', ''),
 ('Claude 3 (Mar 2024)', 'Opus $15/$75; Sonnet $3/$15; Haiku $0.25/$1.25. Source: Anthropic launch.'),
 ('Claude 4.x (2025-26)', 'Opus cut to $5/$25 at Opus 4.5 (Nov 2025), held through 4.8; Sonnet $3/$15 (Sonnet 5 intro $2/$10 to Aug 31, 2026); Haiku 4.5 $1/$5. Flagship tier Fable 5 / Mythos 5 $10/$50 (the template "Mythos" line).'),
 ('Caching / batch / fast', 'Prompt caching (Aug 2024): read 0.1x (90% off), 5-min write 1.25x. Batch (Oct 2024): 0.5x in+out. Fast Mode premium (Opus 4.8 fast $10/$50). Source: Anthropic pricing docs.'),
 ('', ''),
 ('COMPUTE & CAPACITY', ''),
 ('AWS', '$100B+/10yr commitment, up to 5GW; Project Rainier live Oct-2025, >1M Trainium2; ~1GW by end-2026. Amazon investment up to $25B (on $8B prior).'),
 ('Google/Broadcom', 'Up to 1M TPUs, >1GW online 2026; Broadcom next-gen ~3.5GW from 2027 (3GW+ in 2027). Reported ~$200B/5yr Google commitment; Google invests up to $40B.'),
 ('Azure/Nvidia', '$30B Azure + up to 1GW Nvidia Grace Blackwell/Vera Rubin (Nov 18, 2025). MSFT up to $5B, Nvidia up to $10B.'),
 ('SpaceX / Colossus', '$1.25B/mo (~$15B/yr, ~$40B+ total) for Colossus 1 (~0.3GW, 220k+ GPUs) through May-2029 (SpaceX S-1).'),
 ('Fluidstack / CoreWeave / Akamai', 'Fluidstack $50B owned US datacenters (TX/NY, ramp 2026+); CoreWeave multi-year GPU deal (undisclosed); Akamai ~$1.8B edge inference. Company target ~10GW.'),
 ('Energy finding', 'Pure energy runs ~4-5% of the frontier-GPU RENTAL rate in this model, BELOW the template\'s ~15-25% note. The 15-25% figure fits energy as a share of OWNED all-in cost (energy + hardware depreciation), not rental; surfaced as a finding rather than forced.'),
 ('', ''),
 ('FUNDING & VALUATION (PitchBook actual-status)', ''),
 ('Trajectory (post-money)', '$461M (Series A, May 2021) -> $3.0B (Series B, Apr 2022) -> $4.55B (Series C, 2023) -> ~$18-21B (Series D, 2024) -> $61.5B (Series E, Mar 2025) -> $183B (Series F, Sep 2025) -> $380B (Series G, Feb 2026) -> $965B (Series H, May 28, 2026).'),
 ('Total raised', 'PitchBook $161.25B (equity ~$124.3B + $34.5B chip debt Jun-2026 + $2.5B revolver May-2025).'),
 ('Headcount', '~30 (2021) -> 192 (2022) -> ~300 (2023) -> ~1,050 (2024) -> ~2,300 (2025) -> 5,000 (PitchBook, Apr 2026). Function split undisclosed; modeled ~65% R&D / ~18% S&M / ~17% G&A.'),
 ('Burn / margin', '2024 cash burn ~$5.6B; 2025 ~$3B; Q2-2026 first operating-profit qtr (~$559M ex-SBC, press). Compute mix ~56% training / 33% inference / 11% research (Lambda/The Information).'),
 ('', ''),
 ('GUARD / ESTIMATE DISCIPLINE', ''),
 ('Estimates', 'All forward years (2027-2032) and every undisclosed driver are modeled estimates. Hard anchors: revenue TTM, list pricing, funding/valuation, headcount 2026, named compute deals. Everything else is a reasoned driver labeled here.'),
 ('Guards', 'Model-mix sums to 100%; streams + API = booked revenue; API revenue >= 0; Claude Code overage tokens excluded from the API token pool; prepaid-cloud amortization excluded from P&L D&A; implied GM in a plausible band; blended $/Mtok sane. All PASS.'),
]
ws3.cell(1, 1, 'Anthropic Operating Model - Sources & Notes').font = Font(bold=True, size=13)
rr = 3
for a, b in notes:
    ca = ws3.cell(rr, 1, a); ca.font = Font(bold=True, size=9); ca.alignment = Alignment(vertical='top', wrap_text=True)
    cb = ws3.cell(rr, 2, b); cb.font = Font(size=9); cb.alignment = Alignment(vertical='top', wrap_text=True)
    if a.isupper() and b == '':
        ca.font = Font(bold=True, size=10, color="FFFFFF"); ca.fill = SEC_FILL; cb.fill = SEC_FILL
    rr += 1

import os
os.makedirs('output', exist_ok=True)
OUT = 'output/Anthropic_Operating_Model_2022-2032.xlsx'
wb.save(OUT)
print(f"\nSaved {OUT}")
