# Eco-genetic regimes govern when genetic early warning can be validated

## Abstract

Genetic early warning is usually evaluated by asking whether genetic change precedes ecological loss, but that comparison is meaningful only when loss itself occurs at a reproducible, nondegenerate rate. We used a finite eco-genetic model in which interaction feedback maintains a functional state, fragmentation can disrupt it, and warning domains are selected without access to genetic-warning outcomes. Genetic erosion preceded functional loss in one calibrated benchmark. Across a common recurrent-transition grid, however, source feasibility and loss regime changed enough that no common validation domain was selected. Prospective warning-blind refinement recovered a narrow reproducible intermediate-risk regime, and allele-frequency connectivity moved that same anchor from warning-evaluable to seed-heterogeneous loss without a simple change in mean risk. Genetic early warning therefore has biological conditions of estimability: functional loss must first be generated reproducibly before warning performance can be interpreted.

## Introduction

Ecological function can disappear before the population carrying it disappears. A species may remain numerically present while becoming ineffective as a pollinator, seed disperser, mutualist, defender, or other ecological actor (Soulé et al. 2005; McConkey & Drake 2006; Valiente-Banuet et al. 2015). Conservation monitoring therefore has to distinguish population persistence from the persistence of ecological function. Abundance, interaction state, allele presence, genetic diversity and realised functional-trait occupancy are related, but they are not interchangeable state variables.

Habitat fragmentation provides a natural setting in which those states can separate. Fragmentation changes local patch size and connectivity, which can alter interaction intensity, local demography, gene flow, drift and eco-evolutionary feedbacks (Legrand et al. 2017; Govaert et al. 2019). If a function depends on positive interaction feedback, fragmentation can first weaken the interaction that supports the function, then reduce local effective population size and realised functional-trait occupancy, even while the population persists. Such a sequence creates the possibility of an earlier genetic signal.

This possibility motivates genetic early warning. Classical ecological early-warning studies ask whether a statistic changes before a transition (Scheffer et al. 2009; Drake & Griffen 2010), while conservation genetic monitoring asks whether changes in diversity or allele frequencies diagnose deterioration (Schwartz et al. 2007; Stange et al. 2021). Yet early-warning signals are not expected to be universal across transition mechanisms or observation regimes. Regime shifts can occur without classical warning, and detectability depends on the process generating the transition, the state variable measured and the observation design (Hastings & Wysham 2010; Boettiger & Hastings 2012, 2013; Gsell et al. 2016). Genetic diversity is likewise ecologically important without being a context-free surrogate for ecological function (Hughes et al. 2008; Whitlock 2014).

Most warning analyses nevertheless begin one step downstream: they compare a proposed signal with an observed loss event and ask whether the signal leads. That comparison assumes that the system first generates a suitable loss process. If functional loss is almost certain, almost absent, or highly unstable among otherwise comparable stochastic realizations, lead time is not the only problem; the warning comparison itself may be poorly defined. We therefore treat **warning estimability** as a biological condition to be established before warning performance is analysed.

We organize the study around four questions. **First**, how is an interaction-dependent ecological function maintained, and how can fragmentation destroy it? **Second**, can genetic erosion precede that functional loss in at least one independently calibrated regime? **Third**, under what eco-genetic conditions does the system generate a reproducible, nondegenerate functional-loss regime in which a warning can actually be estimated? **Fourth**, once evaluability is recovered, is warning behaviour portable across eco-genetic regimes, and why should portability be limited? Figure 1 summarizes this hierarchy while keeping functional state, population persistence, genetic state and warning performance distinct.

The first two questions establish the mechanism and proof of possibility. The third is the central extension. We changed recurrent state-transition dynamics while keeping source-reconstruction and deterioration families controlled, then refined the event-regime frontier prospectively without access to diversity or warning outcomes. Finally, we held a recovered warning-evaluable event regime fixed and changed only allele-frequency connectivity among fragmented patches. This design separates the biological generation of a warning-comparison domain from the later performance of the warning statistic itself.

## Model and methods

### Study architecture

The study was developed in two computational phases with separate evidence ledgers. The parent phase supplies the theorem-guided interaction mechanism, the paired fragmentation experiment and an inherited symmetric warning benchmark. The extension phase independently reconstructs high-function sources under recurrent state-transition coordinates, maps realised functional-loss regimes, prospectively recovers warning-evaluable conditions, tests an allele-frequency-connectivity axis, and performs a separately declared portability validation. Parent and extension trajectories are never pooled.

All extension analyses using the parent life cycle load the pinned parent scientific state `dd8ee379d0d3518194c767d16402042525bc00dc`. The condition-recovery analyses are warning-blind: genetic diversity, warning times, lead/lag ordering and lead time are unavailable until a condition is prospectively fixed.

### Interaction-dependent function and fragmentation

The ecological mechanism separates analytical state structure from finite stochastic outcomes. In the declared canonical positive-feedback interaction map, explicit parameter conditions permit distinct low- and high-interaction states. A high-trait viability margin links the interaction branch to potential support for a high-investment trait. These are model-specific analytical results rather than universal claims about positive feedback.

The finite model embeds interaction state, a high-trait-associated allele, realised trait-bin occupancy, population size and local effective size in a stochastic multipatch life cycle. Potential high-trait viability, realised high-trait occupancy, allele persistence, genetic diversity and population persistence are recorded separately.

The fragmentation experiment began from the same H1-prepared full state and projected it either to one large patch or to equal isolated fragments at fixed total area. Twelve primary cells contained 100 attempted seed-replicates each. A later fresh-seed sensitivity projected prepared sources across 1, 2, 3, 4, 6, 8, 12 and 16 equal isolated patches, again at fixed total area.

### Conditional symmetric genetic-warning benchmark

A separate trait-loss-only calibration fixed one symmetric deterioration domain before warning values were evaluated. Fresh validation seeds were then introduced. Relative warnings were the first post-baseline generations at which `H_alpha` or `H_gamma` declined by 5%, 10% or 20% relative to their own baselines. Non-events remained right-censored. Predeclared absolute thresholds `H_alpha <= 0.20` and `H_gamma <= 0.20` were audited on the same stored trajectories without rerunning the model.

### Recurrent state-transition coordinates

Let `p` be the high-trait-associated allele frequency. The extension uses the affine recurrent-transition operator

\[
M(p)=\kappa_\mu p_\mu^*+(1-\kappa_\mu)p,
\]

where `kappa_mu` controls relaxation strength and `p_star` is the transition-only equilibrium/direction. The effective low-to-high and high-to-low transition rates are

\[
u_{L\to H}=\kappa_\mu p_\mu^*,\qquad
u_{H\to L}=\kappa_\mu(1-p_\mu^*).
\]

`p_star` is an effective recurrent-state equilibrium, not an empirical mutation-rate estimate.

The common grid contained `kappa_mu = 0.05, 0.20, 0.35` crossed with `p_star = 0.10, 0.25, 0.50, 0.75, 0.90`. Each coordinate received independent high-function source reconstruction rather than inheriting a source from the symmetric benchmark.

### Common-grid warning-blind loss calibration

Source reconstruction crossed the 15 recurrent-transition coordinates with three area-reference values, three interaction-feedback values, five master seeds and five replicates, for 3,375 attempts. Prepared sources were projected under declared landscape scenarios and retained only when projection invariants passed.

The common deterioration campaign then crossed those coordinates with two horizons and three normalized barrier increases. Calibration used realised post-baseline functional-trait loss only. A candidate was warning-evaluable only if every one of five independent seed blocks had trait-loss frequency in `[0.30,0.70]`. A coordinate with no such candidate was recorded as `no_domain_selected`.

We distinguish four complete-candidate regimes: **R1 persistence**, when every seed-block loss rate is below 0.30; **R2 rapid loss**, when every seed-block rate is above 0.70; **R3 seed-heterogeneous**, when seed blocks cross these categories or the eligibility band; and **R4 warning-evaluable**, when every seed-block rate lies in `[0.30,0.70]`. R4 defines only event-regime estimability, not warning success.

### Prospective recovery of the event-regime frontier

The original common grid selected no R4 domain. We therefore used the completed warning-blind loss data to locate the rapid-to-persistence frontier, without inspecting any diversity or warning field, then prospectively declared new refinement phases.

Phase A refined the weak-transition frontier at `kappa_mu=0.05`. Phase B refined a clean historical rapid-to-persistence bracket at `kappa_mu=0.35`, holding `A_ref=1.0`, interaction `kappa=4.5`, horizon 120 and normalized barrier increase 0.30 fixed while testing interior `p_star` values. Phase C increased replication to 20 replicates per seed with fresh seeds at the two central Phase-B coordinates. Phase D independently replayed `p_star=0.35` and its immediate neighbours `0.325` and `0.375`, again using fresh seeds and 20 replicates per seed.

The recurrent-transition search was stopped after Phase D. No finer `p_star` tuning was permitted merely to widen R4.

### Effective genetic connectivity

Phase E asked whether a recovered R4 condition was stable to genetic connectivity. All non-migration parameters were frozen to the independently reproduced R4 anchor: `A_ref=1.0`, interaction `kappa=4.5`, `kappa_mu=0.35`, `p_star=0.35`, four equal patches at fixed total area, horizon 120 and normalized barrier increase 0.30.

The current simulator implements allele-frequency mixing after local selection as

\[
p_i'=(1-m)p_i+m\bar p,
\]

where `m` is `migration_rate` and \(\bar p\) is the population-weighted selected mean. This is an **allele-frequency connectivity** operator. It is not demographic migration, pollinator movement, seed dispersal, recolonisation or trait-bin dispersal.

One hundred independently prepared sources were paired across `m = 0, 0.025, 0.05, 0.10, 0.20`, using the same prepared source and trajectory seed at every migration level. The resulting 500 trajectories were classified from realised functional loss only. Migration rates were fixed prospectively and were not subsequently refined to preserve or create R4.

### Portability validation and uncertainty

A historical separately declared protocol began after the original common-grid no-domain result. It used warning-blind recalibration to recover two evaluable domains, one symmetric and one directional. Those domains differ in recurrent-transition parameters, ecological parameters, deterioration strength and horizon, so their fresh-seed validation is interpreted as a **portability comparison across calibrated eco-genetic domains**, not a single-factor effect of transition direction.

Post-review uncertainty analyses resampled whole attempted trajectories, retaining the six correlated endpoint records within each trajectory. Direct between-domain timing differences were bootstrapped from the two independent domains rather than inferred from marginal interval overlap. Because lead-time medians condition on observing both events and a leading warning, full-denominator event incidence and warning availability are treated as more primary than conditional lead-time summaries.

### Exact support-diversity boundaries

For heterozygosity \(H(p)=2p(1-p)\),

\[
\frac{\partial H(M(p))}{\partial p_\mu^*}
=2\kappa_\mu[1-2M(p)].
\]

The sign therefore changes at `M(p)=0.5`. At the same time, increasing `p_star` always increases the local high-state support margin `M(p)-p_c`. Thus stronger local high-state support can coincide with lower heterozygosity.

With fixed patch weights,

\[
H_\gamma'-H_\alpha'=(1-\kappa_\mu)^2(H_\gamma-H_\alpha),
\]

so the contraction of among-patch allele-frequency heterogeneity depends on transition strength but not direction. Parent migration theory likewise shows that allele-frequency mixing homogenises patch differences without imposing a universal sign on demographic or functional rescue.

## Results

### Fragmentation disrupted an interaction-supported functional state

Of 1,200 attempted parent replicates, 1,055 satisfied the H1 full-state hold criterion. Every qualified replicate had lower final interaction, local effective size and realised high-trait mass after equal isolation than in its matched one-large projection.

Mean final interaction was 0.998 in one large patch and 0.0048 after equal isolation; the median paired reduction was 99.86%. Mean local effective size fell from 72.83 to 8.18, with a median paired reduction of 88.73%. Mean realised high-trait mass fell from 0.575 to 0.177, with a median paired reduction of 68.87%.

The fresh fragmentation gradient confirmed that the effect appeared after the first split. Among 1,037 prepared sources, moving from one patch to two isolated patches reduced paired median interaction by 99.83%, local effective size by 77.87% and realised high-trait mass by 71.71%. Interaction and local effective size declined further with additional fragmentation, whereas realised high-trait mass was non-monotonic. Fragmentation therefore provides the ecological bridge from interaction-dependent function to demographic and genetic vulnerability without requiring population extinction (Figure 2A).

### Genetic erosion could precede functional loss, but not as a universal absolute threshold

In the inherited symmetric benchmark, 83 of 100 attempted trajectories were available after source preparation and projection. Thirty-five reached post-baseline realised functional-trait loss; 48 remained right-censored for loss.

For each of the six baseline-relative `H_alpha` and `H_gamma` endpoints, all 35 valid same-trajectory pairs had genetic erosion before functional loss, with no ties and no lags. This establishes that genetic erosion can provide advance information in a calibrated regime.

The result did not extend to the predeclared absolute thresholds. `H_alpha <= 0.20` produced 14 leads and six lags among 20 valid pairs; `H_gamma <= 0.20` produced eight leads and eight lags among 16 valid pairs. Warning behaviour therefore depended on the definition of genetic change even within one biological closure (Figure 2B).

### Recurrent state turnover changed both source feasibility and the way function was lost

Across the common 15-coordinate recurrent-transition grid, all 3,375 source attempts were completed and 2,269 supported source preparation and projection. Coordinate support ranged from 44.89% at `kappa_mu=0.05, p_star=0.10` to 86.67% at `kappa_mu=0.35, p_star=0.90`, generally increasing with `p_star` within fixed-`kappa_mu` rows.

The common deterioration campaign completed 20,250 attempts in 810 batches. Among 648 complete five-seed candidates, 322 were rapid-loss, 242 persistence and 84 seed-heterogeneous. No candidate satisfied the strict all-seed R4 rule, so all 15 coarse coordinates were `no_domain_selected`.

This result occurred before warning values were inspected. It therefore did not show warning failure; it showed that the shared candidate family failed to generate a reproducible intermediate-risk functional-loss process at the sampled coordinates (Figure 3).

### Warning-blind refinement recovered a narrow reproducible R4 event regime

The prospective frontier phases changed that interpretation. Phase A produced no R4 cell. In the cleaner Phase-B bracket at `kappa_mu=0.35`, pooled loss declined smoothly from 0.739 to 0.095 as `p_star` increased from 0.30 to 0.45, but all four low-rep interior cells remained seed-heterogeneous. A middle pooled probability was therefore not sufficient to identify a warning-evaluable regime.

With fresh high replication in Phase C, `p_star=0.35` became R4-highrep: seed-block loss rates were 0.579, 0.529, 0.474, 0.588 and 0.368, with pooled loss 0.505. `p_star=0.40` remained R3-highrep.

Phase D independently replayed the central point and its neighbours. `p_star=0.35` again satisfied R4, with seed-block rates 0.500, 0.667, 0.647, 0.588 and 0.632 and pooled loss 0.609. The lower neighbour `0.325` had pooled loss 0.663 but two seed blocks above 0.70; the upper neighbour `0.375` had pooled loss 0.391 but one seed block below 0.30. Both were R3-highrep.

The original 15/15 no-domain result was therefore a coarse-grid/common-family result rather than structural impossibility. R4 exists, but occupies a narrower region than pooled loss probability alone suggests. **Reproducibility across independent stochastic blocks is an additional biological condition of warning estimability** (Figure 4).

### Effective genetic connectivity moved the same R4 anchor into a heterogeneous event regime

Phase E held the independently reproduced R4 anchor fixed and changed only allele-frequency migration. The isolated replay remained R4-highrep with pooled functional-loss rate 0.571. Low migration also retained R4: pooled loss was 0.549 at `m=0.025` and 0.593 at `m=0.05`.

At stronger tested mixing, the event-regime class changed despite only modest change in pooled risk. At `m=0.10`, pooled loss was 0.626 but one seed block reached 0.722, producing R3-highrep. At `m=0.20`, pooled loss was 0.604 and one seed block again reached 0.722, also producing R3-highrep.

Because the same prepared sources and trajectory seeds were paired across migration levels, we could ask which individual trajectories changed loss status. Relative to isolation, 8 of 91 comparable trajectories switched status at `m=0.025`, 12 at `0.05`, 21 at `0.10` and 25 at `0.20`. At every nonzero rate, some trajectories changed from loss to no loss and others from no loss to loss.

Thus genetic connectivity did not behave as a simple rescue or collapse axis. Instead, it changed **which stochastic trajectories lost function** and, at the stronger tested rates, changed whether the event process remained reproducible enough to satisfy R4. Warning estimability is therefore conditional not only on recurrent state turnover but also on effective genetic connectivity (Figure 5).

### Warning behaviour was not fully portable across independently calibrated domains

The separately declared portability protocol recovered two evaluable domains only after warning-blind recalibration. Fresh validation attempted 100 trajectories in each domain.

Valid-pair availability across the six endpoints was 0.540 in the recalibrated symmetric domain and 0.335 in the directional calibrated domain. The symmetric domain contained 323 leads, one tie and no lags among 324 valid comparisons. The directional calibrated domain contained 184 leads, five ties and 12 lags among 201 valid comparisons.

Conditional positive lead-time medians were shorter in absolute generations in the directional calibrated domain, but direct between-domain difference intervals excluded zero at only two of six endpoints. After normalization by each calibrated horizon, all six direct timing-difference intervals included zero. Because the domains also differ in ecological parameters and deterioration schedules, these results support bounded **non-portability across calibrated eco-genetic domains**, not an isolated effect of recurrent-transition direction (Figure 6).

## Discussion

### Genetic early warning has biological conditions of estimability

The central result is not simply that genetic early warning is context dependent. The study identifies an upstream biological requirement that is often treated as implicit: a warning can be estimated only if the system first generates a functional-loss process that is both nondegenerate and reproducible across comparable stochastic realizations.

This distinction became visible in three steps. The original common grid produced rapid-loss, persistence and seed-heterogeneous regimes but no R4 condition. Prospective warning-blind refinement then recovered and independently reproduced a narrow R4 region, showing that the original no-domain result reflected coarse placement rather than impossibility. Finally, genetic connectivity moved the same biological anchor from R4 to R3 while pooled loss probability changed only modestly. The event-regime class therefore contains information that a pooled transition probability alone does not.

This suggests a different workflow for early-warning studies. Rather than beginning with a candidate statistic and searching for a threshold that leads collapse, first map the event-generating regime without using the warning. Ask whether the state of interest can exist, whether deterioration produces the target loss event, and whether loss occurs reproducibly at a rate that allows timing to be estimated. Only after that domain is fixed should warning performance be compared.

### Reproducibility is not the same as intermediate average risk

The Phase-B to Phase-D sequence makes this point directly. Several cells had pooled functional-loss probabilities near the middle of the range but failed R4 because independent seed blocks occupied different event regimes. Conversely, `p_star=0.35` only became interpretable after increased replication showed that all independent blocks lay inside the intermediate-risk band, and that conclusion was reproduced with a second fresh seed family.

The ecological meaning is important. A system can have a population-level average risk that appears ideal for warning analysis while individual populations, years or stochastic histories separate into almost-certain loss and almost-certain persistence. In such a system a pooled lead time is not simply noisy; it mixes distinct event-generating regimes. The same logic applies to empirical monitoring across sites or years.

### Connectivity can change event-regime reproducibility without a simple rescue sign

Connectivity is often framed as beneficial because it can provide demographic or genetic rescue, or as harmful because it can erode local differentiation. The present model supports neither sign as universal. The exact migration layer homogenizes allele-frequency differences, while the finite Phase-E experiment showed bidirectional loss-status switching under the same paired sources. Stronger tested allele-frequency mixing changed the event regime from R4 to R3 without a large monotone change in pooled loss probability.

This is particularly relevant to fragmented landscapes. Two landscapes with similar patch geometry can occupy different eco-genetic regimes if their effective connectivity differs. But the present `migration_rate` represents allele-frequency mixing only. It should not be equated with demographic movement, pollinator flow, seed dispersal or recolonisation. Those processes can be added only with explicit life-cycle mechanisms.

### Genetic diversity is not a monotone meter of ecological function

The exact recurrent-transition identities explain why a universal diversity threshold should not be expected. Increasing `p_star` always strengthens the local high-associated allele support margin, yet its effect on heterozygosity changes sign at post-transition frequency 0.5. In a high-frequency state, stronger support can therefore coincide with lower genetic diversity.

Spatial diversity is also affected differently by transition strength and direction. Under fixed weights, `H_gamma-H_alpha` contracts with `(1-kappa_mu)^2` independently of `p_star`. Migration similarly contracts spatial allele-frequency differences. A low-diversity or low-differentiation state can therefore arise from mechanisms that either weaken or maintain the high-associated state. Genetic diversity remains biologically important, but its warning meaning must be conditioned on the state-generating pathway.

### Urban and island systems provide complementary empirical tests

Urban and island landscapes are useful not because one is an artificial version of the other, but because they decouple apparent spatial fragmentation from effective biological connectivity in different ways.

Urban habitat patches can be separated by built surfaces yet remain connected by pollen movement, green corridors, repeated introductions or anthropogenic dispersal. Urban population-genetic responses are correspondingly heterogeneous rather than uniformly isolation-like (Miles et al. 2019), and urban pollination can decline even while movement among some green spaces remains substantial (Youngsteadt & Keighron 2023). The model predicts that such systems should be classified by realised connectivity and pollination function separately. Two urban networks with similar mean reproductive failure could differ in warning estimability if connectivity changes how consistently loss occurs across patches or years.

Island systems provide stronger long-term gradients of area, geographic isolation, colonization and mutualist availability. Functional island biogeography predicts changes in pollinator availability, generalism and reproductive assurance along those gradients (Schrader et al. 2021). Self-compatibility is over-represented in many island floras, while obligate outcrossing can persist when an effective pollination niche remains available. These systems therefore offer natural tests of the same hierarchy: can the functional state establish, does interaction-dependent function fail, is failure reproducible, and only then does genetic change provide warning?

The most informative empirical design would follow the same lineage across a network of patches or islands and measure patch support, contemporary gene or pollen flow, interaction success, realised reproductive/function endpoints and temporal genetic state together. The primary classification would be the functional-loss regime; genetic warning would be a second-stage analysis restricted to reproducible intermediate-risk systems.

### Limits and interpretation

The model is finite and intentionally explicit. R4 is not proposed as a universal numerical band, and the tested `p_star` or migration values are not ecological thresholds to be transferred to nature. The band is an operational device for separating persistent, rapid, heterogeneous and estimable event regimes in the declared simulation.

The recovered R4 region is narrow along the tested recurrent-transition axis, and the connectivity result is demonstrated at one R4 anchor. The current model also lacks an independent exogenous pollinator- or mutualist-availability control. We therefore stop condition tuning rather than reinterpret an internal feedback parameter as a direct ecological proxy.

Finally, the study does not establish that genetic warning succeeds throughout R4. The inherited symmetric benchmark proves that advance genetic information is possible, while the historical portability comparison shows that availability and ordering can change across recalibrated domains. The new condition-recovery phases deliberately withheld genetic-warning outcomes. Their contribution is more upstream: they identify when a warning comparison is biologically estimable in the first place.

## Conclusion

Fragmentation can disrupt an interaction-supported ecological function, and genetic erosion can precede that functional loss in a calibrated regime. But a warning statistic cannot be interpreted independently of the biological process that generates the loss event. Recurrent state turnover changed whether a high-function source could be established and how function was lost; warning-blind refinement recovered a narrow, reproducible intermediate-risk regime missed by the coarse grid; and effective genetic connectivity moved that same anchor between reproducible and seed-heterogeneous loss regimes.

Genetic early warning therefore has **conditions of estimability**. The relevant question is not only whether a genetic signal is early, but whether the eco-genetic system first generates a functional-loss process for which “early” is a reproducible quantity. Mapping that event-generating domain before evaluating the signal provides a general route for translating genetic early-warning theory to heterogeneous fragmented landscapes, including urban and island systems.

## Data and code availability

The study is distributed across two versioned repositories to preserve computational provenance. The parent repository contains the theorem-guided interaction model, locked fragmentation campaign, inherited symmetric warning benchmark and its evidence ledger. The extension repository contains the recurrent-transition protocols, warning-blind condition-recovery phases, Phase-E connectivity records, Protocol 003 portability validation, exact theory, figures and integrated manuscript. The parent scientific state is pinned at commit `dd8ee379d0d3518194c767d16402042525bc00dc`. Submission bundles contain both software distributions, exact source archives, machine-readable condition and trajectory summaries, protocol documents, artifact identifiers and SHA-256 manifests.

## References

Alberti, M. (2015). Eco-evolutionary dynamics in an urbanizing planet. *Trends in Ecology & Evolution*, **30**, 114–126. doi:10.1016/j.tree.2014.11.007

Andersen, P.K., Geskus, R.B., de Witte, T. & Putter, H. (2012). Competing risks in epidemiology: possibilities and pitfalls. *International Journal of Epidemiology*, **41**, 861–870. doi:10.1093/ije/dyr213

Bell, G. (2017). Evolutionary rescue. *Annual Review of Ecology, Evolution, and Systematics*, **48**, 605–627. doi:10.1146/annurev-ecolsys-110316-023011

Boettiger, C. & Hastings, A. (2012). Quantifying limits to detection of early warning for critical transitions. *Journal of the Royal Society Interface*, **9**, 2527–2539. doi:10.1098/rsif.2012.0125

Boettiger, C. & Hastings, A. (2013). No early warning signals for stochastic transitions: insights from large deviation theory. *Proceedings of the Royal Society B*, **280**, 20131372. doi:10.1098/rspb.2013.1372

Carlson, S.M., Cunningham, C.J. & Westley, P.A.H. (2014). Evolutionary rescue in a changing world. *Trends in Ecology & Evolution*, **29**, 521–530. doi:10.1016/j.tree.2014.06.005

Drake, J.M. & Griffen, B.D. (2010). Early warning signals of extinction in deteriorating environments. *Nature*, **467**, 456–459. doi:10.1038/nature09389

Field, C.A. & Welsh, A.H. (2007). Bootstrapping clustered data. *Journal of the Royal Statistical Society: Series B*, **69**, 369–390. doi:10.1111/j.1467-9868.2007.00593.x

Frankham, R. (2005). Genetics and extinction. *Biological Conservation*, **126**, 131–140. doi:10.1016/j.biocon.2005.05.002

Gomulkiewicz, R. & Holt, R.D. (1995). When does evolution by natural selection prevent extinction? *Evolution*, **49**, 201–207. doi:10.1111/j.1558-5646.1995.tb05971.x

Govaert, L., Fronhofer, E.A., Lion, S., Eizaguirre, C., Bonte, D., Egas, M., Hendry, A.P., De Brito Martins, A., Melián, C.J., Raeymaekers, J.A.M., Ratikainen, I.I., Sæther, B.-E., Schweitzer, J.A. & Matthews, B. (2019). Eco-evolutionary feedbacks—Theoretical models and perspectives. *Functional Ecology*, **33**, 13–30. doi:10.1111/1365-2435.13241

Gsell, A.S., Scharfenberger, U., Özkundakci, D., Walters, A.W., Hansson, L.-A., Janssen, A.B.G., Nõges, P., Reid, P.C., Schindler, D.E., van Donk, E., Dakos, V. & Adrian, R. (2016). Evaluating early-warning indicators of critical transitions in natural aquatic ecosystems. *Proceedings of the National Academy of Sciences USA*, **113**, E8089–E8095. doi:10.1073/pnas.1608242113

Hastings, A. & Wysham, D.B. (2010). Regime shifts in ecological systems can occur with no warning. *Ecology Letters*, **13**, 464–472. doi:10.1111/j.1461-0248.2010.01439.x

Hughes, A.R., Inouye, B.D., Johnson, M.T.J., Underwood, N. & Vellend, M. (2008). Ecological consequences of genetic diversity. *Ecology Letters*, **11**, 609–623. doi:10.1111/j.1461-0248.2008.01179.x

Legrand, D., Cote, J., Fronhofer, E.A., Holt, R.D., Ronce, O., Schtickzelle, N., Travis, J.M.J. & Clobert, J. (2017). Eco-evolutionary dynamics in fragmented landscapes. *Ecography*, **40**, 9–25. doi:10.1111/ecog.02537

Lipsitch, M., Tchetgen Tchetgen, E. & Cohen, T. (2010). Negative controls: a tool for detecting confounding and bias in observational studies. *Epidemiology*, **21**, 383–388. doi:10.1097/EDE.0b013e3181d61eeb

McConkey, K.R. & Drake, D.R. (2006). Flying foxes cease to function as seed dispersers long before they become rare. *Ecology*, **87**, 271–276. doi:10.1890/05-0386

Miles, L.S., Rivkin, L.R., Johnson, M.T.J., Munshi-South, J. & Verrelli, B.C. (2019). Gene flow and genetic drift in urban environments. *Molecular Ecology*, **28**, 4138–4151. doi:10.1111/mec.15221

Rivkin, L.R., Santangelo, J.S., Alberti, M., et al. (2019). A roadmap for urban evolutionary ecology. *Evolutionary Applications*, **12**, 384–398. doi:10.1111/eva.12734

Scheffer, M., Bascompte, J., Brock, W.A., Brovkin, V., Carpenter, S.R., Dakos, V., Held, H., van Nes, E.H., Rietkerk, M. & Sugihara, G. (2009). Early-warning signals for critical transitions. *Nature*, **461**, 53–59. doi:10.1038/nature08227

Schrader, J., Wright, I.J., Kreft, H. & Westoby, M. (2021). A roadmap to plant functional island biogeography. *Biological Reviews*, **96**, 2851–2870. doi:10.1111/brv.12782

Schwartz, M.K., Luikart, G. & Waples, R.S. (2007). Genetic monitoring as a promising tool for conservation and management. *Trends in Ecology & Evolution*, **22**, 25–33. doi:10.1016/j.tree.2006.08.009

Soulé, M.E., Estes, J.A., Miller, B. & Honnold, D.L. (2005). Strongly interacting species: conservation policy, management, and ethics. *BioScience*, **55**, 168–176. doi:10.1641/0006-3568(2005)055[0168:SISCPM]2.0.CO;2

Stange, M., Barrett, R.D.H. & Hendry, A.P. (2021). The importance of genomic variation for biodiversity, ecosystems and people. *Nature Reviews Genetics*, **22**, 89–105. doi:10.1038/s41576-020-00288-7

Stoltzfus, A. & McCandlish, D.M. (2017). Mutational biases influence parallel adaptation. *Molecular Biology and Evolution*, **34**, 2163–2172. doi:10.1093/molbev/msx180

Storz, J.F., Natarajan, C., Signore, A.V., Witt, C.C., McCandlish, D.M. & Stoltzfus, A. (2019). The role of mutation bias in adaptive molecular evolution: insights from convergent changes in protein function. *Philosophical Transactions of the Royal Society B*, **374**, 20180238. doi:10.1098/rstb.2018.0238

Traveset, A. & Navarro, L. (2018). Plant reproductive ecology and evolution in the Mediterranean islands: state of the art. *Plant Biology*, **20** Suppl. 1, 63–77. doi:10.1111/plb.12636

Valiente-Banuet, A., Aizen, M.A., Alcántara, J.M., Arroyo, J., Cocucci, A., Galetti, M., García, M.B., García, D., Gómez, J.M., Jordano, P., Medel, R., Navarro, L., Obeso, J.R., Oviedo, R., Ramírez, N., Rey, P.J., Traveset, A., Verdú, M. & Zamora, R. (2015). Beyond species loss: the extinction of ecological interactions in a changing world. *Functional Ecology*, **29**, 299–307. doi:10.1111/1365-2435.12356

Whitlock, R. (2014). Relationships between adaptive and neutral genetic diversity and ecological structure and functioning: a meta-analysis. *Journal of Ecology*, **102**, 857–872. doi:10.1111/1365-2745.12240

Youngsteadt, E. & Keighron, M.C. (2023). Urban Pollination Ecology. *Annual Review of Ecology, Evolution, and Systematics*, **54**, 21–42. doi:10.1146/annurev-ecolsys-102221-044616
