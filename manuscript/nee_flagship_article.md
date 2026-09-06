# Eco-genetic sorting and buffering shape functional vulnerability under fragmentation

## Abstract

Fragmentation can leave ecological components present while changing the life-cycle processes that keep them functionally coupled. We combine exact results with prospectively locked finite experiments to identify why systems with the same marginal ecological and genetic quantities can reach different futures. A fixed-area fragmentation gradient separates potential viability from realised occupancy. At fixed mean support, cross-layer covariance changes spatial support variance 49-fold and produces exact next-state differences despite identical census, trait, allele-frequency and diversity summaries. Prospective interventions then resolve the mechanism: q-dependent allele selection is an exact spatial sorting operator, and deleting that single edge removes a late functional-loss contrast by **6.88 percentage points** (95% CI **5.80–7.97**). Allele-linked recruitment acts oppositely as a buffer, while density-to-interaction feedback gates entry into system-wide loss. Functional vulnerability therefore emerges from **eco-genetic sorting opposed by buffering**, not component amounts or alignment alone.

Ecological fragmentation changes more than habitat amount. It can alter local demographic support, partner interactions, mating opportunity, movement, trait expression and genetic composition, and those quantities need not respond on the same schedule. The central ecological problem is therefore not simply how much of each component remains, but how the components required for a focal function are organized and coupled through the life cycle.

Numerical persistence can consequently conceal functional vulnerability. Ecological interactions may become ineffective before species disappear; movement or behavioural reorganization can sometimes compensate local resource loss; and standing genetic summaries can retain historical information after contemporary interaction or mating processes have changed. These possibilities suggest that fragmentation may change not only component abundance but the **pathways that sort, replenish and reconnect functional state**.

Existing theory provides pieces of this problem. Critical-transition theory formalizes nonlinear state changes; eco-evolutionary theory in fragmented landscapes couples demography, dispersal, selection and inheritance; multilayer ecology shows that interlayer organization can matter beyond layer-wise summaries; and forecasting theory emphasizes explicit targets and horizons. A less explicit mechanistic question is: **when two systems retain the same marginal ecological and genetic quantities, which life-cycle processes make their futures diverge or converge again?**

Natural systems motivate that question without serving as validation data for the finite model developed here. Urban *Crepis sancta* illustrates local interaction limitation that wider movement does not fully rescue. On Miyake-jima, reduced floral resources can instead be accompanied by broader *Zosterops* movement and pollen mixing that compensate pollination. In fragmented *Conospermum undulatum*, current pollen connectivity can deteriorate while adult neutral genetics retain an older landscape signature. These contrasting routes motivate a distinction among sorting, buffering and memory rather than a universal `urban`, `island` or `fragmented` state.

We test the mechanism in four stages. First, we ask whether one fragmentation gradient generates one biological deterioration coordinate. Second, we formalize transition sufficiency and identify the exact source of an immediate matched-marginal transition difference. Third, through prospectively locked factorial, edge-deletion and focused single-edge experiments, we identify the life-cycle processes that propagate or buffer relational differences. Fourth, we ask whether an early marginal diversity response identifies functional fate once the full event and non-event denominator is restored. Natural examples enter only after these tests, as ecological projections rather than external validation.

## Results

### Fragmentation separated functional support from persistence

The parent framework begins with a canonical positive-feedback interaction map

\[
q_{t+1}=\operatorname{sigmoid}\left[\kappa\left(\frac{A}{A_{\rm ref}}q_t-\theta\right)\right].
\]

Writing `K = kappa A/A_ref`, the map has a unique fixed point when `K <= 4`. For `K > 4`, two turning points define an exact open interval of `theta` with two locally stable branches separated by an unstable branch. This exact geometry applies to the declared map rather than to fragmented ecosystems universally.

We linked this interaction geometry to a finite trait–allele closure in which interaction state, potential high-trait viability, realised trait occupancy, effective size and genetic diversity remain distinct biological objects. A preregistered fixed-area fragmentation gradient projected the same 1,037 independently prepared high-state sources into 1, 2, 3, 4, 6, 8, 12 and 16 isolated equal patches.

The response was not one-dimensional. Potential high-trait viability was present in **1,037/1,037** supported one-patch outcomes but absent in 1,037/1,037 outcomes at every tested subdivision. Yet realised high-trait occupancy persisted at generation 30 in approximately 99.6–100% of supported trajectories. At the first split into two patches, median retained interaction was 0.001744 of the one-patch value, local effective size was 0.221311 and realised high-trait mass was 0.282918. Interaction and effective size continued to decline with patch count, whereas realised high-trait mass partially recovered, reaching 0.393880 of its one-patch reference at sixteen patches.

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

A previously locked 1,500-pair propagation experiment showed that this distinction could be consequential under one deterioration path, with anti-aligned minus aligned functional-loss risk differences of **+5.33** and **+5.20** percentage points at generations 20 and 40. We therefore asked prospectively which life-cycle processes determine whether such an immediate relational difference persists, disappears or reverses.

### Prospective interventions resolved sorting opposed by buffering

Our first prospective mechanism experiment crossed trait assignment (`aligned` or `reversed`) with allele assignment (`aligned` or `reversed`) under full feedback, producing `AA`, `AR`, `RA` and `RR` states. Full feedback did not reproduce a stable directional `AA`–`RR` loss contrast, but trait and allele organization interacted strongly. Mismatched `AR/RA` states had average functional-loss risk **6.23 points** above matched `AA/RR` states at generation 20 and **4.70 points** above them at generation 40. Thus coherence between trait and allele layers mattered, but one alignment orientation was not universally protective.

Removing direct trait/allele feedback into `q` exposed an indirect matched-state advantage. In the first locked q-only experiment, `RR-AA` loss risk was `+7.13` points at generation 20 and `+6.93` at generation 40. A separate edge-decomposition protocol repeated the q-only comparison with five fresh master seeds and reproduced the effect at **+4.20 points** at generation 20 and **+4.40 points** at generation 40.

The edge deletions overturned our initial interpretation. Deleting allele-linked recruitment did not remove the AA advantage; it widened `RR-AA` to **+13.20 points** at generation 20 and **+12.73 points** at generation 40. The preregistered difference-in-differences was `-9.00` points and `-8.33` points, respectively, with both confidence intervals excluding zero. Allele-linked recruitment is therefore a **recruitment-mediated buffering** process in this closure.

By contrast, deleting both local `q -> allele selection` and local `q -> trait selection` removed the late matched-state advantage. The preregistered generation-40 difference-in-differences was **+7.27 points** (95% CI `+2.67,+11.87`). Local ecological selection therefore supplies a late **selection-mediated spatial sorting** contribution. Removing density from the `q` update prevented all functional losses in both states by generation 20, identifying density-to-interaction feedback as a **failure gate and amplifier** for the declared deterioration regime.

We then isolated the leading single edge in a third protocol that was locked before outcomes. The local high-allele selection operator is

\[
p^+=\frac{p(0.75+0.4q)}{1-p+p(0.75+0.4q)}.
\]

For every `0<p<1`,

\[
\frac{\partial p^+}{\partial q}
=\frac{0.4p(1-p)}
{[1+p\{(0.75+0.4q)-1\}]^2}>0.
\]

Equivalently,

\[
\operatorname{logit}(p^+)-\operatorname{logit}(p)=\log(0.75+0.4q).
\]

Thus q-dependent allele selection is an exact sorting operator. Its direction switches at `q*=0.625`: above this value the high allele increases, below it decreases. The same value is the declared potential high-trait viability threshold. Across patches, with `u_i=logit(p_i)` and `g(q)=log(0.75+0.4q)`,

\[
\mathrm{Cov}(q,u^+)-\mathrm{Cov}(q,u)
=\mathrm{Cov}(q,g(q))>0
\]

whenever q varies spatially, so a single deterministic selection step strictly increases q–allele spatial sorting.

The endpoint consequence was tested with **6,000 paired AA/RR keys per condition**, using twelve entirely new master seeds. Under baseline local allele selection, `RR-AA` functional-loss risk was **+6.65 points** at generation 40 (95% CI `+5.07,+8.23`). When only local `q -> allele selection` was deleted, the contrast collapsed to **-0.23 points** (`-1.80,+1.34`). The preregistered primary difference-in-differences was therefore

\[
\boxed{+6.883\ \text{percentage points}}
\]

with 95% CI

\[
\boxed{[+5.800,+7.967]}.
\]

The secondary generation-20 DID was similarly positive at **+6.783 points** (`+5.478,+8.088`). Local q-dependent allele sorting is therefore a **resolved single-edge causal contributor** to late functional fate in the declared q-only closure.

The mediator pattern matched the theorem. With local allele selection retained, AA relative to RR had higher allele-frequency variance at generation 40 (`+0.01238`, 95% CI `+0.00938,+0.01537`), higher mean high-allele frequency (`+0.01823`, `+0.01397,+0.02248`), greater maximum high-trait mass (`+0.06440`, `+0.04871,+0.08008`) and more realised refugia (`+0.08033` patch, `+0.06263,+0.09804`). Deleting only local allele selection reduced all four generation-40 AA–RR contrasts to intervals containing zero.

Together these results resolve the competing pathways. **q-dependent allele sorting** concentrates eco-genetic compatibility in locally favourable states; **allele-linked recruitment buffers** mismatch by replenishing focal trait state; direct trait/allele feedback into `q` supplies a second recoupling route; and density feedback gates whether the forcing trajectory enters system-wide loss.

### Early genetic erosion did not identify functional fate

Relational mechanisms can shape future function without making every marginal variable a useful warning. We tested six frozen baseline-relative diversity rules: 5%, 10% and 20% declines in `H_alpha` or `H_gamma`.

Every rule preceded all **35 observed losses** in the inherited ensemble and all **33 losses** in an independently seeded fresh ensemble. But the same rules also fired in all **48 inherited non-event** trajectories and all **49 fresh non-events** by the common horizon. Every frozen rule therefore had sensitivity `1`, false-positive rate `1`, specificity `0` and binary-marker AUC `0.5` in both ensembles.

The separation follows exactly from the denominator. If `Y=1` denotes loss by the horizon and `M=1` marker firing, perfect event-conditioned precedence fixes sensitivity at one but places no restriction on firing among `Y=0` trajectories. If `f` of `n_0` non-events fire,

\[
\mathrm{specificity}=\frac{n_0-f}{n_0},
\qquad
\mathrm{AUC}=\frac{1+\mathrm{specificity}}{2}
\]

for a binary horizon marker. Perfect event-side ordering is therefore compatible with binary AUC from `0.5` to `1.0`. The observed rules occupy the lower endpoint because every non-event fired.

Genetic diversity is not therefore ecologically irrelevant. Rather, marginal erosion can be stress-sensitive and temporally early while failing to identify whether sorting, buffering or feedback is currently controlling functional fate.

## Discussion

The combined results replace a static interpretation of fragmentation with a mechanistic one. Functional vulnerability is relational, but **relation is not a scalar alignment score**. Cross-layer covariance can alter the exact next transition at fixed marginal state, while the long-horizon fate of that difference is controlled by specific life-cycle operators.

The mechanism is now more specific than “local ecological selection matters”. The exact allele-selection theorem shows how ecological state q deterministically sorts high-allele log odds in space, with a switch at the same q threshold that supports the high trait. The focused 6,000-pair deletion then shows that this single operator is not only mathematically sorting: it contributes causally to the later all-patch functional-loss contrast. Removing it erases the late AA–RR difference and collapses the corresponding allele, trait and refuge mediators.

That sorting pathway competes with buffering. The prospective recruitment deletion gave the opposite result from our initial intuition: removing allele-linked recruitment worsened overall persistence and disproportionately harmed the reversed state. Recruitment therefore replenishes mismatch rather than creating the sorting advantage. Full eco-genetic feedback into q provides another buffering route by strengthening weak local interaction states. Density feedback plays a different role: it determines whether the system enters the early collapse regime at all.

The temporal dynamics clarify what sorting buys the system. Compatible state can first concentrate in fewer strong patches and later persist in more refugia under continued forcing. Fragmentation may therefore generate a trade-off between short-term spatial coverage and long-term persistence of compatible local cores. Buffering processes can reduce that trade-off by replenishing state or altering the local environment before sorting becomes irreversible.

This framework gives a precise ecological interpretation to collapse and compensation. In an uncompensated system, local ecological filtering can sort focal genotypes and traits away from mismatched locations until too few compatible cores remain. In a buffered system, recruitment, movement, partner reorganization or other feedbacks can replenish the focal state or improve local conditions. Historical memory adds a third axis when standing genetic state records an earlier configuration after current interactions have changed.

Published natural systems illustrate these possibilities without validating the finite model. In urban *Crepis sancta*, reduced local flowering density is associated with reduced pollinator activity and reproduction despite wider movement, consistent with limited buffering. Miyake-jima *Camellia–Zosterops* provides the opposite ecological projection: reduced floral resources are accompanied by broader bird movement and pollen mixing, consistent with recoupling through movement. *Conospermum undulatum* illustrates temporal mismatch between current pollen processes and adult genetic memory, whereas *Spondias purpurea* shows coordinated deterioration across visitation, pollen flow, reproductive function and younger-cohort genetics. These systems motivate candidate pathways; they are not replications of the model.

The same interpretation sharpens the earlier urban–island comparison. `Urban` and `island` are upstream histories, not mechanistic states. They can differ in partner mobility, rewiring, mating opportunity, reproductive assurance and genetic memory, all of which determine the balance between sorting and buffering. Existing Honshu–Izu and Zurich archives cannot identify a universal shared urban–island law because their state coordinates and endpoints are not harmonized. A prospective comparison should instead ask whether measured sorting and buffering processes explain why mismatch becomes persistent in one landscape but is repaired in another.

Our separate natural-data measurement programme remains non-load-bearing here. Its value is to specify an empirical design: synchronize local resource and demographic support, realised interactions, movement or mating connectivity, trait and cohort-specific genetic state, and later function in the same held-out populations. The mechanism here adds a specific requirement: estimate not only state marginals but the **operators that sort or buffer their spatial association through time**.

The warning result becomes a monitoring consequence of the same logic. Marginal diversity erosion may reveal system-wide stress while missing whether q-dependent sorting is concentrating compatible state, recruitment is replenishing mismatch, or feedback has begun to fail. A useful warning for functional collapse therefore needs to discriminate **pathway balance**, not merely detect that one component has begun to erode.

Together, the results suggest a different organizing question for fragmentation ecology: not simply how much habitat, abundance or diversity remains, but **which life-cycle operator currently determines whether functional compatibility is being sorted into durable local cores or buffered against mismatch?** Collapse, compensation and lag need not be contradictory responses to fragmentation; they can emerge when sorting, buffering and historical memory dominate to different degrees.

The claim is deliberately bounded. The finite closure does not establish that q-dependent allele sorting is a universal natural mechanism, that density feedback is always destabilizing, or that the observed generations map to natural timescales. It establishes an exact spatial sorting operator and a prospectively locked endpoint-level causal contribution within the declared closure, while natural systems remain hypotheses for empirical projection.

Functional vulnerability under fragmentation is therefore not only a property of what remains, or even of how remaining components are aligned at one moment. It is a property of the **life-cycle balance between sorting and buffering** that determines whether functional compatibility is concentrated, replenished or lost.

## Methods

### Evidence architecture

The integrated analysis uses five load-bearing blocks. The fragmentation/state-separation results are inherited from the theorem-guided parent framework; the transition-sufficiency counterexample is owned by the state-validity programme; the first prospective mechanism experiment identifies full-feedback non-additivity and q-only divergence; the pathway edge decomposition separates sorting, buffering and density feedback; the focused single-edge proof resolves q-dependent allele sorting; and the full-denominator warning audit tests fate discrimination. Published natural systems and the separate natural-data measurement programme are used only for ecological interpretation and prospective measurement design.

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

For each deletion and horizon 20/40, the primary mechanism estimand was

\[
\Delta_{\rm DID}=(RR-AA)_{\rm baseline}-(RR-AA)_{\rm deletion}.
\]

A positive paired 95% interval excluding zero was predeclared as evidence that the deleted edge supported the matching advantage; a negative interval excluding zero indicated a countervailing pathway; otherwise the edge was unresolved. No additional edge deletions, parameter values, seeds, thresholds or horizons were opened after outcomes were read.

### Focused q-dependent allele-sorting proof

The focused protocol was committed before outcomes and allowed exactly two conditions: the q-only baseline with local q-dependent allele selection, and an otherwise identical condition in which only local spatial q was replaced by the within-condition spatial mean q in the allele-selection step. Twelve fresh master seeds with 500 replicates each yielded **6,000 paired AA/RR keys per condition**. No master seed from the preceding edge-decomposition experiment was reused.

The primary endpoint was the existing all-patch realised-high-trait loss by generation 40. The predeclared estimand was

\[
DID_{40}=(RR-AA)_{\rm baseline}-(RR-AA)_{\rm deletion}.
\]

A paired 95% interval strictly above zero resolved a positive sorting contribution; an interval strictly below zero resolved a countervailing contribution; an interval containing zero required an unresolved stop. Replication could not be extended after the first outcome file.

The operator theorem follows directly from the pinned high-trait fitness surface `W(1;q)=0.5+0.8q` and selection strength `0.5`, yielding `w(q)=0.75+0.4q` and the exact allele-frequency update given in Results. The spatial covariance result follows from the monotonicity of `g(q)=log(0.75+0.4q)`.

### Warning denominator audit

The six frozen markers were the first post-baseline generations at which `H_alpha` or `H_gamma` declined 5%, 10% or 20% from baseline. The inherited ensemble retained 83 baseline-eligible trajectories (35 losses, 48 non-events); the independently seeded fresh ensemble retained 82 (33 losses, 49 non-events). Thresholds, eligibility, horizon and event definition were not recalibrated.

### Natural projection boundary

Published natural systems are ecological examples only. The separate natural-data analyses are not external validation of the finite simulator. No cross-system effect is pooled, and no urban–island equality is estimated from unmatched archives. Their role is to define candidate sorting, buffering and memory processes for future synchronized empirical tests.

### Reproducibility

Load-bearing evidence is version controlled with locked protocols, machine-readable summaries and reproducible artifacts. The pathway edge-decomposition run is pinned to workflow `34014537015`, artifact `9983623440`, digest `sha256:45b38de7514dac8df356579156d994fbc5728e8924308299b2b73571b3595842`. The focused single-edge proof is pinned to workflow `34016797940`, job `101441868527`, artifact `9984306657`, and digest `sha256:61a07cc6a8680a59185537b03abdca85d0f172a65d068ee9661dd9f2fb448c2d`.
