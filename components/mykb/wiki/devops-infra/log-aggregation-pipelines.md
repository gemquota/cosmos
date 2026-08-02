---
type: "concept"
title: "Log Aggregation Pipelines"
description: "Collecting, shipping, and indexing logs at scale"
tags: ["logs", "aggregation", "pipelines", "observability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://docs.fluentbit.io/manual/",
  "https://www.elastic.co/guide/en/elastic-stack/current/index.html",
]
---

# Log Aggregation Pipelines

## Summary
Log aggregation pipelines collect, parse, buffer, and index logs from every host into one searchable store. They make debugging possible across large fleets and feed both operations and security workflows. Pipeline design balances completeness, latency, and cost.

## Details
- Agents (Fluent Bit, Filebeat) collect from files, journald, and container stdout.
- Pipelines parse, enrich, and buffer before shipping to storage such as Elasticsearch or Loki.
- Fluent Bit documentation covers inputs, filters, and outputs.
- The Elastic stack documentation describes the indexing and querying side.
- Retention tiers and sampling control cost as volume grows.
- In mykb, log pipelines connect to observability pillars, SIEM, and incident response.
- Structured logging with JSON keys makes parsing deterministic and queries fast.
- Buffer sizing and retry logic prevent log loss when the destination is briefly unavailable.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.
- Pipelines and GitOps practices in the delivery articles show how this concept is deployed and promoted safely.

## Related
- [[wiki/infrastructure/openflow-pipelines|OpenFlow Pipelines]]
- [[wiki/devops-infra/envoy-data-plane|Envoy Data Plane]]
- [[wiki/devops-infra/log-aggregation|Log Aggregation]]
- [[wiki/os-shell/text-processing-pipelines|Text Processing Pipelines]]
