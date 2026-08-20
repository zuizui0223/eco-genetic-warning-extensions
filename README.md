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
| **H-MD-1** | Do recurrent-transition coordinates change whether a high-function source can be established? | **2,269 of 3,375** attempts supported source preparation/projection; support 44.89–86.67% across the common grid | **supported, finite Type S** |
| **H-MD-2** | Under the same deterioration family, do recurrent-transition coordinates change the realised functional-loss regime? | 648 complete candidates split into 322 rapid-loss, 242 persistence, and 84 seed-heterogeneous candidates | **supported, finite Type S** |
| **H-MD-3a** | Does the common candidate family contain an eligible intermediate-risk warning-validation domain at each coordinate? | eligible set empty at all 15 coordinates; 15/15 `no_domain_selected` | **negative result, recovered for the declared grid/family** |
| **H-MD-3b** | If matched evaluable domains exist, does recurrent-transition direction itself change warning reliability? | the matched common-grid prerequisite failed; Protocol 003 domains are not single-factor matched | **matched finite effect unresolved** |

H-MD-3a/3b are a **post hoc logical decomposition** of the original H-MD-3 question. They do not introduce a new simulation or pretend to be preregistered labels; they make explicit which part of H-MD-3 the completed evidence resolves.

## Why H-MD-3a is a real negative result

For recurrent-transition coordinate `θ`, let `E_θ` be the set of complete Protocol 002 candidates whose five seed-block trait-loss frequencies are all in the preregistered `[0.30, 0.70]` interval.

The Protocol 002 selector can choose a warning-validation domain **if and only if** `E_θ` is non-empty. The stored Stage II calibration shows `E_θ = ∅` for every one of the 15 coordinates. Therefore, within the declared common deterioration family and strict gate, a matched warning-validation comparison does not exist.

This is not evidence that genetic warning failed: warning and diversity fields were unavailable during calibration. It is a finite **evaluability certificate** for the declared candidate family.

## What is now recovered theoretically around H-MD-3b

For single-locus expected heterozygosity `H(p)=2p(1-p)` and transition map

`M(p) = p + kappa_mu * (p_star - p)`, the exact one-step diversity change is

`H(M(p)) - H(p) = 2*kappa_mu*(p_star-p)*(1-2p-kappa_mu*(p_star-p))`.

The derivative with respect to `p_star` changes sign at `M(p)=0.5`. Thus transition direction can raise or lower diversity depending on the current allele-frequency state.

For fixed patch weights,

`H_gamma' - H_alpha' = (1-kappa_mu)^2 * (H_gamma-H_alpha)`.

The contraction of the alpha/gamma gap depends on transition strength but **not** on direction. Direction moves the weighted mean state; `kappa_mu` contracts among-patch frequency differences.

A stronger exact decoupling also holds for a local high-associated allele condition `M(p) >= p_c`. Its support margin `S=M(p)-p_c` satisfies

`dS/dp_star = kappa_mu > 0`,

so increasing `p_star` always makes that local high-state condition easier to satisfy. But

`dH(M(p))/dp_star = 2*kappa_mu*(1-2M(p))`.

Therefore, whenever `M(p)>0.5`, increasing `p_star` **strengthens local high-state allele support while decreasing heterozygosity**. At `M(p)<0.5`, support and diversity increase together; at exactly `0.5`, support increases while diversity is stationary to first order.

This is an exact **function-support/diversity decoupling boundary**. Genetic diversity is therefore not a monotone proxy for local functional support under recurrent transitions.

These Type T identities are documented in [`docs/RECURRENT_TRANSITION_DIVERSITY_THEORY.md`](docs/RECURRENT_TRANSITION_DIVERSITY_THEORY.md), implemented in `mutation_coordinates.py`, and tested directly. They do not determine full dynamic warning first-passage ordering.

## What Protocol 003 does — and does not do

Protocol 003 was declared only after Protocol 002 closed. Warning-blind candidate expansion and independent confirmation recovered two evaluable domains:

- recalibrated symmetric domain;
- directional calibrated domain.

They differ in recurrent-transition parameters **and** `A_ref`, interaction-feedback `kappa`, deterioration strength, and horizon. Stage III is therefore **not a single-factor causal effect** experiment. It is a portability comparison across independently calibrated eco-genetic domains, not a recovery of H-MD-3b as a direction-only causal effect.

Observed Stage III results:

- recalibrated symmetric domain: **323 leads**, 1 tie, 0 lags across 324 valid endpoint comparisons; valid-pair availability `0.540`;
- directional calibrated domain: **184 leads**, 5 ties, 12 lags across 201 valid endpoint comparisons; valid-pair availability `0.335`;
- directional `H_gamma` 20%: warning incidence `41/81`, realised functional-trait-loss incidence `52/81`;
- all six full-horizon-normalized direct timing-difference intervals include zero.

So warning behaviour was not invariant across the two calibrated domains, but the cause cannot be assigned to recurrent-transition direction alone.

## Final scientific chain

```text
parent H1/H3 mechanism
→ change recurrent-transition closure
→ H-MD-1: source feasibility changes
→ H-MD-2: functional-loss regime changes
→ H-MD-3a: common matched warning domain absent in the declared family
→ H-MD-3b: matched direction-only warning effect empirically unidentified
      ├─ direction has no universal sign on heterozygosity
      └─ stronger local high-state support can coincide with lower diversity
→ Protocol 003: separate portability result across recalibrated domains
```

The extension's strongest conclusion is therefore upstream of warning timing:

> **Recurrent-transition dynamics reshape the existence and loss of a high-function state, and genetic diversity need not move monotonically with that functional support. A direction-only warning effect cannot be inferred until both a matched event regime and a state-constrained prediction exist.**

## Stop rule before any new finite campaign

Do **not** open a Protocol 004 merely by widening the Protocol 002 schedule search or relaxing its gate. The current evidence already establishes that the original matched candidate family has no eligible domain, and the theory shows that direction alone has no universal diversity sign.

A new finite H-MD-3b campaign is justified only if it predeclares all of the following before simulation:

1. a matched deterioration family that preserves all non-direction parameters across compared coordinates;
2. an evaluability criterion fixed without warning/diversity fields;
3. an explicit allele-frequency state/path region, such as a high-frequency regime with `M(p)>0.5`;
4. a directional prediction derived from the exact support/diversity identities above;
5. fresh calibration and validation seeds.

Until those conditions are specified, H-MD-3b remains a bounded unresolved finite effect rather than an invitation to tune the existing campaign until a warning contrast appears.

## Protocol map

- **Protocol 001 — historical bridge/pilot.** Original H2-R-AS directional-warning formulation; retained for provenance, not the current headline structure.
- **Protocol 002 Stage I — H-MD-1.** Common-grid source reconstruction.
- **Protocol 002 Stage II — H-MD-2 + H-MD-3a.** Common-family loss-regime mapping and strict no-domain certificate.
- **Protocol 003 — separate portability analysis.** Warning-blind recalibration, confirmation, and fresh-seed validation in two non-matched domains.
- **Secondary review audit.** Locked-record uncertainty/censoring analysis; no simulation rerun or domain reselection.

## Publication and reproducibility

The current integrated manuscript and checksummed **submission bundle** are downstream publication products of this scientific state; they do not define the hypotheses. The bundle preserves the pinned parent scientific source, the separately archived post-review fragmentation sensitivity, extension software, machine-readable tables, figures, and provenance manifests.

## Source of truth

- [`docs/HYPOTHESIS_PROGRAM.md`](docs/HYPOTHESIS_PROGRAM.md) — current hypothesis definitions and recovery status
- [`docs/RECURRENT_TRANSITION_DIVERSITY_THEORY.md`](docs/RECURRENT_TRANSITION_DIVERSITY_THEORY.md) — exact recurrent-transition diversity/support identities
- [`manuscript/claim_evidence_map.md`](manuscript/claim_evidence_map.md) — permitted/prohibited numerical claims
- [`manuscript/main_text.md`](manuscript/main_text.md) — current integrated manuscript, downstream of the scientific repository state
- [`manuscript/artifact_index.md`](manuscript/artifact_index.md) — workflow/artifact provenance
- [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) — exact reproduction and archive guide
- [`docs/README.md`](docs/README.md) — active versus historical documentation map

All numerical conclusions are finite Type S evidence for their declared model closures. Final author metadata, licence, release, and DOI decisions remain outside the scientific hypothesis program.