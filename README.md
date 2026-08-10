# Eco-genetic warning extensions

Independent, protocol-locked extensions of the finite eco-genetic criticality framework, plus the reproducible submission package for the integrated Ecology Letters manuscript.

## Current status

The directional-transition campaigns are complete. The repository now contains:

- an algebraic certificate for 15 predeclared transition coordinates;
- 3,375 independent source-reconstruction and projection attempts;
- 20,250 warning-blind trait-loss calibration attempts;
- a closed Protocol 002 result with 15/15 coordinates recorded as `no_domain_selected`;
- a separately declared Protocol 003 calibration and fresh-seed warning validation;
- publication tables, accessible figures, manuscript files, and a checksummed submission-bundle workflow.

The integrated manuscript entry point is [`manuscript/main_text.md`](manuscript/main_text.md). The current supervisor-facing draft is [`manuscript/supervisor_first_draft.md`](manuscript/supervisor_first_draft.md).

## Why this remains a separate repository

[`eco-genetic-criticality`](https://github.com/zuizui0223/eco-genetic-criticality) closed a finite-model campaign covering interaction-conditioned high-trait viability (H1), fragmentation effects (H3), and a conditional symmetric relative-diversity warning result (H2-R). Its numerical results remain bounded by its declared symmetric mutation, trait-recruitment, source-transfer, and deterioration closures.

This repository changes a specific genetic boundary condition and uses new source, calibration, confirmation, and validation seed families. Parent trajectories are not extension evidence, and extension results do not retroactively revise the parent ledger.

The parent scientific state is fixed at:

```text
repository: zuizui0223/eco-genetic-criticality
commit:     dd8ee379d0d3518194c767d16402042525bc00dc
```

The exact two-repository lock is recorded in [`reproducibility/upstream-lock.json`](reproducibility/upstream-lock.json).

## Paper question and mechanism

The recurrent transition operator is

\[
p_{t+1}^{\mathrm{mut}}
= u_{L\to H}+(1-u_{L\to H}-u_{H\to L})p_t,
\]

parameterised by

\[
\kappa_\mu=u_{L\to H}+u_{H\to L},\qquad
p_\mu^\ast=\frac{u_{L\to H}}{\kappa_\mu}.
\]

At fixed \(\kappa_\mu\), the study asks how transition direction changes high-trait source feasibility, realised functional-trait loss, the availability of a warning-validation regime, and the ordering and lead time of relative genetic warnings.

The broader manuscript claim is not that one direction universally causes collapse or rescue. It is that warning availability and reliability emerge from the ecological, demographic, genetic, and observation processes that jointly generate both the signal and the functional-loss event.

## Locked headline results

- **Source feasibility:** 2,269 of 3,375 attempts completed source preparation and supported projection; coordinate support ranged from 44.89% to 86.67%.
- **Warning-blind regime map:** among 648 complete candidates, 322 were rapid-loss-side, 242 persistence-side, and 84 seed-heterogeneous; no Protocol 002 coordinate met the all-seed eligibility rule.
- **Symmetric bridge:** 323 leads, one tie, and no lags across 324 valid endpoint comparisons; median positive lead time 106–112 generations.
- **Directional transition:** 184 leads, five ties, and 12 lags across 201 valid endpoint comparisons; median positive lead time 74–81 generations, with greater baseline ineligibility and censoring.

These endpoint comparisons share trajectories and are correlated repeated summaries. All numerical results remain finite Type S evidence for their declared closures.

## Package and repository architecture

The submission uses two installable packages rather than a merged code base:

```text
eco-genetic-criticality
  mechanistic parent, theorem layer, finite H1/H3 closure, symmetric benchmark

eco-genetic-warning-extensions
  directional-transition protocols, publication outputs, integrated manuscript

submission bundle
  both wheels/source distributions + figures + tables + manuscript + provenance
```

This arrangement keeps the parent evidence ledger immutable while giving reviewers one checksummed package to inspect.

## Quick reproducibility check

See [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) for the full three-level guide. The lightweight verification is:

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

The **Paper completion sprint** workflow additionally:

1. downloads immutable Stage I and Stage II publication artifacts;
2. regenerates all six figures with the current code;
3. reads the committed Stage III summary;
4. builds both software distributions;
5. assembles manuscript, figures, tables, software, and provenance;
6. writes a SHA-256 manifest for every bundled file.

## Protocol boundaries

- **Protocol 001:** three-anchor asymmetric-transition bridge/pilot.
- **Protocol 002:** 15-coordinate source reconstruction and warning-blind common-family calibration. It remains closed with `no_domain_selected` at all coordinates.
- **Protocol 003:** separately declared bracket, calibration, confirmation, and fresh-seed warning-validation campaign.

No diversity, warning time, lead/lag ordering, or lead-time quantity was available during trait-loss calibration.

## Evidence labels

- **T** — theorem under explicitly stated mathematical assumptions;
- **C** — conditional result after a declared ecological closure;
- **H** — dynamic hypothesis;
- **S** — finite, model-specific simulation evidence.

A successful software build verifies reproducibility contracts; it does not strengthen Type S evidence into a theorem.

## Key entry points

- [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) — complete reproducibility and archival guide
- [`manuscript/README.md`](manuscript/README.md) — manuscript identity and claim boundaries
- [`manuscript/artifact_index.md`](manuscript/artifact_index.md) — workflow, artifact, and digest provenance
- [`manuscript/claim_evidence_map.md`](manuscript/claim_evidence_map.md) — permitted and prohibited claims
- [`docs/PROTOCOL_002_MUTATION_DIRECTION_PHASE_DIAGRAM.md`](docs/PROTOCOL_002_MUTATION_DIRECTION_PHASE_DIAGRAM.md) — closed common-family campaign
- [`docs/PROTOCOL_003_STAGE3_OPTIONS.md`](docs/PROTOCOL_003_STAGE3_OPTIONS.md) — separately declared validation logic

Final author order, affiliations, CRediT roles, licence, funding, conflicts, archive DOI, and repository citation metadata require explicit author approval and are not inferred by automation.
