---
type: "concept"
title: "Kill Chain"
description: "Stage model of an attack from reconnaissance to actions on objectives"
tags: ["kill-chain", "cyber", "model", "defense"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html"]
---

# Kill Chain

- Lockheed Martin's cyber kill chain models intrusions as stages: reconnaissance, weaponization, delivery, exploitation, installation, command-and-control, actions on objectives.
- Disrupting any stage breaks the chain, which guides layered defenses and detection timing.
- Criticisms: it is intrusion-centric and underplays insider and cloud-native paths; ATT&CK complements it.
- For mykb: mapping defenses to chain stages shows where detection gaps concentrate.

## Related

- [[wiki/security-auth/mitre-attack-framework|MITRE ATT&CK Framework]] — the richer modern taxonomy
- [[wiki/security-auth/security-incident-monitoring|Security Incident Monitoring]] — detection across stages
- [[wiki/security-auth/lateral-movement|Lateral Movement]] — a mid-chain stage
- [[wiki/security-auth/data-exfiltration|Data Exfiltration]] — the final-stage objective
