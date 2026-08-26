# State-defined reproducibility: bridge from the model to natural ecosystems

## Central result

The current programme supports a sharper statement than either `genetic warning is conditional` or `fragmentation effects are context dependent`:

> **Reproducibility belongs to a loss-generating state, not to a habitat label or a genetic statistic by itself.**

Three evidence layers now point in the same direction.

1. **Model state sufficiency:** under the declared Markov closure, complete equality of the present joint state makes prior history irrelevant for the future distribution, whereas coarse marginals and standard genetic summaries can hide dynamically different patchwise alignments.
2. **Natural partial-state tests:** in two independent ecological datasets, adding an upstream habitat/context variable after a measured interaction-functional state did not improve transfer to unseen ecological units under the preregistered validation rule.
3. **Full-denominator warning boundary:** event-conditional `H_alpha/H_gamma` ordering replicated, but the same thresholds fired in every non-event trajectory in both frozen ensembles.

The scientific problem is therefore to **identify the smallest future-relevant state in nature**, then test warning inside that state, and only then ask whether it ports to other states.

## 1. Direct natural-data evidence

### E1 Honshu–Izu: mainland distance after functional interaction state

Source: Hiraiwa & Ushimaru (2024), Figshare `10.6084/m9.figshare.25025000.v1`.

The locked archive supplies 40 site-season network states and 572 standardized pollen-receipt observations. The preregistered leave-one-site-out comparison was:

- `C0`: pollinator richness + season + focal plant;
- `C1`: `TM_z + FDQ + FEve + season + focal plant`;
- `C2`: `C1 + mainland distance`.

Row-weighted held-out MSE was:

- C0: `1.10963`;
- C1: `1.08774`;
- C2: `1.13209`.

Adding distance improved only 3/8 site folds and worsened aggregate MSE by `+4.08%`.

**Interpretation:** mainland distance did not add transferable predictive accuracy after the fixed ecological `I/T` partial state. However C1 itself only modestly improved over richness and beat C0 in 4/8 folds, so this is **not** evidence that `TM_z + FDQ + FEve` is a complete sufficient state. The missing `G/C/R/M` layers remain biologically important targets.

### E2 Zurich: urban context after function-specific interaction state

Source: EnviDat `10.16904/envidat.676` and locked BetterBlooms commit `d6361f6874398e797322afe07a8fea85a3c7e927`.

Six reproductive endpoints were fixed before the new comparison. For each function:

- `S1`: the source-defined function-specific pollinator interaction state;
- `S2`: `S1 + PlantS + Urban_500 + PlantS×Urban_500`;
- whole gardens were held out;
- positive `Delta_g = NLL(S1)-NLL(S2)` would favour transferable residual context information.

**0/6 endpoints** met the preregistered positive-residual-context rule. All six were classified `no_detected_residual_urban_information`. Two endpoints had bootstrap intervals wholly below zero, so the larger context model predicted unseen gardens worse.

**Interpretation:** the measured urban/local context layer did not carry detected transferable information after the interaction state under this design. This does not prove the interaction state is complete or that urban context is biologically irrelevant.

## 2. What E1 and E2 jointly establish

E1 and E2 are deliberately not pooled: their functions, predictors, sampling units and validation scores differ. Their common result is at the level of the hypothesis test:

> **An upstream fragmentation descriptor can have known marginal ecological effects yet fail to add transferable prediction after a more proximal measured process state is supplied.**

For Izu the upstream descriptor is mainland distance. For Zurich it is local/urban context. In both cases it is tested last, not promoted to the regime definition.

This is the first direct natural-data support for the manuscript's conditional-independence target:

`future/realised function ⟂ upstream fragmentation context | measured process state`

at an **ecological partial-state** resolution.

It is not yet a full eco-genetic convergence result because neither dataset synchronizes the complete candidate state `D/I/T/C/R/G_by_cohort/M/A`.

## 3. Natural systems show what the missing state coordinates look like

The quantitative natural anchors prevent E1/E2 from being interpreted as a generic `context does not matter` result.

- **U-LIM — *Crepis sancta*:** low local `D` is followed by lower realised `I` and lower `F`; nonzero wider pollen/seed movement does not guarantee local functional rescue.
- **I-COMP — Miyake-jima *Camellia–Zosterops*:** local floral support falls while partner/pollen movement broadens and pollination is maintained or enhanced; movement is an explicit compensatory coordinate.
- **U-LAG — *Conospermum undulatum*:** contemporary mating/function can deteriorate while adult neutral genetics still represents an older connectivity state; `G` must be indexed by cohort/history.
- **T-JOINT — *Spondias purpurea*:** reduced realised visitation, contracted pollen flow, lower sire diversity, lower reproductive function and stronger seed/juvenile genetic deterioration occur in one near-synchronized fragmentation comparison.
- **T-MATCH — Honshu–Izu:** functional partner diversity and trait matching carry information not replaced by species richness.

These examples show why a residual context term should be interpreted as **missing process information**, not as proof that a habitat category is itself the mechanistic state.

## 4. Event-conditional ordering is reproducible but not discriminative

The original C3 valid-pair ordering was independently replicated under a frozen loss-generating domain, but the post-review full-denominator audit changes its scientific meaning.

Original parent benchmark:

- all six baseline-relative `H_alpha/H_gamma × 5/10/20%` endpoints;
- `35/35` valid warning/loss pairs were leads at every endpoint.

Fresh Phase V:

- 100 attempted trajectories across fresh seeds `20291110–20291114`;
- 82 available trajectories;
- 33 realised functional losses;
- for **all six endpoints: 33/33 leads, 0 ties, 0 lags**;
- exact one-sided binomial `p=1.1641532182693481e-10` per endpoint;
- preregistered decision: **`strict_replication`** under the original event-pair rule.

The denominator-restored result is:

> **All six thresholds led 35/35 and 33/33 observed losses, but also fired in 48/48 and 49/49 non-events; full-horizon specificity was zero and binary-marker AUC was 0.5.**

This is replicated event-conditional temporal ordering, not predictive warning validity. The frozen protocol label remains historical provenance and does not override the full-denominator interpretation.

## 5. Resulting causal and empirical ordering

The combined programme is now:

```text
fragmentation / disturbance / landscape history
                  ↓
      measured joint process state S(t)
  D / I / T / C / R / G_by_cohort / M / A
                  ↓
       future realised function F(t+Δ)
                  ↓
     full-denominator validation inside S
                  ↓
  only then test portability across states
```

This ordering shows that state restriction alone cannot rescue a non-discriminative threshold. Event and non-event trajectories must both enter warning validation.

## 6. Current cross-system hypothesis

The next general ecological hypothesis is not `urban systems behave like islands`.

It is:

> **Different fragmentation mechanisms converge on the same operational functional-fragmentation regime only when their measured future-relevant joint states make origin/history dispensable for predicting what function happens next.**

E1 and E2 provide the first direct partial-state tests of this criterion. The natural anchors specify which missing coordinates need to be measured when the ecological partial state is incomplete.

A decisive full test should therefore synchronize, in the same site-year and cohort:

- direct function;
- effective interaction support and functional matching;
- contemporary pollen/seed/partner movement;
- compensation/reproductive assurance;
- adult plus offspring/pollen-pool genetic state;
- fragmentation/disturbance history;
- cross-layer spatial alignment.

The target is not the largest covariate set. It is the **smallest measured state that predicts future function and renders upstream origin/history predictively redundant at the declared scale**.

## Claim boundaries

Do not infer from the current evidence that:

- urban context or island distance is ecologically irrelevant;
- the E1 or E2 interaction state is already complete;
- cities and islands have been shown to occupy one common regime;
- one numerical natural-system threshold transfers across ecosystems;
- the Phase V relative-warning percentages are universal genetic-warning thresholds;
- within-state replication implies portability across states.

The supported synthesis is state-defined reproducibility, not universal context independence.
