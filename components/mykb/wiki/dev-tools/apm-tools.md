---
type: "concept"
title: "APM Tools"
description: "Application performance monitoring suites that combine metrics, traces, and alerts"
tags: ["apm", "observability", "monitoring", "tooling"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# APM Tools

## Summary
APM tools (Datadog, New Relic, Sentry Performance) bundle auto-instrumentation, dashboards, traces, and alerting for applications. They give teams a turnkey view of request latency, errors, and throughput.

## Details
- Auto-instrumentation captures spans for common frameworks with little code, but custom spans are needed for domain logic.
- APM cost scales with volume: sample traces and curate dashboards to keep the bill and the noise down.
- Correlate traces with logs and error events so an alert leads to a root cause in one click.
- mykb relevance: an APM lens on the acquisition pipeline would surface slow curation steps.

## Related
- [[wiki/dev-tools/trace-viewers|Trace Viewers]]
- [[wiki/devops-infra/observability|Observability]]
- [[wiki/dev-tools/metric-backends|Metric Backends]]
- [[wiki/dev-tools/error-tracking-tools|Error Tracking Tools]]
- [[wiki/devops-infra/alert-fatigue|Alert Fatigue]]
