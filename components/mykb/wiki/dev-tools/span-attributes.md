---
type: "concept"
title: "Span Attributes"
description: "Structured key-value metadata attached to a tracing span"
tags: ["tracing", "spans", "attributes", "observability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Span Attributes

## Summary
Span attributes enrich a span with facts — URL, status code, queue name, tenant — that make traces queryable and meaningful. They are the difference between a bare timing box and a debuggable timeline.

## Details
- Semantic conventions standardize attribute names (http.method, db.system) so tools and dashboards agree.
- Cardinality discipline applies: high-cardinality values belong in logs, not span attributes.
- Attributes let you filter traces by error class, feature flag, or experiment group after the fact.
- mykb relevance: span attributes could record the model, prompt hash, and article slug for agent spans.

## Related
- [[wiki/dev-tools/request-tracing|Request Tracing]]
- [[wiki/dev-tools/trace-viewers|Trace Viewers]]
- [[wiki/dev-tools/baggage-propagation|Baggage Propagation]]
- [[wiki/devops-infra/opentelemetry-instrumentation|OpenTelemetry Instrumentation]]
- [[wiki/dev-tools/sampling-traces|Sampling Traces]]
