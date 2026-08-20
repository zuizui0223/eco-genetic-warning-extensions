# Protocol 002 warning-blind condition-map results

## Provenance

This is a secondary reaggregation of already locked Protocol 002 Stage II trait-loss batches. It is not a new simulation and does not inspect warning or diversity outcomes.

- workflow: `Protocol 002 warning-blind condition map`
- run: `32346697621`
- artifact: `9398407271`
- artifact digest: `sha256:5d61e71f6febf1c65304716958b329b329612359f1d170b4747532a124b5a8a2`
- input batches: 810
- complete five-seed candidates: 648
- incomplete candidates: 162
- warning fields inspected: false
- diversity fields inspected: false
- selection rule changed: false

Global regimes reproduce the locked Stage II result:

- rapid loss: 322;
- persistence: 242;
- seed heterogeneous: 84;
- warning evaluable under the strict all-seed `[0.30,0.70]` gate: 0.

## 1. Recurrent-transition coordinates dominate the matched loss-rate shifts

For every adjacent factor contrast, candidates were paired only when all other declared factors were identical and both candidate records were complete. The outcome below is directional change in **pooled trait-loss rate**; no warning variable is involved.

### `p_star`

| contrast | matched pairs | mean delta loss | median delta loss | lower loss at higher p_star | higher loss at higher p_star | unchanged |
|---|---:|---:|---:|---:|---:|---:|
| 0.10 -> 0.25 | 78 | 0.000 | 0.000 | 0 | **0** | 78 |
| 0.25 -> 0.50 | 108 | **-0.527** | **-0.600** | 72 | **0** | 36 |
| 0.50 -> 0.75 | 126 | **-0.162** | **-0.0476** | 80 | **0** | 46 |
| 0.75 -> 0.90 | 144 | **-0.107** | 0.000 | 58 | **0** | 86 |

Within the matched complete-candidate subset, increasing `p_star` never increased pooled trait-loss rate. The strongest change occurred across `0.25 -> 0.50`.

### `kappa_mu`

| contrast | matched pairs | mean delta loss | median delta loss | lower loss at higher kappa_mu | higher loss at higher kappa_mu | unchanged |
|---|---:|---:|---:|---:|---:|---:|
| 0.05 -> 0.20 | 180 | **-0.532** | **-0.595** | 120 | **0** | 60 |
| 0.20 -> 0.35 | 204 | **-0.0767** | 0.000 | 49 | **0** | 155 |

Within the matched complete-candidate subset, increasing `kappa_mu` also never increased pooled trait-loss rate.

These are finite matched patterns inside the declared grid. They do not prove a universal monotone law and do not include effects on source feasibility or candidate completeness.

## 2. Deterioration duration matters more than deterioration magnitude in the tested grid

### Horizon

Increasing the calibrated horizon from 120 to 240 generations gave:

- 324 matched pairs;
- mean delta pooled loss `+0.0520`;
- 71 increases;
- 0 decreases;
- 253 unchanged.

Thus a longer observation/deterioration horizon could expose additional functional loss, but most candidate pairs remained unchanged.

### Normalised barrier increase

Barrier changes were weak and mixed inside the tested `0.15, 0.30, 0.45` range:

- `0.15 -> 0.30`: 216 pairs, mean delta `-0.00264`, 23 decreases / 14 increases / 179 unchanged;
- `0.30 -> 0.45`: 216 pairs, mean delta `+0.00096`, 14 decreases / 11 increases / 191 unchanged.

The current data therefore do not support widening barrier magnitude as the first condition-refinement axis.

## 3. `A_ref` and interaction-feedback `kappa` are not the first refinement axes for Stage II loss among complete candidates

Matched adjacent contrasts had median delta zero and mixed directions:

- `A_ref 0.8 -> 1.0`: 198 pairs, 31 decreases / 16 increases / 151 unchanged;
- `A_ref 1.0 -> 1.2`: 174 pairs, 18 decreases / 37 increases / 119 unchanged;
- interaction `kappa 3.0 -> 4.5`: 138 pairs, 37 decreases / 13 increases / 88 unchanged;
- interaction `kappa 4.5 -> 6.0`: 234 pairs, 20 decreases / 33 increases / 181 unchanged.

This does **not** imply that these ecological parameters are unimportant: they also affect source preparation and which candidates become complete. It means only that, conditional on the matched complete Stage II subset, they moved pooled trait-loss rate less consistently than the recurrent-transition coordinates.

## 4. The closest strict-gate candidates cluster at `(kappa_mu=0.05, p_star=0.90)` and short horizon

The two closest candidates to the strict all-seed intermediate-risk band both had `kappa_mu=0.05`, `p_star=0.90`, `A_ref=0.8`, horizon 120:

1. `kappa=4.5`, barrier increase `0.45`: pooled loss `0.458`; seed-block rates `0.60, 0.40, 0.25, 0.60, 0.40`; four of five blocks inside the strict band; total/max distance to band `0.05`.
2. `kappa=3.0`, barrier increase `0.15`: pooled loss `0.524`; seed-block rates `0.50, 0.50, 0.40, 0.50, 0.75`; four of five blocks inside; total/max distance `0.05`.

The next several closest candidates were also at `kappa_mu=0.05`, `p_star=0.90`, horizon 120 across multiple interaction `kappa` and barrier settings.

This concentration argues that the first refinement should resolve the **recurrent-transition frontier**, not globally widen every ecological/deterioration parameter.

## 5. Condition-frontier interpretation

Combining the new candidate-level matched effects with the previously published 15-coordinate regime map gives a coherent finite pattern:

```text
higher p_star / stronger recurrent transition
        -> lower realised trait-loss frequency among matched complete candidates
        -> rapid-loss regime gives way to heterogeneous boundary cells
        -> persistence dominates beyond the boundary
```

The frontier shifts toward lower `p_star` as `kappa_mu` increases:

- `kappa_mu=0.05`: rapid through `p_star=0.75`, heterogeneous at `0.90`;
- `kappa_mu=0.20`: rapid at `0.25`, heterogeneous at `0.50`, persistence at `0.75`;
- `kappa_mu=0.35`: rapid at `0.25`, persistence at `0.50`.

The existing grid is therefore too coarse precisely where an R4 warning-evaluable regime would be expected if such a region is present: along the narrow rapid-to-persistence frontier.

## 6. Next condition search

The next campaign should remain warning-blind and should **not** uniformly enlarge the old grid.

Priority order:

1. refine `p_star` between the observed rapid and persistence/heterogeneous coordinates within each fixed `kappa_mu` row;
2. retain the existing ecological/support and deterioration settings initially so the recurrent-transition frontier can be identified cleanly;
3. use the short horizon as the primary refinement layer, with longer horizon as a secondary axis because 120 -> 240 only shifts loss upward or leaves it unchanged;
4. do not prioritize wider barrier increments because the existing matched effect is nearly zero/mixed;
5. once candidate frontier cells are identified, increase replication with fresh seeds and confirm the event regime before any warning/diversity endpoint is calculated.

If multiple adjacent `p_star` values at the same `kappa_mu` and identical non-transition conditions produce reproducible intermediate-risk loss, the study can finally instantiate a clean direction-only H-MD-3b comparison. If refinement remains seed-heterogeneous, the width and stochasticity of that boundary become the recovered scientific result.
