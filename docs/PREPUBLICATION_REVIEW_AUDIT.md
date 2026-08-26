# Prepublication warning-validity and precision audit

## Decision

The reviewer concern is confirmed. The frozen relative-diversity rules reproduce temporal ordering **conditional on observed functional loss**, but their fixed generation-30 binary markers do not discriminate events usefully in either saved symmetric H2-R ensemble. By the common horizon every marker is positive, so full-horizon AUC 0.5 is a degenerate consequence rather than the main evidence.

The current warning claim is therefore reduced to:

> In the frozen H2-R state, each of six baseline-relative diversity crossings occurred before every observed loss in two independent seed ensembles. The same crossings also occurred in every observed non-event trajectory, so this is replicated event-conditional ordering, not a validated predictive early warning.

The historical `strict_replication` label remains an immutable preregistered protocol outcome. It is no longer used as the scientific classification of predictive validity.

## Frozen population and provenance

No threshold, seed, domain, schedule, endpoint, trajectory or outcome was changed. The audit uses only saved trajectories from:

- inherited parent run `28500796310`, artifact `8003007618`, raw member SHA-256 `c1552616a94b23ffc1340580231d7d1b16bc7d84c951c3d2606cc437fb15673e`;
- fresh Phase-V run `32636847803`, artifact `9492587604`, raw member SHA-256 `1674c817b760f5a20320ffdf775181f3c3134d60cc977feffe76c9296c253fb9`.

The population is all available baseline-eligible trajectories: 83 inherited and 82 fresh. The common administrative horizon is generation 120. Non-event trajectories remain right-censored for event-time claims and serve as known event-free controls only at that fixed horizon.

The six endpoints are repeated observations of each trajectory. They are reported separately and are never treated as six independent replicates in inference or confidence intervals.

## Fixed-landmark classification

The schedule-derived ramp end (generation 30) is the primary binary landmark. Generations 60 and 90 are retained as fixed half- and three-quarter-horizon audits; no favourable landmark is selected.

At generation 30, inherited binary-marker AUC ranged from `0.500` to `0.538` across the six endpoints. Fresh AUC ranged from `0.500` to `0.510`. The largest combined descriptive value was `0.521` for the 20% `H_gamma` endpoint. These non-degenerate fixed-time values do not support useful discrimination.

## Full-horizon degeneration

The counts below are identical for all six locked 5%, 10% and 20% `H_alpha`/`H_gamma` endpoints within each ensemble.

| ensemble | baseline eligible | losses | non-events | warning before loss | warning in non-events | full-horizon sensitivity | specificity | PPV | NPV | binary-marker AUC |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| inherited | 83 | 35 | 48 | 35/35 | 48/48 | 1.000 | 0.000 | 0.422 | undefined | 0.500 |
| fresh | 82 | 33 | 49 | 33/33 | 49/49 | 1.000 | 0.000 | 0.402 | undefined | 0.500 |
| combined, descriptive only | 165 | 68 | 97 | 68/68 | 97/97 | 1.000 | 0.000 | 0.412 | undefined | 0.500 |

The 95% Wilson interval for the combined lead sensitivity is `[0.947, 1.000]`; for the combined non-event false-positive rate it is `[0.962, 1.000]`. PPV equals the event prevalence because every trajectory is warning-positive. NPV and full-horizon risk separation are unidentified because there are no warning-negative trajectories.

The full-horizon table is retained because it documents false-positive burden and event-only denominator selection. Its `1/1/0/0.5` pattern mainly restates that every frozen binary rule became a constant positive by generation 120.

## Separately preregistered exploratory continuous audit

After the binary review, commit `bf9f492996cfb57718e03edd4a3620c0756b32c4` prospectively fixed `1 - H(t)/H(0)` for both diversity coordinates at all three landmarks. No slope, transformation, selected landmark or endpoint pooling was allowed. Cumulative/dynamic AUC used cases in `(t,120]`, controls event-free through 120, and 10,000 stratified trajectory-level bootstrap samples.

At generation 30, continuous AUC remained near chance: `0.535/0.533` inherited and `0.522/0.556` fresh for `H_alpha/H_gamma`. Across all landmarks, inherited AUC ranged `0.418–0.692` and fresh AUC `0.422–0.687`. Inherited generation-90 `H_alpha` was `0.692 [0.523,0.840]`; fresh generation-60 `H_gamma` was `0.687 [0.504,0.848]`. These were different coordinate/time cells and neither reproduced in the other ensemble. Fresh generation 90 had only three future cases and wide intervals.

The exploratory result does not support a portable continuous warning score. It also prevents the overbroad claim that `H_alpha/H_gamma` contain no information: time-specific separation is possible, but was not stable across the fixed ensembles and landmarks.

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

## Eschscholzia compatibility decision and STOP

The primary exact-metadata result remains `multi_endpoint_not_identifiable`; it cannot be repaired or reclassified. A post-review F-only sensitivity was prospectively restricted to the single key-specific mapping `Fallow graound -> Fallow ground` at array `1||3`, with no model/endpoint/held-out unit/bootstrap change and no authority to rescue the primary decision. Pre-model metadata inspection then found the same mismatch at `1||4`. The one-key sensitivity remains stopped.

A third, separately labelled post-lock descriptive reconstruction was then fixed at commit `bf9f492996cfb57718e03edd4a3620c0756b32c4`. It corrected exactly `1||3` and `1||4` (three rows each) and verified zero remaining Habitat mismatches. The unchanged `_prepare_f` gate stopped because the F primary response contained a missing, non-finite or negative value. No response repair, row exclusion, model, score or bootstrap followed. Decision: `postlock_descriptive_reconstruction_not_estimable`; no F estimate exists.

## Main-story consequence

The main story is now:

1. joint state representation can be necessary even when common marginals agree;
2. empirical candidate states must pass measurement-adequacy and representation-preservation gates before residual origin/history is interpreted.

Warning and other negative phases become supporting boundaries. The warning result demonstrates why event-only validation is insufficient; the connectivity/partner trials bound tested closures without claiming equivalence.
