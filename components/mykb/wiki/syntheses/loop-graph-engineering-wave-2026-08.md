---
type: synthesis
title: "Loop & Graph Engineering Wave — 14-Source Ingest"
description: "Synthesis of the 2025-26 progression from prompt engineering to context, harness, loop, and graph engineering across Anthropic, Cognition, LangChain, Willison, Osmani, and the arXiv loop-specification paper"
tags: [synthesis, loop-engineering, graph-engineering, context-engineering, multi-agent, ingest, 2026-08]
timestamp: "2026-08-03T12:30:00Z"
status: stable
source: []
---
# Loop & Graph Engineering Wave — 14-Source Ingest

## Context
The AI-engineering vocabulary moved up a layer roughly every year: prompt (2023-24), context (2024), harness (2025), loop (early 2026), graph (mid-2026). This ingest consolidates 14 sources — three Anthropic engineering posts, Cognition's counterposition, LangChain's reconciliation and LangGraph docs, Simon Willison's and Addy Osmani's loop essays, Firecrawl's practitioner guide, explainx/TrueFoundry/AI Builder Club on graph engineering, the MarkTechPost layer comparison, and the arXiv loop-specification paper.

## The stack, one layer at a time
- **Prompt engineering** — writing the instruction for a single call; the defining assumption is a human present at every iteration, which breaks under volume, multi-step tasks, and unattended grading.
- **Context engineering** — deciding what token configuration enters the window at all; context is finite with diminishing marginal returns (attention budget, context rot), so the job is curating the smallest set of high-signal tokens each step.
- **Harness engineering** — the environment one agent runs inside: files, tools, memory, feedback.
- **Loop engineering** — designing the system that prompts the agent on a schedule; primitives are automations, worktrees, skills, plugins/connectors, sub-agents, and external state, with the stop condition the hard part.
- **Graph engineering** — designing the multi-agent organization as a programmable topology; the org graph (who owns what, stable) and the work graph (what right now, ephemeral) run simultaneously.

## Convergent findings
- **The layers compose; they do not replace.** A loop is a prompt repeated with scaffolding; a graph is built from loops. Prompt engineering stayed the primary lever even inside Anthropic's multi-agent research system — coordination failures were fixed by prompting, not topology.
- **Verification is the bottleneck everywhere.** The maker/checker split, the five-level verification ladder in the arXiv paper, "done is a claim not a proof," and evaluator-optimizer all name the same failure: the model that wrote the work grades it too generously.
- **Context is the scarce resource.** Cognition's two principles (share full traces; actions carry implicit decisions) and Anthropic's compaction, structured note-taking, and sub-agent context isolation are the same lesson from both sides of the multi-agent debate.
- **Read-systems parallelize; write-systems conflict.** Multi-agent research (mostly read) gained +90.2% and is the standard success case; multi-agent coding (mostly write) fragments context and is the standard failure case.
- **Cost must be engineered.** ~15× tokens for multi-agent research, Uber's $1,500/person/tool caps, and every loop needing an iteration cap, no-progress check, and spend cap: token spend alone explained 80% of performance variance.
- **The operator is the wildcard.** Comprehension debt and cognitive surrender make identical loops produce opposite outcomes depending on the engineer's judgment.

## Practice implications for mykb / RSIS3
- Treat RSIS3's loop layers as loop specifications with explicit triggers, verification steps, and terminal states; audit loops for named stop conditions before unattended runs.
- mykb retrieval is context engineering: the right knowledge in the right order beats a bigger model; keep compaction and note-taking patterns in mind for long-horizon passes.
- The dual wiki (knowledge vs meta) mirrors the org-graph/work-graph distinction: durable roles with accumulated context vs ephemeral task structure.

## Related
- [[wiki/llm-agents/prompt-loop-graph-layers|Prompt vs Loop vs Graph]]
- [[wiki/llm-agents/loop-engineering|Loop Engineering]]
- [[wiki/llm-agents/loop-specification|Loop Specification]]
- [[wiki/llm-agents/graph-engineering|Graph Engineering]]
- [[wiki/llm-agents/agentic-loops|Agentic Loops]]
- [[wiki/prompt-engineering/context-engineering|Context Engineering]]
- [[wiki/llm-agents/building-effective-agents|Building Effective Agents]]
- [[wiki/llm-agents/multi-agent-research-systems|Multi-Agent Research Systems]]
- [[wiki/llm-agents/dont-build-multi-agents|Don't Build Multi-Agents]]
- [[wiki/llm-agents/multi-agent-systems-guide|How and When to Build Multi-Agent Systems]]
- [[wiki/llm-agents/langgraph-graph-api|LangGraph Graph API]]
