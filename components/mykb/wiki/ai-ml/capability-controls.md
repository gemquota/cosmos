---
type: "concept"
title: "Capability Controls"
description: "Mechanisms that limit what a model or agent can do regardless of its intent"
tags: ["safety", "control", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Capability Controls

## Summary
Mechanisms that limit what a model or agent can do regardless of its intent

## Details
- Controls include sandboxes, permission scopes, tool allowlists, and kill switches.
- They reduce blast radius of misalignment or error.
- Controls must be tested against bypass attempts.
- A practical complement to value alignment.

## Related
- [[wiki/agent-systems/agent-sandboxing-variants|Agent Sandboxing Variants]] — containment approaches
- [[wiki/llm-agents/permissioning-and-approvals|Permissioning and Approvals]] — authorization layer
- [[wiki/agent-systems/tool-selection-policies|Tool Selection Policies]] — allowed tool surface
- [[wiki/agent-systems/circuit-breakers-for-agents|Circuit Breakers for Agents]] — automated stops
- [[wiki/agent-systems/agent-runtime-security|Agent Runtime Security]] — enforcement layer
