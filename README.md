# Eco-genetic warning extensions

This repository tests **when an eco-genetic warning question is biologically well posed**. It is the condition-recovery extension of [`eco-genetic-criticality`](https://github.com/zuizui0223/eco-genetic-criticality), pinned for inherited scientific results at `dd8ee379d0d3518194c767d16402042525bc00dc`.

The repository is organised condition-first rather than protocol-first:

```text
C0  Can an interaction-dependent high-function state exist?
        ↓
C1  Does fragmentation / deterioration disrupt that state?
        ↓
C2  Which biological conditions generate reproducible functional loss?
        ├─ recurrent state turnover
        ├─ effective genetic connectivity
        ├─ aggregate interaction support
        └─ matched reduced-form partner loss
        ↓
C3  Only inside an evaluable loss regime: does genetic change precede loss?
        ↓
C4  Is that warning portable across eco-genetic regimes?
```

**Warning is a downstream conditional outcome, not the starting hypothesis.** If a general proposition is not recovered, the next result is its boundary or recovery condition.

## Current scientific state

### Inherited mechanism

The parent repository supplies the mechanistic base:

- interaction feedback can support a high-function state in the declared model;
- fragmenting the same prepared high state reduces interaction, local effective size and realised high-trait mass;
- in one independently calibrated symmetric benchmark, relative genetic-diversity erosion preceded observed functional loss, whereas fixed absolute thresholds produced both leads and lags.

Parent and extension trajectories are never pooled.

### Recovered extension results

1. **Source feasibility is conditional.** Across the original 15 recurrent-transition coordinates, 2,269/3,375 source attempts supported preparation/projection; support varied from 44.89% to 86.67%.
2. **Functional-loss regime is conditional.** Among 648 complete common-grid candidates, 322 were rapid-loss, 242 persistence and 84 seed-heterogeneous.
3. **The original common grid contained no strict warning-evaluable domain.** All 15 coordinates remain historically `no_domain_selected`; this is an event-regime result, not warning failure.
4. **A warning-evaluable event regime exists, but narrowly along the recurrent-turnover axis.** Prospective warning-blind high-rep runs independently recovered R4 at `kappa_mu=0.35, p_star=0.35`; neighbouring `p_star` values remained seed-heterogeneous.
5. **Genetic connectivity can change evaluability without acting as a universal rescue axis.** At the recovered anchor, `m=0–0.05` remained R4-highrep whereas `m=0.10–0.20` became R3-highrep, with loss-status switches in both directions.
6. **Aggregate interaction support did not break R4 across the predeclared tested range.** At `kappa=3.0,4.5,6.0`, all five seed blocks at every level remained inside the R4 loss-frequency band. Source/baseline eligibility was 0.77, 0.94 and 0.87, while pooled loss among eligible trajectories was 0.468, 0.521 and 0.552. Thus state establishment varied descriptively while post-source event-regime classification remained R4-highrep.
7. **Matched one-partner loss changed event-regime reproducibility more than pooled risk.** A fresh intact control reproduced R4 (`49/90`, pooled loss 0.544). Three prospectively declared one-partner-loss conditions, matched for the same `4→3` richness change and mean retained support 0.75, all became R3-highrep while pooled loss stayed 0.556–0.578. Paired status switched in both directions and a secondary paired incidence audit found no pooled-risk difference (`Cochran Q p=0.943`). The result separates event frequency from warning estimability; contribution concentration itself did not separate regimes.
8. **Portability is bounded.** The historical Protocol 003 domains differ in several ecological and recurrent-transition parameters; their warning contrast is therefore a portability result, not a matched direction-only causal effect.

All numerical conclusions are finite Type S evidence for the declared model closure.

## Interaction conditions

### Aggregate support

Phase F is closed. It used only the existing Protocol 002 interaction-feedback values `kappa = 3.0, 4.5, 6.0`, fresh five-seed blocks × 20 attempts and independent source reconstruction at every kappa. All three levels remained R4-highrep, so this tested axis did **not** supply the missing R4 boundary.

`interaction kappa` is aggregate positive-feedback/effective interaction support. It is **not partner richness**, connectance, pollinator diversity or interaction-network dimensionality. The present result therefore does not say that network simplification is irrelevant or that all feedback strengths preserve R4.

Per the prospective stop rule, no finer or wider kappa search is opened merely to manufacture a boundary. The committed evidence is [`artifacts/interaction_support/phase_f_summary.json`](artifacts/interaction_support/phase_f_summary.json).

### Reduced-form partner loss

Phase G is closed. It paired the same fresh prepared sources across an intact four-partner control and three predeclared one-partner-loss architectures. The loss architectures had identical partner-richness loss and identical mean retained support; all three moved from the intact R4 classification to R3 while average loss incidence changed little.

This is a bounded **partner-loss / functional-redundancy closure**, not an explicit network model. It does not establish an effect of connectance, nestedness, modularity, adaptive rewiring, partner population dynamics or coextinction. No partner weights or thresholds are retuned after the result. Evidence: [`artifacts/partner_redundancy/phase_g_summary.json`](artifacts/partner_redundancy/phase_g_summary.json).

## Urban and island translation

Urban and island systems are contrasting empirical routes through the condition space, **not ecological equivalents and not demonstrated here to occupy the same regime**.

Because `functional fragmentation` already has an established landscape-ecology usage centred largely on organismal functional connectivity, the manuscript uses **interaction-mediated functional fragmentation** for the focal process here: loss or destabilisation of the biotic interaction support required for realised ecological function while habitat or focal populations may remain present.

Keep these variables separate:

- structural fragmentation / local habitat support and matrix quality;
- realised interaction support and partner composition;
- partner functional diversity, contribution evenness and rewiring;
- biological connectivity separated by pollen, seed/propagule, demographic and partner movement;
- reproductive assurance / alternative functional routes;
- realised functional loss through time;
- genetic state through time.

The next empirical question is:

> **Do different fragmentation mechanisms converge on the same operational interaction-mediated functional-fragmentation regime once state feasibility, realised function and loss reproducibility are measured separately?**

This is a prospective convergence hypothesis, not a current result. A shared regime would not require cities and islands to share geography, network topology, species composition or neutral genetic differentiation.

See [`manuscript/urban_island_regime_tests.md`](manuscript/urban_island_regime_tests.md) and [`manuscript/urban_island_literature_synthesis_2026.md`](manuscript/urban_island_literature_synthesis_2026.md) for the empirical translation and literature audit.

## Scientific sources of truth

Use this order when files disagree:

1. [`docs/HYPOTHESIS_PROGRAM.md`](docs/HYPOTHESIS_PROGRAM.md) — condition-first hypothesis status and stop rules;
2. [`manuscript/hypothesis_condition_ledger.md`](manuscript/hypothesis_condition_ledger.md) — result → condition → boundary ledger;
3. [`manuscript/claim_evidence_map.md`](manuscript/claim_evidence_map.md) — permitted and prohibited manuscript claims;
4. [`manuscript/main_text.md`](manuscript/main_text.md) — publication manuscript downstream of the scientific state;
5. [`manuscript/artifact_index.md`](manuscript/artifact_index.md) and [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) — artifact and two-repository provenance.

Historical Stage/Phase documents are provenance only; they do not override these files.

## Stop rules

- Do not tune `p_star`, migration, interaction kappa, Phase-G partner weights or the R4 gate merely to obtain a desired result.
- Do not inspect warning/diversity fields while selecting an event regime.
- Do not call allele-frequency mixing demographic, pollen or seed dispersal.
- Do not call interaction `kappa` network simplification.
- Do not call Phase G a full network/connectance/rewiring experiment.
- If a conceptual hypothesis is not general, report its recovered condition/boundary instead of widening the search until it appears true.
