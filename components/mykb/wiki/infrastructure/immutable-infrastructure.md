---
type: "concept"
title: "Immutable Infrastructure"
description: "Replacing servers instead of modifying them, so running systems are always reproducible and easy to roll back"
tags: ["immutable", "golden-images", "devops", "reproducibility", "deployment"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/immutable-infrastructure.html"]
---

# Immutable Infrastructure

## Summary
Immutable infrastructure treats servers as disposable: changes ship by replacing instances built from a known image or config, never by patching running ones. Because production state is always derivable from committed artifacts, environments become reproducible and rollback becomes a swap. It is the philosophical opposite of snowflake servers and pairs naturally with blue-green and canary deployments.

## Details
- Core rule: never modify a running server after it is provisioned — updates create a new instance from the same definition and retire the old one.
- Baking vs composing: a golden image bakes configuration into the artifact (AMI), while compose approaches build a fresh instance from code and config at launch.
- Benefits: reproducible environments (no hidden manual state), reliable rollback (repoint traffic to the previous version), and simpler debugging (known-good baseline).
- Cattle vs pets: immutable management treats instances as interchangeable members of a group rather than individually named machines.
- Trade-offs: build time and storage for images, no in-place hotfixes (emergency patches must be baked or rolled forward), and stateful data must live outside the instance.
- Relationship: Terraform and packer produce the artifacts; load balancers and deployment strategies switch traffic; configuration management is used at image-build time rather than post-boot.
- Relevance to mykb: RSIS3's agent deployments can adopt immutable releases so every run uses a pinned, reproducible environment.

## Related
- [[wiki/devops-infra/rollback-plans|Rollback Plans]] — rollback is trivial when servers are disposable
- [[wiki/infrastructure/configuration-drift|Configuration Drift]] — largely eliminated by immutability
- [[wiki/infrastructure/blue-green-deployments|Blue-Green Deployments]] — traffic-switch pattern built for immutable fleets
- [[wiki/devops-infra/terraform|Terraform]] — provisions replacement infrastructure
- [[wiki/devops-infra/kubernetes|Kubernetes]] — replaces pods instead of patching them
- [[wiki/devops-infra/feature-flags|Feature Flags]] — runtime toggle complement to image swaps
