---
type: "concept"
title: "Policy Enforcement"
description: "Runtime mechanisms that check agent actions against policy"
tags: ["policy-enforcement", "policies", "safety", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# Policy Enforcement

## Summary

Policy enforcement makes agent constraints real: rules live in code that checks every action before execution, not in prompts that a model may ignore. It is the difference between asking an agent to behave and guaranteeing it.

## Details
- Mechanism: policies are executable predicates — allow/deny rules over actions (tool, target, payload, context) evaluated at the enforcement point (before tool calls, before writes, before external sends); policy engines (OPA-style, custom checks, permission models) render verdicts (allow, deny, require-approval); verdicts are logged; hard constraints (never send to this endpoint) and soft rules (flag unusual patterns) coexist.
- Concrete example: a policy denies any agent write to the wiki's config directory regardless of prompt; a policy requires approval for posts to the external channel but auto-allows edits to drafts; a cost policy caps daily model spend and pauses the agent at the limit.
- Failure modes: policy gaps — actions not covered by any rule defaulting to allow (deny-by-default closes this); prompt-policy conflict where the model is instructed to bypass (enforcement must be uninfluenced by prompt); enforcement at the wrong layer (checking the plan, not the executed action); and policies that block legitimate work without an escalation path.
- Operational tradeoffs: policy enforcement costs design and maintenance; it buys the safety properties that make autonomy deployable. The discipline is deny-by-default, evaluate at execution time, log every verdict, and test policies against both benign and adversarial scenarios.
- RSIS3/mykb relevance: the wiki's policy layer executes before every agent action, so loop autonomy stays bounded by the same rules regardless of prompt or model version.
- Policy testing: unit-test policies against a corpus of allowed and denied actions, including adversarial prompts that try to bypass them.
- Verdict telemetry: log allow/deny/approve verdicts with reasons; a policy that never denies anything is either perfectly scoped or not enforcing.

## Related
- [[wiki/agent-systems/risk-bounded-agents|Risk-Bounded Agents]] — the bounds being enforced
- [[wiki/llm-agents/permission-model|Permission Model]] — the policy source
- [[wiki/llm-agents/approval-gates|Approval Gates]] — enforcement via human checkpoints
- [[wiki/agent-systems/agent-sandboxing|Agent Sandboxing]] — environment-level enforcement
- [[wiki/llm-agents/success-criteria|Success Criteria]] — policy as success constraints
