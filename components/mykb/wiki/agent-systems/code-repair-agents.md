---
type: "concept"
title: "Code Repair Agents"
description: "Agents that diagnose failing code and produce patches validated by tests"
tags: ["repair-agents", "code", "repair", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Code Repair Agents

## Summary
Code repair agents diagnose failing code and produce patches validated by tests, closing the loop between test feedback and fixes. They matter because writing code is only half the job; getting it to pass its tests is where agents earn their keep. The repair loop turns test failures into concrete, verifiable fixes. Repair loops are only as good as the tests that define done.

## Details
- **Definition** — a repair agent takes failing code and its test output, localizes the fault, produces a patch, and re-runs the tests to confirm.
- **Loop structure** — the core loop is: run tests, read failures, localize, patch, re-run; each iteration narrows the remaining defect.
- **Dependencies** — repair quality depends on test coverage, the completeness of failure context, and the agent's ability to read code structurally.
- **Bounded retries** — retry limits and timeouts prevent infinite repair loops on unfixable or flaky problems.
- **Worked example** — a test fails on a null pointer; the agent traces the call site, adds a guard, re-runs the suite, and submits the patch for review.
- **Evaluation** — repair agents are benchmarked on real-world issues, such as swe-bench tasks, measuring fix rate and patch correctness.
- **Failure modes** — superficial patches that pass tests but break intent, regression-causing fixes, and flaky-test chasing are common failures.
- **Composition** — repair agents consume the output of testing-agents and hand verified patches to verifier-agents for approval.
- **Practical relevance** — code repair is a flagship agent workload because tests provide an objective quality signal for the loop.
- **Patch review** — patches should be reviewed for intent, not just test-passing, to avoid superficial fixes.
- **Regression guard** — new tests should accompany patches so the fix is protected.
- **Failure example** — a patch that removes the failing test instead of fixing the code passes the loop but solves nothing.

## Related
- [[wiki/agent-systems/code-generation-agents-revisited|Code Generation Agents]] — the generation sibling
- [[wiki/agent-systems/testing-agents|Testing Agents]] — the source of failure feedback
- [[wiki/ai-ml/swe-bench|SWE-bench]] — the benchmark for repair work
- [[wiki/agent-systems/retry-and-backoff-patterns|Retry and Backoff Patterns]] — bounding the repair loop
- [[wiki/agent-systems/verifier-agents|Verifier Agents]] — the approval layer for patches
