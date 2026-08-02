---
type: "concept"
title: "Degraded Mode Operations"
description: "Graceful reduction of service quality when resources or dependencies fail"
tags: ["degraded-mode", "reliability", "operations", "fallback"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Degraded Mode Operations

## Summary
Graceful reduction of service quality when resources or dependencies fail

## Details
- Define fallback behaviors: cached answers, simpler models, read-only.
- Explicit degraded modes beat uncontrolled failure.
- Communicated via error-messages-llm.
- Governed by model-fallback-chains.

## Related
- [[wiki/agent-systems/model-fallback-chains|Model Fallback Chains]] — model degradation
- [[wiki/agent-systems/partial-failure-handling|Partial Failure Handling]] — failure taxonomy
- [[wiki/api-protocols/load-shedding|Load Shedding]] — traffic reduction
- [[wiki/agent-systems/feature-flags-for-agents|Feature Flags for Agents]] — toggle control
- [[wiki/prompt-engineering/error-messages-llm|Error Messages for LLMs]] — user communication
