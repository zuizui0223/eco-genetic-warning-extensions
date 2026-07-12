# Protocol 002 Stage II calibration grid

## Purpose

This grid enumerates the complete trait-loss-only Stage II calibration plan before
any calibration trajectory is run.

## Planned size

```text
15 mutation coordinates
× 3 area_reference values
× 3 kappa values
× 2 hold durations
× 3 normalized barrier increases
= 810 candidate cells
```

Each candidate cell has:

```text
5 master seeds × 5 replicates = 25 attempts
```

Therefore the complete planned campaign contains:

```text
810 × 25 = 20,250 attempts
```

## Blindness boundary

The full manifest contains only coordinate, source-domain, schedule, seed, and
replicate identity. It contains no warning, lead/lag, diversity,
heterozygosity, or event-pair fields.

The committed lightweight lock records the SHA-256 digest of the full generated
manifest:

```text
artifacts/protocol002/stage2_calibration_planned_lock.json
```

## Interpretation

- planning rows only;
- no calibration simulation result;
- no domain selected;
- trait-loss-only endpoint boundary retained;
- Stage III warning validation remains unavailable.

## Next gate

Connect one tiny pinned-upstream trait-loss-only calibration smoke run using one
mutation coordinate, one source cell, one schedule, one master seed, and one
replicate. The smoke artifact must still contain no warning or diversity fields.
