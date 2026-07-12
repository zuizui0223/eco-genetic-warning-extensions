# Protocol 002 Stage II calibration batch campaign

## Batch unit

The full trait-loss-only calibration campaign is partitioned into 810 candidate-cell batches.

Each batch fixes:

```text
one mutation coordinate
one area_reference
one kappa
one hold duration
one normalized barrier increase
```

and runs:

```text
5 calibration master seeds × 5 replicates = 25 attempts
```

The full campaign therefore contains:

```text
810 × 25 = 20,250 attempts
```

## Blindness boundary

Batch artifacts retain only:

- source support and preparation;
- equal-isolated projection support;
- baseline realised high-trait eligibility;
- realised trait-loss time and occurrence;
- seed-block trait-loss rates.

They do not contain warning, diversity, lead/lag, or event-pair fields.

## Wave 001

The first execution wave runs batch indices 0–19 with `max-parallel: 20`, for 500 attempts total.

No calibration domain is selected until all candidate-cell artifacts required by the predeclared ranking rule are available.
