---
type: "concept"
title: "Agent Templates"
description: "Reusable blueprints defining agent roles, tools, and workflows"
tags: ["agent-templates", "agents", "templates", "reuse"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Agent Templates

## Summary
Agent templates are reusable blueprints that define an agent's role, tools, and workflow structure in one place. They matter because they make agent construction repeatable, testable, and auditable instead of ad hoc. Templates are the unit of standardization for fleets of agents. Templates also encode organizational memory: each one captures how a role should behave.

## Details
- **Definition** — a template packages the system prompt, tool allowlist, memory configuration, and loop structure that define how an agent behaves.
- **Structure** — a good template declares the agent's goal, constraints, available tools, escalation path, and success criteria so every instance behaves predictably.
- **Reuse** — templates eliminate duplicated prompt text and configuration, so fixes propagate to every agent built from them.
- **Variants** — templates range from role templates (one job description) to full workflow templates (a pipeline of stages with handoffs).
- **Versioning** — templates need version control and change review because editing a template silently changes every downstream agent.
- **Testing** — template quality is tested with representative tasks and golden-test-sets before the template is released to a fleet.
- **Worked example** — an organization defines a support-agent template once, then each product team instantiates it with product-specific knowledge and tone.
- **Failure modes** — templates that are too rigid fight legitimate variation, while templates that are too loose fail to standardize anything.
- **Consumers** — agent-factories instantiate templates at scale, and agent-pipelines compose them into multi-stage flows.
- **Practical relevance** — templates are the foundation of governance for agent fleets, tying every running agent back to a reviewed source.
- **Parameterization** — templates expose a small number of tuned parameters, such as knowledge base and tone, to keep instances varied but controlled.
- **Lifecycle** — template changes go through review, deprecation, and migration so instances do not silently fork.
- **Metrics** — tracking per-template success rates shows which blueprints are healthy and which need revision.

## Related
- [[wiki/agent-systems/agent-factories|Agent Factories]] — the machinery that instantiates templates
- [[wiki/prompt-engineering/prompt-templates|Prompt Templates]] — the prompt layer inside a template
- [[wiki/llm-agents/agent-versioning|Agent Versioning]] — versioning templates and their instances
- [[wiki/agent-systems/agent-pipelines|Agent Pipelines]] — assembling templates into workflows
- [[wiki/agent-systems/tool-selection-policies|Tool Selection Policies]] — defining the tool surface a template allows
