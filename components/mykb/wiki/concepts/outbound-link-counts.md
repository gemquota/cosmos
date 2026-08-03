---
type: "concept"
title: "Outbound Link Counts"
description: "How many distinct articles a given page links to"
tags: ["links", "metrics", "navigation", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Outbound Link Counts

## Summary
Outbound link count is the number of distinct targets a page links to; it measures how well the page situates itself in the knowledge graph. A page's outbound links are its claims of relevance — "these ideas connect" — and the count is a rough signal of whether the page is doing the work of integration that a knowledge base requires.

## Details
- Too few outbound links isolates the page; too many dilutes each link's context and reads as a tag dump rather than prose integration. The failure modes are symmetric and both are about navigation: a page with zero or one outbound links is a dead end for browsing — the reader reaches the end of what the page can teach and has nowhere to go — while a page with dozens of undifferentiated links stops being a reading experience and becomes a keyword list, where the links carry no explanation of why they are related. Both violate the wiki's purpose: links must carry meaning, and meaning needs both count and context.
- The count should be read alongside link context — a link buried in a list carries less meaning than one in the opening paragraph. Two pages can have identical outbound counts with completely different navigational value: one integrates its links into the prose where the reader learns why the connection matters; the other dumps them at the bottom in a bare list. The count is the crude signal; link context is the quality signal, and the two are read together.
- The metric also has a graph-theoretic face: outbound links are what make the knowledge graph traversable. A page with outbound links is a node that routes traffic; a page without them is a sink. Clusters of pages with healthy outbound sets form the connected subgraphs that retrieval and browsing depend on, and pages that never link anywhere are exactly what the orphan and connectivity checks are looking for from the other direction.
- The failure mode of the metric itself: gaming — pages padded with links to inflate counts, or counts read without checking whether the links resolve. Counts are a diagnostic to trigger inspection, not a score to maximize.
- For mykb, the related-block convention gives every article a predictable minimum outbound set, and linting flags pages below it. The convention standardizes the floor — every article links its nearest relatives — so the count metric has a baseline to compare against, and outliers in either direction are flagged for review.

## Related
- [[wiki/concepts/incoming-link-counts|Incoming Link Counts]]
- [[wiki/dev-tools/related-blocks|Related Blocks]]
- [[wiki/concepts/link-context|Link Context]]
- [[wiki/concepts/first-paragraph-links|First-Paragraph Links]]
- [[wiki/ai-ml/link-score|Link Score]]
- [[wiki/ai-ml/link-diversity|Link Diversity]]
