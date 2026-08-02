---
type: "concept"
title: "Outbound Link Counts"
description: "How many distinct articles a given page links to"
tags: ["links", "metrics", "navigation", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Outbound Link Counts

## Summary
Outbound link count is the number of distinct targets a page links to; it measures how well the page situates itself in the knowledge graph.

## Details
- Too few outbound links isolates the page; too many dilutes each link's context and reads as a tag dump rather than prose integration.
- The count should be read alongside link context — a link buried in a list carries less meaning than one in the opening paragraph.
- For mykb, the related-block convention gives every article a predictable minimum outbound set, and linting flags pages below it.

## Related
- [[wiki/concepts/incoming-link-counts|Incoming Link Counts]]
- [[wiki/dev-tools/related-blocks|Related Blocks]]
- [[wiki/concepts/link-context|Link Context]]
- [[wiki/concepts/first-paragraph-links|First-Paragraph Links]]
- [[wiki/ai-ml/link-score|Link Score]]
- [[wiki/ai-ml/link-diversity|Link Diversity]]
