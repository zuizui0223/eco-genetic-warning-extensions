# Reproducibility guide

This repository is the **independent condition-recovery extension and submission orchestrator** for the eco-genetic warning study. It depends on a fixed scientific state of `eco-genetic-criticality` but does not rewrite the parent evidence ledger.

The parent scientific commit is fixed at `dd8ee379d0d3518194c767d16402042525bc00dc`.

## Reproduction levels

### Level 1 — package and invariant tests

```bash
git clone https://github.com/zuizui0223/eco-genetic-warning-extensions.git
git clone https://github.com/zuizui0223/eco-genetic-criticality.git upstream
git -C upstream checkout dd8ee379d0d3518194c767d16402042525bc00dc

python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e upstream
python -m pip install -e '.[dev,reproducibility]'
python -m pytest
python scripts/verify_reproducibility_contract.py --upstream upstream
```

### Level 2 — rebuild the publication package

The paper-completion workflow regenerates publication outputs from locked evidence, retains finite-horizon censoring, resamples whole trajectories for secondary intervals and builds checksummed submission bundles. Historical artifacts remain immutable.

### Level 3 — reproduce condition campaigns

The warning-blind campaigns can be rerun independently:

- recurrent-turnover source/loss calibration;
- historical Phase E/F/G condition tests;
- high-precision Phases K–Q;
- historical Protocol 003 portability validation.

A rerun with new seeds creates a new finite evidence set and must not overwrite locked historical or precision results.

## Historical screen and precision protocol

The preregistered R1–R4 classifier is retained exactly for historical reproducibility. Its R3/R4 labels are no longer interpreted as biological estimands by themselves.

The precision-validation protocol is:

1. reuse every historical master seed for the disputed contrast;
2. increase to 100 attempted replicates per seed block;
3. require exact first-20 eligible/loss prefix reproduction;
4. retain the historical `[0.30,0.70]` screen unchanged;
5. report pooled functional-loss incidence separately;
6. report an equal-rate diagnostic across high-precision blocks;
7. for paired perturbations, report bidirectional switches and exact McNemar evidence.

This protocol was motivated by Phase J/L finite-sample audits and confirmed by Phase K, where conflicting low-replicate Phase-H/I labels converged to R4 in both exact historical seed families at high precision.

## Locked precision evidence

- Phase K seed-family replay: run `32557289628`, artifact `9471883061`.
- Phase L cross-campaign R3 audit: run `32557903970`, artifact `9471949092`.
- Phase M connectivity: run `32558147960`, artifact `9472067167`, digest `sha256:0b15ca5a3b7f40a24332f8bcc14fad01036ed2d3fb4c0ff7ff181208a5d940d6`.
- Phase N partner loss: run `32558466157`, artifact `9472148035`, digest `sha256:c55654b556280c5caa63ee1b9febe62a0b545da6227104799014484f65dc25c0`.
- Phase O immediate frontier: run `32558742101`, artifact `9472838181`, digest `sha256:4b39d7df5d60b08bef0f78eb59524510c5549bae9199064f5a9841164db9a610`.
- Phase P outer frontier: scientific run `32562175464`; the five seed artifact IDs/digests and deterministic aggregate are committed in `artifacts/high_precision_condition_map.json`.
- Phase Q aggregate interaction support: run `32559058069`, artifact `9472941879`, digest `sha256:7ccaf8efd253499f047de2a40a35eaab6007292005814fc2f9539b66891d3df7`.

## Current reproducible condition conclusions

Recurrent turnover: pooled loss declines from about `.682` at `p_star=.325` through intermediate `.350–.375` conditions to `.273` at `.400`; no tested high-precision frontier condition shows detectable excess block heterogeneity.

Connectivity: only `m=.10` shows detectable high-precision between-block heterogeneity; the response is non-monotone and paired marginal-risk tests are null.

Aggregate feedback: all three predeclared `kappa=3.0/4.5/6.0` remain intermediate at high precision with no detected block heterogeneity.

Reduced-form partner loss: intact/even/graded/dominant architectures have similar high-precision incidence and no detected block heterogeneity; paired trajectory identities nevertheless switch frequently.

## Interpretation safeguards

Reproduction must preserve that:

- parent trajectories and extension trajectories are separate evidence;
- historical Protocol 002 remains 15/15 `no_domain_selected` under its original screen;
- the historical R1–R4 screen is a calibration device, not a latent biological classification;
- Phase M `migration_rate` is allele-frequency mixing, not demographic, pollinator, pollen, seed or recolonisation movement;
- Phase Q `interaction kappa` is aggregate positive feedback, not partner richness, connectance or network simplification;
- Phase N is reduced-form and does not represent explicit network topology or adaptive rewiring;
- no outcome-informed parameter refinement is opened to recover an old R3/R4 pattern;
- Protocol 003 tests bounded portability across non-matched calibrated domains, **not a single-factor effect of transition direction**;
- finite-horizon non-events remain right-censored;
- `p_star` is an effective recurrent-transition equilibrium, not an estimated biological mutation rate;
- a successful build does not convert finite Type S results into a theorem.

## Archival release checklist

Before final deposition, merge only after protocol/manuscript/figure/bundle checks pass; run the paper-completion workflow from merged `main`; verify checksums and final figure rendering; create immutable releases for both repositories; archive the release pair and bundle; and add author-approved DOI, authorship, funding, licence and CRediT metadata.
