# Phase P — high-precision validation of the Phase-C .35/.40 frontier contrast

Phase L showed that the historical `p_star=.40` R3 label is highly compatible with finite-sample hard-gate failure at its original block sizes. Phase P precision-expands the exact Phase-C design.

## Fixed design

- actual locked Phase-C master seeds `20290210–20290214` only;
- `p_star=.35` and `.40` only;
- independent source reconstruction for each `p_star` exactly as Phase C;
- 100 attempted replicates per seed×`p_star`;
- historical `[0.30,0.70]` five-block gate unchanged;
- no warning/diversity outcomes used.

## Provenance correction

The first workflow attempt mistakenly supplied `20290320–20290324`. The runner rejected those values before simulation because they are not the master seeds declared by Phase C. No scientific result or aggregate was generated. The workflow matrix, prefix registry and tests were corrected to the actual Phase-C seeds before the high-precision scientific execution.

## Prefix gate

All ten seed×`p_star` first-20 eligible/loss prefixes must exactly reproduce the locked Phase-C counts before interpretation.

## Primary decision

- `.35` remains R4 and `.40` remains outside R4 at high precision → a bounded outer frontier difference remains;
- both are R4 → withdraw the historical `.40` R3 boundary claim;
- `.35` leaves R4 → the original anchor is not stable under the new precision and the frontier must be reframed from the full high-precision map.

## Stop rule

No replacement seeds, additional `p_star` points, altered R4 band or further precision escalation merely to preserve the historical `.40` R3 label.
