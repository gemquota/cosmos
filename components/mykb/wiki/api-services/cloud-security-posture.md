---
type: "concept"
title: "Cloud Security Posture"
description: "Continuous assessment of cloud configurations against security and compliance baselines"
tags: ["cspm", "cloud", "configuration", "compliance"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://attack.mitre.org/matrices/enterprise/cloud/"]
---

# Cloud Security Posture

- Cloud security posture management (CSPM) continuously scans cloud accounts for misconfigurations — open buckets, over-permissive IAM, exposed services.
- CSPM tools map findings to frameworks (CIS, NIST, SOC 2) and prioritize by exploitability.
- The cloud is misconfiguration-driven: most cloud incidents trace to configuration errors, not vendor flaws.
- For mykb: periodic posture scans of the hosting account should be a scheduled governance task.

## Related

- [[wiki/api-services/aws-iam|AWS IAM]] — a core posture surface
- [[wiki/api-services/azure-ad|Microsoft Entra ID]] — identity posture in Azure
- [[wiki/security-auth/compliance-frameworks|Compliance Frameworks]] — baselines CSPM checks
- [[wiki/api-services/kubernetes-security|Kubernetes Security]] — workload posture in the cloud
