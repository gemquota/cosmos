---
type: "concept"
title: "Error Messages for LLM Systems"
description: "Designing and surfacing clear errors when models, tools, or pipelines fail"
tags: ["error-messages", "errors", "ux", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Error Messages for LLM Systems

## Summary
Designing and surfacing clear errors when models, tools, or pipelines fail

## Details
- Map failure modes to actionable messages for users and operators.
- Distinguish retryable, permanent, and safety errors.
- Good errors speed debugging and recovery.
- Feed user-confirmation-flows and escalation.

## Related
- [[wiki/agent-systems/partial-failure-handling|Partial Failure Handling]] — failure taxonomy
- [[wiki/agent-systems/retry-and-backoff-patterns|Retry and Backoff Patterns]] — retry guidance
- [[wiki/agent-systems/escalation-handling|Escalation Handling]] — handoff on failure
- [[wiki/agent-systems/model-fallback-chains|Model Fallback Chains]] — degraded responses
- [[wiki/llm-agents/user-confirmation-flows|User Confirmation Flows]] — user-facing UX
