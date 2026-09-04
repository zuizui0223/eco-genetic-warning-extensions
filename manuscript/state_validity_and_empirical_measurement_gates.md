# Matching eco-genetic summaries can hide different ecological futures

**Publication status:** active state-validity manuscript. This manuscript owns the constructive joint-state, next-transition, propagation-horizon, and process-portability claims. Natural-data measurement-gate development is authoritative in `zuizui0223/egwee`; the local `natural_data_four_gate_program.md` is retained for provenance and validator stability. This manuscript does not claim validated predictive genetic warning.

## Abstract

Ecological forecasts depend not only on the declared dynamics but also on whether measured summaries preserve the state relevant to the prediction target and horizon. In a finite multipatch model, two states with identical census, interaction, allele-frequency and trait marginals, `H_alpha`, `H_gamma`, and `F_ST` but opposite patchwise cross-layer alignment had next interaction transitions differing by 0.2543. In the original fixed 500-pair, 60-generation campaign, anti-alignment increased observed loss incidence by 4.4 percentage points relative to alignment, but the paired 95% interval ranged from -1.2 to +10.0 percentage points, so a moderate effect remained compatible with the locked data. A separately prospectively locked post-Phase-V propagation experiment then read one common forcing path at generations 5, 10, 20, and 40 with 1,500 paired trajectories. Anti-aligned minus aligned loss-risk differences were 0.0, +0.33, +5.33, and +5.20 percentage points, respectively; paired 95% intervals at generations 20 and 40 were +2.04 to +8.62 and +1.96 to +8.44 points. Under this closure, a state distinction erased by standard marginals was already transition-relevant and propagated to a roughly five-point functional-loss risk contrast between the 10- and 20-generation readouts, maintained through generation 40. Portability tests further showed that one historical allele-mixing pattern did not reproduce in fresh seeds or transfer to whole-individual and pollen-only movement closures. Matching ecological and genetic summaries therefore does not establish dynamic equivalence: representation adequacy is target-, horizon-, and operator-dependent. The results do not establish a universal temporal cutoff, state completeness, operator equivalence, or predictive warning validity.

## Introduction

Ecological forecasting requires a declared prediction target, an initial state, and a forecast horizon. The broader forecasting literature has long emphasized explicit quantitative prediction and iterative confrontation with future observations (Clark et al. 2001; Dietze et al. 2018), while the ecological forecast-horizon framework makes the further point that useful predictability can change with temporal distance and with the ecological quantity being predicted (Petchey et al. 2015). A less explicit but logically prior question is whether the representation supplied as the present state preserves the distinctions that matter for that target and horizon.

Population persistence, ecological function, interaction support, genetic diversity, allele persistence, and realised trait occupancy are related but are not interchangeable states. Matching their marginal summaries need not imply that their spatial association is also matched. This matters in multilayer ecological systems, where dynamics can depend on interlayer as well as intralayer structure (Pilosof et al. 2017). We therefore ask whether two eco-genetic states that agree on standard layer-wise summaries can nevertheless have different futures because cross-layer spatial alignment has been erased.

A second representation problem is portability. The same numeric value attached to an allele-frequency mixer, whole-individual dispersal operator, or pollen-only gene-flow operator does not define one common biological connectivity state. Fragmented eco-evolutionary systems can couple dispersal, demography, selection, and ecological interactions through different mechanisms (Legrand et al. 2017; Govaert et al. 2019). Process labels must therefore remain tied to the operator that gives them meaning unless an identification argument shows that the alternative representations preserve the same target-relevant distinctions.

We combine three evidence layers. First, a constructive state pair tests whether matching standard marginals guarantees the same next transition. Second, a separately prospectively locked propagation experiment tests how the same aligned/anti-aligned contrast appears across fixed forecast horizons and paired replication. Third, frozen portability and negative model tests ask whether a scalar process label can be transported across seeds and biological movement closures. The claim is deliberately bounded: coarse marginal equality does not guarantee transition equality; the relevance of a hidden state distinction can change with horizon and endpoint; and a pattern observed under one operator cannot be transferred to another merely because the scalar parameter value looks comparable.

## Methods

### Complete state and a constructive coarse-state contrast

Under the declared parent closure, the simulator is Markov in its complete explicit present state together with the future forcing and stochastic law. We constructed two two-patch states that held habitat area, census, interaction-state multiset, allele-frequency multiset, realised high-trait-mass multiset, complete trait-bin totals, `H_alpha`, `H_gamma`, and `F_ST` fixed while reversing the patchwise alignment between interaction support and the genetic/trait-support bundle.

The primary certificate compared the exact one-generation transition before a long-horizon outcome was inspected. A single preregistered 60-generation deterioration schedule then compared 500 paired aligned and anti-aligned trajectories. No warning endpoints, replacement seeds, alternative alignment permutations, or altered schedules were opened after the result.

For that paired 60-generation loss contrast, the estimand is the anti-aligned minus aligned risk difference. With 114 aligned-no-loss/anti-loss pairs, 92 aligned-loss/anti-no-loss pairs, and 500 total pairs, the observed difference is `(114-92)/500 = 0.044`. We report a paired large-sample 95% interval using the variance of the paired difference variable `D in {-1,0,1}`: `Var(D) = (114+92)/500 - 0.044^2`, divided by 500 for the variance of the mean. This gives a 95% interval of approximately `[-0.012, 0.100]`. The interval is descriptive for the locked campaign and is not a post-hoc acceptance rule.

### Post-Phase-V propagation experiment

After the original Phase-V result had been frozen, a separate propagation protocol was locked before opening its outcomes. The experiment changed neither the aligned/anti-aligned state values nor the Phase-V result. It extended only the readout horizon and paired replication.

The future barrier followed the original 60-generation linear forcing rate, `0.50 + (0.65-0.50) g/60`, and was truncated rather than rescaled. Each aligned/anti-aligned pair was simulated once to generation 40, then read at the predeclared horizons 5, 10, 20, and 40. Five master seeds and the original deterministic pair-seed mapping were retained. Nested prefixes of 100, 200, and 300 replicates per master seed yielded 500, 1,000, and 1,500 paired comparisons. The 1,500-pair horizon curve was primary; the smaller nested prefixes were precision diagnostics, not independent experiments.

The primary estimand at every horizon was again anti-aligned minus aligned functional-loss risk with a paired 95% interval. Exact McNemar p values were secondary. All horizon-by-pair-count cells were retained, and the protocol prohibited selecting a biological cutoff because a p value crossed 0.05.

### Frozen portability and negative model tests

The historical allele-frequency-mixing screen used the operator `p_i'=(1-m)p_i+m*p_bar`. This is allele-frequency mixing, not demographic, individual, pollen, seed, or pollinator movement. Its historical `m=.10` between-block pattern was tested once in an independently seeded fixed Phase-U ensemble. Distinct preregistered closures then represented post-recruitment whole-individual dispersal and paternal pollen-only gene flow in the historical seed family. A separate matched-expected-support experiment compared constant, even-dynamic, and dominant-dynamic partner architectures. These tests withheld warning outcomes and retained their prospective stop rules.

## Results

### Coarse state equality did not guarantee the same next transition

The aligned and anti-aligned states had identical declared coarse marginal signatures, while cross-layer covariance changed from `+0.025` to `-0.025`. Their exact opening transitions differed patchwise, with a maximum generation-1 interaction difference of **0.2543**. The declared marginals and standard diversity statistics were therefore not transition-sufficient representations of the local dynamics.

Across the original fixed 500 paired trajectories at generation 60, realised functional loss occurred in 339 aligned trajectories (`0.678`) and 361 anti-aligned trajectories (`0.722`). The observed anti-aligned minus aligned loss-risk difference was therefore **+4.4 percentage points**. The 114 aligned-no-loss/anti-loss and 92 aligned-loss/anti-no-loss discordant pairs give a paired large-sample **95% CI of approximately -1.2 to +10.0 percentage points**; exact McNemar `p=.143`. Relative to the aligned baseline risk of `0.678`, the upper confidence limit corresponds to about a **14.8% relative increase**. The original campaign therefore did not establish a signed long-horizon effect, but it also did not exclude effects of roughly this magnitude. Non-significant tests do not establish equivalence.

### Propagation was horizon-dependent and the 500-pair contrast was imprecise

In the separately locked 1,500-pair propagation cohort, neither condition had a realised loss by generation 5, giving a risk difference of **0.0 points**. By generation 10, loss occurred in 15 aligned and 20 anti-aligned trajectories, for a difference of **+0.33 points** (95% CI **-0.44 to +1.11**). By generation 20, the corresponding counts were 504 and 584 and the difference was **+5.33 points** (95% CI **+2.04 to +8.62**). At generation 40, counts were 979 and 1,057 and the difference remained **+5.20 points** (95% CI **+1.96 to +8.44**).

The nested replication prefixes separated effect magnitude from precision. At generation 20, the estimated excess risk was +5.4 points at 500 pairs (95% CI -0.46 to +11.26), +5.9 at 1,000 pairs (+1.83 to +9.97), and +5.33 at 1,500 pairs (+2.04 to +8.62). At generation 40, the corresponding estimates were +4.4 points (-1.29 to +10.09), +6.4 (+2.44 to +10.36), and +5.2 (+1.96 to +8.44). Thus the 500-pair intervals could span zero while the effect-size estimates remained similar and the larger paired samples narrowed uncertainty.

Under this declared deterioration path, the directional contrast was therefore essentially absent at the 5- and 10-generation readouts, had reached about five percentage points by generation 20, and remained of similar magnitude at generation 40. The experiment supports a quantitative propagation timescale **between the 10- and 20-generation readouts**; it does not establish generation 20 as a universal or exact biological cutoff and does not establish generation 20 as a true cutoff.

### A scalar connectivity label did not transport across seeds or mechanisms

Within one historical seed family, only allele-frequency mixing at `m=.10` showed detectable excess equal-rate heterogeneity (`p=.0205`). In the single preregistered fresh Phase-U ensemble, equal-rate p values were `.134` at `m=0` and `.745` at `m=.10`; paired McNemar `p=.694`. The historical observation was therefore not independently reproduced.

In the historical family, whole-individual dispersal at `d=.10` produced pooled loss `.606` and equal-rate `p=.811`, with McNemar `p=.143` versus no connectivity. Pollen-only paternal gene flow at `g=.20` produced pooled loss `.532` and equal-rate `p=.728`; paired contrasts were non-significant. The historical allele-mixing pattern did not transport to either process-resolved operator. Matched-expected-support partner dynamics likewise yielded precision-bounded null results and left the adaptive-rewiring gate closed. These are negative, closure-specific results, not equivalence claims or evidence that connectivity and interaction networks are biologically irrelevant.

## Discussion

### State representation is joint and horizon-relative

The constructive pair shows why matching standard marginals cannot establish dynamic equivalence. Spatial co-location among interaction support, genetic support, and realised traits can be future-relevant even when every declared layer-wise summary agrees. In multilayer language, a layer-wise summary can preserve the components while discarding interlayer organization (Pilosof et al. 2017); the present counterexample shows that such discarded alignment can change the next transition under the declared dynamics.

The propagation experiment then adds the time dimension. Ecological forecast horizons are explicitly target-dependent (Petchey et al. 2015), and our result isolates one mechanism by which the predictive relevance of an initial representation can change across horizon. The aligned/anti-aligned contrast produced almost no functional-loss risk difference at generations 5–10 but about a five-point excess anti-aligned risk at generations 20 and 40. This is not a general forecast-horizon estimate for ecology; it is a controlled demonstration that a state distinction can be dynamically real at one step yet become visible in a coarser loss endpoint only after additional propagation.

The original 500-pair 60-generation comparison was therefore correctly unresolved by its interval rather than interpreted as evidence of no effect. The separately locked 1,500-pair experiment shows that the principal change with replication was interval width, not a dramatic reversal of the estimated generation-20/40 effect magnitude. More broadly, quantitative ecological forecasting gains information by declaring prediction targets, horizons, and uncertainty rather than converting a single significance test into a claim about predictability (Clark et al. 2001; Dietze et al. 2018).

### Process state is operator-specific

The portability tests establish a second non-identity. A parameter value attached to one mathematical operator is not a transferable biological connectivity state. Seed-family contingency, whole-individual movement, paternal pollen flow, and partner rewiring address different processes and must retain separate labels. In fragmented eco-evolutionary systems, movement can alter demography, composition, and selection through different routes (Legrand et al. 2017; Govaert et al. 2019). A common scalar axis is justified only after the observation and transition maps establish that the operators preserve the distinctions relevant to the target.

### This result does not explain warning failure

The separate full-denominator warning-validity audit addresses a different inferential failure. Nothing in the state counterexample or propagation experiment shows that the frozen relative-diversity rules failed because cross-layer alignment was omitted, and no warning threshold was rerun with alignment information. The defensible shared principle is more abstract: information for one inferential target does not guarantee adequacy for another. This manuscript therefore does not claim that joint-state representation repairs or validates the frozen warning rules.

### Empirical handoff

The natural-data programme asks the next question: what happens when candidate ecological states are confronted with held-out biological endpoints? Those results are intentionally routed outside this manuscript into `natural_data_four_gate_program.md`, with reader-facing development now authoritative in `zuizui0223/egwee`. Keeping those results separate prevents a finite model counterexample from borrowing empirical breadth it does not need and prevents heterogeneous natural systems from being used as validation of the synthetic closure.

### Claim boundary

The model results are finite and closure-specific. Non-significant tests do not establish equivalence. The original 500-pair Phase-V comparison remains a frozen, imprecise 60-generation result; the post-Phase-V experiment is a separate, prospectively locked extension and is not relabelled as part of the original preregistration. The propagation experiment supports an approximately five-point anti-aligned excess loss risk by the declared generation-20 readout, maintained at generation 40, after little contrast at generations 5–10. It does not establish generation 20 as a true cutoff, a universal temporal threshold, or a natural-system timescale. Failure of one historical connectivity pattern to reproduce or transport does not establish that connectivity is irrelevant. This manuscript **makes no claim that the frozen relative-diversity thresholds are validated predictive warnings**; that full-denominator validity audit is owned exclusively by `manuscript/warning_validity.md`.

## Data and code availability

The parent and extension repositories remain separate provenance units. The original Phase-V result remains fixed by its existing locked artifact. The post-Phase-V propagation protocol, implementation, successful workflow provenance, complete 12-cell compact result, and result interpretation boundary are stored in `experiments/alignment_propagation_protocol.json`, `src/eco_genetic_warning_extensions/alignment_propagation_experiment.py`, `artifacts/alignment_propagation/locked_summary.json`, and `docs/ALIGNMENT_PROPAGATION_RESULT_2026-09-04.md`. Locked model summaries, contracts, negative results, STOP artifacts, workflow identifiers, and source-version metadata remain indexed in `manuscript/artifact_index.md`.

The load-bearing external bibliography for this lane is recorded in `manuscript/state_validity_references.md`.
