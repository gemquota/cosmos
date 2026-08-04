---
type: "entity"
title: "Wiki Index"
description: "Wiki Index: index pages that structure navigation and discoverability"
tags: ["entity", "ajax", "alpine", "android", "angular", "ansible", "documentation"]
timestamp: "2026-07-19T22:41:42Z"
resource: ""
---

# Wiki Index

## Summary

Wiki Index is the frontend entity for index pages: curated entry points that organize a wiki or documentation set into browsable structure. Indexes bridge search and navigation by grouping related pages. They matter because discoverability determines whether documented knowledge is ever used. Index pages are the wiki's navigation system, and like code, they need maintenance.

## Details

- **Definition** — An index page lists and links a set of related pages, giving readers a stable entry point into a cluster.
- **Structure** — Indexes group by topic, type, or workflow, making the collection's shape visible at a glance.
- **Bridging search** — Indexes complement full-text search by capturing relationships that text matching misses.
- **Maintenance** — Indexes rot when pages move or rename; automated link checks keep them truthful.
- **Convention** — This wiki uses a 00-index page per cluster, so navigation follows a predictable pattern.
- **Failure modes** — Stale links, orphaned pages, and indexes that duplicate rather than organize defeat the purpose.
- **Worked example** — The frontend cluster's index lists framework, tooling, and UX subclusters, each with its own index page.
- **Practical relevance** — Index discipline is what makes a growing wiki navigable instead of a flat pile of notes.
- **Consistency** — A uniform naming and placement convention makes indexes predictable across clusters.
- **Automation** — Generators and link checkers keep indexes in sync with the pages they list.
- **Entry depth** — Indexes should point at meaningful entry points, not every leaf, to keep browsing tractable.
- **Curation** — A human-reviewed index catches what automation cannot, such as renamed topics and obsolete sections.

## Related

- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/00-index|Angular Index]] — the cluster's own index
- [[wiki/web-platforms/00-index|Web Platforms Index]] — higher-level index
- [[wiki/entities/00-index|Entities Index]] — entity cluster index
- [[wiki/decisions/00-index|Decisions Index]] — decision cluster index
- [[wiki/memory/00-index|Memory Index]] — memory cluster index
- [[wiki/llm-agents/00-index|LLM Agents Index]] — another cluster index
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/00-index|Bootstrap Index]] — another cluster index
