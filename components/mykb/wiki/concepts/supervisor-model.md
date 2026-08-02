---
type: "concept"
title: "Supervisor Model"
description: "A model that evaluates or supervises another model"
tags: ["supervisor", "model", "oversight"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Supervisor Model

## Summary
A supervisor model grades, critiques, or gates another model's behavior, from reward models to verifiers.

## Details
- A supervisor model grades, critiques, or gates another model's behavior, from reward models to verifiers.
- Supervisors inherit the limits of their own training and need external grounding.
- Supervision quality is a system property, not a single-model property.
- RSIS3 relevance: checkers and verifiers are the bundle's supervisor layer.

## Related
- [[wiki/concepts/overseer-models|Overseer Models]] — the oversight role
- [[wiki/concepts/rlaif|RLAIF (RL from AI Feedback)]] — AI-as-supervisor training
- [[wiki/concepts/reward-model-issues|Reward Model Issues]] — supervisor flaws
- [[wiki/concepts/weak-to-strong-generalization|Weak-to-Strong Generalization]] — supervisor capability gap
- [[wiki/agent-systems/agent-supervision|Agent Supervision]] — existing graph context
