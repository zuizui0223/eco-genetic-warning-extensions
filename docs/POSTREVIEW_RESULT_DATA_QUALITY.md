# Post-review warning and Eschscholzia audit

## Technical summary

The frozen binary warning rules do not discriminate future functional loss in either saved ensemble. At the primary fixed generation-30 landmark, AUC spans 0.500–0.538 in the inherited ensemble and 0.500–0.510 in the fresh ensemble. The full-horizon result is more extreme but less informative: all six rules fire in every non-event trajectory (48/48 inherited; 49/49 fresh), so specificity is zero and the binary score degenerates to a constant with AUC 0.5.

A one-time, prospectively specified exploratory analysis tested whether the continuous baseline-relative diversity level retained information hidden by binary thresholds. Across generations 30, 60, and 90, AUC spans 0.418–0.692 in the inherited ensemble and 0.422–0.687 in the fresh ensemble. Two isolated cells have percentile intervals above 0.5, but neither reproduces at the same diversity measure and landmark in the other ensemble. These results do not establish a portable continuous warning score and do not establish that genetic diversity contains no time-specific information.

The separate post-lock *Eschscholzia* path corrected exactly the two preregistered `Habitat` mismatches, then stopped at the unchanged F-response preparation gate. The response contained a missing, non-finite, or negative value. No response repair, row exclusion, model fit, score, bootstrap, or rerun of other endpoints occurred. The primary non-identifiability decision and the earlier one-key sensitivity STOP remain unchanged.

## Fixed-landmark evidence carries the warning conclusion

| Analysis | Inherited ensemble | Fresh ensemble | Defensible interpretation |
|---|---:|---:|---|
| Binary rules, generation 30 | AUC 0.500–0.538 | AUC 0.500–0.510 | Near-chance discrimination before full-horizon marker degeneration |
| Continuous `1 - H(t)/H(0)`, generation 30 | AUC 0.533–0.535 | AUC 0.522–0.556 | Near chance in both independent saved ensembles |
| Continuous score, generations 30/60/90 | AUC 0.418–0.692 | AUC 0.422–0.687 | Heterogeneous, coordinate-specific signals without cross-ensemble replication |
| Frozen binary rules, full horizon | sensitivity 1.0; FPR 1.0; specificity 0 | sensitivity 1.0; FPR 1.0; specificity 0 | All-marker-positive degeneration; supporting boundary, not the primary discrimination result |

The continuous cells are not independent replicates. Each ensemble contributes one shared set of trajectories to two diversity measures at three landmarks; no pooled endpoint test is used. A compact table is more audit-able than a chart here because the inferential issue is the exact landmark-by-measure correspondence and its failure to replicate, not a smooth temporal trend.

## Population, outcomes, and right-censoring rules

The analysis population is every saved baseline-eligible trajectory: 83 inherited trajectories (35 functional-loss events and 48 administratively censored non-events) and 82 fresh trajectories (33 events and 49 censored non-events). A non-event is therefore a trajectory observed without functional loss through generation 120, not proof that loss would never occur.

For a landmark at generation `t`, trajectories with functional loss at or before `t` are excluded from that landmark's risk set. Cases lose function after `t` and by generation 120. Dynamic controls remain event-free through generation 120. The continuous score is fixed as `1 - H(t)/H(0)`, with greater erosion assigned the higher predicted risk. This yields a landmark cumulative/dynamic concordance AUC through the administrative horizon; it does not identify performance beyond generation 120.

At generation 90, only 10 inherited and 3 fresh future cases remain. The fresh generation-90 intervals are consequently very wide (0.102–0.898 for `H_alpha`; 0.082–0.898 for `H_gamma`) and cannot support stable late-landmark ranking claims.

## Prospective design and uncertainty

The one-time exploratory analysis was registered before outcome access in commit `bf9f492996cfb57718e03edd4a3620c0756b32c4`. Thresholds, seeds, domain, endpoints, score direction, landmarks, and administrative horizon were not changed. Each AUC interval is a 95% percentile interval from 10,000 trajectory-level bootstrap replicates, stratified by future case versus dynamic control. The inherited and fresh source artifact digests and raw-member SHA-256 values are retained in the result artifact.

The *Eschscholzia* third path was registered in the same prospective commit. It permitted only `Fallow graound` to `Fallow ground` replacement for array keys `1||3` and `1||4`. Six rows were corrected and the cross-source mismatch count became zero before the locked F-response preparation gate stopped the analysis.

The prospective runner first raised that locked-gate exception before writing an artifact. A later record-only patch caught the same `NotIdentifiable` exception and serialized the STOP; it did not change correction, response preparation, eligibility or modelling. The manual workflow runs this descendant recorder only after verifying the prospective commit is its ancestor.

Primary evidence:

- [Frozen warning validity audit](../artifacts/prepublication_review/warning_validity_audit.json)
- [Continuous landmark result](../artifacts/prepublication_review/continuous_warning_landmark_auc.json)
- [Continuous landmark table](../manuscript/tables/continuous_warning_landmark_auc.csv)
- [Eschscholzia full metadata-repair result](../artifacts/empirical/eschscholzia_f_full_metadata_repair_result.json)
- [Continuous analysis preregistration](../manuscript/warning_continuous_landmark_exploratory_preregistration.md)
- [Eschscholzia repair preregistration](../manuscript/empirical_eschscholzia_f_full_metadata_repair_preregistration.md)

## Data-quality and robustness checks passed

Automated checks require the exact 12 continuous cells (two ensembles × two diversity measures × three landmarks), unique cell keys and bootstrap seeds, JSON/CSV equality, finite ordered AUC intervals, and the following denominator identities for every cell:

`risk set + losses at or before landmark = baseline-eligible trajectories`

`future cases + losses at or before landmark = all event trajectories`

`risk set = future cases + dynamic controls`

The checks also fix dynamic-control counts at 48 inherited and 49 fresh trajectories, verify both warning source hashes, verify both *Eschscholzia* CSV hashes, require both metadata corrections, and require every post-STOP information-boundary flag to remain false.

## Claim ceiling and next steps

The manuscript should lead with fixed-landmark discrimination and treat full-horizon AUC 0.5 as the mechanical endpoint of marker saturation. The warning claim is limited to the six frozen binary rules and this one fixed continuous score; it is not a claim that `H_alpha` or `H_gamma` can never carry predictive information.

No further score, landmark, threshold, response repair, or within-dataset rescue analysis should be opened. Any stronger warning claim now requires a newly preregistered score evaluated in genuinely independent trajectories. The *Eschscholzia* F endpoint remains non-estimable under all allowed paths and should be reported as a preserved STOP rather than as a null effect.

The remaining scientific question is whether a continuous score defined from mechanism rather than selected from these trajectories can reproduce at the same landmark in a new ensemble. That is an independent-validation question, not a reason to tune the current saved data.
