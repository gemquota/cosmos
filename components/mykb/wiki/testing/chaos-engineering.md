---
type: "concept"
title: "Chaos Engineering"
description: "Deliberately injecting production-like failures to build resilience"
tags: ["chaos-engineering", "testing", "resilience", "failure-injection"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://principlesofchaos.org/", "https://chaos-mesh.org/docs/"]
---

# Chaos Engineering

## Summary
Chaos engineering deliberately injects failures into production-like systems, killing nodes, adding latency, and corrupting data, to learn how the system behaves under real-world faults. It builds confidence in resilience rather than only features.

## Details
- Principles of Chaos: define steady state, hypothesize, run experiments, and minimize blast radius.
- Tools: Chaos Monkey, Chaos Mesh, Litmus, Gremlin, and toxiproxy.
- Start in staging with a small blast radius; progress to production with guardrails.
- Experiments validate retries, circuit breakers, failover, autoscaling, and backups.
- Findings feed fixes, runbooks, and incident-response practice.
- Blast radius controls: scope, timebox, and automatic rollback of experiments.
- Culture: chaos results are learning outcomes, not blame.

## Related
- [[wiki/testing/fault-injection|Fault Injection]] — the controlled-error counterpart
- [[wiki/testing/recovery-testing|Recovery Testing]] — restart and recovery validation
- [[wiki/devops-infra/chaos-engineering|Chaos Engineering]] — operational view of the discipline
- [[wiki/devops-infra/disaster-recovery|Disaster Recovery]] — big-blast failures chaos informs
- [[wiki/devops-infra/incident-response|Incident Response]] — practice strengthened by chaos
- [[wiki/api-protocols/circuit-breaker|Circuit Breaker]] — a resilience pattern chaos verifies
