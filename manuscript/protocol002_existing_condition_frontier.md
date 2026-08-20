# Existing Protocol 002 condition frontier

## Purpose

This note extracts the condition structure already present in the locked Protocol 002 Stage II publication artifact before any new simulation is considered.

Source artifact:

- workflow run `29399936061`;
- artifact `8336631530`;
- digest `sha256:3c7f63b5bc054c37012bb448ad1dc5e9bf45a4ec79737520390b576079ccc8f7`;
- file `stage2_coordinate_regimes.csv`.

The artifact is trait-loss-only. No warning or diversity field is used below.

## Coordinate-level regime structure

| kappa_mu | p_star | complete candidates | rapid | heterogeneous | persistence | dominant regime | closest pooled loss | seed blocks inside strict band | closest max distance to band |
|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|
| 0.05 | 0.10 | 24 | 24 | 0 | 0 | rapid-loss | 1.000 | 0 | 0.30 |
| 0.05 | 0.25 | 48 | 48 | 0 | 0 | rapid-loss | 1.000 | 0 | 0.30 |
| 0.05 | 0.50 | 36 | 36 | 0 | 0 | rapid-loss | 1.000 | 0 | 0.30 |
| 0.05 | 0.75 | 54 | 51 | 3 | 0 | rapid-loss | 0.889 | 1 | 0.30 |
| 0.05 | 0.90 | 54 | 19 | 35 | 0 | seed-heterogeneous | 0.458 | 4 | **0.05** |
| 0.20 | 0.10 | 30 | 30 | 0 | 0 | rapid-loss | 1.000 | 0 | 0.30 |
| 0.20 | 0.25 | 42 | 42 | 0 | 0 | rapid-loss | 1.000 | 0 | 0.30 |
| 0.20 | 0.50 | 42 | 0 | 40 | 2 | seed-heterogeneous | 0.524 | 2 | **0.10** |
| 0.20 | 0.75 | 54 | 0 | 4 | 50 | persistence | 0.056 | 1 | 0.30 |
| 0.20 | 0.90 | 42 | 0 | 0 | 42 | persistence | 0.000 | 0 | 0.30 |
| 0.35 | 0.10 | 30 | 30 | 0 | 0 | rapid-loss | 1.000 | 0 | 0.30 |
| 0.35 | 0.25 | 42 | 42 | 0 | 0 | rapid-loss | 0.957 | 0 | 0.30 |
| 0.35 | 0.50 | 48 | 0 | 2 | 46 | persistence | 0.130 | 0 | 0.30 |
| 0.35 | 0.75 | 54 | 0 | 0 | 54 | persistence | 0.000 | 0 | 0.30 |
| 0.35 | 0.90 | 48 | 0 | 0 | 48 | persistence | 0.000 | 0 | 0.30 |

The closest candidate at `(kappa_mu=0.05, p_star=0.90)` had seed-block trait-loss frequencies `0.60, 0.40, 0.25, 0.60, 0.40`: four of five blocks were already inside the strict `[0.30, 0.70]` band and the remaining block missed it by only `0.05`.

The closest candidate at `(0.20, 0.50)` had pooled loss `0.524`, but seed-block rates `0.20, 0.75, 0.333, 0.80, 0.50`, showing that an apparently intermediate pooled rate can still be strongly seed-heterogeneous.

## First recovered condition pattern

Increasing `p_star` moves the common-grid system from rapid loss toward persistence, but the location of that transition depends strongly on `kappa_mu`.

```text
kappa_mu = 0.05:
  rapid through p_star=0.75
  heterogeneous by p_star=0.90

kappa_mu = 0.20:
  rapid through p_star=0.25
  heterogeneous near p_star=0.50
  persistence by p_star=0.75

kappa_mu = 0.35:
  rapid through p_star=0.25
  persistence by p_star=0.50
```

Thus the transition frontier shifts toward lower `p_star` as recurrent-transition strength increases. The current 15-coordinate grid samples this frontier too coarsely to determine whether a narrow reproducible intermediate-risk region exists between rapid loss and persistence.

## Immediate refinement priority

Do **not** expand all parameters uniformly. First refine `p_star` only inside the observed rapid-to-persistence frontier for each `kappa_mu`, while retaining warning-blind trait-loss classification.

Priority intervals suggested by the locked artifact are:

- `kappa_mu=0.05`: refine between `p_star=0.75` and the upper boundary near/above `0.90`;
- `kappa_mu=0.20`: refine the broad `0.25–0.75` transition region around the existing heterogeneous `0.50` coordinate;
- `kappa_mu=0.35`: refine between `0.25` and `0.50`, where the grid currently jumps directly from rapid loss to persistence.

The exact refined grid should be declared only after the new warning-blind candidate-level condition-map artifact reports which ecological/schedule axes (`A_ref`, interaction `kappa`, horizon, barrier increase) consistently move candidates toward or away from the intermediate-risk band.

## Scientific interpretation

This already changes the next research question. The issue is not simply whether warning succeeds at a chosen coordinate. It is whether an **intermediate reproducible event regime forms a narrow frontier between rapid loss and persistence**, and how ecological support, deterioration and recurrent state turnover shift that frontier.

If such a region is recovered warning-blind and independently confirmed, H-MD-3b can be tested cleanly inside it with fresh seeds. If the frontier remains seed-heterogeneous after refinement, that heterogeneity itself becomes a recovered condition boundary rather than an unsuccessful warning test.
