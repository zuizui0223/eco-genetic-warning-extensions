# Warning-blind R4 width refinement — Phase D

## Status

Prospectively declared after Phase C recovered exactly one R4-highrep cell at `p_star=0.35` and before any genetic-warning field is released.

Phase D measures the **width and reproducibility of the event-regime R4 region**. It does not tune ecological/deterioration parameters and does not evaluate genetic warning.

## Fixed non-direction conditions

Retain the exact Phase B/C anchor:

- `A_ref=1.0`;
- interaction-feedback `kappa=4.5`;
- `kappa_mu=0.35`;
- ramp 30, hold 90, horizon 120;
- normalized barrier increase `0.30`;
- equal-isolated projection.

Only `p_star` varies.

## Phase-D grid

Use three cells on one fresh common seed family:

- `p_star=0.325` — new lower neighbor;
- `p_star=0.350` — independent replay of the Phase-C R4 cell;
- `p_star=0.375` — new upper neighbor between the Phase-C R4 `0.35` and R3-highrep `0.40` cell.

No wider grid is allowed in Phase D.

## Fresh seeds and replication

Use a seed family not previously present in the repository:

`20290310, 20290311, 20290312, 20290313, 20290314`

For each cell:

- 20 replicates per seed;
- 5 seeds;
- 100 attempts per cell;
- 300 planned attempts total.

Every cell independently reconstructs its own high-function source.

## Permitted quantities

Only source and functional-loss event-regime quantities are available:

- source preparation/projection support;
- baseline realised high-trait presence;
- baseline-eligible denominator per seed;
- realised functional-loss occurrence/time;
- seed-block and pooled trait-loss rates;
- R1/R2/R3/R4 classification.

Forbidden:

- `H_alpha`, `H_gamma` or any diversity metric;
- warning value/time;
- lead/lag/tie or intervention time;
- parameter selection based on warning results.

## R4 classification

A cell is classifiable only if every seed has at least 10 baseline-eligible trajectories.

- `R4-highrep`: every seed-block functional-loss rate is in `[0.30,0.70]`;
- `R2-highrep`: every rate >0.70;
- `R1-highrep`: every rate <0.30;
- `R3-highrep`: all other supported patterns.

## Decision rule

1. If `0.35` replays as R4-highrep and at least one adjacent cell (`0.325` or `0.375`) is also R4-highrep, freeze the contiguous R4 interval spanned by those cells. Condition exploration on recurrent-transition direction is complete for the current closure; no further `p_star` tuning is allowed before a separately declared warning-validation protocol.
2. If all three are R4-highrep, freeze `[0.325,0.375]` as the finite matched event-regime interval.
3. If `0.35` is R4-highrep but neither neighbor is R4-highrep, record R4 as narrower than the current 0.025 grid resolution; do not widen ecological parameters.
4. If `0.35` fails to replay as R4-highrep, record the Phase-C R4 result as seed-family sensitive and do not open warning validation. Further work, if any, must address event-regime reproducibility rather than warning performance.

## Evidence boundary

Phase D uses only source/trait-loss information from prior phases to choose the local grid. No genetic-warning outcome has been inspected in Protocol 002 frontier refinement Phases A–D.
