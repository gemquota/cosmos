---
type: "entity"
title: "Cognitive Dimensions"
description: "Referenced in session 019f1a6c"
tags: ["api", "ast", "auth", "authentication", "aws", "bash", "bootstrap", "entity"]
timestamp: "2026-07-19T22:41:40Z"
status: "growing"
resource: ""
---


## Cognitive Dimensions 2

Cognitive Dimensions appears in 2 session(s) categorized as API, Cloud, Security, Shell. Related topics: api, auth, authentication, aws, bash, bootstrap.

**Domain:** Web Platforms › [[wiki/web-platforms/supercategories/security-auth/index|Security Auth]] › [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/index|Auth Security]] › Cognitive Dimensions 2

## Overview

Cognitive Dimensions is a framework for evaluating the usability of notations, interfaces, and information structures. It names a small set of dimensions along which any notation can be assessed — viscosity (resistance to change), hidden dependencies, premature commitment, visibility, and abstraction level, among others. The framework is used to compare languages, APIs, configuration formats, and dashboards: rather than asking "is it user-friendly?" in the abstract, it asks how the notation behaves under specific activities like modification, comprehension, and error recovery.

## Details

- Viscosity: how hard is it to make a change? A highly viscous design punishes edits and discourages iteration.
- Hidden dependencies: relationships that are not visible until they break; they make comprehension and change risky.
- Premature commitment: forcing decisions before the user has enough information constrains later choices.
- Visibility: whether relevant information is displayed when needed; poor visibility causes guessing and errors.
- Abstraction level: how close the notation sits to the user's mental model versus raw implementation details.
- Error-proneness: whether the notation invites mistakes; combined with the others it predicts failure modes.

Applied to API and auth systems, cognitive dimensions evaluate API contracts, permission policies, and configuration files: a policy format with hidden dependencies and high viscosity leads to misconfiguration and security gaps. Sessions use the framework to critique tooling — dashboards, specs, and shell scripts — and to justify redesigns with a shared vocabulary. The value is structural: it moves usability discussion from taste to analyzable properties.

## Related Entities

- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/ab|Ab]]
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/automatic-10|Automatic 10]]
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/fov-2|Fov 2]]
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/selective-chaos|Selective Chaos]]
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/rubenverborgh|Rubenverborgh]]
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/sim-speed|Sim Speed]]
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/missing-content|Missing Content]]
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/searchtext|Searchtext]]
