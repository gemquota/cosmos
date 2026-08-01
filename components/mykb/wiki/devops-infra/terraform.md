---
type: "concept"
title: "Terraform"
description: "Declarative infrastructure-as-code tool for provisioning cloud resources reproducibly"
tags: ["terraform", "iac", "devops", "cloud", "infrastructure"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://developer.hashicorp.com/terraform/docs"]
---

# Terraform

## Summary
Terraform is a declarative infrastructure-as-code (IaC) tool that defines cloud resources in HashiCorp Configuration Language (HCL) and provisions them through provider APIs. State tracks real-world resources, enabling plan/apply workflows, drift detection, and destruction. It is the de facto standard for multi-cloud infrastructure automation.

## Details
- Core loop: `init` (providers/modules), `plan` (diff against state), `apply` (execute changes), `destroy` (tear down); every change is reviewed before execution.
- State: `terraform.tfstate` records mappings; remote backends (S3, Terraform Cloud) enable team locking and history.
- Providers: AWS, GCP, Azure, Kubernetes, and hundreds more expose resources as typed HCL blocks; modules package reusable patterns.
- HCL features: variables, outputs, data sources, `for_each`, and dependencies make environments parameterizable (staging vs production).
- Best practices: pin provider versions, use workspaces or per-env directories, run plan in CI (GitHub Actions) and apply with review.
- Worked example: a cosmos deploy could define the dashboard's static hosting bucket, CDN, and DNS as Terraform, so the gemquota.github.io redirect stack is reproducible and auditable.
- Alternatives: AWS CDK/CloudFormation, Pulumi (general-purpose languages), Ansible (config management, not provisioning).

## Related
- [[wiki/devops-infra/github-actions|GitHub Actions]] — CI gate for plan/apply
- [[wiki/devops-infra/cloudflare|Cloudflare]] — DNS/CDN resources managed by providers
- [[wiki/security/secrets-management|Secrets Management]] — state and vars hold sensitive values
- [[wiki/security/sbom|SBOM]] — infrastructure dependencies need inventorying too
- [[wiki/frontend/static-site-generation|Static Site Generation]] — output hosted by provisioned buckets
- [[wiki/concepts/mykb-implementation-report|Mykb Implementation Report]] — deployment notes for the bundle
- [[wiki/frontend/aws-s3|AWS S3]] — buckets and state backends provisioned as code
- [[wiki/ops/gap-report|Gap Analysis Report]] — infrastructure gaps tracked
