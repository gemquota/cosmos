---
type: "entity"
title: "Nah"
resource: ""
---
description: "Handling negation and rejection in agent conversations and instructions"
tags: ["entity", "bash", "bootstrap", "bun", "ide", "json", "agents", "communication"]
timestamp: "2026-07-19T22:41:41Z"

# Nah

## Summary
Nah represents the challenge of handling negation and rejection in agent interactions: recognizing when a user or reviewer says no, correcting course, and not repeating the rejected action. It matters because agents that ignore rejection erode trust and waste work. Treating rejection as a first-class signal is essential for interactive agents that work with people.

## Details
- **Definition** — negation handling covers detecting negative responses, interpreting what exactly was rejected, and adjusting the plan.
- **Signal detection** — rejection arrives in many forms: explicit no, corrected phrasing, changed preferences, or silence that implies dissatisfaction.
- **Scope** — a rejection may target the whole plan, one step, or just the wording; the agent must identify the scope before acting.
- **Correction** — after rejection, the agent should revise and confirm, not repeat the same approach with different words.
- **Human in the loop** — rejection is a prompt to involve the user in the next decision rather than guessing again.
- **Persistence** — rejected options should be remembered so they are not proposed again in the same session.
- **Common failure modes** — ignoring rejection, over-correcting to the opposite extreme, and treating every objection as a directive to stop entirely.
- **Worked example** — a user rejects a generated design; the agent asks which aspect failed, records it, and proposes an alternative that avoids it.
- **Practical relevance** — graceful handling of rejection is what makes agents feel responsive and collaborative instead of stubborn.

- **Tone** — rejection is often indirect; agents should treat lukewarm feedback as a signal to check rather than assume approval.
- **Clarification** — asking one precise question beats guessing when the rejected aspect is ambiguous.
- **Respect** — repeated rejections should reduce confidence and escalate to the user rather than plow ahead.
## Related
- [[wiki/llm-agents/hallucination-mitigation|Hallucination Mitigation]] — responding to corrections
- [[wiki/prompt-engineering/adversarial-prompts|Adversarial Prompts]] — hostile inputs
- [[wiki/agent-systems/instruction-following|Instruction Following]] — respecting direction
- [[wiki/llm-agents/human-in-the-loop|Human in the Loop]] — user involvement
- [[wiki/prompt-engineering/error-messages-llm|Error Messages for LLMs]] — clear feedback
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — measuring responsiveness
