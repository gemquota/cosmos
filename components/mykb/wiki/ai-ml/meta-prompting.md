---
type: "concept"
title: "Meta-Prompting"
description: "Using prompts that guide the model to act as a coordinator that manages sub-prompts"
tags: ["meta-prompting", "prompting", "decomposition", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2401.12954", "https://arxiv.org/abs/2307.09488"]
---

# Meta-Prompting

## Summary
Meta-prompting instructs the model to act as a meta-agent that decomposes a task and dispatches focused sub-prompts to itself. It matters because complex tasks benefit from structured decomposition with explicit roles. It is a lightweight stepping stone to full agent frameworks.

## Details
- **Mechanism** — the model plays coordinator, expert, and verifier roles through structured prompt templates.
- **Benefits** — better structure on multi-part tasks, easier debugging, and reusable scaffolding.
- **Worked example** — a research question is split into sub-prompts for definitions, evidence, and counterarguments, then synthesized.
- **Limits** — token overhead and shallow role separation compared to true multi-agent systems.
- **mykb relevance** — RSIS3 can use meta-prompting to structure knowledge synthesis from multiple angles.
- **Worked example** — a research question is split into sub-prompts for definitions, evidence, and counterarguments, then synthesized.
- **Cost control** — meta-prompting multiplies calls; budget per sub-task and cache shared context.
- **Limits** — token overhead and shallow role separation compared to true multi-agent systems; use it when decomposition alone suffices.

## Related
- [[wiki/agent-systems/multi-agent-systems|Multi-Agent Systems]] — full multi-agent pattern
- [[wiki/llm-agents/self-reflection-agents|Self-Reflection Agents]] — self-review
- [[wiki/agent-systems/agent-planning-systems|Agent Planning Systems]] — planning
- [[wiki/ai-ml/structured-output-generation|Structured Output Generation]] — structured outputs
- [[wiki/prompt-engineering/prompt-templates|Prompt Templates]] — related concept in this cluster
- [[wiki/prompt-engineering/self-ask-technique|Self-Ask Technique]] — related concept in this cluster
- [[wiki/syntheses/knowledge-synthesis|Knowledge Synthesis]] — the synthesis pipeline
- [[wiki/llm-agents/tree-of-thought|Tree of Thought]] — reasoning search
