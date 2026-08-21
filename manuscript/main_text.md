# Functional-loss distributions govern when genetic early warning can be validated

## Abstract

Habitat fragmentation can leave populations present while ecological function weakens, but genetic warning is interpretable only if the loss process it predicts is estimable. In a finite eco-genetic model, fragmentation reduced interaction, local effective size and realised high-trait mass. Warning-blind experiments showed that recurrent turnover, genetic connectivity and partner loss reshuffled functional-loss histories; mean incidence and among-block reproducibility separated. Explicit rewiring restored network connectance and interaction support without restoring loss reproducibility. A pollen-gene-flow closure showed exact equivalence between regional pollen contribution g and global allele mixing m=g/2, while pollen kernels changed individual histories but not mean risk. Crucially, an all-block R4 calibration gate changed across independent seed panels at one fixed condition, revealing sampling-design dependence. Genetic erosion preceded loss in one calibrated benchmark, but not by a universal threshold. Genetic early warning is therefore downstream of the distribution of functional-loss events, not a property of genetic diversity alone.

## Introduction

Ecological function can disappear before the population carrying it disappears. A species may remain numerically present while becoming ineffective as a pollinator, seed disperser, mutualist or other ecological actor (Soulé et al. 2005; McConkey & Drake 2006; Valiente-Banuet et al. 2015). Conservation monitoring therefore has to separate population persistence, realised ecological function, interaction state and genetic state rather than treating them as interchangeable indicators.

Habitat fragmentation is a natural setting in which those quantities can decouple. Fragmentation changes habitat amount, spatial configuration and matrix quality, with consequences for demography, dispersal, interactions, gene flow and eco-evolutionary feedbacks (Legrand et al. 2017; Govaert et al. 2019; Benitez et al. 2025; Fletcher et al. 2026). It also need not produce one monotone ecological-network response. Partner identity, functional diversity, interaction strength and rewiring can matter beyond species counts or connectance (Brosi & Briggs 2013; Hiraiwa & Ushimaru 2024; Domínguez-Garcia et al. 2024; Ward et al. 2026). We therefore use **interaction-mediated functional fragmentation** for loss or destabilisation of the biotic support required to maintain a realised function while habitat patches or focal populations may remain present. This is distinct from the established landscape-ecology concept of functional connectivity.

Genetic monitoring adds another layer. Genetic diversity, effective size and differentiation can respond to deterioration, but their relationship to ecological function is context dependent (Schwartz et al. 2007; Hughes et al. 2008; Whitlock 2014; Stange et al. 2021). Recent work has also shown that fragmentation networks can generate early-warning signals before rapid genetic transitions (Peled et al. 2026). Our endpoint is different: we ask whether genetic change can warn of **interaction-dependent functional-trait loss**. That question requires an upstream condition that is often implicit. The loss process itself must occur often enough, and reproducibly enough across comparable stochastic contexts, for warning availability and timing to be meaningfully estimated.

Early-warning theory already cautions that signal reliability depends on transition mechanism, state-variable choice, sampling design and stochasticity (Hastings & Wysham 2010; Boettiger & Hastings 2012, 2013; Gsell et al. 2016). We therefore use a condition-first design (Figure 1). First, can an interaction-supported high-function state exist and be disrupted by fragmentation? Second, how do recurrent state turnover, genetic connectivity and interaction processes change the distribution of functional-loss outcomes? Third, once that loss process has been characterised independently of warning values, can genetic erosion precede loss? Fourth, is warning behaviour portable across independently calibrated eco-genetic domains?

Our calibration initially used a conservative finite-panel certificate, R4: every seed block in a five-block panel had to show an observed loss rate between 0.30 and 0.70. R4 was never defined as warning success. A later prospective stability audit revealed an additional distinction: an all-block certificate can itself depend on which finite seed ensemble is sampled. We therefore retain R4 as a transparent historical opening rule, but treat **central loss incidence and among-block heterogeneity/tail behaviour** as the primary biological estimands.

## Model and methods

### Condition-first architecture

The study uses two computational provenance units. The parent repository supplies the theorem-guided interaction mechanism, paired fragmentation experiment and an inherited symmetric warning benchmark. The extension reconstructs high-function sources under recurrent state transitions, maps functional-loss outcomes, tests connectivity and interaction conditions, introduces explicit partner rewiring and pollen-mediated gene flow, and audits the sampling stability of the finite calibration certificate. Parent and extension trajectories are never pooled. Extension analyses use parent scientific commit `dd8ee379d0d3518194c767d16402042525bc00dc`.

All source and loss analyses are warning-blind. Genetic diversity, warning times and lead/lag outcomes are unavailable while the ecological candidate family is selected or classified.

### Interaction-supported function and fragmentation

The finite multipatch model records population size, local effective size, interaction state, a high-trait-associated allele and realised trait-bin occupancy. Potential high-trait viability, realised high-trait occupancy, allele persistence and genetic diversity are distinct outputs.

The parent fragmentation experiment projected the same H1-prepared full state either to one large patch or to equal isolated fragments at fixed total area. A fresh sensitivity subsequently projected independently prepared sources across 1, 2, 3, 4, 6, 8, 12 and 16 equal isolated patches.

### Recurrent state turnover and finite loss calibration

For high-associated allele frequency \(p\), the extension uses

\[
M(p)=\kappa_\mu p_\mu^*+(1-\kappa_\mu)p.
\]

`kappa_mu` controls relaxation strength and `p_star` the transition equilibrium/direction; `p_star` is not an empirical mutation-rate estimate.

Source reconstruction crossed 15 recurrent-transition coordinates with ecological source conditions. The common deterioration family used a 30-generation ramp followed by a hold and recorded realised post-baseline functional-trait loss only.

Historically, a five-seed candidate received R1 when every seed-block loss rate was below 0.30, R2 when every rate was above 0.70, R4 when every rate was inside `[0.30,0.70]`, and R3 otherwise. A coordinate without an R4 candidate was `no_domain_selected`. Later high-rep work prospectively refined one warning-blind frontier without inspecting genetic-warning variables.

### Connectivity, interaction support and partner loss

At the recovered anchor (`A_ref=1`, interaction `kappa=4.5`, `kappa_mu=.35`, `p_star=.35`, four equal patches, horizon 120, barrier increase .30), Phase E paired prepared sources across allele-frequency mixing `m=0,.025,.05,.10,.20`. The operator mixes selected allele frequencies toward the census-weighted metapopulation mean. It is **not demographic migration**, pollen, seed, pollinator or recolonisation movement.

Phase F varied only the pre-existing aggregate interaction-feedback values `kappa=3,4.5,6`, reconstructing sources independently at each level. `interaction kappa` is **not partner richness, connectance, pollinator diversity or network dimensionality**.

Phase G introduced a reduced-form four-partner representation. The intact condition retained four partners. Three loss architectures removed one balanced partner and were matched for the same richness change and mean retained support while differing in contribution concentration. A prospective stop rule prohibited tuning partner weights after outcomes were observed.

### Explicit rewiring

Phase H represented six candidate partners, four initially active edges and two latent edges. The same balanced primary partner was removed in both loss conditions. One fixed rewiring rule reallocated 50% of lost interaction effort over ten generations according to trait-match score multiplied by spare edge capacity. Edge strength, active-edge count, realised connectance and match-weighted interaction support were explicit diagnostics.

The preregistered opening required a fresh intact R4 certificate and a matched no-rewiring R3 certificate. Rewiring was considered a finite certificate rescue only if it returned the same fresh loss panel to R4. Rewiring strength, edge capacities, partner scores and loss identity were not tuned after the result.

### Pollen-mediated movement

Phase I separated one biological movement process from generic allele mixing. If a fraction \(g\) of paternal contribution comes from a pollen pool, while maternal contribution remains local, offspring allele frequency is

\[
p_{\rm off}=(1-g/2)p_{\rm local}+(g/2)p_{\rm pool}.
\]

For a census-weighted regional pollen pool this is exactly legacy global mixing with `m=g/2`. We fixed `g=.20`, hence the implementation comparator `m=.10`, and required trajectory-exact equality before interpreting the pollen-kernel comparison. A regional pollen pool was then compared once with a ring kernel restricted to two neighbouring donor patches at the same `g`.

### Classification-stability audit

Phase E and Phase I gave different finite R3/R4 labels for the same nominal `m=.10` condition under independent seed/source ensembles. Phase J therefore fixed the complete biological condition and generated 20 new master-seed blocks, each with 20 attempted sources. Before outcomes were generated, the 20 seeds were partitioned into four non-overlapping five-seed panels. Each panel used the unchanged historical R1–R4 rule. No seeds could be replaced or regrouped.

We also recorded the exact design property of the all-block certificate. If a block lies inside the operational incidence band with probability \(q\), an independent \(B\)-block panel passes an all-block rule with probability \(q^B\). Thus, unless `q=0` or `1`, the binary certificate is mechanically panel-size dependent. After the preregistered Phase-J result, we used all 20 block rates only for a labelled secondary combinatorial audit and distributional summary.

### Conditional genetic-warning benchmark and portability

The inherited symmetric benchmark fixed one trait-loss domain without warning values, then introduced fresh validation seeds. Relative warnings were first 5%, 10% or 20% declines of `H_alpha` or `H_gamma` from each trajectory's own baseline. Non-events remained right-censored. Fixed absolute thresholds were audited on the same stored trajectories.

Historical Protocol 003 separately recalibrated two warning-evaluable finite domains and then used fresh seeds. Because those domains differ in recurrent-transition, ecological and deterioration parameters, the comparison tests portability across calibrated eco-genetic domains, **not a single-factor effect of transition direction**. Secondary uncertainty analyses resample complete attempted trajectories; full-denominator event incidence and warning availability are treated as more primary than conditional positive lead-time summaries.

## Results

### Fragmentation disrupted an interaction-supported functional state

Of 1,200 attempted parent replicates, 1,055 met the full-state hold criterion. Every qualified replicate had lower final interaction, local effective size and realised high-trait mass after equal isolation than in its matched one-large projection. Median paired reductions were 99.86% for interaction, 88.73% for local effective size and 68.87% for realised high-trait mass.

The fresh fragmentation gradient recovered **1,037** prepared sources. The first split from one to two isolated patches reduced median interaction by 99.83%, local effective size by 77.87% and realised high-trait mass by 71.71%. Interaction and effective size declined further with fragmentation, whereas realised high-trait mass was not universally monotone (Figure 2A). Functional vulnerability therefore arose before population disappearance.

### Recurrent state turnover changed source feasibility and functional-loss regime

Across **3,375** common-grid source attempts, **2,269** supported preparation/projection; coordinate support ranged from 44.89% to 86.67%. Among 648 complete five-seed deterioration candidates, **322** were rapid-loss, **242** persistence and **84** seed-heterogeneous. None passed the original strict R4 certificate, so all 15 coarse coordinates were historically `no_domain_selected` (Figure 3).

Because calibration was warning-blind, this was not evidence that a genetic warning failed. It showed that the sampled candidate family did not supply a finite validation panel satisfying the predeclared event-incidence rule.

### Warning-blind refinement recovered a narrow reproducible event regime

Prospective refinement showed that **the coarse result was a placement boundary rather than structural impossibility**. `p_star=.35` passed an R4 high-rep panel and independently passed again, whereas immediate tested neighbours `.325` and `.375` were R3 in the replay (Figure 4). This established that finite intermediate-risk panels could be recovered without inspecting warning outcomes.

Phase J later changes the interpretation of “narrow regime”: the C/D results remain valid finite certificates, but the all-block label is not itself a sample-size-invariant biological state.

### Genetic connectivity changed loss-regime reproducibility without a simple rescue sign

In Phase E, pooled loss was **0.571**, .549 and .593 at `m=0,.025,.05`, with finite R4 certificates; at `m=.10,.20`, pooled loss was .626 and .604 and the five-seed panels were R3 because one seed block exceeded .70. Paired loss status switched in both directions, with 21/91 and 25/91 switches at `m=.10` and `.20`, respectively (Figure 5).

The bidirectional trajectory effect is robust. The categorical boundary is not: Phase I's independent `m=.10` comparator later passed R4, and Phase J directly confirmed ensemble sensitivity at fixed `m=.10`.

### Aggregate interaction support changed source eligibility but not the R4 classification

Phase F produced **77/100**, **94/100** and **87/100** baseline-eligible sources at `kappa=3,4.5,6`. Pooled loss was **0.468**, **0.521** and **0.552**, and all 15 seed-block rates were inside the operational band. **All three levels were therefore R4-highrep** in that finite campaign.

This is a **bounded negative condition result** separating source establishment from the subsequent loss distribution. It does not show that interaction support is irrelevant or that `kappa` represents network simplification. **The kappa search was closed rather than widened to manufacture a boundary.**

### Partner loss altered reproducibility more than mean risk

The Phase-G intact control had 49/90 losses (pooled .544) and passed R4. Even, graded and dominant one-partner-loss conditions had pooled loss .567, .556 and .578, respectively, but broader seed-rate ranges and R3 finite certificates. Paired loss status changed in both directions, while a labelled secondary paired-incidence audit found no evidence of a mean-risk difference (Cochran Q, `p=.943`).

Thus the main change was not a monotone rise in average failure probability. The perturbation changed the distribution of stochastic histories across blocks. Contribution concentration itself did not separate the three loss architectures.

### Explicit rewiring recovered network structure but not the loss distribution

The Phase-H opening succeeded: fresh intact passed R4 and matched partner loss without rewiring was R3. Constrained rewiring increased active edges from 3 to 5, realised connectance from .500 to .833, activated both latent edges and increased final network-derived support from .750 to .844 of intact support. Yet pooled functional loss changed only from .430 to .419, only one of 86 comparable trajectories changed from loss to no loss, and the rewiring panel remained R3.

Network recovery was therefore real but insufficient to restore the downstream loss distribution under this fixed closure. Connectance or aggregate support cannot be used alone as proxies for functional-regime recovery.

### Pollen movement exposed a narrow mechanistic equivalence but no kernel-level certificate change

At `g=.20`, the regional pollen closure and legacy `m=.10` comparator were snapshot-exact in all 90 completed pairs, verifying the analytical `m=g/2` identity for this specific paternal-gene-flow process.

No pollen, regional pollen, legacy `m=.10` and ring pollen had pooled loss .511, .500, .500 and .511; all four finite panels passed R4. Regional versus ring pollen nevertheless switched 7 trajectories from loss to no loss and 8 in the opposite direction. Spatial pollen kernel therefore reorganised individual stochastic histories without changing mean incidence or the finite certificate in this campaign.

### The finite R4 certificate was ensemble-sensitive at a fixed condition

Phase J held `m=.10` and every other biological condition fixed. Its four prospectively fixed panels classified **R4, R3, R4 and R4**. Across all 20 blocks, **19** observed loss rates were inside `[.30,.70]`, none were below, and one was `.750`. Mean block loss was .525 and median .513.

The secondary all-combinations audit made the design dependence explicit. Of all **15,504** possible five-block panels from these 20 rates, **11,628 (75%)** excluded the single failing block and passed R4; **3,876 (25%)** included it and were R3. The observed block-pass fraction was .95 (95% Wilson interval .764–.991), giving a plug-in independent five-block pass propensity of .774.

Therefore R4 is best interpreted as a conservative **finite-panel calibration certificate**, not a sample-size-invariant biological regime. The primary loss-process description is distributional: pooled incidence was 180/342=.526, unweighted mean block incidence .525, median .513 and block-rate SD .118.

### Genetic erosion could precede functional loss, but not by a universal absolute threshold

In the inherited symmetric benchmark, 83/100 trajectories were available after source preparation/projection and 35 experienced post-baseline realised functional loss. At each of six baseline-relative `H_alpha`/`H_gamma` endpoints, genetic erosion preceded all 35 observed losses. Fixed absolute thresholds were not robust: `H_alpha<=.20` produced 14 leads and 6 lags; `H_gamma<=.20` produced 8 leads and 8 lags (Figure 2B).

This remains a bounded proof that genetic warning can exist once an appropriate loss process and warning definition are fixed. It does not establish that warning succeeds throughout R4.

### Warning behaviour was not fully portable across independently calibrated domains

Protocol 003 attempted 100 fresh trajectories in each of two separately calibrated domains. Valid-pair availability was **0.540** versus **0.335**; aggregate lead/tie/lag counts were 323/1/0 versus 184/5/12. Conditional positive lead-time medians differed in generations, but only two of six direct absolute timing intervals excluded zero, and **all six direct timing-difference intervals included zero** after horizon normalization. Because the domains also differ in ecological parameters and deterioration schedules, this is bounded portability evidence and **not a single-factor effect of transition direction** (Figure 6).

## Discussion

### Functional fragmentation is a process, not a map pattern

The fragmentation experiment shows why persistence and function must be separated. Dividing the same prepared state sharply reduced interaction, effective size and realised high-trait mass while focal populations remained present. In nature, habitat amount, configuration, matrix quality and partner communities can contribute through different pathways. The appropriate empirical question is therefore whether structural fragmentation disrupts the interaction process maintaining function, not whether a landscape crosses one geometric threshold.

### Mean failure risk, heterogeneity and a validation certificate are distinct

The extension repeatedly separated average risk from the distribution of stochastic outcomes. Phase G changed among-block variability much more than pooled incidence. Phase H restored network structure without restoring the downstream loss panel. Phase I changed individual histories without changing the certificate. Phase J then showed directly that an all-block R4 label can change across independent panels at one fixed biological condition.

This requires a methodological correction. The earlier R4 gate remains useful operationally: a warning-validation analysis needs enough losses and non-losses in the finite panel it will analyse. But an “all five blocks inside the band” rule cannot define a sample-size-invariant biological regime because its pass probability is `q^B`. Biological inference should instead report where the functional-loss distribution is centred and how heterogeneous its tails are. A finite R4 certificate is downstream of those estimands and should always carry its panel design.

This interpretation aligns with early-warning theory's emphasis on error rates, stochasticity and observation design rather than deterministic indicator thresholds (Boettiger & Hastings 2012; Gsell et al. 2016).

### Network recovery is not equivalent to functional recovery

Phase H adds a particularly useful ecological result. The rewiring rule increased connectance and match-weighted interaction support substantially, yet the realised loss distribution scarcely changed. This does not imply that rewiring is generally ineffective. It shows that a structurally “recovered” network can still occupy a different dynamical state from one whose downstream function is reliably restored.

That distinction matters for restoration monitoring. Partner richness, connectance, visitation and even aggregate interaction support are informative state variables, but none is automatically a functional endpoint. Functional diversity, interaction identity and realised service should be measured directly where possible (Hiraiwa & Ushimaru 2024; Ward et al. 2026).

### Biological connectivity must be process resolved

Phase I provides an exact bridge and an equally important boundary. Regional paternal pollen flow at fraction `g` can be mathematically equivalent to global allele mixing `m=g/2` under one random-mating closure, but changing the pollen kernel breaks that identity. Pollen, seed/propagule, demographic and partner movement therefore should not be collapsed into a generic connectivity parameter.

The fixed regional-versus-ring comparison changed trajectory identities but not the loss distribution enough to change the finite certificate. Further pollen fractions were not searched because the negative result answers the preregistered question. Seed, demographic and partner movement remain genuinely different future closures.

### Genetic warning is downstream of an estimable loss distribution

The inherited benchmark demonstrates that baseline-relative genetic erosion can precede interaction-dependent functional loss. Phase J clarifies what must come before that claim. The analyst first needs an independently characterised distribution of functional-loss events; only then can a finite sampling design be certified as suitable for warning validation.

This distinction also sharpens novelty relative to genetic EWS under landscape fragmentation. The contribution is not that genetic signals can precede genetic transitions. It is the ordering of a different problem: interaction-supported function → distribution of functional loss → finite validation design → genetic-warning availability/timing.

### Urban and island systems provide contrasting empirical routes

Cities and islands are not ecological equivalents. Urban mosaics can combine strong structural fragmentation with corridors, human-mediated movement and continued gene flow while heat, pollution, management and partner turnover alter local interactions. Oceanic islands combine geographic isolation with colonisation filters, mutualist availability, stepping-stone connectivity and reproductive assurance.

The model suggests comparing them through a shared measurement architecture rather than a habitat label: habitat amount/configuration and matrix quality; partner identity and interaction strength; functional diversity and rewiring; pollen, seed, demographic and partner movement; realised function through time; block-to-block or year-to-year loss heterogeneity; and genetic state.

The prospective convergence question is therefore whether different mechanisms produce similar **functional-loss distributions**, not whether urban and island systems share the same network topology, genetic differentiation or binary R4 label. Phase H further predicts that apparent network recovery may not imply recovery of functional-loss dynamics.

### Limits

All simulations are finite and model-specific. The operational `[.30,.70]` incidence band is not a universal ecological threshold. Phase J demonstrates that its all-block use is sampling-design dependent. Phase H represents one focal network and one fixed rewiring rule; partner population dynamics and endogenous coextinction remain absent. Phase I represents paternal pollen contribution only. The current model does not yet move seeds, census individuals or interaction partners.

The warning benchmark remains a proof of possibility in one calibrated domain, and Protocol 003 is a bounded portability comparison across non-matched domains. Neither supports a universal genetic threshold.

## Conclusion

Fragmentation can weaken interaction-supported function before population disappearance, but the downstream consequences cannot be summarised by a single state variable. Recurrent turnover, connectivity and partner processes changed source feasibility, individual loss histories and among-block variability; explicit rewiring restored network structure without restoring the functional-loss process, and pollen-kernel changes reshuffled trajectories without a categorical regime shift.

The central methodological result is that **warning estimability is distributional**. Mean functional-loss incidence, among-block heterogeneity and tail behaviour are biological properties of the event-generating process; the historical R4 rule is only a finite-panel calibration certificate whose outcome depends on sampling design. Genetic early warning becomes interpretable only downstream of that event distribution.

This yields a direct empirical programme for urban and island systems: measure structural fragmentation, interaction structure, process-resolved connectivity, realised function and its variability separately, and ask whether different causal routes converge on similar functional-loss distributions before evaluating genetic warning.

## Data and code availability

The mechanistic parent and condition-recovery extension are maintained as separate versioned repositories. The extension pins parent scientific commit `dd8ee379d0d3518194c767d16402042525bc00dc`. Locked machine-readable summaries include Phase E connectivity, Phase F aggregate support, Phase G partner loss, Phase H explicit rewiring, Phase I pollen movement and Phase J classification stability. Phase-H run/artifact are `32453377127` / `9436467391`; Phase-I `32454142670` / `9436762723`; Phase-J `32454874360` / `9437232755`. Exact digests and interpretation boundaries are recorded in the artifact and claim-evidence ledgers.

## References

Benitez, L.M., Parr, C.L., Sankaran, M. & Ryan, C.M. (2025). Fragmentation in patchy ecosystems: a call for a functional approach. *Trends in Ecology & Evolution*, 40, 27–36. doi:10.1016/j.tree.2024.09.004

Boettiger, C. & Hastings, A. (2012). Quantifying limits to detection of early warning for critical transitions. *Journal of the Royal Society Interface*, 9, 2527–2539. doi:10.1098/rsif.2012.0125

Boettiger, C. & Hastings, A. (2013). No early warning signals for stochastic transitions: insights from large deviation theory. *Proceedings of the Royal Society B*, 280, 20131372. doi:10.1098/rspb.2013.1372

Brosi, B.J. & Briggs, H.M. (2013). Single pollinator species losses reduce floral fidelity and plant reproductive function. *Proceedings of the National Academy of Sciences USA*, 110, 13044–13048. doi:10.1073/pnas.1307438110

Domínguez-Garcia, V., Molina, F.P., Godoy, O. & Bartomeus, I. (2024). Interaction network structure explains species' temporal persistence in empirical plant–pollinator communities. *Nature Ecology & Evolution*, 8, 423–429. doi:10.1038/s41559-023-02314-3

Fletcher, R.J. Jr., Smith, T.A.H., Jones, M., et al. (2026). Landscape quality drives ecological responses to habitat loss and fragmentation. *Nature Ecology & Evolution*, 10, 1265–1272. doi:10.1038/s41559-026-03095-1

Govaert, L., Fronhofer, E.A., Lion, S., et al. (2019). Eco-evolutionary feedbacks—Theoretical models and perspectives. *Functional Ecology*, 33, 13–30. doi:10.1111/1365-2435.13241

Gsell, A.S., Scharfenberger, U., Özkundakci, D., et al. (2016). Evaluating early-warning indicators of critical transitions in natural aquatic ecosystems. *Proceedings of the National Academy of Sciences USA*, 113, E8089–E8095. doi:10.1073/pnas.1608242113

Hastings, A. & Wysham, D.B. (2010). Regime shifts in ecological systems can occur with no warning. *Ecology Letters*, 13, 464–472. doi:10.1111/j.1461-0248.2010.01439.x

Hiraiwa, M.K. & Ushimaru, A. (2024). Loss of functional diversity rather than species diversity of pollinators decreases community-wide trait matching and pollination function. *Functional Ecology*, 38, 1296–1308. doi:10.1111/1365-2435.14527

Hughes, A.R., Inouye, B.D., Johnson, M.T.J., Underwood, N. & Vellend, M. (2008). Ecological consequences of genetic diversity. *Ecology Letters*, 11, 609–623. doi:10.1111/j.1461-0248.2008.01179.x

Legrand, D., Cote, J., Fronhofer, E.A., et al. (2017). Eco-evolutionary dynamics in fragmented landscapes. *Ecography*, 40, 9–25. doi:10.1111/ecog.02537

McConkey, K.R. & Drake, D.R. (2006). Flying foxes cease to function as seed dispersers long before they become rare. *Ecology*, 87, 271–276. doi:10.1890/05-0386

Peled, O., Kim, J. & Greenbaum, G. (2026). Network-based genetic monitoring of landscape fragmentation. *Proceedings of the National Academy of Sciences USA*, 123, e2515033123. doi:10.1073/pnas.2515033123

Schwartz, M.K., Luikart, G. & Waples, R.S. (2007). Genetic monitoring as a promising tool for conservation and management. *Trends in Ecology & Evolution*, 22, 25–33. doi:10.1016/j.tree.2006.08.009

Soulé, M.E., Estes, J.A., Miller, B. & Honnold, D.L. (2005). Strongly interacting species: conservation policy, management, and ethics. *BioScience*, 55, 168–176.

Stange, M., Barrett, R.D.H. & Hendry, A.P. (2021). The importance of genomic variation for biodiversity, ecosystems and people. *Nature Reviews Genetics*, 22, 89–105. doi:10.1038/s41576-020-00288-7

Valiente-Banuet, A., Aizen, M.A., Alcántara, J.M., et al. (2015). Beyond species loss: the extinction of ecological interactions in a changing world. *Functional Ecology*, 29, 299–307. doi:10.1111/1365-2435.12356

Ward, C.A., Tunney, T.D., Hale, K.R.S., et al. (2026). The rewiring of ecological networks in a variable world. *Nature Reviews Biodiversity*, 2, 355–369. doi:10.1038/s44358-026-00159-9

Whitlock, R. (2014). Relationships between adaptive and neutral genetic diversity and ecological structure and functioning: a meta-analysis. *Journal of Ecology*, 102, 857–872. doi:10.1111/1365-2745.12240
