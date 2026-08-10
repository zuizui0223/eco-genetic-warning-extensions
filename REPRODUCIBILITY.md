# Reproducibility guide

This repository is the **independent extension and integrated-submission orchestrator** for the eco-genetic warning study. It depends on a fixed scientific state of [`eco-genetic-criticality`](https://github.com/zuizui0223/eco-genetic-criticality), but it does not merge, rewrite, or retroactively enlarge the parent evidence ledger.

## Repository roles

| Repository | Submission role | Scientific boundary |
|---|---|---|
| `eco-genetic-criticality` | mechanistic parent | theorem-guided interaction/fragmentation framework and closed symmetric-warning benchmark |
| `eco-genetic-warning-extensions` | independent extension and submission orchestrator | directional recurrent-transition campaigns, integrated manuscript, figures, tables, and submission bundle |

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

This verifies package imports, protocol invariants, manuscript contracts, the exact upstream checkout, locked numerical summaries, and evidence-boundary language.

### Level 2 — rebuild the submission package from locked evidence

The canonical submission workflow downloads the immutable Stage I and Stage II publication artifacts, regenerates all figures with the current checked-out figure code, reads the committed Stage III summary, builds wheels and source distributions for both repositories, and writes a SHA-256 manifest over the complete bundle.

Run the **Paper completion sprint** workflow from GitHub Actions, or reproduce its commands locally after downloading the locked artifacts listed in `manuscript/artifact_index.md`.

The resulting bundle contains:

```text
figures/       six regenerated SVG figures
tables/        machine-readable Stage I–III summaries
manuscript/    main text, references, captions, supplement, and evidence maps
software/      parent and extension wheels/source distributions
provenance/    upstream lock, evidence ledgers, package metadata, and repository roles
manifest.json  SHA-256 digest for every bundled file
```

### Level 3 — rerun the full stochastic campaigns

The Stage I, Stage II, and Protocol 003 workflows remain available with their declared seeds and grids. A full rerun is computationally expensive and creates a new finite Type S evidence set. It is not required to regenerate the publication figures from the locked evidence summaries and must not replace the historical Protocol 002 `no_domain_selected` result or the separately declared Protocol 003 validation.

## Locked evidence used by the paper

- parent scientific commit: `dd8ee379d0d3518194c767d16402042525bc00dc`;
- Stage I source reconstruction: six workflow runs, 3,375 attempts;
- Stage II warning-blind calibration: 20,250 attempts and 648 complete candidates;
- Protocol 003 Stage III: workflow run `29417632137`, 200 attempted trajectories;
- committed Stage III summary: `artifacts/protocol003/stage3_validation_summary.json`;
- integrated manuscript entry point: `manuscript/main_text.md`;
- supervisor-facing working draft: `manuscript/supervisor_first_draft.md`.

Exact workflow IDs, artifact IDs, digests, and claim boundaries are recorded in `reproducibility/upstream-lock.json`, `manuscript/artifact_index.md`, and `manuscript/claim_evidence_map.md`.

## Interpretation safeguards

Reproduction must preserve the following distinctions:

- parent trajectories and extension trajectories are separate evidence;
- Protocol 002 remains closed with 15/15 `no_domain_selected`;
- Protocol 003 is a separately declared calibration and validation campaign;
- endpoint rows from the same trajectory are correlated repeated summaries;
- `p_mu*` is an effective recurrent-transition equilibrium, not an estimated biological mutation rate;
- finite-horizon non-events and missing warning/loss events remain censored;
- a successful build does not convert finite Type S results into a theorem.

## Archival release checklist

Before submission or repository deposition:

1. merge the parent reproducibility-maintenance PR without changing its canonical scientific commit;
2. merge this repository's reproducibility PR after both workflows pass;
3. run **Paper completion sprint** on the merged extension commit;
4. download the checksummed submission bundle;
5. inspect all six figures at final size and verify `manifest.json`;
6. create immutable releases for both repositories;
7. archive the release pair and submission bundle in Zenodo or an equivalent repository;
8. add the final DOI, author-approved citation metadata, licence, and CRediT statements.

Authorship, licence choice, funding, conflicts, and CRediT roles are not inferred by automation and remain explicit author decisions.
