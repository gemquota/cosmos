---
type: "concept"
title: "Attribute-Based Access Control"
description: "Authorization that evaluates subject, resource, action, and environment attributes against policies"
tags: ["abac", "authorization", "policy", "nist"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://csrc.nist.gov/pubs/sp/800/162/final"]
---

# Attribute-Based Access Control

## Summary

Attribute-based access control (ABAC) decides access by evaluating attributes of the subject, resource, action, and environment against a policy — for example, 'allow read if subject.department == resource.owner.department and time is business hours'. NIST SP 800-162 is the defining guide. ABAC matters because policies can express dynamic, contextual conditions that static role assignments cannot, enabling fine-grained and data-aware authorization. For RSIS3, ABAC is the model for controlling access to sensitive knowledge: policy can depend on who asks, which memory is touched, and under what circumstances.

## Details

- Attribute classes: subject attributes (role, clearance, department), resource attributes (classification, owner), action attributes (read, write, delete), and environment attributes (time, network, risk score).
- Architecture: the policy enforcement point (PEP) intercepts requests and asks the policy decision point (PDP), which evaluates policies against attributes from the policy information point (PIP).
- Policy languages: XACML is the OASIS standard for ABAC policies; JSON-based and cloud-native policy engines (e.g. OPA/Rego, AWS Cedar) are common alternatives.
- Relationship to RBAC: roles become one attribute among many; many deployments layer ABAC on top of RBAC for coarse-to-fine enforcement.
- Design risks: attribute sprawl, inconsistent attribute naming, and the need for authoritative attribute sources (directories, classifications).
- For mykb, attribute names should be governed in one schema so that data-classification labels and identity attributes compose in policies.

## Related

- [[wiki/security-auth/role-based-access-control|Role-Based Access Control]] — the static model ABAC extends
- [[wiki/security-auth/least-privilege|Least Privilege]] — ABAC policies implement least privilege dynamically
- [[wiki/security-auth/data-classification|Data Classification]] — resource attributes that feed policies
- [[wiki/security/abac|ABAC]] — existing article on ABAC
- [[wiki/api-services/aws-iam|AWS IAM]] — cloud IAM policies as ABAC
- [[wiki/api-services/gcp-iam|GCP IAM]] — condition-based IAM policies
- [[wiki/security/zero-trust|Zero Trust Architecture]] — per-request policy evaluation
- [[wiki/security/rbac|RBAC]] — coarse-grained baseline under ABAC
- [[wiki/concepts/triad-architecture|Triad Architecture]] — policy decisions at the memory boundary
