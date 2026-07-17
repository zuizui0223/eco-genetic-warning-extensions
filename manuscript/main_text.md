# Genetic warning emerges from eco-genetic closure in fragmented systems

## Abstract

Ecological function can disappear before population extinction, motivating indicators of realised functional-trait loss. We tested whether genetic warning is portable across eco-genetic closures by combining a finite model of interaction feedback and fragmentation with a directional recurrent-transition extension. Under a symmetric benchmark, diversity erosion preceded all 35 observed trait-loss events. Across 15 transition coordinates, 2,269 of 3,375 reconstructed sources were supported, but warning-blind calibration found no eligible validation domain among 20,250 attempts because candidate regimes separated into rapid loss, persistence, or seed heterogeneity. A separately declared protocol recovered two calibrated domains. The symmetric bridge produced 323 leads, one tie, and no lags across 324 valid comparisons; the directional transition produced 184 leads, five ties, and 12 lags across 201 comparisons, shortening median positive lead time from 106–112 to 74–81 generations. Warning availability, ordering, censoring, and intervention time therefore emerged from ecological, demographic, genetic, and observation closure.

## Introduction

Ecological deterioration can remove an interaction-dependent trait before the population carrying it goes extinct. This distinction matters because conservation often seeks to maintain pollination, dispersal, defence, mutualism, or other ecological processes rather than persistence alone (Soulé et al. 2005; McConkey & Drake 2006; Valiente-Banuet et al. 2015). Abundance, allele presence, genetic diversity, interaction state, and realised trait occupancy are therefore distinct monitoring targets.

Early-warning research asks whether a statistic changes before collapse (Scheffer et al. 2009; Drake & Griffen 2010), while genetic monitoring asks whether diversity or allele-frequency change reveals deterioration before demographic or functional loss (Schwartz et al. 2007; Stange et al. 2021). Both can overlook a more basic dependency: warning depends on mechanism, observation, and the event definition, and need not be universal across systems (Hastings & Wysham 2010; Boettiger & Hastings 2012, 2013). The closure linking ecological feedback, demography, inheritance, recurrent state turnover, observation, and the loss endpoint may determine whether a warning is observable, whether it precedes loss, and whether enough comparable events exist to validate it.

A predecessor framework linked interaction thresholds, fragmentation, local effective size, realised high-trait occupancy, and genetic diversity. This connection is consistent with broader evidence that spatial structure jointly alters demography, interaction, gene flow, drift, and adaptation (Legrand et al. 2017; Govaert et al. 2019). Under one independently calibrated symmetric-transition configuration, baseline-relative diversity erosion preceded observed trait loss. That result was explicitly conditional on one life-cycle closure and one selected deterioration domain.

Here we alter one genetic boundary condition while holding the ecological life cycle fixed. Recurrent transitions between high-trait-associated and low-trait-associated states need not be symmetric. Directional introduction of variants can shape evolutionary outcomes, but its effect depends on selection, demography, and the supply of alternatives (Stoltzfus & McCandlish 2017; Storz et al. 2019). Separating transition-map relaxation strength from equilibrium direction changes recurrent input and loss without changing selection, migration, finite drift, trait recruitment, source transfer, projection, or trait-loss semantics.

We ask whether transition direction changes high-trait source reconstruction, realised trait-loss regimes, the existence of a warning-validation domain under a warning-blind rule, and warning availability, ordering, censoring, and lead time after independent calibration. Our central proposition is that genetic warning is an emergent property of eco-genetic closure rather than a portable property of a diversity statistic.

## Model and mechanism

Let `p` denote the high-trait-associated allele frequency. The recurrent transition operator is

\[
M(p)=\kappa_\mu p_\mu^\ast+(1-\kappa_\mu)p.
\]

Here `kappa_mu` controls contraction towards the transition-only equilibrium and `p_mu*` controls direction. The effective transition rates are

\[
u_{L\to H}=\kappa_\mu p_\mu^\ast,\qquad
u_{H\to L}=\kappa_\mu(1-p_\mu^\ast).
\]

At a local post-transition threshold `p_c`, the required pre-transition frequency is

\[
\theta(p_c)=\frac{p_c-\kappa_\mu p_\mu^\ast}{1-\kappa_\mu}.
\]

Increasing `p_mu*` therefore lowers the pre-transition frequency required to remain above a high-state boundary. Whether this local mechanism organizes the finite stochastic system was tested rather than assumed. The operator can represent recurrent mutation, gain–loss asymmetry, epimutation, switching, or another effective state transition; `p_mu*` is not an empirical mutation-rate estimate.

## Protocol

We evaluated three relaxation strengths (`0.05`, `0.20`, `0.35`) and five transition equilibria (`0.10`, `0.25`, `0.50`, `0.75`, `0.90`). All other life-cycle components were inherited from pinned predecessor commit `dd8ee379d0d3518194c767d16402042525bc00dc`.

Source reconstruction was repeated independently for every coordinate using three area-reference values, three interaction-feedback values, five master seeds, and five replicates. Prepared sources were held for 30 generations and projected into one-large, equal-isolated, and equal-migrating landscapes. Projection support required every declared invariant to pass.

Warning-blind calibration evaluated two horizons and three normalized barrier increases using five new calibration seeds and five replicates. Calibration could inspect source eligibility and realised trait loss only. A candidate was eligible only if every seed block had post-baseline trait-loss frequency in `[0.30, 0.70]`; otherwise the protocol required `no_domain_selected` without expanding the candidate family.

Because this family selected no domain, a separate protocol used independent seed families for bracket search, calibration, confirmation, and validation. Two domains were fixed before warning outcomes were computed: a symmetric bridge (`kappa_mu=0.20`, `p_star=0.50`) and a directional transition (`kappa_mu=0.05`, `p_star=0.90`). Validation used five fresh master seeds and 20 replicates per seed in each domain.

Relative warnings were the first post-baseline generation at which `H_alpha` or `H_gamma` declined by 5%, 10%, or 20% from its own baseline. Analyses retained baseline ineligibility, warning censoring, trait-loss censoring, ties, leads, and lags. The six endpoint records from one trajectory are correlated and are not independent biological replicates.

## Results

### Fragmentation established an eco-genetic route to warning

The predecessor mechanism linked patch size to interaction intensity, high-trait-state stability, local effective size, diversity, and realised high-trait occupancy. Equal isolation reduced interaction, local effective size, and realised high-trait mass relative to one large patch. Under one independently calibrated symmetric closure, all 35 observed trait-loss events were preceded by baseline-relative erosion across all six preregistered endpoints. This benchmark is conditional rather than universal.

### Transition direction reorganized high-trait source feasibility

All 3,375 planned source attempts were completed. Source support, full-state preparation, and supported projection each occurred in 2,269 attempts (67.23%); every prepared source passed all projection invariants. Coordinate support ranged from 101 of 225 attempts (44.89%) at `kappa_mu=0.05`, `p_star=0.10` to 195 of 225 (86.67%) at `kappa_mu=0.35`, `p_star=0.90`. Within each relaxation-strength row, support generally increased towards higher `p_star`, extending the local threshold mechanism to a finite source-reconstruction boundary.

### Eco-genetic closures separated into loss regimes

Warning-blind calibration completed 20,250 attempts in 810 batches. Of 648 candidates with complete five-seed blocks, 322 had all loss frequencies above the eligibility band, 242 had all rates below it, and 84 crossed the band among seeds.

Low transition equilibria were dominated by rapid loss: the closest candidates at `p_star=0.10` had loss frequency 1.0 across every seed block and relaxation strength. High transition equilibria at stronger relaxation were dominated by persistence, including zero loss in every seed block at (`0.20`, `0.90`), (`0.35`, `0.75`), and (`0.35`, `0.90`). Intermediate coordinates were often seed-heterogeneous; at (`0.20`, `0.50`), for example, the pooled frequency was 0.524 while seed-block rates ranged from 0.20 to 0.80.

None of the 648 complete candidates satisfied the all-seed rule, so all 15 coordinates were recorded as `no_domain_selected`. This was an event-regime result, not evidence that genetic warning failed.

### Warning reliability emerged from calibrated closures

Separate confirmation calibration recovered two eligible domains using fresh seeds and larger within-seed replication. The symmetric bridge had pooled trait-loss frequency 0.679 among 84 baseline-eligible trajectories; the directional transition had frequency 0.625 among 88. Both domains were locked before validation diversity trajectories were examined.

Fresh-seed validation completed 200 attempts. In the symmetric bridge, 82 trajectories completed and each endpoint produced 54 valid warning–loss pairs. Across 324 correlated comparisons, 323 were leads, one was a tie, and none was a lag; median positive lead time was 106–112 generations. In the directional transition, 91 trajectories completed, valid-pair availability ranged from 28 to 38 among endpoints, and ten trajectories were baseline-ineligible throughout. Across 201 valid comparisons, 184 were leads, five were ties, and 12 were lags; median positive lead time was 74–81 generations. Warning censoring increased at stricter thresholds, especially for `H_gamma`.

Relative diversity erosion remained predominantly leading in the directional domain, but it was less consistently available, occasionally lagged, and provided a shorter intervention window than in the symmetric bridge.

## Discussion

Genetic warning was not portable across the tested closures. Diversity endpoints that produced nearly uniform leading order under the symmetric bridge became less available, more censored, occasionally lagging, and shorter-lived under a directional transition. Mutation or effective state-transition direction was one mechanism that moved the system among closures; the broader result is that warning behaviour emerged from the joint ecological, demographic, genetic, and observation process. This mechanism dependence parallels broader cautions against treating early-warning statistics as universal signals independent of the process generating them (Hastings & Wysham 2010; Boettiger & Hastings 2012, 2013).

Event-regime feasibility is part of early-warning biology. Near-certain rapid functional loss offers little discrimination among warning rules, persistence yields too few loss events for validation, and seed-heterogeneous regimes can make pooled frequencies look suitable while individual seed blocks occupy opposing regimes. Reporting `no_domain_selected` therefore identifies where warning performance cannot be estimated under a declared design.

Functional-trait loss is distinct from population extinction. Populations and trait-associated alleles may persist while realised ecological function disappears through altered interaction, demographic, or recruitment states, as emphasized in work on ecological or functional extinction (Soulé et al. 2005; McConkey & Drake 2006; Valiente-Banuet et al. 2015). Monitoring abundance or allele presence alone can therefore miss the endpoint most relevant to ecosystem function.

The practical implication is that genetic-warning thresholds require biological calibration. A threshold learned in one species, trait architecture, or deterioration regime should not be transferred without evidence of comparable state turnover, interaction feedback, baseline eligibility, censoring, and timescale. Evolutionary rescue and early warning are related but non-identical: high-trait-directed turnover may support persistence while reducing observable loss events, whereas low-trait-directed turnover may accelerate loss and compress the intervention window. More generally, rescue depends jointly on variation supply, demography, and environmental deterioration (Gomulkiewicz & Holt 1995; Carlson et al. 2014; Bell 2017).

The study remains finite and conditional. `p_mu*` is an effective recurrent-transition equilibrium, not an estimated mutation spectrum. The warning comparison includes two calibrated domains rather than all 15 coordinates, and endpoint counts are correlated within trajectories. These findings are Type S evidence for declared closures, not a universal theorem of genetic warning.

Genetic monitoring should therefore not be interpreted independently of ecological process. Warning reliability is not intrinsic to genetic diversity trajectories; it is an emergent property of the eco-genetic closure that generates functional persistence, loss events, and the opportunity to observe them.

## Relationship to the predecessor

The predecessor and extension remain separate evidence ledgers. The predecessor supplies the theorem-guided ecological mechanism and conditional symmetric benchmark; the extension supplies independent source reconstruction, warning-blind regime mapping, and fresh-seed comparison under altered transition closure. Numerical results remain attributed to their originating protocols.

## Data and code availability

Model code, protocols, immutable grid locks, calibration decisions, validation summaries, figure builders, workflow identifiers, and artifact digests are maintained in this repository and its pinned predecessor.

## References

The verified reference list is provided in `manuscript/references.md` and is included in the reproducible submission bundle.
