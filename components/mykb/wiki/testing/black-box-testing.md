---
type: "concept"
title: "Black-Box Testing"
description: "Testing external behavior without internal implementation knowledge"
tags: ["black-box", "testing", "behavioral", "technique"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.ibm.com/topics/black-box-testing", "https://www.istqb.org/glossary"]
---

# Black-Box Testing

## Summary
Black-box testing verifies external behavior, inputs, outputs, and interfaces, without knowledge of internal implementation. It tests what the system does, derived from requirements and specifications.

## Details
- Techniques: equivalence partitioning, boundary values, decision tables, state transitions, and error guessing.
- Levels: functional, integration, system, acceptance, and security testing.
- Strengths: mirrors the user perspective and stays independent of implementation details.
- Limitations: redundant tests are possible, and internals cannot be targeted directly.
- Pair with white-box insights such as coverage to close gaps.
- API and UI automation treat the system as a black box.
- Requirements quality directly drives black-box test quality.

## Related
- [[wiki/testing/white-box-testing|White-Box Testing]] — the implementation-aware complement
- [[wiki/testing/equivalence-partitioning|Equivalence Partitioning]] — a core black-box technique
- [[wiki/testing/decision-table-testing|Decision Table Testing]] — rule coverage from the outside
- [[wiki/testing/state-transition-testing|State Transition Testing]] — behavioral flows
- [[wiki/testing/api-testing|API Testing]] — black-box endpoint verification
- [[wiki/testing/acceptance-testing|Acceptance Testing]] — criteria-driven black-box checks
