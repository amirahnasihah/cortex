#!/usr/bin/env bash
# Apply GitHub rulesets from .github/rulesets/ via the REST API.
#
# Usage:
#   ./scripts/apply-rulesets.sh repo              # current repository
#   ./scripts/apply-rulesets.sh org               # organization (needs org admin)
#   ./scripts/apply-rulesets.sh repo --dry-run    # print actions only
#   ./scripts/apply-rulesets.sh repo --evaluate   # enforce in evaluate mode first
#
# Requires: gh CLI authenticated with admin:repo or admin:org scope.

set -euo pipefail

SCOPE="${1:-repo}"
DRY_RUN=false
EVALUATE=false

shift || true
while [ $# -gt 0 ]; do
  case "$1" in
    --dry-run) DRY_RUN=true ;;
    --evaluate) EVALUATE=true ;;
    *) echo "Unknown option: $1" >&2; exit 1 ;;
  esac
  shift
done

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RULESETS_DIR="$ROOT/.github/rulesets"
MANIFEST="$RULESETS_DIR/manifest.json"

if ! command -v gh >/dev/null 2>&1; then
  echo "gh CLI is required: https://cli.github.com/" >&2
  exit 1
fi

if ! command -v jq >/dev/null 2>&1; then
  echo "jq is required" >&2
  exit 1
fi

OWNER="${GITHUB_REPOSITORY_OWNER:-$(gh repo view --json owner -q .owner.login)}"
REPO="${GITHUB_REPOSITORY_NAME:-$(gh repo view --json name -q .name)}"

if [ "$SCOPE" != "repo" ] && [ "$SCOPE" != "org" ]; then
  echo "Scope must be 'repo' or 'org', got: $SCOPE" >&2
  exit 1
fi

mapfile -t FILES < <(jq -r --arg scope "$SCOPE" '.[$scope][]' "$MANIFEST")

if [ "${#FILES[@]}" -eq 0 ]; then
  echo "No rulesets listed for scope: $SCOPE" >&2
  exit 1
fi

list_rulesets() {
  if [ "$SCOPE" = "org" ]; then
    gh api "orgs/$OWNER/rulesets" --paginate
  else
    gh api "repos/$OWNER/$REPO/rulesets" --paginate
  fi
}

find_ruleset_id() {
  local name="$1"
  list_rulesets | jq -r --arg name "$name" '.[] | select(.name == $name) | .id' | head -1
}

apply_ruleset() {
  local relative_path="$1"
  local file="$RULESETS_DIR/$relative_path"

  if [ ! -f "$file" ]; then
    echo "Missing ruleset file: $file" >&2
    exit 1
  fi

  local payload name existing_id
  payload="$(jq -c '.' "$file")"

  if [ "$EVALUATE" = true ]; then
    payload="$(echo "$payload" | jq '.enforcement = "evaluate"')"
  fi

  name="$(echo "$payload" | jq -r '.name')"
  existing_id="$(find_ruleset_id "$name" || true)"

  if [ "$DRY_RUN" = true ]; then
    if [ -n "$existing_id" ]; then
      echo "[dry-run] UPDATE $name (id=$existing_id) ← $relative_path"
    else
      echo "[dry-run] CREATE $name ← $relative_path"
    fi
    return
  fi

  if [ -n "$existing_id" ]; then
    echo "Updating ruleset: $name (id=$existing_id)"
    if [ "$SCOPE" = "org" ]; then
      echo "$payload" | gh api --method PUT "orgs/$OWNER/rulesets/$existing_id" --input -
    else
      echo "$payload" | gh api --method PUT "repos/$OWNER/$REPO/rulesets/$existing_id" --input -
    fi
  else
    echo "Creating ruleset: $name"
    if [ "$SCOPE" = "org" ]; then
      echo "$payload" | gh api --method POST "orgs/$OWNER/rulesets" --input -
    else
      echo "$payload" | gh api --method POST "repos/$OWNER/$REPO/rulesets" --input -
    fi
  fi
}

echo "Applying ${#FILES[@]} ruleset(s) to scope=$SCOPE owner=$OWNER"
if [ "$SCOPE" = "repo" ]; then
  echo "Repository: $OWNER/$REPO"
fi

for relative_path in "${FILES[@]}"; do
  apply_ruleset "$relative_path"
done

echo "Done."
