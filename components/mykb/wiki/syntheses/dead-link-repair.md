---
type: "synthesis"
title: "Dead-Link Repair"
description: "Finding and fixing links that point nowhere"
tags: ["dead-links", "repair", "link-rot", "wiki"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Dead_link", "https://en.wikipedia.org/wiki/Link_rot"]
---

# Dead-Link Repair

## Summary
Dead-link repair is the process of detecting links that no longer resolve — renamed files, moved pages, rot — and fixing them to the correct target or removing them. It is the outbound counterpart of orphan detection and a standing item in every wiki health check.

## Details
- **Detection** — crawl all wikilinks and compare against the file index; report targets that fail to resolve.
- **Repair strategies** — retarget to the moved page, fix casing/typos, or delete the link when the target is gone.
- **Prevention** — keep slugs stable, document renames, and check links at write time (the mykb linter does).
- **Link rot context** — the web version of the same problem (404s, moved domains) motivates permalinks and archives.
- **RSIS3 relevance** — pass verification catches dead wikilinks before consolidation, keeping the graph navigable.

## Related
- [[wiki/syntheses/graph-health-checks|Graph Health Checks]] — the detection pass
- [[wiki/syntheses/orphan-detection|Orphan Detection]] — the inbound counterpart
- [[wiki/syntheses/graph-health-checks|graph-health-checks]] — the general problem
- [[wiki/syntheses/knowledge-graph-maintenance|Knowledge Graph Maintenance]] — the upkeep context
- [[wiki/syntheses/graph-health-checks|graph-health-checks]] — the checker
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — graph that stays navigable
- [[wiki/syntheses/knowledge-synthesis|Knowledge Synthesis]] — the synthesis step in the existing graph
- [[wiki/syntheses/transparency-reports|Transparency Reports]] — reporting outcomes
- [[wiki/concepts/eval-contamination|Eval Contamination]] — measurement hygiene
