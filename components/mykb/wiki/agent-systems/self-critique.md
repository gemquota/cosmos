---
type: "concept"
title: "Self-Critique"
description: "A model generating its own critical feedback on its outputs"
tags: ["self-critique", "reflection", "llm", "evaluation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2303.17651", "https://arxiv.org/abs/2206.05862"]
---

# Self-Critique

## Summary
Self-critique is the step where a model reviews its own draft output and produces concrete objections, before a revision step incorporates them. It powers Self-Refine and Reflexion, and it is only as good as the critic's honesty and coverage.

## Details
- **How it works** — a critique prompt (or a separate critic model) enumerates flaws; the generator revises accordingly.
- **Evidence** — Self-Refine improved code and dialogue quality without extra training; critique quality degrades when the signal is flattering.
- **Risks** — self-critique can reinforce bias, hallucinate defects, or rubber-stamp errors; cross-examination and external graders help.
- **Variants** — verbal critique, structured rubrics, and multi-model critique committees.
- **RSIS3 link** — the practice checker critiques the workspace against practices (a fixed rubric), avoiding self-flattery.

- **Prompt design** — targeted critique questions ('what assumption is unsupported? what case breaks this?') outperform generic 'find problems' prompts.
- **Multi-pass critique** — several critique passes, each focused on a different failure class, find more real defects than one comprehensive pass.
- **Role separation** — a separate critic model (or a critic prompt with no memory of generation) is more honest than the generator critiquing its own draft.
- **Arbitration** — when critique and generator disagree, an external verifier should arbitrate; self-critique alone cannot settle whether a flaw is real.
- **Failure mode** — critique can hallucinate defects, so accepted revisions should be re-checked, not trusted because a critic proposed them.

- **Measurement** — critique quality is measured by precision (are the claimed flaws real?) and recall (were the real flaws found?); both numbers are needed because a critic that invents flaws and one that misses them fail differently.

## Related
- [[wiki/agent-systems/self-correction|Self-Correction]] — the revise step that consumes critique
- [[wiki/agent-systems/reflection-agents|Reflection Agents]] — host architecture
- [[wiki/concepts/cross-examination|Cross-Examination]] — multi-perspective variant
- [[wiki/agent-systems/self-evaluation|Self-Evaluation]] — the scoring sibling
- [[wiki/agent-systems/honest-ai|Honest AI]] — the disposition critique requires
- [[wiki/concepts/confabulation|Confabulation]] — why self-reports can mislead
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the base agent loop in the existing graph
