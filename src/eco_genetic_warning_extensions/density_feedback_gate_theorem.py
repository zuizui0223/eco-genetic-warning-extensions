from __future__ import annotations

import math


def sigmoid(x: float) -> float:
    x = float(x)
    if x >= 0.0:
        e = math.exp(-x)
        return 1.0 / (1.0 + e)
    e = math.exp(x)
    return e / (1.0 + e)


def interaction_next(
    interaction: float,
    density: float,
    barrier: float,
    kappa: float = 4.5,
) -> float:
    q = float(interaction)
    d = float(density)
    theta = float(barrier)
    if not 0.0 <= q <= 1.0:
        raise ValueError("interaction must lie in [0,1]")
    if not 0.0 <= d <= 1.0:
        raise ValueError("density must lie in [0,1]")
    if kappa <= 0.0:
        raise ValueError("kappa must be positive")
    return sigmoid(float(kappa) * (d * q - theta))


def interaction_density_derivative(
    interaction: float,
    density: float,
    barrier: float,
    kappa: float = 4.5,
) -> float:
    qn = interaction_next(interaction, density, barrier, kappa)
    return float(kappa) * float(interaction) * qn * (1.0 - qn)


def interaction_population_derivative(
    interaction: float,
    population: float,
    capacity: float,
    barrier: float,
    kappa: float = 4.5,
) -> float:
    q = float(interaction)
    n = float(population)
    K = float(capacity)
    if K <= 0.0:
        raise ValueError("capacity must be positive")
    if n < 0.0:
        raise ValueError("population must be nonnegative")
    density = min(1.0, n / K)
    if n >= K:
        return 0.0
    return interaction_density_derivative(q, density, barrier, kappa) / K


def required_density_product(
    barrier: float,
    target_interaction: float = 0.625,
    kappa: float = 4.5,
) -> float:
    c = float(target_interaction)
    if not 0.0 < c < 1.0:
        raise ValueError("target_interaction must lie in (0,1)")
    if kappa <= 0.0:
        raise ValueError("kappa must be positive")
    return float(barrier) + math.log(c / (1.0 - c)) / float(kappa)


def minimum_density_for_target(
    interaction: float,
    barrier: float,
    target_interaction: float = 0.625,
    kappa: float = 4.5,
) -> float:
    q = float(interaction)
    if q <= 0.0:
        return math.inf
    return required_density_product(barrier, target_interaction, kappa) / q


def barrier_schedule(generation: int) -> float:
    g = int(generation)
    if g < 1:
        raise ValueError("generation must be positive")
    return 0.50 + 0.15 * g / 60.0


def continuous_population_next(
    population: float,
    next_interaction: float,
    selected_high_allele: float,
    capacity: float = 40.0,
    baseline_growth: float = 0.3,
    interaction_growth: float = 0.4,
    high_allele_growth: float = 0.1,
) -> float:
    n = float(population)
    K = float(capacity)
    if n <= 0.0 or K <= 0.0:
        raise ValueError("population and capacity must be positive")
    q = float(next_interaction)
    p = float(selected_high_allele)
    exponent = (
        float(baseline_growth)
        + float(interaction_growth) * q
        + float(high_allele_growth) * p
        - n / K
    )
    return n * math.exp(exponent)


def direct_population_q_derivative(
    population_next_value: float,
    interaction_growth: float = 0.4,
) -> float:
    return float(interaction_growth) * float(population_next_value)


def direct_two_step_loop_gain(
    interaction_t1: float,
    population_t1: float,
    interaction_t2: float,
    capacity: float = 40.0,
    kappa: float = 4.5,
    interaction_growth: float = 0.4,
) -> float:
    """Direct q -> N -> q loop gain on the unsaturated smooth branch.

    This is the product of the direct demographic partial derivative holding
    selected allele state fixed and the following density-to-q derivative.
    It is not the total derivative of the full stochastic/discrete life cycle.
    """
    q1 = float(interaction_t1)
    n1 = float(population_t1)
    q2 = float(interaction_t2)
    K = float(capacity)
    if n1 >= K:
        return 0.0
    if min(q1, n1, q2) < 0.0 or q1 > 1.0 or q2 > 1.0:
        raise ValueError("states outside declared range")
    return (
        float(kappa)
        * float(interaction_growth)
        * q1
        * n1
        * q2
        * (1.0 - q2)
        / K
    )


def gate_certificate(
    target_interaction: float = 0.625,
    kappa: float = 4.5,
) -> dict[str, object]:
    generations = (1, 20, 40)
    product = {
        str(g): required_density_product(
            barrier_schedule(g), target_interaction, kappa
        )
        for g in generations
    }
    return {
        "kappa": float(kappa),
        "target_interaction": float(target_interaction),
        "logit_target_over_kappa": math.log(
            target_interaction / (1.0 - target_interaction)
        )
        / float(kappa),
        "required_density_interaction_product": product,
        "required_density_if_q_0_8": {
            g: value / 0.8 for g, value in product.items()
        },
        "required_density_if_q_0_9": {
            g: value / 0.9 for g, value in product.items()
        },
    }
