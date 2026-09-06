# Exact local allele-sorting theorem for the q-only closure

Status: **operator-level theorem for the declared finite closure**. Theorem 1 and the focused endpoint protocol were written and committed before the focused endpoint experiment was opened. The spatial covariance corollary below was derived and recorded in PR #154 while the locked workflow was still in progress, before the outcome artifact was opened.

## Setup

Use the pinned parent simulator `zuizui0223/eco-genetic-criticality@b7ee738767c92307d6d23a85a3eeb857faf6ddfb` with the q-only intervention used by the pathway-decomposition programme. For the high endpoint trait `z=1`, the declared trait-performance surface is

\[
W(1;q)=0.5+0.8q.
\]

The allele-selection step uses selection strength `s=0.5`, so the high-allele relative fitness multiplier is

\[
w(q)=1+s\{W(1;q)-1\}=0.75+0.4q.
\]

For interior high-allele frequency `0<p<1`, the deterministic selection update before drift is

\[
p^+(p,q)=\frac{p\,w(q)}{1-p+p\,w(q)}.
\]

Migration and symmetric mutation are both zero in the focused proof experiment, so no spatial averaging or mutation is inserted between this selection operator and finite drift.

## Theorem 1 — exact sorting monotonicity

For every `0<p<1` and `0<=q<=1`,

\[
\frac{\partial p^+}{\partial q}
=\frac{0.4\,p(1-p)}{[1+p\{w(q)-1\}]^2}>0.
\]

Hence the selected high-allele frequency is strictly increasing in local interaction state q at every interior allele frequency.

Equivalently, the odds update factorizes exactly:

\[
\frac{p^+}{1-p^+}=\frac{p}{1-p}\,w(q),
\]

so

\[
\operatorname{logit}(p^+)-\operatorname{logit}(p)=\log(0.75+0.4q).
\]

The selection-induced increment in high-allele log odds is therefore independent of p and strictly increasing in q.

## Corollary 1 — exact sorting switch at q*=0.625

Because

\[
w(q)=1 \iff q=0.625,
\]

we have, for every `0<p<1`,

\[
q>0.625 \Rightarrow p^+>p,
\]
\[
q=0.625 \Rightarrow p^+=p,
\]
\[
q<0.625 \Rightarrow p^+<p.
\]

Thus `q*=0.625` is an exact local allele-sorting switch in the declared closure.

## Corollary 2 — the sorting switch coincides with the high-trait viability threshold

The high endpoint trait is potentially viable when

\[
W(1;q)\ge1,
\]

which gives the same threshold

\[
q\ge0.625.
\]

Therefore the closure contains an exact eco-genetic consistency relation: patches above the high-trait viability threshold are also the patches in which deterministic local selection increases the high allele, whereas patches below that threshold deterministically decrease it before drift.

This coincidence is algebraic for the declared life cycle; it is not asserted as a universal natural law.

## Theorem 2 — one selection step increases spatial q–allele sorting

Let

\[
u_i=\operatorname{logit}(p_i)
\]

for patch `i`, and define

\[
g(q)=\log(0.75+0.4q).
\]

Theorem 1 gives

\[
u_i^+=u_i+g(q_i).
\]

Therefore

\[
\operatorname{Cov}(q,u^+)-\operatorname{Cov}(q,u)
=\operatorname{Cov}(q,g(q)).
\]

For equally weighted patches,

\[
\operatorname{Cov}(q,g(q))
=\frac{1}{2n^2}\sum_{i,j}(q_i-q_j)\{g(q_i)-g(q_j)\}.
\]

Because `g` is strictly increasing, every summand is nonnegative. If q is nonconstant across patches, at least one pair has `q_i != q_j`, so at least one summand is strictly positive. Hence

\[
\boxed{
\operatorname{Cov}(q,\operatorname{logit}p^+)
>
\operatorname{Cov}(q,\operatorname{logit}p)
}
\]

whenever q varies spatially and allele frequencies are interior.

Thus local q-dependent allele selection is not merely monotone patchwise: a single deterministic selection step **strictly increases spatial association between interaction state and high-allele log odds** whenever ecological state is spatially heterogeneous.

## What these theorems prove — and what they do not

They prove exactly that the local `q -> allele selection` operator is a spatial sorting operator, that its direction switches at the same q threshold as potential high-trait viability, and that one deterministic selection step increases q–allele spatial sorting whenever q varies among patches.

The theorem alone does **not** prove that this single edge changes the later all-patch realised-high-trait loss endpoint. That endpoint claim is tested separately in the prospectively locked 6,000-pair focused intervention and is recorded in `docs/ALLELE_SORTING_SINGLE_EDGE_RESULT_2026-09-06.md`.
