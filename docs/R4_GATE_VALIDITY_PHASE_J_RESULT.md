# Phase J result — R3 does not by itself identify biological seed heterogeneity

## Decision

**The historical R4 all-block classifier is strongly finite-sample sensitive at the block sizes used by Phases H and I.** Historical R1–R4 labels remain unchanged, but `R3_highrep` must no longer be translated automatically as biological `seed-heterogeneous` evidence.

## Provenance

- workflow run `32556672652`
- artifact `9471623282`
- digest `sha256:f4c1ba1ac8f06d185a86a5d6d9bfe008b00af9204eb2df925fbfc1e712f61acb`
- preregistered head `d4e2c07afbf29371e4fde846313fab5a50da3380`
- committed compact evidence `artifacts/r4_gate_validity/phase_j_locked_summary.json`

## Phase H

Partner loss/no rewiring had blocks:

`9/18, 8/17, 9/17, 6/17, 5/17`

Pooled loss = `37/86 = 0.4302`; historical label = `R3_highrep` because `5/17 = 0.2941` is just below the R4 lower bound 0.30.

Under a homogeneous Bernoulli reference with the same pooled probability and exact observed block sizes:

- probability all five empirical rates pass the historical R4 gate = **0.3320**;
- probability the gate fails = **0.6680**.

The observed five blocks do not show detectable excess equal-rate heterogeneity by the secondary Pearson diagnostic: `X²=2.852`, `df=4`, `p=0.583`.

Thus the historical R3 outcome is entirely plausible from finite within-block sampling under a homogeneous reference. It cannot by itself identify a biological seed-heterogeneity mechanism.

## Phase I

Partner loss/no rescue had blocks:

`7/17, 8/18, 11/19, 9/18, 9/18`

Pooled loss = `44/90 = 0.4889`; historical label = `R4_highrep`.

Under the same homogeneous reference construction:

- probability the historical five-block gate passes = **0.5873**;
- probability it fails = **0.4127**.

The equal-rate diagnostic is again non-significant: `X²=1.181`, `df=4`, `p=0.881`.

The Phase-H R3 / Phase-I R4 flip is therefore not surprising at these finite block sizes.

## Gate calibration

For five equal blocks with latent homogeneous loss probability 0.5:

| eligible per block | R4 gate pass | gate failure |
|---:|---:|---:|
| 17 | 0.461 | 0.539 |
| 18 | 0.603 | 0.397 |
| 20 | 0.809 | 0.191 |
| 50 | 0.987 | 0.013 |
| 100 | 0.99984 | 0.00016 |

The historical all-five-block gate therefore becomes far more stable when within-block precision is increased.

## Scientific correction

The following distinction is now mandatory:

- **Historical fact:** a candidate did or did not pass the strict five-block R4 screen.
- **Not identified by that fact alone:** whether latent biological loss probabilities truly differed among seed blocks.

Accordingly, wording such as `R3 seed-heterogeneous` should be treated as an internal historical regime label, not a demonstrated biological mechanism. The claim that reproducibility across stochastic blocks is an additional biological condition requires a higher-precision validation or a separately justified heterogeneity estimand.

## Next prospective validation

Increase within-block precision **without selecting replacement seeds**. Use all ten master seeds that generated the Phase-H and Phase-I disagreement, expand each from 20 attempted replicates to 100, and pair intact versus partner-loss/no-rescue outcomes under the same biological closure.

The first 20 replicate prefix must reproduce the locked Phase-H / Phase-I counts. Failure of this prefix audit is an implementation failure. The full 100-replicate blocks then determine whether the R3/R4 discrepancy persists after within-block sampling error is strongly reduced.

## Stop rule

Do not alter the historical `[0.30,0.70]` band to make the two campaigns agree. Do not select new replacement master seeds. Any revised future warning-evaluability estimand must be prospectively declared only after this precision validation.
