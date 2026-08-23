# Warning-blind migration-condition Phase E

## Status

Prospectively declared after Phase D closed the recurrent-transition `p_star` refinement.

Phase D independently replayed a narrow R4 event regime at:

- `A_ref=1.0`;
- interaction `kappa=4.5`;
- `kappa_mu=0.35`;
- `p_star=0.35`;
- ramp 30 + hold 90;
- horizon 120;
- normalized barrier increase `0.30`;
- equal isolated patches (`migration_rate=0`).

The neighboring `p_star=0.325` and `0.375` cells were R3-highrep. The `p_star` search is therefore closed; Phase E does not refine or retune that coordinate.

## Question

At the independently reproduced R4 anchor, how does **allele-frequency migration among fragmented patches** change the realised functional-loss regime?

This is a condition-mapping question, not a genetic-warning test.

## Scope of `migration_rate`

In the pinned parent simulator, after local selection the patch allele frequency is updated as

\[
p_i'=(1-m)p_i+m\bar p,
\]

where \(\bar p\) is the population-weighted selected mean.

Therefore the Phase-E axis is **genetic mixing among patches**. It is not:

- demographic migration;
- pollinator movement;
- seed dispersal;
- recolonisation;
- trait-bin dispersal.

Parent theory implies that the migration step contracts deviations from the selected mean by a factor `1-m` and can homogenize patch frequencies. That theorem does not determine the sign of migration on realised functional loss in the full stochastic life cycle.

## Fixed biological anchor

All non-migration parameters are frozen to the independently reproduced Phase-C/D R4 anchor:

- `A_ref=1.0`;
- interaction `kappa=4.5`;
- `kappa_mu=0.35`;
- `p_star=0.35`;
- ramp generations = 30;
- hold generations = 90;
- horizon = 120;
- normalized barrier increase = `0.30`;
- four equal fragmented patches at fixed total area;
- same parent scientific commit `dd8ee379d0d3518194c767d16402042525bc00dc`.

The only Phase-E factor is `migration_rate`.

## Migration grid

Predeclared rates:

`0.000, 0.025, 0.050, 0.100, 0.200`

Rationale:

- `0` replays the isolated R4 anchor;
- `0.10` is the migration rate already used by the parent standard `equal_migrating` scenario;
- `0.05` is its half-rate;
- `0.025` resolves the low-connectivity interval between isolation and the half-rate;
- `0.20` tests a twofold increase above the parent standard rate while remaining well inside a convex mean-mixing update.

No rate was chosen from warning or diversity outcomes.

## Paired design

For each master seed and replicate:

1. reconstruct the high-function source once at the fixed recurrent-transition coordinate;
2. retain the same prepared full source and H1 anchor;
3. project that same source to the same equal fragmented patch geometry at each of the five migration rates;
4. use the same trajectory seed across migration levels;
5. apply the same deterioration schedule;
6. record only source/projection/baseline and realised functional-loss fields.

This produces a paired connectivity experiment rather than five independently tuned domains.

## Replication

Fresh master seeds:

`20290410, 20290411, 20290412, 20290413, 20290414`

Replicates per seed: `20`.

Thus:

- 100 independently prepared source replicates;
- five paired migration projections per prepared replicate;
- 500 migration-level trajectories total.

Minimum baseline-eligible count per seed and migration level: `10`.

## Event-regime classification

Retain the same high-rep condition rule:

- **R1-highrep persistence:** every seed-block trait-loss rate < 0.30;
- **R2-highrep rapid loss:** every seed-block trait-loss rate > 0.70;
- **R3-highrep seed heterogeneous:** otherwise, if support is sufficient;
- **R4-highrep:** every seed-block trait-loss rate lies in `[0.30,0.70]`;
- insufficient support is reported separately.

R4 means only that realised functional loss is reproducible and nondegenerate enough to be estimable. It is not evidence that a genetic warning succeeds.

## Permitted outputs

- source support/preparation;
- projection support;
- baseline realised high-trait presence;
- realised trait-loss occurrence/time;
- seed-block and pooled trait-loss rates;
- paired loss-status changes across migration levels;
- R1-R4 event-regime class.

## Forbidden outputs

- `H_alpha`, `H_gamma`, heterozygosity or F_ST;
- warning values or warning times;
- lead, lag, tie or lead time;
- any warning-based selection or stopping rule.

## Predeclared interpretation

Phase E asks whether the narrow R4 condition is stable, widened, shifted into persistence, shifted into rapid loss, or made seed-heterogeneous by genetic mixing.

No monotone sign is assumed in advance. Migration can homogenize allele frequencies, but the full model couples allele state to trait recruitment and interaction feedback, so realised functional-loss consequences are finite-model outcomes.

## Urban and island relevance

Phase E is the first direct condition test that maps to the connectivity contrast motivating the applications:

- urban patches can be spatially fragmented yet genetically connected by corridors, pollen movement, introductions or anthropogenic dispersal;
- island systems can be geographically isolated yet connected by stepping-stone gene flow.

The model result must still be described as an **allele-frequency mixing analogue**, not a direct estimate of pollen, seed, pollinator or demographic movement.

## Stop rule

After Phase E, do not tune migration rates to preserve or create R4.

The five-rate condition map is the result. Any later warning comparison must use a prospectively justified matched subset and fresh seeds, and only if the scientific question requires it.
