# Warning-blind partner-redundancy Phase G

## Question

Phase F showed that the recovered R4 loss regime remained R4 across the predeclared scalar interaction-feedback range, while source eligibility changed. That result could not answer whether **how interaction support is distributed among partners** matters.

Phase G therefore asked a narrower, previously untested question:

> If intact aggregate interaction support and partner richness are matched, does concentration versus redundancy of partner contributions change the reproducibility of functional loss after the same one-partner loss?

This is an explicit reduced-form partner-contribution closure. It is not a full multi-species network model.

## Prospective design

The eco-genetic anchor was fixed before any Phase-G result was generated:

- `kappa_mu=0.35`, `p_star=0.35`;
- `A_ref=1.0`, interaction `kappa=4.5`;
- four equal patches at fixed total area;
- allele-frequency `migration_rate=0`;
- 30-generation ramp + 90-generation hold;
- normalized barrier increase `0.30`;
- five fresh master seeds × 20 replicates.

A high-function source was reconstructed once for each seed × replicate and paired across every Phase-G condition.

### Partner architectures

All loss architectures started with four partners and normalized total contribution 1.0. Exactly one partner was removed at deterioration onset.

| condition | partner weights | post-loss partner richness | mean retained support per 20-replicate block |
|---|---|---:|---:|
| intact control | 0.25, 0.25, 0.25, 0.25 | 4 | 1.00 |
| even redundant | 0.25, 0.25, 0.25, 0.25 | 3 | 0.75 |
| graded contributions | 0.40, 0.30, 0.20, 0.10 | 3 | 0.75 |
| dominant partner | 0.70, 0.10, 0.10, 0.10 | 3 | 0.75 |

Partner identity was assigned prospectively as `replicate_index mod 4`; every partner was therefore removed exactly five times in each 20-replicate seed block. The three loss architectures had **identical mean retained support and identical richness loss**. What differed was contribution concentration and the variance of retained support across matched trajectories.

## Outcomes and blinding

Only source preparation/projection, baseline realised high-trait presence, realised functional-trait loss time/status, and the predeclared partner architecture/lost-partner identity were available during classification. No diversity statistic, genetic-warning time, lead/lag ordering or lead-time value was available.

R1/R2/R3/R4 classification used the same five-seed rule as the recovered condition map. Partner-loss strata were a predeclared mechanism diagnostic, not a warning analysis.

## Opening and stop rules

1. The fresh intact control had to have sufficient high-rep support and classify as `R4_highrep`. Otherwise Phase G would record failure to reproduce the anchor without tuning seeds, weights or thresholds.
2. If the opening rule was satisfied, the three predeclared loss architectures were compared once.
3. Partner weights and lost-partner identity were not refined to manufacture an R4 switch.
4. A negative architecture result closes only this reduced-form redundancy axis; it does not prove network architecture irrelevant.

## Locked result

Workflow run `32450362310` completed successfully. Artifact `9435520830` has digest `sha256:669cfc468f8a36e53ccc157aaa97e5a4de14f6ad7c09458ed105762e4d0d6ec7`. The run used extension head `bc39c7003fb97dd10ee17034813c46f4ec85252d` and parent commit `dd8ee379d0d3518194c767d16402042525bc00dc`.

The fresh intact control reproduced R4, satisfying the opening rule.

| condition | eligible | losses | pooled loss | seed-rate range | regime |
|---|---:|---:|---:|---:|---|
| intact control | 90/100 | 49 | 0.544 | 0.129 | R4-highrep |
| even redundant | 90/100 | 51 | 0.567 | 0.261 | R3-highrep |
| graded contributions | 90/100 | 50 | 0.556 | 0.353 | R3-highrep |
| dominant partner | 90/100 | 52 | 0.578 | 0.235 | R3-highrep |

The exact five seed-block rates were:

- intact: `0.500, 0.471, 0.556, 0.600, 0.588`;
- even: `0.556, 0.471, 0.444, 0.650, 0.706`;
- graded: `0.500, 0.412, 0.556, 0.550, 0.765`;
- dominant: `0.500, 0.471, 0.667, 0.550, 0.706`.

Relative to the intact control, paired loss status switched in both directions: 38/90 trajectories for even loss (18 loss→no-loss; 20 no-loss→loss), 39/90 for graded loss (19; 20), and 31/90 for dominant loss (14; 17).

### What changed—and what did not

The predeclared classifier therefore changed from **R4 to R3 after one-partner loss in all three tested architectures**. Yet pooled loss incidence remained very similar (0.544–0.578). A post-hoc paired descriptive audit found no evidence of a difference in pooled binary loss incidence across the four conditions (Cochran's Q = 0.385, df = 3, p = 0.943; exact McNemar comparisons against intact all p >= 0.72).

The result is therefore **not** that partner loss simply raises average failure probability. In this reduced-form closure it chiefly changed **between-seed reproducibility / which stochastic histories lost function**, so an R4 warning-evaluable event regime became R3 even while pooled risk stayed near one half.

The architecture contrast itself was negative at the regime level: even, graded and dominant contribution structures were all R3. Thus Phase G does **not** support the stronger claim that contribution concentration alone determines the regime over these predeclared architectures.

This directly strengthens the manuscript's central distinction: **event frequency and event estimability are not the same object**. Interaction perturbation can change whether functional loss is reproducible enough for warning validation without producing a large directional change in average loss incidence.

## Interpretation ceiling

Phase G directly tests **matched single-partner loss under a reduced-form partner-contribution / functional-redundancy closure**. It does not directly test:

- connectance, nestedness or modularity;
- adaptive rewiring;
- partner population dynamics or coextinction;
- pollinator movement;
- pollen or seed dispersal;
- a real plant–pollinator network.

Those remain distinct empirical or future explicit-network questions. Per the prospective stop rule, Phase G is closed without tuning its partner weights or thresholds.

Machine-readable compact evidence: `artifacts/partner_redundancy/phase_g_summary.json`.
