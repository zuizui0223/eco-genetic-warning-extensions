# Inherited H3 paired effect-size summary

## Status

This is a manuscript-facing descriptive summary of the already completed parent H1/H3 campaign. It does not rerun the parent model or alter the closed evidence ledger.

Source:

- repository: `zuizui0223/eco-genetic-criticality`;
- canonical H1/H3 workflow run: `28456092898`;
- artifact: `7987193632` (`mutation-primary-h1-h2-h3-seeds-20260810-20260814`);
- artifact digest: `sha256:b74b604f3233fa6086e2afa39cd780fa375aac4b1abd8c63e6f5ed8b3a467d2c`.

The source artifact contains 12 predeclared primary cells with 100 attempted seed-replicates each. Across those cells, 1,055 replicates satisfied the H1 full-state hold criterion. The parent artifact reports `h3_fragmentation_pattern_supported_probability = 1.0` in every primary cell.

## Descriptive effect sizes

For every H1-qualified replicate, the one-large and equal-isolated outcomes were already stored in the locked parent artifact. The manuscript summary uses paired final-state values:

- interaction: mean of `final_q_by_patch`;
- local effective size: mean of `final_effective_size_by_patch`;
- realised high-trait mass: `realised_high_trait_mass_mean`.

For each metric, the paired fractional reduction is

\[
1-\frac{\text{equal isolated}}{\text{one large}}.
\]

Across the 1,055 H1-qualified replicates:

| Metric | one-large mean | equal-isolated mean | median paired reduction | IQR of paired reduction |
|---|---:|---:|---:|---:|
| final interaction | 0.997729 | 0.004815 | 99.86% | 99.28–99.98% |
| final local effective size | 72.828 | 8.182 | 88.73% | 88.52–88.93% |
| realised high-trait mass | 0.575312 | 0.177313 | 68.87% | 59.90–78.50% |

The machine-readable summary is `manuscript/tables/inherited_h3_effect_summary.csv`.

## Interpretation boundary

These are pooled descriptive effect sizes across the 12 already selected parent primary cells. They are not new model runs, a universal fragmentation effect size, or a population-level estimate.

They are used only to prevent the manuscript's first Results section from presenting a qualitative fragmentation claim without a denominator or magnitude.
