---
type: "concept"
title: "Baggage Propagation"
description: "Carrying small metadata strings alongside trace context across service boundaries"
tags: ["tracing", "metadata", "propagation", "observability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Baggage Propagation

## Summary
Baggage lets a trace carry small key-value metadata — tenant, region, experiment, user cohort — through every hop so downstream systems can tag their spans and logs. W3C baggage headers standardize the format, and OpenTelemetry exposes it as the Baggage API; it is powerful but easy to overuse.

## Details
- Mechanism: at the edge, code injects baggage entries into the W3C baggage header; each instrumented hop propagates the header and exposes the values via the Baggage API; spans, logs, and metrics can read them to add attributes; downstream services get context without re-deriving it.
- Concrete example: an API gateway adds region and tenant to baggage; every downstream service tags its spans and logs with them, so support can filter logs by tenant; an experiment flag rides in baggage, letting all services log which variant a user saw.
- Failure modes: baggage bloat — every entry crosses every call and lands in every span and log line, so size and cardinality must be bounded; PII in baggage leaking into logs and trace stores (scrub before injecting); values used for routing or security decisions (baggage is advisory, not trusted); propagation gaps where a non-instrumented hop drops the header.
- Tradeoffs: baggage gives cheap, pervasive correlation versus re-deriving context at each layer, but it trades privacy and log hygiene for convenience; the alternative — passing explicit context parameters — is type-safe and auditable but invasive; the discipline is small, low-cardinality, non-sensitive keys only.
- Operational notes: document the baggage schema, cap size and count, and sanitize values at the edge.
- RSIS3 relevance: agent runs could carry task and worker IDs as baggage for cross-service correlation — exactly the pattern RSIS3 needs when debugging a loop across components.

## Practice
- Operational notes: document the baggage schema, cap its size, and treat baggage values as untrusted strings at every hop — never use them for access decisions.
## Related
- [[wiki/dev-tools/distributed-tracing-ids|Distributed Tracing IDs]]
- [[wiki/devops-infra/opentelemetry-instrumentation|OpenTelemetry Instrumentation]]
- [[wiki/dev-tools/span-attributes|Span Attributes]]
- [[wiki/dev-tools/request-tracing|Request Tracing]]
- [[wiki/dev-tools/correlation-ids|Correlation IDs]]
