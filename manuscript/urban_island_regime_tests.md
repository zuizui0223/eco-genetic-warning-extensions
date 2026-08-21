# Urban and island tests of functional fragmentation

## Common empirical question

Urban and island systems are **contrasting tests of the same condition map**, not two decorative applications and not ecological equivalents.

> **When does spatial fragmentation become functional fragmentation?**

The working mechanism is an **interaction bottleneck**: spatial fragmentation may reduce or destabilise effective interaction support before population disappearance. Whether that propagates to functional-trait loss depends on genetic connectivity, reproductive assurance, functional redundancy and local habitat support.

Do not assume that fragmentation automatically means interaction-network simplification. Partner richness may fall, remaining interactions may rewire toward generalists, connectance can change in either direction, and ecological function can be buffered or lost despite similar spatial patchiness.

The empirical state variables must therefore remain separate:

1. spatial fragmentation / local habitat support;
2. realised interaction support and partner composition;
3. effective genetic connectivity;
4. reproductive assurance / functional redundancy;
5. realised functional performance or loss;
6. local genetic state and among-patch differentiation through time.

## Model-facing conditions already recovered

### Recurrent state turnover

The common-grid and refined campaigns show that recurrent state turnover changes source feasibility and the realised functional-loss regime. A reproducible intermediate-risk R4 condition exists, but narrowly, around one tested recurrent-transition anchor.

### Effective genetic connectivity

At that recovered anchor, allele-frequency mixing `m=0–0.05` retained R4-highrep, whereas `m=0.10–0.20` produced R3-highrep. Paired trajectories switched loss status in both directions. Thus connectivity can change **which stochastic realisations lose function** and whether functional loss remains reproducible without acting as a universal rescue/collapse axis.

The simulator's `migration_rate` is allele-frequency mixing only. It is not demographic migration, pollen/seed movement, pollinator movement or recolonisation.

### Aggregate interaction support — active Phase F

Phase F directly tests the existing interaction-feedback parameter at the pre-existing `kappa=3.0,4.5,6.0` levels with fresh source reconstruction at each level.

This is a test of **aggregate effective interaction support / feedback strength**. It is not a direct simulation of partner richness, connectance, pollinator diversity or network dimensionality. Those are empirical mechanisms that may alter effective support and would require a new explicit network closure to model directly.

## Urban prediction set

Urban landscapes are useful because geographic distance and biological connectivity often decouple.

### U1 — spatial fragmentation is not sufficient

Two equally fragmented urban patch networks can occupy different functional regimes if pollinator movement, introductions, corridors or matrix permeability generate different effective interaction support or gene flow.

### U2 — interaction bottleneck can precede genetic isolation

If pollinator/interaction support collapses while gene flow is maintained by mobile generalists, horticultural movement or other routes, ecological function can deteriorate without immediate strong loss of neutral diversity or increase in genetic differentiation.

### U3 — specialist systems should cross the functional boundary earlier

Lineages dependent on a narrow or habitat-sensitive interaction partner set should enter source-limited or rapid-loss regimes under weaker spatial disruption than lineages with redundant/generalist interactions, all else equal.

### U4 — rewiring can buffer or destabilise

Loss of partners need not equal loss of function if remaining interactions compensate. The empirical prediction is therefore about **effective interaction support and redundancy**, not raw partner richness.

### U5 — connectivity can change reproducibility rather than mean risk

Urban networks with similar mean reproductive failure may differ in among-patch/year heterogeneity. Phase-E logic predicts that this difference can determine whether a warning comparison is estimable even when pooled failure rates are close.

### Minimum urban measurements

- patch area, isolation and matrix resistance;
- visitation/interaction rates and partner identities;
- successful compatible pollen delivery or the appropriate functional endpoint;
- contemporary gene flow / paternity / genomic connectivity;
- repeated local functional success/failure;
- temporal effective size/diversity and among-patch differentiation;
- disturbance, heat, pollution or management covariates when relevant.

## Island prediction set

Island systems are useful because geographic isolation, colonisation filters, interaction availability and reproductive strategy can be strongly separated among islands or archipelagos.

### I1 — mutualist-limited source feasibility

Small/remote islands with low effective mutualist support should have lower high-function source feasibility for obligately outcrossing or specialist-dependent lineages.

### I2 — reproductive assurance decouples persistence from function

Self-compatibility, autonomous selfing, vegetative reproduction or generalised interactions may preserve population persistence after the original interaction-dependent function has weakened. Demographic persistence therefore does not guarantee persistence of the focal ecological function.

### I3 — pollination-niche rescue is a condition, not an exception

A remote island with a stable effective pollination niche may retain a high-function state despite strong geographic isolation. Distance alone should therefore not determine the predicted regime.

### I4 — stepping-stone connectivity has two consequences

Among-island gene flow can support local persistence while homogenising allele frequencies. Low differentiation can therefore coexist with ecological vulnerability and need not imply strong local interaction support.

### I5 — warning-evaluable systems should be intermediate in functional risk, not necessarily geography

The most informative island systems for genetic warning should be those in which interaction-dependent function is vulnerable but functional loss is neither nearly deterministic nor nearly absent across comparable populations/years. This need not coincide with the most isolated islands.

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
local habitat support + effective interaction support
        ↓
source feasibility / functional persistence
        ↕
effective genetic connectivity + reproductive assurance
        ↓
functional-loss regime and its reproducibility
        ↓
only if evaluable: genetic-warning performance
```

Cities are particularly useful for decoupling spatial patchiness from movement; islands are particularly useful for decoupling geographic isolation from interaction availability and reproductive assurance. Both can test whether different mechanisms converge on the same eco-genetic regime.

## Concrete empirical test

Use a replicated network in which the same biological lineage spans gradients of local support, realised interaction support and effective connectivity. Classify population×time units **first** by functional event regime—persistence, rapid loss, heterogeneous, or reproducible intermediate risk. Analyse genetic warning only inside the independently defined reproducible regime.

For an explicit interaction-network test, additionally quantify partner richness, interaction-strength evenness, specialisation, rewiring and functional redundancy. These quantities should be tested as candidate mechanisms of aggregate interaction support; they must not be silently substituted by the model's `kappa`.

## Evidence anchors

- Parent interaction/fragmentation mechanism and migration theorem: pinned `eco-genetic-criticality` scientific state.
- Recurrent-transition and connectivity conditions: `docs/HYPOTHESIS_PROGRAM.md`, `manuscript/hypothesis_condition_ledger.md`, and committed machine-readable summaries under `artifacts/`.
- Miles et al. (2019), *Molecular Ecology*, doi:10.1111/mec.15221 — heterogeneous effects of urbanisation on genetic diversity/connectivity.
- Youngsteadt & Keighron (2023), *Annual Review of Ecology, Evolution, and Systematics*, doi:10.1146/annurev-ecolsys-102221-044616 — urban pollination signal and strong context dependence.
- Schrader et al. (2021), *Biological Reviews*, doi:10.1111/brv.12782 — island functional-biogeography hypotheses involving isolation, mutualists and reproductive strategy.
- Grossenbacher et al. (2017), *New Phytologist*, doi:10.1111/nph.14534 — island over-representation of self-compatibility in the sampled families.
- Xu et al. (2018), *Scientific Reports* 8:13765, doi:10.1038/s41598-018-32143-5 — persistence of obligate outcrossing when an effective island pollination niche is available.
