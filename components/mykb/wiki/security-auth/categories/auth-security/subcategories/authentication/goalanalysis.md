---
type: "entity"
title: "GoalAnalysis"
resource: ""
---
description: "Examining goals for clarity, feasibility, measurability, and conflicts before acting"
tags: ["entity", "android", "api", "ast", "auth", "authentication", "goals", "planning"]
timestamp: "2026-07-19T22:41:44Z"

# GoalAnalysis

## Summary
Goal analysis is the step of examining a goal before acting on it: checking that it is clear, measurable, feasible, and free of conflicts. It matters because agents and teams waste effort on goals that are ambiguous or internally contradictory, and the waste compounds when others build on those results. A few minutes of analysis up front prevents hours of misdirected execution.

## Details
- **Definition** — goal analysis evaluates a goal against criteria such as clarity, measurability, feasibility, and alignment with existing constraints.
- **Clarity** — a goal must specify what success looks like; vague phrasing produces arbitrary or drifting work that is hard to review.
- **Measurability** — attaching observable success criteria makes completion verifiable rather than subjective, for both humans and agents.
- **Feasibility** — resources, permissions, and time bounds must support the goal, or the plan should be revised before starting.
- **Conflict detection** — goals often collide, such as "fast" versus "safe"; analysis surfaces the trade-offs that need an explicit decision.
- **Decomposition readiness** — a well-analyzed goal is specific enough to decompose into subtasks with confidence and clear checks.
- **Escalation** — when analysis finds an infeasible goal, the right output is a revised plan or a request for scope change, not silent adjustment.
- **Common failure modes** — analysis paralysis, goals that are rewritten mid-execution, and hidden constraints discovered after work begins.
- **Worked example** — before implementing, an agent checks a goal against its permissions and deadline, finds the deadline infeasible, and escalates with a revised estimate.
- **Practical relevance** — goal analysis is the difference between efficient execution and confident execution in the wrong direction.

## Related
- [[wiki/agent-systems/goal-decomposition|Goal Decomposition]] — splitting analyzed goals
- [[wiki/agent-systems/goal-locking|Goal Locking]] — preventing goal drift
- [[wiki/agent-systems/goal-disclosure|Goal Disclosure]] — stating goals openly
- [[wiki/agent-systems/stated-vs-hidden-goals|Stated vs Hidden Goals]] — goal honesty
- [[wiki/agent-systems/accountability-ai|Accountability for AI]] — responsibility for outcomes
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — measuring goal success
