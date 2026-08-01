---
type: "concept"
title: "Endpoint Security"
description: "Protecting devices \u2014 laptops, servers, mobiles \u2014 from malware and misuse"
tags: ["endpoint", "edr", "malware", "defense"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://en.wikipedia.org/wiki/Endpoint_security"]
---

# Endpoint Security

- Endpoint security protects end-user and server devices with antivirus, EDR behavior detection, firewalls, and patch management.
- Modern EDR detects attacker behavior (process injection, credential access) rather than only signatures.
- Endpoints are the most exposed part of the estate because they hold credentials and run user code.
- For mykb: endpoint telemetry on the machines that run agents feeds both risk scoring and incident detection.

## Related

- [[wiki/security-auth/patch-management|Patch Management]] — keeping endpoint software current
- [[wiki/security-auth/malware-analysis|Malware Analysis]] — understanding what EDR catches
- [[wiki/security-auth/security-incident-monitoring|Security Incident Monitoring]] — EDR events into the SOC pipeline
- [[wiki/security-auth/mdm|Mobile Device Management]] — mobile endpoint control
