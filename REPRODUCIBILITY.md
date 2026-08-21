# Reproducibility guide

This repository is the **independent condition-recovery extension and submission orchestrator** for the eco-genetic warning study. It depends on a fixed scientific state of [`eco-genetic-criticality`](https://github.com/zuizui0223/eco-genetic-criticality), but does not rewrite or retroactively enlarge the parent evidence ledger.

## Repository roles

| repository | role | scientific boundary |
|---|---|---|
| `eco-genetic-criticality` | mechanistic parent | theorem-guided interaction/fragmentation framework, locked H1/H3 campaign, inherited symmetric warning benchmark |
| `eco-genetic-warning-extensions` | condition-recovery extension | recurrent-transition source/loss maps, prospective R4 recovery, connectivity, aggregate interaction-support and reduced-form partner-loss conditions, bounded portability validation, manuscript/bundle |

The parent scientific commit is fixed at `dd8ee379d0d3518194c767d16402042525bc00dc`; the machine-readable lock is `reproducibility/upstream-lock.json`.

## Reproduction levels

### Level 1 — package and invariant tests

```bash
git clone https://github.com/zuizui0223/eco-genetic-warning-extensions.git
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

This verifies package imports, scientific locks, protocol invariants, manuscript contracts, historical Stage III totals and the condition-first interpretation boundaries.

### Level 2 — rebuild the publication package from locked evidence

The canonical **Paper completion sprint** downloads immutable Stage I/II publication artifacts and the two historical Stage III validation artifacts, regenerates the secondary trajectory-level audit and figures, builds both packages/source archives, assembles the manuscript/evidence bundle and writes SHA-256 digests for bundled files.

The source Stage III artifacts remain immutable historical evidence. Conventional-median correction, horizon normalization, cumulative event-incidence curves and trajectory-cluster intervals are explicit secondary analyses of those payloads.

### Level 3 — reproduce condition-recovery campaigns

The warning-blind condition campaigns remain separately reproducible:

- recurrent-turnover common grid and prospective frontier recovery;
- Phase E effective genetic connectivity at the recovered R4 anchor;
- Phase F aggregate interaction support at the same anchor;
- Phase G reduced-form matched one-partner loss at a fresh reproduced R4 anchor.

A rerun with new seeds creates a new finite Type S evidence set and must not overwrite the locked historical results.

#### Phase F — aggregate interaction support

Phase F is closed. Its prospective design used `interaction kappa = 3.0, 4.5, 6.0`, `A_ref=1.0`, `kappa_mu=0.35`, `p_star=0.35`, migration 0, horizon 120, normalized barrier increase 0.30, five master seeds × 20 attempts and independent source reconstruction at every kappa.

| kappa | source/baseline eligible | pooled loss | regime |
|---:|---:|---:|---|
| 3.0 | 77/100 | 0.468 | R4-highrep |
| 4.5 | 94/100 | 0.521 | R4-highrep |
| 6.0 | 87/100 | 0.552 | R4-highrep |

Run `32441549848`; artifact `9432854668`; artifact digest `sha256:bb221af16a9b6557280610e90807fdfe058dccbafd7d0183e38d4525ecef2c16`; committed compact evidence `artifacts/interaction_support/phase_f_summary.json`.

#### Phase G — reduced-form matched one-partner loss

Phase G is closed. Four partner contributions summed to one before deterioration. The intact control retained all four partners; each loss architecture removed exactly one partner. Lost-partner identity was balanced prospectively across each 20-replicate seed block. The three loss architectures shared the same `4→3` richness change and mean retained interaction support `0.75` while contribution concentration differed.

| condition | baseline eligible | pooled loss | seed-rate range | regime |
|---|---:|---:|---:|---|
| intact control | 90/100 | 0.544 | 0.129 | R4-highrep |
| even redundant loss | 90/100 | 0.567 | 0.261 | R3-highrep |
| graded-contribution loss | 90/100 | 0.556 | 0.353 | R3-highrep |
| dominant-partner loss | 90/100 | 0.578 | 0.235 | R3-highrep |

Paired loss status switched in both directions relative to intact. The labelled secondary paired-incidence audit gave Cochran's Q `p=0.943`, so the locked interpretation is a classifier-level change in **loss-regime reproducibility / warning estimability**, not a directional increase in pooled failure risk. Contribution concentration itself did not separate regimes because all three loss architectures were R3.

Run `32450362310`; artifact `9435520830`; artifact digest `sha256:669cfc468f8a36e53ccc157aaa97e5a4de14f6ad7c09458ed105762e4d0d6ec7`; committed compact evidence `artifacts/partner_redundancy/phase_g_summary.json`.

The Phase-G closure is reduced-form only. It does not simulate connectance, nestedness, modularity, adaptive rewiring, partner population dynamics, coextinction or biological movement. No partner weights, removal identities or thresholds are tuned after the result.

## Locked/committed evidence used by the study

- parent scientific commit `dd8ee379d0d3518194c767d16402042525bc00dc`;
- inherited H1/H3 primary campaign: parent run `28456092898`, artifact `7987193632`;
- fresh fragmentation gradient: parent run `31937210601`, artifact `9261157020`;
- common source reconstruction: 3,375 attempts over six workflow runs;
- strict common loss calibration: 20,250 attempts, 648 complete candidates, historical 15/15 `no_domain_selected`;
- prospective R4 recovery: committed Phase C/D summaries under `artifacts/frontier_refinement/`;
- connectivity condition: Phase E run `32376912392`, artifact `9409687687`, committed summary under `artifacts/migration_condition/`;
- interaction-support condition: Phase F run/artifact above;
- reduced-form partner-loss condition: Phase G run/artifact above;
- historical Protocol 003 validation: run `29417632137`, 200 attempted trajectories;
- recalibrated symmetric artifact `8343958766`, digest `sha256:c1b42fc9e6ac912a44667ef4cee02090fab37d50fc3a9928c46ae728c0610f58`;
- directional calibrated artifact `8343922879`, digest `sha256:0a994bea874fc9c47544169cd31bbc317c88690dfe1b6fa7548516e35fd7bca8`;
- historical Stage III summary `artifacts/protocol003/stage3_validation_summary.json`;
- post-review compact audit `manuscript/tables/stage3_review_summary.csv`;
- publication manuscript `manuscript/main_text.md`.

Exact workflow IDs, artifact IDs, digests and claim boundaries are recorded in `manuscript/artifact_index.md` and `manuscript/claim_evidence_map.md`.

## Interpretation safeguards

Reproduction must preserve all of the following:

- parent trajectories and extension trajectories are separate evidence;
- historical Protocol 002 remains 15/15 `no_domain_selected` under its original strict all-seed rule;
- prospective high-rep refinement later recovered a narrow R4 condition without inspecting warning/diversity fields;
- Phase E `migration_rate` is allele-frequency mixing, not demographic, pollinator, pollen, seed or recolonisation movement;
- Phase F `interaction kappa` is aggregate positive-feedback/effective interaction support, not partner richness, connectance or network simplification;
- all three Phase-F kappa levels retained R4, so the tested interaction-support range is a bounded robustness result rather than an identified R4 boundary;
- no finer/wider kappa search is opened merely to manufacture a boundary;
- Phase G is a reduced-form partner-contribution perturbation, not an explicit network/connectance/rewiring model;
- all three Phase-G one-partner-loss architectures became R3 while pooled loss remained similar; this is not evidence of a universal increase in mean failure probability;
- the Phase-G contribution-concentration contrast is negative at regime level and no post-result partner-weight tuning is opened;
- Protocol 003 is separately declared and its two validation domains differ in ecological, recurrent-transition and deterioration parameters;
- Stage III therefore tests bounded portability across calibrated eco-genetic domains, not a direction-only effect;
- endpoint rows from the same trajectory are correlated; secondary intervals resample whole attempted trajectories;
- finite-horizon non-events remain censored rather than assigned the final generation;
- `p_star` is an effective recurrent-transition equilibrium, not an estimated biological mutation rate;
- a successful build does not convert finite Type S results into a theorem.

## Archival release checklist

Before final repository deposition:

1. merge only after protocol, manuscript, figure and bundle checks pass;
2. run **Paper completion sprint** from merged `main`;
3. download and independently verify the checksummed bundle;
4. render all publication figures at final journal width in colour and grayscale;
5. build the final submission document from the single `manuscript/main_text.md` source rather than resurrecting deleted working drafts;
6. create immutable releases for both repositories;
7. archive the release pair and bundle in Zenodo or equivalent;
8. add final DOI, author-approved metadata, licence and CRediT statements.

Authorship, licence, funding, conflicts and CRediT roles remain explicit author decisions.
