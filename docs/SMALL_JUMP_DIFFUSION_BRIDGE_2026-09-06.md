# Small-jump trait-bin mutation -> mesoscopic diffusion bridge

This extension strengthens the earlier small-jump trait-bin module without
modifying the locked `eco-genetic-criticality` parent simulator.

Implementation:

```text
src/eco_genetic_warning_extensions/small_jump_diffusion_bridge.py
tests/test_small_jump_diffusion_bridge.py
```

---

## 1. Radius-one mutation operator

Let `f_i` be trait-bin mass on equally spaced bins with spacing `h`. For an
interior source bin, the registered radius-one mutation operator keeps
`1-mu` of the mass in place and sends `mu/2` to each adjacent bin.

For a strict-interior target bin `i`, therefore

```text
f_i'
=(1-mu)f_i
 +(mu/2)f_{i-1}
 +(mu/2)f_{i+1}.
```

Hence

```text
(f_i'-f_i)/Delta t
=
(mu/(2 Delta t))
(f_{i-1}-2f_i+f_{i+1}).
```

Define

```text
D=mu h^2/(2 Delta t).
```

Then exactly

```text
(f_i'-f_i)/Delta t
=
D (f_{i-1}-2f_i+f_{i+1})/h^2.
```

This is an exact finite-difference identity on the strict interior. The only
continuum approximation is the later statement that the centered second
difference converges to a second derivative as `h -> 0` for a sufficiently
smooth density.

---

## Theorem SJD1 — exact strict-interior diffusion identity

For radius-one mutation on an equally spaced trait grid, every bin at least two
indices away from a finite boundary obeys

```text
G_mu f_i = D Delta_h f_i
```

with

```text
G_mu f_i=(f_i'-f_i)/Delta t,
D=mu h^2/(2 Delta t),
Delta_h f_i=(f_{i-1}-2f_i+f_{i+1})/h^2.
```

The executable audit computes the residual of this identity and requires it to
be zero to numerical tolerance.

---

## 2. Diffusive scaling

If grid spacing is refined while `mu`, `Delta t`, and the radius in bins are all
held fixed, then

```text
D proportional to h^2
```

and the mutation contribution collapses toward zero in physical trait units.

Therefore a non-degenerate diffusion limit requires a diffusive scaling. For a
target physical diffusion coefficient `D_target`, choose

```text
Delta t
=mu h^2/(2 D_target).
```

The helper

```text
diffusive_time_step(...)
```

implements this scaling exactly.

This is the precise content behind the earlier informal "small jumps become a
Fokker--Planck diffusion" statement.

---

## 3. Boundary caveat is part of the result

The current finite-bin mutation operator truncates and renormalises its
neighbour set at the endpoints. An endpoint source sends all mutated mass to its
single available inward neighbour, whereas an interior source splits mutated
mass between two neighbours.

Consequently, bins adjacent to a boundary do **not** obey the same centered
Laplacian identity without an additional boundary correction.

The audit therefore checks only indices

```text
2,...,n-3.
```

It does not silently label the current parent-compatible finite-bin rule as a
Neumann, reflecting, absorbing, or other continuum boundary condition.

That boundary condition must be declared and derived separately before a full
PDE claim is made.

---

## 4. Cross-repository meaning

The resulting hierarchy is now explicit:

```text
finite eco-genetic trait bins
        |
        | radius-one local mutation
        v
exact interior discrete diffusion generator
        |
        | h -> 0 under Delta t ~ h^2
        v
mesoscopic trait-density diffusion term.
```

This is complementary to `payoff`:

```text
payoff
-> architecture density and frequency-dependent selection landscape;

eco-genetic-warning-extensions
-> explicit finite trait-bin state and exact local-mutation diffusion bridge.
```

The two should not yet be collapsed into one simulator. A future bridge must
first align the biological state coordinate, selection term, time scale and
boundary semantics.

---

## Claim boundary

This result does not claim that the locked parent simulator already implements
trait mutation, nor that its finite endpoints correspond to any particular PDE
boundary condition. It also does not prove convergence of the entire
selection-demography-genetics process to one continuum PDE.

The positive claim is narrower and exact:

> once radius-one local trait mutation is prospectively added, its strict-
> interior generator is exactly a discrete diffusion operator, with physical
> diffusion coefficient `D=mu h^2/(2 Delta t)`.
