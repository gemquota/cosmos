---
type: "concept"
title: "Orphan Page Report"
description: "A report of pages with no incoming links, unreachable from the rest of the wiki"
tags: ["orphans", "report", "links", "discoverability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Orphan Page Report

## Summary
An orphan page has zero incoming links, so nothing in the wiki navigates to it; the orphan report is the list that makes them findable to curators.

## Details
- Orphans usually mean one of three things: the page is new, the page was renamed without updating referrers, or the page deserves no referrers and should be archived.
- The fix is editorial, not mechanical: link it from the most semantically related existing pages, or argue for archival.
- For mykb, the orphan report is a standing output of the graph-health pass, and link-updates after renames are the main prevention.

## Related
- [[wiki/concepts/incoming-link-counts|Incoming Link Counts]]
- [[wiki/dev-tools/link-updates|Link Updates]]
- [[wiki/concepts/archival-criteria|Archival Criteria]]
- [[wiki/concepts/discoverability-score|Discoverability Score]]
- [[wiki/syntheses/graph-health-checks|Graph Health Checks]]
- [[wiki/concepts/keystone-articles|Keystone Articles]]
