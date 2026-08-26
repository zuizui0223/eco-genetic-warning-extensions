# Prepublication warning-validity and precision audit

## Decision

The reviewer concern is confirmed. The frozen relative-diversity rules reproduce temporal ordering **conditional on observed functional loss**, but they do not discriminate event from non-event trajectories in either saved symmetric H2-R ensemble.

The current warning claim is therefore reduced to:

> In the frozen H2-R state, each of six baseline-relative diversity crossings occurred before every observed loss in two independent seed ensembles. The same crossings also occurred in every observed non-event trajectory, so this is replicated event-conditional ordering, not a validated predictive early warning.

The historical `strict_replication` label remains an immutable preregistered protocol outcome. It is no longer used as the scientific classification of predictive validity.

## Frozen population and provenance

No threshold, seed, domain, schedule, endpoint, trajectory or outcome was changed. The audit uses only saved trajectories from:

- inherited parent run `28500796310`, artifact `8003007618`, raw member SHA-256 `c1552616a94b23ffc1340580231d7d1b16bc7d84c951c3d2606cc437fb15673e`;
- fresh Phase-V run `32636847803`, artifact `9492587604`, raw member SHA-256 `1674c817b760f5a20320ffdf775181f3c3134d60cc977feffe76c9296c253fb9`.

The population is all available baseline-eligible trajectories: 83 inherited and 82 fresh. The common administrative horizon is generation 120. Non-event trajectories remain right-censored for event-time claims and serve as known event-free controls only at that fixed horizon.

The six endpoints are repeated observations of each trajectory. They are reported separately and are never treated as six independent replicates in inference or confidence intervals.

## Full-denominator warning validity

The counts below are identical for all six locked 5%, 10% and 20% `H_alpha`/`H_gamma` endpoints within each ensemble.

| ensemble | baseline eligible | losses | non-events | warning before loss | warning in non-events | full-horizon sensitivity | specificity | PPV | NPV | binary-marker AUC |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| inherited | 83 | 35 | 48 | 35/35 | 48/48 | 1.000 | 0.000 | 0.422 | undefined | 0.500 |
| fresh | 82 | 33 | 49 | 33/33 | 49/49 | 1.000 | 0.000 | 0.402 | undefined | 0.500 |
| combined, descriptive only | 165 | 68 | 97 | 68/68 | 97/97 | 1.000 | 0.000 | 0.412 | undefined | 0.500 |

The 95% Wilson interval for the combined lead sensitivity is `[0.947, 1.000]`; for the combined non-event false-positive rate it is `[0.962, 1.000]`. PPV equals the event prevalence because every trajectory is warning-positive. NPV and full-horizon risk separation are unidentified because there are no warning-negative trajectories.

## Fixed-landmark classification

The schedule-derived ramp end (generation 30) is the primary landmark. Generations 60 and 90 are retained as fixed half- and three-quarter-horizon audits; no favourable landmark is selected.

At generation 30, inherited binary-marker AUC ranged from `0.500` to `0.538` across the six endpoints. Fresh AUC ranged from `0.500` to `0.510`. The largest combined descriptive value was `0.521` for the 20% `H_gamma` endpoint. These values do not support useful discrimination.

A continuous cumulative/dynamic AUC is not introduced. The locked endpoint family defines six binary first-passage rules, not a preregistered continuous risk score at a common prediction time. Deriving and selecting a new continuous score from the stored series would add an outcome-facing endpoint after results were known. Binary-marker cumulative/dynamic performance at the three fixed landmarks is the defensible alternative.

## Precision-bounded negative results

Paired risk differences use whole trajectories as the unit. The intervals are two-sided 95% normal intervals for the mean paired `{-1,0,+1}` difference. Every interval includes zero; none is an equivalence test.

| comparison | paired risk difference | 95% CI |
|---|---:|---:|
| Phase U `m=.10 - m=0` | +0.0111 | [-0.0330, +0.0551] |
| Phase N even loss - intact | -0.0113 | [-0.0688, +0.0462] |
| Phase N graded loss - intact | +0.0091 | [-0.0461, +0.0643] |
| Phase N dominant loss - intact | -0.0068 | [-0.0577, +0.0441] |
| Phase T even dynamic - constant | +0.0045 | [-0.0293, +0.0384] |
| Phase T dominant dynamic - constant | +0.0091 | [-0.0350, +0.0531] |
| Phase T dominant - even dynamic | +0.0045 | [-0.0256, +0.0347] |

The allowed wording is **precision-bounded null**: the fixed trials did not detect paired marginal-risk differences and constrain them only to the displayed compatible ranges. They do not establish equivalence or biological absence.

## Eschscholzia compatibility decision

The primary exact-metadata result remains `multi_endpoint_not_identifiable`; it cannot be repaired or reclassified. A separate post-review F-only sensitivity is compatible with the scientific stop rule only if it prospectively fixes the single key-specific literal mapping `Fallow graound -> Fallow ground` at array `1||3`, verifies that no other metadata mismatch exists, changes no model/endpoint/held-out unit/bootstrap seed, and cannot rescue the primary decision. The separate preregistration records those constraints before any F model is run.

## Main-story consequence

The main story is now:

1. joint state representation can be necessary even when common marginals agree;
2. empirical candidate states must pass measurement-adequacy and representation-preservation gates before residual origin/history is interpreted.

Warning and other negative phases become supporting boundaries. The warning result demonstrates why event-only validation is insufficient; the connectivity/partner trials bound tested closures without claiming equivalence.
