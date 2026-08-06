---
type: "concept"
title: "Bounded Agents"
description: "Agents designed with explicit limits on resources, impact, and authority"
tags: ["bounded", "agents", "limits", "safety"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Bounded_rationality", "https://en.wikipedia.org/wiki/Satisficing"]
---

# Bounded Agents

## Summary
A bounded agent operates under explicit caps: compute budgets, action horizons, scope restrictions, and approval requirements. Bounds are a safety feature — they make an agent's worst case small and its behavior predictable — and a realism feature, since real agents face resource limits anyway.

## Details
- **Kinds of bounds** — compute (test-time budget), horizon (plan depth), scope (allowed actions and files), and impact (world-change caps such as no writes outside a directory).
- **Why bounds help safety** — a bounded optimizer cannot optimize everything; mild optimization and satisficing are objective-level bounds, while tool and permission caps are mechanism-level bounds.
- **Design tension** — bounds that are too tight cripple capability; adaptive bounds (raise after verification) preserve both safety and usefulness.
- **Enforcement** — bounds are enforced outside the model: budgets in the runtime, scope in the sandbox, approvals at the gate; enforcement must not depend on the agent's goodwill.
- **Relation to bounded rationality** — the classical study of decision-making under resource limits informs agent design, where the resources are tokens, time, and authority rather than cognitive capacity.
- **RSIS3 relevance** — scope discipline (write only your files, no git, no shared-dir edits) is a bound on the acquisition workers, and loop budgets bound runaway recursion.
- **Failure modes** — hard caps can strand a run mid-task; the mitigation is graceful degradation: finalize, checkpoint, and escalate rather than halt abruptly.

- **Verification loop** — adaptive bounds are raised only after verified performance: telemetry shows the agent stayed within scope and quality held, then the cap moves; verification failure lowers it again.
- **Worst-case design** — bounds are specified for the worst case, not the average case: a runaway loop must hit a hard stop even if normal runs never approach the cap.
## Related
- [[wiki/agent-systems/satisficing-agents|Satisficing Agents]] — stop-when-good-enough bound
- [[wiki/concepts/mild-optimization|Mild Optimization]] — objective-level bound
- [[wiki/concepts/bounded-rationality|Bounded Rationality]] — cognitive limits
- [[wiki/agent-systems/approval-based-agents|Approval-Based Agents]] — authority bound
- [[wiki/agent-systems/test-time-compute|Test-Time Compute]] — compute bound
- [[wiki/agent-systems/risk-bounded-agents|Risk-Bounded Agents]] — risk budgets
- [[wiki/agent-systems/budget-and-quota-control|Budget and Quota Control]] — resource caps
