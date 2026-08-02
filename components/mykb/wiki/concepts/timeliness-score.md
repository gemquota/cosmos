---
type: "concept"
title: "Timeliness Score"
description: "The sub-score rating how current an article is"
tags: ["score", "timeliness", "metrics", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Timeliness Score

## Summary
The timeliness score rates how current an article is: source dates, dated claims, review status, and the freshness of fast-moving content.

## Details
- It is computed from the freshness signals — the difference between now and the article's review date, weighted by how fast the topic decays.
- A low timeliness score triggers refresh-days work, not demotion — staleness is fixable.
- For mykb, the timeliness score is the dashboard's canary for content rot.

## Related
- [[wiki/ai-ml/score-components|Score Components]]
- [[wiki/concepts/timeliness-score|Timeliness Score]]
- [[wiki/concepts/freshness-signals|Freshness Signals]]
- [[wiki/concepts/stale-articles|Stale Articles]]
- [[wiki/devops-infra/refresh-days|Refresh Days]]
- [[wiki/concepts/content-freshness-review|Content Freshness Review]]
