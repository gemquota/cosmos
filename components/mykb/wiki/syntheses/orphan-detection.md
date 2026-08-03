---
type: "synthesis"
title: "Orphan Detection"
description: "Finding nodes with no inbound links in a knowledge graph"
tags: ["orphans", "knowledge-graph", "detection", "wiki"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Backlink", "https://en.wikipedia.org/wiki/Link_rot"]
---

# Orphan Detection

## Summary
Orphan detection finds nodes no other node links to — knowledge that exists but is unreachable. Orphans signal coverage that was captured but never integrated, and they are the cheapest, most actionable sign of a knowledge base drifting toward disconnectedness.

## Details
- **Why orphans matter** — an orphaned note is effectively lost; backlink analysis is the standard detection tool.
- **Detection** — compare every node against the inbound-link index; flag zero-inbound nodes (except designated entry points).
- **Causes** — bulk imports, renamed topics, and passes that add pages without linking them.
- **Fix** — link orphans from related concepts or fold them into broader pages; occasionally delete true junk.
- **RSIS3 relevance** — the graph engine's backlink traversal and pass verifiers surface orphans for the next pass.

## Related
- [[wiki/syntheses/graph-health-checks|Graph Health Checks]] — where detection runs
- [[wiki/syntheses/dead-link-repair|Dead-Link Repair]] — the outbound counterpart
- [[wiki/memory/backlinks|Backlinks]] — the detection primitive
- [[wiki/syntheses/knowledge-graph-maintenance|Knowledge Graph Maintenance]] — the fix loop
- [[wiki/syntheses/wiki-self-improvement|Wiki Self-Improvement]] — the wiki context
- [[wiki/concepts/knowledge-graph-memory|Knowledge-Graph Memory]] — graph substrate
- [[wiki/syntheses/transparency-reports|Transparency Reports]] — reporting outcomes
- [[wiki/concepts/eval-contamination|Eval Contamination]] — measurement hygiene
