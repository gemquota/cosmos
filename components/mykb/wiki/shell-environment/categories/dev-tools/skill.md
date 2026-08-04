---
type: "entity"
title: "Skill"
resource: ""
---
description: "A packaged, reusable capability that an agent can load and apply on demand"
tags: ["entity", "bash", "bootstrap", "bun", "ide", "json", "skills", "agents"]
timestamp: "2026-07-19T22:41:42Z"

# Skill

## Summary
A skill is a packaged, reusable capability an agent can load on demand: instructions, references, and scripts bundled under one name. It matters because agents perform better when knowledge is retrieved when needed rather than crammed into every context. Skills make expertise modular, versionable, and shareable across sessions and projects.

## Details
- **Definition** — a skill bundles a description, instructions, and supporting files that an agent activates when a task matches.
- **Discovery** — a skill's description tells the agent when to use it, so accurate summaries determine adoption.
- **Progressive disclosure** — details live in referenced files and load only when relevant, keeping the active context small.
- **Reusability** — well-crafted skills transfer across projects and sessions, encoding hard-won procedures once.
- **Versioning** — skills change as practices evolve; versioned updates keep agents on the current method.
- **Maintenance** — a skill is a small codebase: it needs tests, examples, and periodic review to stay correct.
- **Common failure modes** — vague descriptions that never trigger, bloated skills that defeat progressive disclosure, and skills that drift from current practice.
- **Worked example** — a deployment skill contains its checklist, commands, and rollback script; an agent loads it when a deploy task appears and follows the packaged procedure.
- **Practical relevance** — skills are how agent workflows encode expertise into repeatable, inspectable capability.

- **Granularity** — a skill should cover one coherent capability; oversized skills become hard to maintain and load.
- **Activation** — the trigger description should be precise so the skill loads for the right tasks and not others.
- **Observability** — logging which skills load and when helps tune descriptions and spot misfires.
## Related
- [[wiki/agent-systems/skill-acquisition-loops|Skill Acquisition Loops]] — building skills over time
- [[wiki/agent-systems/agent-templates|Agent Templates]] — reusable agent scaffolds
- [[wiki/agent-systems/agent-bootstrapping|Agent Bootstrapping]] — loading capabilities
- [[wiki/llm-agents/agent-personas|Agent Personas]] — role packaging
- [[wiki/prompt-engineering/categories/patterns/subcategories/prompt-techniques/system-instructions|System Instructions]] — instruction packaging
- [[wiki/agent-systems/agent-factories|Agent Factories]] — producing skill-holding agents
