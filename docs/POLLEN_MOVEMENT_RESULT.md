# Pollen-movement result: process identity is exact, spatial kernel did not change the loss regime

## Result

Phase I completed under the prospectively fixed warning-blind design.

The opening rule was satisfied:

1. the fresh no-pollen control was `R4_highrep`;
2. the census-weighted regional pollen closure at `g=0.20` was snapshot-exact with legacy global allele mixing at `m=0.10` for **90/90** completed paired trajectories.

The predeclared regional-versus-ring pollen comparison yielded:

> **`kernel_same_regime`**

Both pollen kernels remained `R4_highrep`.

No pollen fraction, kernel, patch order, seed, deterioration parameter or R4 threshold was changed after observing the result.

## Exact process bridge

Under the declared diploid random-mating closure,

`p_off = (1-g/2) p_local + (g/2) p_pool`.

For a census-weighted regional pollen pool this is exactly the existing global allele-mixing operator at `m=g/2`.

With `g=0.20`, the exact comparator is `m=0.10`. The finite run confirmed the analytical identity at trajectory level: all 90 completed regional-pollen trajectories had snapshots exactly equal to their legacy `m=0.10` partners.

This is a narrow equivalence statement. It does **not** mean the legacy `migration_rate` is generally pollen dispersal. The equivalence requires this regional pollen pool, random-mating closure and paternal-only movement rule.

## Condition results

| condition | eligible | trait loss | pooled loss | regime |
|---|---:|---:|---:|---|
| no pollen | 90/100 | 46 | 0.511 | R4-highrep |
| regional pollen `g=0.20` | 90/100 | 45 | 0.500 | R4-highrep |
| legacy allele mixing `m=0.10` | 90/100 | 45 | 0.500 | R4-highrep |
| ring pollen `g=0.20` | 90/100 | 46 | 0.511 | R4-highrep |

Regional pollen seed-block rates were:

`0.412, 0.500, 0.579, 0.500, 0.500`.

Ring pollen seed-block rates were:

`0.471, 0.444, 0.632, 0.389, 0.611`.

All remained inside the predeclared R4 interval.

## Spatial kernel changed histories without changing regime

Regional versus ring pollen produced 90 comparable trajectories:

- 7 loss → no loss;
- 8 no loss → loss;
- 38 remained loss;
- 37 remained no loss.

Thus the pollen kernel changed **which trajectories failed** in both directions while leaving pooled incidence and the R4 classification nearly unchanged.

Likewise, no pollen versus regional pollen produced 10 loss→no-loss and 9 no-loss→loss switches, with pooled loss changing only `0.511 → 0.500`.

The bounded conclusion is:

> **At the tested pollen contribution, spatial pollen kernel reorganised stochastic functional-loss histories but did not change warning-evaluable regime classification.**

## Important cross-campaign boundary: the earlier `m=0.10` R3 is not portable across seed ensembles

Phase E previously classified legacy allele mixing `m=0.10` as `R3_highrep` at the same nominal eco-genetic anchor. Phase I's fresh `m=0.10` comparator is `R4_highrep`.

This is not a numerical contradiction because the campaigns use independent master-seed ensembles and fresh source reconstruction. It is scientifically important because it shows that the hard R3/R4 classification at a fixed parameter point can itself depend on the finite stochastic ensemble.

The earlier Phase-E result remains valid for its locked five-seed ensemble; Phase I does not overwrite it. Conversely, the Phase-I fresh R4 result prevents treating `m=0.10` as a portable connectivity boundary.

The stronger combined inference is:

> **The sign-free trajectory effect of connectivity is reproducible, but the exact categorical R4→R3 boundary at `m=0.10` is not yet shown to be stable across independent seed/source ensembles.**

This promotes **classification stability across independent ensembles** to the next methodological/scientific question before adding more movement mechanisms.

## What Phase I does and does not establish

Phase I establishes:

- a Type-T-style operator identity linking one regional pollen closure to `m=g/2` global mixing;
- finite trajectory-exact verification of that identity at `g=.20` / `m=.10`;
- a bounded negative spatial-kernel result at `g=.20`;
- bidirectional trajectory reshuffling under both movement comparisons;
- evidence that categorical loss-regime classification can be ensemble-sensitive.

Phase I does not establish:

- that pollen movement never changes regime;
- that regional and local pollen kernels are universally equivalent;
- a universal `g` threshold;
- seed/propagule, demographic or partner movement effects;
- a portable R3 boundary at `m=.10`.

## Provenance

- stacked PR: `#63`
- preregistered head: `3779464947e29fd85fdab106117e7ece296bbdf9`
- workflow run: `32454142670`
- artifact: `9436762723`
- artifact digest: `sha256:9a5ef1f86d040ecc9f12a92c2250cde2c6ec3fb6a24a0783f12cae2dbc3aab72`
- parent scientific commit: `dd8ee379d0d3518194c767d16402042525bc00dc`
- committed compact evidence: `artifacts/pollen_movement/phase_i_summary.json`

## Stop decision

**Phase I is closed.** Do not search additional `g` values or pollen kernels merely to obtain a regime switch.

Before opening seed/propagule or demographic movement, the next priority is a prospectively defined **cross-ensemble classification-stability audit** at fixed conditions. This directly tests whether an R4/R3 label itself is robust enough to serve as the gate for downstream warning validation.
