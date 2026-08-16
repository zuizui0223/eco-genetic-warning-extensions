# Eco-genetic warning extensions

Independent, protocol-locked extensions of the finite eco-genetic criticality framework, plus the reproducible submission package for the integrated Ecology Letters manuscript.

## Current status

The recurrent-transition campaigns are complete. The repository contains 3,375 independent source-reconstruction attempts, 20,250 warning-blind common-family calibration attempts, a closed Protocol 002 result with 15/15 coordinates recorded as `no_domain_selected`, a separately declared and amended Protocol 003 calibration/confirmation/validation campaign, a post-review whole-trajectory uncertainty audit, publication tables and figures, and a checksummed submission-bundle workflow.

The publication source of truth is [`manuscript/main_text.md`](manuscript/main_text.md), synchronized with [`manuscript/supervisor_first_draft.md`](manuscript/supervisor_first_draft.md). Permitted and prohibited claims are locked in [`manuscript/claim_evidence_map.md`](manuscript/claim_evidence_map.md).

## Relationship to the mechanistic phase

[`eco-genetic-criticality`](https://github.com/zuizui0223/eco-genetic-criticality) contains the theorem-guided interaction/fragmentation mechanism, locked H1/H3 finite campaign, and inherited symmetric warning benchmark. This repository is the second computational phase of the same manuscript, but the two repositories remain separate provenance ledgers and their trajectories are never pooled.

The parent scientific state is fixed at:

```text
repository: zuizui0223/eco-genetic-criticality
commit:     dd8ee379d0d3518194c767d16402042525bc00dc
```

The exact two-repository and publication-evidence lock is [`reproducibility/upstream-lock.json`](reproducibility/upstream-lock.json).

## Paper question and identification boundary

The recurrent-transition operator is

\[
p_{t+1}^{\mathrm{mut}}
= u_{L\to H}+(1-u_{L\to H}-u_{H\to L})p_t,
\]

parameterised by

\[
\kappa_\mu=u_{L\to H}+u_{H\to L},\qquad
p_\mu^\ast=\frac{u_{L\to H}}{\kappa_\mu}.
\]

At fixed `kappa_mu`, the common-grid analyses ask how transition direction reorganises high-trait source feasibility and realised functional-loss regimes. These are the direct transition-coordinate comparisons and the strongest identified extension evidence.

Strict Protocol 002 warning-blind calibration selected no common validation domain: the common deterioration family separated into rapid-loss, persistence, and seed-heterogeneous regimes. This means that **event-regime feasibility must be established before warning performance can be compared**.

Protocol 003 was subsequently declared. Amendment 001 expanded the candidate schedules and defined a pooled + four-of-five seed-block event-risk gate before any warning endpoint was calculated. Amendment 002 retained that gate and increased replication with fresh confirmation seeds.

The two final validation domains are not matched except for transition direction. They differ in `A_ref`, interaction-feedback `kappa`, `kappa_mu`, `p_star`, barrier increase, and calibrated horizon. Their comparison therefore tests **warning portability across independently calibrated eco-genetic domains**, not a single-factor causal effect of transition direction.

## Locked headline results

- **Fragmentation bridge:** across 1,055 H1-qualified paired projections in the mechanistic phase, median reductions after equal isolation were 99.86% for final interaction, 88.73% for local effective size, and 68.87% for realised high-trait mass.
- **Inherited symmetric benchmark:** 83 of 100 attempted trajectories were available; 35 experienced functional-trait loss, and all six relative-warning endpoints led in all 35 observed event pairs. Fixed absolute thresholds produced both leads and lags.
- **Source feasibility:** 2,269 of 3,375 attempts completed source preparation and supported projection; coordinate support ranged from 44.89% to 86.67%.
- **Strict warning-blind regime map:** among 648 complete Protocol 002 candidates, 322 were rapid-loss-side, 242 persistence-side, and 84 seed-heterogeneous; zero candidates satisfied the all-seed gate and all 15 coordinates remained `no_domain_selected`.
- **Recalibrated symmetric domain:** 323 leads, one tie, and no lags across 324 valid endpoint comparisons; valid-pair availability 0.540 and whole-trajectory bootstrap lead fraction 0.997 (95% interval 0.990–1.000).
- **Directional calibrated domain:** 184 leads, five ties, and 12 lags across 201 valid endpoint comparisons; valid-pair availability 0.335 and lead fraction 0.915 (0.848–0.971). For the 20% `H_gamma` endpoint, final warning incidence was 41/81 (0.506) versus 52/81 (0.642) for realised trait loss.
- **Direct timing audit:** conventional median positive lead times were 106–109 versus 72.5–77.5 generations. Directional-minus-symmetric absolute 95% difference intervals excluded zero only for `H_alpha` 5% and 10%. Full-horizon-normalized point estimates reversed (0.442–0.454 versus 0.604–0.646), but all six normalized difference intervals included zero. Neither timing ordering is a general single-factor Stage III result.

The six endpoint rows within each trajectory are correlated repeated summaries. All uncertainty resamples whole attempted trajectories. All numerical conclusions remain finite Type S evidence for their declared model closures.

## Reproducibility architecture

The submission uses two installable packages rather than merging scientific code bases:

```text
eco-genetic-criticality
  mechanistic parent + exact scientific source archive

eco-genetic-warning-extensions
  recurrent-transition protocols + publication/audit code

submission bundle
  manuscript + Figures 1–6 + machine-readable tables
  + parent/extension software distributions
  + exact source archives + provenance + SHA-256 manifest
```

A lightweight check is:

```bash
git clone https://github.com/zuizui0223/eco-genetic-criticality.git upstream
git -C upstream checkout dd8ee379d0d3518194c767d16402042525bc00dc
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -e upstream
python -m pip install -e '.[dev,reproducibility]'
python -m pytest
python scripts/verify_reproducibility_contract.py --upstream upstream
```

The **Paper completion sprint** additionally downloads the locked Stage I, Stage II, and Stage III workflow artifacts; flattens the immutable Stage III validation payloads to 1,200 trajectory-endpoint records; regenerates the fixed 20,000-resample audit and direct between-domain timing contrasts; byte-verifies both committed publication CSVs; regenerates Figures 1–6; builds both software distributions; and writes a SHA-256 manifest over the complete bundle.

Historical Stage III source artifacts remain immutable. The original compact summary is retained for provenance; corrected conventional medians, schedule-normalized timing, and direct timing differences are explicitly labelled as post-review secondary analyses rather than silently rewriting historical evidence.

## Protocol boundaries

- **Protocol 001:** bridge/pilot.
- **Protocol 002:** 15-coordinate source reconstruction and strict warning-blind common-family calibration; closed with 15/15 `no_domain_selected`.
- **Protocol 003:** separately declared bracket, amended warning-blind calibration, confirmation, and fresh-seed validation.
- **Secondary review audit:** data-only analysis of the locked Stage III validation records; no simulation rerun, domain reselection, or endpoint change.

No diversity, warning time, lead/lag ordering, or lead-time quantity was available during any trait-loss calibration stage.

## Evidence labels

- **T** — theorem under explicitly stated mathematical assumptions;
- **C** — conditional result after a declared ecological closure;
- **H** — dynamic hypothesis;
- **S** — finite, model-specific simulation evidence.

## Key entry points

- [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) — reproduction and archival guide
- [`manuscript/artifact_index.md`](manuscript/artifact_index.md) — workflow, artifact, and digest provenance
- [`manuscript/claim_evidence_map.md`](manuscript/claim_evidence_map.md) — permitted/prohibited claims and corrected timing values
- [`docs/PROTOCOL_003_AMENDMENT_001.md`](docs/PROTOCOL_003_AMENDMENT_001.md) — warning-blind candidate expansion and revised event-risk gate
- [`docs/PROTOCOL_003_AMENDMENT_002.md`](docs/PROTOCOL_003_AMENDMENT_002.md) — confirmation with unchanged gate and increased replication
- [`docs/PROTOCOL_003_SECONDARY_WARNING_AUDIT.md`](docs/PROTOCOL_003_SECONDARY_WARNING_AUDIT.md) — identification correction, conventional median scope, direct difference bootstrap, normalization, censoring, and cumulative incidence

Final author order, affiliations, CRediT roles, licence, funding, conflicts, archive DOI, and repository citation metadata require explicit author approval and are not inferred by automation.
