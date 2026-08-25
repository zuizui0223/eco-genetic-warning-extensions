# Antirrhinum realised-visitation discovery — archive access boundary

## Decision

**`wild_state_not_identifiable` due to archive access before schema inspection.**

This is an access result, not an ecological null and not a statement that the wild visitation/paternity records cannot be joined biologically.

The campaign prospectively fixed ISTA records `5552` / doi:`10.15479/AT:ISTA:36` and `5553` / doi:`10.15479/AT:ISTA:37`, their exact archive filenames, published MD5 values, and the 2012-only wild-population bridge before any archive member was inspected.

No archive bytes matched the published MD5 because no usable public download URL could be resolved in the current GitHub Actions execution environment. No ZIP member, header or data row was inspected.

## Access diagnosis

### Attempt 1 — run `32803491214`

The ISTA record landing page was reachable, but the visible archive filename was not encoded as a normal anchor href. The adapter stopped before attempting any guessed file route.

### Attempt 2 — run `32803612516`

The resolver was expanded only to metadata sources independently tied to the same ISTA record:

- all embedded landing-page attributes / URL strings;
- the ISTA OAI endpoint advertised by B2FIND for that record.

No usable exact archive URL was exposed. The only filename-containing landing value resolved as the relative candidate

`https://research-explorer.ista.ac.at/record/IST-2016-36-v1+1_tag_assay_archive.zip`

and returned an HTTP error. OAI metadata did not add a verified exact archive URL. The workflow stopped before archive inspection.

## Scientific interpretation

The institutional records remain useful external evidence that:

- plant-level tag-loss visitation data were collected in the wild hybrid zone in 2010–2012;
- the 2012 mating archive contains 2,128 wild plants and 1,127 open-pollinated progeny;
- a 2012 realised-visitation/mating linkage is scientifically plausible.

However, the project does not infer join keys, model an endpoint, or call the system `wild_IG_partial_state_identifiable` without a reproducibly retrieved source snapshot.

## Stop rule

No third ISTA download-route search is opened in this campaign. The workflow is manual-only after this access result. The controlled-tent `ISTA:35` archive remains excluded from rescuing the wild bridge.

Further measurement validation moves to an archive with a stable machine-readable public download, prioritizing Zenodo/Figshare/Dataverse sources.