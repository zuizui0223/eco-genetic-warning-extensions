# Urban and island tests of interaction-mediated functional fragmentation

## Common empirical question

Urban and island systems are **contrasting causal routes, not ecological equivalents**.

> **Do different fragmentation mechanisms converge on similar interaction-mediated functional-loss distributions?**

This is a prospective empirical hypothesis, not a conclusion of the current simulations. `Functional fragmentation` already has an established landscape-ecology usage centred largely on organismal functional connectivity. Here **interaction-mediated functional fragmentation** means loss or destabilisation of the biotic interaction support required for realised ecological function while habitat patches or focal populations may remain present.

Do not assume that fragmentation automatically means **network simplification**. Habitat amount, configuration and matrix quality can differ in effect; partner identities can turn over; interactions can rewire; functional diversity can change independently of species richness; and gene flow can remain high despite structural patchiness.

## What the current model implies

### 1. State establishment and loss are separate

Recurrent state turnover changes whether a high-function source can be established. Phase F further showed that aggregate interaction feedback can alter source eligibility while leaving the subsequent finite loss panel broadly intermediate. Natural surveys should therefore distinguish **whether the functional state exists** from **how it subsequently fails**.

### 2. Mean loss and among-unit heterogeneity are separate

Phase G changed block-to-block variability much more than mean failure incidence. Phase J then proved that a hard all-block R4 label can change across independent finite panels at one fixed biological condition. Therefore empirical urban/island work should report the **distribution of functional loss across comparable populations or years**, not reduce each system immediately to one categorical warning-evaluable label.

The main upstream quantities are:

- central functional-loss incidence;
- among-population / among-year heterogeneity;
- tail probability of near-persistence or near-deterministic loss;
- uncertainty in those quantities.

A finite all-block certificate may still be used to decide whether one particular warning-validation dataset is usable, but it is a sampling-design rule rather than a biological regime.

### 3. Network recovery is not functional recovery

Phase H explicitly recovered network structure after partner loss: active edges increased `3→5`, realised connectance `.500→.833`, and match-weighted support `.750→.844` of intact support. Yet pooled functional loss changed only `.430→.419` and the downstream loss panel did not recover its finite certificate.

Thus restoration monitoring should not stop at partner richness, connectance, visitation or aggregate interaction support. A recovered-looking network can still generate a different functional-loss distribution. Realised function must be measured directly.

### 4. Connectivity must be process resolved

Legacy model `migration_rate` is allele-frequency mixing only. Phase I showed that one regional paternal pollen process has an exact narrow bridge to that operator: `g=.20` regional pollen is equivalent to `m=.10` because, under the declared diploid closure, `m=g/2`. Changing the pollen kernel changed which trajectories failed while leaving mean incidence and the finite certificate similar.

This supports separating:

- pollen-mediated gene flow;
- seed / propagule movement;
- demographic movement / recolonisation;
- movement of interaction partners.

These processes can have different spatial kernels, timescales and functional consequences.

## Urban route

Urban landscapes are useful because structural patchiness, biological movement and interaction structure can decouple.

### U1 — neutral genetic connectivity can remain high while function changes

Urban plant genetic studies show highly heterogeneous responses to urbanisation, and gene flow can persist through long-distance or human-mediated movement. At the same time, heat, pollution, management and resource turnover can filter partner composition and interaction structure. An urban population can therefore be **genetically connected yet interaction-functionally fragmented**.

### U2 — urban restoration should test function, not green-space geometry alone

Two green-space networks with similar patch area or isolation can differ in partner functional diversity, interaction strength, rewiring and realised pollen delivery. Structural connectivity is necessary context, not a direct functional endpoint.

### U3 — repeated years are part of the estimand

Phase J implies that a single small set of years or parks can generate a brittle categorical label. Repeated populations × years should instead be used to estimate the distribution of reproductive or ecological failure and its temporal/spatial heterogeneity.

### Minimum urban measurements

1. habitat amount/configuration and matrix resistance/quality;
2. visitation/interaction rates and partner identities;
3. partner functional traits, interaction-strength evenness and rewiring;
4. compatible pollen delivery, seed set or another realised focal function;
5. pollen, propagule, demographic and partner movement where relevant;
6. repeated functional success/failure across populations and years;
7. temporal genetic diversity/effective size and among-patch differentiation;
8. heat, pollution, disturbance and management covariates.

## Island route

Island systems provide a different causal decomposition: persistent geographic isolation combines with colonisation filters, mutualist availability, regional species turnover, stepping-stone structure and reproductive assurance.

### I1 — geographic isolation alone does not define functional vulnerability

Oceanic-island pollination networks are often smaller and lower in interaction diversity than mainland networks, but area and distance do not determine every network property. Mutualist availability and partner functional identity can alter whether an interaction-supported state is established at all.

### I2 — reproductive assurance can decouple persistence from focal function

Self-compatibility, autonomous selfing, vegetative reproduction or generalised interactions can preserve demographic persistence after a particular interaction-dependent function weakens. Baker's law concerns capacity for uniparental reproduction under colonisation or mate limitation, not universal autonomous selfing on islands.

### I3 — stepping-stone connectivity has multiple meanings

Low neutral differentiation can coexist with weak local interaction support, and strong differentiation does not itself measure functional isolation. Pollen, seed/propagule and partner movement should be estimated separately where possible.

### I4 — repeated island populations/years should estimate a loss distribution

The relevant comparison is not whether one island passes a binary R4 rule. It is whether island populations with different isolation, mutualist filters or reproductive assurance show different distributions of realised functional failure across comparable periods.

### Minimum island measurements

1. island area, habitat amount, isolation and stepping-stone structure;
2. colonisation/population history where available;
3. mutualist/pollinator composition, functional diversity and realised interaction rate;
4. breeding system, self-compatibility and reproductive assurance;
5. realised reproductive/ecological function through time;
6. pollen, seed/propagule and demographic connectivity;
7. repeated functional success/failure across populations/years;
8. temporal genetic diversity/effective size and among-island differentiation.

Repeated populations of the same lineage or a tightly controlled clade are preferable to an unconstrained island-mainland species contrast.

## What convergence would mean

The shared comparison is a **distributional state map**, not `city versus island` and not a binary R4 map:

```text
structural fragmentation + matrix context
                ↓
interaction support / partner architecture
                ↓
functional-state feasibility and realised function
                ↕
process-resolved connectivity + reproductive assurance
                ↓
functional-loss distribution
    ├─ central incidence
    └─ among-unit heterogeneity / tails
                ↓
finite validation design, if needed
                ↓
genetic-warning availability / timing
```

Cities and islands would be said to converge only if different causal routes produced similar combinations of state feasibility, realised function, central loss incidence and among-unit heterogeneity under comparable observation windows. They need not share network topology, species composition, neutral genetic differentiation or geography.

## Concrete empirical test

Use replicated populations or population-years spanning gradients of structural support, realised interaction support and process-resolved connectivity. Measure **state/function maintenance first**. Then model the distribution of functional outcomes across comparable units, including among-unit heterogeneity. Only after that distribution is independently characterised should a finite subset be used to evaluate whether genetic change precedes loss.

For explicit interaction tests, quantify partner richness, functional diversity, edge strength, specialisation, turnover and rewiring. Do not substitute those variables silently with model `kappa`, Phase-G weights or Phase-H connectance.

## Evidence anchors

### Current model

- Parent fragmentation mechanism: pinned `eco-genetic-criticality` scientific state.
- Phase E: allele-frequency connectivity and bidirectional loss-status switching.
- Phase F: scalar interaction-support/source-feasibility separation.
- Phase G: partner-loss mean-risk/reproducibility separation.
- Phase H: explicit network recovery without functional-loss recovery; run `32453377127`, artifact `9436467391`.
- Phase I: regional pollen `g=.20` exact legacy `m=.10` bridge plus regional/ring kernel comparison; run `32454142670`, artifact `9436762723`.
- Phase J: fixed-condition classification stability; 19/20 blocks inside the operational band and exact 75%/25% five-panel certificate split; run `32454874360`, artifact `9437232755`.

### Literature anchors

- Benitez et al. (2025), *Trends in Ecology & Evolution*, doi:10.1016/j.tree.2024.09.004 — organism-centred functional fragmentation/connectivity framing.
- Fletcher et al. (2026), *Nature Ecology & Evolution*, doi:10.1038/s41559-026-03095-1 — habitat loss, fragmentation and matrix quality as distinct landscape processes.
- Ward et al. (2026), *Nature Reviews Biodiversity*, doi:10.1038/s44358-026-00159-9 — rewiring and interaction-strength change in network resilience.
- Hiraiwa & Ushimaru (2024), *Functional Ecology*, doi:10.1111/1365-2435.14527 — pollinator functional diversity, trait matching and pollination function.
- Hardion et al. (2026), *Perspectives in Plant Ecology, Evolution and Systematics*, doi:10.1016/j.ppees.2025.125920 — heterogeneous urban plant genetic connectivity.
- Traveset et al. (2016), *Global Ecology and Biogeography*, doi:10.1111/geb.12362 — mainland/insular pollination-network patterns.
- Delavaux et al. (2024), *Nature*, doi:10.1038/s41586-024-07110-y — mutualist filtering as a candidate island mechanism; retain critique/response caveat.
- Pannell et al. (2015), *New Phytologist*, doi:10.1111/nph.13539 — Baker's-law boundary.
- Peled, Kim & Greenbaum (2026), *PNAS*, doi:10.1073/pnas.2515033123 — genetic early warning under fragmentation; the present target is instead interaction-dependent functional loss and upstream event-process estimability.
