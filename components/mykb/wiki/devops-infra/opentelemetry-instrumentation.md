---
type: "concept"
title: "OpenTelemetry Instrumentation"
description: "Vendor-neutral telemetry generation and export"
tags: ["opentelemetry", "telemetry", "instrumentation", "tracing"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://opentelemetry.io/docs/concepts/instrumentation/",
  "https://opentelemetry.io/docs/concepts/signals/",
]
---

# OpenTelemetry Instrumentation

## Summary
OpenTelemetry is the vendor-neutral standard for generating and exporting telemetry: traces, metrics, and logs. Instrumentation can be automatic, manual, or agent-based, and the SDKs export through OTLP. Adopting OpenTelemetry prevents vendor lock-in for observability data and standardizes the collection layer.

## Details
- The OTel instrumentation concepts page distinguishes auto-instrumentation, manual instrumentation, and the agent model.
- SDKs export data through OTLP to any compatible backend.
- Context propagation carries trace IDs across service boundaries.
- Instrumentation libraries cover the major languages and frameworks.
- Sampling and cardinality control keep OTel overhead manageable.
- In mykb, OTel connects to distributed tracing, observability pillars, and network observability.
- Auto-instrumentation hooks into popular frameworks with minimal code, while manual spans add business context.
- A solid instrumentation strategy defines naming, attributes, and cardinality before rollout at scale.
- Context propagation headers such as traceparent flow across service boundaries automatically when configured.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.

## Related
- [[wiki/devops-infra/envoy-data-plane|Envoy Data Plane]]
- [[wiki/devops-infra/nginx-configuration-patterns|NGINX Configuration Patterns]]
- [[wiki/devops-infra/acid|ACID]]
- [[wiki/devops-infra/alert-fatigue|Alert Fatigue]]
