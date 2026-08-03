---
type: "concept"
title: "Health Endpoint Contracts"
description: "Standardized /healthz and /readyz response semantics"
tags: ["health", "endpoints", "probes", "contracts"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Health Endpoint Contracts

## Summary
Health endpoint contracts standardize how services expose liveness, readiness, and dependency health so orchestrators, load balancers, and dashboards can interpret them uniformly. The contract — usually JSON with a status field and per-dependency detail — separates process-alive from can-serve-useful-work, the two questions probes must answer distinctly.

## Details
- Mechanism: `/healthz` reports liveness (process up, able to serve probes); `/readyz` reports readiness (dependencies reachable, caches warm, migrations applied); both return 200 when healthy and 503 otherwise; a detailed variant returns a JSON body listing per-dependency status and latency so operators see what is actually wrong; Kubernetes livenessProbe/readinessProbe, cloud LB health checks, and custom polling all consume the same endpoints.
- Concrete example: a service whose readiness endpoint checks the database connection and returns `{"status":"ready","deps":{"db":"ok"}}`; during a DB outage it returns 503 with `"db":"down"`, and the load balancer stops sending traffic while liveness stays 200 so the orchestrator does not restart the process.
- Failure modes: conflating liveness and readiness — a readiness failure that restarts the pod in a crash loop, or a liveness check that passes while the app serves errors; health checks that are too expensive (full dependency probes on every poll, scaling cost) or too shallow (process up only); checks that depend on themselves (a health endpoint calling the same service); 503s from missing but non-critical dependencies taking capacity out unnecessarily.
- Tradeoffs: deep readiness checks protect users from broken services but reduce capacity during partial outages; shallow checks keep capacity but let bad traffic through; the contract should distinguish critical from non-critical dependencies and let operators tune which failures remove a node.
- Operational notes: keep health endpoints cheap and cache dependency results briefly, document the contract, and monitor health-check failure rates as a signal.
- RSIS3 relevance: the wiki daemon and dashboard should expose the same liveness/readiness contract so RSIS3's monitoring and any LB can decide availability without guessing.

## Related
- [[wiki/infrastructure/health-check-patterns|Health Check Patterns]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
