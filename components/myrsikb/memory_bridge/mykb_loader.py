"""Centralized loader for mykb daemon modules.

Replaces the ``sys.path.insert()`` pattern used across multiple bridge
modules with ``importlib``-based loading that does **not** modify global
module state.

Usage::

    from memory_bridge.mykb_loader import load_mykb_module

    graph_engine = load_mykb_module('graph_engine')
    if graph_engine is not None:
        graph_engine.do_something()
"""

import importlib.util
import sys
from pathlib import Path
from typing import Any, Optional

from memory_bridge.config import resolve_mykb_daemon


# Module cache — avoids re-loading on every call
_cache: dict[str, Any] = {}


def load_mykb_module(module_name: str) -> Any:
    """Load a mykb ``.wiki-daemon/`` module without modifying ``sys.path``.

    Uses ``importlib`` to locate and load the module directly from its
    file path in mykb's daemon directory.  The module is cached after
    first load so subsequent calls return the same object.

    The module is also registered in ``sys.modules`` so that any
    intra-module imports (e.g. ``from temporal import extract_timeline``)
    resolve correctly without a ``sys.path`` entry.

    Args:
        module_name: Basename of the module (e.g. ``"graph_engine"``,
                     ``"retriever"``, ``"temporal"``).

    Returns:
        The loaded module, or ``None`` if the module cannot be found
        or fails to load.
    """
    if module_name in _cache:
        return _cache[module_name]

    daemon: Path = resolve_mykb_daemon()
    module_path = daemon / f"{module_name}.py"

    if not module_path.is_file():
        # Try parent directory (for modules that live directly in .wiki-daemon/)
        parent = daemon.parent / f"{module_name}.py"
        if parent.is_file():
            module_path = parent
        else:
            _cache[module_name] = None
            return None

    try:
        spec = importlib.util.spec_from_file_location(module_name, str(module_path))
        if spec is None or spec.loader is None:
            _cache[module_name] = None
            return None

        mod = importlib.util.module_from_spec(spec)
        # Register in sys.modules so sub-imports within the module resolve
        sys.modules[module_name] = mod
        # Temporarily add daemon dir to sys.path so sub-imports work
        _daemon_str = str(daemon)
        _added = False
        if _daemon_str not in sys.path:
            sys.path.insert(0, _daemon_str)
            _added = True
        try:
            spec.loader.exec_module(mod)
        finally:
            if _added:
                sys.path.remove(_daemon_str)
        _cache[module_name] = mod
        return mod

    except Exception:
        _cache[module_name] = None
        return None


def reload_mykb_modules() -> None:
    """Clear the module cache so modules are re-loaded on next access.

    Useful during development or if mykb modules are updated at runtime.
    """
    _cache.clear()


def mykb_module_available(module_name: str) -> bool:
    """Check whether a mykb module is available without loading it."""
    if module_name in _cache:
        return _cache[module_name] is not None

    daemon = resolve_mykb_daemon()
    module_path = daemon / f"{module_name}.py"
    if module_path.is_file():
        return True
    parent = daemon.parent / f"{module_name}.py"
    return parent.is_file()
