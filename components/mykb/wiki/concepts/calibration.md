---
type: "concept"
title: "Calibration"
description: "The match between an agent's stated confidence and its actual accuracy"
tags: ["calibration", "confidence", "evaluation", "reliability"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Calibration

## Summary
Calibration measures whether confidence matches reality: an agent that is right 80% of the time when it says 80% is calibrated. It matters because uncalibrated confidence drives both overreach and wasted caution. RSIS3 tracks self-assessed confidence against outcomes.

## Details
- Metrics: expected calibration error, reliability diagrams.
- Causes of miscalibration: distribution shift, overfitting to training, reward hacking.
- Improvements: temperature scaling, verbalized uncertainty, outcome tracking.
- Open questions: calibration of tool-use agents under new environments.

## Related
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — where calibration is measured
- [[wiki/concepts/metacognition|Metacognition]] — the source of confidence estimates
- [[wiki/llm-agents/self-reflection-agents|Self-Reflection Agents]] — reflection quality depends on it
- [[wiki/llm-agents/reward-hacking|Reward Hacking]] — the failure mode of misplaced confidence
- [[wiki/concepts/confabulation|Confabulation]] — high confidence in invented content
