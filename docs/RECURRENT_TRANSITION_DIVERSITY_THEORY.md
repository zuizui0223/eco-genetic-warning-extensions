# Exact diversity identities for the recurrent-transition operator

## Status and scope

This document records **Type T algebraic results** for one common affine recurrent-transition step with fixed patch weights. It is part of the current scientific source of truth for the H-MD-3b theoretical boundary.

It is **not** a theorem about full warning first-passage ordering. Selection, drift, demographic change, interaction feedback, functional-trait loss, and censoring enter after or around this local transition step and require separate dynamic analysis.

## Operator

For high-trait-associated allele frequency \(p\), let

\[
M(p)=\kappa_\mu p_\mu^*+(1-\kappa_\mu)p
=p+k(s-p),
\]

where \(k=\kappa_\mu\in(0,1]\) and \(s=p_\mu^*\in[0,1]\).

The single-locus expected heterozygosity used by the parent finite model is

\[
H(p)=2p(1-p).
\]

## T1 — exact one-step heterozygosity change

Direct substitution gives

\[
H(M(p))-H(p)
=2k(s-p)\left[1-2p-k(s-p)\right].
\]

Therefore the recurrent transition can either increase or decrease heterozygosity. It increases \(H\) when the transition moves frequency toward \(1/2\), and decreases \(H\) when it moves frequency away from \(1/2\).

Equivalently,

\[
\frac{\partial H(M(p))}{\partial s}
=2k\left[1-2M(p)\right].
\]

The directional derivative changes sign exactly at

\[
M(p)=\frac12.
\]

### Consequence

There is **no universal signed effect of increasing `p_star` on heterozygosity without a constraint on the allele-frequency state**.

This is the first theoretical boundary relevant to H-MD-3b.

## T2 — exact alpha/gamma decomposition across patches

Let fixed nonnegative patch weights \(w_j\) sum to one, with frequencies \(p_j\) and weighted mean

\[
\bar p=\sum_j w_jp_j.
\]

Define the parent-model diversity quantities

\[
H_\alpha=\sum_j w_jH(p_j),
\qquad
H_\gamma=H(\bar p).
\]

Because \(H(p)=2p(1-p)\),

\[
H_\gamma-H_\alpha
=2\operatorname{Var}_w(p_j).
\]

Apply the same affine transition to every patch. Since

\[
M(p_j)-M(\bar p)=(1-k)(p_j-\bar p),
\]

weighted frequency variance contracts exactly as

\[
\operatorname{Var}_w(M(p_j))
=(1-k)^2\operatorname{Var}_w(p_j).
\]

Hence

\[
H_\gamma'-H_\alpha'
=(1-k)^2(H_\gamma-H_\alpha).
\]

### Consequence

The one-step contraction of the \(H_\gamma-H_\alpha\) gap depends on **transition strength `kappa_mu` but not on direction `p_star`**. Under fixed weights, direction shifts the mean allele frequency, whereas the affine contraction controls the reduction of among-patch frequency heterogeneity.

This separates two effects that were previously easy to conflate:

```text
p_star      -> directional shift of the weighted mean state
kappa_mu    -> affine contraction of deviations among patches
```

## T3 — H-alpha and H-gamma have the same directional derivative at fixed weights

Because a common affine operator commutes with the weighted mean,

\[
\overline{M(p)}=M(\bar p),
\]

and because the alpha/gamma gap contraction above does not depend on \(s\),

\[
\frac{\partial H_\alpha'}{\partial s}
=
\frac{\partial H_\gamma'}{\partial s}
=
2k\left[1-2M(\bar p)\right].
\]

### Consequence

For the transition step alone and fixed patch weights, `p_star` does not push \(H_\alpha\) and \(H_\gamma\) in opposite directional derivatives. Their direction-specific derivative is governed by the **post-transition weighted mean**, while their difference is governed by contraction strength.

Dynamic divergence between the warning behaviour of \(H_\alpha\) and \(H_\gamma\) must therefore enter through other life-cycle components or changing weights/states, not from the common affine transition direction alone.

## Relation to H-MD-3b

These results do not assign H-MD-3b a true/false dynamic answer. They recover a stronger theoretical boundary around what a future matched experiment may legitimately predict:

1. a universal `p_star -> lower diversity` or `p_star -> higher diversity` hypothesis is not valid without state constraints;
2. `p_star` and `kappa_mu` have analytically separable roles at the transition step;
3. a directional warning hypothesis must specify the relevant pre/post-transition allele-frequency region and cannot infer warning ordering from transition direction alone.

The current Protocol 002 evidence independently shows that the matched warning-validation domain required for a finite H-MD-3b causal contrast was absent under the declared common candidate family. Thus the repository has both an **empirical evaluability boundary** and an **exact diversity-sign boundary**.

## Executable implementation

The identities are implemented in:

- `src/eco_genetic_warning_extensions/mutation_coordinates.py`

and tested in:

- `tests/test_mutation_coordinates.py`

The tests verify the direct one-step formula, both possible heterozygosity signs, the sign switch at \(M(p)=0.5\), exact direction-independent contraction of the \(H_\gamma-H_\alpha\) gap, and equality of the fixed-weight `p_star` derivatives of \(H_\alpha\) and \(H_\gamma\).