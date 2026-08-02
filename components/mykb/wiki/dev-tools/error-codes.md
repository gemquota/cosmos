---
type: "concept"
title: "Error Codes"
description: "Stable identifiers attached to failures so they can be looked up and handled uniformly"
tags: ["errors", "codes", "contracts", "debugging"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Error Codes

## Summary
Error codes are stable machine-readable identifiers for failure conditions, often paired with a human message and a lookup table. They make errors searchable, testable, and consistent across clients.

## Details
- Prefer typed errors plus codes over string matching; codes are for stable identification, messages for humans.
- Document every code with meaning, likely causes, and remediation — a code without docs is a mystery.
- Reserve codes for categories, not instances: ERROR_TIMEOUT, not ERROR_TIMEOUT_AT_17_43.
- mykb relevance: article sync failures get codes (SYNC_CONFLICT, LINK_BROKEN) that dashboards can count.

## Related
- [[wiki/dev-tools/error-contracts|Error Contracts]]
- [[wiki/dev-tools/exception-handling-practice|Exception Handling Practice]]
- [[wiki/dev-tools/structured-logs|Structured Logs]]
- [[wiki/api-protocols/http-status-codes|HTTP Status Codes]]
- [[wiki/dev-tools/error-tracking-tools|Error Tracking Tools]]
