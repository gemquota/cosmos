---
type: "concept"
title: "Circuit Breakers for Agents"
description: "Automatically stopping agent activity when failures cross a threshold"
tags: ["agents", "circuit-breaker", "reliability", "failure"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://github.com/langchain-ai/langgraph", "https://arxiv.org/abs/2307.09288"]
---

# Circuit Breakers for Agents

## Summary
A circuit breaker halts agent work when failure rates or error patterns cross a threshold, protecting the system from cascading damage. It is a tripwire between "retry a bit" and "keep hammering a broken dependency." Opening the circuit forces the agent to escalate, pause, or degrade gracefully.

## Details
- **States** — closed (normal), open (trip, no calls), half-open (probe with limited traffic); transitions depend on failure counts or latency.
- **Trip conditions** — consecutive 5xx errors, timeout ratios, budget overruns, or detection of a pathological loop.
- **Agent-specific uses** — stop a coding agent that keeps generating failing patches, or halt a research agent whose sources all return errors.
- **Worked example** — after three consecutive failed tool calls, the breaker opens; the agent records the failures and escalates instead of looping.
- **Relationship to retries** — retries handle transient blips; the breaker handles persistent failure; both need clear thresholds.
- **mykb relevance** — the circuit-breaker concept already exists in mykb's api-protocols and maps directly to agent run control.

- **Half-open probing** — after a cooldown the breaker allows a limited probe; success closes it, failure reopens it, preventing flapping on a still-broken dependency.
- **Breaker state as telemetry** — breaker open/close events are logged and surfaced, because a repeatedly tripping breaker is a signal about the dependency, not just the agent.
- **Failure vs fault distinction** — the breaker trips on persistent failure patterns, not single faults; distinguishing transient noise from systemic breakage is what the thresholds encode.
- **Human visibility** — an open breaker surfaces in the dashboard with the trip reason, so an operator can decide to intervene, repair the dependency, or force-reset with care.
## Related
- [[wiki/agent-systems/agent-timeouts|Agent Timeouts]] — timeouts as trip conditions
- [[wiki/agent-systems/degraded-mode-operations|Degraded Mode Operations]] — behavior while open
- [[wiki/api-protocols/circuit-breaker|Circuit Breaker]] — existing circuit-breaker concept
- [[wiki/agent-systems/partial-failure-handling|Partial Failure Handling]] — surviving partial failures
- [[wiki/agent-systems/budget-and-quota-control|Budget and Quota Control]] — cost-based tripwires
- [[wiki/agent-systems/agent-supervision|Agent Supervision]] — monitoring breaker state
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the loop agents execute
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
