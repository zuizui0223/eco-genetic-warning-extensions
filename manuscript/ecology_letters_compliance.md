# Ecology Letters compliance gate

## Selected article type

**Letter.** The manuscript reports original model-based ecological research and should remain positioned as a general ecological contribution rather than a software, protocol, or sensitivity-analysis paper.

## Current journal limits checked 16 August 2026

The official Ecology Letters author guidance specifies for a Letter:

- maximum main text: **5,000 words**;
- maximum combined display items: **6 figures, tables, or text boxes**;
- maximum abstract: **150 words**;
- running title: **fewer than 45 characters including spaces**;
- keywords: **up to 10**;
- title page must report article type, abstract word count, main-text word count, reference count, and numbers of figures, tables, and text boxes;
- the graphical abstract is required at major or minor revision, with a 2–3 sentence summary of no more than 500 characters and a legible 50 mm × 60 mm image.

## Locked submission allocation

- Article type: Letter.
- Main display items: **Figures 1–6 only**.
- Main tables: **none**.
- Supplementary tables: **Tables S1–S5**.
- Supplementary figures: **Figure S1** for the fresh fixed-area fragmentation gradient.
- Text boxes: **none**.
- Running title: **Eco-genetic closure and warning**.
- Keywords: **early warning; eco-evolutionary dynamics; fragmentation; functional extinction; genetic diversity; genetic monitoring; interaction feedback; mutation bias; recurrent transition; trait loss**.

The six-figure allocation exactly reaches the Letter display-item ceiling. The post-review fragmentation gradient is therefore kept in Supporting Information as Figure S1 rather than added to the main display count.

## Automated gates

`scripts/check_ecology_letters_compliance.py` checks:

1. abstract length is at most 150 words;
2. estimated main-text length is at most 5,000 words;
3. the allocation declares exactly six main figures and no main tables or text boxes;
4. running title is shorter than 45 characters;
5. keyword count is at most 10;
6. all main and supplementary display labels are unique.

The script is a repository guard, not a replacement for the word count produced by the final Word or journal submission file. Template conversion must repeat the counts because equations, hyphenation, and journal software can tokenize words differently.

## Current merged-main counts

After the completed fragmentation-gradient integration, the merged manuscript remains within the Letter limits under the repository tokenizer:

- abstract: **137 words**;
- estimated main text (Introduction through Conclusion): **4,416 words**;
- references: **21**;
- main display items: **6 figures**;
- main tables: **0**;
- text boxes: **0**;
- supplementary figure added by the D sensitivity: **Figure S1**;
- keywords: **10**;
- running title: **31 characters**.

The current main-text title is **“Eco-genetic regimes govern when genetic early warning can be validated”** and `manuscript/submission_metadata.md` is synchronized to that title. Final author approval of the title remains separate from this technical consistency check.

## Completed non-author checks

- [x] Complete repository invariant/compliance checks passed on the identification/gradient-integrated state.
- [x] Rebuilt submission-bundle workflow passed on merged `main` after D integration.
- [x] Figures 1–6 were regenerated and visually checked at journal width in colour and grayscale.
- [x] Supplementary Figure S1 was visually checked without smoothing away the non-monotonic realised-trait response.
- [x] Figure 1–6 calls, captions, and file names were synchronized.
- [x] The checksummed merged-main submission bundle contains the 9,600-row gradient record and separate historical/post-review parent provenance layers.
- [x] The merged-main submission manifest was independently verified with zero missing, mismatched, or unmanifested files.

## Remaining submission/revision checks

- Rebuild the supervisor/submission DOCX **from scratch** from the frozen manuscript and current six main figures plus Supporting Information; do not reuse a previous Word package containing orphaned media.
- Generate final title-page counts from that clean converted submission file and update the counts if Word/journal tokenization differs.
- Prepare the 50 mm × 60 mm graphical-abstract asset at major/minor revision stage.
- Replace repository/commit-based data and code wording with permanent archive DOI(s) after the author approves release metadata, licences, and versions.
- Recheck Ecology Letters/Wiley submission and automated-tool disclosure policies immediately before portal submission because journal requirements can change.

## Source of truth

The limits above were rechecked against the official Wiley Ecology Letters author guidance on 16 August 2026. Recheck immediately before submission.
