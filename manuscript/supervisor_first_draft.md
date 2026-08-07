# Genetic warning emerges from eco-genetic closure in fragmented systems

## Abstract

Ecological function can disappear before population extinction, creating a need for indicators that warn of functional-trait loss. We asked whether genetic erosion can provide such warning and whether its reliability persists when the biological processes generating genetic variation change. In a symmetric benchmark, 83 of 100 trajectories were available; 35 lost the focal trait, and relative diversity erosion preceded all 35 losses across six endpoints. We then altered only recurrent transition direction. Across 15 coordinates, 2,269 of 3,375 sources were supported, while warning-blind calibration separated candidate regimes into rapid loss, persistence, or seed heterogeneity and selected no common validation domain. Independent calibration recovered two domains. The symmetric bridge produced 323 leads, one tie, and no lags; the directional domain produced 184 leads, five ties, and 12 lags and shorter positive lead times. Genetic warning therefore depended on the eco-genetic system generating both signal and loss.

## Introduction

Ecological function can be lost before the population carrying it disappears. A species may remain present while becoming ineffective as a pollinator, seed disperser, mutualist, defender, or other ecological actor (Soulé et al. 2005; McConkey & Drake 2006; Valiente-Banuet et al. 2015). Conservation therefore needs to distinguish population persistence from the persistence of ecological function. Abundance, allele presence, genetic diversity, interaction state, and realised trait occupancy are related, but they are not interchangeable monitoring targets.

Habitat fragmentation provides a direct route by which these states can become uncoupled. Fragmentation changes patch size and connectivity, which can alter interaction intensity, local demography, gene flow, drift, and adaptation (Legrand et al. 2017; Govaert et al. 2019). If an ecological function depends on interaction feedback, a smaller or more isolated patch may first weaken the interaction that supports the function. The resulting ecological change can then reduce realised functional-trait occupancy and local effective population size before the population itself disappears.

This sequence suggests a possible early-warning signal. If local effective size and genetic diversity respond before realised functional-trait loss, genetic erosion may provide intervention time. Early-warning research asks whether a statistic changes before collapse (Scheffer et al. 2009; Drake & Griffen 2010), while genetic monitoring uses changes in diversity or allele frequency to diagnose deterioration (Schwartz et al. 2007; Stange et al. 2021). Yet neither approach guarantees that the same genetic threshold will work across biological systems. Early-warning behaviour depends on the process that generates the signal, the event used to define loss, and the observation window (Hastings & Wysham 2010; Boettiger & Hastings 2012, 2013).

Our predecessor framework followed this logic in three steps. First, it established an interaction threshold for a specified positive-feedback map and connected the low and high interaction branches to potential high-trait viability. Second, a finite-population experiment showed that equal isolation of the same prepared source reduced interaction, local effective size, and realised high-trait mass relative to one large patch. Third, an independently calibrated symmetric genetic closure showed that baseline-relative diversity erosion preceded every observed realised trait-loss event. Fixed absolute diversity thresholds, however, produced both leads and lags. Together, these results raised a new question: is warning reliability a property of genetic diversity itself, or does it depend on the biological processes that generate genetic variation and trait persistence?

Here we test that question by changing one genetic boundary condition while holding the ecological life cycle fixed. Recurrent transitions between high-trait-associated and low-trait-associated states need not be symmetric. Directional introduction of variants can shape evolutionary outcomes, but its effects depend on selection, demography, and the supply of alternatives (Stoltzfus & McCandlish 2017; Storz et al. 2019). We therefore ask whether recurrent-transition direction changes (1) the feasibility of establishing a high-trait source, (2) the realised trait-loss regime, (3) whether a comparable warning-validation domain exists, and (4) the availability, ordering, censoring, and lead time of relative genetic warnings. Our central proposition is that genetic warning is an emergent property of the eco-genetic system that generates both the signal and the functional-loss event (Figure 1).

## Model and methods

### From interaction feedback to realised functional loss

The predecessor framework separates the ecological mechanism from the finite stochastic outcomes. For its stated canonical sigmoid interaction map, the analytical result identifies the conditions under which one interaction state or three fixed points occur; within the strict bistable interval, the low and high fixed points are locally stable and the middle point is unstable. A declared high-trait viability margin then distinguishes potential viability on the low and high branches. These analytical results apply to the specified map and performance surface rather than to all positive-feedback systems.

The finite model asks what happens after those ecological states are embedded in a stochastic trait-allele life cycle. The causal sequence is

`patch size -> interaction intensity -> high-trait-state stability -> local effective size -> genetic diversity -> realised functional-trait loss`.

Potential viability, realised trait occupancy, allele persistence, local effective size, and genetic diversity are tracked separately. This separation allows a population or an allele to remain present even when the realised functional trait has been lost. Full theorem statements, proofs, migration bounds, and the complete finite-model specification belong to the Supplementary Material; the main text retains only the steps needed to connect fragmentation to genetic warning.

### The symmetric warning benchmark

The predecessor study first compared the same prepared high-state source after projection into different landscape configurations. Conditional on successful source preparation and conservation-preserving projection, equal isolation reduced interaction, local effective size, and realised high-trait mass relative to one large patch.

It then evaluated genetic warning as a first-passage problem. Deterioration was calibrated using realised trait loss only; diversity values and warning times were not available during schedule selection. Fresh validation seeds were used after the deterioration domain was locked. Relative warnings were the first post-baseline generations at which `H_alpha` or `H_gamma` declined by 5%, 10%, or 20% from their own baselines. Non-events remained right-censored rather than being assigned the final generation.

The same stored validation trajectories were also evaluated with the predeclared absolute thresholds `H_alpha <= 0.20` and `H_gamma <= 0.20`. This secondary audit did not alter the simulation, threshold, or selected domain. It provides a direct contrast between baseline-relative and fixed absolute warning rules.

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

Increasing $p_\mu^*$ therefore lowers the pre-transition frequency required to remain above a high-state boundary. We tested, rather than assumed, whether this local mechanism organizes the finite stochastic system. The operator can represent recurrent mutation, gain-loss asymmetry, epimutation, switching, or another effective state transition; $p_\mu^*$ is not an empirical mutation-rate estimate.

### Warning-blind source reconstruction and calibration

We evaluated three relaxation strengths (`0.05`, `0.20`, `0.35`) and five transition equilibria (`0.10`, `0.25`, `0.50`, `0.75`, `0.90`). All other life-cycle components were inherited from pinned predecessor commit `dd8ee379d0d3518194c767d16402042525bc00dc`.

Each transition coordinate received an independent source reconstruction rather than inheriting a qualified source from the symmetric benchmark. The source grid used three area-reference values, three interaction-feedback values, five master seeds, and five replicates. Prepared sources were held for 30 generations and projected into one-large, equal-isolated, and equal-migrating landscapes. Projection support required every declared invariant to pass.

Calibration then asked only whether realised trait loss occurred at an intermediate and reproducible frequency. Two horizons and three normalized barrier increases were evaluated with five new calibration seeds and five replicates. A candidate was eligible only if every seed block had a post-baseline trait-loss frequency in `[0.30, 0.70]`. Diversity, warning times, lead-lag ordering, and lead time were unavailable during calibration. If no candidate satisfied the rule, the coordinate was recorded as `no_domain_selected` without expanding the candidate family.

### Independently calibrated warning comparison

Because the common calibration family selected no domain, a separately declared protocol used new and non-overlapping seed families for bracket search, calibration, confirmation, and validation. Two domains were fixed before warning outcomes were computed: a symmetric bridge (`kappa_mu=0.20`, `p_star=0.50`) and a directional transition (`kappa_mu=0.05`, `p_star=0.90`). Validation used five fresh master seeds and 20 replicates per seed in each domain.

Relative warnings again used 5%, 10%, and 20% post-baseline declines in `H_alpha` and `H_gamma`. Analyses retained baseline ineligibility, warning censoring, trait-loss censoring, ties, leads, and lags. The six endpoint records from each trajectory are correlated and are not independent biological replicates.

## Results

### Fragmentation reduced interaction, local effective size, and realised high-trait mass

The ecological mechanism produced the first link in the warning story. A prepared high-trait state could retain interaction memory under the declared finite continuation closure. When the same prepared state was projected into equal isolated fragments, final interaction, local effective size, and realised high-trait mass were lower than in one large patch. These finite results connect the analytical interaction threshold to the demographic and functional states from which genetic warning can emerge (Figure 1).

### Relative genetic erosion preceded functional-trait loss in the symmetric benchmark

Genetic erosion provided a strong but conditional warning in the selected symmetric closure. Of 100 attempted sources, 83 produced an available, projection-supported trajectory. Thirty-five of those 83 trajectories reached post-baseline realised trait loss, whereas the remaining 48 available trajectories were right-censored for trait loss.

For each of the six predeclared relative-diversity endpoints, all 35 valid same-trajectory comparisons had warning before realised trait loss. There were no ties and no lags. This result applies only to observed event pairs in the independently selected symmetric domain; it does not establish a universal warning rule.

Fixed absolute thresholds behaved differently. For `H_alpha <= 0.20`, 20 valid pairs contained 14 leads and six lags. For `H_gamma <= 0.20`, 16 valid pairs contained eight leads and eight lags. The absolute thresholds were therefore not retained as robust warning rules in this closure. The contrast shows that warning performance depended on how genetic change was defined even before the recurrent-transition closure was altered.

### Transition direction changed whether a high-trait source could be established

Changing recurrent-transition direction affected the system before deterioration began. All 3,375 planned source attempts were completed, and 2,269 attempts (67.23%) completed source preparation and supported projection. Every prepared source passed all projection invariants.

Source support varied strongly across the transition map. It ranged from 101 of 225 attempts (44.89%) at `kappa_mu=0.05`, `p_star=0.10` to 195 of 225 attempts (86.67%) at `kappa_mu=0.35`, `p_star=0.90`. Within each relaxation-strength row, support generally increased with `p_star`. Thus recurrent-transition direction changed whether the high-trait ecological starting state could be reconstructed at all (Figure 2).

### Transition direction separated rapid-loss, persistence, and heterogeneous regimes

The same transition map also changed how realised functional loss occurred. Warning-blind calibration completed 20,250 attempts in 810 batches. Among 648 candidates with complete five-seed blocks, 322 had all loss frequencies above the eligibility band, 242 had all rates below it, and 84 crossed the band among seeds (Figures 3 and 4).

Low transition equilibria were dominated by rapid loss. At `p_star=0.10`, the closest candidates had a loss frequency of 1.0 in every seed block and at every relaxation strength. High transition equilibria at stronger relaxation were dominated by persistence, including zero loss in every seed block at (`0.20`, `0.90`), (`0.35`, `0.75`), and (`0.35`, `0.90`). Intermediate coordinates were often seed-heterogeneous; at (`0.20`, `0.50`), for example, the pooled frequency was 0.524 while seed-block rates ranged from 0.20 to 0.80.

No complete candidate satisfied the all-seed eligibility rule. All 15 coordinates were therefore recorded as `no_domain_selected`. This was not evidence that genetic warning failed. It showed that the declared biological and deterioration family did not generate a common event regime in which warning performance could be compared reproducibly.

### Genetic warning became less available and provided less lead time under directional turnover

Independent calibration allowed warning to be compared in two domains without using warning outcomes to select them. The symmetric bridge had a pooled trait-loss frequency of 0.679 among 84 baseline-eligible trajectories, while the directional transition had a frequency of 0.625 among 88. Both domains were locked before validation diversity trajectories were examined.

Fresh-seed validation completed 200 attempts. In the symmetric bridge, 82 trajectories were completed and each endpoint produced 54 valid warning-loss pairs. Across 324 correlated endpoint comparisons, 323 were leads, one was a tie, and none was a lag. Median positive lead time was 106-112 generations.

The directional transition retained predominantly leading warnings but made them less reliable as an operational signal. Ninety-one trajectories were completed, ten remained baseline-ineligible, and valid-pair availability ranged from 28 to 38 across endpoints. Among 201 valid endpoint comparisons, 184 were leads, five were ties, and 12 were lags. Median positive lead time was 74-81 generations, and warning censoring increased at stricter thresholds, especially for `H_gamma` (Figures 5 and 6).

Thus directional turnover did not eliminate genetic warning. It reduced its availability, admitted nonzero lag, and shortened the intervention window in the tested closure.

## Discussion

### Genetic warning is a property of the system, not of the diversity metric alone

The same class of genetic signal behaved differently across biological settings. In the symmetric benchmark, baseline-relative diversity erosion preceded every observed trait-loss event. Fixed absolute thresholds already showed mixed ordering, and changing recurrent-transition direction further reduced warning availability, introduced lags, increased censoring, and shortened positive lead time. Warning reliability therefore cannot be assigned to genetic diversity independently of the ecological and genetic processes that generate both the signal and the loss event.

This conclusion extends a central lesson of ecological early-warning research to genetic monitoring. Early-warning indicators can be informative in some transition mechanisms and weak or misleading in others (Scheffer et al. 2009; Hastings & Wysham 2010; Boettiger & Hastings 2012, 2013). Here, effective population size, migration, drift, selection, trait recruitment, recurrent state turnover, and the observation design jointly determined whether a relative-diversity warning could be observed and whether it arrived before functional loss.

### The ability to validate a warning is itself biologically conditional

A warning cannot be evaluated in the same way when functional loss is almost certain, almost absent, or strongly seed-dependent. The warning-blind calibration exposed all three regimes. Rapid-loss systems generated many losses but potentially little time for intervention. Persistent systems produced too few loss events for reliable warning validation. Seed-heterogeneous systems could appear suitable after pooling even when individual stochastic backgrounds occupied opposing regimes.

The `no_domain_selected` result therefore carries biological information. It identifies a region in which a common deterioration design did not generate reproducible intermediate event risk. Treating this outcome as a result, rather than expanding the search until a convenient warning domain appears, protects the warning comparison from post hoc selection.

### Functional-trait loss is not population extinction

The ecological endpoint in this study was realised loss of a high-trait state, not extinction of the whole population. Species can persist numerically while losing their effectiveness as pollinators, seed dispersers, mutualists, defenders, or other ecological actors (Soulé et al. 2005; McConkey & Drake 2006; Valiente-Banuet et al. 2015). The model therefore separates population persistence, potential trait viability, realised trait occupancy, allele persistence, local effective size, and genetic diversity.

This distinction changes how warning should be interpreted. A population-based monitor may respond after an interaction-dependent function has already been lost. A genetic indicator may respond earlier, but only if the demographic and genetic processes that produce erosion operate on a timescale that precedes realised functional loss. Monitoring should therefore be calibrated against the ecological function at risk rather than against population persistence alone.

### Recurrent-transition direction changes both persistence and observability

The directional-transition experiment is related to evolutionary rescue but does not test demographic rescue in the conventional sense. Evolutionary-rescue theory asks whether heritable change prevents population extinction during environmental deterioration (Gomulkiewicz & Holt 1995; Carlson et al. 2014; Bell 2017). Our endpoint is functional-trait loss. A high-trait-directed transition can favour functional persistence without demonstrating that the whole population would otherwise have gone extinct.

Likewise, $p_\mu^*$ is not an estimated nucleotide mutation rate and does not imply directed adaptive mutation. It represents the equilibrium direction of effective recurrent transitions between high-trait-associated and low-trait-associated states. Such transitions could represent allelic mutation, biased gain and loss of function, epimutation, developmental switching, or another recurrent process. Mapping this effective parameter to a particular mechanism requires system-specific data.

### Genetic monitoring requires biological calibration

The practical implication is not that one genetic metric should replace another. Relative diversity erosion was highly informative in one closure and less available in another, while fixed absolute thresholds were already unreliable in the symmetric benchmark. A warning threshold learned in one species, trait architecture, landscape, or turnover regime should therefore not be transferred without evidence that the underlying interaction feedback, state turnover, deterioration timescale, baseline eligibility, and censoring structure are comparable.

Connectivity should be interpreted with the same caution. The predecessor framework established exact bounds for deterministic allele-frequency mixing, but those bounds do not guarantee demographic or functional rescue. More connectivity or more diversity is therefore not automatically the management target. The relevant target is a biological regime in which ecological function persists and any genetic warning appears early enough to support intervention.

### Censoring is part of the ecological result

Censored trajectories were not homogeneous missing data. They included cases in which function persisted throughout the observation horizon, warning thresholds were never crossed, trait loss was not observed, the baseline was ineligible, or source preparation failed. Each outcome represents a different ecological or monitoring regime.

Reporting only valid warning-loss pairs would therefore overstate operational reliability. A signal can lead almost whenever both events occur and still be of limited use if valid pairs are rare. Warning availability, event ordering, and positive lead time must be interpreted together.

### Limits and empirical tests

All numerical results are finite Type S evidence for declared model closures. The study does not establish a universal theorem that recurrent-transition direction controls genetic warning, estimate biological mutation rates, or show that neutral genetic diversity universally predicts functional decline. Only two independently calibrated directional-comparison domains entered warning validation, and the six endpoint records within a trajectory share the same simulation. The comparison should therefore be interpreted mechanistically rather than as a universal effect-size estimate.

Empirical tests would need repeated measurements of at least four distinct layers: spatial configuration and connectivity, the interaction-dependent ecological function, effective population size or genetic diversity, and the recurrent process that generates or removes trait-associated states. Candidate systems include plant-pollinator and plant-disperser interactions, host-symbiont states, defence traits, and other functions whose ecological effectiveness can be measured before population extinction. A prospective study should predefine the functional-loss threshold, collect temporal genetic data, retain non-events, and ask whether relative genetic change creates useful intervention time.

## Conclusion

Fragmentation can weaken interaction-dependent ecological function and reduce the local effective population size that maintains genetic variation. Under one independently calibrated symmetric closure, baseline-relative diversity erosion preceded every observed functional-trait loss, but fixed absolute thresholds did not provide a robust rule. Changing recurrent-transition direction then altered whether high-trait sources could be established, whether functional loss occurred too rapidly or too rarely for common calibration, whether warning-loss pairs were observable, and how much time remained before loss. Genetic warning is therefore not an intrinsic property of a diversity statistic. It is an emergent, system-specific property of the eco-genetic processes that generate functional persistence, genetic change, and the opportunity to observe both.

## Relationship to the predecessor

The predecessor and extension remain separate evidence ledgers. The predecessor supplies the theorem-guided interaction mechanism, the fragmentation result, and the conditional symmetric warning benchmark. The extension supplies independent source reconstruction, warning-blind regime mapping, and fresh-seed warning comparison under an altered recurrent-transition closure. Numerical results remain attributed to their originating protocols.

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