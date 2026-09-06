#!/usr/bin/env python3
"""Collect every fenced block-markup example in the repo into one file so the
whole set can be validated in a single editor round-trip.

Usage:  python3 tools/extract-examples.py OUT.html [file.md ...]

Fences opened as ```html are collected. Add <!-- skip-validate --> on the line
before a fence to exclude a deliberately-invalid example (the "don't do this"
snippets). A manifest is written next to OUT.html so failures can be traced
back to the source file and line.
"""
import json
import pathlib
import re
import sys

FENCE = re.compile(r"^```html\s*$")
END = re.compile(r"^```\s*$")
SKIP = "<!-- skip-validate -->"


def collect(path):
    out = []
    lines = path.read_text().splitlines()
    i = 0
    while i < len(lines):
        if FENCE.match(lines[i]):
            skip = i > 0 and SKIP in lines[i - 1]
            start = i + 1
            j = start
            while j < len(lines) and not END.match(lines[j]):
                j += 1
            body = "\n".join(lines[start:j])
            if not skip and "wp:" in body:
                out.append({"file": str(path), "line": start + 1, "body": body})
            i = j + 1
        else:
            i += 1
    return out


def main():
    out_path = pathlib.Path(sys.argv[1])
    sources = [pathlib.Path(p) for p in sys.argv[2:]] or sorted(pathlib.Path(".").glob("kadence-*.md"))
    examples = []
    for src in sources:
        examples.extend(collect(src))

    chunks = []
    for n, ex in enumerate(examples):
        # Two examples in one document must not share a uniqueID, or Kadence's
        # generated CSS collides. Rewrite by exact ID value rather than by class
        # prefix: the class formulas differ per block (some concatenate, some
        # hyphenate) and prefix matching mangles fixed classes like
        # `kt-svg-icon-list-item-wrap`.
        body = ex["body"]
        ids = sorted(set(re.findall(r'"uniqueID":"([^"]+)"', body)), key=len, reverse=True)
        for uid in ids:
            body = body.replace(uid, f"x{n}_{uid}")
        chunks.append(body)
        ex["index"] = n
        ex["ids"] = ids

    out_path.write_text("\n\n".join(chunks) + "\n")
    manifest = out_path.with_suffix(".manifest.json")
    manifest.write_text(json.dumps(examples, indent=2) + "\n")
    print(f"{len(examples)} examples from {len(sources)} files -> {out_path}")
    for ex in examples:
        print(f"  [{ex['index']:3d}] {ex['file']}:{ex['line']}")


if __name__ == "__main__":
    main()
