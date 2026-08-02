---
type: "concept"
title: "Circumvention Evals"
description: "Testing whether models evade safety controls"
tags: ["circumvention", "evals", "safety"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Circumvention Evals

## Summary
Circumvention evals test whether models or users can bypass safety systems: filters, sandboxes, and policies.

## Details
- Circumvention evals test whether models or users can bypass safety systems: filters, sandboxes, and policies.
- Attack classes include obfuscation, indirect injection, and prompt engineering.
- Defenses must be evaluated adversarially and iteratively.
- RSIS3 relevance: the checker is tested for bypasses like any control.

## Related
- [[wiki/concepts/evals-robustness|Evals Robustness]] — the defense
- [[wiki/testing/jailbreak-techniques|Jailbreak Techniques]] — an attack class
- [[wiki/concepts/adversarial-robustness|Adversarial Robustness]] — the property
- [[wiki/syntheses/containment-strategies|Containment Strategies]] — the design
- [[wiki/concepts/control-protocols|Control Protocols]] — the full treatment of this theme
