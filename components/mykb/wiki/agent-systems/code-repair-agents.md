---
type: "concept"
title: "Code Repair Agents"
description: "Agents that diagnose failing code and produce patches validated by tests"
tags: ["repair-agents", "code", "repair", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Code Repair Agents

## Summary
Agents that diagnose failing code and produce patches validated by tests

## Details
- Loop: run tests, read failures, localize, patch, re-run.
- Repair quality depends on test coverage and context.
- Bounded retries prevent infinite loops.
- A core workload for swe-bench.

## Related
- [[wiki/agent-systems/code-generation-agents-revisited|Code Generation Agents]] — generation sibling
- [[wiki/agent-systems/testing-agents|Testing Agents]] — feedback source
- [[wiki/ai-ml/swe-bench|SWE-bench]] — benchmark
- [[wiki/agent-systems/retry-and-backoff-patterns|Retry and Backoff Patterns]] — loop control
- [[wiki/agent-systems/verifier-agents|Verifier Agents]] — approval layer
