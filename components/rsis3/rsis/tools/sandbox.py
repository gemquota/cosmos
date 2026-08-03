"""Execution sandbox — the security boundary (ported from Agent OS).

Tier 1 (default):  subprocess + resource limits + privilege drop +
                    minimal env + timeouts.  Good for structured tools
                    like git/gh/compilers.
Tier 2 (optional):  RestrictedPython for evaluating untrusted *pure
                    Python* in-process with a whitelisted builtin set.
Tier 3 (optional):  Docker backend — ephemeral container with hard
                    RAM/CPU/pid caps, no network, and a hard kill timeout.
                    Enabled via sandbox_backend=docker; falls back to
                    Tier 1/2 when the docker SDK is unavailable.

None of these tiers is a magic bullet: network egress and filesystem
access are only as safe as the tool that exposes them.  Tools must opt
in via scoped env + explicit path checks.
"""

from __future__ import annotations

import logging
import os
import signal
import subprocess
import sys
import warnings
from dataclasses import dataclass, field
from pathlib import Path

try:                                   # POSIX resource limits (Linux/macOS)
    import pwd
    import resource
except ImportError:                    # non-POSIX: limits become no-ops
    pwd = None
    resource = None

from rsis.tools.base import ToolResult, ToolStatus

logger = logging.getLogger(__name__)

# Minimal environment for child processes: no accidental secret leakage.
# The interpreter's own bin dir is included so subprocesses find the real
# python3/gh, not a system stub, regardless of the host distro.
_EXEC_DIR = str(Path(sys.executable).resolve().parent)

_BASE_ENV = {
    "PATH": os.pathsep.join([_EXEC_DIR, "/usr/local/bin", "/usr/bin",
                             "/bin", "/usr/sbin", "/sbin"]),
    "LANG": "C.UTF-8",
    "PYTHONUNBUFFERED": "1",
}


@dataclass
class SandboxResult:
    """Result of one sandboxed operation."""

    ok: bool
    returncode: int
    stdout: str
    stderr: str
    timed_out: bool = False
    cmd: list[str] = field(default_factory=list)

    def as_tool_result(self) -> ToolResult:
        status = (ToolStatus.OK if self.ok
                  else ToolStatus.TIMEOUT if self.timed_out
                  else ToolStatus.ERROR)
        return ToolResult(status=status,
                          output=(self.stdout + self.stderr).strip(),
                          metadata={"returncode": self.returncode})


class Sandbox:
    def __init__(self, workdir: Path, default_timeout: int = 30,
                 allow_network: bool = False, max_memory_mb: int = 512,
                 mem_limit: str = "data", backend: str = "auto",
                 docker_image: str = "python:3.11-slim",
                 docker_mem_limit: str = "256m",
                 docker_nano_cpus: int = 1_000_000_000):
        self.workdir = Path(workdir)
        self.workdir.mkdir(parents=True, exist_ok=True)
        self.default_timeout = default_timeout
        self.allow_network = allow_network
        self.max_memory_mb = max_memory_mb
        self.mem_limit = mem_limit  # "data" | "as" | "off"
        self.backend = backend      # "auto" | "restricted" | "subprocess" | "docker"
        self.docker_image = docker_image
        self.docker_mem_limit = docker_mem_limit
        self.docker_nano_cpus = docker_nano_cpus
        self._docker_client = None  # lazy: avoids hard docker dependency

    # ------------------------------------------------------------------ #
    # Tier 1: restricted subprocess
    # ------------------------------------------------------------------ #
    def _child_limits(self):
        """Resource limits + privilege drop, applied inside the child.

        NOTE: `preexec_fn` runs after fork; keep it minimal.  If the
        parent is heavily multithreaded, prefer the Docker backend.
        """
        def setup() -> None:
            if resource is not None:
                try:
                    resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
                    # RLIMIT_AS is disabled by default: on some platforms
                    # (e.g. Android/Termux) it aborts CPython at startup.
                    # RLIMIT_DATA is enforced for anonymous mmap on modern
                    # Linux and is startup-safe everywhere.
                    if self.mem_limit == "data":
                        resource.setrlimit(
                            resource.RLIMIT_DATA,
                            (self.max_memory_mb * 1024 * 1024,) * 2)
                    elif self.mem_limit == "as":
                        resource.setrlimit(
                            resource.RLIMIT_AS,
                            (self.max_memory_mb * 1024 * 1024,) * 2)
                    resource.setrlimit(resource.RLIMIT_NOFILE, (64, 64))
                except (ValueError, OSError):
                    pass
            # Drop to an unprivileged user when running as root.
            if pwd is not None and hasattr(os, "geteuid") and os.geteuid() == 0:
                try:
                    nobody = pwd.getpwnam("nobody")
                    os.setgid(nobody.pw_gid)
                    os.setuid(nobody.pw_uid)
                except (KeyError, PermissionError, OSError):
                    pass
        return setup

    def run_command(self, cmd: list[str], env: dict | None = None,
                    timeout: int | None = None,
                    cwd: str | Path | None = None,
                    inherit_env: bool = False) -> SandboxResult:
        """
        Run a command in a fresh process group with limits + scoped env.

        `env` is the ONLY place secrets should be injected — never argv.
        """
        timeout = timeout or self.default_timeout
        workdir = Path(cwd) if cwd else self.workdir

        child_env = dict(_BASE_ENV)
        child_env["HOME"] = str(workdir)
        if inherit_env:
            child_env.update(os.environ)   # opt-in only
        child_env.update(env or {})        # scoped secrets land here

        try:
            proc = subprocess.Popen(
                cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                cwd=str(workdir), env=child_env,
                preexec_fn=self._child_limits(),
                start_new_session=True,    # own process group -> clean kill
            )
        except FileNotFoundError:
            # Missing binary (e.g. gh not installed) -> clean error.
            return SandboxResult(
                ok=False, returncode=127,
                stdout="", stderr=f"command not found: {cmd[0]!r}",
                cmd=cmd)

        try:
            out, err = proc.communicate(timeout=timeout)
            return SandboxResult(
                ok=proc.returncode == 0, returncode=proc.returncode,
                stdout=out.decode(errors="replace"),
                stderr=err.decode(errors="replace"), cmd=cmd)
        except subprocess.TimeoutExpired:
            try:
                os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
            except (ProcessLookupError, PermissionError):
                proc.kill()
            out, err = proc.communicate()
            return SandboxResult(
                ok=False, returncode=-1, timed_out=True,
                stdout=out.decode(errors="replace"),
                stderr=err.decode(errors="replace"), cmd=cmd)

    # ------------------------------------------------------------------ #
    # Tier 2/3 dispatch for run_python
    # ------------------------------------------------------------------ #
    def run_python(self, code: str, timeout: int = 10) -> SandboxResult:
        """
        Evaluate untrusted Python, honoring the configured backend:

          docker      -> ephemeral container (RAM/CPU caps, no network,
                         hard kill timeout)
          subprocess  -> child interpreter with resource limits
          restricted  -> RestrictedPython, whitelisted builtins
          auto        -> RestrictedPython when installed, else subprocess
        """
        if self.backend == "docker":
            if self._get_docker_client() is not None:
                return self.run_docker(["python", "-c", code], timeout=timeout)
            logger.warning("docker backend requested but unavailable; "
                           "falling back to restricted execution")
        elif self.backend == "subprocess":
            return self.run_command([sys.executable, "-c", code],
                                    timeout=timeout)
        return self._run_restricted_python(code, timeout)

    # ------------------------------------------------------------------ #
    # Tier 2: restricted in-process Python
    # ------------------------------------------------------------------ #
    def _run_restricted_python(self, code: str,
                               timeout: int = 10) -> SandboxResult:
        """
        Evaluate untrusted pure-Python code with a whitelisted builtin set.

        No imports, no file I/O, no eval.  This protects against
        accidental damage, NOT against a determined attacker — use the
        Docker backend for hard isolation.
        """
        try:
            from RestrictedPython import compile_restricted, safe_builtins
            from RestrictedPython.PrintCollector import PrintCollector
        except ImportError:
            # Last-resort fallback: subprocess interpreter with limits.
            logger.warning("RestrictedPython not installed; "
                           "using subprocess fallback for run_python")
            return self.run_command([sys.executable, "-c", code], timeout=timeout)

        # Guards compiled into the restricted bytecode (version-proof
        # pass-through implementations; see module docstring for limits).
        def _safe_getattr(obj, name, default=None):
            if name.startswith("_"):
                raise AttributeError(f"attribute {name!r} is forbidden")
            return getattr(obj, name, default)

        def _allow_write(obj, *args, **kwargs):
            return obj      # in-memory writes only; no FS builtins exist

        def _passthrough(iterable, *args, **kwargs):
            return iterable

        def _getiter(iterable):
            return iter(iterable)   # allow 'for x in seq' over safe builtins

        builtins = {k: v for k, v in dict(safe_builtins).items()
                    if k not in ("__import__", "input", "open")}
        restricted_globals = {
            "__builtins__": builtins,
            "_print_": PrintCollector,          # print is rewritten to this
            "_getattr_": _safe_getattr,
            "_write_": _allow_write,
            "_unpack_sequence_": _passthrough,
            "_iter_unpack_sequence_": _passthrough,
            "_getiter_": _getiter,
        }

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            try:
                bytecode = compile_restricted(code, "<agent-sandbox>", "exec")
            except (SyntaxError, TypeError) as exc:
                return SandboxResult(ok=False, returncode=-1, stdout="",
                                     stderr=f"SyntaxError: {exc}",
                                     cmd=["restricted-python"])
        try:
            exec(bytecode, restricted_globals)
        except Exception as exc:   # runtime errors surface to the agent
            return SandboxResult(ok=False, returncode=-1, stdout="",
                                 stderr=f"{type(exc).__name__}: {exc}",
                                 cmd=["restricted-python"])

        collector = restricted_globals.get("_print")
        printed = collector() if collector is not None else ""
        return SandboxResult(ok=True, returncode=0,
                             stdout=printed, stderr="",
                             cmd=["restricted-python"])

    # ------------------------------------------------------------------ #
    # Tier 3: Docker container isolation
    # ------------------------------------------------------------------ #
    def _get_docker_client(self):
        """Lazily build the Docker client; None when unavailable."""
        if self._docker_client is None:
            try:
                import docker  # lazy: OS boots fine without docker-py
                self._docker_client = docker.from_env()
                logger.info("Docker sandbox backend ready")
            except Exception as exc:
                logger.warning("Docker unavailable (%s); "
                               "falling back to subprocess sandbox", exc)
                self._docker_client = False
        return self._docker_client or None

    def run_docker(self, cmd: list[str], image: str | None = None,
                   timeout: int | None = None, mem_limit: str | None = None,
                   nano_cpus: int | None = None,
                   network_mode: str | None = None) -> SandboxResult:
        """
        Run a command in an ephemeral container with hard blast-radius caps:

          * RAM limit (default 256m) and 1-CPU cap (nano_cpus)
          * no network egress by default (network_mode="none")
          * no new privileges, all capabilities dropped
          * hard kill after `timeout` seconds; container always removed
        """
        timeout = timeout or self.default_timeout
        client = self._get_docker_client()
        if client is None:
            return SandboxResult(ok=False, returncode=-1, stdout="",
                                 stderr="Docker backend unavailable", cmd=cmd)

        container = None
        try:
            container = client.containers.run(
                image=image or self.docker_image,
                command=cmd,
                detach=True,                 # run, then wait/kill explicitly
                network_mode=network_mode or ("none" if not self.allow_network
                                              else "bridge"),
                mem_limit=mem_limit or self.docker_mem_limit,
                nano_cpus=nano_cpus or self.docker_nano_cpus,
                pids_limit=64,               # fork-bomb guard
                cap_drop=["ALL"],            # drop every Linux capability
                security_opt=["no-new-privileges:true"],
                remove=False,                # we remove explicitly in finally
            )
            wait_result = container.wait(timeout=timeout)
            returncode = int(wait_result.get("StatusCode", -1))
            logs = container.logs(stdout=True, stderr=True)
            text = logs.decode(errors="replace") if isinstance(logs, bytes) else str(logs)
            return SandboxResult(ok=returncode == 0, returncode=returncode,
                                 stdout=text, stderr="", cmd=cmd)
        except Exception as exc:
            # docker-py raises requests.exceptions.ReadTimeout on wait timeout
            timed_out = type(exc).__name__ == "ReadTimeout"
            text = ""
            if container is not None:
                try:
                    container.kill()         # hard kill: no graceful escape
                except Exception:
                    pass
                try:
                    logs = container.logs(stdout=True, stderr=True)
                    text = logs.decode(errors="replace") if isinstance(logs, bytes) else str(logs)
                except Exception:
                    pass
            return SandboxResult(
                ok=False, returncode=-1, timed_out=timed_out,
                stdout=text if timed_out else "",
                stderr="" if timed_out else f"docker error: {exc}",
                cmd=cmd)
        finally:
            if container is not None:
                try:
                    container.remove(force=True)
                except Exception:
                    pass
