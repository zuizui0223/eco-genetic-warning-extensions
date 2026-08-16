# Results III — warning portability across independently calibrated domains

> Publication source: `manuscript/main_text.md`. This file is a focused Stage III result note and must preserve the same identification boundary.

Fresh-seed validation was run in the two Protocol 003 domains that passed confirmation calibration. Each domain contained five new master seeds and 20 replicates per seed, for 100 attempted trajectories per domain. All six preregistered relative-warning endpoints were retained: 5%, 10%, and 20% post-baseline declines in `H_alpha` and `H_gamma`.

The two domains are **not** a matched transition-direction experiment. The recalibrated symmetric domain uses `A_ref=0.8`, interaction-feedback `kappa=6.0`, `kappa_mu=0.20`, `p_star=0.50`, ramp 30, hold 210, horizon 240 and normalized barrier increase 0.20. The directional calibrated domain uses `A_ref=1.0`, `kappa=4.5`, `kappa_mu=0.05`, `p_star=0.90`, ramp 30, hold 90, horizon 120 and increase 0.10. Stage III therefore tests warning portability across complete calibrated eco-genetic domains.

## Recalibrated symmetric domain

The domain completed 82 of 100 attempted trajectories. All completed trajectories had an eligible diversity baseline. Fifty-four trajectories produced a valid warning/loss pair at every endpoint. Across the six endpoint summaries, there were 323 leads, one tie and no lags among 324 valid pairs.

Keeping the full attempted denominator, valid-pair availability was 0.540. Whole-trajectory bootstrap resampling gave a lead fraction of 0.997 with a 95% interval of 0.990–1.000.

Using the conventional median, positive warning-to-loss lead times ranged from 106 to 109 generations. Dividing by the full 240-generation calibrated horizon gave median fractions of 0.442–0.454.

## Directional calibrated domain

The domain completed 91 of 100 attempted trajectories. Ten completed trajectories were baseline-ineligible. Endpoint-specific valid-pair counts ranged from 28 to 38. Across all six endpoint summaries, there were 184 leads, five ties and 12 lags among 201 valid pairs.

Keeping the full attempted denominator, valid-pair availability was 0.335. Whole-trajectory bootstrap resampling gave a lead fraction of 0.915 (95% interval 0.848–0.971) and a lag fraction of 0.060 (0.016–0.112).

Conventional median positive lead times ranged from 72.5 to 77.5 generations. Dividing by the full 120-generation calibrated horizon gave median fractions of 0.604–0.646.

## Interpretation

Absolute positive lead times are shorter in the directional calibrated domain, but the direction of the contrast reverses after normalization by the calibrated horizon. Because the two domains also differ in ecological parameters and barrier schedules, the Stage III timing difference cannot be attributed to recurrent-transition direction alone.

The supported Stage III result is narrower and more useful: the same six relative-warning definitions were not equally available or equally ordered across two independently warning-blind calibrated eco-genetic domains. Source failure, baseline ineligibility and censoring are therefore part of the warning-performance result rather than missing data to be removed.
