---
type: "concept"
title: "Retry-After"
description: "HTTP header telling clients when a temporarily unavailable resource may be retried"
tags: ["http", "retry", "headers", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Retry-After

## Summary
HTTP header telling clients when a temporarily unavailable resource may be retried. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Retry-After carries an HTTP date or delay seconds
- Clients must honor it to avoid thundering herds after outages
- Open question — how do retry schedulers parse and cap it safely?

## Related
- [[wiki/api-protocols/rest-api-design|REST API Design]] — related coverage in the same cluster
- [[wiki/api-protocols/429-handling|Handling 429]] — related coverage in the same cluster
- [[wiki/api-protocols/503-handling|Handling 503]] — related coverage in the same cluster
- [[wiki/api-protocols/502-handling|Handling 502]] — related coverage in the same cluster
- [[wiki/api-protocols/http-status-codes|HTTP Status Codes]] — related coverage in the same cluster
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]] — related coverage in the same cluster
- [[wiki/api-protocols/error-contract-design|Error Contract Design]] — related coverage in the same cluster
