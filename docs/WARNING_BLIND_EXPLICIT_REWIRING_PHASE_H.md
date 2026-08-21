# Warning-blind explicit rewiring Phase H

## Question

Phase G showed that a matched one-partner loss could move a fresh intact R4 control to R3 without materially changing pooled loss incidence. That result did not model rewiring.

Phase H asks one prospective question:

> **Can one fixed, biologically constrained interaction-rewiring rule recover a reproducible R4 functional-loss regime after the same matched partner-loss perturbation?**

The target is **event-regime reproducibility / warning estimability**, not average failure risk and not warning performance itself.

## Why Phase H is separate from PR #61

PR #61 is the fixed scientific baseline through Phase G. Phase H begins on a new stacked branch from that head so the completed condition-recovery manuscript is not enlarged retroactively.

## Fixed eco-genetic anchor

Before any Phase-H outcome is generated:

- `kappa_mu=0.35`, `p_star=0.35`;
- `A_ref=1.0`, interaction `kappa=4.5`;
- four equal focal patches at fixed total area;
- allele-frequency `migration_rate=0`;
- 30-generation deterioration ramp + 90-generation hold;
- normalized barrier increase `0.30`;
- five fresh master seeds × 20 replicates.

The same high-function source and the same trajectory seed are paired across every Phase-H condition.

## Explicit one-focal-node interaction network

The focal function has a six-partner candidate pool.

### Initial network

- partners `0–3`: active primary partners, edge strength `0.25` each;
- partners `4–5`: available latent partners, initial edge strength `0`;
- initial active partner count: `4`;
- initial total interaction effort: `1.0`.

Fixed trait-match scores are:

`(1.0, 0.9, 0.8, 0.7, 0.6, 0.5)`.

Every edge has fixed capacity `0.30`.

These values define a canonical prospective stress test. They are not empirical estimates and will not be tuned after observing outcomes.

## Partner loss

Both loss conditions remove the same primary partner:

`lost_primary_partner_index = replicate_index mod 4`.

Across every 20-replicate seed block, each primary partner is therefore lost exactly five times.

Partner loss happens at the start of the deterioration run. The lost edge remains unavailable thereafter.

## Rewiring rule

Three paired conditions are run:

1. `intact_control` — no partner loss;
2. `partner_loss_no_rewiring` — matched primary-partner loss, surviving edges unchanged;
3. `partner_loss_trait_capacity_rewiring` — the same loss followed by one fixed rewiring rule.

The rewiring rule attempts to reallocate exactly **50% of the lost edge effort**. Reallocation is distributed among surviving and latent available partners according to

`trait_match_score × spare_edge_capacity`,

with deterministic redistribution if an edge reaches its capacity.

Rewiring is gradual: generation 1 begins at the post-loss network, the target network is reached by generation 10, and that network is then held. This allows latent edges to activate and surviving edges to strengthen while the lost edge remains absent.

## Functional mapping

At each generation, network-mediated support is

`sum(edge_strength_j × trait_match_score_j)`.

It is normalized by the intact network's functional support and capped at `1.0`. That prospective multiplier scales only the existing local interaction-support signal during the deterioration run. Source reconstruction and the baseline state remain common across conditions.

The full edge vector, active-edge count, realized connectance and network-derived functional support remain explicit diagnostics; they are not silently equated with model `kappa`.

## Opening rule

A rewiring **rescue** interpretation is opened only if both fresh controls reproduce the required upstream states:

1. `intact_control` has sufficient high-rep support and is `R4_highrep`;
2. `partner_loss_no_rewiring` has sufficient high-rep support and is `R3_highrep`.

If either fails, Phase H records `not_opened`. Seeds, match scores, capacities, candidate partners, rewiring fraction, rewiring window and R4 thresholds remain unchanged.

## Rescue rule

If the opening rule is satisfied:

- rewiring `R4_highrep` → `rescued_to_R4`;
- rewiring in any other regime → `not_rescued`.

This rule is fixed before results are generated.

## Blinding

Condition classification may inspect only:

- source preparation/projection;
- explicit network condition and network diagnostics;
- baseline realised high-trait presence;
- realised functional-trait loss time/status.

Genetic diversity, genetic-warning time, lead/lag ordering and lead time remain unavailable.

## Stop rule

After the first complete classification, do **not** tune:

- trait-match scores;
- edge capacities;
- candidate partner pool;
- rewiring fraction;
- rewiring time window;
- lost-partner assignment;
- seeds;
- R4 thresholds.

A negative result closes this canonical rewiring rule; it does not justify searching rewiring parameters until R4 appears.

## Interpretation ceiling

Phase H is more explicit than Phase G because partner nodes, latent candidate edges, edge strengths, trait matching, capacities, partner loss and dynamic rewiring are represented directly.

It remains deliberately bounded. It does not model:

- partner population dynamics or partner extinction probability;
- multilayer/multi-focal ecological networks;
- endogenous coextinction;
- pollen or seed movement;
- demographic recolonisation;
- pollinator movement;
- adaptive evolution of rewiring.

A successful Phase-H rescue would therefore mean only that **this predeclared trait/capacity-constrained rewiring closure recovered event-regime estimability at the tested eco-genetic anchor**. It would not be a universal rewiring-rescue theorem.
