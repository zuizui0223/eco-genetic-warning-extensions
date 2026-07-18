# Figure accessibility review

## Scope

This review covers the six reader-facing figures in the submission bundle. The first rendered bundle was inspected at a common 1,400-pixel review width, after which the source generators for Figures 2, 3, 5, and 6 were revised. The final inspection must be repeated on the regenerated merged-head bundle because the manifest changes whenever a figure changes.

## Global requirements

- Every figure must remain interpretable without colour alone.
- Every symbol, abbreviation, line type, fill, and threshold must be defined in the caption or figure.
- Text must remain legible at final single- or double-column size.
- Panel labels must follow one sequence and appear in the same position.
- Grayscale export must preserve category separation.
- Every repository-generated SVG must contain a machine-readable title, description, and image role.
- Publication-facing titles must use biological language rather than internal protocol-stage labels.

## Figure-by-figure status

| Figure | Primary encoding | Non-colour encoding | Repository status | Final merged-bundle action |
|---|---|---|---|---|
| Figure 1 | boxes, arrows, position | labels and causal ordering | SVG title, description, and image role present | confirm smallest explanatory text at journal width |
| Figure 2 | source-feasibility map | printed fraction and supported/planned count in every cell | biological title, larger cells and labels, SVG metadata added | regenerate and inspect numeric labels in grayscale |
| Figure 3 | loss-regime map | direct R/H/P code, regime name, pooled frequency, and candidate count | biological title, larger cells, SVG metadata, high-contrast text added | regenerate and confirm the heterogeneous-cell text remains legible |
| Figure 4 | stacked regime composition | in-bar R/H/P labels plus legend | SVG title, description, and image role present | confirm narrow segments do not obscure labels |
| Figure 5 | lead, tie, lag ordering | category name and count printed in every non-zero segment | biological title, larger text, outlines, SVG metadata added | regenerate and inspect the narrow tie and lag segments |
| Figure 6 | intervention time | direct S/D code and value on every paired bar | biological title, larger canvas, relocated legend, SVG metadata added | regenerate and confirm rightmost values do not approach the legend |

## Findings from the first rendered bundle

1. Figures 2, 5, and 6 retained internal `Stage I` or `Stage III` titles; these were removed from the publication generators.
2. Figures 2, 3, 5, and 6 lacked SVG `<title>`, `<desc>`, and `role="img"`; these were added at the source-generator level.
3. Figure 6 placed the legend close to the rightmost value labels; the canvas and legend position were revised.
4. Figure 3 contained dense small-cell text; the canvas, cells, and minimum cell-label size were increased.
5. Colour categories were already accompanied by some text, but the revised generators now make redundancy explicit: numeric values for Figure 2, R/H/P for Figure 3, direct category names for Figure 5, and S/D codes for Figure 6.

## Implemented repository-level safeguards

1. Figures 1–6 now have generator-level machine-readable titles and descriptions.
2. Every colour encoding has direct text redundancy.
3. Regression tests reject internal protocol-stage titles in publication figures.
4. Regression tests require accessible metadata for all six SVGs.
5. Captions define the six warning endpoints and state that endpoint summaries are correlated within trajectories.

## Final visual inspection protocol

For the frozen submission bundle:

1. render every SVG at the intended journal width;
2. export one colour PDF and one grayscale PDF;
3. confirm all labels at 100% view without zoom;
4. confirm that no category identification depends on hue alone;
5. confirm consistency between figure numbering, file names, captions, and main-text calls;
6. verify every file against `manifest.json`;
7. record the inspected artifact digest and manifest SHA-256 in the release notes.
