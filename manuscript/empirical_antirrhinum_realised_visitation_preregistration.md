# Prospective realised-visitation state discovery — wild *Antirrhinum majus*

## Purpose

The Eschscholzia campaign showed that array-level pollinator availability from pan traps cannot simply be promoted to an effective interaction state: count + mean ITD did not receive reproducible held-out support for mating or pollen-movement outcomes. The next measurement step therefore moves closer to the focal plant.

This campaign asks whether a **plant-level realised-visitation assay** from the wild *Antirrhinum majus* hybrid zone can be synchronized with mating/paternity data from the same 2012 population.

The visitation assay is not direct visual observation of every visit. Snapdragon flowers were fitted with small cellophane tags held in the corolla mouth; tag loss was used to infer that a pollinator had opened the flower. We therefore call this `I_realised_proxy`, not direct visitation and not pollinator availability.

## Fixed sources before archive inspection

Two open institutional data records from the Institute of Science and Technology Austria (ISTA) are fixed prospectively:

1. **Wild visitation / phenotype archive**  
   Ellis (2016), doi:`10.15479/AT:ISTA:36`, record `5552`, file `IST-2016-36-v1+1_tag_assay_archive.zip`, published MD5 `cbc61b523d4d475a04a737d50dc470ef`.  
   The repository description states that wild plants were surveyed over multiple days in 2010, 2011 and 2012 and that phenotypic/demographic explanatory variables are included.

2. **Wild 2012 mating / paternity archive**  
   Field & Ellis (2016), doi:`10.15479/AT:ISTA:37`, record `5553`, file `IST-2016-37-v1+1_paternity_archive.zip`, published MD5 `4ae751b1fa4897fa216241f975a57313`.  
   The repository description states that the archive contains genotypic, phenotypic and demographic data for 2,128 wild snapdragons and 1,127 open-pollinated progeny from the natural hybrid zone in 2012.

The controlled-tent array archive doi:`10.15479/AT:ISTA:35` is **not** part of this primary discovery because it is a different experimental system. It may not be used to patch missing wild-population keys after inspection.

## Access and schema-only boundary

The discovery adapter may fetch each ISTA record landing page only to locate the exact predeclared archive filename. The archive bytes must match the published MD5 before any member is inspected.

Discovery may then record only:

- landing-page / resolved archive URL;
- archive filename, byte size, MD5 and SHA-256;
- archive member filenames and byte sizes;
- for text/CSV/TSV files, the first header row only;
- for spreadsheet files, workbook sheet names, dimensions and first-row column labels.

It must not inspect or report any data-row value, visitation rate, phenotype frequency, fruit-set value, mating distance, paternity assignment, coefficient, p-value, correlation or descriptive outcome statistic.

## Fixed biological mapping target

Using filenames and header labels only, determine whether the two archives expose a defensible common 2012 hierarchy for:

- year / observation date or season;
- wild plant identity;
- spatial position or population coordinate where source-defined;
- flower colour / phenotype state where present;
- plant-level realised-visitation proxy (`I_realised_proxy`);
- a direct reproductive-function endpoint (`F_reproduction`) **only if one is explicitly present in the locked wild archives**;
- mother/progeny/paternity or other source-defined mating outcome (`G_mating/C_pollen`).

No new reproductive endpoint may be imported from another experiment after schema inspection.

## Required discovery decision

The schema-only campaign must end in exactly one of:

- **`wild_IFG_joint_state_identifiable`** — the 2012 visitation archive and paternity archive share a defensible plant/time hierarchy and the wild archive contains an explicit reproductive-function endpoint that can be synchronized with both;
- **`wild_IG_partial_state_identifiable`** — plant-level 2012 visitation and paternity/mating can be synchronized, but no explicit directly mappable `F_reproduction` endpoint exists in the locked wild records;
- **`wild_state_not_identifiable`** — visitation and paternity cannot be joined at a defensible 2012 plant/population hierarchy without guessing identities, reconstructing keys from values or importing a different experiment.

All three outcomes are acceptable.

## Scientific question if identifiable

If at least the `I_realised_proxy + G_mating/C_pollen` state is identifiable, a second preregistration must ask:

> **Does plant-level realised visitation carry endpoint-relevant held-out predictive information for wild mating state, and after it is supplied does spatial/phenotypic context retain transferable information?**

If `F_reproduction` is also explicitly synchronized, the same nested state sequence may be tested for both F and G. Exact responses, transformations, held-out units, regularization and decision rules must be committed before any data row is inspected.

## Claim ceiling

A positive result would validate this **tag-based realised-visitation assay** as a useful state coordinate for the tested endpoint. It would not prove that tag loss equals every biologically effective visit, that flower colour is a fragmentation mechanism, or that the Antirrhinum hybrid zone is equivalent to urban/island fragmentation.

## Stop rule

Do not use the controlled-tent archive to rescue missing wild keys. Do not choose years other than 2012 for the paternity linkage. Do not derive an outcome from phenotype or genotype values while deciding schema. Do not repair IDs by fuzzy matching after outcome inspection.