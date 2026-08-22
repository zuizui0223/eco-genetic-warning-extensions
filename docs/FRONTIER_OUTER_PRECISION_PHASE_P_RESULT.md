# Phase P result — high-precision Phase-C .35/.40 replay

The corrected Phase-P execution used the actual historical Phase-C master seeds `20290210–20290214`. All ten first-20 seed×`p_star` prefixes reproduced the locked Phase-C eligible/loss counts before high-precision interpretation.

## High-precision result

- `p_star=0.35`: pooled loss `0.5381`; historical screen `R4_highrep`; equal-rate diagnostic `p=0.2524`.
- `p_star=0.40`: pooled loss `0.2725`; historical screen `R3_highrep`; equal-rate diagnostic `p=0.1508`.

At `p_star=0.40`, the five block rates were `0.219, 0.376, 0.272, 0.233, 0.272`. The historical R3 label therefore persists because this condition lies mainly on the **low-incidence side** of the fixed `[0.30,0.70]` screen, not because the high-precision blocks show detectable excess heterogeneity.

Combined with Phase O (`p_star=.325/.350/.375`), the local recurrent-turnover map is an incidence frontier: loss is high at `.325`, intermediate at `.350–.375`, and low by `.400`. The old description of a narrow R4 region bounded by biological seed heterogeneity is withdrawn.

Scientific run: `32562175464`. The result was deterministically aggregated from all five completed seed artifacts using the committed Phase-P aggregate logic while the identical GitHub aggregate job was waiting for a runner; the five artifact IDs and digests are locked in `artifacts/frontier_outer_precision/phase_p_locked_summary.json`.
