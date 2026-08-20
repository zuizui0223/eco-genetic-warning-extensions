# Ecological grounding for the warning-evaluability storyline

## Purpose

This note separates what is already well established in ecology from what the present finite eco-genetic study adds. It is a manuscript-planning source, not a new empirical result.

## 1. What ecology already supports

### 1.1 Ecological function can be lost before population rarity or extinction

Interaction-dependent ecological function need not track population persistence monotonically. McConkey & Drake (2006) showed a nonlinear abundance–function relationship in flying fox seed dispersal: dispersal effectiveness collapsed below a density threshold while the animals were still present. More generally, the loss of ecological interactions can precede taxonomic extinction.

This supports the biological endpoint used here: realised functional-trait loss is not interchangeable with population extinction.

### 1.2 Early-warning signals are not expected to be universal across transition mechanisms

Classical early-warning theory identifies generic signatures for particular classes of critical transition, but later work established important limits. Hastings & Wysham (2010) showed that ecological regime shifts can occur without warning, and Boettiger & Hastings (2012, 2013) quantified detection limits and showed that stochastic transitions need not produce classical early-warning signals.

Empirical synthesis points in the same direction. Gsell et al. (2016) found that early-warning indicators in natural aquatic ecosystems were inconsistent and stressed that a priori knowledge of transition-generating mechanisms is required to choose relevant state variables. More recent multi-lake work likewise found that different trophic levels can exhibit different transition types and that many observed regime shifts do not satisfy the assumptions under which classical critical-transition EWS are expected.

This supports the paper's decision to treat the event-generating mechanism and loss regime as upstream of warning performance.

### 1.3 Monitoring performance depends on observation design as well as biology

Early-warning detection depends on the state variable measured, sampling regime, signal-to-noise ratio, time-series length and the transition mechanism. Experimental reviews report substantial false-positive/false-negative problems and emphasize that sampling should be tailored to monitoring objectives.

This supports retaining censoring, baseline eligibility and warning availability in the denominator rather than treating only observed lead pairs as the warning result.

### 1.4 Genetic diversity is ecologically important, but it is not a context-free proxy for ecological function

Genetic diversity can affect productivity, recovery, interactions, community structure and ecosystem processes (Hughes et al. 2008). However, Whitlock's (2014) meta-analysis showed that the relationship depends on the genetic metric and ecological context: adaptive genotypic diversity had a small positive association with ecological responses, whereas neutral genetic diversity showed no consistent overall association with ecological structure/function.

Thus existing community-genetics evidence already argues against assuming a universal monotone mapping from a generic diversity statistic to ecological function.

## 2. What the present study adds

The novelty should not be stated as "EWS are context dependent" or "genetic diversity and function are not identical." Both are already supported broadly in ecology.

The stronger contribution is an ordered, operational decomposition of the warning problem inside one explicit eco-genetic model:

```text
1. Can the functional source state exist?
2. What loss regime does a common deterioration family generate?
3. Does that regime supply a reproducible intermediate-risk domain in which warning can be evaluated?
4. Only then, how available and how early is the genetic warning?
```

The common recurrent-transition grid provides finite evidence for the first three levels before warning values are inspected:

- source feasibility changes across coordinates;
- loss candidates partition into rapid-loss, persistence and seed-heterogeneous regimes;
- the strict common candidate family yields zero eligible warning-validation domains at all 15 coordinates.

The study therefore promotes **warning evaluability** from an implicit methodological assumption to an explicit eco-genetic outcome of the model closure.

## 3. Novelty boundary

The literature reviewed here already establishes that:

- some ecological transitions have no reliable classical EWS;
- EWS reliability depends on transition mechanism, state-variable choice and sampling;
- ecological function can be lost before population extinction;
- genetic diversity–function relationships vary with genetic metric and ecological context.

The present study should therefore **not** claim to discover any of those points.

The defensible new conceptual step is:

> A genetic warning comparison itself requires a reproducible event-generating regime, and whether that regime exists can be treated as an upstream eco-genetic state-space property rather than assumed by the analyst.

In the present finite closure, recurrent-transition dynamics reorganise both source feasibility and loss-regime structure strongly enough that the predeclared matched warning-validation domain disappears across the complete tested common grid.

This is narrower than a universal theorem about "warning-evaluable regimes." It is an operational finite-model result that suggests a general research program: map the region of ecological/evolutionary parameter space in which a proposed warning is actually identifiable before comparing warning statistics within that region.

## 4. How this grounds the four manuscript questions

### Q1 — How is ecological function maintained and lost under fragmentation?

Grounded by interaction-dependent functional extinction and fragmentation/eco-evolutionary theory. H1 + H3 establish the model-specific mechanism.

### Q2 — Can genetic change precede that functional loss?

Grounded by conservation-genetic monitoring and early-warning theory. The symmetric benchmark supplies a finite proof of possibility, not a universal rule.

### Q3 — Under what eco-genetic regimes is that warning comparison itself evaluable?

Grounded by the established dependence of EWS on transition mechanism and relevant state variables, but made explicit here as a pre-warning calibration/evaluability problem. This is the main conceptual extension.

### Q4 — Why should diversity warning not be expected to transfer monotonically across regimes?

Grounded by community-genetics evidence that diversity–function relationships are context dependent. The exact recurrent-transition Type T identities add a model-specific mechanism: local high-state support and heterozygosity can move in opposite directions.

## 5. Urban ecology application

Urban ecosystems are useful because spatial fragmentation does not imply a single genetic regime. Urban evolutionary-ecology reviews show that cities can reduce population size and connectivity, but also create corridors, repeated introductions, anthropogenic dispersal and novel selection. A quantitative review of urban population genetics found only a weak average reduction in within-population diversity and no consistent increase in between-population differentiation, and a recent plant-focused review reports that urban plants often retain substantial gene flow and diversity despite urban fragmentation.

Urban pollination provides a direct functional endpoint. Urban pollination reviews report an overall negative signal for pollination in cities but strong among-study heterogeneity and difficult-to-predict pollen movement. Thus urban mosaics can plausibly span the model's rapid-loss, persistent, heterogeneous and potentially warning-evaluable regimes.

The model should therefore not map "urbanization" to one parameter. Candidate empirical mappings are:

- green-space area -> patch area;
- roads/impervious matrix -> resistance and effective connectivity;
- green corridors and human/animal-mediated movement -> migration;
- pollinator visitation/network integrity -> interaction support;
- urban heat/pollution/disturbance -> deterioration/selection;
- repeated introduction, biased recruitment or recurrent switching among trait-associated states -> possible analogues of effective state turnover, without treating `p_star` as a mutation rate.

A particularly useful urban prediction is that genetic diversity may remain high through human-mediated movement even while pollination function deteriorates. Such systems would provide an empirical test of the model's support–diversity decoupling.

## 6. Island ecology application

Island systems provide strong gradients in area, isolation, colonization and mutualist availability. Functional island-biogeography theory predicts that pollinator and other mutualist diversity generally declines with island isolation, while generalist pollination, self-compatibility and vegetative reproduction become more common with increasing isolation. Reviews of island plant reproductive biology also emphasize that pollinator availability and breeding system strongly influence colonization and persistence.

Candidate empirical mappings are:

- island area -> patch area/carrying support;
- mainland or source-island distance -> connectivity/colonization pressure;
- stepping-stone archipelago structure -> migration network;
- pollinator/mutualist richness -> interaction support;
- self-compatibility/generalist pollination/vegetative reproduction -> alternative routes to persistence when specialist interaction support is weak;
- bottlenecks and repeated colonization -> starting-state and turnover structure.

This suggests testable regime predictions. Small remote islands with weak mutualist support should be enriched for source-infeasible or rapid functional-loss regimes for specialist/outcrossing systems. Self-compatible or generalized lineages may instead shift toward persistence even after specialist interaction function is weakened. Intermediate area/isolation may be the most plausible location for a warning-evaluable region, but that remains a hypothesis to test rather than an inference from the current simulation.

## 7. Why urban and island systems are complementary

The two applications probe the same framework under contrasting connectivity rules.

```text
islands:
  persistent geographic isolation + colonization/mutualist filters

cities:
  fragmentation + possible corridors + repeated introductions + anthropogenic dispersal
```

This contrast is scientifically useful because similar patchiness can yield different genetic outcomes. Cities are not simply artificial islands, and islands are not simply maximally fragmented cities. The phase-map framework predicts that the same spatial isolation can fall into different functional-loss and warning-evaluability regimes depending on interaction support, effective connectivity and recurrent state turnover.

## 8. References most directly supporting the ecological framing

Core EWS/function/genetics:
- Boettiger, C. & Hastings, A. (2012). Quantifying limits to detection of early warning for critical transitions. *Journal of the Royal Society Interface*, 9, 2527–2539. doi:10.1098/rsif.2012.0125.
- Boettiger, C. & Hastings, A. (2013). No early warning signals for stochastic transitions: insights from large deviation theory. *Proceedings of the Royal Society B*, 280, 20131372. doi:10.1098/rspb.2013.1372.
- Gsell, A.S. et al. (2016). Evaluating early-warning indicators of critical transitions in natural aquatic ecosystems. *Proceedings of the National Academy of Sciences USA*, 113, E8089–E8095. doi:10.1073/pnas.1608242113.
- Hastings, A. & Wysham, D.B. (2010). Regime shifts in ecological systems can occur with no warning. *Ecology Letters*, 13, 464–472. doi:10.1111/j.1461-0248.2010.01439.x.
- Hughes, A.R., Inouye, B.D., Johnson, M.T.J., Underwood, N. & Vellend, M. (2008). Ecological consequences of genetic diversity. *Ecology Letters*, 11, 609–623. doi:10.1111/j.1461-0248.2008.01179.x.
- McConkey, K.R. & Drake, D.R. (2006). Flying foxes cease to function as seed dispersers long before they become rare. *Ecology*, 87, 271–276. doi:10.1890/05-0386.
- Whitlock, R. (2014). Relationships between adaptive and neutral genetic diversity and ecological structure and functioning: a meta-analysis. *Journal of Ecology*, 102, 857–872. doi:10.1111/1365-2745.12240.

Urban:
- Alberti, M. (2015). Eco-evolutionary dynamics in an urbanizing planet. *Trends in Ecology & Evolution*, 30, 114–126. doi:10.1016/j.tree.2014.11.007.
- Rivkin, L.R. et al. (2019). A roadmap for urban evolutionary ecology. *Evolutionary Applications*, 12, 384–398. doi:10.1111/eva.12734.
- Miles, L.S. et al. (2019). Gene flow and genetic drift in urban environments. *Molecular Ecology*, 28, 4138–4151. doi:10.1111/mec.15221.
- Youngsteadt, E. & Keighron, M.C. (2023). Urban Pollination Ecology. *Annual Review of Ecology, Evolution, and Systematics*, 54, 21–42. doi:10.1146/annurev-ecolsys-102221-044616.

Islands:
- Schrader, J. et al. (2021). A roadmap to plant functional island biogeography. *Biological Reviews*. doi:10.1111/brv.12782.
- Traveset, A. et al. (2018). Plant reproductive ecology and evolution in the Mediterranean islands: state of the art. *Plant Biology*. doi:10.1111/plb.12636.
- Whittaker, R.J. et al. (2017). Island biogeography: taking the long view of nature's laboratories. *Science*.
