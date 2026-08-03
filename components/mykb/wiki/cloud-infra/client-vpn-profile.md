---
type: "concept"
title: "Client VPN Profiles"
description: "Per-user VPN configurations for remote access to private networks"
tags: ["client-vpn", "vpn", "remote-access", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Client VPN Profiles

## Summary

A client VPN profile packages the configuration a user's device needs to connect: endpoints, certificates/credentials, routing, and DNS. Getting the profile right — least-privilege routes, safe certificate handling, split tunneling — determines both security and usability of remote access.

## Details
- Mechanism: profiles contain the VPN server address(es), client certificate (or SAML/OTP configuration), CA bundle, cipher preferences, and route/DNS directives (split tunneling lists or full tunnel). AWS Client VPN, Azure P2S, and OpenVPN/WireGuard configs all follow this shape; the profile is the artifact distributed to devices.
- Concrete example: a split-tunnel profile routes only 10.0.0.0/8 through the VPN while the user's internet stays local — better performance and less traffic inspection; a full-tunnel profile sends everything through for compliance, at the cost of latency and egress cost. Certificates should be short-lived per user and revocable.
- Failure modes: distributing long-lived client certificates that survive offboarding (the classic leak); profiles hard-coding credentials in plaintext config files; split-tunnel misconfig leaking traffic or missing required subnets; and DNS leaks where the VPN's resolver is not applied, exposing lookup metadata.
- Operational tradeoffs: certificate-based auth is robust but adds issuance/rotation work; SAML integration trades that for identity-provider dependency. Profile versioning matters — devices need a way to receive revoked or updated configs; document rotation and emergency revocation procedures.
- RSIS3/mykb relevance: the team's admin VPN uses a generated profile with short-lived certs; this note records the profile template and rotation policy for the loop's infrastructure changes.
- Profile distribution: serve profiles through a portal or MDM with per-user revocation, and rotate client certificates on a schedule; a profile handed out on a USB stick is a standing credential leak.
- Expiry alerting: alert before client certificates expire so users are not cut off mid-flight; certificate expiry is the most common silent VPN outage.

## Related
- [[wiki/cloud-infra/vpn-technologies|VPN Technologies]]
- [[wiki/cloud-infra/vpn-split-tunneling|VPN Split Tunneling]]
- [[wiki/cloud-infra/site-to-site-vpn|Site-to-Site VPN]]
- [[wiki/cloud-infra/vpn-tunnels|VPN Tunnels]]
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
