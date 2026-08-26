# Post-lock descriptive Eschscholzia F full-metadata repair

## Status and separation from prior decisions

This is a third, fully separate **post-lock descriptive reconstruction** declared after:

1. the permanent primary decision `multi_endpoint_not_identifiable`; and
2. the prospectively fixed one-key F sensitivity decision `stop_pre_model_unexpected_second_metadata_mismatch`.

Neither decision is reopened, replaced, weakened or rescued. The stopped one-key sensitivity remains stopped and is not expanded. This reconstruction asks only what the already declared F model estimates after correcting the complete metadata-only mismatch set identified before any F response, model score or bootstrap was inspected.

## Exact permitted corrections

The metadata-only preflight fixed exactly two mismatches between the locked pollinator and seed-function sources:

| array key | field | required seed-source value | required pollinator-source value | replacement |
|---|---|---|---|---|
| `1||3` | `Habitat` | `Fallow graound` | `Fallow ground` | `Fallow ground` |
| `1||4` | `Habitat` | `Fallow graound` | `Fallow ground` | `Fallow ground` |

Both and only these key-specific literal corrections are allowed. No fuzzy matching, global spelling normalization, edit-distance rule, row deletion, key reconstruction, majority vote or repair of another field/value is permitted.

The run must stop before `_prepare_f` if the raw mismatch set is not exactly the two rows above, either precondition fails, or any cross-source metadata mismatch remains after correction.

## Frozen analysis

After the two corrections, rerun only the original F analysis:

- response: `log1p(Mean_number_of_seeds_from_field_exposed_flowers)`;
- held-out unit: Experimental array, LOAO;
- S0/S1/S2 definitions unchanged;
- `Ridge(alpha=1.0)` unchanged;
- equal-array scoring unchanged;
- 10,000 array-bootstrap samples with RNG seed `20260825` unchanged;
- existing `D_capacity` S2-to-S3 extension unchanged.

Do not rerun G, C, R or any other endpoint. Do not change the source members, endpoint, pollinator coordinates, regularization, bootstrap, confidence level or model sequence.

## Reporting and claim ceiling

Use the literal analysis label `postlock_descriptive_full_metadata_repair`. Report the unchanged primary decision and unchanged one-key sensitivity STOP beside the estimate. Accept any result.

The reconstruction can describe the F estimate under the exact two-key correction. It cannot establish primary multi-endpoint identifiability, convergence, mediation, biological irrelevance of Habitat, or general sufficiency/insufficiency of pan-trap pollinator availability. It is descriptive information recovery, not a confirmatory sensitivity and not a new primary analysis.
