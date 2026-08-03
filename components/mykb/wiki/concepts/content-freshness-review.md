---
type: "concept"
title: "Content Freshness Review"
description: "Periodic review of whether articles still reflect current facts and tooling"
tags: ["freshness", "maintenance", "review", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Content Freshness Review

## Summary
A content freshness review checks each article for dated claims, changed APIs, dead sources, and drift between the body and current best practice. A knowledge base that is never reviewed does not merely stagnate — it becomes actively misleading, because stale articles carry the same authority as fresh ones and readers cannot tell the difference without timestamps and review history.

## Details
- It is scheduled rather than reactive: a review calendar (monthly for fast-moving topics like Android tooling, yearly for stable ones like git basics) keeps rot from accumulating silently. Reactive reviews only happen after a failure surfaces the staleness, which is exactly when the wrong information has already been acted on. The schedule should be per-cluster, because obsolescence rates differ by an order of magnitude between topics.
- Freshness signals include release notes, source response codes, and the timestamps stored in frontmatter and source records. A concrete workflow: diff the article's claims against the current documentation of any referenced API, check that cited URLs still resolve to the expected content, and compare stated versions with the versions actually in use in the repo. Each finding should update either the article or a dated review note, so the next review can see what changed.
- The failure modes are distinct: a claim that was true and became false (version drift), a claim that was never verified (unfounded content), and a claim that is true but no longer relevant (superseded practice). All three require different fixes — update, verify, or remove — and the review should classify findings rather than blindly editing.
- For mykb, freshness review pairs with link-rot monitoring: an article can be factually fresh but citation-dead, and the two checks cover different failure modes. A page whose sources are gone but whose claims still hold needs its citations replaced; a page whose sources are alive but whose claims are wrong needs its body rewritten.
- RSIS3 relevance: fresh content is a retrieval-quality issue, not just a hygiene issue. When RSIS3 retrieves evidence for an improvement cycle, a stale article can supply confident, wrong premises; the review calendar is what keeps the memory layer's truthfulness high.

## Related
- [[wiki/concepts/timeliness-score|Timeliness Score]]
- [[wiki/concepts/dated-claims|Dated Claims]]
- [[wiki/concepts/stale-articles|Stale Articles]]
- [[wiki/api-services/source-review-schedules|Source Review Schedules]]
- [[wiki/api-services/link-rot-monitoring|Link-Rot Monitoring]]
- [[wiki/concepts/content-freshness-review|Content Freshness Review]]
