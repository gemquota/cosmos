---
type: "concept"
title: "Indicators of Compromise"
description: "Observable artifacts \u2014 hashes, IPs, domains \u2014 that suggest an intrusion"
tags: ["ioc", "detection", "forensics", "indicators"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://en.wikipedia.org/wiki/Indicator_of_compromise"]
---

# Indicators of Compromise

- Indicators of compromise (IoC) are observable data points — file hashes, domains, IPs, registry keys, behaviors — tied to known intrusions.
- IoC matching is fast and automatable but brittle: adversaries change hashes and infrastructure quickly.
- They work best combined with behavioral detection and ATT&CK technique mapping.
- For mykb: IoC lists can enrich audit-log correlation with minimal infrastructure.

## Related

- [[wiki/security-auth/threat-intelligence|Threat Intelligence]] — the source of fresh IoCs
- [[wiki/security-auth/security-incident-monitoring|Security Incident Monitoring]] — matching IoCs against telemetry
- [[wiki/security-auth/mitre-attack-framework|MITRE ATT&CK Framework]] — technique-level context for IoCs
- [[wiki/security-auth/honeypots|Honeypots]] — generating novel IoCs
