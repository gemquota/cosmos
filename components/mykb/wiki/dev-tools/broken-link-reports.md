---
type: "concept"
title: "Broken Link Reports"
description: "Reports that list wikilinks pointing at non-existent files"
tags: ["links", "reports", "maintenance", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Broken Link Reports

## Summary
Broken link reports are the output of the global link check: each entry names the source article, the broken target, and often a suggested correct target.

## Details
- A report without a fix queue is just noise, so entries should be triaged into fixable-now, needs-decision, and already-fixed categories.
- Recurring broken-link patterns (same stale target across many pages) usually trace to one rename that skipped its link updates.
- For mykb, broken link reports feed link-fix sprints and are tracked on the health dashboard.

## Related
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/dev-tools/link-fix-automation|Link-Fix Automation]]
- [[wiki/dev-tools/fix-dry-runs|Fix Dry Runs]]
- [[wiki/dev-tools/link-updates|Link Updates]]
- [[wiki/concepts/wiki-health-dashboard|Wiki Health Dashboard]]
- [[wiki/api-services/dead-link-detection|Dead Link Detection]]
