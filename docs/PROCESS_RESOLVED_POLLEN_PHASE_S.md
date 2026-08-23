# Phase S — pollen-only gametic gene flow

## Question

> Does the high-precision Phase-M heterogeneity at legacy allele-frequency mixing `m=0.10` reproduce when gene flow is represented as external pollen contributing only to the paternal gamete pool?

Phase R showed that the effect did not port to whole-individual dispersal. Phase S asks whether it ports to a biological movement process that is mechanistically closer to allele-frequency mixing while leaving census and realised trait-bin abundance local.

## Fixed comparison

Same Phase-E/M anchor, master seeds `20290410–20290414`, 100 attempted replicates per seed and deterioration schedule:

1. no connectivity;
2. legacy allele-only `m=.10`;
3. pollen-only `g=.20`.

No other pollen fraction is tested.

## Why `g=.20`

The declared closure is biparental: local maternal and paternal gamete pools each contribute half of expected zygotic allele frequency. If 20% of paternal slots are supplied by external pollen, the maximum expected external genomic contribution is therefore about 10% before donor weighting. This gives a mechanistically derived nominal comparison with legacy `m=.10`.

It is **not** calibrated equivalence. Legacy `m` mixes post-selection allele frequencies toward a weighted metapopulation mean; pollen `g` changes only paternal origin and excludes the destination from external donors.

## Pollen operator

After local population and trait recruitment:

- each recruit contributes one paternal slot;
- each paternal slot is external with probability `g`;
- external donor patches are sampled proportional to their locally recruited census, excluding the destination patch;
- maternal allele frequency remains local post-selection frequency;
- paternal allele frequency is computed from realised integer donor-origin counts;
- expected zygotic frequency is one-half maternal plus one-half paternal;
- recurrent allele-state transition is applied next, followed by the parent's finite drift draw.

Census abundance and trait-bin abundance do not move. Pollen-origin sampling uses a separate RNG.

## Opening rule

Interpretation is blocked unless:

- `g=0` exactly reproduces the pinned finite-bin parent life cycle;
- all original first-20 Phase-E no-connectivity / `m=.10` prefixes reproduce;
- all five full 100-attempt Phase-M no-connectivity / `m=.10` block counts reproduce exactly;
- pollen flow leaves paired baseline eligibility identical to no connectivity.

## Estimands

Primary: pooled loss and equal-rate heterogeneity across five pollen blocks.

Secondary: exact paired McNemar pollen versus no connectivity and pollen versus allele-only `m=.10`, plus bidirectional trajectory switches and realised pollen immigration fraction.

Historical R1–R4 labels remain screen descriptors only.

## Representation boundary

The parent does not explicitly model flowers, mating pairs, pollen limitation, selfing rate, self-incompatibility, pollen carryover, pollinator behaviour or genotype-by-trait identities. Phase S is therefore a **paternal gamete-origin gene-flow closure**, not a complete plant mating system and not pollinator movement.

## Stop rule

Run `g=.20` once with the locked seeds. Do not add pollen fractions, donor kernels, selfing parameters, replacement seeds or more precision merely to reproduce or eliminate the legacy `m=.10` heterogeneity.
