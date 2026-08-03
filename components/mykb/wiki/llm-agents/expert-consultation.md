---
type: "concept"
title: "Expert Consultation"
description: "Querying specialized agents or tools on demand for domain knowledge"
tags: ["expert-consultation", "multi-agent", "specialists", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# Expert Consultation

## Summary

Expert consultation lets an agent invoke a specialist — a domain model, a specialized tool, another agent, or a curated knowledge source — when a task exceeds its general competence. It is retrieval and delegation applied to the agent itself.

## Details
- Mechanism: the agent recognizes a consultation trigger (unfamiliar domain, high-stakes decision, uncertain recall), then queries an expert: a fine-tuned/specialized model, a knowledge base (RAG over expert docs), a tool with domain logic, or a peer agent; the response is synthesized into the agent's reasoning with provenance; consultation decisions are logged.
- Concrete example: a generalist writing infrastructure notes consults the wiki's cloud-infra cluster for accuracy; a coding agent routes a security question to a hardened expert model or a policy document; a math-heavy step calls a symbolic tool instead of trusting the model's arithmetic. The failure pattern: the agent never consults (overconfident) or consults everything (slow, expensive, and shallow).
- Failure modes: expert answers taken without skepticism (experts can be wrong — keep provenance and verify); consultation routing that picks the wrong expert; context bloat from pulling whole knowledge bases; and echo chambers where the "expert" is the same model with a different prompt.
- Operational tradeoffs: consultation trades latency and cost for accuracy and grounding; the discipline is trigger rules (when to consult), bounded context (specific documents, not corpora), and recording which consultation shaped which decision for audit.
- RSIS3/mykb relevance: the wiki's acquisition loop consults the OKF clusters before writing syntheses, and the consultation trail is preserved in the session log.
- Provenance: record which expert was consulted, what was taken, and what was overridden; unsourced expert input is indistinguishable from hallucination in audit.
- Cost control: cap consultation size (retrieve the top-k relevant sections, not the whole corpus) and budget consultations per run so they do not dominate spend.

## Related
- [[wiki/agent-systems/sub-agent-delegation|Sub-Agent Delegation]] — consultation as delegation
- [[wiki/llm-agents/debate-agents|Debate Agents]] — the adversarial variant
- [[wiki/agent-systems/multi-agent-orchestration|Multi-Agent Orchestration]] — the coordination pattern
- [[wiki/concepts/expert-systems|Expert Systems]] — the classical specialist
- [[wiki/concepts/metacognition|Metacognition]] — knowing when to consult
