# Reproducibility guide

This repository is the **independent extension and integrated-submission orchestrator** for the eco-genetic warning study. It depends on a fixed scientific state of [`eco-genetic-criticality`](https://github.com/zuizui0223/eco-genetic-criticality), but it does not merge, rewrite, or retroactively enlarge the parent evidence ledger.

## Repository roles

| Repository | Submission role | Scientific boundary |
|---|---|---|
| `eco-genetic-criticality` | mechanistic phase | theorem-guided interaction/fragmentation framework, locked H1/H3 campaign, inherited symmetric warning benchmark |
| `eco-genetic-warning-extensions` | recurrent-transition phase and submission orchestrator | common-grid source/loss-regime analyses, separately declared Protocol 003, post-review Stage III audit, integrated manuscript and bundle |

The parent scientific commit is fixed at `dd8ee379d0d3518194c767d16402042525bc00dc`. The machine-readable lock is `reproducibility/upstream-lock.json`.

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

This verifies package imports, protocol invariants, manuscript contracts, the exact upstream checkout, locked historical Stage III totals, the compact post-review audit summary, and the identification boundary.

### Level 2 — rebuild the submission package from locked evidence

The canonical **Paper completion sprint** downloads the immutable Stage I and Stage II publication artifacts and the two immutable historical Stage III validation artifacts. It then:

1. flattens the 200 Stage III attempted trajectories to 1,200 trajectory-endpoint records;
2. runs the fixed post-review secondary audit with 20,000 whole-trajectory bootstrap resamples and seed `20260814`;
3. verifies that the regenerated compact audit table is byte-identical to `manuscript/tables/stage3_review_summary.csv`;
4. regenerates all six publication SVG figures;
5. builds wheels, source distributions, and exact source archives for both repositories;
6. assembles manuscript, tables, software, evidence provenance, and the generated Stage III records/audit into one bundle;
7. writes a SHA-256 manifest over every bundled file.

The source Stage III artifacts remain the historical primary evidence. The repository does not silently replace them with a rewritten “corrected artifact.” The conventional-median correction, horizon normalization, cumulative event-incidence curves, and trajectory-cluster intervals are explicitly post-review secondary analyses of those immutable payloads.

The bundle contains:

```text
figures/       six regenerated SVG figures
tables/        Stage I/II summaries + historical Stage III summary
               + generated 1,200-row Stage III endpoint table
               + complete secondary-audit JSON + compact publication CSV
manuscript/    main text, references, captions, supplement, and evidence maps
software/      parent and extension wheels/source distributions/source archives
provenance/    upstream lock, evidence ledgers, audit documentation, package metadata
manifest.json  SHA-256 digest for every bundled file
```

### Level 3 — rerun the full stochastic campaigns

The Stage I, Stage II, and Protocol 003 workflows remain available with their declared seeds and grids. A full rerun is computationally expensive and creates a new finite Type S evidence set. It is **not** required for the post-review audit and must not overwrite the historical Protocol 002 `no_domain_selected` result or the historical Protocol 003 validation artifacts.

## Locked evidence used by the paper

- parent scientific commit: `dd8ee379d0d3518194c767d16402042525bc00dc`;
- inherited H1/H3 primary campaign: parent workflow run `28456092898`, artifact `7987193632`;
- Stage I source reconstruction: six workflow runs, 3,375 attempts;
- Stage II strict warning-blind calibration: 20,250 attempts and 648 complete candidates;
- Protocol 003 historical Stage III validation: workflow run `29417632137`, 200 attempted trajectories;
- recalibrated symmetric historical artifact: `8343958766`, digest `sha256:c1b42fc9e6ac912a44667ef4cee02090fab37d50fc3a9928c46ae728c0610f58`;
- directional calibrated historical artifact: `8343922879`, digest `sha256:0a994bea874fc9c47544169cd31bbc317c88690dfe1b6fa7548516e35fd7bca8`;
- historical committed Stage III summary: `artifacts/protocol003/stage3_validation_summary.json`;
- post-review compact audit summary: `manuscript/tables/stage3_review_summary.csv`;
- integrated manuscript: `manuscript/main_text.md` and synchronized `manuscript/supervisor_first_draft.md`.

Exact workflow IDs, artifact IDs, digests, corrected-publication values, and prohibited claims are recorded in `reproducibility/upstream-lock.json`, `manuscript/artifact_index.md`, and `manuscript/claim_evidence_map.md`.

## Protocol and interpretation safeguards

Reproduction must preserve all of the following:

- parent trajectories and extension trajectories are separate evidence;
- Protocol 002 remains closed with 15/15 `no_domain_selected` under the strict all-seed `[0.30,0.70]` rule;
- Protocol 003 is separately declared; Amendment 001 expanded its candidate family and changed its event-risk gate before warning values were calculated;
- Amendment 002 did not relax that gate further and instead increased replication with fresh confirmation seeds;
- the two Stage III validation domains differ in `A_ref`, interaction-feedback `kappa`, `kappa_mu`, `p_star`, normalized barrier increase, and calibrated horizon;
- Stage III therefore tests warning portability across calibrated eco-genetic domains, not a transition-direction-only effect;
- endpoint rows from the same trajectory are correlated repeated summaries; post-review intervals resample whole attempted trajectories;
- the historical Stage III summary's even-`n` upper-middle timing statistic remains preserved as provenance, while the publication audit uses the conventional median;
- finite-horizon non-events remain censored rather than assigned the final generation;
- `p_mu*` is an effective recurrent-transition equilibrium, not an estimated biological mutation rate;
- a successful build does not convert finite Type S results into a theorem.

## Archival release checklist

Before submission or repository deposition:

1. merge the identification-review PR only after protocol, manuscript, figure, and bundle workflows pass;
2. run **Paper completion sprint** from merged `main`;
3. download the checksummed submission bundle;
4. verify `manifest.json` independently;
5. render all six figures at final journal width in colour and grayscale;
6. rebuild the supervisor/submission DOCX from scratch so the Word package contains no orphaned old figures;
7. create immutable releases for both repositories;
8. archive the release pair and submission bundle in Zenodo or an equivalent repository;
9. add final DOI, author-approved citation metadata, licence, and CRediT statements.

Authorship, licence choice, funding, conflicts, and CRediT roles are not inferred by automation and remain explicit author decisions.
