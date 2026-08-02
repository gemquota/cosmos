---
type: "concept"
title: "Partial Failure Handling"
description: "Graceful recovery when some components of a request fail"
tags: ["partial-failure", "reliability", "failure", "systems"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Partial Failure Handling

## Summary
Graceful recovery when some components of a request fail

## Details
- Identify which sub-calls failed and which succeeded.
- Retry, degrade, or escalate per failure class.
- Prevents whole-request failure from one bad tool call.
- Supported by idempotency and circuit breakers.

## Related
- [[wiki/agent-systems/idempotent-agent-actions|Idempotent Agent Actions]] — safe retries
- [[wiki/agent-systems/circuit-breakers-for-agents|Circuit Breakers for Agents]] — fault isolation
- [[wiki/agent-systems/retry-and-backoff-patterns|Retry and Backoff Patterns]] — retry policy
- [[wiki/agent-systems/degraded-mode-operations|Degraded Mode Operations]] — reduced quality
- [[wiki/prompt-engineering/error-messages-llm|Error Messages for LLMs]] — reporting
