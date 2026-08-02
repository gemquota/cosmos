---
type: "concept"
title: "Handling 502"
description: "Bad Gateway responses and debugging upstream failures behind proxies"
tags: ["http", "status-codes", "proxies", "ops"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Handling 502

## Summary
Bad Gateway responses and debugging upstream failures behind proxies. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- 502 Bad Gateway means an upstream produced an invalid response
- Debugging spans proxies, load balancers, and upstream crashes
- Open question — how do observability tools attribute 502s to the right hop?

## Related
- [[wiki/api-protocols/rest-api-design|REST API Design]] — related coverage in the same cluster
- [[wiki/api-protocols/504-handling|Handling 504]] — related coverage in the same cluster
- [[wiki/api-protocols/quota-headers|Quota Headers]] — related coverage in the same cluster
- [[wiki/api-protocols/retry-after-web|Retry-After]] — related coverage in the same cluster
- [[wiki/api-protocols/http-status-codes|HTTP Status Codes]] — related coverage in the same cluster
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]] — related coverage in the same cluster
- [[wiki/api-protocols/error-contract-design|Error Contract Design]] — related coverage in the same cluster
