# Campanula experimental-colonization realised-visitation result

## Locked decision

**`not_identifiable_for_primary_endpoint`**

The prospectively declared test asked whether population-level realised visitation (`visits.per.flower`) improved held-out prediction of individual pollen limitation and whether colonization size or autonomous-selfing state retained residual predictive information after visitation was supplied.

The result-generating workflow on head `90897afe7adf09c82d562f93b6a590e38f8d3cba` completed successfully:

- custom analysis workflow `32820158897`;
- job `97716379289`;
- result artifact `9552804680`;
- artifact digest `sha256:f5b98480a0a59f934ceb444b7ba22d2d923f0174851bed5cb4dfc3ac9ba98e65`;
- Protocol invariant, Paper completion and two-repository reproducibility all succeeded on the same head.

No S0–S3 outcome model was fitted because the preregistered finite-value gate failed first.

## Why the endpoint closed

After the one-directional population-key correction, the response-bearing seed populations were:

`49, 50, 51, 52, 53, 54, 55, 56, 57`.

Every one of those populations had a unique matching pollinator row and passed the declared context-key checks, but `visits.per.flower` was non-finite in all nine. The locked decision therefore became:

- decision: `not_identifiable_for_primary_endpoint`;
- reason: `nonfinite_visits_per_flower`.

The preregistration explicitly prohibited substitution of `total.poll.visits`, bee-group-specific counts, imputation or deletion of response populations after this gate failed.

## Predictor-only diagnosis after closure

A separate predictor-only diagnostic was run **after** the decision had already closed and was not allowed to alter it.

- diagnostic workflow `32821053514`;
- job `97719052467`;
- diagnostic artifact `9553145870`;
- artifact digest `sha256:a27c39cf6ae0231be8b104b84c3b5c2265daa316f787a373dd40e264c988925b`.

For all nine response-bearing populations:

- raw `visits.per.flower` = `NA`;
- raw `total.poll.visits` = `NA`;
- observed flower-count fields contained positive finite values (where present).

Thus the non-finite ratio was **not** caused by zero flowers. The direct visitation measurement itself was unavailable for the populations carrying seed outcomes.

Three additional pollinator populations (`6`, `12`, `37`) had predictor records but no seed-outcome rows; they remain provenance-only and were never used to repair the response-bearing coverage gap.

## Scientific interpretation

This is a stronger measurement boundary than a weak predictive result.

The archive was schema-joinable at the level of keys and declared columns, yet row-level **measurement coverage did not overlap for the required predictor and response units**. Therefore:

> schema-level state identifiability is necessary but not sufficient; a candidate state must also be observed on the same ecological units that carry the future/function endpoint.

The result does **not** show that realised visitation is uninformative. It shows that this particular experimental archive cannot test that question without post-hoc substitution or imputation.

This complements the Eschscholzia result. There, an available array-level pollinator proxy failed to earn endpoint-relevant predictive status. Here, a conceptually stronger realised-visitation coordinate could not be evaluated because it was absent from every response-bearing population. Together they separate two distinct empirical failure modes:

1. **candidate-state inadequacy** — the measured variable exists but does not improve held-out prediction;
2. **candidate-state coverage failure** — the desired variable is not synchronously observed on the response units.

## Claim ceiling

Do not report a visitation effect size, sign, coefficient, pollen-limitation gain, colonization-size residual effect or autonomy residual effect from this campaign. None was estimated.

## Stop rule

Do not reopen this archive with `total.poll.visits`, bee-group visit counts, inferred visits, imputed `visits.per.flower`, response-unit deletion, alternative endpoints or altered validation. Any further test of realised/effective visitation must use an independently declared dataset with predictor and response coverage aligned prospectively.