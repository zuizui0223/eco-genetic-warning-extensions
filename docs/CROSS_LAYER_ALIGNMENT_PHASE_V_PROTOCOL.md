# Cross-layer alignment state-sufficiency test — Phase V

## Question

The prospective urban–island extension asks whether different fragmentation mechanisms can converge on the same operational interaction-mediated functional-fragmentation regime. Before treating such a regime as mechanism-agnostic, one missing mathematical question must be resolved:

> **If layer-wise state summaries are the same, is the downstream functional-loss process independent of how those layers are aligned across patches?**

Phase V tests this necessary state-sufficiency condition. It is not an urban-versus-island simulation.

## Two fixed states

Both states contain four equal patches of area 1 and 40 individuals per patch. They have exactly the same marginal multisets:

- interaction `q = {0.65, 0.75, 0.85, 0.95}`;
- high-allele frequency `p = {0.20, 0.40, 0.60, 0.80}`;
- realised high-trait mass `x_H = {0.20, 0.40, 0.60, 0.80}`;
- the same complete global trait-bin totals;
- the same total population, mean q, mean p, mean high-trait mass, `H_alpha`, `H_gamma` and `FST`.

The genetic/trait bundle keeps `p=x_H` within each patch. Only its assignment to interaction support changes:

- **aligned:** q and the p/x_H bundle increase together;
- **anti-aligned:** the same bundle multiset is reversed relative to q.

Thus the experiment changes cross-layer covariance without changing any declared marginal state summary.

The minimum q is 0.65, just above the default model's analytic high-trait potential-viability threshold at z=1 (`q >= 0.625` from `W(1;q)=0.5+0.8q >= 1`). This ensures every declared patch begins on the potential high-trait side rather than constructing the contrast by making some patches intrinsically non-viable.

## Fixed dynamics

Use the pinned parent scientific model `dd8ee379d0d3518194c767d16402042525bc00dc` with the existing standard finite-bin closure:

- four area-1 patches;
- carrying density 40 and initial N=40 per patch;
- `interaction_feedback=4.5`, `area_reference=1`;
- finite trait-bin recruitment, 31 bins;
- two-kernel recruitment, inheritance weight 0.5;
- q-feedback weights `(q, trait, allele)=(0.6,0.3,0.1)`;
- no migration;
- no added symmetric allele mutation;
- 60 generations;
- one linear interaction-barrier deterioration schedule from 0.50 to 0.65. These are existing standard-profile barrier-grid values, chosen before outcomes rather than searched.

## Opening certificate

Before stochastic interpretation:

1. assert exact equality of the two coarse marginal signatures;
2. assert positive versus negative cross-layer covariance;
3. calculate the exact generation-1 interaction update under carrying density.

Because the parent q update uses local `0.6 q + 0.3 x_H + 0.1 p` inside a nonlinear sigmoid, identical layer-wise marginals need not imply identical local transition vectors. If generation-1 vectors differ, layer-wise marginals are not a sufficient Markov state for this declared dynamics.

## Finite loss experiment

Use five unused master seeds `20300110–20300114`, 100 paired replicates per seed. Each replicate uses the same trajectory seed in aligned and anti-aligned states.

Primary endpoint: post-baseline realised high-trait loss from the parent `tau_trait_realised` definition.

Primary inference: exact paired McNemar test on loss occurrence at alpha=.05.

Secondary description: seed-block loss rates and paired restricted loss time (`tau` if observed; 61 if censored).

No warning time, diversity decline or lead/lag field is used for selection or interpretation.

## Decision rule

- If the opening certificate differs but McNemar `p>=.05`: **coarse marginals are not transition-sufficient, but no functional-loss incidence effect is detected under this fixed schedule**.
- If the opening certificate differs and McNemar `p<.05`: **cross-layer alignment changes functional-loss incidence despite identical coarse marginals**, so an operational regime intended to predict loss must retain cross-layer spatial alignment (or an equivalent sufficient statistic).

Either result is retained.

## Stop rule

Do not change q/p/trait values, seeds, horizon, deterioration schedule, alpha, feedback weights or precision after outcomes. Do not add intermediate permutations or rerun new seed ensembles to obtain a preferred result. Phase V is one preregistered state-sufficiency test.
