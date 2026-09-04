# Cross-layer alignment propagation audit — prospective preregistration

**Status:** post-review prospective extension of the closed Phase-V alignment campaign. This document is locked before any project inspection of intermediate-generation Phase-V snapshot outcomes and before any propagation rerun is executed.

## 1. Why this audit is opened

The existing Phase-V result contains two already-known endpoints at very different forecast scales:

- the exact generation-1 transition certificate shows that the aligned and anti-aligned states, despite matching the declared coarse marginals, can differ in their next interaction transition;
- the fixed 60-generation 500-pair campaign did not establish a directional difference in cumulative realised functional-loss incidence.

The missing object is the propagation path between those endpoints. This audit asks whether information carried by the initial cross-layer alignment remains visible, attenuates, rebounds, or becomes endpoint-specific as forecast horizon increases.

This audit is **not** opened to rescue the genetic-warning result and does not test why the six frozen diversity thresholds failed discrimination. The warning-validity result and the alignment result remain logically distinct.

## 2. Known information before this lock

The following Phase-V facts were already known before this extension and therefore are not treated as newly predicted outcomes:

1. the aligned and anti-aligned baseline states match in patch area, census, interaction, allele-frequency and realised high-trait-mass multisets, trait-bin totals, `H_alpha`, `H_gamma`, and `F_ST` under the declared tolerance;
2. their cross-layer covariance has opposite sign;
3. the exact generation-1 interaction transition differs patchwise, with the historical certificate reporting a maximum difference of about `0.2543`;
4. under the fixed 60-generation campaign, cumulative realised trait loss was `339/500 = 0.678` for aligned and `361/500 = 0.722` for anti-aligned, with `92` aligned-loss/anti-no-loss and `114` aligned-no-loss/anti-loss pairs and exact McNemar `p≈0.143`.

At the time this document is committed, intermediate-generation Phase-V snapshot values have not been opened for this propagation question.

## 3. Immutable computational sources

The propagation audit must reproduce the original closed Phase-V dynamics, not silently define a new biological model.

- EGWE historical Phase-V scientific implementation: commit `260a03220bf09d5f4a4d8cb55ec21062bf120c55`.
- Upstream EGC scientific closure: commit `dd8ee379d0d3518194c767d16402042525bc00dc`.
- Original conditions: exactly `aligned` and `anti_aligned`.
- Master seeds: exactly `20300110, 20300111, 20300112, 20300113, 20300114`.
- Replicates per seed: exactly `100`.
- Comparable pairs: exactly `500`.
- Horizon: exactly `60` generations.
- Barrier schedule: exactly the original linear `0.50 -> 0.65` schedule over 60 generations.
- No migration and zero symmetric allele mutation, as in Phase V.

The same deterministic trajectory-seed mapping from the historical runner is retained. These are **replayed original pairs**, not an independent replication and not new statistical replication.

## 4. Integrity gate before intermediate outcomes may be interpreted

The rerun must first satisfy all of the following:

1. baseline marginal signatures reproduce the closed Phase-V equality checks;
2. the exact generation-1 mechanistic certificate reproduces the locked certificate to numerical tolerance `1e-12`;
3. the generation-60 loss counts and paired 2x2 table reproduce the locked Phase-V summary exactly;
4. all 500 declared pair keys are present once in each condition;
5. no warning threshold, warning time, or warning-derived selection field enters the audit.

If any integrity condition fails, the propagation audit is `reproduction_gate_failed` and stops before scientific interpretation of the intermediate horizons.

## 5. Fixed forecast horizons

The complete preregistered horizon grid is:

`h = {1, 2, 5, 10, 20, 40, 60}` generations post-baseline.

All horizons are reported. No horizon is removed, inserted, or promoted because its result is favourable.

The existing exact deterministic generation-1 certificate remains the mechanistic opening result. The stochastic snapshot at `h=1` is additionally retained as the first point of the paired propagation trajectory; it does not replace the exact certificate.

## 6. Fixed state-propagation measurements

For pair `r` at horizon `h`, corresponding patches retain their declared patch identities. No sorting or rematching of patches is allowed after baseline.

### 6.1 Primary propagation coordinate — interaction state

For the four patchwise interaction values `q_i`:

- `D_I_max(r,h) = max_i |q_i(aligned) - q_i(anti_aligned)|`;
- `D_I_mean(r,h) = mean_i |q_i(aligned) - q_i(anti_aligned)|`.

`D_I_max` is primary because it is directly homologous to the existing maximum-patchwise generation-1 transition certificate. `D_I_mean` is a required secondary summary and cannot replace the primary after outcomes are seen.

### 6.2 Required secondary state coordinates

Using the same pair and patch identities, report the mean absolute patchwise difference at every horizon for:

- census population `N`;
- local effective size `N_e`;
- high-allele frequency `p`;
- realised high-trait mass from `trait_occupancy.high_trait_mass`.

Also report the absolute paired difference in the snapshot-level summaries:

- `H_alpha`;
- `H_gamma`;
- `F_ST` when finite in both conditions.

These diversity quantities are state-description coordinates only. **No percentage decline, threshold crossing, warning time, ROC optimisation, or warning classification is permitted in this audit.**

No composite multivariate distance is constructed because its scaling would introduce a new outcome-facing weighting choice.

## 7. Model-free retention scale

The audit does not assume exponential decay.

Let `M_I(h)` be the median across the 500 pairs of `D_I_max(r,h)`.

Define the preregistered **half-retention horizon** as the earliest horizon in `{2,5,10,20,40,60}` for which:

`M_I(h) <= 0.5 * M_I(1)`

and `M_I` remains at or below that half-baseline level at every later preregistered horizon.

- If such a horizon exists, report it as an interval-censored retention scale on the fixed grid; do not interpolate between horizons.
- If the curve crosses below one-half and later rises above it, classify the interaction propagation as `nonmonotone_half_retention_not_defined`.
- If the curve never remains below one-half by generation 60, report `half_retention_not_reached_by_60`.
- If `M_I(1) <= 1e-15`, the retention ratio is `not_identifiable`; do not replace the denominator.

An exponential decay rate or half-life is **not** part of the primary or secondary analysis. Any later parametric decay fit requires a separate prospective declaration.

## 8. Functional endpoint propagation

At each horizon `h`, define cumulative realised functional loss using the existing Phase-V trait-loss time only:

`L(h) = 1` iff the locked realised high-trait loss time is non-null and `<= h`; otherwise `0`.

For every horizon report:

- aligned cumulative loss count/rate;
- anti-aligned cumulative loss count/rate;
- paired risk difference `RD(h) = mean[L_aligned(h) - L_anti(h)]`;
- paired 2x2 counts (`both no loss`, `aligned only`, `anti only`, `both loss`);
- discordance fraction;
- two-sided exact McNemar p-value as a descriptive paired diagnostic.

No single horizon is declared positive merely because its unadjusted McNemar p-value is below `.05`.

### Simultaneous uncertainty for the horizon family

Use exactly 10,000 pair-cluster bootstrap draws with RNG seed `20260904`. Each draw samples the 500 pair IDs with replacement and retains both conditions for every sampled pair.

For the seven-horizon risk-difference curve, construct a non-studentized simultaneous 95% band from the 95th percentile of

`max_h |RD_boot(h) - RD_observed(h)|`.

A horizon-family loss-incidence separation is called `detected` only if this simultaneous band excludes zero at at least one preregistered horizon. Otherwise report `no_detected_horizon_family_loss_incidence_separation`.

This family-level rule prevents selecting a favourable intermediate horizon after the result.

## 9. Trajectory-identity propagation

The paired 2x2 table is treated as a scientific object, not only as a significance test. At each horizon report:

- fraction of the 500 pairs with identical cumulative-loss status;
- fraction with discordant cumulative-loss status;
- direction of discordance (`aligned only` versus `anti only`).

The audit may therefore distinguish convergence of marginal incidence from persistence of trajectory identity differences.

No pair is removed because its two conditions converge or diverge unusually.

## 10. Descriptive uncertainty for continuous state curves

For each continuous state-distance coordinate, report the observed median across pairs at every fixed horizon and a 95% pair-bootstrap percentile interval using the same 10,000 pair resamples and seed `20260904`.

These intervals describe the fixed horizon curve. They are not used to search for the first individually significant horizon and are not a multiplicity-adjusted hypothesis family.

## 11. Prespecified interpretation classes

The interaction-state curve is classified without fitting a parametric decay model:

- `short_representation_memory`: half-retention is reached and remains below one-half by `h<=5`;
- `attenuating_representation_memory`: half-retention is first reached at `h=10`, `20`, or `40` and remains below thereafter;
- `persistent_representation_memory`: half-retention is not reached by `h=60`;
- `nonmonotone_representation_memory`: the curve crosses below one-half and later rises above it;
- `representation_memory_not_identifiable`: the `h=1` median denominator is effectively zero or the reproduction gate fails.

Separately classify the cumulative-loss family as:

- `horizon_family_loss_incidence_separation_detected`, or
- `no_detected_horizon_family_loss_incidence_separation`.

The joint interpretation is endpoint-relative. In particular, persistent or attenuating state divergence with no cumulative-loss separation is reported as **state information persisting without a detected effect on this binary long-horizon endpoint**, not as equivalence and not as evidence that alignment is irrelevant.

## 12. Publication-routing rule

This audit does **not** automatically merge the warning-validity and state-validity manuscripts.

A combined conceptual framing becomes eligible for consideration only if the propagation result supports a defensible statement about **target- and/or horizon-relative predictive adequacy** that is stronger than simply placing the known warning null beside the known alignment result.

Even then, the manuscript must not claim:

`warning failure -> missing cross-layer alignment`,

or that adding cross-layer alignment rescues the frozen warning rules. The warning denominator failure and the alignment sufficiency boundary remain separate mechanisms unless a separately preregistered direct bridge test establishes otherwise.

If the propagation audit shows only a very short-lived transition difference with no further endpoint structure, the default publication route remains separate warning-validity and state-validity papers.

## 13. Stop rules

After this preregistration is committed, do not:

1. change the two Phase-V initial states or add an intermediate alignment permutation;
2. change seeds, replicate count, forcing, barrier schedule, horizon, dynamics, mutation, migration, or patch identities;
3. add replacement seeds or extra replicates because an interval is wide;
4. insert or remove forecast horizons after inspecting intermediate snapshots;
5. open warning thresholds, warning times, ROC-selected scores, or diversity-decline cutoffs;
6. switch the primary propagation coordinate away from `D_I_max` because another state variable gives a cleaner curve;
7. fit an exponential decay or other parametric timescale and promote it as preregistered evidence;
8. select one intermediate McNemar p-value as the headline while ignoring the horizon family;
9. reinterpret the replay as an independent replication;
10. alter the original Phase-V locked decision or overwrite its artifact.

The propagation audit is a separately versioned post-review extension. All outcomes, including rapid attenuation, persistent divergence, nonmonotone propagation, endpoint-specific persistence, and no additional interpretable structure, are retained.