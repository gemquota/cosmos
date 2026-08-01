---
type: "concept"
title: "Kustomize"
description: "Native Kubernetes manifest customization via overlays without templating"
tags: ["kustomize", "kubernetes", "config", "devops", "overlays"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Kustomize

## Summary
Kustomize customizes raw Kubernetes YAML with overlays — `base` plus environment-specific patches — with no templating language. It is built into `kubectl apply -k`.

## Details
- Overlays add/merge/replace resources; common transformer uses: namespaces, image tags, labels.
- Works from plain kubectl; a lighter-weight alternative to Helm's charts.
- Pairs with GitOps: the overlay tree is the declarative source of truth.

## Related
- [[wiki/devops-infra/helm|Helm]] — templating-based alternative
- [[wiki/devops-infra/kubernetes|Kubernetes]] — target platform
- [[wiki/devops-infra/github-actions|GitHub Actions]] — CI applies overlays
- [[wiki/devops-infra/terraform|Terraform]] — cluster provisioning complement
