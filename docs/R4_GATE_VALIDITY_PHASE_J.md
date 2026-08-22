# Phase J — finite-sample validity audit of the R4 all-block gate

## Why this audit is necessary

Phase H and Phase I used the same declared partner-loss/no-rescue biological condition but independent fresh seed ensembles. Phase H classified it R3 because one block was `5/17 = 0.294`, just below the historical R4 lower bound 0.30. Phase I classified the condition R4 because all five fresh block rates fell inside `[0.30,0.70]`.

Before adding more biological mechanisms or searching additional seed ensembles, Phase J asks whether this label instability can arise from the finite-sample behaviour of the **classifier itself**.

## Historical rule remains fixed

R4 is historically defined as:

> all five observed seed-block functional-loss rates lie in `[0.30,0.70]`.

Phase J does not alter this rule and does not retroactively relabel any campaign. It audits what the rule can and cannot identify statistically.

## Reference-null calculation

For a block with `n` eligible trajectories and a common latent loss probability `p`, the exact probability that the observed empirical rate falls inside the historical band is calculated from the binomial distribution. For a five-block ensemble, the sampling-only gate-pass probability is the product of the five block probabilities.

This homogeneous-binomial model is a **diagnostic reference null**, not a claim that simulator trajectories are literally iid Bernoulli. It asks a narrower question:

> Can an R3 gate failure plausibly occur even if the five blocks do not have different latent loss probabilities?

The calibration grid is fixed at latent `p = 0.30, 0.35, ..., 0.70` and equal eligible block sizes `n = 17, 18, 19, 20, 50, 100`.

## Observed Phase-H / Phase-I audit

The locked partner-loss blocks are:

- Phase H: `9/18, 8/17, 9/17, 6/17, 5/17` → historical R3;
- Phase I: `7/17, 8/18, 11/19, 9/18, 9/18` → historical R4.

For each set Phase J reports:

1. pooled loss probability;
2. exact homogeneous-reference probability that the five-block R4 gate passes/fails at that pooled probability and those exact block sizes;
3. a Pearson equal-proportion test across the five blocks as a diagnostic for excess between-block heterogeneity.

The equal-proportion test is secondary and does not prove homogeneity when non-significant. Its role is to prevent the historical term `seed-heterogeneous` from being treated as statistically identified merely because one empirical block crosses the hard band.

## Interpretation rule

If a historical R3 failure has substantial probability under the homogeneous finite-sample reference, and the observed five blocks do not show detectable excess heterogeneity, then:

- the historical R3 label remains a protocol fact;
- **R3 must not be interpreted by itself as evidence of biological seed heterogeneity**;
- the R4 all-block rule should be described as an operational finite-sample screen;
- claims that block-gate failure establishes a biological reproducibility boundary must be weakened or independently validated with greater within-block precision / a separately justified heterogeneity estimand.

## Consequence for subsequent experiments

Do not replace Phase-I seeds to manufacture the missing R3 opening. If Phase J shows substantial finite-sample gate instability, the next simulation should be a **precision validation of the event-regime estimand**, not another mechanism sweep. Historical R1–R4 results remain recorded exactly as generated.

## Stop rule

Do not alter the `[0.30,0.70]` historical band after this audit in order to make previous classifications agree. Any revised future estimand must be declared prospectively and validated separately from the historical R4 labels.
