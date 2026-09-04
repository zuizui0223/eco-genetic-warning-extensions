# Cross-layer alignment propagation audit — Amendment 001

**Status:** prospective clerical amendment committed before any intermediate-generation propagation outcome is opened or any propagation rerun is executed.

## Reason

`CROSS_LAYER_ALIGNMENT_PROPAGATION_PREREGISTRATION.md` defines the half-retention horizon on the fixed grid `{2,5,10,20,40,60}` and correctly distinguishes:

- half-retention reached and retained;
- a below-half crossing followed by rebound;
- half-retention not reached by generation 60.

Its named interpretation classes, however, accidentally omit the logically possible edge case in which the first retained half-level occurs **exactly at generation 60**. The preregistration assigns `attenuating_representation_memory` only to first retained half-levels at 10, 20, or 40, while `persistent_representation_memory` requires that the half-level is not reached by 60.

## Fixed correction

Without changing any horizon, statistic, threshold, seed, state, dynamics, or outcome rule, the interpretation class is completed as follows:

- `short_representation_memory`: first retained half-level at `h=2` or `h=5`;
- `attenuating_representation_memory`: first retained half-level at `h=10`, `20`, `40`, **or `60`**;
- `persistent_representation_memory`: retained half-level is not reached by `h=60`;
- `nonmonotone_representation_memory`: the median interaction-distance curve crosses below the half-level at a preregistered horizon and later rises above it;
- `representation_memory_not_identifiable`: unchanged from the preregistration.

A first retained half-level at generation 60 may additionally be described in prose as **late attenuation at the terminal horizon**, but it is not promoted to a new statistical class.

## Invariants

This amendment does not alter the primary coordinate `D_I_max`, the one-half retention threshold, the fixed horizon grid, the familywise cumulative-loss analysis, bootstrap procedure, warning firewall, publication-routing rule, or any stop rule. It closes only a previously uncovered classification branch before outcome access.