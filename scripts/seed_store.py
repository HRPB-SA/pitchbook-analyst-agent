"""One-time store seed from the July 2026 canonical pack.

Provenance: Databricks from the July 10, 2026 live re-verification log in this
repo (validation_log.md); the other Frontier Five names from the canonical
refresh of July 16, 2026. Facts carry their original as-of dates, sources and
tiers; staleness is computed live by the engine, so old facts surface as
STALE rather than being silently trusted.

Run once: python3 scripts/seed_store.py
Idempotent-ish: snapshots are append-only; re-running adds duplicate snapshots
but merge keeps canonical stable. Don't re-run casually.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from engine import store
from engine.schema import fact as F

VAL = "validation pack, July 10, 2026"
CTX = "canonical refresh, July 16, 2026"

UNIVERSE = {
    "companies": [
        {"slug": "databricks", "name": "Databricks, Inc.", "pb_entity_id": "59199-40",
         "group": "frontier_five", "sector": "AI-PLAT"},
        {"slug": "anthropic", "name": "Anthropic", "pb_entity_id": "466959-97",
         "group": "frontier_five", "sector": "AI-INFRA"},
        {"slug": "openai", "name": "OpenAI", "pb_entity_id": "149504-14",
         "group": "frontier_five", "sector": "AI-INFRA"},
        {"slug": "xai-spacex", "name": "xAI (within SpaceX, SPCX)", "pb_entity_id": None,
         "group": "frontier_five", "sector": "AI-INFRA"},
        {"slug": "ssi", "name": "Safe Superintelligence (SSI)", "pb_entity_id": None,
         "group": "frontier_five", "sector": "AI-INFRA"},
        {"slug": "perplexity", "name": "Perplexity", "pb_entity_id": None,
         "group": "coverage", "sector": "AI-APP"},
        {"slug": "scale-ai", "name": "Scale AI", "pb_entity_id": None,
         "group": "coverage", "sector": "AI-INFRA"},
        {"slug": "coreweave", "name": "CoreWeave", "pb_entity_id": None,
         "group": "coverage", "sector": "AI-INFRA"},
        {"slug": "cursor", "name": "Cursor (Anysphere)", "pb_entity_id": None,
         "group": "coverage", "sector": "AI-APP"},
        {"slug": "mistral", "name": "Mistral AI", "pb_entity_id": None,
         "group": "coverage", "sector": "AI-INFRA"},
        {"slug": "elevenlabs", "name": "ElevenLabs", "pb_entity_id": None,
         "group": "coverage", "sector": "AI-APP"},
        {"slug": "cohere", "name": "Cohere", "pb_entity_id": None,
         "group": "coverage", "sector": "AI-INFRA"},
        {"slug": "openevidence", "name": "OpenEvidence", "pb_entity_id": None,
         "group": "coverage", "sector": "AI-APP"},
    ]
}

DATABRICKS = {
    "identity": {
        "name": F("Databricks, Inc.", "2026-07-10", VAL, "T2", decay="PERMANENT"),
        "pb_entity_id": F("59199-40", "2026-07-09", "PitchBook profile", "T2", decay="STABLE"),
        "hq": F("San Francisco (+46 offices)", "2026-06-09", "PitchBook", "T2", decay="STABLE"),
        "ceo": F("Ali Ghodsi", "2026-07-10", VAL, "T2", decay="STABLE"),
        "sector": F("AI-PLAT (lakehouse / data + AI platform)", "2026-07-10", VAL, "T2", decay="STABLE"),
    },
    "valuation": {
        "post_money_bn": F(134, "2026-02-09",
                           "Series L, company PR Dec 2025 + PitchBook deal 313367-68T", "T2",
                           decay="STABLE", note="held flat across two closes"),
        "rumored_round": F("$165-175B in talks, unclosed", "2026-07-07",
                           "press reports Jun 9 + PitchBook financing note Jul 7 (deal 334745-56T, Rumor/Speculation)",
                           "T3", decay="VOLATILE", flags=["do-not-adopt"],
                           note="analyzed as forward signal, never anchors the base case"),
    },
    "financing": {
        "total_raised_bn": F(29.5, "2026-07-10", "PitchBook Total Raised $29,515.7M, 21 tracked deals", "T2", decay="STABLE"),
        "equity_raised_bn": F(20.2, "2026-07-10", "PitchBook 21-deal decomposition, 12 completed equity rounds A-L", "T2",
                              decay="STABLE", flags=["est."], note="equity ~= $20.2-20.4B within rounding"),
        "debt_raised_bn": F(9.3, "2026-07-10", "PitchBook deal records: 4 debt deals + embedded", "T2",
                            decay="STABLE", flags=["est."]),
        "last_completed_deal": F("Series L $7.0B ($5.0B equity led by Insight/JPM Growth/Fidelity + Microsoft and ~44 others, $2.0B debt)",
                                 "2026-02-09", "PitchBook deal 313367-68T + company PR", "T2", decay="STABLE"),
        "active_investors": F(148, "2026-07-09", "PitchBook profile", "T2", decay="STABLE"),
    },
    "financials": {
        "run_rate_ladder_bn": [
            F(4.0, "2025-09-30", "company PR", "T2", note="+50% YoY"),
            F(4.8, "2025-12-31", "company PR", "T2", note="+55% YoY"),
            F(5.4, "2026-02-09", "company PR", "T2", note="+65% YoY"),
            F(6.9, "2026-06-16", "company disclosure (analyst session)", "T2", note="+80% YoY"),
        ],
        "growth_yoy_pct_ladder": [
            F(50, "2025-09-30", "company PR", "T2"),
            F(55, "2025-12-31", "company PR", "T2"),
            F(65, "2026-02-09", "company PR", "T2"),
            F(80, "2026-06-16", "company disclosure", "T2"),
        ],
        "gross_margin_pct_ladder": [
            F(80, "2025-12-31", "company (prior level, 'above 80%')", "T2", flags=["est."]),
            F(74, "2026-06-16", "company disclosure; guided to decline further on agent-driven compute", "T2"),
        ],
        "fcf_status": F("Positive, TTM and FY2025 bases; magnitude undisclosed", "2026-02-09",
                        "company PR", "T2", decay="QUARTERLY"),
        "pb_ttm_field_note": F("PitchBook revenue $6,900M labeled TTM 4Q2026 (period end 2026-12-31) = forward-window projection, NOT run-rate",
                               "2026-07-10", VAL, "T2", decay="PERMANENT",
                               note="Ruling 4: never adopt PB TTM as current ARR"),
    },
    "headcount": {
        "employees_ladder": [F(9000, "2026-06-09", "PitchBook", "T2")],
    },
    "products": {
        "ai_products_run_rate_bn": F(1.7, "2026-06-16", "company disclosure", "T2",
                                     note="largest, fastest line; $1.0B Dec-25 -> $1.4B Feb-26 -> $1.7B Jun-26"),
        "dbsql_run_rate_bn": F(1.5, "2026-06-16", "press reports of company disclosure", "T2",
                               note="data warehousing, doubled YoY"),
        "lakebase": F("Thousands of customers in first six months; revenue growing at 2x the DW product's pace at equivalent stage",
                      "2026-02-09", "company PR", "T2"),
    },
    "customers": {
        "nrr_pct": F(">140%", "2026-02-09", "company PR", "T2"),
        "orgs": F(20000, "2026-02-09", "company PR", "T2", note="20,000+ organizations"),
        "customers_1m_plus": F(800, "2026-02-09", "company PR", "T2", note="800+"),
        "customers_10m_plus": F(70, "2026-02-09", "company PR", "T2", note="70+"),
        "fortune500_pct": F(">60%", "2026-02-09", "company PR", "T2"),
    },
    "leadership": {
        "ceo": F("Ali Ghodsi", "2026-07-10", VAL, "T2", decay="STABLE"),
        "naveen_rao_status": F("Departed Sep 12, 2025 to found AI-hardware startup; advisory role retained; Databricks investing",
                               "2025-09-12", "press reports", "T3", decay="STABLE",
                               note="digested; residual key-person watch on the AI line"),
    },
    "competition": {
        "snowflake_mkt_cap_bn": F(91.1, "2026-07-07", "market data aggregators", "T3", decay="VOLATILE"),
        "snowflake_fwd_product_rev_bn": F(5.84, "2026-05-27", "Snowflake 8-K, Q1 FY27 guide, +31%", "T1", decay="QUARTERLY"),
        "vs_snowflake": F("Databricks revenue has overtaken Snowflake; gap ~$1.6B and widening", "2026-06-30",
                          "third-party analyst data", "T3", decay="QUARTERLY", flags=["est."]),
    },
    "deals_ma": {
        "acquisitions_count": F(19, "2026-07-10", "aggregated company disclosures + press", "T3",
                                flags=["est."], decay="STABLE"),
        "latest": F("Panther (security, 3rd security deal; terms undisclosed; $1.4B is Panther's 2021 mark, not a price)",
                    "2026-06-16", "company announcement + press", "T2", decay="STABLE"),
    },
    "ipo_status": {
        "s1_status": F("No S-1 on file; Form D / D/A only (latest 2025-12-31)", "2026-07-10",
                       "SEC EDGAR submissions API, CIK 0001587468", "T1"),
        "window": F("2026 publicly ruled out by CEO; 2027 earliest", "2026-06-04",
                    "company (CEO television interview)", "T2"),
        "prediction_market": F("'No Databricks IPO by Dec 31, 2027' priced 0.54", "2026-07-07",
                               "prediction-market aggregator", "T3", flags=["est."]),
    },
    "scores": {
        "aibq_composite": F(8.81, "2026-07-10", "internal re-score (this desk)", "T2",
                            note="Elite band; prior 8.92; CE 8.9 / RQ 9.0 / CI 8.0 / GO 8.9 / MD 9.0, CRA 0"),
        "aibq_dimensions": F({"CE": 8.9, "RQ": 9.0, "CI": 8.0, "GO": 8.9, "MD": 9.0, "CRA": 0.0},
                             "2026-07-10", "internal re-score (this desk)", "T2"),
    },
    "events": {
        "stream": [
            F("Series L first close >$4B at $134B", "2025-12-15", "company PR", "T2", decay="PERMANENT"),
            F("Series L final close $7.0B total at $134B", "2026-02-09", "PitchBook deal record", "T2", decay="PERMANENT"),
            F("Panther acquisition announced", "2026-06-16", "company + press", "T2", decay="PERMANENT"),
            F("Run-rate $6.9B (+80%) disclosed at Data + AI Summit", "2026-06-16", "company disclosure", "T2", decay="PERMANENT"),
        ],
    },
    "triggers": {
        "named": [
            F({"condition": "Next quarterly print (expected Sep-Oct 2026): gross margin vs the 70% efficiency gate; ~4-point cushion at 74%",
               "status": "armed"}, "2026-07-10", VAL, "T2"),
            F({"condition": "$165-175B round: closes (adopt and re-mark) or lapses (rumor retired)",
               "status": "armed"}, "2026-07-10", VAL, "T3"),
            F({"condition": "S-1 filing at SEC EDGAR CIK 0001587468 (none on file as of Jul 10, 2026)",
               "status": "armed"}, "2026-07-10", VAL, "T1"),
            F({"condition": "Metrics refresh: NRR / customer counts are Feb 2026 vintage; stale after Sep 2026 disclosure",
               "status": "armed"}, "2026-07-10", VAL, "T2"),
        ],
    },
}

ANTHROPIC = {
    "identity": {
        "name": F("Anthropic", "2026-07-16", CTX, "T2", decay="PERMANENT"),
        "pb_entity_id": F("466959-97", "2026-07-16", "PitchBook profile", "T2", decay="STABLE"),
        "sector": F("AI-INFRA (frontier lab)", "2026-07-16", CTX, "T2", decay="STABLE"),
    },
    "valuation": {
        "post_money_bn": F(965, "2026-05-28", "Series H $65B (Dragoneer/Sequoia/Greenoaks/Altimeter), confirmed on PitchBook Jul 16",
                           "T2", decay="VOLATILE"),
    },
    "financing": {
        "total_raised_bn": F(161.3, "2026-07-16", "PitchBook total raised $161.254B, confirmed live", "T2", decay="STABLE"),
        "equity_raised_bn": F(124.3, "2026-07-02", "canonical decomposition: excludes $34.5B chip bonds + $2.5B revolver", "T2", decay="STABLE"),
        "debt_raised_bn": F(37.0, "2026-07-02", "PB 334763-02T ($34.5B tranched chip bonds) + 295197-04T ($2.5B revolver)", "T2", decay="STABLE"),
    },
    "financials": {
        "run_rate_ladder_bn": [
            F(47, "2026-05-15", "company-announced run-rate (gross basis)", "T2",
              flags=["VERIFY"], note="GROSS basis (incl. cloud partner sales); equalized net ~$28.3B at 39.75% (Ruling 5); STALE past quarterly decay"),
        ],
        "fy2025_revenue_bn": F(9.0, "2026-07-16", "PitchBook financials", "T2", decay="STABLE"),
        "pb_ttm_field_note": F("PB revenue field $55B TTM 4Q2027 (period end 2027-12-31) = forward projection, NOT run-rate. Do not adopt.",
                               "2026-07-16", CTX, "T2", decay="PERMANENT"),
        "first_operating_profit": F("~$559M expected Q2 2026", "2026-05-28", "press reports", "T3", flags=["VERIFY"]),
    },
    "headcount": {"employees_ladder": [F(5000, "2026-04-21", "PitchBook", "T2")]},
    "customers": {
        "nrr_pct": F("140%+", "2026-05-15", "company-announced", "T2"),
        "business_customers": F("300K+", "2026-05-15", "company-announced", "T2"),
        "acv_1m_plus": F("1,000+", "2026-05-15", "company-announced", "T2"),
        "claude_code_arr_bn": F(2.5, "2026-05-15", "company-announced", "T2", note="54% coding share"),
    },
    "ipo_status": {
        "s1_status": F("Confidential S-1 filed Jun 1, 2026", "2026-06-01", "press + PitchBook", "T2"),
        "window": F("October 2026 expected (PitchBook financing note, refreshed Jul 6)", "2026-07-16", "PitchBook", "T2"),
    },
    "scores": {
        "aibq_composite": F(8.20, "2026-05-27", "internal AIBQ v3.0 (this desk)", "T2",
                            note="Strong band / S5 / AI-INFRA"),
    },
    "triggers": {
        "named": [
            F({"condition": "Anthropic S-1 public filing / October 2026 pricing vs OpenAI sequencing", "status": "armed"},
              "2026-07-16", CTX, "T2"),
            F({"condition": "Run-rate refresh: $47B gross is May vintage, past quarterly decay; SEC gross-to-net restatement exposure 20-40%",
               "status": "armed"}, "2026-07-16", CTX, "T2"),
        ],
    },
}

OPENAI = {
    "identity": {
        "name": F("OpenAI", "2026-07-16", CTX, "T2", decay="PERMANENT"),
        "pb_entity_id": F("149504-14", "2026-07-16", "PitchBook profile", "T2", decay="STABLE"),
        "sector": F("AI-INFRA (frontier lab)", "2026-07-16", CTX, "T2", decay="STABLE"),
    },
    "valuation": {
        "post_money_bn": F(852, "2026-03-31", "$122B round at $730B pre, confirmed on PitchBook Jul 16", "T2", decay="VOLATILE"),
    },
    "financing": {
        "total_raised_bn": F(186.4, "2026-07-16", "PitchBook $186.4365B", "T2", decay="STABLE"),
        "equity_raised_bn": F(181.2, "2026-07-16", "canonical: excludes $5.2365B debt (incl. $520M Jul-8 deal 338367-43T)", "T2", decay="STABLE"),
        "debt_raised_bn": F(5.2, "2026-07-16", "PitchBook debt decomposition", "T2", decay="STABLE"),
    },
    "financials": {
        "run_rate_ladder_bn": [
            F(25, "2026-06-12", "desk estimate, net basis", "T3",
              flags=["est.", "VERIFY"], note="NET basis; PB $30B TTM 4Q2026 is a forward projection (Ruling 4)"),
        ],
        "fy2025_leak": F("Rev $13.07B / op loss $20.92B / group loss $60.35B incl. $41.55B FV swing; $17.2B paid to MSFT",
                         "2026-06-16", "press reports of audited FY2025 (verified leak)", "T3", decay="STABLE"),
        "gross_margin_2025_pct": F(33, "2026-02-27", "investor documents (press-reported)", "T3", decay="STABLE",
                                   note="13pp miss vs 46% plan"),
        "infra_obligations_tn": F(1.15, "2026-02-27", "investor documents (press-reported), 7 vendors", "T3", decay="STABLE"),
    },
    "headcount": {"employees_ladder": [F(4500, "2026-03-21", "PitchBook", "T2")]},
    "ipo_status": {
        "s1_status": F("Confidential S-1 filed Jun 8, 2026", "2026-06-08", "press + PitchBook", "T2"),
        "window": F("September 2026 (PitchBook, note refreshed Jul 9) vs media 2027-lean; CONFLICT FROZEN, both branches live",
                    "2026-07-16", "PitchBook + press", "T2", flags=["DISPUTED"]),
    },
    "leadership": {
        "altman_pb_listing": F("PB lists Altman as 'Co-Founder, Co-CEO & Board Member', persistent 5+ weeks across a live refresh",
                               "2026-07-16", "PitchBook profile", "T2", flags=["VERIFY"],
                               note="either a real governance change or a durable data error; resolve before media use"),
    },
    "scores": {
        "aibq_composite": F(4.53, "2026-05-27", "internal AIBQ v3.0 (this desk)", "T2",
                            note="Developing band / S5 / AI-INFRA"),
    },
    "triggers": {
        "named": [
            F({"condition": "OpenAI roadshow range vs the $852B mark; Sep (PB) vs 2027 (media) sequencing conflict",
               "status": "armed"}, "2026-07-16", CTX, "T2"),
            F({"condition": "Altman Co-CEO listing on PitchBook: governance change or data error", "status": "armed"},
              "2026-07-16", CTX, "T2"),
        ],
    },
}

XAI = {
    "identity": {
        "name": F("xAI (within SpaceX, ticker SPCX)", "2026-07-16", CTX, "T2", decay="PERMANENT"),
        "structure": F("All-stock merger into SpaceX completed Feb 2, 2026 at $250B; SPCX listed Jun 12, 2026",
                       "2026-07-16", CTX, "T2", decay="STABLE"),
    },
    "valuation": {
        "post_money_bn": F(1250, "2026-07-16",
                           "SOTP residual estimate: implied AI segment ~$1.10-1.41T at the ~$1.77T Jul-15 tape (midpoint carried)",
                           "T3", decay="VOLATILE", flags=["est."],
                           note="was ~$1.4-1.7T at the $2.11T Jun-12 close; method in rush note"),
        "spcx_market_cap_tn": F(1.79, "2026-07-15", "market tape, level DISPUTED ~$132-141/sh", "T3",
                                decay="VOLATILE", flags=["est.", "DISPUTED"]),
    },
    "financing": {
        "equity_raised_bn": F(47.16, "2026-02-02", "pre-merger cumulative", "T2", decay="STABLE"),
    },
    "financials": {
        "run_rate_ladder_bn": [
            F(3.2, "2025-12-31", "SEC S-1: AI segment FY2025 revenue (xAI + X)", "T1",
              note="~$1.25B ex-X-ads (~6.7% of company revenue)"),
        ],
        "segment_detail": F("AI segment FY25: $3.2B rev, -$6.36B op, capex $12.7B; Q1-26 $818M rev, -$2.47B op, capex $7.7B (76% of group)",
                            "2026-05-20", "SEC S-1 + Q1 filing", "T1", decay="QUARTERLY"),
    },
    "ipo_status": {
        "listing": F("Public within SPCX since Jun 12, 2026; broke $135 IPO price Jul 15, 2026 (named trigger fired)",
                     "2026-07-15", "cross-confirmed press (event T2; level disputed)", "T2"),
        "next_print": F("SPCX Q2 2026 earnings Aug 6, 2026: first public frontier-AI-adjacent print; first lockup tranche same day",
                        "2026-07-16", CTX, "T2"),
    },
    "scores": {
        "aibq_composite": F(4.49, "2026-05-27", "internal AIBQ v3.0 (this desk)", "T2",
                            note="Developing band / S4 / AI-INFRA"),
    },
    "triggers": {
        "named": [
            F({"condition": "SPCX 30-day VWAP vs $135 IPO price", "status": "fired", "fired_on": "2026-07-15"},
              "2026-07-16", CTX, "T2"),
            F({"condition": "SPCX Q2 2026 print Aug 6 + first lockup tranche; staged unlocks through Dec 2026",
               "status": "armed"}, "2026-07-16", CTX, "T3"),
        ],
    },
}

SSI = {
    "identity": {
        "name": F("Safe Superintelligence (SSI)", "2026-07-16", CTX, "T2", decay="PERMANENT"),
        "sector": F("AI-INFRA (pre-revenue frontier lab)", "2026-07-16", CTX, "T2", decay="STABLE"),
    },
    "valuation": {
        "post_money_bn": F(31, "2026-06-12", "canonical ~$30-32B, midpoint carried; NOT re-pulled at the Jul 16 refresh",
                           "T3", decay="VOLATILE", flags=["est.", "VERIFY"]),
    },
    "financing": {"equity_raised_bn": F(3, "2026-06-12", "canonical", "T2", decay="STABLE")},
    "financials": {"run_rate_ladder_bn": [F(0, "2026-06-12", "pre-revenue", "T2")]},
    "scores": {
        "aibq_composite": F(2.30, "2026-05-27", "internal AIBQ v3.0 (this desk)", "T2",
                            note="Distressed band / S1 / AI-INFRA"),
    },
}


def seed():
    store._write(os.path.join(store.DATA, "universe.json"), UNIVERSE)
    print("universe: 13 companies")
    for slug, snap in [("databricks", DATABRICKS), ("anthropic", ANTHROPIC),
                       ("openai", OPENAI), ("xai-spacex", XAI), ("ssi", SSI)]:
        as_of = "2026-07-10" if slug == "databricks" else "2026-07-16"
        name = store.add_snapshot(slug, snap, as_of=as_of)
        rep = store.merge_snapshot(slug, snap)
        print(f"{slug}: snapshot {name}; +{len(rep['added'])} added, "
              f"{len(rep['frozen'])} frozen, {len(rep['superseded'])} superseded")
    for c in UNIVERSE["companies"]:
        if c["slug"] not in ("databricks", "anthropic", "openai", "xai-spacex", "ssi"):
            p = store.load_profile(c["slug"])
            p.setdefault("identity", {})["name"] = F(c["name"], "2026-07-16", CTX, "T2", decay="PERMANENT")
            store.save_profile(c["slug"], p)
    print("skeleton profiles for 8 coverage names")


if __name__ == "__main__":
    seed()
