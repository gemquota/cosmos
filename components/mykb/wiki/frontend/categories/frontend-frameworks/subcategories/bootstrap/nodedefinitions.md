---
type: "entity"
title: "NodeDefinitions"
description: "NodeDefinitions: typed registries describing node behavior, ports, and configuration"
tags: ["entity", "api", "ast", "aws", "bash", "bootstrap", "node-editor"]
timestamp: "2026-07-19T22:41:42Z"
resource: ""
---

# NodeDefinitions

## Summary

NodeDefinitions is the bootstrap-cluster entity for node type registries in node-based editors: the schema that describes what each node does, its ports, and its configuration. A clean registry is what makes editors extensible and graphs interpretable. It matters because node behavior is only as trustworthy as its definition. Definitions are also the documentation of what a graph can express, so they should be introspectable.

## Details

- **Definition** — Node definitions describe each node type: its category, input and output ports, parameters, and execution behavior.
- **Registry pattern** — A registry maps type names to definitions, letting graphs reference nodes by name and editors render them generically.
- **Port typing** — Typed ports validate connections at edit time, catching invalid graphs before execution.
- **Configuration schema** — Per-node parameters need schemas with defaults so instances serialize completely.
- **Extensibility** — Plugins contribute definitions, which requires versioning and conflict management.
- **Worked example** — A shader graph's registry defines math nodes with number ports; only matching port types may connect.
- **Failure modes** — Unknown node types in loaded graphs, schema drift, and unversioned definitions break old documents.
- **Practical relevance** — Definitions are the contract between stored graphs and execution, so their stability is safety-critical.
- **Schema versioning** — Versioned definitions let stored graphs declare which definition version they expect.
- **Defaults** — Sensible defaults make nodes usable immediately and keep serialized graphs complete.
- **Introspection** — Listing definitions powers palettes, search, and documentation generated from the registry.
- **Documentation** — Generating help text and examples from definitions keeps editor documentation in sync, and versioned schemas let older graphs load with migrations instead of failing.

## Related

- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/nodeeditor|NodeEditor]] — the editor using definitions
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/noderenderer|NodeRenderer]] — rendering per definition
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/edgeid|EdgeId]] — connections between defined nodes
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/decisiontype|DecisionType]] — typed choices in definitions
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/00-index|Bootstrap Index]] — cluster index page
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/filesystemloader|FileSystemLoader]] — loading graphs that reference definitions
