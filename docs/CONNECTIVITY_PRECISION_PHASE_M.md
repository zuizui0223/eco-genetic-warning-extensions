# Phase M — high-precision validation of the Phase-E connectivity claim

## Trigger

Phase L showed that the historical Phase-E R3 labels at `migration_rate=0.10` and `0.20` do not independently identify biological between-block heterogeneity at the original 15–20 eligible trajectories per block. Phase M therefore precision-expands the exact historical Phase-E experiment rather than retaining the R4→R3 interpretation by label alone.

## Fixed design

- historical Phase-E master seeds: `20290410–20290414`;
- all five historical allele-frequency mixing rates: `0, 0.025, 0.05, 0.10, 0.20`;
- same recurrent-transition and ecological anchor as Phase E;
- 100 attempted source replicates per master seed;
- all migration levels paired on each prepared source and trajectory seed;
- genetic warning/diversity outcomes unavailable to the decision.

`migration_rate` remains an allele-frequency mixing operator only. It is not pollen, seed, demographic, pollinator or recolonisation movement.

## Prefix provenance gate

For every master seed and every migration rate, the first 20 attempted replicates must reproduce the locked Phase-E eligible/loss counts exactly. Any mismatch is an implementation/provenance failure and blocks interpretation.

## Precision target

Each full 100-attempt migration block must retain at least 70 baseline-eligible trajectories. The historical `[0.30,0.70]` five-block screen is applied unchanged.

## Primary question

Do the historical `m=0.10` and `m=0.20` R3 classifications persist at high precision?

- if either remains R3 with precise blocks, retain a bounded event-regime difference and inspect explicit heterogeneity evidence;
- if both become R4, withdraw the claim that allele-frequency connectivity changes warning estimability/reproducibility through an R4→R3 transition;
- if another level changes class, report the full high-precision map rather than selecting a preferred threshold.

## Paired biological effect

The gate classification is not the only estimand. For each nonzero migration rate, compare paired loss status against `m=0` across all high-precision trajectories and report:

- loss→no-loss switches;
- no-loss→loss switches;
- exact two-sided McNemar test;
- direction of the marginal paired difference.

Thus even if all levels are R4 at high precision, connectivity could still alter functional-loss probability or individual stochastic histories. Conversely, bidirectional switching without a directional marginal effect must not be called rescue/collapse.

## Stop rule

Use the five locked master seeds once at 100 attempts per seed. Do not add replacement seeds, alter migration levels, modify the historical R4 band, or increase precision again merely to preserve a previous R3 claim.
