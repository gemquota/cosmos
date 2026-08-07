---
type: "concept"
title: "Obedient AI"
description: "Systems that reliably follow instructions"
tags: ["obedient", "instruction", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Obedient AI

## Summary
An obedient AI reliably follows instructions — it does what it is asked, within the boundaries set for it, without quietly substituting its own agenda. Obedience is one leg of the HHH triad and is valuable precisely because it makes systems predictable; the design problem is distinguishing faithful obedience from harmful servility.

## Details
- **Faithful execution** — obedience means carrying out the requested action as specified, including implicit intent, not just the literal tokens of the instruction.
- **Bounded obedience** — obedience operates inside constraints: harmless and helpful limits are part of the contract, so an obedient system refuses unsafe instructions rather than following them.
- **Instruction hierarchy** — obedience is structured by the instruction hierarchy: the system obeys higher-ranked sources over lower ones and refuses to let untrusted content override its programming.
- **Measurement** — obedience is evaluated with instruction-following suites that test literal compliance, implicit intent, and the handling of conflicting or adversarial instructions.
- **Failure modes** — the dangerous failures are over-obedience to malicious instructions (jailbreaks, prompt injection) and under-obedience driven by sycophancy or hedging.
- **Relationship to approval** — for consequential actions, obedience routes through approval gates: the system is obedient to the process (ask first) rather than to the raw request.
- **mykb relevance** — worker instructions in the wiki's workflow assume obedience to the brief: tasks are executed as specified and deviations are flagged rather than improvised.

- **Training implications** — obedience is partly a training property: models trained to comply with instructions generalize that compliance to instructions they should refuse, so refusal training must be layered in explicitly.

- **The shadow failure** — the subtler risk is over-obedience without understanding: a system that complies with a request that contradicts the user's actual intent. Faithful obedience therefore includes checking intent, not just tokens.

## Related
- [[wiki/agent-systems/instruction-hierarchy|Instruction Hierarchy]] — the ordering that defines what to obey
- [[wiki/agent-systems/helpful-ai|Helpful AI]] — the judgment complement
- [[wiki/agent-systems/harmless-ai|Harmless AI]] — the boundary on obedience
- [[wiki/agent-systems/hha-standards|HHH Standards]] — the bundle
- [[wiki/agent-systems/approval-based-agents|Approval-Based Agents]] — gating obedience
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — measuring compliance
