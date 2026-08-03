---
type: "concept"
title: "Image Signing & Notary"
description: "Cryptographic signatures that authenticate container images"
tags: ["image-signing", "notary", "containers", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Image Signing & Notary

## Summary
Image signing cryptographically binds a container image to its builder so consumers can verify provenance before running it; Notary (and its successor Notation) provides the trust infrastructure — signing keys, trust policies, and signature storage. Signing turns a pull-whatever-the-registry-says policy into a pull-only-what-we-signed policy.

## Details
- Mechanism: a signer creates a signature over the image digest with a private key (or an ephemeral keyless cert via Sigstore); signatures are stored in the registry (tags, OCI artifacts, or Notary's TUF metadata) and fetched with the image; verifiers check the signature against trust policy — who may sign, which keys, which repositories; deployments reject unsigned or wrongly-signed images.
- Concrete example: CI signs every build with a code-signing key (or Sigstore keyless flow); the cluster's admission policy requires a valid signature from the trusted workflow for the prod namespace; a compromise of the registry still cannot inject an unsigned image.
- Failure modes: trust-policy gaps — verifying a signature without pinning the expected signer identity; key management failure (lost keys, exposed keys) — the private key is the crown jewel and needs HSM or short-lived keyless certificates; signature verification only at build time, not at deploy time; Notary/TUF metadata staleness breaking pulls; images signed by one team run in another team's namespace because policy is too broad.
- Tradeoffs: signing adds pipeline and admission complexity but provides the supply-chain guarantee that hashes alone cannot (anyone can compute a hash; only the key holder can sign); the tradeoff is operational — key custody, signature storage, and policy review; keyless Sigstore reduces key management at the cost of trusting the transparency log and OIDC infra.
- Operational notes: sign in CI, verify at admission, pin expected identities in trust policy, and rotate signing keys on a schedule.
- RSIS3 relevance: signed cosmos artifacts (dashboard bundles, packaged tools) let RSIS3 loops verify provenance — later loops know which code produced which output.

## Related
- [[wiki/devops-infra/trivy-and-image-scanning|Trivy & Image Scanning]] — related coverage in the same cluster
- [[wiki/devops-infra/package-signing-and-repositories|Package Signing & Repositories]] — related coverage in the same cluster
- [[wiki/infrastructure/docker-image-optimization|Docker Image Optimization]] — related coverage in the same cluster
- [[wiki/devops-infra/golden-images-and-image-baking|Golden Images & Image Baking]] — related coverage in the same cluster
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/devops-infra/observability-pillars|Observability Pillars]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
