---
type: "entity"
title: "KeyError"
description: "An exception raised when a requested key is missing from a mapping"
tags: ["entity", "exceptions", "python", "mapping", "errors"]
timestamp: "2026-07-19T22:41:42Z"
resource: ""
---

# KeyError

## Summary

KeyError is a Python exception raised when code accesses a key that does not exist in a dictionary or other mapping. It matters because it is one of the most common runtime failures in Python code, usually revealing assumptions about data shape that are not true. Handling it well means either guarding access with membership checks or using defaults.

## Details

- **Definition** — Accessing mapping[key] for a missing key raises KeyError; the exception message names the offending key.
- **Prevention** — Membership tests, the get method with defaults, and setdefault or defaultdict structures avoid the exception at the source.
- **Data-shape lessons** — Frequent KeyErrors usually mean upstream data changed shape: a field is absent, renamed, or nested differently.
- **Worked example** — Parsing a JSON response, code reads record["id"]; a missing field raises KeyError, revealing that some records omit the id.
- **Common failure modes** — Catching KeyError too broadly, relying on exception text parsing, and ignoring the missing-key case so data silently drops.
- **Practical relevance** — In API and data pipelines, KeyError handling determines whether bad data surfaces loudly or corrupts silently.
- **Variants** — Other languages raise similar errors — JavaScript returns undefined, Java throws NoSuchElementException in maps depending on API.
- **Telemetry note** — Recorded in API and cloud sessions with an error tag, matching a real data-shape bug captured in telemetry.
- **Defaults** — dict.get and setdefault turn missing keys into controlled outcomes, but can mask bugs when absence is itself an error.
- **Typed models** — Validating parsed data into typed objects surfaces missing fields at the boundary instead of mid-logic.
- **Worked example** — An ingestion job validates each record against a schema first; a record missing a required field is rejected with a clear reason rather than raising KeyError later.

## Related

- [[wiki/api-services/categories/api-rest/subcategories/rest-http/valueerror-10|ValueError]] — sibling invalid-value error
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/exception-2|Exception]] — the exception family
- [[wiki/api-protocols/json-schema|JSON Schema]] — validating required fields
- [[wiki/api-protocols/json-schema-validation|JSON Schema Validation]] — catching shape drift
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/errorcode|ErrorCode]] — coding the failure
- [[wiki/dev-tools/debug-logging|Debug Logging]] — tracing missing keys
