# Finite-patch headroom extreme bound

Status: **exact finite-dimensional inequality** for any set of patch headrooms. This theorem explains what increased headroom variance necessarily implies at fixed mean; it does not by itself establish that greater variance improves eventual function.

## Theorem

Let `H_1,...,H_n` be real patch headrooms with `n>=2`, mean

\[
\mu=\frac1n\sum_i H_i
\]

and population variance

\[
v=\frac1n\sum_i(H_i-\mu)^2.
\]

Then

\[
\boxed{
\max_i(H_i-\mu)\ge\sqrt{\frac{v}{n-1}}
}
\]

and, symmetrically,

\[
\boxed{
\max_i(\mu-H_i)\ge\sqrt{\frac{v}{n-1}}.
}
\]

Both bounds are sharp.

## Proof

Write `x_i=H_i-mu`, so `sum_i x_i=0`. Let

\[
M=\max_i x_i\ge0.
\]

Let `P` be the sum of all positive `x_i`. Because each positive value is at most `M` and at most `n-1` entries can be positive when variance is nonzero,

\[
P\le(n-1)M.
\]

For positive entries, `x_i^2<=M x_i`, so their squared sum is at most `MP`. The negative entries have total absolute mass `P`; concentrating all that mass into one negative entry maximizes their squared sum, giving at most `P^2`. Therefore

\[
\sum_i x_i^2\le MP+P^2
\le M(n-1)M+(n-1)^2M^2
=n(n-1)M^2.
\]

Dividing by `n`,

\[
v\le(n-1)M^2,
\]

hence

\[
M\ge\sqrt{v/(n-1)}.
\]

Applying the same argument to `-x_i` proves the lower-tail inequality. The upper bound is attained by `n-1` values equal to `M` and one value equal to `-(n-1)M`; reversing signs attains the lower bound.

## Application to the matched-marginal headroom construction

The AA and RR opening states have the same mean headroom but variances

\[
v_{AA}=0.0245,\qquad v_{RR}=0.0005,
\]

so

\[
\frac{v_{AA}}{v_{RR}}=49.
\]

The guaranteed extreme-deviation scales are therefore in the ratio

\[
\boxed{
\sqrt{49}=7.
}
\]

For four patches, the theorem guarantees deviations from the common mean of at least

\[
\sqrt{0.0245/3}=0.09037
\]

for AA and

\[
\sqrt{0.0005/3}=0.01291
\]

for RR on both the upper and lower sides.

The actual construction is even more structured: AA upper and lower deviations from mean headroom are `0.21`, whereas RR deviations are `0.03`, an exact **7-fold amplitude ratio**. Thus the observed 49-fold variance difference corresponds here to a sevenfold widening of both local reserve and local sacrifice around the same mean.

## Ecological meaning

At fixed mean route headroom, variance cannot increase without creating stronger extremes. It necessarily buys some deeper upper-tail reserve while simultaneously allowing a deeper lower-tail deficit. This gives a general mathematical basis for the **coverage–reserve / reserve–sacrifice trade-off** seen in the four-patch construction.

The theorem does **not** say that larger variance is beneficial. Whether a deep upper-tail reserve outweighs sacrificed patches depends on the endpoint, later sorting, recruitment, recoupling, density feedback, movement and stochasticity. Its role is narrower: it proves that spatial variance changes the geometry of available headroom even when the mean is fixed.
