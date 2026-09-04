# State-validity submission display allocation

This is the display contract for the standalone state-validity manuscript only. It replaces the archived integrated six-display plan for this lane; it does not modify historical integrated figures or the warning-validity display plan.

## Main displays — exactly two figures

### Figure 1 — matching marginals can hide different next transitions

**Question:** Can two present states that match the standard ecological/genetic marginals still have different immediate dynamics?

**Panel A — state construction.** Four patches (or the declared patchwise state ordering used by the locked Phase-V certificate) show the same interaction-value multiset and the same genetic/trait-support bundle multiset under aligned and anti-aligned assignment. Label cross-layer covariance `+0.025` versus `-0.025`. Explicitly state that census, interaction marginals, allele-frequency marginals, realised trait marginals, `H_alpha`, `H_gamma`, and `F_ST` are identical.

**Panel B — exact next interaction transition.** Plot the four patchwise generation-1 interaction values for aligned and anti-aligned states, with the maximum absolute patchwise difference labelled **0.2543**.

**Claim ceiling:** this is a transition-level representation certificate under the declared model. It is not a long-horizon risk estimate and not a claim that alignment has the same effect in nature.

**Source:** `artifacts/cross_layer_alignment/phase_v_locked_summary.json`.

### Figure 2 — the hidden state difference propagates on a forecast horizon

**Question:** When does the aligned/anti-aligned state difference become visible in realised functional-loss risk under the fixed deterioration path?

**Panel A — primary horizon curve.** Anti-aligned minus aligned loss-risk difference at the fixed 1,500-pair readouts:

- generation 5: `0.0` percentage points;
- generation 10: `+0.33` pp, paired 95% CI `[-0.44, +1.11]`;
- generation 20: `+5.33` pp, `[+2.04, +8.62]`;
- generation 40: `+5.20` pp, `[+1.96, +8.44]`.

The plot must show effect size and uncertainty, not significance stars or a visually declared cutoff.

**Panel B — precision versus effect magnitude.** For generations 20 and 40, show the nested paired estimates at 500, 1,000, and 1,500 pairs. The visual purpose is to show that interval width contracts while the effect-size estimates remain in the same approximate range. Nested prefixes must be labelled as precision diagnostics, not independent replication.

**Claim ceiling:** under this closure and forcing path, little risk contrast is present at the 5–10 generation readouts and a roughly five-point contrast is present by the 20-generation readout and remains similar at 40. Generation 20 is not a universal or exact biological cutoff.

**Source:** `artifacts/alignment_propagation/locked_summary.json` and `experiments/alignment_propagation_protocol.json`.

## Supplementary displays

### Table S1 — operator-specific portability boundary

Report the historical allele-frequency-mixing result, fresh Phase-U non-replication, whole-individual dispersal closure, pollen-only closure, and matched-partner negative result with exact operator names and their own finite estimands. Do not place different scalar rates on a common biological x-axis.

### Figure S1 — original frozen Phase-V long-horizon result

Show the original generation-60 500-pair aligned/anti-aligned loss contrast separately from the post-Phase-V propagation experiment. Required reporting: aligned `339/500`, anti-aligned `361/500`, anti-minus-aligned risk difference `+4.4` pp, pointwise paired 95% CI approximately `[-1.2,+10.0]`.

### Table S2 — complete propagation grid

All 12 predeclared horizon-by-pair-count cells from the locked propagation result. This preserves the full nested precision audit and makes clear that no horizon was selected post hoc.

## Explicit exclusions from this lane

Do not include as main or supplementary displays merely because they remain in the repository:

- 35/35, 33/33, 48/48, or 49/49 warning-validity counts;
- warning ROC/AUC panels;
- natural-data four-gate systems;
- cross-origin natural-data STOPs;
- historical R1–R4 calibration-screen figures;
- fragmentation-gradient figures owned by the standalone EGC manuscript unless cited only as parent provenance.

## Letter logic

```text
Figure 1: the representation problem exists
        ->
Figure 2: the hidden distinction propagates to a horizon-dependent endpoint effect
        ->
Supplement: operator portability shows why scalar process labels cannot be assumed equivalent
```

This two-figure structure is the default state-validity submission plan unless a venue-specific display limit requires a later author-approved change.
