---
type: "concept"
title: "Skill Acquisition Loops"
description: "Cycles in which agents learn and consolidate new skills"
tags: ["skills", "agents", "learning", "loops"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2303.11366", "https://en.wikipedia.org/wiki/Learning_curve"]
---

# Skill Acquisition Loops

## Summary
A skill acquisition loop is the cycle by which an agent tries a task, learns from feedback, and consolidates the result into reusable capability. Efficiency of this loop — attempts per skill, retention, transfer — determines how fast an agent system can grow.

## Details
- **Stages** — attempt, evaluate, distill (into memory or weights), reuse, and transfer to related tasks.
- **Memory coupling** — episodic records of attempts feed semantic skill libraries; RSIS3's wiki plays this role for the triad.
- **Measurement** — skill acquisition is tracked via learning curves and transfer scores.
- **Failure modes** — brittle skills that overfit their training context, and forgetting (catastrophic interference).
- **Worked example** — an agent that writes a reflection note after each failed task, then searches those notes before retrying, acquires skills faster than one that retries blind.

- **Distillation** — episodic attempt records are distilled into semantic skill entries (what works, when, why), building a skill library the agent searches before acting.
- **Transfer** — the loop's payoff is transfer: a skill learned on one task should generalize; measuring transfer scores exposes brittle, overfit skills.
- **Bottlenecks** — the loop is capped by evaluation signal quality (weak feedback → weak skills) and by forgetting (new skills crowding out old ones).
- **Retention** — periodic re-exposure and consolidated reference notes protect against catastrophic interference between skills.

- **Worked example** — an agent that writes a reflection note after each failed task and searches those notes before retrying acquires skills measurably faster than one that retries blind; the loop is the difference.

- **Measurement** — the loop is tracked with learning curves (success rate vs attempts) and transfer scores (does the skill help on new tasks), which distinguish real acquisition from task memorization.

## Related
- [[wiki/agent-systems/curriculum-self-improvement|Curriculum Self-Improvement]] — ordering acquisition
- [[wiki/agent-systems/reflection-agents|Reflection Agents]] — the reflection-based loop
- [[wiki/concepts/inner-outer-loop-learning|Inner/Outer Loop Learning]] — note
- [[wiki/concepts/continual-self-improvement|Continual Self-Improvement]] — lifetime framing
- [[wiki/concepts/calibration|Calibration]] — measurement
- [[wiki/concepts/procedural-memory|Procedural Memory]] — consolidation substrate
- [[wiki/pulses/self-evaluation-scores|Self-Evaluation Scores]] — self-scored telemetry
- [[wiki/pulses/self-benchmarking|Self-Benchmarking]] — internal benchmarks
