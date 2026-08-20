# Warning-blind frontier refinement Phase B — results

## Provenance

Prospectively declared in `docs/WARNING_BLIND_FRONTIER_REFINEMENT_PHASE_B.md` after Phase A closed and before Phase-B simulation.

- workflow run: `32350564282`;
- artifact: `9399807315`;
- digest: `sha256:132b5cf68f22baa28e4a91bc163544317b013650e77afdafe7c27f4b16cc645d`;
- workflow head: `a0d2d00f4f25f6070989b71f74d75f0d136cb8e6`;
- historical matched bracket: batch 619 (`p_star=0.25`, all five seed-block rates 1.0) to batch 673 (`p_star=0.50`, all five rates 0.0);
- new interior cells: 4;
- attempted trajectories: 100;
- calibration scope: trait-loss only.

No genetic-diversity, warning-time, lead/lag or warning-performance field was available to Phase B.

## Result 1 — no R4 event-regime cell was recovered

All four interior cells were classified as R3 seed-heterogeneous. None satisfied the strict R4 criterion requiring all five seed-block loss rates to lie in `[0.30,0.70]`.

- R4 warning-evaluable event regime: **0/4**;
- R3 seed-heterogeneous: **4/4**;
- R2 rapid-loss: 0/4 interior cells;
- R1 persistence: 0/4 interior cells.

The historical endpoints remain R2 at `p_star=0.25` and R1 at `p_star=0.50`.

## Result 2 — pooled loss changes smoothly while seed-block reproducibility does not

| p_star | pooled loss | seed-block loss rates | regime |
|---:|---:|---|---|
| 0.25 historical | 1.000 | 1, 1, 1, 1, 1 | R2 rapid |
| **0.30** | **0.739** | 1, 0.4, 0.75, 0.5, 1 | R3 heterogeneous |
| **0.35** | **0.476** | 0.5, 0, 0.6, 0.75, 0.5 | R3 heterogeneous |
| **0.40** | **0.304** | 0.4, 0, 0, 0.6, 0.5 | R3 heterogeneous |
| **0.45** | **0.095** | 0, 0, 0, 0, 0.5 | R3 heterogeneous |
| 0.50 historical | 0.000 | 0, 0, 0, 0, 0 | R1 persistence |

Across the matched bracket, pooled loss declines in the expected direction from 1 to 0. The important result is that **the intermediate pooled values are occupied by seed-heterogeneous cells rather than a reproducible all-seed intermediate-risk region**.

At `p_star=0.35`, pooled loss is close to one half (`0.476`) but the five seed-block rates span `0–0.75`. At `p_star=0.40`, pooled loss lies almost exactly at the lower R4 boundary (`0.304`) while two seed blocks show zero loss and others show `0.4–0.6`.

Thus a satisfactory pooled event probability does not imply a reproducible event regime across independent seed blocks.

## Result 3 — Phase A and Phase B recover the same qualitative boundary at different transition strengths

Phase A (`kappa_mu=0.05`) recovered no R4 cell in ten refined cells and was dominated by rapid/heterogeneous outcomes. Phase B (`kappa_mu=0.35`) starts from a clean historical rapid-to-persistence bracket and again places **R3 heterogeneity throughout the interior**.

This cross-row agreement strengthens, but does not yet prove, the interpretation that seed-block heterogeneity is a load-bearing part of the finite rapid-to-persistence frontier rather than merely a consequence of the original coarse 15-coordinate grid.

The current five-replicate-per-seed refinement is still too coarse to distinguish genuine seed-conditioned rate differences from binomial sampling noise with high confidence. A high-rep trait-loss-only reproducibility audit is therefore warranted before elevating R3 heterogeneity to a general model conclusion.

## Result 4 — the condition hierarchy is now sharper

The recovered finite structure is:

```text
R2 rapid loss
    ↓ increasing p_star
R3 seed-heterogeneous frontier
    ↓
R1 persistence
```

At the two tested recurrent-transition strengths, a contiguous R4 interval has not been recovered. This means the immediate scientific target is no longer warning ordering. It is **whether the R3 frontier remains heterogeneous when seed-block event rates are estimated more precisely**.

## Decision under the predeclared Phase-B rule

Because no interior Phase-B cell was R4:

- do not release warning/diversity endpoints;
- do not tune `A_ref`, interaction `kappa`, horizon or barrier strength to manufacture R4;
- retain the fixed ecological/deterioration anchor;
- if further work proceeds, it should be a high-rep warning-blind audit of the two central frontier cells (`p_star=0.35` and `0.40`) to test event-rate reproducibility, not a warning-performance analysis.

Only if that audit independently recovers an R4 cell/interval should a matched warning experiment be considered.
