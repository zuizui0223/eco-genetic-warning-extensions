# Witheringia direct-interaction discovery — archive access boundary

## Decision

**`not_identifiable_from_archive`**

This is an access/non-identifiability result, not a biological null and not evidence against Stone, VanWyk & Hale (2014).

The prospective campaign fixed Dryad doi:`10.5061/dryad.f8539` and four files before any workbook inspection. Anonymous Dryad metadata successfully resolved the source record and exact file identities, including `pollinators_all.xls` as file id `23486`. However, no declared public retrieval route returned a verifiable workbook payload in the GitHub Actions execution environment.

No workbook sheet, column label or data row was inspected by this project.

## Access diagnosis

### Attempt 1 — run `32802948645`

Anonymous metadata succeeded. For `pollinators_all.xls` (file id `23486`):

- API file download relation `/api/v2/files/23486/download` returned HTTP 401;
- public Stash file-stream `/stash/downloads/file_stream/23486` returned HTTP 403.

The workflow stopped before opening a workbook.

### Attempt 2 — run `32803045668`

The source DOI and four filenames were unchanged. The adapter used the DOI-level Stash dataset-bundle route only after individual access had failed. The dataset bundle redirected and ultimately returned HTTP 403. The workflow again stopped before opening a workbook.

## Scientific interpretation

The source remains scientifically well matched to the current measurement question. The publication and Dryad record describe direct pollinator visitation to single focal plants and fruit set across nine common gardens and parental/progeny microsatellite data in seven gardens. Those published properties motivate the system as an external example of direct interaction, reproduction and mating measurement.

They are **not** promoted to a project-generated state-sufficiency result because the archived workbook bytes were not reproducibly retrievable here.

## Measurement-programme consequence

The Eschscholzia result showed that an availability proxy cannot simply be assumed to be an effective interaction state. Witheringia was selected specifically to test direct focal-plant visitation, but archive access prevented that test before schema inspection.

The next direct-interaction empirical campaign should therefore use an independently accessible archive (preferably Figshare, Zenodo, Dataverse or another source with stable machine-readable downloads) rather than continuing to tune Dryad access routes.

## Claim ceiling

Do not report:

- any project-inspected Witheringia workbook schema;
- any project-generated visitation, fruit-set or paternity result;
- `direct_joint_state_identifiable` or `direct_partial_state_identifiable`;
- the access failure as evidence that direct interaction is insufficient.

## Stop rule

No third Dryad download-route modification is opened in this campaign. The discovery workflow is manual-only after this result.