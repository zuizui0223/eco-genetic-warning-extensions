# Matching genetic diversity and interaction summaries can hide different ecological transitions

## Abstract

Ecological forecasts depend on whether measured summaries preserve the state governing what happens next. In a finite multipatch model, states with identical census, interaction, allele-frequency and trait marginals, `H_alpha`, `H_gamma` and `F_ST` but opposite patchwise cross-layer alignment differed by 0.2543 in the next interaction transition. This establishes transition-level insufficiency; a fixed 500-pair campaign did not detect directional long-horizon loss incidence. Natural-data tests then separated informative partial states, missing process coordinates, inadequate proxies and representations that erased mechanistic weighting. Six frozen relative-diversity rules preceded every observed loss, but generation-30 binary AUC was only 0.500–0.538 and 0.500–0.510; by the full horizon every non-event had also crossed. A preregistered exploratory continuous audit produced landmark- and ensemble-dependent AUCs (0.418–0.692 and 0.422–0.687), not a portable signal. Future-relevant state inference requires joint representation and an empirical measurement/representation gate before origin or precursor claims.

## Introduction

Ecological function can disappear before the population carrying it disappears. A species may remain numerically present while becoming ineffective as a pollinator, seed disperser, mutualist, defender or other ecological actor (Soulé et al. 2005; McConkey & Drake 2006; Valiente-Banuet et al. 2015). Conservation monitoring therefore has to distinguish population persistence from persistence of ecological function. Abundance, interaction state, allele presence, genetic diversity and realised functional-trait occupancy are related, but they are not interchangeable state variables.

Habitat fragmentation is a natural setting in which these states can separate. Fragmented landscapes couple dispersal, demography and eco-evolutionary feedbacks (Legrand et al. 2017; Govaert et al. 2019), while habitat amount, configuration and matrix quality can have distinct and interacting effects rather than forming one universal fragmentation gradient (Olhnuud et al. 2025; Fletcher et al. 2026). Here we use **interaction-mediated functional fragmentation** for loss or destabilisation of the biotic interaction support required to maintain realised ecological function while focal populations or patches may remain present. This is distinct from organism-centred functional connectivity (Benitez et al. 2025).

The distinction matters because ecological interactions need not respond monotonically to spatial structure. Networks reorganise through species turnover, changing interaction strengths and rewiring (Ward et al. 2026). Pollinator functional diversity can predict pollination function when species richness does not (Hiraiwa & Ushimaru 2024), network architecture can contain information about persistence (Domínguez-Garcia et al. 2024), and multi-habitat landscapes can support interaction complementarity not recoverable by simply adding component webs (Hackett et al. 2024). Removal experiments likewise show compensation in some systems and limited rewiring in others (Brosi & Briggs 2013; Timóteo et al. 2016; Brosi et al. 2017; Leimberger et al. 2023).

Genetic early-warning studies usually begin downstream of these ecological processes. Classical early-warning work asks whether statistics change before transitions (Scheffer et al. 2009; Drake & Griffen 2010), while genetic monitoring asks whether diversity, differentiation or allele-frequency change diagnoses deterioration (Schwartz et al. 2007; Stange et al. 2021). Peled et al. (2026) showed that changing landscape connectivity can generate detectable genetic signals before rapid genetic transitions. Our endpoint is different: realised **interaction-dependent functional-trait loss**. The upstream question is whether the eco-genetic system generates a functional-loss process that can be characterised independently before any precursor is judged.

Warning validation can fail for several reasons that should not be collapsed into one label. The functional state may not be feasible; loss may be too rare or nearly deterministic; finite blocks may cross a calibration threshold by sampling variation; true block probabilities may differ; a perturbation may change which individual trajectories fail without changing population-level incidence; or apparently matched systems may differ in a future-relevant state coordinate that was averaged away. We therefore distinguish **loss incidence**, **between-block heterogeneity**, **trajectory-identity sensitivity**, **state representation** and **warning performance**.

The study follows a condition-first hierarchy (Figure 1). First, can an interaction-supported functional state exist and be disrupted by fragmentation? Second, which eco-genetic states generate an evaluable functional-loss process, and which state summaries are dynamically sufficient? Third, after the loss process is fixed warning-blind, does genetic erosion reproducibly precede functional loss inside that state? Fourth, is warning portable across separately calibrated states? Finally, in natural ecosystems, does a candidate process state itself predict the downstream endpoint, does the chosen analysis representation preserve the information that makes that state mechanistically distinct, and only then does upstream fragmentation context retain transferable information after that measured state is supplied? Failed generality is retained as a boundary rather than followed by outcome-informed tuning.

## Model and methods

### Condition-first architecture

The parent repository supplies the interaction mechanism, fragmentation experiment and inherited warning benchmark; the extension reconstructs sources, maps loss, tests replication and audits natural-state representations. Their trajectories are never pooled, and extension analyses load parent scientific commit `dd8ee379d0d3518194c767d16402042525bc00dc`. Condition recovery is **warning-blind**: diversity decline and warning timing are unavailable during state selection or replication.

### Interaction-supported function and fragmentation

The multipatch model keeps interaction, allele frequency, realised trait bins, census and local effective size distinct. The same H1-prepared state was projected to one patch or equal isolated fragments at fixed total area (12 cells × 100 attempts); a fresh-seed sensitivity used 1, 2, 3, 4, 6, 8, 12 and 16 patches.

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

`p_star` is an effective equilibrium, not an empirical mutation-rate estimate. The grid crossed `kappa_mu = 0.05, 0.20, 0.35` with `p_star = 0.10, 0.25, 0.50, 0.75, 0.90`, with independent source reconstruction per coordinate. Of 3,375 source and 20,250 deterioration attempts, 648 complete five-seed candidates entered the historical R1–R4 screen. Historical R3/R4 labels are retained as protocol facts, not latent biological classes. Load-bearing contrasts were replayed at 100 attempts per seed; inference separates pooled incidence, equal-rate diagnostics, paired switches and exact McNemar tests.

### Allele-frequency connectivity, fresh replication and process-resolved movement

At the recovered recurrent-turnover anchor, allele-frequency mixing varied while all other conditions were fixed. The operator is

\[
p_i'=(1-m)p_i+m\bar p.
\]

This `migration_rate` is allele-frequency mixing, not demographic migration, dispersal or pollinator movement. Phase M used 100 attempts per historical seed across `m=0,.025,.05,.10,.20`. Because only `m=.10` showed an equal-rate signal, **Phase U is one preregistered independent replication** of `m=0` versus `.10` in five fresh seeds with fixed eligibility and no replacements or precision increase; warning outcomes remained hidden. Separate preregistered tests implemented whole-individual dispersal (`d=.10`) and paternal pollen flow (`g=.20`). These nominal settings were robustness tests, not calibrated operator equivalence.

### Aggregate feedback and partner architecture

The aggregate-support replay used the declared `kappa=3.0,4.5,6.0` grid with independent reconstruction. Partner tests compared four fixed contribution architectures, then varied availability and concentration at matched expected support 0.75. Adaptive rewiring opened only if the latter established a population-level effect.

### State sufficiency and cross-layer alignment

The simulator is Markov in its explicit finite present state, future forcing and stochastic law. A paired contrast tested whether coarse summaries could substitute for that state: habitat, census, interaction, allele-frequency and trait marginals, `H_alpha`, `H_gamma` and `F_ST` were fixed while patchwise cross-layer alignment was reversed. The exact one-generation transition was certified first; one preregistered 60-generation schedule then compared 500 pairs without warnings, replacement seeds or altered alignments.

### Conditional warning, fresh within-state replication and portability

A warning-blind calibration fixed one symmetric domain before evaluating first crossings of 5%, 10% or 20% baseline-relative `H_alpha/H_gamma` decline; non-events remained right-censored. The same six rules were prospectively replicated without recalibration in five fresh seeds (`20291110–20291114`; 20 attempts each). The frozen domain used mutation `.10`, `A_ref=.8`, feedback `6.0`, a 30-generation ramp, 90-generation hold and barrier increase `.15`.

The post-review binary audit restored every baseline-eligible trajectory and evaluated generations 30/60/90 without changing endpoints; endpoint rows sharing a trajectory are repeated measurements. A separate one-time protocol then fixed `1 - H(t)/H(0)` at those landmarks. Prior losses were excluded; cases lost in `(t,120]`, controls remained loss-free through 120, and AUC intervals used 10,000 stratified trajectory bootstraps. No slope, selected landmark or endpoint pooling was opened.

Protocol 003 separately recalibrated two evaluable domains. They differ in recurrent-transition, ecological and deterioration parameters, so their fresh-seed contrast is bounded portability evidence and not a single-factor effect of transition direction. Secondary uncertainty analyses resample whole attempted trajectories rather than endpoint rows (Field & Welsh 2007).

### Natural-system residual-origin tests

The empirical counterpart is conditional predictive redundancy of upstream context after a measured process state is supplied. Datasets are not pooled and whole ecological units are held out. Candidate-state adequacy and representation preservation are required before residual-context redundancy is interpreted.

Honshu–Izu data (Hiraiwa & Ushimaru 2024; Figshare `10.6084/m9.figshare.25025000.v1`) contained 40 site-season networks and 572 pollen-receipt observations. Eight-fold whole-site validation compared richness, functional state (`TM_z + FDQ + FEve`) and functional state plus mainland distance by mean squared error.

Zurich data (Reji Chacko, Moretti & Frey 2025; EnviDat `10.16904/envidat.676`) fixed six reproductive endpoints. Whole-garden validation compared function-specific pollinator state with that state plus plant support, `Urban_500` and their interaction; positive context evidence required a positive held-out gain with its 10,000-bootstrap interval above zero.

For *Oenothera harringtonii* (Rhodes et al. 2017; Dryad `10.5061/dryad.p24q3`), correlated paternity models added maternal isolation after pollinator treatment. Validation grouped rows by maternal plant; 10,000 restricted permutations preserved each plant's treatment multiset.

Four Hillesden *Eschscholzia californica* datasets shared a 16-array/48-plant design (Evans et al. 2017a–d). Preregistered whole-array validation tested `log1p(pollinator count) + mean ITD` before Habitat. Pan traps are treated as an array-level pollinator availability/community proxy, not as direct focal-plant visitation. A separate post-lock path fixed exact repairs at `1||3` and `1||4`, with no further repair or row exclusion.

For 23 *Campanula americana* populations (Koski et al. 2018; Dryad `10.5061/dryad.5nj81nf`), leave-one-population-out ridge models compared a mean, raw visitation, sex-phase visitation and independently calibrated transfer-rate coordinates after feature-wise standardization. A post-lock response-firewalled diagnostic tested whether phase and effective predictors were constant rescalings.

These are **partial-state tests**, not complete eco-genetic convergence tests. The empirical programme therefore applies three ordered gates: **measurement adequacy -> representation/information preservation -> residual origin/history test**. Only a candidate state that is endpoint-informative and remains distinguishable after preprocessing is eligible for a residual-context convergence test.

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

The independent fresh Phase-U ensemble changed the interpretation of that result. Pooled loss was 0.540 at `m=0` and 0.551 at `m=.10`. Both fresh conditions were compatible with common block rates: `p=0.134` for `m=0` and `p=0.745` for `m=.10`. Across 452 comparable trajectories, 49 switched loss→no-loss and 54 no-loss→loss; exact McNemar `p=0.694`, and the paired risk difference was `+0.0111` with 95% CI `[-0.0330,0.0551]`. This is a precision-bounded null, not equivalence.

The preregistered decision was **`historical_m010_heterogeneity_not_freshly_replicated`**. The `p=0.0205` result remains a valid historical seed-family observation, but it is not supported as an independently reproducible `m=.10` heterogeneity effect (Figure 5). **The defensible conclusion is therefore not that `m=.10` is a reproducible heterogeneity threshold.**

### Process-resolved movement also did not establish a portable connectivity effect

Using the historical seed family, whole-individual dispersal at `d=.10` produced pooled loss 0.606 with equal-rate `p=.811`; its paired McNemar contrast versus no connectivity was `p=.143`. Pollen-only paternal gene flow at `g=.20` produced pooled loss 0.532 with equal-rate `p=.728`; paired McNemar tests were `p=.311` versus no connectivity and `p=.266` versus legacy `m=.10`.

Thus the historical allele-mixing heterogeneity observation was absent under both process-resolved operators in the matched historical seed family and absent when the allele-only `m=.10` operator itself was repeated in one independent fresh ensemble. No robust, portable connectivity heterogeneity effect was established across the tested ensembles and closures.

### Aggregate feedback and partner dynamics were bounded negative results

At `kappa=3.0,4.5,6.0`, pooled loss was 0.499, 0.573 and 0.598; all three conditions remained inside the historical intermediate-incidence screen and equal-rate diagnostics were non-significant (`p=.063,.623,.543`).

For reduced-form partner loss, pooled loss was 0.556, 0.544, 0.565 and 0.549 for intact, even, graded and dominant conditions. Paired risk differences relative to intact were `-0.0113 [-0.0688,0.0462]`, `+0.0091 [-0.0461,0.0643]` and `-0.0068 [-0.0577,0.0441]` for even, graded and dominant loss. These are precision-bounded nulls, not equivalence results.

The temporal-partner test increased realised support variance from 0 to 0.04684 to 0.09702 while expected support remained approximately 0.75. Pooled loss was 0.5442, 0.5488 and 0.5533. Paired risk differences were `+0.0045 [-0.0293,0.0384]` for even minus constant, `+0.0091 [-0.0350,0.0531]` for dominant minus constant and `+0.0045 [-0.0256,0.0347]` for dominant minus even. Because the fixed trial detected no matched-support effect and did not establish equivalence, the preregistered adaptive-rewiring gate remained closed.

### Coarse state equality did not guarantee the same next transition

The aligned and anti-aligned states had identical declared coarse marginal signatures, but their cross-layer covariance changed from `+0.025` to `-0.025`. Their generation-1 interaction vectors were `.464/.619/.753/.851` and `.718/.699/.680/.660`, respectively, with a maximum patchwise difference of **0.2543**. Thus layer-wise marginals, standard diversity statistics and aggregate trait occupancy were not transition-sufficient representations of the declared local dynamics.

The long-horizon result was deliberately weaker. Across 500 paired trajectories, realised functional loss occurred in 339 aligned trajectories (`0.678`) and 361 anti-aligned trajectories (`0.722`). There were 92 aligned-loss/anti-no-loss switches and 114 aligned-no-loss/anti-loss switches; exact McNemar `p=.143`. The fixed campaign therefore established a **representation boundary**, not a detected directional long-term loss-incidence effect of alignment.

### Relative diversity thresholds ordered observed losses but did not discriminate events

Only after warning-blind loss calibration did we inspect genetic warning. In the inherited symmetric benchmark, 83 of 100 attempted trajectories were available and 35 reached realised functional-trait loss. For each of six baseline-relative `H_alpha`/`H_gamma` endpoints, all 35 event trajectories crossed before loss. However, every endpoint also crossed in all 48 non-event trajectories by the common administrative horizon.

The independent fixed-domain fresh-warning replication attempted 100 trajectories, retained 82 available trajectories and observed 33 realised functional losses. At all six endpoints, all 33 event trajectories crossed before loss, while all 49 non-event trajectories also crossed by the horizon. The historical preregistered decision **`strict_replication`** is retained as a protocol fact about valid-pair ordering, not as a current predictive-validity classification.

At the fixed generation-30 landmark, inherited binary-marker AUC ranged `0.500–0.538` across the six rules and fresh AUC ranged `0.500–0.510`. These non-degenerate landmark results did not support useful discrimination. By the full horizon, every rule was positive in every event and non-event trajectory: sensitivity and false-positive rate were 1.0, specificity was 0 and binary-marker AUC was mechanically 0.5. PPV equalled event prevalence (0.422 and 0.402), and NPV was undefined. Thus the six frozen rules show **replicated event-conditional ordering without discrimination**, not validated predictive early warning.

The separately preregistered exploratory continuous audit did not show a stable alternative. At generation 30, AUC was near chance in both ensembles (`0.535/0.533` inherited and `0.522/0.556` fresh for `H_alpha/H_gamma`). Later values changed direction across landmarks and ensembles: inherited AUC ranged `0.418–0.692`, while fresh AUC ranged `0.422–0.687`. Two isolated cells had percentile intervals above 0.5—generation-90 inherited `H_alpha` (`0.692 [0.523,0.840]`) and generation-60 fresh `H_gamma` (`0.687 [0.504,0.848]`)—but neither pattern reproduced at the same coordinate and landmark in the other ensemble. With only three future cases at fresh generation 90, its intervals were especially wide. These exploratory data permit time-specific diversity information but do not establish a portable continuous warning score.

### Warning behaviour was not fully portable across calibrated domains

Protocol 003 attempted 100 trajectories per separately calibrated domain. Valid-pair availability was 0.540 versus 0.335, with 323/1/0 versus 184/5/12 lead/tie/lag comparisons; all six horizon-normalised direct contrasts included zero. Because ecological parameters and schedules also differ, this is bounded portability rather than a direction-only effect (Figure 6).

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

The primary lock is permanent. A prospective F-only sensitivity permitted only the declared correction at `1||3`, but metadata preflight found the same mismatch at `1||4` and triggered `stop_pre_model_unexpected_second_metadata_mismatch`. No F model or bootstrap ran, and no secondary estimate exists.

A separately preregistered post-lock descriptive reconstruction then corrected both exact typo keys (`1||3` and `1||4`; three rows each), eliminating the cross-source Habitat mismatches. The unchanged F preparation gate nevertheless stopped on `F primary response has missing/non-finite/negative value`. No additional response repair or row exclusion was allowed; no F model, score or bootstrap ran. The descriptive path therefore ended `postlock_descriptive_reconstruction_not_estimable` and recovered no F estimate.

The independently estimable mating and pollen-movement endpoints provided a measurement boundary. For 457 progeny across 16 arrays, adding pan-trap `log1p(count) + mean ITD` changed held-out negative log likelihood from `0.387347` to `0.383796`; the array-bootstrap gain was `0.003551`, 95% CI `[-0.006385,0.013203]`, so `G_mating` was `process_state_not_predictively_supported`. Adding Habitat after that proxy gave gain `-0.002049 [-0.006579,0.001205]`. Adding the preregistered `R_auto` coordinate to G gave `0.001699 [-0.004095,0.007596]`.

For 254 outcross pollen-movement rows across the same 16 arrays, S0/S1/S2 MSE was `1.703951`, `1.668285` and `1.726978`. The process-state gain `0.035666 [-0.123473,0.170571]` was unsupported, whereas Habitat addition produced a reproducible predictive penalty of `-0.058694 [-0.094528,-0.028381]`. This penalty is not evidence that habitat is biologically irrelevant. Together, the estimable endpoints show that array-level pan-trap abundance and mean ITD cannot simply be assumed to constitute an effective-interaction state for mating or pollen movement.

### Mechanistic weighting was erased by the declared *Campanula* representation

In the 23-population *Campanula americana* test, none of the preregistered interaction representations improved leave-one-population-out prediction of pollen limitation over the training-population mean. MSE was `0.04265` for the mean baseline, `0.05623` for raw visitation and `0.05731` for both phase-matched visitation and independently calibrated effective transfer; the raw-to-effective gain was `-0.00108` with 95% CI `[-0.00510,0.00238]`. The decision was **`no_interaction_representation_supported`**.

The response-firewalled diagnostic then confirmed that all six effective deposition/removal coordinates were constant positive rescalings of their matched phase-visitation coordinates across populations. Maximum relative ratio deviation was `1.74e-16`, and after independent feature-wise z-standardization the paired coordinates differed by at most `8.88e-16`. Thus the machine-identical phase/effective models were explained by the declared preprocessing: standardization erased the constant efficiency multipliers. This is a **representation/information-preservation failure**, not evidence that per-visit efficiency is biologically irrelevant.

## Discussion

### Functional fragmentation can precede demographic disappearance

Dividing the same prepared state into isolated patches sharply reduced interaction, local effective size and realised high-trait mass before population disappearance. This does not imply that every geometrically fragmented landscape has a simpler network. It shows that spatial reorganisation can disrupt the process maintaining function before occupancy itself vanishes. That narrower mechanism is consistent with evidence that habitat amount, configuration, matrix quality and network turnover can have distinct effects (Olhnuud et al. 2025; Fletcher et al. 2026; Gama et al. 2025).

### Calibration labels are not biological estimands

The precision programme separates event incidence, block heterogeneity, trajectory identity and warning performance. The historical R1–R4 classifier remains useful as a prospective warning-blind calibration screen, but a threshold crossing in a small finite block is not evidence of biological heterogeneity by itself.

The recurrent-turnover frontier illustrates the point. `.325` and `.400` both lie outside the historical R4 screen for opposite incidence reasons, yet neither shows excess block heterogeneity at high precision. Conversely, the historical `m=.10` seed family did show an equal-rate signal, but the fresh ensemble did not. A statistically detectable pattern in one finite seed family therefore cannot be silently promoted to a portable parameter-specific mechanism.

### Connectivity is process-specific and representation-dependent

The combined connectivity programme gives a clearer negative boundary than the historical allele-mixing result alone. The historical signal was seed-family contingent, did not alter paired marginal risk detectably, failed one fresh replication and did not port to whole-individual or pollen-only movement. Natural pollen flow, seed dispersal, demographic movement, recolonisation and partner movement act on different state variables and timescales. Monitoring designs should therefore measure the biologically relevant movement process instead of treating one scalar connectivity value as exchangeable across mechanisms.

The cross-layer audit adds a second representation warning. Even when census, allele and interaction marginals, standard diversity statistics and realised trait state match, their patchwise alignment can change the exact next transition. Yet the same contrast did not establish a directional long-term loss-incidence effect under the single fixed schedule. The practical implication is narrow but important: **spatial co-location can be state information even when it is not itself a universal risk axis**.

### Precision-bounded negative tests delimit the model rather than the ecology

The aggregate-feedback, reduced-form partner-loss and matched-support temporal-partner campaigns all returned precision-bounded negative population-level results. Their paired effect intervals include zero but still permit differences of several percentage points; they are not equivalence tests and do not show that ecological networks are dynamically irrelevant. Rather, the fixed trials did not detect robust changes in functional-loss incidence or between-block heterogeneity under their declared closures.

Real networks add partner abundance dynamics, topology, coextinction, trait constraints, spatial movement and adaptive rewiring. Experimental and synthetic studies show that compensation is context dependent (Brosi & Briggs 2013; Timóteo et al. 2016; Brosi et al. 2017; Leimberger et al. 2023; Ward et al. 2026). Because the matched-support temporal test did not establish a dynamic-network effect to decompose, rewiring remains closed rather than being tuned to rescue a preferred result.

### Event-only warning validation failed the full-denominator test

The two frozen symmetric H2-R ensembles reproduced the same six event-conditional orderings as 35/35 and 33/33 leads. Fixed generation-30 binary-marker AUCs remained near chance. By the full horizon, the same rules had fired in 48/48 and 49/49 non-events, so selection on valid warning/loss pairs hid complete loss of specificity.

The continuous audit narrows rather than generalises this conclusion. Baseline-relative diversity erosion occasionally separated later losses within one landmark and ensemble, but the coordinate/time pattern did not reproduce across ensembles. The evidence therefore rejects predictive validity of the six frozen binary rules while leaving open the bounded possibility that genetic diversity carries time-specific information under a prospectively validated continuous model.

The warning result is therefore a supporting boundary, not a positive headline. Loss-process calibration remains necessary to define an endpoint population, but it is not sufficient to validate a predictor. The supported ordering is:

`future-relevant state -> full-denominator warning validation -> only then portability`.

A genetic statistic should not be asked to carry information that belongs to an unmeasured ecological state.

### Different fragmentation routes can converge only through a common measured state

The natural-data tests make the state-sufficiency argument empirically falsifiable. In Honshu–Izu networks, mainland distance is a known upstream filter of network properties, yet adding it after functional diversity and trait matching did not improve transfer to unseen sites. In Zurich, urban/local context has function-specific marginal associations, yet no one of six reproductive endpoints showed reproducible positive held-out gain from adding that context after a function-specific pollinator interaction state.

The *Oenothera* result supplies the complementary failure mode. Pollinator treatment was biologically proximal, yet maternal spatial isolation still improved prediction of correlated paternity by 20.93% and passed the locked permutation test. Spatial mating opportunity therefore remained a missing state coordinate rather than disappearing into a generic pollinator label.

The *Eschscholzia* result moves the logic one step earlier. Pan-trap abundance and mean ITD were plausible pollinator-state coordinates, but they did not show reproducible held-out gains for the estimable mating or pollen-movement endpoints. Exact repair of the complete known Habitat typo set still did not make the F endpoint estimable because the unchanged response-validity gate failed before modelling. Candidate-state adequacy and response support must therefore be demonstrated rather than granted by biological plausibility or metadata repair.

The *Campanula* result adds a distinct analysis-layer boundary. Independent per-visit efficiency information existed in the source data (Koski et al. 2018), but each effective transfer coordinate was only a constant multiplier of its matched phase-visitation coordinate across populations. Feature-wise standardization therefore collapsed the two representations exactly. A state can consequently fail not only because the wrong ecological variable was measured, but because the analysis representation discards the information that made a measured variable mechanistically distinct.

The empirical sequence is therefore **measurement adequacy -> representation/information preservation -> residual origin/history test**. These results are not demonstrations that geography, urbanisation or habitat context is irrelevant. Their common claim is narrower: upstream descriptors may become redundant after an informative preserved state, missing process coordinates may retain residual information, and neither plausible proxies nor mechanistically motivated measurements should be granted state status unless their endpoint-relevant information survives the analysis pipeline.

Mechanistic anchors expose missing coordinates: *Crepis sancta* shows uncompensated interaction loss; Miyake-jima *Camellia japonica* retains partner and pollen movement; *Conospermum undulatum* exposes cohort lag; and *Spondias purpurea* links interaction, pollen flow, function and genetics. They motivate movement, memory and cross-layer spatial alignment.

The cross-system hypothesis is therefore not that cities behave like islands. It is that **different fragmentation routes belong to the same operational functional-fragmentation regime only if a measured future-relevant state makes their origin or history dispensable for predicting what function happens next**. A residual origin effect is evidence to search for a missing process, cohort, alignment term or ecological memory variable—not evidence that the habitat label itself is the mechanistic state.

### Limits

Model coordinates are finite, not transferable ecological thresholds. Undetected block heterogeneity does not establish homogeneity. Phase U is one preregistered independent replication of the upstream loss-process contrast, so its non-replication limits the historical connectivity claim but does not prove that no other seed family could ever show heterogeneity.

The process-resolved movement closures are partial. Whole-individual dispersal does not preserve explicit migrant genotype–trait covariance because the parent representation stores those objects separately. The pollen closure represents paternal gamete origin but not flowers, selfing, incompatibility, pollen limitation, carryover or pollinator behaviour. The partner closure represents stochastic availability rather than a full multispecies dynamic network.

The alignment campaign establishes transition-level insufficiency of coarse marginals but not a detected directional long-term loss-incidence effect. The Honshu–Izu and Zurich analyses are ecological partial-state tests: neither synchronizes the full candidate `D/I/T/C/R/G_by_cohort/M/A` state, and absence of residual context does not prove state completeness. *Oenothera* evaluates a mating-state endpoint rather than direct ecological function, so its residual-isolation result does not establish a functional-loss effect. In *Eschscholzia*, the primary F endpoint and both post-lock repair paths yielded no F estimate; pan traps are availability proxies rather than direct visitation, and failure of their count/ITD state to improve G/C prediction does not imply that pollinators are biologically irrelevant. In *Campanula*, none of the preregistered interaction representations earned held-out predictive adequacy for pollen limitation, and equality of phase/effective models resulted from feature-wise scaling of constant-rescaled predictors; the response-firewalled diagnostic does not authorize rerunning the same outcome with alternative scaling or aggregation. Conversely, a future dataset in which context improves prediction after a demonstrably informative and information-preserving process state would identify a missing state coordinate rather than contradict the condition-first framework.

The frozen relative thresholds do not support predictive early-warning validity: their fixed generation-30 binary AUCs were near chance, and all six eventually fired in every non-event trajectory. Full-horizon AUC 0.5 primarily records that all markers became constant positives. The exploratory continuous audit does not show that `H_alpha` or `H_gamma` lacks information generally; its occasional later discrimination was not portable across landmarks and ensembles. Non-events remain right-censored for event-time inference but are known event-free controls at the common horizon. Protocol 003 compares non-matched calibrated domains, so its contrast cannot identify a direction-only causal effect. The condition-recovery, movement, partner and Phase U **fresh-replication campaigns withheld warning outcomes**; the separate fixed-domain fresh-warning replication is the campaign that inspected warning ordering.

## Data and code availability

The parent and extension repositories are separate computational provenance units. The extension pins the parent scientific state at `dd8ee379d0d3518194c767d16402042525bc00dc`. Machine-readable evidence, workflow/artifact provenance, condition ledgers, state-representation audits, natural-data preregistrations and submission-build instructions are version controlled. Third-party natural raw data are not committed; the analyses lock their public DOI/version or member-level provenance and retain compact derived summaries. Historical low-replicate and allele-mixing results are retained unchanged; precision replays, process-resolved closures, fresh warning replication, cross-layer alignment tests and natural state-sufficiency tests are additive evidence layers and do not overwrite historical provenance.
