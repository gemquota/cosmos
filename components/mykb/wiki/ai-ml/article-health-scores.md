---
type: "concept"
title: "Article Health Scores"
description: "Composite numeric scores that summarize the quality of a wiki article"
tags: ["metrics", "quality", "scores", "health"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Article Health Scores

## Summary
Article health scores condense many quality signals — links, sources, word count, metadata, freshness — into one number or a small scorecard that can trend over time.

## Details
- A composite score is only as honest as its components: each sub-score must be measurable and each weighting decision recorded, otherwise the score hides what it claims to reveal.
- Health dashboards sort by the score so curation effort lands on the weakest articles first, and threshold bands map scores to actions (promote, refresh, demote, archive).
- In mykb the score is a diagnostic, not a goal: gaming the score by padding word counts would fail the underlying quality checks.

## Related
- [[wiki/ai-ml/score-components|Score Components]]
- [[wiki/concepts/wiki-health-dashboard|Wiki Health Dashboard]]
- [[wiki/concepts/article-quality-checklist|Article Quality Checklist]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/syntheses/graph-health-checks|Graph Health Checks]]
- [[wiki/ai-ml/content-score|Content Score]]
