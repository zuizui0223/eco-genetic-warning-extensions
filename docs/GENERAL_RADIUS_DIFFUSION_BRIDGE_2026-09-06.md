# General-radius finite-bin mutation to diffusion bridge

The small-jump extension registers a source-normalised local trait-bin mutation
operator with radius `J` bins.  For arbitrary finite `J`, the translation-
invariant stencil is exact only sufficiently far from both represented trait
boundaries.

## Exact finite stencil and the 2J-deep interior

A destination bin `i` receives mutation inflow from source bins within `J` bins.
Because each source redistributes its mutated mass over the neighbours available
to that source, a source within `J` bins of a finite boundary has a truncated and
renormalised kernel.  Therefore it is not enough for the destination itself to
be `J` bins from the boundary: every source feeding it must also have a full
neighbourhood.

The translation-invariant identity is exact when `i` is at least `2J` bins from
each boundary:

```text
(f_i' - f_i) / Delta t
=
mu/(2 J Delta t)
* sum_{k=1}^J [f_{i-k} + f_{i+k} - 2 f_i].
```

Thus source-side boundary renormalisation creates a boundary-influence layer of
up to `2J` destination bins for this particular finite operator.

## Local continuum expansion for fixed J

Taylor expansion in the `2J`-deep interior gives

```text
partial_t f
= D partial_zz f
  + C4 partial_zzzz f
  + higher orders,
```

with

```text
D
= mu h^2 (J+1)(2J+1) / (12 Delta t)
```

and

```text
C4
= mu h^4 /(24 J Delta t) * sum_{k=1}^J k^4.
```

For fixed `mu` and fixed integer `J`, holding physical `D` fixed requires

```text
Delta t proportional to h^2.
```

Under that scaling, `C4=O(h^2)`.  Halving `h` quarters the first registered
higher-order correction, giving the local-diffusion regime.

Implementation:

```text
src/eco_genetic_warning_extensions/general_radius_diffusion.py
tests/test_general_radius_diffusion.py
```

The tests verify the exact finite-stencil identity for `J=1,2,3` only in the
`2J`-deep interior, explicitly reject a boundary-influenced destination, recover
the previous radius-one diffusion coefficient, and verify refinement scaling.

## A different scaling produces a nonlocal limit

The statement above keeps `J` fixed while `h` shrinks.  If instead the physical
jump radius

```text
rho = J h
```

is held positive while `h -> 0` and `J -> infinity`, the continuum object is not
the same diffusion limit.  The finite stencil approaches the uniform finite-
range jump generator

```text
L_rho f(z)
= mu/Delta t * [
    (1/(2 rho)) integral_{-rho}^{rho} f(z+s) ds
    - f(z)
  ].
```

Its moment expansion has non-vanishing limits

```text
D  -> mu rho^2/(6 Delta t)
C4 -> mu rho^4/(120 Delta t).
```

Because `C4` stays positive when `rho` stays positive, grid refinement alone
does not justify truncating the process to local diffusion.  The physical jump
range must itself shrink for the local PDE limit.

See:

```text
src/eco_genetic_warning_extensions/mutation_scaling_regimes.py
tests/test_mutation_scaling_regimes.py
```

## Boundary condition remains a separate contract

Neither interior regime determines the finite-domain continuum boundary law.
Reflecting, absorbing, flux, moving, or biologically constrained endpoints must
still be declared separately.

## Claim boundary

These bridges are mathematical properties of the prospective extension
operator.  They do not retroactively add mutation to the locked parent simulator
and do not assert that a natural trait distribution follows either a diffusion
PDE or the nonlocal jump equation.  The scaling regime and boundary contract are
part of the scientific model definition.
