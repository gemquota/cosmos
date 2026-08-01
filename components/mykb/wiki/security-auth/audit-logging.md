---
type: "concept"
title: "Audit Logging"
description: "Recording security-relevant events to support accountability, detection, and forensics"
tags: ["audit", "logging", "security", "monitoring"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html"]
---

# Audit Logging

## Summary

Audit logging records security-relevant events — authentication, authorization decisions, data access, admin actions, and failures — in a tamper-evident, searchable stream. OWASP's Logging Cheat Sheet is the practical checklist for what and how to log. Audit logs matter because they are the raw material of incident detection, investigation, compliance evidence, and accountability: without them, an attacker's trail is invisible. RSIS3's memory access patterns make audit logging a core feature: every read or write to sensitive knowledge should be attributable.

## Details

- What to log: auth successes and failures, session lifecycle, access-control decisions (especially denials), data modifications, privilege changes, and system errors.
- What not to log: secrets, passwords, tokens, and full payloads of personal data — logging too much creates a liability; hash or redact.
- Integrity: append-only storage, log signing or write-once media, and separation of log transport from the application so attackers cannot erase evidence.
- Correlation: include request IDs, user IDs, session IDs, timestamps in UTC, and service names so events can be joined across components.
- Retention and privacy: retention policies must balance forensic value against data-protection duties; access to logs itself should be audited.
- For mykb, audit events should flow into the observability stack alongside metrics so security and operations share one timeline.

## Related

- [[wiki/security-auth/security-incident-monitoring|Security Incident Monitoring]] — audit logs feed detection and triage
- [[wiki/security-auth/data-classification|Data Classification]] — classified data needs stronger audit coverage
- [[wiki/security-auth/compliance-frameworks|Compliance Frameworks]] — audit evidence satisfies compliance
- [[wiki/devops-infra/observability|Observability]] — logs, metrics, and traces together
- [[wiki/memory/provenance|Provenance]] — knowledge provenance complements audit
- [[wiki/security-auth/indicators-of-compromise|Indicators of Compromise]] — log events matched against IoCs
- [[wiki/security-auth/honeypots|Honeypots]] — decoy events appear in audit logs
- [[wiki/concepts/triad-architecture|Triad Architecture]] — audit trail across triad services
