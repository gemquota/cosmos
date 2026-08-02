---
type: "concept"
title: "Model Vulnerability Scanning"
description: "Automated scanning of models and artifacts for known vulnerabilities"
tags: ["model-scanning", "security", "scanning", "models"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Model Vulnerability Scanning

## Summary
Automated scanning of models and artifacts for known vulnerabilities

## Details
- Check model formats, runtimes, and dependencies for CVEs.
- Scan for malicious payloads in serialized weights.
- Integrate into CI before deployment.
- Complement red-team-processes.

## Related
- [[wiki/testing/sbom-for-models|SBOMs for Models]] — inventory input
- [[wiki/testing/dependency-pinning-models|Dependency Pinning for Models]] — remediation
- [[wiki/testing/supply-chain-llm-deps|Supply Chain for LLM Dependencies]] — risk family
- [[wiki/ai-ml/llmops-ci-cd|LLMOps CI/CD]] — pipeline gate
- [[wiki/testing/model-poisoning|Model Poisoning]] — target threat
