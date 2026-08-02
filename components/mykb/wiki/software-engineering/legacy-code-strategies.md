---
type: "concept"
title: "Legacy Code Strategies"
description: "Working safely with old, untested, high-risk codebases"
tags: ["legacy-code", "strategy", "refactoring", "risk"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Legacy_code", "https://martinfowler.com/bliki/StranglerFigApplication.html"]
---

# Legacy Code Strategies

## Summary
Legacy code is old code that people fear to change — usually because it lacks tests. Strategies for it are conservative: characterize behavior first, add seams for testing, make small changes, and strangler out whole pieces when growth demands it.

## Details
- Michael Feathers' definition: code without tests. The strategy starts with characterization tests that pin current behavior.
- Seams — injection points for tests — turn untouchable code into changeable code one seam at a time.
- Small, behavior-preserving steps with continuous verification beat big rewrites on unowned code.
- The strangler pattern replaces legacy systems incrementally, routing new behavior to new code until the old dies.
- Budget and ownership are the real levers: legacy code rots faster without an explicit improvement budget.
- For the mykb bundle, legacy is the old curation pipeline: characterize it, wrap it with tests, strangler it feature by feature.
- Worked example — the wiki's old sync script has no tests; a characterization test pins its behavior, a seam injects a fake clock, and a new sync stage stranglers it incrementally.

Worked example — the wiki's old sync script has no tests; a characterization test pins its behavior, a seam injects a fake clock, and a new sync stage stranglers it incrementally.

## Related
- [[wiki/software-engineering/refactoring-techniques|Refactoring Techniques]]
- [[wiki/software-engineering/technical-debt-management|Technical Debt Management]]
- [[wiki/compositions/strangler-pattern|Strangler Pattern]]
- [[wiki/compositions/monolith-to-microservices|Monolith to Microservices]]
- [[wiki/testing/characterization-testing|Characterization Testing]]
- [[wiki/software-engineering/unit-testing-practice|Unit Testing Practice]]
- [[wiki/software-engineering/refactoring|Refactoring]]
- [[wiki/software-engineering/technical-debt|Technical Debt]]
- [[wiki/compositions/feature-toggles|Feature Toggles]]
