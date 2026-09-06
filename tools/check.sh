#!/usr/bin/env bash
# Run every static check in the repo.
#
# The editor-validation step needs a running WordPress with Kadence Blocks
# installed; this script prepares the file for it and tells you what to run.
set -euo pipefail
cd "$(dirname "$0")/.."

echo "== attribute + type + kbVersion + tab-anchor lint =="
python3 tools/lint-attributes.py kadence-*.md SKILL.md reference/save-markup.md

echo
echo "== live page fixtures =="
python3 tools/lint-attributes.py tests/pages/*.html

OUT="${1:-/tmp/kadence-examples.html}"
echo
echo "== example extraction =="
python3 tools/extract-examples.py "$OUT" | tail -n 1

cat <<MSG

Static checks passed. To validate the markup against a real editor, run the
WordPress Studio MCP validate_blocks tool against:

  $OUT

Everything must come back valid with no auto-fix applied. An auto-fix means a
pattern file is wrong — read the diff and correct the source .md, never the
extracted file.
MSG
