---
type: "concept"
title: "Self-Modeling"
description: "An agent maintaining a model of itself and its own capacities"
tags: ["self-model", "agents", "identity", "metacognition"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Self-model", "https://en.wikipedia.org/wiki/Self-awareness"]
---

# Self-Modeling

## Summary
Self-modeling is an agent's representation of its own state, goals, capabilities, and limits. A good self-model lets an agent predict its own failures, plan resource use, and refuse unsafe tasks — and it is a prerequisite for safe self-modification, because you can only safely change what you can represent.

## Details
- **Content** — capabilities, knowledge gaps, current state, goals, and history (identity over time).
- **Use** — calibration of confidence, task selection, and deciding when to stop or ask for help.
- **Risks** — self-models can be wrong (confabulated) or manipulated by hidden processes.
- **RSIS3 example** — the identity system and pulse telemetry are the triad's self-model: layers, scores, and crisis state.
- **Relation to RSI** — versioning-of-selves and memory-surgery presuppose an explicit self-model that survives changes.

- **Content** — a self-model covers capabilities (what can I do), limits (what will fail), state (what is true now), goals, and history (what was decided).
- **Uses** — task selection (accept or decline based on predicted success), resource planning, and refusal all depend on an accurate self-model.
- **Failure modes** — an overconfident self-model causes overreach; an underconfident one causes costly deferral; both are errors in the same representation.
- **Calibration loop** — the self-model should be updated from measured performance (what actually succeeded) rather than from claims, keeping it honest over time.
- **Prerequisite for RSI** — safe self-modification requires representing the self that will change; without a self-model, modifications are blind edits.

- **Relation to introspection** — self-modeling is the static representation (the map); introspection is the dynamic access (reading the territory); a system needs both, and each can be wrong independently.

## Related
- [[wiki/agent-systems/introspection-ai|Introspection in AI]] — first-person access
- [[wiki/agent-systems/identity-and-continuity|Identity and Continuity]] — persistence over time
- [[wiki/decisions/versioning-of-selves|Versioning of Selves]] — versioned self-model
- [[wiki/concepts/calibration|Calibration]] — self-model accuracy
- [[wiki/agent-systems/self-evaluation|Self-Evaluation]] — self-model judgment
- [[wiki/concepts/identity-system|RSIS3 Identity System]] — RSIS3 self-model
- [[wiki/pulses/self-evaluation-scores|Self-Evaluation Scores]] — self-scored telemetry
- [[wiki/pulses/self-benchmarking|Self-Benchmarking]] — internal benchmarks
