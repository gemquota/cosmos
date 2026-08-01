---
type: "concept"
title: "Self-Reflection Agents"
description: "Agents that critique their own outputs and revise them"
tags: ["reflection", "self-critique", "agents", "metacognition", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2303.11366"]
---

# Self-Reflection Agents

## Summary
Self-reflection agents evaluate their own work — output quality, failed attempts, reasoning gaps — and revise it before presenting or continuing. This matters because single-shot generation is brittle, and a critique pass catches errors cheaply. Reflexion shows the pattern: the agent verbalizes what went wrong and incorporates that lesson into the next attempt.

## Details
- **Critique loop**: generate → evaluate own output → identify errors → regenerate with the lesson included.
- **Verbal reinforcement**: written self-critique (not just a score) carries information into the next attempt.
- Reflection works best with a rubric: correctness, style, constraint compliance, safety.
- Risks: confident self-critique can be wrong, so calibration matters and external checks still gate final results.
- RSIS3's L2 loop is reflection at the session level: it reviews the session, tunes prompts or code, and re-tests.
- Worked example: an agent writes code, tests it, reflects on the failure mode, then rewrites the patch.

## Related

- [[wiki/llm-agents/reflexion|Reflexion]] — the paper and pattern behind self-critique
- [[wiki/concepts/metacognition|Metacognition]] — the cognitive basis for self-observation
- [[wiki/concepts/calibration|Calibration]] — keeping self-assessment honest
- [[wiki/concepts/confabulation|Confabulation]] — the failure mode of invented explanations
- [[wiki/concepts/mykb-research-report|Mykb Research Report]] — research context for reflection loops
- [[wiki/ops/gap-report|Gap Analysis Report]] — reflection findings feed gap analysis