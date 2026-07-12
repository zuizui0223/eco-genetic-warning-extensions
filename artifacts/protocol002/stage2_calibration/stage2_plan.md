# Protocol 002 Stage II — trait-loss-only calibration plan

## Entry condition

Stage II begins only after the Stage I completion lock records all `3,375`
source attempts as computationally complete.

## Calibration candidate family

```text
barrier ramp generations: 30
barrier hold generations: 90, 210
normalised total barrier increase: 0.15, 0.30, 0.45
calibration master seeds: 20270310–20270314
replicates: 5 per source cell per master seed
```

## Allowed calibration endpoint

Calibration may inspect only whether realised trait loss occurs by the declared
horizon, conditional on:

- source prepared;
- projection supported;
- baseline high trait present;
- no generation-0 crossing.

The calibration table may retain source/projection eligibility, trait-loss event
indicator, trait-loss time, horizon, barrier schedule, seed, and replicate.

## Forbidden calibration fields

The following must not be computed, loaded, ranked, or inspected during Stage II:

```text
H_alpha
H_gamma
warning
lead
lag
lead_time
diversity threshold crossing
relative diversity loss
```

## Eligibility and deterministic selection

Every calibration seed block must have trait-loss frequency in `[0.30, 0.70]`.
For each Protocol 002 mutation coordinate, select at most one eligible domain by:

```text
(abs(mean_trait_loss_probability - 0.50), horizon, barrier_increase, A_ref, kappa)
```

If no candidate is eligible, retain `no_domain_selected`.

## First implementation gate

The next PR should add:

1. a typed Stage II calibration-row schema;
2. a blind-column guard rejecting warning/diversity fields;
3. deterministic candidate eligibility and ranking tests;
4. a tiny no-simulation fixture artifact.

No full calibration campaign should run before those gates pass.
