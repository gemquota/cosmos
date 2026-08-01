#!/usr/bin/env python3
"""Standalone usage-practice check for an RSIS3 workspace.

Usage:
    python3 ops/check_practices.py [WORKSPACE]

Without an argument, uses RSIS_WORKSPACE or the current directory. Exits
non-zero if any practice is violated. Same checks as `python -m rsis
check-practices`.
"""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from rsis.practices import run_checks  # noqa: E402


def main() -> int:
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    workspace = Path(arg) if arg else Path(os.environ.get("RSIS_WORKSPACE", "."))
    return run_checks(workspace)


if __name__ == "__main__":
    sys.exit(main())
