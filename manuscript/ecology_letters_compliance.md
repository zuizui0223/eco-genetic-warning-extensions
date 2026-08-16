# Ecology Letters compliance gate

## Selected article type

**Letter.** The manuscript reports original model-based ecological research and should remain positioned as a general ecological contribution rather than a software, protocol, or sensitivity-analysis paper.

## Current journal limits checked 17 July 2026

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
- Text boxes: **none**.
- Running title: **Eco-genetic closure and warning**.
- Keywords: **early warning; eco-evolutionary dynamics; fragmentation; functional extinction; genetic diversity; genetic monitoring; interaction feedback; mutation bias; recurrent transition; trait loss**.

The six-figure allocation exactly reaches the Letter display-item ceiling. Figure 3 now absorbs the former stand-alone candidate-composition display, freeing Figure 4 for cumulative warning/loss incidence while preserving six main figures overall.

## Automated gates

`scripts/check_ecology_letters_compliance.py` checks:

1. abstract length is at most 150 words;
2. estimated main-text length is at most 5,000 words;
3. the allocation declares exactly six main figures and no main tables or text boxes;
4. running title is shorter than 45 characters;
5. keyword count is at most 10;
6. all main and supplementary display labels are unique.

The script is a repository guard, not a replacement for the word count produced by the final Word or journal submission file. Template conversion must repeat the counts because equations, hyphenation, and journal software can tokenize words differently.

## Current development counts

The identification-revised Markdown remains within the Letter limits:

- abstract: **150 words**;
- estimated main text: **approximately 3,850 words** under the repository tokenizer;
- main display items: **6 figures**;
- main tables: **0**;
- keywords: **10**;
- running title: **31 characters**.

The final converted DOCX must be counted again.

## Remaining non-author checks

- Run the complete repository test suite and the rebuilt submission-bundle workflow on the identification-review head.
- Render the regenerated Figures 1–6 at intended journal width in colour and grayscale; check Figure 3 dense labels, Figure 5 narrow categories, and Figure 6 interval/`n` labels.
- Confirm that every Figure 1–6 call agrees with captions and file names and every Table S1–S5 call is restricted to Supplementary Material.
- Rebuild the supervisor/submission DOCX **from scratch** from the revised manuscript and current six figures; do not reuse the previous Word package containing orphaned media.
- Generate final title-page counts from that clean converted submission file.
- Prepare the 50 mm × 60 mm graphical-abstract asset at revision stage.
- Rebuild and independently verify the checksummed bundle from merged `main` only after manuscript freeze.

## Source of truth

The limits above were taken from the official Wiley Ecology Letters author guidance accessed on 17 July 2026. Recheck immediately before submission because journal requirements can change.
