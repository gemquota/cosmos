---
type: "concept"
title: "Multi-Agent Research Systems"
description: "Anthropic's production multi-agent research system: parallel subagents, token economics, and evaluation practice"
tags: ["multi-agent", "research", "subagents", "evaluation", "llm-as-judge"]
timestamp: "2026-08-03T12:00:00Z"
status: "growing"
source: ["https://www.anthropic.com/engineering/built-multi-agent-research-system"]
---

# Multi-Agent Research Systems

## Summary
Anthropic's Claude Research feature is a production multi-agent system: a lead agent plans a research process and spawns parallel subagents that search simultaneously. The writeup explains why the architecture works, what it costs, and how to evaluate systems whose steps are non-deterministic. It is the reference counterpoint to Cognition's "Don't Build Multi-Agents" — both are right, for different task shapes.

## Details
- **Why multi-agent works for research** — research is open-ended and path-dependent; parallel subagents compress the search space by exploring different aspects with their own context windows, then returning condensed summaries to the lead.
- **Measured gains** — a multi-agent system (Opus 4 lead, Sonnet 4 subagents) beat single-agent Opus 4 by 90.2% on an internal research eval; token usage alone explained 80% of BrowseComp performance variance, with tool-call count and model choice the other factors.
- **Token economics** — agents use ~4× more tokens than chat; multi-agent systems ~15× more; viability requires tasks valuable enough to pay for the increase, so breadth-first research is the sweet spot.
- **Parallelism** — the lead spins up 3-5 subagents in parallel and subagents use 3+ tools in parallel, cutting research time by up to 90% on complex queries.
- **Prompting heuristics** — encode how skilled humans research (decompose hard questions, evaluate source quality, adjust approach, balance depth vs breadth) as heuristics with guardrails rather than rigid rules.
- **Evaluation** — start with ~20 real-usage queries immediately; LLM-as-judge scoring against a rubric (factual accuracy, citation accuracy, completeness, source quality, tool efficiency) scales to hundreds of outputs; human testing catches what automation misses.
- **Appendix lessons** — end-state evaluation for state-mutating agents; long-horizon context management via summarizing completed phases into external memory; subagents write artifacts to filesystem and pass lightweight references back to avoid the "game of telephone."
- **When not to use it** — domains requiring all agents to share context, many inter-agent dependencies, or mostly-sequential coding work are poor fits today.

## Related
- [[wiki/llm-agents/multi-agent-systems-guide|How and When to Build Multi-Agent Systems]] — the reconciliation
- [[wiki/llm-agents/dont-build-multi-agents|Don't Build Multi-Agents]] — the counterposition
- [[wiki/llm-agents/graph-engineering|Graph Engineering]] — org/work graph structure
- [[wiki/prompt-engineering/context-engineering|Context Engineering]] — long-horizon management
- [[wiki/agent-systems/sub-agent-delegation|Sub-Agent Delegation]] — delegation mechanics
- [[wiki/agent-systems/multi-agent-orchestration|Multi-Agent Orchestration]] — orchestrator pattern
- [[wiki/syntheses/loop-graph-engineering-wave-2026-08|Loop/Graph Engineering Wave]] — synthesis

## Sources
- Anthropic, "How we built our multi-agent research system", 2025-06-13 — https://www.anthropic.com/engineering/built-multi-agent-research-system
