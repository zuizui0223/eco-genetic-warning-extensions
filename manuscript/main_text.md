# Eco-genetic conditions govern when genetic early warning of functional loss can be validated

## Abstract

Habitat fragmentation can leave populations present while interaction-dependent function weakens, but genetic warning is meaningful only if downstream loss is characterised independently. In a finite model, fragmentation reduced interaction, local effective size and realised high-trait mass, while recurrent turnover shifted functional-loss incidence. A historical allele-mixing heterogeneity signal failed fresh replication and did not port to process-resolved movement. Cross-layer spatial alignment changed the exact next interaction transition despite identical coarse marginals, but did not yield a detected long-term loss-incidence difference under one fixed schedule. By contrast, baseline-relative `H_alpha` and `H_gamma` erosion at 5%, 10% and 20% strictly replicated as leading functional loss across two independent seed ensembles within one frozen domain. Absolute thresholds, direction-only identification and cross-domain portability remained limited. Genetic warning is therefore reproducible within a specified eco-genetic loss domain, not a universal property of a genetic statistic.

## Introduction

Ecological function can disappear before the population carrying it disappears. A species may remain numerically present while becoming ineffective as a pollinator, seed disperser, mutualist, defender or other ecological actor (Soulé et al. 2005; McConkey & Drake 2006; Valiente-Banuet et al. 2015). Conservation monitoring therefore has to distinguish population persistence from persistence of ecological function. Abundance, interaction state, allele presence, genetic diversity and realised functional-trait occupancy are related, but they are not interchangeable state variables.

Habitat fragmentation is a natural setting in which these states can separate. Fragmented landscapes couple dispersal, demography and eco-evolutionary feedbacks (Legrand et al. 2017; Govaert et al. 2019), while habitat amount, configuration and matrix quality can have distinct and interacting effects rather than forming one universal fragmentation gradient (Olhnuud et al. 2025; Fletcher et al. 2026). Here we use **interaction-mediated functional fragmentation** for loss or destabilisation of the biotic interaction support required to maintain realised ecological function while focal populations or patches may remain present. This is distinct from organism-centred functional connectivity (Benitez et al. 2025).

The distinction matters because ecological interactions need not respond monotonically to spatial structure. Networks reorganise through species turnover, changing interaction strengths and rewiring (Ward et al. 2026). Pollinator functional diversity can predict pollination function when species richness does not (Hiraiwa & Ushimaru 2024), network architecture can contain information about persistence (Domínguez-Garcia et al. 2024), and multi-habitat landscapes can support interaction complementarity not recoverable by simply adding component webs (Hackett et al. 2024). Removal experiments likewise show compensation in some systems and limited rewiring in others (Brosi & Briggs 2013; Timóteo et al. 2016; Brosi et al. 2017; Leimberger et al. 2023).

Genetic early-warning studies usually begin downstream of these ecological processes. Classical early-warning work asks whether statistics change before transitions (Scheffer et al. 2009; Drake & Griffen 2010), while genetic monitoring asks whether diversity, differentiation or allele-frequency change diagnoses deterioration (Schwartz et al. 2007; Stange et al. 2021). Peled et al. (2026) showed that changing landscape connectivity can generate detectable genetic signals before rapid genetic transitions. Our endpoint is different: realised **interaction-dependent functional-trait loss**. The upstream question is whether the eco-genetic system generates a functional-loss process that can be characterised independently before any precursor is judged.

Warning validation can fail for several reasons that should not be collapsed into one label. The functional state may not be feasible; loss may be too rare or nearly deterministic; finite blocks may cross a calibration threshold by sampling variation; true block probabilities may differ; or a perturbation may change which individual trajectories fail without changing population-level incidence. We therefore distinguish **loss incidence**, **between-block heterogeneity**, **trajectory-identity sensitivity**, **state sufficiency** and **warning performance**.

The study follows a condition-first hierarchy (Figure 1). First, can an interaction-supported functional state exist and be disrupted by fragmentation? Second, how do recurrent turnover, connectivity representation, interaction conditions and cross-layer spatial alignment alter source feasibility and functional loss? Third, after the loss process is fixed warning-blind, can genetic erosion precede functional loss, and does that ordering replicate in fresh stochastic realisations? Fourth, is warning behaviour portable or causally identifiable across eco-genetic domains? Failed generality is retained as a boundary rather than followed by outcome-informed tuning.

## Model and methods

### Condition-first architecture

The study uses two computational provenance units. The parent repository supplies the theorem-guided interaction mechanism, paired fragmentation experiment and inherited symmetric warning benchmark. The extension independently reconstructs high-function sources, maps functional loss and performs robustness, replication, state-sufficiency and portability tests. Parent and extension trajectories are never pooled. All extension analyses using the parent life cycle load scientific commit `dd8ee379d0d3518194c767d16402042525bc00dc`.

Condition recovery is **warning-blind**: genetic-diversity decline, warning times, lead/lag ordering and lead time are unavailable while loss conditions or state representations are selected or replicated. Warning outcomes are inspected only in separately frozen C3 validation/replication campaigns.

### Interaction-supported function and fragmentation

The finite multipatch model records interaction state, a high-trait-associated allele, realised trait-bin occupancy, population size and local effective size. Potential high-trait viability, realised high-trait occupancy, allele persistence, genetic diversity and population persistence remain separate variables.

The fragmentation experiment projected the same H1-prepared full state either to one large patch or to equal isolated fragments at fixed total area. Twelve primary cells contained 100 attempted seed-replicates each. A later fresh-seed sensitivity projected prepared sources across 1, 2, 3, 4, 6, 8, 12 and 16 equal isolated patches.

### Recurrent state transition and historical loss screen

Let `p` be the high-trait-associated allele frequency. The extension applies

\[
M(p)=\kappa_\mu p_\mu^*+(1-\kappa_\mu)p,
\]

with effective low-to-high and high-to-low transition rates

\[
u_{L\to H}=\kappa_\mu p_\mu^*,\qquad
u_{H\to L}=\kappa_\mu(1-p_\mu^*).
\]

`p_star` is an effective recurrent-transition equilibrium, not an empirical mutation-rate estimate. The common grid crossed `kappa_mu = 0.05, 0.20, 0.35` with `p_star = 0.10, 0.25, 0.50, 0.75, 0.90`. Each coordinate received independent high-function source reconstruction.

Source reconstruction comprised 3,375 attempts. The common deterioration campaign completed 20,250 attempts and contained 648 complete five-seed candidates. The preregistered historical classifier called a candidate R1 when all five block loss rates were below 0.30, R2 when all were above 0.70, R4 when all were within `[0.30,0.70]`, and R3 otherwise. Historical R3/R4 labels are retained as protocol facts, not latent biological classes.

A finite-sample audit then quantified sampling-only failure of the all-five-block screen. Load-bearing historical contrasts were replayed at 100 attempted replicates per master seed, with exact first-20 prefix reproduction. Final inference reports pooled loss incidence and a separate Pearson equal-rate diagnostic; paired contrasts also report bidirectional switches and exact McNemar tests.

### Allele-frequency connectivity, fresh replication and process-resolved movement

At the recovered recurrent-turnover anchor, allele-frequency mixing varied while all other conditions were fixed. The operator is

\[
p_i'=(1-m)p_i+m\bar p.
\]

This `migration_rate` is allele-frequency mixing, not demographic migration, pollen or seed dispersal, pollinator movement, recolonisation or trait-bin movement. Phase M precision-expanded the five historical Phase-E master seeds to 100 attempts per block across `m=0,.025,.05,.10,.20`.

Because only the historical `m=.10` condition showed an equal-rate signal, Phase U preregistered one independent replication using fresh seeds `20291010–20291014`, 100 attempts per seed and exactly two paired conditions: `m=0` and `m=.10`. Interpretation required at least 70 baseline-eligible trajectories in every block and identical paired eligibility; neither condition had to pass the historical R4 screen. The fixed decision rule classified `m=.10` as replicated only if its equal-rate `p<.05` while the `m=0` control remained `p>=.05`. No replacement seeds, repeated fresh ensembles or post-result precision increase were allowed.

Phases R and S tested whether the historical Phase-M `m=.10` pattern ported to more explicit movement closures using the historical Phase-M seed family. Whole-individual dispersal (`d=.10`) moved integer post-recruitment individuals and realised trait-bin abundance among patches before recurrent transition and drift. Pollen-only gene flow (`g=.20`) replaced a fraction of paternal gamete contributions with external donors while census and realised trait-bin abundance remained local. These nominal comparisons were preregistered robustness tests, not calibrated operator equivalence.

### Aggregate feedback and partner architecture

The aggregate-support precision replay used the three interaction-feedback values already declared in the source grid: `kappa=3.0,4.5,6.0`, with independent source reconstruction at every kappa.

A reduced-form partner-contribution test represented four contributions summing to one and compared intact, even-loss, graded-loss and dominant-loss architectures. Phase T then tested temporal partner availability while holding expected aggregate support at 0.75. Four partners were independently available each generation with probability 0.75 under even or dominant contribution weights, producing increasing support variance while sharing identical availability draws within each paired trajectory. Adaptive rewiring was preregistered to open only if this matched-expected-support test established a dynamic-network effect.

### Cross-layer state sufficiency

A separate warning-blind alignment audit tested whether layer-wise coarse summaries suffice to define a functional-fragmentation state. Four equal patches had identical census and habitat area in both conditions. The interaction multiset was fixed at `q={.65,.75,.85,.95}`, while allele frequency and realised high-trait mass shared the multiset `{.20,.40,.60,.80}`. Aligned and anti-aligned conditions therefore had identical interaction, allele and trait marginals; identical total trait-bin counts; identical means; and identical `H_alpha`, `H_gamma` and `F_ST`. Only the patchwise alignment between interaction support and the paired genetic/trait-support bundle changed.

The opening certificate evaluated the exact generation-1 interaction update before stochastic interpretation. A preregistered finite campaign then used five unused master seeds (`20300110–20300114`), 100 paired replicates per seed, and a fixed 60-generation interaction-barrier schedule from 0.50 to 0.65. The primary endpoint was post-baseline realised high-trait loss; the paired primary test was exact McNemar at `alpha=.05`. Warning fields were not inspected, and no state values, permutations, horizon, schedule, seeds or precision could be changed after outcomes.

### Conditional warning, fresh replication and portability

A separate trait-loss-only calibration fixed one symmetric deterioration domain before warning values were evaluated. Relative warnings were first post-baseline generations at which `H_alpha` or `H_gamma` declined 5%, 10% or 20% from their own baselines. Non-events remained right-censored. Predeclared absolute thresholds `H_alpha <= 0.20` and `H_gamma <= 0.20` were audited on the same stored trajectories.

The independent parent validation supplied the historical relative-warning benchmark. A later preregistered fresh replication reused the **same frozen symmetric H2-R domain** without recalibration: mutation `0.10`, `A_ref=.8`, interaction `kappa=6`, ramp 30 + hold 90, total normalised barrier increase `.15`, standard finite-bin profile, five unused master seeds `20291110–20291114`, and 20 attempts per seed. The six endpoint definitions (`H_alpha/H_gamma × 5/10/20%` relative decline) were unchanged. Strict replication required at least 20 valid same-trajectory pairs at every endpoint and every valid pair to be a lead with zero ties and zero lags. No endpoint search, seed replacement, recalibration or precision escalation was allowed.

Protocol 003 separately recalibrated two evaluable domains. They differ in recurrent-transition, ecological and deterioration parameters, so their fresh-seed contrast is bounded portability evidence and not a single-factor effect of transition direction. A subsequent warning-blind identifiability audit held the frozen symmetric ecology/schedule and `kappa_mu=.20` fixed while examining the predeclared `p_star=.10,.25,.50,.75,.90` grid. It asked whether any directional coordinate retained an intermediate loss process suitable for a direction-only warning comparison; no new simulation or warning outcome was used. Secondary uncertainty analyses resample whole attempted trajectories rather than endpoint rows (Field & Welsh 2007).

## Results

### Fragmentation disrupted an interaction-supported functional state

Of 1,200 attempted parent replicates, 1,055 satisfied the full-state hold criterion. Every qualified replicate had lower final interaction, local effective size and realised high-trait mass after equal isolation than in its matched one-large projection. Mean final interaction was 0.998 versus 0.0048; mean local effective size was 72.83 versus 8.18; mean realised high-trait mass was 0.575 versus 0.177.

The fresh fixed-area gradient retained 1,037 prepared sources. The first split from one patch to two isolated patches reduced paired median interaction by 99.83%, local effective size by 77.87% and realised high-trait mass by 71.71%. Interaction and local effective size fell further with additional splitting, while realised high-trait mass was not universally monotone (Figure 2).

### Recurrent turnover changed source feasibility and loss incidence

Across the 15-coordinate grid, 2,269 of 3,375 source attempts supported preparation and projection. The common deterioration campaign contained 648 complete five-seed candidates: 322 historical rapid-loss, 242 persistence and 84 historical R3/mixed-block candidates. No candidate satisfied the original strict R4 screen, so all 15 coarse coordinates remain historically `no_domain_selected` **within the original candidate family** (Figure 3).

The precision audit showed that this coarse candidate-family result was a placement boundary rather than structural impossibility and that low-replicate R3/R4 labels could not themselves establish block heterogeneity. Across ten previously load-bearing R3 cases, none showed detectable excess equal-rate heterogeneity at the historical block sizes.

Exact Phase-C/D seed families then recovered a high-to-low incidence frontier. Pooled loss was 0.682 at `p_star=.325`, 0.546/0.538 at `.350` in two historical seed families, 0.407 at `.375` and 0.273 at `.400`. Equal-rate diagnostics were non-significant at all four tested coordinates. The former “narrow R4 bounded by seed-heterogeneous neighbours” interpretation is therefore withdrawn (Figure 4).

### The historical `m=.10` connectivity heterogeneity did not replicate in fresh seeds

In the historical Phase-M seed family, pooled loss remained near 0.54–0.56 across `m=0,.025,.05,.10,.20`. Only `m=.10` showed excess equal-rate heterogeneity (`p=0.0205`); `m=.20` returned to homogeneous behaviour. Paired McNemar tests versus isolation were non-significant at every nonzero level.

The preregistered Phase-U fresh ensemble changed the interpretation of that result. Every fresh block met the precision requirement and eligibility was exactly paired. Pooled loss was 0.540 at `m=0` and 0.551 at `m=.10`. Both fresh conditions were compatible with common block rates: `p=0.134` for `m=0` and `p=0.745` for `m=.10`. Across 452 comparable trajectories, 49 switched loss→no-loss and 54 no-loss→loss; exact McNemar `p=0.694`.

The preregistered decision was **`historical_m010_heterogeneity_not_freshly_replicated`**. The Phase-M `p=0.0205` result remains a valid observation in its original seed family, but it is not supported as an independently reproducible `m=.10` heterogeneity effect (Figure 5).

### Process-resolved movement also did not establish a portable connectivity effect

Using the historical Phase-M seed family, whole-individual dispersal at `d=.10` produced pooled loss 0.606 with equal-rate `p=.811`; its paired McNemar contrast versus no connectivity was `p=.143`. Pollen-only paternal gene flow at `g=.20` produced pooled loss 0.532 with equal-rate `p=.728`; paired McNemar tests were `p=.311` versus no connectivity and `p=.266` versus legacy `m=.10`.

Thus the historical Phase-M heterogeneity observation was not only absent under two process-resolved operators in the matched historical seed family, but also absent when the allele-only `m=.10` operator itself was repeated in one independent fresh ensemble. No robust, portable connectivity heterogeneity effect was established across the tested ensembles and closures.

### Aggregate feedback and partner dynamics were bounded negative results

At `kappa=3.0,4.5,6.0`, pooled loss was 0.499, 0.573 and 0.598; all three conditions remained inside the historical intermediate-incidence screen and equal-rate diagnostics were non-significant (`p=.063,.623,.543`).

For reduced-form partner loss, pooled loss was 0.556, 0.544, 0.565 and 0.549 for intact, even, graded and dominant conditions. Equal-rate and paired marginal-risk tests were non-significant despite many trajectory-status switches.

Phase T increased realised temporal support variance from 0 to 0.04684 to 0.09702 while expected support remained approximately 0.75. Pooled loss was 0.5442, 0.5488 and 0.5533; equal-rate `p=.488,.299,.208`, and paired McNemar `p=.896,.762,.883`. Because no matched-support dynamic-network effect was detected, the preregistered adaptive-rewiring gate remained closed.

### Cross-layer alignment changed the exact transition but not detected long-term loss incidence

Aligned and anti-aligned states had mathematically identical declared coarse signatures, including census, interaction/allele/high-trait marginals, total trait-bin counts, `H_alpha=.4`, `H_gamma=.5` and `F_ST=.2`. Their cross-layer covariance had opposite signs (`+.025` versus `-.025`). The exact generation-1 interaction vectors nevertheless differed, with a maximum patchwise difference of **0.2543**. Layer-wise coarse marginals were therefore not transition-sufficient for the declared local dynamics.

Across the preregistered finite campaign, realised functional loss occurred in 339/500 aligned trajectories (`.678`) and 361/500 anti-aligned trajectories (`.722`). Paired outcomes comprised 92 aligned-loss/anti-no-loss switches, 114 aligned-no-loss/anti-loss switches, 247 shared losses and 47 shared non-losses; exact McNemar `p=.143`. Restricted loss timing was likewise nearly balanced (215 aligned earlier, 221 anti-aligned earlier, 64 ties). Thus cross-layer alignment is required to represent the exact next transition, but the one declared 60-generation deterioration schedule did **not** establish a directional long-term loss-incidence effect.

### Baseline-relative genetic warning strictly replicated within the frozen domain

Only after warning-blind loss calibration did we inspect genetic warning. In the inherited symmetric benchmark, 83 of 100 attempted trajectories were available and 35 reached realised functional-trait loss. For each of six baseline-relative `H_alpha/H_gamma × 5/10/20%` endpoints, all **35/35** valid same-trajectory pairs had genetic erosion before functional loss. Fixed absolute thresholds were not robust: `H_alpha <= 0.20` produced 14 leads and six lags among 20 valid pairs, while `H_gamma <= 0.20` produced eight leads and eight lags among 16 (Figure 2).

The preregistered fresh replication used 100 new attempts in the same frozen symmetric domain. Eighty-two trajectories were available and 33 realised functional losses were observed. Every one of the six relative endpoints had **33 valid pairs, 33 leads, 0 ties and 0 lags**; the exact one-sided binomial `p` against lead probability .5 was `1.1641532182693481e-10` at every endpoint. The five seed blocks contributed `7,7,7,7,5` valid pairs and every valid pair was a lead. The preregistered decision was **`strict_replication`**.

Thus baseline-relative warning ordering is supported across two independent stochastic ensembles within the frozen symmetric H2-R domain: historical 35/35 and fresh 33/33 leads at all six endpoints. This strengthens within-domain reproducibility without converting the failed absolute thresholds into universal rules.

### Warning portability remained bounded and direction-only identification stayed closed

Protocol 003 attempted 100 fresh trajectories in each separately calibrated domain. Valid-pair availability across the six endpoints was 0.540 in the recalibrated symmetric domain and 0.335 in the directional calibrated domain. The two domains contained 323/1/0 versus 184/5/12 lead/tie/lag comparisons. **All six horizon-normalised direct bootstrap contrasts included zero.** The domains also differ in ecological parameters and deterioration schedules, so this remains bounded non-portability across calibrated eco-genetic domains, not a single-factor effect of transition direction (Figure 6).

The matched direction audit explains why a direction-only warning comparison was not opened. At fixed `kappa_mu=.20` and the exact frozen ecology/schedule, pooled functional loss across `p_star=.10,.25,.50,.75,.90` was `1.0, 1.0, .4, 0, 0`. Only the symmetric `.50` cell lay in the historical intermediate-loss band. A cross-strength `.90` cell recovered intermediate loss (`10/21=.476`) only by changing `kappa_mu` to `.05`, which destroys direction-only identification. Finer `p_star` refinement after observing this split would be outcome-guided. The decision was **`direction_only_warning_comparison_not_identifiable_under_frozen_common_schedule`**.

## Discussion

### Functional fragmentation can precede demographic disappearance

Dividing the same prepared state into isolated patches sharply reduced interaction, local effective size and realised high-trait mass before population disappearance. This does not imply that every geometrically fragmented landscape has a simpler network. It shows that spatial reorganisation can disrupt the process maintaining function before occupancy itself vanishes. That narrower mechanism is consistent with evidence that habitat amount, configuration, matrix quality and network turnover can have distinct effects (Olhnuud et al. 2025; Fletcher et al. 2026; Gama et al. 2025).

### Calibration labels are not biological estimands

The precision programme separates event incidence, block heterogeneity, trajectory identity, state sufficiency and warning performance. The historical R1–R4 classifier remains useful as a prospective warning-blind calibration screen, but a threshold crossing in a small finite block is not evidence of biological heterogeneity by itself.

The recurrent-turnover frontier illustrates the point. `.325` and `.400` both lie outside the historical R4 screen for opposite incidence reasons, yet neither shows excess block heterogeneity at high precision. Conversely, the historical Phase-M `m=.10` family did show an equal-rate signal, but the fresh Phase-U ensemble did not. A statistically detectable pattern in one finite seed family therefore cannot be silently promoted to a portable parameter-specific mechanism.

### Connectivity is process-specific and the historical heterogeneity was seed-family contingent

The combined connectivity programme now gives a clearer negative boundary than the Phase-M result alone. In the historical Phase-M family, `m=.10` was the only migration level with detected block heterogeneity, but pooled loss was nearly unchanged and paired marginal-risk tests were null. In the independent Phase-U ensemble, the same `m=.10` operator was homogeneous. Whole-individual and pollen-only closures were also homogeneous in the historical Phase-M family.

The defensible conclusion is therefore not that `m=.10` is a reproducible heterogeneity threshold. It is that one historical allele-mixing seed family produced an excess-block pattern that was **both seed-family contingent and representation-specific** within the tested programme. Natural pollen flow, seed dispersal, demographic movement, recolonisation and partner movement act on different state variables and timescales; empirical plant genetics likewise shows heterogeneous fragmentation responses (Miguel-Peñaloza et al. 2023). Monitoring designs should therefore measure the relevant movement process instead of treating a scalar allele-frequency mixer as biological connectivity in general.

### Interaction architecture remains bounded by negative tests

The aggregate-feedback, reduced-form partner-loss and matched-support temporal-partner campaigns all returned bounded negative population-level results. These nulls do not show that ecological networks are dynamically irrelevant. Rather, the tested scalar feedback range, one-partner reductions and temporal support variance/concentration were insufficient to create a robust change in functional-loss incidence or between-block heterogeneity under their declared closures.

Real networks add partner abundance dynamics, topology, coextinction, trait constraints, spatial movement and adaptive rewiring. Experimental and synthetic studies show that compensation is context dependent (Brosi & Briggs 2013; Timóteo et al. 2016; Brosi et al. 2017; Leimberger et al. 2023; Ward et al. 2026). Because Phase T did not establish a dynamic-network effect to decompose, rewiring remains closed rather than being tuned to rescue a preferred result.

### Genetic warning is reproducible within a fixed domain, but remains downstream

The strongest positive warning result is now strict fresh replication inside the frozen symmetric H2-R domain. The historical ensemble yielded 35/35 leads at all six baseline-relative endpoints; the independently preregistered fresh ensemble yielded 33/33 leads at all six, with zero ties or lags. The ordering is therefore robust to a second stochastic seed ensemble **within that calibrated closure**.

That strength should not be confused with universality. Fixed absolute thresholds produced leads and lags, cross-domain warning behaviour remained bounded, and no matched direction-only loss process existed at fixed transition strength. Changing recurrent-transition direction changed the downstream event process before warning was evaluated. The condition-first ordering is therefore not a rhetorical caveat: it is what makes the strong within-domain warning result interpretable.

### Different fragmentation routes can converge only through a common measured state

The state-sufficiency programme sharpens this ecological translation. Under the declared Markov closure, complete equality of the present full state is future-sufficient. But both the constructive state audit and the 500-pair alignment campaign show that layer-wise marginals are too coarse: opposite patchwise alignment changes the exact next interaction transition even when census, interaction and allele marginals, `H_alpha`, `H_gamma`, `F_ST` and realised trait state match. The finite alignment campaign did not detect a directional 60-generation loss-incidence effect, so alignment is presently a **state-representation requirement**, not an established universal long-term risk axis.

Natural systems already expose the other required coordinates. In Montpellier, low-density urban populations of *Crepis sancta* receive fewer pollinator visits and set fewer seeds, while parentage studies in the same urban programme detect contemporary pollen/seed movement and immigration among patches (Cheptou & Avendaño 2006; Dornier & Cheptou 2013). On Miyake-jima, volcanic damage reduced *Camellia japonica* floral resources, yet wider-ranging *Zosterops japonicus* increased pollen immigration and donor diversity and compensated pollination; seed genetic diversity increased with damage (Abe et al. 2013). Across 40 Honshu–Izu coastal networks, pollinator functional diversity altered trait matching and pollination success more directly than pollinator species diversity (Hiraiwa & Ushimaru 2024). In Zurich gardens, released model outputs further show that urban-intensity effects and pollinator-guild associations differ among focal reproductive functions.

These systems represent contrasting routes—uncompensated interaction limitation, movement-mediated compensation, functional-diversity limitation and focal-function-specific filtering—not habitat categories to pool. A common functional-fragmentation regime is supported only if system origin or fragmentation history no longer improves prediction of subsequent realised function after conditioning on demographic support, realised interactions, trait/functional state, process-specific connectivity, mating/genetic state, alternative functional routes, baseline function, plausible memory and their spatial alignment. Residual history would indicate a missing process or ecological memory variable.

### Limits

The model is finite and its numerical coordinates are not transferable ecological thresholds. Failure to detect block heterogeneity is not a theorem of universal homogeneity. Phase U is one preregistered independent connectivity replication, so non-replication limits the Phase-M claim but does not prove that no seed ensemble could ever show heterogeneity at `m=.10`. The cross-layer alignment campaign likewise establishes a transition-representation boundary but not a universal directional effect on long-term loss incidence.

The process-resolved movement closures are partial. Whole-individual dispersal does not preserve explicit migrant genotype–trait covariance because the parent representation stores those objects separately. The pollen closure represents paternal gamete origin but not flowers, selfing, incompatibility, pollen limitation, carryover or pollinator behaviour. Phase T represents stochastic partner availability but not explicit partner abundance dynamics, coextinction, spatial partner movement or a full multispecies network. Adaptive rewiring was not tested because its preregistered opening condition was not met.

Warning ordering is independently replicated only **within the frozen symmetric H2-R domain**. C2 condition-recovery, connectivity, movement, partner and alignment campaigns withheld warning outcomes; the fresh warning campaign was a separately preregistered C3 replication. Protocol 003 compares non-matched calibrated domains, and the same-strength directional grid contained no matched intermediate-loss comparator, so the isolated causal effect of recurrent-transition direction remains unresolved by design. Finite-horizon non-events remain right-censored.

The empirical Zurich and Izu audits currently use published/open model results rather than new raw-data joint refits. They identify measurable candidate state variables and exact residual-origin tests, but do not yet demonstrate that urban/island history becomes conditionally irrelevant in nature.

## Data and code availability

The parent and extension repositories are separate computational provenance units. The extension pins the parent scientific state at `dd8ee379d0d3518194c767d16402042525bc00dc`. Machine-readable evidence, workflow/artifact provenance, condition ledgers, empirical state audits and submission-build instructions are version controlled. Historical low-replicate and Phase-M results are retained unchanged; high-precision replays, process-resolved robustness closures, dynamic-partner tests, the preregistered Phase-U connectivity replication, the locked cross-layer alignment campaign, the fresh strict-warning replication and the direction-identifiability audit are additive evidence layers and do not overwrite historical provenance.
