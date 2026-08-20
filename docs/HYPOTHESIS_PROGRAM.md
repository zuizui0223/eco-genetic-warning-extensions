# Independent hypothesis program

## What this repository is for

`eco-genetic-warning-extensions` is the second computational phase of the integrated eco-genetic warning study. It does not reopen the parent repository's completed H1/H3 evidence ledger.

The parent study established the mechanistic sequence that motivates the extension:

```text
interaction feedback can support distinct functional states
-> fragmentation can disrupt that state and reduce local effective size
-> relative genetic erosion can precede realised functional-trait loss in one calibrated symmetric domain
```

The extension asks what happens when the **recurrent state-transition process itself is changed**.

The final paper-level structure is not a single “does warning still work?” hypothesis. It is a three-step chain:

```text
H-MD-1  source feasibility
-> H-MD-2  functional-loss regime
-> H-MD-3  warning reliability / evaluability
```

The first two are directly tested on a common recurrent-transition grid. The third cannot be cleanly tested as a common-grid single-factor contrast because the strict calibration produces no shared warning-validation domain.

## H-MD-1 — recurrent-transition direction changes high-function source feasibility

### Proposition

At fixed recurrent-transition relaxation strength `kappa_mu`, changing the directional equilibrium `p_star` changes the finite region in which an H1-prepared high-function source can be reconstructed and retained under the declared closure.

### Mechanistic basis

For the recurrent-transition operator

\[
M(p)=\kappa_\mu p_\mu^\ast+(1-\kappa_\mu)p,
\]

a local post-transition requirement `M(p) >= p_c` implies

\[
p \ge \frac{p_c-\kappa_\mu p_\mu^\ast}{1-\kappa_\mu}.
\]

Increasing `p_star` therefore lowers the pre-transition frequency required to remain above a local high-state boundary. This algebraic relation is a mechanism-level prediction; the finite stochastic result must be tested separately.

### Test

Protocol 002 Stage I used a common 15-coordinate grid (`3 kappa_mu × 5 p_star`) and independently reconstructed sources at every coordinate.

### Result

- 3,375 source attempts;
- 2,269 source-prepared, projection-supported outcomes;
- coordinate support range 44.89%–86.67%;
- within fixed-`kappa_mu` rows, support generally increased with `p_star`.

### Status

**Supported as finite Type S evidence for the declared closure.**

This is one of the cleanly identified extension hypotheses because the comparison is made on a common source-reconstruction grid.

## H-MD-2 — recurrent-transition direction changes the functional-loss regime

### Proposition

At fixed common deterioration family, recurrent-transition coordinates change the probability and timing structure of realised high-trait loss, including rapid loss, persistence, censoring, and seed sensitivity.

### Test

Protocol 002 Stage II applied the same warning-blind deterioration candidate family across the 15-coordinate grid. Candidate selection could use source/projection eligibility, baseline high-trait presence, realised trait-loss occurrence, and trait-loss time only. Genetic diversity, warning time, lead/lag, and lead time were unavailable.

A candidate was eligible only if every seed block had trait-loss frequency in `[0.30, 0.70]`.

### Result

Among 648 complete five-seed candidates:

- 322 were rapid-loss-side;
- 242 were persistence-side;
- 84 were seed-heterogeneous;
- 0 satisfied the strict all-seed intermediate-risk gate;
- all 15 recurrent-transition coordinates were recorded as `no_domain_selected`.

### Status

**Supported as finite Type S evidence for the declared closure.**

The important result is not that warning failed. Warning had not yet been inspected. The biological result is that recurrent-transition dynamics changed the event-generating regime itself.

## H-MD-3 — recurrent-transition conditions change genetic-warning reliability

### Intended proposition

For each recurrent-transition coordinate with an independently calibration-selected deterioration domain, relative genetic-diversity warning should have a measurable availability, lead/lag/censoring profile, and positive lead-time distribution before realised functional-trait loss.

No uniform direction of effect was assumed.

### Why the clean common-grid test could not be completed

Protocol 002 produced no eligible warning-validation domain at any of the 15 coordinates. Therefore a matched common-family test of H-MD-3 was **not evaluable under the strict declared gate**.

This is a result, not a missing analysis: the same biological process being manipulated to test warning reliability also determined whether a comparable loss regime existed.

### Protocol 003 recovery of evaluability

Protocol 003 was declared separately after Protocol 002 closed. It expanded candidate schedules and changed the event-risk gate using trait-loss-only information before any warning endpoint was calculated. Independent confirmation with fresh seeds produced two evaluable domains.

Those domains differ in more than recurrent-transition direction: they also differ in `A_ref`, interaction-feedback `kappa`, deterioration strength, and horizon. Stage III therefore cannot identify a transition-direction-only effect.

### Stage III result

- recalibrated symmetric domain: 323 leads, 1 tie, 0 lags across 324 valid endpoint comparisons; valid-pair availability 0.540;
- directional calibrated domain: 184 leads, 5 ties, 12 lags across 201 valid endpoint comparisons; valid-pair availability 0.335;
- at directional `H_gamma` 20%, warning incidence was 41/81 while realised functional-trait loss incidence was 52/81;
- direct whole-trajectory timing bootstrap found endpoint-dependent absolute contrasts;
- all six full-horizon-normalized between-domain 95% difference intervals included zero.

### Status

**Not cleanly recovered as a transition-direction hypothesis.**

The retained conclusion is a **portability/evaluability boundary**:

> warning availability and ordering were not invariant across two independently calibrated eco-genetic domains, but the Stage III comparison does not identify recurrent-transition direction alone as the cause.

## Where H2-R-AS fits

H2-R-AS was the original Protocol 001 special-case hypothesis:

\[
\tau_{\Delta H_x(r)} < \tau_T,
\quad x\in\{\alpha,\gamma\},\quad r\in\{0.05,0.10,0.20\},
\]

under a direction-specific recurrent-mutation closure.

It remains part of the project history and motivated the extension, but it is **not the final paper-level organising hypothesis**. The broader H-MD-1/H-MD-2/H-MD-3 structure better matches the completed evidence because the project discovered that source feasibility and loss-regime structure change before warning reliability can be fairly compared.

## Protocol-to-hypothesis map

| protocol | scientific role | hypothesis status |
|---|---|---|
| Protocol 001 | historical directional-mutation bridge/pilot | motivated H2-R-AS; not final headline structure |
| Protocol 002 Stage I | common-grid source reconstruction | direct H-MD-1 test; supported |
| Protocol 002 Stage II | common-family loss-regime calibration | direct H-MD-2 test; supported; H-MD-3 not evaluable under strict gate |
| Protocol 003 | separately declared warning-blind recalibration and validation | restores evaluability in two non-matched domains; portability/boundary result, not direction-only test |
| Secondary review audit | locked-record uncertainty and censoring analysis | refines Stage III interpretation; no new hypothesis or rerun |

## Interpretation discipline

Permitted conclusions:

- recurrent-transition coordinates reorganise high-function source feasibility under the declared common grid;
- they reorganise the functional-loss regime under the declared common deterioration family;
- a common warning-validation domain is not guaranteed to exist;
- after separate warning-blind recalibration, warning availability and ordering can differ across eco-genetic domains;
- potential function, realised function, population persistence, genetic diversity, and warning observability are distinct states.

Prohibited conclusions:

- directional mutation universally causes ecological collapse or rescue;
- recurrent-transition direction alone caused the Stage III warning difference;
- genetic diversity always warns before function is lost;
- genetic warning universally fails under directional transition;
- `p_star` is an empirical mutation-rate estimate;
- the two Stage III domains form a complete phase diagram;
- the historical parent H1/H3 evidence is replaced by extension trajectories.

## Final research logic

```text
parent H1/H3 mechanism
-> change recurrent-transition closure
-> H-MD-1: can the high-function source still exist?
-> H-MD-2: if deterioration begins, what loss regime is generated?
-> only if a comparable event regime exists:
   H-MD-3: how available and reliable is genetic warning?
```

The main conceptual advance is therefore not a universal warning threshold. It is the ordering of questions: **source feasibility and event-regime structure must be established before warning performance is interpretable.**
