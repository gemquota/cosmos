---
type: "concept"
title: "Service Virtualization"
description: "Simulating dependent services for isolated testing"
tags: ["service-virtualization", "testing", "mocking", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Service Virtualization

## Summary
Service virtualization replaces real downstream services with simulated versions for testing: a virtual service mimics the API, data, and behavior of a dependency (payments, identity, third-party APIs) so tests, demos, and preview environments can run without the real thing. It sits between simple mocks and full contract-simulation environments.

## Details
- Mechanism: a virtualization tool (WireMock, Mountebank, Hoverfly, or a lightweight server) records or defines responses keyed by request; behavior includes status codes, headers, latency, and stateful sequences; the system under test is pointed at the virtual service via config; virtual services are versioned with the tests that use them.
- Concrete example: CI runs the checkout flow against a virtual payment provider returning scripted outcomes (success, declined, timeout); a preview environment uses a virtual identity provider so reviewers can test login without real accounts; a demo environment stays fully self-contained.
- Failure modes: virtualization drift — the virtual service diverges from the real API, so tests pass against the fake and break in production (anchor it with contract tests); over-scripted responses that encode assumptions (happy path only) hiding error-handling gaps; stateful scenarios (webhooks, callbacks) that are hard to virtualize faithfully; teams that never run the real integration, accumulating risk.
- Tradeoffs: virtualization gives fast, cheap, deterministic test and preview environments at the cost of fidelity; the alternative, real integrations, is realistic but slow, costly, and flaky; the mature pattern is virtualization for daily cycles plus scheduled real-integration runs (nightly or pre-release) to catch drift.
- Operational notes: keep virtual services in the repo, pin their API versions, and schedule real-provider runs.
- Scenario design: script realistic failures — timeouts, malformed payloads, 429s — into the virtual service so error-handling paths execute in every run, not only the happy path.
- RSIS3 relevance: cosmos can virtualize external APIs (LLM providers, hosting services) for deterministic eval runs — scripted successes and failures — reserving live calls for acceptance.

## Related
- [[wiki/devops-infra/service-mesh-sidecars|Service Mesh Sidecars]]
- [[wiki/infrastructure/network-function-virtualization|Network Function Virtualization]]
- [[wiki/devops-infra/service-meshes-istio-linkerd|Service Meshes: Istio & Linkerd]]
- [[wiki/cloud-infra/function-as-a-service|Function-as-a-Service]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
