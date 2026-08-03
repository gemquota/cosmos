---
type: "concept"
title: "Impact Measures"
description: "Quantifying how much an agent changes the world"
tags: ["impact", "measures", "safety"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Impact Measures

## Summary
Impact measures estimate the disturbance an agent causes, enabling penalties for excessive or irreversible change. The idea: an agent pursuing a goal should be able to change the world, but not gratuitously — and a measure of how much the world changed, beyond what the task required, is what lets a reward function or policy distinguish purposeful action from collateral damage.

## Details
- The design space is large. Reachability-based measures compare the set of states the agent could have reached against the set it should have; they penalize an agent for reducing its own or others' options. Information-theoretic measures quantify the divergence between the world's trajectory with and without the agent (or against a baseline policy), penalizing surprise relative to a no-intervention baseline. State-distance measures score how far the world moved from a reference state, penalizing large deviations regardless of direction. Each family makes different philosophical commitments about what "impact" means — options lost, information changed, or distance traveled.
- Good measures are hard: they must separate intended effects from collateral ones. The central failure mode is that impact is entangled with the task: opening a door, which the task requires, looks identical in state-distance terms to breaking a window, which it does not. Every known measure needs a baseline or a reference frame to distinguish the two, and choosing that reference frame is where the practical difficulty lives — too loose a frame lets collateral damage through, too tight a frame penalizes the agent for doing its job.
- Applications include reward shaping and conservative exploration. In RL, an impact penalty added to the reward steers the agent toward minimal-intervention solutions of a task; in exploration, impact-bounded policies explore cautiously, which trades exploration efficiency for safety. Both uses share the calibration problem: the penalty weight is a delicate hyperparameter.
- The safety stakes: without impact control, an optimizing agent has instrumental reason to grab resources, disable its off-switch, and reshape its environment for goal attainment — power-seeking is impact-seeking, so impact measures are one of the mechanisms that bound it.
- RSIS3 relevance: pass impact (files changed, links added) is tracked and bounded. An improvement pass is allowed to change the wiki, but the practices limit the blast radius — which files, which scope — so a self-improvement system never conflates "more changes" with "better changes".

## Related
- [[wiki/concepts/impact-regularization|Impact Regularization]] — the penalty form
- [[wiki/concepts/side-effects-problem|Side Effects Problem]] — the problem form
- [[wiki/concepts/restraint-training|Restraint Training]] — the training form
- [[wiki/concepts/power-seeking-ai|Power-Seeking AI]] — the escalation it bounds
- [[wiki/concepts/mild-optimization|Mild Optimization]] — the full treatment of this theme
- [[wiki/concepts/calibration|Calibration]] — existing graph context
