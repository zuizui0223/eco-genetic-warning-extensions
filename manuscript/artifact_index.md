# Artifact and workflow index

## Core evidence provenance

| Campaign | Evidence | Workflow run / artifact |
|---|---|---|
| Inherited H1/H3 finite chain | paired one-large versus equal-isolated outcomes used for the fragmentation effect-size audit | parent run `28456092898`, artifact `7987193632`, digest `sha256:b74b604f3233fa6086e2afa39cd780fa375aac4b1abd8c63e6f5ed8b3a467d2c` |
| Post-review H3 fragmentation gradient | fresh fixed-area paired projections at 1, 2, 3, 4, 6, 8, 12, and 16 isolated patches; 1,200 attempted / 1,037 prepared sources | parent run `31937210601`, artifact `9261157020`, digest `sha256:424031d0f6bcdf75c13e03deb35324f0d3f6fd46f58ff7b34961bbd00556537c` |
| Inherited relative-warning benchmark | trait-loss-only calibration and fresh-seed H2-R validation | parent calibration run `28496735824`; parent validation run `28500796310` |
| Source reconstruction and projection | 135 batches, 3,375 attempts over the common 15-coordinate transition grid | runs `29177214259`, `29186610167`, `29188592519`, `29188748077`, `29190149319`, `29190149344` |
| Source-feasibility publication outputs | coordinate CSV and summary JSON | run `29422431944`, artifact `8345805712`, digest `sha256:fc9b9a410908cf4446b65d5caee8de8d731734f0fae47e69c94cddc830a814e9` |
| Protocol 002 warning-blind calibration | 810 batches, 20,250 attempts; 648 complete candidates; 15/15 coordinates `no_domain_selected` | locked Stage II audit and selection artifacts |
| Trait-loss-regime publication outputs | coordinate regime CSV and regime map inputs | run `29399936061`, artifact `8336631530`, digest `sha256:3c7f63b5bc054c37012bb448ad1dc5e9bf45a4ec79737520390b576079ccc8f7` |
| Protocol 003 Amendment 001 | warning-blind candidate-family extension and event-risk gate | `docs/PROTOCOL_003_AMENDMENT_001.md` |
| Protocol 003 Amendment 002 | unchanged gate, increased replication, fresh confirmation seeds | `docs/PROTOCOL_003_AMENDMENT_002.md` |
| Protocol 003 validation | 200 attempted fresh-seed trajectories | run `29417632137` |
| Recalibrated symmetric validation domain | 100 attempts; `A_ref=0.8`, `kappa=6.0`, `kappa_mu=0.20`, `p_star=0.50`, ramp 30 + hold 210, increase 0.20 | artifact `8343958766`, digest `sha256:c1b42fc9e6ac912a44667ef4cee02090fab37d50fc3a9928c46ae728c0610f58` |
| Directional calibrated validation domain | 100 attempts; `A_ref=1.0`, `kappa=4.5`, `kappa_mu=0.05`, `p_star=0.90`, ramp 30 + hold 90, increase 0.10 | artifact `8343922879`, digest `sha256:0a994bea874fc9c47544169cd31bbc317c88690dfe1b6fa7548516e35fd7bca8` |
| Post-review Stage III secondary audit | conventional medians, horizon-normalized lead times, whole-trajectory bootstrap, cumulative event incidence, and direct directional-minus-symmetric timing differences | regenerated from the two immutable Stage III artifacts above during publication builds |

Protocol and stage identifiers remain in workflow metadata and Methods because they are necessary for provenance. Biological Results and figure titles use reader-facing ecological language.

## Machine-readable manuscript and bundle tables

- `manuscript/tables/inherited_h3_effect_summary.csv` — paired first-phase H3 descriptive effects from the locked parent artifact.
- `h3_fragmentation_gradient_records.csv` in the checksummed submission bundle — 9,600 post-review repeated-measures rows from 1,200 attempted fresh sources across eight patch counts.
- `h3_fragmentation_gradient_cell_summary.csv` and `h3_fragmentation_gradient_pooled_summary.csv` — cell-level and pooled paired gradient summaries underlying Supplementary Figure S1.
- Stage I `stage1_coordinate_summary.csv` — source feasibility over the common 15-coordinate grid; generated from locked publication artifact `8345805712` and included in the bundle.
- Stage II `stage2_coordinate_regimes.csv` — strict Protocol 002 loss-regime map; generated from locked publication artifact `8336631530` and included in the bundle.
- `manuscript/tables/stage3_endpoint_summary.csv` — historical Stage III compact summary retained for provenance.
- `stage3_trajectory_endpoint_records.csv` in the checksummed submission bundle — generated full 100-attempt denominator for every Stage III endpoint (1,200 rows).
- `stage3_review_audit.json` in the checksummed submission bundle — complete fixed secondary audit including within-domain bootstrap summaries, cumulative incidence and direct between-domain differences.
- `manuscript/tables/stage3_review_summary.csv` — committed compact publication summary; bundle generation rejects a regenerated table that is not byte-identical.
- `manuscript/tables/stage3_between_domain_differences.csv` — committed directional-minus-symmetric median differences for absolute, full-horizon-normalized and hold-normalized lead time; publication builds regenerate and byte-compare this file from the immutable Stage III trajectories.

The historical Stage III summary is not silently overwritten. Corrected conventional medians, normalized timing, and direct timing differences are labelled as a post-review secondary analysis of immutable validation artifacts.

## Main figures

1. **Eco-genetic closure and the emergence of genetic warning.** Conceptual synthesis linking fragmentation, interaction state, high-trait state, local effective size, genetic diversity, relative warning and realised functional-trait loss.
2. **High-trait source feasibility across recurrent-transition coordinates.** Common-grid source reconstruction; direct transition-coordinate evidence.
3. **Functional-loss regimes and candidate composition across recurrent-transition coordinates.** The 15-cell regime map and complete-candidate composition are combined; 322 rapid-loss-side, 84 seed-heterogeneous and 242 persistence-side candidates are shown together with the 0/15 selection result.
4. **Cumulative warning and functional-loss incidence in the two calibrated validation domains.** Administrative censoring is retained over each domain-specific horizon; warning and loss are paired repeatable events rather than classical competing-risk outcomes.
5. **Warning availability, censoring and ordering from the full attempted denominator.** Each endpoint bar retains 100 attempts, source failure, baseline ineligibility, both-censored, warning-censored, trait-loss-censored, lead, tie and lag categories.
6. **Absolute and horizon-normalized positive warning lead time.** Conventional medians and whole-trajectory bootstrap intervals are shown; the direct between-domain audit demonstrates endpoint-dependent absolute contrasts and no separated full-horizon-normalized contrast.

### Supplementary figure

S1. **Fixed-area fragmentation gradient from paired H1-prepared sources.** Fresh-seed repeated-measures sensitivity across 1, 2, 3, 4, 6, 8, 12, and 16 isolated equal patches; interaction and local effective size decline after the first split, while realised high-trait mass is non-monotonic.

## Figure-caption boundaries

Every numerical figure caption states the statistical unit and relevant evidence boundary. Figures 4–6 distinguish the **recalibrated symmetric domain** and **directional calibrated domain**. Figure 6 must not be described as identifying a transition-direction timing effect: the validation domains differ in transition parameters, ecological parameters and deterioration schedules, and every full-horizon-normalized direct difference interval includes zero. Figure 1 is conceptual and does not claim a universal causal theorem.

## Evidence rules

- The two repositories are computational phases of one manuscript but remain separate provenance ledgers; trajectories are never pooled across phases.
- Direct recurrent-transition-coordinate effects are supported by the common-grid source-feasibility and loss-regime analyses, not by a single-factor Stage III contrast.
- Protocol 002 remains closed with 15/15 `no_domain_selected` under its strict all-seed rule.
- Protocol 003 is separately declared. Amendment 001 expanded the candidate family and changed the event-risk eligibility gate before any warning outcome was calculated; Amendment 002 did not relax that gate further and instead increased replication with fresh seeds.
- The two Protocol 003 validation domains differ in `A_ref`, interaction-feedback `kappa`, `kappa_mu`, `p_star`, deterioration horizon and barrier increase. Their Stage III contrast is therefore a portability comparison across independently calibrated eco-genetic domains.
- The shared Protocol 002 deterioration family is the matched-schedule experiment; because it selected no validation domain at any coordinate, a matched Stage III warning comparison was not available without changing the event-risk regime.
- Endpoint comparisons from the same trajectory are correlated. Post-review uncertainty intervals resample whole trajectories, never endpoint rows independently.
- Direct timing contrasts resample the two independent domains separately and calculate the difference itself; marginal interval overlap is not used as the difference test.
- Historical Stage III artifacts remain immutable. The conventional-median correction and timing audit are explicitly labelled as post-review secondary analyses.
- `p_mu*` is an effective recurrent-transition equilibrium, not an estimated biological mutation rate.
