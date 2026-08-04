---
type: "entity"
title: "ErrorCode"
description: "A stable identifier for a failure that clients can branch on"
tags: ["entity", "errors", "codes", "api-design", "contracts"]
timestamp: "2026-07-19T22:41:42Z"
resource: ""
---

# ErrorCode

## Summary

An error code is a stable, machine-readable identifier for a failure mode, distinct from a human message. It matters because clients need to branch on failures programmatically, and messages change while codes should not. A good error-code taxonomy is small, documented, and versioned like the rest of the API contract.

## Details

- **Definition** — Error codes categorize failures — not_found, rate_limited, invalid_argument — so clients can react precisely.
- **Codes vs messages** — Messages are for humans and can change; codes are contract and should be treated as stable.
- **Hierarchies** — A code plus a namespace or type forms a hierarchy that balances specificity with client-side matching burden.
- **Worked example** — A payment API returns code insufficient_funds with a retryable flag; the client shows a top-up prompt instead of a generic error.
- **Common failure modes** — Duplicate codes for the same failure, codes so specific they multiply without bound, and clients matching on messages because codes are unstable.
- **Practical relevance** — Code-first error design improves SDK quality, monitoring, and support triage, all of which key off stable identifiers.
- **Documentation** — A public error catalog with causes and remediation turns errors into self-service documentation.
- **Telemetry note** — Recorded in API sessions alongside exception and logging tags, matching error-handling design work.
- **Retryability** — Marking codes as retryable or not gives clients a mechanical decision: retry with backoff or surface the error immediately.
- **Versioning** — Adding or renaming codes is a contract change; deprecated codes should map to replacements rather than vanish.
- **Worked example** — A client library switches on code, showing retry UI for rate_limited and validation forms for invalid_input, with a fallback for unknown codes.
- **Tooling** — Linters and generators can enforce that every raise site carries a documented code, keeping the catalog complete.

## Related

- [[wiki/api-protocols/error-codes-api|Error Codes API]] — the API practice
- [[wiki/api-protocols/error-contract-design|Error Contract Design]] — designing the contract
- [[wiki/api-protocols/http-status-codes|HTTP Status Codes]] — transport-level codes
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/exception-2|Exception]] — the internal failure
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/connectionerror|ConnectionError]] — a coded failure class
- [[wiki/testing/api-testing|API Testing]] — asserting error codes
