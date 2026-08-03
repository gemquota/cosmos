---
type: "concept"
title: "Permission Model"
description: "The rules deciding which agent actions are allowed"
tags: ["permissions", "authorization", "safety", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# Permission Model

## Summary

A permission model defines what an agent may do — which tools, which scopes, which resources — and who grants it. It is the agent analog of IAM: least privilege, explicit grants, and audit, applied to model-driven actions.

## Details
- Mechanism: the model binds agent identity to capabilities: allowed tools with parameter constraints, allowed targets (repos, wikis, APIs), action classes (read-only vs mutating), and rate/cost limits; enforcement happens at the tool boundary (the model cannot call what the runtime denies), not in the prompt; grants are explicit, revocable, and logged.
- Concrete example: a wiki agent has read/write on the notes directory but read-only on the config; a deployment agent requires a separate grant for production credentials, granted per session; an analysis agent can call search APIs but not external send endpoints. The failure pattern: broad grants ("everything") that make the permission model decorative.
- Failure modes: prompt-level "permissions" that the model can be talked out of (enforce at runtime); grants that outlive sessions (expiry and revocation); tool access without parameter constraints (a write tool that can target anywhere); and permission sprawl accumulating as new tools ship.
- Operational tradeoffs: a strict permission model costs configuration and review; it pays in safety, auditability, and the ability to grant autonomy safely. The standard is deny-by-default, tool-boundary enforcement, scoped grants with expiry, and a permission audit trail.
- RSIS3/mykb relevance: the wiki's agents would run under a deny-by-default permission model enforced at the tool boundary, with every grant versioned in the environment config.
- Parameter scoping: constrain tool arguments (paths, endpoints, sizes) in the grant, not just the tool name; an unrestricted write tool grant is a full-access grant in disguise.
- Session scoping: tie grants to session duration and purpose; a permission granted for one task should not linger for the next.

## Related
- [[wiki/agent-systems/risk-bounded-agents|Risk-Bounded Agents]] — permissions as risk bounds
- [[wiki/llm-agents/approval-gates|Approval Gates]] — human checkpoints on permission boundaries
- [[wiki/llm-agents/policy-enforcement|Policy Enforcement]] — runtime enforcement of the model
- [[wiki/agent-systems/agent-sandboxing|Agent Sandboxing]] — enforcement at the environment level
- [[wiki/agent-systems/tool-use-patterns|Tool Use Patterns]] — tools as permissioned actions
