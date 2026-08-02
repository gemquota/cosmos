---
type: "concept"
title: "Handling 503"
description: "Service Unavailable responses, Retry-After, and graceful degradation"
tags: ["http", "status-codes", "reliability", "ops"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Handling 503

## Summary
Service Unavailable responses, Retry-After, and graceful degradation. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- 503 signals temporary unavailability, often with Retry-After
- Degraded modes and queuing beat unbounded client retries
- Open question — what distinguishes 503 from 429 in practice?

## Related
- [[wiki/api-protocols/rest-api-design|REST API Design]] — related coverage in the same cluster
- [[wiki/api-protocols/502-handling|Handling 502]] — related coverage in the same cluster
- [[wiki/api-protocols/504-handling|Handling 504]] — related coverage in the same cluster
- [[wiki/api-protocols/quota-headers|Quota Headers]] — related coverage in the same cluster
- [[wiki/api-protocols/http-status-codes|HTTP Status Codes]] — related coverage in the same cluster
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]] — related coverage in the same cluster
- [[wiki/api-protocols/error-contract-design|Error Contract Design]] — related coverage in the same cluster
