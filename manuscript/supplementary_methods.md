# Supplementary methods

## S1. Study phases, repository provenance, and evidence separation

The manuscript integrates two computational phases but retains them as separate provenance units. The first-phase repository, `zuizui0223/eco-genetic-criticality`, is pinned at scientific commit `dd8ee379d0d3518194c767d16402042525bc00dc` and contains the theorem-guided interaction model, the locked H1/H3 fragmentation campaign, and the inherited symmetric warning benchmark. The extension repository contains the directional recurrent-transition operator, independent source reconstruction, Protocol 002 and Protocol 003, and the secondary manuscript-review audit.

Trajectories are never pooled across phases. The integrated submission bundle contains exact source archives, software distributions, machine-readable summaries, workflow IDs, artifact IDs, and SHA-256 manifests for both repositories.

## S2. First-phase H1/H3 paired fragmentation summary

The canonical H1/H3 campaign is workflow run `28456092898`, artifact `7987193632`, digest `sha256:b74b604f3233fa6086e2afa39cd780fa375aac4b1abd8c63e6f5ed8b3a467d2c`. It contains 12 predeclared primary cells with 100 attempted seed-replicates each. Across those cells, 1,055 replicates satisfied the H1 full-state hold criterion.

For each H1-qualified replicate, the stored one-large and equal-isolated outcomes were paired. Manuscript-facing descriptive effect sizes were calculated without rerunning the simulation:

\[
R_x = 1-\frac{x_{\mathrm{isolated}}}{x_{\mathrm{one\ large}}},
\]

where final interaction is the mean of `final_q_by_patch`, local effective size is the mean of `final_effective_size_by_patch`, and realised high-trait mass is the stored metapopulation mean.

**Table S1. Paired fragmentation effect sizes in 1,055 H1-qualified replicates.**

| Metric | one-large mean | equal-isolated mean | median paired reduction | IQR |
|---|---:|---:|---:|---:|
| final interaction | 0.997729 | 0.004815 | 99.86% | 99.28–99.98% |
| final local effective size | 72.828 | 8.182 | 88.73% | 88.52–88.93% |
| realised high-trait mass | 0.575312 | 0.177313 | 68.87% | 59.90–78.50% |

The parent campaign reports the H3 directional pattern in every H1-qualified replicate. These pooled values are descriptive finite-model summaries rather than universal fragmentation effect sizes. These medians were calculated separately from the locked H3 paired outcomes using the conventional median; they do not use the historical Stage III timing-summary function discussed in Section S9.

The locked parent artifact contains the predeclared `one_large`, `equal_isolated`, and `equal_migrating` scenarios, but not an intermediate gradient in the number of isolated fragments. Consequently, an additional fragmentation-gradient figure would require a new finite-model campaign rather than replotting an existing locked result.

## S3. Inherited symmetric warning benchmark

The first-phase warning benchmark used symmetric allele-state mutation rate `0.10`, `A_ref=0.8`, interaction-feedback `kappa=6.0`, an equal-isolated landscape, a 30-generation barrier ramp, a 90-generation hold, and normalized total barrier increase `0.15`. Trait-loss-only calibration selected this configuration without loading genetic-warning fields.

Validation used fresh master seeds `20261110`–`20261114`, 20 replicates per seed. Of 100 attempted sources, 83 produced available trajectories; 35 experienced post-baseline realised trait loss and 48 available trajectories remained right-censored. Each of the six baseline-relative endpoints had 35 lead, zero tie, and zero lag pairs.

The stored trajectories were subsequently audited at the pre-existing fixed thresholds `H_alpha <= 0.20` and `H_gamma <= 0.20`, producing mixed ordering. No new simulation or threshold search was performed.

## S4. Directional recurrent-transition operator

The high-trait-associated allele frequency is transformed after selection and migration and before finite drift by

\[
M(p)=\kappa_\mu p_\mu^\ast+(1-\kappa_\mu)p.
\]

The effective transition rates are `low_to_high = kappa_mu * p_star` and `high_to_low = kappa_mu * (1-p_star)`. The common phase grid comprises `kappa_mu = 0.05, 0.20, 0.35` crossed with `p_star = 0.10, 0.25, 0.50, 0.75, 0.90`.

## S5. Protocol 002 source reconstruction and strict warning-blind calibration

Stage I contains 15 transition coordinates × 3 area-reference values × 3 interaction-feedback values × 5 master seeds × 5 replicates = 3,375 attempts. Every attempt reruns the pinned H1 boundary-resolution audit, reconstructs a full high-state source when supported, holds it for 30 generations, and projects it into one-large, equal-isolated, and equal-migrating landscapes. Projection support requires every conservation and state-transfer invariant to pass.

Stage II contains 15 coordinates × 3 area references × 3 interaction-feedback values × 2 holds × 3 barrier increases × 5 seeds × 5 replicates = 20,250 attempts. Candidate selection may inspect only source/projection eligibility, baseline high-trait presence, trait-loss occurrence, and trait-loss time. Warning, diversity, lead/lag, and event-pair fields are prohibited by executable guards.

Each Protocol 002 candidate requires five complete seed blocks. A domain is eligible only when **every** seed-block trait-loss frequency lies in `[0.30, 0.70]`. No candidate met this rule. Protocol 002 therefore closed with 15/15 `no_domain_selected` and did not widen its own candidate family.

This common-family experiment is also the study's matched-schedule test across recurrent-transition coordinates. Because it yielded no eligible intermediate-risk validation domain at any coordinate, the same schedule family could not support a matched Stage III warning comparison without first changing the event-risk regime.

## S6. Protocol 003 Amendment 001: warning-blind candidate expansion and revised gate

Protocol 003 was declared only after Protocol 002 closed. A trait-loss-only bracket pilot was inspected without calculating or loading any diversity or warning outcome.

Amendment 001 allowed two sentinel coordinates to proceed and explicitly declared their candidate schedules:

- recalibrated symmetric sentinel (`kappa_mu=0.20`, `p_star=0.50`): `(hold=210, increase=0.20)` and `(hold=300, increase=0.30)`;
- directional sentinel (`kappa_mu=0.05`, `p_star=0.90`): `(hold=90, increase=0.10)` and `(hold=90, increase=0.15)`.

The `(hold=90, increase=0.10)` directional schedule was a weaker neighbour added **before independent calibration**.

Amendment 001 also replaced the Protocol 002 all-seed gate. A Protocol 003 candidate was eligible when:

1. pooled trait-loss frequency lay in `[0.30, 0.70]`;
2. at least four of five seed-block frequencies lay in `[0.20, 0.80]`;
3. every seed block contained at least three baseline-eligible trajectories.

Independent calibration used master seeds `20270610`–`20270614` with five replicates per seed. No warning endpoint was calculated or inspected.

## S7. Protocol 003 Amendment 002: confirmation without further rule relaxation

The first independent calibration completed 100 trajectories across four candidates but none met the Amendment 001 gate. The candidates nearest pooled 0.5 were the recalibrated symmetric schedule `(hold=210, increase=0.20)` and directional schedule `(hold=90, increase=0.10)`.

Amendment 002 **did not change the gate**. It increased replication to 20 per seed and used a fresh confirmation seed family `20270620`–`20270624`. Only confirmation candidates marked `calibration_eligible: true` were allowed to proceed.

The confirmed Stage III domains differ in more than recurrent-transition direction:

| Parameter | recalibrated symmetric domain | directional calibrated domain |
|---|---:|---:|
| `A_ref` | 0.8 | 1.0 |
| interaction-feedback `kappa` | 6.0 | 4.5 |
| `kappa_mu` | 0.20 | 0.05 |
| `p_star` | 0.50 | 0.90 |
| ramp | 30 | 30 |
| hold | 210 | 90 |
| total horizon | 240 | 120 |
| normalized barrier increase | 0.20 | 0.10 |

Stage III is therefore a portability comparison across independently calibrated domains, not a matched single-factor experiment. Coordinate-specific recalibration restored an evaluable event regime but necessarily sacrificed single-factor identification.

## S8. Stage III warning endpoints and censoring

Validation used fresh master seeds `20270710`–`20270714`, 20 replicates per domain. Six endpoints were preregistered: 5%, 10%, and 20% post-baseline declines in `H_alpha` and `H_gamma`. Generation zero cannot be a warning.

For a completed trajectory, categories are mutually exclusive at each endpoint:

- `baseline_ineligible`;
- `both_censored`;
- `warning_censored`;
- `trait_loss_censored`;
- `lead`;
- `tie`;
- `lag`.

Source-preparation failure is retained separately in the full attempted denominator. A valid pair requires an eligible positive baseline, an observed warning crossing, and an observed post-baseline trait-loss time. Missing events are never assigned the final generation.

## S9. Post hoc secondary timing and uncertainty audit

The manuscript-review audit is documented in `docs/PROTOCOL_003_SECONDARY_WARNING_AUDIT.md`. It uses only locked Stage III records from workflow run `29417632137`, artifacts `8343958766` and `8343922879`. It does not rerun trajectories or alter any domain or endpoint.

### S9.1 Conventional-median correction and scope

The historical Stage III artifact generator calculated `sorted(lead_times)[len(lead_times)//2]`. For even `n`, this is the upper middle order statistic. The review audit uses the conventional median, averaging the two central observations.

Repository-wide inspection found this historical definition only in the Stage III timing-summary path. It does not affect the separately calculated H3 paired-reduction medians or other manuscript-facing medians. Historical Stage III source artifacts remain immutable.

### S9.2 Horizon normalization

For each leading pair,

\[
L_{\mathrm{norm}}=
\frac{\tau_{\mathrm{trait\ loss}}-\tau_{\mathrm{warning}}}
{\text{ramp generations}+\text{hold generations}}.
\]

A hold-only normalization is retained in the machine-readable audit. The main paper reports full-horizon normalization because both event times are measured from the start of the ramp. Neither normalization converts the two calibrated domains into a matched causal contrast.

### S9.3 Whole-trajectory bootstrap within domains

The six endpoint observations within a trajectory are correlated. Whole attempted trajectories were therefore sampled with replacement, preserving all six endpoint rows. The audit uses 20,000 replicates, fixed random seed `20260814`, and percentile 95% intervals.

The intervals are finite-campaign descriptive uncertainty, not population-level inferential confidence intervals.

### S9.4 Direct bootstrap of between-domain timing differences

The two Stage III domains use independent attempted trajectories. In each bootstrap replicate, 100 whole attempted trajectories are resampled independently within each domain. For each endpoint, the median among positive leads is calculated in both resampled domains and the directional-minus-symmetric difference is stored.

The direct difference is evaluated on three scales: absolute generations, fraction of the full calibrated horizon, and fraction of the hold duration. The latter is a sensitivity description only. This procedure avoids treating overlap or non-overlap of the two marginal intervals as a test of the difference.

For absolute generations, the 95% directional-minus-symmetric difference interval excludes zero only for `H_alpha` at 5% and 10% decline. For the other four endpoints it includes zero. For full-horizon-normalized lead time, **all six** difference intervals include zero. The normalized point-estimate reversal is therefore descriptive evidence of schedule dependence rather than a separated timing effect.

The compact direct-difference results are stored in `manuscript/tables/stage3_between_domain_differences.csv` and are regenerated from the immutable Stage III artifacts during publication builds.

### S9.5 Cumulative event incidence

Warning and trait loss can both occur in one trajectory and are therefore not classical mutually exclusive competing risks. For each endpoint, cumulative warning incidence and cumulative realised trait-loss incidence are calculated among baseline-eligible completed trajectories over the domain-specific administrative horizon. Censored non-events remain in the denominator through the end of follow-up.

For the directional calibrated domain at the 20% `H_gamma` endpoint, final warning incidence was 41/81 (0.506), whereas final realised functional-trait-loss incidence was 52/81 (0.642).

## S10. Reproducibility

All locked campaign identifiers, source artifact digests, and exact software states are recorded in the submission bundle. `Paper completion sprint` downloads the immutable Stage III domain artifacts, generates the 1,200-row trajectory-endpoint table, reruns the fixed secondary audit, verifies both committed publication CSVs against regenerated versions, and archives records, audit JSON, direct differences, figures, software and provenance in the checksummed bundle.

## S11. Interpretation boundary

All numerical conclusions are finite Type S evidence for declared model closures. `p_star` is an effective recurrent-transition equilibrium and is not an empirical mutation-rate estimate. The study does not claim a universal warning theorem, universal rescue, independence among the six endpoint observations from a trajectory, an isolated Stage III effect of recurrent-transition direction, or a separated full-horizon-normalized timing contrast.
