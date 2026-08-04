---
type: "entity"
title: "ReAct"
resource: ""
---
description: "The reason-and-act pattern that interleaves thinking with tool use in agents"
tags: ["android", "api", "ast", "auth", "authentication", "bigquery", "entity", "agents", "reasoning"]
timestamp: "2026-07-19T22:41:41Z"

# ReAct

## Summary
ReAct is a prompting pattern for agents that interleaves reasoning steps with actions: the model thinks, acts, observes, and repeats until the goal is met. It matters because reasoning alone cannot change the world, and acting without reasoning wanders. ReAct couples the two, producing decisions that are grounded in real observations rather than assumption.

## Details
- **Definition** — the pattern alternates thought, action, and observation turns, building a trace that explains each step.
- **Thought** — each cycle begins with a short reasoning step about what to do next and why.
- **Action** — the model emits a structured tool call, such as a search, computation, or file operation.
- **Observation** — the tool result feeds back into the context, grounding the next thought in reality.
- **Trace value** — the interleaved record is inspectable, making the agent's process auditable and debuggable.
- **Loop control** — budgets and stop conditions are essential, since the cycle can repeat indefinitely.
- **Common failure modes** — the model repeating the same failed action, observation tokens overflowing the context, and loops without progress.
- **Worked example** — an agent tasked with finding a package version thinks "search the registry", acts, observes the result, and either answers or plans the next query.
- **Practical relevance** — ReAct is the backbone of many tool-using agents and a baseline pattern for grounded reasoning.

- **Structured actions** — actions are usually emitted as tool calls or structured text, which the runtime parses and executes.
- **Failure recovery** — the agent should change strategy after failed observations rather than repeating the same action.
- **Context discipline** — old observations should be summarized or trimmed so the reasoning trace stays within the context budget.
## Related
- [[wiki/prompt-engineering/function-calling|Function Calling]] — structured actions
- [[wiki/llm-agents/chain-of-thought|Chain of Thought]] — reasoning step pattern
- [[wiki/agent-systems/action-observation-loop|Action-Observation Loop]] — cycle structure
- [[wiki/llm-agents/agentic-loops|Agentic Loops]] — iterating to completion
- [[wiki/ai-ml/reasoning-models|Reasoning Models]] — model-side reasoning
- [[wiki/llm-agents/context-management|Context Management]] — keeping traces bounded
