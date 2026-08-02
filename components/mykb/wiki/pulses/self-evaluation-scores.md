---
type: "concept"
title: "Self-Evaluation Scores"
description: "Numerical scores a system assigns to its own outputs"
tags: ["self-evaluation", "scores", "telemetry"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Self-Evaluation Scores

## Summary
Self-evaluation scores are numeric ratings a system gives its own work, typically on rubrics or confidence scales.

## Details
- Self-evaluation scores are numeric ratings a system gives its own work, typically on rubrics or confidence scales.
- They are telemetry, not ground truth: useful for trends, unreliable in absolute value.
- Calibration checks compare scores against external outcomes.
- RSIS3 relevance: pulse layer scores are self-evaluation scores recorded as telemetry.

## Related
- [[wiki/pulses/self-ratings|Self-Ratings]] — the same signal, less formal
- [[wiki/pulses/self-reports-vs-measures|Self-Reports vs Measures]] — why scores can diverge
- [[wiki/pulses/capability-measurement|Capability Measurement]] — external counterpart
- [[wiki/concepts/telemetry|Workspace Telemetry]] — where scores are stored
- [[wiki/agent-systems/self-evaluation|Self-Evaluation]] — the full treatment of this theme
