# Eco-genetic conditions govern when genetic early warning of functional loss can be validated

## Abstract

Habitat fragmentation can leave populations present while interaction-dependent function weakens. We asked when genetic change can reproducibly precede realised functional loss. In a finite multipatch model, fragmentation reduced interaction, local effective size and high-trait mass before demographic disappearance. Warning-blind calibration recovered a loss-incidence frontier, while a historical allele-mixing heterogeneity signal failed fresh replication and process-resolved portability tests. Complete present-state equality was future-sufficient under the declared Markov closure, but coarse ecological and genetic summaries were not transition-sufficient. Within one frozen loss-generating state, all six baseline-relative `H_alpha/H_gamma` warnings led loss in both the original 35/35 and fresh 33/33 valid pairs. Natural-data tests showed both residual-context redundancy and candidate-state insufficiency across endpoints. These results support state-defined reproducibility: warning should be evaluated within a future-relevant eco-genetic state, not inferred from habitat labels, connectivity scalars or genetic statistics alone.

## Introduction

Ecological function can disappear before the population carrying it disappears. A species may remain numerically present while becoming ineffective as a pollinator, seed disperser, mutualist, defender or other ecological actor (Soulé et al. 2005; McConkey & Drake 2006; Valiente-Banuet et al. 2015). Conservation monitoring therefore has to distinguish population persistence from persistence of ecological function. Abundance, interaction state, allele presence, genetic diversity and realised functional-trait occupancy are related, but they are not interchangeable state variables.

Habitat fragmentation is a natural setting in which these states can separate. Fragmented landscapes couple dispersal, demography and eco-evolutionary feedbacks (Legrand et al. 2017; Govaert et al. 2019), while habitat amount, configuration and matrix quality can have distinct and interacting effects rather than forming one universal fragmentation gradient (Olhnuud et al. 2025; Fletcher et al. 2026). Here we use **interaction-mediated functional fragmentation** for loss or destabilisation of the biotic interaction support required to maintain realised ecological function while focal populations or patches may remain present. This is distinct from organism-centred functional connectivity (Benitez et al. 2025).

The distinction matters because ecological interactions need not respond monotonically to spatial structure. Networks reorganise through species turnover, changing interaction strengths and rewiring (Ward et al. 2026). Pollinator functional diversity can predict pollination function when species richness does not (Hiraiwa & Ushimaru 2024), network architecture can contain information about persistence (Domínguez-Garcia et al. 2024), and multi-habitat landscapes can support interaction complementarity not recoverable by simply adding component webs (Hackett et al. 2024). Removal experiments likewise show compensation in some systems and limited rewiring in others (Brosi & Briggs 2013; Timóteo et al. 2016; Brosi et al. 2017; Leimberger et al. 2023).

Genetic early-warning studies usually begin downstream of these ecological processes. Classical early-warning work asks whether statistics change before transitions (Scheffer et al. 2009; Drake & Griffen 2010), while genetic monitoring asks whether diversity, differentiation or allele-frequency change diagnoses deterioration (Schwartz et al. 2007; Stange et al. 2021). Peled et al. (2026) showed that changing landscape connectivity can generate detectable genetic signals before rapid genetic transitions. Our endpoint is different: realised **interaction-dependent functional-trait loss**. The upstream question is whether the eco-genetic system generates a functional-loss process that can be characterised independently before any precursor is judged.

Warning validation can fail for several reasons that should not be collapsed into one label. The functional state may not be feasible; loss may be too rare or nearly deterministic; finite blocks may cross a calibration threshold by sampling variation; true block probabilities may differ; a perturbation may change which individual trajectories fail without changing population-level incidence; or apparently matched systems may differ in a future-relevant state coordinate that was averaged away. We therefore distinguish **loss incidence**, **between-block heterogeneity**, **trajectory-identity sensitivity**, **state representation** and **warning performance**.

The study follows a condition-first hierarchy (Figure 1). First, can an interaction-supported functional state exist and be disrupted by fragmentation? Second, which eco-genetic states generate an evaluable functional-loss process, and which state summaries are dynamically sufficient? Third, after the loss process is fixed warning-blind, does genetic erosion reproducibly precede functional loss inside that state? Fourth, is warning portable across separately calibrated states? Finally, in natural ecosystems, does a candidate process state itself predict the downstream endpoint, and only then does upstream fragmentation context retain transferable information after that measured state is supplied? Failed generality is retained as a boundary rather than followed by outcome-informed tuning.

## Model and methods

### Condition-first architecture

The study uses two computational provenance units. The parent repository supplies the theorem-guided interaction mechanism, paired fragmentation experiment and inherited symmetric warning benchmark. The extension independently reconstructs high-function sources, maps functional loss, performs robustness and replication tests, and audits natural-system state representations. Parent and extension trajectories are never pooled. All extension analyses using the parent life cycle load scientific commit `dd8ee379d0d3518194c767d16402042525bc00dc`.

Condition recovery is **warning-blind**: genetic-diversity decline, warning times, lead/lag ordering and lead time are unavailable while loss conditions or state representations are selected or replicated.

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

Because only the historical `m=.10` condition showed an equal-rate signal, **Phase U is one preregistered independent replication** using fresh seeds `20291010–20291014`, 100 attempts per seed and exactly two paired conditions: `m=0` and `m=.10`. Interpretation required at least 70 baseline-eligible trajectories in every block and identical paired eligibility. No replacement seeds, repeated fresh ensembles or post-result precision increase were allowed. Phase U replicated the upstream loss-generating closure without inspecting warning outcomes.

Process-resolved tests asked whether the historical allele-only pattern ported to two more explicit movement closures using the same historical seed family. Whole-individual dispersal (`d=.10`) moved integer post-recruitment individuals and realised trait-bin abundance among patches before recurrent transition and drift. Pollen-only gene flow (`g=.20`) replaced a fraction of paternal gamete contributions with external donors while census and realised trait-bin abundance remained local. These nominal comparisons were preregistered robustness tests, not calibrated operator equivalence.

### Aggregate feedback and partner architecture

The aggregate-support precision replay used the three interaction-feedback values already declared in the source grid: `kappa=3.0,4.5,6.0`, with independent source reconstruction at every kappa.

A reduced-form partner-contribution test represented four contributions summing to one and compared intact, even-loss, graded-loss and dominant-loss architectures. A subsequent temporal-partner test held expected support at 0.75 while independently varying partner availability and contribution concentration. Adaptive rewiring was preregistered to open only if this matched-expected-support test established a population-level dynamic-network effect.

### State sufficiency and cross-layer alignment

Under the declared parent closure, the simulator is Markov in its explicit finite present state together with the future forcing and stochastic law. Two histories that reach the same complete present state therefore have the same future trajectory distribution; when the random-number stream is also identical, their realised future trajectories are identical.

To test whether commonly reported coarse summaries could substitute for that complete state, a constructive paired contrast held habitat area, census, the interaction-state multiset, allele-frequency multiset, realised high-trait-mass multiset, complete trait-bin totals, `H_alpha`, `H_gamma` and `F_ST` fixed while reversing the patchwise alignment between interaction support and the genetic/trait-support bundle. The opening certificate compared the exact one-generation transition before any long-horizon outcome was inspected. A single preregistered 60-generation deterioration schedule then compared 500 paired aligned and anti-aligned trajectories. No warning endpoints were inspected and no replacement seeds, alignment permutations or altered schedules were opened after the result.

### Conditional warning, fresh within-state replication and portability

A separate trait-loss-only calibration fixed one symmetric deterioration domain before warning values were evaluated. Relative warnings were first post-baseline generations at which `H_alpha` or `H_gamma` declined 5%, 10% or 20% from their own baselines. Non-events remained right-censored. Predeclared absolute thresholds `H_alpha <= 0.20` and `H_gamma <= 0.20` were audited on the same stored trajectories.

The strongest relative-warning result was then prospectively replicated without recalibration in one independent five-seed ensemble (`20291110–20291114`, 20 attempts per seed). The frozen domain retained mutation `0.10`, `A_ref=.8`, interaction feedback `6.0`, a 30-generation ramp plus 90-generation hold and total normalised barrier increase `.15`. The six endpoint definitions were unchanged. Strict replication required at least 20 valid warning/loss pairs at every endpoint and every valid pair to be a lead with zero ties and zero lags.

Protocol 003 separately recalibrated two evaluable domains. They differ in recurrent-transition, ecological and deterioration parameters, so their fresh-seed contrast is bounded portability evidence and not a single-factor effect of transition direction. Secondary uncertainty analyses resample whole attempted trajectories rather than endpoint rows (Field & Welsh 2007).

### Natural-system residual-origin tests

The empirical counterpart of state sufficiency is conditional predictive redundancy of the upstream fragmentation descriptor after a measured process state is supplied. Natural datasets are not pooled; each is evaluated at its own ecological resolution with whole ecological units held out. We distinguish **candidate-state adequacy** from **residual-context redundancy**: a biologically plausible proximal variable is not treated as an operational state coordinate unless it first carries reproducible information for the downstream process being predicted.

For Honshu–Izu coastal plant–pollinator networks (Hiraiwa & Ushimaru 2024; Figshare `10.6084/m9.figshare.25025000.v1`), the locked archive contains 40 site-season network states and 572 species-level standardized pollen-receipt observations. The preregistered sequence compared: `C0`, pollinator richness + season + focal plant; `C1`, community trait matching `TM_z` + `FDQ` + `FEve` + season + focal plant; and `C2`, `C1 + mainland distance`. Validation left out one entire site at a time across eight folds, with mean squared prediction error as the primary score.

For the Zurich urban-garden system (Reji Chacko, Moretti & Frey 2025 dataset; EnviDat `10.16904/envidat.676`), six reproductive endpoints were fixed before analysis. For each endpoint, `S1` contained the source-defined function-specific pollinator interaction state and `S2` added local plant support, `Urban_500` and their predeclared interaction. Whole gardens were held out. The primary comparison used held-out negative log predictive likelihood, with 10,000 garden-level bootstrap replicates. Positive residual-context evidence required a mean held-out gain above zero with its 95% bootstrap interval wholly above zero.

For *Oenothera harringtonii* (Rhodes et al. 2017; Dryad `10.5061/dryad.p24q3`), correlated paternity was compared between a pollinator-treatment-only model and a model adding standardized maternal spatial isolation. Because maternal plants contributed multiple fruit/seed-family rows, all rows sharing one `plantID` were held out together. A fixed 10,000-permutation test shuffled maternal isolation only among plants with the same multiset of pollinator treatments, preserving the experimental treatment structure.

For the 2015 Hillesden *Eschscholzia californica* experiment, four EIDC datasets from the same 16-array/48-plant design supplied pan-trap pollinator availability and mean intertegular distance, exposed versus supplemented seed production, exposed versus pollinator-excluded seed production, and microsatellite/Cervus paternity (Evans et al. 2017a–d datasets). Schema-only discovery first established the hierarchy `Block -> Experimental array -> focal plant -> fruit/progeny`. Exact models were then preregistered before outcome rows were opened. The candidate process state was fixed to `log1p(pollinator count) + mean ITD`, Habitat was added only after that state, and validation left out one entire array. Pan traps are treated as an array-level pollinator availability/community proxy, not as direct focal-plant visitation.

These are **partial-state tests**, not complete eco-genetic convergence tests. The empirical programme therefore asks two ordered questions: does the candidate state itself predict the endpoint, and, if so, does origin/history still add transferable information?

## Results

### Fragmentation disrupted an interaction-supported functional state

Of 1,200 attempted parent replicates, 1,055 satisfied the full-state hold criterion. Every qualified replicate had lower final interaction, local effective size and realised high-trait mass after equal isolation than in its matched one-large projection. Mean final interaction was 0.998 versus 0.0048; mean local effective size was 72.83 versus 8.18; mean realised high-trait mass was 0.575 versus 0.177.

The fresh fixed-area gradient retained 1,037 prepared sources. The first split from one patch to two isolated patches reduced paired median interaction by 99.83%, local effective size by 77.87% and realised high-trait mass by 71.71%. Interaction and local effective size fell further with additional splitting, while realised high-trait mass was not universally monotone (Figure 2).

### Recurrent turnover changed source feasibility and loss incidence

Across the 15-coordinate grid, 2,269 of 3,375 source attempts supported preparation and projection. The common deterioration campaign contained 648 complete five-seed candidates: 322 historical rapid-loss, 242 persistence and 84 historical R3/mixed-block candidates. No candidate satisfied the original strict R4 screen, so all 15 coarse coordinates remain historically `no_domain_selected` **within the original candidate family** (Figure 3).

The precision audit showed that this coarse candidate-family result was a placement boundary rather than structural impossibility and that low-replicate R3/R4 labels could not themselves establish block heterogeneity. Across ten previously load-bearing R3 cases, none showed detectable excess equal-rate heterogeneity at the historical block sizes.

Exact seed-family replays then recovered a high-to-low incidence frontier. Pooled loss was 0.682 at `p_star=.325`, 0.546/0.538 at `.350` in two historical seed families, 0.407 at `.375` and 0.273 at `.400`. Equal-rate diagnostics were non-significant at all four tested coordinates. The former “narrow R4 bounded by seed-heterogeneous neighbours” interpretation is therefore withdrawn (Figure 4).

### The historical `m=.10` connectivity heterogeneity did not replicate in fresh seeds

In the historical seed family, pooled loss remained near 0.54–0.56 across `m=0,.025,.05,.10,.20`. Only `m=.10` showed excess equal-rate heterogeneity (`p=0.0205`); `m=.20` returned to homogeneous behaviour. Paired McNemar tests versus isolation were non-significant at every nonzero level.

The independent fresh Phase-U ensemble changed the interpretation of that result. Pooled loss was 0.540 at `m=0` and 0.551 at `m=.10`. Both fresh conditions were compatible with common block rates: `p=0.134` for `m=0` and `p=0.745` for `m=.10`. Across 452 comparable trajectories, 49 switched loss→no-loss and 54 no-loss→loss; exact McNemar `p=0.694`.

The preregistered decision was **`historical_m010_heterogeneity_not_freshly_replicated`**. The `p=0.0205` result remains a valid historical seed-family observation, but it is not supported as an independently reproducible `m=.10` heterogeneity effect (Figure 5). **The defensible conclusion is therefore not that `m=.10` is a reproducible heterogeneity threshold.**

### Process-resolved movement also did not establish a portable connectivity effect

Using the historical seed family, whole-individual dispersal at `d=.10` produced pooled loss 0.606 with equal-rate `p=.811`; its paired McNemar contrast versus no connectivity was `p=.143`. Pollen-only paternal gene flow at `g=.20` produced pooled loss 0.532 with equal-rate `p=.728`; paired McNemar tests were `p=.311` versus no connectivity and `p=.266` versus legacy `m=.10`.

Thus the historical allele-mixing heterogeneity observation was absent under both process-resolved operators in the matched historical seed family and absent when the allele-only `m=.10` operator itself was repeated in one independent fresh ensemble. No robust, portable connectivity heterogeneity effect was established across the tested ensembles and closures.

### Aggregate feedback and partner dynamics were bounded negative results

At `kappa=3.0,4.5,6.0`, pooled loss was 0.499, 0.573 and 0.598; all three conditions remained inside the historical intermediate-incidence screen and equal-rate diagnostics were non-significant (`p=.063,.623,.543`).

For reduced-form partner loss, pooled loss was 0.556, 0.544, 0.565 and 0.549 for intact, even, graded and dominant conditions. Equal-rate and paired marginal-risk tests were non-significant despite many trajectory-status switches.

The temporal-partner test increased realised support variance from 0 to 0.04684 to 0.09702 while expected support remained approximately 0.75. Pooled loss was 0.5442, 0.5488 and 0.5533; equal-rate `p=.488,.299,.208`, and paired McNemar `p=.896,.762,.883`. Because no matched-support dynamic-network effect was detected, the preregistered adaptive-rewiring gate remained closed.

### Coarse state equality did not guarantee the same next transition

The aligned and anti-aligned states had identical declared coarse marginal signatures, but their cross-layer covariance changed from `+0.025` to `-0.025`. The exact opening transition differed patchwise, with a maximum generation-1 interaction difference of **0.2543**. Thus layer-wise marginals, standard diversity statistics and aggregate trait occupancy were not transition-sufficient representations of the declared local dynamics.

The long-horizon result was deliberately weaker. Across 500 paired trajectories, realised functional loss occurred in 339 aligned trajectories (`0.678`) and 361 anti-aligned trajectories (`0.722`). There were 92 aligned-loss/anti-no-loss switches and 114 aligned-no-loss/anti-loss switches; exact McNemar `p=.143`. The fixed campaign therefore established a **representation boundary**, not a detected directional long-term loss-incidence effect of alignment.

### Genetic erosion could precede functional loss, but not by a universal threshold

Only after warning-blind loss calibration did we inspect genetic warning. In the inherited symmetric benchmark, 83 of 100 attempted trajectories were available and 35 reached realised functional-trait loss. For each of six baseline-relative `H_alpha`/`H_gamma` endpoints, all 35 valid same-trajectory pairs had genetic erosion before functional loss. Fixed absolute thresholds were not robust: `H_alpha <= 0.20` produced 14 leads and six lags among 20 valid pairs, while `H_gamma <= 0.20` produced eight leads and eight lags among 16 (Figure 2).

The independent fixed-domain fresh-warning replication attempted 100 trajectories, retained 82 available trajectories and observed 33 realised functional losses. At **all six** predeclared relative endpoints, all 33 valid warning/loss pairs were leads, with zero ties and zero lags. The five seed blocks contributed `7,7,7,7,5` valid pairs at every endpoint, and the exact one-sided binomial `p` versus a 0.5 lead probability was `1.1641532182693481e-10` per endpoint. The preregistered decision was **`strict_replication`**.

The supported C3 statement is therefore within-state: baseline-relative genetic erosion strictly replicated as leading functional loss across two independent seed ensembles under the same frozen H2-R loss-generating state. It is not a universal percentage threshold.

### Warning behaviour was not fully portable across calibrated domains

Protocol 003 attempted 100 fresh trajectories in each separately calibrated domain. Valid-pair availability across the six endpoints was 0.540 in the recalibrated symmetric domain and 0.335 in the directional calibrated domain. The two domains contained 323/1/0 versus 184/5/12 lead/tie/lag comparisons. **All six horizon-normalised direct bootstrap contrasts included zero.** The domains also differ in ecological parameters and deterioration schedules, so this is bounded non-portability across calibrated eco-genetic domains, not a single-factor effect of transition direction (Figure 6).

### Upstream geography did not improve held-out prediction after the measured ecological partial state

In the Honshu–Izu test, row-weighted held-out MSE was `1.10963` for the richness-based `C0`, `1.08774` for the functional-state `C1`, and `1.13209` after mainland distance was added in `C2`. Adding distance improved only **3/8** held-out sites and worsened row-weighted MSE by `+0.04436` or **+4.08%** overall. The strongest extrapolation penalty was Hachijo (`dist=178`), where MSE increased from `0.6212` to `0.8660` after distance was added.

The preregistered decision was `ecological_partial_state_convergence_supported`, with a strong completeness caveat. The functional state itself improved only modestly over the richness comparator and beat it in 4/8 folds. The result therefore says that mainland distance carried no detected transferable residual gain after the fixed `I/T` partial state; it does **not** establish that `TM_z + FDQ + FEve` is a complete sufficient state.

### Urban context also showed no reproducible held-out gain after function-specific interaction state

Across the six fixed Zurich reproductive endpoints, **0/6** met the preregistered positive residual-context rule. All six were classified `no_detected_residual_urban_information`. For carrot seed set, mean held-out `Delta_g=NLL(S1)-NLL(S2)` was `-3.1047` with a garden-bootstrap 95% interval `[-6.1169,-0.7893]`; for radish seed set it was `-0.00543 [-0.01039,-0.00094]`, so the larger context model predicted unseen gardens worse for those endpoints. The other four intervals included zero.

This result does not show that urban context is ecologically irrelevant or that the interaction-only state is complete. It shows that under the fixed whole-garden validation design, adding local plant support and `Urban_500` after the source-defined function-specific interaction state did not recover transferable residual predictive information.

### Spatial mating opportunity remained after pollinator treatment in *Oenothera*

The locked *Oenothera harringtonii* test contained 60 fruit/seed-family rows from 23 maternal plants. Adding maternal spatial isolation after pollinator treatment reduced leave-one-maternal-plant-out MSE from `0.11619` to `0.09187`, a **20.93%** improvement, and MAE from `0.28515` to `0.24107`. The coefficient on standardized isolation was `+0.15638` on the correlated-paternity scale, and the treatment-profile-preserving 10,000-permutation test gave `p=0.00130`. The preregistered decision was **`residual_isolation_detected`**.

This is a mating-state result, not a direct functional-loss result. Higher correlated paternity indicates lower realised paternal diversity, so the supported statement is that pollinator treatment alone did not close the contemporary `G_mating/C_pollen` state: local spatial mating opportunity retained independent process-relevant information.

### A plausible pollinator proxy did not earn general state status in *Eschscholzia*

The *Eschscholzia californica* multi-process analysis first passed a schema-only synchronization gate, but the preregistered F endpoint was subsequently closed by its exact metadata-consistency rule: array `1||3` was encoded as `Fallow ground` in the pollinator source and `Fallow graound` in the seed-function source. Because post hoc typo repair was prohibited, `F_seed` was classified `not_identifiable_for_endpoint` and the overall primary decision was **`multi_endpoint_not_identifiable`**.

The independently estimable mating and pollen-movement endpoints provided a measurement boundary. For 457 progeny across 16 arrays, adding pan-trap `log1p(count) + mean ITD` changed held-out negative log likelihood from `0.387347` to `0.383796`; the array-bootstrap gain was `0.003551`, 95% CI `[-0.006385,0.013203]`, so `G_mating` was `process_state_not_predictively_supported`. Adding Habitat after that proxy gave gain `-0.002049 [-0.006579,0.001205]`. Adding the preregistered `R_auto` coordinate to G gave `0.001699 [-0.004095,0.007596]`.

For 254 outcross pollen-movement rows across the same 16 arrays, S0/S1/S2 MSE was `1.703951`, `1.668285` and `1.726978`. The process-state gain `0.035666 [-0.123473,0.170571]` was unsupported, whereas Habitat addition produced a reproducible predictive penalty of `-0.058694 [-0.094528,-0.028381]`. This penalty is not evidence that habitat is biologically irrelevant. Together, the estimable endpoints show that array-level pan-trap abundance and mean ITD cannot simply be assumed to constitute an effective-interaction state for mating or pollen movement.

## Discussion

### Functional fragmentation can precede demographic disappearance

Dividing the same prepared state into isolated patches sharply reduced interaction, local effective size and realised high-trait mass before population disappearance. This does not imply that every geometrically fragmented landscape has a simpler network. It shows that spatial reorganisation can disrupt the process maintaining function before occupancy itself vanishes. That narrower mechanism is consistent with evidence that habitat amount, configuration, matrix quality and network turnover can have distinct effects (Olhnuud et al. 2025; Fletcher et al. 2026; Gama et al. 2025).

### Calibration labels are not biological estimands

The precision programme separates event incidence, block heterogeneity, trajectory identity and warning performance. The historical R1–R4 classifier remains useful as a prospective warning-blind calibration screen, but a threshold crossing in a small finite block is not evidence of biological heterogeneity by itself.

The recurrent-turnover frontier illustrates the point. `.325` and `.400` both lie outside the historical R4 screen for opposite incidence reasons, yet neither shows excess block heterogeneity at high precision. Conversely, the historical `m=.10` seed family did show an equal-rate signal, but the fresh ensemble did not. A statistically detectable pattern in one finite seed family therefore cannot be silently promoted to a portable parameter-specific mechanism.

### Connectivity is process-specific and representation-dependent

The combined connectivity programme gives a clearer negative boundary than the historical allele-mixing result alone. The historical signal was seed-family contingent, did not alter paired marginal risk detectably, failed one fresh replication and did not port to whole-individual or pollen-only movement. Natural pollen flow, seed dispersal, demographic movement, recolonisation and partner movement act on different state variables and timescales. Monitoring designs should therefore measure the biologically relevant movement process instead of treating one scalar connectivity value as exchangeable across mechanisms.

The cross-layer audit adds a second representation warning. Even when census, allele and interaction marginals, standard diversity statistics and realised trait state match, their patchwise alignment can change the exact next transition. Yet the same contrast did not establish a directional long-term loss-incidence effect under the single fixed schedule. The practical implication is narrow but important: **spatial co-location can be state information even when it is not itself a universal risk axis**.

### Negative network tests delimit the model rather than the ecology

The aggregate-feedback, reduced-form partner-loss and matched-support temporal-partner campaigns all returned bounded negative population-level results. These nulls do not show that ecological networks are dynamically irrelevant. Rather, the tested scalar feedback range, one-partner reductions and temporal support variance/concentration were insufficient to create a robust change in functional-loss incidence or between-block heterogeneity under their declared closures.

Real networks add partner abundance dynamics, topology, coextinction, trait constraints, spatial movement and adaptive rewiring. Experimental and synthetic studies show that compensation is context dependent (Brosi & Briggs 2013; Timóteo et al. 2016; Brosi et al. 2017; Leimberger et al. 2023; Ward et al. 2026). Because the matched-support temporal test did not establish a dynamic-network effect to decompose, rewiring remains closed rather than being tuned to rescue a preferred result.

### Reproducibility belongs to a loss-generating state

The fresh warning replication changes the interpretation of conditionality. The result is no longer only that baseline-relative genetic erosion *can* precede functional loss. Within one frozen symmetric H2-R state, the same six relative-warning orderings were recovered as 35/35 leads in the inherited benchmark and 33/33 leads in an independent fresh-seed ensemble.

Conditionality is therefore not merely a limitation. It identifies the domain in which the positive warning result is reproducible. At the same time, fixed absolute thresholds produced both leads and lags, and warning behaviour was not fully portable across separately calibrated domains. The supported ordering is:

`loss-generating state -> warning evaluability -> within-state replication -> cross-state portability test`.

A genetic statistic should not be asked to carry information that belongs to an unmeasured ecological state.

### Different fragmentation routes can converge only through a common measured state

The natural-data tests make the state-sufficiency argument empirically falsifiable. In Honshu–Izu networks, mainland distance is a known upstream filter of network properties, yet adding it after functional diversity and trait matching did not improve transfer to unseen sites. In Zurich, urban/local context has function-specific marginal associations, yet no one of six reproductive endpoints showed reproducible positive held-out gain from adding that context after a function-specific pollinator interaction state.

The *Oenothera* result supplies the complementary failure mode. Pollinator treatment was biologically proximal, yet maternal spatial isolation still improved prediction of correlated paternity by 20.93% and passed the locked permutation test. Spatial mating opportunity therefore remained a missing state coordinate rather than disappearing into a generic pollinator label.

The *Eschscholzia* result moves the logic one step earlier. Pan-trap abundance and mean ITD were plausible pollinator-state coordinates, but they did not show reproducible held-out gains for the estimable mating or pollen-movement endpoints. The correct empirical sequence is therefore **candidate-state adequacy -> residual-origin/history test**. Conditioning on an ecologically plausible variable is not evidence that it belongs to the minimal future-relevant state.

These results are not demonstrations that geography, urbanisation or habitat context is irrelevant. Nor do they prove that any tested interaction state is complete. Their common result is narrower: upstream descriptors can become predictively redundant after an informative proximal state, missing process coordinates can retain residual information, and candidate proxies that are not endpoint-informative should not be granted state status by assumption.

Natural examples also show what remains outside these partial states. Low-density urban *Crepis sancta* can show reduced visitation and seed set despite nonzero wider movement; Miyake-jima *Camellia japonica* can retain pollination through broadened partner and pollen movement; *Conospermum undulatum* shows why standing adult genetics can lag the contemporary mating landscape; and *Spondias purpurea* links reduced visitation, contracted pollen flow, lower reproductive function and stronger seed/juvenile genetic deterioration within one near-synchronised fragmentation comparison (Cristóbal-Pérez et al. 2021). These mechanisms motivate an empirical search basis containing demographic support, effective interactions, trait matching, process-specific movement, compensation, cohort-specific genetics, ecological memory and cross-layer spatial alignment.

The cross-system hypothesis is therefore not that cities behave like islands. It is that **different fragmentation routes belong to the same operational functional-fragmentation regime only if a measured future-relevant state makes their origin or history dispensable for predicting what function happens next**. A residual origin effect is evidence to search for a missing process, cohort, alignment term or ecological memory variable—not evidence that the habitat label itself is the mechanistic state.

### Limits

The model is finite and its numerical coordinates are not transferable ecological thresholds. Failure to detect block heterogeneity is not a theorem of universal homogeneity. Phase U is one preregistered independent replication of the upstream loss-process contrast, so its non-replication limits the historical connectivity claim but does not prove that no other seed family could ever show heterogeneity.

The process-resolved movement closures are partial. Whole-individual dispersal does not preserve explicit migrant genotype–trait covariance because the parent representation stores those objects separately. The pollen closure represents paternal gamete origin but not flowers, selfing, incompatibility, pollen limitation, carryover or pollinator behaviour. The partner closure represents stochastic availability rather than a full multispecies dynamic network.

The alignment campaign establishes transition-level insufficiency of coarse marginals but not a detected directional long-term loss-incidence effect. The Honshu–Izu and Zurich analyses are ecological partial-state tests: neither synchronizes the full candidate `D/I/T/C/R/G_by_cohort/M/A` state, and absence of residual context does not prove state completeness. *Oenothera* evaluates a mating-state endpoint rather than direct ecological function, so its residual-isolation result does not establish a functional-loss effect. In *Eschscholzia*, the primary F endpoint remained non-identifiable under the preregistered metadata gate; pan traps are availability proxies rather than direct visitation, and failure of their count/ITD state to improve G/C prediction does not imply that pollinators are biologically irrelevant. Conversely, a future dataset in which context improves prediction after a demonstrably informative process state would identify a missing state coordinate rather than contradict the condition-first framework.

Within-state warning replication does not establish a universal relative or absolute threshold and does not imply portability across eco-genetic states. Protocol 003 compares non-matched calibrated domains, so its contrast cannot identify a direction-only causal effect. The condition-recovery, movement, partner and Phase U **fresh-replication campaigns withheld warning outcomes**; the separate fixed-domain fresh-warning replication is the campaign that inspected warning ordering. Finite-horizon non-events remain right-censored.

## Data and code availability

The parent and extension repositories are separate computational provenance units. The extension pins the parent scientific state at `dd8ee379d0d3518194c767d16402042525bc00dc`. Machine-readable evidence, workflow/artifact provenance, condition ledgers, state-representation audits, natural-data preregistrations and submission-build instructions are version controlled. Third-party natural raw data are not committed; the analyses lock their public DOI/version or member-level provenance and retain compact derived summaries. Historical low-replicate and allele-mixing results are retained unchanged; precision replays, process-resolved closures, fresh warning replication, cross-layer alignment tests and natural state-sufficiency tests are additive evidence layers and do not overwrite historical provenance.