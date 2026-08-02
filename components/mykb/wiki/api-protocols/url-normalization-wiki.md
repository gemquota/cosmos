---
type: "concept"
title: "URL Normalization"
description: "Canonicalizing equivalent URLs so they compare equal"
tags: ["urls", "normalization", "tooling", "references"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# URL Normalization

## Summary
URL normalization rewrites equivalent URLs to one canonical form — stripping tracking parameters, resolving default ports, standardizing scheme and trailing slash — so checks can compare them.

## Details
- Normalization is the prerequisite for url-deduplication: without it, the same page referenced twice with different query strings looks like two sources.
- Normalization rules must be conservative: stripping a parameter that changes content would corrupt the citation.
- For mykb, URL normalization runs over reference blocks and feeds source-health reports.

## Related
- [[wiki/api-protocols/url-formatting|URL Formatting]]
- [[wiki/api-protocols/url-deduplication|URL Deduplication]]
- [[wiki/api-protocols/url-normalization-wiki|URL Normalization]]
- [[wiki/api-protocols/archive-urls|Archive URLs]]
- [[wiki/cloud-infra/source-vetting|Source Vetting]]
- [[wiki/api-services/dead-link-detection|Dead Link Detection]]
