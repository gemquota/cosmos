---
type: "concept"
title: "Loop Specification"
description: "The arXiv formalization of loop engineering: trigger, goal, verification ladder, stopping rule, and memory as a reusable artifact"
tags: ["loop-specification", "loop-engineering", "arxiv", "verification", "stop-hand-holding"]
timestamp: "2026-08-03T12:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2607.00038"]
---

# Loop Specification

## Summary
The June 2026 arXiv paper "Stop Hand-Holding Your Coding Agent: Engineering the Loops that Replace Step-by-Step Prompting" formalizes the practice behind the "stop prompting, start designing loops" slogan. It defines the loop specification: a bounded, reusable artifact — made of a trigger, a goal, a verification step, a stopping rule, and a memory — that a human hands to an agent harness (Claude Code, Codex) so the agent pursues a goal on its own.

## Details
- **Definition** — a loop specification replaces step-by-step prompting; the human designs the loop that prompts the agent, not the individual prompts.
- **Two things it is not** — an ordinary programming loop, and the harness's internal perceive-act-observe cycle; the external loop specification sits on top of both.
- **Progression** — loop engineering is the next layer in the sequence prompt → context → harness → loop; the paper argues against the stronger headlines that it does not retire prompt engineering — loop and prompt are distinct tools with distinct uses.
- **Anatomy** — trigger (what starts the loop), goal type, a five-level verification ladder, architecture, and named terminal states; the stopping rule is the part practitioners under-engineer.
- **Evidence** — a descriptive analysis of the Loop Library, a public corpus of 50 hand-coded loops: 70% verify in the "autonomous zone" of the ladder, 74% name their terminal states, while automated triggering and durable memory remain comparatively underdeveloped.
- **Grounding** — design principles and anti-patterns tied to the literature on self-correction, reward hacking, and model-as-judge fragility (the model that wrote the work grades it too generously).
- **Limits** — verification burden, comprehension debt, and cognitive surrender are the three costs the practice must respect; a loop that runs unattended also makes mistakes unattended.

## Related
- [[wiki/llm-agents/loop-engineering|Loop Engineering]] — the practitioner discipline
- [[wiki/llm-agents/agentic-loops|Agentic Loops]] — the underlying cycle
- [[wiki/llm-agents/prompt-loop-graph-layers|Prompt vs Loop vs Graph]] — the stack placement
- [[wiki/llm-agents/multi-agent-research-systems|Multi-Agent Research Systems]] — verification at scale
- [[wiki/llm-agents/success-criteria|Success Criteria]] — defining done
- [[wiki/llm-agents/approval-gates|Approval Gates]] — human verification
- [[wiki/syntheses/loop-graph-engineering-wave-2026-08|Loop/Graph Engineering Wave]] — synthesis

## Sources
- Sandeco Macedo, "Stop Hand-Holding Your Coding Agent: Engineering the Loops that Replace Step-by-Step Prompting", arXiv:2607.00038, submitted 2026-06-28 — https://arxiv.org/abs/2607.00038
