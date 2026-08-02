---
type: "concept"
title: "Legacy Code Testing"
description: "Introducing tests to untested legacy systems safely"
tags: ["legacy-code", "testing", "refactoring", "safety-net"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.oreilly.com/library/view/working-effectively-with/0131177052/", "https://understandlegacycode.com/"]
---

# Legacy Code Testing

## Summary
Legacy code testing introduces safety nets to untested, aging systems without rewriting them first. The goal is behavior preservation and confidence before refactoring, because untested changes are gambling.

## Details
- Start with characterization tests that lock in current behavior.
- Use seams, extracted methods and interfaces, to make code testable gradually.
- Prioritize high-risk, high-churn modules; cover the rest opportunistically.
- Add tests before touching a module: characterize, change, and verify.
- Feature flags and wrappers reduce the blast radius of refactors.
- Combine with static analysis to find dead code and risks.
- Success is confidence to refactor, not a coverage number.

## Related
- [[wiki/testing/characterization-testing|Characterization Testing]] — locking current behavior first
- [[wiki/testing/testability|Testability]] — seams needed in legacy code
- [[wiki/software-engineering/technical-debt|Technical Debt]] — the context legacy lives in
- [[wiki/software-engineering/refactoring|Refactoring]] — what the safety net enables
- [[wiki/testing/regression-testing|Regression Testing]] — protecting behavior during change
- [[wiki/testing/approval-testing|Approval Testing]] — baselines for legacy output
