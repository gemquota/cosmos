---
type: "synthesis"
title: "Graph Health Checks"
description: "Automated checks that verify a knowledge graph's structural integrity"
tags: ["graph-health", "checks", "verification", "knowledge"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Data_quality", "https://en.wikipedia.org/wiki/Referential_integrity"]
---

# Graph Health Checks

## Summary
Graph health checks are automated scans that verify a knowledge graph's structural integrity: all links resolve, no orphans or duplicates accumulate, frontmatter is valid, and density is stable. They turn 'the wiki is getting messy' into a measurable, fixable signal.

## Details
- **Check classes** — link resolution, orphan detection, duplicate titles, schema/frontmatter validity, and coverage gaps.
- **Frequency** — run per-pass and on a schedule; failures block consolidation until fixed.
- **Metric caution** — health checks measure structure, not meaning; they must be paired with quality sampling.
- **Worked example** — verify_pass3.py checks every expected file's existence, frontmatter, word count, and wikilink resolution.
- **RSIS3 relevance** — the pass verifier and linkmap builder are the bundle's health-check suite.

## Related
- [[wiki/syntheses/orphan-detection|Orphan Detection]] — a check class
- [[wiki/syntheses/dead-link-repair|Dead-Link Repair]] — the fix after a check
- [[wiki/syntheses/knowledge-graph-maintenance|Knowledge Graph Maintenance]] — the upkeep loop
- [[wiki/syntheses/wiki-stats-hub|Wiki Stats Hub Architecture & Snapshot Hygiene]] — a checked metric
- [[wiki/data-storage/data-quality-checks|Data Quality Checks]] — the general discipline
- [[wiki/syntheses/wiki-stats-hub|Wiki Stats Hub Architecture & Snapshot Hygiene]] — stats infrastructure
- [[wiki/syntheses/transparency-reports|Transparency Reports]] — reporting outcomes
- [[wiki/concepts/eval-contamination|Eval Contamination]] — measurement hygiene
