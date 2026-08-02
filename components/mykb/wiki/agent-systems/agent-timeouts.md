---
type: "concept"
title: "Agent Timeouts"
description: "Maximum execution durations that force agents to stop and report"
tags: ["timeouts", "agents", "control", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Agent Timeouts

## Summary
Maximum execution durations that force agents to stop and report

## Details
- Wall-clock and step-count timeouts bound runaway loops.
- Timeout behavior: checkpoint, escalate, or abort.
- Timeouts integrate with budget-and-quota-control.
- Prevent cost and resource exhaustion.

## Related
- [[wiki/agent-systems/agent-cancellation|Agent Cancellation]] — stop mechanism
- [[wiki/agent-systems/budget-and-quota-control|Budget and Quota Control]] — cost bounds
- [[wiki/agent-systems/checkpointing-agent-runs|Checkpointing Agent Runs]] — state capture
- [[wiki/agent-systems/escalation-handling|Escalation Handling]] — post-timeout path
- [[wiki/agent-systems/circuit-breakers-for-agents|Circuit Breakers for Agents]] — failure protection
