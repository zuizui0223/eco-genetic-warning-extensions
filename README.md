# Eco-genetic warning extensions

This repository is the **second computational phase** of the integrated eco-genetic warning study. Its central question is not whether genetic diversity is always an early warning. It asks:

> **When recurrent state-transition dynamics change, do they first change the ability to establish a high-function state, then the way functional loss occurs, and only after that the conditions under which genetic warning can be evaluated?**

The repository therefore has a three-step hypothesis structure. The first two steps are directly identified on a common parameter grid; the third is only conditionally evaluable because the common calibration produced no shared warning-validation domain.

## What comes from the parent repository

[`eco-genetic-criticality`](https://github.com/zuizui0223/eco-genetic-criticality) supplies the mechanistic foundation:

1. **H1 / interaction criticality:** interaction feedback can support distinct low- and high-function states in the declared model;
2. **H3 / fragmentation:** projecting the same prepared high state into isolated fragments lowers interaction, local effective size, and realised high-trait mass;
3. **H2-R benchmark:** in one warning-blind calibrated symmetric domain, baseline-relative diversity erosion preceded all observed functional-trait losses, whereas fixed absolute diversity thresholds produced both leads and lags.

Those are **not new hypotheses of this repository**. Parent trajectories are never pooled with extension trajectories. The historical parent scientific state remains pinned at:

```text
repository: zuizui0223/eco-genetic-criticality
commit:     dd8ee379d0d3518194c767d16402042525bc00dc
```

A post-review fragmentation-gradient sensitivity was later run in the parent repository and archived separately; it is supplementary evidence and does not replace the historical H1/H3 ledger.

## The extension hypothesis chain

### H-MD-1 — Does recurrent-transition direction change high-function source feasibility?

At fixed transition relaxation strength `kappa_mu`, changing the transition equilibrium `p_star` changes the local pre-transition frequency needed to remain above a high-state boundary. The finite-model question is whether that mechanism reorganises the region in which a prepared high-function state can actually be reconstructed and projected.

**How it was tested.** Protocol 002 Stage I used a common 15-coordinate grid (`3 kappa_mu × 5 p_star`) with independent source reconstruction at every coordinate.

**Result.** 2,269 of 3,375 attempts completed source preparation and supported projection. Coordinate support ranged from 44.89% to 86.67%; within fixed-`kappa_mu` rows, support generally increased with `p_star`.

**Status.** **Supported for the declared finite closure.** This is a direct common-grid result.

### H-MD-2 — Does recurrent-transition direction change the way functional loss occurs?

If source feasibility changes, the next question is whether the same deterioration family produces the same loss process across coordinates.

**How it was tested.** Protocol 002 Stage II applied the same predeclared deterioration family across the 15-coordinate grid. Calibration could inspect source/projection eligibility, baseline high-trait presence, trait-loss occurrence, and trait-loss time, but not diversity, warning time, lead/lag, or lead time.

**Result.** Among 648 complete five-seed candidates, 322 were rapid-loss-side, 242 persistence-side, and 84 seed-heterogeneous. No candidate satisfied the strict all-seed intermediate-risk gate; all 15 coordinates were recorded as `no_domain_selected`.

**Status.** **Supported for the declared finite closure.** Recurrent-transition coordinates reorganised the functional-loss regime itself.

This is the key upstream result: before asking whether a genetic signal leads functional loss, the system must first generate a reproducible event regime in which that comparison is possible.

### H-MD-3 — Does genetic-warning reliability change across recurrent-transition conditions?

The intended third question was whether relative genetic-diversity warning has different availability, ordering, and lead time across recurrent-transition conditions.

**What happened.** Protocol 002 could not provide a common matched warning-validation domain at any of the 15 coordinates. Therefore H-MD-3 was **not cleanly testable as a common-grid single-factor contrast**.

Protocol 003 was then declared separately. It used warning-blind candidate expansion, a new event-risk gate, fresh calibration/confirmation seeds, and finally recovered two evaluable domains. Those domains differ not only in recurrent-transition parameters but also in `A_ref`, interaction-feedback `kappa`, deterioration strength, and horizon.

**Stage III result.** Warning remained predominantly leading when valid pairs were observed, but warning availability fell from 0.540 in the recalibrated symmetric domain to 0.335 in the directional calibrated domain, and ties/lags appeared. For the 20% `H_gamma` endpoint in the directional domain, warning was observed in 41/81 baseline-eligible completed trajectories while realised functional-trait loss occurred in 52/81. Direct whole-trajectory bootstrap contrasts showed endpoint-dependent absolute timing and no separated full-horizon-normalized timing contrast.

**Status.** **Not recovered as a clean transition-direction hypothesis.** The defensible result is a **portability/boundary result**: after warning-blind recalibration, warning availability and ordering were not invariant across two non-matched eco-genetic domains, but Stage III cannot identify a transition-direction-only timing effect.

## The biological story in one line

```text
recurrent-transition dynamics
→ change whether a high-function source can be established
→ change whether deterioration produces rapid loss, persistence, or unstable/seed-dependent loss
→ determine whether a genetic-warning comparison is even available
→ only then can warning ordering be interpreted within a calibrated domain
```

So this repository does **not** conclude that “directional mutation makes warning fail” or that “genetic diversity always warns before function is lost.” Its strongest extension conclusion is:

> **The biological process that generates functional loss also determines whether an early-warning test is evaluable; warning performance is downstream of that event-regime structure.**

## Why the older H2-R-AS wording still appears in history

Protocol 001 was the original directional-mutation pilot and framed a special-case hypothesis, H2-R-AS, about relative-diversity warning preceding trait loss under directional recurrent mutation. That framing is retained as project history in the Protocol 001 and decision-log documents, but it is **not the final paper-level hypothesis structure**. The completed project is better represented by H-MD-1, H-MD-2, and H-MD-3 above.

## Protocol map

- **Protocol 001 — historical bridge/pilot.** Initial asymmetric/directional recurrent-mutation formulation; useful for provenance, not the final headline result.
- **Protocol 002 — common-grid identification.** Directly tests source feasibility and loss-regime structure, and attempts strict warning-blind selection of a common validation domain. Closed with 15/15 `no_domain_selected`.
- **Protocol 003 — separate evaluability recovery.** Warning-blind candidate expansion, amended event-risk gate, independent confirmation, and fresh-seed validation in two recalibrated domains.
- **Secondary review audit — data-only uncertainty/identification audit.** Uses locked Stage III records; no simulation rerun, domain reselection, or endpoint change.

## Locked headline numbers

- **Common-grid source feasibility:** 2,269 / 3,375 supported projections; 44.89%–86.67% across coordinates.
- **Common deterioration family:** 20,250 attempts; 648 complete candidates; 322 rapid-loss-side, 84 seed-heterogeneous, 242 persistence-side; 0 eligible; 15/15 `no_domain_selected`.
- **Recalibrated symmetric Stage III domain:** 323 leads, 1 tie, 0 lags across 324 valid endpoint comparisons; valid-pair availability 0.540.
- **Directional calibrated Stage III domain:** 184 leads, 5 ties, 12 lags across 201 valid endpoint comparisons; valid-pair availability 0.335.
- **Timing audit:** all six full-horizon-normalized directional-minus-symmetric 95% difference intervals include zero; Stage III is not a direction-only timing experiment.

All endpoint rows within a trajectory are correlated repeated summaries. Uncertainty resamples whole attempted trajectories. All numerical conclusions are finite Type S evidence for their declared model closures.

## Publication and reproducibility

The publication source of truth is [`manuscript/main_text.md`](manuscript/main_text.md). Permitted and prohibited claims are locked in [`manuscript/claim_evidence_map.md`](manuscript/claim_evidence_map.md). Exact parent/extension evidence locks are recorded in [`reproducibility/upstream-lock.json`](reproducibility/upstream-lock.json).

Key entry points:

- [`docs/PAPER_001_MUTATION_DIRECTION_PHASE_DIAGRAM.md`](docs/PAPER_001_MUTATION_DIRECTION_PHASE_DIAGRAM.md) — paper-level H-MD-1/H-MD-2/H-MD-3 definitions;
- [`docs/HYPOTHESIS_PROGRAM.md`](docs/HYPOTHESIS_PROGRAM.md) — current hypothesis status and how the protocols map onto it;
- [`manuscript/claim_evidence_map.md`](manuscript/claim_evidence_map.md) — permitted/prohibited claims;
- [`manuscript/artifact_index.md`](manuscript/artifact_index.md) — workflow, artifact, and digest provenance;
- [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) — reproduction and archival guide;
- [`docs/PROTOCOL_003_AMENDMENT_001.md`](docs/PROTOCOL_003_AMENDMENT_001.md) and [`docs/PROTOCOL_003_AMENDMENT_002.md`](docs/PROTOCOL_003_AMENDMENT_002.md) — the separately declared warning-blind recalibration history;
- [`docs/PROTOCOL_003_SECONDARY_WARNING_AUDIT.md`](docs/PROTOCOL_003_SECONDARY_WARNING_AUDIT.md) — timing, censoring, bootstrap, and identification audit.

Final author order, affiliations, CRediT roles, licence, funding, conflicts, archive DOI, and repository citation metadata require explicit author approval and are not inferred by automation.
