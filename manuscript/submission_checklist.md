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
- [x] Abstract is at or below the Ecology Letters Letter limit of 150 words.
- [x] Abstract retains the principal denominators, regime result, ordering result, and intervention-time contrast.
- [x] Introduction follows function loss → warning → closure → test logic.
- [x] Biological Results headings contain no Stage labels.
- [x] Methods distinguish the preregistered no-domain protocol from the separately declared recovery protocol.
- [x] Discussion generalizes to monitoring, calibration, functional loss, and evolutionary rescue.
- [x] Finite Type S limitations and effective-transition interpretation are explicit.
- [x] Relationship to the predecessor is explicit and ledger boundaries are preserved.
- [x] In-text citation families have matching verified bibliography records and DOI identifiers.
- [x] Article type is fixed as Letter.
- [x] Running title and ten keywords are prepared.
- [ ] Final punctuation and author-display rules are rendered with the selected venue style.
- [ ] Author list, affiliations, acknowledgements, funding, author contributions, data statement, and conflicts are supplied.
- [ ] Final Word or LaTeX file confirms the automated main-text word count.

## Main versus supplement

- [x] Main text retains only the minimum predecessor mechanism and symmetric benchmark.
- [x] Main text reports coordinate ranges and representative regime cells rather than every candidate.
- [x] Full parameter grids, calibration diagnostics, trajectory-level endpoints, censoring tables, and provenance remain supplementary.
- [x] Main display allocation is fixed at Figures 1–6, with no main tables or text boxes.
- [x] All tables are supplementary and numbered Tables S1–S5.
- [x] Statistical-unit language is repeated in every endpoint table caption.
- [ ] Every final main-text and supplementary display call is checked after journal-template conversion.

## Figures and tables

- [x] Figure 1 is a closure-first conceptual diagram.
- [x] Source-feasibility, regime, ordering, and lead-time figures are generated reproducibly.
- [x] Machine-readable source, regime, and endpoint tables are included.
- [x] Figure captions are written in biological prose and define the interpretation boundaries.
- [x] Table captions define numbering, statistical units, censoring, and the no-domain interpretation.
- [x] Six-item Letter display ceiling is respected.
- [ ] Imported Figures 2, 3, 5, and 6 pass final-width colour, grayscale, label, and font-size inspection.
- [ ] Graphical abstract asset and ≤500-character summary are prepared at major or minor revision.

## Reproducibility and release

- [x] Pinned upstream commit recorded.
- [x] Immutable completion locks retained.
- [x] Submission bundle built in CI from locked artifacts.
- [x] Bundle builder includes the manuscript, bibliography, figure captions, and table captions.
- [ ] Clean bundle is rebuilt from the merged manuscript head.
- [ ] DOI/archive release is created after manuscript freeze.
- [ ] Repository landing pages point to the archived release and cite both evidence ledgers correctly.

## Editorial gate before submission

- [x] Cover-letter draft centres the ecological and conceptual advance rather than a model sensitivity analysis.
- [ ] A reader can state the central claim after the title, abstract, and Figure 1 alone.
- [ ] Mutation direction is consistently presented as one mechanism reshaping closure, not the sole conceptual novelty.
- [ ] `no_domain_selected` is consistently described as an event-regime result, not a failed simulation.
- [ ] No sentence implies a universal warning theorem, empirical mutation-rate estimate, or independent endpoint replication.
- [ ] Author-dependent cover-letter placeholders are replaced and approved.
