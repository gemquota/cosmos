---
type: "concept"
title: "Freshness Signals"
description: "The data points that reveal how fresh an article is"
tags: ["freshness", "signals", "metrics", "health"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Freshness Signals

## Summary
Freshness signals are the observable data that reveal an article's currency: source dates, access dates, review timestamps, dated claims, and change history.

## Details
- No single signal is enough — a recently edited article can still cite dead sources, and a never-touched article can be evergreen.
- The signals feed the timeliness score and the freshness report that plans refresh-days.
- For mykb, freshness signals are collected automatically from frontmatter and reference blocks.

## Related
- [[wiki/concepts/freshness-signals|Freshness Signals]]
- [[wiki/concepts/timeliness-score|Timeliness Score]]
- [[wiki/concepts/dated-claims|Dated Claims]]
- [[wiki/api-protocols/source-dates|Source Dates]]
- [[wiki/api-protocols/access-dates|Access Dates]]
- [[wiki/devops-infra/refresh-days|Refresh Days]]
