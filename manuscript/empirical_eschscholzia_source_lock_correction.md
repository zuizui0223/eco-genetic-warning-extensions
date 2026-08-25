# Eschscholzia source-lock correction before outcome inspection

## Status

This correction was made **before any outcome row was opened or parsed by the multi-process analysis**.

The first analysis workflow (`32800718619`) stopped inside `_download_source` on the first EIDC product before the ZIP member was read. It compared the newly downloaded ZIP-wrapper SHA-256 with the package SHA observed during schema discovery and found:

- schema-discovery ZIP SHA: `66b0b9eec2ffcf6df8bc19f4677c159e5f574a4a23aa452221cc2b552b01f0c5`
- newly generated ZIP SHA: `0c770c74d2bd1e1b2d0310e8c441bed61fbc6871bf57159b3e9797c304a8aaae`

The run stopped at that point. No CSV member, data row, outcome value, class frequency, coefficient or model score was inspected.

## Diagnosis

The EIDC download endpoint can regenerate the outer ZIP package. Archive-level metadata such as member timestamps or wrapper bytes can therefore change even when the locked data member is unchanged. The scientific source identity should not depend on a transport-container hash when a stronger content-level lock already exists.

## Corrected source identity

The four source identities remain unchanged. Each analysis download must match **all** of:

1. the same EIDC DOI / UUID;
2. the exact preregistered CSV member path inside the package; and
3. the exact CSV-member SHA-256 obtained in the schema-only discovery.

Locked CSV hashes:

- pollinator: `db063840850fb4f358db7e99271feb9b9a92f6701b889d1b59a1348ffada89ef`
- exposed/supplemented F: `83ab56cc8b3e4b2ae2b7141e55683b1cff2734006d4fa4f6735605d3a2be379f`
- exposed/excluded R: `ad52e8b52885cde66a0ed5476bffb0e9894b4d0429e42d927ea72b388b3ea27b`
- paternity G/C: `6805ceb4164fefa373ba758a0fcf0a58fe67624b432d3aea6d344d690efd71f2`

The outer ZIP SHA is still recorded as access provenance but is **not** an identity criterion.

## Scientific invariants

This correction changes only transport validation. It does **not** change:

- the four DOI/UUID sources;
- CSV member paths;
- any response or state coordinate;
- key normalization;
- `I_count` or `T_mean_ITD` definitions;
- F, G, C, D or R endpoint definitions;
- S0/S1/S2/S3 model sequence;
- Ridge/logistic regularization;
- leave-one-array-out validation;
- bootstrap count or seed;
- decision rules.

The original exact-model preregistration remains controlling for all scientific choices.
