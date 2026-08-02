---
type: "concept"
title: "Chaos Experiments"
description: "Deliberately injecting failures to learn how a system behaves under stress"
tags: ["chaos-engineering", "experiments", "reliability", "tooling"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Chaos Experiments

## Summary
Chaos experiments inject controlled failures — kill a node, drop packets, throttle a service — to verify that resilience mechanisms actually work. The point is not destruction but evidence: hypotheses about failure behavior tested in production-like conditions.

## Details
- Design experiments as hypotheses with blast-radius controls: what do we expect, how do we measure?
- Start small (one instance, one region) and automate with tools like Chaos Monkey or Litmus.
- Blast radius first: never experiment without rollback and observability in place.
- mykb relevance: chaos-test the wiki sync to prove link-checking survives a source outage.

## Related
- [[wiki/testing/chaos-engineering|Chaos Engineering]]
- [[wiki/tooling/game-days|Game Days]]
- [[wiki/tooling/failure-drills|Failure Drills]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
- [[wiki/devops-infra/chaos-engineering|Chaos Engineering]]
