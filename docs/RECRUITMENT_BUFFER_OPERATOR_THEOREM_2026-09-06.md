# Exact recruitment-buffer theorem for the q-only closure

Status: **operator-level theorem for the declared finite closure**, paired with an already prospectively locked edge-deletion result. This theorem explains the deterministic action of the allele-linked recruitment edge; it does not convert the finite closure into a universal natural mechanism.

## Setup

Use the pinned parent simulator `zuizui0223/eco-genetic-criticality@b7ee738767c92307d6d23a85a3eeb857faf6ddfb` and the q-only pathway-decomposition parameters.

Let:

- `R(z)` be the normalized resident trait distribution;
- `p` be the high-allele frequency;
- `L(z)` be the declared low-trait recruitment kernel;
- `H(z)` be the declared high-trait recruitment kernel;
- `h` be `inheritance_weight`.

The parent closure defines

\[
A_p(z)=(1-p)L(z)+pH(z)
\]

and the pre-selection recruit distribution

\[
Q(z)=(1-h)A_p(z)+hR(z).
\]

All terms are normalized probability distributions, so the final normalization in the implementation leaves this convex combination unchanged.

The kernel construction has disjoint declared support relative to the high-trait cutoff `z_c=0.7`:

\[
\sum_{z\ge z_c}L(z)=0,
\qquad
\sum_{z\ge z_c}H(z)=1.
\]

Let

\[
m=\sum_{z\ge z_c}R(z)
\]

be resident high-trait mass and

\[
r=\sum_{z\ge z_c}Q(z)
\]

be pre-selection recruit high-trait mass.

## Theorem 1 — exact trait–allele coherence contraction

By linearity of high-region mass,

\[
r=(1-h)p+hm.
\]

Therefore

\[
r-p=h(m-p)
\]

and

\[
r-m=(1-h)(p-m).
\]

For any `0<=h<1`, recruitment moves resident high-trait mass strictly toward the high-allele frequency whenever `m != p`:

\[
|r-p|=h|m-p|<|m-p|.
\]

Thus the allele-linked recruitment operator is an exact **trait–allele mismatch contraction** before ecological trait selection.

## Corollary 1 — exact 50% contraction in the pathway-decomposition closure

The locked q-only experiments use

\[
h=0.5.
\]

Hence

\[
\boxed{r=\frac{m+p}{2}}
\]

and

\[
\boxed{|r-p|=\frac12|m-p|}.
\]

Every recruitment step places pre-selection high-trait mass exactly halfway between resident trait mass and high-allele frequency.

The squared mismatch contracts fourfold:

\[
(r-p)^2=\frac14(m-p)^2.
\]

## Corollary 2 — exact spatial discrepancy contraction

For patches `j=1,...,n`, let resident high-trait masses and high-allele frequencies be `m_j` and `p_j`. The recruitment operator acts patchwise:

\[
r_j-p_j=h(m_j-p_j).
\]

Therefore, for any `L_k` norm with `k>=1`,

\[
\|r-p\|_k=h\|m-p\|_k.
\]

In particular, with `h=0.5`, both maximum and mean absolute trait–allele discrepancy are halved exactly, while mean squared discrepancy is quartered:

\[
\frac1n\sum_j(r_j-p_j)^2
=\frac14\frac1n\sum_j(m_j-p_j)^2.
\]

This is an exact spatial buffering property of the declared recruitment operator.

## Corollary 3 — direction of local replenishment

For `h=0.5`,

\[
r-m=\frac12(p-m).
\]

Hence:

- if `p>m`, recruitment raises high-trait mass by exactly `(p-m)/2` before selection;
- if `p<m`, recruitment lowers high-trait mass by exactly `(m-p)/2` before selection;
- if `p=m`, recruitment leaves high-trait mass unchanged.

The operator therefore does not universally increase the high trait. Its exact role is **coherence restoration** between genetic high-allele state and phenotypic high-trait state.

## Endpoint causal evidence from the locked intervention

The theorem concerns the deterministic pre-selection recruitment operator. Its later functional consequence was tested separately in the prospectively locked pathway edge decomposition (workflow `34014537015`, artifact `9983623440`).

Fresh q-only baseline RR-minus-AA functional-loss risk was:

- generation 20: `+4.20 pp`;
- generation 40: `+4.40 pp`.

Deleting the allele-linked recruitment edge increased the RR-minus-AA contrast to:

- generation 20: `+13.20 pp`;
- generation 40: `+12.73 pp`.

The preregistered baseline-minus-deletion differences-in-differences were:

\[
DID_{20}=-9.00\ \mathrm{pp},
\qquad 95\%\ CI=[-13.29,-4.71],
\]

and

\[
DID_{40}=-8.33\ \mathrm{pp},
\qquad 95\%\ CI=[-12.53,-4.14].
\]

Both intervals are strictly negative under the predeclared rule, resolving the edge as a **countervailing buffer** of the sorting advantage.

## Mechanistic synthesis

The q-only closure now contains two analytically distinct operators with prospectively resolved endpoint consequences:

1. **q-dependent allele sorting**
   - exact update: `logit(p+) - logit(p) = log(0.75+0.4q)`;
   - strictly increases spatial q–allele sorting;
   - focused 6,000-pair deletion resolves a positive late functional-fate contribution (`DID_40=+6.883 pp`, 95% CI `[+5.800,+7.967]`).

2. **allele-linked recruitment buffering**
   - exact update: `r=(1-h)p+hm`, with `h=0.5`;
   - halves trait–allele mismatch before selection every recruitment step;
   - deleting the edge enlarges the RR disadvantage by `8–9 pp`, resolving a countervailing endpoint contribution.

The two operators therefore act in opposite mechanistic directions: local ecological selection can sort genetic state toward favourable interaction environments, while recruitment restores coherence between genetic and trait state and thereby buffers mismatch produced elsewhere in the life cycle.

## Claim ceiling

The mismatch-contraction theorem is exact for the declared two-kernel recruitment closure. The endpoint effect is a prospectively locked finite-model causal result. Neither establishes that natural recruitment universally halves eco-genetic mismatch, nor that this recruitment architecture is Mendelian inheritance, mutation or a universal biological law.
