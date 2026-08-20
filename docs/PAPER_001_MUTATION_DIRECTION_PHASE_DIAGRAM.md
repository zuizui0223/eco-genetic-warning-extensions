# Historical Paper 001 design note — recurrent-transition direction

> **Status: historical design record, superseded as a current hypothesis source.**
>
> The current scientific source of truth is [`HYPOTHESIS_PROGRAM.md`](HYPOTHESIS_PROGRAM.md). The integrated manuscript is in `manuscript/main_text.md`.

This document originally framed an independent paper around directional recurrent mutation and genetic-warning reliability. That framing motivated Protocol 001 and the later common-grid work, but the completed evidence changed the logical structure of the project.

## Mechanism retained from the original design

For high-trait-associated allele frequency \(p\), the recurrent-transition operator is

\[
M_{\kappa_\mu,p_\mu^\ast}(p)
=\kappa_\mu p_\mu^\ast+(1-\kappa_\mu)p.
\]

At fixed \(\kappa_\mu\), changing \(p_\mu^\ast\) changes transition direction while retaining the same contraction strength. A local condition \(M(p)\ge p_c\) gives

\[
p\ge\frac{p_c-\kappa_\mu p_\mu^\ast}{1-\kappa_\mu}.
\]

This algebraic prediction remains the mechanism-level basis for H-MD-1.

## Final hypothesis decomposition after the completed campaigns

The original three questions were source persistence, trait-loss dynamics, and warning reliability. The completed project now resolves them as:

1. **H-MD-1 — source feasibility:** supported on the common 15-coordinate grid.
2. **H-MD-2 — functional-loss regime:** supported under the common deterioration family.
3. **H-MD-3a — matched-domain evaluability:** negative result; the strict Protocol 002 eligible set is empty at all 15 coordinates.
4. **H-MD-3b — direction-only warning effect conditional on matched evaluability:** unresolved because the matched common-grid prerequisite was absent.
5. **Protocol 003:** separately recalibrated portability comparison; it does not identify H-MD-3b because the two final domains differ in multiple ecological, transition, and schedule parameters.

H-MD-3a/3b are a post hoc logical decomposition used to state the completed evidence precisely; they are not retroactively preregistered labels.

## Why the original Paper 001 architecture is no longer active

The initial plan assumed that each recurrent-transition condition would yield a calibration-selected deterioration domain and that warning reliability could then be mapped across those domains. Protocol 002 falsified that operational assumption for the declared common candidate family: all 15 coordinates closed as `no_domain_selected`.

The scientifically informative outcome was therefore upstream of the planned warning map. Recurrent-transition dynamics changed source feasibility and functional-loss regime strongly enough that the matched warning contrast was not instantiated.

For this reason, the old stand-alone figure plan, manuscript architecture, and publication gate are retired. They remain in Git history rather than being treated as current requirements.

## Current navigation

- current hypothesis definitions/status: [`HYPOTHESIS_PROGRAM.md`](HYPOTHESIS_PROGRAM.md)
- protocol history: `PROTOCOL_001_ASYMMETRIC_MUTATION.md`, Protocol 002/003 documents, and `DECISION_LOG.md`
- permitted numerical claims: `../manuscript/claim_evidence_map.md`
- integrated manuscript: `../manuscript/main_text.md`

No historical simulation, artifact, calibration decision, or evidence ledger is changed by this documentation cleanup.