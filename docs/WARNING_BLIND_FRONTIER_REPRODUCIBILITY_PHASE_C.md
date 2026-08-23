# Warning-blind frontier reproducibility audit — Phase C

## Status

Prospectively declared after Phase B closed with 0/4 R4 cells and before Phase-C simulation.

Phase C does **not** search a wider parameter space and does not inspect genetic warning. It asks whether the central R3 frontier cells remain non-reproducible when seed-block event rates are estimated with higher replication.

## Fixed ecological and recurrent-transition setting

Retain the Phase-B matched anchor unchanged:

- `A_ref=1.0`;
- interaction-feedback `kappa=4.5`;
- `kappa_mu=0.35`;
- ramp 30, hold 90, horizon 120;
- normalized barrier increase `0.30`;
- equal-isolated projection.

Retain only the two central Phase-B frontier values:

- `p_star=0.35` — Phase-B pooled loss `0.476`, seed rates `0.50, 0.00, 0.60, 0.75, 0.50`;
- `p_star=0.40` — Phase-B pooled loss `0.304`, seed rates `0.40, 0.00, 0.00, 0.60, 0.50`.

These cells are selected using trait-loss outcomes only because they are the central interior cells whose pooled rates lie within or at the strict intermediate-risk band while seed-block rates remain heterogeneous.

## Fresh seed family and replication

Use a new seed family not previously present in the repository:

`20290210, 20290211, 20290212, 20290213, 20290214`

For each `p_star`:

- 20 replicates per seed;
- 5 seeds;
- 100 attempted trajectories per cell;
- 200 planned attempts total.

Every `p_star` receives an independently reconstructed source under its own recurrent-transition coordinate.

## Permitted quantities

Only source/event-regime quantities are permitted:

- source preparation and projection support;
- baseline realised high-trait presence;
- realised functional-loss occurrence/time;
- baseline-eligible denominator per seed;
- seed-block trait-loss rate;
- pooled trait-loss rate;
- event-regime classification and seed-rate range.

Forbidden throughout Phase C:

- `H_alpha`, `H_gamma`, heterozygosity or any diversity output;
- warning endpoints/times;
- lead, lag, tie, or lead-time outcomes;
- selection based on any genetic-warning field.

## Reproducibility classification

A cell is evaluated only if every seed has at least 10 baseline-eligible trajectories. Otherwise it is classified as insufficient for the high-rep reproducibility audit.

For sufficiently supported cells:

- `R4-highrep`: all five seed-block loss rates lie in `[0.30,0.70]`;
- `R2-highrep`: all five rates are `>0.70`;
- `R1-highrep`: all five rates are `<0.30`;
- `R3-highrep`: any remaining cross-seed pattern.

The seed-rate range `max(rate)-min(rate)` is retained as a descriptive measure of cross-seed instability.

## Decision rule

1. If **both adjacent cells** (`0.35` and `0.40`) are R4-highrep, freeze the interval `[0.35,0.40]` as a confirmed matched event-regime domain. A separate future protocol with fresh warning-validation seeds may then test H-MD-3b; Phase C itself still does not release warning fields.
2. If exactly one cell is R4-highrep, do not tune ecological/deterioration parameters. The result is a narrow event-regime boundary; further local refinement requires a separately declared trait-loss-only protocol.
3. If neither cell is R4-highrep and R3 persists, treat seed-conditioned event-regime heterogeneity as a confirmed finite property of this recurrent-transition frontier.

## Evidence boundary

Phase C is a precision/reproducibility audit of an already selected trait-loss frontier, not an attempt to optimize warning performance. No warning result is permitted to influence its design, execution, classification, or stopping rule.
