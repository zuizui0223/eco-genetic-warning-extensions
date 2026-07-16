# Genetic warning emerges from eco-genetic closure in fragmented systems

## Abstract

Ecological function can disappear before population extinction, creating a need for indicators that warn of realised trait loss rather than abundance decline alone. Yet genetic-warning performance is often treated as a property of a diversity statistic, even though the ecological and genetic processes generating the statistic also determine whether comparable loss events occur. We integrated a theorem-guided finite eco-genetic model of interaction feedback and fragmentation with an independently declared directional-transition extension. Under a symmetric benchmark, equal isolation reduced interaction, local effective size, and realised high-trait mass, and baseline-relative erosion of two diversity measures preceded all 35 observed trait-loss events across six preregistered endpoints. We then separated recurrent-transition relaxation strength from equilibrium direction. Across 15 preregistered coordinates, 2,269 of 3,375 independently reconstructed sources were preparation- and projection-supported, with support ranging from 44.89% to 86.67%. Warning-blind calibration comprised 20,250 attempts: among 648 complete candidates, 322 were rapid-loss-side, 242 persistence-side, and 84 seed-heterogeneous, leaving no common eligible validation domain under the preregistered family. A separately declared protocol recovered two independently calibrated domains. The symmetric bridge yielded 323 leads, one tie, and no lags across 324 valid endpoint comparisons, whereas a directional transition yielded 184 leads, five ties, and 12 lags across 201 comparisons and shortened median positive lead time from 106–112 to 74–81 generations. Genetic warning was therefore not portable across closures: its availability, ordering, and intervention time emerged from the joint ecological, demographic, genetic, and observation system.

## Introduction

Ecological deterioration can remove an interaction-dependent or functional trait before the population carrying it goes extinct. Such functional loss matters because conservation frequently seeks to maintain pollination, dispersal, defence, mutualism, or other ecological processes rather than population persistence alone. Abundance, allele presence, genetic diversity, interaction state, and realised trait occupancy are therefore distinct monitoring targets.

Early-warning research usually asks whether a statistic changes before collapse. Genetic monitoring similarly asks whether diversity or allele-frequency change can reveal deterioration before demographic or functional loss. Both approaches can miss a more basic dependency: the biological closure linking ecological feedback, demography, inheritance, recurrent state turnover, observation, and the loss endpoint may determine whether a warning is observable, whether it precedes loss, and whether enough comparable events exist to validate it.

A predecessor framework established exact and finite-model links among interaction thresholds, fragmentation, local effective size, realised high-trait occupancy, and genetic diversity. Under one independently calibrated symmetric-transition configuration, baseline-relative diversity erosion preceded observed trait loss. That finding was explicitly conditional on one life-cycle closure and one selected deterioration domain.

Here we test whether warning remains stable when one genetic boundary condition is changed while the ecological life cycle is held fixed. Recurrent transitions between high-trait-associated and low-trait-associated states need not be symmetric. Separating transition-map relaxation strength from equilibrium direction allows recurrent input and loss to change without modifying selection, migration, finite drift, trait recruitment, source transfer, projection, or trait-loss semantics.

We ask whether transition direction changes (i) reconstruction of a high-trait source, (ii) the realised trait-loss regime, (iii) the existence of a warning-validation domain under a warning-blind decision rule, and (iv) warning availability, ordering, censoring, and lead time after independent calibration. Our central proposition is that genetic warning is an emergent property of eco-genetic closure rather than a portable property of a diversity statistic.

## Model and mechanism

Let `p` denote the high-trait-associated allele frequency. The recurrent transition operator is

\[
M(p)=\kappa_\mu p_\mu^\ast+(1-\kappa_\mu)p.
\]

Here `kappa_mu` controls contraction toward the transition-only equilibrium and `p_mu*` controls direction. The effective transition rates are

\[
u_{L\to H}=\kappa_\mu p_\mu^\ast,\qquad
u_{H\to L}=\kappa_\mu(1-p_\mu^\ast).
\]

At a local post-transition threshold `p_c`, the required pre-transition frequency is

\[
\theta(p_c)=\frac{p_c-\kappa_\mu p_\mu^\ast}{1-\kappa_\mu}.
\]

Increasing `p_mu*` therefore lowers the pre-transition frequency required to remain above a high-state boundary. Whether this local mechanism organizes the finite stochastic system was tested rather than assumed. The operator can represent recurrent mutation, gain–loss asymmetry, epimutation, switching, or another effective state transition; `p_mu*` is not interpreted as an empirical mutation-rate estimate.

## Protocol

We evaluated three relaxation strengths (`0.05`, `0.20`, `0.35`) and five transition equilibria (`0.10`, `0.25`, `0.50`, `0.75`, `0.90`). All other life-cycle components were inherited from pinned predecessor commit `dd8ee379d0d3518194c767d16402042525bc00dc`.

Source reconstruction was repeated independently for every coordinate using three area-reference values, three interaction-feedback values, five master seeds, and five replicates. Each prepared source was held for 30 generations and projected into the declared one-large, equal-isolated, and equal-migrating landscapes. A projection was supported only when all invariants passed.

Warning-blind calibration evaluated two horizons and three normalized barrier increases using five new calibration seeds and five replicates. Calibration could inspect source eligibility and realised trait loss only. Diversity values, warning times, lead/lag status, and usable lead time were unavailable. A candidate was eligible only if every seed block had post-baseline trait-loss frequency in `[0.30, 0.70]`. If none qualified, the protocol required `no_domain_selected` without expanding the candidate family.

Because the preregistered family selected no domain, a separate protocol was declared. It used independent seed families for bracket search, calibration, confirmation, and warning validation. Two confirmation-eligible domains were fixed before warning outcomes were computed: a symmetric bridge (`kappa_mu=0.20`, `p_star=0.50`) and a directional transition (`kappa_mu=0.05`, `p_star=0.90`). Validation used five fresh master seeds and 20 replicates per seed in each domain.

Relative warnings were defined within trajectories as the first post-baseline generation at which `H_alpha` or `H_gamma` declined by 5%, 10%, or 20% from its own baseline. Each comparison retained baseline ineligibility, warning censoring, trait-loss censoring, ties, leads, and lags. The six endpoint records from one trajectory are correlated and are not treated as independent biological replicates.

## Results

### Fragmentation established an eco-genetic route to warning

The predecessor mechanism linked patch size to interaction intensity, high-trait-state stability, local effective size, genetic diversity, and realised high-trait occupancy. Equal isolation reduced interaction, local effective size, and realised high-trait mass relative to one large patch. Under one independently calibrated symmetric closure, 35 observed trait-loss events were preceded by baseline-relative erosion across all six preregistered diversity endpoints. This benchmark is conditional rather than universal.

### Transition direction reorganized high-trait source feasibility

All 3,375 planned source attempts were completed. Source support, full-state preparation, and supported projection each occurred in 2,269 attempts (67.23%). The three counts were identical because every prepared source passed all projection invariants; there were zero projection failures and 1,106 attempts in which projection was not run because source reconstruction or preparation was unsupported.

Success varied strongly across the transition-coordinate map. The minimum was 101 of 225 attempts (44.89%) at `kappa_mu=0.05`, `p_star=0.10`, whereas the maximum was 195 of 225 (86.67%) at `kappa_mu=0.35`, `p_star=0.90`. Within each relaxation-strength row, support generally increased toward higher `p_star`. At `kappa_mu=0.35`, support rose from 53.33% at `p_star=0.10` to 86.67% at `p_star=0.90`. Thus the local threshold mechanism extended to a finite source-reconstruction boundary despite stochastic and parameter-cell variation.

### Eco-genetic closures separated into rapid-loss, persistence, and heterogeneous regimes

Warning-blind calibration completed all 20,250 attempts in 810 resumable batches. Of 648 candidates with complete five-seed blocks, 322 had all seed-block loss frequencies above the eligibility band, 242 had all rates below it, and 84 crossed the band among seeds.

Low transition equilibria were dominated by rapid-loss candidates. For example, the closest candidates at `p_star=0.10` had loss frequency 1.0 across all five seed blocks at every tested relaxation strength. High transition equilibria at stronger relaxation were dominated by persistence: the closest candidates at (`0.20`, `0.90`), (`0.35`, `0.75`), and (`0.35`, `0.90`) had loss frequency zero in every seed block. Intermediate coordinates were often seed-heterogeneous. At (`0.05`, `0.90`), the closest candidate had pooled loss frequency 0.458 with seed-block rates 0.60, 0.40, 0.25, 0.60, and 0.40. At the symmetric coordinate (`0.20`, `0.50`), the closest candidate had pooled frequency 0.524 but seed-block rates ranging from 0.20 to 0.80.

None of the 648 complete candidates satisfied the all-seed eligibility rule. All 15 coordinates were therefore recorded as `no_domain_selected`. This was a preregistered event-regime result, not evidence that genetic warning failed.

### Warning reliability emerged from independently calibrated closures

The separately declared confirmation calibration recovered two eligible domains using larger within-seed replication and fresh seeds while retaining the eligibility rule. The symmetric bridge had pooled trait-loss frequency 0.679 among 84 baseline-eligible trajectories; the directional transition had pooled frequency 0.625 among 88 eligible trajectories. Both domains were locked before validation diversity trajectories were examined.

Fresh-seed validation completed 200 attempts. In the symmetric bridge, 82 trajectories completed and each of the six endpoints produced 54 valid warning–loss pairs. Across the 324 correlated endpoint comparisons, 323 were leads, one was a tie, and none was a lag. Median positive lead time ranged from 106 to 112 generations. Twenty-eight completed trajectories per endpoint had censored trait loss, while warning censoring and baseline ineligibility were absent.

In the directional transition, 91 trajectories completed, but valid-pair availability varied from 28 to 38 among endpoints. Ten trajectories were baseline-ineligible for every endpoint. Across 201 valid comparisons, 184 were leads, five were ties, and 12 were lags. Warning censoring increased with stricter decline thresholds and was more frequent for `H_gamma`; at the 20% `H_gamma` endpoint, 24 trajectories were warning-censored and four valid pairs lagged trait loss. Median positive lead times ranged from 74 to 81 generations.

Relative diversity erosion therefore remained predominantly leading in the directional domain, but the warning was less consistently available, included non-zero lag, and provided a shorter intervention window than the symmetric bridge.

## Discussion

Genetic warning was not portable across the tested eco-genetic closures. The same diversity endpoints that produced nearly uniform leading order under the symmetric bridge became less available, more censored, occasionally lagging, and shorter-lived under a directional transition. Mutation or effective state-transition direction was one mechanism that moved the system among closures; the broader result is that warning behaviour emerged from the joint ecological, demographic, genetic, and observation process.

Event-regime feasibility is part of early-warning biology. A system with nearly certain rapid functional loss offers little discrimination among warning rules, whereas a persistent system yields too few loss events for validation. Seed-heterogeneous regimes create a third problem: pooled event frequencies can appear suitable while individual seed blocks occupy opposing regimes. Reporting `no_domain_selected` is therefore informative because it identifies where warning performance cannot be estimated under a declared design.

Functional-trait loss is also distinct from population extinction. Populations and trait-associated alleles may persist while realised ecological function disappears through altered interaction, demographic, or recruitment states. Monitoring programmes that track abundance or allele presence alone can consequently miss the endpoint most relevant to ecosystem function.

The practical implication is that genetic-warning thresholds require biological calibration. A threshold learned in one species, trait architecture, or deterioration regime should not be transferred without evidence of comparable state turnover, interaction feedback, baseline eligibility, censoring, and timescale. Evolutionary rescue and early warning are related but non-identical goals: high-trait-directed turnover may promote persistence while reducing observable loss events, whereas low-trait-directed turnover may accelerate loss and compress the intervention window.

The study remains finite and conditional. `p_mu*` is an effective recurrent-transition equilibrium, not an estimated mutation spectrum for a particular species. The warning comparison includes two independently calibrated domains rather than all 15 coordinates, and endpoint counts are correlated within trajectories. These findings are Type S evidence for declared closures, not a universal theorem of genetic warning.

The general conclusion is nevertheless clear: genetic monitoring should not be interpreted independently of ecological process. Warning reliability is not an intrinsic property of genetic diversity trajectories; it is an emergent property of the eco-genetic closure that generates functional persistence, loss events, and the opportunity to observe them.

## Relationship to the predecessor

The predecessor and extension remain separate evidence ledgers. The predecessor supplies the theorem-guided ecological mechanism and conditional symmetric benchmark; the extension supplies independent source reconstruction, warning-blind regime mapping, and fresh-seed comparison under altered transition closure. Numerical results are attributed to their originating protocols and are not retroactively reassigned.

## Data and code availability

All model code, protocols, immutable grid locks, batch workflows, calibration decisions, validation summaries, figure builders, and submission-package workflows are maintained in this repository. The pinned predecessor commit and every source workflow run and artifact digest are recorded in machine-readable metadata.
