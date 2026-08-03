---
type: "concept"
title: "Mirroring & Shadow Traffic"
description: "Copying live traffic to new versions without user impact"
tags: ["mirroring", "shadow-traffic", "testing", "releases"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Mirroring & Shadow Traffic

## Summary
Mirroring and shadow traffic send a copy of production requests to a new version or a canary without the new version answering real users: the shadow receives real traffic, executes fully, and its behavior is compared against the primary's response. It validates rewrites, load, and compatibility under production conditions with zero user-visible risk.

## Details
- Mechanism: the proxy (Envoy, Istio, nginx mirror, or app-level) duplicates requests to a shadow upstream; the primary's response is returned to the client; shadow results are logged and compared (status codes, latency, payload similarity); discrepancies surface in dashboards; rollout flips traffic only after the shadow proves out.
- Concrete example: an API rewrite sends every request to both the old and new backend; the new backend's responses are compared offline — field diffs, error rate, latency percentiles; a message-broker shadow duplicates events to a new pipeline; load testing uses shadowed production traffic instead of synthetic workloads.
- Failure modes: shadow traffic that is not truly read-only — a buggy shadow writing to databases or sending emails duplicates side effects (isolate the shadow environment); resource doubling — the shadow executes the full workload, so budget for 2x compute; comparison bias when the shadow lacks the same context (headers, session state); shadow responses discarded without comparison, producing zero learning.
- Tradeoffs: shadowing gives the highest-fidelity pre-rollout validation at 2x cost and operational complexity; it complements canaries, which expose real users to the new version gradually; keep shadow windows bounded and remove the shadow path once the rollout completes.
- Operational notes: tag shadow requests in traces, alert on divergence rather than only on errors, and size shadow capacity explicitly.
- RSIS3 relevance: RSIS3 can shadow-propose — run a candidate L2 strategy against live pulse data in parallel, compare outcomes, and promote only what demonstrably improves the loop.

## Related
- [[wiki/infrastructure/traffic-shaping-and-qos|Traffic Shaping & QoS]]
- [[wiki/devops-infra/traffic-shifting-and-splitting|Traffic Shifting & Splitting]]
- [[wiki/devops-infra/mirroring-and-proxying-registries|Mirroring & Proxying Registries]]
- [[wiki/infrastructure/east-west-vs-north-south-traffic|East-West vs North-South Traffic]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
