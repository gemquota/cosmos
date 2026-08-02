---
type: "concept"
title: "Named Pipes (FIFOs)"
description: "mkfifo creation and reader/writer blocking semantics"
tags: ["fifo", "named-pipes", "ipc", "mkfifo"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man7/fifo.7.html", "https://man7.org/linux/man-pages/man1/mkfifo.1.html"]
---

# Named Pipes (FIFOs)

## Summary
A FIFO is a filesystem object that behaves like an anonymous pipe but has a name, so unrelated processes can connect through it. Data flows in one direction, byte-stream style, and open(2) blocks until both a reader and a writer exist.

## Details
- mkfifo(1) or mkfifo(3) creates the node; open for reading blocks until a writer opens, and vice versa — with O_NONBLOCK the behavior changes to immediate open plus errors.
- Reads return what is available: a read of n bytes may return fewer, and a read on a pipe with the last writer closed returns EOF.
- Writes are atomic up to PIPE_BUF (4096 bytes on Linux): interleaved small writers never mix data; larger writes can interleave.
- Because FIFOs are files, they inherit permissions and can be opened across users; access control is the filesystem's.
- Classic uses: feeding log streams between processes, connecting output of one cron job to a consumer, and simple client/server scaffolding.
- Anonymous pipes (shell |) are the same mechanism without a name, created by pipe(2) and inherited through fork.
- FIFOs have no message boundaries and no seek; use Unix sockets or message queues when structure is needed.

## Related
- [[wiki/os-shell/unix-domain-sockets|Unix Domain Sockets]] — the message-aware alternative
- [[wiki/os-shell/stdin-stdout-stderr|Stdin, Stdout & Stderr]] — how shells wire pipes into fds
- [[wiki/os-shell/text-processing-pipelines|Text Processing Pipelines]] — anonymous pipes at scale
- [[wiki/os-shell/file-descriptors|File Descriptors]] — the fd plumbing pipes rely on
- [[wiki/os-shell/here-documents|Here Documents]] — another shell I/O device
