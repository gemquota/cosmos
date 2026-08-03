---
type: "concept"
title: "Expert Systems"
description: "Classical rule-based systems encoding human expertise in a domain"
tags: ["expert-systems", "rules", "knowledge-base", "classical-ai"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Expert Systems

## Summary
Expert systems encode domain expertise as a knowledge base of rules plus an inference engine (typically forward or backward chaining) to apply them. They matter because they were the first successful applied AI and still define the knowledge-engineering trade-offs. Modern agents reuse the pattern with learned knowledge.

## Details
- Components: knowledge base, inference engine, explanation facility. The knowledge base holds facts and production rules ("IF the patient has X and Y THEN conclude Z with confidence 0.8"); the inference engine decides which rules to apply and in what order; and the explanation facility records the chain of fired rules so a user can ask "why?" and get a trace. That traceability — you can always reconstruct exactly why a conclusion was reached — is the property modern LLM agents struggle to reproduce.
- Successes: MYCIN diagnosed bacterial infections with rule-based reasoning and outperformed junior clinicians in trials; XCON configured DEC computer systems and saved the company millions; both are the canonical demonstrations that narrow, well-engineered rule systems could beat broad human judgment in a bounded domain. The lesson generalizes: expertise confined to a narrow domain with clear inputs is exactly what rule-based systems encode best.
- Limits: brittle, costly to maintain. Rules do not degrade gracefully — an input that matches no rule yields "I don't know" or a wrong default rather than a reasonable guess. Knowledge engineering is the bottleneck: interviewing experts, extracting their tacit rules, and keeping the rule base in sync with changing practice is expensive, and every domain change requires rule maintenance. MYCIN's rules took years to encode and never achieved clinical deployment for exactly this reason.
- Contrast: LLM agents trade rules for learned, flexible reasoning — broad coverage and graceful handling of novel inputs, at the cost of opacity, confabulation, and the absence of a clean explanation trace. The hybrid promise is to keep the rule layer where determinism and auditability matter and let the learned layer handle interpretation and open-ended reasoning.
- RSIS3 relevance: the RSIS3 constraint registry is an expert-system knowledge base in miniature — explicit rules the loop must obey, checkable by an inference engine; the question is how much learned judgment to admit into that layer without losing its auditability.

## Related
- [[wiki/agent-systems/action-observation-loop|Action-Observation Loop]] — rule firing in a loop
- [[wiki/concepts/production-rules|Production Rules]] — the knowledge representation
- [[wiki/concepts/forward-chaining|Forward Chaining]] — the inference engine
- [[wiki/concepts/backward-chaining|Backward Chaining]] — goal-driven inference
- [[wiki/llm-agents/expert-consultation|Expert Consultation]] — the modern specialist pattern
