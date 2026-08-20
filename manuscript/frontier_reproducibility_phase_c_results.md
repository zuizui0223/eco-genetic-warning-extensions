# Warning-blind frontier reproducibility Phase C — results

## Provenance

Prospectively declared in `docs/WARNING_BLIND_FRONTIER_REPRODUCIBILITY_PHASE_C.md` after Phase B closed and before Phase-C simulation.

- workflow run: `32351311692`;
- artifact: `9400398146`;
- digest: `sha256:598334369bcc00e8a977500b20e7f0f561f964b79193cf2cbb870f21e636a1c8`;
- workflow head: `e228bee01165289674f044de0997fc6afaf30afb`;
- fixed Phase-B anchor: `A_ref=1.0`, interaction `kappa=4.5`, `kappa_mu=0.35`, horizon 120, barrier increase 0.30;
- fresh seeds: `20290210–20290214`;
- 20 replicates per seed;
- 100 attempts per cell, 200 total;
- calibration scope: trait-loss only.

No genetic-diversity, warning-time, lead/lag or warning-performance field was available to Phase C.

## Result 1 — one high-rep R4 cell exists

At `p_star=0.35`:

- baseline-eligible counts by seed: `19, 17, 19, 17, 19`;
- functional-loss rates by seed: **0.579, 0.529, 0.474, 0.588, 0.368**;
- pooled loss rate: **0.505**;
- seed-rate range: `0.220`;
- all five seed-block rates lie inside `[0.30,0.70]`;
- classification: **R4-highrep**.

Thus a reproducible intermediate-risk event regime **does exist** in the finite recurrent-transition frontier. The earlier 15/15 no-domain result therefore does not imply structural impossibility; the coarse/common candidate grid missed a narrower condition region.

This is an event-regime result only. It does not establish that a genetic warning succeeds.

## Result 2 — the adjacent `p_star=0.40` cell remains outside R4 at high replication

At `p_star=0.40`:

- baseline-eligible counts by seed: `20, 15, 18, 20, 19`;
- seed-block loss rates: **0.300, 0.400, 0.389, 0.200, 0.263**;
- pooled loss rate: **0.304**;
- seed-rate range: `0.200`;
- two seed blocks lie below the strict 0.30 lower bound;
- classification: **R3-highrep**.

The cell is therefore not warning-evaluable under the predeclared all-seed gate despite a pooled loss rate lying almost exactly at 0.30.

## Result 3 — Phase B heterogeneity was partly sampling-limited but the evaluable region is narrow

Phase B used only five replicates per seed. At `p_star=0.35` it classified the cell as R3 because one seed showed no loss and another 0.75. With 20 fresh replicates per seed, the same nominal cell becomes R4-highrep.

This shows that the apparent seed heterogeneity near the frontier can be exaggerated by small within-seed replication. It also validates the decision to treat Phase A/B heterogeneity as provisional until a high-rep audit was run.

However, the neighboring `p_star=0.40` cell remains R3-highrep under the same 20-replicate design. Therefore the refined result is not “heterogeneity disappears with replication.” It is:

> **a reproducible intermediate-risk event regime exists, but it occupies a narrower region than pooled-loss probability alone suggests.**

## Result 4 — evaluability is now a positive condition result, not only a negative no-domain result

The condition hierarchy can now be sharpened:

```text
rapid-loss regime
      ↓
reproducible intermediate-risk R4 near p_star≈0.35
      ↓
heterogeneous/lower-loss boundary by p_star=0.40
      ↓
persistence toward the historical p_star=0.50 endpoint
```

The exact width of R4 is not yet recovered. Phase C confirms one interior point and rejects the adjacent `0.40` point under the strict gate.

## Decision under the predeclared Phase-C rule

Exactly one of the two Phase-C cells is R4-highrep. Therefore:

- do **not** release warning/diversity endpoints;
- do not tune ecological/deterioration parameters;
- one additional trait-loss-only local refinement around `p_star=0.35` is allowed by the predeclared rule;
- that refinement should use the same fixed ecological/deterioration anchor and new fresh seeds, and should independently replay `0.35` alongside its immediate new neighbors so R4 width can be estimated on one common seed family.

Only after a contiguous independently confirmed R4 interval is recovered should a separate matched H-MD-3b warning-validation protocol be considered.
