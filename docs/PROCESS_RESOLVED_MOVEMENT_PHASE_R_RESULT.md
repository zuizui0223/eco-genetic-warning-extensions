# Phase R result — process-resolved movement does not reproduce legacy m=.10 heterogeneity

## Opening gate

All preregistered opening checks passed:

- zero dispersal exactly reproduced the pinned parent finite-bin life cycle;
- every historical first-20 Phase-E prefix for no connectivity and allele-only `m=.10` reproduced;
- the five full 100-attempt Phase-M block counts reproduced exactly for both legacy comparator conditions;
- process-resolved movement and no connectivity had identical paired baseline eligibility.

The scientific run is therefore interpretable.

## High-precision result

| condition | pooled loss | historical screen | equal-rate p |
|---|---:|---|---:|
| no connectivity | 0.559 | R4 | 0.710 |
| allele-only `m=.10` | 0.557 | R3 | **0.0205** |
| whole-individual dispersal `d=.10` | 0.606 | R4 | **0.811** |

The process-resolved `d=.10` blocks were `49/88`, `57/89`, `57/93`, `54/86`, `54/91`. They show no detectable excess between-block heterogeneity.

The realised movement operator was active: mean realised mover fraction was `0.0923`, with a mean `568.3` realised movement events per trajectory across the 120-generation schedule.

## Paired marginal comparisons

Whole-individual dispersal versus no connectivity, among 447 comparable paired trajectories:

- loss → no loss: 83;
- no loss → loss: 104;
- exact McNemar `p=0.143`.

Whole-individual dispersal versus allele-only `m=.10`:

- loss → no loss: 86;
- no loss → loss: 108;
- exact McNemar `p=0.131`.

Thus the higher point estimate under process movement (`0.606`) is **not a detected directional marginal-risk effect** under the preregistered paired test.

## Scientific conclusion

> **The Phase-M `m=.10` block-heterogeneity result does not port to the first preregistered process-resolved whole-individual dispersal closure.**

This strengthens the operator boundary around connectivity. The legacy scalar `migration_rate` cannot stand in for biological movement in general. Allele-frequency mixing and whole-individual dispersal can generate different stochastic structures even when compared at the same nominal rate value and the same source/seed ensemble.

The result also sharpens the current four-estimand framework:

- loss incidence can be similar or moderately shifted without a significant paired marginal effect;
- trajectory identities can switch in both directions;
- between-block heterogeneity can differ between connectivity operators;
- genetic-warning performance remains a separate downstream question.

## Boundary

`d=.10` and `m=.10` are not calibrated to equivalent realised gene flow. Phase R tests operator portability at one fixed nominal stress level; it does not rank movement mechanisms or identify a movement threshold.

The parent state does not contain joint genotype×trait identities. Phase R therefore moves realised trait-bin individuals exactly and source genetic composition in expectation, but does not preserve migrant genotype–trait covariance.

This is whole-individual post-recruitment dispersal, not pollen-only, seed-only, pollinator or partner movement.

## Stop rule applied

Phase R is closed after this result. No additional `d`, destination kernels, replacement seeds, changed screen bands or higher precision are opened merely to reproduce the legacy `m=.10` heterogeneity.

## Provenance

- workflow run `32613357637`;
- scientific head `9ecde4cb1527709bc92e26a5a617b845cf07dbb4`;
- aggregate artifact `9486225034`;
- digest `sha256:13474765636fe839f4953a94618cfdf1dc7bd145f029ae97df26ced32443c143`;
- compact locked result: `artifacts/process_resolved_movement/phase_r_locked_summary.json`.
