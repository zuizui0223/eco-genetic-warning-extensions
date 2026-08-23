# Cross-layer alignment and state sufficiency

## Proposition — layer-wise marginals are not a sufficient dynamic state under local cross-layer feedback

Consider the declared local interaction update at equal area and carrying density,

\[
q_i^+ = \sigma\!\left(\kappa[\alpha q_i + \beta x_i + \gamma p_i - b]\right),
\]

where `q_i` is current interaction state, `x_i` realised high-trait mass, `p_i` high-associated allele frequency, `b` the current barrier, `kappa>0`, and `sigma` is the logistic map. Assume at least one of `beta` or `gamma` is non-zero.

Let a coarse summary retain the separate multisets

\[
\{q_i\},\qquad \{x_i\},\qquad \{p_i\},
\]

and any permutation-invariant summaries computed from those layers, including their means and standard global genetic-diversity summaries. The summary does not retain which `x_i,p_i` values occur in the same patch as each `q_i`.

Then that coarse summary is **not sufficient in general to determine the next interaction state**.

### Proof

Construct two states that share identical `q` values and differ only by a non-trivial permutation `pi` of the paired `(x,p)` bundle across patches:

\[
S_A=\{(q_i,x_i,p_i)\}_{i=1}^n,
\qquad
S_B=\{(q_i,x_{\pi(i)},p_{\pi(i)})\}_{i=1}^n.
\]

The two states have exactly the same separate layer-wise multisets and therefore the same values for every summary invariant to the permutation. Their local feedback inputs are

\[
z_i^A=\alpha q_i+\beta x_i+\gamma p_i,
\qquad
z_i^B=\alpha q_i+\beta x_{\pi(i)}+\gamma p_{\pi(i)}.
\]

For any permutation for which `z_i^A != z_i^B` for at least one patch, strict monotonicity of the logistic map and `kappa>0` imply

\[
q_i^+(S_A) \neq q_i^+(S_B).
\]

Hence the coarse permutation-invariant summary cannot determine the next state and is not a sufficient Markov state for the declared dynamics. QED.

## Phase-V constructive certificate

The preregistered aligned and anti-aligned states instantiate the proposition while also matching habitat area, census, complete global trait-bin totals, `H_alpha`, `H_gamma` and `FST`.

With `(alpha,beta,gamma)=(.6,.3,.1)`:

- aligned local support: `.47, .61, .75, .89`;
- anti-aligned local support: `.71, .69, .67, .65`;
- aligned q-by-bundle covariance: `+.025`;
- anti-aligned covariance: `-.025`.

At the first fixed barrier step, exact generation-1 interaction states are:

- aligned: `.4635, .6186, .7528, .8512`;
- anti-aligned: `.7178, .6993, .6800, .6601`.

The maximum patchwise difference is `.2543` despite identical declared layer-wise marginals.

The subsequent 500-pair finite campaign did **not** detect a directional difference in 60-generation functional-loss occurrence (`.678` vs `.722`; McNemar `p=.143`). This does not weaken the state-sufficiency proposition: transition non-equivalence and long-horizon marginal event incidence are different estimands.

## Corollary for functional-fragmentation regimes

A cross-system regime intended to be mechanism-agnostic cannot be defined only by independent layer scores such as habitat amount, mean interaction support, mean functional-trait support and neutral genetic diversity whenever the transition law couples those quantities locally.

At minimum, a candidate operational state must retain either:

1. the relevant **joint spatial state** (for example the patchwise pairing/covariance of interaction, function and eco-genetic support), or
2. a lower-dimensional statistic proven sufficient for the transition law.

For urban/island comparison this changes the convergence question. Different fragmentation mechanisms are allowed to converge, but convergence cannot be inferred from matching separate snapshot indicators. It must be assessed as **joint-state and transition equivalence** for the focal functional-loss process.

## Boundary

This proposition is exact for the declared local interaction update. It does not claim that the specific Phase-V alignment contrast universally changes long-horizon loss probability, and it does not establish that the same joint-state variables are sufficient in empirical urban or island systems. Those are empirical/process-specific questions.
