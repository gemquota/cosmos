---
type: "concept"
title: "Under Review"
description: "The state marking an article currently being reviewed"
tags: ["review", "state", "process", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Under Review

## Summary
Under-review marks an article that a reviewer has checked out and is actively working on, preventing double review.

## Details
- It is a transient state between needs-review and reviewed; articles that linger under-review indicate a stuck queue.
- The state should record who is reviewing and since when, so stalls are visible.
- For mykb, under-review pages are tracked in the review queue with the reviewer's name and start date.

## Related
- [[wiki/concepts/needs-review|Needs Review]]
- [[wiki/concepts/reviewed-tag|Reviewed Tag]]
- [[wiki/concepts/under-review|Under Review]]
- [[wiki/agent-systems/review-queues-wiki|Review Queues]]
- [[wiki/agent-systems/approval-workflows-wiki|Approval Workflows]]
- [[wiki/devops-infra/review-sprints|Review Sprints]]
