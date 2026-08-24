# Empirical candidate regimes for interaction-mediated functional fragmentation

## Purpose

The state-sufficiency result is ecologically useful only if its candidate state can be observed in nature. This registry therefore translates the model state into field measurements and identifies published systems in which most of the required coordinates already exist.

The goal is not to label habitats as `urban`, `island` or `fragmented`. The goal is to test whether different causal routes become dynamically equivalent after conditioning on a future-relevant ecological state.

## Empirical state to search for

For patch or population `i` before an outcome window, treat the following as candidate state coordinates rather than collapsing them into one fragmentation or genetic index:

- `D_i` — **demographic support**: census, density, flowering density and effective size where estimable;
- `I_i` — **realised interaction support**: visitation weighted by effectiveness, compatible pollen receipt, or an equivalent interaction-specific measure;
- `T_i` — **realised trait/functional support**: trait matching, floral-morph composition, partner functional traits or another mechanism-specific state;
- `G_i` — **genetic and mating state**: heterozygosity, inbreeding, mating-system state and functional/adaptive alleles where available;
- `C_i` — **process-specific connectivity**: pollen, seed/propagule, demographic and partner movement measured separately;
- `R_i` — **alternative functional routes**: autonomous selfing, reproductive assurance, compensatory partners or other substitute pathways;
- `F_i` — **realised ecological function**: compatible pollen delivery, fruit/seed set, dispersal effectiveness, recruitment or another direct endpoint;
- `M_i` — **plausible ecological memory**: prior disturbance, age structure, seed bank, persistent resource states or interaction legacies when biologically relevant.

The candidate state must also preserve **joint spatial alignment**, not only marginal means. A simple empirical starting statistic is a population-weighted spatial association such as

`A_IG = cor_w(I_i, G_i)`

with analogous `A_ID`, `A_IT` or multivariate cross-covariance terms. These are candidate compressions, not assumed sufficient statistics. Predictive sufficiency must be tested.

## Operational convergence test in nature

For a future window `t -> t + Delta`:

1. measure the candidate state before the outcome window;
2. define realised functional loss independently of genetic-warning variables;
3. fit a common loss model using the candidate state;
4. add fragmentation origin/history (`urban`, `island`, disturbance route, matrix type, etc.);
5. compare held-out prediction, calibration and residual structure.

**Convergence is supported only if origin/history no longer improves prediction after conditioning on the candidate state.** If origin/history still matters, the state is incomplete; the next task is to identify the missing process or memory variable rather than to declare habitat categories intrinsically different.

## Published systems that already approximate the candidate state

### Tier A — near-complete natural systems

#### 1. *Crepis sancta*, Montpellier urban patch network

The Montpellier *Crepis sancta* programme is a strong urban candidate because studies on the same species and city collectively measure several state layers: small pavement-patch demography, pollinator activity, seed set, selfing/outcrossing, seed-dispersal phenotype, parentage-based pollen and seed movement, immigration, neutral microsatellite variation and quantitative-trait differentiation.

Cheptou & Avendaño (2006) linked low local density to lower pollinator activity and seed set while also estimating selfing from progeny arrays. The subsequent urban-dispersal programme showed strong selection against dispersing seeds in the built matrix. Dornier & Cheptou (2013) estimated pollen and seed dispersal and immigration by parentage in two urban patch networks; its population microsatellite/spatial data are openly archived at Dryad (`10.5061/dryad.b911r`). Dubois & Cheptou (2017) combined neutral microsatellites with dispersal and reproductive traits across fragmented/unfragmented and urban/rural populations; those data are archived at Dryad (`10.5061/dryad.fv58t`).

The principal gap is synchronisation: the published state coordinates were not all measured in the same population-years and outcome windows. Existing data can therefore support a partial process audit, whereas a decisive state-sufficiency test requires simultaneous interaction, function and genetic/connectivity observations.

**Candidate natural regime:** interaction-limited, strongly matrix-fragmented urban populations with restricted local seed dispersal but nonzero pollen or immigration pathways.

#### 2. *Camellia japonica*–*Zosterops japonicus*, Miyake-jima

The Miyake-jima camellia–white-eye system is a strong island candidate because disturbance, interaction support, pollen movement, reproductive function and next-generation genetics were measured within one island system across a volcanic-damage gradient.

Abe et al. (2013) combined vegetation/disturbance context, flowering-tree and flower density, bird-mediated pollination, fruit/seed production, adult and seed microsatellites, pollen-donor diversity and pollen immigration. Greater volcanic damage reduced floral density, but wider white-eye movement increased pollen movement and donor diversity, while reproduction was maintained or compensated and seed genetic diversity increased.

This is a natural counterexample to a simple `greater disturbance/isolation -> lower connectivity -> lower function` chain.

**Candidate natural regime:** low local floral support buffered by increased partner movement and pollen mixing, so realised function is maintained through compensation rather than unchanged habitat support.

### Tier B — highly informative but missing one major state axis

#### 3. Izu coastal plant–pollinator networks

Hiraiwa & Ushimaru's coastal programme spans Honshu and Oshima, Niijima, Kozu, Miyake and Hachijo. The 2024 analysis contains 40 spatiotemporally variable networks and directly links pollinator functional diversity to trait matching and pollen receipt/pollination success. Data and code are archived at Figshare (`10.6084/m9.figshare.25025000.v1`); the earlier interaction dataset is on Dryad (`10.5061/dryad.pm29d`).

This system provides unusually strong measurements of `I`, `T` and `F` across repeated mainland/island site-seasons. It lacks matched focal-population genetics and process-specific pollen/seed connectivity for the same networks.

**Best next addition:** genotype focal plant populations and offspring/pollen pools at the same sites. This would convert an existing interaction-function natural experiment into a direct test of `I-G` spatial alignment and mainland/island state convergence.

#### 4. Zurich urban garden phytometer network

An open 24-garden dataset (`10.16904/envidat.676`; Reji Chacko et al. 2025) contains site coordinates, urban intensity, time-resolved visitation, visitor identities and traits, flower-visitation matrices and direct fruit/seed set for four phytometer species.

It is a strong urban `spatial support -> I/T -> F` dataset with standardized plant material, which helps isolate interaction support but removes natural among-population plant genetic structure.

**Best next addition:** pair the same garden network with a naturally occurring focal plant whose parentage/genetics can be sampled, or add an explicit pollinator-movement/connectivity layer.

#### 5. *Penstemon hirsutus* on Chicago green roofs

Ten experimental green-roof populations provide site configuration, co-flowering vegetation, reproductive output, parent/offspring microsatellites, selfing/outcrossing and paternity-based pollen movement. Ksiazek-Mikenas et al. (2019) found both within- and between-roof pollen movement and strong site-to-site variation in reproduction and mating. Microsatellite data are archived at Dryad (`10.5061/dryad.1j86179`).

This system has strong `G`, `C_pollen` and `F` information but lacks a detailed interaction-network / visitation-effectiveness time series.

**Best next addition:** pollinator identity, visitation and effectiveness for each roof, allowing direct estimation of whether genetic support and interaction support are spatially aligned.

#### 6. *Conospermum undulatum*, Perth urban fragments

A process-specific paternity study of the threatened *Conospermum undulatum* (Delnevo et al. 2026) found pollen movement through continuous bushland but no detected inter-fragment pollen immigration across built urban infrastructure. Adult/offspring microsatellite data are archived at Dryad (`10.5061/dryad.95x69p907`), and the broader study programme includes fragmentation effects on pollinators, pollen quality and reproductive success.

**Candidate natural regime:** interaction-vector limitation in which built infrastructure breaks contemporary pollen flow even before standing adult genetic structure necessarily records the same fragmentation event.

### Tier C — cross-system bridge beyond urban/island labels

#### 7. *Primula elatior*, fragmented Dutch landscapes

A 2025 study of 33 populations jointly analysed population size, genetic diversity/differentiation, floral-morph ratio, landscape context, pollinator abundance and seed production. Small populations had lower genetic diversity and more skewed morph ratios, while seed production depended on morph balance, pollinator abundance and landscape context. Genetic data are archived under NCBI BioProject `PRJNA837403`.

This system matters because it shows that the candidate state can be measured jointly outside the urban/island contrast. It is therefore a bridge test of whether the same state representation generalises to conventional terrestrial fragmentation.

## Candidate regimes suggested by the empirical literature

The literature already supports several mechanistically distinct combinations worth testing:

1. **interaction-limited / genetically connected** — local interaction or function weakens while pollen, animal or anthropogenic movement remains substantial;
2. **interaction- and connectivity-limited** — specialised interaction vectors are lost or blocked by the matrix, reducing both realised function and contemporary gene flow;
3. **interaction-buffered by movement or compensation** — local resources decline but wider partner movement, rewiring or compensatory interactions maintain function;
4. **joint demographic-genetic-interaction limitation** — demography, genetic state, mating/trait balance and partner availability jointly constrain reproduction.

These are **candidate regimes, not established universal classes**. Their value is that they convert habitat labels into testable combinations of processes. The empirical target is to determine whether these combinations predict future function better than the category that generated them.

## Immediate analyses possible with existing open data

### E1 — Izu ecological state map

Use the archived 40-network data to estimate a candidate ecological state from pollinator functional diversity, functional generality, trait matching, season and island distance, with pollen receipt/pollination success as the functional endpoint. Test whether the mainland/island label still improves held-out prediction after conditioning on the functional state.

This is the closest immediate cross-system convergence test, but without matched genetics it tests the **ecological state layer only**.

### E2 — Zurich urban interaction-function state map

Use garden-level urban intensity, floral richness, time-resolved visitation, visitor traits and fruit/seed set. Build candidate `I/T` state summaries and test whether impervious-surface or urban-intensity labels add predictive information once interaction state is included.

This tests whether a landscape category can be reduced to a measured interaction-functional state within one city.

### E3 — *Crepis* process-specific connectivity audit

Use the open parentage/dispersal and fragmentation/genetics datasets at the study-programme level. Do **not** pool incompatible populations or years as if they were one synchronized experiment. Instead test whether fragmentation descriptors explain dispersal/genetic outcomes after explicit patch geometry and measured dispersal state are accounted for, then use the gaps to design a prospective synchronized pollination-function-genetics resurvey.

### E4 — Chicago green-roof connectivity/function audit

Use roof configuration, paternity, selfing/outcrossing and reproductive output to quantify contemporary pollen connectivity and function. The explicit unresolved variable is interaction support: a future pollinator-observation layer can test whether residual site effects are explained by interaction-genetic spatial alignment.

## Field design for a decisive urban–island test

The strongest prospective test uses repeated focal populations of the same lineage where possible, or tightly controlled ecological analogues, and measures all state variables before the functional outcome window.

Minimum per population-year:

1. plant and flowering density;
2. partner identity and visitation frequency;
3. pollinator effectiveness or compatible pollen deposition;
4. direct realised function such as fruit/seed set;
5. breeding system and reproductive assurance;
6. parent and offspring genotypes for pollen-mediated gene flow;
7. seed/propagule movement where biologically important;
8. spatial coordinates, habitat amount and matrix resistance;
9. previous disturbance/resource state;
10. enough repeated patches or years to estimate joint spatial alignment and future functional loss.

The objective is not to maximise the number of covariates. It is to find the **smallest measured joint state for which origin/history ceases to improve prediction of future function**.

## Interpretation boundary

The parent model proves state sufficiency only for its declared Markov closure. Natural systems can retain ecological memory through seed banks, age structure, persistent soil states, learned pollinator routes, microbial partners or other omitted variables. In empirical work, a residual history effect is therefore evidence that the candidate state is incomplete—not evidence against a state-based formulation itself.
