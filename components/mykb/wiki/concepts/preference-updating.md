---
type: "concept"
title: "Preference Updating"
description: "How systems should revise preferences as they learn"
tags: ["preference-updating", "values", "dynamics"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Preference Updating

## Summary
Preference updating is the question of when and how a system's learned preferences should change with new information.

## Details
- Preference updating is the question of when and how a system's learned preferences should change with new information.
- Naive updating allows value drift; frozen preferences cause lock-in.
- Normative models (e.g., CEV-style extrapolation) try to define the right updating rule.
- RSIS3 relevance: the wiki's practices would be updated per pass with explicit review.

- The updating question: when new information should revise learned preferences, how fast, and under whose authority — the answer determines whether a system drifts, locks in, or adapts safely.
- Two failure poles: naive updating allows value drift under noisy feedback, while frozen preferences cause lock-in when the world changes; the design space sits between them.
- Normative rules: CEV-style extrapolation and similar models try to define the right updating rule in principle; in practice the rule needs explicit review and a human checkpoint when stakes are high.
- Practices policy: the wiki's practices would be updated per pass with explicit review — each pass may revise a practice, but only through a visible step that records what changed and why.
- Relationship to identity: preference updating is the temporal side of identity — what stays constant and what may change; the identity system anchors the constant part while the update rule governs the rest.
- Signals that should not move preferences: adversarial feedback, popularity shocks, and single-outcome coincidences — the update rule should distinguish evidence from noise.
- Reviewability: every update should leave a trace — the old preference, the new preference, and the evidence — so a later pass can audit how the system's values changed over time.
- Slowing mechanisms: thresholds, cooling-off periods, and consensus requirements are the standard brakes on too-fast updating; the standing rule is to make drift slower than deliberate change.
## Related
- [[wiki/concepts/preference-drift|Preference Drift]] — the temporal problem
- [[wiki/concepts/coherent-extrapolated-volition|Coherent Extrapolated Volition]] — the normative rule
- [[wiki/agent-systems/value-locking|Value Locking]] — the freezing alternative
- [[wiki/syntheses/post-pass-consolidation|Post-Pass Consolidation]] — the update ritual
- [[wiki/ai-ml/preference-tuning|Preference Tuning]] — existing graph context
