---
type: "concept"
title: "Fault Injection Tools"
description: "Chaos tools that deliberately break dependencies in test"
tags: ["fault-injection", "chaos", "testing", "resilience"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Fault Injection Tools

## Summary
Fault injection tools deliberately introduce failures — latency, errors, network partitions, resource exhaustion — into a running system to prove it degrades gracefully. Chaos engineering tools (Chaos Mesh, Litmus, Gremlin) and library-level injectors (toxiproxy, resilience4j) make fault injection repeatable and safe enough to run in CI and staging.

## Details
- Mechanism: injection is scoped and blast-radius controlled — target a pod, service, or dependency; inject a defined fault (kill a node, add latency to a proxy, return 500s from a dependency); observe behavior against hypotheses; roll back automatically; experiments are versioned and repeatable, not random destruction.
- Concrete example: Chaos Mesh kills a random pod in a stateful service to prove leader election recovers; Toxiproxy adds 200ms latency to the database connection to verify timeouts and circuit breakers; Litmus runs scheduled chaos experiments against staging during off-peak windows.
- Failure modes: injection escaping its blast radius (a chaos experiment taking down production accidentally — always tag and limit targets); fault injection on systems without observability, producing no learning; experiments that are not hypotheses-driven, so teams celebrate "nothing broke" without knowing what was tested; injection interacting badly with automated rollbacks, triggering mass reverts.
- Tradeoffs: fault injection gives the highest-fidelity evidence that failure handling works, but it is risky and noisy — run in staging first, start with small blast radius, and pair with game days; library-level injection is safer and cheaper but tests only the app's own resilience, not infrastructure behavior.
- Operational notes: keep experiments in version control, define an abort mechanism, and integrate regular injection into the release pipeline rather than one-off events.
- RSIS3 relevance: RSIS3's loops are exactly the kind of system that benefits from fault injection — prove that a failed MyKB call or a slow LLM provider degrades loop telemetry instead of corrupting state.

## Related
- [[wiki/shell-environment/unix-text-processing-tools|Unix Text Processing Tools]]
- [[wiki/devops-infra/backup-tools-restic-borg|Backup Tools: restic & Borg]]
- [[wiki/os-shell/checksums-and-hashing-tools|Checksums & Hashing]]
- [[wiki/infrastructure/network-simulation-tools|Network Simulation Tools]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
