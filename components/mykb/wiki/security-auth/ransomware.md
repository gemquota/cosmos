---
type: "concept"
title: "Ransomware"
description: "Malware that encrypts data and extorts payment for recovery"
tags: ["ransomware", "malware", "extortion", "defense"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://www.cisa.gov/stopransomware"]
---

# Ransomware

- Ransomware encrypts or exfiltrates data and demands payment; modern variants combine encryption with data theft for double extortion.
- CISA guidance: back up and test restores, patch aggressively, enforce MFA, and segment networks.
- Response: isolate infected systems, preserve evidence, involve authorities, and weigh payment risks (no guarantee of recovery).
- For mykb: tested, offline backups and least-privilege access are the decisive defenses.

## Related

- [[wiki/security-auth/data-exfiltration|Data Exfiltration]] — double-extortion exfiltrates before encrypting
- [[wiki/devops-infra/backups|Backups]] — recovery without paying
- [[wiki/security-auth/patch-management|Patch Management]] — closing ransomware entry points
- [[wiki/security-auth/data-breach-response|Data Breach Response]] — the response playbook
- [[wiki/security-auth/security-incident-monitoring|Security Incident Monitoring]] — detecting ransomware activity
