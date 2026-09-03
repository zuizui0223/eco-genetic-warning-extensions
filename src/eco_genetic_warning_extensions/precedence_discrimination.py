"""Exact denominator consequences of perfect event-conditioned precedence."""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True)
class PerfectPrecedenceBinaryAudit:
    event_count: int
    non_event_count: int
    marker_positive_non_events: int
    sensitivity: float
    specificity: float
    binary_auc: float
    positive_predictive_value: float


def binary_marker_auc(*, sensitivity: float, specificity: float) -> float:
    """AUC of a binary score from its TPR and TNR."""
    se = float(sensitivity)
    sp = float(specificity)
    if not (isfinite(se) and isfinite(sp) and 0.0 <= se <= 1.0 and 0.0 <= sp <= 1.0):
        raise ValueError("sensitivity and specificity must lie in [0,1]")
    return 0.5 * (se + sp)


def perfect_precedence_binary_audit(
    *, event_count: int, non_event_count: int, marker_positive_non_events: int
) -> PerfectPrecedenceBinaryAudit:
    """Full-denominator metrics when every event has a preceding binary marker.

    Perfect event-conditioned precedence forces all event trajectories to be
    marker-positive by the common horizon, hence sensitivity=1.  The number of
    marker-positive non-events is otherwise unconstrained by precedence.
    """
    n1 = int(event_count)
    n0 = int(non_event_count)
    fp = int(marker_positive_non_events)
    if n1 < 1 or n0 < 1:
        raise ValueError("event_count and non_event_count must be positive")
    if fp < 0 or fp > n0:
        raise ValueError("marker_positive_non_events must lie in [0, non_event_count]")

    sensitivity = 1.0
    specificity = (n0 - fp) / n0
    auc = binary_marker_auc(sensitivity=sensitivity, specificity=specificity)
    ppv = n1 / (n1 + fp)
    return PerfectPrecedenceBinaryAudit(
        event_count=n1,
        non_event_count=n0,
        marker_positive_non_events=fp,
        sensitivity=sensitivity,
        specificity=specificity,
        binary_auc=auc,
        positive_predictive_value=ppv,
    )
