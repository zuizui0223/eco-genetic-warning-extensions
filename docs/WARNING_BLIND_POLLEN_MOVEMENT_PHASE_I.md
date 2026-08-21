# Warning-blind pollen-movement Phase I

## Question

The current simulator's `migration_rate` mixes allele frequencies. It does not move pollen, seed, individuals or interaction partners. Phase I therefore introduces a specific biological movement process instead of relabelling that parameter.

The question is:

> **At a fixed paternal pollen-pool contribution, does the spatial kernel of pollen-mediated gene flow change functional-loss regime reproducibility?**

## Why pollen first

Pollen-mediated gene flow is the cleanest first biological-movement closure because it changes offspring allele frequencies without moving census individuals or realised trait-bin abundance.

Under the declared diploid random-mating closure:

- maternal allele frequency is the local selected frequency `p_local`;
- paternal pollen is `(1-g) p_local + g p_pool`;
- offspring allele frequency is the mean of maternal and paternal gene copies.

Therefore

`p_off = (1-g/2) p_local + (g/2) p_pool`.

For a census-weighted regional pollen pool, this is **exactly** the current global allele-mixing operator with `m=g/2`. This identity is used as an implementation control, not as a claim that legacy `migration_rate` is generally pollen dispersal.

## Fixed design

Before any Phase-I outcome is generated:

- `kappa_mu=0.35`, `p_star=0.35`;
- `A_ref=1.0`, interaction `kappa=4.5`;
- four equal focal patches at fixed total area;
- 30-generation deterioration ramp + 90-generation hold;
- normalized barrier increase `0.30`;
- five fresh master seeds × 20 replicates;
- pollen-pool fraction `g=0.20`;
- exact global-mixing comparator `m=g/2=0.10`.

`g=0.20` is fixed because its exact global equivalent is the previously studied `m=0.10` boundary level. It is not tuned to the new outcome.

## Four paired conditions

1. `no_pollen_control` — no pollen-pool contribution, no legacy mixing;
2. `regional_pollen_pool_g020` — 20% of paternal contribution follows the census-weighted regional pollen pool;
3. `legacy_allele_mixing_m010` — the existing allele-mixing operator at `m=0.10`, used only as an exact implementation comparator;
4. `ring_pollen_pool_g020` — the same `g=0.20`, but the paternal pool for each patch is restricted to its two circular nearest neighbours and census-weighted within that donor set.

The same prepared source and trajectory seed are paired across all four conditions.

## Opening rule

Interpret the spatial-kernel comparison only if:

1. fresh `no_pollen_control` has sufficient support and is `R4_highrep`;
2. every completed `regional_pollen_pool_g020` trajectory has snapshots exactly equal to its paired `legacy_allele_mixing_m010` trajectory.

If either condition fails, record `not_opened`. Do not change `g`, the kernel, patch ordering, seeds, deterioration or R4 thresholds.

## Main comparison

If opening succeeds, compare the regional and ring pollen kernels once at the same `g=0.20`.

- same R1/R2/R3/R4 classification → `kernel_same_regime`;
- different classification → `kernel_changed_regime`.

Paired loss-status switches are retained as a trajectory diagnostic.

## Blinding

Phase-I condition classification may inspect only:

- source preparation and projection;
- declared movement operator and kernel;
- baseline realised high-trait presence;
- realised functional-trait loss time/status;
- implementation-equivalence diagnostics.

Genetic diversity, warning times, lead/lag ordering and lead time remain unavailable.

## Stop rule

After the first complete run, do not tune:

- pollen-pool fraction `g`;
- regional or ring kernel;
- patch ordering;
- seeds;
- deterioration schedule;
- R4 thresholds.

A negative kernel result closes this fixed movement comparison. It does not authorize testing more `g` values until a regime difference appears.

## Interpretation ceiling

Phase I represents **pollen-mediated paternal gene contribution only**. It does not move:

- census individuals;
- seeds or propagules;
- realised trait bins;
- interaction partners.

The exact `g↔m/2` identity applies only to the census-weighted regional pollen pool under this diploid random-mating closure. It is a mechanistic bridge that defines when legacy allele mixing can mimic this one pollen process; it is not a general biological interpretation of `migration_rate`.
