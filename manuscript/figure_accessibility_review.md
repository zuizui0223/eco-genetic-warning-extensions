# Figure accessibility review

## Scope

This review covers the six reader-facing figures in the submission bundle after the identification and censoring revision. Figures 3–6 were redesigned so the main visual encodings match the revised claims.

## Global requirements

- Every figure must remain interpretable without colour alone.
- Every symbol, abbreviation, line type, fill, and threshold must be defined in the caption or figure.
- Text must remain legible at final single- or double-column size.
- Every repository-generated SVG must contain a machine-readable title, description, and image role.
- Publication-facing labels must use biological language rather than internal Stage/Protocol identifiers.
- Valid-pair displays must not hide source failure, baseline ineligibility, or censoring by normalising every bar to the valid-pair denominator.

## Figure-by-figure design

| Figure | Primary encoding | Non-colour redundancy | Revision purpose |
|---|---|---|---|
| Figure 1 | boxes, arrows, causal position | direct labels and ordering | compact conceptual architecture; no overlapping arrows |
| Figure 2 | source-feasibility cells | printed fraction and supported/planned count | common-grid transition-direction evidence |
| Figure 3 | regime cells + candidate-count bars | R/H/P codes, pooled frequency, counts | merges former Figures 3 and 4 and frees one display slot |
| Figure 4 | four cumulative-incidence panels | line style, direct axis labels, thresholds | retains administrative censoring and shows event availability over each calibrated horizon |
| Figure 5 | full 100-attempt horizontal bars | SF/BI/BC/WC/TC/Lead/Tie/Lag codes and counts | makes availability and censoring visible rather than plotting only valid pairs |
| Figure 6 | points + 95% interval whiskers | domain-specific shapes, `n` labels, explicit axes | shows absolute and horizon-normalized timing and avoids legend/data overlap |

## Identification safeguards visible in figures

1. Stage III domains are labelled **Recalibrated symmetric domain** and **Directional calibrated domain**; raw code labels `symmetric_bridge` and `transition` are not reader-facing names.
2. Figure 4 labels the calibrated horizons (240 and 120 generations).
3. Figure 5 retains the attempted denominator of 100 for every endpoint.
4. Figure 6 has separate panels for generations and fraction of calibrated horizon.
5. Figure 6 states that its intervals come from trajectory resampling and that the absolute timing comparison is not a single-factor transition-direction effect.

## Final visual inspection protocol

For the frozen submission bundle:

1. render every SVG at the intended journal width;
2. export one colour PDF and one grayscale PDF;
3. confirm all labels at 100% view without zoom;
4. confirm that no category identification depends on hue alone;
5. inspect Figure 3 heterogeneous-cell text, Figure 5 narrow tie/lag segments, and Figure 6 interval/n labels for overlap;
6. confirm consistency between figure numbering, file names, captions, and main-text calls;
7. verify every file against `manifest.json`;
8. record the inspected artifact digest and manifest SHA-256 in the release notes.
