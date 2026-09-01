# Joint state representation defines eco-genetic predictability before warning validity

**Publication status:** active state-validity manuscript. This manuscript owns only the constructive joint-state, next-transition, and process-portability claims. Natural-data measurement-gate results have been moved to the deferred four-gate empirical program in `natural_data_four_gate_program.md`. This manuscript does not claim validated predictive genetic warning.

## Abstract

Ecological forecasts depend on whether measured summaries preserve the state governing what happens next. In a finite multipatch model, two states with identical census, interaction, allele-frequency and trait marginals, `H_alpha`, `H_gamma`, and `F_ST` but opposite patchwise cross-layer alignment had next interaction transitions differing by 0.2543. A fixed 500-pair campaign did not establish a directional long-horizon loss-risk effect. Portability tests further showed that one historical allele-mixing pattern did not reproduce in fresh seeds or transfer to whole-individual and pollen-only movement closures. These results separate transition-sufficient state representation from coarse marginal similarity and from scalar labels attached to different biological operators. They do not establish state completeness, operator equivalence, or predictive warning validity.

## Introduction

Population persistence, ecological function, interaction support, genetic diversity, allele persistence, and realised trait occupancy are related but are not interchangeable states. A representation is useful for forecasting only if it preserves the distinctions that determine the downstream quantity under the declared dynamics. Matching marginal summaries may therefore be insufficient when local interactions depend on how ecological, genetic, and trait layers are aligned in space.

A second problem is portability. The same numeric value attached to an allele-frequency mixer, whole-individual dispersal operator, or pollen-only gene-flow operator does not define one common biological connectivity state. Process labels must therefore remain tied to the operator that gives them meaning.

We combine a constructive state counterexample with frozen portability and negative tests. The claim is deliberately bounded: coarse marginal equality does not guarantee transition equality, and a pattern observed under one connectivity operator cannot be transferred to another merely because the scalar parameter value looks comparable.

## Methods

### Complete state and a constructive coarse-state contrast

Under the declared parent closure, the simulator is Markov in its complete explicit present state together with the future forcing and stochastic law. We constructed two two-patch states that held habitat area, census, interaction-state multiset, allele-frequency multiset, realised high-trait-mass multiset, complete trait-bin totals, `H_alpha`, `H_gamma`, and `F_ST` fixed while reversing the patchwise alignment between interaction support and the genetic/trait-support bundle.

The primary certificate compared the exact one-generation transition before a long-horizon outcome was inspected. A single preregistered 60-generation deterioration schedule then compared 500 paired aligned and anti-aligned trajectories. No warning endpoints, replacement seeds, alternative alignment permutations, or altered schedules were opened after the result.

### Frozen portability and negative model tests

The historical allele-frequency-mixing screen used the operator `p_i'=(1-m)p_i+m*p_bar`. This is allele-frequency mixing, not demographic, individual, pollen, seed, or pollinator movement. Its historical `m=.10` between-block pattern was tested once in an independently seeded fixed Phase-U ensemble. Distinct preregistered closures then represented post-recruitment whole-individual dispersal and paternal pollen-only gene flow in the historical seed family. A separate matched-expected-support experiment compared constant, even-dynamic, and dominant-dynamic partner architectures. These tests withheld warning outcomes and retained their prospective stop rules.

## Results

### Coarse state equality did not guarantee the same next transition

The aligned and anti-aligned states had identical declared coarse marginal signatures, while cross-layer covariance changed from `+0.025` to `-0.025`. Their exact opening transitions differed patchwise, with a maximum generation-1 interaction difference of **0.2543**. The declared marginals and standard diversity statistics were therefore not transition-sufficient representations of the local dynamics.

Across the fixed 500 paired trajectories, realised functional loss occurred in 339 aligned trajectories (`0.678`) and 361 anti-aligned trajectories (`0.722`). There were 92 aligned-loss/anti-no-loss and 114 aligned-no-loss/anti-loss switches; exact McNemar `p=.143`. The campaign established transition-level representation insufficiency, **not a directional long-horizon loss-incidence effect**.

### A scalar connectivity label did not transport across seeds or mechanisms

Within one historical seed family, only allele-frequency mixing at `m=.10` showed detectable excess equal-rate heterogeneity (`p=.0205`). In the single preregistered fresh Phase-U ensemble, equal-rate p values were `.134` at `m=0` and `.745` at `m=.10`; paired McNemar `p=.694`. The historical observation was therefore not independently reproduced.

In the historical family, whole-individual dispersal at `d=.10` produced pooled loss `.606` and equal-rate `p=.811`, with McNemar `p=.143` versus no connectivity. Pollen-only paternal gene flow at `g=.20` produced pooled loss `.532` and equal-rate `p=.728`; paired contrasts were non-significant. The historical allele-mixing pattern did not transport to either process-resolved operator. Matched-expected-support partner dynamics likewise yielded precision-bounded null results and left the adaptive-rewiring gate closed. These are negative, closure-specific results, not equivalence claims or evidence that connectivity and interaction networks are biologically irrelevant.

## Discussion

### State is joint and endpoint-relative

The constructive pair shows why matching standard marginals cannot establish dynamic equivalence. Spatial co-location among interaction support, genetic support, and realised traits can be future-relevant even when every declared layer-wise summary agrees. The weaker long-horizon result is equally important: transition insufficiency does not license a universal signed risk claim.

### Process state is operator-specific

The portability tests establish a second non-identity. A parameter value attached to one mathematical operator is not a transferable biological connectivity state. Seed-family contingency, whole-individual movement, paternal pollen flow, and partner rewiring address different processes and must retain separate labels. A common scalar axis is justified only after the observation and transition maps establish that the operators preserve the distinctions relevant to the target.

### Empirical handoff

The natural-data programme asks the next question: what happens when candidate ecological states are confronted with held-out biological endpoints? Those results are intentionally routed outside this manuscript into `natural_data_four_gate_program.md`, where four empirical outcomes remain separate: residual-context redundancy after an informative partial state, a missing process coordinate, inadequate process proxies, and representation-induced loss of mechanistic information. Keeping those results separate prevents a finite model counterexample from borrowing empirical breadth it does not need and prevents heterogeneous natural systems from being used as validation of the synthetic closure.

### Claim boundary

The model results are finite and closure-specific. Non-significant tests do not establish equivalence. Transition insufficiency does not prove a directional long-horizon risk effect. Failure of one historical connectivity pattern to reproduce or transport does not establish that connectivity is irrelevant. This manuscript makes no claim that the frozen relative-diversity thresholds are validated predictive warnings; that full-denominator validity audit is owned exclusively by `manuscript/warning_validity.md`.

## Data and code availability

The parent and extension repositories remain separate provenance units. Locked model summaries, contracts, negative results, STOP artifacts, workflow identifiers, and source-version metadata are indexed in `manuscript/artifact_index.md`. The publication split changes claim ownership and manuscript presentation only; it does not modify frozen evidence, rerun endpoints, or alter any scientific decision.