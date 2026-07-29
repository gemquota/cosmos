"""Configuration for the RSIS3 ↔ mykb memory bridge.

The bridge discovers mykb's wiki path via:

1. Environment variable ``MYKB_WIKI_PATH``
2. A ``.memory_bridge.json`` config file in the project root
3. Default: ``~/dev/codex/mykb/wiki`` (the canonical mykb location)
"""

import json
import os
from pathlib import Path
from typing import Optional

# Default: the canonical mykb location (not the copy in this dir)
_DEFAULT_WIKI = Path.home() / 'dev' / 'codex' / 'mykb' / 'wiki'


def resolve_wiki_path() -> Path:
    """Resolve the mykb wiki directory.

    Priority:
      1. ``MYKB_WIKI_PATH`` environment variable
      2. ``<project_root>/.memory_bridge.json`` → ``wiki_root`` key
      3. ``~/dev/codex/mykb/wiki`` (canonical location)
    """
    # 1. Env var
    env = os.environ.get('MYKB_WIKI_PATH')
    if env:
        p = Path(env)
        if p.exists():
            return p.resolve()

    # 2. Config file in project root
    pkg_root = Path(__file__).resolve().parent
    for candidate in [pkg_root.parent, pkg_root.parent.parent]:
        cfg = candidate / '.memory_bridge.json'
        if cfg.exists():
            try:
                data = json.loads(cfg.read_text())
                wiki = Path(data.get('wiki_root', ''))
                if wiki.is_absolute():
                    if wiki.exists():
                        return wiki.resolve()
                else:
                    resolved = (candidate / wiki).resolve()
                    if resolved.exists():
                        return resolved
            except (json.JSONDecodeError, KeyError):
                pass

    # 3. Default canonical location
    return _DEFAULT_WIKI.resolve()


def resolve_mykb_daemon() -> Path:
    """Resolve the mykb ``.wiki-daemon/`` directory."""
    wiki = resolve_wiki_path()
    daemon = wiki.parent / '.wiki-daemon'
    return daemon.resolve() if daemon.exists() else daemon


def write_config(wiki_root: str | Path, config_path: Optional[Path] = None):
    """Write a ``.memory_bridge.json`` config file for persistence."""
    if config_path is None:
        config_path = Path(__file__).resolve().parent.parent / '.memory_bridge.json'
    data = {'wiki_root': str(wiki_root)}
    config_path.write_text(json.dumps(data, indent=2) + '\n')
