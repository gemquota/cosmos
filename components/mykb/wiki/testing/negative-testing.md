---
type: "concept"
title: "Negative Testing"
description: "Verifying graceful handling of invalid inputs and error paths"
tags: ["negative-testing", "testing", "error-handling", "robustness"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.ibm.com/topics/negative-testing", "https://owasp.org/www-project-web-security-testing-guide/"]
---

# Negative Testing

## Summary
Negative testing verifies the system handles invalid inputs, unauthorized actions, and error paths gracefully, with no crashes, clear errors, and safe state. Robustness is defined by how software behaves when things go wrong.

## Details
- Invalid inputs: wrong types, out-of-range values, malformed payloads, unicode, and huge sizes.
- Unauthorized actions: missing or expired tokens, forbidden roles, and IDOR attempts.
- System failures: timeouts, down dependencies, full disks, and network loss.
- Assert correct error codes, safe rollback, no data corruption, and useful messages.
- Derive negative cases from specifications, schemas, and threat models.
- Automate with parametrized invalid-input tables, fault injection, and fuzzing.
- Prioritize negative tests on high-traffic paths where failures are visible.

## Related
- [[wiki/testing/fault-injection|Fault Injection]] — forcing dependency error paths
- [[wiki/testing/boundary-value-analysis|Boundary Value Analysis]] — just-outside valid values
- [[wiki/testing/error-guessing|Error Guessing]] — heuristic negative cases
- [[wiki/testing/fuzzing|Fuzz Testing]] — automated malformed inputs
- [[wiki/testing/authentication-testing|Authentication Testing]] — unauthorized negative cases
- [[wiki/testing/api-testing|API Testing]] — error responses under test
