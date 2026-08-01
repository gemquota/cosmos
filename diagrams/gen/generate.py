#!/usr/bin/env python3
"""Generate all COSMOS diagram SVGs + the interactive X++ omega page."""
import os, sys, xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from basic import BASIC
from advanced import ADVANCED
from expert import EXPERT
from abstract import ROUND3 as ABSTRACT
from conceptual import CONCEPTUAL
from semantic import SEMANTIC
from experimental import EXPERIMENTAL
from dynamics import DYNAMICS
from round6_basic import BASIC6
from round6_advanced import ADVANCED6
from round6_expert import EXPERT6
from expert_plus import EXPERT_PLUS
import omega

ALL = {}
for name, fn in {**BASIC, **ADVANCED, **EXPERT, **ABSTRACT, **CONCEPTUAL, **SEMANTIC,
                 **EXPERIMENTAL, **DYNAMICS, **BASIC6, **ADVANCED6, **EXPERT6,
                 **EXPERT_PLUS}.items():
    ALL[name] = fn


def main():
    for name, fn in ALL.items():
        path = os.path.join(OUT, name)
        svg = fn()
        with open(path, "w") as f:
            f.write(svg)
        # validate XML only (the X++ page is HTML and is written separately)
        try:
            ET.parse(path)
            status = "✅"
        except ET.ParseError as e:
            status = f"❌ {e}"
        print(f"{status}  {name}  ({os.path.getsize(path)//1024}KB)")
    omega.main()
    print(f"\nGenerated {len(ALL)} SVGs + 1 interactive HTML → {OUT}")

if __name__ == "__main__":
    main()
