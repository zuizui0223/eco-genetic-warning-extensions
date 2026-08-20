# Documentation map

This directory contains both **current scientific sources** and **historical protocol/development records**. Historical files are retained for provenance but must not be read as competing current hypotheses.

## Current scientific sources

Read these first:

1. [`HYPOTHESIS_PROGRAM.md`](HYPOTHESIS_PROGRAM.md) — current H-MD-1 / H-MD-2 / H-MD-3a / H-MD-3b definitions and recovery status.
2. [`RECURRENT_TRANSITION_DIVERSITY_THEORY.md`](RECURRENT_TRANSITION_DIVERSITY_THEORY.md) — exact Type T one-step diversity identities: non-universal direction→heterozygosity sign, direction-independent contraction of the `H_gamma-H_alpha` gap, and equal fixed-weight `p_star` derivatives of `H_alpha` and `H_gamma`.
3. [`DECISION_LOG.md`](DECISION_LOG.md) — chronology of protocol declarations and the final interpretation boundary.
4. `PROTOCOL_002_*` scientific protocol/audit documents — common-grid source reconstruction, common deterioration family, and strict no-domain selection.
5. [`PROTOCOL_003_AMENDMENT_001.md`](PROTOCOL_003_AMENDMENT_001.md) and [`PROTOCOL_003_AMENDMENT_002.md`](PROTOCOL_003_AMENDMENT_002.md) — separately declared evaluability recovery.
6. [`PROTOCOL_003_SECONDARY_WARNING_AUDIT.md`](PROTOCOL_003_SECONDARY_WARNING_AUDIT.md) — locked-record timing/censoring audit.
7. [`../manuscript/claim_evidence_map.md`](../manuscript/claim_evidence_map.md) — final permitted/prohibited manuscript claims.

## Historical design/provenance records

These explain how the project arrived at the current design but are **not current claim sources**:

- [`PROTOCOL_001_ASYMMETRIC_MUTATION.md`](PROTOCOL_001_ASYMMETRIC_MUTATION.md)
- [`MATHEMATICAL_DESIGN_PROTOCOL_001.md`](MATHEMATICAL_DESIGN_PROTOCOL_001.md)
- [`LITERATURE_SCREEN_PROTOCOL_001.md`](LITERATURE_SCREEN_PROTOCOL_001.md)
- [`NOVELTY_REVIEW_PROTOCOL.md`](NOVELTY_REVIEW_PROTOCOL.md)
- [`PAPER_001_MUTATION_DIRECTION_PHASE_DIAGRAM.md`](PAPER_001_MUTATION_DIRECTION_PHASE_DIAGRAM.md) — historical paper-planning note; explicitly superseded by `HYPOTHESIS_PROGRAM.md`.

The older H2-R-AS framing belongs here. It motivated the project but is not the completed project's headline hypothesis structure.

## Inherited-parent audit records

- [`INHERITED_H3_EFFECT_SIZE_AUDIT.md`](INHERITED_H3_EFFECT_SIZE_AUDIT.md) documents manuscript-facing summaries derived from the locked parent evidence. It does not make those parent results extension hypotheses.

## Implementation notes

Files describing smoke adapters, minimal fixtures, runner wiring, or batch mechanics document reproducibility and development constraints. They support execution but do not define scientific conclusions.

## Current recovery status

```text
H-MD-1   supported, finite Type S
H-MD-2   supported, finite Type S
H-MD-3a  negative / recovered: no eligible common-family validation domain at 15/15 coordinates
H-MD-3b  matched finite effect unresolved
          + Type T boundaries recovered for the recurrent-transition diversity step
Protocol 003  separate portability result across non-matched recalibrated domains
```

The Type T theory is implemented in `src/eco_genetic_warning_extensions/mutation_coordinates.py` and tested in `tests/test_mutation_coordinates.py`. It constrains what a direction-only warning hypothesis may claim, but it does not determine full dynamic warning first-passage ordering.

When a historical file and the current hypothesis program differ in framing, **`HYPOTHESIS_PROGRAM.md`, `RECURRENT_TRANSITION_DIVERSITY_THEORY.md`, and `manuscript/claim_evidence_map.md` take precedence for current interpretation**, while the historical file remains authoritative only for what was declared at that earlier protocol stage.