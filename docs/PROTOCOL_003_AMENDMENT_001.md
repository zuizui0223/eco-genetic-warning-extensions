# Protocol 003 Amendment 001 — calibration gate after blind bracket pilot

## Evidence boundary

This amendment was written after inspecting only the trait-loss-only aggregation of
Protocol 003 bracket run `29399936075`. No diversity, warning, lead/lag, event-pair,
or validation outcome was calculated or inspected.

The 64-trajectory pilot produced:

- `rapid_loss`: all four schedules had pooled trait-loss rate 1.0;
- `symmetric_bridge`: rates 0.0, 0.0, 1/3, and 2/3;
- `transition`: rates 3/4, 1.0, 1.0, and 1.0;
- `persistence`: all four schedules had pooled trait-loss rate 0.0.

## Independent calibration gate

Two sentinels proceed to independent calibration because at least one pilot schedule
was within 0.25 of 0.5:

1. `symmetric_bridge` `(kappa_mu=0.20, p_star=0.50)`
   - `(hold=210, increase=0.20)`
   - `(hold=300, increase=0.30)`
2. `transition` `(kappa_mu=0.05, p_star=0.90)`
   - `(hold=90, increase=0.10)` — weaker neighbour added before calibration
   - `(hold=90, increase=0.15)`

Calibration master seeds are fixed at `20270610`–`20270614`, with five replicates
per seed and 25 attempts per candidate. The endpoint remains realised trait loss only.

A candidate is eligible when:

- pooled trait-loss rate lies in `[0.30, 0.70]`;
- at least four of five seed-block rates lie in `[0.20, 0.80]`;
- every seed block has at least three baseline-eligible trajectories.

Rank eligible candidates by:

1. absolute distance of pooled rate from 0.50;
2. shorter horizon;
3. smaller normalised barrier increase.

## Additional blind bracket search

The unresolved extremes do not enter calibration yet.

- `rapid_loss`: test weaker schedules `(hold, increase)` =
  `(30,0.01)`, `(60,0.02)`, `(90,0.025)`, `(90,0.04)`.
- `persistence`: test stronger schedules =
  `(300,0.90)`, `(450,0.90)`, `(450,1.00)`, `(600,1.00)`.

These use new bracket seeds `20270520` and `20270521`, two replicates per seed.
No warning endpoint may be loaded or persisted.

## Validation boundary

No warning-validation domain is selected by this amendment. Fresh validation seeds
will be declared only after independent calibration is complete.
