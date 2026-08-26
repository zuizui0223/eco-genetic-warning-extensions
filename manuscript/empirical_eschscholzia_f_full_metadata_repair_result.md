# Eschscholzia post-lock full-metadata repair result

## Decision

**`postlock_descriptive_reconstruction_not_estimable`**

The post-lock descriptive path was fixed at prospective commit `bf9f492996cfb57718e03edd4a3620c0756b32c4`. It corrected exactly the two metadata-only Habitat mismatches declared in advance:

- `1||3`: three `Fallow graound` rows to `Fallow ground`;
- `1||4`: three `Fallow graound` rows to `Fallow ground`.

After those corrections, the cross-source Habitat mismatch count was zero. The unchanged `_prepare_f` gate then stopped with:

> `F primary response has missing/non-finite/negative value`

The prospective runner originally surfaced this exception before it could write an artifact. The only post-result code change catches that already observed `NotIdentifiable` exception and serializes the STOP and information-boundary flags. It does not alter metadata correction, F preparation, response values, row eligibility or any model path. The workflow therefore executes the recorder from a descendant commit while verifying that the prospective protocol commit is an ancestor.

## Information boundary

- F preparation completed: **no**;
- F model fitted: **no**;
- held-out score calculated: **no**;
- bootstrap run: **no**;
- another response repair or row exclusion: **no**;
- G, C, R or another endpoint rerun: **no**.

No F estimate exists. The primary `multi_endpoint_not_identifiable` decision and the one-key `stop_pre_model_unexpected_second_metadata_mismatch` decision remain unchanged. The full-metadata repair shows that the known Habitat typo set was not the only barrier to an estimable F endpoint; it does not authorize outcome repair or weaken the empirical measurement gate.
