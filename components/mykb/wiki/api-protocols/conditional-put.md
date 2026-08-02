---
type: "concept"
title: "Conditional PUT"
description: "Using If-Match and ETags for safe, optimistic full updates"
tags: ["http", "rest", "concurrency", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Conditional PUT

## Summary
Using If-Match and ETags for safe, optimistic full updates. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- If-Match with an ETag makes PUT optimistic and conflict-safe
- Precondition failures return 412 and the current state
- Open question — how does conditional PUT interact with idempotency keys?

## Related
- [[wiki/api-protocols/rest-api-design|REST API Design]] — related coverage in the same cluster
- [[wiki/api-protocols/error-codes-api|Error Codes in APIs]] — related coverage in the same cluster
- [[wiki/api-protocols/conditional-put|Conditional PUT]] — related coverage in the same cluster
- [[wiki/api-protocols/error-codes-api|Error Codes in APIs]] — related coverage in the same cluster
- [[wiki/api-protocols/error-contract-design|Error Contract Design]] — related coverage in the same cluster
- [[wiki/api-protocols/problem-details|Problem Details]] — related coverage in the same cluster
- [[wiki/api-protocols/http-conditional-requests|HTTP Conditional Requests]] — related coverage in the same cluster
