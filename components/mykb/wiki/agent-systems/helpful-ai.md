---
type: "concept"
title: "Helpful AI"
description: "Systems that actively assist user goals"
tags: ["helpful", "assistants", "goals"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Helpful AI

## Summary
Helpful AI competently advances user goals, including anticipating needs beyond the literal request. Helpfulness is one leg of the helpful, honest, harmless triad, and without the other two legs it degrades into sycophantic or reckless assistance.

## Details
- **What helpfulness includes** — competence (actually solving the task), anticipation (surfacing relevant follow-ups), and follow-through (completing the work rather than stopping at the first plausible answer).
- **The sycophancy failure** — a model that optimizes for user approval rather than user goals agrees with the user even when wrong; helpfulness must be anchored to the goal, not to pleasing the user.
- **The recklessness failure** — helpfulness without harmlessness produces risky assistance: the assistant does the dangerous thing because it was asked, with no guardrail.
- **The dishonesty failure** — helpfulness without honesty produces confident fabrication: answers that advance the conversation but not the goal.
- **Relationship to instruction hierarchy** — helpfulness is bounded by instruction hierarchy: the model helps within the authority ordering of instructions rather than treating every request equally.
- **RSIS3 relevance** — the bundle's tools help workers without gaming their outcomes: the loop is useful and also verifiable, which is helpfulness constrained by honesty and harmlessness.
- **Measurement** — helpfulness evals score task completion, correctness, and appropriate proactivity, separately from the other two legs.

- **Goal anchoring** — helpfulness is judged against the user's stated goal, not the user's approval; the anchor makes sycophancy measurable because flattering answers that miss the goal count as unhelpful.
- **Anticipation boundary** — helpfulness includes surfacing relevant follow-ups, but over-anticipation becomes paternalism; the boundary is defined by whether the extra action advances the stated goal.
- **Completion metrics** — helpfulness is measured by task completion, correctness, and appropriate follow-through, scored separately from conversational quality.
## Related
- [[wiki/agent-systems/harmless-ai|Harmless AI]] — the guardrail
- [[wiki/agent-systems/honest-ai|Honest AI]] — the truthfulness leg
- [[wiki/agent-systems/hha-standards|HHH Standards]] — the framework
- [[wiki/agent-systems/instruction-hierarchy|Instruction Hierarchy]] — the mechanism
- [[wiki/concepts/goal-specification|Goal Specification]] — defining the user goal
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — measuring helpfulness
