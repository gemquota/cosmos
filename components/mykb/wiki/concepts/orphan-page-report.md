---
type: "concept"
title: "Orphan Page Report"
description: "A report of pages with no incoming links, unreachable from the rest of the wiki"
tags: ["orphans", "report", "links", "discoverability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Orphan Page Report

## Summary
An orphan page has zero incoming links, so nothing in the wiki navigates to it; the orphan report is the list that makes them findable to curators. The report exists because orphans are invisible by definition: no link reaches them, so no browsing path, search ranking signal, or knowledge-graph traversal will surface them — only a systematic audit can.

## Details
- Orphans usually mean one of three things: the page is new, the page was renamed without updating referrers, or the page deserves no referrers and should be archived. New pages are orphans in the moment before anyone links to them — a normal, transient state that the report identifies for immediate linking. Renamed pages become orphans when the referrers still point at the old slug or the links were bulk-deleted; this is a mechanical failure with a mechanical fix. Pages that no longer fit the wiki's scope accumulate referrers that get pruned over time, and the report flags them so a curator decides whether they deserve re-integration or archival.
- The fix is editorial, not mechanical: link it from the most semantically related existing pages, or argue for archival. Mechanical fixes fail because they create arbitrary links — linking an orphan to a random hub page technically resolves the orphan status but damages the graph's semantic integrity. The correct response requires judgment: find the pages whose content genuinely connects, and add the links there. When no honest connection exists, that is evidence the page does not belong, and archival is the honest action.
- The failure mode of the report itself is false orphans: pages that are linked only by tools, index pages, or the file system rather than by wiki links, and pages whose only referrers were deleted. The report should be read with the full link picture — incoming-link counts and the graph layout — before acting.
- For mykb, the orphan report is a standing output of the graph-health pass, and link-updates after renames are the main prevention. Renames are the highest-volume orphan generator in active wikis, so a convention of updating referrers in the same change that renames a page prevents most orphans before the report ever sees them.

## Related
- [[wiki/concepts/incoming-link-counts|Incoming Link Counts]]
- [[wiki/dev-tools/link-updates|Link Updates]]
- [[wiki/concepts/archival-criteria|Archival Criteria]]
- [[wiki/concepts/discoverability-score|Discoverability Score]]
- [[wiki/syntheses/graph-health-checks|Graph Health Checks]]
- [[wiki/concepts/keystone-articles|Keystone Articles]]
