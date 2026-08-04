---
type: "entity"
title: "ValueError"
description: "A Python exception raised when a value is of the right type but wrong"
tags: ["entity", "exceptions", "python", "validation", "errors"]
timestamp: "2026-07-19T22:41:38Z"
resource: ""
---

# ValueError

## Summary

ValueError is a Python exception raised when an operation receives a value of the correct type but an inappropriate one — like converting a non-numeric string to int or asking for a negative square root. It matters because it distinguishes bad values from bad types, guiding callers toward validation. Catching it at boundaries keeps bad data from traveling deep into the system.

## Details

- **Definition** — ValueError signals a semantic error in a value: the type is fine but the content violates the operation's requirements.
- **Examples** — int("abc"), math.sqrt(-1), and unhashable sequence operations raise ValueError under different circumstances in the standard library.
- **Boundary validation** — Validating inputs where they enter — request parsing, file loading — converts deep ValueError surprises into early, clear failures.
- **Worked example** — An API parses a query parameter with int(); malformed input raises ValueError, which the handler converts to a 400 with a message naming the parameter.
- **Common failure modes** — Catching ValueError too broadly and masking bugs, or not catching it and leaking stack traces to users.
- **Custom errors** — Domain-specific subclasses carry structured context, letting handlers respond without parsing messages.
- **Practical relevance** — In data pipelines, ValueError usually indicates schema or format drift upstream, so the traceback points to where trust broke.
- **Telemetry note** — Recorded among many platform tags, consistent with a generic parsing error observed across environments.
- **Custom exceptions** — Subclassing ValueError with structured fields, such as the bad value and accepted range, lets handlers react without string parsing.
- **Validation at edges** — Schema validators and typed parsers reject bad values early, keeping ValueError out of deep business logic.
- **Worked example** — A config loader parses a port number; a non-integer value raises ValueError converted into a readable configuration error with the key name.
- **Testing** — Tests should cover the boundary values that trigger ValueError, since those are exactly where parsing contracts fail.

## Related

- [[wiki/api-services/categories/api-rest/subcategories/rest-http/exception-2|Exception]] — the exception family
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/keyerror|KeyError]] — missing-key sibling
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/errorcode|ErrorCode]] — coding the failure
- [[wiki/api-protocols/json-schema-validation|JSON Schema Validation]] — validating at the boundary
- [[wiki/api-protocols/error-codes-api|Error Codes API]] — mapping to responses
- [[wiki/dev-tools/debug-logging|Debug Logging]] — tracing bad values
