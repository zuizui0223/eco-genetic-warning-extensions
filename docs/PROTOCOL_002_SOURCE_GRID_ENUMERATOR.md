# Protocol 002 Stage I source-grid enumerator

## Purpose

This enumerator writes the declared Stage I source-attempt plan before any H1
source reconstruction is run.

It is a planning artifact only. Every row is retained as `not_run`.

## Default grid

The default grid is:

```text
mutation coordinates: 15
area_reference:       0.8, 1.0, 1.2
kappa:                3.0, 4.5, 6.0
nested barrier grid:  25, 49, 97
master seeds:         20270210–20270214
replicates:           5 per cell
stage generations:    30
hold generations:     30
```

Total planned rows:

```text
15 × 3 × 3 × 3 × 5 × 5 = 10,125
```

## Command

```bash
protocol002 write-source-grid-plan \
  --output artifacts/protocol002/source_grid_planned_manifest.json \
  --force
```

The same planned manifest can be inspected without writing a file:

```bash
protocol002 write-source-grid-plan --stdout
```

## Interpretation

The planned manifest must declare:

```text
simulation_result_present = false
```

and its status counts must be:

```text
not_run = 10125
preparation_failed = 0
source_support_failed = 0
projection_failed = 0
success = 0
```

## What is intentionally absent

- no H1 source reconstruction;
- no source-support statistic;
- no projection result;
- no stochastic finite-drift campaign;
- no deterioration calibration;
- no warning calculation.

## Next gate

The next PR may commit the generated planned-grid manifest and require it to
match the writer output exactly. Only after that should the source-reconstruction
runner itself be introduced.
