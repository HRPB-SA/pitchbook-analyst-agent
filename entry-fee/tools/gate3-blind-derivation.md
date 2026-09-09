# Gate 3 — Blind re-derivation of the load-bearing figures (orchestrator)

Written 2026-09-09 BEFORE any draft, brief, or model existed, from `research/evidence-ledger.md` only. At Gate 3 the report and workbooks are reconciled against THIS file; any mismatch fails the gate. Arithmetic shown. Status = the weakest load-bearing row.

## The ten figures

| # | Figure | Value | As-of | Basis | Rows | Status / tier |
|---|---|---|---|---|---|---|
| F1 | Anthropic revenue run-rate | $65.0B | end-Jul 2026 | GROSS, annualized, company-to-investors | L-032 (CNBC; TechCrunch/Bloomberg; Fortune) | confirmed T2 |
| F2 | OpenAI revenue run-rate | >$40B | Jul 2026 performance, reported Aug 13-14 | annualized; gross/net NOT stated (register convention: net of Microsoft share) | L-065 (Bloomberg via Yahoo; Hindu BusinessLine) | confirmed T2, basis open (C-16) |
| F3 | Marks | Anthropic $965B post (Series H, May 28, 2026); OpenAI $852B post (Mar 31, 2026), reaffirmed by ~$7B tender Aug 10 | May 28 / Mar 31 (Aug 10) | post-money primary | L-005, L-038 (T1), L-019, L-020, L-067 | confirmed T1/T2 |
| F4 | Equity-only capital raised | Anthropic $124.254B; OpenAI $181.2165B | May 28, 2026 / Mar 31, 2026 | sum of PB equity rounds; debt and grants excluded (Ruling 1) | L-007, L-022 | estimated T2 (derived; reproduces PB Total Raised to the dollar) |
| F5 | OpenAI 2026 compute spend | $50B | 2026E, sworn testimony May 5, 2026 | company plan | L-078 (Reuters) | confirmed T2 |
| F6 | OpenAI planned compute spend through 2030 | ~$750B (raised from ~$600B) | Jul 22, 2026 | SPEND projection 2026-2030, not contractual obligations; separate scopes: $665B (Feb 2026 vintage, L-082), $1.15T obligations through 2035 (recalled T4), $1.4T Altman headline | L-062 (WSJ via Yahoo), L-082 | estimated T2 |
| F7 | OpenAI H1-2026 P&L | Q1 rev $5.7B / op loss $9.3B; Q2 rev $6.7B / op loss $12.3B (incl. SBC); H1 rev $12.4B, H1 op loss $21.6B; FY2025 revenue $13.1B | Aug 19, 2026 (WSJ) | recognized quarterly, presumed NET | L-066, L-063 | confirmed T2 |
| F8 | Anthropic Q2-2026 print | revenue $11.5-11.6B; first quarterly operating profit (projected $559M; WSJ "small operating profit") | Aug 14-19, 2026 | recognized quarterly (preliminary), GROSS presumed; op profit is NOT FCF (Ruling 3 sweep open) | L-033, L-034 | confirmed T2 |
| F9 | Cash actually paid: Microsoft revenue from OpenAI arrangements incl. revenue share | $24.1B in FY2026 (Jul 2025-Jun 2026); A/R $6.0B at Jun 30, 2026 | FY2026 10-K filed Jul 29, 2026 | audited | L-054 | confirmed T1 |
| F10 | S-1 status | Neither Anthropic nor OpenAI has a public S-1 on EDGAR as of Sep 9, 2026; Friar (Aug 19): OpenAI "will be a public company in 2027" or sooner; PB still carries Oct 2026 (Anthropic) and Sep 2026 (OpenAI, note dated Jul 9) | Sep 9, 2026 | EDGAR full-text + company browse | L-001, L-002 (T1), L-068 (T2), L-003, L-004 (T2) | confirmed T1; C-02 frozen |

## Derived ratios the report will lean on (all est., arithmetic shown)

Equalization switch (C-13): internal Ruling 5 haircut 39.75% (net = 60.25% of gross) vs external adversarial ~27% (net = 73% of gross). Both branches:

| Derived | 39.75% branch | 27% branch | OpenAI (basis as reported) |
|---|---|---|---|
| Net run-rate | 65.0 x 0.6025 = $39.2B | 65.0 x 0.73 = $47.5B | >$40B |
| Multiple on mark | 965 / 39.2 = 24.6x | 965 / 47.5 = 20.3x | 852 / 40 = 21.3x |
| Gross multiple (Anthropic) | 965 / 65 = 14.8x | same | n/a |
| CE, equity-only (Ruling 1) | 39.2 / 124.254 = 0.315x | 47.5 / 124.254 = 0.382x | 40 / 181.2165 = 0.221x |
| CE ratio Anthropic : OpenAI | 1.43x | 1.73x | (prior register: 1.65x on $28.3B vs $25B) |
| $/AIBQ-point (May-27 scores, unrefreshed) | 965 / 8.20 = $117.7B/pt | same | 852 / 4.53 = $188.1B/pt |

Consequence to test at Gate 3: the Jul-16 finding "both names at 34.1x, identical" is DEAD on the fresh prints under either branch. On the 39.75% branch Anthropic trades at a ~15% PREMIUM multiple to OpenAI (24.6x vs 21.3x); on the 27% branch at a ~5% discount (20.3x vs 21.3x). Growth-adjusted, both multiples compressed materially versus May because revenue grew and marks did not.

Compute intensity: OpenAI 2026 compute $50B / run-rate $40B = 1.25x (was 2.0x on $25B in May). Anthropic: no company-stated 2026 compute figure (L-128, could-not-verify); any Anthropic figure in the report must be labelled derived.

Obligation-stack components (dollar-stated, maximum values, NOT to be summed without scope):
- Anthropic: AWS >$100B/10yr (T1 L-072) · Azure $30B (T1 L-074) · SpaceX $1.25B/mo to May 2029 ≈ $45B derived, 90-day termination (T1 L-046) · Fluidstack $50B (T1 L-076) · Nscale ~$45B (T2 L-135) · Lambda $35B (T2 L-137) · Riot $9.1B/20yr (T2 L-136) · Volta $10B (T3 L-048) · TPU lease SPV $34.5B debt, off-balance-sheet (T3 L-044) · project debt $15.2B (T3 L-045). Sum of the eight dollar-stated commitments = $324.1B (scope: all announced, maxima, mixed terms 6-20 years). Bloomberg's "at least $175B" (L-138) counts four of them.
- OpenAI: Oracle $300B/5yr from 2027 (T2 L-064) · AWS ~$138B (T2/T4 L-064) · CoreWeave ~$22.4B, of which $6.5B in the Q2-26 10-Q (T1 L-058) · Cerebras >$20B, 750 MW + 1.25 GW option (T1 L-149) · SB Energy PORTS 8.0 GW-IT 20-yr leases + Milam 753 MW 15-yr, rent undisclosed (T1 L-061) · Azure $250B could-not-verify (T4 L-121) · AMD 6 GW, $ undisclosed (T1 L-060) · Broadcom 1.3 GW 2027 / >5 GW 2028, $ undisclosed (T1 L-050) · Nvidia: $30B equity invested, $100B LOI retired, $105B residual-value guaranty at PORTS (T1/T2 L-061, L-075). Dollar-stated sum (Oracle + AWS + CoreWeave + Cerebras) = $480.4B; with the unverified Azure $250B = $730.4B, which is within 3% of the company's ~$750B spend-through-2030 plan (F6): consistent, not a confirmation.

Capital-structure cross-checks:
- Anthropic debt at the company: $2.5B revolver (T2 L-014); $15B expansion "nears finalizing" Sep 3 (T3 L-042), not closed. The $34.5B "chip bonds" of the Jul-16 register are SPV/lessor debt (C-01): PB Total Raised fell from $161.254B to $126.754B, exactly the $34.5B (L-006).
- OpenAI debt at the company: $4.0B revolver (Oct 2024) + $0.7B (Mar 2026) + $0.52B term loan (Jul 8, 2026) = $5.22B (T2 L-023). Total raised $186.4365B = $181.2165B equity + $5.22B debt (L-021, L-022).

## Figures from the old draft that must NOT appear without a fresh row
$47B (Anthropic run-rate, May) except as history · ~$25B OpenAI net run-rate · $161.3B Anthropic total raised · "$34.5B chip bonds tranched Superpriority / 1st Lien / 2nd Lien" as Anthropic-issued debt · 34.1x vs 34.1x · 1.65x CE advantage · $118B and $188B per AIBQ point as current (scores are May-27 vintage; marks unchanged, so the ladder is unchanged but must be dated) · $1.15T "obligations across 7 vendors" as a verified total · Nvidia "$100B / 10 GW" · "Fast Mode ~3x cheaper" · Altman "Co-CEO" · OpenAI capex $190B 2026E · $38B cap as confirmed (it is T3) · 20% revenue-share percentage (T4 only) · 27% Microsoft stake as current (decreased per 10-K).
