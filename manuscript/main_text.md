# Eco-genetic regimes govern when genetic early warning can be validated

## Abstract

Habitat fragmentation can leave populations present while ecological function disappears, but genetic warning is interpretable only when functional loss itself occurs reproducibly. We used a finite eco-genetic model in which interaction feedback supports a functional state and condition selection is blind to warning outcomes. Fragmentation strongly reduced interaction, local effective size and realised high-trait mass. Recurrent state turnover altered source feasibility and loss regime; prospective refinement recovered a narrow reproducible intermediate-risk regime. Allele-frequency connectivity moved that anchor from reproducible to seed-heterogeneous loss, whereas three predeclared levels of aggregate interaction support all retained the reproducible regime despite differing source eligibility. Genetic erosion preceded loss in one calibrated benchmark, but warning behaviour was not fully portable across independently calibrated domains. Genetic early warning is therefore a downstream property of the eco-genetic process generating functional loss.

## Introduction

Ecological function can disappear before the population carrying it disappears. A species may remain numerically present while becoming ineffective as a pollinator, seed disperser, mutualist, defender or other ecological actor (Soulé et al. 2005; McConkey & Drake 2006; Valiente-Banuet et al. 2015). Conservation monitoring therefore has to distinguish population persistence from persistence of ecological function. Abundance, interaction state, allele presence, genetic diversity and realised functional-trait occupancy are related, but they are not interchangeable state variables.

Habitat fragmentation provides a natural setting in which these states can separate. Fragmentation changes local patch size and connectivity, which can alter interaction intensity, local demography, gene flow, drift and eco-evolutionary feedbacks (Legrand et al. 2017; Govaert et al. 2019). If a function depends on positive interaction feedback, spatial fragmentation may first weaken the interaction supporting that function, then reduce local effective population size and realised functional-trait occupancy while the population remains present. The central ecological question is therefore not simply whether habitat is fragmented, but **when spatial fragmentation becomes functional fragmentation**.

Genetic early-warning studies usually begin one step downstream. Classical early-warning work asks whether a statistic changes before a transition (Scheffer et al. 2009; Drake & Griffen 2010), while conservation genetic monitoring asks whether changes in diversity or allele frequencies diagnose deterioration (Schwartz et al. 2007; Stange et al. 2021). Yet warning detectability depends on the process generating the transition, the state variable measured and the observation design (Hastings & Wysham 2010; Boettiger & Hastings 2012, 2013; Gsell et al. 2016). Genetic diversity is likewise biologically important without being a context-free surrogate for ecological function (Hughes et al. 2008; Whitlock 2014).

We therefore treat **warning estimability** as a biological condition that must be established before warning performance is analysed. A functional state must first be possible; fragmentation or deterioration must be capable of disrupting it; and the resulting loss process must be neither nearly absent, nearly deterministic nor irreproducibly heterogeneous among comparable stochastic realisations. If those conditions fail, a lead time is not merely noisy—the warning comparison itself is poorly posed.

The study follows that hierarchy (Figure 1). **First**, can an interaction-supported functional state exist and be disrupted by fragmentation? **Second**, which eco-genetic conditions determine whether functional loss is generated reproducibly? We test recurrent state turnover, effective genetic connectivity and aggregate interaction support. **Third**, only after an evaluable loss regime is established, can genetic erosion precede functional loss? **Fourth**, is that warning behaviour portable across independently calibrated eco-genetic regimes? This condition-first design turns failed generality into a boundary result rather than a reason to tune until a favourable warning appears.

## Model and methods

### Condition-first study architecture

The study uses two computational provenance units. The parent repository supplies the theorem-guided interaction mechanism, paired fragmentation experiment and an inherited symmetric warning benchmark. The extension independently reconstructs high-function sources under recurrent state-transition coordinates, maps functional-loss regimes, prospectively recovers an evaluable loss regime, tests genetic-connectivity and aggregate-interaction-support conditions, and performs a separately declared portability validation. Parent and extension trajectories are never pooled.

All extension analyses using the parent life cycle load scientific commit `dd8ee379d0d3518194c767d16402042525bc00dc`. Condition recovery is warning-blind: genetic diversity, warning times, lead/lag ordering and lead time are unavailable until an event regime has been fixed independently.

### Interaction-supported function and fragmentation

The finite model records interaction state, a high-trait-associated allele, realised trait-bin occupancy, population size and local effective size in a stochastic multipatch life cycle. Potential high-trait viability, realised high-trait occupancy, allele persistence, genetic diversity and population persistence are recorded separately.

The fragmentation experiment began from the same H1-prepared full state and projected it either to one large patch or equal isolated fragments at fixed total area. Twelve primary cells contained 100 attempted seed-replicates each. A later fresh-seed sensitivity projected prepared sources across 1, 2, 3, 4, 6, 8, 12 and 16 equal isolated patches at fixed total area.

### Recurrent state-transition coordinates

Let `p` be the high-trait-associated allele frequency. The extension uses

\[
M(p)=\kappa_\mu p_\mu^*+(1-\kappa_\mu)p,
\]

where `kappa_mu` controls relaxation strength and `p_star` is the transition-only equilibrium/direction. The effective low-to-high and high-to-low transition rates are

\[
u_{L\to H}=\kappa_\mu p_\mu^*,\qquad
u_{H\to L}=\kappa_\mu(1-p_\mu^*).
\]

`p_star` is an effective recurrent-state equilibrium, **not an empirical mutation-rate estimate**. The common grid crossed `kappa_mu = 0.05, 0.20, 0.35` with `p_star = 0.10, 0.25, 0.50, 0.75, 0.90`. Each coordinate received independent high-function source reconstruction.

### Warning-blind functional-loss calibration

Source reconstruction crossed the 15 recurrent-transition coordinates with three area-reference values, three interaction-feedback values, five master seeds and five replicates, for 3,375 attempts. The common deterioration campaign crossed those coordinates with two horizons and three normalized barrier increases. Calibration used realised post-baseline functional-trait loss only.

A candidate was classified **R1 persistence** when every seed-block loss rate was below 0.30; **R2 rapid loss** when every rate was above 0.70; **R3 seed-heterogeneous** when blocks crossed categories or the eligibility band; and **R4 warning-evaluable** when every seed-block rate lay in `[0.30,0.70]`. R4 defines event-regime estimability, not warning success. A coordinate with no eligible candidate was recorded as `no_domain_selected`.

The completed loss data were then used to locate a rapid-to-persistence frontier without inspecting diversity or warning fields. Prospectively declared high-rep runs tested and independently replayed the central frontier and immediate neighbours. The recurrent-turnover search stopped after the replay; no finer `p_star` tuning was permitted merely to widen R4.

### Effective genetic connectivity

At the independently reproduced R4 anchor, allele-frequency mixing was varied while all non-migration conditions were fixed: `A_ref=1.0`, interaction `kappa=4.5`, `kappa_mu=0.35`, `p_star=0.35`, four equal patches at fixed total area, horizon 120 and normalized barrier increase 0.30.

The operator is

\[
p_i'=(1-m)p_i+m\bar p,
\]

where `m` is `migration_rate` and \(\bar p\) is the population-weighted selected mean. This is allele-frequency connectivity and **not demographic migration**, pollinator movement, pollen or seed dispersal, recolonisation or trait-bin dispersal. One hundred independently prepared sources were paired across `m = 0, 0.025, 0.05, 0.10, 0.20` using the same prepared source and trajectory seed at every level.

### Aggregate interaction support

A final warning-blind condition test used only the three interaction-feedback values already declared in the original source grid: `kappa = 3.0, 4.5, 6.0`. The recurrent-turnover anchor, `A_ref`, fragmentation geometry, deterioration schedule and zero allele-frequency mixing were fixed. Five fresh master seeds × 20 attempts were run at each kappa, with source reconstruction repeated independently because feedback strength changes source geometry.

`interaction kappa` is aggregate positive-feedback/effective interaction support. It is not partner richness, connectance, pollinator diversity or network dimensionality. The three levels were classified once; no finer or wider kappa search was allowed merely to manufacture an R4 boundary.

### Conditional genetic-warning benchmark

A separate trait-loss-only calibration fixed one symmetric deterioration domain before warning values were evaluated. Fresh validation seeds were then introduced. Relative warnings were the first post-baseline generations at which `H_alpha` or `H_gamma` declined by 5%, 10% or 20% from their own baselines. Non-events remained right-censored. Predeclared absolute thresholds `H_alpha <= 0.20` and `H_gamma <= 0.20` were audited on the same stored trajectories without rerunning the model.

### Portability validation and uncertainty

A separately declared historical protocol used warning-blind recalibration to recover two evaluable domains. They differ in recurrent-transition parameters, ecological parameters, deterioration strength and horizon, so the fresh-seed comparison is interpreted as portability across calibrated eco-genetic domains, **not a single-factor effect of transition direction**.

Post-review uncertainty analyses resampled whole attempted trajectories, retaining correlated endpoint records within each trajectory. Direct between-domain timing differences were bootstrapped from the two domains rather than inferred from marginal interval overlap. Because lead-time medians condition on observing both events and a leading warning, full-denominator event incidence and warning availability are treated as more primary than conditional lead-time summaries.

### Exact support-diversity boundaries

For heterozygosity \(H(p)=2p(1-p)\),

\[
\frac{\partial H(M(p))}{\partial p_\mu^*}=2\kappa_\mu[1-2M(p)].
\]

The sign changes at `M(p)=0.5`, whereas increasing `p_star` always increases the local high-state support margin `M(p)-p_c`. Under fixed patch weights,

\[
H_\gamma'-H_\alpha'=(1-\kappa_\mu)^2(H_\gamma-H_\alpha).
\]

Thus local high-state support, within-patch diversity and among-patch differentiation need not change in the same direction.

## Results

### Fragmentation disrupted an interaction-supported functional state

Of 1,200 attempted parent replicates, 1,055 satisfied the full-state hold criterion. Every qualified replicate had lower final interaction, local effective size and realised high-trait mass after equal isolation than in its matched one-large projection.

Mean final interaction was 0.998 in one large patch and 0.0048 after equal isolation; the median paired reduction was 99.86%. Mean local effective size fell from 72.83 to 8.18, with a median paired reduction of 88.73%. Mean realised high-trait mass fell from 0.575 to 0.177, with a median paired reduction of 68.87%.

The fresh fragmentation gradient showed that the major change appeared after the first split. Among **1,037** prepared sources, moving from one patch to two isolated patches reduced paired median interaction by 99.83%, local effective size by 77.87% and realised high-trait mass by 71.71%. Interaction and local effective size declined further with additional fragmentation, whereas realised high-trait mass was non-monotonic. Spatial fragmentation therefore created a functional vulnerability before population disappearance (Figure 2A).

### Recurrent state turnover changed source feasibility and functional-loss regime

Across the common 15-coordinate grid, all **3,375** source attempts were completed and **2,269** supported source preparation and projection. Coordinate support ranged from 44.89% at `kappa_mu=0.05, p_star=0.10` to 86.67% at `kappa_mu=0.35, p_star=0.90`.

The common deterioration campaign completed 20,250 attempts in 810 batches. Among 648 complete five-seed candidates, **322** were rapid-loss, **242** persistence and **84** seed-heterogeneous. No candidate satisfied the strict all-seed R4 rule, so all 15 coarse coordinates were historically `no_domain_selected`.

Because warning values were unavailable during this calibration, the result was not warning failure. It showed that the original candidate family did not generate a reproducible intermediate-risk loss process at the sampled coordinates (Figure 3).

### Warning-blind refinement recovered a narrow reproducible event regime

Prospective refinement changed the interpretation of the coarse no-domain result. In the high-rep recovery, `p_star=0.35` produced seed-block loss rates 0.579, 0.529, 0.474, 0.588 and 0.368, with pooled loss 0.505; `p_star=0.40` remained R3-highrep.

An independent replay again classified `p_star=0.35` as R4, with block rates 0.500, 0.667, 0.647, 0.588 and 0.632 and pooled loss 0.609. The lower neighbour `0.325` had pooled loss 0.663 but two blocks above 0.70; the upper neighbour `0.375` had pooled loss 0.391 but one block below 0.30. Both remained R3-highrep.

**R4 exists**, but at the tested resolution it occupies a narrower recurrent-turnover region than pooled loss probability alone suggests. Reproducibility across independent stochastic blocks is therefore an additional biological condition of warning estimability (Figure 4).

### Genetic connectivity changed loss-regime reproducibility without a simple rescue sign

At the reproduced R4 anchor, isolation remained R4-highrep with pooled functional-loss rate **0.571**. Low allele-frequency mixing also retained R4: pooled loss was 0.549 at `m=0.025` and 0.593 at `m=0.05`.

At `m=0.10`, pooled loss was 0.626 but one seed block reached 0.722, producing R3-highrep. At `m=0.20`, pooled loss was 0.604 and one block again reached 0.722, also producing R3-highrep.

Paired prepared sources showed why the classification changed. Relative to isolation, 8 of 91 comparable trajectories switched loss status at `m=0.025`, 12 at `0.05`, 21 at `0.10` and 25 at `0.20`. At every nonzero level, some trajectories changed from loss to no loss and others from no loss to loss. Connectivity therefore changed which stochastic histories lost function and whether loss remained reproducible enough for R4, rather than acting as a universal rescue or collapse axis (Figure 5).

### Aggregate interaction support changed source eligibility but not the R4 classification

The warning-blind interaction-support test produced 100 source attempts at each predeclared kappa. Source preparation, projection and baseline eligibility succeeded for 77/100 attempts at `kappa=3.0`, 94/100 at `4.5` and 87/100 at `6.0`.

Among eligible trajectories, pooled functional-loss rates were 0.468, 0.521 and 0.552, respectively. Crucially, every one of the five seed-block loss rates at every tested kappa remained inside `[0.30,0.70]`. All three levels were therefore R4-highrep.

This is a bounded negative condition result. Across the predeclared `kappa=3.0–6.0` range, aggregate interaction support did not provide the missing R4 boundary at this anchor, although source eligibility differed descriptively. The result separates two stages that can otherwise be conflated: whether a high-function state can be established and retained for analysis, and how reproducibly function is lost once that state is available. The kappa search was closed rather than widened to manufacture a boundary.

### Genetic erosion could precede functional loss, but not by a universal absolute threshold

Only after the loss-regime condition map is established do we turn to warning itself. In the inherited symmetric benchmark, 83 of 100 attempted trajectories were available after source preparation and projection. Thirty-five reached post-baseline realised functional-trait loss; 48 remained right-censored for loss.

For each of six baseline-relative `H_alpha` and `H_gamma` endpoints, all 35 valid same-trajectory pairs had genetic erosion before functional loss, with no ties and no lags. The predeclared absolute thresholds were not robust: `H_alpha <= 0.20` produced 14 leads and six lags among 20 valid pairs, whereas `H_gamma <= 0.20` produced eight leads and eight lags among 16 valid pairs. Genetic warning is therefore possible in a calibrated regime but depends on both biological closure and warning definition (Figure 2B).

### Warning behaviour was not fully portable across independently calibrated domains

The separately declared portability validation attempted 100 fresh trajectories in each calibrated domain. Valid-pair availability across the six endpoints was **0.540** in the recalibrated symmetric domain and **0.335** in the directional calibrated domain. The symmetric domain contained 323 leads, one tie and no lags among 324 valid comparisons; the directional calibrated domain contained 184 leads, five ties and 12 lags among 201 valid comparisons.

Conditional positive lead-time medians were shorter in absolute generations in the directional calibrated domain, but direct between-domain difference intervals excluded zero at only two of six endpoints. After normalization by calibrated horizon, all six direct timing-difference intervals included zero. Because the domains also differ in ecological parameters and deterioration schedules, this is bounded non-portability across calibrated eco-genetic domains, **not an isolated effect of recurrent-transition direction** (Figure 6).

## Discussion

### Spatial fragmentation becomes functional fragmentation through an eco-genetic bottleneck

The parent fragmentation experiment establishes the first part of the causal story: dividing the same prepared state into isolated patches sharply reduced interaction, local effective size and realised high-trait mass before population disappearance. This motivates an **interaction-bottleneck** view of fragmentation. Patch geometry matters because it can reorganise the biological process maintaining function, not merely because it divides habitat area.

The extension shows why the next steps cannot be collapsed into one generic “fragmentation effect.” Recurrent state turnover changed both source feasibility and the loss regime. Genetic connectivity could move the same recurrent-turnover anchor between reproducible and seed-heterogeneous loss. Aggregate interaction support, by contrast, left the R4 classification intact across all three predeclared levels even though source eligibility differed. Source establishment, functional deterioration and warning estimability are therefore related but separable stages.

### Failed generality is a condition result, not unfinished tuning

The original common grid produced rapid-loss, persistence and seed-heterogeneous regimes but no R4. Prospective warning-blind refinement recovered and independently replayed R4 at one central coordinate, showing that the coarse result was a placement boundary rather than structural impossibility. Immediate neighbours remained R3, so pooled intermediate risk was not enough.

The same logic determined when to stop. Stronger allele-frequency mixing provided a genuine R4→R3 boundary at the tested anchor. The predeclared interaction-support levels did not: all remained R4. We therefore report robustness over that tested range rather than expanding kappa until a switch appears. This is the practical meaning of condition-first hypothesis recovery—negative results close an axis when the predeclared question has been answered.

### Connectivity and interaction support act on different parts of the state-to-loss pathway

Connectivity is often framed as beneficial through rescue or harmful through homogenisation. Neither sign was universal here. The exact mixing operator contracts allele-frequency differences, but finite paired trajectories switched functional-loss status in both directions. Stronger tested mixing increased heterogeneity among seed blocks enough to change event-regime classification without a large monotone shift in pooled loss.

The interaction-support result adds a complementary boundary. Across `kappa=3.0–6.0`, the post-source loss regime remained R4, whereas the fraction of attempts that produced an eligible source/baseline state was 0.77, 0.94 and 0.87. Those descriptive differences are not a monotone ecological dose-response, but they show why empirical work should distinguish **whether an interaction-dependent function is maintained at all** from **how that function subsequently fails**.

Actual network simplification remains outside the current model. `interaction kappa` is not partner richness, connectance or pollinator diversity. Partner loss, rewiring, interaction-strength evenness and functional redundancy are empirical mechanisms that may alter effective support and require direct measurement or an explicit network closure.

### Genetic warning is downstream of the loss-generating process

The inherited benchmark shows that baseline-relative genetic erosion can precede functional-trait loss. But that proof of possibility is not a universal rule: absolute thresholds produced both leads and lags, and warning availability and ordering differed across independently calibrated domains.

The condition map explains why. A warning statistic is meaningful only after the system produces a loss event with adequate incidence and reproducibility. A pooled mean risk can hide a mixture of nearly persistent and nearly collapsing stochastic blocks. In such a system, a pooled lead time mixes distinct event-generating processes rather than merely adding measurement noise.

Genetic diversity itself also has no universal monotone relation to functional support. Increasing `p_star` strengthens the local high-associated allele support margin, yet its effect on heterozygosity changes sign at post-transition frequency 0.5. Under fixed weights, `H_gamma-H_alpha` contracts with transition strength independently of direction, and allele-frequency mixing also homogenises patch differences. Low diversity or low differentiation can therefore arise under biological states with different functional implications.

### Urban and island systems offer complementary tests

Urban and island landscapes are useful because they decouple spatial isolation, biological connectivity and interaction structure in different ways. Urban habitat patches may be separated by built surfaces yet linked by pollen movement, corridors, repeated introductions or anthropogenic dispersal; population-genetic responses to urbanisation are correspondingly heterogeneous (Miles et al. 2019), while urban pollination effects are strongly context dependent (Youngsteadt & Keighron 2023). Island systems provide strong gradients in area, geographic isolation, colonisation, mutualist availability and reproductive assurance (Schrader et al. 2021).

The model suggests a shared empirical sequence. Measure spatial support, realised interaction support and partner composition, effective genetic connectivity, reproductive assurance and realised function separately. First ask whether the high-function state is maintained. Then classify functional loss across comparable populations or years. Only within a reproducible intermediate-risk regime should genetic warning be analysed.

Phase F sharpens rather than weakens the interaction-bottleneck hypothesis. It says that moderate changes in the model's aggregate feedback parameter need not change warning estimability once an eligible high-function state exists. Empirically, interaction-network change may therefore reveal itself first through failure to establish or maintain function. Testing partner richness, rewiring, specialisation and redundancy against that source/function boundary is a more direct urban- and island-ecology application than assuming every interaction change must alter warning lead time.

### Limits and interpretation

The model is finite and intentionally explicit. R4 is an operational classification, not a universal numerical risk band. Tested `p_star`, migration and kappa values are not ecological thresholds to transfer to nature. The recurrent-turnover R4 result is narrow at the tested resolution; connectivity and interaction-support tests were performed at one recovered anchor; and the model does not contain an explicit partner network or exogenous pollinator-availability process.

The study also does not establish that warning succeeds throughout R4. The condition-recovery campaigns deliberately withheld warning outcomes. The inherited symmetric benchmark provides proof of possibility, while the historical portability validation shows that warning availability and ordering can change across recalibrated domains. Because those domains differ in multiple parameters, the portability result is **not an isolated effect of recurrent-transition direction**.

Finally, censoring remains part of the finite ecological outcome. Source failure, baseline ineligibility and finite-horizon non-events are not silently removed. This matters because warning availability is itself partly determined by the biology generating observable loss and genetic events.

## Conclusion

The main result is a hierarchy, not a universal warning threshold. Fragmentation can weaken an interaction-supported function before population disappearance. Recurrent state turnover determines whether high-function sources are feasible and where loss regimes fall. Genetic connectivity can change whether loss is reproducible, whereas the predeclared aggregate interaction-support range retained the same R4 event regime while source eligibility varied. Only after those upstream conditions are satisfied does genetic erosion become interpretable as an early signal.

Genetic early warning therefore has **eco-genetic conditions of estimability**. Mapping how spatial fragmentation becomes functional fragmentation—and recovering the conditions under which loss itself is reproducible—provides a more general foundation for warning analysis than beginning with a genetic threshold. It also yields a direct empirical programme for urban and island systems, where spatial isolation, interaction structure, reproductive assurance and genetic connectivity can be measured as distinct pathways to functional loss.

## Data and code availability

The study is distributed across two versioned repositories to preserve computational provenance. The parent repository contains the theorem-guided interaction model, locked fragmentation campaign and inherited symmetric warning benchmark. The extension contains warning-blind condition-recovery campaigns, committed compact summaries, the separately calibrated portability validation, exact theory, figures and manuscript. The parent scientific state is pinned at commit `dd8ee379d0d3518194c767d16402042525bc00dc`. Phase-F evidence is committed at `artifacts/interaction_support/phase_f_summary.json` and traces to workflow run `32441549848`, artifact `9432854668`. Submission bundles contain both software distributions, exact source archives, machine-readable condition and trajectory summaries, protocol documents, artifact identifiers and SHA-256 manifests.

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

Govaert, L., Fronhofer, E.A., Lion, S., et al. (2019). Eco-evolutionary feedbacks—Theoretical models and perspectives. *Functional Ecology*, **33**, 13–30. doi:10.1111/1365-2435.13241

Gsell, A.S., Scharfenberger, U., Özkundakci, D., et al. (2016). Evaluating early-warning indicators of critical transitions in natural aquatic ecosystems. *Proceedings of the National Academy of Sciences USA*, **113**, E8089–E8095. doi:10.1073/pnas.1608242113

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

Valiente-Banuet, A., Aizen, M.A., Alcántara, J.M., et al. (2015). Beyond species loss: the extinction of ecological interactions in a changing world. *Functional Ecology*, **29**, 299–307. doi:10.1111/1365-2435.12356

Whitlock, R. (2014). Relationships between adaptive and neutral genetic diversity and ecological structure and functioning: a meta-analysis. *Journal of Ecology*, **102**, 857–872. doi:10.1111/1365-2745.12240

Youngsteadt, E. & Keighron, M.C. (2023). Urban Pollination Ecology. *Annual Review of Ecology, Evolution, and Systematics*, **54**, 21–42. doi:10.1146/annurev-ecolsys-102221-044616
