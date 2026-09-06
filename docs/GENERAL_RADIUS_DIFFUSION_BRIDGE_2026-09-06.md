# General-radius finite-bin mutation to diffusion bridge

The small-jump extension originally registered a local trait-bin mutation
operator with radius `J` bins.  The radius-one case has an exact strict-interior
nearest-neighbour diffusion identity.  This note generalizes that identity to
arbitrary finite `J`.

For a strict interior bin `i`, symmetric mutation rate `mu`, radius `J`, and
step duration `Delta t`, the finite operator satisfies exactly

```text
(f_i' - f_i) / Delta t
=
mu/(2 J Delta t)
* sum_{k=1}^J [f_{i-k} + f_{i+k} - 2 f_i].
```

This is a finite nonlocal stencil, not yet a continuum PDE.

Taylor expansion for a smooth density with grid spacing `h` gives

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

Thus for fixed `mu` and `J`, holding physical `D` fixed requires

```text
Delta t proportional to h^2.
```

Under that scaling, `C4` is `O(h^2)`.  Halving `h` therefore quarters the first
registered higher-order correction.

Implementation:

```text
src/eco_genetic_warning_extensions/general_radius_diffusion.py
tests/test_general_radius_diffusion.py
```

The tests verify the exact finite-stencil identity for `J=1,2,3`, recover the
previous radius-one diffusion coefficient, and verify the expected refinement
scaling.

## Boundary condition remains a separate contract

The strict-interior identity does not determine a continuum boundary condition.
The finite trait-bin implementation truncates and renormalises mutation near the
represented trait limits.  Whether a continuum application should use
reflecting, absorbing, flux, moving, or biologically constrained boundaries is
not inferred from the interior expansion and must be declared separately.

## Claim boundary

This bridge is a mathematical property of the prospective extension operator.
It does not retroactively add mutation to the locked parent simulator and does
not assert that a natural trait distribution obeys a Fokker--Planck equation.
