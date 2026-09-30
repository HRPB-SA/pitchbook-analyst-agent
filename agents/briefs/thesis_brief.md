# Bull / Bear / Judge brief (analyst-bull, analyst-bear, analyst-judge)

The question: **Is the desk bullish or bearish on Anthropic equity around its IPO, and why?** Today is 2026-09-30; Anthropic is private, S-1 confidential, listing expected Oct/Nov 2026.
Reference prices: Series H post-money $965B (May 28 2026, priced round), reported secondary marks ~$1.5T, reported IPO target ~$2T (reported, not confirmed).
Horizon: 12 to 24 months after listing. A call without a price is not a call: every verdict is stated **at each reference price** using the model's reverse-DCF.
Rigor 4/5. A true claim with an undefended flank costs credibility; every attackable claim carries its defense in the artifact.

## Inputs (read first)
```
cd /home/user/pitchbook-analyst-agent
cat data/topics.json | python3 -c "import json,sys; [print(t['slug'],'|',t['one_liner']) for t in json.load(sys.stdin)['topics']]"     # topic analyses (what/means/implications, watch items)
python3 -c "import json; d=json.load(open('data/model.json')); print(json.dumps(d['outputs'], indent=0)[:6000])"                    # three-scenario model outputs incl. reverse-DCF marks
python3 scripts/q.py --table rounds ; --table run_rate_desk ; --table margins ; --table compute ; --table prospectus_facts ; --table comparables ; --table market_share ; --table cases
python3 scripts/q.py --conflicts ; python3 scripts/q.py --open ; python3 scripts/q.py --ids <ids>
cat data/compute.json | head -c 6000
```
Event ids you cite must exist (`q.py --ids` prints `# unknown id` otherwise). Tiers T1 primary … T5 social; anything DISPUTED/VERIFY stays flagged in your prose. Anthropic revenue is GROSS of cloud-partner resale, OpenAI's is NET;
run-rate is not recognized revenue; "up to" is not contracted; debt is not equity; PitchBook TTM 4Q2026/4Q2027 fields are forward projections.

## analyst-bull and analyst-bear (run independently, in parallel; never read each other's output)
Write the strongest case FOR (bull) or AGAINST (bear) owning Anthropic at the reference prices, with the same evidentiary standard. A manufactured case is worthless: if your side is weak on a point, say so in one line.
Output ONE JSON file: `agents/outputs/analyst-bull.json` or `analyst-bear.json`:
```
{"agent": "...", "role": "Bull Analyst|Bear Analyst", "started": "<ISO>", "finished": "<ISO>",
 "case": [ {"claim": "<one sentence, sharp>", "evidence": "<2-3 sentences: dated, tiered, named source in words, basis stated>", "event_ids": ["..."], "strength": 1-5,
            "type": "growth|margin|moat|valuation|capital|catalyst|structure|governance|legal|compute", "defense": "<the best attack on this claim and the answer>"} ],       // 6 to 9 claims, ranked
 "at_price": [ {"mark": "series_h|secondary|ipo_target", "ev_usd_m": n, "argument": "<what has to be true at this price for your side; use the model's reverse-DCF numbers (required 2030 revenue, CAGR) and say how they compare with the outside view>"} ],
 "outside_view": {"reference_class": "...", "base_rate": "...", "source": "<record or 'recalled (unverified)'>", "what_is_different": "..."},
 "thesis_breakers": [ {"metric": "...", "threshold": "...", "observable_by": "<date>", "current": "<latest reading with date>", "event_id": "..."} ],      // 4 to 6: what would prove YOUR side wrong
 "concedes": "<the single strongest point the other side has>",
 "log": [ ... ], "stats": {...}}
```
Bear-specific angles to test (use the record): gross-vs-net revenue and what a restatement would do; cloud-channel and supplier concentration; non-cancelable compute commitments vs price deflation; customer/coding-share concentration and competitor pricing; legal and export-control exposure; IPO absorption (pipeline vs capacity, OpenAI timing); governance (super-voting, LTBT) and key-person risk; valuation vs outside-view growth persistence.
Bull-specific angles to test: growth durability and operating leverage (run-rate path, first operating profit), unit economics and gross-margin trajectory, enterprise/coding share and switching costs, compute access as a moat, capital efficiency (equity raised per $ of run-rate; debt excluded), governance/safety as an enterprise and government advantage, optionality (new segments), what the reverse-DCF needs vs what the record shows.
Disclosure (COI): the desk's model portfolio is Anthropic 6% overweight and OpenAI 2% underweight. Bull: red-team yourself harder. Bear: do not over-correct. Neither may cite this as evidence.

## analyst-judge (runs after both)
Read both case files and the model; do not average them. Decide. Output `agents/outputs/analyst-judge.json`:
```
{"agent": "analyst-judge", "role": "Judge", "started": "<ISO>", "finished": "<ISO>",
 "verdict": {"call": "BULLISH|LEAN BULLISH|NEUTRAL|LEAN BEARISH|BEARISH", "one_liner": "<= 30 words with the price condition>", "horizon": "12-24 months after listing",
             "rationale": ["<5-7 ranked reasons, each one sentence with a number or date>"], "what_flips": ["<4-6 specific observations that would change the call>"],
             "house_view_check": ["<does this confirm, extend or contradict each standing belief: valuation-quality paradox; equalization (gross vs net); IPO absorption; CE methodology; sector conventions>"],
             "by_mark": [ {"mark": "series_h|secondary|ipo_target", "ev_usd_m": n, "call": "BULLISH|LEAN BULLISH|NEUTRAL|LEAN BEARISH|BEARISH", "why": "<one sentence tied to the reverse-DCF and the outside view>"} ]},
 "scorecard": [ {"dimension": "growth durability|gross margin|moat|capital structure|valuation|governance|legal/regulatory|IPO mechanics", "bull": 1-5, "bear": 1-5, "edge": "bull|bear|even", "note": "..."} ],
 "thesis_breakers": [ {"metric": "...", "threshold": "...", "observable_by": "<date>", "current": "...", "status": "open|intact|breached", "event_id": "..."} ],       // 6 to 8 merged, deduped, dated
 "consensus": "<where this differs from what the market is likely pricing, and what the consensus is missing>",
 "unresolved": ["<items that could change the verdict and are still [VERIFY] or [DISPUTED] in the record>"],
 "log": [ ... ], "stats": {...}}
```
Judge rules: name the reference class and base rate before the specifics; a verdict must be consistent with the model (if the model says the price requires X and X is below the outside-view base rate, the call cannot be bullish at that price without saying why this case is different);
check both cases for claims that rest on one source ("many agents, one source" is one confirmation); state the strongest argument for the side you rejected; do not use confidence percentages.
Style for all three: plain short sentences; $14.2B, 27.1x, +47% YoY; no "it's worth noting", "importantly", "leverage" (verb), "unlock", "delve", "going forward"; no em-dash asides; each prose field ≤ 80 words.
Log for the dashboard (searches, found with event_id, flags, verify, messages to: analyst-bull, analyst-bear, analyst-judge, analyst-model, analyst-compute, certifier, orchestrator). Never fabricate a flag.
Write only your output file; validate with python; final reply ≤ 8 lines.
