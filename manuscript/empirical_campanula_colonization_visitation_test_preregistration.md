# Prospective Campanula colonization realised-visitation state test

## Status at registration

This is the required second exact-model preregistration after #111 established `realised_visitation_function_state_identifiable` from file hashes and headers only. No row-level seed number or realised visitation value has been inspected by this project before this document is committed.

Source remains fixed to Zenodo `10.5281/zenodo.10814705`:

- `PLdataindividual.csv`, MD5 `b84fa5c83513dbe75c0bf7840d1c74aa`;
- `pollinator.csv`, MD5 `81e0deaa78a6a97e1211484cb9d0d3b3`.

## Scientific question

> **Does realised pollinator visitation per flower add transferable information about individual pollen limitation after source/site/timing background is represented, and do colonization size or autonomous-selfing state retain residual predictive information after realised visitation is supplied?**

The primary target is process-state information, not significance of any one source-model coefficient.

## Fixed hierarchy and validation unit

The locked sampling hierarchy is:

`site -> experimental population -> individual -> pollination treatment`.

`visits.per.flower` is shared by all individuals in one experimental population. Therefore the primary validation is **leave-one-experimental-population-out (LOPO)**. Every individual/treatment row from the held-out experimental population is excluded from model fitting. Row-wise or individual-wise cross-validation is prohibited.

## Source consistency gates before fitting

Before any model is fit:

1. `pollinator.csv` must contain exactly one row per `experimental.population`. If duplicate population rows occur, they are not averaged; the endpoint is `not_identifiable_for_primary_endpoint`.
2. In the seed file, `site`, `source.population`, `autonomy`, and `size` must each be constant within `experimental.population` after stripping leading/trailing whitespace.
3. Those population-level values must exactly match the corresponding pollinator-file values after stripping whitespace. `source.population` in the seed file is mapped only to the source-declared `source population` column in the pollinator file. No spelling, case, majority-vote or fuzzy correction is allowed.
4. `dayfromstartofexperiment` must be numeric and constant within each `individual` across its treatment rows. If not, that individual is excluded from the paired primary endpoint; no value is imputed.
5. `visits.per.flower` must be finite numeric for every experimental population used in validation. No alternate bee-group or visit-count metric is substituted.

If fewer than 8 experimental populations or fewer than 20 individuals remain with a valid paired primary endpoint, the primary endpoint is `not_identifiable_for_primary_endpoint`.

## Fixed treatment mapping and primary response

`treatment` values are normalized only by trimming whitespace and lower-casing for token detection.

- a value containing `control` is the control treatment;
- a value containing `supp` is the supplemented treatment;
- any other treatment label is not used in the primary paired endpoint and is not remapped after inspection.

For each `experimental.population × individual × treatment-class`, multiple seed rows, if present, are averaged within that fixed class. An individual must have both classes.

Primary response:

\[
PL_{abs} = \overline{seed}_{supplemented} - \overline{seed}_{control}.
\]

Higher `PL_abs` means greater seed-set increase under pollen supplementation and therefore greater realised pollen limitation on this source scale. No ratio or relative transformation is opened after seeing values.

Secondary direct-function response, fixed now:

\[
F_{control}=\overline{seed}_{control}.
\]

The secondary endpoint is descriptive/parallel validation and does not replace the primary endpoint if `PL_abs` is weak.

## Fixed state sequence

All models use the same valid individuals for a given endpoint.

### S0 — background state

- categorical `site`;
- categorical `source.population`;
- standardized numeric `dayfromstartofexperiment`.

This is the baseline/background representation and is not interpreted as an interaction state.

### S1 — realised interaction state

S0 plus standardized population-level `visits.per.flower`.

This is the fixed `I_realised` coordinate. `total.poll.visits` and individual bee-group counts are not opened as alternatives.

### S2 — colonization-size context

S1 plus categorical `size`.

This asks whether the single/small colonization context retains residual transferable information after realised visitation.

### S3 — compensatory/reproductive route

S2 plus categorical `autonomy`.

`autonomy` is interpreted only as a source-defined alternative reproductive-route / reproductive-assurance coordinate (`R`). It is not converted into a continuous score.

## Fixed model family

Both `PL_abs` and `F_control` are modelled with `sklearn.linear_model.Ridge(alpha=1.0)`.

- categorical predictors: one-hot encoding with `handle_unknown="ignore"`;
- numeric predictors: standardized from the training fold only;
- no interactions;
- no polynomial terms;
- no feature selection;
- no hyperparameter search;
- no alternative alpha after the result.

## LOPO scoring

For each held-out experimental population and state S0–S3:

1. fit on all other populations;
2. predict every valid individual in the held-out population;
3. calculate the population-level mean squared error (MSE).

Primary comparisons use paired held-out-population score gains:

- realised-interaction gain: `MSE(S0) - MSE(S1)`;
- colonization-size residual gain: `MSE(S1) - MSE(S2)`;
- autonomy residual gain: `MSE(S2) - MSE(S3)`.

Positive gain means the larger state predicts the unseen population better.

## Fixed uncertainty

For each score gain, bootstrap the held-out experimental populations with replacement **10,000 times**, RNG seed `20260825`.

A positive gain is `supported_positive_gain` only when the 95% percentile bootstrap interval lies wholly above zero. No alternative bootstrap seed, confidence level, or row-level bootstrap is opened.

## Primary endpoint decision

For `PL_abs`:

- **`realised_visitation_informative_context_redundant`**: S0→S1 is supported positive, while S1→S2 and S2→S3 are not supported positive;
- **`residual_colonization_size_after_visitation`**: S1→S2 is supported positive, regardless of the S0→S1 result; report the process-state result separately;
- **`residual_compensation_after_context`**: S2→S3 is supported positive; report earlier state gains separately;
- **`realised_visitation_not_predictively_supported`**: S0→S1 is not supported positive and neither residual extension is supported positive;
- **`not_identifiable_for_primary_endpoint`**: a source-consistency, sample-size, treatment-pairing, finite-value, or LOPO fitting gate fails.

If both S1→S2 and S2→S3 are supported, the overall label is `residual_compensation_after_context`, with the size result retained explicitly rather than overwritten.

## Cross-endpoint interpretation

`F_control` is evaluated with the same S0–S3 sequence and uncertainty rules, but it cannot rescue or replace the primary `PL_abs` classification. Concordance or disagreement is itself retained as a measurement result.

## Claim ceiling

This test can establish whether population-level realised visitation is a transferable predictor of pollen limitation/direct seed function in this experimental-colonization system. It does not measure stigma pollen receipt, pollen quality, donor identity, or genetics; it cannot establish a universally sufficient interaction state or a universal colonization threshold.

## Stop rule

Do not switch to `total.poll.visits`, bee-group-specific visits, a ratio pollen-limitation endpoint, a subset of sites/source populations, another ridge alpha, interactions, row-level validation, or alternative bootstrap seeds because the result is weak or surprising. No category spelling is repaired after outcome inspection.