---
type: "entity"
title: "NarrativeIdentity"
resource: ""
---
description: "The self-story an agent maintains about its history, role, and continuity"
tags: ["android", "api", "ast", "auth", "authentication", "bigquery", "entity", "identity", "agents"]
timestamp: "2026-07-19T22:41:43Z"

# NarrativeIdentity

## Summary
Narrative identity is the coherent self-story an agent maintains about who it is, what it has done, and why it acts. It matters because continuity and trust depend on an agent that remembers its role and history across sessions. A deliberate narrative keeps behavior consistent without drifting into false self-description or overclaiming capability.

## Details
- **Definition** — narrative identity is the persistent account of an agent's role, goals, history, and the principles it claims to follow.
- **Continuity** — sessions reference the narrative so a returning agent resumes with the same commitments and context.
- **Persona** — role and tone are part of the narrative, shaping how the agent communicates consistently.
- **Memory hooks** — the narrative is grounded in real memory and logs, not invented biography, keeping claims verifiable.
- **Honesty** — agents should distinguish what they actually did from what they were told, avoiding fabricated history.
- **Evolution** — the narrative should update with real experience, which raises the question of who approves changes to the self-story.
- **Common failure modes** — inflated self-descriptions, identity drift across sessions, and narratives that contradict observable behavior.
- **Worked example** — a coding assistant's narrative records its workspace, tools, and prior fixes; a new session reads the narrative and continues with the same role.
- **Practical relevance** — a grounded narrative identity is what makes long-lived agents feel coherent and act accountable.

- **Audience** — the narrative is told to the agent itself and to collaborators, so it should be useful, not just descriptive.
- **Safety** — a narrative that overclaims capability can cause an agent to attempt things beyond its real scope.
## Related
- [[wiki/agent-systems/identity-and-continuity|Identity and Continuity]] — persistence of self
- [[wiki/llm-agents/agent-personas|Agent Personas]] — role and style
- [[wiki/agent-systems/stated-vs-hidden-goals|Stated vs Hidden Goals]] — honest self-description
- [[wiki/agent-systems/goal-disclosure|Goal Disclosure]] — declaring intent
- [[wiki/llm-agents/memory-augmented-agents|Memory-Augmented Agents]] — grounding the story
- [[wiki/llm-agents/agent-versioning|Agent Versioning]] — versioned identity
