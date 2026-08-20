# Warning-blind recurrent-transition frontier refinement protocol

## Status

Prospectively declared after completion of the locked Protocol 002 campaign and the warning-blind secondary condition-map analysis. This protocol is **condition discovery**, not warning validation. Genetic-diversity and warning fields remain unavailable throughout refinement and confirmation.

Evidence used to choose the refinement region:

- locked Protocol 002 Stage II: 810 batches / 20,250 attempts;
- warning-blind condition-map run `32346697621`, artifact `9398407271`, digest `sha256:5d61e71f6febf1c65304716958b329b329612359f1d170b4747532a124b5a8a2`;
- coordinate regime artifact run `29399936061`, artifact `8336631530`;
- exact local support-frontier theorem in `RECURRENT_TRANSITION_SUPPORT_FRONTIER.md`.

No warning or diversity outcome was used to choose the grid below.

## Question

Does a reproducible intermediate-risk functional-loss regime exist in the narrow warning-blind frontier between the rapid-loss and persistence regimes already identified by Protocol 002?

## Regime classification

The same strict event-risk definition is retained for condition discovery:

- `R1 persistence`: every seed-block trait-loss rate < 0.30;
- `R2 rapid-loss`: every seed-block trait-loss rate > 0.70;
- `R3 seed-heterogeneous`: seed blocks cross those categories or the strict band;
- `R4 warning-evaluable`: every seed-block trait-loss rate lies in `[0.30,0.70]`.

`R0 source-infeasible` is recorded before deterioration if source preparation/projection does not support the candidate.

R4 here means only **event-regime evaluability**. It is not evidence that a genetic warning succeeds.

## Why the search is staged

The existing grid shows a rapid-to-persistence frontier that moves to lower `p_star` as `kappa_mu` increases. Candidate-level matched reanalysis shows that increasing `p_star` or `kappa_mu` never increased pooled trait-loss rate among matched complete candidates in the completed grid. Barrier magnitude had weak mixed effects, while longer horizon increased or left unchanged observed loss.

The closest strict-gate candidates concentrate at `kappa_mu=0.05, p_star=0.90, horizon=120`; two candidates missed R4 by only one seed block and a maximum band distance of 0.05. Therefore refinement begins there rather than expanding the whole parameter space.

## Phase A — primary fine frontier at kappa_mu = 0.05

Keep `kappa_mu=0.05` fixed and refine only `p_star` inside the observed `0.75–0.90` rapid-to-heterogeneous interval.

New interior `p_star` values:

`0.775, 0.800, 0.825, 0.850, 0.875`

The existing `0.75` and `0.90` cells remain historical anchors and are not counted as new evidence unless replayed with the new seed family.

Use two predeclared non-transition anchor settings because both were among the closest warning-blind candidates:

- **A1:** `A_ref=0.8`, interaction `kappa=4.5`, ramp 30, hold 90, horizon 120, normalized barrier increase 0.45;
- **A2:** `A_ref=0.8`, interaction `kappa=3.0`, ramp 30, hold 90, horizon 120, normalized barrier increase 0.15.

For every new `p_star`, reconstruct the high-function source independently under the same recurrent-transition coordinate before deterioration. Do not reuse a source prepared at another `p_star`.

### Phase-A decision

- If at least two adjacent `p_star` values under the **same anchor** independently confirm R4, freeze that contiguous R4 interval as the candidate matched warning domain for a later H-MD-3b protocol.
- If exactly one value confirms R4, perform one additional warning-blind local refinement around that value before warning endpoints are released.
- If no value confirms R4 but the frontier remains ordered R2 -> R3 -> R1, record the width and seed heterogeneity of the transition boundary and proceed to Phase B only if scientifically useful.

## Phase B — secondary frontier rows, conditional on Phase A

Phase B is not run merely because a warning comparison is desired. It is run only if Phase A fails to recover a contiguous R4 region or if comparison of frontier geometry across transition strengths remains a primary scientific question.

Candidate refinement intervals from the locked coordinate map:

- `kappa_mu=0.20`: refine within `p_star=0.25–0.75`, centred on the existing heterogeneous `0.50` row;
- `kappa_mu=0.35`: refine within `p_star=0.25–0.50`, where the coarse grid jumps from rapid loss to persistence.

Exact Phase-B interior values and non-transition anchors must be declared after Phase-A trait-loss-only results, still without warning/diversity inspection.

## Seed discipline

Use seed families not used in Protocol 002 calibration, Protocol 003 calibration/confirmation/validation, or the parent H2 validation.

For refinement, use five master seeds with at least five replicates per seed. If a candidate is provisionally R4, confirm it with a fresh five-seed family and increased replication before freezing any warning-validation domain.

Seed values must be recorded in the implementation manifest before execution. They must not be changed in response to observed warning/diversity values.

## Variables permitted during refinement

Permitted:

- source support/preparation/projection status;
- baseline realised high-trait presence;
- realised functional-trait-loss occurrence/time;
- seed-block trait-loss rate;
- candidate completeness and R0-R4 event-regime classification.

Forbidden:

- `H_alpha`, `H_gamma`, heterozygosity or any diversity summary;
- warning threshold/value/time;
- lead, lag, tie or lead time;
- event-pair classification involving a warning endpoint.

## Theoretical prediction declared before execution

The local support frontier for a pre-transition allele frequency `p` and local threshold `p_c` is

`p_star_crit = p + (p_c-p)/kappa_mu`.

When `p < p_c`, stronger `kappa_mu` lowers the `p_star` required to meet the same local high-associated threshold. This predicts the **direction** of the finite frontier shift observed in Protocol 002, but not its numerical location or full loss-regime outcome.

## Interpretation boundaries

A recovered R4 region would establish that the previous 15/15 no-domain result reflected coarse/common-family placement rather than structural impossibility. It would then permit a prospectively matched H-MD-3b warning test with non-direction parameters fixed.

Failure to recover R4 after fine warning-blind refinement would not prove that no evaluable domain exists anywhere. It would strengthen the finite conclusion that the rapid-to-persistence boundary is narrow and/or seed-heterogeneous under the declared closure.
