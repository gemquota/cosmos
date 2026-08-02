---
type: "concept"
title: "Content Freshness Review"
description: "Periodic review of whether articles still reflect current facts and tooling"
tags: ["freshness", "maintenance", "review", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Content Freshness Review

## Summary
A content freshness review checks each article for dated claims, changed APIs, dead sources, and drift between the body and current best practice.

## Details
- It is scheduled rather than reactive: a review calendar (monthly for fast-moving topics like Android tooling, yearly for stable ones like git basics) keeps rot from accumulating silently.
- Freshness signals include release notes, source response codes, and the timestamps stored in frontmatter and source records.
- For mykb, freshness review pairs with link-rot monitoring: an article can be factually fresh but citation-dead, and the two checks cover different failure modes.

## Related
- [[wiki/concepts/timeliness-score|Timeliness Score]]
- [[wiki/concepts/dated-claims|Dated Claims]]
- [[wiki/concepts/stale-articles|Stale Articles]]
- [[wiki/api-services/source-review-schedules|Source Review Schedules]]
- [[wiki/api-services/link-rot-monitoring|Link-Rot Monitoring]]
- [[wiki/concepts/content-freshness-review|Content Freshness Review]]
