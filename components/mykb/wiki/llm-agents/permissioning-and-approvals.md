---
type: "concept"
title: "Permissioning and Approvals"
description: "Defining who or what may authorize each agent action"
tags: ["agents", "permissions", "approvals", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.anthropic.com/en/docs/build-with-claude/tool-use", "https://github.com/openai/swarm"]
---

# Permissioning and Approvals

## Summary
Permissioning assigns each action a sensitivity class and each actor (agent, sub-agent, human) a set of authorizations; approvals are the human review step for actions beyond an agent's authority. The two together bound what an agent can do on its own. Least privilege is the operating principle.

## Details
- **Permission classes** — read-only, internal writes, external side effects (email, publish), and destructive operations; each maps to a different authorization level.
- **Authorization sources** — policy files, identity scopes, and human approvers; the runtime consults them before each call.
- **Approval UX** — the agent proposes with context; the approver approves, rejects, or edits; the decision is logged for audit.
- **Worked example** — a publishing agent can draft internally, but the publish tool requires an approval with a rendered preview attached.
- **Policy as code** — declarative permission policies are testable and reviewable, unlike ad hoc checks.
- **mykb relevance** — the permission model and approval gates are existing mykb patterns used by RSIS3 sub-agents.

## Related
- [[wiki/llm-agents/permission-model|Permission Model]] — the permission model pattern
- [[wiki/llm-agents/approval-gates|Approval Gates]] — approval gate mechanics
- [[wiki/agent-systems/tool-selection-policies|Tool Selection Policies]] — permissions on tool use
- [[wiki/security/rbac|RBAC]] — role-based access control
- [[wiki/llm-agents/policy-enforcement|Policy Enforcement]] — enforcing agent policies
- [[wiki/llm-agents/user-confirmation-flows|User Confirmation Flows]] — related concept in this cluster
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
- [[wiki/concepts/triad-architecture|Triad Architecture]] — the RSIS3/mykb architecture it serves
