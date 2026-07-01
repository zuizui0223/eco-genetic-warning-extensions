# Mathematical design — Protocol 001

## Boundary

This repository changes one biological closure only: the recurrent allele-state
mutation operator. It does not revise the canonical H1--H3 claims, theorem layer,
trait-recruitment rule, source-transfer rule, conservation projection, or event
semantics of `eco-genetic-criticality`.

Let \(p_t\in[0,1]\) denote the high-trait-associated allele frequency after the
unchanged selection and migration operations in a patch at generation \(t\). The
new mutation update is inserted **after migration and before finite drift**:

\[
M_{u}(p_t)=u_{L\to H}+(1-u_{L\to H}-u_{H\to L})p_t.
\]

The downstream drift, demographic, interaction, and trait updates receive the
mutated frequency exactly where the predecessor closure received its symmetric
mutated frequency.

## Mathematical properties

Define total mutation pressure \(\kappa_\mu=u_{L\to H}+u_{H\to L}\). Validity
requires \(0\le\kappa_\mu\le1\). Then

\[
\frac{dM_u}{dp}=1-\kappa_\mu,
\]

so the map preserves \([0,1]\) and contracts frequency differences whenever
\(0<\kappa_\mu\le1\). When \(\kappa_\mu>0\), mutation alone has equilibrium

\[
p_\mu^\ast=\frac{u_{L\to H}}{u_{L\to H}+u_{H\to L}}.
\]

The symmetric predecessor bridge is exact for \(u_{L\to H}=u_{H\to L}=\mu\):

\[
M_u(p)=\mu+(1-2\mu)p.
\]

Protocol 001 fixes \(\kappa_\mu=0.20\) and therefore holds contraction strength
constant while changing only \(p_\mu^\ast\):

| panel | \(u_{L\to H}\) | \(u_{H\to L}\) | \(p_\mu^\ast\) |
|---|---:|---:|---:|
| SYM | 0.10 | 0.10 | 0.50 |
| UP | 0.15 | 0.05 | 0.75 |
| DOWN | 0.05 | 0.15 | 0.25 |

Thus any cross-panel difference cannot be attributed merely to unequal
one-generation mutation turnover.

## Stage separation

For each panel separately:

1. **H1 source reconstruction.** Run the frozen \((A_{\rm ref},\kappa)\) grid
   and retain every source-preparation and projection outcome.
2. **Trait-loss-only calibration.** Candidate schedules are evaluated only with
   \(P(0<\tau_T\le T\mid\text{eligible baseline})\). Inputs containing
   H-alpha, H-gamma, warning, lead, lag, or lead-time fields are invalid.
3. **Domain freeze.** Select at most one eligible cell/schedule pair per panel
   using the deterministic rank
   \[
   (|\bar P_T-0.50|,\ T,\ d,\ A_{\rm ref},\ \kappa).
   \]
4. **Fresh-seed validation.** Only now evaluate all six relative-warning
   endpoints. Events absent within the horizon are right-censored; a generation-0
   crossing is baseline-ineligible, not an early warning.
5. **Secondary audit.** Apply the pre-existing absolute thresholds only to the
   saved validation trajectories. No resimulation, schedule selection, or
   threshold tuning is allowed.

## Required artifacts

Every run must write a protocol identity record containing: upstream commit,
operator rates, H1 grid, seed sets, candidate family, selected-domain outcome,
and code version. Each trajectory-level output must preserve source status,
projection status, baseline eligibility, warning time, trait-loss time, and
censoring reason.
