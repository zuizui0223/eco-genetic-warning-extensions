"""Protocol 001's only changed biological closure.

The operator is applied after selection/migration and before finite drift, matching
that lifecycle position in the predecessor closure. This module does not implement
or alter the upstream simulator; it supplies a testable replacement operator only.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isclose


@dataclass(frozen=True)
class AsymmetricMutation:
    """Directional recurrent mutation rates in closure units.

    ``low_to_high`` is u_{L->H}; ``high_to_low`` is u_{H->L}. Rates are
    probabilities for one update and must sum to at most one.
    """

    low_to_high: float
    high_to_low: float

    def __post_init__(self) -> None:
        for name, value in (("low_to_high", self.low_to_high), ("high_to_low", self.high_to_low)):
            if not 0.0 <= float(value) <= 1.0:
                raise ValueError(f"{name} must lie in [0, 1]")
        if self.total_pressure > 1.0:
            raise ValueError("low_to_high + high_to_low must be at most 1")

    @property
    def total_pressure(self) -> float:
        """One-generation mutation turnover, u_LH + u_HL."""
        return float(self.low_to_high + self.high_to_low)

    @property
    def mutation_only_equilibrium(self) -> float | None:
        """Fixed point of mutation alone, or None for the identity operator."""
        return None if self.total_pressure == 0.0 else self.low_to_high / self.total_pressure

    @property
    def contraction_factor(self) -> float:
        """Slope of the mutation map; equals 1 - total mutation pressure."""
        return 1.0 - self.total_pressure

    def apply(self, frequency: float) -> float:
        """Apply p' = u_LH + (1 - u_LH - u_HL) p."""
        p = float(frequency)
        if not 0.0 <= p <= 1.0:
            raise ValueError("frequency must lie in [0, 1]")
        result = self.low_to_high + self.contraction_factor * p
        # Floating-point rounding should never manufacture an out-of-domain state.
        return min(1.0, max(0.0, result))

    def is_symmetric(self) -> bool:
        return isclose(self.low_to_high, self.high_to_low, rel_tol=0.0, abs_tol=1e-15)


def mutate_frequency(frequency: float, *, low_to_high: float, high_to_low: float) -> float:
    """Convenience wrapper for the declared Protocol 001 mutation operator."""
    return AsymmetricMutation(low_to_high, high_to_low).apply(frequency)
