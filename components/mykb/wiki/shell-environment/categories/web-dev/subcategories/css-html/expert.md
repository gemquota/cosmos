---
type: "entity"
title: "Expert"
timestamp: "2026-07-19T22:41:42Z"
resource: ""
---
description: "Encapsulating deep domain knowledge so agents can consult specialized capability"
tags: ["entity", "bash", "bootstrap", "bun", "ide", "json", "experts", "domains"]

# Expert

## Summary
An expert, in agent terms, is a specialized component or persona that holds deep knowledge of one domain and can be consulted when that domain is in scope. It matters because general agents are adequate at everything and excellent at nothing. Routing work to experts combines broad orchestration with deep, reliable knowledge in each domain.

## Details
- **Definition** — an expert encapsulates domain knowledge, procedures, and vocabulary for a specific area, such as security, databases, or legal review.
- **Consultation** — an orchestrator calls on the expert when the task's domain matches, keeping general context lean.
- **Persona and style** — experts often carry a distinct tone and methodology that matches their field's norms.
- **Knowledge packaging** — rules, checklists, and references are stored so the expert's advice is grounded, not generic.
- **Composition** — multiple experts can cooperate, each handling its slice, coordinated by a router or blackboard.
- **Quality bar** — an expert's value comes from precision; it should decline out-of-domain questions rather than improvise.
- **Common failure modes** — experts that drift into general answers, routers that misroute domains, and overlapping experts that contradict each other.
- **Worked example** — a security expert reviews a proposed change against an attack checklist, while a database expert separately reviews the schema migration.
- **Practical relevance** — the expert pattern scales capability by partitioning knowledge instead of accumulating it in one context.

- **Grounding** — experts should cite or link their sources so advice can be verified, not just asserted.
- **Escalation** — when certainty is low, an expert should say so and escalate rather than fabricate confidence.
- **Retention** — expert knowledge should be reviewed and updated as the domain evolves.
## Related
- [[wiki/agent-systems/research-agents|Research Agents]] — knowledge-gathering experts
- [[wiki/agent-systems/ai-researcher-agents|AI Researcher Agents]] — research specialization
- [[wiki/llm-agents/expert-consultation|Expert Consultation]] — consulting pattern
- [[wiki/agent-systems/blackboard-architecture|Blackboard Architecture]] — expert coordination
- [[wiki/llm-agents/agent-personas|Agent Personas]] — role definition
- [[wiki/agent-systems/agent-ensembling|Agent Ensembling]] — combining specialists
