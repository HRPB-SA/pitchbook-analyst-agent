# Pilot Protocol

| Field | Value |
| --- | --- |
| Thesis | Agentic Commerce Infrastructure |
| Sub-segment | Agent networking / identity overlay |
| Stage | Seed |
| Status | Passed |
| Decision | Pass |
| Durability score | 3/10 |
| Website | https://pilotprotocol.network/ |
| Notion record | https://app.notion.com/3ae77aecd4eb815f8dd9f4bbf181be1d |

## What they do

A UDP overlay giving AI agents addresses, peer discovery, Ed25519 identity and x402/USDC settlement, positioned as 'the internet for agents'.

## Deal profile

- Series round: Seed
- Round size: $4.5M
- Raise status: Closed
- Lead investor: Version One Ventures (Precursor, Night Capital, Todd & Rahul Capital, angels Lenny Rachitsky and Ben Tossell)
- Deal date: 2026-07-24

## Pipeline position

- Status: Passed
- Decision: Pass
- Durability score: 3/10
- 90-day target: no
- Sourced via: Sourcing agent

### Decision reasoning

PASS 2026-07-28 ON METRIC INTEGRITY - a REFUTATION, not a failure to corroborate, and the strongest evidence chain in the batch. The company's headline is '250,000 agents generating two billion requests per day'. Its own CTO wrote on Hacker News that they are 'exchanging ~2B PACKETS/day'. Pilot's own IETF Internet-Draft specifies empty-ACK keepalives every 30 seconds on idle connections, and the arithmetic lands at 2.78 idle sockets per agent - so the two-billion figure is dominated by protocol overhead, not application traffic. Combined npm and PyPI SDK downloads are ~3,210 per month against 250,000 claimed agents, a 78x gap. The same CTO disclosed clusters of 10-250 agents per IP and said operators they contacted 'didn't even know we exist' - so the agent count is not an operator count and the installs are largely unwitting. The validator independently re-verified every element through the HN, IETF, npm and PyPI APIs: quotes accurate and in context, arithmetic exact, download figures confirmed to the digit. The team is genuinely better than the metrics - Razvan Roman's Two Tap (YC W14) exit to Honey/PayPal is real, and the IETF draft is real protocol engineering - but a strong team telling a story their own data does not support is a GOVERNANCE SIGNAL, not a rounding error. Notably, no token exists, a genuine positive that removes the usual disqualifier in this lane.

## People

- Founder (company record): Razvan Roman (Co-Founder & CEO; prior company Two Tap, YC W14, exited to Honey/PayPal). Co-founders: Artemii Amelin, Teodor Ioan C., Alexandru Godoroja, Philip Stayetski.
- Razvan Roman — Co-Founder & CEO
  - Prior company Two Tap (YC W14), exited to Honey/PayPal. No email on record.
- Artemii Amelin — Co-Founder
- Teodor Ioan C. — Co-Founder
  - Surname is abbreviated in every source found; full name unverified. No email on record.
- Alexandru Godoroja — Co-Founder
- Philip Stayetski — Co-Founder

## Open questions

Secondary risk: a network that propagates by installing itself without owner knowledge is an enterprise-security advisory waiting to happen. No outreach; the single event trigger that would reopen this is a published x402 settlement volume. NEW METRIC FROM LAUNCH COVERAGE, and it cuts BOTH ways: the company claims 'more than 30,000 autonomous installs of partner applications' in the two weeks since the Pilot App Store launched. That is a far more defensible number than the 2-billion-requests headline the Pass was built on - it is an action count, not protocol overhead - but it is still company-reported with no independent instrumentation, and 30K installs against 250K claimed agents is its own ratio worth asking about. Does not overturn the metric-integrity Pass; does mean the re-check trigger should be widened from x402 settlement volume alone to include verifiable App Store install data.

## Validation

FLAGGED (mild)

## Tracking

- Last brief: 2026-07-28
- Notion row created: 2026-07-31T19:24:13Z

---
*Mirrored from the Layer H Notion Companies database on 2026-08-11. Edit in Notion; this file is a snapshot.*
