---
type: "concept"
title: "Error Codes in APIs"
description: "Stable machine-readable codes that make error responses actionable"
tags: ["api", "errors", "design", "http"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Error Codes in APIs

## Summary
API error codes are stable, machine-readable strings that identify a specific failure beyond the HTTP status. They let clients branch on the exact condition, let support correlate incidents, and survive status-code ambiguities.

## Details
An error response typically carries an HTTP status (400, 404, 409) plus a body with a code, message, and details: {"error": {"code": "rate_limit_exceeded", "message": "...", "details": {...}}}. The code is the contract — the human message may change, but clients depend on the code. RFC 7807 (Problem Details) standardizes the envelope with type, title, status, detail, and instance.

The mechanism: the HTTP status gives the coarse class (client vs server error); the code gives the precise reason (validation_failed, insufficient_scope, duplicate_entry). Codes must be stable across versions, documented, and additive — adding a code is safe, changing or removing one is breaking. Each code should map to retry behavior: retryable (timeouts, 429, 503) versus terminal (validation, 403), so clients can implement uniform handling.

Concrete example: a wiki API rejects a publish with 409 and code=conflict_revision_missing plus details containing the current revision. The client's sync logic reads the code, re-fetches, merges, and retries — no message parsing. A support ticket quoting the code and instance id points straight at the log line. Without codes, clients string-match on messages, which breaks on every copy edit.

Failure modes: codes that change between versions break client branches silently; messages that expose internal details (stack traces, SQL) leak information; the same condition represented by different codes on different routes defeats clients; and errors without an instance or trace id cannot be correlated in logs. Missing codes force clients to treat all 4xx alike, losing the retry-vs-terminal distinction.

Operational tradeoffs: designing a small, stable code taxonomy costs a little upfront design and pays back in client robustness and support efficiency; too granular a taxonomy churns, too coarse loses information. The pragmatic model: status plus code plus details plus instance, documented in the OpenAPI spec, with a registry that requires approval to add codes. Internal-only detail fields should be stripped from public responses.

RSIS3/mykb relevance: RSIS3 loops branch on error codes when calling external APIs; documenting the code taxonomy for wiki and dashboard services lets the loops handle retryable versus terminal errors uniformly.

## Related
- [[wiki/api-protocols/rest-api-design|REST API Design]]
- [[wiki/api-protocols/conditional-put|Conditional PUT]]
- [[wiki/api-protocols/error-contract-design|Error Contract Design]]
- [[wiki/api-protocols/problem-details|Problem Details]]
- [[wiki/api-protocols/http-conditional-requests|HTTP Conditional Requests]]
