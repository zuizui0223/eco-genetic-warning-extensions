# Manuscript workspace

**Working title:** *Eco-genetic conditions govern when genetic early warning of functional loss can be validated*

The manuscript is downstream of the scientific condition map. Do not organise the paper around protocol chronology, and do not treat `urban`, `island` or another habitat label as a biological regime by itself.

## Publication logic

```text
C0  interaction-dependent functional state exists
 ↓
C1  fragmentation / deterioration can disrupt it before demographic disappearance
 ↓
C2  eco-genetic state determines source feasibility and the functional-loss process
     ├─ loss incidence
     ├─ between-block heterogeneity
     ├─ trajectory identity
     ├─ representation / replication boundaries
     └─ future-relevant joint spatial state
 ↓
C3  only then test whether genetic change precedes independently defined loss
 ↓
C4  finally test portability across calibrated domains
 ↓
E1  ask in nature whether different fragmentation mechanisms converge after
    conditioning on the same future-relevant measured ecological state
```

The central contribution is no longer a particular migration threshold or historical R1–R4 label. It is the **ordering and state definition**: genetic warning is a conditional downstream property of a loss-generating eco-genetic state.

## Current evidence

- **C0/C1 — inherited mechanism:** the parent model establishes a high-function interaction-supported state and a paired fragmentation effect before population disappearance.
- **C2a — recurrent turnover:** recurrent-transition coordinates alter source feasibility and define a high-to-low functional-loss incidence frontier. High-precision frontier conditions do not show detectable excess block heterogeneity.
- **C2b — historical screen correction:** R1–R4 remain protocol labels, not latent biological regimes. Low-replicate R3/R4 calls cannot establish heterogeneity by themselves.
- **C2c — connectivity representation boundary:** the historical allele-only `m=.10` heterogeneity observation failed one preregistered fresh-seed replication (Phase U) and did not port to whole-individual dispersal (Phase R) or pollen-only gene flow (Phase S). No robust portable connectivity-heterogeneity effect is established.
- **C2d — interaction / partner boundary:** the predeclared aggregate-feedback range and reduced-form / temporal partner perturbations produced bounded negative population-level results. Adaptive rewiring remains closed because its prospective opening condition was not met.
- **C2e — state sufficiency:** under the declared parent Markov closure, complete present-state equality is future-sufficient, but common coarse summaries are not. A constructive two-patch counterexample preserves census, interaction and allele marginals/means, `H_alpha`, `H_gamma`, `F_ST` and realised trait state while changing patchwise interaction–genetic alignment; the next interaction field changes.
- **C3 — within-state warning replication:** the inherited frozen H2-R benchmark had 35/35 leads at all six baseline-relative `H_alpha/H_gamma × 5/10/20%` endpoints, and one independent preregistered fresh-seed ensemble strictly replicated the ordering with 33/33 leads, 0 ties and 0 lags at every endpoint. Fixed absolute thresholds remain non-robust; this is within-domain replication, not a universal threshold.
- **C4 — bounded portability:** independently calibrated domains differ in warning availability/order, but the comparison is not a matched single-factor causal experiment. Within-state replication therefore does not imply cross-state portability.

## Empirical extension: find the state in nature

The theoretical state is not the endpoint. The empirical programme asks whether a **measured joint state** can make different fragmentation histories dynamically equivalent.

Candidate field coordinates are:

1. demographic support;
2. realised interaction support;
3. functional/trait state;
4. genetic and mating state;
5. process-specific pollen, seed/propagule, demographic and partner connectivity;
6. reproductive assurance or compensatory routes;
7. direct realised ecological function;
8. plausible ecological memory and **cohort identity**;
9. the **joint spatial alignment** among these quantities.

The falsifiable convergence criterion is:

> after conditioning on the candidate measured state, system origin or fragmentation history should no longer improve out-of-sample prediction of subsequent realised functional loss.

If origin/history remains predictive, the state representation is incomplete and the missing process or memory variable must be sought.

Concrete natural systems and open-data opportunities are registered in [`empirical_regime_candidates.md`](empirical_regime_candidates.md), with measurement completeness and synchronization tracked in [`empirical_measurement_crosswalk.md`](empirical_measurement_crosswalk.md).

Four quantitative natural anchors now make the condition language operational:

- [`empirical_e3_crepis_audit.md`](empirical_e3_crepis_audit.md): Montpellier *Crepis sancta* identifies **interaction-limited local fragmentation** — low local flowering support is accompanied by reduced pollinator activity and reproductive function, without strong autonomous-selfing compensation, even though the wider urban metapopulation has nonzero pollen/seed immigration.
- [`empirical_e4_miyake_audit.md`](empirical_e4_miyake_audit.md): Miyake-jima *Camellia japonica*–*Zosterops japonicus* identifies **movement-compensated local fragmentation** — volcanic damage reduces local floral resources while broader partner movement and pollen mixing maintain or enhance the pollination component and next-generation genetic mixing.
- [`empirical_e5_conospermum_audit.md`](empirical_e5_conospermum_audit.md): Perth *Conospermum undulatum* identifies **cohort/history-lag functional fragmentation** — contemporary pollen connectivity and reproductive function respond to recent built-matrix fragmentation while standing adult neutral genetics still retains the signature of the historically connected landscape.
- [`empirical_e6_spondias_audit.md`](empirical_e6_spondias_audit.md): Mexican tropical dry-forest *Spondias purpurea* identifies **joint interaction–connectivity limitation with cohort-emergent genetic deterioration** — realised visitation, paternity-derived pollen flow, reproductive success, sire diversity and adult/seed/juvenile genetics are measured within one fragmentation comparison.

Together these anchors show four different reasons why a coarse state fails: local interaction support can be uncompensated or movement-compensated, standing adult genetics can be temporally out of phase with the contemporary process, and synchronized interaction/connectivity deterioration can first become most visible in offspring cohorts.

The *Spondias* study is currently the strongest natural bridge to the full state logic because `I`, `C`, `F` and cohort-specific `G` are not assembled from unrelated study years. It is therefore useful as a model for future urban/island sampling even though it is neither an urban nor an island system.

Two direct open-data residual-context tests are now available:

- **Honshu–Izu E1:** in 572 pollen-receipt observations across eight held-out sites, adding mainland distance after `TM_z + FDQ + FEve + season + focal plant` worsened row-weighted MSE by about 4.08% and improved only 3/8 folds. The ecological partial state itself only modestly improved over richness, so this is absence of transferable distance gain, not proof of complete state sufficiency.
- **Zurich E2:** across six fixed reproductive endpoints, adding `PlantS + Urban_500 + PlantS×Urban_500` after the source-defined function-specific interaction state produced 0/6 preregistered positive residual-context detections. This is absence of detected transferable urban/context information, not proof that urban context is ecologically irrelevant.

## Publication sources of truth

Use this hierarchy when files disagree:

1. [`main_text.md`](main_text.md) — publication manuscript;
2. [`claim_evidence_map.md`](claim_evidence_map.md) — permitted/prohibited claims;
3. [`hypothesis_condition_ledger.md`](hypothesis_condition_ledger.md) — recovered result → condition → boundary;
4. [`urban_island_regime_tests.md`](urban_island_regime_tests.md) — state-sufficiency convergence logic;
5. [`empirical_regime_candidates.md`](empirical_regime_candidates.md) — real-system measurements, candidate regimes and open-data tests;
6. [`empirical_measurement_crosswalk.md`](empirical_measurement_crosswalk.md) — measurement completeness, synchronization and field identification rules;
7. [`empirical_e3_crepis_audit.md`](empirical_e3_crepis_audit.md), [`empirical_e4_miyake_audit.md`](empirical_e4_miyake_audit.md), [`empirical_e5_conospermum_audit.md`](empirical_e5_conospermum_audit.md) and [`empirical_e6_spondias_audit.md`](empirical_e6_spondias_audit.md) — quantitative natural anchor conditions;
8. [`state_reproducibility_bridge.md`](state_reproducibility_bridge.md) — current synthesis connecting E1/E2 natural-state tests to within-state warning replication;
9. [`ecological_grounding.md`](ecological_grounding.md) — broader ecological translation;
10. [`artifact_index.md`](artifact_index.md) — numerical provenance.

Historical phase documents and **phase-specific result notes** remain provenance only and **must not compete with the current sources**; they do not override the current condition map or publication sources of truth.

## Main line

- function can be lost before population disappearance;
- recurrent turnover and ecological closure condition the loss process;
- finite screen labels and stochastic observations are not biological regimes by themselves;
- connectivity is process-specific and the historical allele-mixing signal is non-replicated/non-portable;
- complete future-relevant state is sufficient under the declared model, while coarse averages and standard genetic summaries can hide dynamically distinct spatial alignments;
- genetic warning is meaningful only downstream of the independently characterised loss-generating state;
- **inside one frozen loss-generating state, baseline-relative genetic-warning ordering strictly replicates across independent seed ensembles; portability across states remains bounded**;
- natural systems already show opposite outcomes from superficially similar local-support loss, depending on interaction limitation versus movement compensation;
- long-lived natural populations can retain historical genetic structure after contemporary interaction/connectivity has already changed, so cohort and memory must be aligned to the outcome window;
- a near-synchronized natural system (*Spondias*) shows that reduced realised visitation, contracted pollen flow, lower function and next-generation genetic deterioration can form one joint fragmentation state;
- E1 and E2 directly test whether upstream island/urban context retains transferable information after a measured ecological process state, rather than treating habitat labels as regimes;
- urban, island and other fragmented ecosystems become direct empirical tests of whether different causal histories converge on a common measured state.

## Claims not made

- No universal genetic-warning theorem or universal genetic threshold.
- No universal numerical meaning for historical R1–R4 labels or tested migration/kappa values.
- No claim that `p_star` is an empirical mutation rate.
- No claim that allele-frequency `migration_rate` is demographic, pollinator, pollen or seed movement.
- No claim that interaction `kappa` is interaction-network simplification.
- No claim that Phase U proves heterogeneity can never occur at `m=.10`.
- No claim that real networks are irrelevant because reduced-form partner tests were null.
- No claim that cities and islands already occupy the same regime.
- No assumption that matching occupancy, mean interaction or genetic diversity is enough to establish dynamic equivalence.
- No assumption that lower neutral genetic diversity always means poorer ecological function.
- No claim that the separate *Crepis* publications form one synchronized population-year state table.
- No claim that Miyake-style movement compensation is a universal island response.
- No claim that every adult neutral marker must lag recent fragmentation; *Conospermum* is an explicit natural example of cohort/history mismatch, not a universal lag constant.
- No claim that the *Spondias* numerical pollen-distance or heterozygosity contrasts are transferable thresholds; they are one observed joint-state anchor.
- No claim that E1/E2 establish a complete natural sufficient state or full urban–island convergence.
- No claim that the Phase V 5%, 10% or 20% relative declines are universal thresholds; they are replicated endpoints inside one frozen domain.

## Editorial rule

Results sections are named by biological result, not `Stage I/II/III` or `Phase A/B/...`. Protocol labels belong in Methods, Supplement and provenance. Natural-system examples must be tied to measured state coordinates and direct function, not used as decorative analogies.
