# Protocol 002 Stage I — Bulk remaining plan

- batches: `36–134`
- batch count: `99`
- attempts per batch: `25`
- attempts in bulk run: `2,475`
- completed before bulk run: `900 / 3,375` after Wave 004 succeeds
- expected cumulative completion after bulk success: `3,375 / 3,375` (`100%`)
- configured matrix parallelism: `20`

GitHub Actions may queue jobs above the account concurrency limit. The workflow remains resumable because every batch writes a separate artifact and `fail-fast` is disabled.

This bulk run keeps the pinned upstream H1 source-reconstruction/projection design unchanged. H2/H3 horizon simulation remains outside Stage I.
