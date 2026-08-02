---
type: "concept"
title: "Baggage Propagation"
description: "Carrying small metadata strings alongside trace context across service boundaries"
tags: ["tracing", "metadata", "propagation", "observability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Baggage Propagation

## Summary
Baggage lets a trace carry small key-value metadata — tenant, region, experiment — through every hop so downstream systems can tag their spans and logs. It is powerful but easy to overuse.

## Details
- W3C baggage headers standardize the format; tools like OpenTelemetry expose it as Baggage API.
- Keep baggage small and cardinality-bounded: it crosses every call and lands in every span and log line.
- Privacy and size limits matter — baggage can leak PII into logs if teams are careless.
- RSIS3 relevance: agent runs could carry the task and worker IDs as baggage for cross-service correlation.

## Related
- [[wiki/dev-tools/distributed-tracing-ids|Distributed Tracing IDs]]
- [[wiki/devops-infra/opentelemetry-instrumentation|OpenTelemetry Instrumentation]]
- [[wiki/dev-tools/span-attributes|Span Attributes]]
- [[wiki/dev-tools/request-tracing|Request Tracing]]
- [[wiki/dev-tools/correlation-ids|Correlation IDs]]
