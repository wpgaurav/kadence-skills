#!/usr/bin/env python3
"""Add "kbVersion":2 to the six blocks whose PHP render gates on it.

Without it those blocks fall back to a legacy path: rowlayout emits no wrapper
at all, testimonials render as a plain list, and column/infobox/googlemaps/
advancedgallery lose their modern classes. The markup still validates in the
editor, which is what makes this worth automating.
"""
import json
import pathlib
import re
import sys

GATED = {"rowlayout", "column", "infobox", "googlemaps", "advancedgallery", "testimonials"}
BLOCK = re.compile(r'<!--\s*wp:(kadence/[a-z0-9-]+)\s*(\{.*?\})\s*(/?)-->', re.S)


def patch(text):
    added = 0

    def repl(m):
        nonlocal added
        name, raw, close = m.group(1), m.group(2), m.group(3)
        if name.split("/")[1] not in GATED:
            return m.group(0)
        try:
            attrs = json.loads(raw)
        except json.JSONDecodeError:
            return m.group(0)
        if "kbVersion" in attrs:
            return m.group(0)
        attrs["kbVersion"] = 2
        added += 1
        return m.group(0).replace(raw, json.dumps(attrs, separators=(",", ":")), 1)

    return BLOCK.sub(repl, text), added


def main():
    total = 0
    for arg in sys.argv[1:]:
        p = pathlib.Path(arg)
        new, added = patch(p.read_text())
        if added:
            p.write_text(new)
            print(f"{arg}: +{added}")
        total += added
    print(f"total kbVersion added: {total}")


if __name__ == "__main__":
    main()
