# Upstream lock — Protocol 002

## Purpose

Protocol 002 is a new mutation-direction closure, not a modification of the
completed `eco-genetic-criticality` evidence ledger. This document fixes exactly
which upstream finite life cycle is referenced and which operation may change.

## Pinned upstream source

```text
repository: zuizui0223/eco-genetic-criticality
commit:     dd8ee379d0d3518194c767d16402042525bc00dc
module:     causal_model/symmetric_allele_mutation_closure.py
function:   simulate_with_symmetric_allele_mutation
```

The commit is pinned before Protocol 002 implementation. A future upstream
change does not alter this protocol unless a new lock and a new protocol number
are created.

## Inherited life-cycle position

The pinned simulator performs, per generation:

```text
resident allele frequency p_t
-> interaction / selection
-> allele-frequency migration
-> mutation
-> finite genetic drift
-> p_(t+1)
```

Trait recruitment at generation \(t\) uses the resident \(p_t\); mutation changes
\(p_{t+1}\) and therefore affects later trait recruitment and interaction
feedback. This temporal ordering is inherited without change.

## The only permitted replacement

Replace the symmetric map

\[
p\mapsto \mu+(1-2\mu)p
\]

with the direction-specific recurrent-mutation map

\[
p\mapsto u_{L\to H}+(1-u_{L\to H}-u_{H\to L})p
=\kappa_\mu p_\mu^\ast+(1-\kappa_\mu)p.
\]

No other operation may change in Protocol 002:

- no change to selection,
- no change to migration,
- no change to finite drift,
- no change to interaction support or barrier updates,
- no change to trait recruitment,
- no change to source transfer or conservation projection,
- no change to diversity statistics, and
- no change to the trait-loss event definition.

## Implementation boundary

The local `MutationCoordinates` module is an algebraic/operator layer only. It
does not copy or fork the upstream simulator. The future upstream adapter must:

1. import or reproduce the pinned life cycle under a separately recorded license
   and provenance decision;
2. change only the post-migration/pre-drift mutation transform;
3. prove the SYM bridge with exact regression tests; and
4. write the upstream commit and adapter version into every artifact manifest.

Until that adapter exists, Protocol 002 is limited to Stage 0 algebraic
certification and no ecological simulation result may be reported.
