---
type: "concept"
title: "Handling 429"
description: "Client and server behavior for HTTP Too Many Requests responses"
tags: ["http", "rate-limiting", "status-codes", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Handling 429

## Summary
Client and server behavior for HTTP Too Many Requests responses. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- 429 Too Many Requests should include Retry-After and limit metadata
- Clients back off, queue, or degrade instead of hammering
- Open question — how does mykb's retry layer treat 429s today?

## Related
- [[wiki/api-protocols/rest-api-design|REST API Design]] — related coverage in the same cluster
- [[wiki/api-protocols/503-handling|Handling 503]] — related coverage in the same cluster
- [[wiki/api-protocols/502-handling|Handling 502]] — related coverage in the same cluster
- [[wiki/api-protocols/504-handling|Handling 504]] — related coverage in the same cluster
- [[wiki/api-protocols/http-status-codes|HTTP Status Codes]] — related coverage in the same cluster
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]] — related coverage in the same cluster
- [[wiki/api-protocols/error-contract-design|Error Contract Design]] — related coverage in the same cluster
