# Protocol 002 source-runner interface

## Purpose

This interface is the first bridge from planned Stage I source rows to retained
attempt records.

It does not run H1 source reconstruction. It only defines how an evaluator must
map each planned source coordinate into a retained `SourceAttemptRecord`.

## Core contract

A source runner receives:

```text
Protocol002SourceCoordinate
```

and returns:

```text
SourceAttemptEvaluation
```

The evaluation is then attached to the coordinate and converted into a retained
record. The record is validated by the existing source-skeleton consistency
rules.

## Retained statuses

The deterministic fixture covers all retained statuses:

```text
success
preparation_failed
source_support_failed
projection_failed
not_run
```

The fixture uses five replicates from a tiny one-cell source grid and maps each
replicate to one status. This is for interface testing only.

## What is intentionally absent

- no ecological simulation;
- no H1 source reconstruction;
- no source-support statistic;
- no projection result from a real source;
- no stochastic finite-drift campaign;
- no deterioration calibration;
- no warning calculation;
- no Type S ecological result.

## Next gate

The next PR may add a deterministic fixture artifact writer for the runner
interface. After that, a minimal source-runner adapter can be introduced before
any full source-reconstruction campaign is launched.
