---
type: "entity"
title: "MCP"
description: "API — service communication interface, Bash — shell scripting language, CSS — web styling language"
tags: ["entity", "acronym", "api", "ast", "bash", "css"]
timestamp: "2026-07-19T22:41:41Z"
status: "growing"
resource: ""
---

## Mcp

A technical protocol or system component referenced in agent sessions. May refer to a control protocol or management interface.

**Domain:** Web Platforms › [[wiki/web-platforms/index|Frontend]] › [[wiki/web-platforms/index|Css Styling]]

## Overview

MCP is an acronym with multiple plausible expansions; the most common in current tooling is the Model Context Protocol, a standard for connecting AI applications to external data sources and tools through a uniform client-server interface. In that reading, an MCP server exposes resources, tools, and prompts, and an MCP client lets an agent or application invoke them consistently. The protocol's value is standardization: one integration surface replaces many ad-hoc API adapters.

## Details

- Resources: named data sources that clients can read, such as documents, files, or database records.
- Tools: callable operations the model may invoke, with typed schemas describing parameters and results.
- Prompts: reusable instruction templates that structure how a model is asked to perform a task.
- Transport: JSON-RPC over stdio or HTTP carries messages between client and server, keeping the boundary simple to implement.
- Security: capabilities are declared and scoped; clients control which servers and tools are available, and sensitive operations should still require explicit authorization.

In this knowledge base, MCP sits under frontend and CSS styling categories, where it likely appeared as a tool-adjacent component in agent sessions — for example, a server that feeds styling or reference data to an assistant. Regardless of the exact expansion, the pattern is the same: a well-defined protocol boundary between a consumer and the systems it needs, with discoverable capabilities and explicit contracts. When the acronym is ambiguous, resolve it from the session context: the command that started the server, the tools it exposed, and the data it made available are the authoritative clues.

## Related Entities

- [[wiki/frontend/categories/css-styling/importerror-10|Importerror 10]]
- [[wiki/frontend/categories/css-styling/css-10|Css 10]]
- [[wiki/frontend/categories/css-styling/complete-reference-2|Complete Reference 2]]
- [[wiki/frontend/categories/css-styling/database-2|Database 2]]
- [[wiki/frontend/categories/css-styling/display-2|Display 2]]
- [[wiki/frontend/categories/css-styling/html-10|Html 10]]
- [[wiki/frontend/categories/css-styling/reference-2|Reference 2]]
- [[wiki/frontend/categories/css-styling/dob-2|Dob 2]]
