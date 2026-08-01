---
type: "concept"
title: "Data Exfiltration"
description: "Unauthorized transfer of data out of an environment"
tags: ["exfiltration", "attacks", "mitre", "dlp"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://attack.mitre.org/tactics/TA0010/"]
---

# Data Exfiltration

- Data exfiltration (ATT&CK TA0010) is the final objective of many intrusions: copying sensitive data out via network, media, or cloud services.
- Detection: unexpected egress volumes, unusual API calls, DNS tunneling, and large downloads by non-bulk roles.
- Prevention: egress filtering, DLP, encryption of data at rest, and least privilege on data access.
- For mykb: the memory graph is the crown jewel, so egress monitoring of retrieval APIs is essential.

## Related

- [[wiki/security-auth/security-incident-monitoring|Security Incident Monitoring]] — detecting exfiltration patterns
- [[wiki/security-auth/data-classification|Data Classification]] — knowing which data matters most
- [[wiki/security-auth/least-privilege|Least Privilege]] — limiting who can bulk-read
- [[wiki/security-auth/network-segmentation|Network Segmentation]] — egress controls
