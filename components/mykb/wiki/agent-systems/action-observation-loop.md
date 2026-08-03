---
type: "concept"
title: "Action-Observation Loop"
description: "The ReAct-style pattern of interleaving reasoning, actions, and observations"
tags: ["react", "reasoning", "actions", "observations", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2210.03629"]
---

# Action-Observation Loop

## Summary
The action-observation loop is the ReAct pattern: the agent writes a reasoning trace, takes an action, observes the result, and repeats — grounding thought in the environment. It matters because interleaved reasoning prevents the model from drifting on pure imagination and because observations correct wrong beliefs mid-task. RSIS3's L1 loop is a production version of this pattern with tools instead of free-form actions.

## Details
- **Thought** makes reasoning explicit and auditable; **action** changes the world; **observation** updates beliefs.
- The loop grounds LLM reasoning in tool feedback, reducing hallucinated steps.
- Each iteration is a (thought, action, observation) triple, which is exactly the structure RSIS3 logs and replays.
- Failure handling: an unexpected observation triggers re-planning rather than blind continuation.
- Worked example: ReAct on a knowledge task searches, reads a page, notices a contradiction, and searches again before answering.
- Distinction: the action-observation loop is the pattern; the agent loop is the full control cycle around it.

## Related

- [[wiki/agent-systems/agent-loop|Agent Loop]] — the full control cycle hosting this pattern
- [[wiki/concepts/perception-loop|Perception Loop]] — the observation side of the cycle
- [[wiki/concepts/belief-states|Belief States]] — what observations update
- [[wiki/concepts/forward-chaining|Forward Chaining]] — reasoning forward from observations
- [[wiki/concepts/production-rules|Production Rules]] — condition-action rules as actions
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — observations become wiki knowledge
