# Phase I result: decomposition not opened because the partner-loss regime did not reproduce

## Decision

**Phase I is closed as `not_opened`.** The preregistered positive control reproduced R4, but the preregistered partner-loss/no-rescue negative control did **not** reproduce the Phase-H R3 classification on the new fresh seed ensemble. It was R4-highrep. Per the opening rule, support-magnitude and recovery-timing contrasts are not interpreted causally and no seeds, support schedules, recovery windows or R4 thresholds are changed.

## Provenance

- preregistered head: `f879a4f4fbbe0a9786536a76d8fce97798cd704c`
- workflow run: `32556093071`
- artifact: `9471533889`
- artifact digest: `sha256:218d476ebc2fc5f140df681f7d36a3500b64872f514e93b249ee78ef46e6e164`
- parent scientific commit: `dd8ee379d0d3518194c767d16402042525bc00dc`
- committed compact evidence: `artifacts/support_timing/phase_i_summary.json`

## Opening controls

| condition | eligible | losses | pooled loss | seed-block loss rates | regime |
|---|---:|---:|---:|---|---|
| intact control | 90/100 | 46 | 0.511 | 0.529, 0.556, 0.526, 0.444, 0.500 | R4-highrep |
| partner loss / no rescue | 90/100 | 44 | 0.489 | 0.412, 0.444, 0.579, 0.500, 0.500 | R4-highrep |

The opening required `intact = R4` **and** `partner loss / no rescue = R3`. The second requirement failed. This is not a software failure and not a warning result. It is a prospective failure to reproduce the event-regime class required for the planned causal decomposition.

## Representation audits all passed

Three comparisons were required to be biologically identical by construction because they presented the same effective-support trajectory to the eco-genetic life cycle. All passed exactly across 90 comparable trajectories:

- `topology_only_null` = `partner_loss_no_rescue`: 0 status switches;
- `partial_support_only` = `coupled_rewiring_replay`: 0 status switches;
- `full_support_immediate` = `intact_control`: 0 status switches.

This confirms the intended representation boundary: in the current closure, rewired topology has no independent life-cycle effect beyond its network-derived support multiplier.

## Non-causal descriptive outcomes

Because the opening failed, the following rows are retained only as implementation/provenance outputs and are **not** evidence that partial or full support rescued R4:

| condition | pooled loss | regime |
|---|---:|---|
| topology-only null | 0.489 | R4-highrep |
| partial-support only | 0.478 | R4-highrep |
| coupled rewiring replay | 0.478 | R4-highrep |
| full support delayed | 0.489 | R4-highrep |
| full support immediate | 0.511 | R4-highrep |

The correct interpretation is that the prerequisite R3 loss regime was absent from this fresh ensemble, so there was nothing prospectively defined to rescue.

## New condition boundary exposed by the failed opening

Phase H and Phase I used the same declared biological anchor and partner-loss closure but independent fresh seed ensembles:

- Phase H partner loss / no rewiring: seed rates `0.500, 0.471, 0.529, 0.353, 0.294` → **R3-highrep**;
- Phase I partner loss / no rescue: seed rates `0.412, 0.444, 0.579, 0.500, 0.500` → **R4-highrep**.

The Phase-H R3 call was already near the operational boundary because its lowest block was `0.294`, just below the R4 lower limit `0.30`. Phase I now prospectively shows that the same biological condition can change R4/R3 classification across independent finite seed ensembles.

Therefore the next unresolved question is no longer support magnitude or rewiring timing. It is:

> **How stable is the R4/R3 event-regime classification itself across independently generated stochastic ensembles at a fixed biological condition?**

## Next validation requirement

The next campaign should freeze the biological conditions and R4 rule and estimate **ensemble-level classification stability** across several prospectively declared independent five-block seed ensembles. It should not search for an ensemble that reproduces R3 or R4. The estimand is the frequency/distribution of regime classifications and block-rate dispersion under the same condition.

At minimum, retain the intact control and partner-loss/no-rescue condition. The fixed Phase-H coupled rewiring condition may be retained as a secondary condition if the campaign is explicitly framed as stability mapping rather than rescue testing.

## Stop rule

Do not rerun Phase I with replacement seeds to obtain the missing R3 opening condition. Do not change the `[0.30, 0.70]` R4 band, recovery window, support levels or partner-loss identity. The failed opening is itself the result and motivates a new independently preregistered ensemble-stability question.
