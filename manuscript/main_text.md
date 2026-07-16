# Directional recurrent mutation partitions trait-loss regimes and genetic-warning reliability in finite eco-genetic systems

## Abstract

Genetic early-warning studies usually ask whether a genetic signal precedes demographic or functional loss, but the genetic process itself may determine whether a comparable loss-event regime exists. We extended a theorem-guided finite eco-genetic model by separating the relaxation strength of recurrent mutation from its directional equilibrium. Across 15 preregistered mutation coordinates, Stage I independently reconstructed high-trait sources in 3,375 attempts. Source support, full-state preparation, and projection were obtained in 2,269 attempts (67.23%), ranging from 44.89% to 86.67% among coordinates, with no projection failure after successful preparation. Stage II then completed 20,250 warning-blind trait-loss calibration attempts in 810 candidate cells. Among 648 candidates with complete five-seed blocks, 322 were entirely above the preregistered loss-frequency band, 242 were entirely below it, and 84 crossed the band among seeds; none satisfied the all-seed eligibility rule. A separately declared Protocol 003 used disjoint bracket, calibration, confirmation, and validation seed families to recover two comparison domains. In 200 fresh-seed validation trajectories, a symmetric bridge yielded 323 leads, one tie, and no lags across 324 valid endpoint comparisons, whereas a directional transition yielded 184 leads, five ties, and 12 lags across 201 valid comparisons, with greater baseline ineligibility and censoring. Median positive lead times were 106–112 generations in the symmetric bridge and 74–81 generations in the directional transition. These finite Type S results show that mutation direction can partition source feasibility and trait-loss regimes and can alter the availability, ordering, and usable lead time of relative genetic warnings.

## Introduction

Ecological deterioration can remove an interaction-dependent or functional trait before population extinction. Genetic monitoring may therefore be useful when genetic change precedes realised trait loss, but abundance, allele persistence, genetic diversity, interaction state, and realised trait occupancy are distinct state variables.

The predecessor framework established exact and finite-model links among interaction thresholds, fragmentation, local effective size, realised high-trait occupancy, and genetic diversity. Under one independently calibrated symmetric-mutation configuration, baseline-relative diversity erosion preceded observed trait loss. That result was explicitly conditional on one life-cycle closure and one selected deterioration domain.

Here we examine a separate boundary condition. Recurrent transitions between high-trait-associated and low-trait-associated allelic states need not be symmetric. Holding the contraction strength of the mutation map fixed while changing its equilibrium direction changes recurrent input and loss without modifying selection, migration, finite drift, trait recruitment, source transfer, projection, or trait-loss semantics.

We ask whether mutation direction changes (i) the feasibility of reconstructing a high-trait source, (ii) the probability regime of realised trait loss, (iii) the existence of a warning-validation domain under a warning-blind decision rule, and (iv) relative-warning availability and ordering after independent calibration.

## Model and mechanism

Let `p` denote the high-trait-associated allele frequency. The recurrent mutation operator is

\[
M(p)=\kappa_\mu p_\mu^\ast+(1-\kappa_\mu)p.
\]

Here `kappa_mu` controls contraction toward the mutation-only equilibrium and `p_mu*` controls direction. The effective transition rates are

\[
u_{L\to H}=\kappa_\mu p_\mu^\ast,\qquad
u_{H\to L}=\kappa_\mu(1-p_\mu^\ast).
\]

At a local post-mutation threshold `p_c`, the required pre-mutation frequency is

\[
\theta(p_c)=\frac{p_c-\kappa_\mu p_\mu^\ast}{1-\kappa_\mu}.
\]

Increasing `p_mu*` therefore lowers the pre-mutation frequency required to remain above a high-state boundary. Whether this local mechanism organizes the finite stochastic system was tested rather than assumed.

## Protocol

We evaluated three relaxation strengths (`0.05`, `0.20`, `0.35`) and five mutation equilibria (`0.10`, `0.25`, `0.50`, `0.75`, `0.90`). All other life-cycle components were inherited from pinned predecessor commit `dd8ee379d0d3518194c767d16402042525bc00dc`.

Stage I independently reconstructed sources for every coordinate using three area-reference values, three interaction-feedback values, five master seeds, and five replicates. Each prepared source was held for 30 generations and projected into the declared one-large, equal-isolated, and equal-migrating landscapes. A projection was counted as supported only when all projection invariants passed.

Stage II evaluated two horizons and three normalized barrier increases using five new calibration seeds and five replicates. Calibration could inspect source eligibility and realised trait loss only. Diversity values, warning times, lead/lag status, and usable lead time were unavailable. A candidate was eligible only if every seed block had post-baseline trait-loss frequency in `[0.30, 0.70]`. If none qualified, the protocol required `no_domain_selected` without expanding the candidate family.

Because Protocol 002 selected no domain, Protocol 003 was declared separately. It used independent seed families for bracket search, calibration, confirmation, and warning validation. Two confirmation-eligible domains were fixed before warning outcomes were computed: a symmetric bridge (`kappa_mu=0.20`, `p_star=0.50`) and a directional transition (`kappa_mu=0.05`, `p_star=0.90`). Validation used five fresh master seeds and 20 replicates per seed in each domain.

Relative warnings were defined within trajectories as the first post-baseline generation at which `H_alpha` or `H_gamma` declined by 5%, 10%, or 20% from its own baseline. Each comparison retained baseline ineligibility, warning censoring, trait-loss censoring, ties, leads, and lags. The six endpoint records from one trajectory are correlated and are not treated as independent biological replicates.

## Results

### Mutation direction changed source feasibility

Stage I completed all 3,375 planned attempts. Source support, full-state preparation, and supported projection each occurred in 2,269 attempts (67.23%). The three counts were identical because every prepared source passed all projection invariants; there were zero projection failures and 1,106 attempts in which projection was not run because source reconstruction or preparation was unsupported.

Success varied strongly across the mutation-coordinate map. The minimum was 101 of 225 attempts (44.89%) at `kappa_mu=0.05`, `p_star=0.10`, whereas the maximum was 195 of 225 (86.67%) at `kappa_mu=0.35`, `p_star=0.90`. Within each relaxation-strength row, support generally increased toward higher `p_star`. At `kappa_mu=0.35`, support rose from 53.33% at `p_star=0.10` to 86.67% at `p_star=0.90`. These results connect the local threshold prediction to the finite source-reconstruction boundary while retaining stochastic and parameter-cell variation.

### Directional mutation partitioned trait-loss regimes

Stage II completed all 20,250 attempts in 810 resumable batches. Of 648 candidates with complete five-seed blocks, 322 had all seed-block loss frequencies above the eligibility band, 242 had all rates below it, and 84 crossed the band among seeds.

Low mutation equilibria were dominated by rapid-loss candidates. For example, the closest candidates at `p_star=0.10` had loss frequency 1.0 across all five seed blocks at every tested relaxation strength. High mutation equilibria at stronger relaxation were dominated by persistence: the closest candidates at (`0.20`, `0.90`), (`0.35`, `0.75`), and (`0.35`, `0.90`) had loss frequency zero in every seed block. Intermediate coordinates were often seed-heterogeneous. At (`0.05`, `0.90`), the closest candidate had pooled loss frequency 0.458 with seed-block rates 0.60, 0.40, 0.25, 0.60, and 0.40. At the symmetric coordinate (`0.20`, `0.50`), the closest candidate had pooled frequency 0.524 but seed-block rates ranging from 0.20 to 0.80.

None of the 648 complete candidates satisfied the Protocol 002 all-seed eligibility rule. All 15 coordinates were therefore recorded as `no_domain_selected`. This was a preregistered decision-rule result, not evidence that genetic warning failed.

### Independent calibration recovered two warning-validation domains

Protocol 003 confirmation calibration recovered two eligible domains using larger within-seed replication and fresh seeds while retaining the declared eligibility rule. The symmetric bridge had pooled trait-loss frequency 0.679 among 84 baseline-eligible trajectories; the directional transition had pooled frequency 0.625 among 88 eligible trajectories. These domains were locked before validation diversity trajectories were examined.

### Mutation direction changed warning availability and ordering

Stage III completed 200 fresh-seed validation attempts. In the symmetric bridge, 82 trajectories completed and each of the six endpoints produced 54 valid warning–loss pairs. Across the 324 correlated endpoint comparisons, 323 were leads, one was a tie, and none was a lag. Median positive lead time ranged from 106 to 112 generations. Twenty-eight completed trajectories per endpoint had censored trait loss, while warning censoring and baseline ineligibility were absent.

In the directional transition, 91 trajectories completed, but valid-pair availability varied from 28 to 38 among endpoints. Ten trajectories were baseline-ineligible for every endpoint. Across 201 valid comparisons, 184 were leads, five were ties, and 12 were lags. Warning censoring increased with stricter decline thresholds and was more frequent for `H_gamma`; at the 20% `H_gamma` endpoint, 24 trajectories were warning-censored and four valid pairs lagged trait loss. Median positive lead times ranged from 74 to 81 generations.

Thus, valid relative warnings remained predominantly leading in the independently calibrated directional domain, but they were less consistently available, included non-zero lag, and provided shorter usable lead times than the symmetric bridge.

## Discussion

The results identify three linked roles for mutation direction. First, it changed whether high-trait source states could be reconstructed under otherwise fixed ecological and demographic rules. Second, it partitioned deterioration experiments into rapid-loss, persistence, and seed-heterogeneous regimes. Third, after independent calibration recovered comparable loss-event domains, it changed warning availability, ordering, censoring, and lead-time magnitude.

This distinction matters for ecological monitoring. A system with nearly certain rapid functional loss offers little discrimination among warning rules, whereas a system with almost no loss yields few event pairs. Seed-heterogeneous regimes create a third difficulty: pooled event frequencies can appear appropriate while individual seed blocks cross both sides of the declared target. Warning-validation feasibility is therefore an ecological and experimental outcome, not merely a technical preprocessing step.

The contrast between the two Protocol 003 domains also limits universal interpretation of relative-diversity warnings. The symmetric bridge reproduced a near-uniform lead pattern, but the directional transition retained baseline-ineligible trajectories, greater warning censoring, shorter median lead time, and non-zero lag. A monitoring rule that is useful under one mutation closure may remain informative under another yet be available less often or too late in a larger fraction of realised losses.

The study is finite and conditional. `p_mu*` is an effective recurrent-transition equilibrium, not an estimated mutation spectrum for a particular species. The comparison includes two independently calibrated domains, not all 15 coordinates, and endpoint counts are correlated within trajectories. The results therefore constitute Type S evidence for the declared finite closure rather than a universal theorem or an empirical estimate.

The ecological implication is nevertheless direct: genetic processes can shape both functional-trait persistence and the observation window in which genetic monitoring is useful. Studies of evolutionary rescue, interaction-dependent traits, and conservation warning indicators should declare the mutation or state-transition closure, separate calibration from warning evaluation, retain censoring, and report when a warning-validation domain cannot be obtained.

## Relationship to the predecessor

The predecessor and this extension form a companion pair. The predecessor asks when interaction feedback, fragmentation, and genetic change can produce a conditional warning result under a symmetric closure. This paper tests how changing the mutation closure modifies source feasibility, loss-event regimes, and warning reliability. The predecessor's trajectories are context, not numerical evidence for the present claims.

## Data and code availability

All model code, protocols, immutable grid locks, batch workflows, calibration decisions, validation summaries, figure builders, and submission-package workflows are maintained in this repository. The pinned predecessor commit and every source workflow run and artifact digest are recorded in machine-readable metadata.
