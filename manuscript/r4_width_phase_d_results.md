# Warning-blind R4 width refinement Phase D — results

## Provenance

Prospectively declared in `docs/WARNING_BLIND_R4_WIDTH_PHASE_D.md` after Phase C recovered one R4-highrep cell and before Phase-D simulation.

- workflow run: `32352987752`;
- artifact: `9401002111`;
- digest: `sha256:f56ffb7dcbccdca1d681145b4fcfe01b88389d0e7be66b16adaa41df3a0b1000`;
- workflow head: `f7ab41a06e9ffbb60b295d68f1fb52b357c26a4a`;
- fixed non-direction conditions: `A_ref=1.0`, interaction `kappa=4.5`, `kappa_mu=0.35`, horizon 120, normalized barrier increase 0.30;
- fresh seeds: `20290310–20290314`;
- 20 replicates per seed;
- 100 attempts per cell, 300 total;
- calibration scope: trait-loss only.

No genetic-diversity, warning-time, lead/lag or warning-performance field was available to Phase D.

## Result 1 — the Phase-C R4 cell independently replayed

At `p_star=0.350`:

- baseline-eligible counts by seed: `16, 18, 17, 17, 19`;
- seed-block functional-loss rates: **0.500, 0.667, 0.647, 0.588, 0.632**;
- pooled loss rate: **0.609**;
- seed-rate range: `0.167`;
- all five blocks lie in `[0.30,0.70]`;
- classification: **R4-highrep**.

This independently reproduces the Phase-C result at the same nominal `p_star=0.35` with a completely new master-seed family.

## Result 2 — neither immediate neighbor was R4

### Lower neighbor: `p_star=0.325`

- seed rates: `0.529, 0.526, 0.800, 0.667, 0.778`;
- pooled loss: `0.663`;
- two seed blocks exceed the strict upper bound 0.70;
- classification: **R3-highrep**.

### Upper neighbor: `p_star=0.375`

- seed rates: `0.412, 0.389, 0.529, 0.389, 0.235`;
- pooled loss: `0.391`;
- one seed block lies below the strict lower bound 0.30;
- classification: **R3-highrep**.

Thus `p_star=0.35` is not merely one point inside a broad `[0.325,0.375]` R4 interval under the current strict gate.

## Result 3 — R4 exists, is reproducible, and is narrower than the 0.025 grid resolution

Combining Phases C and D:

- `p_star=0.35` is R4-highrep under **two independent five-seed families**, each with 20 replicates per seed;
- `p_star=0.325`, `0.375` and `0.40` are outside R4 under high-rep evaluation;
- the original coarse Protocol 002 grid omitted `0.35` and therefore missed this evaluable condition.

The recoverable conclusion is therefore:

> **A reproducible intermediate-risk event regime exists in the declared finite closure, but its location along the recurrent-transition direction axis is narrow: the confirmed R4 point at `p_star=0.35` is flanked by non-R4 cells within ±0.025 under the same ecological and deterioration conditions.**

The exact mathematical width of R4 is not identified. Phase D establishes only that it is narrower than the present 0.025 neighbor spacing under the strict all-seed criterion.

## Result 4 — pooled event probability still overstates evaluability

Both non-R4 neighbors have apparently intermediate pooled loss rates:

- `p_star=0.325`: pooled `0.663`;
- `p_star=0.375`: pooled `0.391`.

Yet each fails because at least one independent seed block leaves `[0.30,0.70]`.

Therefore pooled event risk alone would classify a much broader interval as usable than the reproducibility-based R4 criterion. This distinction survives high replication and fresh seed families.

## Decision under the predeclared Phase-D rule

`p_star=0.35` replayed as R4-highrep, but neither immediate neighbor was R4-highrep. Therefore:

- record R4 as **narrower than the current 0.025 grid resolution**;
- stop recurrent-transition `p_star` tuning for the present condition-recovery program;
- do not release genetic-warning endpoints from Phases A–D;
- do not claim a contiguous R4 interval wider than the confirmed point;
- move the next condition question to an independent biological axis rather than searching ever-finer `p_star` values merely to widen R4.

The next biologically motivated axis is **effective connectivity/migration**, because the parent closure already contains isolated and equal-migrating projections plus an exact rescue–homogenization trade-off. This axis also connects directly to urban corridor/pollen-flow and island stepping-stone applications.
