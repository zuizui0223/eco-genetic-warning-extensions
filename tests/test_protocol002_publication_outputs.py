from eco_genetic_warning_extensions.protocol002_publication_outputs import publication_rows


def test_publication_rows_classify_coordinate_regimes():
    audit = {
        "coordinates": [
            {
                "kappa_mu": 0.2,
                "p_star": 0.5,
                "complete_candidate_count": 42,
                "incomplete_candidate_count": 12,
                "pattern_counts": {"all_below_band": 2, "mixed_across_band": 40},
                "closest_candidate_to_predeclared_band": {
                    "batch_index": 406,
                    "area_reference": 1.0,
                    "kappa": 4.5,
                    "horizon": 240,
                    "normalised_barrier_increase": 0.3,
                    "pooled_trait_loss_rate": 0.5238095238,
                    "inside_band_seed_count": 2,
                    "maximum_distance_to_band": 0.1,
                    "seed_block_trait_loss_rates": [0.2, 0.75, 1 / 3, 0.8, 0.5],
                },
            }
        ]
    }
    rows = publication_rows(audit)
    assert len(rows) == 1
    assert rows[0]["dominant_regime"] == "seed-heterogeneous"
    assert rows[0]["domain_selected"] is False
    assert rows[0]["closest_batch_index"] == 406
    assert rows[0]["closest_seed_block_rates"].count(";") == 4
