# Joint state representation defines eco-genetic predictability before warning validity

**Publication status:** active state-validity manuscript. This manuscript owns the constructive joint-state, next-transition, propagation-horizon, and process-portability claims. Natural-data measurement-gate development is now authoritative in `zuizui0223/egwee`; the local `natural_data_four_gate_program.md` is retained for provenance and validator stability. This manuscript does not claim validated predictive genetic warning.

## Abstract

Ecological forecasts depend on whether measured summaries preserve the state relevant to a declared target and forecast horizon. In a finite four-patch model, two states with identical census, interaction, allele-frequency and trait marginals, `H_alpha`, `H_gamma`, and `F_ST` but opposite patchwise cross-layer alignment had next interaction transitions differing by 0.2543. A prospectively fixed replay of the same 500 paired trajectories showed that the median maximum patchwise interaction difference first amplified to 0.3455 at generation 2 and then fell below half its generation-1 value by generation 10. The terminal anti-aligned minus aligned loss-risk difference was +4.4 percentage points; a paired pointwise 95% interval was -1.2 to +10.0 percentage points, while the preregistered simultaneous seven-horizon family likewise did not establish a signed long-horizon effect. Paired loss status nevertheless remained discordant in 45.0% of pairs at generation 20 and 41.2% at generation 60. Portability tests further showed that one historical allele-mixing pattern did not reproduce in fresh seeds or transfer to whole-individual and pollen-only movement closures. These results show that representation adequacy is target- and horizon-relative: a state distinction can matter strongly for local transitions and paired trajectory identity without establishing a portable signed shift in marginal long-horizon risk.

## Introduction

Population persistence, ecological function, interaction support, genetic diversity, allele persistence, and realised trait occupancy are related but are not interchangeable states. A representation is useful for forecasting only if it preserves the distinctions that determine the downstream quantity under the declared dynamics. Matching marginal summaries may therefore be insufficient when local interactions depend on how ecological, genetic, and trait layers are aligned in space.

Sufficiency is also relative to the prediction target and forecast horizon. A distinction that changes the next transition need not induce the same signed difference in a coarse binary endpoint many generations later. Conversely, similar marginal endpoint incidence need not imply that the same paired trajectories reach the endpoint. Transition state, trajectory identity and marginal event risk are therefore separate predictive objects.

A second problem is portability. The same numeric value attached to an allele-frequency mixer, whole-individual dispersal operator, or pollen-only gene-flow operator does not define one common biological connectivity state. Process labels must therefore remain tied to the operator that gives them meaning.

We combine a constructive state counterexample, a prospectively fixed propagation audit, and frozen portability and negative tests. The claim is deliberately bounded: coarse marginal equality does not guarantee transition equality; the relevance of a state distinction can change across horizon and endpoint; and a pattern observed under one connectivity operator cannot be transferred to another merely because the scalar parameter value looks comparable.

## Methods

### Complete state and a constructive coarse-state contrast

Under the declared parent closure, the simulator is Markov in its complete explicit present state together with the future forcing and stochastic law. We constructed two four-patch states that held habitat area, census, interaction-state multiset, allele-frequency multiset, realised high-trait-mass multiset, complete trait-bin totals, `H_alpha`, `H_gamma`, and `F_ST` fixed while reversing the patchwise alignment between interaction support and the genetic/trait-support bundle.

The primary certificate compared the exact one-generation transition before a long-horizon outcome was inspected. A single preregistered 60-generation deterioration schedule then compared 500 paired aligned and anti-aligned trajectories. No warning endpoints, replacement seeds, alternative alignment permutations, or altered schedules were opened after the result.

For the terminal paired loss contrast, the descriptive estimand is the anti-aligned minus aligned risk difference. With 114 aligned-no-loss/anti-loss pairs, 92 aligned-loss/anti-no-loss pairs and 500 total pairs, the observed difference is `(114-92)/500 = 0.044`. We report the paired large-sample pointwise 95% interval from the variance of the paired difference variable `D in {-1,0,1}`: `Var(D) = (114+92)/500 - 0.044^2`, divided by 500 for the variance of the mean. This yields approximately `[-0.012, 0.100]`. This interval is descriptive for the locked terminal campaign and is distinct from the prospectively specified simultaneous horizon-family band below; it is not a post-hoc acceptance rule.

### Prospective propagation audit

After the generation-1 versus generation-60 boundary was already known, we preregistered a post-review propagation audit before inspecting any intermediate-generation Phase-V snapshot outcomes. The audit replayed the exact historical 500 pair keys, five master seeds, trajectory-seed mapping, initial states, zero-migration/zero-mutation closure, and 60-generation barrier schedule. Intermediate state was read only at the fixed horizons `1, 2, 5, 10, 20, 40, 60`.

The primary propagation coordinate was the maximum absolute patchwise aligned-versus-anti-aligned interaction difference for each pair. Required secondary coordinates tracked mean absolute patchwise differences in interaction, census, local effective size, high-allele frequency and realised high-trait mass, plus absolute differences in `H_alpha`, `H_gamma`, and finite `F_ST`. The preregistered half-retention horizon was the first fixed horizon at which the median primary interaction distance was at or below half its generation-1 value and remained at or below that level at every later fixed horizon. No continuous half-life or exponential decay model was fitted.

Cumulative realised functional loss was evaluated at the same fixed horizons. For each horizon we retained marginal loss rates, the paired 2x2 table and discordant-pair fraction. A single 10,000-draw pair-cluster bootstrap, RNG seed `20260904`, supplied a simultaneous non-studentized 95% band for the seven-horizon anti-aligned-minus-aligned paired risk-difference family. No intermediate unadjusted test could promote a horizon outside this family rule. A reproduction gate required exact recovery of the historical generation-1 certificate and the complete generation-60 paired loss table before intermediate outcomes were interpreted.

### Frozen portability and negative model tests

The historical allele-frequency-mixing screen used the operator `p_i'=(1-m)p_i+m*p_bar`. This is allele-frequency mixing, not demographic, individual, pollen, seed, or pollinator movement. Its historical `m=.10` between-block pattern was tested once in an independently seeded fixed Phase-U ensemble. Distinct preregistered closures then represented post-recruitment whole-individual dispersal and paternal pollen-only gene flow in the historical seed family. A separate matched-expected-support experiment compared constant, even-dynamic, and dominant-dynamic partner architectures. These tests withheld warning outcomes and retained their prospective stop rules.

## Results

### Coarse state equality did not guarantee the same next transition

The aligned and anti-aligned states had identical declared coarse marginal signatures, while cross-layer covariance changed from `+0.025` to `-0.025`. Their exact opening transitions differed patchwise, with a maximum generation-1 interaction difference of **0.2543**. The declared marginals and standard diversity statistics were therefore not transition-sufficient representations of the local dynamics.

Across the fixed 500 paired trajectories, realised functional loss occurred in 339 aligned trajectories (`0.678`) and 361 anti-aligned trajectories (`0.722`). The observed anti-aligned minus aligned loss-risk difference was therefore **+4.4 percentage points**. The 114 aligned-no-loss/anti-loss and 92 aligned-loss/anti-no-loss discordant pairs give a paired pointwise **95% CI of approximately -1.2 to +10.0 percentage points**; exact McNemar `p=.143`. Relative to the aligned baseline risk of `0.678`, the upper pointwise confidence limit corresponds to about a **14.8% relative increase**. The original campaign therefore established transition-level representation insufficiency, but **does not establish a signed long-horizon effect** and does not exclude effects of roughly this magnitude.

### Interaction-state memory amplified briefly and then attenuated

The propagation replay passed every historical reproduction check. The median maximum patchwise interaction distance was `0.2543` at generation 1, increased to **`0.3455` at generation 2**, declined to `0.1618` at generation 5, and reached `0.0903` at generation 10. The preregistered half-retention level was `0.1272`; generation 10 was the first fixed horizon below that level with all later horizons remaining below it. The classification was therefore **`attenuating_representation_memory` with half-retention horizon 10 generations**.

The later median maximum interaction distances were `0.0761`, `0.0862`, and `0.0696` at generations 20, 40 and 60. The early generation-2 amplification rules out describing this observed fixed-grid curve as simple monotone exponential decay. Secondary state coordinates propagated differently: patchwise high-allele-frequency and realised high-trait-mass contrasts remained substantial after the primary interaction contrast had attenuated, so the generation-10 result is not a universal memory timescale for the complete state.

### Marginal loss incidence remained directionally unresolved, but paired trajectory status remained sensitive

No cumulative loss occurred by generations 1, 2 or 5. At generation 10, aligned and anti-aligned cumulative loss was `8/500` and `10/500`. At generation 20 it was `169/500` and `196/500`; at generation 40, `334/500` and `356/500`; and at generation 60, `339/500` and `361/500`.

Using the anti-aligned-minus-aligned convention, paired risk differences were `0` at generation 1, `+0.004` at generations 2 and 5, `0` at generation 10, `+0.054` at generation 20, and `+0.044` at generations 40 and 60. The simultaneous seven-horizon 95% band had half-width `0.066` and included zero at every fixed horizon. Thus the preregistered family decision was **`no_detected_horizon_family_loss_incidence_separation`**. At generation 60 this simultaneous familywise band is approximately `[-0.022, +0.110]`, whereas the separately reported terminal pointwise paired interval is approximately `[-0.012, +0.100]`; both retain the observed +4.4-point direction while leaving its sign unresolved.

The paired endpoint identities told a different story. Once loss became common, cumulative-loss status differed between the aligned and anti-aligned members of **225/500 pairs (`45.0%`) at generation 20**, **212/500 (`42.4%`) at generation 40**, and **206/500 (`41.2%`) at generation 60**. This is paired trajectory-status sensitivity under the common historical seed map, not a signed marginal-risk result and not a deterministic biological counterfactual claim.

### A scalar connectivity label did not transport across seeds or mechanisms

Within one historical seed family, only allele-frequency mixing at `m=.10` showed detectable excess equal-rate heterogeneity (`p=.0205`). In the single preregistered fresh Phase-U ensemble, equal-rate p values were `.134` at `m=0` and `.745` at `m=.10`; paired McNemar `p=.694`. The historical observation was therefore not independently reproduced.

In the historical family, whole-individual dispersal at `d=.10` produced pooled loss `.606` and equal-rate `p=.811`, with McNemar `p=.143` versus no connectivity. Pollen-only paternal gene flow at `g=.20` produced pooled loss `.532` and equal-rate `p=.728`; paired contrasts were non-significant. The historical allele-mixing pattern did not transport to either process-resolved operator. Matched-expected-support partner dynamics likewise yielded precision-bounded null results and left the adaptive-rewiring gate closed. These are negative, closure-specific results, not equivalence claims or evidence that connectivity and interaction networks are biologically irrelevant.

## Discussion

### State is joint, target-relative and horizon-relative

The constructive pair shows why matching standard marginals cannot establish dynamic equivalence. Spatial co-location among interaction support, genetic support, and realised traits can be future-relevant even when every declared layer-wise summary agrees.

The propagation result sharpens that statement. The initial alignment difference was not simply carried forward at constant strength: its interaction consequence transiently amplified, then attenuated below the fixed half-retention level by generation 10. At the same time, the complete simultaneous horizon family did not establish a signed cumulative-loss incidence difference, even though the identities of paired trajectories reaching the loss endpoint remained highly sensitive to the alignment contrast after loss onset.

The terminal comparison should be read by its interval rather than by `p=.143` alone. Anti-alignment was associated with an observed +4.4 percentage-point loss-risk difference at generation 60, but the pointwise paired 95% interval ranged from -1.2 to +10.0 percentage points and the simultaneous horizon-family interval was wider. The locked data therefore remain compatible with a moderate directional effect as well as with zero.

Thus **transition representation, paired trajectory identity, and marginal endpoint risk are distinct predictive targets**. A representation can be insufficient for one-step transitions and important for which paired trajectories cross an endpoint without yielding an established portable directional shift in population-level endpoint incidence. The generation-10 interaction attenuation is likewise not a universal ecological timescale.

### This propagation result does not explain warning failure

The separate full-denominator warning-validity audit addresses a different inferential failure. A diversity threshold can precede observed losses yet fail to discriminate event from non-event trajectories. Nothing in the propagation audit shows that those frozen warning rules failed because cross-layer alignment was omitted, and no warning threshold was rerun with alignment information.

The defensible common principle is more abstract: **information for one inferential target does not guarantee adequacy for another**. Event-conditioned temporal precedence is not predictive discrimination; next-transition relevance is not signed long-horizon marginal risk; and paired trajectory-status sensitivity is not the same estimand as marginal incidence. This manuscript therefore does not claim that joint-state representation repairs or validates the frozen warning rules.

### Process state is operator-specific

The portability tests establish a second non-identity. A parameter value attached to one mathematical operator is not a transferable biological connectivity state. Seed-family contingency, whole-individual movement, paternal pollen flow, and partner rewiring address different processes and must retain separate labels. A common scalar axis is justified only after the observation and transition maps establish that the operators preserve the distinctions relevant to the target.

### Empirical handoff

The natural-data programme asks the next question: what happens when candidate ecological states are confronted with held-out biological endpoints? That independent four-gate programme is now developed in `zuizui0223/egwee`; the local provenance file `natural_data_four_gate_program.md` remains intentionally outside this manuscript. Keeping those results separate prevents a finite model representation result from borrowing empirical breadth it does not need and prevents heterogeneous natural systems from being used as validation of the synthetic closure.

### Claim boundary

The model results are finite and closure-specific. **Non-significant tests do not establish equivalence.** The terminal pointwise paired interval remains **-1.2 to +10.0 percentage points** around the observed anti-aligned minus aligned difference, and the simultaneous horizon-family band also includes moderate signed effects. Transition insufficiency therefore does not prove a directional long-horizon risk effect, but neither does the locked long-horizon comparison establish a negligible effect. The propagation replay is not an independent replication and does not define a universal ten-generation memory scale. Failure of one historical connectivity pattern to reproduce or transport does not establish that connectivity is irrelevant. This manuscript makes no claim that the frozen relative-diversity thresholds are validated predictive warnings; that full-denominator validity audit is owned exclusively by `manuscript/warning_validity.md`.

## Data and code availability

The parent and extension repositories remain separate provenance units. The propagation protocol, prospective amendment, locked result and implementation are recorded in `docs/CROSS_LAYER_ALIGNMENT_PROPAGATION_PREREGISTRATION.md`, `docs/CROSS_LAYER_ALIGNMENT_PROPAGATION_AMENDMENT_001.md`, and `docs/CROSS_LAYER_ALIGNMENT_PROPAGATION_RESULT.md`, with the exact historical Phase-V and parent scientific commits pinned there. Locked model summaries, contracts, negative results, STOP artifacts, workflow identifiers, and source-version metadata remain indexed in `manuscript/artifact_index.md`. The publication split changes claim ownership and manuscript presentation only; it does not modify frozen warning evidence or retrospectively alter the historical Phase-V decision.