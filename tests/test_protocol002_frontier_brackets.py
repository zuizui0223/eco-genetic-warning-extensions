import json

from eco_genetic_warning_extensions.protocol002_frontier_brackets import frontier_brackets


def fake_batch(index: int, *, p_star: float, rates) -> dict:
    pooled = None if any(rate is None for rate in rates) else sum(rates) / len(rates)
    return {
        "campaign": {"batch_index": index},
        "cell": {
            "batch_index": index,
            "kappa_mu": 0.20,
            "p_star": p_star,
            "area_reference": 1.0,
            "kappa": 4.5,
            "horizon": 120,
            "normalised_barrier_increase": 0.30,
        },
        "seed_blocks": [
            {"master_seed": 20270310 + i, "trait_loss_rate": rate}
            for i, rate in enumerate(rates)
        ],
        "pooled_trait_loss_rate": pooled,
    }


def test_frontier_brackets_require_adjacent_pstar_and_identical_other_conditions(tmp_path) -> None:
    rows = []
    for index in range(810):
        if index == 0:
            rows.append(fake_batch(index, p_star=0.25, rates=(0.8, 0.8, 0.8, 0.8, 0.8)))
        elif index == 1:
            rows.append(fake_batch(index, p_star=0.50, rates=(0.2, 0.4, 0.8, 0.6, 0.2)))
        elif index < 648:
            # Make the remaining complete records duplicates in p_star identity but
            # irrelevant for frontier extraction; each batch remains a complete candidate.
            row = fake_batch(index, p_star=0.10, rates=(0.8, 0.8, 0.8, 0.8, 0.8))
            row["cell"]["area_reference"] = 1.2
            row["cell"]["kappa"] = 6.0
            row["cell"]["normalised_barrier_increase"] = 0.45
            rows.append(row)
        else:
            rows.append(fake_batch(index, p_star=0.10, rates=(0.8, 0.8, None, 0.8, 0.8)))

    for index, row in enumerate(rows):
        (tmp_path / f"batch_{index:03d}.json").write_text(json.dumps(row), encoding="utf-8")

    artifact = frontier_brackets(tmp_path.glob("batch_*.json"))
    matches = [row for row in artifact["brackets"] if row["low_batch_index"] == 0]
    assert len(matches) == 1
    bracket = matches[0]
    assert bracket["low_p_star"] == 0.25
    assert bracket["high_p_star"] == 0.50
    assert bracket["bracket_type"] == "rapid_to_heterogeneous"
    assert artifact["warning_fields_inspected"] is False
    assert artifact["diversity_fields_inspected"] is False
