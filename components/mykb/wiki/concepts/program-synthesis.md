---
type: "concept"
title: "Program Synthesis"
description: "Automatically generating programs from specifications"
tags: ["program-synthesis", "pl", "automation", "verification"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Program_synthesis", "https://en.wikipedia.org/wiki/Automated_machine_learning"]
---

# Program Synthesis

## Summary
Program synthesis generates programs automatically from examples, natural language, or formal specifications. It is the engineering frontier of 'computer writes computer': successes exist for small DSLs and code completion, while general synthesis remains open and safety-relevant.

## Details
- **Spec forms** — input/output examples (inductive synthesis), natural-language intent, and logical specifications.
- **Methods** — search over program space, constraint solving, and LLM generation with verification.
- **Why it matters for RSI** — synthesized code is a component of self-improving systems; verified synthesis removes the human author bottleneck.
- **Verification link** — synthesized programs need checking (tests, formal verification), or synthesis is just accelerated bug creation.
- **RSIS3 parallel** — the knowledge loop's generated syntheses and practice checks are synthesis with verification gates.

## Related
- [[wiki/concepts/automated-machine-learning|Automated Machine Learning (AutoML)]] — the ML analog
- [[wiki/concepts/formal-verification-of-agents|Formal Verification of Agents]] — the correctness layer
- [[wiki/decisions/self-improving-compilers|Self-Improving Compilers]] — synthesis at compiler level
- [[wiki/concepts/specification-gaming|Specification Gaming]] — what bad specs yield
- [[wiki/software-engineering/code-generation|Code Generation]] — mykb's tooling side
- [[wiki/concepts/immutable-evaluator|Immutable Evaluator]] — verified acceptance
- [[wiki/decisions/checkpoint-selection|Checkpoint Selection]] — choosing states
- [[wiki/decisions/model-selection-practice|Model Selection in Practice]] — choosing configs
