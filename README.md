# Eco-genetic warning extensions

This repository tests **when a genetic warning question about ecological function is biologically well posed**. It is the condition-recovery extension of [`eco-genetic-criticality`](https://github.com/zuizui0223/eco-genetic-criticality), pinned at scientific commit `dd8ee379d0d3518194c767d16402042525bc00dc`.

```text
C0  Can an interaction-dependent high-function state exist?
        ↓
C1  Can fragmentation / deterioration disrupt that state?
        ↓
C2  What determines source feasibility and functional loss?
        ├─ loss incidence
        ├─ between-block heterogeneity
        ├─ trajectory identity
        └─ replication / representation boundary
        ↓
C3  Only after C2 is fixed warning-blind: does genetic change precede loss?
        ↓
C4  Is that warning portable across eco-genetic domains?
```

**Warning is a downstream conditional outcome, not the starting hypothesis.**

## Statistical correction to the condition map

The original calibration used preregistered R1–R4 block-rate labels. Those labels remain historical provenance, but low-replicate R3/R4 calls are too sampling-sensitive to serve as biological regime labels by themselves.

The current sources of truth separate:

1. pooled functional-loss incidence;
2. between-block heterogeneity;
3. paired trajectory-identity changes;
4. replication / representation boundaries for load-bearing stochastic findings;
5. downstream warning performance.

Historical R3 is not automatically “seed heterogeneity”, and historical R4 is not proof that warning succeeds.

## Current scientific state

### Inherited mechanism

The parent repository establishes that interaction feedback can support a high-function state and that fragmenting the same prepared state lowers interaction, local effective size and realised high-trait mass before demographic disappearance. In one independently calibrated symmetric benchmark, baseline-relative genetic-diversity erosion preceded observed functional loss; fixed absolute thresholds did not provide a universal rule.

### High-precision extension results

- **Source feasibility is conditional.** 2,269/3,375 original recurrent-transition source attempts supported preparation/projection.
- **The coarse no-domain result remains historical.** Among 648 complete candidates there were 322 rapid-loss, 242 persistence and 84 historical R3/mixed-block candidates; all 15 coordinates remain `no_domain_selected` under the original strict screen.
- **Recurrent turnover defines an incidence frontier.** High-precision pooled loss is about `.682` at `p_star=.325`, `.54` at `.350`, `.407` at `.375` and `.273` at `.400`. No tested frontier condition shows detectable excess block heterogeneity.
- **The historical `m=.10` connectivity signal did not freshly replicate.** In the original Phase-M seed family, `m=.10` alone showed equal-rate `p=.0205`. In one preregistered independent Phase-U ensemble at the same anchor, fresh `m=0/.10` equal-rate p values were `.134/.745`, pooled loss `.540/.551`, and paired McNemar `p=.694`. The historical result is therefore seed-family contingent, not an established reproducible threshold.
- **Process-resolved movement did not recover the historical-family pattern.** Whole-individual `d=.10` and pollen-only `g=.20` closures were block-homogeneous in the historical Phase-M family. Combined with Phase U, no robust portable connectivity heterogeneity effect is established.
- **Aggregate feedback is robust across the tested range.** At `kappa=3.0,4.5,6.0`, high-precision pooled loss is `.499/.573/.598`; all remain intermediate and block-homogeneous.
- **Partner perturbations are bounded negative results.** Reduced-form partner loss and matched-expected-support temporal partner variability changed some stochastic histories but not detected population-level incidence or block heterogeneity. The adaptive-rewiring gate remains closed.
- **Warning remains conditional and portability bounded.** Protocol 003 domains differ in multiple ecological and recurrent-transition parameters, so their warning contrast is portability evidence, not a single-factor effect of transition direction.

All numerical conclusions are finite Type S evidence for the declared model closures.

## Interpretation boundaries

`migration_rate` is allele-frequency mixing only. It is not demographic migration, pollen or seed dispersal, pollinator movement or recolonisation.

The historical Phase-M `m=.10` equal-rate result is retained as evidence from one seed family. **Do not describe it as independently replicated.** Phase U is one independent non-replication and likewise does not prove that no future seed family could ever show heterogeneity.

`interaction kappa` is aggregate positive-feedback/effective interaction support. It is not partner richness, connectance, pollinator diversity or network dimensionality.

The partner layers are bounded and do not simulate a full multispecies dynamic network, coextinction or adaptive rewiring.

## Urban and island translation

Urban and island systems are contrasting empirical routes through the condition space, not ecological equivalents and not demonstrated here to occupy the same regime.

The next empirical question is:

> **Do different fragmentation mechanisms converge on similar combinations of functional-state feasibility, realised interaction support, loss incidence and temporal stability once pollen, seed/propagule, demographic and partner movement are measured separately?**

## Scientific sources of truth

Use this order when files disagree:

1. `docs/HYPOTHESIS_PROGRAM.md`
2. `manuscript/hypothesis_condition_ledger.md`
3. `manuscript/claim_evidence_map.md`
4. `manuscript/main_text.md`
5. `manuscript/artifact_index.md` and `REPRODUCIBILITY.md`

Historical Phase documents are provenance only; they do not override the current condition map.

## Stop rules

- Do not tune `p_star`, migration, interaction kappa, partner weights or the R1–R4 screen merely to obtain a desired result.
- Do not inspect warning/diversity fields while selecting or replicating C2 conditions.
- Do not read historical R3 as proof of biological heterogeneity.
- Do not rerun fresh Phase-U seed ensembles or replace seeds merely to recover `m=.10` significance.
- Do not call allele-frequency mixing demographic, pollen or seed dispersal.
- Do not call interaction `kappa` network simplification.
- Do not open adaptive rewiring merely to rescue the Phase-T null result.
- If a conceptual or stochastic hypothesis is not general or does not replicate, report its recovered condition or boundary instead of continuing until it appears true.
