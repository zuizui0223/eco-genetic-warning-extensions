# Explicit rewiring result: network recovery did not restore loss-regime estimability

## Result

Phase H completed under the prospectively fixed warning-blind design.

The opening rule was satisfied:

- fresh `intact_control` reproduced `R4_highrep`;
- fresh matched `partner_loss_no_rewiring` reproduced `R3_highrep`.

The predeclared trait- and capacity-constrained rewiring condition remained `R3_highrep`. The prospective rescue classification is therefore:

> **`not_rescued`**

No rewiring parameter, seed, partner score, capacity, loss identity, time window or R4 threshold was changed after observing the result.

## Condition results

| condition | eligible | trait loss | pooled loss | seed-block rates | regime |
|---|---:|---:|---:|---|---|
| intact control | 86/100 | 37 | 0.430 | 0.500, 0.471, 0.412, 0.353, 0.412 | R4-highrep |
| partner loss, no rewiring | 86/100 | 37 | 0.430 | 0.500, 0.471, 0.529, 0.353, 0.294 | R3-highrep |
| partner loss + constrained rewiring | 86/100 | 36 | 0.419 | 0.500, 0.471, 0.471, 0.353, 0.294 | R3-highrep |

The no-rewiring R3 classification is caused by the final seed block falling just below the R4 lower bound (`0.294 < 0.30`). Constrained rewiring changed one loss trajectory to no loss but left that same seed block below the bound, so the regime remained R3.

## Network recovery was real

The negative rescue result is not because the rewiring operator failed to change the network.

| network diagnostic | no rewiring | constrained rewiring |
|---|---:|---:|
| final active edges | 3 | 5 |
| final realised connectance | 0.500 | 0.833 |
| latent edges activated | 0 | 2 |
| final rewired edge effort | 0 | 0.125 |
| mean final support multiplier | 0.750 | 0.844 |
| mean support multiplier through time | 0.750 | 0.840 |

Thus the fixed rewiring rule substantially recovered network connectivity and match-weighted interaction support, but did **not** recover the predeclared functional-loss regime.

## Paired trajectories

Relative to the intact control, matched partner loss without rewiring produced bidirectional switching:

- 16 loss → no loss;
- 16 no loss → loss;
- 21 remained loss;
- 33 remained no loss;
- 86 comparable pairs.

Relative to partner loss without rewiring, constrained rewiring changed only one comparable trajectory:

- 1 loss → no loss;
- 0 no loss → loss;
- 36 remained loss;
- 49 remained no loss;
- 86 comparable pairs.

The pooled loss rate therefore changed only from `0.430` to `0.419`.

## Scientific conclusion

The strongest bounded conclusion is:

> **Recovering interaction-network structure and aggregate match-weighted support is not sufficient to recover functional-loss regime reproducibility.**

In this closure, network recovery and functional-regime recovery are distinct state transitions. The result strengthens the earlier distinction among:

1. structural/network state;
2. realised functional-loss incidence;
3. reproducibility of the loss-generating process;
4. downstream warning estimability.

A network can look more connected and recover more interaction support while the downstream event process remains non-evaluable under the predeclared R4 rule.

This result also argues against using connectance or aggregate interaction support as stand-alone proxies for ecological-function resilience.

## What was not shown

Do not infer that:

- rewiring is generally ineffective;
- stronger rewiring could never restore R4;
- all forms of topological rewiring are equivalent to this rule;
- connectance is ecologically irrelevant;
- the `0.30–0.70` R4 band is a universal ecological threshold;
- biological partner movement or partner population recovery has been tested.

The fixed Phase-H rule is one canonical prospective closure. Per the stop rule, its failure does not authorize parameter tuning until rescue appears.

## Provenance

- stacked PR: `#62`
- workflow run: `32453377127`
- workflow artifact: `9436467391`
- artifact digest: `sha256:3b26257527e6c1c22fa33cbcdf19ddf7d381c3df55c857f2c6f2f8f1acc50a85`
- preregistered head: `611cf4e884e7d125465bf0fd16884d95424bd389`
- parent scientific commit: `dd8ee379d0d3518194c767d16402042525bc00dc`
- committed compact evidence: `artifacts/explicit_rewiring/phase_h_summary.json`

## Stop decision

**Phase H is closed.** Do not vary rewiring fraction, time window, partner match scores, capacities, latent-partner pool or loss assignment merely to obtain `rescued_to_R4`.

The next genuinely distinct unresolved mechanism is **process-resolved biological movement** (pollen, seed/propagule, demographic or partner movement), or a later independently motivated network model with endogenous partner dynamics. Neither should be represented by retuning the completed Phase-H closure.
