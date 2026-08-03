---
type: "concept"
title: "Loop Engineering"
description: "Designing the system that prompts an agent on a schedule — automations, worktrees, skills, connectors, sub-agents, and state"
tags: ["loop-engineering", "automations", "subagents", "skills", "state", "stopping-conditions"]
timestamp: "2026-08-03T12:00:00Z"
status: "growing"
source: ["https://addyosmani.com/blog/loop-engineering/", "https://firecrawl.dev/blog/loop-engineering"]
---

# Loop Engineering

## Summary
Loop engineering replaces the human as the person prompting an agent: you design a small system that finds work, dispatches it, checks it, records what is done, and decides the next step — poking the agent on your behalf. Peter Steinberger's June 2026 post ("You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents") and Boris Cherny's "my job is to write loops" made the practice mainstream. The core cycle remains act → observe → reason → repeat; everything else is scaffolding around it.

## Details
- **Six primitives** — automations (scheduled discovery and triage), worktrees (parallel isolation), skills (project knowledge written once in SKILL.md), plugins and connectors (MCP access to real tools), sub-agents (maker/checker split), and state (a markdown file or board outside the conversation). Both Codex and Claude Code now ship all six.
- **Sub-agents** — the most useful structural split is separating the writer from the checker: the model that wrote the code grades its own homework too generously, so a second agent with different instructions verifies.
- **Stopping is the hard part** — a loop that cannot mechanically distinguish done from stuck keeps spending tokens; every loop needs a hard iteration cap, a no-progress/diff check, and a token or dollar spend cap. Without them it's "an open invoice."
- **Open vs closed loops** — open loops give the agent a goal plus guardrails and let it route itself (great for prototyping, brutal on budgets); closed loops predefine the path, the per-step checks, and the halt rules (predictable cost, the production default).
- **Task fit** — a task wants a loop if it is repetitive (design cost pays back), reviewable ("done" is expressible as a runnable check), and valuable enough to clear the token floor.
- **Risk: comprehension debt** — the faster a loop ships code you didn't write, the wider the gap between repo and understanding; verification stays on the human, and "done" is a claim, not a proof.
- **Risk: cognitive surrender** — the comfortable posture is dangerous; the same loop accelerates someone who understands the work and hides someone who avoids understanding it. The loop doesn't know the difference.
- **Cost reality** — Uber capped engineers at $1,500/person/tool/month after burning its annual AI budget in four months; token cost moved from writing code to running the thing that writes it.

## Related
- [[wiki/llm-agents/agentic-loops|Agentic Loops]] — the underlying loop design
- [[wiki/llm-agents/loop-specification|Loop Specification]] — the formal artifact
- [[wiki/llm-agents/graph-engineering|Graph Engineering]] — the layer above
- [[wiki/llm-agents/prompt-loop-graph-layers|Prompt vs Loop vs Graph]] — the stack
- [[wiki/agent-systems/sub-agent-delegation|Sub-Agent Delegation]] — maker/checker split
- [[wiki/llm-agents/approval-gates|Approval Gates]] — human checkpoints
- [[wiki/syntheses/loop-graph-engineering-wave-2026-08|Loop/Graph Engineering Wave]] — synthesis

## Sources
- Addy Osmani, "Loop Engineering", 2026-06-07 — https://addyosmani.com/blog/loop-engineering/
- Firecrawl, "Loop Engineering: Should You Stop Prompting Agents and Start Designing Loops", 2026-06-11 — https://firecrawl.dev/blog/loop-engineering
