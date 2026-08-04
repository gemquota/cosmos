---
type: "entity"
title: "Skills"
description: "Packaged bundles of instructions and reference material that teach an agent how to perform recurring tasks"
tags: ["entity", "api", "ast", "bash", "css", "documentation"]
timestamp: "2026-07-19T22:41:41Z"
resource: ""
status: "growing"
---
## Skills

Skills appears in 1 session(s) categorized as API, Frontend, Shell. Related topics: api, bash, css, documentation.

In agent-based development, a skill is a packaged bundle of instructions and reference material that teaches an agent how to perform a recurring task. A skill typically consists of a SKILL.md file describing when to use it, what steps to follow, and what conventions apply, sometimes accompanied by scripts, templates, and assets.

Skills are discovered through their name and description, so good metadata is essential: a clear trigger description lets the agent decide when the skill applies, while the body carries the procedural knowledge. Skills compose, so a workflow can chain several skills, each responsible for one phase of the work.

Documentation inside skills keeps procedures executable: commands, expected outputs, and failure handling are spelled out rather than assumed. Because skills are reused across sessions, they benefit from the same review and versioning discipline as code: changes are tested, and outdated instructions are updated or removed.

Skills also appear in the human sense of the word, as the competencies a team relies on: shell scripting, API design, CSS, and documentation are all skills that show up in session topics. The wiki records both senses, cataloguing agent-facing capabilities and the technical disciplines behind them under the [[wiki/web-platforms/00-index|Frontend]] and [[wiki/web-platforms/00-index|Shell Environment]] domains.

Keeping skills focused, documented, and versioned makes them a compounding asset: each new skill shortens the work for every future session that faces the same problem.

The entry also notes that skills are most valuable when they encode judgment: not just what to run, but how to verify the result and what to do when it fails.

**Domain:** Web Platforms › [[wiki/web-platforms/00-index|Llm Agents]] › Skills

## Related Entities

- [[wiki/frontend/categories/css-styling/importerror|Importerror 10]]
- [[wiki/frontend/categories/css-styling/css|Css 10]]
- [[wiki/frontend/categories/css-styling/complete-reference-2|Complete Reference 2]]
- [[wiki/frontend/categories/css-styling/database-2|Database 2]]
- [[wiki/frontend/categories/css-styling/display-2|Display 2]]
- [[wiki/frontend/categories/css-styling/html|Html 10]]
- [[wiki/frontend/categories/css-styling/reference-2|Reference 2]]
- [[wiki/frontend/categories/css-styling/dob-2|Dob 2]]
