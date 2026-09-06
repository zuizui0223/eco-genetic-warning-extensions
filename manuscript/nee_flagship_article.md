# Eco-genetic sorting and buffering shape functional vulnerability under fragmentation

## Abstract

Fragmentation can leave ecological components present while changing the life-cycle processes that keep them functionally coupled. We combine exact results with prospectively locked finite experiments to identify why systems with the same marginal ecological and genetic quantities can reach different futures. A fixed-area fragmentation gradient first separates potential viability, realised occupancy, interaction support, effective size and realised trait mass. At fixed mean support, cross-layer covariance then changes spatial support variance 49-fold and produces exact next-state differences despite identical census, trait, allele-frequency and diversity summaries. Long-horizon interventions reveal the mechanism is not a scalar alignment effect. On fresh seeds an indirect matched-state advantage reappears, but deleting allele-linked recruitment enlarges rather than removes it, showing that recruitment buffers mismatch. Conversely, deleting local ecological selection removes the late matching advantage, while density-to-interaction feedback gates entry into system-wide loss. Functional vulnerability therefore emerges from **selection-mediated sorting opposed by recruitment- and feedback-mediated buffering**, not from component amounts or alignment alone.

Ecological fragmentation changes more than habitat amount. It can alter local demographic support, partner interactions, mating opportunity, movement, trait expression and genetic composition, and those quantities need not respond on the same schedule. The central ecological problem is therefore not simply how much of each component remains, but how the components required for a focal function are organized and coupled through the life cycle.

Numerical persistence can consequently conceal functional vulnerability. Ecological interactions may become ineffective before species disappear; movement or behavioural reorganization can sometimes compensate local resource loss; and standing genetic summaries can retain historical information after contemporary interaction or mating processes have changed. These possibilities suggest that fragmentation may change not only component abundance but the **pathways that sort, replenish and reconnect functional state**.

Existing theory provides pieces of this problem. Critical-transition theory formalizes nonlinear state changes; eco-evolutionary theory in fragmented landscapes couples demography, dispersal, selection and inheritance; multilayer ecology shows that interlayer organization can matter beyond layer-wise summaries; and forecasting theory emphasizes explicit targets and horizons. A less explicit mechanistic question is: **when two systems retain the same marginal ecological and genetic quantities, which life-cycle processes make their futures diverge or converge again?**

Natural systems motivate that question without serving as validation data for the finite model developed here. Urban *Crepis sancta* illustrates local interaction limitation that wider movement does not fully rescue. On Miyake-jima, reduced floral resources can instead be accompanied by broader *Zosterops* movement and pollen mixing that compensate pollination. In fragmented *Conospermum undulatum*, current pollen connectivity can deteriorate while adult neutral genetics retain an older landscape signature. These contrasting routes motivate a distinction among sorting, buffering and memory rather than a universal `urban`, `island` or `fragmented` state.

We test the mechanism in four stages. First, we ask whether one fragmentation gradient generates one biological deterioration coordinate. Second, we formalize transition sufficiency and identify the exact source of an immediate matched-marginal transition difference. Third, through two prospectively locked intervention programmes, we separate trait–allele organization, direct interaction feedback and individual life-cycle edges to identify why relational differences propagate or are buffered. Fourth, we ask whether an early marginal diversity response identifies functional fate once the full event and non-event denominator is restored. Natural examples enter only after these tests, as ecological projections rather than external validation.

## Results

### Fragmentation separated functional support from persistence

The parent framework begins with a canonical positive-feedback interaction map

\[
q_{t+1}=\operatorname{sigmoid}\left[\kappa\left(\frac{A}{A_{\rm ref}}q_t-\theta\right)\right].
\]

Writing `K = kappa A/A_ref`, the map has a unique fixed point when `K <= 4`. For `K > 4`, two turning points define an exact open interval of `theta` with two locally stable branches separated by an unstable branch. This exact geometry applies to the declared map rather than to fragmented ecosystems universally.

We linked this interaction geometry to a finite trait–allele closure in which interaction state, potential high-trait viability, realised trait occupancy, effective size and genetic diversity remain distinct biological objects. A preregistered fixed-area fragmentation gradient projected the same 1,037 independently prepared high-state sources into 1, 2, 3, 4, 6, 8, 12 and 16 isolated equal patches.

The response was not one-dimensional. Potential high-trait viability was present in 1,037/1,037 supported one-patch outcomes but absent in 1,037/1,037 outcomes at every tested subdivision. Yet realised high-trait occupancy persisted at generation 30 in approximately 99.6–100% of supported trajectories. At the first split into two patches, median retained interaction was 0.001744 of the one-patch value, local effective size was 0.221311 and realised high-trait mass was 0.282918. Interaction and effective size continued to decline with patch count, whereas realised high-trait mass partially recovered, reaching 0.393880 of its one-patch reference at sixteen patches.

Thus numerical occupancy could persist after the declared interaction environment supporting potential high-trait function had changed sharply. Fragmentation separated biological states rather than moving one latent deterioration coordinate.

### Cross-layer covariance changed the next transition without changing mean state

Let `X` be the complete explicit present state and let

\[
\phi:X\rightarrow Z
\]

be a coarse representation containing habitat area, patch and total census, interaction, trait and allele-frequency marginals, complete trait-bin totals, `H_alpha`, `H_gamma` and `F_ST`. Let `T_I:X\rightarrow Q` be the exact one-generation interaction transition. We call `phi` transition-sufficient for `T_I` if there exists a map `g` such that

\[
T_I=g\circ\phi
\]

for every admissible state under the declared closure.

We constructed two states with identical `phi(X)` while reversing the spatial association between interaction state and a common trait/allele support bundle. Cross-layer covariance changed from `+0.025` to `-0.025`, and the exact generation-1 interaction fields differed by as much as **0.2543**. Because `phi(X_A)=phi(X_B)` but `T_I(X_A) != T_I(X_B)`, no transition map defined only on the retained marginals can reproduce both next states.

The source of that immediate difference is exact. Local interaction support is

\[
S_j=\alpha q_j+\beta T_j+\gamma G_j,
\]

with `(alpha,beta,gamma)=(0.6,0.3,0.1)`. In the original construction `T_j=G_j=B_j`, so `S_j=0.6q_j+0.4B_j`. Both states have the same mean support, `0.68`, yet their support distributions are `.47,.61,.75,.89` and `.71,.69,.67,.65`, with population variances `0.0245` and `0.0005`: a **49-fold difference at identical mean support**. More generally,

\[
\mathrm{Var}(S)=\alpha^2\mathrm{Var}(q)+(\beta+\gamma)^2\mathrm{Var}(B)
+2\alpha(\beta+\gamma)\mathrm{Cov}(q,B),
\]

so with fixed marginals, cross-layer covariance changes where support is concentrated rather than how much average support exists.

A previously locked 1,500-pair propagation experiment showed that this distinction could be consequential under one deterioration path, with anti-aligned minus aligned functional-loss risk differences of `+5.33` and `+5.20` percentage points at generations 20 and 40. We therefore asked prospectively which life-cycle processes determine whether such an immediate relational difference persists, disappears or reverses.

### Long-horizon fate reflected sorting opposed by buffering

Our first prospective mechanism experiment crossed trait assignment (`aligned` or `reversed`) with allele assignment (`aligned` or `reversed`) under full feedback, producing `AA`, `AR`, `RA` and `RR` states. It also compared `AA` and `RR` after direct trait and allele contributions to interaction support were removed (`q-only`). Each condition used 1,500 trajectories under fixed forcing and endpoints.

Full feedback did not reproduce a stable directional `AA`–`RR` loss contrast: `RR-AA` was `-0.8` percentage points at generation 20 (95% CI `-4.16,+2.56`) and `+0.6` at generation 40 (`-2.69,+3.89`). However, trait and allele organization interacted strongly. Mismatched `AR/RA` states had average functional-loss risk **6.23 points** above matched `AA/RR` states at generation 20 (`+4.32,+8.15`) and **4.70 points** above them at generation 40 (`+2.90,+6.50`). Thus coherence between trait and allele layers mattered, but one alignment orientation was not universally protective.

Removing direct trait/allele feedback into `q` exposed an indirect matched-state advantage. In the first locked q-only experiment, `RR-AA` loss risk was `+7.13` points at generation 20 and `+6.93` at generation 40. We then opened a separate edge-decomposition protocol before viewing new outcomes and repeated the q-only comparison with five fresh master seeds. The indirect effect reproduced at **+4.20 points** at generation 20 (`+0.86,+7.54`) and **+4.40 points** at generation 40 (`+1.18,+7.62`). The magnitude therefore varied, but the fresh experiment confirmed that direct trait/allele feedback into `q` was not necessary for relational divergence.

The edge deletions changed the interpretation of that indirect pathway. Deleting allele-linked recruitment did not remove the AA advantage. Instead, absolute loss increased sharply and `RR-AA` widened to **+13.20 points** at generation 20 and **+12.73 points** at generation 40. The preregistered difference-in-differences was `-9.00` points (`-13.29,-4.71`) and `-8.33` (`-12.53,-4.14`), respectively. Allele-linked recruitment therefore acts as a **countervailing buffer**: it replenishes the focal trait state in both arrangements and disproportionately reduces the cost of the reversed configuration.

By contrast, deleting local ecological selection as a joint block removed the late matched-state advantage. When both local `q -> allele selection` and local `q -> trait selection` were replaced by spatially averaged selection environments, `RR-AA` was only `+0.60` points at generation 20 and became `-2.87` at generation 40. The preregistered generation-40 difference-in-differences was **+7.27 points** (`+2.67,+11.87`). The two single-edge deletions were more informative about location than about formal resolution: deleting local trait selection alone produced essentially no attenuation, whereas deleting local allele selection reduced the generation-40 `RR-AA` contrast from `+4.40` to `+0.33` points and collapsed AA–RR differences in high-trait mass, allele frequency and refuge number. Its single-edge risk difference-in-differences nevertheless crossed zero, so **local q-dependent allele sorting remains the leading single-edge candidate rather than a separately resolved causal claim**.

The fresh q-only trajectories show what this sorting process looks like dynamically. At generation 5, AA states held substantially more maximum high-trait mass (`AA-RR=+0.0744`, 95% CI `+0.0626,+0.0862`) while occupying fewer realised high-trait refugia (`-0.1813` patch, `-0.2188,-0.1439`). By generation 20 that refuge-number difference reversed (`+0.0767`, `+0.0285,+0.1248`) while AA retained its upper-tail high-trait-mass advantage. The same direction persisted at generation 40. The matched state therefore exhibited a **concentration-to-persistence crossover**: it initially concentrated focal state into fewer stronger patches and later retained more refugia.

Other edge deletions bound the causal chain. Removing resident trait inheritance, local trait selection alone, or q/high-allele contributions to demographic growth did not produce a resolved attenuation of the AA–RR risk contrast. Removing density from the `q` update, however, prevented all functional losses in both states by generation 20 and greatly delayed loss by generation 40. Density-to-interaction feedback is therefore a **failure gate and amplifier** for the declared deterioration regime, although the degenerate zero-event generation-20 endpoint prevents interpreting it as clean matching-specific mediation.

Together the interventions revise the mechanism. The indirect AA advantage is generated by **selection-mediated spatial sorting**, with local allele sorting the leading single-edge candidate. It is opposed by **recruitment-mediated buffering**, which is strongly protective and especially benefits the reversed configuration. Under full feedback, direct trait/allele contributions to `q` add a second buffering route by strengthening weak local interaction states. Long-horizon fate is therefore the net result of sorting versus buffering under a feedback-amplified deterioration process.

### Early genetic erosion did not identify functional fate

Relational mechanisms can shape future function without making every marginal variable a useful warning. We tested six frozen baseline-relative diversity rules: 5%, 10% and 20% declines in `H_alpha` or `H_gamma`.

Every rule preceded all 35 observed losses in the inherited ensemble and all 33 losses in an independently seeded fresh ensemble. But the same rules also fired in all 48 inherited non-event trajectories and all 49 fresh non-events by the common horizon. Every frozen rule therefore had sensitivity `1`, false-positive rate `1`, specificity `0` and binary-marker AUC `0.5` in both ensembles.

The separation follows exactly from the denominator. If `Y=1` denotes loss by the horizon and `M=1` marker firing, perfect event-conditioned precedence fixes sensitivity at one but places no restriction on firing among `Y=0` trajectories. If `f` of `n_0` non-events fire,

\[
\mathrm{specificity}=\frac{n_0-f}{n_0},
\qquad
\mathrm{AUC}=\frac{1+\mathrm{specificity}}{2}
\]

for a binary horizon marker. Perfect event-side ordering is therefore compatible with binary AUC from `0.5` to `1.0`. The observed rules occupy the lower endpoint because every non-event fired.

Genetic diversity is not therefore ecologically irrelevant. Rather, marginal erosion can be stress-sensitive and temporally early while failing to identify whether sorting, buffering or feedback is currently controlling functional fate.

## Discussion

The combined results replace a static interpretation of fragmentation with a mechanistic one. Functional vulnerability is relational, but **relation is not a scalar alignment score**. Cross-layer covariance can alter the exact next transition at fixed marginal state. Whether that difference persists, however, depends on opposing life-cycle processes that either sort compatibility into durable local states or buffer spatial mismatch.

The edge-decomposition result is particularly important because it overturned our initial mechanistic reading. We had interpreted allele-linked recruitment as part of the matching pathway. The prospective deletion showed the opposite: removing that link sharply worsened overall persistence and disproportionately harmed the reversed state. Recruitment is therefore a buffering process in this closure. Conversely, late matching advantage required local ecological selection as a joint block. The leading single-edge signature points to q-dependent allele sorting, but the predeclared risk interval for that edge alone remains unresolved. This distinction prevents a mechanistic story from being inferred solely from the direction of one simulation contrast.

The temporal crossover clarifies what sorting buys the system. The matched state initially retains a stronger concentration of focal trait state in fewer patches, whereas the reversed state distributes occupancy more broadly. Under continued forcing, the concentrated state later retains more refugia. Fragmentation may therefore create a trade-off between **short-term spatial coverage and long-term persistence of compatible local cores**. Recruitment buffering reduces that trade-off by replenishing phenotype where genotype and ecological state are poorly matched. Direct interaction feedback provides another route to recoupling by altering the ecological state itself.

This framework gives a more precise ecological interpretation to collapse and compensation. In an uncompensated system, local ecological filtering can progressively sort away mismatched functional states until too few viable cores remain. In a buffered system, recruitment, movement, partner reorganization or other feedbacks can replenish the focal state or improve the local environment before that sorting becomes irreversible. Historical memory adds a third axis when standing genetic state records a previous configuration after current interactions have changed.

Published natural systems illustrate these possibilities without validating the finite model. In urban *Crepis sancta*, reduced local flowering density is associated with reduced pollinator activity and reproduction despite wider movement, consistent with limited buffering. Miyake-jima *Camellia–Zosterops* provides the opposite ecological projection: reduced floral resources are accompanied by broader bird movement and pollen mixing, consistent with recoupling through movement. *Conospermum undulatum* illustrates temporal mismatch between current pollen processes and adult genetic memory, whereas *Spondias purpurea* shows more coordinated deterioration across visitation, pollen flow, reproductive function and younger-cohort genetics. These systems motivate candidate pathways; they are not replications of the model.

The same interpretation sharpens the earlier urban–island comparison. `Urban` and `island` are upstream histories, not mechanistic states. They can differ in partner mobility, rewiring, mating opportunity, reproductive assurance and genetic memory, all of which determine the balance between sorting and buffering. Existing Honshu–Izu and Zurich archives cannot identify a universal shared urban–island law because their state coordinates and endpoints are not harmonized. A prospective comparison should instead ask whether measured buffering processes explain why a given degree of ecological mismatch becomes persistent in one landscape but is repaired in another.

Our separate natural-data measurement programme reaches a complementary boundary. Candidate process states can fail because a relevant coordinate is absent, a proxy does not earn endpoint relevance, or preprocessing erases the relation it was meant to measure. Those analyses remain non-load-bearing here. Their value is to specify an empirical design: synchronize local resource and demographic support, realised interactions, movement or mating connectivity, trait and cohort-specific genetic state, and later function in the same held-out populations. The mechanism here adds a specific requirement: measure not only mismatch, but the **processes that sort or buffer it through time**.

The warning result becomes a monitoring consequence of the same logic. Marginal diversity erosion may reveal system-wide stress while missing whether local sorting is concentrating viable state, recruitment is replenishing mismatch, or feedback has begun to fail. A useful warning for functional collapse therefore needs to discriminate **pathway balance**, not merely detect that one component has begun to erode.

Together, the results suggest a different organizing question for fragmentation ecology: not simply how much habitat, abundance or diversity remains, but **is functional state being sorted into persistent local cores faster than buffering processes can replenish or reconnect it?** Collapse, compensation and lag need not be contradictory responses to fragmentation. They can emerge when sorting, buffering and historical memory dominate to different degrees.

The claim is deliberately bounded. The finite closure does not establish that q-dependent allele sorting is a universal mechanism, that density feedback is always destabilizing, or that the observed generations map to natural timescales. It establishes that matched marginals can hide transition-relevant covariance; that long-horizon relational effects can be decomposed into opposing causal pathways; and that the intuitive direction of those pathways must be tested rather than assumed.

Functional vulnerability under fragmentation is therefore not only a property of what remains, or even of how remaining components are aligned at one moment. It is a property of the **life-cycle balance between sorting and buffering** that determines whether functional compatibility is concentrated, replenished or lost.

## Methods

### Evidence architecture

The integrated analysis uses four load-bearing blocks. The fragmentation/state-separation results are inherited from the theorem-guided parent framework; the transition-sufficiency counterexample is owned by the state-validity programme; the full-feedback and q-only mechanism experiments plus the new edge-decomposition experiment identify the competing relational pathways; and the full-denominator warning audit tests fate discrimination. Published natural systems and the separate natural-data measurement programme are used only for ecological interpretation and prospective measurement design.

### Canonical interaction-state theorem and fragmentation gradient

For the canonical map, fixed points satisfy

\[
\operatorname{logit}(q)-Kq+\kappa\theta=0,
\qquad K=\kappa A/A_{\rm ref}.
\]

Because the derivative is `1/[q(1-q)]-K` and `1/[q(1-q)] >= 4` on `(0,1)`, strict bistability requires `K>4`; the exact barrier interval follows from the two turning points. The finite fragmentation experiment used 1,200 attempted fresh source preparations, of which 1,037 completed the required high-state preparation. Each supported source was projected into 1, 2, 3, 4, 6, 8, 12 or 16 isolated equal patches under fixed total area and the declared full-state preservation contract.

### Transition sufficiency and immediate relational mechanism

The coarse representation `phi` and transition `T_I` are defined in Results. The aligned/anti-aligned constructive pair holds all declared marginals fixed and reverses only cross-layer spatial association. Exact generation-1 transition fields were evaluated before long-horizon outcomes. The support-variance identity follows algebraically from the weighted local support signal and the fixed layer marginals.

### Full-feedback and q-only mechanism experiment

Before outcomes were opened, a six-condition protocol fixed four full-feedback trait-by-allele assignments and two q-only conditions, the state values, deterioration path, horizons, seeds and endpoint. Each condition used 1,500 trajectories. The full-feedback factorial estimated trait and allele main effects and their interaction. The q-only intervention removed direct trait and allele contributions to the interaction-support signal while retaining the remaining life cycle.

### Prospective pathway edge decomposition

A separate protocol was committed before its first outcome file. All eight interventions retained the q-only direct-support weights `(1,0,0)`, zero migration and mutation, the same initial AA/RR states, the original barrier path and the existing all-patch realised-high-trait loss endpoint. Five fresh master seeds with 300 replicates each yielded 1,500 AA/RR paired keys per intervention.

The baseline indirect condition retained allele-linked two-kernel recruitment, resident inheritance weight `0.5`, local q-dependent allele and trait selection, state-dependent demographic growth and density in the q update. Seven predeclared deletions removed, one at a time, allele-linked recruitment, resident trait inheritance, local trait selection, local allele selection, state-dependent demographic growth, or density-to-q feedback; the final intervention removed both local selection edges jointly. Spatial selection deletions replaced local q by the within-condition spatial mean q for the relevant selection step, preserving the time-varying average environment while deleting local spatial matching.

For each deletion and horizon 20/40, the primary mechanism estimand was

\[
\Delta_{\rm DID}=(RR-AA)_{\rm baseline}-(RR-AA)_{\rm deletion}.
\]

A positive paired 95% interval excluding zero was predeclared as evidence that the deleted edge supported the matching advantage; a negative interval excluding zero indicated a countervailing pathway; otherwise the edge was unresolved. Secondary paired mediators were high-trait mass, realised refuge number, interaction state, population and allele-frequency state at generations 1, 5, 10, 20 and 40. No additional edge deletions, parameter values, seeds, thresholds or horizons were opened after outcomes were read.

### Warning denominator audit

The six frozen markers were the first post-baseline generations at which `H_alpha` or `H_gamma` declined 5%, 10% or 20% from baseline. The inherited ensemble retained 83 baseline-eligible trajectories (35 losses, 48 non-events); the independently seeded fresh ensemble retained 82 (33 losses, 49 non-events). Thresholds, eligibility, horizon and event definition were not recalibrated. The audit restored all baseline-eligible trajectories and calculated horizon sensitivity, specificity, false-positive rate, predictive values and binary-marker AUC.

### Natural projection boundary

Published natural systems are ecological examples only. The separate natural-data analyses are not external validation of the finite simulator. No cross-system effect is pooled, and no urban–island equality is estimated from unmatched archives. Their role is to define candidate sorting, buffering and memory processes for future synchronized empirical tests.

### Reproducibility

Load-bearing evidence is version controlled with locked protocols, machine-readable summaries and reproducible artifacts. The edge-decomposition scientific run is pinned to workflow `34014537015`, job `101435935218`, artifact `9983623440` and digest `sha256:45b38de7514dac8df356579156d994fbc5728e8924308299b2b73571b3595842`. Its workflow is manual-reproduction only after the locked run so later manuscript edits cannot create replacement scientific ensembles.
