# Protocol 002 Stage I source-runner skeleton

## Purpose

This skeleton fixes the artifact schema for H1 source reconstruction before any
Protocol 002 source grid is run.

It is not a source-reconstruction campaign. It records what every future attempt
must retain, including failures and non-runs.

## Required retained statuses

Every declared source coordinate must be represented by one of the following
closed statuses:

```text
not_run
preparation_failed
source_support_failed
projection_failed
success
```

A future source campaign may not retain only successful source attempts. Failed
preparation, failed support, failed projection, and explicit non-runs are all
part of the evidence boundary.

## Coordinate identity

Every source attempt row must include:

```text
kappa_mu
p_star
area_reference
kappa
nested_barrier_grid
stage_generations
hold_generations
master_seed
replicate
```

The row must also contain:

```text
status
source_prepared
source_supported
projection_supported
reason
```

## Consistency rules

- `success` requires `source_prepared`, `source_supported`, and
  `projection_supported` all to be true.
- An unprepared source may only be `not_run` or `preparation_failed`.
- Every row must have a non-empty reason.
- Skeleton manifests must declare `simulation_result_present: false`.

## What is intentionally absent

- no H1 source grid execution;
- no stochastic finite drift campaign;
- no ecological result;
- no source-support statistics;
- no deterioration schedule;
- no H2 warning calculation.

This PR only fixes the container into which the future Stage I source campaign
will write results.

## Next gate

The next PR should add a tiny deterministic example manifest using this schema
and a command to write it. Only after the schema and writing path are stable
should the declared Stage I source seeds be launched.