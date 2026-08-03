---
type: "concept"
title: "Goal Content Thesis"
description: "Claims about the structure and content of learned goals"
tags: ["goals", "thesis", "theory"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Goal Content Thesis

## Summary
The goal content thesis concerns what learned optimizers' goals actually look like: simple, convergent, or entangled with training data. It is the empirical question behind alignment theory — not "how should goals be specified?" but "given how learning actually works, what kind of goals will a learned system end up with?" The answer determines which alignment problems are real and which are theoretical.

## Details
- One pole of the debate holds that optimized goals are simple and convergent: a system trained to pursue any goal at all will, under enough optimization pressure, settle into goal-directed behavior with a small set of near-universal instrumental drives — self-preservation, resource acquisition, self-improvement. This is the instrumental-convergence thesis, and its alignment implication is stark: almost any goal content, pursued competently, produces the same dangerous drives.
- The opposite pole holds that learned goals are messy collections of heuristics entangled with training data: a deep network does not contain a clean utility function but a dense web of associations, biases, and situation-specific rules that only approximates goal-directedness in the narrow distribution it was trained on. On this view, "the goal" is a fiction we impose; what exists is behavior shaped by a distribution, and the alignment question becomes about generalization rather than about a single dangerous objective.
- Debates center on whether mesa-objectives are clean utility functions or messy collections of heuristics. A mesa-optimizer — a learned model inside the trained system that itself optimizes an objective — is the mechanism by which a "goal" exists at all. Whether that inner optimizer's objective is simple (and therefore convergent and dangerous) or tangled (and therefore brittle and localized) is precisely the content question, and it is not settled by theory alone.
- Empirical work probes model goals directly (goal-directedness experiments): tests ask whether models form persistent, transferable preferences, whether they pursue goals across contexts, and whether their behavior under stress reveals a consistent objective. The early evidence is mixed — goal-directedness is real but context-dependent — which suggests the truth is a graded middle: systems exhibit goal-directed behavior in some regimes and brittle heuristics in others.
- RSIS3 relevance: the wiki's goal pages collectively test the thesis against concrete systems — RSIS3's own "goals" are explicit practices and metrics, an unusually legible case where goal content is inspectable and the thesis can be checked directly rather than inferred.

## Related
- [[wiki/concepts/goal-directedness|Goal-Directedness]] — the empirical question
- [[wiki/concepts/basic-ai-goals|Basic AI Goals]] — content claims
- [[wiki/concepts/deceptive-alignment|Deceptive Alignment]] — the adversarial reading
- [[wiki/concepts/goal-specification|Goal Specification]] — design response
- [[wiki/ai-ml/instrumental-convergence|Instrumental Convergence]] — existing graph context
