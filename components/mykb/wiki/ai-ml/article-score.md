---
type: "concept"
title: "Article Score"
description: "A single composite number rating an article's quality"
tags: ["score", "quality", "metrics", "health"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Article Score

## Summary
The article score is a single composite number that rates an article's quality, rolled up from component sub-scores with recorded weights. Its job is prioritization — deciding which articles to promote, refresh, or review first — not a verdict on an article's worth.

## Details
- **Composite construction** — component sub-scores (content depth, clarity, citation coverage, freshness) are weighted and combined; the weights encode what the wiki values at a point in time.
- **Breakdown must travel with the score** — a composite hides its components, so the score is only meaningful when published with the sub-score breakdown and weights attached.
- **Drives triage** — low-scoring keystone articles get review or rewrite first because their degradation hurts more readers; high-scoring articles can be promoted to stable status.
- **Score drift** — scores change as the graph and review ratings change, so they are recomputed on a schedule rather than stored as permanent labels.
- **For mykb** — the article score feeds the health dashboard and the promotion-queue ordering, and it sits alongside graph centrality so maintenance effort targets both importance and weakness.
- **Limits** — composite metrics can mask a single catastrophic sub-score, and weights tuned to one corpus may not transfer; both are reasons to keep the breakdown visible.

- **Worked example** — an article with strong content but stale citations gets a mid score; the breakdown shows the freshness sub-score dragging the composite, which routes it to the citation-refresh queue rather than a rewrite.
- **Updating cadence** — scores recompute on graph and review changes, and the dashboard shows both the current composite and its delta so a promotion is traceable to which sub-score improved.
## Related
- [[wiki/ai-ml/score-components|Score Components]] — the parts being combined
- [[wiki/ai-ml/article-health-scores|Article Health Scores]] — the component family
- [[wiki/ai-ml/clarity-score|Clarity Score]] — a major component
- [[wiki/concepts/promotion-readiness|Promotion Readiness]] — what the score gates
- [[wiki/ai-ml/centrality-weighting|Centrality Weighting]] — importance-side counterpart
- [[wiki/concepts/keystone-articles|Keystone Articles]] — highest-priority targets
