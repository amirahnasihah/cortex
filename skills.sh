#!/bin/bash
# skills.sh — Install all skills for this harness
# Usage: bash skills.sh [category]
# Categories: all, design, dev, util
# Example: bash skills.sh design

set -e

# ── Design & Frontend ────────────────────────────
DESIGN_SKILLS=(
  "impeccable"
  "taste-skill"
  "frontend-design"
  "web-design-guidelines"
)

# ── Dev Tools ────────────────────────────────────
DEV_SKILLS=(
  "remotion-best-practices"
  "remotion-render"
)

# ── Utilities ────────────────────────────────────
UTIL_SKILLS=(
  "find-skills"
  "skill-creator"
)

install_skills() {
  local label=$1
  shift
  local skills=("$@")
  echo "── Installing $label skills ──"
  for skill in "${skills[@]}"; do
    echo "  → $skill"
    npx skills add "$skill" 2>/dev/null || echo "    ⚠ Failed: $skill (may need manual install)"
  done
  echo ""
}

category="${1:-all}"

case "$category" in
  design)
    install_skills "Design" "${DESIGN_SKILLS[@]}"
    ;;
  dev)
    install_skills "Dev" "${DEV_SKILLS[@]}"
    ;;
  util)
    install_skills "Utilities" "${UTIL_SKILLS[@]}"
    ;;
  all)
    install_skills "Design" "${DESIGN_SKILLS[@]}"
    install_skills "Dev" "${DEV_SKILLS[@]}"
    install_skills "Utilities" "${UTIL_SKILLS[@]}"
    ;;
  *)
    echo "Usage: bash skills.sh [all|design|dev|util]"
    exit 1
    ;;
esac

echo "✓ Done. Skills installed to .agents/skills/"
