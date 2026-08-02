---
type: "concept"
title: "Goal Specification"
description: "The task of stating what an AI system should optimize"
tags: ["goal-specification", "alignment", "specification", "objectives"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/AI_alignment", "https://arxiv.org/abs/2206.05862"]
---

# Goal Specification

## Summary
Goal specification is the problem of expressing the intended objective precisely enough that optimization cannot exploit the gap between the spec and the intent. Nearly every alignment failure traces back to a specification failure, making it the foundational alignment problem.

## Details
- **Formats** — reward functions, constitutions/rules, preference datasets, and descriptions (LLM goals).
- **Failure modes** — specification gaming, reward hacking, and Goodhart drift all exploit spec gaps.
- **Improvements** — preference elicitation, process supervision, and iterative refinement of specs against discovered exploits.
- **Evaluation** — spec-gaming red teams probe whether behavior matches intent beyond the letter of the spec.
- **RSIS3 relevance** — the practices document is a goal specification for the workspace; the checker enforces it mechanically.

## Related
- [[wiki/concepts/value-specification|Value Specification]] — the normative layer
- [[wiki/concepts/specification-gaming|Specification Gaming]] — the failure mode
- [[wiki/concepts/specification-problems|Specification Problems]] — taxonomy of gaps
- [[wiki/concepts/preference-elicitation|Preference Elicitation]] — learning the intent
- [[wiki/concepts/goal-drift|Goal Drift]] — spec decay over time
- [[wiki/concepts/utility-functions|Utility Functions]] — objective form
- [[wiki/concepts/calibration|Calibration]] — measurement honesty in the existing graph
- [[wiki/concepts/preference-falsification|Preference Falsification]] — data corruption
