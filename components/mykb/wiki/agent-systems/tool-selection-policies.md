---
type: "concept"
title: "Tool Selection Policies"
description: "Rules deciding which tools an agent may use and when"
tags: ["tool-policies", "tools", "policies", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Tool Selection Policies

## Summary
Tool selection policies decide which tools an agent may use and when, shaping both capability and risk. They matter because every tool is a surface for cost, mistakes, and security incidents, and letting agents pick freely from everything is dangerous. A policy makes tool choice deliberate, bounded, and auditable. Tool policy is where agent capability becomes organizational risk management.

## Details
- **Definition** — a tool selection policy is the set of rules governing which tools an agent can access, under what conditions, and with what constraints.
- **Mechanisms** — allowlists, capability matching, risk tiers, and per-task grants determine what is available; permissioning-and-approvals enforce it.
- **Risk shaping** — policies limit the attack surface and cost by denying dangerous or expensive tools by default and granting them explicitly.
- **Schema quality** — selection quality depends on tool-schema-design: clear descriptions and parameters let agents and policies reason about fit.
- **Worked example** — a coding agent may read files and run tests freely, but write access to production requires an approval and a human-confirmed flag.
- **Failure modes** — overly broad defaults, stale allowlists, and policy bypass through composed tools are common failure modes.
- **Dynamic selection** — policies can adapt by task type, data sensitivity, or model trust level, tightening controls as risk rises.
- **Practical relevance** — tool policies are the interface between an agent's capability-controls and its runtime security posture.
- **Default deny** — starting closed and opening tools deliberately is safer than starting open.
- **Audit trail** — every tool grant and use should be logged for review.
- **Worked example** — a data agent can query read-only endpoints by default but needs an approved grant for write endpoints.
- **Failure example** — a policy that allows any file read lets a prompt-injection leak secrets from the filesystem.

## Related
- [[wiki/prompt-engineering/tool-schema-design|Tool Schema Design]] — the schema layer policies reason over
- [[wiki/llm-agents/permissioning-and-approvals|Permissioning and Approvals]] — enforcement of tool policy
- [[wiki/ai-ml/capability-controls|Capability Controls]] — the safety limit layer
- [[wiki/llm-agents/tool-use-function-calling|Tool Use and Function Calling]] — the mechanism policies gate
- [[wiki/agent-systems/agent-runtime-security|Agent Runtime Security]] — runtime enforcement of policy
