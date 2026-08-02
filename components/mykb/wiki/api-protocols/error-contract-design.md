---
type: "concept"
title: "Error Contract Design"
description: "Error shapes, codes, and documentation"
tags: ["errors", "error-handling", "api-design", "contracts", "developer-experience"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://cloud.google.com/apis/design/errors", "https://stripe.com/docs/api/errors"]
---

# Error Contract Design

## Summary
An error contract is the promise of how failures look: a stable envelope, a stable set of codes, and documentation of what each code means. Well-designed error contracts turn failures from guesswork into machine-actionable signals — retryable vs permanent, which field is wrong, and where to get help.

## Details
- Shape: a consistent error object across every endpoint — code, message, details, and a correlation id; never a raw string or an ad-hoc struct.
- Codes: stable, documented identifiers (RESOURCE_NOT_FOUND, RATE_LIMITED) distinct from HTTP status codes; versioned like the API.
- Granularity: field-level errors (which field, why) for validation; endpoint-level codes for business failures.
- Retryability: expose whether an error is retryable (429/503, transient) — clients branch on it safely.
- Correlation: include a request/correlation id in error bodies and logs so support and debugging can tie failures together.
- Documentation: enumerate every code with cause, recovery steps, and examples; OpenAPI components define the error schema once.
- Anti-patterns: leaking stack traces or SQL, changing code meanings between versions, and burying errors in 200 responses.

## Related
- [[wiki/api-protocols/problem-details|Problem Details]] — an RFC-standard error envelope
- [[wiki/api-protocols/response-envelopes|Response Envelopes]] — where the error shape lives
- [[wiki/api-protocols/http-status-codes|HTTP Status Codes]] — codes complement status classes
- [[wiki/api-protocols/graphql-error-handling|GraphQL Error Handling]] — the GraphQL error contract
- [[wiki/api-protocols/contract-testing|Contract Testing]] — error shapes are part of the contract
