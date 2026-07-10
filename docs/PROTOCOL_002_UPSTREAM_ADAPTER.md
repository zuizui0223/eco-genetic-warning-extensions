# Protocol 002 upstream adapter contract

## Status

Adapter-contract stage only. No ecological simulation is run by this document or
by the accompanying tests.

## Pinned upstream life cycle

```text
repository: zuizui0223/eco-genetic-criticality
commit:     dd8ee379d0d3518194c767d16402042525bc00dc
module:     causal_model/symmetric_allele_mutation_closure.py
position:   after selection and migration, before finite drift
```

Protocol 002 may replace only the affine mutation transform at this position.
All selection, migration, interaction, trait recruitment, finite drift, event
semantics, and censoring logic remain outside this adapter PR.

## Symmetric bridge

The pinned upstream symmetric mutation map is

\[
p\mapsto \mu + (1-2\mu)p.
\]

The Protocol 002 coordinate

\[
\kappa_\mu = 2\mu,\qquad p_\mu^\ast=0.5
\]

is algebraically identical:

\[
\kappa_\mu p_\mu^\ast+(1-\kappa_\mu)p
=2\mu\cdot0.5+(1-2\mu)p
=\mu+(1-2\mu)p.
\]

The adapter test suite requires the difference between these two expressions to
be zero, up to floating-point tolerance, across a fixed set of allele
frequencies.

## Why this is not yet Stage I

This PR does not import the upstream simulator or run H1 source reconstruction.
The reason is deliberate: private-repository access and full simulator execution
should not be mixed with the algebraic adapter contract. A later PR must either
provide a reproducible source-vendoring decision or a CI-safe upstream checkout
strategy before source reconstruction can start.

## Next gate

The next implementation gate is a separately versioned finite-life-cycle runner
that proves the SYM bridge against the pinned upstream closure for a minimal
set of deterministic parameter fixtures. Only after that bridge passes may
Protocol 002 Stage I source reconstruction begin.
