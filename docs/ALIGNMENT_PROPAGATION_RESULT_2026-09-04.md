# Alignment propagation result — 2026-09-04

## Status

Completed post-Phase-V propagation experiment under the prospectively locked protocol `experiments/alignment_propagation_protocol.json`.

This experiment does **not** alter or rerun the original preregistered Phase-V 60-generation / 500-pair result. It extends the question along two dimensions declared before outcomes were opened: fixed readout horizons and paired replication.

## Provenance

- source workflow run: `33839184864`
- source head: `27f73ce621fc687369e529d736a381c03ce4986a`
- workflow artifact: `9924340712`
- artifact name: `alignment-propagation-post-phase-v-v1`
- artifact digest: `sha256:92332ec3fb0ac04d7bfcab6b7ab56dbb2aac65d7021ae6aa71523bcfdca4fb52`
- compact locked result: `artifacts/alignment_propagation/locked_summary.json`

## Primary 1,500-pair effect-size trajectory

The primary estimand is anti-aligned minus aligned realised functional-loss risk.

| horizon | aligned loss | anti-aligned loss | risk difference | paired 95% CI | McNemar p |
|---:|---:|---:|---:|---:|---:|
| 5 | 0/1500 | 0/1500 | 0.0 pp | 0.0 to 0.0 pp | 1.000 |
| 10 | 15/1500 | 20/1500 | +0.33 pp | -0.44 to +1.11 pp | .500 |
| 20 | 504/1500 | 584/1500 | +5.33 pp | +2.04 to +8.62 pp | .00174 |
| 40 | 979/1500 | 1057/1500 | +5.20 pp | +1.96 to +8.44 pp | .00193 |

Under the fixed deterioration path, the contrast is essentially absent at the 5- and 10-generation readouts, is about +5 percentage points by generation 20, and remains of similar magnitude at generation 40. The experiment therefore supports a **horizon-dependent propagation pattern** under the declared closure.

It does **not** identify generation 20 as a universal or exact biological cutoff. The four horizons were predeclared readout points; the allowed inference is that the effect-size trajectory changed between the 10- and 20-generation readouts and persisted through the 40-generation readout under this forcing path.

## Replication audit

The nested prefixes show why the original 500-pair non-detection should not be read as evidence of negligible effect.

At generation 20:

- 500 pairs: +5.4 pp, 95% CI -0.46 to +11.26 pp;
- 1,000 pairs: +5.9 pp, 95% CI +1.83 to +9.97 pp;
- 1,500 pairs: +5.33 pp, 95% CI +2.04 to +8.62 pp.

At generation 40:

- 500 pairs: +4.4 pp, 95% CI -1.29 to +10.09 pp;
- 1,000 pairs: +6.4 pp, 95% CI +2.44 to +10.36 pp;
- 1,500 pairs: +5.2 pp, 95% CI +1.96 to +8.44 pp.

The effect-size estimates are similar across the nested prefixes while intervals contract with additional paired replication. The result therefore separates **precision** from **effect magnitude** rather than converting a p-value crossing into the scientific conclusion.

## Claim ceiling

Allowed:

> Under the declared aligned/anti-aligned state contrast and fixed deterioration path, little loss contrast was present by generations 5–10, whereas an anti-aligned excess loss risk of about five percentage points was present by generation 20 and remained similar at generation 40. Increasing paired replication from 500 to 1,500 narrowed the intervals around that effect-size trajectory.

Not allowed:

- generation 20 is the true or universal onset time;
- significance at one horizon defines a biological threshold;
- the post-Phase-V experiment was part of the original Phase-V preregistration;
- the result establishes the same propagation timescale in natural systems;
- nested 500/1000/1500 prefixes are independent experiments.
