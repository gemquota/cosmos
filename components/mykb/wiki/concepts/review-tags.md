---
type: "concept"
title: "Review Tags"
description: "Tags that record an article's review state"
tags: ["review", "tags", "process", "metadata"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Review Tags

## Summary
Review tags record an article's review state — needs-review, under-review, reviewed — directly in its tag set.

## Details
- They make review state machine-readable: a dashboard can list every page that needs review by scanning tags.
- Review tags must be distinct from topical tags so automated tooling can tell process state from content.
- For mykb, review tags feed the review queues and are removed or updated by the review workflow.

## Related
- [[wiki/concepts/needs-review|Needs Review]]
- [[wiki/concepts/under-review|Under Review]]
- [[wiki/concepts/reviewed-tag|Reviewed Tag]]
- [[wiki/agent-systems/review-queues-wiki|Review Queues]]
- [[wiki/concepts/tags-practice|Tags Practice]]
- [[wiki/devops-infra/review-sprints|Review Sprints]]
