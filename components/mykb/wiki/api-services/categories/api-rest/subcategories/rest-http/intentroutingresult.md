---
type: "entity"
title: "IntentRoutingResult"
description: "The outcome of routing a user intent to a handler, agent, or skill"
tags: ["entity", "intent", "routing", "agents", "nlp"]
timestamp: "2026-07-19T22:41:42Z"
resource: ""
---

# IntentRoutingResult

## Summary

IntentRoutingResult is the output of an intent-routing step: the classification of a user request into a target handler, agent, or capability, along with confidence and supporting evidence. It matters because routing quality decides whether the right tool answers the request. A routing result typically carries the chosen intent, alternatives, and the signal that justified the choice.

## Details

- **Definition** — Intent routing maps an utterance or task to a destination; the result object records the selection and its rationale.
- **Classification** — Classifiers or language models score candidate intents; the highest score wins unless a fallback threshold is not met.
- **Result fields** — Typical fields include intent id, confidence, ranked alternatives, matched entities, and the raw text or features that drove the decision.
- **Fallbacks** — Low-confidence results route to clarification, a generalist handler, or an escalation path rather than guessing.
- **Worked example** — A request to book a flight scores high for the booking intent, so the router returns BookingIntent with the parsed city and date and a confidence score.
- **Common failure modes** — Confidently misrouting ambiguous requests, overfitting to phrase patterns, and results that omit the evidence needed for debugging.
- **Practical relevance** — In agent systems, intent routing decides which agent or skill executes, so its results should be logged and auditable.
- **Evaluation** — Routing accuracy is measured on held-out utterance sets; confusion matrices reveal which intents are confused with each other.
- **Telemetry note** — Recorded in API and backend sessions with an intent tag, matching dialogue and agent pipeline contexts.
- **Logging** — Routing results should be logged with the utterance and selected intent so misroutes are diagnosable and improvable.
- **Threshold tuning** — Confidence thresholds balance precision and fallback rate; tuning uses logged results rather than intuition.
- **Worked example** — A virtual assistant logs that a refund request scored refund-intent at 0.41 and escalation at 0.39, so it asks a clarifying question instead of routing.
- **Evaluation** — A confusion matrix of intents reveals systematic confusions, such as refunds being routed to order-status, guiding training data collection.

## Related

- [[wiki/concepts/intent-alignment|Intent Alignment]] — matching intent to action
- [[wiki/mobile-platform/android-intents|Android Intents]] — platform intent dispatch
- [[wiki/agent-systems/delegation-and-handoffs|Delegation and Handoffs]] — routing to agents
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/goalgenerator|GoalGenerator]] — converting routed intent to goals
- [[wiki/llm-agents/success-criteria|Success Criteria]] — defining routing success
- [[wiki/concepts/category-learning|Category Learning]] — learning intent categories
