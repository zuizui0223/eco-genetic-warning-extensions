# Dynamic partner architecture Phase T — locked result

## Decision

**`no_detected_dynamic_partner_architecture_effect_at_matched_expected_support`**

Phase T passed every preregistered opening condition and then found no detected change in pooled functional-loss incidence, between-block heterogeneity, or paired marginal loss status when temporal partner availability was introduced while expected aggregate interaction support remained fixed at 0.75.

## Opening gate

All opening conditions passed:

- the `constant_support_075` condition reproduced every locked first-20 Phase-G even-loss prefix;
- it reproduced all five high-precision Phase-N blocks exactly: `51/86, 45/90, 45/86, 46/91, 53/88`;
- paired baseline eligibility was identical across constant, even-dynamic, and dominant-dynamic conditions.

The dynamic comparisons are therefore interpretable under the declared protocol.

## High-precision result

| condition | pooled loss | block screen | equal-rate p | realised support variance |
|---|---:|---|---:|---:|
| constant support 0.75 | 0.5442 | R4 | 0.488 | 0 |
| even dynamic | 0.5488 | R4 | 0.299 | 0.04684 |
| dominant dynamic | 0.5533 | R4 | 0.208 | 0.09702 |

The intended mechanism was active: temporal support variance increased from zero in the scalar comparator to approximately 0.0468 under equal partner contributions and 0.0970 under dominant-partner concentration. Mean realised support remained approximately 0.75 in both dynamic architectures.

No dynamic condition showed detectable excess between-block heterogeneity.

## Paired trajectory effects

Across 441 comparable trajectories per comparison:

- even dynamic vs constant: 28 loss→no-loss, 30 no-loss→loss; exact McNemar `p=0.896`;
- dominant dynamic vs constant: 47 loss→no-loss, 51 no-loss→loss; `p=0.762`;
- dominant dynamic vs even dynamic: 22 loss→no-loss, 24 no-loss→loss; `p=0.883`.

Thus dynamic availability reshuffled some individual stochastic histories, but switches were balanced and no directional marginal-risk effect was detected.

## Scientific interpretation

Within this predeclared one-focal-node/four-partner closure, **temporal partner availability and contribution concentration do not alter the detected functional-loss process merely because they increase support variance while preserving expected support at 0.75**.

This strengthens the boundary already recovered by the high-precision partner-loss audit: aggregate support, partner contribution structure, and stochastic trajectory identity should not be promoted to general functional-loss mechanisms without an independently detected effect.

The result does not imply that ecological networks are generally insensitive to partner dynamics. Phase T does not represent partner abundance dynamics, coextinction, spatial partner movement, adaptive rewiring, or full multispecies feedback.

## Stop rule

Phase T is closed. Because it did **not** establish a dynamic-network effect, its preregistered rewiring gate remains closed. Do not tune partner availability, contribution weights, correlation structure, seeds, precision, or rewiring parameters to manufacture an effect from this campaign.

## Provenance

- workflow run: `32614486507`;
- scientific head: `f19bffe8b875e6ca3cd5c8ca9f338b041fcdcd60`;
- aggregate artifact: `9486577103`;
- artifact digest: `sha256:44f54e4b8ac313e01ea43444a84351012f308a69ccbcc4d0bf253cfa8ed9dc1c`;
- locked machine-readable result: `artifacts/dynamic_partner_architecture/phase_t_locked_summary.json`.
