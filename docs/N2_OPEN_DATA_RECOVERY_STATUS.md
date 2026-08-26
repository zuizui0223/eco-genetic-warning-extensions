# N2 open-data recovery status

## Current state

N2 is a response-firewalled audit of whether future-relevant pollination-state layers are not only measured in the source studies but also retained in a reusable public representation that can support held-out prediction.

The direct urban–island convergence hypothesis remains open:

`F_future ⟂ origin | S_measured`.

No N2 outcome model has been used to infer that urban and island systems differ or converge.

## N2 bounded registry result

The preregistered registry contains five urban and five island systems scored only from public measurement/archive descriptions. Published effect directions, p-values and preferred ecological conclusions are excluded from the scoring fields.

The committed registry/summary currently show:

- urban systems with both direct reusable `I` and realised reusable `F` scored `yes`: **3/5**;
- island systems with both direct reusable `I` and realised reusable `F` scored `yes`: **0/5**;
- systems with reusable process-specific connectivity `C` scored `yes`: **0/10**;
- systems with reusable contemporary mating/genetic state `G` scored `yes`: **0/10**;
- systems with the full intended proximal-state stack available as reusable public data: **0/10**.

Decision:

`N2_measurement_representation_gap_prevents_direct_cross_origin_test`

This is a measurement/representation boundary in this bounded registry. It is not evidence that the corresponding biological mechanisms are absent, nor evidence that island and urban systems occupy different regimes.

## Why the first four-archive bridge stopped

The earlier prospective four-archive minimal bridge required every admitted system to expose both direct pollinator visitation and realised reproduction at a joinable ecological unit.

The locked Hawaii archive (`10.5061/dryad.tm575v4`) is publicly described as raw flower-visitation observations. The source paper measured reproductive responses, but the locked archive metadata do not demonstrate a deposited realised-reproduction table. Under the preregistered Stage-A rule, that candidate is therefore not admissible to the minimal `I_visit -> F` bridge.

Because candidate replacement after inspection was prohibited, the original two-urban/two-island bridge stopped rather than adding a more convenient fifth study.

## Toronto independent residual-context replication

`U_TORONTO_2025` is the only N2 system whose public metadata explicitly co-locate all ingredients required for a direct within-system residual-context test in one public CSV:

- held-out ecological unit: `site_id`;
- upstream context: `urban_cover`, `ugs_edge_density`;
- direct interaction: `number_of_visits / survey_effort`;
- focal floral support: `floral_units_array`;
- phenology-matched garden richness;
- species identity;
- realised seed production: `number_seed` with `fruit_sample_size` exposure.

The model, endpoint, holdout unit, standardisation rule and bootstrap decision were preregistered in `manuscript/empirical_toronto_residual_context_preregistration.md` before project-level reproductive outcome access.

Primary frozen comparison:

`M0: number_seed ~ species + I_visit + floral_units_array + garden_richness_matched + offset(log(fruit_sample_size))`

versus

`M1: M0 + urban_cover + ugs_edge_density`.

Validation is leave-one-garden-out. Species rows sharing one garden are not independent systems.

## Current execution boundary

The Toronto outcome analysis is not yet complete because the exact `data.csv` bytes have not been acquired by this project.

Dryad anonymous metadata access is available, but Dryad's current REST API documentation states that anonymous API users are not permitted to download data files and that dataset/file download endpoints require API authentication. Browser `file_stream` probes from GitHub Actions have also returned anti-bot challenge HTML rather than declared dataset bytes in prior diagnostics.

A separate session-level network probe could not resolve the Dryad host, so it was not used as a data source.

These are access/execution boundaries only. They do not change the preregistered scientific design and do not supply an ecological result.

## Exact next gate

Do not change the Toronto predictor set, response, endpoint, holdout unit or decision rule.

The next valid execution step is:

1. obtain the exact Dryad `data.csv` for `10.5061/dryad.b8gtht7r4` through an authorised/public interactive route;
2. verify file identity against the locked DOI/file manifest;
3. run the already committed `scripts/run_toronto_residual_context.py` without model changes;
4. retain whichever preregistered decision results: `residual_urban_context_information_detected`, `no_detected_residual_urban_context_information`, or `primary_model_not_identifiable`;
5. treat the result as one independent urban residual-context case, not as an urban–island convergence result.

## Claim ceiling

The strongest supported statement at this stage is:

> In the bounded N2 registry, the main obstacle to a direct urban–island state-convergence test is not a demonstrated ecological difference but failure to retain the same future-relevant process and response layers in reusable, joinable public representations across independent systems.

The stronger cross-origin future-law hypothesis remains open.