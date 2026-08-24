# Eco-genetic conditions govern when genetic early warning of functional loss can be validated

## Abstract

Habitat fragmentation can leave populations present while interaction-dependent function weakens, but genetic warning is meaningful only if downstream loss is characterised independently. In a finite model, fragmentation reduced interaction, local effective size and realised high-trait mass. Warning-blind calibration located intermediate-loss conditions, while a finite-sample audit separated loss incidence from block heterogeneity. Recurrent turnover shifted loss incidence. A historical allele-mixing heterogeneity observation failed one preregistered fresh-seed replication; process-resolved movement, aggregate feedback and partner-dynamic tests yielded bounded negative results. Baseline-relative genetic erosion preceded observed losses in one calibrated benchmark, whereas absolute thresholds and portability were limited. Genetic warning is therefore downstream of the eco-genetic process generating functional loss.

## Introduction

Ecological function can disappear before the population carrying it disappears. A species may remain numerically present while becoming ineffective as a pollinator, seed disperser, mutualist, defender or other ecological actor (Soulé et al. 2005; McConkey & Drake 2006; Valiente-Banuet et al. 2015). Conservation monitoring therefore has to distinguish population persistence from persistence of ecological function. Abundance, interaction state, allele presence, genetic diversity and realised functional-trait occupancy are related, but they are not interchangeable state variables.

Habitat fragmentation is a natural setting in which these states can separate. Fragmented landscapes couple dispersal, demography and eco-evolutionary feedbacks (Legrand et al. 2017; Govaert et al. 2019), while habitat amount, configuration and matrix quality can have distinct and interacting effects rather than forming one universal fragmentation gradient (Olhnuud et al. 2025; Fletcher et al. 2026). Here we use **interaction-mediated functional fragmentation** for loss or destabilisation of the biotic interaction support required to maintain realised ecological function while focal populations or patches may remain present. This is distinct from organism-centred functional connectivity (Benitez et al. 2025).

The distinction matters because ecological interactions need not respond monotonically to spatial structure. Networks reorganise through species turnover, changing interaction strengths and rewiring (Ward et al. 2026). Pollinator functional diversity can predict pollination function when species richness does not (Hiraiwa & Ushimaru 2024), network architecture can contain information about persistence (Domínguez-Garcia et al. 2024), and multi-habitat landscapes can support interaction complementarity not recoverable by simply adding component webs (Hackett et al. 2024). Removal experiments likewise show compensation in some systems and limited rewiring in others (Brosi & Briggs 2013; Timóteo et al. 2016; Brosi et al. 2017; Leimberger et al. 2023).

Genetic early-warning studies usually begin downstream of these ecological processes. Classical early-warning work asks whether statistics change before transitions (Scheffer et al. 2009; Drake & Griffen 2010), while genetic monitoring asks whether diversity, differentiation or allele-frequency change diagnoses deterioration (Schwartz et al. 2007; Stange et al. 2021). Peled et al. (2026) showed that changing landscape connectivity can generate detectable genetic signals before rapid genetic transitions. Our endpoint is different: realised **interaction-dependent functional-trait loss**. The upstream question is whether the eco-genetic system generates a functional-loss process that can be characterised independently before any precursor is judged.

Warning validation can fail for several reasons that should not be collapsed into one label. The functional state may not be feasible; loss may be too rare or nearly deterministic; finite blocks may cross a calibration threshold by sampling variation; true block probabilities may differ; or a perturbation may change which individual trajectories fail without changing population-level incidence. We therefore distinguish **loss incidence**, **between-block heterogeneity**, **trajectory-identity sensitivity** and **warning performance**.

The study follows a condition-first hierarchy (Figure 1). First, can an interaction-supported functional state exist and be disrupted by fragmentation? Second, how do recurrent turnover, connectivity representation and interaction conditions alter source feasibility and functional loss? Third, after the loss process is fixed warning-blind, can genetic erosion precede functional loss? Fourth, is warning behaviour portable across independently calibrated eco-genetic domains? Failed generality is retained as a boundary rather than followed by outcome-informed tuning.

## Model and methods

### Condition-first architecture

The study uses two computational provenance units. The parent repository supplies the theorem-guided interaction mechanism, paired fragmentation experiment and inherited symmetric warning benchmark. The extension independently reconstructs high-function sources, maps functional loss and performs robustness and portability tests. Parent and extension trajectories are never pooled. All extension analyses using the parent life cycle load scientific commit `dd8ee379d0d3518194c767d16402042525bc00dc`.

Condition recovery is **warning-blind**: genetic-diversity decline, warning times, lead/lag ordering and lead time are unavailable while loss conditions are selected or replicated.

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

### Conditional warning and portability

A separate trait-loss-only calibration fixed one symmetric deterioration domain before warning values were evaluated. Relative warnings were first post-baseline generations at which `H_alpha` or `H_gamma` declined 5%, 10% or 20% from their own baselines. Non-events remained right-censored. Predeclared absolute thresholds `H_alpha <= 0.20` and `H_gamma <= 0.20` were audited on the same stored trajectories.

Protocol 003 separately recalibrated two evaluable domains. They differ in recurrent-transition, ecological and deterioration parameters, so their fresh-seed contrast is bounded portability evidence and not a single-factor effect of transition direction. Secondary uncertainty analyses resample whole attempted trajectories rather than endpoint rows (Field & Welsh 2007).

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

### Genetic erosion could precede functional loss, but not by a universal threshold

Only after warning-blind loss calibration did we inspect genetic warning. In the inherited symmetric benchmark, 83 of 100 attempted trajectories were available and 35 reached realised functional-trait loss. For each of six baseline-relative `H_alpha`/`H_gamma` endpoints, all 35 valid same-trajectory pairs had genetic erosion before functional loss. Fixed absolute thresholds were not robust: `H_alpha <= 0.20` produced 14 leads and six lags among 20 valid pairs, while `H_gamma <= 0.20` produced eight leads and eight lags among 16 (Figure 2).

### Warning behaviour was not fully portable across calibrated domains

Protocol 003 attempted 100 fresh trajectories in each separately calibrated domain. Valid-pair availability across the six endpoints was 0.540 in the recalibrated symmetric domain and 0.335 in the directional calibrated domain. The two domains contained 323/1/0 versus 184/5/12 lead/tie/lag comparisons. **All six horizon-normalised direct bootstrap contrasts included zero.** The domains also differ in ecological parameters and deterioration schedules, so this is bounded non-portability across calibrated eco-genetic domains, not a single-factor effect of transition direction (Figure 6).

## Discussion

### Functional fragmentation can precede demographic disappearance

Dividing the same prepared state into isolated patches sharply reduced interaction, local effective size and realised high-trait mass before population disappearance. This does not imply that every geometrically fragmented landscape has a simpler network. It shows that spatial reorganisation can disrupt the process maintaining function before occupancy itself vanishes. That narrower mechanism is consistent with evidence that habitat amount, configuration, matrix quality and network turnover can have distinct effects (Olhnuud et al. 2025; Fletcher et al. 2026; Gama et al. 2025).

### Calibration labels are not biological estimands

The precision programme separates event incidence, block heterogeneity, trajectory identity and warning performance. The historical R1–R4 classifier remains useful as a prospective warning-blind calibration screen, but a threshold crossing in a small finite block is not evidence of biological heterogeneity by itself.

The recurrent-turnover frontier illustrates the point. `.325` and `.400` both lie outside the historical R4 screen for opposite incidence reasons, yet neither shows excess block heterogeneity at high precision. Conversely, the historical Phase-M `m=.10` family did show an equal-rate signal, but the fresh Phase-U ensemble did not. A statistically detectable pattern in one finite seed family therefore cannot be silently promoted to a portable parameter-specific mechanism.

### Connectivity is process-specific and the historical heterogeneity was seed-family contingent

The combined connectivity programme now gives a clearer negative boundary than the Phase-M result alone. In the historical Phase-M family, `m=.10` was the only migration level with detected block heterogeneity, but pooled loss was nearly unchanged and paired marginal-risk tests were null. In the independent Phase-U ensemble, the same `m=.10` operator was homogeneous. Whole-individual and pollen-only closures were also homogeneous in the historical Phase-M family.

The defensible conclusion is therefore not that `m=.10` is a reproducible heterogeneity threshold. It is that one historical allele-mixing seed family produced an excess-block pattern that was **both seed-family contingent and representation-specific** within the tested programme. Natural pollen flow, seed dispersal, demographic movement, recolonisation and partner movement act on different state variables and timescales; empirical plant genetics likewise shows heterogeneous fragmentation responses (Miguel-Peñaloza et al. 2023). Monitoring designs should therefore measure the relevant movement process instead of treating a scalar allele-frequency mixer as biological connectivity in general.

### Interaction architecture remains bounded by negative tests

The aggregate-feedback, reduced-form partner-loss and matched-support temporal-partner campaigns all returned bounded negative population-level results. These nulls do not show that ecological networks are dynamically irrelevant. Rather, the tested scalar feedback range, one-partner reductions and temporal support variance/concentration were insufficient to create a robust change in functional-loss incidence or between-block heterogeneity under their declared closures.

Real networks add partner abundance dynamics, topology, coextinction, trait constraints, spatial movement and adaptive rewiring. Experimental and synthetic studies show that compensation is context dependent (Brosi & Briggs 2013; Timóteo et al. 2016; Brosi et al. 2017; Leimberger et al. 2023; Ward et al. 2026). Because Phase T did not establish a dynamic-network effect to decompose, rewiring remains closed rather than being tuned to rescue a preferred result.

### Genetic warning is downstream of the loss-generating process

The inherited benchmark proves that baseline-relative genetic erosion can precede realised functional loss in one calibrated domain. It does not provide a universal threshold: absolute cut-offs produced both leads and lags, and warning availability differed across recalibrated domains.

The condition-first ordering therefore survives every robustness correction. Before asking whether a genetic statistic leads loss, establish whether the functional state exists, estimate loss incidence, distinguish sampling variation from block heterogeneity, replicate load-bearing stochastic findings where possible, and verify that the ecological operator represents the biological process being claimed. Only then should lead time and ordering be evaluated.

### Different fragmentation routes can converge only through a common measured state

The state-sufficiency audit sharpens this ecological translation. Under the declared Markov closure, complete equality of the present joint state is future-sufficient, whereas matched census, interaction and allele-frequency marginals, `H_alpha`, `H_gamma`, `F_ST` and realised trait state can still produce different next states when patchwise interaction–genetic alignment differs. Empirical conditioning must therefore preserve future-relevant joint spatial structure rather than averages alone.

Natural systems already expose these coordinates. In Montpellier, low-density urban populations of *Crepis sancta* receive fewer pollinator visits and set fewer seeds, while parentage studies in the same urban programme detect contemporary pollen/seed movement and immigration among patches (Cheptou & Avendaño 2006; Dornier & Cheptou 2013). On Miyake-jima, volcanic damage reduced *Camellia japonica* floral resources, yet wider-ranging *Zosterops japonicus* increased pollen immigration and donor diversity and compensated pollination; seed genetic diversity increased with damage (Abe et al. 2013). Across 40 Honshu–Izu coastal networks, pollinator functional diversity altered trait matching and pollination success more directly than pollinator species diversity (Hiraiwa & Ushimaru 2024).

These systems represent contrasting routes—interaction limitation, movement-mediated compensation and functional-diversity limitation—not habitat categories to pool. A common functional-fragmentation regime is supported only if system origin or fragmentation history no longer improves prediction of subsequent realised function after conditioning on demographic support, realised interactions, trait/functional state, process-specific connectivity, mating/genetic state, alternative functional routes and their spatial alignment. Residual history would indicate a missing process or ecological memory variable.

### Limits

The model is finite and its numerical coordinates are not transferable ecological thresholds. Failure to detect block heterogeneity is not a theorem of universal homogeneity. Phase U is one preregistered independent replication, so non-replication limits the Phase-M claim but does not prove that no seed ensemble could ever show heterogeneity at `m=.10`.

The process-resolved movement closures are partial. Whole-individual dispersal does not preserve explicit migrant genotype–trait covariance because the parent representation stores those objects separately. The pollen closure represents paternal gamete origin but not flowers, selfing, incompatibility, pollen limitation, carryover or pollinator behaviour. Phase T represents stochastic partner availability but not explicit partner abundance dynamics, coextinction, spatial partner movement or a full multispecies network. Adaptive rewiring was not tested because its preregistered opening condition was not met.

Warning succeeds only in the inherited calibrated benchmark; condition-recovery, movement, partner and fresh-replication campaigns withheld warning outcomes. Protocol 003 compares non-matched calibrated domains, so its contrast cannot identify a direction-only causal effect. Finite-horizon non-events remain right-censored.

## Data and code availability

The parent and extension repositories are separate computational provenance units. The extension pins the parent scientific state at `dd8ee379d0d3518194c767d16402042525bc00dc`. Machine-readable evidence, workflow/artifact provenance, condition ledgers and submission-build instructions are version controlled. Historical low-replicate and Phase-M results are retained unchanged; high-precision replays, process-resolved robustness closures, dynamic-partner tests and the preregistered Phase-U fresh replication are additive evidence layers and do not overwrite historical provenance.