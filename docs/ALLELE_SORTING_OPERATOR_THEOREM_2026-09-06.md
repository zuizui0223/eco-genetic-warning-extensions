# Exact local allele-sorting theorem for the q-only closure

Status: **operator-level theorem for the declared finite closure**. This document is written and committed before the focused endpoint experiment is opened.

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

## What this theorem proves — and what it does not

It proves exactly that the local `q -> allele selection` operator is a spatial sorting operator and that its direction switches at the same q threshold as potential high-trait viability.

It does **not** by itself prove that this single edge is necessary for the later all-patch realised-high-trait loss contrast. The previous prospectively locked 1,500-pair edge-deletion experiment made this the leading single-edge candidate but left the preregistered generation-40 risk difference-in-differences unresolved because its 95% interval slightly crossed zero. A separate focused prospective precision experiment is therefore required for endpoint-level causal attribution.
