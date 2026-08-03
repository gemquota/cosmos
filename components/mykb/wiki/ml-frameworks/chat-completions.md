---
type: "concept"
title: "Chat Completions"
description: "The chat endpoint pattern (messages in, assistant message out) that most LLM APIs standardize on"
tags: ["chat-completions", "apis", "chat", "protocols"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# Chat Completions

## Summary

The Chat Completions API is the dominant hosted LLM interface: a conversation as a message list (system/user/assistant/tool) with a generation request (model, temperature, max tokens). It defined the conventions every other provider clones.

## Details
- Mechanism: the client sends messages with roles and content; the server returns a completion (or streams deltas); parameters control sampling (temperature, top_p), length (max_tokens/max_completion_tokens), and behavior (stop sequences, frequency/penalty, response_format); tool/function definitions ride along so the model can request calls; usage fields report exact token counts.
- Concrete example: a chat UI maps its conversation to messages and appends each assistant turn; a RAG loop assembles retrieved context into the system message and questions into user messages; a tool-using agent includes the tool schema and executes the returned tool_calls, appending results as tool messages.
- Failure modes: role misuse (system content treated as untrusted instructions when prompt-injected); length miscalculation (max tokens counting output only); temperature/top_p interplay misunderstood (they are not interchangeable); and relying on the model to respect message boundaries — role semantics are a convention, so treat all content as untrusted.
- Operational tradeoffs: chat-shaped prompting is the compatibility layer of the LLM ecosystem — same shape across providers and local runtimes via adapters; the trade is verbosity and context management versus a single-prompt design. Track tokens per role and cache static prefixes for cost control.
- RSIS3/mykb relevance: the wiki's loop would target OpenAI-compatible chat endpoints across hosted and local runtimes, so one prompting convention spans experiments.
- Streaming contract: with stream=true the response is delta events ending with a final chunk carrying usage; clients must handle partial content, cancellation, and the no-usage edge case.
- Retry and backoff: provider rate limits and overload errors (429/5xx) are the norm at scale — implement jittered backoff and Retry-After honoring rather than assuming availability.

## Related
- [[wiki/prompt-engineering/message-format|Message Format]] — The protocol it transports
- [[wiki/ml-frameworks/openai-api|OpenAI API]] — The reference implementation
- [[wiki/ml-frameworks/ollama|Ollama]] — Local OpenAI-compatible endpoint
- [[wiki/prompt-engineering/function-calling|Function Calling]] — Tool calls in responses
- [[wiki/prompt-engineering/json-mode|JSON Mode]] — Structured response formats
