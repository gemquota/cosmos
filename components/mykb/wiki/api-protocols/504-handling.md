---
type: "concept"
title: "Handling 504"
description: "Gateway Timeout responses and upstream deadline propagation"
tags: ["http", "status-codes", "timeouts", "ops"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Handling 504

## Summary
Gateway Timeout responses and upstream deadline propagation. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- 504 Gateway Timeout fires when an upstream exceeds the timeout budget
- Propagating deadlines and streaming progress reduce false timeouts
- Open question — how do deadlines propagate across service meshes?

## Related
- [[wiki/api-protocols/rest-api-design|REST API Design]] — related coverage in the same cluster
- [[wiki/api-protocols/quota-headers|Quota Headers]] — related coverage in the same cluster
- [[wiki/api-protocols/retry-after-web|Retry-After]] — related coverage in the same cluster
- [[wiki/api-protocols/429-handling|Handling 429]] — related coverage in the same cluster
- [[wiki/api-protocols/http-status-codes|HTTP Status Codes]] — related coverage in the same cluster
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]] — related coverage in the same cluster
- [[wiki/api-protocols/error-contract-design|Error Contract Design]] — related coverage in the same cluster
