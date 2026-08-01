---
type: "concept"
title: "Prompt Chaining"
description: "Decomposing a complex task into a sequence of linked prompts where each stage's output feeds the next stage's input"
tags: ["prompt-engineering", "chaining", "agents", "workflows"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://www.promptingguide.ai/techniques/prompt_chaining"]
---

# Prompt Chaining

## Summary
Prompt chaining splits one hard task into several smaller, verifiable prompt calls, passing each output forward as the next input. It trades a single large context for staged, inspectable steps, which improves reliability, debuggability, and token efficiency when intermediate states matter.

## Details
- Classic pattern: extract -> transform -> validate -> format, with each stage having its own prompt, schema, and error handling.
- Because each link is a separate call, failures are localized: a bad parse in stage 2 does not corrupt the whole output.
- Chain design should align with the human review loop — checkpoints between stages let a human or a validator gate what flows onward.
- Trade-off: latency and cost grow with chain length; short chains (2-5 links) are the sweet spot for most pipelines.
- Chaining is the structural ancestor of agent loops: an agent is a chain whose links are chosen by the model rather than hardcoded.
- RSIS3 relevance: RRP-style refinement cycles are naturally expressed as chains (ideate -> critique -> refine -> test), matching the prompt engine's staged protocol.

## Related
- [[wiki/prompt-engineering/multi-step-reasoning|Multi-Step Reasoning]] — Chaining is the engineering expression of multi-step reasoning
- [[wiki/prompt-engineering/prompt-compression|Prompt Compression]] — Keeps intermediate state small between chain links
- [[wiki/prompt-engineering/context-engineering|Context Engineering]] — Chains manage what context each stage sees
- [[wiki/prompt-engineering/tool-calling|Tool Calling]] — Chains often invoke tools at intermediate stages
- [[wiki/prompt-engineering/structured-output|Structured Output]] — Strict schemas make chain hand-offs machine-checkable
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — Each chain stage can log to the wiki for replay
- [[wiki/concepts/mykb-implementation-report|mykb Implementation Report: 6-Phase Buildout — Actual State, Architecture, and Results]] — Pipeline-style prompt stages are logged in the mykb buildout
