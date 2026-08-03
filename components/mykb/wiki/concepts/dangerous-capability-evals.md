---
type: "concept"
title: "Dangerous Capability Evals"
description: "Assessments of capabilities that could cause severe harm"
tags: ["dangerous", "capabilities", "evals"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Dangerous Capability Evals

## Summary
Dangerous capability evals test for skills whose misuse is severe: bioweapon synthesis, cyber offense, deception, self-replication. They measure what a model could do in the hands of a malicious or careless actor, and they are the empirical backbone of responsible scaling policies — deployment decisions are gated on measured dangerous capability, not on stated intentions.

## Details
- The eval design problem is sharp: each test item is itself a small piece of dangerous knowledge, so the eval must measure the capability without teaching it. Practical approaches include using fictional or obfuscated instantiations, gating test content behind access controls, and evaluating enabling knowledge (does the model know the relevant concepts and sequences?) rather than full end-to-end recipes. The more powerful the model, the more the eval suite itself becomes a biosecurity or cyber-security asset that must be protected.
- Scoring is not a single pass/fail: dangerous capabilities live on a gradient of uplift and synthesis. An eval might measure whether the model can produce a correct protocol given the components, whether it can correct errors in a flawed protocol, or whether it can combine pieces of knowledge into a novel dangerous procedure. The last is the hardest to test and the most important to know, because it measures the capability that no single source of training data obviously provides.
- They are the measurement backbone of responsible scaling policies: an organization declares capability thresholds (e.g., "no model above this bio-risk score deploys without additional mitigations") and the evals determine which tier a model falls into. The weakness of the approach is that evals are point-in-time samples; a model can score low today and high after fine-tuning, or the eval can miss a capability entirely, so the policy needs continuous re-evaluation alongside the gated deployment.
- RSIS3 relevance: capability gating in the bundle mirrors this idea at small scale. If an improvement loop proposes enabling an agentic mode, self-modification, or broader access, the analogous discipline is to test the proposed capability's blast radius in a sandbox before granting it — measure first, deploy second.

## Related
- [[wiki/concepts/bio-risk-evals|Bio Risk Evals]] — the bio domain
- [[wiki/concepts/cyber-risk-evals|Cyber Risk Evals]] — the cyber domain
- [[wiki/concepts/safety-evals-practice|Safety Evals Practice]] — the practice
- [[wiki/concepts/capability-classification|Capability Classification]] — the tiering
- [[wiki/concepts/responsible-scaling|Responsible Scaling]] — the full treatment of this theme
- [[wiki/testing/ai-safety-evals|Ai Safety Evals]] — existing graph context
