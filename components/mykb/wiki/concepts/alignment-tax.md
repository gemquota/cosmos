---
type: "concept"
title: "Alignment Tax"
description: "The performance cost of making an AI system safe rather than just capable"
tags: ["alignment-tax", "safety", "capabilities", "tradeoff"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/AI_alignment", "https://arxiv.org/abs/2206.05862"]
---

# Alignment Tax

## Summary
The alignment tax is the capability cost paid for alignment: guardrails, filters, and training constraints that trade raw benchmark performance for safety. Whether the tax is small or large determines whether aligned systems can compete with unaligned ones — a central question for competitive pressure models.

## Details
- **Forms** — safety training reduces some benchmark scores; sandboxing slows agents; oversight consumes compute.
- **Evidence** — RLHF and Constitutional AI show modest taxes on many tasks, sometimes near zero, sometimes large for specialized skills.
- **Strategic role** — if the tax is large, competitive markets reward skipping safety; if small, safety is cheap insurance.
- **Measurement** — alignment-tax-practice tracks the delta between a system with and without safety measures on the same evals.
- **RSIS3 relevance** — the knowledge loop's practice checks are a tax (verification overhead) paid for workspace reliability.

## Related
- [[wiki/concepts/alignment-tax-practice|Alignment Tax in Practice]] — how the tax is measured
- [[wiki/concepts/capability-vs-alignment|Capability vs Alignment]] — the tradeoff space
- [[wiki/concepts/competitive-pressures|Competitive Pressures]] — why the tax matters strategically
- [[wiki/concepts/responsible-scaling|Responsible Scaling]] — policy response
- [[wiki/concepts/safety-evals-practice|Safety Evals Practice]] — measuring both sides
- [[wiki/concepts/meta-parameter-tuning|Meta-Parameter Tuning]] — tuning the tradeoff
- [[wiki/concepts/utility-functions|Utility Functions]] — objective structure in the existing graph
