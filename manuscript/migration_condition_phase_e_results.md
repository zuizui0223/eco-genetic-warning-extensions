# Warning-blind migration-condition Phase E results

## Provenance

Phase E was prospectively declared only after the recurrent-transition `p_star` search closed. It holds the independently reproduced R4 anchor fixed and varies only the current simulator's allele-frequency mixing parameter.

- workflow run: `32376912392`
- artifact: `9409687687`
- artifact digest: `sha256:b2464d1b415fa62c6d8335c4ac20cb324ea0bc7bfa04aa6ab686da66c83f5b98`
- run head: `423253e567edb92185ae4fc672920e5de0a29ef7`
- calibration scope: `trait_loss_only`
- prepared sources: 100
- migration-level trajectories: 500
- paired design: the same prepared source and trajectory seed were used at every migration rate

No diversity, FST, warning-time, lead/lag or warning-performance field was available to the condition analysis.

## Fixed R4 anchor

All non-migration conditions were fixed at:

- `A_ref=1.0`;
- interaction `kappa=4.5`;
- `kappa_mu=0.35`;
- `p_star=0.35`;
- four equal patches at fixed total area;
- ramp 30 + hold 90, horizon 120;
- normalized barrier increase `0.30`.

The only experimental factor was `migration_rate`, interpreted strictly as allele-frequency mixing toward the population-weighted selected mean.

## Event-regime result

| migration rate | pooled trait-loss rate | seed-block rates | regime |
|---:|---:|---|---|
| 0.000 | 0.571 | 0.467, 0.611, 0.550, 0.667, 0.550 | **R4-highrep** |
| 0.025 | 0.549 | 0.533, 0.556, 0.450, 0.611, 0.600 | **R4-highrep** |
| 0.050 | 0.593 | 0.533, 0.667, 0.500, 0.667, 0.600 | **R4-highrep** |
| 0.100 | 0.626 | 0.667, 0.722, 0.600, 0.556, 0.600 | **R3-highrep** |
| 0.200 | 0.604 | 0.600, 0.722, 0.450, 0.667, 0.600 | **R3-highrep** |

Thus the independently reproduced R4 anchor remained warning-evaluable under low allele-frequency mixing (`m<=0.05`) but left the strict R4 class at the two larger tested rates because at least one independent seed block crossed the upper 0.70 boundary.

This is not a monotone pooled-risk result. Pooled trait-loss rate varied only from 0.549 to 0.626 across the five migration levels, whereas the reproducibility classification changed from R4 to R3.

## Paired trajectory switching

Relative to isolation (`m=0`), the same 91 baseline-comparable prepared sources showed loss-status changes in both directions:

| migration rate | loss→no loss | no loss→loss | total switches | switch fraction |
|---:|---:|---:|---:|---:|
| 0.025 | 5 | 3 | 8 | 0.088 |
| 0.050 | 5 | 7 | 12 | 0.132 |
| 0.100 | 8 | 13 | 21 | 0.231 |
| 0.200 | 11 | 14 | 25 | 0.275 |

The number of switched trajectories increased with migration rate, but both switch directions were always present. Under this closure, genetic mixing therefore does not act as a simple universal rescue or universal erosion operator for realised functional loss.

## Recovered condition conclusion

Phase E extends H3/H-MD-3a condition recovery:

> **Effective genetic connectivity can change whether a functional-loss regime is reproducible enough to be warning-evaluable even when pooled functional-loss probability changes only modestly.**

At the tested anchor, low migration preserved R4, whereas stronger allele mixing produced seed-heterogeneous R3 regimes. The key effect is therefore on the event-generating regime and trajectory identity, not a simple monotone shift in average loss risk.

This is a finite Type S result for the declared life cycle. It does not show that demographic movement, pollinator movement, seed dispersal or recolonisation has the same effect.

## Relation to parent migration theory

The parent migration layer shows analytically that allele-frequency mixing contracts patch deviations from a mean and that homogenisation can coexist with separately certified rescue. Phase E adds the finite full-life-cycle observation that this mixing can reassign which trajectories lose realised function and can alter R4/R3 evaluability.

The theorem and finite result are complementary:

```text
migration theorem:
  mixing changes spatial allele-frequency structure

Phase E:
  under one fixed eco-genetic R4 anchor, that mixing changes event-regime reproducibility
```

Neither implies a universal beneficial or harmful sign of connectivity.

## Urban and island interpretation

Phase E gives a concrete empirical translation for the urban/island program.

- **Urban systems:** corridors, repeated introductions or pollen-mediated gene flow can maintain genetic connection without guaranteeing a uniform functional response across patches or years. The prediction is not simply "more connectivity rescues function"; connectivity may change which local populations cross the functional-loss boundary.
- **Island systems:** stepping-stone gene flow can similarly alter local genetic states without mapping monotonically to current mutualist-dependent function. Archipelagos should therefore be classified by effective connectivity and interaction support rather than geographic distance alone.

The empirical analogue should measure realised pollen/gene flow and ecological function separately. `migration_rate` is not itself an estimate of pollen, seed or individual movement.

## Stop rule

The Phase-E migration grid is closed. Do not tune additional migration rates merely to enlarge R4 or locate a prettier threshold. The next scientific step is to integrate this recovered connectivity boundary into the hypothesis ledger and decide whether another ecological condition axis is necessary before the manuscript rewrite.
