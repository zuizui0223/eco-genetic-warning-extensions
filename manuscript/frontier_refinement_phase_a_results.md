# Warning-blind frontier refinement Phase A — results

## Provenance

Prospectively declared in `docs/WARNING_BLIND_FRONTIER_REFINEMENT_PROTOCOL.md` after the locked Protocol 002 condition-map analysis and before these outcomes were generated.

- workflow run: `32348846844`;
- artifact: `9399411509`;
- digest: `sha256:c1da8f6fc1d381924c6660b6844c18464e3c2e63035a2ca6416babd940f4da14`;
- workflow head: `8cdde2eb16d63c2afb42a73b2d8d2c80cdeac317`;
- new cells: 10;
- attempted trajectories: 250;
- recurrent-transition strength: `kappa_mu=0.05`;
- refined `p_star`: `0.775, 0.800, 0.825, 0.850, 0.875`;
- two predeclared non-transition anchors;
- calibration scope: trait-loss only.

No genetic-diversity, warning-time, lead/lag or warning-performance field was available to the Phase-A calibration artifact.

## Result 1 — no R4 event-regime domain was recovered

None of the ten refined cells satisfied the strict R4 definition requiring all five seed-block post-baseline functional-loss rates to lie in `[0.30,0.70]`.

Across the ten cells:

- R4 warning-evaluable: **0**;
- R3 seed-heterogeneous: **6**;
- R2 rapid-loss: **4**;
- R1 persistence: **0**.

Therefore Phase A does not recover a matched warning-validation interval and **does not release warning endpoints for evaluation**.

## Result 2 — the apparent intermediate pooled rate at the frontier is seed-heterogeneous

The most striking refined cell was anchor A2 at `p_star=0.875`:

- pooled functional-loss rate: **0.50**;
- seed-block rates: **0.00, 0.50, 0.333, 0.60, 0.75**;
- baseline-eligible trajectories: 18/25;
- observed functional losses: 9/18.

A pooled rate of 0.50 would look ideal if seeds were collapsed. The strict seed-block criterion instead reveals a wide 0.00–0.75 range. Thus the obstacle is not merely failure to tune the pooled event probability: **between-seed reproducibility itself breaks at the candidate frontier**.

This strengthens the interpretation of H-MD-3a. The no-domain result is not adequately described as “the mean loss probability missed 0.5.” In at least this refined frontier, the same nominal cell can produce qualitatively different event rates among independent seed blocks.

## Result 3 — the fine frontier is not a smooth monotone dose response at five-replicate resolution

### Anchor A1

| p_star | pooled loss | seed rates | regime |
|---:|---:|---|---|
| 0.775 | 0.889 | 1, 1, 1, 0.333, 1 | R3 heterogeneous |
| 0.800 | 0.889 | 1, 1, 1, 1, 0.5 | R3 heterogeneous |
| 0.825 | 1.000 | 1, 1, 1, 1, 1 | R2 rapid |
| 0.850 | 0.857 | 0.75, 1, 1, 1, 0.6 | R3 heterogeneous |
| 0.875 | 0.800 | 1, 1, 0.8, 0.75, 0.6 | R3 heterogeneous |

### Anchor A2

| p_star | pooled loss | seed rates | regime |
|---:|---:|---|---|
| 0.775 | 1.000 | 1, 1, 1, 1, 1 | R2 rapid |
| 0.800 | 0.938 | 0.5, 1, 1, 1, 1 | R3 heterogeneous |
| 0.825 | 0.947 | 1, 1, 1, 0.75, 1 | R2 rapid |
| 0.850 | 1.000 | 1, 1, 1, 1, 1 | R2 rapid |
| 0.875 | 0.500 | 0, 0.5, 0.333, 0.6, 0.75 | R3 heterogeneous |

The earlier coarse-grid condition map established a broad finite tendency for higher `p_star` to reduce loss among matched complete candidates. Phase A shows that, near the boundary and at five refinement replicates per seed, the realized cell-level response is not a smooth deterministic dose response. Stochastic seed structure remains load-bearing.

This does not contradict the exact local support-frontier theorem, which predicts only the direction in which local allele support shifts under a constrained pre-state. It does not predict the full stochastic loss probability.

## Result 4 — source/baseline availability remains part of the boundary

Source-prepared / projection-supported counts ranged from 16 to 21 of 25 attempts among the ten cells, and baseline eligibility likewise varied. Thus the frontier cannot be interpreted only through loss probability conditional on an already available trajectory.

The condition hierarchy remains:

```text
source/high-state availability
        ↓
baseline functional state
        ↓
functional-loss regime
        ↓
seed-block reproducibility
        ↓
only then warning evaluability
```

## Decision under the predeclared stop rule

Phase A produced no R4 cell, so there is no basis for confirmation or warning validation in the `kappa_mu=0.05`, `p_star=0.775–0.875` interior grid.

The useful recovered result is a **seed-heterogeneous rapid-loss frontier**, not a hidden successful warning domain.

Phase B is scientifically justified only if the purpose remains mapping condition geometry across transition strength. It should not be run merely to find a cell that makes warning work.

If Phase B proceeds, the strongest target is the `kappa_mu=0.35`, `p_star=0.25–0.50` coarse transition, because the historical grid changes from rapid loss to persistence across that interval and therefore provides the sharpest test of whether a reproducible R4 window exists at stronger recurrent-transition relaxation. A second target is `kappa_mu=0.20` around the historical heterogeneous `p_star=0.50` cell.

Exact Phase-B interior points and non-transition anchors must be declared using trait-loss/source evidence only before execution.
