---
type: "entity"
title: "MIME"
description: "Authentication — identity verification, CLI — command-line tooling, CSS — web styling language"
tags: ["entity", "acronym", "ast", "auth", "cli", "css"]
timestamp: "2026-07-19T22:41:41Z"
resource: ""
---

# MIME

## Summary

MIME, or Multipurpose Internet Mail Extensions, is the standard system for declaring the type of content carried in emails, HTTP responses, and file uploads. Type declarations such as text/html and application/json tell clients how to interpret bytes. MIME handling matters in security because mismatches between declared and actual content enable content-sniffing attacks, upload abuse, and cross-site scripting. MIME handling is a boundary problem: every place untrusted bytes cross a type boundary is a place to harden.

## Details

- **Entity record** — this page indexes "MIME" as an acronym entity from analyzed session content touching authentication and web tooling.
- **Content types** — MIME types label data by major type (text, image, application) and subtype, with parameters such as charset.
- **HTTP role** — servers send Content-Type headers so browsers render, download, or process responses correctly.
- **Upload security** — file uploads declare a MIME type, but attackers can claim one type while uploading executable content; validation must inspect actual bytes.
- **Content sniffing** — some browsers ignore declared types and guess from content, enabling attacks; the X-Content-Type-Options: nosniff header disables this.
- **Failure modes** — trusting client-supplied MIME types, serving user content with dangerous types, and missing nosniff headers are common findings.
- **Worked example** — an audit found an avatar upload endpoint accepting image/png claims; a crafted HTML file passed the check, so validation was changed to verify magic bytes.
- **Practical relevance** — correct MIME handling is part of secure file upload, email filtering, and web response hardening.
- **Relation to entity indexing** — acronym expansion pages help analysts resolve what a term meant in the analyzed session.
- **Best practice** — validate content by signature, not declaration; serve untrusted content with restrictive types and headers.
- **Magic-byte validation** — checking the first bytes of a file against its claimed type catches the most common upload spoofing.


## Related

- [[wiki/security/categories/authentication/instructions|Instructions]] — sibling entity
- [[wiki/security/categories/authentication/mcq|MCQ]] — sibling entity
- [[wiki/security/categories/authentication/pixi|PIXI]] — sibling entity
- [[wiki/security-auth/security-headers|Security Headers]] — the nosniff defense
- [[wiki/security-auth/xss-prevention|XSS Prevention]] — the attack class
- [[wiki/security-auth/content-security-policy|Content Security Policy]] — related hardening

