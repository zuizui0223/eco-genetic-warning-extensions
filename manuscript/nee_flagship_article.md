# Relational eco-genetic state governs functional vulnerability under fragmentation

## Abstract

Fragmentation is usually summarized by habitat geometry, abundance, interaction strength or genetic diversity, yet these quantities need not describe the same ecological state. We combine exact results and prospectively bounded finite experiments to ask what must be retained for functional vulnerability to be dynamically identifiable. A canonical interaction map gives an exact threshold for alternative interaction states, while a fixed-area fragmentation gradient separates potential viability, realised occupancy, interaction support, effective size and realised trait mass. We then formalize transition sufficiency and construct two eco-genetic states with identical census, interaction, allele-frequency and trait marginals, `H_alpha`, `H_gamma` and `F_ST`, but opposite cross-layer alignment. Their exact next interaction transitions differ by 0.2543, and a locked 1,500-pair experiment yields approximately five-percentage-point differences in later functional-loss risk. Finally, six frozen diversity thresholds precede every observed loss in two ensembles yet fire in every non-event, giving specificity zero and binary AUC 0.5. Functional vulnerability is therefore relational: persistence, marginal diversity and early erosion do not identify ecological fate unless the future-relevant organization of the state is retained.

Ecological fragmentation changes far more than the amount of habitat. It can alter local demographic support, partner interactions, mating opportunities, movement, trait expression and genetic composition, and those quantities can respond on different schedules. The central ecological problem is therefore not simply how much of each component remains, but which combination of components still constitutes a state capable of sustaining a focal function.

This distinction matters because population persistence can conceal functional vulnerability. Strongly interacting species can cease to deliver ecological function before numerical extinction, and interaction loss can precede species loss. Conversely, movement and behavioural reorganization can sometimes compensate local resource loss, while standing genetic summaries can retain historical information after contemporary interaction or mating processes have changed. These observations suggest that ecological deterioration can be relational rather than purely compositional: function may depend on whether its required ecological and genetic components remain coordinated in space and time.

Existing theory provides pieces of this problem. Critical-transition theory formalizes alternative states and changing stability; eco-evolutionary theory in fragmented landscapes couples demography, dispersal, selection and inheritance; multilayer ecology shows that interlayer organization can matter beyond layer-wise summaries; and ecological forecasting emphasizes explicit prediction targets and horizons. What remains less explicit is a state-identification question: **when do commonly retained ecological and genetic summaries actually determine the transition relevant to future function?**

Natural systems motivate this question without serving as validation data for the model developed here. In urban *Crepis sancta*, reduced local flowering density is associated with reduced pollinator activity and reproduction despite nonzero wider movement. On Miyake-jima, volcanic damage reduces local floral resources, yet broader *Zosterops* movement and pollen mixing can maintain pollination and next-generation mixing. In fragmented *Conospermum undulatum*, contemporary pollen connectivity and reproduction deteriorate while adult neutral genetics retain the signature of historical connectivity. These contrasting routes suggest that labels such as `urban`, `island` or `fragmented` are upstream histories, not sufficient descriptions of the functional state they create.

We develop a three-part test of this idea. First, we ask whether fragmentation moves distinct biological objects along one common deterioration axis. Second, we formalize whether a coarse eco-genetic representation is sufficient to determine the next transition and then test whether a hidden state distinction propagates to later functional loss. Third, we ask whether an apparently early marginal genetic signal distinguishes functional fate once the full event and non-event denominator is restored. The resulting synthesis is intentionally asymmetric: the mathematical and finite-model results carry the causal and inferential claims; natural examples are used only to interpret what those results make visible in real ecological systems.

## Results

### Fragmentation separated functional support from persistence

The parent framework begins with a canonical positive-feedback interaction map

\[
q_{t+1}=\operatorname{sigmoid}\left[\kappa\left(\frac{A}{A_{\rm ref}}q_t-\theta\right)\right].
\]

Writing `K = kappa A/A_ref`, the map has a unique fixed point when `K <= 4`. For `K > 4`, two turning points define an exact open interval of `theta` within which three fixed points exist, with low and high locally stable branches separated by an unstable branch. This is an exact statement for the declared map, not a generic theorem for every fragmented ecosystem.

The branch geometry was then linked to a declared finite trait–allele closure in which interaction state, potential high-trait viability, realised trait occupancy, local effective size, allele persistence and genetic diversity remain distinct biological objects. A preregistered fixed-area fragmentation gradient projected the same 1,037 independently prepared high-state sources into 1, 2, 3, 4, 6, 8, 12 and 16 isolated equal patches.

The response was not one-dimensional. Potential high-trait viability was present in 1,037/1,037 supported one-patch outcomes but absent in 1,037/1,037 outcomes at every tested subdivision. Yet realised high-trait occupancy persisted at generation 30 in approximately 99.6–100% of supported trajectories. At the first split into two patches, the paired median retained interaction was 0.001744 of the one-patch value, local effective size was 0.221311 and realised high-trait mass was 0.282918. Interaction and effective size continued to decline with patch count, whereas realised high-trait mass partially recovered, reaching 0.393880 of its paired one-patch reference at sixteen patches.

Thus a fragmented system could remain numerically occupied while the interaction environment required for potential function had already changed sharply. Fragmentation created a separation among biological states rather than a single scalar deterioration trajectory.

### Relational organization was required to determine the next state

We next formalized the representation problem. Let `X` be the complete explicit present state of the finite closure and let

\[
\phi:X\rightarrow Z
\]

be a coarse representation containing habitat area, patch and total census, interaction-state marginals, allele-frequency marginals, realised high-trait-mass marginals, complete trait-bin totals, `H_alpha`, `H_gamma` and `F_ST`. Let

\[
T_I:X\rightarrow Q
\]

be the exact one-generation interaction transition. We call `phi` transition-sufficient for `T_I` if there exists a map `g` such that

\[
T_I=g\circ\phi
\]

for every admissible state under the declared closure.

The sufficiency test is constructive. If two admissible states satisfy `phi(X_A)=phi(X_B)` but `T_I(X_A) != T_I(X_B)`, no such `g` can exist. We therefore constructed aligned and anti-aligned two-patch states that held every declared marginal fixed while reversing the patchwise association between interaction support and the genetic/trait-support bundle.

The two states had identical coarse signatures, but cross-layer covariance changed from +0.025 to -0.025. Their exact generation-1 interaction fields differed patchwise, with a maximum absolute difference of **0.2543**. The commonly retained marginals were therefore not sufficient to determine even the next transition.

We then tested whether the exact one-step distinction propagated to a later, coarser endpoint. A separately prospectively locked experiment followed 1,500 aligned/anti-aligned pairs under one fixed deterioration path and read cumulative functional loss at generations 5, 10, 20 and 40. Anti-aligned minus aligned loss risk was 0.0 percentage points at generation 5, +0.33 points at generation 10 (95% CI -0.44 to +1.11), **+5.33 points at generation 20** (+2.04 to +8.62), and **+5.20 points at generation 40** (+1.96 to +8.44). Nested 500- and 1,000-pair prefixes showed that additional replication mainly narrowed uncertainty around the generation-20/40 contrast rather than creating a qualitatively different effect.

The fixed readouts do not identify generation 20 as a universal cutoff. They show that a relational distinction that is exact at the next transition can remain nearly invisible to a coarser loss endpoint at short horizons and become consequential later under the declared dynamics.

A separate portability audit reached the same identification boundary from another direction. A historical pattern associated with an allele-frequency mixing operator did not reproduce in one independently seeded ensemble and did not transport to separately declared whole-individual or pollen-only movement closures. A shared scalar parameter value therefore did not identify a shared biological connectivity state across different transition operators.

### Early genetic erosion did not identify functional fate

A relational state can be future-relevant without implying that every biologically plausible marginal variable is a predictive warning. We tested six frozen baseline-relative diversity rules: 5%, 10% and 20% declines in `H_alpha` or `H_gamma`. These rules had previously been summarized by whether they crossed before functional loss among trajectories in which both crossing and loss were observed.

The temporal-order result reproduced perfectly. Every rule preceded all 35 observed losses in the inherited ensemble and all 33 observed losses in an independently seeded fresh ensemble. If the analysis stopped there, every rule would appear to be a perfectly reproducible early signal.

Restoring the full baseline-eligible denominator changed the interpretation. The same rules also fired in all 48 inherited non-event trajectories and all 49 fresh non-event trajectories by the common horizon. Every frozen rule therefore had sensitivity 1, false-positive rate 1, specificity 0 and binary-marker AUC 0.5 in both ensembles.

This is not merely an empirical peculiarity. Let `Y=1` denote functional loss by the horizon and `M=1` denote marker firing. Perfect event-conditioned precedence forces `M=1` for every `Y=1` trajectory and therefore fixes sensitivity at one, but it places no restriction on marker firing among `Y=0` trajectories. If `f` of `n_0` non-events fire,

\[
\mathrm{specificity}=\frac{n_0-f}{n_0},
\]

and for a binary horizon marker

\[
\mathrm{AUC}=\frac{1+\mathrm{specificity}}{2}.
\]

Thus the same perfect event-side lead result is compatible with binary AUC anywhere from 0.5 to 1.0. The observed ensembles occupy the sharp lower endpoint because every non-event fired.

The result does not show that genetic diversity is ecologically irrelevant, nor does it show that omitted cross-layer alignment caused the warning failure. It establishes a different point: marginal erosion can be temporally early and biologically real while failing to distinguish which trajectories will undergo the declared functional loss.

## Discussion

The three results converge on a positive ecological interpretation. Fragmentation does not create one universal deterioration coordinate. It can separate the state that supports a function from the state that records persistence, and the future can depend on relational organization that is invisible to familiar marginal summaries. Under the declared closure, the relevant distinction is spatial alignment among interaction support and genetic/trait support. The broader ecological lesson is not that this one alignment statistic is universal, but that **functional vulnerability can depend on relations among components rather than on their separate amounts alone**.

This interpretation changes how persistence under fragmentation is read. In the fixed-area gradient, realised occupancy persisted after potential viability had collapsed under the declared support criterion. Such a state is not equivalent to immediate extinction, but neither is persistence evidence that the function-supporting state remains intact. The distinction provides a mechanistic form of hidden vulnerability: current components can remain observable while the organization required for future function has already changed.

The natural literature illustrates several ways such relational states could arise without validating the finite model. *Crepis sancta* represents an uncompensated route in which low local support is associated with reduced interaction and reproduction despite nonzero wider movement. Miyake-jima *Camellia–Zosterops* provides the opposite ecological possibility: local floral support declines, but bird movement and pollen mixing reorganize in a compensating direction, maintaining pollination and next-generation mixing. *Conospermum undulatum* illustrates temporal mismatch, because contemporary pollen connectivity and reproduction can deteriorate while adult neutral genetics retain information from an older landscape. *Spondias purpurea* illustrates a more coordinated deterioration in which visitation, pollen flow, reproductive function and younger-cohort genetics move in the same adverse direction. These systems are not replications of the simulator; they show why a state description based only on abundance, geography or adult neutral diversity can miss ecologically distinct routes.

The same logic reframes the earlier urban–island comparison. `Urban` and `island` are not candidate regimes by themselves. They are different upstream histories that can alter interaction composition, partner movement, mating opportunity, reproductive assurance and genetic memory through different mechanisms. Existing Honshu–Izu and Zurich archives cannot identify a universal shared urban–island law because their state coordinates, endpoints, taxa and protocols are not harmonized. Their useful implication is prospective: a cross-origin comparison should ask whether matched process states, rather than habitat labels, explain future function.

Our separate natural-data measurement programme reaches a complementary but non-load-bearing conclusion. Across heterogeneous archives, candidate process states can fail because a relevant coordinate is missing, because a plausible proxy does not earn endpoint relevance, or because preprocessing erases the biological distinction the representation was meant to preserve. Those analyses do not validate the synthetic closure and are not pooled into the present mechanistic result. They instead specify what an end-to-end natural test would have to measure: local demographic/resource support, realised interaction state, process-specific movement or mating connectivity, target-relevant trait/genetic state, cross-layer alignment, and a future functional endpoint measured under ecological holdout.

The warning result adds a monitoring consequence. A marginal variable can respond early to deterioration without identifying functional fate. In the frozen ensembles, diversity erosion was perfectly early among losses precisely because it was also ubiquitous among non-losses. This distinguishes a **stress-sensitive variable** from a **fate-discriminating variable**. The distinction is general even though the observed thresholds and trajectories are model-specific: temporal precedence alone does not identify false-positive behaviour.

Together, these results suggest a different organizing question for fragmentation ecology. Instead of asking only how much habitat, abundance or diversity remains, ask whether the components required for the focal function remain coordinated in the places and times where that function is produced. Collapse, compensation and lag then become alternative ecological outcomes of different relational states rather than contradictions to a single fragmentation rule.

The strongest prospective test is therefore not a larger retrospective collection of heterogeneous examples. It is a synchronized natural design in which the same populations or sites are measured for local support, realised interactions, movement/mating, cohort-specific genetics or traits, relational alignment and later function before outcomes are opened. A successful compression would be the smallest measured state for which upstream labels such as island, urban history or disturbance no longer improve held-out future-function prediction. If they still do, the state is incomplete and the missing process or memory should be sought explicitly.

Functional vulnerability under fragmentation is therefore relational. The presence of components, their marginal diversity and even their early erosion can all be informative while remaining insufficient to determine ecological fate. What matters for prediction is whether the representation preserves the organization through which those components jointly generate function.

## Methods

### Evidence architecture

The integrated analysis uses three load-bearing evidence blocks. The fragmentation/state-separation results are inherited from the theorem-guided parent framework; the relational-state counterexample and propagation experiment are owned by the state-validity programme; and the full-denominator warning result is owned by the frozen warning-validity audit. Natural examples and natural-data audits are used only for ecological interpretation and prospective measurement design.

### Canonical interaction-state theorem and finite fragmentation gradient

For the canonical map, fixed points satisfy

\[
\operatorname{logit}(q)-Kq+\kappa\theta=0,
\qquad K=\kappa A/A_{\rm ref}.
\]

Because the derivative is `1/[q(1-q)]-K` and `1/[q(1-q)] >= 4` on `(0,1)`, strict bistability requires `K>4`; the exact barrier interval is obtained from the two turning points. The finite fragmentation experiment used 1,200 attempted fresh source preparations, of which 1,037 completed the required high-state source preparation. Each supported source was projected into 1, 2, 3, 4, 6, 8, 12 or 16 isolated equal patches under fixed total area and the declared full-state preservation contract.

### Transition-sufficiency counterexample and propagation

The coarse representation `phi` and transition `T_I` are defined in the Results. The aligned/anti-aligned constructive pair holds all declared marginals fixed and reverses only the cross-layer association. The exact generation-1 transition is evaluated before long-horizon outcomes. A later protocol, locked after the original state-pair result and before extension outcomes were opened, followed 1,500 paired trajectories once to generation 40 and read cumulative functional loss at generations 5, 10, 20 and 40. The primary estimand was anti-aligned minus aligned paired risk difference with a paired 95% interval.

### Warning denominator audit

The six frozen markers were the first post-baseline generations at which `H_alpha` or `H_gamma` declined 5%, 10% or 20% from its own baseline. The inherited ensemble retained 83 baseline-eligible trajectories (35 losses, 48 horizon non-events); the independently seeded fresh ensemble retained 82 (33 losses, 49 non-events). Thresholds, eligibility, horizon and event definition were not recalibrated. The audit restored all baseline-eligible trajectories and calculated horizon sensitivity, specificity, false-positive rate, predictive values and binary-marker AUC.

### Natural projection boundary

Published natural systems are cited as ecological examples only. The separate natural-data measurement analyses are likewise not treated as external validation of the finite simulator. No cross-system ecological effect is pooled, and no urban–island equality is estimated from unmatched archives. Their role is to define candidate coordinates and failure modes for future synchronized empirical tests.

### Reproducibility

The load-bearing parent and extension evidence remains version controlled with locked protocols, machine-readable summaries and reproducible artifacts. The integrated submission bundle pins the exact parent repository commit and the latest reviewed extension base containing the state and warning source-of-truth files. The flagship build regenerates its main displays from those locked evidence objects without rerunning frozen scientific searches.