# Phase M result — connectivity effect is non-monotone and not a marginal-risk shift

## Decision

The low-precision Phase-E interpretation is revised.

At 100-attempt precision, `m=0.20` returns to R4 and shows no detectable excess block heterogeneity. `m=0.10` remains R3 and, unlike the low-precision audit, now shows detectable between-block rate heterogeneity. None of the tested migration levels shows a directional paired marginal loss-probability effect versus isolation.

## Provenance

- workflow run `32558147960`
- artifact `9472067167`
- digest `sha256:0b15ca5a3b7f40a24332f8bcc14fad01036ed2d3fb4c0ff7ff181208a5d940d6`
- preregistered head `ddb4d208d7524eeae578b93c65b67ceee1d30b7d`
- first-20 prefix audit passed for all five master seeds × five migration levels

## High-precision map

| m | pooled loss | gate regime | equal-rate p |
|---:|---:|---|---:|
| 0 | 0.559 | R4 | 0.710 |
| .025 | 0.548 | R4 | 0.779 |
| .05 | 0.564 | R4 | 0.702 |
| .10 | 0.557 | **R3** | **0.0205** |
| .20 | 0.541 | R4 | 0.923 |

At `m=.10`, block rates are `0.511, 0.539, 0.710, 0.488, 0.527`. The `66/93=0.710` block crosses the upper historical R4 boundary and the five high-precision blocks show detectable excess equal-rate heterogeneity.

By contrast, the old `m=.20` R3 label disappears at high precision.

## Paired marginal effects versus isolation

| m | loss→no-loss | no-loss→loss | exact McNemar p |
|---:|---:|---:|---:|
| .025 | 24 | 19 | 0.542 |
| .05 | 31 | 33 | 0.901 |
| .10 | 50 | 49 | 1.000 |
| .20 | 71 | 63 | 0.546 |

The trajectory identities change substantially, especially at higher mixing, but there is no evidence for a directional marginal increase or decrease in functional-loss probability.

## Corrected biological claim

Do **not** claim a monotone `m>=0.10` R4→R3 connectivity boundary.

The supported bounded statement is:

> At one fixed eco-genetic anchor, allele-frequency mixing changed which paired stochastic trajectories lost function. At the specifically tested `m=0.10` level, high-precision blocks also showed excess between-block heterogeneity and failed the historical R4 screen, whereas `m=0.20` did not. The effect is therefore non-monotone and is not a directional marginal-risk response.

`migration_rate` remains allele-frequency mixing only, not demographic, pollen, seed, pollinator or recolonisation movement.

## Stop rule

Do not refine migration around 0.10 to manufacture or map a sharper heterogeneity peak in the present programme. The predeclared historical levels have answered the validation question. A future mechanism study could examine why a non-monotone mixing level generates block dependence, but it must be separately prospectively declared.
