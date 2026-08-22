# Phase K result — the conflicting partner-loss seed families converge to R4 at high precision

## Decision

**Phase K passes the provenance prefix gate and returns `precision_convergence:R4_highrep`.**

The same ten historical master seeds that produced the Phase-H R3 / Phase-I R4 disagreement were expanded from 20 to 100 attempted replicates per block. No replacement seeds were selected and the historical `[0.30,0.70]` R4 band was unchanged.

## Implementation correction caught by the prefix gate

The first Phase-K execution was rejected because the partner-loss support was incorrectly simplified to constant `0.75`. Historical Phase H/I instead used four replicate-specific trait-match-weighted post-loss support levels, balanced to mean 0.75. The prefix audit detected this mismatch.

The corrected runner restored the exact historical `support_multiplier(post_loss_edges(replicate_index))` closure. Seeds, partner-loss identity, deterioration, precision target, R4 band and decision rule were unchanged. A contract test now locks the four support levels.

## Provenance

- corrected workflow run: `32557289628`
- corrected head: `ec15cdb9640727993a7991f7e9ef6dbad9cc5023`
- summary artifact: `9471883061`
- artifact digest: `sha256:6d198c819033c4931fc2ac7dca763b670c94dc12c5447116cf7940d274b70dcb`
- parent scientific commit: `dd8ee379d0d3518194c767d16402042525bc00dc`
- locked compact summary: `artifacts/r4_precision/phase_k_locked_summary.json`

## Prefix audit

**Passed for all ten master seeds and both conditions.** The first 20 attempted replicates exactly reproduce the locked Phase-H / Phase-I eligible and loss counts, so the 100-replicate extensions are valid precision continuations of the historical conditions.

## Phase-H seed family at 100-attempt precision

### Intact

| master seed | loss / eligible | rate |
|---:|---:|---:|
| 20290710 | 50/86 | 0.581 |
| 20290711 | 51/86 | 0.593 |
| 20290712 | 44/85 | 0.518 |
| 20290713 | 45/87 | 0.517 |
| 20290714 | 40/85 | 0.471 |

Pooled loss = `0.536`; historical full-precision regime = **R4-highrep**. Equal-rate diagnostic `p=0.472`.

### Partner loss / no rescue

| master seed | loss / eligible | rate |
|---:|---:|---:|
| 20290710 | 47/86 | 0.547 |
| 20290711 | 44/86 | 0.512 |
| 20290712 | 46/85 | 0.541 |
| 20290713 | 43/87 | 0.494 |
| 20290714 | 47/85 | 0.553 |

Pooled loss = `0.529`; full-precision regime = **R4-highrep**. Equal-rate diagnostic `p=0.928`. Under the homogeneous finite-sample reference at these exact block sizes and pooled rate, historical gate failure probability is only `0.00319`.

## Phase-I seed family at 100-attempt precision

### Intact

Block rates: `0.548, 0.576, 0.581, 0.511, 0.565`; pooled `0.557`; **R4-highrep**; equal-rate `p=0.883`.

### Partner loss / no rescue

Block rates: `0.505, 0.533, 0.581, 0.544, 0.609`; pooled `0.554`; **R4-highrep**; equal-rate `p=0.649`. Homogeneous-reference gate failure probability `0.00869`.

## Scientific conclusion

The Phase-H R3 classification does **not** reproduce when the exact same master-seed family is measured with substantially greater within-block precision. It is therefore best interpreted as a finite-sample failure of the historical hard all-five-block gate, not demonstrated biological seed heterogeneity.

The Phase-I fresh ensemble had already returned R4 at low precision; at high precision both formerly conflicting seed families converge to R4 and show no detectable excess block-rate heterogeneity.

This directly confirms the Phase-J diagnosis.

## Consequence for earlier claims

The historical R3 label remains immutable provenance. However, any manuscript statement that equates a small-block R3 classification with a biological change in loss-regime reproducibility must now be re-audited.

At minimum this applies to:

- Phase E migration `m=0.10/0.20` R3 claims;
- Phase G one-partner-loss R3 claims;
- Phase H rewiring/non-rewiring R3 claims;
- Phase C/D statements that infer a narrow R4 frontier from neighbouring R3 labels.

These results may still encode real changes in pooled loss probability or event-generation, but the historical R3 label alone is no longer sufficient evidence.

## Stop rule

Do not extend Phase K further. The ten locked seeds have converged at the preregistered high precision. The next step is a cross-campaign validity audit of all headline R3 claims, followed only where needed by prospectively declared precision validation.
