# Phase L — cross-campaign validity audit of load-bearing R3 claims

## Trigger

Phase J showed that the historical all-five-block R4 gate is strongly finite-sample sensitive at the 17–20 eligible trajectories used in many high-rep campaigns. Phase K then precision-expanded the exact Phase-H / Phase-I conflicting seed families and showed both converge to R4, confirming that the Phase-H R3 label was a finite-sample gate failure rather than demonstrated biological seed heterogeneity.

Phase L therefore audits every historical **R3 classification that currently carries manuscript-level mechanistic weight** before any further mechanism sweep is accepted.

## Cases

The audit includes:

- Phase C: `p_star=0.40`;
- Phase D: immediate neighbours `p_star=0.325` and `0.375`;
- Phase E: allele-frequency mixing `m=0.10` and `0.20`;
- Phase G: even, graded and dominant one-partner-loss architectures;
- Phase H: partner loss/no rewiring and the fixed rewiring condition.

Historical R4 controls from Phases C/D/E/G are retained as calibration context.

## Audit

For every fixed five-block historical case, report:

1. pooled loss rate;
2. exact homogeneous-binomial reference probability that the historical all-five-block R4 gate passes/fails at the observed block sizes and pooled rate;
3. Pearson equal-rate diagnostic across the five blocks.

The homogeneous-binomial model is a sampling reference, not a simulator model. The equal-rate test is a secondary diagnostic and a non-significant value does not prove equality. Together they answer whether the old R3 gate failure **by itself** identifies biological block heterogeneity.

## Interpretation

A historical R3 label remains an immutable protocol fact. However, when:

- gate failure is common under a homogeneous finite-sample reference, and
- observed block rates do not show detectable excess equal-rate heterogeneity,

then R3 cannot be used alone as evidence that the biological event process changed reproducibility across seed blocks.

This distinction matters because several manuscript claims currently infer mechanisms from R4→R3 or neighbour-R3 transitions.

## Required consequences

- **Phase C/D:** do not call the recovered R4 region biologically narrow solely because neighbouring 17–20-trajectory blocks were labelled R3. Precision-validate the frontier.
- **Phase E:** do not claim allele-frequency connectivity changes loss-regime reproducibility solely from `m=0.10/0.20` R3 labels. Precision-validate the migration levels.
- **Phase G:** do not claim partner loss changes event-regime reproducibility solely from the three R3 labels. Precision-validate the partner architectures.
- **Phase H:** the no-rewiring R3 label is already refuted mechanistically by Phase K high precision. The rewiring R3 label likewise cannot establish non-rescue by gate class alone.

## Stop rule

Do not alter historical R3/R4 labels or the `[0.30,0.70]` band. Do not retain a mechanistic claim merely because a low-precision block crossed the hard gate. Where the claim is load-bearing, validate the biological contrast at greater within-block precision using fixed historical conditions/seeds where feasible.
