# Prospective natural-state discovery — *Mertensia ciliata* cross-year efficiency calibration

## Purpose

This campaign follows the locked Campanula representation boundary. It asks whether an **independent** natural dataset contains enough structure to define pollinator effectiveness before fitting a reproductive outcome, while preserving that effectiveness in the state representation rather than erasing it by feature-wise rescaling.

The source is Gallagher & Campbell (2020), *American Journal of Botany*, doi:`10.1002/ajb2.1439`, archived at Dryad doi:`10.7280/D19X0D` and mirrored at Zenodo record `3901407`.

The published design separates two programmes:

- 2015 phenology manipulation: potted *M. ciliata* plants exposed for one week, repeated pollinator observations recording visitor identity and flowers visited, followed by pollen receipt and seed production;
- 2016 pollinator-effectiveness experiment: single visits to virgin flowers in wild populations, with visitor identity, conspecific/heterospecific pollen receipt and seed set measured after the single visit.

This creates a prospectively testable cross-year calibration idea:

`2015 visitation composition × 2016 single-visit effectiveness -> efficiency-preserving interaction state -> 2015 reproductive outcome`

The cross-year/site shift is a limitation to be retained, not hidden.

## Source lock before workbook inspection

Zenodo record: `3901407`.

Exactly two data workbooks are permitted:

1. `gallagher&campbell_phenologyExperimentData.xlsx`
2. `gallagher&campbell_pollinatorEffectivenessData.xlsx`

The two non-spatial PDF documentation files are not used for numeric discovery. Source identity is Zenodo record + exact filename + Zenodo-published checksum obtained before workbook inspection.

## Schema-only boundary

The discovery may inspect only:

- Zenodo API file metadata, size and checksum;
- exact workbook file hash;
- workbook sheet names and dimensions;
- **string-valued cells only** in the first 12 rows of each sheet, with coordinates, to recover multi-row headers/labels when needed.

It must not record or use any numeric study-cell value, visitation rate, pollen receipt, seed-set value, date/elevation value, model result, effect direction, coefficient or p-value.

## Fixed biological target

The next stage is allowed only if schema/string labels can identify:

### 2015 outcome programme
- a phenology/time/group or plant sampling key;
- pollinator visitation amount and visitor identity/composition;
- a reproductive function endpoint, preferably source-defined seed set / seeds per flower.

### 2016 calibration programme
- pollinator/visitor identity;
- **single-visit conspecific pollen receipt** as the primary independent effectiveness calibration;
- single-visit seed set may be retained only as a secondary effectiveness coordinate.

Primary mechanistic representation, if identifiable, must aggregate **before scaling**:

`E_pollen(t) = sum_k visitation_2015(t,k) * mean_single_visit_conspecific_pollen_2016(k)`.

No future model may independently z-standardize the taxon-specific visitation and efficiency factors before this multiplication/summation. A later global scaling of the already-aggregated `E_pollen` coordinate is allowed if preregistered.

## Required discovery decision

- **`crossyear_effective_state_identifiable`**: the 2015 workbook exposes visitation composition + reproductive outcome keys and the 2016 workbook exposes visitor identity + single-visit conspecific pollen receipt, with a defensible source-defined taxonomic mapping possible without outcome values;
- **`partial_crossyear_effective_state_identifiable`**: both programmes exist but the taxonomic or sampling mapping is only coarser than the source visitor labels; a bounded grouped calibration may be preregistered;
- **`not_identifiable_from_archive`**: required process columns/keys cannot be identified without numeric outcome inspection or post hoc reconstruction.

All decisions are acceptable.

## Claim ceiling

Even if later predictive support is obtained, this system cannot show same-year calibration. The efficiency measurements come from 2016 wild populations whereas the phenology/outcome experiment was in 2015. The scientific test is whether an independently calibrated, information-preserving efficiency representation transfers across that declared domain shift.

## Stop rule

Do not inspect numeric outcome values in this discovery; do not replace pollen receipt with single-visit seed set because it looks more favorable; do not select visitor groups from reproductive outcomes; and do not reopen Koski/Campanula with a new preprocessing scheme. If identifiable, commit a separate exact-model preregistration before any numeric study row is read.