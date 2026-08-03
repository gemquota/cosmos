---
type: "concept"
title: "Security Group Best Practices"
description: "Least-privilege rules, tagging, and audit habits for security groups"
tags: ["security-groups", "best-practices", "firewall", "aws"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Security Group Best Practices

## Summary

Security group best practices turn the most misconfigured control in cloud networking into a dependable boundary: least privilege, group-to-group references, code-based management, and continuous verification. Most cloud breaches trace back to a stray 0.0.0.0/0 rule.

## Details
- Mechanism: define groups per role (web, app, db, bastion), allow only required ports, reference other groups instead of IPs where possible, keep rules minimal, and manage them as code (Terraform/CDK) with review; use prefix lists for shared ranges and NACLs as a coarse second layer; audit with tools that detect broad exposure.
- Concrete example: the web SG allows 443 from 0.0.0.0/0 (necessary) but 22 only from the bastion SG; the DB SG allows 5432 only from the app SG; a compliance scan flags any management port open to the world and fails CI. The drift pattern is console edits bypassing code review.
- Failure modes: ephemeral "just for debugging" rules that become permanent; security groups referenced by IP instead of group ID (drift when instances change); duplicate groups with near-identical rules; and rules that allow more than the port needs (0-65535 shortcuts).
- Operational tradeoffs: group references give automatic propagation but hide dependencies (deleting a group breaks rules — check references); code management adds process but makes exposure reviewable. The standard is defense in depth: SG per role + NACL baseline + flow-log alerts on unexpected egress.
- RSIS3/mykb relevance: the wiki's environment templates would encode security groups as code with a rule vocabulary; this note is the review checklist the loop would run before merging network changes.
- Review cadence: run an exposure scan on a schedule and treat any new 0.0.0.0/0 rule on a management port as a review event; drift is the threat, not the initial config.
- Naming: name groups by role and environment (web-prod, db-prod) so reviews read intent; unnamed or generically-named groups are unreviewable.

## Related
- [[wiki/devops-infra/ci-cd-best-practices|CI/CD Best Practices]]
- [[wiki/devops-infra/on-call-practices|On-Call Practices]]
- [[wiki/infrastructure/security-information-and-event-management|SIEM]]
- [[wiki/cloud-infra/cloud-security-groups|Cloud Security Groups]]
