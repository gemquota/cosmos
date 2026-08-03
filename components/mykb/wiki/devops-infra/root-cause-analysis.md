---
type: "concept"
title: "Root Cause Analysis"
description: "Systematically finding the underlying causes of incidents, beyond the immediate trigger"
tags: ["rca", "incidents", "analysis", "reliability"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Root Cause Analysis

## Summary
Root cause analysis digs past the immediate trigger to the contributing causes that allowed an incident to happen. The trigger is the final push — the condition that existed before it, the missing guardrail, the deferred fix — is where durable improvement lives. The output is owned action items, not blame.

## Details
- Methods: five whys chains from symptom to condition (asking why until reaching a fixable cause); fishbone diagrams group causes into categories (people, process, tooling, environment); timeline analysis reconstructs what happened in order, separating evidence from assumptions.
- Distinguish trigger from root causes: the trigger answers what happened at the moment (a pod restarted); root causes answer why it could happen (the liveness threshold was too tight, the rollout lacked a gate, the fix was deferred twice). Fixing only the trigger guarantees recurrence.
- Every root cause needs a concrete, owned action item: a finding without an owner, a ticket, and a verification step is a discussion, not a fix; the action should be specific enough that an auditor could check it.
- Failure modes: analysis driven by blame rather than systems, producing defensive silence instead of honesty; the five-whys stopping at a human error, ignoring the conditions that made the error possible; findings that are unactionable (more vigilance); RCA performed without evidence, relying on memory and conjecture; action items that are never tracked to completion.
- Tradeoffs: the root-cause lens assumes causes can be found and fixed; complex incidents are often emergent, with no single root cause — a systems view (multiple contributing factors, feedback loops) fits better there; the practical approach is to look for the leverage points the team can actually change and to pair every finding with an experiment or a guardrail.
- Operational notes: run RCA with the incident timeline and metrics in hand, review action items at a fixed cadence, and treat recurrence as evidence the analysis stopped too early.
- RSIS3 relevance: RSIS3's own loop failures deserve the same discipline — the L2 improvement loop should learn from incident-like anomalies by finding fixable conditions, not just patching the trigger.

## Related
- [[wiki/devops-infra/incident-response|Incident Response]] — RCA is the follow-up phase
- [[wiki/devops-infra/distributed-tracing|Distributed Tracing]] — evidence for tracing failure paths
- [[wiki/devops-infra/postmortem-culture|Postmortem Culture]] — where RCA findings live
- [[wiki/devops-infra/observability|Observability]] — data that makes RCA possible
