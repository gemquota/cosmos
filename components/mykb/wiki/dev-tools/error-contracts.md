---
type: "concept"
title: "Error Contracts"
description: "Agreements about the shape and semantics of errors between producers and consumers"
tags: ["errors", "contracts", "apis", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Error Contracts

## Summary
An error contract fixes what an error looks like — status, code, message, fields, retryability — so every caller can depend on it. APIs and libraries with defined error contracts are far easier to integrate and debug.

## Details
- Declare which errors are transient (caller may retry) versus permanent (caller should not).
- Stable field names beat stable prose: code, retryable, details, request_id.
- Version error payloads with the API; breaking the contract silently breaks every consumer.
- mykb relevance: the wiki service documents its error contract so agents handle failures deterministically.

## Related
- [[wiki/dev-tools/error-codes|Error Codes]]
- [[wiki/api-protocols/error-contract-design|Error Contract Design]]
- [[wiki/api-protocols/problem-details|Problem Details]]
- [[wiki/software-engineering/retry-patterns|Retry Patterns]]
- [[wiki/dev-tools/exception-handling-practice|Exception Handling Practice]]
