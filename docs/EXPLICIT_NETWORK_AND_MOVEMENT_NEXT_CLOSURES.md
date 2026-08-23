# Explicit network and biological-movement closures: unresolved next-model work

## Purpose

The current condition programme has now tested recurrent state turnover, allele-frequency connectivity, aggregate interaction support, and a reduced-form matched one-partner-loss perturbation. Two ecologically important axes remain genuinely unresolved:

1. explicit interaction-network dynamics, especially adaptive rewiring and partner population dynamics;
2. biologically explicit movement, separating pollen, seed/propagule, demographic and partner movement.

These are **not missing parameter sweeps in the current model**. They require new state variables and/or life-cycle operators. They must therefore not be backfilled by relabelling existing parameters.

## What Phase G did and did not close

Phase G established a bounded reduced-form result: at one fresh R4 anchor, matched one-partner loss moved the predeclared classifier from R4 to R3 in three partner-contribution architectures while pooled loss incidence remained similar. Contribution concentration itself did not separate regimes.

Phase G did not represent:

- a bipartite or multilayer interaction matrix;
- partner abundances or partner extinction dynamics;
- connectance, nestedness or modularity as state variables;
- adaptive or opportunistic rewiring;
- trait matching constraints on rewiring;
- spatial movement of interaction partners;
- coextinction cascades.

Therefore no claim about those mechanisms is available from Phase G.

## Minimum explicit-network closure required before a rewiring test

A scientifically interpretable rewiring extension should introduce at minimum:

1. **partner state** — explicit identity and abundance/availability for each partner in each patch;
2. **interaction state** — a patch-specific weighted interaction matrix or equivalent edge-strength representation;
3. **functional mapping** — a declared mapping from realised partner interactions to focal ecological function;
4. **partner loss process** — exogenous removal and/or endogenous partner decline defined independently of the focal warning statistic;
5. **rewiring rule** — a prospective rule specifying which surviving edges can form or strengthen, with explicit constraints from availability or trait matching;
6. **network diagnostics** — connectance, interaction-strength evenness, functional partner diversity and rewiring recorded as diagnostics rather than silently collapsed into scalar `kappa`;
7. **warning-blind regime classification** — source/function and loss-regime selection completed before genetic-warning fields are exposed.

A first explicit-network experiment should compare at least `no rewiring` versus a biologically constrained rewiring rule under the **same initial network, partner loss, deterioration schedule and random source identity**. Rewiring intensity should not be tuned after observing R4/R3 outcomes.

## Why existing `interaction kappa` cannot substitute

`interaction kappa` is aggregate positive-feedback/effective interaction support. It does not encode which partner supplies support, which edge is lost, whether a new edge forms, or whether surviving partners compensate. Phase F therefore answers a scalar support question, not a network-topology question.

## Minimum biological-movement closure required before a dispersal test

The pinned parent model's `migration_rate` changes allele frequencies through mixing toward the population-weighted patch mean. It does **not** move individuals, trait-bin occupancy, pollen, seeds or interaction partners.

A biological-movement extension must choose and declare a specific process rather than a generic `dispersal` parameter.

### Pollen-mediated gene flow

Minimum additions:

- male-gamete contribution among patches;
- distance/matrix or partner-mediated pollen-transfer kernel;
- explicit effect on offspring allele frequencies without direct movement of established individuals;
- optional dependence on realised pollinator interaction support if pollination is the focal system.

### Seed / propagule movement

Minimum additions:

- movement of recruits or propagules among patches;
- destination-dependent establishment or survival;
- genotype/trait state carried with propagules;
- matrix or distance dependence.

### Demographic movement / recolonisation

Minimum additions:

- movement of individuals or demographic mass;
- explicit effects on local abundance and extinction/recolonisation;
- genotype and realised trait state transported with migrants.

### Partner movement

Minimum additions:

- movement/availability dynamics for interacting partners;
- effect on realised interaction edges and focal function;
- potentially a timescale distinct from focal-organism gene flow.

These processes can differ in direction, timescale and ecological effect; they should not be collapsed into one scalar connectivity variable.

## Cross-system reason this distinction matters

The literature audit indicates that urban and island systems can decouple these processes in different ways. Urban habitat can be spatially patchy while gene flow remains substantial through long-distance or human-mediated movement, yet local interaction composition changes. Oceanic islands can have strong geographic isolation while mutualist availability, stepping-stone structure and reproductive assurance alter whether a focal function is established or maintained.

Therefore the next urban–island programme should compare **process-resolved connectivity and interaction-mediated functional state**, not geography alone.

## Prospective convergence hypothesis

The next empirical/model question remains:

> Do different fragmentation mechanisms converge on the same operational interaction-mediated functional-fragmentation regime once state feasibility, realised interaction support, biological connectivity and functional-loss reproducibility are measured separately?

This is not a result of the current model. It becomes testable only after the relevant network and movement processes are represented or measured explicitly.

## Stop rule for the present manuscript

Do not add a synthetic rewiring or biological-dispersal parameter to the current paper merely to close every ecological mechanism. Phase G closes the reduced-form partner-loss question. Explicit rewiring and process-resolved biological movement are **next-model hypotheses** unless a new prospective closure is fully specified before outcomes are generated.
