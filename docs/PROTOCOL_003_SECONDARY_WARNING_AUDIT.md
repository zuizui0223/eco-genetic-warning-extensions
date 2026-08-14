# Protocol 003 secondary warning audit after manuscript identification review

## Status

This is a **post hoc secondary audit of already locked Stage III validation records**. It was added after manuscript review identified that the two independently calibrated validation domains differed in more than recurrent-transition direction.

No simulation is rerun. No domain, schedule, endpoint, seed family, warning threshold, censoring rule, or validation trajectory is changed.

The source records are the immutable Protocol 003 Stage III artifacts:

- symmetric-domain artifact `8343958766`, digest `sha256:c1b42fc9e6ac912a44667ef4cee02090fab37d50fc3a9928c46ae728c0610f58`;
- directional-domain artifact `8343922879`, digest `sha256:0a994bea874fc9c47544169cd31bbc317c88690dfe1b6fa7548516e35fd7bca8`;
- source workflow run `29417632137`.

The publication workflow downloads those locked artifacts directly and materialises a 1,200-row trajectory-endpoint table inside the checksummed submission bundle before calculating the secondary audit.

## Identification issue

The Stage III domains are not a single-factor comparison.

The recalibrated symmetric domain uses `A_ref=0.8`, interaction-feedback `kappa=6.0`, `kappa_mu=0.20`, `p_star=0.50`, ramp 30 generations, hold 210 generations, total horizon 240 generations, and normalized barrier increase 0.20.

The directional calibrated domain uses `A_ref=1.0`, interaction-feedback `kappa=4.5`, `kappa_mu=0.05`, `p_star=0.90`, ramp 30 generations, hold 90 generations, total horizon 120 generations, and normalized barrier increase 0.10.

These differences arose because strict common-family Protocol 002 calibration selected no domain and Protocol 003 subsequently performed a separately declared, warning-blind event-risk calibration. Stage III therefore tests **portability across independently calibrated eco-genetic domains**, not the isolated causal effect of transition direction. The common Stage I/II grid remains the appropriate evidence for statements about how recurrent-transition parameters reorganised source feasibility and functional-loss regimes.

## Protocol 003 calibration amendments

Protocol 002 required every seed block to have post-baseline trait-loss frequency in `[0.30, 0.70]`. All 15 coordinates were recorded as `no_domain_selected`.

Protocol 003 Amendment 001 was written after inspecting trait-loss-only bracket results and before warning validation. It:

1. expanded the candidate schedules for two sentinel coordinates, including the weaker directional neighbour `(hold=90, increase=0.10)`;
2. defined eligibility as pooled trait-loss frequency in `[0.30, 0.70]`, at least four of five seed-block rates in `[0.20, 0.80]`, and at least three baseline-eligible trajectories in every seed block;
3. prohibited loading or persisting any warning endpoint during calibration.

The first independent calibration did not satisfy this gate. Amendment 002 did **not** relax the gate; it increased replication to 20 per seed and used a fresh confirmation seed family. Only confirmation-eligible candidates proceeded to fresh-seed warning validation.

## Secondary analyses

### Conventional medians

The original Stage III generator used `sorted(lead_times)[len(lead_times)//2]` for `median_positive_lead_time`. For even sample sizes this returns the upper middle order statistic rather than the conventional median. This audit uses `statistics.median`, which averages the two middle values for even `n`. The original artifacts remain immutable; the manuscript and revised publication figure use the corrected secondary summary.

### Horizon-normalized timing

Absolute positive lead time is divided by the **full calibrated deterioration horizon** (ramp + hold) for each domain. A hold-only normalization is retained in the machine-readable audit as a sensitivity description, but the manuscript uses full-horizon normalization because warning and trait-loss times are measured from the start of the ramp. The normalized result is descriptive; it does not create a schedule-matched causal contrast.

### Trajectory-cluster bootstrap

The six warning endpoints from one trajectory are correlated. Aggregate uncertainty is therefore calculated by resampling whole attempted trajectories with replacement, preserving all six endpoint rows within each sampled trajectory. The audit uses 20,000 bootstrap replicates, fixed seed `20260814`, and percentile 95% intervals.

Reported aggregate quantities are lead fraction among valid endpoint pairs, lag fraction among valid endpoint pairs, and valid-pair availability among all attempted endpoint opportunities. Endpoint-specific positive lead-time medians and horizon-normalized medians are also bootstrapped by trajectory. These intervals describe uncertainty in this finite model campaign; they are not population-level inferential confidence intervals.

### Cumulative event incidence

Warning and functional-trait loss are not classical competing risks because both can occur in the same trajectory. The audit therefore reports cumulative observed incidence of warning and realised functional-trait loss among baseline-eligible completed trajectories over the administratively censored horizon. Non-events remain in the denominator through the end of follow-up.

## Locked secondary results

Across all six endpoints, valid-pair availability among attempted endpoint opportunities was 0.540 in the recalibrated symmetric domain and 0.335 in the directional calibrated domain. Whole-trajectory bootstrap lead fractions among valid pairs were 0.997 (95% interval 0.990–1.000) and 0.915 (0.848–0.971), respectively. The directional-domain lag fraction was 0.060 (0.016–0.112).

Correct conventional median positive lead times were 106–109 generations in the recalibrated symmetric domain and 72.5–77.5 generations in the directional calibrated domain. After division by each domain's full calibrated horizon, the ranges were 0.442–0.454 and 0.604–0.646, respectively. The direction of the absolute timing contrast therefore reverses under horizon normalization.

## Interpretation boundary

The revised manuscript may state that strict common-family calibration failed at all 15 coordinates; recurrent-transition parameters reorganised source feasibility and functional-loss regimes in the common grid; after separately declared warning-blind calibration, warning availability and ordering differed between two complete eco-genetic domains; absolute positive lead times were lower in the directional calibrated domain; and horizon-normalized positive lead times were higher there.

The revised manuscript must **not** state that transition direction alone shortened lead time in Stage III. No secondary analysis here changes the original Protocol 002 or Protocol 003 decisions.

## Reproduction and preservation

`Paper completion sprint` downloads the two immutable Stage III artifacts by workflow run and artifact name, verifies the locked repository contract, flattens the 200 attempted trajectories to the endpoint table, runs the fixed 20,000-replicate audit, and checks that the regenerated compact publication summary is byte-identical to `manuscript/tables/stage3_review_summary.csv`.

The final submission bundle therefore contains the generated trajectory-endpoint table, the complete secondary-audit JSON, the compact publication CSV, artifact identifiers and digests, and a SHA-256 manifest. This avoids making the repository dependent on an undocumented local copy while preserving the historical artifacts as the primary source provenance.
