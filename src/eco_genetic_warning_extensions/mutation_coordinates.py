"""Coordinate system for Protocol 002 recurrent-transition phase diagrams.

The coordinates separate transition-map relaxation strength from its directional
equilibrium. They intentionally do not claim to hold the frequency-dependent
expected transition flux constant.

This module also records the exact one-step heterozygosity consequence of the
affine transition operator. That result is a local algebraic boundary, not a
dynamic early-warning theorem.
"""
from __future__ import annotations

from dataclasses import dataclass

from .asymmetric_mutation import AsymmetricMutation


def heterozygosity(frequency: float) -> float:
    """Return single-locus expected heterozygosity ``H(p)=2p(1-p)``."""
    p = float(frequency)
    if not 0.0 <= p <= 1.0:
        raise ValueError("frequency must lie in [0, 1]")
    return 2.0 * p * (1.0 - p)


@dataclass(frozen=True)
class MutationCoordinates:
    """A recurrent-transition operator expressed as ``(kappa_mu, p_star)``.

    Parameters
    ----------
    kappa_mu:
        Sum of directional transition probabilities. It controls the contraction
        factor of the transition map, ``1 - kappa_mu``.
    p_star:
        Transition-only equilibrium frequency of the high-trait-associated allele.
        It is identifiable only when ``kappa_mu > 0``.
    """

    kappa_mu: float
    p_star: float

    def __post_init__(self) -> None:
        if not 0.0 < float(self.kappa_mu) <= 1.0:
            raise ValueError("kappa_mu must lie in (0, 1]")
        if not 0.0 <= float(self.p_star) <= 1.0:
            raise ValueError("p_star must lie in [0, 1]")

    @property
    def low_to_high(self) -> float:
        """Return directional rate u_LH = kappa_mu * p_star."""
        return self.kappa_mu * self.p_star

    @property
    def high_to_low(self) -> float:
        """Return directional rate u_HL = kappa_mu * (1 - p_star)."""
        return self.kappa_mu * (1.0 - self.p_star)

    @property
    def contraction_factor(self) -> float:
        """Slope of the affine transition map."""
        return 1.0 - self.kappa_mu

    @property
    def is_symmetric(self) -> bool:
        """Whether directional rates are equal."""
        return self.p_star == 0.5

    def mutation(self) -> AsymmetricMutation:
        """Return the Protocol 001/002 operator in directional-rate form."""
        return AsymmetricMutation(self.low_to_high, self.high_to_low)

    def apply(self, frequency: float) -> float:
        """Apply ``M(p) = kappa_mu*p_star + (1-kappa_mu)*p``."""
        return self.mutation().apply(frequency)

    def expected_flux(self, frequency: float) -> float:
        """Return ``J(p)=u_LH(1-p)+u_HL p`` at the current frequency.

        This is allowed to vary across directionality coordinates even when
        ``kappa_mu`` is fixed.
        """
        p = float(frequency)
        if not 0.0 <= p <= 1.0:
            raise ValueError("frequency must lie in [0, 1]")
        return self.low_to_high * (1.0 - p) + self.high_to_low * p

    def pre_mutation_threshold(self, post_mutation_threshold: float) -> float:
        """Return p needed for M(p) >= p_c, for ``kappa_mu < 1``."""
        threshold = float(post_mutation_threshold)
        if not 0.0 <= threshold <= 1.0:
            raise ValueError("post_mutation_threshold must lie in [0, 1]")
        if self.kappa_mu == 1.0:
            raise ValueError("pre-mutation threshold is undefined when kappa_mu is 1")
        return (threshold - self.kappa_mu * self.p_star) / self.contraction_factor

    def heterozygosity_after_transition(self, frequency: float) -> float:
        """Return ``H(M(p))`` for the exact one-step affine transition."""
        return heterozygosity(self.apply(frequency))

    def heterozygosity_change(self, frequency: float) -> float:
        """Return the exact one-step change ``H(M(p))-H(p)``.

        With ``s=p_star`` and ``k=kappa_mu``, the closed form is

        ``2*k*(s-p)*(1-2*p-k*(s-p))``.

        Its sign is positive when the transition moves the allele frequency
        closer to 0.5, negative when it moves it farther away, and zero when
        heterozygosity is unchanged. Therefore transition direction alone has no
        universal signed effect on diversity without a state constraint.
        """
        p = float(frequency)
        if not 0.0 <= p <= 1.0:
            raise ValueError("frequency must lie in [0, 1]")
        displacement = self.kappa_mu * (self.p_star - p)
        return 2.0 * displacement * (1.0 - 2.0 * p - displacement)

    def heterozygosity_pstar_derivative(self, frequency: float) -> float:
        """Return ``d H(M(p)) / d p_star = 2*kappa_mu*(1-2*M(p))``.

        The derivative changes sign at ``M(p)=0.5``. This is the exact local
        non-monotonicity boundary behind the absence of a universal
        direction-to-diversity sign.
        """
        return 2.0 * self.kappa_mu * (1.0 - 2.0 * self.apply(frequency))

    @classmethod
    def from_directional_rates(cls, *, low_to_high: float, high_to_low: float) -> "MutationCoordinates":
        """Recover phase coordinates from an admissible non-identity operator."""
        operator = AsymmetricMutation(low_to_high, high_to_low)
        equilibrium = operator.mutation_only_equilibrium
        if equilibrium is None:
            raise ValueError("the identity mutation operator has no identifiable p_star")
        return cls(kappa_mu=operator.total_pressure, p_star=equilibrium)


PRIMARY_KAPPA_MU = (0.05, 0.20, 0.35)
PRIMARY_P_STAR = (0.10, 0.25, 0.50, 0.75, 0.90)


def primary_phase_grid() -> tuple[MutationCoordinates, ...]:
    """Return the 15 predeclared Protocol 002 coordinates in stable order."""
    return tuple(
        MutationCoordinates(kappa_mu=kappa_mu, p_star=p_star)
        for kappa_mu in PRIMARY_KAPPA_MU
        for p_star in PRIMARY_P_STAR
    )
