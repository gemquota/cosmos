---
type: "concept"
title: "Chaos Engineering"
description: "Experimenting with failures to build confidence"
tags: ["chaos", "failure", "experiments", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://principlesofchaos.org/",
  "https://litmuschaos.io/",
]
---

# Chaos Engineering

## Summary
Chaos engineering experiments with failures in production to build confidence in resilience. Controlled disruption reveals weaknesses before real incidents do. It operationalizes the question: what happens when this component fails under real conditions?

## Details
- Experiments have hypotheses: inject a failure, observe behavior, and compare against expectations.
- The Principles of Chaos define the discipline's scope and boundaries.
- Blast radius control (small, reversible experiments) is a hard requirement.
- Game days simulate incidents for training; chaos tools automate fault injection.
- Litmus is an open-source chaos platform for Kubernetes.
- In mykb, chaos connects to game days, fault injection tools, and reliability.
- Experiments start small, in staging, and grow in scope only as confidence increases.
- Automated chaos runs as part of CI catch regressions in resilience behavior.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.
- Pipelines and GitOps practices in the delivery articles show how this concept is deployed and promoted safely.

## Related
- [[wiki/devops-infra/release-engineering-trains|Release Engineering Trains]]
- [[wiki/infrastructure/traffic-engineering|Traffic Engineering]]
- [[wiki/devops-infra/chaos-engineering|Chaos Engineering]]
- [[wiki/devops-infra/site-reliability-engineering|Site Reliability Engineering]]
