---
type: "concept"
title: "Supply Chain Attestations"
description: "Verified metadata about how artifacts were built and shipped"
tags: ["attestation", "supply-chain", "security", "sigstore"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Supply Chain Attestations

## Summary
Supply-chain attestations are signed statements about an artifact — who built it, from what source, with which settings, and what it contains. Built on in-toto and Sigstore, they turn bare signatures into a verifiable chain: a signature proves the signer, an attestation proves claims about the artifact that an automated policy can check before deploy.

## Details
- Mechanism: in-toto defines attestation predicates (SLSA provenance, SPDX SBOM, test results, vulnerability scan results); Sigstore signs them with keyless certificates; attestations attach to images (cosign attach) or registries; verifiers check signatures and evaluate attestation contents against policy (expected builder, source repo, scan status).
- Concrete example: CI builds an image, runs tests, scans for vulnerabilities, and signs a SLSA provenance attestation recording the builder ID, commit, and build command; the deploy admission policy requires a valid attestation from the trusted workflow with no critical vulnerabilities; a compromised registry cannot inject an image that satisfies the policy.
- Failure modes: attestations signed but never verified (the signature is theater); policies that check the attestation exists but not its contents; attestations that are stale — describing an old build after the artifact changed; builder identity confusion where any workflow can claim the trusted builder ID; storing attestations separately from artifacts so they are lost in migration.
- Tradeoffs: attestations add pipeline complexity and storage but give deploy-time, machine-checkable provenance — the strongest supply-chain control available; the alternative, trusting the registry or the pipeline implicitly, fails at compromise time; the maturity path is sign, attach, verify at admission, and audit.
- Operational notes: verify at admission, keep attestations with the artifact, and monitor for unexpected attestations on your repositories.
- Witness model: attestations are meaningful only when the builder is independently trusted — an attestation signed on a developer's own machine proves little about where the artifact came from.
- RSIS3 relevance: cosmos artifacts with attestations let RSIS3 loops verify that a dashboard bundle or daemon build came from the trusted pipeline before deployment.

## Related
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
