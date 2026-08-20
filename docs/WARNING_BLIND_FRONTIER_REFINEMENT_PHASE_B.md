# Warning-blind recurrent-transition frontier refinement — Phase B

## Status

Prospectively declared after Phase A closed with 0/10 R4 cells and before Phase-B simulation.

Phase B is **condition-boundary mapping**, not a search for a successful warning. Genetic-diversity and warning fields remain unavailable throughout refinement and any later confirmation.

## Why this boundary is chosen

The locked Protocol 002 grid contains a particularly clean matched bracket at `kappa_mu=0.35` with every non-transition condition held identical:

- `A_ref=1.0`;
- interaction-feedback `kappa=4.5`;
- ramp 30, hold 90, horizon 120;
- normalized barrier increase `0.30`.

Historical anchor outcomes, using only trait-loss fields:

- `p_star=0.25`, batch `619`: pooled loss `1.0`; seed-block rates `1,1,1,1,1`; 21 baseline-eligible / 21 losses -> R2 rapid-loss.
- `p_star=0.50`, batch `673`: pooled loss `0.0`; seed-block rates `0,0,0,0,0`; 21 baseline-eligible / 0 losses -> R1 persistence.

This is therefore a pure recurrent-transition bracket: the coarse grid crosses from deterministic rapid loss to deterministic persistence while ecological and deterioration parameters remain matched.

## Phase-B grid

Fix `kappa_mu=0.35` and the matched ecological/deterioration anchor above.

New interior `p_star` values:

`0.30, 0.35, 0.40, 0.45`

The historical `0.25` and `0.50` endpoints are bracket anchors only. New Phase-B evidence comes from independently reconstructed sources at the four interior values with fresh seeds.

## Seeds and replication

Refinement seed family, reserved before execution:

`20281210, 20281211, 20281212, 20281213, 20281214`

- 5 replicates per seed;
- 25 attempts per interior cell;
- 4 cells;
- 100 planned refinement attempts.

Confirmation seed family, used **only if an R4 candidate is found**:

`20290110, 20290111, 20290112, 20290113, 20290114`

- 20 replicates per seed for confirmation.

Repository search found no use of either seed family before this declaration.

## Regime classification

Retain the same warning-blind strict definition:

- R0 source-infeasible: source/projection/baseline prerequisites fail sufficiently to prevent a complete event-regime estimate;
- R1 persistence: every seed-block loss rate < 0.30;
- R2 rapid-loss: every seed-block loss rate > 0.70;
- R3 seed-heterogeneous: seed-block rates span the strict band/categories;
- R4 warning-evaluable event regime: every seed-block loss rate lies in `[0.30,0.70]`.

R4 is only a property of the functional-loss event regime. It is not evidence that genetic warning succeeds.

## Decision rule

1. If two or more adjacent interior `p_star` cells are R4, freeze the contiguous interval and confirm it with the reserved fresh confirmation seeds before any warning/diversity endpoint is released.
2. If exactly one interior cell is R4, one additional warning-blind local refinement around that cell may be declared before confirmation.
3. If no interior cell is R4, do not tune ecological/deterioration parameters to manufacture one. Record the rapid/persistence/heterogeneous frontier as the result.
4. Warning endpoints remain unavailable unless a matched R4 region is independently confirmed.

## Theoretical prediction declared before execution

For the local affine support condition,

`p_star_crit = p + (p_c-p)/kappa_mu`.

When the pre-transition state is below its local high-state threshold (`p<p_c`), stronger `kappa_mu` lowers the `p_star` required to reach the same local support boundary. This predicts that the finite support/loss frontier should lie at lower `p_star` for `kappa_mu=0.35` than for the weaker Phase-A row, but it does not predict the exact stochastic loss probabilities or guarantee an R4 interval.

## Evidence boundary

The choice of Phase-B anchor and grid uses only source/trait-loss information from the locked Protocol 002 campaign plus the warning-blind Phase-A result. No genetic-diversity, warning, lead/lag or timing outcome was inspected to choose this Phase-B design.
