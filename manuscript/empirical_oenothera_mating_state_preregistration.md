# Prospective natural-data test — *Oenothera harringtonii* mating-state residual isolation

## Purpose

This test targets a missing empirical layer in the current state-defined reproducibility programme: **contemporary mating/genetic state** rather than direct ecological function.

The question is:

> After conditioning on the available functional pollinator treatment, does individual spatial isolation still contain predictive information about correlated paternity / mating diversity?

A positive residual isolation effect would not contradict E1/E2. It would show why `C` / mating opportunity must remain a separate state coordinate when `I/T` alone does not absorb spatial structure.

## Source lock

The source is fixed before refitting to:

- Rhodes, Fant & Skogen (2017), *Molecular Ecology* 26:4296–4308, doi:`10.1111/mec.14115`;
- archived dataset doi:`10.5061/dryad.p24q3`;
- public Zenodo mirror record `4942351`;
- primary file `multiplePaternity.csv`, published MD5 `600f6f370ffa8ad205d0ccb6bc92ab65`.

The public metadata defines the primary columns:

- `plantID` — maternal family identifier;
- `treatment` — pollinator-exclusion treatment (`c`, `de`, `ne`);
- `isolation20` — summed Euclidean distance to the twenty nearest neighbours;
- `correlatedPaternity` — MLTR correlated-paternity estimate for the seed family.

No additional response or landscape variable is selected after the result.

## Biological interpretation of variables

`treatment` is used as the available **functional pollinator-access state**. The treatments experimentally alter access by day- versus night-active pollinators; they are not treated as a generic habitat label.

`isolation20` represents the local spatial mating opportunity that is not encoded by pollinator identity alone.

`correlatedPaternity` is retained on its source scale as the primary response. Higher correlated paternity means a greater probability that two offspring share a father and therefore **lower realised paternal diversity**. No threshold is imposed.

This endpoint is a `G_mating / C_pollen` process outcome, **not** realised ecological function `F` and not a functional-loss endpoint.

## Fixed model sequence

### M0 — pollinator state only

`correlatedPaternity ~ treatment`

### M1 — pollinator state + residual isolation

`correlatedPaternity ~ treatment + z(isolation20)`

No treatment × isolation interaction is opened for the primary test. The published study reports the isolation effect as broadly consistent across pollinator identity, and the purpose here is the incremental state coordinate, not interaction discovery.

## Validation

Primary prediction uses leave-one-maternal-family-out cross-validation. Each seed-family row is held out once; no offspring within a family are split across train/test because the response is already family-level.

Primary predictive score: mean squared prediction error (MSE).

Secondary summaries:

- mean absolute error;
- full-data OLS coefficient on standardized `isolation20`;
- treatment-level sample sizes and response means.

## Permutation test

Incremental isolation information is also tested with a fixed 10,000-permutation procedure, random seed `20260824`.

- fit M0 and M1 to the observed data;
- statistic: `RSS(M0) - RSS(M1)`;
- permute `isolation20` **within treatment groups**, preserving treatment composition and the response;
- refit M1 for every permutation;
- one-sided permutation p-value = `(1 + number(permuted statistic >= observed statistic)) / 10001`.

This tests the incremental isolation term without converting the source data into arbitrary isolation classes.

## Decision rule

- **`residual_isolation_detected`**: M1 has lower leave-one-family-out MSE than M0, the full-data isolation coefficient is positive on the correlated-paternity scale, and permutation `p < .05`.
- **`predictive_residual_isolation_only`**: M1 improves held-out MSE but the coefficient/permutation criterion is not met.
- **`model_residual_isolation_only`**: coefficient is positive with permutation `p < .05`, but held-out MSE does not improve.
- **`no_detected_residual_isolation`**: neither predictive nor permutation criterion is met.
- **`not_identifiable_from_archive`**: required source columns are absent, contain unrecoverable missingness, or leave-one-family-out fitting is not defined.

All classifications are retained. No alternative response, isolation metric or subset is opened because the primary result is weak or strong.

## Claim ceiling

A detected residual isolation effect supports only:

> functional pollinator identity/access is not sufficient to describe the contemporary mating state in this natural system; local spatial mating opportunity remains future-/process-relevant information.

It does **not** establish a general fragmentation threshold, a direct functional-loss effect, or full eco-genetic state sufficiency.

## Stop rule

Run the locked public file once. Do not replace the correlated-paternity endpoint, dichotomise isolation, remove treatments, search alternative neighbourhood definitions, or use the offspring genotypes to create a new primary endpoint after seeing the result.
