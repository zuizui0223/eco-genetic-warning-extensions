# Phase U — fresh independent replication of allele-only m=.10 heterogeneity

## Question

> Does the high-precision between-block heterogeneity observed at legacy allele-frequency mixing `m=.10` reproduce in one completely fresh five-seed ensemble?

This is the next priority because Phases R and S showed that the historical `m=.10` effect does not port to whole-individual dispersal or pollen-only gene flow, while Phase T found no dynamic-partner effect at matched expected support. Before retaining `m=.10` as a headline stochastic mechanism, its replication across an independent seed ensemble must be tested directly.

## Fresh seeds

The master seeds are fixed prospectively as:

`20291010, 20291011, 20291012, 20291013, 20291014`.

A repository search performed before declaration found no prior use of these seed values. They are not replacements selected after an outcome.

## Fixed design

The Phase-E/M eco-genetic anchor is unchanged:

- `A_ref=1.0`;
- interaction `kappa=4.5`;
- `kappa_mu=.35`, `p_star=.35`;
- four equal patches at fixed total area;
- ramp 30 + hold 90 generations;
- normalised barrier increase `.30`.

Each fresh master seed has 100 attempted source replicates. Each prepared source and trajectory seed is paired across exactly two conditions:

1. `m=0`;
2. legacy allele-frequency mixing `m=.10`.

No other migration level or biological movement operator is included.

## Opening rule

The fresh replication does **not** require `m=0` or `m=.10` to fall in a favourable historical R1–R4 category. Interpretation requires only:

- at least 70 baseline-eligible trajectories in every seed block for both conditions;
- identical paired baseline eligibility between `m=0` and `m=.10`.

This avoids selecting a fresh ensemble because a control happened to reproduce R4.

## Primary and negative-control estimands

Primary: Pearson equal-rate diagnostic across the five fresh `m=.10` blocks.

Negative control: the same equal-rate diagnostic across the five paired `m=0` blocks.

Secondary:

- pooled realised functional-loss incidence;
- paired bidirectional loss-status switches;
- exact McNemar marginal-risk contrast;
- historical R1–R4 screen label for provenance only.

## Preregistered decision

- `m=.10 p<.05`, `m=0 p>=.05` → **specific m=.10 heterogeneity replicated**;
- both `p<.05` → **fresh-ensemble heterogeneity not specific to m=.10**;
- `m=.10 p>=.05` → **historical m=.10 heterogeneity not freshly replicated**;
- any block with <70 paired eligible trajectories → **insufficient fresh precision**.

The fixed alpha is `.05`.

## Consequence

If `m=.10` fails this one fresh replication, the paper-level interpretation must be downgraded from a reproducible `m=.10` heterogeneity effect to a historical-seed-family-specific observation. The stronger supported connectivity result would then be that the legacy allele-frequency operator changes stochastic trajectory identity and differs from biological movement closures, not that `.10` reliably generates block heterogeneity.

If it replicates specifically at `m=.10`, the operator-specific heterogeneity result gains independent ensemble support.

## Stop rule

Run exactly this one fresh ensemble. Do not replace seeds, add migration levels, rerun fresh ensembles, alter alpha or the historical screen, or increase precision after observing outcomes merely to obtain replication.
