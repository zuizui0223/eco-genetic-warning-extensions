# Hypothesis recovery and condition-phase-map program

## Purpose

Before rewriting the paper around warning performance, first recover the scientific conditions under which each part of the eco-genetic chain is true, false, or not evaluable. The next research product should be a warning-blind **eco-genetic phase map**, not another tuned warning comparison.

## 1. Recovery hierarchy

Treat the current results as a hierarchy of questions rather than a flat hypothesis list.

```text
H1/H3 mechanism
  Can an interaction-dependent functional state exist, and can fragmentation disrupt it?
        ↓
H2 benchmark
  In one calibrated regime, can genetic erosion precede realised functional loss?
        ↓
H-MD-1
  Under altered recurrent-transition closure, can the high-function source state exist?
        ↓
H-MD-2
  What functional-loss regime does a common deterioration family generate?
        ↓
H-MD-3a
  Does that regime contain a reproducible intermediate-risk domain in which warning can be evaluated?
        ↓
H-MD-3b
  Only if such a domain exists: how available and how early is the genetic warning?
```

Current status:

- H1/H3: mechanistic core recovered for the declared parent closure.
- H2 relative warning: conditionally supported in one warning-blind calibrated symmetric domain; fixed absolute thresholds are not robust.
- H-MD-1: supported finite Type S.
- H-MD-2: supported finite Type S.
- H-MD-3a: negative/recovered for the tested common 15-coordinate grid and deterioration family; eligible set empty at 15/15 coordinates.
- H-MD-3b: matched finite effect bounded unresolved because the required matched evaluable domains were not instantiated.
- Type T recurrent-transition identities: recovered boundaries showing non-universal direction-to-diversity sign and local support-diversity decoupling.

## 2. What should be explored next

The next scientific target is the boundary structure among five finite regimes:

```text
R0  source-infeasible
R1  persistent / functional loss too rare
R2  rapid-loss / functional loss too fast or nearly certain
R3  seed-heterogeneous / event regime not reproducible across seed blocks
R4  warning-evaluable / reproducible intermediate-risk loss regime
```

`R4` must be defined without warning or diversity values. Warning endpoints are evaluated only after a candidate region is frozen and fresh validation seeds are introduced.

The present Protocol 002 result establishes only that `R4` was absent from the declared 15-coordinate common grid/candidate family. It does **not** establish that `R4` cannot exist elsewhere in parameter space.

## 3. Condition axes

Explore the phase space along biologically interpretable axes, keeping warning fields unavailable during search.

### Ecological state/support

- patch number and patch area at fixed total area;
- migration/connectivity among patches;
- interaction-feedback strength (`kappa`) and area reference (`A_ref`);
- barrier/deterioration strength and duration;
- initial/high-state support margin where analytically identifiable.

### Recurrent eco-genetic turnover

- transition strength `kappa_mu`;
- transition equilibrium/direction `p_star`;
- starting allele-frequency region relative to the exact `M(p)=0.5` diversity-sign boundary;
- among-patch allele-frequency heterogeneity, whose one-step contraction is controlled by `(1-kappa_mu)^2` under fixed weights.

### Stochastic/event structure

- trait-loss frequency;
- between-seed variability of trait-loss frequency;
- baseline eligibility;
- censoring/administrative horizon.

## 4. Search discipline

Do not enlarge a warning domain by looking at warning outcomes.

1. Use analytical Type T boundaries where available to partition parameter space before simulation.
2. Run a warning-blind phase-map campaign using only source feasibility, realised functional loss, baseline eligibility and seed-block reproducibility.
3. Map boundaries among R0-R4, with denser sampling only near regime boundaries identified from those warning-blind outcomes.
4. Freeze candidate R4 cells before any diversity/warning fields are calculated.
5. Use fresh calibration/validation seeds for the actual warning test.

This turns `no_domain_selected` from a terminal negative result into a boundary-finding result.

## 5. Urban ecology as a natural application domain

Cities are useful because urbanization can move several phase-map axes independently rather than simply increasing isolation.

Empirical literature shows that urban fragmentation can reduce population size and alter gene flow/drift, but urban genetic responses are not uniformly isolation-like. Reviews report weak average losses of within-population diversity and no consistent increase in differentiation, while plant systems can retain high gene flow through animal- and human-mediated dispersal and repeated introductions.

Map urban variables to the model cautiously:

- green-space size / habitat-remnant area -> patch area;
- impervious surface / road barriers -> resistance and effective connectivity;
- green corridors / animal or human-mediated dispersal -> migration/connectivity;
- pollinator abundance, visitation and network integrity -> interaction support/function;
- heat, pollution and other urban selective environments -> ecological deterioration and state-dependent selection;
- recurrent introductions, biased recruitment or switching among trait-associated states -> possible empirical analogues of effective recurrent state turnover; do **not** interpret `p_star` as a mutation rate.

### Urban predictions to test

- Small isolated patches with weak pollinator interaction and low effective connectivity should be enriched for rapid-loss or seed-heterogeneous regimes.
- Highly connected or repeatedly introduced urban populations may retain genetic diversity even when ecological interaction/function is impaired, providing an empirical test of support-diversity decoupling.
- Intermediate urban mosaics may be the most promising place to find warning-evaluable regimes because both persistence and functional loss can occur at nondegenerate frequencies; this is a hypothesis, not a conclusion.

Urban pollination is especially suitable because city effects on pollination are globally negative on average but highly heterogeneous, while pollen movement through cities remains difficult to predict.

## 6. Island ecology as a natural application domain

Islands supply strong gradients in area, isolation, colonization, mutualist availability and reproductive mode. Functional island-biogeography theory predicts that mutualist diversity, including pollinators, generally declines with isolation, while generalist pollination, self-compatibility and vegetative reproduction become more common with increasing isolation.

Map island variables to the phase map:

- island area -> patch area/carrying support;
- distance from source islands/mainland -> connectivity/colonization pressure;
- within-archipelago stepping-stone structure -> migration network;
- pollinator/mutualist richness -> interaction support;
- self-compatibility/generalist pollination/vegetative reproduction -> alternative routes to persistence when specialist interaction support is weak;
- demographic bottlenecks and repeated colonization -> starting-state and recurrent-turnover structure.

### Island predictions to test

- Small remote islands with low mutualist availability should be enriched for source-infeasible or rapid functional-loss regimes for strongly outcrossing/specialist systems.
- Lineages with self-compatibility or generalized pollination may move from rapid-loss into persistence regimes even after specialist interaction function is reduced.
- Intermediate isolation/area combinations may contain warning-evaluable regimes if functional loss occurs reproducibly but not deterministically.
- Genetic diversity can remain an imperfect proxy for interaction-dependent function because colonization history, bottlenecks, selfing and retained/introduced gene flow can alter diversity independently of current ecological function.

## 7. Why urban and island systems are complementary

The two applications should not be treated as decorative examples.

```text
islands:
  isolation is strong and mutualist/colonization filters are often natural and persistent

cities:
  fragmentation can coexist with corridors, repeated introductions and human-mediated dispersal
```

Together they provide contrasting natural tests of the same phase-map idea: **similar spatial fragmentation can generate different eco-genetic regimes depending on connectivity, interaction support and state turnover.**

This contrast is especially valuable because the urban literature explicitly warns that cities are not always genetically isolated islands, while island functional ecology predicts strong isolation-dependent mutualist and reproductive filtering.

## 8. Immediate scientific target

Do not yet claim a universal warning-evaluable phase diagram. The next target is narrower:

> **Identify which combinations of ecological support, connectivity, recurrent state turnover and deterioration generate source-infeasible, persistence, rapid-loss, seed-heterogeneous or warning-evaluable regimes in the declared finite model, using warning-blind classification.**

Only after this condition map is recovered should the manuscript decide whether warning evaluability itself is the main paper result or whether a well-supported R4 region permits a stronger conditional warning comparison.

## Literature anchors for applications

Urban:
- Alberti, M. (2015). Eco-evolutionary dynamics in an urbanizing planet. *Trends in Ecology & Evolution* 30:114-126. doi:10.1016/j.tree.2014.11.007.
- Rivkin, L.R. et al. (2019). A roadmap for urban evolutionary ecology. *Evolutionary Applications* 12:384-398. doi:10.1111/eva.12734.
- Miles, L.S. et al. (2019). Gene flow and genetic drift in urban environments. *Molecular Ecology* 28:4138-4151. doi:10.1111/mec.15221.
- Youngsteadt, E. & Keighron, M.C. (2023). Urban Pollination Ecology. *Annual Review of Ecology, Evolution, and Systematics* 54:21-42. doi:10.1146/annurev-ecolsys-102221-044616.
- Urban plant population genetics review (2026), *Perspectives in Plant Ecology, Evolution and Systematics* 70:125920, emphasizes high context dependence and frequent maintenance of gene flow/diversity in urban plants.

Islands:
- Schrader, J. et al. (2021). A roadmap to plant functional island biogeography. *Biological Reviews*. doi:10.1111/brv.12782.
- Traveset, A. et al. (2018). Plant reproductive ecology and evolution in the Mediterranean islands: state of the art. *Plant Biology*. doi:10.1111/plb.12636.
- Whittaker, R.J. et al. (2017). Island biogeography: taking the long view of nature's laboratories. *Science*.
- Fernández-Palacios, J.M. et al. (2023). Island evolutionary syndromes in—and involving—plants. In *Island Biogeography*.
