# Urban and island tests of functional fragmentation

## Common empirical question

Urban and island systems are **contrasting tests of the same condition map**, not ecological equivalents.

> **When does spatial fragmentation become functional fragmentation?**

The working mechanism is an **interaction bottleneck**: spatial fragmentation may reduce or destabilise effective interaction support before population disappearance. Whether that propagates to functional-trait loss depends on genetic connectivity, reproductive assurance, functional redundancy and local habitat support.

Do not assume that fragmentation automatically means interaction-network simplification. Partner richness may fall, remaining interactions may rewire toward generalists, connectance can change in either direction, and ecological function can be buffered or lost despite similar spatial patchiness.

Keep these empirical state variables separate:

1. spatial fragmentation / local habitat support;
2. realised interaction support and partner composition;
3. effective genetic connectivity;
4. reproductive assurance / functional redundancy;
5. realised functional performance or loss;
6. local genetic state and among-patch differentiation through time.

## What the model condition map now says

### Recurrent state turnover

The common-grid and refined campaigns show that recurrent state turnover changes both source feasibility and the realised functional-loss regime. A reproducible intermediate-risk R4 condition exists, but narrowly, around one tested recurrent-transition anchor.

### Effective genetic connectivity

At that anchor, allele-frequency mixing `m=0–0.05` retained R4-highrep whereas `m=0.10–0.20` produced R3-highrep. Paired trajectories switched loss status in both directions. Thus connectivity can change **which stochastic realisations lose function** and whether functional loss remains reproducible without acting as a universal rescue/collapse axis.

The simulator's `migration_rate` is allele-frequency mixing only. It is not demographic, pollen/seed, pollinator or recolonisation movement.

### Aggregate interaction support

Phase F is closed. It tested the pre-existing `kappa=3.0,4.5,6.0` levels with fresh independent source reconstruction at each level.

| interaction kappa | source/baseline eligible | pooled loss | regime |
|---:|---:|---:|---|
| 3.0 | 77/100 | 0.468 | R4-highrep |
| 4.5 | 94/100 | 0.521 | R4-highrep |
| 6.0 | 87/100 | 0.552 | R4-highrep |

All five seed-block loss rates at all three kappa levels remained in the R4 band. Thus, at this recovered anchor, the predeclared aggregate interaction-support range **did not move the system out of R4**, even though source/baseline eligibility varied descriptively.

This sharpens the empirical translation: interaction processes may affect at least two distinct stages—**whether a high-function state is established/maintained at all**, and **how reproducible loss is once that state exists**. Phase F gives evidence for robustness of the second stage over the tested range, not evidence that the first stage or real interaction networks are unimportant.

`interaction kappa` is aggregate feedback strength. It is not partner richness, connectance, pollinator diversity or network dimensionality. An explicit network-simplification hypothesis still requires direct measurements or a newly declared network model.

## Urban predictions

Urban landscapes are useful because spatial patchiness, biological movement and interaction structure can decouple.

### U1 — spatial fragmentation is not sufficient

Equally fragmented urban patch networks can differ in functional state if pollinator movement, introductions, corridors, matrix permeability or local resource support differ.

### U2 — interaction bottleneck can precede genetic isolation

If interaction support collapses while gene flow remains high through mobile generalists, horticultural movement or other routes, ecological function can deteriorate without an immediate strong neutral-genetic isolation signal.

### U3 — interaction structure should be tested first against source/function maintenance

Because Phase F retained R4 across all three aggregate support levels while source eligibility varied, the first empirical question for partner loss or rewiring should be whether it changes **functional-state establishment and maintenance**, not an assumption that it must alter warning estimability.

Specialist systems and systems with low functional redundancy are natural candidates for crossing this source/function boundary earlier.

### U4 — rewiring can buffer or destabilise

Raw partner richness is insufficient. Quantify interaction strength, specialisation, rewiring and functional redundancy because fewer partners may still provide comparable effective support—or the same number of partners may provide much less.

### U5 — connectivity can alter reproducibility without a large mean-risk shift

Urban networks with similar pooled functional-failure rates may differ strongly in among-patch/year heterogeneity. Phase-E logic predicts that this can determine whether a warning comparison is estimable.

### Minimum urban measurements

- patch area, isolation and matrix resistance;
- visitation/interaction rates and partner identities;
- interaction-strength evenness, specialisation and rewiring where possible;
- successful compatible pollen delivery or the relevant functional endpoint;
- contemporary gene flow / paternity / genomic connectivity;
- repeated local functional success/failure;
- temporal effective size/diversity and among-patch differentiation;
- disturbance, heat, pollution and management covariates when relevant.

## Island predictions

Island systems are useful because geographic isolation, colonisation filters, interaction availability and reproductive strategy can be separated among islands or archipelagos.

### I1 — mutualist limitation should be tested as a source/function boundary

Small or remote islands with weak effective mutualist support should be less likely to establish or maintain the interaction-dependent high-function state in obligately outcrossing or specialist-dependent lineages. Phase F suggests not assuming that moderate variation in aggregate support must also change the post-source R4 classification.

### I2 — reproductive assurance decouples persistence from function

Self-compatibility, autonomous selfing, vegetative reproduction or generalised interactions may preserve population persistence after the original interaction-dependent function weakens. Demographic persistence therefore does not guarantee persistence of the focal ecological function.

### I3 — pollination-niche rescue is a condition, not an exception

A remote island with a stable effective pollination niche may retain a high-function state despite strong geographic isolation. Distance alone should not determine the predicted regime.

### I4 — stepping-stone connectivity has two consequences

Among-island gene flow can support local persistence while homogenising allele frequencies. Low differentiation can therefore coexist with ecological vulnerability and need not imply strong local interaction support.

### I5 — warning-evaluable systems are intermediate in functional risk, not necessarily geography

The most informative island systems for genetic warning are those in which functional loss is neither nearly deterministic nor nearly absent across comparable populations/years. This need not coincide with the most isolated islands.

### Minimum island measurements

- island area, isolation and stepping-stone structure;
- colonisation/population history where available;
- mutualist/pollinator composition and realised interaction rate;
- breeding system, self-compatibility and reproductive assurance;
- realised functional/reproductive success through time;
- contemporary effective gene flow;
- temporal effective size/diversity and among-island differentiation.

Repeated populations of the same lineage or a tightly controlled clade are preferable to an unconstrained island-mainland species comparison.

## Urban–island comparison

The common comparison is not `city versus island` but:

```text
spatial fragmentation
        ↓
local habitat support + realised interaction structure
        ↓
source feasibility / functional-state maintenance
        ↕
effective genetic connectivity + reproductive assurance
        ↓
functional-loss regime and its reproducibility
        ↓
only if evaluable: genetic-warning performance
```

Cities are especially useful for decoupling spatial patchiness from movement. Islands are especially useful for decoupling geographic isolation from interaction availability and reproductive assurance. Both can test whether different mechanisms converge on the same eco-genetic state.

## Concrete empirical test

Use a replicated network in which the same lineage spans gradients of spatial support, realised interaction support and effective connectivity. Measure **source/function maintenance first**; then classify population×time units by functional event regime—persistence, rapid loss, heterogeneous or reproducible intermediate risk. Analyse genetic warning only inside the independently defined reproducible regime.

For an explicit interaction-network test, quantify partner richness, interaction-strength evenness, specialisation, rewiring and functional redundancy as candidate mechanisms of effective interaction support. Do not substitute these quantities silently with model `kappa`.

## Evidence anchors

- Parent interaction/fragmentation mechanism and migration theorem: pinned `eco-genetic-criticality` scientific state.
- Recurrent-turnover, connectivity and interaction-support conditions: `docs/HYPOTHESIS_PROGRAM.md`, `manuscript/hypothesis_condition_ledger.md` and committed summaries under `artifacts/`.
- Miles et al. (2019), *Molecular Ecology*, doi:10.1111/mec.15221 — heterogeneous urbanisation effects on genetic diversity/connectivity.
- Youngsteadt & Keighron (2023), *Annual Review of Ecology, Evolution, and Systematics*, doi:10.1146/annurev-ecolsys-102221-044616 — urban pollination signal and context dependence.
- Schrader et al. (2021), *Biological Reviews*, doi:10.1111/brv.12782 — island functional-biogeography hypotheses involving isolation, mutualists and reproductive strategy.
- Grossenbacher et al. (2017), *New Phytologist*, doi:10.1111/nph.14534 — island over-representation of self-compatibility in sampled families.
- Xu et al. (2018), *Scientific Reports* 8:13765, doi:10.1038/s41598-018-32143-5 — persistence of obligate outcrossing when an effective island pollination niche is available.
