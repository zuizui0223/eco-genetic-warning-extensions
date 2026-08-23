# High-precision condition reassessment

## Why this reassessment was necessary

The original warning-blind programme used a preregistered five-block R1–R4 screen to locate intermediate functional-loss conditions before genetic warning was inspected. Phases J–L showed that low-replicate R3/R4 labels are strongly finite-sample sensitive. The final programme therefore preserves historical labels while separating the underlying estimands.

## Final estimands

1. **Functional-loss incidence:** pooled post-baseline realised functional-loss probability.
2. **Between-block heterogeneity:** whether high-precision blocks are compatible with a common loss probability.
3. **Trajectory-identity sensitivity:** whether a paired perturbation changes which stochastic realisations fail.
4. **Warning performance:** warning availability and lead/lag ordering after the downstream process is fixed warning-blind.

## High-precision conclusions

### Recurrent turnover

Exact Phase-C/D seed families show a high-to-low incidence frontier:

- `p_star=.325`: pooled loss `.682`;
- `.350`: `.546` and `.538` in two historical seed families;
- `.375`: `.407`;
- `.400`: `.273`.

No tested frontier condition shows detectable excess equal-rate heterogeneity. The former “narrow R4 bounded by seed-heterogeneous neighbours” interpretation is withdrawn.

### Allele-frequency connectivity: historical family and fresh replication

In the historical Phase-M seed family, pooled loss remained near `.54–.56` across `m=0–.20`. Only `m=.10` showed detectable between-block heterogeneity (`p=.0205`), while paired marginal-risk tests were null.

Phase U then preregistered one independent fresh five-seed ensemble at the same anchor and 100 attempts per block, comparing only `m=0` with `m=.10`. Every block met the precision requirement and paired baseline eligibility was identical.

- fresh `m=0`: pooled loss `.540`, equal-rate `p=.134`;
- fresh `m=.10`: pooled loss `.551`, equal-rate `p=.745`;
- paired McNemar `p=.694`.

The preregistered decision is **`historical_m010_heterogeneity_not_freshly_replicated`**. The historical `m=.10` result remains valid in its original seed family but is not supported as an independently reproducible parameter-specific heterogeneity effect.

### Process-resolved movement

Using the historical Phase-M seed family, whole-individual dispersal `d=.10` and pollen-only paternal gene flow `g=.20` both remained block-homogeneous and had null paired marginal-risk contrasts. Combined with Phase U, no robust portable connectivity heterogeneity effect is established across the tested ensembles and movement closures.

### Aggregate interaction feedback

`kappa=3.0,4.5,6.0` all retain intermediate high-precision loss incidence and show no detected excess block heterogeneity. This is a bounded robustness result for scalar aggregate interaction feedback.

### Partner architecture

Intact, even, graded and dominant partner-loss architectures have similar high-precision pooled loss and no detected excess block heterogeneity. Phase T additionally increased temporal support variance and contribution concentration at matched expected support without detecting an incidence, block-heterogeneity or paired marginal-risk effect. The adaptive-rewiring gate remains closed.

## Consequence for genetic warning

The condition-first programme remains valid but its gate is stated more precisely. Intermediate event incidence is useful for calibration; it is not the same as biological exchangeability. A high-precision stochastic signal in one finite seed family is also not automatically a portable mechanism: when a claim becomes load-bearing, independent prospective replication should be used where feasible.

Genetic warning should be evaluated only after the downstream functional-loss process is characterised independently, with incidence, block heterogeneity, censoring, paired trajectory structure and replication status kept separate.

Historical artifacts remain immutable. This document changes their permitted interpretation, not their recorded outcomes.
