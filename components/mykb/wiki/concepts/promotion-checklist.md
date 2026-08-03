---
type: "concept"
title: "Promotion Checklist"
description: "The concrete itemized steps executed when promoting a stub to growing"
tags: ["checklist", "promotion", "process", "curation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Promotion Checklist

## Summary
The promotion checklist is the operational form of promotion-readiness: each item maps to a pass/fail check on the article itself. It exists because promotion decisions are judgment calls, and judgment without structure drifts — the checklist forces every promotion to satisfy the same explicit criteria, in the same order, so that the graph's quality bar stays visible and auditable.

## Details
- Items include: status flipped, body expanded to the full-article word range, two or more curl-verified sources, every wikilink resolving, and at least the required forward and back links present. The word-range item enforces substance (the body must carry real content, not a padded definition); the source item enforces provenance (claims must trace to verifiable references); the link items enforce integration (the article must both link its relatives and be reachable from them). Each item is mechanically checkable, which is the point — a checklist item that requires taste is a review criterion, not a checklist item, and belongs in the quality checklist instead.
- The checklist also covers bookkeeping: the article's promotion should update the health dashboard inputs and any queue it was listed in. A promotion that changes the article but not the tracking data creates two truths — the article says "growing", the dashboard still counts it as a stub — and the bookkeeping items exist to prevent that divergence. The queue update matters for the same reason: if promotion waves are tracked in a queue, promoting without dequeuing breaks the wave's accounting.
- The order of items is deliberate: content checks come before bookkeeping, because a promotion should not be recorded until the article actually passes. Running the checklist bottom-up (bookkeeping first) is the classic failure — the system records a promotion that the article did not earn.
- For mykb, promotion checklists make the pass-3 style promotion waves auditable — the diff should show only the listed changes. An auditor can take any promoted article, re-run the checklist, and see whether the promotion was earned or gamed; that auditability is the checklist's real product.

## Related
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/concepts/article-quality-checklist|Article Quality Checklist]]
- [[wiki/concepts/full-article-ratio|Full Article Ratio]]
- [[wiki/dev-tools/frontmatter-linting|Frontmatter Linting]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/devops-infra/review-sprints|Review Sprints]]
