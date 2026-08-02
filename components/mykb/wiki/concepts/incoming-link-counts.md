---
type: "concept"
title: "Incoming Link Counts"
description: "How many other articles link to a given page"
tags: ["links", "backlinks", "metrics", "discoverability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Incoming Link Counts

## Summary
Incoming link count is the number of distinct articles with a wikilink to a target page — the wiki equivalent of backlinks.

## Details
- High counts usually mark keystone or hub articles; zero counts mark orphans that the rest of the graph cannot reach.
- Counts are distinct-article based: five links from one page should count once, otherwise a single noisy source inflates the number.
- For mykb, incoming counts feed the discoverability score and the orphan-page report, and they change the moment a curation pass adds or removes links.

## Related
- [[wiki/memory/backlinks|Backlinks]]
- [[wiki/concepts/orphan-page-report|Orphan Page Report]]
- [[wiki/concepts/outbound-link-counts|Outbound Link Counts]]
- [[wiki/concepts/bidirectional-link-ratio|Bidirectional Link Ratio]]
- [[wiki/concepts/discoverability-score|Discoverability Score]]
- [[wiki/concepts/keystone-articles|Keystone Articles]]
