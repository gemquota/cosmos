---
type: "concept"
title: "Cloud Security Groups"
description: "Stateful instance-level firewall rules on AWS and cloud platforms"
tags: ["security-groups", "firewall", "aws", "cloud"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Cloud Security Groups

## Summary

Cloud security groups are stateful, instance-level firewalls (AWS SG, GCP firewall rules, Azure NSGs in part) that filter traffic by port/protocol/source. They are the primary network control plane for workloads — and the top source of accidental exposure when rules drift.

## Details
- Mechanism: rules allow inbound/outbound by protocol, port, and source (CIDR, security group, or service tag); responses to allowed traffic are automatically permitted (stateful). In AWS, SGs are per-enumeration of rules with implicit deny; GCP firewall rules are hierarchical with priority; Azure NSGs use priority numbers and are subnet/NIC-scoped.
- Concrete example: an app SG allows 443 from the load-balancer SG and 22 from a bastion SG only; the database SG allows 5432 from the app SG. Using group references instead of CIDRs means adding a server to the app tier automatically inherits the rules — and removing it drops them.
- Failure modes: 0.0.0.0/0 on management ports (22, 3389, 5432) — the most common breach vector; rules referencing stale CIDRs after environments move; duplicate/conflicting rules that shadow intended policy; and drift between IaC and console edits that makes the source of truth lie.
- Operational tradeoffs: groups are cheap, stateful, and per-application — the right default filter — but they are not a substitute for identity-aware controls (IAM), network inspection (firewalls), or logging. Treat security groups as code: review diffs, minimize rule count, and use group-to-group references.
- RSIS3/mykb relevance: the wiki's environment templates encode security groups as code with a documented rule vocabulary, so loop-provisioned workloads inherit a safe baseline.
- Default posture: start with deny-all per environment and open rules only as services require; a permissive starter template is how the first exposure ships.
- Deny-by-default: delete default allow rules where the platform creates them; a fresh environment should start closed and open only what is needed.

## Related
- [[wiki/cloud-infra/cloud-providers-aws-azure-gcp|Cloud Providers: AWS, Azure, GCP]]
- [[wiki/cloud-infra/multi-cloud-hybrid-cloud|Multi-Cloud & Hybrid Cloud]]
- [[wiki/os-shell/users-groups-and-acls|Users, Groups & ACLs]]
- [[wiki/infrastructure/security-information-and-event-management|SIEM]]
