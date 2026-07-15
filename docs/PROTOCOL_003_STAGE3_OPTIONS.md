# Protocol 003 options for a future warning-validation study

## Current boundary

Protocol 002 selected no calibration domain at any of the 15 mutation coordinates. Its preregistered rule explicitly forbids expanding the candidate family after observing `no_domain_selected`. Therefore no Protocol 002 Stage III warning-validation campaign exists, and none should be retroactively created.

The completed companion paper can close on source feasibility, trait-loss regimes, seed heterogeneity, and warning-validation feasibility. A future warning paper requires Protocol 003 with a new question, new selection rule, and fresh seeds.

## Recommended scientific question

Protocol 003 should not ask whether the Protocol 002 warning result can be made positive. It should ask:

> Under a deliberately broader deterioration design, which mutation-direction regimes admit estimable trait-loss event rates, and conditional on that independently selected domain, what are the availability and timing of relative-diversity warnings?

The calibration stage must remain blind to all warning and diversity outcomes.

## Option A — replicate-stabilised calibration

Keep the existing source grid, horizons, and barrier increases, but increase calibration replication so that seed-block rates are not dominated by denominators of three to five eligible trajectories.

- calibration seeds: a fresh, preregistered set
- target: at least 20 baseline-eligible trajectories per seed block
- eligibility: each seed-block confidence interval intersects a declared target interval
- selection: deterministic distance from target event probability, then shorter horizon and weaker deterioration

Strength: directly addresses the observed seed-block discreteness and heterogeneity.

Risk: extreme rapid-loss and persistence coordinates may remain outside the estimable regime.

## Option B — coordinate-specific bracket search

Use trait-loss-only pilot brackets to locate, separately for each mutation coordinate, deterioration schedules producing neither near-zero nor near-one event probability.

- bracket variable: normalized barrier increase, horizon, or both
- bracket algorithm and stopping rule fixed before simulation
- calibration seeds distinct from bracket and validation seeds
- warning outputs prohibited until the bracket and final domain are locked

Strength: makes warning validation possible across a broader phase map.

Risk: it changes the paper question from one common deterioration family to coordinate-specific stress matching. Cross-coordinate warning comparisons must then be interpreted at matched event risk, not matched environmental forcing.

## Option C — sentinel-coordinate validation

Choose a small set of mutation coordinates from mechanistic categories fixed without warning inspection:

- rapid-loss sentinel
- transition/seed-heterogeneous sentinel
- persistence sentinel
- symmetric bridge control

Run a new calibration and fresh validation only for those sentinels.

Strength: computationally efficient and mechanistically readable.

Risk: no longer supports a complete warning phase diagram.

## Recommended route

For a separate future warning paper, use **Option B with a small preregistered sentinel panel**, combining the interpretability of Option C with coordinate-specific event-rate matching.

Suggested sentinel coordinates, justified only by completed trait-loss regimes and not by warning outcomes:

- `(kappa_mu=0.20, p_star=0.25)` — rapid-loss regime
- `(kappa_mu=0.20, p_star=0.50)` — seed-heterogeneous symmetric bridge
- `(kappa_mu=0.05, p_star=0.90)` — closest-to-band transition case
- `(kappa_mu=0.20, p_star=0.90)` — persistence regime

These are planning candidates, not selected domains. Final inclusion, bracket grid, sample size, and seeds must be locked in Protocol 003 before any new simulation.

## Required separation of seeds

Protocol 003 must use three non-overlapping seed families:

1. bracket-search seeds;
2. final trait-loss-only calibration seeds;
3. warning-validation seeds.

No trajectory may move between stages, and no warning output may be available during bracket search or calibration.

## Validation outputs

After a domain is independently selected, fresh validation may calculate:

- trait-loss probability and first-passage time;
- warning availability for relative `H_alpha` and `H_gamma` decline thresholds;
- valid event-pair denominator;
- lead, tie, and lag proportions;
- usable lead-time distribution;
- right-censoring composition;
- seed-block heterogeneity.

Absolute diversity thresholds may only be a deterministic secondary audit on the same stored validation trajectories.

## Decision point

Protocol 003 is optional and should not delay submission of the current mutation-direction regime paper. It should be opened only as a separately titled warning-validation project after the current publication tables, figures, and manuscript are complete.
