# Artifact and workflow index

## Core evidence

| Stage | Evidence | Workflow run / artifact |
|---|---|---|
| Stage I | 135 batches, 3,375 attempts | runs `29177214259`, `29186610167`, `29188592519`, `29188748077`, `29190149319`, `29190149344` |
| Stage I publication outputs | coordinate CSV, summary JSON, Figures 2, 5, 6 | run `29422431944`, artifact `8345805712`, digest `sha256:fc9b9a410908cf4446b65d5caee8de8d731734f0fae47e69c94cddc830a814e9` |
| Stage II | 810 batches, 20,250 attempts | Wave 001 plus bulk remaining completion locks |
| Stage II selection | 648 complete candidates, zero eligible | selection and no-domain audit artifacts |
| Stage II publication outputs | coordinate regime CSV and Figure 3 | run `29399936061`, artifact `8336631530`, digest `sha256:3c7f63b5bc054c37012bb448ad1dc5e9bf45a4ec79737520390b576079ccc8f7` |
| Stage III validation | 200 fresh-seed trajectories | run `29417632137` |
| Stage III symmetric artifact | 100 attempts | artifact `8343958766`, digest `sha256:c1b42fc9e6ac912a44667ef4cee02090fab37d50fc3a9928c46ae728c0610f58` |
| Stage III directional artifact | 100 attempts | artifact `8343922879`, digest `sha256:0a994bea874fc9c47544169cd31bbc317c88690dfe1b6fa7548516e35fd7bca8` |

## Main manuscript tables

- `manuscript/tables/stage1_coordinate_summary.csv`
- `manuscript/tables/stage2_coordinate_regimes.csv`
- `manuscript/tables/stage3_endpoint_summary.csv`

## Main figures

1. Mutation-coordinate mechanism and transition rates.
2. Stage I source/projection feasibility map.
3. Stage II coordinate regime map.
4. Stage II seed-block eligibility composition.
5. Stage III lead/tie/lag ordering.
6. Stage III median positive lead time.

## Evidence rules

- Parent trajectories are context, not extension evidence.
- Protocol 002 remains closed with 15/15 `no_domain_selected`.
- Protocol 003 seed families are disjoint across bracket, calibration, confirmation, and validation.
- Endpoint comparisons from the same trajectory are correlated.
- Every numerical figure caption must identify the evidence as finite Type S evidence for the declared closure.
