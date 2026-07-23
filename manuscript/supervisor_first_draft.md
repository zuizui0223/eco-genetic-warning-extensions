# Genetic warning emerges from eco-genetic closure in fragmented systems

## Abstract

Ecological function can disappear before population extinction, motivating indicators of realised functional-trait loss. We tested whether genetic warning is portable across eco-genetic closures by combining a finite model of interaction feedback and fragmentation with an extension incorporating directional recurrent transitions. Under a symmetric benchmark, diversity erosion preceded all 35 trait-loss events. Across 15 transition coordinates, 2,269 of 3,375 reconstructed sources were supported, but warning-blind calibration identified no eligible validation domain among 20,250 attempts because candidate regimes separated into rapid loss, persistence, or seed heterogeneity. A separately declared protocol recovered two calibrated domains. The symmetric bridge produced 323 leads, one tie, and no lags across 324 valid comparisons; the directional transition produced 184 leads, five ties, and 12 lags across 201 comparisons, shortening median positive lead time from 106–112 to 74–81 generations. Warning availability, ordering, censoring, and intervention time therefore emerged from ecological, demographic, genetic, and observational closure.

## Introduction

Ecological deterioration can eliminate an interaction-dependent trait before the population carrying it goes extinct. This distinction matters because conservation often seeks to maintain pollination, dispersal, defence, mutualism, or other ecological processes rather than population persistence alone (Soulé et al. 2005; McConkey & Drake 2006; Valiente-Banuet et al. 2015). Abundance, allele presence, genetic diversity, interaction state, and realised trait occupancy are therefore distinct monitoring targets.

Early-warning research asks whether a statistic changes before collapse (Scheffer et al. 2009; Drake & Griffen 2010), whereas genetic monitoring asks whether changes in diversity or allele frequency reveal deterioration before demographic or functional loss (Schwartz et al. 2007; Stange et al. 2021). Both can overlook a more fundamental dependency: warning depends on mechanism, observation, and event definition and need not be universal across systems (Hastings & Wysham 2010; Boettiger & Hastings 2012, 2013). The closure linking ecological feedback, demography, inheritance, recurrent state turnover, observation, and the loss endpoint may determine whether a warning is observable, whether it precedes loss, and whether sufficient comparable events exist to validate it.

A predecessor framework linked interaction thresholds, fragmentation, local effective size, realised high-trait occupancy, and genetic diversity. This connection is consistent with broader evidence that spatial structure jointly alters demography, interactions, gene flow, drift, and adaptation (Legrand et al. 2017; Govaert et al. 2019). Under one independently calibrated symmetric-transition configuration, baseline-relative diversity erosion preceded observed trait loss. That result was explicitly conditional on one life-cycle closure and one selected deterioration domain.

Here, we alter one genetic boundary condition while holding the ecological life cycle fixed. Recurrent transitions between high-trait-associated and low-trait-associated states need not be symmetric. The directional introduction of variants can shape evolutionary outcomes, but its effects depend on selection, demography, and the supply of alternatives (Stoltzfus & McCandlish 2017; Storz et al. 2019). Separating transition-map relaxation strength from equilibrium direction changes recurrent input and loss without altering selection, migration, finite drift, trait recruitment, source transfer, projection, or trait-loss semantics.

We ask whether transition direction changes high-trait source reconstruction, realised trait-loss regimes, the existence of a warning-validation domain under a warning-blind rule, and warning availability, ordering, censoring, and lead time after independent calibration. Our central proposition is that genetic warning is an emergent property of eco-genetic closure rather than a portable property of a diversity statistic (Figure 1).

## Model and methods

### Eco-genetic framework

The predecessor framework describes a finite eco-genetic system in which habitat configuration alters interaction intensity, the stability of a high-trait ecological state, local effective population size, genetic diversity, and realised high-trait occupancy. The principal causal sequence is

`patch size -> interaction intensity -> high-trait-state stability -> local effective size -> genetic diversity -> realised functional-trait loss`.

Potential viability, allele persistence, realised trait occupancy, and genetic diversity are tracked as distinct states. This distinction allows functional-trait loss to occur before population extinction and prevents abundance, allele presence, and ecological function from being treated as interchangeable outcomes.

### Directional recurrent-transition operator

Let `p` denote the high-trait-associated allele frequency. The recurrent transition operator is

\[
M(p)=\kappa_\mu p_\mu^\ast+(1-\kappa_\mu)p.
\]

Here, $\kappa_\mu$ controls contraction towards the transition-only equilibrium, and $p_\mu^*$ controls direction. In code, tables, and figure labels, these quantities are recorded as `kappa_mu` and `p_star`, respectively. The effective transition rates are

\[
u_{L\to H}=\kappa_\mu p_\mu^\ast,\qquad
u_{H\to L}=\kappa_\mu(1-p_\mu^\ast).
\]

At a local post-transition threshold $p_c$, the required pre-transition frequency is

\[
\theta(p_c)=\frac{p_c-\kappa_\mu p_\mu^\ast}{1-\kappa_\mu}.
\]

Increasing $p_\mu^*$ therefore lowers the pre-transition frequency required to remain above a high-state boundary. We tested, rather than assumed, whether this local mechanism organizes the finite stochastic system. The operator can represent recurrent mutation, gain–loss asymmetry, epimutation, switching, or another effective state transition; $p_\mu^*$ is not an empirical mutation-rate estimate.

### Protocol 002: source reconstruction and warning-blind calibration

We evaluated three relaxation strengths (`0.05`, `0.20`, `0.35`) and five transition equilibria (`0.10`, `0.25`, `0.50`, `0.75`, `0.90`). All other life-cycle components were inherited from pinned predecessor commit `dd8ee379d0d3518194c767d16402042525bc00dc`.

Source reconstruction was repeated independently for every coordinate using three area-reference values, three interaction-feedback values, five master seeds, and five replicates. Prepared sources were held for 30 generations and projected into one-large, equal-isolated, and equal-migrating landscapes. Projection support required every declared invariant to pass.

Warning-blind calibration evaluated two horizons and three normalized barrier increases using five new calibration seeds and five replicates. Calibration could inspect only source eligibility and realised trait loss. A candidate was eligible only if every seed block had a post-baseline trait-loss frequency in `[0.30, 0.70]`; otherwise, the protocol required `no_domain_selected` without expanding the candidate family. No diversity, warning, lead–lag, warning-time, or lead-time quantity was available during calibration.

### Protocol 003: independently calibrated warning comparison

Because Protocol 002 selected no domain, a separately declared protocol used independent seed families for bracket search, calibration, confirmation, and validation. Two domains were fixed before warning outcomes were computed: a symmetric bridge (`kappa_mu=0.20`, `p_star=0.50`) and a directional transition (`kappa_mu=0.05`, `p_star=0.90`). Validation used five fresh master seeds and 20 replicates per seed in each domain.

Relative warnings were defined as the first post-baseline generation at which `H_alpha` or `H_gamma` declined by 5%, 10%, or 20% from its own baseline. Analyses retained baseline ineligibility, warning censoring, trait-loss censoring, ties, leads, and lags. The six endpoint records from each trajectory are correlated and are not independent biological replicates.

## Results

### Fragmentation established an eco-genetic route to warning

The predecessor mechanism linked patch size to interaction intensity, high-trait-state stability, local effective size, diversity, and realised high-trait occupancy. Equal isolation reduced interaction, local effective size, and realised high-trait mass relative to one large patch. Under one independently calibrated symmetric closure, baseline-relative erosion across all six preregistered endpoints preceded all 35 observed trait-loss events. This benchmark is conditional rather than universal; Figure 1 summarizes its causal position within the coupled system.

### Transition direction reorganized high-trait source feasibility

All 3,375 planned source attempts were completed. Source support, full-state preparation, and supported projection each occurred in 2,269 attempts (67.23%); every prepared source passed all projection invariants. Coordinate support ranged from 101 of 225 attempts (44.89%) at `kappa_mu=0.05`, `p_star=0.10` to 195 of 225 attempts (86.67%) at `kappa_mu=0.35`, `p_star=0.90`. Within each relaxation-strength row, support generally increased with `p_star`, a pattern consistent with the local threshold mechanism at the finite source-reconstruction scale (Figure 2).

### Eco-genetic closures separated into loss regimes

Warning-blind calibration completed 20,250 attempts in 810 batches. Among 648 candidates with complete five-seed blocks, 322 had all loss frequencies above the eligibility band, 242 had all rates below it, and 84 crossed the band among seeds (Figures 3 and 4).

Low transition equilibria were dominated by rapid loss: the closest candidates at `p_star=0.10` had a loss frequency of 1.0 in every seed block and at every relaxation strength. High transition equilibria at stronger relaxation were dominated by persistence, including zero loss in every seed block at (`0.20`, `0.90`), (`0.35`, `0.75`), and (`0.35`, `0.90`). Intermediate coordinates were often seed-heterogeneous; at (`0.20`, `0.50`), for example, the pooled frequency was 0.524, whereas seed-block rates ranged from 0.20 to 0.80.

None of the 648 complete candidates satisfied the all-seed rule, so all 15 coordinates were recorded as `no_domain_selected`. This was an event-regime result, not evidence that genetic warning failed. It showed that a common deterioration family suitable for warning validation did not exist under the declared source and calibration design.

### Warning reliability emerged from calibrated closures

The separately declared recovery protocol identified two eligible domains using fresh seeds and greater within-seed replication. The symmetric bridge had a pooled trait-loss frequency of 0.679 among 84 baseline-eligible trajectories; the directional transition had a frequency of 0.625 among 88. Both domains were locked before validation diversity trajectories were examined.

Fresh-seed validation completed 200 attempts. In the symmetric bridge, 82 trajectories were completed, and each endpoint produced 54 valid warning–loss pairs. Across 324 correlated comparisons, 323 were leads, one was a tie, and none was a lag; median positive lead time was 106–112 generations. In the directional transition, 91 trajectories were completed, valid-pair availability ranged from 28 to 38 among endpoints, and ten trajectories remained baseline-ineligible throughout. Across 201 valid comparisons, 184 were leads, five were ties, and 12 were lags; median positive lead time was 74–81 generations. Warning censoring increased at stricter thresholds, especially for `H_gamma` (Figures 5 and 6).

Relative diversity erosion remained predominantly leading in the directional domain, but it was less consistently available, occasionally lagged, and provided a shorter intervention window than in the symmetric bridge.

## Discussion

### Genetic warning is conditional on the full eco-genetic closure

The central result is not simply that genetic diversity declined before realised functional-trait loss. That ordering was nearly deterministic in the independently calibrated symmetric benchmark, but it became less available and less consistent in the directional-transition domain. The symmetric bridge produced 323 leads, one tie, and no lags across 324 valid endpoint comparisons, with median positive lead times of 106–112 generations. The directional transition produced 184 leads, five ties, and 12 lags across 201 valid comparisons, with median positive lead times of 74–81 generations and stronger censoring. These endpoint counts are correlated within trajectories and are not independent replicates, but the contrast shows that the same class of relative-diversity signal can occupy different warning regimes under different recurrent-transition closures.

This result aligns with a central lesson of ecological early-warning research: indicators are conditional on the mechanism of transition. Critical slowing down and related signals are informative in some systems, while other transitions provide weak, reversed, or no generic warning (Scheffer et al. 2009; Hastings & Wysham 2010; Boettiger & Hastings 2012, 2013). Our contribution is to extend that conditionality to the genetic life cycle. A genetic statistic cannot be evaluated apart from the processes governing effective population size, migration, drift, selection, trait recruitment, and the recurrent supply or loss of trait-associated states.

### Warning-validation feasibility is itself a biological result

Before warning validation, the common Protocol 002 calibration family generated rapid-loss, persistence, and seed-heterogeneous regimes. None of the 648 complete five-seed candidates satisfied the preregistered requirement that every seed block have an intermediate trait-loss frequency, and all 15 transition coordinates were recorded as `no_domain_selected`. This was not a failed simulation and does not show that warning was absent. It shows that a shared experimental regime suitable for comparing warning performance did not exist under the declared source and deterioration family.

This distinction matters because warning studies can be biased by conditioning on convenient events. A rapid-loss system may provide many losses but little usable intervention time; a persistent system may retain function but provide too few events to estimate warning ordering; a seed-heterogeneous system may appear suitable after pooling even when the event regime is not reproducible. By treating calibration feasibility and censoring as outcomes, the study avoids tuning deterioration or thresholds until a desired warning appears.

### Functional-trait loss is not population extinction

The focal ecological endpoint was realised loss of a high-trait state, not extinction of the entire population. This places the work closer to the literature on ecological and functional extinction than to models that define failure only as zero abundance. Species can persist numerically while becoming ineffective pollinators, seed dispersers, mutualists, defenders, or ecosystem engineers. Such losses can reorganise communities before taxonomic disappearance (Soulé et al. 2005; McConkey & Drake 2006; Valiente-Banuet et al. 2015).

The model makes this distinction operational by separating potential viability, allele persistence, realised trait occupancy, local effective population size, and genetic diversity. This separation is ecologically important because a monitoring programme based only on abundance may detect decline after an interaction-dependent function has already crossed its effective threshold. Conversely, genetic erosion may precede realised functional loss and provide intervention time even when census abundance remains substantial.

### Relation to evolutionary rescue and mutation bias

The directional-transition results are adjacent to evolutionary rescue but do not demonstrate rescue in the conventional sense. Evolutionary-rescue theory asks whether heritable change prevents demographic extinction under environmental deterioration. Our endpoint is functional-trait loss, and a persistence-favouring transition may preserve that function without establishing whether the entire population would otherwise have gone extinct. The relevant extension is therefore from rescue probability to the observability and timing of warning before a functional endpoint.

Likewise, $p_\mu^*$ should not be interpreted as an empirically estimated nucleotide mutation rate or as evidence for directed adaptive mutation. It represents the equilibrium direction of effective recurrent transitions between high-trait-associated and low-trait-associated states. Mutation-bias theory predicts that asymmetries in the introduction of variation can shape outcomes through their interaction with selection and finite population size. Our results show a corresponding ecological consequence within the declared closure: transition direction altered source feasibility, trait-loss regime, warning-pair availability, censoring, ordering, and lead time. The biological analogue could include allelic mutation, biased loss and gain of function, epigenetic switching, developmental state transitions, or other recurrent processes, but mapping the effective parameter to a particular mechanism requires system-specific data.

### Fragmentation, connectivity, and genetic monitoring

The predecessor results established the mechanistic bridge from patch geometry and interaction feedback to local effective size, realised high-trait mass, and genetic diversity. This bridge helps explain why a genetic warning can exist: fragmentation changes more than abundance; it modifies the interaction and reproductive context that generates both function and genetic variation. At the same time, neither connectivity nor migration is uniformly beneficial. Gene flow can increase variation and rescue small populations, but it can also impose migration load, erode local adaptation, or alter interaction-dependent states. The management target is therefore not maximum connectivity or maximum diversity in isolation, but a joint regime in which ecological function, adaptive or functional variation, and actionable warning coexist.

Conservation genomics increasingly provides temporal estimates of diversity, inbreeding, connectivity, and effective population size, but those measurements are often interpreted as generic indicators of population health. The present results support a more conditional use. Relative genetic erosion may be informative when it is calibrated against the ecological function at risk, the observation horizon, and the system's demographic and recurrent-transition processes. The same threshold should not be transferred uncritically between species, traits, or landscapes.

### Censoring has ecological meaning

Censored trajectories were not homogeneous missing data. They included systems in which function persisted throughout the horizon, warning thresholds were not crossed, trait loss was not observed, the baseline was ineligible, or source preparation failed. Each category corresponds to a different ecological or monitoring regime. Reporting only valid event pairs would exaggerate apparent reliability by omitting cases where a warning could not be used. For conservation decisions, warning availability is as important as conditional ordering: a signal that leads whenever both events occur may still have limited operational value if valid pairs are rare or baseline conditions are frequently unavailable.

### Limits and next empirical steps

All numerical results are finite Type S evidence for declared model closures. The study does not establish a universal theorem that transition direction controls genetic warning, estimate biological mutation rates, or show that neutral genetic diversity universally predicts functional decline. Only two independently calibrated Protocol 003 domains entered warning validation, and the six endpoints within a trajectory share the same underlying simulation. The contrast should therefore be interpreted mechanistically rather than as a population-level estimate of a universal effect size.

Empirical tests require repeated measurements of at least four distinct layers: spatial configuration and connectivity, the interaction-dependent functional trait, effective population size or genetic diversity, and the recurrent process generating or removing trait-associated states. Candidate systems include plant–pollinator or plant–disperser interactions, host–symbiont states, defence traits, and other functions for which ecological effectiveness can be measured before population extinction. A prospective design should predefine the functional-loss threshold, collect temporal genetic data, retain non-events, and estimate whether a relative genetic change creates useful intervention time.

## Conclusion

Fragmentation and interaction loss can create conditions in which genetic diversity erosion precedes realised functional-trait loss, but that warning is not a property of genetic diversity alone. Directional recurrent transitions changed whether high-trait sources could be established, whether losses occurred often enough for calibration, whether warning–loss pairs were observable, whether warnings led or lagged, and how much time remained before functional loss. Genetic warning is therefore best understood as an emergent, system-specific property of an eco-genetic closure. Conservation monitoring can gain intervention time from genetic data, but only when genetic signals are calibrated to the ecological function and biological turnover process they are intended to warn about.

## Relationship to the predecessor

The predecessor and extension remain separate evidence ledgers. The predecessor supplies the theorem-guided ecological mechanism and conditional symmetric benchmark; the extension supplies independent source reconstruction, warning-blind regime mapping, and fresh-seed comparison under an altered transition closure. Numerical results remain attributed to their originating protocols.

## Data and code availability

Model code, protocols, immutable grid locks, calibration decisions, validation summaries, figure builders, workflow identifiers, and artifact digests are maintained in this repository and its pinned predecessor.

## References

Bell, G. (2017). Evolutionary rescue. *Annual Review of Ecology, Evolution, and Systematics*, **48**, 605–627. doi:10.1146/annurev-ecolsys-110316-023011

Boettiger, C. & Hastings, A. (2012). Quantifying limits to detection of early warning for critical transitions. *Journal of the Royal Society Interface*, **9**, 2527–2539. doi:10.1098/rsif.2012.0125

Boettiger, C. & Hastings, A. (2013). No early warning signals for stochastic transitions: insights from large deviation theory. *Proceedings of the Royal Society B*, **280**, 20131372. doi:10.1098/rspb.2013.1372

Carlson, S.M., Cunningham, C.J. & Westley, P.A.H. (2014). Evolutionary rescue in a changing world. *Trends in Ecology & Evolution*, **29**, 521–530. doi:10.1016/j.tree.2014.06.005

Drake, J.M. & Griffen, B.D. (2010). Early warning signals of extinction in deteriorating environments. *Nature*, **467**, 456–459. doi:10.1038/nature09389

Gomulkiewicz, R. & Holt, R.D. (1995). When does evolution by natural selection prevent extinction? *Evolution*, **49**, 201–207. doi:10.1111/j.1558-5646.1995.tb05971.x

Govaert, L., Fronhofer, E.A., Lion, S., Eizaguirre, C., Bonte, D., Egas, M., Hendry, A.P., De Brito Martins, A., Melián, C.J., Raeymaekers, J.A.M., Ratikainen, I.I., Sæther, B.-E., Schweitzer, J.A. & Matthews, B. (2019). Eco-evolutionary feedbacks—Theoretical models and perspectives. *Functional Ecology*, **33**, 13–30. doi:10.1111/1365-2435.13241

Hastings, A. & Wysham, D.B. (2010). Regime shifts in ecological systems can occur with no warning. *Ecology Letters*, **13**, 464–472. doi:10.1111/j.1461-0248.2010.01439.x

Legrand, D., Cote, J., Fronhofer, E.A., Holt, R.D., Ronce, O., Schtickzelle, N., Travis, J.M.J. & Clobert, J. (2017). Eco-evolutionary dynamics in fragmented landscapes. *Ecography*, **40**, 9–25. doi:10.1111/ecog.02537

McConkey, K.R. & Drake, D.R. (2006). Flying foxes cease to function as seed dispersers long before they become rare. *Ecology*, **87**, 271–276. doi:10.1890/05-0386

Scheffer, M., Bascompte, J., Brock, W.A., Brovkin, V., Carpenter, S.R., Dakos, V., Held, H., van Nes, E.H., Rietkerk, M. & Sugihara, G. (2009). Early-warning signals for critical transitions. *Nature*, **461**, 53–59. doi:10.1038/nature08227

Schwartz, M.K., Luikart, G. & Waples, R.S. (2007). Genetic monitoring as a promising tool for conservation and management. *Trends in Ecology & Evolution*, **22**, 25–33. doi:10.1016/j.tree.2006.08.009

Soulé, M.E., Estes, J.A., Miller, B. & Honnold, D.L. (2005). Strongly interacting species: conservation policy, management, and ethics. *BioScience*, **55**, 168–176. doi:10.1641/0006-3568(2005)055[0168:SISCPM]2.0.CO;2

Stange, M., Barrett, R.D.H. & Hendry, A.P. (2021). The importance of genomic variation for biodiversity, ecosystems and people. *Nature Reviews Genetics*, **22**, 89–105. doi:10.1038/s41576-020-00288-7

Stoltzfus, A. & McCandlish, D.M. (2017). Mutational biases influence parallel adaptation. *Molecular Biology and Evolution*, **34**, 2163–2172. doi:10.1093/molbev/msx180

Storz, J.F., Natarajan, C., Signore, A.V., Witt, C.C., McCandlish, D.M. & Stoltzfus, A. (2019). The role of mutation bias in adaptive molecular evolution: insights from convergent changes in protein function. *Philosophical Transactions of the Royal Society B*, **374**, 20180238. doi:10.1098/rstb.2018.0238

Valiente-Banuet, A., Aizen, M.A., Alcántara, J.M., Arroyo, J., Cocucci, A., Galetti, M., García, M.B., García, D., Gómez, J.M., Jordano, P., Medel, R., Navarro, L., Obeso, J.R., Oviedo, R., Ramírez, N., Rey, P.J., Traveset, A., Verdú, M. & Zamora, R. (2015). Beyond species loss: the extinction of ecological interactions in a changing world. *Functional Ecology*, **29**, 299–307. doi:10.1111/1365-2435.12356