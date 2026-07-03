# Protocol 002 — mutation-direction phase diagram

**Status:** preregistered main-campaign design; no numerical result.

## 1. Scope and relationship to Protocol 001

Protocol 001 is retained as a three-anchor bridge/pilot:

```text
SYM   kappa_mu = 0.20, p_star = 0.50
UP    kappa_mu = 0.20, p_star = 0.75
DOWN  kappa_mu = 0.20, p_star = 0.25
```

Protocol 002 is the primary campaign for Paper 001. It asks about the
phase structure induced by mutation direction. It does not pool Protocol 001 and
Protocol 002 outcomes, and Protocol 001 does not select coordinates for Protocol
002.

## 2. Declared mutation coordinates

The coordinate system is

\[
\kappa_\mu=u_{L\to H}+u_{H\to L},\qquad
p_\mu^\ast=\frac{u_{L\to H}}{\kappa_\mu},
\]

with rates reconstructed as

\[
u_{L\to H}=\kappa_\mu p_\mu^\ast,\qquad
u_{H\to L}=\kappa_\mu(1-p_\mu^\ast).
\]

The full primary grid is

```text
kappa_mu: 0.05, 0.20, 0.35
p_star:   0.10, 0.25, 0.50, 0.75, 0.90
```

for 15 predeclared mutation coordinates. `p_star = 0.50` is symmetric; lower
values bias recurrent mutation toward the low-trait allele and higher values bias
it toward the high-trait allele.

`kappa_mu` fixes mutation-map relaxation strength, not instantaneous expected
mutation flux. This distinction is reported explicitly in all outputs.

## 3. Unchanged closure

Only the recurrent mutation operator differs from the inherited declared
finite closure. Selection, migration, finite drift, trait recruitment, full-state
source transfer, conservation projection, diversity metrics, and trait-loss event
semantics are imported unchanged and version-pinned before simulation.

The operator must be applied after selection/migration and before finite drift.
Any other biological modification is out of scope and requires a new protocol.

## 4. Stage 0 — algebraic and implementation certificate

Before a stochastic run, write an immutable certificate showing for every grid
coordinate:

- \(u_{L\to H},u_{H\to L}\in[0,1]\) and their sum is \(\kappa_\mu\);
- the map preserves \([0,1]\);
- the map has contraction factor \(1-\kappa_\mu\);
- the mutation-only equilibrium is \(p_\mu^\ast\);
- all symmetric coordinates reproduce the predecessor operator exactly; and
- expected mutation flux \(J(p)\) is reported at \(p=0,0.5,1\) rather than
  silently equated across directional panels.

No ecological or warning outcome may be computed in Stage 0.

## 5. Stage I — independent H1 source reconstruction

For every mutation coordinate, run the frozen source grid:

```text
A_ref: 0.8, 1.0, 1.2
kappa: 3.0, 4.5, 6.0
source master seeds: 20270210–20270214
replicates: 5 per cell per master seed
nested barrier grids: 25, 49, 97
stage generations: 30
hold generations: 30
```

A source record retains all preparation failures, source support failures,
full-state projection failures, and successful transfers. The source grid exists
to determine feasibility under each new closure; no predecessor source is
inherited as qualified.

## 6. Stage II — trait-loss-only calibration

For each coordinate with at least one valid source, evaluate only the following
candidate family:

```text
barrier ramp: 30 generations
barrier hold: 90 or 210 generations
normalised total barrier increase: 0.15, 0.30, 0.45
calibration master seeds: 20270310–20270314
replicates: 5 per cell per master seed
```

The only calibration endpoint is

\[
P(0<\tau_T\le T\mid\text{source prepared, projection supported, baseline high trait present}).
\]

No diversity, warning, lead/lag, warning time, or lead-time field may be loaded,
calculated, persisted, or inspected during this stage.

A cell/schedule pair is eligible only if every calibration seed block has a
trait-loss frequency in \([0.30,0.70]\). Select at most one pair per mutation
coordinate by:

\[
(|\bar P_T-0.50|,\ T,\ d,\ A_{\rm ref},\ \kappa),
\]

where \(T\) is total horizon and \(d\) normalised barrier increase. If no pair
is eligible, record `no_domain_selected` and do not expand the candidate family.

## 7. Stage III — fresh-seed validation

Validate each selected coordinate independently using:

```text
validation master seeds: 20270410–20270414
replicates: 20 per selected coordinate per master seed
```

For every available trajectory, calculate all six relative-warning endpoints:

```text
H_alpha: r = 0.05, 0.10, 0.20
H_gamma: r = 0.05, 0.10, 0.20
```

Retain, for every endpoint and replicate:

```text
coordinate, source_status, projection_status, baseline_eligibility,
warning_time, trait_loss_time, event_pair_validity,
lead_tie_lag, usable_lead_time, censoring_reason
```

A generation-0 crossing is baseline-ineligible rather than an early warning.
Missing warning and/or trait-loss events remain right-censored. A trajectory is
not removed merely because it lacks a valid event pair.

## 8. Primary estimands

For each coordinate and endpoint, report:

1. H1 source feasibility proportion;
2. source-to-projection support proportion;
3. post-baseline trait-loss probability by the locked horizon;
4. trait-loss-time distribution conditional on occurrence;
5. warning availability;
6. valid-pair denominator;
7. lead, tie, and lag counts and proportions;
8. usable-lead-time distribution among leads;
9. censoring composition; and
10. seed-block heterogeneity.

No pooled cross-coordinate average may replace the coordinate-resolved phase map.

## 9. Secondary audit

After Stage III has completed, apply the predeclared absolute thresholds

\[
H_\alpha\le0.20,\qquad H_\gamma\le0.20
\]

to the exact same stored validation trajectories. It is a deterministic audit
only: no resimulation, no threshold tuning, and no cell/schedule change.

## 10. Decision rules

- A directional effect is supported only as Type S evidence for a named
  coordinate/domain/output; it is never declared a general biological law.
- One coordinate's lead result does not imply a lead result at another coordinate.
- A lag in any endpoint remains reported; it cannot be removed by choosing a
  different threshold or horizon after inspection.
- A non-selected coordinate is not an H2 failure. It is an explicit feasibility
  result under the declared source and calibration families.
- Any added coordinate, changed seed set, or changed candidate schedule requires
  Protocol 003.

## 11. Paper independence constraints

The Paper 001 figures must be produced from Protocol 002 artifacts. Protocol 001
may appear only as an implementation bridge/control figure or supplement. The
predecessor repository's numerical trajectories, selected source, calibration
result, and validation outcomes are not inputs to the Paper 001 evidence set.