---
type: "concept"
title: "Reviewed Tag"
description: "The tag confirming an article passed its latest review"
tags: ["review", "tags", "process", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Reviewed Tag

## Summary
The reviewed tag records that an article passed its latest review, with the review date as the meaningful payload.

## Details
- A reviewed tag without a date is nearly useless — review state decays with time, not with the tag's presence.
- Reviewed is the cleared state of needs-review and under-review, set by the reviewer at the end of the workflow.
- For mykb, reviewed tags feed the freshness report and let dashboards show coverage of the review schedule.

## Related
- [[wiki/concepts/needs-review|Needs Review]]
- [[wiki/concepts/under-review|Under Review]]
- [[wiki/concepts/review-tags|Review Tags]]
- [[wiki/concepts/reviewed-tag|Reviewed Tag]]
- [[wiki/concepts/verified-tag|Verified Tag]]
- [[wiki/devops-infra/review-sprints|Review Sprints]]
