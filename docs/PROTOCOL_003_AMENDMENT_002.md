# Protocol 003 Amendment 002: confirmation calibration

The first independent calibration completed 100 trajectories across four candidates. No candidate met the predeclared eligibility rule. The two candidates closest to the pooled target of 0.5 were:

- symmetric bridge: hold 210, normalized barrier increase 0.20, pooled trait-loss rate 0.6842;
- transition: hold 90, normalized barrier increase 0.10, pooled trait-loss rate 0.6316.

The failure was driven by unstable within-seed estimates after source-preparation losses left only 2–5 eligible trajectories per seed block. This amendment does not relax or alter the eligibility rule. It increases replication and uses a fresh confirmation seed family.

## Locked design

- candidates: the two schedules above;
- master seeds: 20270620–20270624;
- replicates: 20 per seed;
- total trajectories: 2 × 5 × 20 = 200;
- endpoint contract: trait loss only;
- eligibility rule: unchanged from the independent calibration;
- no warning endpoint is calculated or inspected.

A candidate may proceed to fresh-seed warning validation only if its confirmation artifact reports `calibration_eligible: true`.
