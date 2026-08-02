---
type: "concept"
title: "Log Retention"
description: "Policies for how long logs are kept, where, and in what form"
tags: ["logging", "retention", "compliance", "cost"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Log Retention

## Summary
Log retention policies define how long logs live in hot storage, warm archives, and cold compliance stores. Retention is a cost-and-compliance decision, not just a disk setting.

## Details
- Hot searchable logs are expensive; move old logs to object storage and keep cheap indexes.
- Compliance and audit needs (Sarbanes-Oxley, GDPR evidence) may force longer retention than debugging needs.
- Define retention per log class — security events long, debug logs short — and document the policy.
- mykb relevance: agent audits need longer retention than interactive session logs.

## Related
- [[wiki/dev-tools/log-rotation|Log Rotation]]
- [[wiki/dev-tools/log-aggregators|Log Aggregators]]
- [[wiki/dev-tools/centralized-logging|Centralized Logging]]
- [[wiki/cloud-infra/data-archiving|Data Archiving]]
- [[wiki/dev-tools/structured-logs|Structured Logs]]
