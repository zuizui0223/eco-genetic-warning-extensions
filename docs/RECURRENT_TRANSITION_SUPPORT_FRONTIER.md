# Exact local support frontier for recurrent transitions

## Scope

This note records a Type T boundary for the declared affine recurrent-transition operator. It explains the **direction** of the support frontier seen in the finite Protocol 002 condition map, but it is not a theorem for the full stochastic functional-loss regime.

For

\[
M(p)=\kappa_\mu p_\mu^*+(1-\kappa_\mu)p,
\]

suppose the local high-associated state requires

\[
M(p)\ge p_c.
\]

At fixed pre-transition frequency \(p\), threshold \(p_c\), and \(\kappa_\mu>0\), the equality frontier is

\[
p_{\mu,\mathrm{crit}}^*
=\frac{p_c-(1-\kappa_\mu)p}{\kappa_\mu}
=p+\frac{p_c-p}{\kappa_\mu}.
\]

Because the coefficient of \(p_\mu^*\) in \(M(p)\) is positive,

\[
M(p)\ge p_c
\iff
p_\mu^*\ge p_{\mu,\mathrm{crit}}^*.
\]

The critical value may lie outside `[0,1]`. In that case the formula certifies that the local threshold cannot be met exactly by any admissible `p_star` at that pre-state and transition strength.

## Frontier shift with transition strength

Differentiate with respect to \(\kappa_\mu\):

\[
\frac{\partial p_{\mu,\mathrm{crit}}^*}{\partial \kappa_\mu}
=-\frac{p_c-p}{\kappa_\mu^2}.
\]

Therefore:

- if \(p<p_c\), stronger recurrent-transition relaxation **lowers** the `p_star` required to reach the same local high-state threshold;
- if \(p=p_c\), the local frontier is independent of `kappa_mu`;
- if \(p>p_c\), the derivative reverses sign because the pre-transition state is already above the threshold.

The first case is the relevant state-constrained prediction when deterioration has moved the high-associated allele frequency below the local support threshold.

## Relation to the finite Protocol 002 frontier

The warning-blind finite condition map shows that the rapid-loss-to-persistence transition moves toward lower `p_star` as `kappa_mu` increases:

```text
kappa_mu = 0.05: rapid through p_star=0.75; heterogeneous at 0.90
kappa_mu = 0.20: rapid at 0.25; heterogeneous at 0.50; persistence at 0.75
kappa_mu = 0.35: rapid at 0.25; persistence at 0.50
```

The exact local theorem predicts the **same frontier direction** when the relevant pre-transition allele state is below its local high-state threshold: increasing `kappa_mu` lowers the directional equilibrium required to restore/support that state.

This agreement is mechanistically useful but bounded. The finite loss regime also depends on source preparation, interaction feedback, drift, demography, deterioration, trait realization and stochastic seed history. The theorem therefore does not predict the observed coordinate boundary quantitatively and must not be presented as a proof that `kappa_mu` or `p_star` alone causes the full rapid/persistence regime transition.

## Consequence for the next condition search

The theorem and finite map jointly justify **frontier refinement rather than global parameter expansion**:

1. hold non-transition ecological and deterioration settings matched initially;
2. refine `p_star` between observed rapid and heterogeneous/persistence cells within fixed `kappa_mu` rows;
3. use warning-blind trait-loss and seed-reproducibility outcomes to locate the finite transition frontier;
4. only after a reproducible intermediate-risk region is confirmed should diversity/warning endpoints be released.

This supplies a state-constrained theoretical prediction before any new condition-refinement simulation is run.

## Executable implementation

Implemented in `src/eco_genetic_warning_extensions/recurrent_transition_frontier.py` and tested in `tests/test_recurrent_transition_frontier.py`.
