---
type: "concept"
title: "Safety Case Approach"
description: "Structuring safety justification as explicit cases"
tags: ["safety-case", "assurance", "safety"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Safety Case Approach

## Summary
The safety case approach documents, in an explicit argument structure, why a system is safe enough to deploy: claims, evidence, and reasoning. Instead of asserting "it is safe" as a conclusion, it forces the assertion to be built from sub-claims, each supported by evidence and connected by reasoning — so the safety argument can be reviewed, challenged, and repaired where it is weakest.

## Details
- The safety case approach documents, in an explicit argument structure, why a system is safe enough to deploy: claims, evidence, and reasoning. The canonical shape is a goal tree: the top goal ("the system is safe to deploy for the stated use") decomposes into sub-goals (no unauthorized data access, no harmful outputs, graceful failure), each supported by evidence (test results, design documents, monitoring data) and an argument connecting them.
- It borrows from aerospace and nuclear engineering, where the cost of failure is extreme and regulators require the argument to be explicit before operation begins. Those industries developed the assurance-case discipline that AI safety is now adapting: the case is a living artifact, updated when the system or its environment changes.
- Good cases surface assumptions and make disagreement tractable. Every argument step rests on assumptions (the threat model, the operating envelope, the reliability of evidence); writing them down turns hidden disagreement into reviewable points — "the case assumes the sandbox cannot be escaped" is a claim reviewers can attack directly.
- Concrete example: a claim "the model refuses disallowed requests" decomposes into evidence (eval results on a refusal suite), argument (the suite covers the disallowed categories), and an assumption (adversarial users will not find a bypass); a review that finds the suite omits a category forces the case to change — the safety case turns the omission into a visible gap instead of a hidden one.
- Failure modes: evidence that is asserted but not produced; arguments that are post-hoc rationalizations of a system that was never designed for safety; cases that go stale after the system changes; and cases that are so vague ("we follow best practices") that no claim can be checked.
- Tradeoffs: explicit cases cost time and rigor that feel disproportionate for low-risk systems, but they pay back at review time — the argument is inspectable, and a disagreement about safety becomes a disagreement about a specific claim and its evidence.
- RSIS3 relevance: pass verification artifacts are a small safety case for the bundle — each pass's checks, results, and assumptions form the evidence and reasoning that the next pass uses to decide whether the change is safe to keep.

## Related
- [[wiki/syntheses/assurance-cases|Assurance Cases]] — the formal sibling
- [[wiki/syntheses/audit-frameworks-ai|AI Audit Frameworks]] — the external layer
- [[wiki/concepts/dangerous-capability-evals|Dangerous Capability Evals]] — the evidence
- [[wiki/concepts/responsible-scaling|Responsible Scaling]] — the policy frame
- [[wiki/testing/ai-safety-evals|Ai Safety Evals]] — existing graph context
