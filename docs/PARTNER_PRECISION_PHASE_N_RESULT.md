# Phase N result — historical Phase-G partner-loss R3 labels disappear at high precision

## Decision

**All four architectures classify R4-highrep at 100-attempt precision.** The historical Phase-G claim that one-partner loss changes warning estimability/reproducibility through an R4→R3 transition is withdrawn.

The first-20 provenance audit passed for all five historical master seeds and all four architectures, so this is an exact precision continuation of Phase G rather than a replacement-seed experiment.

## High-precision map

| architecture | pooled loss | regime | equal-rate p |
|---|---:|---|---:|
| intact | 0.556 | R4 | 0.117 |
| even loss | 0.544 | R4 | 0.488 |
| graded loss | 0.565 | R4 | 0.263 |
| dominant loss | 0.549 | R4 | 0.121 |

No architecture shows detectable excess block-rate heterogeneity at this precision.

## Paired effects versus intact

| architecture | loss→no-loss | no-loss→loss | exact McNemar p |
|---|---:|---:|---:|
| even | 86 | 81 | 0.757 |
| graded | 75 | 79 | 0.809 |
| dominant | 67 | 64 | 0.861 |

Partner loss changes many individual stochastic histories in both directions, but there is no directional paired marginal functional-loss effect.

## Corrected claim

Do not state that partner loss, contribution concentration or reduced-form functional redundancy changes the R4/R3 event-regime class at this anchor.

The supported bounded result is:

> Under the tested reduced-form partner-loss closure, removing one of four partner contributions changes which stochastic trajectories lose function, but at high precision the intact, even, graded and dominant architectures have similar pooled loss, no directional paired marginal effect, and all remain within the historical R4 event regime.

This is not an explicit partner-demography, coextinction or rewiring model.

## Provenance

- run `32558466157`
- artifact `9472148035`
- digest `sha256:c55654b556280c5caa63ee1b9febe62a0b545da6227104799014484f65dc25c0`
- corrected head `199faf10e26c040f8559efe38462ff9f20c9b3b3`
- locked summary `artifacts/partner_precision/phase_n_locked_summary.json`

## Stop rule

Phase N is closed. Do not retune partner weights, select other lost partners, replace seeds, or further increase precision merely to recreate the historical R3 labels.
