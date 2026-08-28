# Submission readiness checklist

## Publication routing

- [x] Exactly two active manuscript paths are declared in `publication_lanes.json`.
- [x] Warning validity is owned only by `warning_validity.md`.
- [x] Joint-state and empirical-gate claims are owned only by `state_validity_and_empirical_measurement_gates.md`.
- [x] `main_text.md` is labelled as an integrated source archive, not a third submission.
- [x] The warning lane pairs 35/35 with 48/48 and 33/33 with 49/49.
- [x] The state lane does not claim validated predictive warning.
- [ ] Final venue, author metadata, word counts, figures, and supplements are approved separately for each lane.

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

- [x] Warning-lane title and abstract foreground the full-denominator validity result.
- [x] State-lane title and abstract foreground joint representation and empirical gates.
- [x] Warning-lane abstract retains all event and non-event denominators plus specificity and AUC.
- [x] State-lane abstract excludes a positive warning-validity claim.
- [ ] Both active abstracts and main texts are checked against the selected venue limits.
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
- [x] The historical integrated display allocation is retained for provenance.
- [ ] Independent active-lane display allocations are fixed after venue selection.
- [x] All tables are supplementary and numbered Tables S1–S5.
- [x] Statistical-unit language is repeated in every endpoint table caption.
- [ ] Every final main-text and supplementary display call is checked after journal-template conversion.

## Figures and tables

- [x] Figure 1 is a closure-first conceptual diagram.
- [x] Source-feasibility, regime, ordering, and lead-time figures are generated reproducibly.
- [x] Machine-readable source, regime, and endpoint tables are included.
- [x] Figure captions are written in biological prose and define the interpretation boundaries.
- [x] Table captions define numbering, statistical units, censoring, and the no-domain interpretation.
- [x] The archived integrated source respected its historical six-item Letter display ceiling.
- [ ] Each active lane receives a separately validated display ceiling.
- [x] Publication generators for Figures 2, 3, 5, and 6 use biological titles rather than internal Stage labels.
- [x] Figures 1–6 have generator-level SVG title, description, and image-role metadata.
- [x] Every colour encoding has direct text redundancy.
- [ ] Regenerated merged-head Figures 1–6 pass final-width colour and grayscale inspection.
- [ ] Graphical abstract asset and ≤500-character summary are prepared at major or minor revision.

## Reproducibility and release

- [x] Pinned upstream commit recorded.
- [x] Immutable completion locks retained.
- [x] Submission bundle builder includes both active manuscripts, the lane registry, and the integrated source archive.
- [x] Bundle builder includes the manuscript, bibliography, figure captions, and table captions.
- [ ] Clean two-lane bundle is rebuilt from the merged manuscript head.
- [ ] DOI/archive release is created after manuscript freeze.
- [ ] Repository landing pages point to the archived release and cite both evidence ledgers correctly.

## Editorial gate before submission

- [x] Cover-letter draft centres the ecological and conceptual advance rather than a model sensitivity analysis.
- [ ] A reader can state the central claim after the title, abstract, and Figure 1 alone.
- [ ] Mutation direction is consistently presented as one mechanism reshaping closure, not the sole conceptual novelty.
- [ ] `no_domain_selected` is consistently described as an event-regime result, not a failed simulation.
- [ ] No sentence implies a universal warning theorem, empirical mutation-rate estimate, or independent endpoint replication.
- [ ] Author-dependent cover-letter placeholders are replaced and approved.
