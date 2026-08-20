"""Coordinate system and exact diversity identities for recurrent transitions.

The coordinates separate transition-map relaxation strength from its directional
equilibrium. They intentionally do not claim to hold the frequency-dependent
expected transition flux constant.

The exact identities in this module describe one affine transition step with
fixed patch weights. They are Type-T algebraic boundaries for the declared
operator, not dynamic early-warning theorems.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .asymmetric_mutation import AsymmetricMutation


def heterozygosity(frequency: float) -> float:
    """Return single-locus expected heterozygosity ``H(p)=2p(1-p)``."""
    p = float(frequency)
    if not 0.0 <= p <= 1.0:
        raise ValueError("frequency must lie in [0, 1]")
    return 2.0 * p * (1.0 - p)


def _normalised_weights(weights: Sequence[float]) -> tuple[float, ...]:
    values = tuple(float(value) for value in weights)
    if not values or any(value < 0.0 for value in values):
        raise ValueError("weights must be nonempty and nonnegative")
    total = sum(values)
    if total <= 0.0:
        raise ValueError("weights must have positive total")
    return tuple(value / total for value in values)


def alpha_gamma_diversity(
    frequencies: Sequence[float],
    weights: Sequence[float],
) -> tuple[float, float]:
    """Return the parent model's ``(H_alpha, H_gamma)`` for fixed weights."""
    ps = tuple(float(value) for value in frequencies)
    ws = _normalised_weights(weights)
    if len(ps) != len(ws) or not ps:
        raise ValueError("frequencies and weights must have the same nonzero length")
    if any(not 0.0 <= p <= 1.0 for p in ps):
        raise ValueError("frequencies must lie in [0, 1]")
    p_bar = sum(weight * p for weight, p in zip(ws, ps))
    h_alpha = sum(weight * heterozygosity(p) for weight, p in zip(ws, ps))
    h_gamma = heterozygosity(p_bar)
    return h_alpha, h_gamma


@dataclass(frozen=True)
class MutationCoordinates:
    """A recurrent-transition operator expressed as ``(kappa_mu, p_star)``."""

    kappa_mu: float
    p_star: float

    def __post_init__(self) -> None:
        if not 0.0 < float(self.kappa_mu) <= 1.0:
            raise ValueError("kappa_mu must lie in (0, 1]")
        if not 0.0 <= float(self.p_star) <= 1.0:
            raise ValueError("p_star must lie in [0, 1]")

    @property
    def low_to_high(self) -> float:
        return self.kappa_mu * self.p_star

    @property
    def high_to_low(self) -> float:
        return self.kappa_mu * (1.0 - self.p_star)

    @property
    def contraction_factor(self) -> float:
        return 1.0 - self.kappa_mu

    @property
    def is_symmetric(self) -> bool:
        return self.p_star == 0.5

    def mutation(self) -> AsymmetricMutation:
        return AsymmetricMutation(self.low_to_high, self.high_to_low)

    def apply(self, frequency: float) -> float:
        """Apply ``M(p)=kappa_mu*p_star+(1-kappa_mu)*p``."""
        return self.mutation().apply(frequency)

    def expected_flux(self, frequency: float) -> float:
        """Return ``J(p)=u_LH(1-p)+u_HL p`` at the current frequency."""
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
        return heterozygosity(self.apply(frequency))

    def heterozygosity_change(self, frequency: float) -> float:
        """Return the exact one-step change ``H(M(p))-H(p)``.

        With ``s=p_star`` and ``k=kappa_mu``:
        ``2*k*(s-p)*(1-2*p-k*(s-p))``.
        """
        p = float(frequency)
        if not 0.0 <= p <= 1.0:
            raise ValueError("frequency must lie in [0, 1]")
        displacement = self.kappa_mu * (self.p_star - p)
        return 2.0 * displacement * (1.0 - 2.0 * p - displacement)

    def heterozygosity_pstar_derivative(self, frequency: float) -> float:
        """Return ``d H(M(p))/d p_star = 2*kappa_mu*(1-2*M(p))``."""
        return 2.0 * self.kappa_mu * (1.0 - 2.0 * self.apply(frequency))

    def diversity_after_transition(
        self,
        frequencies: Sequence[float],
        weights: Sequence[float],
    ) -> tuple[float, float]:
        """Return ``(H_alpha, H_gamma)`` after applying M patchwise."""
        return alpha_gamma_diversity(tuple(self.apply(p) for p in frequencies), weights)

    def diversity_pstar_derivative(
        self,
        frequencies: Sequence[float],
        weights: Sequence[float],
    ) -> float:
        """Return the common p_star derivative of post-transition H_alpha/H_gamma.

        For fixed patch weights and a common affine operator,
        ``d H_alpha'/d p_star = d H_gamma'/d p_star`` and both equal
        ``2*kappa_mu*(1-2*M(p_bar))``.
        """
        ps = tuple(float(value) for value in frequencies)
        ws = _normalised_weights(weights)
        if len(ps) != len(ws) or not ps:
            raise ValueError("frequencies and weights must have the same nonzero length")
        if any(not 0.0 <= p <= 1.0 for p in ps):
            raise ValueError("frequencies must lie in [0, 1]")
        p_bar = sum(weight * p for weight, p in zip(ws, ps))
        return self.heterozygosity_pstar_derivative(p_bar)

    def expected_alpha_gamma_gap_after_transition(
        self,
        frequencies: Sequence[float],
        weights: Sequence[float],
    ) -> float:
        """Return the exact post-transition ``H_gamma-H_alpha`` gap.

        The identity is
        ``gap_after = (1-kappa_mu)^2 * gap_before``.
        Direction ``p_star`` drops out entirely because a common affine shift
        changes the weighted mean but not among-patch deviations from that mean.
        """
        h_alpha, h_gamma = alpha_gamma_diversity(frequencies, weights)
        return self.contraction_factor**2 * (h_gamma - h_alpha)

    @classmethod
    def from_directional_rates(cls, *, low_to_high: float, high_to_low: float) -> "MutationCoordinates":
        operator = AsymmetricMutation(low_to_high, high_to_low)
        equilibrium = operator.mutation_only_equilibrium
        if equilibrium is None:
            raise ValueError("the identity mutation operator has no identifiable p_star")
        return cls(kappa_mu=operator.total_pressure, p_star=equilibrium)


PRIMARY_KAPPA_MU = (0.05, 0.20, 0.35)
PRIMARY_P_STAR = (0.10, 0.25, 0.50, 0.75, 0.90)


def primary_phase_grid() -> tuple[MutationCoordinates, ...]:
    return tuple(
        MutationCoordinates(kappa_mu=kappa_mu, p_star=p_star)
        for kappa_mu in PRIMARY_KAPPA_MU
        for p_star in PRIMARY_P_STAR
    )
