---
type: "concept"
title: "Dialog State Tracking"
description: "Maintaining structured state of user goals and slots across a conversation"
tags: ["dialog-state", "dialog", "state", "conversation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Dialog State Tracking

## Summary

Dialog state tracking maintains a structured representation of user goals and slot values across a conversation. It turns a stream of turns into updatable, queryable state that the agent can reason over. It matters because coherent multi-turn dialogue depends on remembering what was established and what is still missing. Dialog state is the interface between understanding and action, so its quality bounds the whole agent.

## Details

- **Definition** — Dialog state is the accumulated understanding of the conversation: intents, slot values, and unresolved questions.
- **Slots and goals** — Slots are typed fillable fields; the goal is the task the user is trying to complete with those values.
- **Update rules** — New turns overwrite or refine slots; contradictions, confirmations, and corrections each update state differently.
- **Confidence** — State tracks how certain each slot value is, so the agent knows when to ask for confirmation.
- **Persistence** — State must survive rephrasing, interruptions, and topic shifts within a session.
- **Failure modes** — Overwriting values from clarifications, ignoring implicit slots, and state that drifts from the transcript cause wrong actions.
- **Worked example** — A booking agent records destination, date, and party size across turns, asking only for the slots still missing.
- **Practical relevance** — Voice and chat agents both depend on dialog state; it is the interface between understanding and acting.
- **Correction handling** — When users correct a value, state must update precisely instead of appending a conflicting duplicate.
- **Slot elicitation** — Tracking which slots are missing drives natural follow-up questions that complete the goal.
- **Multi-turn memory** — State that persists across topic shifts lets users return to an earlier task without restating it.

## Related

- [[wiki/llm-agents/conversation-history-management|Conversation History Management]] — the raw history state is distilled from
- [[wiki/llm-agents/voice-agents|Voice Agents]] — spoken dialog with tracked state
- [[wiki/llm-agents/user-confirmation-flows|User Confirmation Flows]] — confirming tracked values
- [[wiki/llm-agents/memory-hierarchy-agentic|Memory Hierarchy Agentic]] — where dialog state fits in memory
- [[wiki/agent-systems/agent-state-machines|Agent State Machines]] — state transitions in agents
