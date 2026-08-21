# Eco-genetic regimes govern when genetic early warning can be validated

## Abstract

Habitat fragmentation can leave populations present while ecological function becomes weak or disappears, but genetic warning is interpretable only when the functional-loss process itself is sufficiently reproducible. We used a finite eco-genetic model in which positive interaction feedback supports a high-function state and all condition selection is blind to genetic-warning outcomes. Fragmentation sharply reduced interaction, local effective size and realised high-trait mass before population disappearance. Recurrent state turnover altered source feasibility and functional-loss regime, and prospective warning-blind refinement recovered a narrow reproducible intermediate-risk regime (R4). Allele-frequency connectivity moved that anchor from reproducible to seed-heterogeneous loss, whereas three predeclared levels of aggregate interaction support all retained R4 despite differing source eligibility. A new preregistered reduced-form partner-loss experiment then reproduced R4 in an intact control but moved all three one-partner-loss architectures to seed-heterogeneous R3 while pooled loss incidence remained similar. Thus average risk and event-regime estimability can separate. Only downstream of these conditions did baseline-relative genetic erosion precede functional loss in one calibrated benchmark; fixed absolute thresholds were unreliable and warning behaviour was not fully portable across independently calibrated domains. We conclude that genetic early warning is an emergent property of the eco-genetic process generating functional loss. The model motivates an empirical programme in which urban and island systems are treated not as equivalents, but as contrasting routes through a shared condition space of habitat support, interaction structure, biological connectivity, reproductive assurance and realised function.

## Introduction

Ecological function can disappear before the population carrying it disappears. A species may remain numerically present while becoming ineffective as a pollinator, seed disperser, mutualist, defender or other ecological actor (Soulé et al. 2005; McConkey & Drake 2006; Valiente-Banuet et al. 2015). Conservation monitoring therefore has to distinguish population persistence from persistence of ecological function. Abundance, interaction state, allele presence, genetic diversity and realised functional-trait occupancy are related, but they are not interchangeable state variables.

Habitat fragmentation provides a natural setting in which these states can separate. Fragmentation changes habitat amount, spatial configuration and matrix context, which in turn can alter interaction intensity, demography, dispersal, gene flow, drift and eco-evolutionary feedbacks (Legrand et al. 2017; Govaert et al. 2019). Recent experimental and meta-analytic work reinforces that habitat amount, configuration and matrix quality have separable and interacting effects rather than forming one universal fragmentation gradient (Olhnuud et al. 2025; Fletcher et al. 2026). At the same time, landscape ecology increasingly defines fragmentation functionally from the organism's perspective, especially through connectivity, rather than from vegetation geometry alone (Benitez et al. 2025).

Here we use the more specific term **interaction-mediated functional fragmentation** for a different but complementary object: loss or destabilisation of the biotic interaction support required to maintain a realised ecological function, even while habitat patches or focal populations remain present. This usage is deliberately distinguished from functional connectivity. If a function depends on positive interaction feedback, structural fragmentation may weaken the interaction maintaining that function, reduce local effective population size, and erode realised functional-trait occupancy before demographic disappearance. The central ecological question is therefore not simply whether habitat is fragmented, but **when spatial fragmentation becomes interaction-mediated functional fragmentation**.

That question sits between landscape ecology and ecological-network theory. Interaction networks can reorganise through species turnover, altered interaction strengths and rewiring, and those changes need not be captured by one topological metric (Ward et al. 2026). Pollinator functional diversity can predict pollination function even when pollinator species diversity does not (Hiraiwa & Ushimaru 2024), network architecture can predict temporal persistence (Domínguez-Garcia et al. 2024), and multi-habitat landscapes can support interaction complementarity, robustness and pollination performance not recoverable by simply adding their component webs (Hackett et al. 2024). Conversely, species removal experiments show that rewiring can either compensate for partner loss or alter network complementarity and visitation (Kaiser-Bunbury et al. 2010; Brosi & Briggs 2013; Timóteo et al. 2016; Biella et al. 2017). Fragmentation therefore cannot be equated with a monotone decline in connectance, richness or any single network statistic.

Genetic early-warning studies usually begin one step downstream. Classical early-warning work asks whether a statistic changes before a transition (Scheffer et al. 2009; Drake & Griffen 2010), while conservation genetic monitoring asks whether changes in diversity, differentiation or allele frequencies diagnose deterioration (Schwartz et al. 2007; Stange et al. 2021). A recent network-based population-genetic framework showed that different landscape-fragmentation trajectories can generate qualitatively different genetic trajectories and detectable early-warning signals before rapid **genetic** transitions (Peled et al. 2026). Our target differs: the transition to be warned about is a realised **interaction-dependent functional loss**, not a genetic transition itself. We therefore ask an upstream question that genetic monitoring alone cannot answer: does the eco-genetic system generate a functional-loss process that is reproducible enough for a genetic warning to be estimable at all?

Warning detectability depends on the process generating the transition, the state variable measured and the observation design (Hastings & Wysham 2010; Boettiger & Hastings 2012, 2013; Gsell et al. 2016). Genetic diversity is likewise biologically important without being a context-free surrogate for ecological function (Hughes et al. 2008; Whitlock 2014). Empirically, habitat fragmentation need not produce one consistent change in fine-scale plant genetic structure, with dispersal biology and other factors contributing substantial heterogeneity (Miguel-Peñaloza et al. 2023).

We therefore treat **warning estimability** as a biological condition that must be established before warning performance is analysed. A functional state must first be possible; fragmentation or deterioration must be capable of disrupting it; and the resulting loss process must be neither nearly absent, nearly deterministic nor irreproducibly heterogeneous among comparable stochastic realisations. If those conditions fail, a lead time is not merely noisy—the warning comparison itself is poorly posed.

The study follows that hierarchy (Figure 1). **First**, can an interaction-supported functional state exist and be disrupted by fragmentation? **Second**, which eco-genetic conditions determine whether functional loss is generated reproducibly? We test recurrent state turnover, allele-frequency connectivity, aggregate interaction support and a reduced-form one-partner-loss perturbation. **Third**, only after an evaluable loss regime is established, can genetic erosion precede functional loss? **Fourth**, is that warning behaviour portable across independently calibrated eco-genetic regimes? This condition-first design turns failed generality into a boundary result rather than a reason to tune until a favourable warning appears.

## Model and methods

### Condition-first study architecture

The study uses two computational provenance units. The parent repository supplies the theorem-guided interaction mechanism, paired fragmentation experiment and an inherited symmetric warning benchmark. The extension independently reconstructs high-function sources under recurrent state-transition coordinates, maps functional-loss regimes, prospectively recovers an evaluable loss regime, tests connectivity and interaction conditions, and performs a separately declared portability validation. Parent and extension trajectories are never pooled.

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

A warning-blind condition test used only the three interaction-feedback values already declared in the original source grid: `kappa = 3.0, 4.5, 6.0`. The recurrent-turnover anchor, `A_ref`, fragmentation geometry, deterioration schedule and zero allele-frequency mixing were fixed. Five fresh master seeds × 20 attempts were run at each kappa, with source reconstruction repeated independently because feedback strength changes source geometry.

`interaction kappa` is aggregate positive-feedback/effective interaction support. It is not partner richness, connectance, pollinator diversity or network dimensionality. The three levels were classified once; no finer or wider kappa search was allowed merely to manufacture an R4 boundary.

### Reduced-form partner-loss test

To test an interaction property that scalar `kappa` cannot represent, we prospectively added a reduced-form partner-contribution layer at the same recovered R4 anchor. Every prepared source began with four partners whose normalized contributions summed to one. The intact control retained all four. In each loss condition, exactly one partner was removed at deterioration onset. Lost-partner identity was fixed prospectively by replicate index so that every partner was removed exactly five times in each 20-replicate seed block.

Three one-partner-loss architectures were declared before results were generated: even contributions `(0.25, 0.25, 0.25, 0.25)`, graded contributions `(0.40, 0.30, 0.20, 0.10)` and a dominant-partner architecture `(0.70, 0.10, 0.10, 0.10)`. All three began with the same intact total support and richness, ended with three partners, and had an exactly matched **mean** retained support of 0.75 across each balanced 20-replicate block. They differed in contribution concentration and in trajectory-level retained-support variance. Five fresh master seeds × 20 replicates were paired across the intact control and all three architectures.

This experiment is a reduced-form test of partner loss and contribution redundancy. It does **not** contain explicit partner population dynamics, connectance, nestedness, modularity, coextinction, adaptive rewiring or partner movement. The intact control had to reproduce R4 before partner-loss classifications were interpreted. Genetic-warning variables remained unavailable. A prospective stop rule prohibited changing partner weights, loss identity or thresholds after observing the result.

### Conditional genetic-warning benchmark

A separate trait-loss-only calibration fixed one symmetric deterioration domain before warning values were evaluated. Fresh validation seeds were then introduced. Relative warnings were the first post-baseline generations at which `H_alpha` or `H_gamma` declined by 5%, 10% or 20% from their own baselines. Non-events remained right-censored. Predeclared absolute thresholds `H_alpha <= 0.20` and `H_gamma <= 0.20` were audited on the same stored trajectories without rerunning the model.

### Portability validation and uncertainty

A separately declared historical protocol used warning-blind recalibration to recover two evaluable domains. They differ in recurrent-transition parameters, ecological parameters, deterioration strength and horizon, so the fresh-seed comparison is interpreted as portability across calibrated eco-genetic domains, **not an isolated effect of recurrent-transition direction**.

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

The fresh fragmentation gradient showed that the major change appeared after the first split. Among **1,037** prepared sources, moving from one patch to two isolated patches reduced paired median interaction by 99.83%, local effective size by 77.87% and realised high-trait mass by 71.71%. Interaction and local effective size declined further with additional fragmentation, whereas realised high-trait mass was non-monotonic. Spatial fragmentation therefore created functional vulnerability before population disappearance (Figure 2A).

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

### Aggregate interaction support changed source eligibility but not R4

The warning-blind interaction-support test produced 100 source attempts at each predeclared kappa. Source preparation, projection and baseline eligibility succeeded for **77/100** attempts at `kappa=3.0`, **94/100** at `4.5` and **87/100** at `6.0`.

Among eligible trajectories, pooled functional-loss rates were **0.468**, **0.521** and **0.552**, respectively. Crucially, every one of the five seed-block loss rates at every tested kappa remained inside `[0.30,0.70]`; **all three levels were therefore R4-highrep**.

This is a **bounded negative condition result**. Across the predeclared `kappa=3.0–6.0` range, aggregate interaction support did not provide the missing R4 boundary at this anchor, although source eligibility differed descriptively. The result separates whether a high-function state can be established and retained for analysis from how reproducibly function is lost once that state is available. The kappa search was closed rather than widened to manufacture a boundary.

### One-partner loss changed event-regime reproducibility more than pooled risk

The fresh intact control for the partner-loss experiment reproduced R4, satisfying the prospective opening rule. Ninety of 100 attempted sources were baseline eligible; 49 of 90 lost realised function, giving pooled loss 0.544. Its five seed-block rates were 0.500, 0.471, 0.556, 0.600 and 0.588, a range of 0.129.

All three preregistered one-partner-loss architectures were classified R3-highrep. The even-contribution loss condition produced 51/90 losses (0.567; seed-rate range 0.261), the graded condition 50/90 (0.556; range 0.353), and the dominant-partner condition 52/90 (0.578; range 0.235). Relative to intact, paired loss status switched in both directions in 38/90, 39/90 and 31/90 comparable trajectories, respectively.

Pooled risk barely separated the conditions. A labelled post-hoc paired audit gave Cochran's Q = 0.385, df = 3, `p=0.943`; exact McNemar tests against intact were also non-significant. The predeclared classifier therefore changed from R4 to R3 principally because **between-seed reproducibility changed**, not because average loss incidence rose strongly. The tested contribution-concentration contrast was itself negative at the regime level: even, graded and dominant architectures all yielded R3. Two R3 calls were threshold-near because one seed block reached 0.706, whereas the graded condition reached 0.765; accordingly, the bounded inference is a classifier-level loss of reproducibility at this anchor, not a universal claim that any partner loss destabilises all systems.

Together with the connectivity result, Phase G strengthens the distinction between **event frequency** and **event estimability**. Comparable pooled failure probabilities can arise from different distributions of stochastic histories, and those differences determine whether warning validation is coherently posed.

### Genetic erosion could precede functional loss, but not by a universal absolute threshold

Only after the loss-regime condition map was established did we turn to warning itself. In the inherited symmetric benchmark, 83 of 100 attempted trajectories were available after source preparation and projection. Thirty-five reached post-baseline realised functional-trait loss; 48 remained right-censored for loss.

For each of six baseline-relative `H_alpha` and `H_gamma` endpoints, all 35 valid same-trajectory pairs had genetic erosion before functional loss, with no ties and no lags. The predeclared absolute thresholds were not robust: `H_alpha <= 0.20` produced 14 leads and six lags among 20 valid pairs, whereas `H_gamma <= 0.20` produced eight leads and eight lags among 16 valid pairs. Genetic warning is therefore possible in a calibrated regime but depends on both biological closure and warning definition (Figure 2B).

### Warning behaviour was not fully portable across independently calibrated domains

The separately declared portability validation attempted 100 fresh trajectories in each calibrated domain. Valid-pair availability across the six endpoints was **0.540** in the recalibrated symmetric domain and **0.335** in the directional calibrated domain. The symmetric domain contained 323 leads, one tie and no lags among 324 valid comparisons; the directional calibrated domain contained 184 leads, five ties and 12 lags among 201 valid comparisons.

Conditional positive lead-time medians were shorter in absolute generations in the directional calibrated domain, but direct between-domain difference intervals excluded zero at only two of six endpoints. After normalization by calibrated horizon, all six direct timing-difference intervals included zero. Because the domains also differ in ecological parameters and deterioration schedules, this is bounded non-portability across calibrated eco-genetic domains, **not an isolated effect of recurrent-transition direction** (Figure 6).

## Discussion

### Structural fragmentation and interaction-mediated functional fragmentation are different objects

The parent experiment establishes the first part of the causal story: dividing the same prepared state into isolated patches sharply reduced interaction, local effective size and realised high-trait mass before population disappearance. The important inference is not that every geometrically fragmented landscape must have a simpler ecological network. It is that fragmentation can reorganise the process maintaining function before occupancy itself vanishes.

This distinction matters because fragmentation is multidimensional in nature. Habitat amount, spatial configuration and matrix quality can have different or interacting effects (Olhnuud et al. 2025; Fletcher et al. 2026), and landscape functionality cannot always be inferred from vegetation geometry (Benitez et al. 2025). Biotic interactions introduce another layer: interaction effects on distribution and persistence remain poorly integrated into broad-scale biogeography despite growing network data (Galiana & Araújo 2026). We therefore reserve **interaction-mediated functional fragmentation** for the case in which effective interaction support or its realised function becomes fragmented or unstable. It is a mechanistic extension, not a replacement definition for functional connectivity.

The distinction also gives a concrete empirical prediction. Two landscapes with similar focal-species occupancy, and even similar neutral genetic diversity, can differ in realised function if partner identity, interaction strength or functional complementarity differ. Natural plant–pollinator studies support precisely this separation: pollinator functional diversity can matter more for trait matching and pollination success than species richness alone (Hiraiwa & Ushimaru 2024), and network structure contains information about temporal persistence beyond raw diversity (Domínguez-Garcia et al. 2024).

### Event frequency and event estimability are not the same ecological quantity

The strongest new condition result is the separation between average loss incidence and the reproducibility of the loss-generating process. The recurrent-turnover map first showed that pooled intermediate risk does not guarantee R4: seed blocks can mix persistence-like and rapid-loss behaviour. Connectivity then moved an otherwise fixed R4 anchor to R3 without a monotone rescue or collapse sign.

The reduced-form partner-loss experiment makes the distinction more explicit. The intact control and all three loss architectures had pooled loss near one half, and a post-hoc paired test found no detectable incidence difference. Yet all partner-loss conditions crossed from R4 to R3 under the preregistered block rule because loss became less reproducible across seeds. Thus a perturbation can alter **which stochastic histories fail** without substantially changing the average fraction that fail.

For early-warning work, that difference is fundamental. A risk estimator asks how often loss occurs. A warning estimator asks whether a precursor can be compared with a sufficiently coherent downstream event process. If an apparent 50% pooled risk combines some near-persistent blocks and some near-collapsing blocks, a single pooled lead-time distribution mixes distinct data-generating regimes. More data do not automatically repair that biological non-exchangeability.

The Phase-G result should nevertheless remain bounded. It is not a full ecological network, and the even and dominant R3 calls each crossed the 0.70 boundary only narrowly in one block. What is robustly established is that the **predeclared event-regime classifier** changed after the tested partner-loss perturbation; what is not established is a universal law that partner loss increases collapse risk or that contribution concentration determines robustness.

### Interaction architecture can matter, but rewiring prevents a one-directional prediction

Phase F and Phase G answer different interaction questions. Varying aggregate positive-feedback strength from `kappa=3.0` to `6.0` changed source eligibility but did not change the post-source R4 classification. Removing one reduced-form partner changed the R4 classifier even though the three loss architectures were matched in mean retained support. Aggregate strength and distribution of support among partners therefore cannot be assumed to be interchangeable axes.

Real interaction networks add mechanisms that Phase G deliberately omits. Pollinator removals can alter resource complementarity and which plants are visited even when connectance changes little (Biella et al. 2017). Rewiring can increase robustness in models and some field manipulations (Kaiser-Bunbury et al. 2010; Timóteo et al. 2016), but another experimental plant–hummingbird system showed limited compensatory rewiring after removal of a locally abundant plant (Leimberger et al. 2023). Recent synthesis accordingly treats changes in both topology and interaction strength as central to network resilience rather than assuming automatic compensation (Ward et al. 2026).

The empirical implication is therefore stronger as a measurement rule than as a directional prediction: partner identity, functional diversity, interaction strength, contribution evenness and rewiring should be measured separately from partner richness. Multi-habitat experiments show why this can matter at landscape scale: higher interaction evenness and complementarity can improve pollination function without simply tracking pollinator abundance or richness (Hackett et al. 2024).

### Connectivity is also a process family, not one scalar rescue axis

The present `migration_rate` operator mixes allele frequencies only. Its R4→R3 transition is therefore evidence that genetic-state connectivity can change loss-regime reproducibility, not evidence about demographic recolonisation, pollen flow, seed dispersal or pollinator movement. Those processes can be coupled in real systems but need not have the same sign or timescale.

This boundary is empirically important. A global meta-analysis found no consistent overall change in fine-scale plant genetic structure between fragmented, degraded and undisturbed habitats, with large heterogeneity and a detectable role for seed-dispersal mode (Miguel-Peñaloza et al. 2023). Genetic structure is therefore not a universal readout of habitat fragmentation. Conversely, Peled et al. (2026) showed theoretically and empirically that heterogeneous landscape connectivity can generate complex genetic trajectories and early warning before rapid genetic transitions. Together, these findings support treating spatial structure, biological movement, genetic state and realised function as linked but separate observables.

A direct future model extension would need biologically explicit movement—pollen, seed/propagule, demographic or partner movement—rather than silently relabelling allele-frequency mixing. We therefore leave that as an unresolved mechanism rather than claiming the present Phase E is a full dispersal experiment.

### Genetic warning is downstream of the loss-generating process

The inherited benchmark shows that baseline-relative genetic erosion can precede functional-trait loss. But that proof of possibility is not a universal threshold rule: fixed absolute thresholds produced both leads and lags, and warning availability and ordering differed across independently calibrated domains.

The condition map explains why. Before asking whether a genetic statistic leads a transition, one must establish what transition the system generates, how frequently it occurs and whether comparable stochastic blocks generate it reproducibly. This ordering complements rather than duplicates network-based genetic monitoring. Peled et al. (2026) ask whether genetic metrics warn of rapid genetic transitions under changing landscape connectivity. Here the monitored genetic state is instead a potential precursor to a different endpoint—loss of interaction-supported ecological function—and the main contribution is the upstream recovery of conditions under which that comparison becomes estimable.

Genetic diversity itself also has no universal monotone relation to functional support. Increasing `p_star` strengthens the local high-associated allele support margin, yet its effect on heterozygosity changes sign at post-transition frequency 0.5. Under fixed weights, `H_gamma-H_alpha` contracts with transition strength independently of direction, and allele-frequency mixing homogenises patch differences. Low diversity or low differentiation can therefore arise under biological states with different functional implications.

### Urban and island systems are contrasting routes through a common condition space

The cross-system application is deliberately **not** a `city versus island` comparison. Cities can be island-like in some respects, but they are heterogeneous mosaics connected by infrastructure and human movement rather than oceanic islands in miniature (Alaasam et al. 2026). Urbanisation can filter whether species are present, whether they co-occur and whether they interact (Moreno-García et al. 2025). Thus an urban site may remain spatially or genetically connected while local heat, pollution, resource turnover or management alters partner composition and realised interaction structure.

Oceanic islands offer a different causal decomposition. Global pollination-network comparisons found oceanic-island networks to be smaller and lower in interaction diversity on average than mainland or continental-island networks, while individual island attributes did not control every network metric (Traveset et al. 2016). Global biogeographic work further suggests that mutualist availability can act as an establishment filter in addition to area and isolation (Delavaux et al. 2024), although the magnitude and statistical robustness of that global mutualism-filter result have been debated. Reproductive assurance supplies yet another route: Baker's-law theory predicts an advantage of the capacity for uniparental reproduction under colonisation or mate limitation, not universal autonomous selfing on islands (Pannell et al. 2015).

These literatures make the next question more precise:

> **Do different fragmentation mechanisms converge on the same operational functional-fragmentation regime once state feasibility, realised interaction support, biological connectivity and functional loss are measured separately?**

This is a **prospective convergence hypothesis**, not a result of the present simulations. Convergence would not mean that cities and islands share the same geography, species composition, network topology or genetic differentiation. It would mean that different causal routes produce similar combinations of (i) feasibility of an interaction-supported functional state, (ii) realised functional level, and (iii) incidence and reproducibility of functional loss under comparable observation windows.

The model and literature together imply a common field design. For each population, fragment or population-year, measure: **(1)** habitat amount/configuration and matrix quality; **(2)** partner identity and interaction strength; **(3)** functional diversity, contribution evenness, turnover and rewiring; **(4)** pollen, seed/propagule, demographic and partner movement separately where possible; **(5)** reproductive assurance or alternative functional pathways; **(6)** realised ecological function through time; and **(7)** genetic state through time, distinguishing neutral from functional or adaptive information where feasible. The resulting comparison is a **regime map**, not a habitat-category contrast.

That design gives immediate practical meaning to the present results. In cities, management based only on habitat patches or neutral genetic connectivity could miss local interaction-mediated functional fragmentation. On islands, geographic isolation alone could miss whether function is buffered by generalist mutualists, functional redundancy or reproductive assurance. In both systems, the first monitoring question should be whether function is established and maintained; the second is whether its failure is reproducible; only the third is whether genetic change provides useful lead time.

### Limits and interpretation

The model is finite and intentionally explicit. R4 is an operational classification, not a universal numerical risk band. Tested `p_star`, migration and kappa values are not ecological thresholds to transfer to nature. The recurrent-turnover R4 result is narrow at the tested resolution; connectivity, scalar interaction-support and partner-loss tests were performed at one recovered anchor.

The Phase-G partner layer is reduced-form. It does not simulate partner abundance, explicit bipartite topology, connectance, nestedness, modularity, coextinction or adaptive rewiring. Because the loss architectures were matched in mean retained support but not in trajectory-level retained-support variance, Phase G tests a bounded combination of partner-contribution concentration and loss identity rather than a universal network statistic. The absence of a regime difference among even, graded and dominant architectures is therefore as important as their common R4→R3 classification.

The study also does not establish that warning succeeds throughout R4. Condition-recovery campaigns deliberately withheld warning outcomes. The inherited symmetric benchmark provides proof of possibility, while the historical portability validation shows that warning availability and ordering can change across recalibrated domains. Because those domains differ in multiple parameters, the portability result is not a direction-only causal test.

Finally, censoring remains part of the finite ecological outcome. Source failure, baseline ineligibility and finite-horizon non-events are not silently removed. This matters because warning availability is itself partly determined by the biology generating observable loss and genetic events.

## Conclusion

The main result is a hierarchy, not a universal warning threshold. Fragmentation can weaken interaction-supported function before population disappearance. Recurrent state turnover determines whether high-function sources are feasible and where functional-loss regimes fall. Allele-frequency connectivity can change whether loss remains reproducible. Aggregate interaction-support variation across the predeclared range left R4 intact while source eligibility varied. A matched reduced-form one-partner perturbation then moved the intact R4 control to seed-heterogeneous R3 without a detectable shift in pooled loss incidence, showing that **average functional-loss risk and warning estimability are not the same ecological quantity**.

Only downstream of those event-generating conditions does genetic erosion become interpretable as an early signal. Genetic early warning therefore has **eco-genetic conditions of estimability**. The broader empirical programme is to map how structural fragmentation becomes interaction-mediated functional fragmentation and to recover the conditions under which functional loss itself is reproducible.

Urban and island systems provide complementary tests because they can reach those conditions through different mechanisms. The present study does **not** show that they occupy the same regime. It instead supplies the testable next hypothesis: distinct routes—urban environmental and interaction filtering on one hand, island colonisation, mutualist and reproductive filters on the other—may converge on the same functional-state/loss regime even when their geography, networks and genetic connectivity differ.

## Data and code availability

The study is distributed across two versioned repositories to preserve computational provenance. The parent repository contains the theorem-guided interaction model, locked fragmentation campaign and inherited symmetric warning benchmark. The extension contains warning-blind condition-recovery campaigns, committed compact summaries, the separately calibrated portability validation, exact theory, figures and manuscript. The parent scientific state is pinned at commit `dd8ee379d0d3518194c767d16402042525bc00dc`.

Phase-F evidence is committed at `artifacts/interaction_support/phase_f_summary.json` and traces to workflow run `32441549848`, artifact `9432854668`. Phase-G evidence is committed at `artifacts/partner_redundancy/phase_g_summary.json` and traces to workflow run `32450362310`, artifact `9435520830`, digest `sha256:669cfc468f8a36e53ccc157aaa97e5a4de14f6ad7c09458ed105762e4d0d6ec7`. Submission bundles retain software distributions, exact source archives, machine-readable condition and trajectory summaries, protocol documents, artifact identifiers and SHA-256 manifests.

## References

Alaasam, V., Snead, A., Thonis, A., et al. (2026). Eco-evolutionary dynamics shaping biodiversity in the urban mosaic. *Nature Reviews Biodiversity*, **2**, 170–185. doi:10.1038/s44358-026-00138-0

Benitez, L.M., Parr, C.L., Sankaran, M. & Ryan, C.M. (2025). Fragmentation in patchy ecosystems: a call for a functional approach. *Trends in Ecology & Evolution*, **40**, 27–36. doi:10.1016/j.tree.2024.09.004

Biella, P., Ollerton, J., Barcella, M. & Assini, S. (2017). Experimental species removals impact the architecture of pollination networks. *Biology Letters*, **13**, 20170243.

Boettiger, C. & Hastings, A. (2012). Quantifying limits to detection of early warning for critical transitions. *Journal of the Royal Society Interface*, **9**, 2527–2539. doi:10.1098/rsif.2012.0125

Boettiger, C. & Hastings, A. (2013). No early warning signals for stochastic transitions: insights from large deviation theory. *Proceedings of the Royal Society B*, **280**, 20131372. doi:10.1098/rspb.2013.1372

Brosi, B.J. & Briggs, H.M. (2013). Single pollinator species losses reduce floral fidelity and plant reproductive function. *Proceedings of the National Academy of Sciences USA*.

Delavaux, C.S., Crowther, T.W., Bever, J.D., et al. (2024). Mutualisms weaken the latitudinal diversity gradient among oceanic islands. *Nature*, **627**, 335–339. doi:10.1038/s41586-024-07110-y

Domínguez-Garcia, V., Molina, F.P., Godoy, O. & Bartomeus, I. (2024). Interaction network structure explains species' temporal persistence in empirical plant–pollinator communities. *Nature Ecology & Evolution*, **8**, 423–429. doi:10.1038/s41559-023-02314-3

Drake, J.M. & Griffen, B.D. (2010). Early warning signals of extinction in deteriorating environments. *Nature*, **467**, 456–459. doi:10.1038/nature09389

Fletcher, R.J. Jr., Smith, T.A.H., Jones, M., et al. (2026). Landscape quality drives ecological responses to habitat loss and fragmentation. *Nature Ecology & Evolution*, **10**, 1265–1272. doi:10.1038/s41559-026-03095-1

Galiana, N. & Araújo, M.B. (2026). Biotic interactions biogeography: A framework for understanding how species interactions shape biodiversity patterns across scales. *PLOS Biology*, **24**, e3003813. doi:10.1371/journal.pbio.3003813

Govaert, L., Fronhofer, E.A., Lion, S., et al. (2019). Eco-evolutionary feedbacks—Theoretical models and perspectives. *Functional Ecology*, **33**, 13–30. doi:10.1111/1365-2435.13241

Gsell, A.S., Scharfenberger, U., Özkundakci, D., et al. (2016). Evaluating early-warning indicators of critical transitions in natural aquatic ecosystems. *Proceedings of the National Academy of Sciences USA*, **113**, E8089–E8095. doi:10.1073/pnas.1608242113

Hackett, T.D., Sauve, A.M.C., Maia, K.P., et al. (2024). Multi-habitat landscapes are more diverse and stable with improved function. *Nature*, **633**, 114–119. doi:10.1038/s41586-024-07825-y

Hastings, A. & Wysham, D.B. (2010). Regime shifts in ecological systems can occur with no warning. *Ecology Letters*, **13**, 464–472. doi:10.1111/j.1461-0248.2010.01439.x

Hiraiwa, M.K. & Ushimaru, A. (2024). Loss of functional diversity rather than species diversity of pollinators decreases community-wide trait matching and pollination function. *Functional Ecology*, **38**, 1296–1308. doi:10.1111/1365-2435.14527

Hughes, A.R., Inouye, B.D., Johnson, M.T.J., Underwood, N. & Vellend, M. (2008). Ecological consequences of genetic diversity. *Ecology Letters*, **11**, 609–623. doi:10.1111/j.1461-0248.2008.01179.x

Kaiser-Bunbury, C.N., Muff, S., Memmott, J., Müller, C.B. & Caflisch, A. (2010). The robustness of pollination networks to the loss of species and interactions: a quantitative approach incorporating pollinator behaviour. *Ecology Letters*, **13**, 442–452. doi:10.1111/j.1461-0248.2009.01437.x

Legrand, D., Cote, J., Fronhofer, E.A., et al. (2017). Eco-evolutionary dynamics in fragmented landscapes. *Ecography*, **40**, 9–25. doi:10.1111/ecog.02537

Leimberger, K.G., Hadley, A.S. & Betts, M.G. (2023). Plant-hummingbird pollination networks exhibit limited rewiring after experimental removal of a locally abundant plant species. *Journal of Animal Ecology*, **92**, 1680–1694. doi:10.1111/1365-2656.13935

McConkey, K.R. & Drake, D.R. (2006). Flying foxes cease to function as seed dispersers long before they become rare. *Ecology*, **87**, 271–276. doi:10.1890/05-0386

Miguel-Peñaloza, A., Cultid-Medina, C.A., Pérez-Alquicira, J. & Rico, Y. (2023). Do habitat fragmentation and degradation influence the strength of fine-scale spatial genetic structure in plants? A global meta-analysis. *AoB PLANTS*, **15**, plad019. doi:10.1093/aobpla/plad019

Moreno-García, P., Savage, A., Salgado, A.L., et al. (2025). The effects of urbanization on species interactions. *Nature Cities*, **2**, 693–702. doi:10.1038/s44284-025-00288-w

Olhnuud, A., Wen, J., Yu, J., Lyu, F. & Zhang, Q. (2025). Responses of insect pollinators to habitat fragmentation: A global meta-analysis. *Journal of Applied Ecology*, **62**, 2502–2514. doi:10.1111/1365-2664.70161

Pannell, J.R., Auld, J.R., Brandvain, Y., et al. (2015). The scope of Baker's law. *New Phytologist*, **208**, 656–667. doi:10.1111/nph.13539

Peled, O., Kim, J. & Greenbaum, G. (2026). Network-based genetic monitoring of landscape fragmentation. *Proceedings of the National Academy of Sciences USA*, **123**, e2515033123. doi:10.1073/pnas.2515033123

Scheffer, M., Bascompte, J., Brock, W.A., et al. (2009). Early-warning signals for critical transitions. *Nature*, **461**, 53–59. doi:10.1038/nature08227

Schwartz, M.K., Luikart, G. & Waples, R.S. (2007). Genetic monitoring as a promising tool for conservation and management. *Trends in Ecology & Evolution*, **22**, 25–33.

Soulé, M.E., Estes, J.A., Miller, B. & Honnold, D.L. (2005). Strongly interacting species: conservation policy, management, and ethics. *BioScience*, **55**, 168–176.

Stange, M., Barrett, R.D.H. & Hendry, A.P. (2021). The importance of genomic variation for biodiversity, ecosystems and people. *Nature Reviews Genetics*, **22**, 89–105.

Timóteo, S., Correia, M., Rodríguez-Echeverría, S., Freitas, H. & Heleno, R. (2016). High resilience of seed dispersal webs highlighted by the experimental removal of the dominant disperser. *Current Biology*, **26**, 910–915. doi:10.1016/j.cub.2016.01.046

Traveset, A., Tur, C., Trøjelsgaard, K., Heleno, R., Castro-Urgal, R. & Olesen, J.M. (2016). Global patterns of mainland and insular pollination networks. *Global Ecology and Biogeography*, **25**, 880–890. doi:10.1111/geb.12362

Valiente-Banuet, A., Aizen, M.A., Alcántara, J.M., et al. (2015). Beyond species loss: the extinction of ecological interactions in a changing world. *Functional Ecology*, **29**, 299–307.

Ward, C.A., Tunney, T.D., Hale, K.R.S., et al. (2026). The rewiring of ecological networks in a variable world. *Nature Reviews Biodiversity*, **2**, 355–369. doi:10.1038/s44358-026-00159-9

Whitlock, R. (2014). Relationships between adaptive and neutral genetic diversity and ecological structure and functioning: a meta-analysis. *Journal of Ecology*, **102**, 857–872. doi:10.1111/1365-2745.12240
