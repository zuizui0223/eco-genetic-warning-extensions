# Small-jump trait-bin bridge

**Status:** prospective extension utility; does not modify the locked scientific parent model or retroactively change any registered result.

The parent `eco-genetic-criticality` finite model already carries a realised trait distribution over a finite grid and updates it by multiplicative viability selection. Its current registered trait-bin update explicitly has no mutation or dispersal across trait bins. This note adds the missing local-mutation operator only in the extension repository.

## Finite-bin operator

Let the resident trait-bin distribution be

```text
f=(f_0,...,f_{n-1}), sum_i f_i=1.
```

After viability selection,

```text
f_i^sel propto f_i W_i.
```

A declared fraction `mu` then mutates locally. For jump radius `J`,

```text
M_ij=0 when |i-j|>J.
```

For interior source bins the mutated mass is distributed uniformly over the other bins within `J`; at the finite boundaries the available destinations are renormalised so mass does not leak outside the represented trait domain.

Implementation:

- `src/eco_genetic_warning_extensions/small_jump_trait_bins.py`
- `tests/test_small_jump_trait_bins.py`

## Why this belongs in the extension repository

The parent repository explicitly freezes its existing finite H1/H3 scientific campaign and requires new mutation models or biological closures to be separately declared extensions. This module therefore does **not** patch the parent simulator. It provides a composable operator for a new prospective experiment.

## Small-jump scaling diagnostic

For an evenly spaced interior grid with spacing `h`, mutation probability `mu`, and jump radius `J`, the implementation reports

```text
E[(Delta z)^2]
= mu * h^2 * mean(k^2, k=1,...,J).
```

A diffusion scaling diagnostic is then

```text
D = E[(Delta z)^2] / (2 Delta t).
```

This quantity is only a bridge diagnostic. It does not by itself prove that the finite ecological life cycle is governed by a Fokker–Planck PDE.

## Prospective experiment enabled by the bridge

A clean next experiment can cross

```text
mutation rate mu
x jump radius J
x interaction-feedback regime
x fragmentation/connectivity regime
```

while holding the already defined trait fitness surface and state-reporting distinctions fixed. The relevant outcomes are not only mean trait, but the full realised trait distribution, high-trait mass, component occupancy, demographic state and genetic state.

The key question is:

> Does a potential high-trait state remain globally viable but become dynamically inaccessible when trait mutation is constrained to sufficiently small local jumps?

That question connects the parent state-separation programme to PAYOFF's explicit distinction between global architecture value and local accessibility without merging the repositories or their claim ownership.

## Tests

```bash
pytest -q tests/test_small_jump_trait_bins.py
```

The tests cover probability-mass conservation, strict local support, identity at zero jump radius, compatibility with multiplicative viability selection, and the interior small-jump variance/diffusion diagnostic.
