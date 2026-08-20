# Eco-genetic warning extensions

This repository is the **second computational phase** of the integrated eco-genetic warning study. The recurrent-transition campaigns are complete.

Its question is not simply whether genetic diversity is an early warning. It asks what happens after the recurrent state-transition process is changed:

```text
Can a high-function state be established?
        ↓
How does realised functional loss occur?
        ↓
Is there a comparable domain in which genetic warning can be tested?
        ↓
Only then: how does warning behave within that domain?
```

## What is inherited, not retested here

The parent repository [`eco-genetic-criticality`](https://github.com/zuizui0223/eco-genetic-criticality) supplies the mechanistic foundation:

- **H1:** interaction feedback can support distinct low- and high-function states in the declared model;
- **H3:** fragmentation of the same prepared high state lowers interaction, local effective size, and realised high-trait mass;
- **H2-R benchmark:** relative diversity erosion preceded observed functional-trait loss in one warning-blind calibrated symmetric domain, while fixed absolute thresholds produced both leads and lags.

These are not extension hypotheses. Parent and extension trajectories are never pooled. The historical parent scientific state is pinned at `dd8ee379d0d3518194c767d16402042525bc00dc`.

## Current extension hypothesis status

| hypothesis | question | result | status |
|---|---|---|---|
| **H-MD-1** | Do recurrent-transition coordinates change whether a high-function source can be established? | 2,269/3,375 supported projections; support 44.89–86.67% across the common grid | **supported, finite Type S** |
| **H-MD-2** | Under the same deterioration family, do recurrent-transition coordinates change the realised functional-loss regime? | 648 complete candidates split into 322 rapid-loss, 242 persistence, and 84 seed-heterogeneous candidates | **supported, finite Type S** |
| **H-MD-3a** | Does the common candidate family contain an eligible intermediate-risk warning-validation domain at each coordinate? | eligible set empty at all 15 coordinates; 15/15 `no_domain_selected` | **negative result, recovered for the declared grid/family** |
| **H-MD-3b** | If matched evaluable domains exist, does recurrent-transition direction itself change warning reliability? | the matched common-grid prerequisite failed; Protocol 003 domains are not single-factor matched | **unresolved / not identified** |

H-MD-3a/3b are a **post hoc logical decomposition** of the original H-MD-3 question. They do not introduce a new simulation or pretend to be preregistered labels; they make explicit which part of H-MD-3 the completed evidence actually resolves.

## Why H-MD-3a is a real negative result

For recurrent-transition coordinate `θ`, let `E_θ` be the set of complete Protocol 002 candidates whose five seed-block trait-loss frequencies are all in the preregistered `[0.30, 0.70]` interval.

The Protocol 002 selector can choose a warning-validation domain **if and only if** `E_θ` is non-empty. The stored Stage II calibration shows `E_θ = ∅` for every one of the 15 coordinates. Therefore, within the declared common deterioration family and strict gate, a matched warning-validation comparison does not exist.

This is not evidence that genetic warning failed: warning and diversity fields were unavailable during calibration. It is a finite **evaluability certificate** for the declared candidate family.

## What Protocol 003 does — and does not do

Protocol 003 was declared only after Protocol 002 closed. Warning-blind candidate expansion and independent confirmation recovered two evaluable domains:

- recalibrated symmetric domain;
- directional calibrated domain.

They differ in recurrent-transition parameters **and** `A_ref`, interaction-feedback `kappa`, deterioration strength, and horizon. Thus Stage III is a **portability comparison across independently calibrated eco-genetic domains**, not a recovery of H-MD-3b as a direction-only causal effect.

Observed Stage III results:

- valid-pair availability: `0.540` vs `0.335`;
- ordering: `323/1/0` vs `184/5/12` lead/tie/lag;
- directional `H_gamma` 20%: warning incidence `41/81`, realised functional-trait-loss incidence `52/81`;
- all six full-horizon-normalized direct timing-difference intervals include zero.

So warning behaviour was not invariant across the two calibrated domains, but the cause cannot be assigned to recurrent-transition direction alone.

## Final scientific chain

```text
parent H1/H3 mechanism
→ change recurrent-transition closure
→ H-MD-1: source feasibility changes
→ H-MD-2: functional-loss regime changes
→ H-MD-3a: a common evaluable warning domain is not guaranteed and was absent here
→ H-MD-3b: direction-only warning effect remains unidentified
→ Protocol 003: separate portability result across recalibrated domains
```

The extension's strongest conclusion is therefore upstream of warning timing:

> **Recurrent-transition dynamics reshape both the existence of a high-function state and the way that function is lost; those changes can remove the matched event regime required to identify a direction-only genetic-warning effect.**

## Protocol map

- **Protocol 001 — historical bridge/pilot.** Original H2-R-AS directional-warning formulation; retained for provenance, not the current headline structure.
- **Protocol 002 Stage I — H-MD-1.** Common-grid source reconstruction.
- **Protocol 002 Stage II — H-MD-2 + H-MD-3a.** Common-family loss-regime mapping and strict no-domain certificate.
- **Protocol 003 — separate portability analysis.** Warning-blind recalibration, confirmation, and fresh-seed validation in two non-matched domains.
- **Secondary review audit.** Locked-record uncertainty/censoring analysis; no simulation rerun or domain reselection.

## Source of truth

- [`docs/HYPOTHESIS_PROGRAM.md`](docs/HYPOTHESIS_PROGRAM.md) — current hypothesis definitions and recovery status
- [`manuscript/claim_evidence_map.md`](manuscript/claim_evidence_map.md) — permitted/prohibited numerical claims
- [`manuscript/main_text.md`](manuscript/main_text.md) — current integrated manuscript, downstream of the scientific repository state
- [`manuscript/artifact_index.md`](manuscript/artifact_index.md) — workflow/artifact provenance
- [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) — exact reproduction and archive guide
- [`docs/README.md`](docs/README.md) — active versus historical documentation map

All numerical conclusions are finite Type S evidence for their declared model closures. Final author metadata, licence, release, and DOI decisions remain outside the scientific hypothesis program.