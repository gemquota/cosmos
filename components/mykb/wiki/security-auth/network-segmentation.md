---
type: "concept"
title: "Network Segmentation"
description: "Dividing networks into isolated zones to contain attacks and limit lateral movement"
tags: ["segmentation", "network", "isolation", "defense"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://en.wikipedia.org/wiki/Network_segmentation"]
---

# Network Segmentation

- Network segmentation splits the network into zones with controlled traffic between them, so one compromise does not reach everything.
- Firewalls, VLANs, and cloud security groups implement the policy; the model is 'deny by default, allow by exception'.
- Segmentation is a foundation of zero trust and makes lateral movement expensive.
- For mykb: memory stores, agent runtimes, and public APIs should live in separate zones with explicit rules.

## Related

- [[wiki/security-auth/microsegmentation|Microsegmentation]] — fine-grained per-workload segmentation
- [[wiki/security/zero-trust|Zero Trust Architecture]] — segmentation inside zero trust
- [[wiki/security-auth/lateral-movement|Lateral Movement]] — the attack segmentation blocks
- [[wiki/api-services/kubernetes-security|Kubernetes Security]] — network policies as segmentation
- [[wiki/security-auth/least-privilege|Least Privilege]] — segmentation is least privilege at the network layer
