# Documentation map

This directory contains both **current scientific sources** and **historical protocol/development records**. Historical files are retained for provenance but must not be read as competing current hypotheses.

## Current scientific sources

Read these first:

1. [`HYPOTHESIS_PROGRAM.md`](HYPOTHESIS_PROGRAM.md) — current H-MD-1 / H-MD-2 / H-MD-3a / H-MD-3b definitions, finite recovery status, and the exact no-universal-sign heterozygosity boundary.
2. [`DECISION_LOG.md`](DECISION_LOG.md) — chronology of protocol declarations and the final interpretation boundary.
3. `PROTOCOL_002_*` scientific protocol/audit documents — common-grid source reconstruction, common deterioration family, and strict no-domain selection.
4. [`PROTOCOL_003_AMENDMENT_001.md`](PROTOCOL_003_AMENDMENT_001.md) and [`PROTOCOL_003_AMENDMENT_002.md`](PROTOCOL_003_AMENDMENT_002.md) — separately declared evaluability recovery.
5. [`PROTOCOL_003_SECONDARY_WARNING_AUDIT.md`](PROTOCOL_003_SECONDARY_WARNING_AUDIT.md) — locked-record timing/censoring audit.
6. [`../manuscript/claim_evidence_map.md`](../manuscript/claim_evidence_map.md) — final permitted/prohibited manuscript claims.

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
          + Type T boundary recovered: direction alone has no universal signed effect on H(p)=2p(1-p)
Protocol 003  separate portability result across non-matched recalibrated domains
```

The Type T boundary is implemented in `src/eco_genetic_warning_extensions/mutation_coordinates.py` and tested in `tests/test_mutation_coordinates.py`. It explains why a universal direction→genetic-warning sign cannot be inferred from the transition operator alone, but it does not determine full dynamic warning first-passage ordering.

When a historical file and the current hypothesis program differ in framing, **`HYPOTHESIS_PROGRAM.md` and `manuscript/claim_evidence_map.md` take precedence for current interpretation**, while the historical file remains authoritative only for what was declared at that earlier protocol stage.