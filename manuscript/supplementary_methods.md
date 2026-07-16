# Supplementary methods

## S1. Repository and model provenance

The extension repository is an independent companion to `zuizui0223/eco-genetic-criticality`. All inherited life-cycle behavior is pinned to upstream commit `dd8ee379d0d3518194c767d16402042525bc00dc`. The extension replaces only the recurrent mutation operator and reconstructs all sources with independent seeds.

## S2. Directional recurrent mutation

The high-trait-associated allele frequency is transformed after selection and migration and before finite drift by

\[
M(p)=\kappa_\mu p_\mu^\ast+(1-\kappa_\mu)p.
\]

The effective transition rates are `low_to_high = kappa_mu * p_star` and `high_to_low = kappa_mu * (1-p_star)`. The phase grid comprises `kappa_mu = 0.05, 0.20, 0.35` crossed with `p_star = 0.10, 0.25, 0.50, 0.75, 0.90`.

## S3. Stage I source reconstruction

The declared Stage I campaign contains 15 mutation coordinates × 3 area-reference values × 3 interaction-feedback values × 5 master seeds × 5 replicates = 3,375 attempts. Every attempt reruns the pinned H1 boundary-resolution audit, reconstructs a full high-state source when supported, holds it for 30 generations, and projects it into one-large, equal-isolated, and equal-migrating landscapes. Projection support requires every conservation and state-transfer invariant to pass.

## S4. Protocol 002 warning-blind calibration

The Stage II grid contains 15 coordinates × 3 area references × 3 interaction-feedback values × 2 holds × 3 barrier increases × 5 seeds × 5 replicates = 20,250 attempts. Candidate selection may inspect only source/projection eligibility, baseline high-trait presence, trait-loss occurrence, and trait-loss time. Warning, diversity, lead/lag, and event-pair fields are prohibited by executable guards.

Each candidate requires five complete seed blocks. A domain is eligible only when every seed-block trait-loss frequency lies in `[0.30, 0.70]`. No candidate met this rule; no candidate family was widened within Protocol 002.

## S5. Protocol 003 amendments and seed separation

Protocol 003 was declared after Protocol 002 closed. Bracket-search, independent-calibration, confirmation-calibration, and warning-validation seeds are disjoint. Warning and diversity fields remain unavailable until the two final domains are locked.

Confirmation calibration used five seeds and 20 replicates per seed. Eligibility required pooled loss frequency in `[0.30, 0.70]`, at least three baseline-eligible trajectories in every seed block, and at least four of five seed-block frequencies in `[0.20, 0.80]`. Two domains qualified: the symmetric bridge and directional transition.

## S6. Stage III relative-warning endpoints

Validation used five fresh seeds and 20 replicates per domain. Six endpoints were preregistered: 5%, 10%, and 20% post-baseline declines in `H_alpha` and `H_gamma`. Generation zero cannot be a warning. A valid pair requires an eligible positive baseline, a warning crossing, and an observed post-baseline trait-loss time. Missing events remain censored.

Ordering is defined as lead when `warning_time < trait_loss_time`, tie when equal, and lag when `warning_time > trait_loss_time`. Lead time is `trait_loss_time - warning_time`. Endpoint records are correlated within trajectories and are summarized descriptively rather than treated as independent replicates.

## S7. Reproducibility

All campaigns are partitioned into resumable GitHub Actions jobs. Completion locks record run IDs, artifact IDs, digests, batch coverage, and expected denominators. Publication builders reject missing or duplicate batches and regenerate tables and SVG figures from immutable JSON artifacts.

## S8. Interpretation boundary

All numerical conclusions are finite Type S evidence for the declared model closure. `p_star` is an effective mutation-only equilibrium and is not an empirical mutation-rate estimate. The study does not claim a universal warning theorem, universal rescue, or independence among the six endpoint observations from a trajectory.
