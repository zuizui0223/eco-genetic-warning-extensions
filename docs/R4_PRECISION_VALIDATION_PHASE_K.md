# Phase K — high-precision validation of the R4/R3 discrepancy

## Question

Phase J showed that the historical five-block all-in-band R4 screen is strongly finite-sample sensitive when each block contains only about 17–20 eligible trajectories. Phase H and Phase I therefore cannot be distinguished reliably by their R3/R4 labels alone.

Phase K asks:

> **Does the Phase-H versus Phase-I partner-loss regime discrepancy persist when the exact same ten historical master seeds are precision-expanded from 20 to 100 attempted replicates per block?**

## No seed selection

Phase K uses every master seed involved in the disagreement:

- Phase-H family: `20290710–20290714`;
- Phase-I family: `20290810–20290814`.

No new or replacement master seed is allowed.

## Conditions

For every prepared source, run only:

1. `intact_control` — effective interaction support multiplier `1.0`;
2. `partner_loss_no_rescue` — the **exact Phase-H/Phase-I one-primary-partner-loss closure**. Losing primary partner `replicate_index mod 4` produces one of four trait-match-weighted support multipliers (approximately 0.706, 0.735, 0.765, 0.794). Because partner identity is balanced across each 20-replicate cycle, their mean is exactly 0.75, but the trajectory-level multiplier is not replaced by that mean.

The two conditions use the same prepared source and trajectory seed. Genetic warning/diversity fields are unavailable to the precision decision.

## Prefix provenance audit

The parent seed derivation is deterministic in `(master_seed, cell_index, replicate_index)`. Increasing the requested replicate count therefore preserves the first 20 derived replicate seeds. Before interpreting the expanded blocks, Phase K requires the first 20 attempted replicates for every master seed and both conditions to reproduce the locked historical eligible/loss counts exactly.

Any prefix mismatch is an implementation/provenance failure and stops interpretation.

### Prefix-detected implementation correction

The first Phase-K execution failed this audit. Diagnosis showed that the runner had simplified the historical partner-loss closure to a constant support multiplier `0.75`. That was not the Phase-H/Phase-I condition: `0.75` is only the balanced mean of four replicate-specific trait-match-weighted post-loss multipliers.

The correction restores the exact historical `support_multiplier(post_loss_edges(replicate_index))` closure. **No scientific design choice changed:** the ten master seeds, 100-replicate precision target, partner-loss identity rule, deterioration schedule, historical R4 band and decision rule are unchanged. A new contract test now requires all four historical support levels and their balanced mean, preventing recurrence of this implementation error.

The rejected first execution remains provenance evidence and is not interpreted scientifically.

## Precision target

Each master-seed block is expanded to `100` attempted replicates and must retain at least `70` baseline-eligible trajectories. The historical R4 band `[0.30,0.70]` is unchanged.

This is sufficient to make sampling-only five-block gate failure much less likely for latent rates near the observed 0.43–0.49 range than at the historical 17–20 eligible trajectories per block. Phase K does not alter the gate to obtain agreement.

## Primary decision

Apply the historical five-block R1–R4 classifier separately to the full-precision Phase-H seed family and Phase-I seed family for `partner_loss_no_rescue`.

- same regime in both families → `precision_convergence:<regime>`;
- different regimes → `between_ensemble_instability_persists`;
- fewer than 70 eligible in any partner-loss block → `insufficient_precision`;
- any historical prefix mismatch → `prefix_reproducibility_failed`.

The intact condition is a paired reference and is reported with the same precision diagnostics.

## Secondary diagnostics

For each five-block seed family and condition, report:

- full block loss counts/rates;
- pooled loss rate;
- historical gate regime;
- Pearson equal-rate diagnostic across the five high-precision blocks;
- homogeneous-reference probability that the historical gate passes/fails at the observed full block sizes and pooled rate.

These do not replace the historical classifier; they diagnose why it passes or fails.

## Interpretation

If both partner-loss seed families converge to R4 at high precision, the Phase-H R3 call is best treated as a finite-sample gate failure rather than demonstrated biological seed heterogeneity.

If the two families remain R3 versus R4 with precise block estimates, a genuine between-master-seed-family dependence of the event-generating process remains plausible and must be modelled explicitly before warning estimability is claimed portable.

If both converge to R3, the Phase-I R4 pass was finite-sample unstable instead.

## Stop rule

After the prefix-detected implementation correction, run all ten locked master seeds once at 100 attempted replicates per block. Do not add replacement seeds, alter the historical `[0.30,0.70]` band, or increase the replicate count again merely to obtain agreement.
