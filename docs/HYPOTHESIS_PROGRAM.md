# Independent hypothesis program

## Scope

`eco-genetic-warning-extensions` does not reopen the completed H1/H3 evidence ledger in `eco-genetic-criticality`. It changes the recurrent state-transition closure and asks what new finite-model propositions follow.

Parent logic:

```text
interaction feedback can support distinct functional states
→ fragmentation can disrupt the high-function state and reduce local effective size
→ relative genetic erosion can precede realised functional-trait loss in one calibrated symmetric domain
```

Extension logic:

```text
H-MD-1  source feasibility
→ H-MD-2  functional-loss regime
→ H-MD-3a  matched warning-domain evaluability
→ H-MD-3b  direction-only warning effect, conditional on evaluability
```

H-MD-3a/3b are a post hoc logical decomposition of the original H-MD-3 question. The labels clarify the status of completed evidence; they do not retroactively preregister a new hypothesis.

## H-MD-1 — recurrent-transition coordinates change high-function source feasibility

### Proposition

At fixed recurrent-transition relaxation strength `kappa_mu`, changing directional equilibrium `p_star` changes the finite region in which a prepared high-function source can be reconstructed and retained under the declared closure.

### Mechanistic basis

For

\[
M(p)=\kappa_\mu p_\mu^\ast+(1-\kappa_\mu)p,
\]

a local requirement `M(p) >= p_c` implies

\[
p \ge \frac{p_c-\kappa_\mu p_\mu^\ast}{1-\kappa_\mu}.
\]

Increasing `p_star` lowers the pre-transition frequency required to remain above that local boundary. This is a mechanism-level algebraic prediction; the finite stochastic result is tested separately.

### Test and result

Protocol 002 Stage I used the common `3 kappa_mu × 5 p_star` grid with independent source reconstruction at every coordinate.

- attempts: 3,375;
- source-prepared and projection-supported: 2,269;
- support range: 44.89%–86.67%;
- within fixed-`kappa_mu` rows, support generally increased with `p_star`.

### Status

**Supported as finite Type S evidence for the declared closure.**

This is a clean common-grid extension result.

## H-MD-2 — recurrent-transition coordinates change the functional-loss regime

### Proposition

Under the same predeclared deterioration candidate family, recurrent-transition coordinates change the probability/timing structure of realised high-trait loss, including rapid loss, persistence, censoring, and seed sensitivity.

### Test and result

Protocol 002 Stage II applied the same warning-blind deterioration family across all 15 coordinates. Calibration could inspect source/projection eligibility, baseline high-trait presence, trait-loss occurrence, and trait-loss time only; diversity and warning fields were unavailable.

Among 648 complete five-seed candidates:

- 322 were rapid-loss-side;
- 242 were persistence-side;
- 84 were seed-heterogeneous.

### Status

**Supported as finite Type S evidence for the declared closure.**

The key result is upstream of warning: the recurrent-transition manipulation reorganised the event-generating regime itself.

## H-MD-3a — common-family warning-domain evaluability

### Proposition

For a matched warning comparison to be available under Protocol 002, each recurrent-transition coordinate must contain at least one complete candidate with all five seed-block trait-loss frequencies in the preregistered intermediate-risk interval `[0.30, 0.70]`.

This is the evaluability component implicit in the original H-MD-3 question.

### Exact finite certificate

For coordinate \(\theta\), define

\[
E_\theta = \left\{c : 0.30 \le r_{c,b} \le 0.70\;\;\text{for every seed block }b\right\},
\]

where \(r_{c,b}\) is the realised trait-loss frequency for candidate \(c\) in seed block \(b\).

The Protocol 002 selector returns a domain for coordinate \(\theta\) if and only if \(E_\theta\neq\varnothing\). This is implemented directly by the locked calibration selector; warning fields are not involved.

The completed Stage II artifacts show:

- eligible candidate count: 0;
- selected domain count: 0;
- `no_domain_selected`: 15/15 coordinates.

Therefore

\[
E_\theta=\varnothing
\]

for every tested coordinate under the declared common candidate family and strict gate.

### Status

**Negative result, recovered for the declared finite grid and candidate family.**

The proposition that every coordinate supplies an eligible common-family warning domain is false in this finite design. This is not a claim that no such domain can exist under any other deterioration family or biological model.

This result is stronger than “calibration happened to fail”: the stored finite calibration table plus the preregistered gate form a complete no-domain certificate for Protocol 002.

## H-MD-3b — direction-only genetic-warning effect conditional on matched evaluability

### Proposition

Conditional on matched warning-validation domains existing under a common deterioration family, recurrent-transition direction changes warning availability, lead/lag ordering, or lead time.

### Status of the matched test

**Unresolved / not identified.**

Protocol 002 did not supply the matched evaluable domains required to define this contrast. Because H-MD-3a failed, the intended common-grid Stage III estimand was unavailable. A null result cannot be assigned, because the comparison itself was not instantiated.

This is the only part of the current H-MD chain that remains neither supported nor rejected by a matched common-grid experiment.

## Protocol 003 — separate recovery of evaluability, not H-MD-3b recovery

Protocol 003 was declared after Protocol 002 closed. It expanded candidate schedules and changed the event-risk gate using trait-loss-only information before warning endpoints were calculated. Fresh independent confirmation recovered two evaluable domains.

Those domains differ in recurrent-transition parameters and also in `A_ref`, interaction-feedback `kappa`, deterioration strength, and horizon. Therefore their Stage III contrast cannot identify recurrent-transition direction alone.

Observed portability results:

- recalibrated symmetric: 323 leads, 1 tie, 0 lags across 324 valid endpoint comparisons; valid-pair availability 0.540;
- directional calibrated: 184 leads, 5 ties, 12 lags across 201 valid endpoint comparisons; valid-pair availability 0.335;
- directional `H_gamma` 20%: warning incidence 41/81; realised functional-trait-loss incidence 52/81;
- all six full-horizon-normalized direct timing-difference intervals include zero.

### Status

**Separate portability/boundary result.**

Warning behaviour was not invariant across the two recalibrated domains, but the contrast does not recover H-MD-3b as a direction-only causal statement.

## Where H2-R-AS fits

H2-R-AS was the original Protocol 001 special-case formulation:

\[
\tau_{\Delta H_x(r)} < \tau_T,
\quad x\in\{\alpha,\gamma\},\quad r\in\{0.05,0.10,0.20\}.
\]

It remains historical motivation, not the final organising hypothesis. The completed evidence showed that source feasibility and loss-regime structure change before warning reliability can be fairly compared, so H-MD-1/H-MD-2/H-MD-3a/H-MD-3b is the clearer final logic.

## Recovery table

| item | empirical object | status | what is actually concluded |
|---|---|---|---|
| H-MD-1 | common-grid source reconstruction | **supported** | source feasibility changes across recurrent-transition coordinates |
| H-MD-2 | common-family Stage II loss outcomes | **supported** | functional-loss regime changes across recurrent-transition coordinates |
| H-MD-3a | strict all-seed eligibility sets `E_theta` | **negative / recovered** | no matched common-family warning domain exists in the tested grid/family |
| H-MD-3b | matched common-grid warning contrast | **unresolved** | direction-only warning effect is not identified |
| Protocol 003 | two independently recalibrated validation domains | **portability result** | warning availability/ordering are not invariant across the two domains; cause is not isolated to direction |

## Protocol map

- **Protocol 001:** historical directional-mutation bridge/pilot; preserves H2-R-AS provenance.
- **Protocol 002 Stage I:** H-MD-1.
- **Protocol 002 Stage II:** H-MD-2 and the finite H-MD-3a no-domain certificate.
- **Protocol 003:** separately declared evaluability recovery and portability validation; not a matched H-MD-3b test.
- **Secondary review audit:** locked-record uncertainty, timing, and censoring analysis; no new simulation or hypothesis selection.

## Interpretation discipline

Permitted:

- recurrent-transition coordinates reorganise high-function source feasibility;
- recurrent-transition coordinates reorganise the functional-loss regime under the common deterioration family;
- the declared common candidate family contains no eligible warning-validation domain at any of the 15 coordinates;
- after separate warning-blind recalibration, warning availability and ordering differ across two non-matched eco-genetic domains;
- potential function, realised function, population persistence, genetic diversity, and warning observability are distinct states.

Prohibited:

- directional transition universally causes collapse or rescue;
- H-MD-3b is false because Protocol 002 selected no domain;
- Protocol 003 identifies a direction-only warning effect;
- genetic diversity always warns before function is lost;
- `p_star` is an empirical mutation-rate estimate;
- the two Stage III domains form a complete phase diagram;
- extension trajectories replace the parent H1/H3 evidence ledger.

## Final logic

```text
parent H1/H3 mechanism
→ change recurrent-transition closure
→ H-MD-1: can the high-function source exist?
→ H-MD-2: what functional-loss regime is generated?
→ H-MD-3a: does a matched warning-validation domain exist?
   → here: no, under the declared common family
→ H-MD-3b: if matched domains exist, does direction change warning performance?
   → here: unresolved
→ Protocol 003: separately recalibrated portability test
```

The main scientific advance is therefore not a universal warning threshold. It is a resolved ordering of questions: **source feasibility, functional-loss regime, and matched-domain evaluability must be established before a direction-only warning effect can be identified.**