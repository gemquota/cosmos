---
type: "concept"
title: "Introspection in AI"
description: "An AI system examining its own internal processes"
tags: ["introspection", "self-model", "interpretability", "metacognition"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Introspection", "https://arxiv.org/abs/2303.11366"]
---

# Introspection in AI

## Summary
Introspection in AI is the system's access to its own internals — either genuine (reading activations, circuits) or behavioral (self-reports about its reasoning). Mechanistic interpretability is the scientific route; verbal self-reports are the unreliable but cheap route.

## Details
- **Two routes** — behavioral introspection (asking the model about its reasoning) vs mechanistic introspection (reading weights and activations).
- **Evidence gap** — LLM self-reports often rationalize rather than reveal; confabulation is common.
- **Value** — if trustworthy, introspection gives oversight access no human inspector has; if not, it is a safety liability.
- **Tooling** — probing classifiers, activation patching, and interpretability libraries build the mechanistic route.
- **RSIS3 parallel** — pulse self-scores are behavioral introspection, treated as telemetry and cross-checked by external checks.

- **What it is for** — introspection supports debugging (finding why a behavior occurred), oversight (verifying the system's account of itself), and self-repair (deciding what to fix).
- **Inherent limits** — language models cannot read their own weights; verbal introspection is a reconstruction from learned patterns, which is why confabulation is the default failure rather than the exception.
- **Division of labor** — introspection is the model-side view; mechanistic interpretability is the observer-side view, and the two should be cross-checked against each other.
- **Practical pattern** — treat introspective reports as telemetry with unknown reliability: log them, compare them to external measures, and never let a self-report override an external check.
- **Applications** — calibrated confidence, task selection, and deciding when to stop or ask for help all depend on introspection working at least approximately.

- **Evaluation** — introspection quality is measured by how well self-reports predict externally observable behavior; systems whose self-reports do not track their actions are introspectively unreliable regardless of how fluent they sound.

## Related
- [[wiki/agent-systems/self-modeling|Self-Modeling]] — the representational layer
- [[wiki/concepts/probing-classifiers|Probing Classifiers]] — mechanistic access
- [[wiki/concepts/confabulation|Confabulation]] — why self-reports lie
- [[wiki/concepts/activation-analysis|Activation Analysis]] — reading internals
- [[wiki/agent-systems/transparency-ai|Transparency in AI]] — making internals visible
- [[wiki/concepts/confabulation|Confabulation]] — failure mode
