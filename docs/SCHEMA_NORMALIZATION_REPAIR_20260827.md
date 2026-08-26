# Response-firewalled schema normalization repairs — 2026-08-27

Two first-pass executions stopped before their intended scientific decisions because source-format details differed from the literal parser assumptions. These are treated as schema repairs, not as outcome-facing model revisions.

## Toronto phytometer code case

The locked Toronto version bundle was acquired successfully and `data.csv` matched the preregistered identity exactly: 5,543 bytes and SHA256 `0739cd11bf2afea3a8da7db953e7940fcde5570d5f7cb88e15f08a02140b3127`.

The frozen analysis then stopped before any model fit because the source stores the four already-preregistered phytometer codes as lowercase (`deca`, `losi`, `pehi`, `syno`) while the preregistered mapping uses uppercase (`DECA`, `LOSI`, `PEHI`, `SYNO`). No endpoint, predictor, holdout unit, likelihood, interaction term, or decision rule is changed.

Permitted repair: create a canonical analysis copy in which only `species_phytometer` is normalized by whitespace stripping plus uppercase conversion, after verifying that its case-insensitive unique set is exactly the preregistered four-code set. All other cells remain byte-for-byte represented by the CSV parser/writer and no outcome value is inspected for model choice.

## Mallorca CSV delimiter

The first Mallorca network schema audit acquired and digest-verified the three locked files successfully, but parsed each CSV with the default comma delimiter. The returned headers themselves demonstrate that these files are semicolon-delimited (for example `Year;Species;...` and `PlantSpecies;...`). The resulting zero-overlap alignment decision is therefore an invalid parser result, not a biological/schema-alignment result.

Permitted repair: rerun the same response-firewalled schema audit using semicolon-delimited parsing (or equivalent delimiter detection restricted to the header structure). Only file identity, headers, dimensions, species identifiers, year identifiers, and cross-file key alignment may be inspected. Fecundity and visitation values remain unopened for association or model fitting.

## Stop rule

Neither repair may change a scientific model or select a favorable endpoint. If Toronto still fails after exact code canonicalization, preserve that failure. If Mallorca still lacks demonstrable species-by-year alignment after correct delimiter parsing, preserve that boundary and do not invent a join.
