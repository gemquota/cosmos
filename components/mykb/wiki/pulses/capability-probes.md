---
type: "pulse"
title: "Capability Probes"
description: "Focused tests that detect specific capabilities"
tags: ["probes", "capabilities", "evals"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Capability Probes

## Summary

Capability probes are minimal, targeted tests for specific skills — a reasoning type, a tool-use pattern, a hazardous behavior. They detect capability early and cheaply, and can be inserted into longer pipelines to catch emerging ability before it matters.

## Details
- Mechanism: a probe is a focused task with a known-correct answer (or verifiable outcome) engineered to isolate one capability; probe batteries cover reasoning, instruction-following, tool use, and hazardous behaviors; probes run often and cheaply, producing a capability time series; design must resist memorization (fresh variants) and contamination (probes seen in training).
- Concrete example: a probe battery tests a model's ability to follow multi-step instructions, use a tool correctly, and refrain from a prohibited behavior; a weekly run plots each capability over time, so a sudden jump in a hazardous skill triggers review; a long pipeline inserts probes between stages to attribute capability to the stage that produced it.
- Failure modes: probe contamination (the model memorized the probe from training data — rotate variants); shallow probes that measure surface behavior, not robust capability; single-trial noise misread as capability change; and probe results treated as absolute rather than signal to investigate.
- Operational tradeoffs: probes trade eval coverage for cheap repetition; the discipline is calibrating probes on known models, running them at fixed cadence, and treating anomalies as triggers for deeper evaluation rather than conclusions.
- RSIS3/mykb relevance: capability tracking in the loop uses probes on the knowledge graph's own outputs — the loop measures its own evolving capability the same way it measures models.
- Probe lifecycle: retire and replace probes on a schedule; a probe that has been saturated for months is measuring nothing new.
- Battery composition: mix easy and hard items so the time series stays informative across capability growth, avoiding both floor and ceiling effects.

## Related
- [[wiki/pulses/capability-measurement|Capability Measurement]] — the general method
- [[wiki/concepts/capability-jumps|Capability Jumps]] — what probes should catch
- [[wiki/concepts/dangerous-capability-evals|Dangerous Capability Evals]] — hazard probes
- [[wiki/concepts/evals-practice-ai|Evals Practice]] — probe hygiene
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]]
