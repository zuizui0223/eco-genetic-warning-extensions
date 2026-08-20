# Eco-genetic regimes govern when genetic early warning can be validated

## One-sentence thesis

**Genetic early warning is not a property of a diversity statistic alone: it is a downstream property of an eco-genetic regime that must first sustain a functional state, generate a reproducible loss process, and align genetic change with that functional loss.**

## Central question

The paper should ask one question throughout:

> **Is genetic early-warning reliability a portable property of the genetic signal, or does it emerge from the eco-genetic regime that generates both the signal and functional loss?**

Everything in the paper has one of five roles in answering that question.

## The single causal story

### Act 1 — establish what can be lost before population extinction

The parent mechanism is the foundation, not a parallel paper inside the paper.

1. Positive interaction feedback permits distinct low- and high-function states in the declared model.
2. Fragmentation of the same prepared high state weakens interaction support, local effective size, and realised high-trait mass.
3. Therefore ecological function can disappear while population/allele presence persists, creating a biologically meaningful target for early warning.

**Role in the story:** this establishes the eco-genetic pathway that makes a genetic warning biologically plausible.

The fresh fragmentation gradient is supporting sensitivity evidence. It belongs mainly in the Supplement because the paper does not need a second fragmentation story once the bridge is established.

### Act 2 — show that genetic warning can work, but only conditionally

The inherited symmetric benchmark is a proof of possibility, not the final claim.

- In one warning-blind calibrated symmetric domain, baseline-relative `H_alpha` and `H_gamma` erosion preceded all 35 observed realised functional-trait losses.
- Fixed absolute thresholds produced both leads and lags.

**Role in the story:** genetic erosion can provide advance information in a calibrated regime, but the warning rule is already not universally portable across definitions.

This motivates the real extension question: what happens when the recurrent process maintaining/removing the high-associated state changes?

### Act 3 — the core result: recurrent transitions change the prerequisites for warning before warning is measured

This is the empirical centre of the paper.

#### H-MD-1: source feasibility

Across the common 15-coordinate recurrent-transition grid, 2,269 of 3,375 attempts supported source preparation/projection, with support spanning 44.89%–86.67%. Recurrent-transition coordinates therefore change whether the high-function starting state can be established at all.

#### H-MD-2: functional-loss regime

Protocol 002 completed 20,250 warning-blind calibration attempts. Under the same common deterioration family, the 648 complete candidates separated into 322 rapid-loss, 242 persistence, and 84 seed-heterogeneous candidates.

#### H-MD-3a: matched-domain evaluability

No candidate satisfied the strict all-seed intermediate-risk gate. All 15 coordinates were `no_domain_selected`.

**This is the turning point of the paper.** The manipulation changed the event-generating system so strongly that a common warning comparison ceased to exist before any warning endpoint was inspected.

The paper should therefore not frame Protocol 002 as a failed attempt to test warning. It is the strongest identified result:

> **Event-regime feasibility is itself an eco-genetic outcome and is upstream of warning performance.**

### Act 4 — recover evaluability and test portability, not direction-only causation

Protocol 003 asks a narrower downstream question: if warning-blind recalibration is allowed to recover evaluable event regimes, does the same warning behave similarly across those calibrated systems?

The two recovered domains are not matched single-factor contrasts. They differ in recurrent-transition parameters, ecological parameters, deterioration strength, and horizon.

The useful result is therefore portability:

- valid-pair availability fell from 0.540 to 0.335;
- the recalibrated symmetric domain had 323 leads, 1 tie, 0 lags;
- the directional calibrated domain had 184 leads, 5 ties, 12 lags;
- timing contrasts were endpoint- and schedule-dependent, and all six full-horizon-normalized direct difference intervals included zero.

**Role in the story:** once evaluability is restored, warning availability and ordering still depend on the calibrated system. Stage III supports non-portability, not a direction-only timing effect.

Availability/censoring is more important to the main story than conditional lead-time medians. The latter should remain secondary.

### Act 5 — theoretical closure: diversity is not a monotone proxy for functional support

The new Type T identities explain why a universal warning rule should not be expected from the transition operator itself.

For

\[
M(p)=p+\kappa_\mu(p_\mu^*-p),
\qquad H(p)=2p(1-p),
\]

increasing `p_star` always strengthens the local high-associated allele support margin,

\[
\frac{\partial [M(p)-p_c]}{\partial p_\mu^*}=\kappa_\mu>0,
\]

but its effect on heterozygosity is

\[
\frac{\partial H(M(p))}{\partial p_\mu^*}
=2\kappa_\mu[1-2M(p)].
\]

Thus when `M(p)>0.5`, stronger local high-state support coincides with **lower** heterozygosity.

With fixed patch weights,

\[
H_\gamma'-H_\alpha'=(1-\kappa_\mu)^2(H_\gamma-H_\alpha),
\]

so contraction of among-patch frequency heterogeneity depends on transition strength but not direction.

**Role in the story:** this is the mechanistic capstone. Genetic diversity is not a monotone surrogate for functional support, so a genetic warning must be calibrated to the state/path and loss regime rather than transferred as a context-free threshold.

This local theorem does not determine full stochastic warning first-passage ordering.

## Final causal chain

```text
interaction feedback creates a functional state
        ↓
fragmentation can weaken that state and local effective size
        ↓
in one calibrated regime, genetic erosion can precede realised functional loss
        ↓
change recurrent state-transition dynamics
        ↓
source feasibility changes (H-MD-1)
        ↓
functional-loss regime changes (H-MD-2)
        ↓
a common intermediate-risk warning domain can disappear (H-MD-3a)
        ↓
warning is no longer a comparable quantity until evaluability is recalibrated
        ↓
when recalibrated, warning availability/ordering are not fully portable (Protocol 003)
        ↓
Type T: genetic diversity and functional support need not move monotonically together
```

## What is the main result versus supporting evidence?

### Main line

1. **Fragmentation/function bridge:** establishes the biological pathway from ecological support to local effective size and realised function.
2. **Conditional warning benchmark:** proves genetic warning can exist in one calibrated regime but is definition-dependent.
3. **H-MD-1 + H-MD-2 + H-MD-3a:** the central empirical result — recurrent-transition dynamics reorganise source feasibility and loss regimes and can remove the matched domain required for warning validation.
4. **Protocol 003 availability/order:** downstream portability evidence after warning-blind recalibration.
5. **Type T support–diversity decoupling:** mechanistic explanation for why no context-free diversity warning should be expected.

### Keep secondary

- detailed fragmentation-gradient dose response: Supplementary Fig. S1;
- exact H3 cell-level effect-size tables: Supplement;
- Protocol 003 calibration chronology beyond the minimum needed to prove warning-blindness: Supplementary Methods;
- conditional positive lead-time medians and hold-only normalization: secondary diagnostic, candidate for Supplement rather than headline evidence;
- all CI/debugging/branch history: repository provenance only.

## Recommended Results order

1. **Fragmentation establishes the eco-genetic route from interaction loss to demographic/genetic vulnerability.**
2. **Relative genetic erosion can lead functional loss in one calibrated symmetric regime, but absolute thresholds are not robust.**
3. **Recurrent-transition coordinates reorganise high-function source feasibility.**
4. **The same common deterioration family reorganises functional-loss regimes and yields 15/15 no-domain outcomes.**
5. **Warning-blind recalibration restores evaluability, but warning availability and ordering differ across calibrated domains.**
6. **Exact transition theory shows why diversity is not a monotone proxy for high-state support.**

This order preserves causality. The current `main_text.md` begins its Results with H-MD-1/H-MD-2 and then returns to fragmentation; that ordering should be changed when the publication source is revised.

## Paper-level conclusion

The strongest paper is **not** “genetic diversity warns before functional collapse” and not “directional transition weakens warning.” It is:

> **Before asking whether a genetic signal is early, we must ask whether the eco-genetic regime generates a functional state, a reproducible loss process, and an interpretable relationship between genetic diversity and function. Recurrent-transition dynamics alter each prerequisite, making genetic early warning a regime-dependent and calibration-dependent property rather than a portable property of the metric itself.**
