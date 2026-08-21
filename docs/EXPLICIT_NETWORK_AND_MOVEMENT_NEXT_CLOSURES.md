# Explicit network and biological-movement closures

## Current status

The programme has now tested:

1. recurrent state turnover;
2. allele-frequency connectivity;
3. aggregate interaction support;
4. reduced-form matched partner loss;
5. one prospectively fixed explicit interaction-rewiring rule.

The canonical explicit-rewiring test is now **closed**. The remaining major unrepresented mechanism is biologically explicit movement, separated into pollen, seed/propagule, demographic and partner movement. Broader network dynamics with endogenous partner abundance or coextinction also remain outside the current closure.

These are not missing parameter sweeps. They require new state variables and/or life-cycle operators and must not be backfilled by relabelling existing parameters.

## What Phase G established

Phase G recovered a bounded reduced-form result: at one fresh R4 anchor, matched one-partner loss moved the predeclared classifier from R4 to R3 in three partner-contribution architectures while pooled loss incidence remained similar. Contribution concentration itself did not separate regimes.

Phase G did not represent explicit partner nodes, latent edges or rewiring, motivating a new prospective network closure.

## What Phase H added

Phase H represented one focal interaction network with:

- six candidate partner nodes;
- four initially active primary edges;
- two latent available partners;
- explicit edge strengths;
- fixed trait-match scores;
- per-edge capacities;
- balanced exogenous primary-partner loss;
- dynamic trait- and capacity-constrained rewiring;
- explicit active-edge, connectance and functional-support diagnostics.

The same high-function source, lost primary partner, deterioration schedule and trajectory seed were paired across:

1. intact control;
2. partner loss without rewiring;
3. the same partner loss with constrained rewiring.

The opening rule required fresh intact `R4_highrep` and fresh no-rewiring loss `R3_highrep`. Both were recovered, so the rescue comparison was valid.

The rewiring condition remained `R3_highrep`, giving prospective classification **`not_rescued`**.

### Network state recovered, loss-regime reproducibility did not

The rewiring rule changed the network substantially:

| diagnostic | no rewiring | constrained rewiring |
|---|---:|---:|
| final active edges | 3 | 5 |
| realised connectance | 0.500 | 0.833 |
| latent edges activated | 0 | 2 |
| rewired edge effort | 0 | 0.125 |
| final support multiplier | 0.750 | 0.844 |

Yet pooled functional loss changed only `0.430 → 0.419`, and the final seed block remained below the R4 lower bound (`0.294`). The rewiring condition therefore remained R3.

The bounded conclusion is:

> **Network structural recovery and match-weighted interaction-support recovery were not sufficient to recover functional-loss regime reproducibility under this predeclared closure.**

This strengthens the separation among network state, functional-loss incidence, event reproducibility and downstream warning estimability.

Phase-H evidence: `artifacts/explicit_rewiring/phase_h_summary.json`; workflow run `32453377127`; artifact `9436467391`.

## Stop rule for explicit rewiring

Phase H is closed. Do not vary the partner pool, match scores, edge capacities, rewiring fraction, rewiring window, loss identity, seeds or R4 thresholds merely to obtain a rescue.

The result does not imply that rewiring is universally ineffective. A different rewiring mechanism may be scientifically justified later only as a separately motivated and prospectively declared model, not as a continuation of Phase-H tuning.

## Why existing `interaction kappa` still cannot substitute for network state

`interaction kappa` is aggregate positive-feedback/effective interaction support. It does not encode which partner supplies support, which edge is lost, whether a latent edge activates, or how interaction effort is redistributed. Phase F and Phase H therefore address distinct axes.

Conversely, Phase H shows that higher realised connectance and greater network-derived support do not automatically restore the downstream functional-loss regime. This makes it especially unsafe to use any one network metric as a stand-alone proxy for functional resilience.

## Remaining biological-movement closure

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

## Cross-system implication

The urban–island literature audit makes process-resolved movement the natural next axis. Urban habitat can be spatially patchy while focal gene flow or anthropogenic movement remains substantial, even as local interaction composition changes. Oceanic islands can have strong geographic isolation while mutualist availability, stepping-stone structure and reproductive assurance alter whether a focal function is established or maintained.

Phase H adds an important warning to that programme: even if an interaction network appears structurally reconnected, the relevant functional-loss process may remain heterogeneous. Field tests should therefore measure realised function and its temporal/among-population reproducibility rather than stopping at connectance or visitation-network recovery.

## Prospective convergence hypothesis

The cross-system question remains:

> Do different fragmentation mechanisms converge on the same operational interaction-mediated functional-fragmentation regime once state feasibility, realised interaction support, process-resolved biological connectivity and functional-loss reproducibility are measured separately?

Current simulations do not establish such convergence. They now show that **network recovery itself is not sufficient evidence of regime recovery**, which sharpens what an empirical convergence test must measure.
