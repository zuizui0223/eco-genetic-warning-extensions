# Joint state representation controls transition predictability and process portability in a finite eco-genetic model

**Publication status:** active state-validity manuscript. This manuscript owns only the constructive joint-state, next-transition, horizon-dependent propagation, and process-portability claims. Natural-data state-measurement results and full-denominator warning validity are separate studies and are not used as evidence for the claims here.

## Abstract

Ecological forecasts depend on whether measured summaries preserve the state governing what happens next. In a finite multipatch model, two states with identical census, interaction, allele-frequency and trait marginals, `H_alpha`, `H_gamma`, and `F_ST` but opposite patchwise cross-layer alignment had next interaction transitions differing by 0.2543. In the original fixed 500-pair, 60-generation campaign, anti-alignment increased observed loss incidence by 4.4 percentage points relative to alignment, but the paired 95% interval ranged from -1.2 to +10.0 percentage points, so a moderate effect remained compatible with the locked data. A separately locked post-Phase-V propagation experiment then read one common trajectory family at generations 5, 10, 20, and 40 with 1,500 paired trajectories: the anti-aligned minus aligned loss-risk differences were 0.0, +0.33, +5.33, and +5.20 percentage points, respectively; the paired 95% intervals at generations 20 and 40 were +2.04 to +8.62 and +1.96 to +8.44 points. Under the declared forcing path, the cross-layer state difference therefore propagated to a roughly five-point loss-risk contrast between the 10- and 20-generation readouts and remained of similar magnitude through generation 40. Portability tests further showed that one historical allele-mixing pattern did not reproduce in fresh seeds or transfer to whole-individual and pollen-only movement closures. These results separate transition-sufficient state representation from coarse marginal similarity and from scalar labels attached to different biological operators. They do not establish a universal temporal cutoff, state completeness, operator equivalence, or natural-system generality.

## Introduction

Population persistence, ecological function, interaction support, genetic diversity, allele persistence, and realised trait occupancy are related but are not interchangeable states. A representation is useful for forecasting only if it preserves the distinctions that determine the downstream quantity under the declared dynamics. Matching marginal summaries may therefore be insufficient when local interactions depend on how ecological, genetic, and trait layers are aligned in space.

A second problem is portability. The same numeric value attached to an allele-frequency mixer, whole-individual dispersal operator, or pollen-only gene-flow operator does not define one common biological connectivity state. Process labels must therefore remain tied to the operator that gives them meaning.

We combine a constructive state counterexample with a frozen propagation experiment and process-specific portability tests. The claim is deliberately bounded: coarse marginal equality does not guarantee transition equality; a hidden alignment difference can propagate to a measurable downstream risk contrast under the declared dynamics; and a pattern observed under one connectivity operator cannot be transferred to another merely because the scalar parameter value looks comparable.

## Methods

### Complete state and a constructive coarse-state contrast

Under the declared parent closure, the simulator is Markov in its complete explicit present state together with the future forcing and stochastic law. We constructed two two-patch states that held habitat area, census, interaction-state multiset, allele-frequency multiset, realised high-trait-mass multiset, complete trait-bin totals, `H_alpha`, `H_gamma`, and `F_ST` fixed while reversing the patchwise alignment between interaction support and the genetic/trait-support bundle.

The primary certificate compared the exact one-generation transition before a long-horizon outcome was inspected. A single preregistered 60-generation deterioration schedule then compared 500 paired aligned and anti-aligned trajectories. No replacement seeds, alternative alignment permutations, altered schedules, or post-result endpoint changes were opened after the result.

For that paired 60-generation loss contrast, the estimand is the anti-aligned minus aligned risk difference. With 114 aligned-no-loss/anti-loss pairs, 92 aligned-loss/anti-no-loss pairs, and 500 total pairs, the observed difference is `(114-92)/500 = 0.044`. We report a paired large-sample 95% interval using the variance of the paired difference variable `D in {-1,0,1}`: `Var(D) = (114+92)/500 - 0.044^2`, divided by 500 for the variance of the mean. This gives a 95% interval of approximately `[-0.012, 0.100]`. The interval is descriptive for the locked campaign and is not a post-hoc acceptance rule.

### Post-Phase-V propagation experiment

After the original Phase-V result had been frozen, a separate propagation protocol was locked before opening its outcomes. The experiment changed neither the aligned/anti-aligned state values nor the Phase-V result. It extended only the readout horizon and paired replication.

The future barrier followed the original 60-generation linear forcing rate, `0.50 + (0.65-0.50) g/60`, and was truncated rather than rescaled. Each aligned/anti-aligned pair was simulated once to generation 40, then read at the predeclared horizons 5, 10, 20, and 40. Five master seeds and the original deterministic pair-seed mapping were retained. Nested prefixes of 100, 200, and 300 replicates per master seed yielded 500, 1,000, and 1,500 paired comparisons. The 1,500-pair horizon curve was primary; the smaller nested prefixes were precision diagnostics, not independent experiments.

The primary estimand at every horizon was again anti-aligned minus aligned functional-loss risk with a paired 95% interval. Exact McNemar p values were secondary. All horizon-by-pair-count cells were retained, and the protocol prohibited selecting a biological cutoff because a p value crossed 0.05.

### Frozen portability and negative model tests

The historical allele-frequency-mixing screen used the operator `p_i'=(1-m)p_i+m*p_bar`. This is allele-frequency mixing, not demographic, individual, pollen, seed, or pollinator movement. Its historical `m=.10` between-block pattern was tested once in an independently seeded fixed Phase-U ensemble. Distinct preregistered closures then represented post-recruitment whole-individual dispersal and paternal pollen-only gene flow in the historical seed family. A separate matched-expected-support experiment compared constant, even-dynamic, and dominant-dynamic partner architectures. These tests retained their prospective stop rules.

## Results

### Coarse state equality did not guarantee the same next transition

The aligned and anti-aligned states had identical declared coarse marginal signatures, while cross-layer covariance changed from `+0.025` to `-0.025`. Their exact opening transitions differed patchwise, with a maximum generation-1 interaction difference of **0.2543**. The declared marginals and standard diversity statistics were therefore not transition-sufficient representations of the local dynamics.

Across the original fixed 500 paired trajectories at generation 60, realised functional loss occurred in 339 aligned trajectories (`0.678`) and 361 anti-aligned trajectories (`0.722`). The observed anti-aligned minus aligned loss-risk difference was therefore **+4.4 percentage points**. The 114 aligned-no-loss/anti-loss and 92 aligned-loss/anti-no-loss discordant pairs give a paired large-sample **95% CI of approximately -1.2 to +10.0 percentage points**; exact McNemar `p=.143`. Relative to the aligned baseline risk of `0.678`, the upper confidence limit corresponds to about a **14.8% relative increase**. The original campaign therefore did not establish a signed long-horizon effect, but it also did not exclude effects of roughly this magnitude.

### Propagation was horizon-dependent and the 500-pair contrast was imprecise

In the separately locked 1,500-pair propagation cohort, neither condition had a realised loss by generation 5, giving a risk difference of **0.0 points**. By generation 10, loss occurred in 15 aligned and 20 anti-aligned trajectories, for a difference of **+0.33 points** (95% CI **-0.44 to +1.11**). By generation 20, the corresponding counts were 504 and 584 and the difference was **+5.33 points** (95% CI **+2.04 to +8.62**). At generation 40, counts were 979 and 1,057 and the difference remained **+5.20 points** (95% CI **+1.96 to +8.44**).

The nested replication prefixes separated effect magnitude from precision. At generation 20, the estimated excess risk was +5.4 points at 500 pairs (95% CI -0.46 to +11.26), +5.9 at 1,000 pairs (+1.83 to +9.97), and +5.33 at 1,500 pairs (+2.04 to +8.62). At generation 40, the corresponding estimates were +4.4 points (-1.29 to +10.09), +6.4 (+2.44 to +10.36), and +5.2 (+1.96 to +8.44). Thus the 500-pair intervals could span zero while the effect-size estimates remained similar and the larger paired samples narrowed uncertainty.

Under this declared deterioration path, the directional contrast was therefore essentially absent at the 5- and 10-generation readouts, had reached about five percentage points by generation 20, and remained of similar magnitude at generation 40. The experiment supports a quantitative propagation timescale **between the 10- and 20-generation readouts**; it does not identify generation 20 as a universal or exact biological cutoff.

### A scalar connectivity label did not transport across seeds or mechanisms

Within one historical seed family, only allele-frequency mixing at `m=.10` showed detectable excess equal-rate heterogeneity (`p=.0205`). In the single preregistered fresh Phase-U ensemble, equal-rate p values were `.134` at `m=0` and `.745` at `m=.10`; paired McNemar `p=.694`. The historical observation was therefore not independently reproduced.

In the historical family, whole-individual dispersal at `d=.10` produced pooled loss `.606` and equal-rate `p=.811`, with McNemar `p=.143` versus no connectivity. Pollen-only paternal gene flow at `g=.20` produced pooled loss `.532` and equal-rate `p=.728`; paired contrasts were non-significant. The historical allele-mixing pattern did not transport to either process-resolved operator. Matched-expected-support partner dynamics likewise yielded precision-bounded null results and left the adaptive-rewiring gate closed. These are negative, closure-specific results, not equivalence claims or evidence that connectivity and interaction networks are biologically irrelevant.

## Discussion

### State is joint, endpoint-relative, and can propagate on a measurable timescale

The constructive pair shows why matching standard marginals cannot establish dynamic equivalence. Spatial co-location among interaction support, genetic support, and realised traits can be future-relevant even when every declared layer-wise summary agrees.

The original 500-pair 60-generation comparison was correctly unresolved by its interval rather than interpreted as evidence of no effect. The separately locked propagation experiment explains why that distinction mattered: with 1,500 paired trajectories the same state contrast produced almost no risk difference at generations 5–10 but about a five-point excess anti-aligned loss risk at generations 20 and 40. The nested 500/1,000/1,500 prefixes further show that the principal change with replication was interval width, not a dramatic change in the estimated 20–40 generation effect magnitude.

This is a stronger state-validity result than a p-value-only null, but it remains closure-specific. The four readout horizons locate the emergence of the contrast only coarsely, between the declared 10- and 20-generation readouts. They do not identify a universal transition time or prove that the same temporal propagation occurs in nature.

### Process state is operator-specific

The portability tests establish a second non-identity. A parameter value attached to one mathematical operator is not a transferable biological connectivity state. Seed-family contingency, whole-individual movement, paternal pollen flow, and partner rewiring address different processes and must retain separate labels. A common scalar axis is justified only after the observation and transition maps establish that the operators preserve the distinctions relevant to the target.

### Relationship to separate empirical and warning-validity studies

The present paper does not use heterogeneous natural systems to validate the finite model, and it does not use the model-state result to validate a warning rule. A separate natural-data study evaluates measurement and representation gates using held-out biological endpoints. A separate full-denominator study evaluates frozen genetic-diversity warning rules. Those studies answer different inferential questions and are not evidence layers for the state-transition and process-portability claims here.

### Claim boundary

The model results are finite and closure-specific. Non-significant tests do not establish equivalence. The original 500-pair Phase-V comparison remains a frozen, imprecise 60-generation result; the post-Phase-V experiment is a separate, prospectively locked extension and is not relabelled as part of the original preregistration. The propagation experiment supports an approximately five-point anti-aligned excess loss risk by the declared generation-20 readout, maintained at generation 40, after little contrast at generations 5–10. It does not establish generation 20 as a true cutoff or a natural-system timescale. Failure of one historical connectivity pattern to reproduce or transport does not establish that connectivity is irrelevant. This manuscript does not claim predictive validity for any genetic warning statistic.

## Data and code availability

The parent and extension repositories remain separate provenance units. The original Phase-V result remains fixed by its existing locked artifact. The post-Phase-V propagation protocol, implementation, successful workflow provenance, complete 12-cell compact result, and result interpretation boundary are stored in `experiments/alignment_propagation_protocol.json`, `src/eco_genetic_warning_extensions/alignment_propagation_experiment.py`, `artifacts/alignment_propagation/locked_summary.json`, and `docs/ALIGNMENT_PROPAGATION_RESULT_2026-09-04.md`. Process-portability evidence and precision-bounded negative results are preserved in version-controlled high-precision condition maps and audit artifacts. No warning-validity or natural-data result is required to reproduce the claims of this manuscript.
