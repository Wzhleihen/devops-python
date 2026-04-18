#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 1 ]; then
  echo "Usage: ./openspec/tools/summarize_tasks.sh <change-name> [markdown|json] [output-path]"
  exit 1
fi

CHANGE_NAME="$1"
FORMAT="${2:-markdown}"
OUTPUT_PATH="${3:-}"

CMD=(python "G:/SRE/devops-python/code/openspec/tools/task_checklist_summary.py" --change "$CHANGE_NAME" --format "$FORMAT")

if [ -n "$OUTPUT_PATH" ]; then
  CMD+=(--output "$OUTPUT_PATH")
fi

"${CMD[@]}"
