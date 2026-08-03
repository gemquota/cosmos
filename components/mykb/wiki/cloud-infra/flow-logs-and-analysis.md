---
type: "concept"
title: "Flow Logs & Analysis"
description: "Capturing network metadata for security and cost analysis"
tags: ["flow-logs", "analysis", "networking", "vpc"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Flow Logs & Analysis

## Summary

Flow logs capture network traffic metadata — who talked to whom, on which ports, how much — without packet payloads. They are the audit trail and troubleshooting source for VPCs, subnets, and security groups, and the raw material for anomaly detection.

## Details
- Mechanism: AWS VPC Flow Logs, Azure NSG flow logs, and GCP VPC flow logs sample accepted/rejected traffic per interface with fields (src/dst IP, ports, protocol, bytes, packets, action); logs stream to S3/Log Analytics/BigQuery; analysis tools (Athena, Cloud Logging queries, netflow analyzers) turn them into usage reports, exposure reviews, and alerting.
- Concrete example: a security review queries flow logs for 0.0.0.0/0 on port 22 and finds a forgotten dev server accepting SSH from everywhere; an incident investigation confirms which internal host talked to a compromised IP and when; capacity planning uses bytes-per-flow to size NAT and firewall bandwidth.
- Failure modes: flow logs disabled (no retroactive visibility — enable them before incidents); sampling and aggregation hiding low-volume but critical traffic; log costs growing with traffic volume (aggregate and filter in the pipeline); and confusing flow logs with packet captures — they lack payloads, so they answer who/what, not content.
- Operational tradeoffs: flow logs are cheap insurance with real storage/query cost at scale; the pattern is enable per VPC/NSG, stream to a queryable store, and build the top queries (rejected traffic, internet egress, cross-AZ) as reusable views. Treat them as a required security control.
- RSIS3/mykb relevance: the wiki's environments would ship flow logs to the analytics store by default; this note records the standard queries the loop's security reviews reuse.
- Query library: keep the top queries (rejected traffic, internet egress, cross-AZ) as saved views so incidents start from a known baseline rather than ad-hoc SQL. Partition the log store by time and aggregate noisy fields upstream so query cost stays flat as traffic grows.

## Related
- [[wiki/infrastructure/packet-analysis-with-tcpdump|Packet Analysis with tcpdump]]
- [[wiki/devops-infra/metrics-logs-traces|Metrics, Logs & Traces]]
- [[wiki/os-shell/resource-utilization-analysis|Resource Utilization Analysis]]
- [[wiki/cloud-infra/flow-control|Flow Control]]
