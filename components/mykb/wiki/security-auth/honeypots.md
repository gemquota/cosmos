---
type: "concept"
title: "Honeypots"
description: "Decoy systems and credentials designed to attract and reveal attackers"
tags: ["honeypots", "deception", "detection", "defense"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://en.wikipedia.org/wiki/Honeypot_(computing)"]
---

# Honeypots

- Honeypots are fake assets — servers, services, files, credentials — that real users never touch, so any interaction signals an attacker.
- They generate high-fidelity alerts and capture attacker tools and techniques.
- Costs: maintenance, risk of being used as a pivot, and the operational noise of keeping decoys realistic.
- For mykb: a honeytoken (fake memory file) could detect unauthorized reads of the knowledge graph.

## Related

- [[wiki/security-auth/indicators-of-compromise|Indicators of Compromise]] — honeypots produce fresh IoCs
- [[wiki/security-auth/security-incident-monitoring|Security Incident Monitoring]] — honeypot alerts into triage
- [[wiki/security-auth/lateral-movement|Lateral Movement]] — honeypots reveal movement
- [[wiki/security/zero-trust|Zero Trust Architecture]] — deception as a zero-trust layer
