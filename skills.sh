#!/bin/bash
# skills.sh — Install all skills for this harness
# Usage: bash skills.sh [category]
# Categories: all, design, dev, util
# Example: bash skills.sh design

set -e

# ── Third-party skills (not bundled in repo) ────
THIRD_PARTY_SKILLS=(
  "impeccable"
  "taste-skill"
)

echo "── Installing third-party skills ──"
for skill in "${THIRD_PARTY_SKILLS[@]}"; do
  echo "  → $skill"
  npx skills add "$skill" 2>/dev/null || echo "    ⚠ Failed: $skill (may need manual install)"
done

echo ""
echo "✓ Third-party skills installed."
echo "  Custom skills (design-styles, code-rules, cloudflare, web-perf) already in repo."
