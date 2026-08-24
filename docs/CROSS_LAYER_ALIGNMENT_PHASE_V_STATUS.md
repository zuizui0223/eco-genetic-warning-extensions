# Phase V result — cross-layer alignment and state sufficiency

Status: **completed and locked**.

## Decision

`coarse_marginals_not_transition_sufficient_but_no_detected_loss_incidence_effect`

## Opening certificate

Aligned and anti-aligned states retained the same declared habitat, census, interaction, allele-frequency, realised high-trait-mass and genetic-diversity marginals. Only cross-patch alignment changed.

- q-by-eco-genetic covariance: `+.025` versus `-.025`;
- aligned generation-1 q: `.464, .619, .753, .851`;
- anti-aligned generation-1 q: `.718, .699, .680, .660`;
- maximum patchwise generation-1 difference: **`.2543`**.

Thus the declared layer-wise marginals are **not transition-sufficient** for the local nonlinear interaction dynamics.

## Finite functional-loss contrast

Five preregistered master seeds, 100 paired replicates per seed, 500 pairs total:

| state | loss / 500 | pooled loss | seed-block loss rates | mean restricted loss time |
|---|---:|---:|---|---:|
| aligned | 339 | `.678` | `.63/.74/.73/.64/.65` | `34.332` |
| anti-aligned | 361 | `.722` | `.70/.71/.77/.71/.72` | `32.100` |

Paired loss switches:

- aligned loss → anti no-loss: `92`;
- aligned no-loss → anti loss: `114`;
- exact McNemar `p=.1432448563`.

No preregistered directional loss-incidence effect was detected at alpha=.05. Restricted loss time is descriptive only in this phase; no post hoc timing test is opened.

## Interpretation

Phase V falsifies the idea that a functional-fragmentation regime can be defined only by separate layer-wise snapshot marginals. Spatial joint organization can change the exact next ecological transition even when those marginals and standard genetic-diversity summaries match.

The stronger claim that cross-layer alignment alone changes long-horizon functional-loss probability is **not supported** by this one fixed deterioration schedule. The recovered boundary is therefore:

> **Operational regime equivalence requires a joint state and transition rule, not merely matching static layer-wise indicators.**

This is the bridge to natural comparisons: distinct fragmentation mechanisms may be compared as convergent only after testing whether they produce comparable joint eco-genetic-interaction states and comparable downstream transition dynamics. Similar habitat amount, genetic diversity, species richness, or mean interaction support alone is insufficient evidence of regime convergence.

For empirical work this means alignment `A` belongs in the candidate state **until predictive sufficiency permits it to be removed**, but `A` must not be treated as a universally directional risk score. A measurable alignment difference can matter to short-term dynamics without being sufficient to create a detectable long-horizon loss-incidence shift under every deterioration schedule.

## Provenance

- workflow run: `32636913615`;
- scientific head: `260a03220bf09d5f4a4d8cb55ec21062bf120c55`;
- artifact ID: `9492558602`;
- artifact digest: `sha256:a5754ab2d54dea868a72fed582a9862cbc88b83510e1cf81e0a872f56b70a1bd`;
- compact locked summary: `artifacts/cross_layer_alignment/phase_v_locked_summary.json`.

## Stop rule

No replacement seeds, added permutations, altered state values, horizon, barrier schedule, feedback weights, alpha or precision are opened after this result.
