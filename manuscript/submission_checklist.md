# Submission readiness checklist

## Evidence integrity

- [x] Source-reconstruction denominator fixed at 3,375 attempts.
- [x] Warning-blind calibration denominator fixed at 20,250 attempts.
- [x] Protocol 002 no-domain result retained without post hoc widening.
- [x] Protocol 003 calibration and validation use disjoint seed families.
- [x] Fresh-seed validation denominator fixed at 200 attempts.
- [x] Workflow identifiers and artifact digests recorded.
- [x] Censoring and baseline ineligibility retained.
- [x] Correlated endpoint counts are not treated as independent replicates.
- [x] Parent and extension trajectories are not pooled.

## Manuscript

- [x] Title foregrounds the conceptual advance: eco-genetic closure.
- [x] Abstract opens with functional-trait loss rather than mutation direction.
- [x] Abstract retains the principal denominators, regime result, ordering result, and intervention-time contrast.
- [x] Introduction follows function loss → warning → closure → test logic.
- [x] Biological Results headings contain no Stage labels.
- [x] Methods distinguish the preregistered no-domain protocol from the separately declared recovery protocol.
- [x] Discussion generalizes to monitoring, calibration, functional loss, and evolutionary rescue.
- [x] Finite Type S limitations and effective-transition interpretation are explicit.
- [x] Relationship to the predecessor is explicit and ledger boundaries are preserved.
- [x] In-text citation families have matching verified bibliography records and DOI identifiers.
- [ ] Final punctuation and author-display rules are rendered with the selected venue style.
- [ ] Author list, affiliations, acknowledgements, funding, author contributions, data statement, and conflicts are supplied.
- [ ] Final venue word, display-item, title-length, abstract-length, and data-policy limits are verified against current author guidance.

## Main versus supplement

- [x] Main text retains only the minimum predecessor mechanism and symmetric benchmark.
- [x] Main text reports coordinate ranges and representative regime cells rather than every candidate.
- [x] Full parameter grids, calibration diagnostics, trajectory-level endpoints, censoring tables, and provenance remain supplementary.
- [x] Main and supplementary table numbering is fixed as Tables 1–2 and Tables S1–S3.
- [x] Statistical-unit language is repeated in every endpoint table caption.
- [ ] Every final main-text and supplementary display call is checked after journal-template conversion.

## Figures and tables

- [x] Figure 1 is a closure-first conceptual diagram.
- [x] Source-feasibility, regime, ordering, and lead-time figures are generated reproducibly.
- [x] Machine-readable source, regime, and endpoint tables are included.
- [x] Figure captions are written in biological prose and define the interpretation boundaries.
- [x] Table captions define numbering, statistical units, censoring, and the no-domain interpretation.
- [ ] Accessibility review covers panel labels, font size, contrast, colour-blind interpretation, and grayscale legibility.
- [ ] Final figure count and main-versus-supplement allocation comply with the selected article type.

## Reproducibility and release

- [x] Pinned upstream commit recorded.
- [x] Immutable completion locks retained.
- [x] Submission bundle built in CI from locked artifacts.
- [x] Bundle builder includes the manuscript, bibliography, figure captions, and table captions.
- [ ] Clean bundle is rebuilt from the merged manuscript head.
- [ ] DOI/archive release is created after manuscript freeze.
- [ ] Repository landing pages point to the archived release and cite both evidence ledgers correctly.

## Editorial gate before submission

- [ ] A reader can state the central claim after the title, abstract, and Figure 1 alone.
- [ ] Mutation direction is consistently presented as one mechanism reshaping closure, not the sole conceptual novelty.
- [ ] `no_domain_selected` is consistently described as an event-regime result, not a failed simulation.
- [ ] No sentence implies a universal warning theorem, empirical mutation-rate estimate, or independent endpoint replication.
- [ ] Cover letter explains why the advance is ecological and conceptual rather than a model sensitivity analysis.
