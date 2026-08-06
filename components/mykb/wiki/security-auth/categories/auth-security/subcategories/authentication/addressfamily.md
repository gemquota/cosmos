---
status: "growing"
type: "entity"
title: "AddressFamily"
description: "AddressFamily"
tags: ["entity", "android", "api", "ast", "auth", "authentication"]
timestamp: "2026-07-19T22:41:41Z"
resource: ""
---

## Addressfamily

AddressFamily appears in 1 session(s) categorized as API, Mobile, Security. Related topics: android, api, auth, authentication.

**Domain:** Mobile Platform › [[wiki/android-core/00-index|Android Core]] › [[wiki/web-platforms/00-index|Auth Security › Addressfamily]]

## Overview

AddressFamily identifies the addressing scheme a socket uses. The most common families are `AF_INET` for IPv4, `AF_INET6` for IPv6, and `AF_UNIX` for local inter-process communication. Choosing the family determines the address format, the address length, and which protocols the socket can speak, so it is the first decision in any network programming task.

## Common Families

- `AF_INET` / `AF_INET6`: internet sockets with IP addresses and ports; dual-stack applications handle both.
- `AF_UNIX`: filesystem-backed sockets for fast local IPC without the network stack.
- `getaddrinfo` returns a list of addresses across families; code should iterate and try each.

## Binding and Connection Details

When a server binds, it supplies an address literal in the family's format — a dotted-quad IPv4 address, a bracketed IPv6 address with scope identifiers, or a filesystem path for `AF_UNIX`. The kernel matches incoming packets against the bound address and port, and for local sockets it enforces filesystem permissions on the socket file. Client code typically resolves a hostname with `getaddrinfo`, which may return both `AF_INET` and `AF_INET6` candidates; robust clients try each entry in order until one connects, rather than assuming a single family. IPv6-specific behavior, such as link-local addresses that require a scope ID, is a frequent source of subtle bugs when address families are mixed.

## Security Notes

- Validate and constrain which families and endpoints a service accepts; unfiltered resolution can enable server-side request forgery attacks.
- Dual-stack binding must decide whether a socket listens on both IPv4 and IPv6, and how that affects access control.
- Local `AF_UNIX` endpoints need careful permissions and socket-file hygiene — stale socket files can cause bind failures or unauthorized access.

## Related Concepts

- [[wiki/os-shell/network-sockets|Network Sockets]] — the API that uses address families
- [[wiki/os-shell/ip-addresses-and-subnetting|IP Addresses and Subnetting]] — addressing semantics

## Related Entities

- [[wiki/security-auth/categories/auth-security/subcategories/authentication/abuseipdb-2|Abuseipdb 2]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/ac-2|Ac 2]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/access-denied|Access Denied]]
- [[raw/archive/junk-entities-2026-08c/security-auth/categories/auth-security/subcategories/authentication/ach-2|Ach 2]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/actionnode-2|Actionnode 2]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/aec-2|Aec 2]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/agentconfig|Agentconfig]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/agentswitchrecord|Agentswitchrecord]]
