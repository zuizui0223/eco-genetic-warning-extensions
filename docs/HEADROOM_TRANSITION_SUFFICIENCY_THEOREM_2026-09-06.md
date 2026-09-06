# Headroom as an exact transition-sufficient coordinate

Status: **constructive transition-sufficiency theorem** for the declared interaction update. This provides a positive counterpart to the matched-marginal non-sufficiency result.

## 1. Earlier negative result

The state-validity construction showed that a coarse representation `phi(X)` containing conventional ecological and genetic marginals can satisfy

\[
\phi(X_A)=\phi(X_B)
\]

while the exact next interaction states differ,

\[
T_I(X_A)\ne T_I(X_B).
\]

Hence no map `g` defined only on those retained marginals can satisfy `T_I=g o phi` for all admissible states.

That result identifies what the conventional representation loses, but not what representation is sufficient.

## 2. Constructive sufficient coordinate

For each patch define route headroom at target `c`:

\[
H_j(X;c)=a_jd_jS_j-\theta-\frac{\operatorname{logit}(c)}{\kappa},
\]

where

\[
S_j=0.6q_j+0.3T_j+0.1G_j
\]

for the locked full-feedback weights.

Let

\[
\psi(X)=(H_1,\ldots,H_n).
\]

The interaction update can then be written exactly as

\[
\boxed{
T_I(X)_j
=\sigma\{\operatorname{logit}(c)+\kappa H_j\}.
}
\]

Therefore define

\[
g(h_1,\ldots,h_n)
=\left(
\sigma[\operatorname{logit}(c)+\kappa h_1],\ldots,
\sigma[\operatorname{logit}(c)+\kappa h_n]
\right).
\]

Then, for every admissible explicit state under the declared interaction update,

\[
\boxed{T_I=g\circ\psi.}
\]

Thus the patchwise headroom vector is an exact **transition-sufficient coordinate** for the next interaction field.

## 3. Why this is relational

Headroom is not a layer-wise marginal. Each patch combines

- local interaction state q;
- realised high-trait state T;
- high-allele state G;
- local density d;
- area ratio a;
- the current forcing boundary theta.

The matched-marginal AA/RR states differ precisely because they generate different headroom vectors even though their conventional marginal summaries are identical. At the opening full-feedback state,

- AA: `H=(-.1460,-.0060,.1340,.2740)`;
- RR: `H=(.0940,.0740,.0540,.0340)`.

Their means are equal, but their patchwise relational coordinates are not, so their exact next interaction fields differ.

## 4. What is and is not established

This theorem does **not** claim that headroom is a unique or minimal state representation. Many invertible transformations of H are equally sufficient, and a richer representation can also be sufficient.

Nor is patchwise H alone sufficient for the complete multi-generation eco-genetic trajectory. Trait recruitment, allele drift, demographic updates and later forcing require additional state information. The theorem is target-specific:

> the headroom vector is sufficient for the **one-step interaction transition** under the declared update.

This target specificity is exactly the point. A representation should be called a state coordinate only relative to the transition or endpoint it is required to determine.

## 5. Positive state-validity synthesis

The combined constructive result is therefore stronger than “marginals are insufficient”:

\[
\boxed{
\text{conventional marginals are not transition-sufficient,}
\qquad
\text{patchwise relational headroom is.}
}
\]

This gives an operational answer to what information the interaction transition actually needs: not the separate global amounts of ecological and genetic components, but their local weighted co-occurrence after density and forcing are accounted for.
