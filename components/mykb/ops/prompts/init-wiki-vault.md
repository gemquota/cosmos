---
type: prompt
title: init-wiki-vault
description: Agent prompt for init wiki vault
tags: [prompt, ops]
---

# Prompt: Init Wiki Vault

Use `$obsidian-wiki-system` to initialize a new Obsidian wiki knowledge iteration system in the specified folder.

Input:

- Target folder:
- Vault name:
- Preferred language:

Rules:

1. Preserve existing user notes.
2. Match the user's preferred language. If no preference is given, infer it from the user's message or existing notes.
3. Copy the appropriate template.
4. Replace `2026-07-18` and `mykb`.
5. Do not overwrite meaningful existing files without asking.
6. Tell the user which entry page to open first.
