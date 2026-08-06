---
type: "concept"
title: "Capability Controls"
description: "Mechanisms that limit what a model or agent can do regardless of its intent"
tags: ["safety", "control", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Capability Controls

## Summary
Capability controls are mechanisms that limit what a model or agent can do regardless of its intent — sandboxes, permission scopes, tool allowlists, rate limits, and kill switches. They reduce the blast radius of misalignment or error and work as a complement to value alignment rather than a replacement for it.

## Details
- **Layers** — controls sit at the environment (sandbox, network egress), the interface (tool allowlist, permission scopes), and the execution level (budgets, timeouts, kill switches).
- **Intent-independence** — the key property is that controls bind even a misaligned or adversarial model, because enforcement lives outside the model's reasoning.
- **Blast-radius reduction** — a leaked credential is less harmful when the agent runs in a read-only scope; a runaway loop is contained by budget and timeout limits.
- **Bypass resistance** — controls must be tested against bypass attempts: prompt injection that requests forbidden tools, tool calls that chain to escalate permissions, and path traversal out of the sandbox.
- **Enforcement patterns** — enforcement can be an allowlist (deny by default), a deny-list, human-in-the-loop approval gates for high-impact actions, and circuit breakers that stop execution on anomaly signals.
- **Trade-offs** — tighter controls add friction, reduce autonomy, and can push agents to work around them; the design goal is the least restriction that keeps risk acceptable.
- **Verification** — red-team the control surface and log every denial so the policy can be audited and tightened from evidence.

- **Relationship to alignment** — alignment tries to make a model want the right things; capability controls make it unable to do the wrong things; the two compose because each covers failure modes the other misses, and controls buy time while alignment work continues.
## Related
- [[wiki/agent-systems/agent-sandboxing|Agent Sandboxing]] — containment approaches
- [[wiki/llm-agents/permissioning-and-approvals|Permissioning and Approvals]] — authorization layer
- [[wiki/agent-systems/tool-selection-policies|Tool Selection Policies]] — allowed tool surface
- [[wiki/agent-systems/circuit-breakers-for-agents|Circuit Breakers for Agents]] — automated stops
- [[wiki/agent-systems/agent-runtime-security|Agent Runtime Security]] — enforcement layer
- [[wiki/agent-systems/agent-sandboxing-variants|Agent Sandboxing Variants]] — containment menu
