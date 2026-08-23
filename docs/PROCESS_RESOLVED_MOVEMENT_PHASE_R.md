# Phase R — process-resolved biological movement

## Question

> Does the one high-precision Phase-M block-heterogeneity result at legacy allele-frequency mixing `m=0.10` reproduce when connectivity is represented instead by actual movement of whole individuals?

This is an **operator-portability** test. It does not ask whether more connectivity is good or bad and it does not search for a movement threshold.

## Why a new closure is required

The pinned parent `migration_rate` acts only on post-selection allele frequencies. Population abundance and realised trait-bin abundance remain local. Therefore Phase M cannot be interpreted as demographic, seed, pollen or partner movement.

Phase R adds a separately declared post-recruitment whole-individual movement operator while leaving the pinned parent source-preparation and local life-cycle rules unchanged.

## Fixed comparison

All three conditions share the exact Phase-E/M anchor, five historical master seeds `20290410–20290414`, 100 attempted replicates per seed, deterioration schedule and prepared source:

1. `no_connectivity`: legacy `migration_rate=0`, no process movement;
2. `allele_only_m010`: legacy allele-frequency mixing `m=0.10`;
3. `individual_dispersal_d010`: legacy migration disabled and per-individual post-recruitment emigration probability `d=0.10`.

`d=0.10` is a nominal stress-test match to the already load-bearing `m=0.10` comparator. **No quantitative equivalence of movement or gene flow is claimed.**

## Movement operator

For each generation after local population and trait recruitment:

- each patch retains at least one recruit;
- each remaining recruit emigrates independently with probability `d`;
- emigrants choose uniformly among the other three patches;
- the realised integer source→destination flux moves census abundance and realised trait-bin counts exactly;
- the receiving genetic pool is the resident plus migrant census weighted by each source patch's post-selection high-allele frequency;
- the recurrent-state transform `p -> kappa_mu*p_star + (1-kappa_mu)*p` is applied after movement-derived genetic mixing and before finite drift.

A separate movement RNG prevents the extra movement draws from shifting the parent's local trait-recruitment/drift RNG stream solely because the movement mechanism exists.

## Representation boundary

The parent simulator tracks allele frequency and trait-bin abundance separately and does not store joint genotype-by-trait identities. Phase R can therefore move **trait-bin individuals exactly** and move their **source genetic composition in expectation**, but it cannot preserve or estimate migrant genotype–trait covariance. The result is process-resolved demographic/trait dispersal relative to the parent, not a full individual-based genome/trait pedigree model.

It is also not pollen-only movement, seed-only movement, pollinator movement or partner movement. Those require separate biological operators.

## Opening rule

Scientific interpretation is blocked unless all of the following pass:

- `d=0` reproduces the pinned parent finite-bin life cycle exactly in an integration contract;
- all ten original first-20 Phase-E `no connectivity` / `m=.10` eligible-loss prefixes are reproduced;
- the five full 100-attempt Phase-M block counts are reproduced exactly for both legacy comparator conditions;
- process-resolved movement has the same baseline eligibility as paired no-connectivity trajectories, because movement starts only after baseline.

## Estimands

Primary:

- pooled functional-loss incidence under `d=.10`;
- Pearson equal-rate diagnostic across the five high-precision blocks.

Secondary:

- exact paired McNemar process movement vs no connectivity;
- exact paired McNemar process movement vs allele-only `m=.10`;
- bidirectional trajectory-status switches;
- realised movement fraction as an operator diagnostic.

Historical R1–R4 screen labels are retained only as protocol descriptors.

## Decision

- process `d=.10` has equal-rate `p < .05`: the high-precision block-dependence phenomenon is not unique to allele-only mixing under this nominal movement comparison;
- process `d=.10` has equal-rate `p >= .05`: the Phase-M `m=.10` heterogeneity does not port to this first process-resolved whole-individual movement closure.

Marginal-risk effects are interpreted separately from the heterogeneity decision.

## Stop rule

Run the three declared conditions once. Do **not** add movement rates, tune destination kernels, replace seeds, change the observation band or increase precision merely to reproduce or eliminate the Phase-M result. A negative result closes this first movement closure and motivates a new biologically specified mechanism rather than a sweep.
