---
type: "entity"
title: "Exception"
description: "Exceptional control flow raised when code encounters an error condition"
tags: ["entity", "exceptions", "error-handling", "runtime", "programming"]
timestamp: "2026-07-19T22:41:39Z"
resource: ""
---

# Exception

## Summary

An exception is a language-level signal raised when code encounters an error condition, unwinding the stack until a handler catches it. Exceptions matter because they separate error handling from the happy path, but they also create subtle control flow. Disciplined exception design — typed errors, narrow catches, clear boundaries — keeps failures debuggable.

## Details

- **Definition** — Raising an exception interrupts normal execution and transfers control to the nearest matching handler up the call stack.
- **Hierarchies** — Typed exception classes let callers catch broad categories or precise cases; language runtimes ship standard hierarchies for common failures.
- **Try-catch semantics** — Handlers may catch, wrap, re-raise, or finally-cleanup; the semantics differ subtly across languages in scope and cleanup guarantees.
- **Checked vs unchecked** — Java distinguishes checked exceptions that callers must declare; Python, JavaScript, and Go use different explicit or value-based approaches.
- **Worked example** — A file parser opens a file, raises a specific ParseError on malformed input, and the caller catches it to report the offending line.
- **Common failure modes** — Swallowing exceptions silently, catching too broadly, using exceptions for normal control flow, and leaking stack traces to clients.
- **Practical relevance** — API boundaries convert exceptions into error responses, making the mapping between internal failures and external status codes a design decision.
- **Telemetry note** — The stub records Exception from session dd75982d among logging and CLI tags, reflecting its role in operational tooling.
- **Stack traces** — Preserving the original trace when wrapping exceptions keeps root-cause context through several layers of handling.
- **Boundary mapping** — An unhandled exception at the edge becomes a 500 with a correlation ID, while expected failures map to specific status codes.
- **Worked example** — A service catches a timeout exception, wraps it with the request ID, logs it, and returns a retryable error to the client.

## Related

- [[wiki/api-protocols/error-contract-design|Error Contract Design]] — mapping errors to responses
- [[wiki/api-protocols/error-codes-api|Error Codes API]] — coding failures for clients
- [[wiki/shell-environment/exit-codes-and-error-handling|Exit Codes and Error Handling]] — process-level failures
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/connectionerror|ConnectionError]] — network exception subtype
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/valueerro|ValueError]] — invalid value exception
- [[wiki/dev-tools/debug-logging|Debug Logging]] — logging exception paths
