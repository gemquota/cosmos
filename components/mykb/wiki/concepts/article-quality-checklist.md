---
type: "concept"
title: "Article Quality Checklist"
description: "Review criteria for promoting mykb articles from stub to full"
tags: ["mykb", "quality", "checklist", "curation"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Article Quality Checklist

## Summary
The article quality checklist is the review criteria mykb uses to decide when an article is good enough to leave stub status. It turns "this article should be better" from a taste judgment into a checkable list: substance, structure, links, provenance, and RSIS3 relevance.

## Details
- Substance is the first gate. A stub is a definition; a full article explains mechanisms, gives concrete examples, and names failure modes and tradeoffs. The checklist asks: could a reader reproduce or apply the idea from this page alone? If the answer is no, the article still needs work regardless of word count, because length without specificity is padding.
- Structure follows the standard mykb shape: a summary that states the core claim, a details section organized by mechanism or theme, and a related section that situates the article in the graph. Headings and bullets should make the article scannable; paragraphs of undifferentiated prose are a review flag.
- Links are checked in both directions. The article must link to the concepts it depends on, and the checklist verifies every wikilink resolves to an existing file so the knowledge graph stays navigable. Orphan articles and dead links are structural debt that the wiki-health dashboard tracks.
- Provenance matters for a knowledge base that feeds decision-making: claims that cite sources, name assumptions, and distinguish established results from speculation carry more weight. The checklist prefers explicit evidence markers ("measured", "observed", "in this repo") over unstated inference.
- RSIS3 relevance is the final criterion: an article should say why the knowledge matters to the system's loops, retrieval, or constraints. That tie-in is what makes the wiki a working memory rather than a static archive — it tells the next session where this concept plugs into self-improvement.
- Operational tradeoff: the checklist raises the bar for promotion, which slows the pipeline but keeps the graph trustworthy. The seed-article criteria govern creation, the stub criteria govern what counts as a stub, and this checklist governs the promotion decision.

## Related
- [[wiki/concepts/promotion-checklist|Promotion Checklist]] — the checklist in action
- [[wiki/concepts/stub-criteria|Stub Criteria]] — what counts as a stub
- [[wiki/concepts/seed-article-criteria|Seed Article Criteria]] — what gets seeded
- [[wiki/concepts/wiki-health-dashboard|Wiki Health Dashboard]] — graph health monitoring
- [[wiki/concepts/orphan-page-report|Orphan Page Report]] — link-structure debt
- [[wiki/syntheses/knowledge-graph-maintenance|Knowledge Graph Maintenance]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/data-storage/open-knowledge-format|Open Knowledge Format]]
- [[wiki/dev-tools/frontmatter-linting|Frontmatter Linting]]
- [[wiki/syntheses/graph-health-checks|Graph Health Checks]]
