---
type: "concept"
title: "Wiki Health Dashboard"
description: "A single view over metrics that track wiki growth, density, and quality"
tags: ["dashboard", "metrics", "health", "curation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Wiki Health Dashboard

## Summary
A wiki health dashboard aggregates the key ratios and trends — stub ratio, growth ratio, broken links, orphan pages, source health — into one view that a curator can read at a glance. It exists because wiki quality is not one number: it is a set of interacting signals, and the dashboard's job is to make the interactions visible so curation decisions are driven by the graph's actual state rather than by impressions.

## Details
- The core metrics: stub-ratio (share of pages still promising promotion), growth-ratio (new pages relative to total), broken-link count (dead navigation), orphan-page count (unreachable pages), bidirectional-link-ratio (reciprocity of the graph), and source health (dead or stale citations). Each is a different failure mode: stubs are deferred work, broken links are navigation debt, orphans are invisible content, low reciprocity is weak integration. No single metric tells the story — a wiki can have zero orphans and be full of stubs, or full articles and dead sources — so the dashboard's value is the joint view.
- Good dashboards pair a number with its denominator and its trend: a stub ratio of 40% means different things during an acquisition wave than after a promotion pass. The raw number is ambiguous; the trend disambiguates it. Rising stub ratio during a capture sprint is the expected cost of growth; the same ratio after a promotion pass is a failure of the pass. Trend context also prevents overreaction — a single bad week of broken links is noise; a persistent climb is a systemic issue. The dashboard should therefore be designed as a trends view, not a snapshot.
- The dashboard should surface alerts (spike in broken links, orphan cluster forming) rather than only reporting raw counts. A health dashboard that just displays numbers requires the curator to know what to worry about; an alerting dashboard encodes the thresholds — "broken links up 20% week over week", "a new cluster of orphans appeared" — and directs attention where intervention is needed. Alerts are where the dashboard becomes a control loop rather than a report.
- The failure modes of the dashboard itself: metric gaming (curators optimize the displayed numbers rather than the wiki's health), dashboard obsolescence (metrics defined for the old corpus no longer discriminate), and the dashboard effect (what is displayed becomes what is managed, and what is not displayed is ignored).
- For mykb, the dashboard is the feedback loop for curation sprints: it shows whether promotion, link-fix, and archive work moved the metrics they were supposed to move — the same loop-closure discipline the RSIS3 system applies to its own improvement metrics.

## Related
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/orphan-page-report|Orphan Page Report]]
- [[wiki/concepts/stub-ratio|Stub Ratio]]
- [[wiki/dev-tools/broken-link-reports|Broken Link Reports]]
- [[wiki/syntheses/graph-health-checks|Graph Health Checks]]
- [[wiki/ai-ml/graph-density-metrics|Graph Density Metrics]]
