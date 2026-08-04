---
type: "entity"
title: "CalledProcessError"
description: "A Python exception raised when a subprocess exits with a non-zero status"
tags: ["entity", "exceptions", "python", "subprocess", "errors"]
timestamp: "2026-07-19T22:41:39Z"
resource: ""
---

# CalledProcessError

## Summary

CalledProcessError is a Python exception raised by subprocess functions when a child process exits with a non-zero return code. It matters because every shell-out is a potential failure point: the command may be missing, misconfigured, or fail on real input. Handling it well means capturing stderr, checking the return code deliberately, and converting expected failures into readable messages.

## Details

- **Definition** — subprocess.run with check=True raises CalledProcessError on non-zero exit, carrying the return code and often the output.
- **Fields** — The exception exposes returncode, cmd, and captured stdout or stderr, which together explain what failed.
- **Check vs explicit** — check=True is convenient but raises for any non-zero exit; scripts with expected failures often prefer explicit return-code checks.
- **Worked example** — A build script runs a compiler via subprocess; a syntax error in the source makes the child exit 2, raising CalledProcessError with the compiler's stderr.
- **Common failure modes** — Swallowing the exception and continuing, leaking captured output that contains secrets, and timeouts that kill children mid-run.
- **Practical relevance** — Automation and agent tooling shell out constantly, so robust subprocess handling is a core reliability skill.
- **Variants** — Non-checked calls return a CompletedProcess; capture_output and text options shape how output is collected and parsed.
- **Telemetry note** — Recorded among backend, CLI, and logging tags, matching script-driven operations where subprocesses fail loudly.
- **Timeout** — Wrapping subprocess calls with timeout bounds runaway children; on expiry, Python kills the process and raises, preventing hangs.
- **Output size** — Capturing unbounded output can exhaust memory; streaming to files or capping capture keeps automation stable on chatty commands.
- **Worked example** — A provisioning script runs apt commands; a missing package exits non-zero, and the handler prints the command and stderr before failing the run.
- **Security** — Shelling out with unvalidated input risks injection; argument lists and shlex help keep commands well-formed.

## Related

- [[wiki/shell-environment/exit-codes-and-error-handling|Exit Codes and Error Handling]] — the process contract
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/exception-2|Exception]] — the exception family
- [[wiki/os-shell/fork-exec-and-process-creation|Fork Exec and Process Creation]] — how children start
- [[wiki/os-shell/errexit-and-shell-options|Errexit and Shell Options]] — shell-side equivalent
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/errorcode|ErrorCode]] — coding the failure
- [[wiki/dev-tools/debug-logging|Debug Logging]] — logging command failures
