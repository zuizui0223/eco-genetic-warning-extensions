# Phase W — matched recurrent-transition direction identifiability audit

## Question

After Phase V met its original event-pair ordering rule inside the frozen symmetric H2-R domain, can the existing warning-blind evidence support a **direction-only** warning comparison in which ecological parameters, deterioration schedule and recurrent-transition strength are all held fixed?

**Post-review note:** the later full-denominator audit found that all relative thresholds also fired in every non-event trajectory in both frozen ensembles. Phase V therefore retains event-conditional ordering but no longer supports predictive warning validity.

Phase W adds no simulation and inspects no warning outcome. It reuses immutable Protocol 002 Stage II trait-loss-only batches from workflow run `29192711417`.

## Exact common context

The Phase-V symmetric H2-R domain corresponds to the affine recurrent-transition coordinate `kappa_mu=0.20, p_star=0.50`. The matched Stage II cell fixes:

- `A_ref=0.8`;
- interaction feedback `kappa=6.0`;
- equal-isolated projection;
- ramp 30 generations;
- hold 90 generations;
- horizon 120;
- normalized barrier increase `0.15`.

To isolate transition **direction**, Phase W keeps `kappa_mu=0.20` fixed and examines only the already predeclared `p_star` grid `.10/.25/.50/.75/.90` under that exact common context.

## Locked warning-blind evidence

| `p_star` | batch | eligible | loss | pooled loss | five seed-block rates |
|---:|---:|---:|---:|---:|---|
| .10 | 282 | 22 | 22 | **1.000** | 1, 1, 1, 1, 1 |
| .25 | 336 | 17 | 17 | **1.000** | 1, 1, 1, 1, 1 |
| .50 | 390 | 20 | 8 | **0.400** | .60, .667, 0, .60, 0 |
| .75 | 444 | 21 | 0 | **0.000** | 0, 0, 0, 0, 0 |
| .90 | 498 | 22 | 0 | **0.000** | 0, 0, 0, 0, 0 |

The old intermediate-loss target band is `[0.30,0.70]`. Only the symmetric `.50` cell lies inside it.

For the four directional cells the pooled observations are boundary-extreme. Under a standard two-sided 95% Clopper–Pearson reference for those boundary cases, the all-loss cells have lower bounds `.846` and `.805`, while the no-loss cells have upper bounds `.161` and `.154`. This reference is descriptive only; it does not assume simulator trajectories are literally iid Bernoulli.

## Why the Protocol 003 directional domain does not solve identification

An exact ecology/schedule cell at `kappa_mu=.05, p_star=.90` (Stage II batch `228`) had pooled loss `10/21=.476`, close to the symmetric cell. But it changes **both** `p_star` and `kappa_mu`.

Thus matching the loss process is possible only after changing recurrent-transition strength as well as direction. That is useful portability evidence, but it is not a single-factor direction experiment.

## Decision

**`direction_only_warning_comparison_not_identifiable_under_frozen_common_schedule`**

The predeclared same-strength directional grid does not contain a matched intermediate-loss comparator. A warning comparison cannot therefore be opened while simultaneously holding:

1. ecology fixed;
2. deterioration schedule fixed;
3. `kappa_mu` fixed;
4. downstream loss process in the same intermediate-incidence region.

## Scientific consequence

Phase V establishes **within-domain replication** of baseline-relative genetic warning. Phase W explains why the unresolved direction-only question should remain unresolved rather than be forced by retuning.

Changing to finer `p_star` values would be a new outcome-guided refinement after observing the sharp incidence split. Changing `kappa_mu`, `A_ref`, interaction `kappa`, horizon or deterioration magnitude would destroy the intended single-factor identification. Neither path is opened in the present programme.

Therefore the strongest current C4 statement is:

> event-conditional warning ordering replicated within the frozen symmetric domain but lacked non-event discrimination; cross-domain portability remains bounded and the isolated causal effect of recurrent-transition direction is not identifiable under the predeclared matched schedule because direction changes the loss-generating process itself.

## Provenance

The five same-strength cells are immutable Stage II artifacts from run `29192711417`:

- batch 282 — artifact `8260028479`, digest `sha256:a88a1c5614054263ad08290acadb671977ae1d66e428c2c2dcc9936c5d21a0a9`;
- batch 336 — artifact `8260079020`, digest `sha256:07201c3e7704b60eb85961390ab9641267279f520574b67b619237606578e2e9`;
- batch 390 — artifact `8260125567`, digest `sha256:4b842a4ccc113309623c87d1c2228dfa9abc36d93d4598b28c4bc72fc984a42e`;
- batch 444 — artifact `8260180102`, digest `sha256:df96e9d5951b1f9a03afed3efbf9a86f973d2ec62cbe041d221cada341020d5b`;
- batch 498 — artifact `8260233506`, digest `sha256:fc8b53ef8a24038d6f728655d2bec20bd5acbd01812c6439ae08e07a7c23fd83`.

Cross-strength identification counterexample: batch 228, artifact `8260226534`, digest `sha256:3e1795a43f0afb5bc528be62513f40860950f2ba6d58ab4eaff4a52f0f97662b`.

## Stop rule

Phase W is closed as a deterministic audit. Do not add finer `p_star`, retune deterioration/ecology, change `kappa_mu`, or inspect warning outcomes merely to manufacture a matched direction-only comparison.
