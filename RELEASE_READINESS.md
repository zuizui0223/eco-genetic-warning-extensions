# Release readiness

This ledger separates repository facts that are already fixed from metadata decisions that require explicit author approval. It does not change the scientific evidence or release version.

## Ready now

- [x] extension scientific/manuscript state is synchronized through the natural measurement/representation boundary, including the locked *Campanula americana* result and response-firewalled rescaling diagnostic
- [x] current manuscript title in the source-of-truth manuscript is **Eco-genetic conditions govern when genetic early warning of functional loss can be validated**
- [x] `manuscript/cover_letter.md` is synchronized to the current title and state-defined reproducibility argument
- [x] `manuscript/submission_metadata.md` contains a reviewable AI/automated-tool disclosure draft and explicit author-approval checklist; final wording and exact materially used tool/model versions remain author-controlled
- [x] parent scientific commit used by the extension is pinned: `dd8ee379d0d3518194c767d16402042525bc00dc`
- [x] parent maintenance `main` is release-green at `bfd61af1fe2b30593ce5f5e8bd1ae990b8ee42a6`
- [x] software licence is MIT in both repositories
- [x] package version is `0.1.0` in both repositories
- [x] no GitHub Release has been created in either repository
- [x] no `CITATION.cff` has been generated before author approval
- [x] third-party raw data are not committed; source provenance and compact derived results are retained where analyses ran
- [x] scientific stop rules prohibit outcome-informed simulator or empirical retuning

### Current merged-main validation

Extension #117 was merged as `9f002c811d9d59e53b3e65a4bf9fea77a781116b` and synchronized the cover letter plus submission metadata without changing scientific evidence or package version.

Merged-main gates on that state:

- Protocol invariant CI: **success** (`32925893927`)
- Two-repository reproducibility contract: **success** (`32925894071`)
- Paper completion sprint: **success** (`32925893924`)

The two-repository workflow completed invariant/manuscript tests, repository/evidence-lock verification, both distribution/source-archive builds, clean-wheel smoke tests, checksums and artifact upload. The Paper completion workflow completed scientific-lock verification, locked publication-data materialization, both distribution/source-archive builds, manuscript/figure/table bundle creation, provenance assembly, complete-package validation and submission-bundle upload.

Parent release-maintenance gates on `bfd61af1fe2b30593ce5f5e8bd1ae990b8ee42a6`:

- ordinary CI: **success** (`32921087236`)
- Submission reproducibility: **success** (`32921087208`)

## Author approval required before citation/release metadata can be finalized

- [ ] final manuscript title approved by all authors
- [ ] complete author names and order
- [ ] affiliations and corresponding author
- [ ] author ORCIDs
- [ ] CRediT contributor statements
- [ ] funding / grant identifiers
- [ ] acknowledgements
- [ ] conflict-of-interest declaration
- [ ] final AI/automated-tool disclosure, including exact materially used tool/model versions as required at submission
- [ ] licence for manuscript text, figures, tables, and other non-software outputs
- [ ] confirm whether release version remains `0.1.0` or is promoted for submission/archive
- [ ] approve repository descriptions/topics/homepage wording

`CITATION.cff` is intentionally not generated before these author-controlled fields are approved. Do not infer author identity, author order, ORCIDs, contributions, funding, conflicts or output licensing from repository ownership or commit metadata.

## After author approval

1. Add coordinated `CITATION.cff` files to parent and extension with explicit repository roles.
2. Confirm package/release version and update version fields only if approved.
3. Apply approved repository descriptions/topics/homepage wording.
4. Run the full two-repository submission workflow on the final metadata commit.
5. Create coordinated immutable Git tags/releases.
6. Deposit the release/submission package in Zenodo or an equivalent archive.
7. Record concept DOI and version DOI(s), then add them to README, citation metadata, cover letter, and manuscript data/code availability.
8. Freeze and record the final release bundle digest.

## Repository roles for future citation metadata

### `eco-genetic-criticality`

Mechanistic parent: theorem-guided interaction/fragmentation framework, finite-model evidence ledger, and inherited conditional warning benchmark. The canonical scientific state remains the pinned historical scientific commit even when release-maintenance commits advance `main`.

### `eco-genetic-warning-extensions`

Condition-recovery, warning replication/portability, state-representation, natural state-sufficiency, integrated manuscript, submission metadata, and submission-bundle repository.

## Release gate

Do not create a final citation record, immutable release tag, GitHub Release or archive DOI until the author-controlled metadata above are explicitly approved. Scientific and repository-level reproducibility work is release-ready; remaining blockers are authorship/citation metadata, disclosure/licensing decisions and archival approval, not unresolved simulator tuning.
