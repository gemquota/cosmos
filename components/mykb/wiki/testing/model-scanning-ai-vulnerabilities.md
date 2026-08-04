---
type: "concept"
title: "Model Vulnerability Scanning"
description: "Automated scanning of models and artifacts for known vulnerabilities"
timestamp: "2026-08-02T00:00:00Z"
---
tags: ["model-scanning", "security", "scanning", "models", "supply-chain"]
status: "growing"

# Model Vulnerability Scanning

## Summary
Model vulnerability scanning automatically checks models and their artifacts for known vulnerabilities before deployment. It matters because model files, runtimes, and dependencies carry the same supply-chain risks as traditional software. Scanning catches problems that manual review misses, at the speed automation provides.

## Details
- **Definition** — scanners inspect model formats, serialized weights, runtimes, and dependency manifests for known vulnerabilities and malicious payloads.
- **CVE correlation** — dependencies and runtime libraries are matched against vulnerability databases to flag known issues.
- **Malicious payloads** — serialized weights can hide code execution paths; scanners look for suspicious structures and embedded objects.
- **Integrity** — hashes and signatures verify that artifacts match their declared provenance.
- **Pipeline integration** — scans run in CI and block deployment on findings, making security a gate rather than an afterthought.
- **Complementarity** — scanning handles known risks while red-team processes handle unknown, behavioral threats.
- **Common failure modes** — scanning only the model and missing the runtime, ignoring the CVE database staleness, and findings without owners.
- **Worked example** — a CI pipeline scans every model artifact, flags a vulnerable ONNX runtime version, and the team upgrades before the model reaches production.
- **Practical relevance** — automated scanning operationalizes supply-chain hygiene for machine learning artifacts.

- **Formats** — scanners must understand model file formats deeply, since serialization is where hidden payloads live.
- **Signatures** — signed artifacts paired with verification prevent substitution during distribution.
- **Remediation workflow** — findings need owners, deadlines, and verification so scans change outcomes.
- **Baselines** — comparing scan results across releases shows whether the risk profile is improving.- **Shift-left** — running scans at CI time makes model supply-chain risk a developer concern rather than a release surprise.

## Related
- [[wiki/testing/sbom-for-models|SBOMs for Models]] — inventory input
- [[wiki/testing/dependency-pinning-models|Dependency Pinning for Models]] — remediation
- [[wiki/testing/supply-chain-llm-deps|Supply Chain for LLM Dependencies]] — risk family
- [[wiki/ai-ml/llmops-ci-cd|LLMOps CI/CD]] — pipeline gate
- [[wiki/testing/model-poisoning|Model Poisoning]] — target threat
- [[wiki/testing/vulnerability-scanning|Vulnerability Scanning]] — general practice
