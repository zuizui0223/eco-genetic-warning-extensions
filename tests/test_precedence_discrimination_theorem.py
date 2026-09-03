from __future__ import annotations

import csv
import math
from pathlib import Path

from eco_genetic_warning_extensions.precedence_discrimination import (
    binary_marker_auc,
    perfect_precedence_binary_audit,
)

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ENSEMBLES = {"inherited_202611", "fresh_202911"}


def pairwise_auc(event_scores, non_event_scores):
    wins = ties = total = 0
    for positive in event_scores:
        for negative in non_event_scores:
            total += 1
            if positive > negative:
                wins += 1
            elif positive == negative:
                ties += 1
    return (wins + 0.5 * ties) / total


def test_perfect_precedence_allows_every_finite_specificity_grid_point():
    n1 = 7
    n0 = 11
    observed = []
    for false_positives in range(n0 + 1):
        audit = perfect_precedence_binary_audit(
            event_count=n1,
            non_event_count=n0,
            marker_positive_non_events=false_positives,
        )
        observed.append(audit.specificity)
        assert audit.sensitivity == 1.0
        assert math.isclose(audit.specificity, (n0 - false_positives) / n0)
    assert observed == [j / n0 for j in range(n0, -1, -1)]


def test_binary_auc_identity_matches_independent_pairwise_ranking_oracle():
    for n1 in (2, 5):
        for n0 in (3, 7):
            for false_positives in range(n0 + 1):
                event_scores = [1] * n1
                non_event_scores = [1] * false_positives + [0] * (n0 - false_positives)
                specificity = (n0 - false_positives) / n0
                expected = pairwise_auc(event_scores, non_event_scores)
                assert math.isclose(
                    binary_marker_auc(sensitivity=1.0, specificity=specificity),
                    expected,
                    rel_tol=0,
                    abs_tol=1e-12,
                )


def test_same_perfect_precedence_spans_chance_to_perfect_binary_auc():
    n1, n0 = 5, 10
    aucs = [
        perfect_precedence_binary_audit(
            event_count=n1,
            non_event_count=n0,
            marker_positive_non_events=f,
        ).binary_auc
        for f in range(n0 + 1)
    ]
    assert min(aucs) == 0.5
    assert max(aucs) == 1.0
    assert len(set(aucs)) == n0 + 1


def test_all_non_events_positive_is_sharp_chance_discrimination_endpoint():
    audit = perfect_precedence_binary_audit(
        event_count=35,
        non_event_count=48,
        marker_positive_non_events=48,
    )
    assert audit.sensitivity == 1.0
    assert audit.specificity == 0.0
    assert audit.binary_auc == 0.5
    assert math.isclose(audit.positive_predictive_value, 35 / 83)


def test_locked_warning_table_realizes_sharp_endpoint_for_all_six_rules_in_both_source_ensembles():
    path = ROOT / "manuscript/tables/warning_validity_audit.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        all_rows = list(csv.DictReader(handle))

    # The publication table also contains a six-row combined_descriptive block.
    # The theorem application is source-ensemble specific: inherited and fresh
    # were generated independently and are never pooled for replication claims.
    rows = [row for row in all_rows if row["ensemble"] in SOURCE_ENSEMBLES]
    assert len(all_rows) == 18
    assert len(rows) == 12

    grouped = {}
    for row in rows:
        grouped.setdefault(row["ensemble"], []).append(row)
        event_count = int(row["events"])
        non_event_count = int(row["right_censored_non_events"])
        false_positive_rate = float(row["non_event_false_positive_rate"])
        assert false_positive_rate == 1.0
        audit = perfect_precedence_binary_audit(
            event_count=event_count,
            non_event_count=non_event_count,
            marker_positive_non_events=non_event_count,
        )
        assert float(row["lead_sensitivity"]) == audit.sensitivity == 1.0
        assert float(row["full_horizon_specificity"]) == audit.specificity == 0.0
        assert float(row["full_horizon_binary_auc"]) == audit.binary_auc == 0.5
        assert math.isclose(float(row["full_horizon_ppv"]), audit.positive_predictive_value)

    assert set(grouped) == SOURCE_ENSEMBLES
    assert {len(v) for v in grouped.values()} == {6}
    denominators = {
        ensemble: (int(items[0]["events"]), int(items[0]["right_censored_non_events"]))
        for ensemble, items in grouped.items()
    }
    assert denominators == {
        "inherited_202611": (35, 48),
        "fresh_202911": (33, 49),
    }
