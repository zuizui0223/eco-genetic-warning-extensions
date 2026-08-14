# Genetic warning emerges from eco-genetic closure in fragmented systems

## Abstract

Ecological function can disappear before population extinction, creating a need for genetic indicators of functional-trait loss. We used a finite eco-genetic model with warning-blind calibration, frozen endpoints and fresh validation seeds. In an inherited symmetric benchmark, relative diversity erosion preceded all 35 observed trait-loss events. Directional recurrent transitions altered source feasibility and loss regimes across a common 15-coordinate grid; strict calibration selected no common validation domain. A separately declared warning-blind protocol expanded the candidate family and used a relaxed event-risk gate before fixing two validation domains. These domains also differed in ecological parameters and deterioration schedules, so their comparison tests warning portability rather than a single transition-direction effect. Valid-pair availability was 0.540 versus 0.335; cluster-bootstrap lead fractions were 0.997 and 0.915. Absolute lead times were shorter in the directional domain, but horizon-normalized lead times were larger. Genetic warning therefore depended on calibration and the eco-genetic system.

## Introduction

Ecological function can be lost before the population carrying it disappears. A species may remain present while becoming ineffective as a pollinator, seed disperser, mutualist, defender, or other ecological actor (Soulé et al. 2005; McConkey & Drake 2006; Valiente-Banuet et al. 2015). Conservation therefore needs to distinguish population persistence from the persistence of ecological function. Abundance, allele presence, genetic diversity, interaction state, and realised trait occupancy are related, but they are not interchangeable monitoring targets.

Habitat fragmentation provides a direct route by which these states can become uncoupled. Fragmentation changes patch size and connectivity, which can alter interaction intensity, local demography, gene flow, drift, and adaptation (Legrand et al. 2017; Govaert et al. 2019). If an ecological function depends on interaction feedback, a smaller or more isolated patch may first weaken the interaction that supports the function. The resulting ecological change can then reduce realised functional-trait occupancy and local effective population size before the population itself disappears.

This sequence suggests a possible early-warning signal. If local effective size and genetic diversity respond before realised functional-trait loss, genetic erosion may provide intervention time. Early-warning research asks whether a statistic changes before collapse (Scheffer et al. 2009; Drake & Griffen 2010), while genetic monitoring uses changes in diversity or allele frequency to diagnose deterioration (Schwartz et al. 2007; Stange et al. 2021). Yet neither approach guarantees that the same genetic threshold will work across biological systems. Early-warning behaviour depends on the process that generates the signal, the event used to define loss, and the observation window (Hastings & Wysham 2010; Boettiger & Hastings 2012, 2013).

The first phase of this study followed that causal sequence. A specified positive-feedback interaction map established an ecological threshold and connected low and high interaction branches to potential high-trait viability. The same prepared high-trait state was then projected into one large patch or equal isolated fragments, linking fragmentation to realised function and local effective size. Finally, warning-blind calibration fixed a symmetric deterioration domain before fresh validation trajectories were examined. Baseline-relative diversity erosion preceded every observed realised trait-loss event, whereas fixed absolute diversity thresholds produced both leads and lags. These results raised a more difficult question: is warning reliability a property of the diversity metric, or of the biological and observational system that generates both warning and loss?

We addressed this question in two stages. First, we varied recurrent-transition parameters across a common 15-coordinate grid while keeping the source-reconstruction and deterioration families fixed. This tests how transition direction reorganises source feasibility and functional-loss regimes. Second, because the strict common calibration selected no validation domain, we used a separately declared warning-blind calibration to recover two event-risk domains for validation. Those final domains differ in recurrent-transition parameters, ecological parameters, and deterioration schedules. Their validation is therefore a test of **warning portability across calibrated eco-genetic domains**, not a single-factor causal test of transition direction. This distinction is central to our interpretation (Figure 1).

## Model and methods

### Study architecture and computational provenance

The study was developed in two computational phases stored in separate repositories so that later extensions could not overwrite the closed evidence ledger of the first phase. The present manuscript treats both phases as one study. The first-phase repository supplies the theorem-guided interaction mechanism, the locked fragmentation experiment, and the inherited symmetric warning benchmark. The extension repository supplies independent source reconstruction under directional recurrent transitions, strict common-family calibration, the separately declared recalibration protocol, fresh-seed validation, and the integrated publication outputs.

Numerical trajectories from the two phases are never pooled. The parent scientific state is pinned at commit `dd8ee379d0d3518194c767d16402042525bc00dc`, and all extension analyses that use parent life-cycle code load that exact state. Workflow identifiers, artifact digests, and claim boundaries are retained in the Supplementary Material and repository evidence ledgers.

### From interaction feedback to realised functional loss

The ecological mechanism separates exact analytical results from finite stochastic outcomes. For the stated canonical sigmoid interaction map, the analytical result identifies the conditions under which one interaction state or three fixed points occur; within the strict bistable interval, the low and high fixed points are locally stable and the middle point is unstable. A declared high-trait viability margin then distinguishes potential viability on the low and high branches. These results apply to the specified map and performance surface rather than to all positive-feedback systems.

The finite model embeds those ecological states in a stochastic trait-allele life cycle. The causal sequence is

`patch size -> interaction intensity -> high-trait-state stability -> local effective size -> genetic diversity -> realised functional-trait loss`.

Potential viability, realised trait occupancy, allele persistence, local effective size, and genetic diversity are tracked separately. This allows a population or allele to remain present even when the realised functional trait has been lost. Full theorem statements, proofs, migration bounds, and the complete finite-model specification are provided in the Supplementary Material.

### Fragmentation and the inherited symmetric benchmark

The first-phase fragmentation experiment compared the same H1-prepared full state after conservation-preserving projection into one-large and equal-isolated landscapes. Twelve predeclared primary cells, each with 100 attempted seed-replicates, were evaluated. Manuscript-facing effect sizes were calculated after the campaign from the already locked paired outcomes: final interaction was the mean of `final_q_by_patch`, local effective size was the mean of `final_effective_size_by_patch`, and realised high-trait mass used the stored metapopulation summary. No simulation was rerun for this descriptive summary.

The inherited symmetric warning benchmark was selected separately by trait-loss-only calibration. Its locked configuration used symmetric allele-state mutation rate `0.10`, `A_ref=0.8`, interaction-feedback `kappa=6.0`, an equal-isolated landscape, a 30-generation ramp followed by a 90-generation hold, and normalized barrier increase `0.15`. Calibration used realised trait loss only; genetic diversity, warning time, ordering, and lead time were unavailable during selection. Fresh validation seeds were introduced only after the configuration was fixed.

Relative warnings were the first post-baseline generations at which `H_alpha` or `H_gamma` declined by 5%, 10%, or 20% from their own baselines. Non-events remained right-censored. The same stored validation trajectories were also evaluated with the predeclared fixed thresholds `H_alpha <= 0.20` and `H_gamma <= 0.20`, without rerunning or reselecting the model.

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

Increasing $p_\mu^*$ therefore lowers the pre-transition frequency required to remain above a high-state boundary. We tested, rather than assumed, whether this local mechanism organised the finite stochastic system. The operator can represent recurrent mutation, gain-loss asymmetry, epimutation, switching, or another effective state transition; $p_\mu^*$ is not an empirical mutation-rate estimate.

### Common-grid source reconstruction and strict warning-blind calibration

We evaluated three relaxation strengths (`0.05`, `0.20`, `0.35`) and five transition equilibria (`0.10`, `0.25`, `0.50`, `0.75`, `0.90`). All other life-cycle components were loaded from the pinned first-phase commit.

Each coordinate received an independent source reconstruction rather than inheriting a qualified source from the symmetric benchmark. The source grid used three area-reference values, three interaction-feedback values, five master seeds, and five replicates. Prepared sources were held for 30 generations and projected into one-large, equal-isolated, and equal-migrating landscapes. Projection support required every declared invariant to pass.

Protocol 002 then evaluated two horizons and three normalized barrier increases with five new calibration seeds and five replicates. A candidate was eligible only if **every** seed block had a post-baseline trait-loss frequency in `[0.30, 0.70]`. Diversity, warning times, lead-lag ordering, and lead time were unavailable during calibration. If no candidate satisfied the rule, the coordinate was recorded as `no_domain_selected`; the Protocol 002 candidate family was not expanded.

### Separately declared warning-blind recalibration

Protocol 002 selected no common validation domain. Protocol 003 therefore began as a separate warning-blind protocol, not as a silent relaxation of Protocol 002. After a trait-loss-only bracket pilot, Amendment 001 declared a broader candidate family and a different event-risk gate **before any warning endpoint was calculated**. Eligibility required (i) pooled trait-loss frequency in `[0.30, 0.70]`, (ii) at least four of five seed-block frequencies in `[0.20, 0.80]`, and (iii) at least three baseline-eligible trajectories in every seed block. The amendment also added a weaker directional schedule `(hold=90, normalized increase=0.10)` before independent calibration.

The first independent calibration did not satisfy that gate. Amendment 002 did not relax it further; instead, it retained the two candidates closest to the pooled target, increased replication to 20 per seed, and introduced a fresh confirmation seed family. Only candidates that passed this unchanged confirmation gate proceeded to validation. Warning values, warning times, and lead-lag outcomes remained unavailable throughout bracket search, calibration, and confirmation.

The two confirmed validation domains were:

- **recalibrated symmetric domain:** `A_ref=0.8`, interaction-feedback `kappa=6.0`, `kappa_mu=0.20`, `p_star=0.50`, 30-generation ramp, 210-generation hold, total horizon 240 generations, normalized barrier increase `0.20`;
- **directional calibrated domain:** `A_ref=1.0`, interaction-feedback `kappa=4.5`, `kappa_mu=0.05`, `p_star=0.90`, 30-generation ramp, 90-generation hold, total horizon 120 generations, normalized barrier increase `0.10`.

Validation used five fresh master seeds and 20 replicates per seed in each domain. Because these domains differ in ecological parameters and deterioration schedules as well as recurrent-transition parameters, Stage III is interpreted only as a portability comparison across independently calibrated domains.

### Secondary timing, censoring and uncertainty audit

A post hoc secondary audit was added after manuscript review identified the identification problem above. The audit uses only the locked Stage III validation records; it does not rerun simulations, alter domains, or change endpoint definitions.

The original Stage III summary calculated the reported “median” as the upper middle order statistic for even sample sizes. The audit instead uses the conventional median, averaging the two middle values when `n` is even. Absolute positive lead times are also divided by the full calibrated deterioration horizon (ramp + hold). A hold-only normalization is retained in the Supplementary Material as a sensitivity description.

The six endpoint records within one trajectory are correlated. We therefore calculated descriptive 95% percentile intervals by resampling whole attempted trajectories, retaining all six endpoint rows within each sampled trajectory. We used 20,000 trajectory-cluster bootstrap replicates with fixed seed `20260814`. The aggregate quantities were lead fraction among valid pairs, lag fraction among valid pairs, and valid-pair availability among all attempted endpoint opportunities. Endpoint-specific positive lead-time medians were bootstrapped in the same way.

Finally, warning and trait loss are not classical competing risks because both can occur in the same trajectory. We therefore report cumulative observed incidence of each event rather than forcing them into a competing-risk estimand. Cumulative curves retain all baseline-eligible completed trajectories through their full administratively censored horizon.

## Results

### Fragmentation produced large, consistent reductions in interaction, local effective size and realised high-trait mass

The first-phase fragmentation result was quantitatively strong. Across 12 primary cells, 1,055 of 1,200 attempted replicates satisfied the H1 full-state hold criterion. Every one of those 1,055 qualified replicates satisfied the predeclared H3 fragmentation pattern: mean final interaction, mean local effective size, and realised high-trait mass were all lower after equal isolation than in the matched one-large projection.

Pooled descriptively across those paired replicates, mean final interaction was `0.9977` in one large patch and `0.0048` after equal isolation; the median paired reduction was 99.86%. Mean local effective size fell from `72.83` to `8.18`, with a median paired reduction of 88.73%. Mean realised high-trait mass fell from `0.575` to `0.177`, with a median paired reduction of 68.87% (Supplementary Table S1). These finite results provide the demographic and functional bridge between the analytical interaction threshold and later genetic-warning analyses.

### Relative genetic erosion preceded functional-trait loss in the inherited symmetric benchmark

The inherited symmetric benchmark provided a strong but conditional warning result. Of 100 attempted sources, 83 produced an available, projection-supported trajectory. Thirty-five of those 83 trajectories reached post-baseline realised trait loss; the remaining 48 available trajectories were right-censored for trait loss.

For each of the six predeclared relative-diversity endpoints, all 35 valid same-trajectory comparisons had warning before realised trait loss. There were no ties and no lags. This result applies only to observed event pairs in the independently selected benchmark configuration; it does not establish a universal warning rule.

Fixed absolute thresholds behaved differently. For `H_alpha <= 0.20`, 20 valid pairs contained 14 leads and six lags. For `H_gamma <= 0.20`, 16 valid pairs contained eight leads and eight lags. Fixed absolute thresholds were therefore not retained as robust warning rules. The contrast shows that warning performance depended on how genetic change was defined even before the recurrent-transition extension.

### Recurrent-transition direction changed whether a high-trait source could be established

Recurrent-transition parameters affected the system before deterioration began. All 3,375 planned source attempts were completed, and 2,269 attempts (67.23%) completed source preparation and supported projection. Every prepared source passed all projection invariants.

Source support ranged from 101 of 225 attempts (44.89%) at `kappa_mu=0.05`, `p_star=0.10` to 195 of 225 attempts (86.67%) at `kappa_mu=0.35`, `p_star=0.90`. Within each fixed-`kappa_mu` row, support generally increased with `p_star`. Because these comparisons occur within the common source-reconstruction grid, they directly show that transition direction reorganised the feasibility of reconstructing the high-trait starting state (Figure 2).

### The common deterioration family separated into rapid-loss, persistence and heterogeneous regimes

The same common grid also changed how realised functional loss occurred. Strict warning-blind calibration completed 20,250 attempts in 810 batches. Among 648 candidates with complete five-seed blocks, 322 had all loss frequencies above the eligibility band, 242 had all rates below it, and 84 crossed the band among seeds (Figure 3).

Low transition equilibria were dominated by rapid loss. At `p_star=0.10`, the closest candidates had a loss frequency of 1.0 in every seed block and at every relaxation strength. High transition equilibria at stronger relaxation were dominated by persistence, including zero loss in every seed block at (`0.20`, `0.90`), (`0.35`, `0.75`), and (`0.35`, `0.90`). Intermediate coordinates were often seed-heterogeneous; at (`0.20`, `0.50`), for example, the pooled frequency was 0.524 while seed-block rates ranged from 0.20 to 0.80.

No complete candidate satisfied the strict all-seed eligibility rule. All 15 coordinates were therefore recorded as `no_domain_selected`. This result means that the common deterioration family did not provide a reproducible intermediate-risk domain for warning validation; it does not mean that genetic warning failed.

### Warning availability and ordering differed across recalibrated domains; the timing contrast was schedule-dependent

Protocol 003 recovered two domains only after its warning-blind amendment and independent confirmation. In confirmation, the recalibrated symmetric domain had pooled trait-loss frequency `0.679` among 84 baseline-eligible trajectories, and the directional calibrated domain had frequency `0.625` among 88. These domains were then frozen before fresh-seed warning validation.

Validation attempted 100 trajectories per domain. Eighty-two recalibrated symmetric trajectories completed source preparation, all 82 were baseline-eligible, and 54 valid warning-loss pairs were available at each endpoint. Ninety-one directional calibrated trajectories completed source preparation, but ten were baseline-ineligible; endpoint-specific valid-pair counts ranged from 28 to 38. Cumulative event-incidence curves retain those censored trajectories and show that warning incidence reached 1.0 for all six endpoints in the recalibrated symmetric domain, whereas directional-domain warning incidence remained endpoint-dependent and often below functional-loss incidence by the end of its shorter horizon (Figure 4).

Across all six endpoints, valid-pair availability among attempted endpoint opportunities was `0.540` (trajectory-cluster bootstrap 95% interval `0.440–0.640`) in the recalibrated symmetric domain and `0.335` (`0.248–0.425`) in the directional calibrated domain. The recalibrated symmetric domain contained 323 leads, one tie and no lags across 324 valid pairs; its lead fraction was `0.997` (`0.990–1.000`). The directional calibrated domain contained 184 leads, five ties and 12 lags across 201 valid pairs; its lead fraction was `0.915` (`0.848–0.971`) and lag fraction was `0.060` (`0.016–0.112`). These intervals resample trajectories rather than treating the six endpoint rows as independent observations (Figure 5).

The absolute timing contrast did not identify a direction effect. Using the conventional median, positive lead times were `106–109` generations across endpoints in the recalibrated symmetric domain and `72.5–77.5` generations in the directional calibrated domain. However, the calibrated horizons were 240 and 120 generations, respectively. After dividing lead time by the full calibrated horizon, median lead fractions were `0.442–0.454` in the recalibrated symmetric domain but `0.604–0.646` in the directional calibrated domain (Figure 6). Thus the directional calibrated domain had a shorter **absolute** warning-to-loss interval but a larger interval relative to its calibrated horizon. The Stage III timing difference therefore cannot be attributed to recurrent-transition direction alone.

## Discussion

Genetic warning is not a context-free property of a diversity statistic; its meaning depends on the event-generating and observation system.

### Methodological discipline is part of the biological result

The strongest result of this study is not a universal claim that one genetic signal predicts functional loss. It is that warning behaviour depended on whether the biological system generated a usable event regime and on how that regime had to be calibrated. The strict common-family design selected no domain at any of 15 transition coordinates. Rather than treating this as a failed analysis, we retained the `no_domain_selected` outcome and opened a separately documented protocol.

That second protocol did change the candidate family and eligibility rule. The important safeguard was not that the search space never changed; it was that every change was declared from **trait-loss-only information before warning values were calculated**, and that later validation used fresh seeds. Amendment 001 added a weaker directional schedule and replaced the Protocol 002 all-seed `[0.30, 0.70]` requirement with a pooled `[0.30, 0.70]` target plus a four-of-five `[0.20, 0.80]` seed-block requirement and baseline-eligibility floor. When the first independent calibration still failed, Amendment 002 kept that rule fixed and increased replication. Writing these steps explicitly makes the calibration history evidence for, rather than a threat to, the warning-blind design.

### Transition direction is identified for source and loss regimes, not for the final timing contrast

The common 15-coordinate grid supports a direct statement about recurrent-transition direction: within fixed relaxation-strength rows, source feasibility generally increased with `p_star`, and the common deterioration family moved from rapid-loss through heterogeneous to persistence regimes across the transition map. Those analyses use shared source-reconstruction and deterioration families.

The final Stage III comparison answers a different question. The two validation domains differ not only in `p_star` and `kappa_mu`, but also in `A_ref`, interaction-feedback `kappa`, barrier increase, and deterioration horizon. The comparison therefore asks whether a relative-diversity warning is portable across two independently calibrated eco-genetic settings. It cannot identify the isolated causal contribution of transition direction to warning ordering or lead time.

The horizon-normalized timing result makes that limitation concrete. Absolute lead times were shorter in the directional calibrated domain, but they occupied a larger fraction of that domain's shorter calibrated horizon. A claim that direction itself “shortened intervention time” would therefore be unsupported. Instead, the result strengthens the broader conclusion: warning time is a property of the whole calibrated system, including the deterioration schedule used to make functional loss observable.

### Warning availability matters as much as conditional ordering

A warning can lead almost whenever both events occur and still be operationally weak if the pair is rarely observable. This is why Figure 5 retains source failures, baseline ineligibility, and every censoring category in the 100-attempt denominator. The directional calibrated domain retained predominantly leading valid pairs, but valid-pair availability was lower and warning censoring was common, especially for stricter `H_gamma` thresholds.

The cumulative event-incidence curves make the same point without discarding non-events. Warning and trait loss are not mutually exclusive competing risks, so we followed both over the complete horizon rather than forcing a competing-risk model. In the recalibrated symmetric domain, relative-warning incidence rapidly approached one while trait loss accumulated later. In the directional calibrated domain, warning incidence often plateaued below one and approached or fell below trait-loss incidence by the end of follow-up. Warning availability is therefore part of the ecological result, not a nuisance denominator.

### Relative genetic erosion is not automatically an informative warning

The inherited symmetric benchmark might otherwise look almost tautological: a relative decline in diversity was followed by a later functional-loss threshold in every observed event pair. Three results argue against interpreting that ordering as an intrinsic property of the diversity statistic. First, fixed absolute diversity thresholds produced substantial lags in the same stored trajectories. Second, strict common-family calibration failed across the entire transition grid because many systems occupied rapid-loss, persistence, or seed-heterogeneous regimes. Third, the independently recalibrated directional domain produced baseline ineligibility, censoring, ties and lags even though the same six relative-warning definitions were used.

These contrasts do not prove that the warning captures a unique causal precursor. They show that its observability and ordering are not guaranteed by the threshold definition alone. The next empirical and model-based test should therefore compare genetic warning with control variables outside the proposed eco-genetic pathway or with deliberately perturbed baseline windows.

### Functional-trait loss is not population extinction

The ecological endpoint was realised loss of a high-trait state, not extinction of the whole population. Species can persist numerically while losing their effectiveness as pollinators, seed dispersers, mutualists, defenders, or other ecological actors (Soulé et al. 2005; McConkey & Drake 2006; Valiente-Banuet et al. 2015). The model therefore separates population persistence, potential trait viability, realised trait occupancy, allele persistence, local effective size, and genetic diversity.

This distinction changes how warning should be interpreted. A population-based monitor may respond after an interaction-dependent function has already been lost. A genetic indicator may respond earlier, but only if the demographic and genetic processes that produce erosion operate on a timescale that precedes realised functional loss. Monitoring should therefore be calibrated against the ecological function at risk rather than against population persistence alone.

### Recurrent transitions affect persistence without implying directed mutation or demographic rescue

The recurrent-transition extension is related to evolutionary rescue but does not test demographic rescue in the conventional sense. Evolutionary-rescue theory asks whether heritable change prevents population extinction during environmental deterioration (Gomulkiewicz & Holt 1995; Carlson et al. 2014; Bell 2017). Our endpoint is functional-trait loss. A high-trait-directed transition can favour functional persistence without demonstrating that the whole population would otherwise have gone extinct.

Likewise, $p_\mu^*$ is not an estimated nucleotide mutation rate and does not imply directed adaptive mutation. It represents the equilibrium direction of effective recurrent transitions between high-trait-associated and low-trait-associated states. Such transitions could represent allelic mutation, biased gain and loss of function, epimutation, developmental switching, or another recurrent process. Mapping this effective parameter to a particular mechanism requires system-specific data.

### Genetic monitoring requires biological calibration

The practical implication is not that one genetic metric should replace another. Relative diversity erosion was highly informative in the inherited symmetric benchmark, but fixed thresholds were unreliable and relative warnings became less available in a separately calibrated domain. A threshold learned in one species, trait architecture, landscape, turnover regime, or deterioration timescale should therefore not be transferred without evidence that the underlying interaction feedback, state turnover, baseline eligibility, and censoring structure are comparable.

Connectivity should be interpreted with the same caution. The first-phase framework established exact bounds for deterministic allele-frequency mixing, but those bounds do not guarantee demographic or functional rescue. More connectivity or more diversity is therefore not automatically the management target. The relevant target is a biological regime in which ecological function persists and any genetic warning appears early enough to support intervention.

### Limits and empirical tests

All numerical results are finite Type S evidence for declared model closures. The trajectory-cluster bootstrap intervals quantify finite-campaign uncertainty; they are not population-level confidence intervals. The Stage III timing and ordering comparison is not a single-factor experiment because the independently calibrated domains differ in ecological and deterioration parameters. The cumulative-incidence analysis is a post hoc descriptive audit of locked validation records. None of these analyses estimates a universal effect size or a biological mutation rate.

Empirical tests would need repeated measurements of at least four distinct layers: spatial configuration and connectivity, the interaction-dependent ecological function, effective population size or genetic diversity, and the recurrent process that generates or removes trait-associated states. A prospective study should predefine the functional-loss threshold, collect temporal genetic data, retain non-events, and compare the proposed genetic warning with negative-control variables or baseline perturbations so that early ordering is not mistaken for a generic consequence of shared deterioration.

## Conclusion

Fragmentation can weaken interaction-dependent ecological function and reduce the local effective population size that maintains genetic variation. In the first phase of this study, relative diversity erosion preceded every observed functional-trait loss in one warning-blind calibrated symmetric benchmark, while fixed absolute thresholds did not provide a robust rule. Across a common directional-transition grid, recurrent-transition parameters then reorganised source feasibility and functional-loss regimes so strongly that the strict calibration selected no common validation domain.

A separately declared warning-blind protocol recovered two validation domains only after changing the candidate family and event-risk gate. Those domains differed in ecological parameters and deterioration schedules as well as recurrent-transition parameters. Their validation showed lower warning availability and nonzero lag in the directional calibrated domain, but the apparent reduction in absolute lead time reversed after normalization by the calibrated horizon. The defensible conclusion is therefore not that transition direction alone weakens or accelerates genetic warning. Genetic warning is an emergent, calibration-dependent property of the eco-genetic system that generates functional persistence, genetic change, censoring, and the opportunity to observe both warning and loss.

## Data and code availability

The study is distributed across two versioned repositories to preserve computational provenance. The mechanistic parent repository contains the theorem-guided interaction model, locked fragmentation campaign, inherited symmetric warning benchmark, and its evidence ledger. The extension repository contains the directional-transition protocols, amendments, validation records, secondary timing audit, publication figures, and integrated manuscript. The parent scientific state is pinned at commit `dd8ee379d0d3518194c767d16402042525bc00dc`. Submission bundles include both software distributions, exact source archives, machine-readable trajectory summaries, protocol documents, artifact identifiers and SHA-256 manifests.

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
