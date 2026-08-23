# Fresh connectivity replication Phase U — locked result

## Decision

**`historical_m010_heterogeneity_not_freshly_replicated`**

The only surviving high-precision Phase-M connectivity heterogeneity observation, legacy allele-frequency mixing `m=.10`, did **not** reproduce in the one preregistered independent fresh-seed ensemble.

## Opening gate

All opening requirements passed:

- fresh master seeds `20291010–20291014`;
- 100 attempted replicates per seed;
- every block had at least 70 baseline-eligible trajectories in both conditions;
- paired baseline eligibility was identical between `m=0` and `m=.10`;
- neither condition was required to pass the historical R4 screen before interpretation.

## High-precision fresh result

| condition | pooled loss | block rates | historical screen | equal-rate p |
|---|---:|---|---|---:|
| `m=0` | 0.5398 | .539, .442, .593, .505, .618 | R4 | .134 |
| allele-only `m=.10` | 0.5509 | .517, .581, .549, .515, .596 | R4 | .745 |

The preregistered replication criterion required `m=.10 p<.05` while `m=0 p>=.05`. Instead, both conditions were compatible with common block rates and `m=.10` was especially homogeneous in the fresh ensemble.

## Paired marginal effect

Across 452 comparable trajectories:

- loss→no-loss: 49;
- no-loss→loss: 54;
- same loss: 195;
- same no loss: 154;
- exact McNemar `p=.694`.

Thus the fresh ensemble also provides no directional marginal-risk difference between `m=0` and `m=.10`.

## Scientific correction

The historical Phase-M observation remains valid for its original seed family: `m=.10` had equal-rate `p=.0205` there. But the independent Phase-U ensemble gives equal-rate `p=.745` at the same model anchor, migration level, deterioration schedule, and precision.

Therefore the manuscript must **not** describe `m=.10` heterogeneity as independently reproducible or as an established parameter-specific connectivity effect. The defensible statement is:

> One historical high-precision seed family showed excess between-block heterogeneity at allele-only `m=.10`, but this observation did not reproduce in one preregistered independent fresh-seed ensemble. Across both ensembles, pooled loss remained near the same intermediate range and paired marginal-risk contrasts were null.

Combined with Phases R and S, the stronger boundary is now that the historical heterogeneity observation is both **seed-family contingent** and **operator-specific** within the tested closures. It cannot support a generic biological-connectivity mechanism.

## Provenance

- workflow run: `32615044162`;
- scientific head: `d9c5c7852f86d78572d42b98f42c0c307fae3e2d`;
- aggregate artifact: `9486740313`;
- artifact digest: `sha256:f561cb23d8040469db673acbdb329ec0e89bcefef30572dfb63bc8c829801756`;
- locked summary: `artifacts/fresh_connectivity_replication/phase_u_locked_summary.json`.

## Stop rule

Phase U is closed. Do not replace seeds, add migration levels, rerun fresh ensembles, change alpha or the historical screen, or increase precision after this result merely to recover significance.
