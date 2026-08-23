# Phase S result — pollen-only gene flow does not reproduce legacy m=.10 heterogeneity

## Opening gate

All preregistered opening checks passed:

- `g=0` exactly reproduced the pinned parent finite-bin life cycle;
- every original first-20 Phase-E prefix for no connectivity and allele-only `m=.10` reproduced;
- all five full 100-attempt Phase-M block counts reproduced exactly for both legacy comparator conditions;
- pollen flow left paired baseline eligibility identical to no connectivity.

The scientific run is therefore interpretable.

## High-precision result

| condition | pooled loss | historical screen | equal-rate p |
|---|---:|---|---:|
| no connectivity | 0.559 | R4 | 0.710 |
| allele-only `m=.10` | 0.557 | R3 | **0.0205** |
| pollen-only `g=.20` | 0.532 | R4 | **0.728** |

The pollen-only blocks were `46/88`, `45/89`, `53/93`, `42/86`, `52/91`. They show no detectable excess between-block heterogeneity.

The pollen operator was active: mean realised external-pollen fraction was `0.19985`, with a mean `1266.3` external paternal contributions per trajectory over the 120-generation schedule.

## Paired marginal comparisons

Pollen-only gene flow versus no connectivity, among 447 comparable paired trajectories:

- loss → no loss: 65;
- no loss → loss: 53;
- exact McNemar `p=0.311`.

Pollen-only gene flow versus allele-only `m=.10`:

- loss → no loss: 46;
- no loss → loss: 35;
- exact McNemar `p=0.266`.

Thus pollen flow did not produce a detected directional marginal-risk effect relative to either comparator.

## Scientific conclusion

> **The Phase-M `m=.10` block-heterogeneity result does not port to the preregistered pollen-only paternal-gamete gene-flow closure.**

Combined with Phase R, which found no such heterogeneity under whole-individual dispersal, the legacy result is now bounded more strongly: the observed `m=.10` block dependence is not a generic connectivity effect across the tested demographic/trait and gametic movement representations.

This does **not** prove that all realistic gene flow is homogeneous. It shows that the smooth direct post-selection allele-frequency mixing operator cannot be silently relabelled as biological dispersal or pollen flow.

## Why `g=.20` was used

The Phase-S closure is biparental. Maternal and paternal gamete pools each contribute half of expected zygotic allele frequency. A 20% external-pollen fraction therefore contributes at most about 10% external genomic ancestry before donor weighting, providing a mechanistically derived nominal comparison with legacy `m=.10`.

No calibrated equivalence is claimed.

## Representation boundary

The parent does not explicitly represent flowers, mating pairs, pollen limitation, selfing, incompatibility, pollen carryover, pollinator behaviour or genotype×trait identities. Phase S is a finite paternal-gamete-origin closure, not a complete plant mating system and not pollinator movement.

## Stop rule applied

Phase S is closed. No additional pollen fraction, donor kernel, selfing parameter, replacement seed or higher precision is opened merely to reproduce or eliminate the legacy `m=.10` heterogeneity.

## Provenance

- workflow run `32613877695`;
- scientific head `d863971693c1149d572497c3831ed9f91f3e0fa7`;
- aggregate artifact `9486401100`;
- digest `sha256:a320527fbb737209c23cbf3376172f15c189e6c76125c69e90f135a74f70bc04`;
- compact locked result: `artifacts/process_resolved_pollen/phase_s_locked_summary.json`.
