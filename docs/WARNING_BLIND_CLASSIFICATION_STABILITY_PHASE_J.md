# Warning-blind R4 classification-stability Phase J

## Why this audit comes before another mechanism

Phase E and Phase I independently evaluated the same nominal eco-genetic condition with legacy allele-frequency mixing `m=0.10` but obtained different categorical loss-regime labels: Phase E was `R3_highrep`; the fresh Phase-I comparator was `R4_highrep`.

Those locked finite results use different master-seed/source ensembles. Neither overwrites the other. Their disagreement creates a more immediate question than another parameter sweep:

> **Is the categorical R3/R4 gate itself stable across independent stochastic ensembles at one fixed biological condition?**

Phase J tests that question prospectively and warning-blind.

## Fixed biological condition

No biological parameter is varied:

- `kappa_mu=0.35`, `p_star=0.35`;
- `A_ref=1.0`, interaction `kappa=4.5`;
- allele-frequency mixing `m=0.10`;
- four equal patches at fixed total area;
- 30-generation ramp + 90-generation hold;
- normalized barrier increase `0.30`.

The earlier Phase-E and Phase-I labels motivate the audit but are not used to select any Phase-J outcome.

## Fresh ensemble design

Phase J uses exactly 20 new master seeds, `20290910–20290929`, with 20 attempted source replicates per master seed.

The seeds are prospectively partitioned into four non-overlapping five-seed panels in ascending order:

- Panel 1: `20290910–20290914`;
- Panel 2: `20290915–20290919`;
- Panel 3: `20290920–20290924`;
- Panel 4: `20290925–20290929`.

No regrouping is allowed after outcomes are generated.

## Classification

Each master seed yields one baseline-eligible trait-loss rate. Each five-seed panel is then classified with the unchanged Protocol-002 rule:

- R1: all five rates below `0.30`;
- R2: all five rates above `0.70`;
- R4: all five rates inside `[0.30,0.70]`;
- R3: any other sufficient mixture.

Each master seed must retain at least 10 baseline-eligible trajectories. If any block fails that requirement, the audit records `insufficient_support` rather than replacing the seed.

## Stability rule

- all four sufficient panels receive the same regime → `stable_<regime>`;
- sufficient panels disagree → `ensemble_sensitive`;
- any insufficient panel → `insufficient_support`.

The result is categorical stability of the current gate, not a fitted probability model.

## Blinding

Only source preparation/projection, baseline realised high-trait presence and realised trait-loss status/time are available. Genetic diversity, warning time and lead/lag outcomes remain unavailable.

## Stop rule

Run exactly these 20 master seeds and four fixed panels once. Do not:

- add seeds because the first four panels disagree;
- regroup the 20 seeds;
- change `m=0.10`;
- change the R4 band;
- inspect genetic-warning outcomes to redefine a stable panel.

## Interpretation ceiling

Phase J determines whether the current categorical gate is stable over four new finite panels at this one fixed condition. It does not invalidate earlier campaigns, estimate a universal R4 probability, or establish stability elsewhere in parameter space.

If the result is ensemble-sensitive, that instability is the result and the manuscript should distinguish a **continuous loss-rate distribution** from a hard warning-evaluability class more carefully. If all panels agree, the fixed-condition gate gains an independent replication certificate.
