# Artifact and workflow index

## Core evidence provenance

| Campaign | Evidence | Workflow run / artifact |
|---|---|---|
| Source reconstruction and projection | 135 batches, 3,375 attempts | runs `29177214259`, `29186610167`, `29188592519`, `29188748077`, `29190149319`, `29190149344` |
| Source-feasibility publication outputs | coordinate CSV, summary JSON, source-feasibility and warning figures | run `29422431944`, artifact `8345805712`, digest `sha256:fc9b9a410908cf4446b65d5caee8de8d731734f0fae47e69c94cddc830a814e9` |
| Warning-blind trait-loss calibration | 810 batches, 20,250 attempts | Wave 001 plus bulk remaining completion locks |
| Protocol 002 selection | 648 complete candidates, zero eligible | selection and no-domain audit artifacts |
| Trait-loss-regime publication outputs | coordinate regime CSV and regime map | run `29399936061`, artifact `8336631530`, digest `sha256:3c7f63b5bc054c37012bb448ad1dc5e9bf45a4ec79737520390b576079ccc8f7` |
| Protocol 003 validation | 200 fresh-seed trajectories | run `29417632137` |
| Symmetric-bridge validation | 100 attempts | artifact `8343958766`, digest `sha256:c1b42fc9e6ac912a44667ef4cee02090fab37d50fc3a9928c46ae728c0610f58` |
| Directional-transition validation | 100 attempts | artifact `8343922879`, digest `sha256:0a994bea874fc9c47544169cd31bbc317c88690dfe1b6fa7548516e35fd7bca8` |

Protocol and stage identifiers remain in workflow metadata and Methods because they are necessary for provenance. Biological Results and figure titles use ecological findings rather than implementation stages.

## Main manuscript tables

- `manuscript/tables/stage1_coordinate_summary.csv`
- `manuscript/tables/stage2_coordinate_regimes.csv`
- `manuscript/tables/stage3_endpoint_summary.csv`

The retained filenames preserve machine-readable provenance and are not intended as Results-section labels.

## Main figures

1. **Eco-genetic closure and the emergence of genetic warning.** Conceptual synthesis linking fragmentation, interaction state, realised functional trait, local demography, genetic state, warning, and functional-trait loss. Closure modifiers include recurrent state-transition direction, deterioration, calibration, baseline eligibility, and censoring.
2. **High-trait source feasibility across recurrent-transition coordinates.**
3. **Trait-loss regimes across recurrent-transition coordinates.**
4. **Rapid-loss, persistence, and seed-heterogeneous candidate composition.**
5. **Warning lead, tie, and lag ordering in two independently calibrated closures.**
6. **Usable positive lead time in two independently calibrated closures.**

## Figure-caption boundaries

Every numerical figure caption must state that results are finite Type S evidence for the declared closure. Captions must also distinguish trajectory counts from correlated endpoint comparisons and retain censored, baseline-ineligible, tie, and lag outcomes where applicable. Figure 1 is explicitly conceptual and does not claim a universal causal theorem.

## Evidence rules

- Parent trajectories remain parent evidence and are not pooled with extension trajectories.
- Protocol 002 remains closed with 15/15 `no_domain_selected`.
- Protocol 003 is a separately declared protocol, not a retrospective modification.
- Seed families are disjoint across bracket, calibration, confirmation, and validation.
- Endpoint comparisons from the same trajectory are correlated.
- `p_mu*` is an effective recurrent-transition equilibrium, not an estimated biological mutation rate.
