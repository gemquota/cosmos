---
type: "concept"
title: "Link Score"
description: "The sub-score rating an article's link behavior"
tags: ["score", "links", "metrics", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Link Score

## Summary
The link score rates an article's linking: outbound count and diversity, inbound support, reciprocity, and whether links carry context.

## Details
- It is the most automatable component — counts and ratios come straight from the link graph.
- Link score rewards integration, not volume: a page with ten scattered links can score below one with five contextual ones.
- For mykb, the link score is computed from the graph metrics and feeds the article score.

## Related
- [[wiki/ai-ml/score-components|Score Components]]
- [[wiki/ai-ml/link-score|Link Score]]
- [[wiki/ai-ml/link-diversity|Link Diversity]]
- [[wiki/concepts/outbound-link-counts|Outbound Link Counts]]
- [[wiki/concepts/bidirectional-link-ratio|Bidirectional Link Ratio]]
- [[wiki/ai-ml/article-score|Article Score]]
