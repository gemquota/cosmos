---
type: "concept"
title: "Instruction Hierarchy"
description: "Ordering instruction sources by authority"
tags: ["instruction-hierarchy", "priorities", "llm"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Instruction Hierarchy

## Summary
An instruction hierarchy orders instruction sources by authority so that when instructions conflict, the higher-ranked source wins: platform rules outrank system prompts, system prompts outrank user prompts, and user prompts outrank untrusted content like retrieved documents. Hierarchies are the main defense against prompt injection and instruction confusion in deployed agents.

## Details
- **Standard ordering** — developer and platform rules sit at the top, then system prompts, then user turns, then tool outputs and retrieved text; each layer can only override the layers below it.
- **Why it matters** — models are trained to follow user instructions, so without an explicit hierarchy they will happily obey instructions smuggled into web pages, emails, or tool output.
- **Enforcement mechanisms** — hierarchy is baked in via system-prompt phrasing, refusal behavior on conflict, and structured reasoning that identifies which source an instruction came from.
- **Imperfect robustness** — current models follow hierarchies most of the time but can still be confused by indirect injection, role-play, or instructions embedded in data; hierarchy reduces but does not eliminate risk.
- **Evaluation** — hierarchy adherence is measured with conflict suites that mix sources and test whether the model consistently prefers the higher-ranked instruction.
- **Relationship to priorities** — priority weights generalize the idea: instead of a strict ordering, competing instructions get numeric weights; hierarchies are the lexicographic special case.
- **mykb relevance** — worker and sub-agent instructions should state their source rank explicitly so delegated agents resolve conflicts the same way the orchestrator would.

- **Defense in depth** — hierarchy is one layer among several: input filtering, tool sandboxing, and output monitoring all backstop a model that loses the ranking under pressure.

## Related
- [[wiki/agent-systems/priority-weights|Priority Weights]] — the numeric generalization
- [[wiki/ai-ml/prompt-injection|Prompt Injection]] — the threat hierarchy defends against
- [[wiki/concepts/context-robustness|Context Robustness]] — the desired property
- [[wiki/agent-systems/obedient-ai|Obedient AI]] — following instructions correctly
- [[wiki/agent-systems/scaffold-loops|Scaffold Loops]] — where hierarchies are implemented
- [[wiki/agent-systems/agent-sandboxing|Agent Sandboxing]] — containing injection fallout
