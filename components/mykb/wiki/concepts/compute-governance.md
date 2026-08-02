---
type: "concept"
title: "Compute Governance"
description: "Policies that govern AI by tracking and controlling compute"
tags: ["compute-governance", "governance", "policy", "compute"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2002.03497", "https://en.wikipedia.org/wiki/AI_governance"]
---

# Compute Governance

## Summary
Compute governance is the idea that AI's most measurable input — compute — can serve as the handle for oversight: registry of large training runs, export controls on chips, and compute-based thresholds for safety requirements. Sastry et al.'s 2020 analysis made the proposal concrete.

## Details
- **Why compute** — compute is easier to measure and track than models or data, and capability correlates with it.
- **Levers** — registration thresholds, licensing of training clusters, chip export controls, and 'compute provenance' for model releases.
- **Trade-offs** — over-regulation of compute can entrench incumbents and drive runs underground; thresholds must be public and debated.
- **Evidence** — the EU AI Act and national registries already use compute thresholds as triggers.
- **RSIS3 scale note** — consumer devices like Termux can't run frontier training runs, but the knowledge-workload governance principles still apply to agent compute budgets.

## Related
- [[wiki/concepts/responsible-scaling|Responsible Scaling]] — threshold-based safety
- [[wiki/concepts/capability-forecasting|Capability Forecasting]] — what thresholds predict
- [[wiki/decisions/weight-release-policies|Weight Release Policies]] — the release-side lever
- [[wiki/concepts/frontier-models|Frontier Models]] — the governed class
- [[wiki/agent-systems/ai-regulation|AI Regulation]] — legal wrapper
- [[wiki/concepts/competitive-pressures|Competitive Pressures]] — why coordination is needed
- [[wiki/syntheses/evidence-and-provenance|Evidence and Provenance: Open Threads]] — provenance discipline in the graph
- [[wiki/syntheses/parallel-agent-acquisition|Parallel Agent Acquisition (5×100) & Writer Reliability]] — prior parallel-pass experience
