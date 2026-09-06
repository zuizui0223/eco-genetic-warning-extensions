# Eco-genetic sorting and buffering shape functional vulnerability under fragmentation

## Abstract

Fragmentation can leave ecological components present while altering the processes that keep them functionally coupled. We combine exact results with prospectively locked finite experiments to explain why systems with the same marginal ecological and genetic quantities reach different futures. Fixed-area fragmentation first separates potential viability from realised occupancy. At fixed mean support, cross-layer covariance changes support variance 49-fold and exact next interaction states by 0.2543. We then resolve the route mechanism. Local q-dependent allele selection is an exact spatial sorting operator and a resolved single-edge causal contributor to late functional fate (`DID=+6.883` percentage points, 95% CI `+5.800,+7.967`). Allele-linked recruitment contracts trait–allele mismatch by exactly 50% and buffers the reversed state. Direct eco-genetic feedback contracts interaction–bundle mismatch by 40% at the support stage and preferentially recouples the reversed configuration. Density-to-interaction feedback creates a shrinking demographic headroom boundary and amplifies collapse. Functional vulnerability therefore reflects the balance among **sorting, buffering, recoupling and a failure gate**, not component amounts or alignment alone.

Ecological fragmentation changes more than habitat amount. It can alter local demographic support, biotic interactions, movement, mating opportunity, trait expression and genetic composition, and those quantities need not move on the same schedule. A population can therefore remain numerically present while the interaction environment that sustains a focal function has already changed. The relevant ecological question is not simply how much of each component remains, but which processes keep those components jointly usable through time.

This distinction matters because contrasting natural outcomes need not imply contradictory fragmentation effects. Local interaction limitation can remain uncompensated; movement can reorganize and restore pollen transfer; current mating processes can deteriorate while adult genetic state retains historical connectivity; and ecological and genetic deterioration can sometimes move together. We use *Crepis sancta*, Miyake-jima *Camellia–Zosterops*, *Conospermum undulatum* and *Spondias purpurea* only to motivate these possibilities. They are not validation data for the finite model.

Existing theory supplies individual pieces: nonlinear transitions, eco-evolutionary feedback, spatial selection, demographic rescue, multilayer coupling and early-warning statistics. A less explicit question is how these pieces combine when conventional state summaries are held fixed. If two systems have the same abundance, trait and allele-frequency marginals, why can one retain function while another loses it? And if a difference appears, which life-cycle operator causes it, which operator repairs it, and which feedback opens the path to collapse?

We address those questions in four steps. First, we test whether a single fragmentation gradient corresponds to a single biological deterioration coordinate. Second, we construct matched-marginal states and identify the exact source of their next-transition difference. Third, we prospectively intervene on individual life-cycle edges and derive the exact operators responsible for sorting, buffering, recoupling and collapse entry. Fourth, we test whether early marginal genetic erosion discriminates later functional fate. Natural examples return only in the Discussion as projections of these mechanisms.

## Results

### Fragmentation separated persistence from functional support

The parent framework begins with the canonical interaction map

\[
q_{t+1}=\operatorname{sigmoid}\left[\kappa\left(\frac{A}{A_{\rm ref}}q_t-\theta\right)\right].
\]

Writing `K = kappa A/A_ref`, the exact fixed-point geometry changes at `K > 4`: above this threshold two turning points delimit a barrier interval with two locally stable branches separated by an unstable branch. This is an exact result for the declared map, not a universal claim about fragmented ecosystems.

We coupled this interaction state to distinct potential-trait, realised-trait, demographic and genetic states. A preregistered fixed-area fragmentation gradient projected the same 1,037 independently prepared high-state sources into 1, 2, 3, 4, 6, 8, 12 and 16 isolated equal patches. Potential high-trait viability was present in **1,037/1,037** supported one-patch outcomes and absent in 1,037/1,037 outcomes at every tested subdivision, yet realised high-trait occupancy remained approximately 99.6–100% at generation 30.

The remaining variables did not collapse onto one deterioration axis. At the first split into two patches, median retained interaction was 0.001744 of the one-patch value, local effective size was 0.221311 and realised high-trait mass was 0.282918. Interaction and local effective size continued to decline as patch number increased, while realised high-trait mass partially recovered to 0.393880 at sixteen patches. Numerical persistence therefore did not imply retained functional support, and one structural perturbation generated several biological trajectories rather than one latent damage score.

### Matched marginals concealed an exact transition difference

Let `X` denote the complete explicit present state and let

\[
\phi:X\rightarrow Z
\]

retain habitat area, patch and total census, interaction, trait and allele-frequency marginals, complete trait-bin totals, `H_alpha`, `H_gamma` and `F_ST`. Let `T_I:X\rightarrow Q` be the exact one-generation interaction transition. We call `phi` transition-sufficient if there exists a map satisfying

\[
T_I=g\circ\phi
\]

for every admissible state under the declared closure.

We constructed two states with identical retained marginals while reversing only the spatial association between interaction state and a common trait/allele support bundle. Cross-layer covariance changed from `+0.025` to `-0.025`, while the exact generation-1 interaction fields differed by as much as **0.2543**. Because the two states have identical `phi(X)` but different `T_I(X)`, no transition rule defined only on those marginals can reproduce both futures.

The immediate mechanism is algebraic. Local support is

\[
S_j=\alpha q_j+\beta T_j+\gamma G_j,
\]

with `(alpha,beta,gamma)=(0.6,0.3,0.1)`. In the original construction `T_j=G_j=B_j`, giving `S_j=0.6q_j+0.4B_j`. The two states have identical mean support, `0.68`, but support vectors `.47,.61,.75,.89` and `.71,.69,.67,.65`, with variances `0.0245` and `0.0005`: a **49-fold difference**. In general,

\[
\mathrm{Var}(S)=\alpha^2\mathrm{Var}(q)+(\beta+\gamma)^2\mathrm{Var}(B)
+2\alpha(\beta+\gamma)\mathrm{Cov}(q,B).
\]

Thus, with fixed layer marginals, cross-layer covariance changes where support is concentrated rather than its average amount. A previously locked propagation experiment showed that this immediate distinction could reach later function in one ensemble: anti-aligned minus aligned functional-loss risks were **+5.33** and **+5.20** percentage points at generations 20 and 40. We therefore asked prospectively why that difference sometimes persisted and sometimes disappeared.

### Four life-cycle operators explained divergence, repair and collapse entry

The first prospective mechanism experiment crossed trait assignment and allele assignment under full feedback. Trait–allele mismatched states had functional-loss risk **6.23 points** above matched states at generation 20 and **4.70 points** above them at generation 40, but the directional AA-versus-RR contrast itself was not stable. Removing direct trait/allele input into q exposed an indirect AA advantage, and a fresh edge-decomposition experiment reproduced that q-only contrast at **+4.20 points** at generation 20 and **+4.40 points** at generation 40. We then decomposed the responsible operators.

#### q-dependent allele selection is the sorting operator

The local high-allele update before drift is

\[
p^+=\frac{p(0.75+0.4q)}{1-p+p(0.75+0.4q)},
\]

so

\[
\frac{\partial p^+}{\partial q}
=\frac{0.4p(1-p)}{[1+p\{(0.75+0.4q)-1\}]^2}>0
\]

for every interior allele frequency. Equivalently,

\[
\operatorname{logit}(p^+)-\operatorname{logit}(p)=\log(0.75+0.4q).
\]

The exact switch is `q*=0.625`: above it the high allele increases, below it decreases. The same value is the declared potential high-trait viability threshold. Across patches, writing `u_i=logit(p_i)` and `g(q)=log(0.75+0.4q)`,

\[
\mathrm{Cov}(q,u^+)-\mathrm{Cov}(q,u)=\mathrm{Cov}(q,g(q))>0
\]

whenever q varies spatially. One allele-selection step therefore strictly increases q–allele spatial sorting.

We tested the endpoint consequence with **6,000 paired AA/RR keys per condition** using twelve entirely new master seeds. Baseline local allele selection produced `RR-AA = +6.65 points` at generation 40 (95% CI `+5.07,+8.23`). Deleting only `q -> allele selection` reduced the contrast to **-0.23 points** (`-1.80,+1.34`). The preregistered primary DID was **+6.883** percentage points with 95% CI **`+5.800,+7.967`**. The generation-20 DID was +6.783 points (`+5.478,+8.088`). Local q-dependent allele sorting is therefore a **resolved single-edge causal contributor** to late functional fate in this finite closure.

#### Allele-linked recruitment is an exact mismatch buffer

The earlier edge decomposition had shown the opposite effect from our initial intuition. Deleting allele-linked recruitment widened the fresh q-only `RR-AA` contrast from +4.20 to **+13.20 points** at generation 20 and from +4.40 to **+12.73 points** at generation 40. The preregistered baseline-minus-deletion DIDs were `-9.00` points (`-13.29,-4.71`) and `-8.33` points (`-12.53,-4.14`), respectively. Recruitment is therefore a **recruitment-mediated buffering** process rather than the source of the sorting advantage.

The operator is exact. Let `m` be resident high-trait mass, `p` high-allele frequency and `h` the resident inheritance weight. Two-kernel recruitment gives

\[
r=(1-h)p+hm.
\]

With the locked `h=0.5`,

\[
r=\frac{m+p}{2},\qquad r-p=0.5(m-p).
\]

Hence recruitment contracts trait–allele mismatch by exactly **50%** before selection, and squared mismatch by 75%. It can raise or lower high-trait recruit mass depending on the direction of the mismatch; its defining property is coherence restoration, not universally increasing the focal trait.

#### Direct eco-genetic feedback is a recoupling operator

Define the normalized local eco-genetic bundle

\[
B=0.75T+0.25G.
\]

Under full feedback,

\[
S=0.6q+0.3T+0.1G=0.6q+0.4B.
\]

Thus

\[
S-B=0.6(q-B),
\]

so the support stage contracts interaction–bundle mismatch by exactly **40%**. Relative to the q-only transition,

\[
\operatorname{logit}(q_F^+)-\operatorname{logit}(q_Q^+)
=0.4\kappa a d(B-q),
\]

where `a=A/A_ref` and `d` is density. Under the locked `kappa=4.5`, `a=1` setting the shift is `1.8d(B-q)`. Direct feedback therefore raises next q where the bundle exceeds q and lowers it where the bundle is below q. It is a recoupling operator, not a generic positive-q effect.

The prospectively locked six-condition experiment used identical trajectory seeds across conditions, allowing a secondary paired contrast without opening a new ensemble. Direct-feedback benefit, defined as q-only loss minus full-feedback loss, was +0.60 points for AA (`-2.71,+3.91`) but **+8.53 points** for RR (`+5.21,+11.85`) at generation 20; the RR-minus-AA buffering-benefit contrast was **+7.93 points** (`+3.29,+12.58`). At generation 40 the benefits were +1.47 points for AA (`-1.72,+4.65`) and **+7.80 points** for RR (`+4.79,+10.81`), with a difference of **+6.33 points** (`+1.85,+10.82`). These are derived paired contrasts from an already prospectively locked intervention family, not a separately predeclared primary estimand. They nevertheless match the operator: direct feedback preferentially recoupled the reversed arrangement.

#### Density feedback is a failure gate and amplifier

In the q-only closure,

\[
q^+=\sigma\{4.5(dq-\theta)\},\qquad d=\min(1,N/K).
\]

Below carrying capacity,

\[
\frac{\partial q^+}{\partial N}>0.
\]

The smooth demographic backbone also increases with q, giving the positive path `q down -> N down -> density down -> q down`. The direct two-step loop gain is positive on the unsaturated-density branch. Moreover, keeping the next interaction state at or above the shared `q*=0.625` switch requires

\[
\boxed{dq\ge\theta+0.1135168053}.
\]

Under the locked forcing path the required density–interaction product rises from 0.6160168 near the beginning to 0.6635168 at generation 20 and 0.7135168 at generation 40. Deterioration therefore consumes demographic headroom even before the endpoint is crossed.

The locked density-edge deletion produced a system-level effect. By generation 20, deleting density from q reduced cumulative loss by 38.33 points for AA (`35.87,40.79`) and 42.53 points for RR (`40.03,45.04`), leaving **0/1,500 losses in both conditions**. At generation 40, paired reductions were 57.47 points (`54.65,60.28`) and 59.60 points (`56.73,62.47`). Because the preregistered generation-40 attenuation of the RR-minus-AA differential was unresolved, density feedback is not the sorting edge. It is a **failure gate and amplifier** controlling whether demographic erosion feeds back into widespread collapse.

Together these results replace an unexplained branch diagram with an explicit causal architecture. Cross-layer covariance first creates transition-relevant heterogeneity. q-dependent allele selection sorts compatible eco-genetic state into favourable local environments. Recruitment contracts trait–allele mismatch. Direct feedback recouples interaction state toward the local trait/genetic bundle. Density feedback determines whether declining demography is amplified into system-wide loss. Long-horizon fate is the net result of these operators rather than a monotone function of alignment.

### Early genetic erosion did not identify functional fate

A mechanistic state can matter for fate without making every marginal variable a useful warning. We tested six frozen baseline-relative diversity rules: 5%, 10% and 20% declines in `H_alpha` or `H_gamma`. Every rule preceded all **35 observed losses** in the inherited ensemble and all **33 losses** in an independently seeded fresh ensemble. The same rules also fired in all **48 inherited non-event** trajectories and all **49 fresh non-events** by the common horizon. Every rule therefore had sensitivity 1, false-positive rate 1, specificity `0` and binary-marker AUC `0.5`.

The boundary is exact. If `Y=1` denotes loss by the horizon and `M=1` marker firing, perfect event-conditioned precedence fixes sensitivity at one but leaves non-event firing unconstrained. If `f` of `n_0` non-events fire,

\[
\mathrm{specificity}=\frac{n_0-f}{n_0},\qquad
\mathrm{AUC}=\frac{1+\mathrm{specificity}}{2}
\]

for a binary horizon marker. Perfect precedence is therefore compatible with AUC from 0.5 to 1.0. The observed rules occupy the lower endpoint because every non-event fired. Genetic diversity can thus be stress-sensitive and temporally early without identifying whether sorting, buffering, recoupling or failure-gate dynamics currently control functional fate.

## Discussion

The central result is no longer merely that ecological state is relational. We can now identify **why** matched conventional states diverge. Cross-layer covariance changes the immediate transition, but later fate is generated by life-cycle operators with different directions and biological targets. q-dependent allele selection sorts genetic state along the local interaction gradient; recruitment contracts genotype–phenotype mismatch; direct eco-genetic feedback repairs interaction–bundle mismatch; and density feedback determines when demographic erosion becomes self-amplifying.

This decomposition matters because several intuitive explanations failed. Positive alignment was not universally protective under full feedback. Allele-linked recruitment, initially suspected to generate the matched-state advantage, did the opposite: deleting it made the reversed configuration much worse. Direct feedback did not simply raise interaction state everywhere; algebraically it shifts the transition according to the sign of `B-q`, and empirically its benefit was concentrated in the reversed configuration. The mechanism therefore emerged by prospective intervention and exact derivation rather than by assigning a story to the first observed contrast.

The resulting ecology is a competition between sorting and repair. Sorting can concentrate compatible eco-genetic state into local cores, which may initially reduce spatial coverage but later preserve refugia. Recruitment can replenish phenotype when trait and allele state are inconsistent. Interaction feedback can repair a weak ecological context when the local trait/genetic bundle exceeds the current interaction state. These processes can offset one another until the density–interaction headroom becomes too small; once demographic decline lowers q and lower q further lowers demography, the failure gate can convert local deterioration into widespread functional loss.

This framework gives a sharper interpretation to contrasting natural systems without treating them as validation data. In *Crepis sancta*, low local flowering density is associated with reduced pollinator activity and reproduction despite broader movement, consistent with insufficient buffering. On Miyake-jima, reduced floral resources are accompanied by broader *Zosterops* movement and pollen mixing, a plausible real-world analogue of recoupling in which movement repairs local functional mismatch. In *Conospermum undulatum*, current pollen connectivity and reproduction can deteriorate while adult neutral genetics retain a historical signal, adding a memory axis that the current finite closure does not model explicitly. *Spondias purpurea* illustrates more coordinated decline across visitation, pollen flow, reproductive function and younger-cohort genetics. These systems motivate measurements of sorting, repair and memory; they do not replicate the simulator.

The same logic revises the earlier urban–island comparison. `Urban`, `island`, forest fragment and volcanic disturbance are upstream histories, not mechanistic states. Different histories can generate similar or different balances of local selection, recruitment, movement, mating opportunity and demographic feedback. Existing Honshu–Izu and Zurich archives cannot establish a universal urban–island convergence law because study identity, taxa, state coordinates and endpoints are not harmonized. A prospective comparison should instead ask which operator is active and whether measured repair keeps pace with local sorting and demographic headroom loss.

Monitoring follows the same principle. A warning variable should not be judged only by whether it moves early. The diversity thresholds here responded before every observed loss but could not distinguish event from non-event trajectories. A useful monitoring design for functional collapse should measure direct function, local interaction state, trait and cohort-specific genetic state, process-specific movement or mating connectivity, and the cross-layer relations among them. More importantly, repeated measurements should estimate **rates of sorting, buffering and recoupling**, because the same marginal state can have different futures depending on which operator currently dominates.

The claim remains bounded. The algebraic weights, `q*=0.625` switch, generation horizons, density headroom and intervention effects belong to the declared finite closure. The work does not establish q-dependent allele sorting as a universal natural mechanism, does not assert a universal natural recruitment or recoupling law, and does not equate the model generations with natural timescales. What it establishes is a constructive and prospectively tested possibility: matched marginals can hide different transitions, and those differences can be traced to identifiable life-cycle operators whose competing effects determine functional fate.

Functional vulnerability under fragmentation is therefore not only a property of what remains, nor only of how components are aligned at one moment. It is a property of **which processes are sorting functional compatibility, which processes are repairing mismatch, and whether demographic feedback has consumed the headroom for repair**.

## Methods

### Evidence architecture

Load-bearing evidence is restricted to the theorem-guided parent framework, the state/transition-validity programme, the prospectively locked relational mechanism experiment, the prospectively locked edge-decomposition experiment, the prospectively locked focused allele-sorting proof, and the frozen full-denominator warning audit. The recruitment, direct-feedback and density-gate theorems are exact derivations of already declared operators; their paired endpoint contrasts are derived only from locked workflow artifacts. Published natural systems and the separate natural-data measurement programme are Discussion-level projections only.

### Fragmentation and transition sufficiency

The fixed-area fragmentation gradient used 1,200 attempted fresh source preparations, of which 1,037 satisfied the required high-state preparation before projection across the eight patch counts. State variables were preserved according to the declared projection contract. For transition sufficiency, the aligned/reversed pair fixed all retained marginals and changed only cross-layer spatial association. Exact generation-1 interaction fields were evaluated before long-horizon outcomes.

### Prospectively locked mechanism experiments

The six-condition relational mechanism protocol fixed four full-feedback trait-by-allele assignments and two q-only conditions, the initial states, forcing path, horizons, seed map and functional-loss endpoint before outcomes were opened. Each condition used 1,500 trajectories and the same trajectory seed within each master-seed/replicate block across all six conditions.

The separate pathway edge-decomposition protocol retained the q-only support weights `(1,0,0)`, zero migration and mutation, the same AA/RR states, forcing and endpoint. Five fresh master seeds with 300 replicates each yielded 1,500 paired keys per intervention. The preregistered estimand was

\[
\Delta_{DID}=(RR-AA)_{baseline}-(RR-AA)_{deletion}.
\]

No additional edge variants, barriers, thresholds or horizons were opened after outcomes.

### Focused allele-sorting proof

The focused single-edge protocol allowed only baseline local q-dependent allele selection and an otherwise identical condition in which local q was replaced by the spatial mean q in the allele-selection step. Twelve fresh master seeds with 500 replicates each yielded 6,000 paired keys per condition. The primary horizon was generation 40, and replication could not be extended after the first outcome file. The exact allele-selection theorem follows from `W(1;q)=0.5+0.8q` and selection strength 0.5.

### Exact buffering, recoupling and failure-gate derivations

For two-kernel recruitment, the high-trait mass identity follows because the low and high kernels have disjoint support relative to the declared high-trait cutoff. With inheritance weight 0.5, recruit high-trait mass is the arithmetic mean of resident high-trait mass and high-allele frequency.

For direct feedback, define `B=(0.3T+0.1G)/0.4`. The support identity `S=0.6q+0.4B` gives the mismatch contraction directly. Applying `logit(sigmoid(x))=x` to the full and q-only q updates yields the exact transition log-odds shift. The paired full-versus-q-only risk contrasts are secondary derivations from the original locked six-condition records; no new simulations were run.

For the density gate, `d=min(1,N/K)` gives a strictly positive q response to N below carrying capacity. Combining this with the smooth pre-rounding demographic derivative gives a positive q–N–q loop. Solving the q update for the target `q*=0.625` yields `dq >= theta + 0.1135168053`. Paired risk reductions are derived from the already locked density-edge intervention.

### Warning denominator audit

The six frozen markers were the first post-baseline generations at which `H_alpha` or `H_gamma` declined 5%, 10% or 20% from baseline. The inherited ensemble contained 35 losses and 48 non-events; the independently seeded fresh ensemble contained 33 losses and 49 non-events. Thresholds, eligibility, horizon and event definition were not recalibrated.

### Natural projection boundary

Natural examples are not external validation of the finite closure. No cross-system effect is pooled, no urban–island equality is estimated, and no mechanistic weight is inferred from those archives. Their role is to motivate candidate real-world sorting, buffering, recoupling and memory processes for future synchronized empirical tests.

### Reproducibility

All load-bearing finite results are version controlled with locked protocols, machine-readable summaries and workflow artifacts. The relational mechanism decomposition is pinned to workflow `34012983845`, job `101431872354`, artifact `9983093178`, digest `sha256:843a6bdc4a4d4e9de10ce6346cca27a1a863b1780573f000c0f1ab164a81c7ac`. The pathway edge decomposition is pinned to workflow `34014537015`, artifact `9983623440`, digest `sha256:45b38de7514dac8df356579156d994fbc5728e8924308299b2b73571b3595842`. The focused allele-sorting proof is pinned to workflow `34016797940`, job `101441868527`, artifact `9984306657`, digest `sha256:61a07cc6a8680a59185537b03abdca85d0f172a65d068ee9661dd9f2fb448c2d`. Later theorem and manuscript edits do not generate replacement scientific ensembles.
