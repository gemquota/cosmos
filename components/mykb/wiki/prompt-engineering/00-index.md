---
type: "index"
hub: true
title: "Prompt Engineering Index"
description: "Listing of the prompt-engineering/ folder (81 pages)."
tags: ["index"]
timestamp: "2026-08-03T00:00:00Z"
---

# Prompt Engineering

Part of [[wiki/index|Wiki Index]]. 81 pages.

## Pages
- [[wiki/prompt-engineering/adversarial-prompts|Adversarial Prompts]] — Crafted inputs designed to confuse, mislead, or compromise an LLM — the raw material of attacks and red teaming
- [[wiki/prompt-engineering/agent-state|Agent State]] — The accumulated conversation, tool results, goals, and memory an agent carries across its action loop
- [[wiki/prompt-engineering/agentic-context-crafting|Agentic Context Crafting]] — Building and maintaining the context an agent sees each step from memory, retrieval, and tool results
- [[wiki/prompt-engineering/agentic-rails|Agentic Rails]] — Execution-level guardrails that constrain what an agent may do: allowed tools, permissions, budgets, and action policies
- [[wiki/prompt-engineering/beam-search-decoding|Beam Search Decoding]] — Decoding that keeps the top-k partial sequences at each step to find better outputs
- [[wiki/prompt-engineering/code-prompting|Code Prompting]] — Prompting techniques specialized for code generation, repair, and explanation
- [[wiki/prompt-engineering/constrained-decoding|Constrained Decoding]] — Forcing generation to respect hard constraints such as schemas or grammars
- [[wiki/prompt-engineering/context-compression|Context Compression]] — Reducing the size of context through summarization, extraction, or dropping low-value content
- [[wiki/prompt-engineering/context-engineering|Context Engineering]] — The discipline of designing, assembling, and maintaining the context given to a model
- [[wiki/prompt-engineering/context-injection|Context Injection]] — Inserting retrieved or computed context into prompts at the right position and granularity
- [[wiki/prompt-engineering/context-window-management|Context Window Management]] — Strategies for fitting the most useful information into a model context window
- [[wiki/prompt-engineering/context-windows|Context Windows]] — The maximum number of tokens a model can attend to in a single forward pass and conversation
- [[wiki/prompt-engineering/contrastive-decoding|Contrastive Decoding]] — Decoding that contrasts expert and amateur model distributions to reduce errors
- [[wiki/prompt-engineering/csv-tsv-output-parsing|CSV and TSV Output Parsing]] — Parsing tabular model outputs in CSV or TSV for downstream processing
- [[wiki/prompt-engineering/emergent-abilities|Emergent Abilities]] — Capabilities that appear sharply once a model crosses a scale or training threshold, not gradually
- [[wiki/prompt-engineering/entropy-based-sampling|Entropy-Based Sampling]] — Sampling strategies that adapt to model prediction entropy for better decoding
- [[wiki/prompt-engineering/error-messages-llm|Error Messages for LLM Systems]] — Designing and surfacing clear errors when models, tools, or pipelines fail
- [[wiki/prompt-engineering/few-shot-prompting|Few-Shot Prompting]] — Providing a small number of input-output exemplars in the prompt to condition the model's behaviour at inference time
- [[wiki/prompt-engineering/frequency-penalty|Frequency Penalty]] — Decoding parameter that reduces the probability of tokens already emitted many times
- [[wiki/prompt-engineering/function-calling|Function Calling]] — API support for declaring callable functions and having the model emit structured arguments to invoke them
- [[wiki/prompt-engineering/grammar-constrained-generation|Grammar-Constrained Generation]] — Decoding restricted to tokens valid under a formal grammar
- [[wiki/prompt-engineering/image-generation-prompts|Image Generation Prompts]] — Prompt crafting for text-to-image models to control composition and style
- [[wiki/prompt-engineering/in-context-learning|In-Context Learning]] — Task adaptation that happens at inference time from examples and instructions in the prompt, without weight updates
- [[wiki/prompt-engineering/indirect-injection|Indirect Injection]] — Prompt injection that arrives through third-party content — retrieved documents, emails, or web pages — rather than the user's own message
- [[wiki/prompt-engineering/json-mode-function-calling|JSON Mode and Function Calling]] — API features that constrain or route model output to structured JSON and tool invocations
- [[wiki/prompt-engineering/json-mode|JSON Mode]] — An API mode that guarantees the model returns valid JSON, removing the need for fragile text parsing
- [[wiki/prompt-engineering/json-schema-decoding|JSON Schema Decoding]] — Forcing model output to conform to a declared JSON schema during generation
- [[wiki/prompt-engineering/language-consistency|Language Consistency]] — Keeping model input and output language stable and coherent across a system
- [[wiki/prompt-engineering/latex-generation|LaTeX Generation]] — Producing LaTeX-formatted mathematical and scientific output
- [[wiki/prompt-engineering/least-to-most-prompting|Least-to-Most Prompting]] — Teaching a model to solve problems by first solving simpler subproblems in increasing difficulty
- [[wiki/prompt-engineering/logit-bias|Logit Bias]] — A per-token score added to logits before sampling, biasing the model toward or away from specific tokens
- [[wiki/prompt-engineering/markdown-output-rendering|Markdown Output Rendering]] — Producing and rendering markdown-formatted model output for documents and chat
- [[wiki/prompt-engineering/message-format|Message Format]] — The typed conversation structure (system, user, assistant, tool) that chat APIs use to represent multi-turn dialogue
- [[wiki/prompt-engineering/model-context-protocol|Model Context Protocol]] — An open standard for connecting LLM applications to external tools, data sources, and context servers
- [[wiki/prompt-engineering/monte-carlo-tree-search-llm|Monte Carlo Tree Search for LLMs]] — Applying MCTS planning to language-model reasoning and decision problems
- [[wiki/prompt-engineering/multi-step-reasoning|Multi-Step Reasoning]] — Prompts and methods that decompose problems into intermediate reasoning steps to improve complex answers
- [[wiki/prompt-engineering/multilingual-prompting|Multilingual Prompting]] — Crafting prompts that work across languages and cultural contexts
- [[wiki/prompt-engineering/output-format-negotiation|Output Format Negotiation]] — Agreeing on output structure between requester and model before generation
- [[wiki/prompt-engineering/persona-prompting|Persona Prompting]] — Giving the model a defined persona to shape voice, values, and behavior
- [[wiki/prompt-engineering/presence-penalty|Presence Penalty]] — Decoding parameter that penalizes any token that has appeared at least once, encouraging topic diversity
- [[wiki/prompt-engineering/program-of-thoughts|Program of Thoughts]] — Reasoning technique that expresses reasoning steps as executable program code
- [[wiki/prompt-engineering/prompt-chaining|Prompt Chaining]] — Decomposing a complex task into a sequence of linked prompts where each stage's output feeds the next stage's input
- [[wiki/prompt-engineering/prompt-compression|Prompt Compression]] — Techniques for shrinking prompts — summarization, distillation, or learned compressors — while preserving task-relevant information
- [[wiki/prompt-engineering/prompt-debugging|Prompt Debugging]] — Systematic techniques for diagnosing why a prompt produces bad outputs
- [[wiki/prompt-engineering/prompt-engineering-fundamentals|Prompt Engineering Fundamentals]] — Core principles and techniques for designing prompts that reliably produce good outputs
- [[wiki/prompt-engineering/prompt-injection-defense|Prompt Injection Defense]] — Protecting LLM applications from instructions embedded in untrusted content
- [[wiki/prompt-engineering/prompt-leakage|Prompt Leakage]] — Exfiltration of the hidden system prompt or private context by a crafted user or third-party input
- [[wiki/prompt-engineering/prompt-libraries|Prompt Libraries]] — Curated collections of reusable, tested prompts for common tasks
- [[wiki/prompt-engineering/prompt-repositories|Prompt Repositories]] — Versioned storage and review workflows for prompts as code
- [[wiki/prompt-engineering/prompt-templates|Prompt Templates]] — Parameterized prompt skeletons with slots for dynamic content
- [[wiki/prompt-engineering/prompt-testing|Prompt Testing]] — Automated evaluation of prompt variants against expected outputs
- [[wiki/prompt-engineering/prompt-versioning|Prompt Versioning]] — Tracking prompt revisions with metadata so changes are auditable and reversible
- [[wiki/prompt-engineering/re-reading-prompting|Re-Reading Prompting]] — Prompting strategy that repeats the question or context before answering to reduce comprehension errors
- [[wiki/prompt-engineering/red-teaming-llms|Red Teaming LLMs]] — Systematically attacking LLM applications to find safety and security failures before release
- [[wiki/prompt-engineering/red-teaming|Red Teaming]] — Proactively probing an LLM system with adversarial inputs to discover vulnerabilities before attackers do
- [[wiki/prompt-engineering/refusal-behaviour|Refusal Behaviour]] — The trained tendency of a model to decline requests that violate safety, legal, or policy boundaries
- [[wiki/prompt-engineering/retrieval-prompting|Retrieval Prompting]] — Augmenting prompts with relevant documents fetched from a knowledge base, the core of retrieval-augmented generation
- [[wiki/prompt-engineering/role-prompting|Role Prompting]] — Assigning the model a professional or functional role to guide its approach
- [[wiki/prompt-engineering/safety-tuning|Safety Tuning]] — Training techniques — SFT on safe responses, RLHF, and preference data — that teach models to refuse harmful requests
- [[wiki/prompt-engineering/sampling-vs-greedy|Sampling vs Greedy Decoding]] — Trade-offs between deterministic greedy decoding and stochastic sampling for generation
- [[wiki/prompt-engineering/self-ask-technique|Self-Ask Technique]] — Prompting method where the model asks and answers follow-up questions before the final answer
- [[wiki/prompt-engineering/step-back-prompting|Step-Back Prompting]] — Prompting technique that asks the model to abstract to a higher-level principle before solving
- [[wiki/prompt-engineering/stop-sequences|Stop Sequences]] — Explicit token strings that terminate generation when the model emits them
- [[wiki/prompt-engineering/structured-output|Structured Output]] — Constraining an LLM to return machine-parseable, schema-validated responses instead of free text
- [[wiki/prompt-engineering/style-adaptation|Style Adaptation]] — Adjusting model output style to match audience, brand, or genre requirements
- [[wiki/prompt-engineering/system-prompt-design|System Prompt Design]] — Crafting the system prompt that sets model behavior, constraints, and context
- [[wiki/prompt-engineering/system-prompts|System Prompts]] — The persistent instruction block that defines an LLM's role, behaviour, and operating constraints for a session
- [[wiki/prompt-engineering/table-output-generation|Table Output Generation]] — Getting models to produce clean tabular data in markdown, CSV, or HTML
- [[wiki/prompt-engineering/temperature-anisotropy|Temperature Anisotropy]] — Phenomenon where model context and probability distributions are directionally biased in embedding space
- [[wiki/prompt-engineering/temperature-sampling|Temperature Sampling]] — The decoding parameter that controls how peaked or flat the next-token probability distribution is
- [[wiki/prompt-engineering/token-budget-planning|Token Budget Planning]] — Explicitly allocating token quotas across prompt sections before a call is made
- [[wiki/prompt-engineering/token-budgets|Token Budgets]] — Explicit allocation of the context window across system prompt, history, retrieval, and output to keep calls reliable and affordable
- [[wiki/prompt-engineering/tone-control|Tone Control]] — Managing the emotional register of model output for appropriate communication
- [[wiki/prompt-engineering/tool-calling|Tool Calling]] — The general capability of an LLM to request invocations of external tools during a conversation
- [[wiki/prompt-engineering/tool-parallelism|Tool Parallelism]] — Running multiple tool calls from a single model turn concurrently rather than sequentially
- [[wiki/prompt-engineering/tool-schema-design|Tool Schema Design]] — Designing the JSON schemas that describe tools to models for reliable function calling
- [[wiki/prompt-engineering/tool-selection|Tool Selection]] — Deciding which tool (or whether any tool) an agent should call for the current subgoal
- [[wiki/prompt-engineering/top-p-sampling|Top-P Sampling]] — Nucleus sampling: restricting next-token choices to the smallest set whose cumulative probability exceeds p
- [[wiki/prompt-engineering/tree-of-thoughts-variants|Tree of Thought Variants]] — Extensions of tree-of-thought search with different branching, scoring, and backtracking policies
- [[wiki/prompt-engineering/xml-output-parsing|XML Output Parsing]] — Using XML as a model output format and parsing it reliably
- [[wiki/prompt-engineering/zero-shot-prompting|Zero-Shot Prompting]] — Prompting a model to perform a task with no examples, relying on instruction-following from pretraining and instruction tuning
