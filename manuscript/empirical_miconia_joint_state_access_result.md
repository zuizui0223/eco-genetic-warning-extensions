# Miconia joint-state discovery result — archive not identifiable in current execution

## Decision

**`not_identifiable_from_archive`**

The prospective *Miconia affinis* joint-state discovery gate did **not** inspect workbook schema or any outcome values. Dryad public metadata was sufficient to verify the four locked source files and their file identifiers, but no attempted public download route returned bytes that could be validated against the metadata and safely opened as the archived workbooks.

This is an **access/non-identifiability result**, not an ecological null and not evidence against the published study.

## Fixed source

- Castilla et al. (2017), *Proceedings of the National Academy of Sciences*, doi:`10.1073/pnas.1619271114`
- Dryad dataset doi:`10.5061/dryad.1cm80`
- locked files:
  - `30526` — `correlation_dbh_number of inflorescences.xlsx`
  - `30527` — `genotypes_Miconia affinis.xlsx`
  - `30528` — `pollen_dispersal_analysis_data.xlsx`
  - `30529` — `seed_viability_analysis_data.xlsx`

## Access diagnosis

Three access-only attempts were allowed. No scientific model, endpoint or predictor family was changed between them.

### Attempt 1 — run `32732304033`

The legacy landing-page route `https://datadryad.org/downloads/file_stream/{id}` returned HTTP 403 before a workbook was opened.

### Attempt 2 — run `32733136599`

Anonymous Dryad REST metadata succeeded. The adapter resolved the published dataset/version/file list and verified the locked filenames and file IDs before attempting any workbook read. The documented dataset-package `/api/v2/datasets/<encoded-doi>/download` route then returned HTTP 401. No workbook was opened.

### Attempt 3 — run `32733622959`

Anonymous metadata again succeeded. The public Stash route returned a response for file `30526`, but its byte length was **4,324** whereas Dryad metadata specified **13,042** bytes for `correlation_dbh_number of inflorescences.xlsx`. The adapter stopped on this size mismatch before writing/opening the workbook or reading a header row.

Thus all three attempts failed **before schema inspection**.

## Scientific interpretation

The published study remains a strong external natural-system example because it links pollinator traits, direct seed function, molecular paternity/pollen dispersal and plant/population state in one programme. The archive also remains publicly described on the Dryad landing page. However, this repository does not promote those published results into a new project-generated joint-state test without a reproducibly retrieved source snapshot.

The correct project-level conclusion is therefore:

> *Miconia affinis* is scientifically suitable for a synchronized `I/T -> F_seed + C_pollen/G_parentage` test, but the locked archive was not machine-identifiable in the current execution environment before the preregistered access stop rule was reached.

## Claim ceiling

Do not report:

- any Miconia workbook column names as project-inspected schema;
- any project-generated Miconia model result;
- `joint_state_identifiable` or `partial_joint_state_identifiable`;
- the access failure as an ecological null.

Published ecological findings may still be cited as literature, clearly separated from project-generated analyses.

## Stop rule

No fourth download-route modification is allowed in this campaign. The discovery workflow is manual-only after this result. Further empirical work moves to an independently accessible dataset rather than continuing access tuning on Miconia.
