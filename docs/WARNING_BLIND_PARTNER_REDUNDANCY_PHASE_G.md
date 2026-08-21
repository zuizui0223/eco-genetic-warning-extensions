# Warning-blind partner-redundancy Phase G

## Question

Phase F showed that the recovered R4 loss regime remained R4 across the predeclared scalar interaction-feedback range, while source eligibility changed. That result cannot answer whether **how interaction support is distributed among partners** matters.

Phase G therefore asks a narrower, previously untested question:

> If intact aggregate interaction support and partner richness are matched, does concentration versus redundancy of partner contributions change the reproducibility of functional loss after the same one-partner loss?

This is an explicit reduced-form partner-contribution closure. It is not a full multi-species network model.

## Prospective design

The eco-genetic anchor is fixed before any Phase-G result is generated:

- `kappa_mu=0.35`, `p_star=0.35`;
- `A_ref=1.0`, interaction `kappa=4.5`;
- four equal patches at fixed total area;
- allele-frequency `migration_rate=0`;
- 30-generation ramp + 90-generation hold;
- normalized barrier increase `0.30`;
- five fresh master seeds × 20 replicates.

A high-function source is reconstructed once for each seed × replicate and paired across every Phase-G condition.

### Partner architectures

All loss architectures start with four partners and normalized total contribution 1.0. Exactly one partner is removed at deterioration onset.

| condition | partner weights | post-loss partner richness | mean retained support per 20-replicate block |
|---|---|---:|---:|
| intact control | 0.25, 0.25, 0.25, 0.25 | 4 | 1.00 |
| even redundant | 0.25, 0.25, 0.25, 0.25 | 3 | 0.75 |
| graded contributions | 0.40, 0.30, 0.20, 0.10 | 3 | 0.75 |
| dominant partner | 0.70, 0.10, 0.10, 0.10 | 3 | 0.75 |

Partner identity is assigned prospectively as `replicate_index mod 4`; every partner is therefore removed exactly five times in each 20-replicate seed block. The three loss architectures have **identical mean retained support and identical richness loss**. What differs is contribution concentration and the variance of retained support across matched trajectories.

This separates a functional-redundancy hypothesis from a simple aggregate-support dose response.

## Outcomes and blinding

Only the following are available during classification:

- source preparation/projection;
- baseline realised high-trait presence;
- realised functional-trait loss time/status;
- predeclared partner architecture and lost-partner identity.

No diversity statistic, genetic-warning time, lead/lag ordering or lead-time value is available.

R1/R2/R3/R4 classification uses the same five-seed rule as the recovered condition map. Partner-loss strata are a predeclared mechanism diagnostic, not a warning analysis.

## Opening and stop rules

1. The fresh intact control must have sufficient high-rep support and classify as `R4_highrep`. If it does not, Phase G records failure to reproduce the anchor and **does not tune seeds, weights or thresholds**.
2. If the opening rule is satisfied, compare the three predeclared loss architectures once.
3. Do not refine partner weights or choose a different lost partner to manufacture an R4 switch.
4. A negative result closes only this reduced-form redundancy axis; it does not prove network architecture irrelevant.

## Interpretation ceiling

Phase G directly tests **partner-contribution concentration / functional redundancy under matched single-partner loss**. It does not directly test:

- connectance, nestedness or modularity;
- adaptive rewiring;
- partner population dynamics or coextinction;
- pollinator movement;
- pollen or seed dispersal;
- a real plant–pollinator network.

Those remain distinct empirical or future explicit-network questions.
