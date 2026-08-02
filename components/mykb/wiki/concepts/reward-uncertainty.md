---
type: "concept"
title: "Reward Uncertainty"
description: "How confident a system should be about its reward signal"
tags: ["reward-uncertainty", "alignment", "epistemics"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Reward Uncertainty

## Summary
Reward uncertainty is the system's calibrated doubt about whether its reward truly tracks intent.

## Details
- Reward uncertainty is the system's calibrated doubt about whether its reward truly tracks intent.
- Uncertainty-motivated agents defer to humans (the off-switch game result) and avoid irreversible actions.
- Representing uncertainty explicitly is a design choice many safety analyses recommend.
- RSIS3 relevance: the loop treats self-scores as uncertain signals, not ground truth.

## Related
- [[wiki/concepts/reward-model-error|Reward Model Error]] — the source of doubt
- [[wiki/concepts/off-switch-game|Off-Switch Game]] — why doubt helps
- [[wiki/concepts/preference-uncertainty|Preference Uncertainty]] — the human-side doubt
- [[wiki/agent-systems/approval-based-agents|Approval-Based Agents]] — acting on uncertainty
- [[wiki/ai-ml/reward-model|Reward Model]] — existing graph context
