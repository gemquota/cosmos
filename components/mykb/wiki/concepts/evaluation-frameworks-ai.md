---
type: "concept"
title: "Evaluation Frameworks for AI"
description: "Structured systems for evaluating AI models"
tags: ["evaluation", "frameworks", "evals"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Evaluation Frameworks for AI

## Summary
Evaluation frameworks organize how models are tested: which capabilities, which datasets, which metrics, which thresholds. A framework turns "is this model good?" into a reproducible protocol — defined tasks with known difficulty, standard metrics with agreed interpretation, and explicit decision thresholds that map scores to actions like "deploy", "monitor", or "do not release".

## Details
- A framework has four layers. Task selection decides what to test (capability suites, safety behaviors, robustness to shift); data curation builds or acquires the items with known ground truth and contamination controls; metric definition fixes how performance is scored (accuracy, calibration, refusal rates, task completion, human-eval agreement) including how uncertainty is reported; and decision rules map scores to actions with stated thresholds and escalation paths.
- Good frameworks separate development evals from safety gates. Development evals are fast, noisy, and iterative — they guide training and prompt work, and their contamination matters less because they are internal. Safety gates are slower, higher-stakes, and independently administered — held-out private suites, dangerous-capability and deception evals, and thresholds that a developer cannot unilaterally lower. Conflating the two is a classic failure: a development metric that rises with training gets promoted to a safety gate, and the gate silently becomes an overfit leaderboard.
- The framework's quality decays over time: tasks age out as models solve them, item leakage accumulates through public release, and metrics get gamed as pressure concentrates on them. Framework rot is a standing risk, so frameworks need versioning, periodic re-derivation of baselines, and explicit retirement criteria for tasks that no longer discriminate.
- The tradeoff in design is breadth versus rigor: broad frameworks cover more behavior but with shallower, noisier items; narrow frameworks measure a few behaviors deeply but can miss everything outside their scope. Mature frameworks layer both — a wide screening suite plus focused deep-dive evals triggered by screening flags.
- RSIS3 relevance: the pass verifier is an evaluation framework for the bundle. It fixes which outcomes count as improvement, which invariants must hold, and what threshold a proposed change must clear — and its integrity depends on the same discipline of separating the verifier from the generator.

## Related
- [[wiki/concepts/evals-practice-ai|Evals Practice]] — the practice layer
- [[wiki/concepts/safety-evals-practice|Safety Evals Practice]] — the safety subset
- [[wiki/concepts/capability-classification|Capability Classification]] — the tiering use
- [[wiki/concepts/eval-contamination|Eval Contamination]] — the integrity risk
- [[wiki/agent-systems/self-evaluation|Self-Evaluation]] — the full treatment of this theme
- [[wiki/testing/ai-safety-evals|Ai Safety Evals]] — existing graph context
