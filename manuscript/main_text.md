# Eco-genetic conditions govern when genetic early warning of functional loss can be validated

## Abstract

Habitat fragmentation can leave populations present while interaction-dependent function weakens, but genetic warning is meaningful only if the downstream loss process is characterised independently. In a finite eco-genetic model, fragmentation sharply reduced interaction, local effective size and realised high-trait mass. Warning-blind calibration located intermediate-loss conditions, but a finite-sample audit showed that the original blockwise R3/R4 screen could not itself identify biological heterogeneity. High-precision replays separated loss incidence, between-block heterogeneity, trajectory identity and warning performance. Recurrent turnover shifted loss incidence; allele-frequency mixing produced non-monotone heterogeneity at one tested level without changing marginal risk; aggregate interaction feedback was robust across three predeclared levels; reduced-form partner loss changed many trajectories but not incidence or heterogeneity. Baseline-relative genetic erosion preceded observed losses in one calibrated benchmark, while portability was bounded. Genetic warning is therefore downstream of the eco-genetic process generating functional loss.

## Introduction

Ecological function can disappear before the population carrying it disappears. A species may remain numerically present while becoming ineffective as a pollinator, seed disperser, mutualist, defender or other ecological actor (Soulé et al. 2005; McConkey & Drake 2006; Valiente-Banuet et al. 2015). Conservation monitoring therefore has to distinguish population persistence from persistence of ecological function. Abundance, interaction state, allele presence, genetic diversity and realised functional-trait occupancy are related, but they are not interchangeable state variables.

Habitat fragmentation is a natural setting in which these states can separate. Habitat amount, configuration and matrix quality can have distinct and interacting effects, rather than forming one universal fragmentation gradient (Olhnuud et al. 2025; Fletcher et al. 2026). Landscape ecology increasingly defines fragmentation functionally from the organism's perspective, particularly through connectivity (Benitez et al. 2025). Here we use the more specific term **interaction-mediated functional fragmentation** for loss or destabilisation of the biotic interaction support required to maintain realised ecological function while focal populations or patches may remain present. This is deliberately distinct from functional connectivity.

The distinction matters because ecological interactions need not respond monotonically to spatial structure. Networks reorganise through species turnover, changing interaction strengths and rewiring (Ward et al. 2026). Pollinator functional diversity can predict pollination function when species richness does not (Hiraiwa & Ushimaru 2024), network architecture can contain information about persistence (Domínguez-Garcia et al. 2024), and multi-habitat landscapes can support interaction complementarity not recoverable by simply adding component webs (Hackett et al. 2024). Removal experiments likewise show compensation in some systems and limited rewiring in others (Brosi & Briggs 2013; Timóteo et al. 2016; Brosi et al. 2017; Leimberger et al. 2023).

Genetic early-warning studies usually begin downstream of these ecological processes. Classical early-warning work asks whether statistics change before transitions (Scheffer et al. 2009; Drake & Griffen 2010), while genetic monitoring asks whether diversity, differentiation or allele-frequency change diagnoses deterioration (Schwartz et al. 2007; Stange et al. 2021). Peled et al. (2026) recently showed that changing landscape connectivity can generate detectable genetic early-warning signals before rapid **genetic** transitions. Our endpoint is different: realised **interaction-dependent functional-trait loss**. The upstream question is therefore whether the eco-genetic system generates a functional-loss process that can be characterised independently before any precursor is judged.

That qualification is stronger than asking for a convenient event frequency. Warning validation can fail for several reasons that should not be collapsed into one label: the functional state may not be feasible; loss may be too rare or nearly deterministic; comparable blocks may have genuinely different loss probabilities; or a perturbation may change which individual trajectories fail without changing population-level incidence. We therefore distinguish **loss incidence**, **between-block heterogeneity**, **trajectory-identity sensitivity** and **warning performance**.

The study follows a condition-first hierarchy (Figure 1). First, can an interaction-supported functional state exist and be disrupted by fragmentation? Second, how do recurrent turnover, effective genetic connectivity and interaction conditions alter source feasibility and functional loss? Third, after the loss process is characterised warning-blind, can genetic erosion precede functional loss? Fourth, is warning behaviour portable across independently calibrated eco-genetic domains? Failed generality is retained as a boundary rather than followed by outcome-informed tuning.

## Model and methods

### Condition-first architecture

The study uses two computational provenance units. The parent repository supplies the theorem-guided interaction mechanism, paired fragmentation experiment and inherited symmetric warning benchmark. The extension independently reconstructs high-function sources under recurrent-transition coordinates, maps functional loss, tests connectivity and interaction conditions and performs a separately declared portability validation. Parent and extension trajectories are never pooled. All extension analyses using the parent life cycle load scientific commit `dd8ee379d0d3518194c767d16402042525bc00dc`.

Condition recovery is **warning-blind**: genetic-diversity decline, warning times, lead/lag ordering and lead time are unavailable while loss conditions are selected or validated. The original strict calibration used a historical block screen, but subsequent precision validation is treated separately from that screen.

### Interaction-supported function and fragmentation

The finite multipatch model records interaction state, a high-trait-associated allele, realised trait-bin occupancy, population size and local effective size. Potential high-trait viability, realised high-trait occupancy, allele persistence, genetic diversity and population persistence remain separate variables.

The fragmentation experiment projected the same H1-prepared full state either to one large patch or to equal isolated fragments at fixed total area. Twelve primary cells contained 100 attempted seed-replicates each. A later fresh-seed sensitivity projected prepared sources across 1, 2, 3, 4, 6, 8, 12 and 16 equal isolated patches.

### Recurrent state transition

Let `p` be the high-trait-associated allele frequency. The extension applies

\[
M(p)=\kappa_\mu p_\mu^*+(1-\kappa_\mu)p,
\]

with effective low-to-high and high-to-low transition rates

\[
u_{L\to H}=\kappa_\mu p_\mu^*,\qquad
u_{H\to L}=\kappa_\mu(1-p_\mu^*).
\]

`p_star` is an effective recurrent-transition equilibrium, **not an empirical mutation-rate estimate**. The common grid crossed `kappa_mu = 0.05, 0.20, 0.35` with `p_star = 0.10, 0.25, 0.50, 0.75, 0.90`. Each coordinate received independent high-function source reconstruction.

### Historical loss screen and precision audit

Source reconstruction crossed 15 recurrent-transition coordinates with three area-reference values, three interaction-feedback values, five master seeds and five replicates, for 3,375 attempts. The common deterioration campaign completed **20,250** attempts and contained 648 complete five-seed candidates. Calibration used realised post-baseline functional-trait loss only.

The preregistered historical classifier called a candidate R1 when all five observed block loss rates were below 0.30, R2 when all were above 0.70, R4 when all were within `[0.30,0.70]`, and R3 otherwise. The historical code names R3 `seed_heterogeneous` and R4 `warning_evaluable`; we retain those labels for provenance but no longer treat them as biological estimands. **Historical R3 is described as a mixed-block screen failure unless independent high-precision evidence supports excess heterogeneity.** R4 was an operational intermediate-incidence screen, not evidence that genetic warning succeeds.

A later finite-sample audit quantified the probability that this all-five-block screen would pass or fail under a common latent loss probability at the observed block sizes. Every load-bearing historical R3 contrast was then replayed at 100 attempted replicates per master seed using the exact historical seeds. Each precision replay required its first 20 attempts to reproduce the locked historical eligible/loss counts before interpretation. Final inference reports pooled loss incidence and a separate equal-rate diagnostic across blocks; paired contrasts additionally report bidirectional status switches and exact McNemar tests.

### Effective genetic connectivity

At the recovered recurrent-turnover anchor, allele-frequency mixing varied while all other conditions were fixed: `A_ref=1.0`, interaction `kappa=4.5`, `kappa_mu=0.35`, `p_star=0.35`, four equal patches, horizon 120 and normalised barrier increase 0.30. The operator is

\[
p_i'=(1-m)p_i+m\bar p.
\]

This `migration_rate` is allele-frequency mixing and **not demographic migration**, pollen or seed dispersal, pollinator movement, recolonisation or trait-bin movement. The high-precision replay used the five historical master seeds, 100 attempts per seed and paired all migration levels on the same prepared source and trajectory seed.

### Aggregate interaction support and reduced-form partner loss

The aggregate-support test used only the three interaction-feedback values already declared in the source grid: `kappa=3.0,4.5,6.0`. Source reconstruction was independent at every kappa because feedback strength changes source geometry. The precision replay used the same five historical master seeds with 100 attempts per seed and condition.

A separate reduced-form partner-contribution test represented four contributions summing to one. The intact control retained all four. Three predeclared architectures—`(0.25,0.25,0.25,0.25)`, `(0.40,0.30,0.20,0.10)` and `(0.70,0.10,0.10,0.10)`—each lost one partner, balanced by replicate index. The loss architectures shared a `4→3` richness change and mean retained support 0.75. The high-precision replay used the same five historical master seeds and paired architectures on the same prepared sources.

`interaction kappa` is aggregate positive-feedback strength, **not partner richness, connectance, pollinator diversity or network dimensionality**. The partner layer is also reduced-form: it has no explicit partner population dynamics, connectance, nestedness, modularity, coextinction, adaptive rewiring or biological partner movement.

### Conditional warning and portability

A separate trait-loss-only calibration fixed one symmetric deterioration domain before warning values were evaluated. Relative warnings were first post-baseline generations at which `H_alpha` or `H_gamma` declined 5%, 10% or 20% from their own baselines. Non-events remained right-censored. Predeclared absolute thresholds `H_alpha <= 0.20` and `H_gamma <= 0.20` were audited on the same stored trajectories.

Historical Protocol 003 separately recalibrated two evaluable domains. They differ in recurrent-transition, ecological and deterioration parameters, so their fresh-seed contrast is bounded portability evidence and **not a single-factor effect of transition direction**. Secondary uncertainty analyses resample whole attempted trajectories rather than endpoint rows.

## Results

### Fragmentation disrupted an interaction-supported functional state

Of 1,200 attempted parent replicates, 1,055 satisfied the full-state hold criterion. Every qualified replicate had lower final interaction, local effective size and realised high-trait mass after equal isolation than in its matched one-large projection. Mean final interaction was 0.998 versus 0.0048; mean local effective size was 72.83 versus 8.18; mean realised high-trait mass was 0.575 versus 0.177.

The fresh fixed-area gradient retained 1,037 prepared sources. The first split from one patch to two isolated patches reduced paired median interaction by 99.83%, local effective size by 77.87% and realised high-trait mass by 71.71%. Interaction and local effective size fell further with additional splitting, while realised high-trait mass was not universally monotone (Figure 2). Fragmentation therefore created functional vulnerability before demographic disappearance.

### Recurrent turnover changed source feasibility and historical loss-screen placement

Across the 15-coordinate grid, 2,269 of 3,375 source attempts supported preparation and projection. The common deterioration campaign contained 648 complete five-seed candidates: 322 historical rapid-loss, 242 persistence and 84 historical R3/mixed-block candidates. No candidate satisfied the original strict R4 screen, so all 15 coarse coordinates remain historically `no_domain_selected` (Figure 3).

That result is immutable for the original candidate family, but its interpretation changed after precision audit. **The coarse result was a placement boundary rather than structural impossibility.** More importantly, low-replicate R3/R4 labels could not themselves establish block heterogeneity: across ten previously load-bearing R3 cases, none showed detectable excess equal-rate heterogeneity at the historical block sizes, while the hard screen had substantial sampling-only failure probabilities.

### High-precision recurrent-turnover replays recovered an incidence frontier

The corrected high-precision frontier replays used exact historical master seeds and passed every first-20 provenance audit. In the Phase-D seed family, pooled loss declined from **0.682** at `p_star=.325` to **0.546** at `.350` and **0.407** at `.375`. The historical screen classified `.325` outside R4 and `.350/.375` inside it, but equal-rate diagnostics were non-significant at all three conditions (`p=0.295, 0.370, 0.693`).

An independent Phase-C seed family gave pooled loss **0.538** at `.350` and **0.273** at `.400`. `.350` remained inside the historical R4 screen; `.400` remained outside because four of five high-precision block rates were below 0.30. Its equal-rate diagnostic was non-significant (`p=0.151`).

Together these results reject the earlier description of a narrow R4 region bounded by biological seed heterogeneity. The supported local pattern is an **incidence frontier**: functional loss is high at `.325`, intermediate around `.350–.375`, and low by `.400`, with no detected excess block heterogeneity at those four high-precision conditions (Figure 4).

### Allele-frequency connectivity produced non-monotone block heterogeneity, not a marginal-risk gradient

The connectivity precision replay reproduced all 25 historical first-20 prefixes. Pooled loss was 0.559, 0.548, 0.564, 0.557 and 0.541 across `m=0,.025,.05,.10,.20`. Thus average functional-loss risk showed no monotone response.

At high precision, `m=0,.025,.05,.20` were compatible with common block rates. Only `m=.10` retained a historical R3 screen failure and showed detectable excess between-block heterogeneity (`p=0.0205`), driven by one block with 66 losses among 93 eligible trajectories while the other four ranged 0.488–0.539. The effect was non-monotone because `m=.20` returned to homogeneous R4-screen behaviour.

Paired comparisons reinforced the distinction between trajectory identity and marginal risk. Relative to isolation, loss-status switches occurred in both directions at every nonzero migration rate. Exact McNemar tests were non-significant (`p=0.542, 0.901, 1.000, 0.546`). Allele-frequency connectivity therefore changed which trajectories failed, and at one tested level changed exchangeability across blocks, without a directional mean-risk effect (Figure 5).

### Aggregate feedback was robust across the tested range; partner loss was a high-precision negative condition result

The aggregate interaction-feedback replay reproduced all 15 historical prefixes. Pooled loss was **0.499, 0.573 and 0.598** at `kappa=3.0,4.5,6.0`; all three remained inside the historical intermediate-incidence screen. Equal-rate diagnostics were `p=0.063, 0.623, 0.543`. This is a **bounded negative condition result**: the predeclared scalar feedback range did not generate a new incidence or block-heterogeneity boundary. **The kappa search was closed rather than widened to manufacture a boundary.**

The partner-loss precision replay likewise changed the interpretation of the original low-replicate result. Pooled loss was **0.556** for intact, **0.544** for even loss, **0.565** for graded loss and **0.549** for dominant-partner loss. All four conditions were inside the historical intermediate-incidence screen, and none showed detectable excess block heterogeneity. Paired McNemar tests against intact were non-significant (`p=0.757, 0.809, 0.861`) despite many bidirectional trajectory switches.

Thus the earlier claim that one-partner loss moved R4 to R3 by reducing event reproducibility is withdrawn. Under this reduced-form closure, partner loss changed individual stochastic histories but not high-precision marginal incidence or block heterogeneity.

### Genetic erosion could precede functional loss, but not by a universal absolute threshold

Only after warning-blind loss calibration did we inspect genetic warning. In the inherited symmetric benchmark, 83 of 100 attempted trajectories were available and 35 reached realised functional-trait loss. For each of six baseline-relative `H_alpha`/`H_gamma` endpoints, all 35 valid same-trajectory pairs had genetic erosion before functional loss. Fixed absolute thresholds were not robust: `H_alpha <= 0.20` produced 14 leads and six lags among 20 valid pairs, while `H_gamma <= 0.20` produced eight leads and eight lags among 16 (Figure 2).

### Warning behaviour was not fully portable across independently calibrated domains

Protocol 003 attempted 100 fresh trajectories in each separately calibrated domain. Valid-pair availability across the six endpoints was 0.540 in the recalibrated symmetric domain and 0.335 in the directional calibrated domain. The two domains contained 323/1/0 versus 184/5/12 lead/tie/lag comparisons. Absolute-generation timing differed at some endpoints, but all six horizon-normalised direct bootstrap contrasts included zero.

Because the domains also differ in ecological parameters and deterioration schedules, this is bounded non-portability across calibrated eco-genetic domains and **not a single-factor effect of transition direction** (Figure 6).

## Discussion

### Structural fragmentation and interaction-mediated functional fragmentation are distinct

The parent experiment establishes the causal entry point: dividing the same prepared state into isolated patches sharply reduced interaction, local effective size and realised high-trait mass before population disappearance. This does not imply that every geometrically fragmented landscape has a simpler network. It shows that spatial reorganisation can disrupt the process maintaining function before occupancy itself vanishes.

That distinction aligns with contemporary fragmentation research. Habitat amount, configuration and matrix quality need not have the same effects (Olhnuud et al. 2025; Fletcher et al. 2026), while functional connectivity depends on the organism and process considered (Benitez et al. 2025). Interaction-mediated functional fragmentation therefore names a narrower mechanistic possibility: realised function can weaken because its biotic support is disrupted even when focal populations remain.

### Event frequency, block heterogeneity, trajectory identity and warning performance are different quantities

The most important correction from the precision programme is methodological and biological. The historical R1–R4 classifier was useful as a warning-blind screen for locating intermediate loss incidence, but its low-replicate R3/R4 labels were too sampling-sensitive to identify biological heterogeneity directly. A block near 0.5 could cross the fixed 0.30/0.70 boundaries by sampling variation alone; a condition near an incidence boundary could almost inevitably fail the all-five-block screen even when every block shared one latent rate.

The high-precision replays therefore separate four estimands. **Loss incidence** asks how often function is lost. **Between-block heterogeneity** asks whether comparable blocks plausibly share a loss probability. **Trajectory-identity sensitivity** asks whether paired perturbations change which realisations fail. **Warning performance** asks whether a precursor leads the downstream event after that process has been fixed. These quantities can vary independently.

The recurrent-turnover frontier is the clearest example. `.325` and `.400` remain outside the historical R4 screen, but high precision shows opposite incidence boundaries—high loss versus low loss—without detectable excess block heterogeneity. The old common label did not imply a common mechanism. Conversely, `m=.10` shows genuine block heterogeneity at high precision even though its pooled loss is almost identical to isolation and its paired marginal-risk test is null.

### Recurrent turnover primarily controls loss incidence in the tested frontier

The high-precision `p_star` sequence moves from high to low functional-loss incidence. This is consistent with `p_star` changing recurrent support for the high-associated state, but the numerical values are model coordinates rather than ecological thresholds. The result also clarifies the original 15/15 no-domain outcome: the coarse candidate family missed a useful intermediate-incidence region, yet that region is not a razor-thin biological regime bounded by seed heterogeneity.

This matters for warning calibration. A warning study needs enough downstream events to estimate ordering, but intermediate event incidence should not be confused with proof of exchangeability. The historical screen remains a legitimate prospective design device; its role is now explicit and narrower.

### Connectivity is a process family, not a scalar rescue axis

The high-precision connectivity result is non-monotone. `m=.10` produced excess block heterogeneity, while both weaker mixing and the stronger `.20` level did not. No tested level produced a directional marginal-risk change. The present model therefore does not support a simple “more connectivity rescues” or “more connectivity destabilises” story.

The operator also has a strict interpretation boundary. It mixes allele frequencies only. Natural pollen flow, seed dispersal, demographic movement, recolonisation and partner movement can act on different state variables and timescales. Empirical plant genetics likewise shows heterogeneous fragmentation responses rather than one universal genetic signature (Miguel-Peñaloza et al. 2023). Peled et al. (2026) further shows that heterogeneous landscape connectivity can generate complex genetic trajectories. Process-resolved movement is therefore a next-model closure, not a relabelling of `m`.

### Interaction architecture remains unresolved beyond the tested reduced forms

The scalar feedback result is robust within its predeclared range, but it says only that `kappa=3–6` did not create a new high-precision incidence or heterogeneity boundary at this anchor. It does not show that interaction support is irrelevant.

The partner-loss replay is even more informative as a negative result. The original low-replicate R4→R3 shift disappeared completely with precision: intact and all three loss architectures had similar incidence and compatible block rates. Yet paired trajectory identity changed often. This means reduced-form partner removal can alter realised stochastic histories without producing a population-level functional-loss effect under the tested closure.

Real networks add partner abundance, topology, coextinction, trait constraints and adaptive rewiring. Experimental and synthetic studies show that compensation is context dependent (Brosi & Briggs 2013; Timóteo et al. 2016; Brosi et al. 2017; Leimberger et al. 2023; Ward et al. 2026). Those mechanisms require a new prospective model. The present negative result is a reason not to inflate the reduced-form layer into a network theorem.

### Genetic warning is downstream of the loss-generating process

The inherited benchmark proves that baseline-relative genetic erosion can precede realised functional loss in one calibrated domain. It does not provide a universal threshold: absolute cut-offs produced both leads and lags, and warning availability differed across recalibrated domains.

The condition-first ordering therefore survives the statistical correction but becomes more precise. Before asking whether a genetic statistic leads loss, establish whether the functional state exists, estimate the incidence of its loss, test whether comparable blocks are exchangeable when that matters, and retain censoring. Only then should lead time and ordering be evaluated. This complements Peled et al. (2026): their warning target is a rapid genetic transition, whereas ours is loss of interaction-supported ecological function.

### Urban and island systems are contrasting routes through a common condition space

The cross-system application is not a city-versus-island equivalence. Urban systems are heterogeneous mosaics in which species presence, co-occurrence and interactions can be filtered even while movement remains substantial (Moreno-García et al. 2025; Hardion et al. 2026; Alaasam et al. 2026). Oceanic islands differ in colonisation history, mutualist availability and reproductive assurance; pollination networks are often smaller and lower in interaction diversity, but no single island attribute governs every network property (Traveset et al. 2016; Pannell et al. 2015; Delavaux et al. 2024).

The common empirical question is whether distinct fragmentation mechanisms converge on similar combinations of functional-state feasibility, realised interaction support, loss incidence and temporal stability. A field design should therefore measure habitat amount/configuration and matrix quality; partner identity and interaction strength; functional diversity, turnover and rewiring; pollen, seed/propagule, demographic and partner movement separately; reproductive assurance; realised function through time; and genetic state through time. Similar regime occupancy would not require similar geography, species composition, network topology or neutral genetic differentiation.

### Limits

The model is finite and its numerical coordinates are not transferable ecological thresholds. The historical R1–R4 labels remain in code and provenance because they governed prospective calibration, but they are not treated as latent biological categories. The high-precision equal-rate tests diagnose block-level rate differences within the tested seed families; failure to detect heterogeneity is not a theorem of universal homogeneity.

The partner layer does not simulate explicit network topology or partner demography. Biological movement is not represented by the allele-frequency mixing operator. Warning succeeds only in the inherited calibrated benchmark; condition-recovery campaigns withheld warning outcomes. Protocol 003 compares non-matched calibrated domains, so its contrast cannot identify a direction-only causal effect.

Finally, censoring and source feasibility remain part of the ecological outcome. Source failure and baseline ineligibility are not silently discarded when reporting warning availability, and finite-horizon non-events remain right-censored.

## Data and code availability

The parent and extension repositories are separate computational provenance units. The extension pins the parent scientific state at `dd8ee379d0d3518194c767d16402042525bc00dc`. Machine-readable evidence, workflow/artifact provenance, condition ledgers and submission-build instructions are recorded in the repository. Historical low-replicate results are retained unchanged; high-precision replays are additive validation layers and do not overwrite their provenance.
