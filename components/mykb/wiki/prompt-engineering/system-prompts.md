---
type: "concept"
title: "System Prompts"
description: "The persistent instruction block that defines an LLM's role, behaviour, and operating constraints for a session"
tags: ["prompt-engineering", "system-prompts", "agents", "llm", "rsis3"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://platform.openai.com/docs/guides/prompt-engineering", "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts"]
---

# System Prompts

## Summary
A system prompt is the persistent instruction block prepended to a session that fixes the model's role, tone, tools, and constraints before any user turn. It is the highest-leverage part of a prompt system because it shapes every downstream request, and it is where most of RSIS3-style agent scaffolding lives.

## Details
- OpenAI's prompt-engineering guide treats system messages as the place to set personas, output format, and guardrail-style do/don't lists.
- Anthropic recommends system prompts for role definition, task context, tone, and interaction rules; longer system prompts should put the most important instructions first.
- Good system prompts are specific, include examples of desired behaviour, and state negative constraints (what not to do) explicitly.
- In agent systems the system prompt typically also enumerates tool schemas, output contracts, and the agent's memory/loop protocol, so it becomes a shared contract between the controller and the model.
- RSIS3 relevance: each pulse, session, or self-improvement loop can carry a distinct system prompt, making the prompt a versionable artifact that mykb can store, diff, and regress-test.
- Anti-pattern: cramming the whole knowledge base into the system prompt blows the context window and degrades instruction-following; prefer retrieval into a working context.

## Related
- [[wiki/prompt-engineering/few-shot-prompting|Few-Shot Prompting]] — System prompts often embed few-shot exemplars to pin behaviour
- [[wiki/prompt-engineering/in-context-learning|In-Context Learning]] — The mechanism by which system prompts steer behaviour without weight updates
- [[wiki/prompt-engineering/message-format|Message Format]] — System prompts occupy the first message slot in the conversation protocol
- [[wiki/prompt-engineering/refusal-behaviour|Refusal Behaviour]] — System prompts are a first line of refusal and safety steering
- [[wiki/ai-ml/guardrails|Guardrails]] — Runtime validation layered on top of system-prompt rules
- [[wiki/concepts/mykb-analysis|mykb: Personal LLM Wiki — Analysis & Enrichment Theory]] — mykb can index and compare system prompts across sessions
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — Prompt artifacts flow through the capture-process-connect-synthesize loop
