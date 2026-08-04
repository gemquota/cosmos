---
type: "entity"
title: "ValidationResult"
timestamp: "2026-07-19T22:41:42Z"
resource: ""
---
description: "The structured outcome of a validation: status, errors, and actionable detail"
tags: ["entity", "android", "api", "ast", "auth", "authorization", "validation", "results"]

# ValidationResult

## Summary
A validation result is the structured outcome of a validation run: whether the input passed, which checks failed, and why. It matters because validators are only useful if callers can act on their verdicts programmatically. A consistent result shape turns validation from a bare boolean into a diagnosable, machine-readable contract that UIs and automation can share, which is why the shape deserves its own design.

## Details
- **Definition** — a validation result carries a status, a collection of errors or warnings, and optional metadata about what was checked.
- **Status semantics** — clear states such as valid, invalid, and warning-with-acceptance let callers distinguish hard failures from advisories.
- **Error granularity** — each problem should reference the failing field, rule, and value so callers can correct input precisely.
- **Aggregation** — collecting all failures in one pass beats failing on the first, since users can fix everything at once.
- **Machine readability** — stable error codes and structured fields support automated handling, while messages stay human-readable.
- **Composability** — nested results mirror complex inputs, letting a result for a form contain results for each field.
- **Severity** — tagging errors as blocking or advisory lets pipelines decide whether to stop or proceed with warnings.
- **Localization** — stable codes let UIs translate messages without re-parsing validators or embedding display text in logic.
- **Common failure modes** — results that only say no, errors that mix levels, and codes that change between releases.
- **Worked example** — a form validator returns a result with two field errors; the UI maps each code to a localized message and highlights the fields.
- **Practical relevance** — a well-defined validation result makes validation logic reusable and its outcomes safe to automate.

## Related
- [[wiki/api-protocols/error-contract-design|Error Contract Design]] — structured error shapes
- [[wiki/api-protocols/json-schema-validation|JSON Schema Validation]] — schema-based checks
- [[wiki/testing/schema-contract-validation|Schema Contract Validation]] — contract checking
- [[wiki/testing/error-guessing|Error Guessing]] — finding failure cases
- [[wiki/api-protocols/error-codes-api|Error Codes in APIs]] — stable codes
- [[wiki/testing/test-configuration-management|Test Configuration Management]] — validating configs
