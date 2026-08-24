# E3 result — Southern Norway residual-context falsification gate

## Decision

**`not_identifiable_from_public_download_in_current_execution`**

The preregistered four-species residual-context analysis was **not run**. The public Dryad record was identified unambiguously, but the declared automated retrieval path did not produce the workbook bytes within the three predeclared fetch-diagnosis attempts. Per the stop rule, no fourth fetch modification and no alternative scientific model were opened.

This is an **access/execution result**, not a null ecological result and not evidence for or against measured-state convergence.

## Locked source identified before any workbook inspection

- associated study: Lázaro et al. (2020), *Ecological Applications* 30:e02099, doi:`10.1002/eap.2099`;
- Dryad dataset: `10.5061/dryad.d51c59zzj`;
- Dryad version id resolved by the public metadata API: `52421`;
- unique data file: `Visitation&Seedsetdata_Dryad.xlsx`;
- Dryad file id recovered from the public HAL self/download relations: **`241700`**;
- size reported by Dryad metadata: **135,774 bytes**;
- SHA-256 reported by Dryad metadata: **`1f242b448e05582da21fb8fef9443535e515864052a641ac33c853683a091198`**.

No workbook sheet, column or row contents were inspected in this project before the access gate closed.

## Fetch diagnosis

### Attempt 1 — run `32715861222`

Failure point: dataset metadata request returned HTTP 404.

Cause: the `doi:<DOI>` API path segment was not fully URL encoded.

Correction: encode the entire DOI path segment. This changed only the retrieval adapter, not the DOI, species set, response, context variables, validation unit or decision rule.

### Attempt 2 — run `32716610143`

The corrected adapter reached the Dryad dataset/version/file metadata successfully. It then failed with HTTP 401 at the REST file-download endpoint `/api/v2/files/{id}/download`.

Diagnosis: current Dryad REST file-download endpoints require authenticated access even though published dataset metadata are anonymously readable. The exact published file remained identifiable through its public metadata relations.

Correction: keep metadata discovery through the REST API and attempt the public landing-page file-stream route for the exact resolved file id.

### Attempt 3 — run `32718007962`

The adapter again reached the file metadata. Dryad's embedded file object exposed the exact file id only inside the HAL relations (`/api/v2/files/241700`) rather than as a top-level `id` field. The adapter stopped before requesting bytes.

This is a retrieval-schema incompatibility, not an ecological or statistical failure. However the PR had prospectively declared attempt 3 as the final fetch correction. Therefore the access gate is closed rather than modifying the downloader a fourth time after repeated adapter failures.

## Preregistered scientific test retained but not executed

The declaration remains unchanged:

- all four focal plant species retained;
- direct seed production as realised function;
- floral/pollinator/visitation variables as the proximal process state;
- patch size, isolation, patch complexity and surrounding forest as upstream context;
- whole-fragment holdout validation;
- species-family multiplicity correction;
- `residual_context_detected`, `no_detected_residual_context`, `mixed_predictive_evidence` and `not_identifiable_for_species` all allowed outcomes.

None of those choices were updated after the access result.

## What the published study itself supports

The published analysis remains an important **external falsification example**, separate from the unexecuted project reanalysis. Lázaro et al. report that visitation rates were not directly related to reproductive success in any of the four focal plant species, while several landscape variables had direct, strongly species-specific effects on seed production; patch complexity negatively affected seed production in two of four focal species.

That published result shows why an ecological process state based mainly on interaction frequency can be incomplete: landscape context may retain information about realised function through unmeasured resources, microenvironment, reproduction or other mechanisms.

It must **not** be represented as a new held-out result produced by this repository.

## Consequence for the current synthesis

E1 Honshu–Izu and E2 Zurich provide direct project-level partial-state tests in which the upstream context layer did not add detected transferable predictive information after a measured interaction-functional state. E3 adds a different type of evidence:

1. a prospectively declared direct falsification test that remained unidentifiable because the external workbook could not be retrieved within the locked access procedure; and
2. an independent published study whose own analysis demonstrates that landscape context can directly predict seed production even when visitation does not.

The resulting claim is therefore asymmetric and non-circular: **measured-state convergence can be supported at a declared resolution, but it is not assumed. When the measured process state omits future-relevant mechanisms, residual landscape information can remain.**

## Stop rule

Do not retry a fourth download adapter, change the four-species declaration, select a subset of landscape metrics, or substitute published summary statistics for the planned row-level held-out analysis merely to obtain a project-level E3 classification.
