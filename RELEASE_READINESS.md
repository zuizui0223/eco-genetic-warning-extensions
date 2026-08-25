# Release readiness

This ledger separates repository facts that are already fixed from metadata decisions that require explicit author approval. It does not change the scientific evidence or release version.

## Ready now

- [x] extension scientific/manuscript main is synchronized through the natural measurement-boundary synthesis
- [x] parent scientific commit used by the extension is pinned: `dd8ee379d0d3518194c767d16402042525bc00dc`
- [x] software licence is MIT in both repositories
- [x] package version is `0.1.0` in both repositories
- [x] no open pull requests in either repository at the start of this release-readiness pass
- [x] Letter manuscript passes Protocol invariant, two-repository reproducibility, and Paper completion CI after Oenothera/Eschscholzia integration
- [x] third-party raw data are not committed; source provenance and compact derived results are retained where analyses ran
- [x] scientific stop rules prohibit outcome-informed simulator or empirical retuning

## Author approval required before citation/release metadata can be finalized

- [ ] final manuscript title
- [ ] complete author names and order
- [ ] affiliations and corresponding author
- [ ] author ORCIDs
- [ ] CRediT contributor statements
- [ ] funding / grant identifiers
- [ ] acknowledgements
- [ ] conflict-of-interest declaration
- [ ] journal automated-tool disclosure wording
- [ ] licence for manuscript text, figures, tables, and other non-software outputs
- [ ] confirm whether release version remains `0.1.0` or is promoted for submission/archive

`CITATION.cff` is intentionally not generated before these author-controlled fields are approved. Do not infer author identity, author order, ORCIDs, or output licensing from commit metadata.

## After author approval

1. Add coordinated `CITATION.cff` files to parent and extension with explicit repository roles.
2. Confirm package/release version and update version fields only if approved.
3. Confirm repository descriptions/topics and landing-page wording.
4. Run the full two-repository submission workflow on the final metadata commit.
5. Create coordinated immutable Git tags/releases.
6. Deposit the release/submission package in Zenodo or an equivalent archive.
7. Record concept DOI and version DOI(s), then add them to README, citation metadata, and manuscript data/code availability.
8. Freeze and record the final release bundle digest.

## Repository roles for future citation metadata

### `eco-genetic-criticality`

Mechanistic parent: theorem-guided interaction/fragmentation framework, finite-model evidence ledger, and inherited conditional warning benchmark. The canonical scientific state remains the pinned historical scientific commit even when release-maintenance commits advance `main`.

### `eco-genetic-warning-extensions`

Condition-recovery, warning replication/portability, state-representation, natural state-sufficiency, integrated manuscript, and submission-bundle repository.

## Release gate

Do not create a final citation record, immutable release tag, or archive DOI until the author-controlled metadata above are explicitly approved. Scientific work is otherwise release-ready at the repository level; remaining blockers are metadata and archival decisions, not unresolved simulator tuning.
