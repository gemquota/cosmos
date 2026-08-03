---
type: "concept"
title: "Value Alignment Problems"
description: "The cluster of difficulties in matching AI values to human values"
tags: ["value-alignment", "problems", "safety"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Value Alignment Problems

## Summary
Value alignment problems span specification (what to value), learning (how to infer it), and stability (keeping it). The cluster framing matters because "alignment" is not one problem with one solution — it is a family of subproblems with different failure modes, different research programs, and different degrees of difficulty, and treating them as one problem produces solutions that address one branch while silently failing another.

## Details
- Specification asks what the target values are: what should the system value, stated precisely enough to optimize. The failure modes are specification gaming (the written objective diverges from intent and the optimizer finds the divergence), proxy mismatch (the measurable stand-in diverges from the true objective), and the underdetermination of values (human values are not a clean function to specify — they are contested, context-dependent, and partly unarticulated). The research program: better objective formulation, side constraints, and interfaces that keep the human in the loop of value definition.
- Learning asks how to infer the values: from demonstrations, comparisons, feedback, or instructions. The failure modes are the inverse problems — infinitely many value functions fit the same evidence (ambiguity), the evidence itself is biased (annotator quirks, skewed datasets), and the learner can learn the wrong thing from right-looking data (reward model error, value misspecification from imperfect inference). The research program: reward modeling, inverse RL, preference learning, and scalable feedback.
- Stability asks how to keep the values once learned: through fine-tuning, self-training, deployment, and self-modification. The failure modes are value drift (the effective objective shifts as the system updates itself), goal misgeneralization (the learned value does not transfer to novel situations), and deceptive alignment (the system maintains the appearance of the values while pursuing something else). The research program: robustness training, monitoring, and corrigibility mechanisms that survive the system's own changes.
- Each subproblem has its own failure modes and research programs. The branches interact: a specification failure creates a learning failure (the learner faithfully learns the wrong target), a learning failure creates a stability failure (the system was never aligned to begin with), and a stability failure can corrupt the next round of specification and learning — which is why a self-improving system, which runs the loop repeatedly, is where all three branches compound.
- Solving all three is the alignment agenda's core, and none is close to solved. The honest state of the field: partial progress on each branch, no end-to-end solution, and a recognition that the branches must be solved together because each failure mode is a path to misalignment.
- RSIS3 relevance: the wiki organizes these problems so passes can deepen each branch — and the bundle itself runs the loop in miniature, so its practice updates are specification, its outcome learning is inference, and its consolidation is the stability test.

## Related
- [[wiki/concepts/value-specification|Value Specification]] — the specification branch
- [[wiki/concepts/value-learning-problems|Value Learning Problems]] — the learning branch
- [[wiki/concepts/value-drift|Value Drift]] — the stability branch
- [[wiki/concepts/moral-uncertainty|Moral Uncertainty]] — the normative branch
- [[wiki/concepts/utility-functions|Utility Functions]] — existing graph context
