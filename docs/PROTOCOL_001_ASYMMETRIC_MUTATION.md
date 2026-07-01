# Protocol 001 — asymmetric recurrent mutation and relative genetic warning

**Status:** preregistered design; no simulation result.

## 1. Question

Does the conditional relative-warning ordering found in the preceding finite
closure persist when recurrent mutation has a direction tied to the
high-trait-versus-low-trait allele, rather than being symmetric?

This protocol addresses a new dynamic hypothesis:

\[
\textbf{H2-R-AS:}\qquad
\tau_{\Delta H_x(r)} < \tau_T,
\quad x\in\{\alpha,\gamma\},\quad r\in\{0.05,0.10,0.20\},
\]

under an explicitly declared asymmetric mutation closure and a
trait-loss-calibrated deterioration schedule. It is a hypothesis, not a theorem.
Any numerical result is Type S finite evidence only.

## 2. Only changed closure

Let \(p_t\) be the frequency of the allele contributing to the high-trait
recruitment kernel. Replace the symmetric mutation operator with

\[
p_{t+1}^{\mathrm{mut}}
= u_{L\to H}+(1-u_{L\to H}-u_{H\to L})p_t.
\]

- \(u_{L\to H}\): mutation from low-trait allele to high-trait allele;
- \(u_{H\to L}\): mutation from high-trait allele to low-trait allele.

Constraints are \(0\le u_{L\to H},u_{H\to L}\le1\) and
\(u_{L\to H}+u_{H\to L}\le1\). The symmetric rule is recovered exactly when
both rates are equal.

All other finite trait-recruitment, source-transfer, and conservation-projection
rules must be copied verbatim from the completed predecessor closure before this
new operator is enabled. Any additional change requires Protocol 002 rather
than an amendment hidden in implementation.

## 3. Predeclared mutation panel

Rates are **closure units, not biological mutation-rate estimates**. The panel
holds total one-generation mutation pressure at 0.20 and varies only direction:

| label | \(u_{L\to H}\) | \(u_{H\to L}\) | role |
|---|---:|---:|---|
| SYM | 0.10 | 0.10 | exact symmetric bridge / regression control |
| UP | 0.15 | 0.05 | bias toward high-trait allele |
| DOWN | 0.05 | 0.15 | bias away from high-trait allele |

No other mutation pair belongs to Protocol 001.

## 4. H1 source stage

For each mutation panel member, rerun the nested H1 source-resolution stage over
the fixed grid

```text
A_ref: 0.8, 1.0, 1.2
kappa: 3.0, 4.5, 6.0
H1 source master seeds: 20261210–20261214
H1 source replicates: 5 per cell per seed
nested barrier grids: 25, 49, 97
stage generations: 30
hold generations: 30
```

A source is usable only if it passes the existing H1 high-state preparation and
full-state conservation projection. Source-preparation failures are retained.

## 5. Trait-loss-only schedule calibration

For each usable H1 cell and mutation panel member, use only this fixed candidate
family:

```text
barrier ramp: 30 generations
barrier hold: 90 or 210 generations
total normalized barrier increase: 0.15, 0.30, 0.45
calibration master seeds: 20261210–20261214
replicates: 5 per cell per seed
```

The calibration endpoint is post-baseline realised high-trait loss only:

\[
P(0<\tau_T\le T\mid
\text{source prepared, projection supported, baseline high trait present}).
\]

No H-alpha, H-gamma, relative-warning time, lead, tie, lag, or lead-time value
may be computed, written, or inspected during calibration.

A schedule is eligible for a cell only when every calibration seed block has
trait-loss probability in \([0.30,0.70]\). For each mutation panel member,
select at most one cell/schedule pair:

1. pool all eligible cell/schedule pairs;
2. choose pooled trait-loss probability nearest 0.50;
3. break ties by shorter total horizon, then smaller normalized increase, then
   smaller \(A_{\rm ref}\), then smaller \(\kappa\).

If no pair is eligible for a panel member, record `no_domain_selected` for that
member and do not widen the candidate family in this protocol.

## 6. Independent validation

Each selected panel-member domain is validated separately; there is no
cross-panel winner selection. Use fresh seeds:

```text
validation master seeds: 20270110–20270114
replicates: 20 per selected domain per seed
```

For every available trajectory, report **all** six endpoints:

```text
H_alpha: r = 0.05, 0.10, 0.20
H_gamma: r = 0.05, 0.10, 0.20
```

For each endpoint retain baseline eligibility, warning time, trait-loss time,
valid same-replicate pair, lead, tie, lag, and censoring. A baseline crossing is
not an early warning. Missing warning or trait-loss events remain censored.

## 7. Fixed-threshold secondary audit

After—not during—relative-warning validation, apply the already declared
absolute thresholds

\[
H_\alpha\le0.20,\qquad H_\gamma\le0.20
\]

to the raw validation series as a deterministic secondary audit. It is not a
schedule-selection or threshold-selection mechanism.

## 8. Interpretation and stopping rules

- A panel member with no selected domain makes no H2-R-AS ordering claim.
- A selected member with no valid pairs remains censored; it does not count as
  support or refutation.
- Leads, ties, and lags must all be reported. A single observed lag prevents a
  uniform finite ordering claim for that endpoint/domain.
- A result in one panel member does not generalize to another panel member.
- The protocol may close after this panel even if outcomes are mixed. Exploring
  another mutation family requires a new numbered protocol and fresh seeds.
