---
type: "concept"
title: "Chaos Engineering"
description: "Designing and running controlled experiments that inject failures to reveal system weaknesses before users do"
tags: ["chaos-engineering", "resilience", "testing", "sre", "failure-injection"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://principlesofchaos.org/"]
---

# Chaos Engineering

## Summary
Chaos engineering is the disciplined practice of injecting failures into production-like systems to learn how they behave under stress. Experiments start from a hypothesis about steady state, introduce controlled disruption within a bounded blast radius, and either confirm resilience or expose weaknesses to fix. It turns resilience from an aspiration into a measured property.

## Details
- Principles: define steady state (normal behavior via metrics), hypothesize it holds under disruption, introduce varied real-world events (instance loss, latency, network partitions), and run experiments in production or realistic staging.
- Blast-radius control: start small — kill one instance or delay a subset of traffic — and expand only as confidence grows; never experiment on systems without health checks and rollback.
- GameDays make chaos reproducible: scheduled exercises with scenarios, roles, and a timeline exercise the incident-response muscle, not just the infrastructure.
- Tooling: Chaos Monkey terminates instances, chaos-mesh and Litmus inject faults into Kubernetes, and service-mesh fault injection covers L7.
- Relationship to SRE: chaos findings translate directly into error-budget usage, runbook updates, and resilience investments.
- Anti-pattern: random failure injection without hypotheses and observability produces noise, not learning — metrics and tracing must be in place first.
- Relevance to mykb: RSIS3 can rehearse infrastructure failure — losing a database replica or a message broker — with a game day before it happens for real.

## Related
- [[wiki/devops-infra/incident-response|Incident Response]] — the muscle chaos exercises build
- [[wiki/devops-infra/golden-signals|Golden Signals]] — steady-state metrics that define experiments
- [[wiki/devops-infra/error-budgets|Error Budgets]] — how much failure is acceptable to test with
- [[wiki/devops-infra/runbooks|Runbooks]] — documented responses validated by chaos
- [[wiki/devops-infra/observability|Observability]] — prerequisite for meaningful experiments
- [[wiki/devops-infra/kubernetes|Kubernetes]] — primary target platform for fault injection
