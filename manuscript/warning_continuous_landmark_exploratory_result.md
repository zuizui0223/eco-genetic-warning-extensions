# Exploratory continuous landmark warning result

## Scope

The one-time analysis was fixed at prospective commit `bf9f492996cfb57718e03edd4a3620c0756b32c4` before any continuous score or AUC was calculated. It used the two immutable symmetric warning artifacts, baseline-relative erosion `1 - H(t)/H(0)`, both `H_alpha` and `H_gamma`, and all three fixed landmarks 30/60/90. No slope, alternative transformation, selected landmark or endpoint pooling was opened.

## Result

The continuous score did not produce a stable portable discrimination pattern.

| ensemble | coordinate | generation 30 AUC [95% CI] | generation 60 | generation 90 |
|---|---|---|---|---|
| inherited | `H_alpha` | 0.535 [0.407, 0.662] | 0.418 [0.266, 0.576] | 0.692 [0.523, 0.840] |
| inherited | `H_gamma` | 0.533 [0.407, 0.660] | 0.435 [0.277, 0.598] | 0.594 [0.390, 0.792] |
| fresh | `H_alpha` | 0.522 [0.385, 0.661] | 0.653 [0.494, 0.797] | 0.510 [0.102, 0.898] |
| fresh | `H_gamma` | 0.556 [0.421, 0.690] | 0.687 [0.504, 0.848] | 0.422 [0.082, 0.898] |

The inherited range was `0.418–0.692`; the fresh range was `0.422–0.687`. The two cells whose percentile intervals lay above 0.5 were different coordinate/landmark combinations: inherited generation-90 `H_alpha` and fresh generation-60 `H_gamma`. Neither reproduced at the same coordinate and landmark in the other ensemble. Fresh generation 90 retained only three future cases and consequently produced very wide intervals.

## Interpretation

The generation-30 continuous scores were near chance in both ensembles, consistent with the fixed binary-landmark audit. Later continuous erosion may contain time-specific information, but its sign and magnitude were not stable across the two frozen ensembles. This exploratory result therefore does not license a selected landmark, a new binary threshold or a portable continuous early-warning claim.

The permitted conclusion is narrower than “genetic diversity contains no information”: the six frozen binary first-passage rules lacked discrimination, and the fixed exploratory continuous levels did not identify a reproducible coordinate/time signal across ensembles.
