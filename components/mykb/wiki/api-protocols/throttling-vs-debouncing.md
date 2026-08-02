---
type: "concept"
title: "Throttling vs Debouncing"
description: "Two input-rate strategies: fixed-rate limiting versus trailing-edge coalescing"
tags: ["javascript", "performance", "events", "ux"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Throttling vs Debouncing

## Summary
Two input-rate strategies: fixed-rate limiting versus trailing-edge coalescing. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Throttling emits at most once per interval; debouncing emits after quiet
- Each suits different events: scroll position versus resize completion
- Open question — when does rAF sampling beat both for UI work?

## Related
- [[wiki/api-protocols/rate-limiting-api|Rate Limiting for APIs]] — related coverage in the same cluster
- [[wiki/api-protocols/api-throttling|API Throttling]] — related coverage in the same cluster
- [[wiki/api-protocols/throttling-vs-debouncing|Throttling vs Debouncing]] — related coverage in the same cluster
- [[wiki/api-protocols/api-throttling|API Throttling]] — related coverage in the same cluster
- [[wiki/api-protocols/rate-limiting|Rate Limiting]] — related coverage in the same cluster
- [[wiki/api-protocols/rate-limit-algorithms|Rate Limit Algorithms]] — related coverage in the same cluster
- [[wiki/api-protocols/rate-limit-headers|Rate Limit Headers]] — related coverage in the same cluster
