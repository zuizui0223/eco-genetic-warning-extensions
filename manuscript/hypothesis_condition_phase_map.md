# Hypothesis recovery and condition-phase-map program

## Purpose

Before final manuscript rewriting, recover the conditions under which each link in the eco-genetic warning chain is estimable. The organizing object is a **warning-blind condition map**, not another tuned warning comparison.

## 1. Nested condition hierarchy

```text
C0  Can a high functional state exist?                    H1 / H-MD-1
        ↓
C1  Can fragmentation/deterioration move it?              H3 / H-MD-2
        ↓
C2  Is functional loss reproducible but nondegenerate?    H-MD-3a / R4
        ↓
C3  Does genetic change precede that loss?                H2 / H-MD-3b
        ↓
C4  Is that warning portable across regimes?              Protocol 003 / future
```

The frontier program deliberately solves C2 before reopening C3.

## 2. Event-regime classes

All condition search is defined without genetic warning or diversity values.

- `R0`: source/high-state infeasible;
- `R1`: persistence / functional loss too rare;
- `R2`: rapid loss / nearly deterministic loss;
- `R3`: independent stochastic blocks do not share one nondegenerate loss regime;
- `R4`: every independent seed block has functional-loss frequency in `[0.30,0.70]` under the predeclared high-rep gate.

R4 means **warning evaluability**, not warning success.

## 3. What the recurrent-transition condition search recovered

### Coarse Protocol 002 grid

The original 15-coordinate common grid contained zero R4 candidates: 15/15 `no_domain_selected`. This is still the correct historical result for that grid/family.

### Warning-blind matched reanalysis

Within complete matched Stage II candidates:

- increasing `p_star` or `kappa_mu` never increased pooled loss in the tested adjacent contrasts;
- the rapid-to-persistence frontier shifts toward lower `p_star` as `kappa_mu` increases;
- horizon extension can expose more loss;
- barrier magnitude and the tested ecological-support factors moved pooled loss less consistently conditional on candidate completeness.

### Phase A — weak-transition frontier

`kappa_mu=0.05`, ten interior cells, 250 new attempts: 0 R4, 6 R3, 4 R2.

### Phase B — clean matched rapid-to-persistence bracket

Fixed `A_ref=1.0`, interaction `kappa=4.5`, horizon 120, barrier 0.30, `kappa_mu=0.35`.

Historical endpoints:

- `p_star=0.25`: all five seed rates 1.0 → R2;
- `p_star=0.50`: all five seed rates 0.0 → R1.

Four interior low-rep cells were R3 while pooled loss declined `0.739→0.476→0.304→0.095`.

### Phase C — high-rep recovery of R4

With five fresh seeds and 20 replicates per seed:

- `p_star=0.35`: seed rates `0.579,0.529,0.474,0.588,0.368`, pooled 0.505 → **R4-highrep**;
- `p_star=0.40`: seed rates `0.300,0.400,0.389,0.200,0.263`, pooled 0.304 → R3-highrep.

Thus R4 exists. The coarse 15-coordinate grid missed a narrower condition region; the historical no-domain result was not structural impossibility.

### Phase D — independent R4 replay and width bound

Same fixed non-direction conditions, new seed family, 20 replicates per seed:

- `p_star=0.325`: seed rates `0.529,0.526,0.800,0.667,0.778`, pooled 0.663 → R3-highrep;
- `p_star=0.350`: `0.500,0.667,0.647,0.588,0.632`, pooled 0.609 → **R4-highrep**;
- `p_star=0.375`: `0.412,0.389,0.529,0.389,0.235`, pooled 0.391 → R3-highrep.

The Phase-C R4 point therefore independently replays, but neither ±0.025 neighbor is R4.

### Recovered condition conclusion

> **A reproducible intermediate-risk event regime exists, but it occupies a narrow region of recurrent-transition state space; pooled intermediate loss probability describes a broader region than warning evaluability.**

The exact R4 width is not identified, only bounded as narrower than the tested ±0.025 neighbor spacing under this strict criterion.

Under the predeclared stop rule, **no finer `p_star` tuning is allowed merely to widen R4**. No warning/diversity field from Phases A–D is released.

## 4. Why this is more than a negative no-domain result

The scientific progression is now positive:

```text
coarse common grid: no R4
        ↓
condition frontier identified warning-blind
        ↓
higher replication recovers one reproducible R4 condition
        ↓
independent replay confirms it
        ↓
adjacent high-rep cells fail the same reproducibility gate
```

So the result is not “warning cannot be evaluated.” It is that **evaluability itself has a narrow condition boundary that must be established independently of the warning statistic**.

This should not be overclaimed as invention of phase maps, stochastic tipping sets, mechanism-dependent EWS or non-event retention; those have prior art. The load-bearing distinction is between **pooled event probability** and **reproducible event-regime estimability across independent stochastic blocks**.

## 5. Next condition axis — effective connectivity/migration

Recurrent-transition direction is now closed for this condition-recovery phase. The next biologically interpretable unfinished axis is **effective connectivity**.

The pinned parent closure already provides:

- equal-isolated four-patch projection with `m=0`;
- equal-migrating four-patch projection with `m=0.1`;
- Type T two-patch migration identity `|p1'-p2'|=(1-2m)|p1-p2|` for `0<m<1/2`;
- a separate rescue certificate that can coexist with this homogenization.

Thus connectivity can simultaneously support rescue and reduce spatial genetic differentiation.

### Next warning-blind question

At the independently reproduced R4 recurrent-transition condition, does changing only effective connectivity shift the event regime among R1–R4?

A clean next design should prepare the same source and compare paired `m=0` versus `m=0.1` projections with new seeds, using **source/baseline/functional-loss outcomes only**. Genetic warning remains locked.

This axis should be declared prospectively before execution; it should not be tuned to preserve R4.

## 6. Urban ecology application

Cities are a strong test because apparent fragmentation does not uniquely determine effective connectivity.

Map the condition axes as:

- green-space area → patch support;
- roads/impervious matrix → resistance;
- green corridors, pollinator movement and anthropogenic dispersal → effective migration;
- pollinator visitation/compatible pollen delivery → interaction support;
- heat/pollution/disturbance → deterioration.

Predictions:

- specialist-pollinator systems with low effective connectivity should shift toward source-limited or rapid-loss regimes;
- mobile pollinators/human-mediated dispersal can preserve connectivity and possibly move systems away from those regimes;
- connectivity may rescue function/population while homogenizing genetic spatial structure, so low differentiation is not automatically evidence of low vulnerability;
- urban sites with similar patchiness can occupy different R regimes depending on realized pollen movement and interaction support.

## 7. Island ecology application

Islands provide strong area/isolation gradients plus mutualist and reproductive filters.

Map:

- island area → local support;
- inter-island/mainland distance and stepping stones → effective connectivity;
- pollinator/mutualist availability → interaction support;
- self-compatibility, autonomous selfing, vegetative reproduction, generalized pollination → reproductive assurance;
- bottlenecks/colonization history → source and genetic-state conditions.

Predictions:

- specialist/outcrossing lineages on small remote islands should enter source-limited/rapid-loss regimes more readily when mutualist support is weak;
- selfing/generalism can create demographic persistence even after the original interaction-dependent function weakens;
- stepping-stone connectivity can provide rescue while homogenizing genetic differences;
- remote islands with a stable effective pollination niche can retain high-function/outcrossing states despite distance alone predicting isolation.

## 8. Urban–island synthesis

The useful comparison is not “city versus island.” It is:

```text
spatial patchiness
  × effective connectivity
  × interaction support
  × reproductive assurance
        ↓
source feasibility and loss regime
        ↓
R4 evaluability or non-evaluability
        ↓
only then genetic warning
```

Urban and island systems therefore become empirical tests of the same condition hierarchy under contrasting connectivity rules.

## Immediate scientific target

> **Hold the now-confirmed recurrent-transition R4 condition fixed and test whether effective connectivity alone moves the source/loss/evaluability regime, still without access to genetic warning.**

Only after that ecological axis is recovered should the final manuscript decide whether to stop at the condition map or open a separately declared matched warning-validation experiment.
