---
type: "concept"
title: "Secure Enclave Inference"
description: "Running model inference inside trusted hardware enclaves that protect code and data"
tags: ["enclaves", "security", "hardware", "inference"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Secure Enclave Inference

## Summary
Running model inference inside trusted hardware enclaves that protect code and data

## Details
- Enclaves (SGX, confidential VMs) isolate computation from the host.
- Provide confidentiality for weights and queries.
- Performance overhead and attestation complexity apply.
- An alternative to encrypted inference.

## Related
- [[wiki/testing/encrypted-inference|Encrypted Inference]] — crypto alternative
- [[wiki/testing/privacy-preserving-ml|Privacy-Preserving ML]] — family
- [[wiki/testing/model-stealing-attacks|Model Stealing Attacks]] — protection target
- [[wiki/llm-agents/api-key-management-llm|API Key Management for LLMs]] — credential security
- [[wiki/agent-systems/agent-runtime-security|Agent Runtime Security]] — runtime trust
