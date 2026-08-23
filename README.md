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
        └─ trajectory identity under paired perturbation
        ↓
C3  Only after C2 is fixed warning-blind: does genetic change precede loss?
        ↓
C4  Is that warning portable across eco-genetic domains?
```

**Warning is a downstream conditional outcome, not the starting hypothesis.**

## Statistical correction to the condition map

The original calibration used preregistered R1–R4 block-rate labels. Those labels remain historical provenance, but the precision programme showed that low-replicate R3/R4 calls are too sampling-sensitive to serve as biological regime labels by themselves.

The current sources of truth therefore separate:

1. pooled functional-loss incidence;
2. between-block heterogeneity;
3. paired trajectory-identity changes;
4. downstream warning performance.

Historical R3 is not automatically “seed heterogeneity”, and historical R4 is not proof that warning succeeds.

## Current scientific state

### Inherited mechanism

The parent repository establishes that interaction feedback can support a high-function state and that fragmenting the same prepared state lowers interaction, local effective size and realised high-trait mass before demographic disappearance. In one independently calibrated symmetric benchmark, baseline-relative genetic-diversity erosion preceded observed functional loss; fixed absolute thresholds did not provide a universal rule.

### High-precision extension results

- **Source feasibility is conditional.** 2,269/3,375 original recurrent-transition source attempts supported preparation/projection.
- **The coarse no-domain result remains historical.** Among 648 complete candidates there were 322 rapid-loss, 242 persistence and 84 historical R3/mixed-block candidates; all 15 coordinates remain `no_domain_selected` under the original strict screen.
- **Recurrent turnover defines an incidence frontier.** High-precision pooled loss is about `.682` at `p_star=.325`, `.54` at `.350`, `.407` at `.375` and `.273` at `.400`. No tested frontier condition shows detectable excess block heterogeneity.
- **Connectivity is non-monotone.** Pooled loss remains near `.54–.56` across `m=0–.20`; only `m=.10` shows high-precision excess between-block heterogeneity (`p=.0205`). Paired marginal-risk tests are null at all nonzero levels.
- **Aggregate feedback is robust across the tested range.** At `kappa=3.0,4.5,6.0`, high-precision pooled loss is `.499/.573/.598`; all predeclared kappa 3.0/4.5/6.0 remain R4 and no level shows detectable excess block heterogeneity. Phase F is closed.
- **Reduced-form partner loss is a negative population-level result.** Intact/even/graded/dominant conditions have pooled loss `.556/.544/.565/.549`; all remain inside the historical intermediate-incidence screen and paired McNemar tests are non-significant. Partner loss changes many individual stochastic histories but not detected marginal incidence or block heterogeneity.
- **Warning remains conditional and portability bounded.** Protocol 003 domains differ in multiple ecological and recurrent-transition parameters, so their warning contrast is portability evidence, **not a single-factor effect of transition direction**.

All numerical conclusions are finite Type S evidence for the declared model closures.

## Interpretation boundaries

`migration_rate` is allele-frequency mixing only. It is not demographic migration, pollen or seed dispersal, pollinator movement or recolonisation.

`interaction kappa` is aggregate positive-feedback/effective interaction support. It is **not partner richness**, connectance, pollinator diversity or network dimensionality.

The partner layer is reduced-form. It does not simulate explicit connectance, nestedness, modularity, partner demography, coextinction or adaptive rewiring.

## Urban and island translation

Urban and island systems are contrasting empirical routes through the condition space, **not ecological equivalents and not demonstrated here to occupy the same regime**.

The manuscript uses **interaction-mediated functional fragmentation** for loss or destabilisation of biotic interaction support required for realised ecological function while focal populations or habitat patches may remain present. This is distinct from established organism-centred functional connectivity.

The next empirical question is:

> **Do different fragmentation mechanisms converge on similar combinations of functional-state feasibility, realised interaction support, loss incidence and temporal stability once biological movement and genetic state are measured separately?**

A field test should measure habitat amount/configuration and matrix quality; partner identity and interaction strength; functional diversity, turnover and rewiring; pollen, seed/propagule, demographic and partner movement separately; reproductive assurance; realised function through time; and genetic state through time.

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
- Do not inspect warning/diversity fields while selecting C2 conditions.
- Do not read historical R3 as proof of biological heterogeneity.
- Do not call allele-frequency mixing demographic, pollen or seed dispersal.
- Do not call interaction `kappa` network simplification.
- Do not call the reduced-form partner layer a full network/connectance/rewiring experiment.
- If a conceptual hypothesis is not general, report its recovered condition or boundary instead of widening the search until it appears true.
