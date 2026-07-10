# Protocol 002 source-skeleton example CLI

## Purpose

This command writes a deterministic example manifest for the Stage I source-runner
skeleton. It verifies the serialization path before any H1 source reconstruction
campaign is launched.

## Command

```bash
protocol002 write-source-skeleton-example \
  --output artifacts/protocol002/source_skeleton_example_manifest.json \
  --force
```

The same content can be printed without writing a file:

```bash
protocol002 write-source-skeleton-example --stdout
```

## What the example contains

The example manifest has exactly one explicit `not_run` source-attempt record. It
uses a fixed coordinate:

```text
kappa_mu = 0.20
p_star = 0.75
area_reference = 1.0
kappa = 4.5
nested_barrier_grid = 49
stage_generations = 30
hold_generations = 30
master_seed = 20270210
replicate = 0
```

The manifest declares:

```text
simulation_result_present = false
```

## What it does not contain

- no source reconstruction result;
- no source support statistic;
- no projection result;
- no stochastic drift campaign;
- no deterioration calibration;
- no genetic warning calculation.

This command tests only the artifact-writing path and schema stability.

## Next gate

After this writer is stable, the next PR may commit the generated example
artifact and require it to match the writer output exactly. Only after that
should the declared Stage I source seeds be launched.