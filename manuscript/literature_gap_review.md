# Literature review: eco-genetic warning before functional-trait loss

## Review purpose

This document positions the integrated manuscript spanning `eco-genetic-criticality` and `eco-genetic-warning-extensions`. It is a structured scoping review, not a formal PRISMA systematic review. The aim is to identify the nearest intellectual neighbours, distinguish inherited ideas from new contributions, and define defensible ecological claims.

## The six relevant literatures

### 1. Ecological early-warning signals and critical transitions

The modern early-warning literature established that systems approaching some bifurcation-driven transitions may exhibit critical slowing down, rising autocorrelation, variance, altered recovery rates, spatial correlation, flickering, or related changes. Foundational works include Scheffer et al. (2009), Drake and Griffen (2010), Carpenter et al. (2011), and the synthesis by Scheffer et al. (2012). These studies made two major contributions relevant here: they framed advance detection as a dynamical-systems problem, and they emphasized the management value of warning time before an undesirable transition.

This literature also established strong limitations. Hastings and Wysham (2010) showed that regime shifts need not provide generic warning. Boettiger and Hastings (2012, 2013) demonstrated detection limits, false positives, selection bias, and the need for controls, replicates, explicit error rates, and mechanistically appropriate indicators. Consequently, the strongest contemporary claim is not that universal indicators exist, but that warning performance is conditional on transition mechanism, observable, noise process, sampling design, and event definition.

**What this field usually monitors:** abundance, biomass, system state, variance, autocorrelation, recovery rate, spatial pattern, or multivariate state summaries.

**What it rarely asks:** whether a genetic variable precedes loss of a realised ecological function while the population and alleles may still persist; whether the genetic life-cycle closure changes the existence of an evaluable event regime; or whether mutation direction changes warning availability, ordering, and usable lead time.

### 2. Genetic monitoring and conservation genomics

Genetic monitoring has developed into a mature conservation toolkit for tracking effective population size, heterozygosity, allelic diversity, inbreeding, connectivity, introgression, demographic decline, and management response. Schwartz, Luikart and Waples (2007) formalized genetic monitoring as a conservation framework. Allendorf, Hohenlohe and Luikart (2010), Stange, Barrett and Hendry (2021), Hogg et al. (2024), and related conservation-genomics work expanded this agenda to genome-wide variation and practical management.

Policy relevance has increased because genetic composition is now recognized alongside species and ecosystem dimensions in global biodiversity monitoring. Recent global synthesis indicates widespread temporal erosion of within-population genetic diversity, while also showing that targeted management can maintain or restore it.

However, most genetic-monitoring studies are retrospective or diagnostic. They ask whether genetic diversity declined, whether `N_e` is small, whether connectivity was lost, or whether intervention improved genetic health. They generally do not estimate a same-trajectory time ordering between a genetic threshold and a later ecological-function threshold under controlled deterioration. Genetic diversity is therefore commonly treated as a state variable or risk correlate, not as a formally calibrated early-warning endpoint with lead, tie, lag, censoring, and usable intervention time.

**Nearest overlap with this study:** temporal genetic erosion, genetic indicators for management, and the distinction between census abundance and effective population size.

**Remaining gap:** an explicit event-pair framework asking whether genetic diversity erosion precedes realised functional-trait loss, with non-events retained as censored and warning calibration independent of warning outcomes.

### 3. Habitat fragmentation and eco-evolutionary feedback

Fragmentation research has long shown that habitat loss and isolation can reduce local population size, alter dispersal and interactions, increase drift and inbreeding, and change selection. Landscape genetics documents how connectivity and spatial structure shape genetic variation. Eco-evolutionary theory further shows that dispersal, local adaptation, density dependence, frequency dependence, and species interactions can feed back across ecological and evolutionary timescales. Key syntheses include Legrand et al. (2017) on fragmented landscapes and Govaert et al. (2019) on eco-evolutionary feedbacks.

A recurring result is that connectivity is not uniformly beneficial. Migration may rescue small populations, restore variation, or recolonize empty patches, but it may also impose migration load, erode local adaptation, or destabilize interactions. This conditionality is directly aligned with the predecessor model's separation of migration rescue and migration erosion.

Yet fragmentation and landscape-genetic models usually focus on persistence, adaptation, genetic structure, abundance, or extinction probability. They rarely connect the following complete causal sequence within one finite model:

`patch area -> interaction intensity -> high-trait-state stability -> local effective size -> genetic diversity -> realised functional-trait loss`.

They also rarely evaluate how the direction of recurrent allelic or state transitions changes the reliability of a genetic warning along that sequence.

### 4. Functional extinction and loss of ecological interactions

Conservation biology distinguishes numerical persistence from ecological effectiveness. A species may remain present but become too rare, behaviourally altered, or spatially constrained to perform its historical ecological function. Classic examples include flying foxes ceasing to disperse large seeds effectively before becoming numerically rare, strongly interacting species losing community effects below ecologically effective densities, and defaunation causing interaction and trait change before taxonomic extinction.

Relevant work includes Estes et al. (1989) on ecological extinction, Soulé et al. (2005) on strongly interacting species, McConkey and Drake (2006) on seed-dispersal thresholds, Galetti et al. (2013) on evolutionary consequences of functional extinction, and Valiente-Banuet et al. (2015) on the extinction of ecological interactions.

This literature provides the ecological reason the endpoint in the present study matters. Population presence, allele persistence, and ecosystem function are not interchangeable. Monitoring only abundance or species occurrence can miss an earlier loss of pollination, seed dispersal, mutualism, defence, nutrient cycling, or another interaction-dependent trait.

**Gap:** functional-extinction studies rarely incorporate finite population genetics or ask whether genetic erosion supplies actionable warning before realised interaction-dependent trait loss.

### 5. Evolutionary rescue, genetic rescue, and adaptation under deterioration

Evolutionary-rescue theory asks when heritable change prevents extinction under environmental deterioration. Foundational contributions include Gomulkiewicz and Holt (1995), Bell and Gonzalez (2009), Gonzalez et al. (2013), Carlson et al. (2014), Alexander et al. (2014), and Bell (2017). This literature shows that rescue depends on standing variation, mutation supply, population size, deterioration rate, demographic stochasticity, dispersal, recombination, and the timing of adaptive variants.

Genetic rescue focuses more specifically on gene flow reducing inbreeding depression and restoring fitness, while demographic rescue can occur without adaptive evolution. All three literatures emphasize that intervention outcomes depend on the full demographic and genetic context.

The present study is adjacent to evolutionary rescue but asks a different question. The focal event is not necessarily population extinction. It is loss of realised high-trait occupancy or ecological function. Moreover, the response variable is not only rescue probability but whether a genetic indicator provides warning before that loss, how often valid event pairs exist, and how much usable lead time remains.

**Gap:** rescue theory generally asks whether adaptation prevents extinction, not whether genetic-diversity erosion precedes functional-trait loss or how mutation direction changes warning reliability.

### 6. Mutation bias, arrival bias, and directional state transitions

Mutation-bias research has moved beyond the view that mutation merely supplies undirected raw material. Work by Yampolsky and Stoltzfus, Stoltzfus and McCandlish (2017), Storz et al. (2019), Svensson and Berger (2019), and Cano et al. (2023) debates when biases in the introduction of variation affect adaptive outcomes. The cautious consensus is that mutation bias is not a universal autonomous evolutionary force, but it can shape outcomes through interaction with selection, population size, standing variation, and the supply of alternatives.

Most evidence concerns molecular substitutions, parallel adaptation, resistance evolution, mutational spectra, or accessibility of adaptive changes. The ecological consequences are usually measured as adaptation or persistence, not source feasibility, realised functional-trait loss, calibration feasibility, warning censoring, or lead time.

The effective parameter `p_mu*` in the present model must therefore be described carefully. It is not an empirically estimated mutation rate and does not imply directed adaptive mutation. It represents a directional equilibrium of recurrent transitions between high-trait-associated and low-trait-associated states. The most defensible biological interpretation is broader than nucleotide mutation alone and includes effective recurrent allelic, epigenetic, developmental, or state-transition asymmetry.

**Gap:** mutation-direction theory has not been integrated with fragmentation-driven eco-genetic criticality and formally calibrated genetic warning before functional-trait loss.

## Nearest-neighbour matrix

| Literature | Established result | What is missing relative to this manuscript |
|---|---|---|
| Critical-transition EWS | Some transitions produce advance dynamical signals; reliability is mechanism dependent | Genetic-diversity event timing before functional-trait loss under alternative genetic closures |
| Conservation genetics/genomics | Diversity, `N_e`, inbreeding, and connectivity are monitorable and management relevant | Lead/tie/lag, censoring, and intervention time relative to a realised ecological-function endpoint |
| Fragmentation eco-evolution | Spatial structure changes demography, gene flow, adaptation, and interactions | One causal chain from patch geometry through interaction state and `N_e` to warning and functional loss |
| Functional extinction | Ecological function may disappear before numerical extinction | A finite genetic mechanism and calibrated genetic warning preceding the functional endpoint |
| Evolutionary rescue | Variation supply and adaptation can avert extinction | Warning reliability before functional-trait loss; distinction between persistence and observability of warning |
| Mutation bias | Direction of introduced variation can alter evolutionary outcomes | Consequences for event-regime feasibility, warning availability, ordering, and lead time in fragmented populations |

## The central research gap

The literature lacks a framework that simultaneously:

1. distinguishes potential viability, realised functional-trait occupancy, allele persistence, effective population size, and genetic diversity;
2. links habitat geometry and ecological interaction feedback to those genetic and trait states;
3. treats genetic diversity erosion as a candidate warning event rather than merely a retrospective risk correlate;
4. calibrates deterioration without inspecting warning outcomes;
5. retains non-events and unavailable pairs as censoring rather than discarding them;
6. tests whether directional recurrent mutation or effective state transition changes source feasibility, trait-loss regime, warning availability, lead/lag ordering, and usable lead time.

No single neighbouring literature supplies all six elements. The integrated manuscript's novelty lies in their causal combination, not in claiming that fragmentation, early warnings, genetic monitoring, functional extinction, evolutionary rescue, or mutation bias is individually new.

## Novelty hierarchy

### Primary novelty

**Genetic-warning reliability is shown to be an emergent property of the complete eco-genetic closure.** The same general ecological deterioration can yield a highly reliable leading signal in a symmetric bridge and reduced valid-pair availability, non-zero lags, stronger censoring, and shorter lead time under a directional transition.

### Secondary novelty

**Warning-validation feasibility is treated as a biological result.** Rapid-loss, persistence, and seed-heterogeneous regimes can prevent a common calibration domain from existing. A `no_domain_selected` outcome is retained rather than hidden by post hoc tuning.

### Mechanistic novelty

**Fragmentation and ecological interaction feedback are connected to finite population genetics and realised functional-trait loss.** This makes the warning endpoint ecologically interpretable rather than a generic statistical precursor.

### Methodological novelty

**Calibration and validation are separated by endpoint blindness and independent seed families.** Same-trajectory event pairs, valid denominators, censoring classes, and usable positive lead time are reported explicitly.

### What is not novel

- Critical slowing down and ecological early-warning signals.
- The idea that fragmentation reduces genetic diversity.
- The importance of genetic diversity for conservation.
- Functional extinction before species extinction.
- Evolutionary or genetic rescue.
- Mutation bias affecting evolutionary outcomes.

The paper should cite these as foundations and claim novelty only for the integrated causal and validation framework.

## Ecological significance

### Functional loss can precede population extinction

Conservation actions often trigger when abundance or occupancy becomes critically low. The model instead highlights an earlier ecological endpoint: loss of an interaction-dependent high trait while individuals and alleles may remain. This corresponds to real systems in which pollination, seed dispersal, mutualism, defence, or engineering functions collapse below an effective threshold.

### Genetic monitoring may provide intervention time, but not portably

A relative decline in genetic diversity can provide advance notice of functional loss. However, the amount of time and the probability of observing a valid warning depend on the biological turnover process. Monitoring thresholds should therefore be calibrated to the target species, trait, spatial structure, and genetic or state-transition closure.

### Connectivity and mutation direction have conditional effects

Neither connectivity nor high-trait-directed transition should be presented as universally beneficial. Connectivity can rescue or erode local states; a persistence-favouring transition can preserve function but also produce too few loss events to estimate warning performance. The management problem is therefore not maximising a single variable but identifying the regime in which function, genetic variation, and actionable warning coexist.

### Censoring is ecologically meaningful

A censored trajectory may indicate persistent function, an unobserved warning, insufficient horizon, source failure, or baseline ineligibility. These outcomes represent different ecological and monitoring regimes and should not be collapsed into missing data.

### Relevance to biodiversity policy

Global biodiversity frameworks increasingly recognize genetic composition, population status, traits, ecosystem functions, and connectivity as distinct monitoring dimensions. This study supplies a mechanistic argument for integrating those dimensions: genetic diversity can be informative only when interpreted relative to the ecological function at risk and the biological processes generating or removing adaptive states.

## Defensible manuscript claims

Use:

- Genetic diversity erosion **can** precede realised functional-trait loss.
- Warning reliability is conditional on the declared finite eco-genetic closure.
- Mutation or effective state-transition direction changed warning availability, ordering, censoring, and lead time in two independently calibrated domains.
- A common calibration family produced rapid-loss, persistence, and seed-heterogeneous regimes.
- Monitoring thresholds require biological and system-specific calibration.

Avoid:

- Genetic diversity universally predicts ecological collapse.
- Mutation direction universally causes rescue or collapse.
- `p_mu*` is a measured biological mutation rate.
- The six endpoint counts are independent replicates.
- The integrated simulations prove a universal critical-transition theorem.
- Failure to select a domain means that no ecological warning exists.

## Priority references for the Introduction

1. Scheffer et al. 2009. Early-warning signals for critical transitions. *Nature*.
2. Drake & Griffen 2010. Early warning signals of extinction in deteriorating environments. *Nature*.
3. Carpenter et al. 2011. Early warnings of regime shifts: a whole-ecosystem experiment. *Science*.
4. Hastings & Wysham 2010. Regime shifts in ecological systems can occur with no warning. *Ecology Letters*.
5. Boettiger & Hastings 2012/2013. Detection limits, false positives, and the prosecutor's fallacy in EWS.
6. Schwartz, Luikart & Waples 2007. Genetic monitoring as a promising tool for conservation and management. *TREE*.
7. Allendorf, Hohenlohe & Luikart 2010. Genomics and the future of conservation genetics. *Nature Reviews Genetics*.
8. Legrand et al. 2017. Eco-evolutionary dynamics in fragmented landscapes. *Ecography*.
9. Govaert et al. 2019. Eco-evolutionary feedbacks—models and perspectives. *Functional Ecology*.
10. Valiente-Banuet et al. 2015. Beyond species loss: extinction of ecological interactions in a changing world. *Functional Ecology*.
11. McConkey & Drake 2006. Flying foxes cease to function as seed dispersers long before they become rare. *Ecology*.
12. Bell 2017. Evolutionary rescue. *Annual Review of Ecology, Evolution, and Systematics*.
13. Carlson, Cunningham & Westley 2014. Evolutionary rescue in a changing world. *TREE*.
14. Stoltzfus & McCandlish 2017. Mutational biases influence parallel adaptation. *Molecular Biology and Evolution*.
15. Svensson & Berger 2019. The role of mutation bias in adaptive evolution. *TREE*.
16. Cano et al. 2023. Mutation bias and the predictability of evolution. *Philosophical Transactions B*.

## Literature-driven Introduction logic

1. Ecological functions can be lost before species disappear.
2. Early-warning theory seeks indicators that create intervention time but is not universally portable.
3. Genetic monitoring measures a different layer of biodiversity and could, in principle, warn before realised functional loss.
4. Fragmentation couples interaction state, local `N_e`, genetic diversity, and trait expression.
5. Existing work does not establish whether genetic warning remains reliable when recurrent variation is directionally biased.
6. We therefore test the mechanism, calibration feasibility, and warning reliability across symmetric and directional mutation closures.

## Literature-driven Discussion logic

1. The symmetric benchmark demonstrates that a genetic warning is possible under a declared closure.
2. The phase separation demonstrates that warning evaluation itself depends on the event regime.
3. The directional validation demonstrates that availability, ordering, and lead time are not portable across closures.
4. The result joins early-warning theory to conservation genetics and functional-extinction biology.
5. Management implications concern system-specific calibration and integrated monitoring, not a universal threshold.
6. Limitations include effective rather than empirical mutation parameters, two validation domains, finite Type S evidence, and absence of species-specific data.