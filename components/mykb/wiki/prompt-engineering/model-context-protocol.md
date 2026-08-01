---
type: "concept"
title: "Model Context Protocol"
description: "An open standard for connecting LLM applications to external tools, data sources, and context servers"
tags: ["model-context-protocol", "mcp", "interoperability", "tools", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://modelcontextprotocol.io/"]
---

# Model Context Protocol

## Summary
Model Context Protocol (MCP) is an open protocol that standardizes how LLM applications talk to tools, prompts, and data resources. Instead of N custom integrations per agent, one MCP server exposes capabilities that any MCP client can consume.

## Details
- MCP defines three capability types: tools (executable functions), resources (readable data), and prompts (reusable prompt templates).
- Architecture: hosts (apps like Claude Desktop or an agent runtime) connect to MCP servers over stdio or HTTP, with JSON-RPC-style messages.
- Benefits: one integration per tool source, shared auth and lifecycle, and portable context across clients.
- RSIS3 relevance: the L1 action loop's tools (shell, wiki, web) could be exposed as MCP servers, making RSIS3 tooling interoperable with other agent frameworks.
- Ecosystem momentum: MCP servers exist for databases, browsers, filesystems, GitHub, and internal wikis; the spec is maintained by Anthropic.
- Design caveat: MCP standardizes transport and schemas, not safety — prompt-injection surface grows with every connected tool server.

## Related
- [[wiki/prompt-engineering/tool-calling|Tool Calling]] — MCP is a transport standard for tool calling
- [[wiki/prompt-engineering/function-calling|Function Calling]] — MCP tools map onto function-calling schemas
- [[wiki/ml-frameworks/tool-schemas|Tool Schemas]] — Schemas are the contract inside MCP tool definitions
- [[wiki/prompt-engineering/agent-state|Agent State]] — MCP sessions carry state between host and server
- [[wiki/ml-frameworks/openai-api|OpenAI API]] — OpenAI-compatible clients can consume MCP tools
- [[wiki/ml-frameworks/ollama|Ollama]] — Local models can serve as MCP-connected hosts
- [[wiki/concepts/mykb-research-report|mykb Research Report: Personal LLM Wiki Systems — Methodologies, Architectures & Integration Blueprint]] — Interoperability research relevant to MCP adoption
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — MCP servers integrate wiki tools
