# Artifact and workflow index

Protocol and phase identifiers are retained here because they are necessary for provenance. Biological Results and figure titles use condition-first ecological language.

## Core evidence provenance

| Campaign | Evidence | Workflow run / artifact |
|---|---|---|
| Inherited H1/H3 chain | paired one-large versus equal-isolated outcomes | parent run `28456092898`, artifact `7987193632`, digest `sha256:b74b604f3233fa6086e2afa39cd780fa375aac4b1abd8c63e6f5ed8b3a467d2c` |
| Fresh H3 fragmentation gradient | 1–16 equal isolated patches, 1,200 attempted / 1,037 prepared sources | parent run `31937210601`, artifact `9261157020`, digest `sha256:424031d0f6bcdf75c13e03deb35324f0d3f6fd46f58ff7b34961bbd00556537c` |
| Inherited relative-warning benchmark | trait-loss-only calibration and fresh-seed H2-R validation | parent calibration run `28496735824`; validation run `28500796310` |
| Common source reconstruction | 3,375 attempts over 15 recurrent-transition coordinates | runs `29177214259`, `29186610167`, `29188592519`, `29188748077`, `29190149319`, `29190149344` |
| Source-feasibility publication output | coordinate CSV + summary JSON | run `29422431944`, artifact `8345805712`, digest `sha256:fc9b9a410908cf4446b65d5caee8de8d731734f0fae47e69c94cddc830a814e9` |
| Common warning-blind loss calibration | 20,250 attempts; 648 complete candidates; 15/15 `no_domain_selected` | locked Protocol 002 Stage II audit/selection artifacts |
| Loss-regime publication output | coordinate regime CSV + map inputs | run `29399936061`, artifact `8336631530`, digest `sha256:3c7f63b5bc054c37012bb448ad1dc5e9bf45a4ec79737520390b576079ccc8f7` |
| R4 prospective recovery | high-rep warning-blind recovery/replay of `p_star=0.35` | committed Phase C/D summaries under `artifacts/frontier_refinement/` |
| Genetic-connectivity condition | paired `m=0–0.20` test at recovered R4 anchor | run `32376912392`, artifact `9409687687`; committed `artifacts/migration_condition/phase_e_summary.json` |
| Aggregate interaction-support condition | predeclared `kappa=3.0,4.5,6.0`; 100 attempts/level; all three R4-highrep | run `32441549848`, artifact `9432854668`, digest `sha256:bb221af16a9b6557280610e90807fdfe058dccbafd7d0183e38d4525ecef2c16`; committed `artifacts/interaction_support/phase_f_summary.json` |
| Protocol 003 validation | 200 attempted fresh-seed trajectories across separately calibrated domains | run `29417632137` |
| Recalibrated symmetric domain | 100 attempts; `A_ref=0.8`, `kappa=6.0`, `kappa_mu=0.20`, `p_star=0.50`, ramp 30 + hold 210, increase 0.20 | artifact `8343958766`, digest `sha256:c1b42fc9e6ac912a44667ef4cee02090fab37d50fc3a9928c46ae728c0610f58` |
| Directional calibrated domain | 100 attempts; `A_ref=1.0`, `kappa=4.5`, `kappa_mu=0.05`, `p_star=0.90`, ramp 30 + hold 90, increase 0.10 | artifact `8343922879`, digest `sha256:0a994bea874fc9c47544169cd31bbc317c88690dfe1b6fa7548516e35fd7bca8` |
| Stage III secondary audit | conventional medians, normalized timing, trajectory bootstrap, cumulative incidence, direct timing differences | regenerated from the immutable Stage III artifacts during publication builds |

## Condition-recovery machine-readable summaries

- `artifacts/frontier_refinement/phase_b_summary.json` — low-rep pooled frontier.
- `artifacts/frontier_refinement/phase_c_summary.json` — first high-rep R4 recovery.
- `artifacts/frontier_refinement/phase_d_summary.json` — independent replay plus immediate neighbours.
- `artifacts/migration_condition/phase_e_summary.json` — connectivity condition and paired status switches.
- `artifacts/interaction_support/phase_f_summary.json` — aggregate interaction-support result with exact run/artifact provenance.

The Phase-F committed summary records:

| interaction kappa | source/baseline eligible | pooled functional loss | regime |
|---:|---:|---:|---|
| 3.0 | 77/100 | 0.468 | R4-highrep |
| 4.5 | 94/100 | 0.521 | R4-highrep |
| 6.0 | 87/100 | 0.552 | R4-highrep |

All five seed-block loss rates at all three levels remained within `[0.30,0.70]`.

## Submission-bundle tables

- `manuscript/tables/inherited_h3_effect_summary.csv` — locked parent H3 paired effects.
- `h3_fragmentation_gradient_records.csv` in the checksummed bundle — 9,600 repeated-measures rows from 1,200 attempted sources across eight patch counts.
- `h3_fragmentation_gradient_cell_summary.csv` / `h3_fragmentation_gradient_pooled_summary.csv` — gradient summaries.
- `stage1_coordinate_summary.csv` — common-grid source feasibility from artifact `8345805712`.
- `stage2_coordinate_regimes.csv` — strict common-grid loss-regime map from artifact `8336631530`.
- `stage3_trajectory_endpoint_records.csv` — full 100-attempt denominator for every Stage III endpoint.
- `stage3_review_audit.json` — trajectory-level secondary audit.
- `manuscript/tables/stage3_review_summary.csv` and `stage3_between_domain_differences.csv` — committed publication summaries regenerated and byte-compared during builds.

Historical Stage III source artifacts are not overwritten. Conventional-median correction and direct timing contrasts are explicitly secondary analyses of immutable trajectories.

## Publication display rule

The current six-display limit is controlled by `manuscript/display_allocation.md`. The final condition-first layout should not create a seventh main display merely because Phase F closed. Phase E and Phase F are both C2 condition-axis results and should be integrated in the same condition display when figures are revised.

## Evidence rules

- Parent and extension trajectories are never pooled.
- Fresh fragmentation-gradient rows are repeated measures over attempted source replicates, not independent observations.
- The historical 15/15 common-grid no-domain result remains immutable for that candidate family.
- R4 recovery is prospectively warning-blind and does not itself establish warning success.
- Phase E `migration_rate` is allele-frequency mixing only.
- Phase F `interaction kappa` is aggregate positive-feedback/effective interaction support, not partner richness, connectance or network simplification.
- Phase F is closed after its three predeclared levels; no finer/wider kappa search is opened to manufacture a boundary.
- Protocol 003 domains differ in recurrent-transition, ecological and deterioration parameters, so their Stage III contrast is portability rather than a direction-only effect.
- Endpoint records from the same trajectory are correlated; uncertainty resamples whole trajectories.
- `p_star` is an effective recurrent-transition equilibrium, not an estimated biological mutation rate.
