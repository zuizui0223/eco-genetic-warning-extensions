# Protocol 002 Stage I resumable batch campaign

## Campaign partition

The corrected Stage I design contains 3,375 attempts:

```text
15 mutation coordinates
× 3 area-reference values
× 3 interaction-feedback values
× 5 master seeds
× 5 replicates
= 3,375 attempts
```

The campaign is partitioned into 135 resumable batches. One batch is exactly:

```text
1 mutation coordinate
× 1 area_reference
× 1 kappa
× 5 master seeds
× 5 replicates
= 25 attempts
```

The batch order is deterministic:

1. `primary_phase_grid()` order;
2. `area_reference = 0.8, 1.0, 1.2`;
3. `kappa = 3.0, 4.5, 6.0`.

Therefore batch 0 is:

```text
kappa_mu = 0.05
p_star = 0.10
area_reference = 0.8
kappa = 3.0
```

and batch 134 is the last declared phase cell.

## Execution

Each batch runs:

```text
real H1 boundary-resolution audit
→ source-support status
→ full-state high-source reconstruction
→ 30-generation hold
→ projection to one_large / equal_isolated / equal_migrating
→ one retained JSON artifact
```

The workflow can be resumed by batch index. A completed batch artifact is the
unit of retained Stage I evidence. H2/H3 horizon simulation is not run here.

## Completion rule

The full Stage I campaign is complete only when all 135 batch artifacts are
present and their batch identities cover indices 0 through 134 exactly once.
No missing batch may be silently omitted from the denominator.
