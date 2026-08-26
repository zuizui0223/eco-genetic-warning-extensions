# Exploratory continuous landmark audit of the frozen warning ensembles

## Status and information boundary

This is a one-time, explicitly exploratory analysis declared after the full-denominator binary-warning audit and before any continuous landmark score or AUC was calculated. The inherited and fresh symmetric warning ensembles, their seeds, deterioration domain, loss endpoint and administrative horizon remain frozen. The analysis cannot restore the withdrawn predictive-warning claim or reclassify the historical `strict_replication` protocol result.

Schema-only inspection established that every available trajectory in both immutable raw artifacts contains `H_alpha` and `H_gamma` at generations 0 through 120. No continuous score, case-control contrast or AUC was inspected before this protocol and its implementation were committed.

## Fixed population and landmarks

Analyze the two ensembles separately:

- inherited seeds `20261110–20261114` from `eco-genetic-criticality` workflow run `28500796310`;
- fresh seeds `20291110–20291114` from `eco-genetic-warning-extensions` workflow run `32636847803`.

Use all and only available baseline-eligible trajectories. The fixed landmarks are generations `30`, `60` and `90`; the common administrative horizon is generation `120`.

At landmark `t`, exclude trajectories whose functional-trait loss occurred at or before `t`. Among the remaining risk set:

- cumulative cases have loss in `(t, 120]`;
- dynamic controls remain loss-free through generation `120`.

All available baseline-eligible trajectories have complete follow-up to the common horizon, so no inverse-probability censoring weights are introduced. Non-events are right-censored for unrestricted event-time inference but are known event-free controls at generation 120.

## Fixed continuous scores

For diversity coordinate `H` in `{H_alpha, H_gamma}`, define only

\[
E_H(t)=1-\frac{H(t)}{H(0)}.
\]

Larger values mean greater baseline-relative erosion and are fixed to predict greater future-loss risk. No absolute level, slope, windowed decline, threshold optimization, endpoint selection, transformation or model fitting is opened.

The six analysis cells per ensemble are the Cartesian product of two diversity coordinates and three landmarks. They are repeated analyses of the same trajectory ensemble, not independent replicates.

## Estimand and uncertainty

For each ensemble × diversity coordinate × landmark cell, report the cumulative/dynamic concordance AUC, calculated as the Mann–Whitney probability that a randomly selected future case has greater erosion than a randomly selected dynamic control, with half credit for ties.

Report a two-sided 95% percentile interval from 10,000 stratified trajectory-level bootstrap samples. Resample cases and controls separately within each cell. The fixed base RNG seed is `20260826`; the implementation deterministically derives one seed for every fixed cell. Do not pool endpoint rows, select the best landmark, calculate a pooled p-value or add precision after seeing the result.

## Reporting and claim ceiling

Report every fixed cell for both ensembles regardless of direction or magnitude. The existing binary first-passage landmark results remain the primary evidence about the six frozen threshold rules. This continuous audit is exploratory evidence about baseline-relative diversity level at fixed common times.

Even strong AUC would not validate a general genetic early-warning signal because the domain and score were examined after the binary review. Weak AUC would constrain only these two diversity coordinates, score definition, frozen symmetric domain and saved ensembles; it would not show that genetic diversity contains no predictive information in general.
