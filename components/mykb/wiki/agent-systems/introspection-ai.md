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

## Related
- [[wiki/agent-systems/self-modeling|Self-Modeling]] — the representational layer
- [[wiki/concepts/probing-classifiers|Probing Classifiers]] — mechanistic access
- [[wiki/concepts/confabulation|Confabulation]] — why self-reports lie
- [[wiki/concepts/activation-analysis|Activation Analysis]] — reading internals
- [[wiki/agent-systems/transparency-ai|Transparency in AI]] — making internals visible
- [[wiki/concepts/confabulation|Confabulation]] — failure mode
