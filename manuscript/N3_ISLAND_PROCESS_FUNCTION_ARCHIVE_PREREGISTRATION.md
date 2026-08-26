# N3 preregistration — island process–function archive programme

## Purpose

N2 established a measurement/representation boundary in its bounded ten-system registry: reusable direct visitation and realised reproductive function were jointly explicit in several urban systems but not in any of the five locked island systems at the same scoring level. N3 is a new prospective programme opened only after that N2 decision was fixed. It does not replace, add to, or rescue the N2 candidate registry.

N3 asks:

> Can independent island archives be found in which direct pollination process measurements and realised plant reproductive function are retained together at a reusable ecological unit, and can those systems support prospectively frozen within-system process/function or residual-context tests?

N3 does not estimate an island–urban effect by itself.

## Search rule

Search is bounded to public studies/data repositories identified without using a preferred effect direction as an inclusion criterion. Published abstracts and papers necessarily contain scientific conclusions; those directions are not used to rank, add, drop, or redefine candidates.

A candidate is eligible for N3 only when public metadata demonstrate:

1. a real island or archipelago study setting;
2. direct flower-visitation/interaction observations or counts with effort/denominator information sufficient to form an intensity variable;
3. realised plant reproductive function measured in the same study (fruit set, seed set, seeds per flower/fruit, crop yield, or another explicitly retained direct reproductive endpoint);
4. a stable ecological unit or prospectively defensible aggregate unit linking process and function;
5. public raw data or an openly deposited dataset that can in principle be acquired without reconstructing values from fitted coefficients.

Exact response semantics are retained. Fruit set, seed number, seed weight and crop yield are not relabelled as one common scalar by generic standardisation.

## Locked first-pass candidates

### I3_MALLORCA_CAROB_2025

- Study: Gómez-Martínez et al. 2025, *Landscape conservation and orchard management influence carob tree yield through changes in pollinator communities*.
- Setting: 20 carob orchards across Mallorca Island, Spain.
- Public data: Zenodo `10.5281/zenodo.13939479` (version DOI `10.5281/zenodo.13939480`), CC BY 4.0.
- Upstream context reported by the source design: surrounding natural habitat / habitat loss, farming system, male-to-female tree ratio.
- Process: pollinator visitation/community composition.
- Function: fruit and seed production / seed quality-yield endpoints.
- N3 role: primary island residual-context candidate because `O`, direct pollination process and realised crop function are all source-defined at orchard scale.

### I3_MALLORCA_CNEORUM_2020

- Study: Fuster & Traveset 2020, *Importance of intraspecific variation in the pollination and seed dispersal functions of a double mutualist animal species*.
- Setting: Balearic Islands system involving *Cneorum tricoccon* and *Podarcis lilfordi*.
- Public data: Dryad `10.5061/dryad.2ngf1vhj1`.
- Archive structure publicly lists `Pollination_censues_2015_16.csv`, `Fruits-seeds_database.csv`, exclusion, germination and seed-dispersal files.
- Process: direct flower visitation/pollination censuses.
- Function: fruit/seed set and related reproductive measurements.
- N3 role: direct island process→function candidate. It is not assumed to contain a landscape-fragmentation context coordinate comparable to Toronto or the carob system.

### I3_MALLORCA_NETWORK_FITNESS_2020

- Study: Lázaro et al. 2020, *Linking species-level network metrics to flower traits and plant fitness*.
- Setting: coastal plant community on Mallorca Island, Spain.
- Public data: Dryad `10.5061/dryad.hqbzkh1bm`.
- Process: visitation rate per flower and quantitative plant–pollinator networks.
- Function: seeds per flower and seed weight.
- Ecological unit: plant species × study year after the source design's individual-to-species aggregation.
- N3 role: community-level representation candidate; it cannot be used as if its species-year rows were independent landscapes.

### I3_AZORES_APPLE_2020

- Study: Pardo et al. 2020, *Limited Effect of Management on Apple Pollination: A Case Study from an Oceanic Island*.
- Setting: six apple orchards on Terceira Island, Azores.
- Public source: open article/repository and supplementary material, DOI `10.3390/insects11060351`.
- Upstream context: orchard management and surrounding landscape composition.
- Process: pollinator visitation surveys.
- Function: fruit set, seed set and apple weight.
- N3 role: oceanic-island residual-context candidate if reusable row-level/same-orchard data are demonstrated by the deposited supplement/source tables. The paper-level statement that these variables were measured is not enough by itself; schema availability must still pass.

## Stage A — schema and representation gate

Before fitting any new N3 outcome model, each candidate is scored for:

- `O`: upstream context available at the held-out ecological unit;
- `I`: direct visitation intensity with effort/denominator;
- `D`: floral abundance/support denominator;
- `F`: direct realised reproductive function;
- `A`: stable process/function join key;
- `n_holdout`: number of independent ecological holdout units.

Only metadata, file names, column names, units, missingness and join structure may be inspected during Stage A. No association with reproductive outcomes is calculated.

## Stage B — permitted within-system tests

Two classes are allowed and must be declared separately per system after Stage A:

### B1 process adequacy

`M0: F ~ source-defined baseline/support terms`

versus

`M1: F ~ source-defined baseline/support terms + I_visit`

This tests whether direct visitation earns endpoint-relevant predictive information within that system.

### B2 residual context

Only systems with prospective `O + I + F + A` availability may compare:

`M0: F ~ partial process state`

versus

`M1: F ~ partial process state + upstream context O`.

Held-out ecological units are the source-design independent units (e.g. orchard, site, population), never rows sharing the same site.

## Cross-origin use

N3 results may later be paired with independently preregistered urban residual-context cases such as Toronto only at the **system level**. Individual observations are never pooled across studies merely to estimate an `island` coefficient.

A cross-origin convergence claim remains ineligible until at least two independent systems per origin pass a matched biological estimand and the origin label is not identical to one study/protocol.

## Stop rules

Do not:

1. drop a candidate because its published or newly computed effect direction is inconvenient;
2. substitute network centrality, richness or diversity for direct visitation after seeing outcomes;
3. convert unlike reproductive endpoints to generic z-scores solely to force pooling;
4. treat species or years nested in one Mallorca study as independent island systems;
5. call the Cneorum lizard system a fragmentation-context test unless a source-defined comparable context coordinate exists;
6. infer that the Azores apple data are reusable merely because the paper reports fruit/seed outcomes — Stage A must demonstrate the actual representation;
7. add a candidate after outcome inspection merely to manufacture two island positives;
8. infer island–urban convergence from one urban and one island result.

## Claim ceiling

N3 can recover whether public island archives retain the process→function information needed for direct empirical state tests and can produce independent within-island residual-context results where the data structure supports them.

It cannot by itself establish that island and urban systems share the same future law.