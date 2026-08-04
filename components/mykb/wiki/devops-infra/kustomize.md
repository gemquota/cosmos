---
type: "entity"
title: "Kustomize"
description: "Native Kubernetes manifest customization via overlays without templating"
tags: ["kustomize", "kubernetes", "config", "devops", "overlays"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Kustomize

## Summary
Kustomize customizes raw Kubernetes YAML with overlays — `base` plus environment-specific patches — with no templating language. It is built into `kubectl apply -k`.

## Details
- Overlays add/merge/replace resources; common transformer uses: namespaces, image tags, labels.
- Works from plain kubectl; a lighter-weight alternative to Helm's charts.
- Pairs with GitOps: the overlay tree is the declarative source of truth.

## How Overlays Work
A `kustomization.yaml` file in a directory declares the resources that directory owns and the transformations to apply. A base directory holds a complete, environment-agnostic set of manifests; overlay directories reference one or more bases through the `resources` field and layer their own `kustomization.yaml` on top. When `kustomize build` or `kubectl apply -k` runs, the tool resolves the base, applies every patch and transformer in order, and emits a single merged YAML document. Because everything is plain files, the rendered output can be diffed, reviewed, and stored in version control like any other artifact.

## Patches and Transformers
Kustomize supports two main patch styles. Strategic merge patches are Kubernetes-aware: they merge maps and append to lists according to the resource kind's schema, which keeps small environment tweaks concise. JSON patches (RFC 6902) give exact, positional edits for cases where a merge would be ambiguous. Transformers handle the repetitive, common modifications: `commonLabels` and `commonAnnotations` stamp metadata across every resource, `namePrefix` and `nameSuffix` adjust names to prevent collisions between environments, `images` rewrites container image tags, `replicas` sets scale, and `namespace` relocates all resources into a shared namespace.

## GitOps and CI Integration
The overlay tree fits naturally into GitOps workflows: the repository is the source of truth, and a pipeline renders each overlay, validates the output, and applies it to the appropriate cluster. CI can run `kustomize build` to catch invalid YAML before it ever reaches a cluster, and pull requests can show exactly what changes per environment. Tools such as Argo CD can render overlays at sync time, keeping the cluster continuously aligned with the declared state.

## When to Choose Kustomize
Kustomize shines for Kubernetes-native projects that want plain YAML and explicit diffs without learning a templating language. Helm remains a better fit when packaging, sharing charts, or heavy value-driven configuration is needed; the two are often combined, with Helm charts feeding a base that overlays then customize per environment.

## Related
- [[wiki/devops-infra/helm|Helm]] — templating-based alternative
- [[wiki/devops-infra/kubernetes|Kubernetes]] — target platform
- [[wiki/devops-infra/github-actions|GitHub Actions]] — CI applies overlays
- [[wiki/devops-infra/terraform|Terraform]] — cluster provisioning complement
