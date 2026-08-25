# Campanula population-key gate correction before outcome fitting

## Failure point

The first row-level workflow (`32819915952`) successfully verified the two locked Zenodo files and then stopped **before treatment aggregation, response construction, model fitting, prediction, bootstrap inference, or any outcome summary**.

The stop reason was `population_key_mismatch_between_sources`. The diagnostic exposed only population identifiers and merge membership:

- pollinator-only experimental population `6`;
- pollinator-only experimental population `12`;
- pollinator-only experimental population `37`.

No seed number, `visits.per.flower` value, treatment contrast, coefficient, prediction or effect direction was inspected.

## Cause

The implementation used an outer join and required the **entire set** of experimental populations in the pollinator file to equal the set in the seed-outcome file.

That is stricter than the preregistered scientific gate. The preregistration requires that every experimental population contributing a reproductive response has a unique matching pollinator-state row and matching context. It does not require pollinator observations from populations lacking seed outcomes to be treated as response-bearing units.

A pollinator-only population cannot contribute to `PL_abs` or `F_control`; excluding it from an outcome model is defined by response availability, not by the observed direction or magnitude of its pollinator state.

## Fixed correction

Before any outcome model is fitted, the key gate is corrected to:

1. derive the population set from the seed-outcome table;
2. require **every seed-outcome population** to have exactly one pollinator row;
3. require exact context agreement (`site`, source population, `autonomy`, `size`) for those response-bearing populations;
4. permit extra pollinator-only populations to remain in source provenance but not enter outcome fitting;
5. record their IDs and count in diagnostics.

No fuzzy ID repair, ID remapping, response filtering by effect, alternate visitation variable, endpoint change, model change, validation change or bootstrap change is allowed.

## Scientific boundary

This is a one-directional availability correction: predictors may exist for units with no measured response, but every response unit must have its declared predictor state. The correction would be identical regardless of the visitation values or seed outcomes in populations `6`, `12`, and `37`.