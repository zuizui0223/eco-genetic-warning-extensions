# Eco-genetic warning extensions

Independent, predeclared biological closures for testing the robustness and limits of finite eco-genetic early-warning results.

## Why this is a new repository

`eco-genetic-criticality` closed a finite-model campaign with three canonical
results:

- H1: mutation-conditioned interaction memory was supported as finite Type S evidence;
- H3: equal isolation reduced interaction, local effective size, and realised high-trait mass conditional on full-state transfer;
- H2-R: baseline-relative diversity decline preceded observed realised trait loss in one calibration-selected deterioration configuration.

That result is deliberately **not** treated as a universal law. Its symmetric
allele-mutation closure, finite trait-recruitment closure, and selected
ramp-and-hold deterioration path are all part of the claim's boundary.

This repository starts from a clean protocol for testing what changes when a
biological closure changes. It does not silently broaden, replace, or rewrite
the completed evidence ledger in `eco-genetic-criticality`.

## First project: asymmetric recurrent mutation

Protocol 001 tests whether the conditional H2-R ordering is robust when the
symmetric allele-mutation operator is replaced by an allele-direction-specific
recurrent mutation operator:

\[
p_{t+1}^{\mathrm{mut}}
= u_{L\to H} + (1-u_{L\to H}-u_{H\to L})p_t.
\]

Here \(p_t\) is the frequency of the allele contributing to the high-trait
recruitment kernel. The former symmetric closure is recovered only when
\(u_{L\to H}=u_{H\to L}\).

The protocol is intentionally staged:

```text
new mutation closure
-> H1 source reconstruction
-> trait-loss-only deterioration calibration
-> freeze selected domain
-> fresh-seed H2-R relative-warning validation
-> fixed-threshold H2-A secondary audit
```

No genetic-warning value is used while selecting a deterioration schedule.

## Status

**Protocol stage. No new simulation result exists yet.**

See:

- [`docs/PROJECT_BOUNDARY.md`](docs/PROJECT_BOUNDARY.md)
- [`docs/PROTOCOL_001_ASYMMETRIC_MUTATION.md`](docs/PROTOCOL_001_ASYMMETRIC_MUTATION.md)
- [`docs/DECISION_LOG.md`](docs/DECISION_LOG.md)

## Evidence labels

- **T** — theorem under explicitly stated mathematical assumptions.
- **C** — conditional theorem after a stated ecological closure.
- **H** — dynamic hypothesis.
- **S** — finite, model-specific simulation evidence.

All numerical outcomes produced by this repository are Type S unless a separate
proof establishes a different label.
