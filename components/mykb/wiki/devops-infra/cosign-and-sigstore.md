---
type: "concept"
title: "Cosign & Sigstore"
description: "Signing and verifying artifacts with keyless Sigstore flows"
tags: ["cosign", "sigstore", "signing", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Cosign & Sigstore

## Summary
Cosign and Sigstore bring software signing to the container ecosystem without key-management pain: Sigstore provides free, short-lived, ephemeral certificates via OIDC identity, and Cosign signs container images and attestations with them, then verifies signatures at deploy time. The result is provenance — proof of who built and signed an artifact.

## Details
- Mechanism: Sigstore's keyless flow — the signer authenticates via OIDC (GitHub Actions, GitLab CI), Fulcio issues a short-lived certificate bound to that identity, Rekor records the signature in a tamper-evident transparency log; Cosign attaches the signature as an image tag or OCI artifact and verification checks the certificate chain and Rekor entry.
- Concrete example: `cosign sign ghcr.io/org/app@sha256:...` in CI with the ambient GitHub OIDC token; the deploy pipeline runs `cosign verify --certificate-identity-regexp` to accept only images signed by the trusted workflow; SBOMs and SLSA attestations are attached and verified the same way.
- Failure modes: trusting any signature instead of pinning expected identity — verification must assert the certificate identity and issuer, not just validity; Rekor unavailability blocking verification (use offline verification or bundle caching); expired short-lived certificates breaking long-running pipelines; signing keys or tokens exfiltrated from CI, so keep OIDC permissions minimal and rotate frequently.
- Tradeoffs: keyless signing removes long-lived private keys — the biggest operational win — but depends on Sigstore's availability and OIDC infrastructure; self-hosted sigstore deployments trade that dependency for control; verifying everything adds pipeline steps and latency but is the only way to enforce supply-chain policy.
- Operational notes: verify at admission time (policy engines can call cosign), sign SBOMs alongside images, and monitor the transparency log for unexpected entries for your repositories.
- RSIS3 relevance: RSIS3's own builds and artifacts (generated dashboards, packaged tools) benefit from signed provenance so later loops know exactly which code produced which output.

## Related
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
