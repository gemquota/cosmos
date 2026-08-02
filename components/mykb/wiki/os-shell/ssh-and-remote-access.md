---
type: "concept"
title: "SSH & Remote Access"
description: "Key auth, agent, config, and tunnels"
tags: ["ssh", "remote", "key-auth", "tunnels", "security"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man.openbsd.org/ssh.1", "https://man.openbsd.org/ssh_config.5"]
---

# SSH & Remote Access

## Summary
SSH provides encrypted remote login and command execution over the network. Public-key authentication replaces passwords, the ssh-agent holds keys, and the config file turns verbose one-liners into named hosts with tunnels.

## Details
- Keys: ssh-keygen -t ed25519 generates a key pair; the public key goes into ~/.ssh/authorized_keys on the server.
- Key auth flow: the client proves possession of the private key; agent forwarding lets nested hops use the same key.
- Config: ~/.ssh/config aliases Host web with HostName, User, IdentityFile, Port; ControlMaster reuses connections.
- Tunnels: -L local:port:remote:host maps a local port through the server; -R reverse tunnels expose local services; -D opens a SOCKS proxy.
- File transfer: scp, sftp, and rsync over ssh use the same auth; sshfs mounts remote directories.
- Trust: known_hosts pins server host keys to prevent MITM; host key changes trigger loud warnings.
- Hardening: disable PasswordAuthentication, set PermitRootLogin prohibit-password, use key-only access, and run sshd with least privilege.

## Related
- [[wiki/os-shell/rsync-synchronization|rsync]] — file sync over ssh
- [[wiki/os-shell/tmux-sessions|Tmux Sessions]] — persistent sessions over ssh
- [[wiki/security-auth/public-key-infrastructure|Public Key Infrastructure]] — the trust model behind host keys
- [[wiki/security-auth/audit-logging|Audit Logging]] — sshd logs every login
- [[wiki/os-shell/pty-and-pseudo-terminals|PTYs & Pseudo-Terminals]] — what sshd allocates per session
