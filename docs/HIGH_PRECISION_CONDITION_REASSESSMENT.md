# High-precision condition reassessment

## Why this reassessment was necessary

The original warning-blind programme used a preregistered five-block R1–R4 screen to locate intermediate functional-loss conditions before genetic warning was inspected. The screen was scientifically useful, but Phases J–L showed that its low-replicate R3/R4 labels are strongly finite-sample sensitive.

At historical block sizes near 15–20 eligible trajectories, a common latent loss probability can generate apparent mixed-block R3 calls by sampling variation alone. Conversely, a condition whose true incidence lies near 0.30 or 0.70 can fail the all-five-block screen even without biological heterogeneity. The final programme therefore preserves historical labels while separating the underlying estimands.

## Final estimands

1. **Functional-loss incidence:** pooled post-baseline realised functional-loss probability.
2. **Between-block heterogeneity:** whether high-precision blocks are compatible with a common loss probability.
3. **Trajectory-identity sensitivity:** whether a paired perturbation changes which stochastic realisations fail.
4. **Warning performance:** warning availability and lead/lag ordering after the downstream process is fixed warning-blind.

## High-precision conclusions

### Recurrent turnover

Exact Phase-C/D seed families show a high-to-low incidence frontier:

- `p_star=.325`: pooled loss `.682`;
- `.350`: `.546` and `.538` in two independent historical seed families;
- `.375`: `.407`;
- `.400`: `.273`.

No tested frontier condition shows detectable excess equal-rate heterogeneity. The former “narrow R4 bounded by seed-heterogeneous neighbours” interpretation is withdrawn.

### Allele-frequency connectivity

Pooled loss remains near `.54–.56` across `m=0–.20`. Only `m=.10` shows detectable high-precision between-block heterogeneity (`p=.0205`). `m=.20` does not. Paired McNemar tests against isolation are non-significant at all tested nonzero levels.

The supported result is therefore non-monotone block dependence at one tested allele-frequency mixing level, not a monotone rescue/collapse or marginal-risk gradient.

### Aggregate interaction feedback

`kappa=3.0,4.5,6.0` all retain intermediate high-precision loss incidence and show no detected excess block heterogeneity. This is a bounded robustness result for scalar aggregate interaction feedback.

### Reduced-form partner loss

Intact, even, graded and dominant-partner-loss architectures have similar high-precision pooled loss and no detected excess block heterogeneity. Exact paired marginal-risk tests are null, although many individual trajectory outcomes switch in both directions.

The historical low-replicate R4→R3 partner-loss interpretation is withdrawn.

## Consequence for genetic warning

The condition-first programme remains valid but its gate is now stated more precisely. Intermediate event incidence is useful for calibration; it is not the same as biological exchangeability. Genetic warning should be evaluated only after the downstream functional-loss process is characterised independently, with incidence, block heterogeneity, censoring and paired trajectory structure kept separate.

Historical artifacts remain immutable. This document changes their permitted interpretation, not their recorded outcomes.
