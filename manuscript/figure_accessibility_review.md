# Figure accessibility review

## Scope

This review covers the six reader-facing figures in the submission bundle. It distinguishes fixes implemented in repository-generated figures from checks that must be repeated on imported immutable workflow artifacts before final submission.

## Global requirements

- Every figure must remain interpretable without colour alone.
- Every symbol, abbreviation, line type, fill, and threshold must be defined in the caption or figure.
- Text must remain legible at final single- or double-column size.
- Panel labels must follow one sequence and appear in the same position.
- Grayscale export must preserve category separation.
- SVG files should contain a machine-readable title and description when generated in this repository.

## Figure-by-figure status

| Figure | Primary encoding | Non-colour encoding | Text and symbol status | Remaining action |
|---|---|---|---|---|
| Figure 1 | boxes, arrows, position | labels and causal ordering | repository generator now includes SVG title and description | confirm minimum text size after journal scaling |
| Figure 2 | source-feasibility map | coordinate labels and numeric scale | caption defines support and denominator | inspect imported SVG for colour-only cells and add values or contours if needed |
| Figure 3 | loss-regime map | coordinate labels and regime names | caption defines rapid loss, persistence, and seed heterogeneity | inspect imported SVG in grayscale and verify legend contrast |
| Figure 4 | stacked regime composition | in-bar R/H/P labels plus legend | repository generator includes SVG title and description | confirm narrow segments do not obscure labels at final size |
| Figure 5 | lead, tie, lag ordering | category text and counts | caption states valid-pair denominators and trajectory dependence | verify that category shapes or direct labels accompany colour in imported SVG |
| Figure 6 | intervention time and censoring | endpoint labels, values, and censoring categories | caption defines median positive lead time and censoring | verify line or point types remain separable in grayscale |

## Implemented repository-level safeguards

1. Figures 1 and 4 contain SVG `<title>` and `<desc>` elements.
2. Figure 4 uses direct in-bar labels (`R`, `H`, `P`) in addition to colour.
3. Captions define the six warning endpoints and state that endpoint summaries are correlated within trajectories.
4. The submission checklist keeps imported-artifact grayscale and final-size inspection open until the final bundle is rendered.

## Final visual inspection protocol

For the frozen submission bundle:

1. render every SVG at the target journal width;
2. export one colour PDF and one grayscale PDF;
3. confirm all labels at 100% view without zoom;
4. confirm that no category identification depends on hue alone;
5. confirm consistency between figure numbering, file names, captions, and main-text calls;
6. record the inspected bundle manifest SHA-256 in the release notes.
