# Protocol 002 minimal H1 source-runner adapter smoke

## Purpose

This adapter fixes the ordered Stage I runner contract:

```text
prepare source
-> test source support
-> test projection support
-> retain one SourceAttemptRecord
```

The committed smoke artifact uses one mutation coordinate, one master seed, and
two replicates. All three stage checks are deterministic passing callbacks.

## Smoke subset

```text
kappa_mu = 0.20
p_star = 0.50
area_reference = 1.0
kappa = 4.5
nested_barrier_grid = 49
master_seed = 20270210
replicates = 0, 1
```

## Interpretation

This is an adapter smoke execution only. It does not run the ecological H1 source
reconstruction model and therefore is not Type S evidence.

The smoke artifact must retain:

```text
simulation_result_present = false
record_count = 2
success = 2
```

## Next gate

Replace the deterministic stage callbacks with a pinned minimal adapter to the
actual upstream source-reconstruction implementation, then run the same tiny
subset before expanding to the full 10,125-row Stage I campaign.
