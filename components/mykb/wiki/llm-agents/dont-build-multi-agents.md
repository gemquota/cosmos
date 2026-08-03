---
type: "concept"
title: "Don't Build Multi-Agents"
description: "Cognition's case for context engineering and single-threaded agents over premature multi-agent architectures"
tags: ["multi-agent", "context-engineering", "single-agent", "cognition", "reliability"]
timestamp: "2026-08-03T12:00:00Z"
status: "growing"
source: ["https://cognition.ai/blog/dont-build-multi-agents"]
---

# Don't Build Multi-Agents

## Summary
Cognition's June 2025 post argues that most teams should not build multi-agent systems yet. The core problem is context: splitting a task across subagents fragments the context each one sees, and the fragments are where miscommunication and conflicting assumptions live. The post's two principles — share full context and traces, and remember that actions carry implicit decisions — make single-threaded agents the reliable default in 2025.

## Details
- **Context engineering is the job** — prompt engineering writes a task in ideal format for a chatbot; context engineering does that automatically inside a dynamic system, and is effectively the #1 job of engineers building agents.
- **The fragile decomposition** — breaking "build a Flappy Bird clone" into subtasks ("background", "bird") looks clean until each subagent interprets its slice differently; multi-turn tool-call histories make miscommunication likely even when the original task is copied down.
- **Principle 1 — share context and full traces** — subagents need the context of prior agents' actions, not just individual messages; partial context produces style and assumption drift.
- **Principle 2 — actions carry implicit decisions** — each agent's actions encode assumptions the others can't see; conflicting decisions produce incompatible outputs that a coordinator must reconcile.
- **Default architecture** — a single-threaded linear agent keeps context continuous and is the simplest way to avoid conflicting decision-making; wide architecture space still exists within that constraint.
- **Claude Code's design** — as of June 2025 Claude Code spawns subagents serially and only for well-defined questions, never parallel work, because a subtask agent lacks the main agent's context; the benefit is keeping investigative work out of the main trace to extend context longevity.
- **Edit-apply models** — 2024-era pipelines that had a large model describe edits and a small model apply them were fragile; the ambiguity between description and application caused errors, and single-model edit is now more reliable.
- **Multi-agent discourse is premature** — agents today cannot sustain the long-context proactive discourse needed for real consensus; cross-agent context-passing is unsolved, and parallelism will unlock as single-threaded agents get better at communicating with humans.

## Related
- [[wiki/llm-agents/multi-agent-research-systems|Multi-Agent Research Systems]] — the counterexample that works
- [[wiki/llm-agents/multi-agent-systems-guide|How and When to Build Multi-Agent Systems]] — the reconciliation
- [[wiki/prompt-engineering/context-engineering|Context Engineering]] — the discipline
- [[wiki/llm-agents/agentic-loops|Agentic Loops]] — single-threaded loop design
- [[wiki/agent-systems/sub-agent-delegation|Sub-Agent Delegation]] — when subagents do work
- [[wiki/llm-agents/handoff-protocol|Handoff Protocol]] — context passing between agents
- [[wiki/syntheses/loop-graph-engineering-wave-2026-08|Loop/Graph Engineering Wave]] — synthesis

## Sources
- Cognition, "Don't Build Multi-Agents", 2025-06 — https://cognition.ai/blog/dont-build-multi-agents
