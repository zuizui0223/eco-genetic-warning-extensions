# Claim–evidence map

## Study phases and provenance

| manuscript statement | evidence boundary |
|---|---|
| The manuscript integrates a theorem-guided first phase and an independently declared recurrent-transition extension as one study. | Keep the two repositories as separate computational provenance units; do not pool their trajectories. |
| The first phase provides the analytical interaction mechanism, locked H1/H3 fragmentation campaign, and inherited symmetric warning benchmark. | `eco-genetic-criticality` canonical scientific commit `dd8ee379d0d3518194c767d16402042525bc00dc` and final evidence ledger. |
| The extension reconstructs sources, maps common-grid loss regimes, recovers a narrow warning-blind R4 event regime, maps one allele-frequency-connectivity boundary, performs separately declared Protocol 003 portability validation, and derives exact recurrent-transition identities. | Protocol 002/003 documents, Phases A–E condition artifacts, locked Stage III artifacts, and exact theory documents/tests. |

## Permitted first-phase claims

| ID | permitted claim | required evidence | status |
|---|---|---|---|
| P1 | Equal isolation from an H1-prepared full state lowers final interaction, local effective size, and realised high-trait mass relative to the matched one-large projection. | Parent workflow run `28456092898`, artifact `7987193632`; 1,055 H1-qualified paired replicates across 12 primary cells. | supported, finite Type S |
| P2 | In the inherited symmetric benchmark, baseline-relative `H_alpha` and `H_gamma` erosion at 5%, 10%, and 20% preceded all 35 observed realised trait-loss events. | Parent H2-R trait-loss-only calibration and independent fresh-seed validation. | supported conditionally, finite Type S |
| P3 | Fixed absolute thresholds `H_alpha <= 0.20` and `H_gamma <= 0.20` are not robust warning rules in that same benchmark. | Stored-trajectory H2-A audit: 14/0/6 and 8/0/8 lead/tie/lag. | negative robustness result |
| P4 | A fresh fixed-area fragmentation sensitivity shows that the historical four-patch contrast was already present after the first split to two isolated patches; interaction and local effective size then declined further, whereas realised high-trait mass was non-monotonic. | Parent run `31937210601`, artifact `9261157020`; 1,037 prepared sources projected across eight patch counts. | supplementary finite Type S sensitivity |

## Permitted extension claims

| ID | permitted claim | required evidence | status |
|---|---|---|---|
| S1 | At fixed `kappa_mu`, recurrent-transition direction changes high-state source feasibility. | Common Stage I coordinate grid; 3,375 source attempts and 2,269 supported projections. | supported for declared closure |
| S2 | The common deterioration family partitions candidates into rapid-loss, persistence, and seed-heterogeneous regimes. | Stage II complete candidate rates and regime audit. | supported for declared closure |
| S3 | No Protocol 002 coordinate had an eligible warning-validation domain under the original strict all-seed rule. | 648 complete candidates, zero eligible, 15 `no_domain_selected`. | negative/recovered for original coarse grid/family |
| S4 | Protocol 003 used a separately declared, warning-blind amendment that expanded the candidate family and replaced the Protocol 002 all-seed gate before warning values were calculated. | `PROTOCOL_003_AMENDMENT_001.md` and `PROTOCOL_003_AMENDMENT_002.md`. | documented design fact |
| S5 | The two Stage III validation domains differ in recurrent-transition parameters, `A_ref`, interaction-feedback `kappa`, barrier increase, and calibrated horizon. | Locked confirmation cells and Stage III domain identities. | documented design fact |
| S6 | Warning availability and ordering differ between the recalibrated symmetric domain and directional calibrated domain. | Locked Stage III trajectories plus trajectory-cluster secondary audit. | supported as a calibrated-domain portability result |
| S7 | Stage III timing point estimates are schedule-dependent; direct between-domain bootstrap differences are endpoint-dependent for absolute time and include zero for all six full-horizon-normalized contrasts. | Immutable Stage III trajectories, conventional-median audit, and `stage3_between_domain_differences.csv`. | supported uncertainty / identification statement |
| S8 | Censoring and warning availability are part of the finite ecological outcome rather than discarded missing data. | Full 100-attempt endpoint denominators and cumulative event-incidence summaries. | supported as bounded interpretation |
| S9 | Under the original strict common deterioration family, no matched validation domain was available at any of the 15 coarse coordinates; Protocol 003 restored evaluability only by separately recalibrating non-matched domains. | Protocol 002 no-domain audit plus Protocol 003 amendments. | historical design/biology boundary |
| S10 | Warning-blind frontier refinement shows that R4 event-regime evaluability is not structurally absent: at fixed `A_ref=1.0`, interaction `kappa=4.5`, `kappa_mu=0.35`, `p_star=0.35`, horizon 120 and barrier increase 0.30, all five independent seed blocks fell in `[0.30,0.70]` in two fresh high-rep campaigns. | Phase C and Phase D summaries/artifacts. | positive finite condition recovery |
| S11 | The recovered R4 region is narrow along `p_star` at the tested resolution: Phase D neighbors `0.325` and `0.375` were R3-highrep, and Phase C `0.40` was also R3-highrep. | Phase C/D high-rep summaries. | finite boundary result |
| S12 | Intermediate pooled trait-loss probability is not sufficient to define warning evaluability; seed-block reproducibility is an additional condition. | Phase B pooled gradient plus Phase C/D block-level classifications. | supported condition/estimand distinction |
| S13 | At the independently reproduced R4 anchor, allele-frequency migration changed event-regime evaluability: `m=0,0.025,0.05` remained R4-highrep whereas `m=0.10,0.20` were R3-highrep, despite pooled loss remaining in a relatively narrow 0.549–0.626 range. | Phase E paired migration-condition run `32376912392`, artifact `9409687687`. | finite connectivity-boundary result |
| S14 | Migration changed which paired trajectories lost realised function in both directions; relative to isolation, total loss-status switches were 8/91, 12/91, 21/91 and 25/91 at `m=0.025,0.05,0.10,0.20`. | Phase E paired prepared-source records. | finite trajectory-switching result |

## Permitted exact recurrent-transition / migration claims

These are Type T algebraic boundaries for the declared operators under their stated assumptions. They are not finite Stage III effect estimates and not dynamic warning theorems.

| ID | permitted claim | required evidence | status |
|---|---|---|---|
| T1 | Increasing `p_star` has no universal signed effect on heterozygosity: `dH(M(p))/dp_star = 2*kappa_mu*(1-2M(p))`, so the sign changes at `M(p)=0.5`. | `docs/RECURRENT_TRANSITION_DIVERSITY_THEORY.md`; executable tests in `tests/test_mutation_coordinates.py`. | Type T |
| T2 | With fixed patch weights and a common affine transition, `H_gamma' - H_alpha' = (1-kappa_mu)^2 (H_gamma-H_alpha)`, so one-step contraction of the alpha–gamma gap depends on transition strength but not `p_star`. | Same exact derivation and executable tests. | Type T |
| T3 | Increasing `p_star` always strengthens the local high-associated allele support margin `M(p)-p_c`, but when `M(p)>0.5` it decreases heterozygosity; genetic diversity is therefore not a monotone proxy for this local functional-support condition. | Same exact derivation and executable tests. | Type T, local support boundary |
| T4 | For a pre-state below a local high-state threshold, stronger `kappa_mu` lowers the `p_star` required to reach the same post-transition support boundary. | `docs/RECURRENT_TRANSITION_SUPPORT_FRONTIER.md`; executable frontier tests. | Type T, local support frontier |
| T5 | The declared allele-frequency migration operator contracts among-patch frequency deviations toward a weighted mean; this homogenisation does not by itself determine the sign of realised functional loss. | Parent migration theorem plus Phase E bidirectional trajectory switching. | Type T + finite boundary |

## Locked and corrected numerical facts

| fact | value |
|---|---:|
| first-phase primary H1/H3 attempted replicates | 1,200 |
| first-phase H1-qualified paired replicates | 1,055 |
| H3 pattern supported among H1-qualified replicates | 1,055 / 1,055 |
| median paired interaction reduction after isolation | 99.86% |
| median paired local effective-size reduction | 88.73% |
| median paired realised high-trait-mass reduction | 68.87% |
| fresh fragmentation-gradient attempted / prepared sources | 1,200 / 1,037 |
| fresh n=2 paired reductions: interaction / local effective size / realised high-trait mass | 99.83% / 77.87% / 71.71% |
| fresh n=4 paired reductions: interaction / local effective size / realised high-trait mass | 99.86% / 88.73% / 69.82% |
| potential high-trait viability: n=1 / every n>=2 | 1,037/1,037 / 0/1,037 |
| inherited symmetric benchmark attempted / available / trait loss | 100 / 83 / 35 |
| inherited symmetric benchmark censored for trait loss | 48 |
| inherited relative-warning lead/tie/lag per endpoint | 35 / 0 / 0 |
| Protocol 002 batches | 810 |
| Protocol 002 complete five-seed candidates | 648 |
| Protocol 002 rapid-loss / heterogeneous / persistence candidates | 322 / 84 / 242 |
| original Protocol 002 eligible candidates | 0 |
| original Protocol 002 no-domain coordinates | 15 |
| Phase A new attempts / R4 / R3 / R2 | 250 / 0 / 6 / 4 cells |
| Phase B pooled loss across p_star 0.30 / 0.35 / 0.40 / 0.45 | 0.739 / 0.476 / 0.304 / 0.095 |
| Phase C p_star=0.35 pooled loss / regime | 0.505 / R4-highrep |
| Phase C p_star=0.40 pooled loss / regime | 0.304 / R3-highrep |
| Phase D p_star=0.325 pooled loss / regime | 0.663 / R3-highrep |
| Phase D p_star=0.350 pooled loss / regime | 0.609 / R4-highrep |
| Phase D p_star=0.375 pooled loss / regime | 0.391 / R3-highrep |
| Phase E prepared sources / migration-level trajectories | 100 / 500 |
| Phase E pooled loss at m=0 / 0.025 / 0.05 / 0.10 / 0.20 | 0.571 / 0.549 / 0.593 / 0.626 / 0.604 |
| Phase E regime at m=0 / 0.025 / 0.05 / 0.10 / 0.20 | R4 / R4 / R4 / R3 / R3 |
| Phase E paired status switches vs isolation at m=0.025 / 0.05 / 0.10 / 0.20 | 8 / 12 / 21 / 25 of 91 |
| Stage III attempted trajectories | 100 + 100 |
| recalibrated symmetric domain completed trajectories | 82 |
| directional calibrated domain completed trajectories | 91 |
| recalibrated symmetric valid endpoint comparisons | 324 |
| recalibrated symmetric lead / tie / lag | 323 / 1 / 0 |
| directional calibrated valid endpoint comparisons | 201 |
| directional calibrated lead / tie / lag | 184 / 5 / 12 |
| valid-pair availability per attempted endpoint | 0.540 vs 0.335 |
| trajectory-bootstrap lead fraction | 0.997 [0.990, 1.000] vs 0.915 [0.848, 0.971] |
| directional lag fraction | 0.060 [0.016, 0.112] |
| conventional median positive lead-time range | 106–109 vs 72.5–77.5 generations |
| median positive lead fraction of calibrated horizon | 0.442–0.454 vs 0.604–0.646 |
| absolute D−S 95% difference intervals exclude zero | H-alpha 5% and H-alpha 10% only |
| horizon-normalized D−S 95% difference intervals include zero | all six endpoints |
| directional H-gamma 20% final warning / trait-loss incidence | 41/81 (0.506) / 52/81 (0.642) |
| Stage III calibrated horizons | 240 vs 120 generations |

The historical Stage III source artifacts used the upper middle order statistic for even `n` while calling it a median. The source artifacts remain immutable; publication timing values come from the post-review secondary audit, which uses the conventional median. The paired fragmentation reductions were calculated separately and are unaffected.

## Prohibited claims

- The original 15/15 `no_domain_selected` result proves that an evaluable event regime cannot exist.
- The refined R4 condition proves that genetic warning succeeds there; warning fields have not been evaluated in Phases A–E.
- R4 is a broad or contiguous `p_star` interval; only `p_star=0.35` reproduced at the tested high-rep resolution.
- Finer `p_star` tuning is justified merely to manufacture adjacent R4 cells.
- `m=0.05` or any tested migration value is a universal ecological threshold.
- Migration universally rescues, protects, destabilizes or harms ecological function; Phase E contains paired switches in both directions and non-monotone pooled loss.
- The current simulator's `migration_rate` is demographic migration, pollinator movement, seed dispersal, recolonisation or trait-bin dispersal; it is allele-frequency mixing only.
- Recurrent-transition direction alone caused the historical Stage III warning-ordering difference.
- Recurrent-transition direction alone shortened or lengthened intervention time.
- The horizon-normalized Stage III timing difference is separated at any of the six endpoints.
- All six absolute Stage III timing contrasts are separated.
- Stage III changed only one biological parameter or is matched except for `p_star`.
- Protocol 003 retained the Protocol 002 eligibility rule unchanged.
- Directional transition universally causes ecological collapse or rescue.
- Genetic diversity warning universally fails or succeeds under directional transition.
- `p_star` is an empirically estimated mutation rate.
- Endpoint-level comparisons are independent biological replicates.
- Bootstrap intervals are population-level confidence intervals.
- Two calibrated domains constitute a complete phase diagram of warning performance.
- The fragmentation sensitivity is a universal monotone dose-response.
- `K=4` is the observed finite fragmentation threshold.
- Increasing `p_star` universally increases or universally decreases heterozygosity.
- Lower genetic diversity necessarily means poorer ecological function or weaker local high-state support.
- The local Type T support–diversity result determines full stochastic warning first-passage ordering.
- The fixed-weight one-step identities remain exact after arbitrary demographic reweighting, drift or selection without re-evaluation.

## Story-to-evidence mapping

| narrative step | evidence role |
|---|---|
| Functional state can be lost before population disappearance | analytical interaction/function-state distinction + parent finite state definitions |
| Fragmentation creates an eco-genetic vulnerability bridge | P1; P4 is supplementary robustness |
| Genetic erosion can warn in one calibrated regime but not by a universal absolute threshold | P2 + P3 |
| Recurrent transitions change source feasibility | S1 |
| Recurrent transitions change the loss-generating regime | S2 |
| A coarse common grid can miss the narrow region where loss is reproducible and nondegenerate | S3 + S10–S12 |
| Effective genetic connectivity can move that recovered event regime between R4 and R3 without a simple pooled-risk sign | S13 + S14 + T5 |
| Recalibration across non-matched domains yields bounded portability differences | S4–S8 |
| Diversity is not a monotone proxy for local functional support | T1–T4 |

## Required figure-to-claim mapping

Current publication figures remain tied to the locked manuscript campaign. Frontier-condition Phases A–E are **not** silently inserted into those figures before the final manuscript architecture is revised.

| figure | content | claims supported |
|---|---|---|
| Figure 1 | integrated fragmentation-to-warning causal architecture | conceptual mechanism; no numerical effect size |
| Figure 2 | common-grid source feasibility | S1 |
| Figure 3 | original common-grid loss regimes plus 648-candidate composition | S2, S3, S9 |
| Figure 4 | cumulative warning and functional-loss incidence with administrative censoring | S6, S8 |
| Figure 5 | full attempted denominator: source failure, ineligibility, censoring, lead/tie/lag | S6, S8 |
| Figure 6 | corrected absolute and horizon-normalized positive lead time with trajectory-bootstrap intervals | S7; secondary conditional diagnostic |
| Supplementary Figure S1 | fresh fixed-area paired fragmentation gradient | P4 |

Every finite numerical claim must retain the declared Type S closure. T1–T5 are exact/local operator boundaries only within their stated assumptions.
