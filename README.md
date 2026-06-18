# standard-repo

GitHub template for project scaffolding: CI/CD, release automation, issue workflow, and multi-provider deployments.

## Quick start

1. **Use this template** → create a new repo from `amirahnasihah/standard-repo`.
2. Copy `.env.example` → `.env` and fill in values locally.
3. When ready to deploy, copy from [`.github/examples/`](.github/examples/) (workflows + infra) — see [Deployment](#deployment-optional).
4. Add **GitHub secrets** when you enable deploy (see [Required secrets](#required-secrets)).
5. Create GitHub **environments** `staging` and `production` with optional approval gates.
6. Apply **rulesets** (see [Rulesets](#rulesets)) — protect `main`, `release`, and block secret commits.

## Branch model

```
feature branches  →  main (staging)  →  release (production)
     ↑                      ↑                    ↑
  PR from issue           CI only (no deploy     release PR + tag
                          until you copy from
                          examples/)
```

| Branch | Purpose |
|--------|---------|
| `main` | Integration branch. CI runs on push/PR. |
| `release` | Production-ready code. Release PRs merge here; tags published on merge. |
| `addition/*`, `fix/*`, etc. | Feature branches created automatically when an issue is assigned. |

## Workflow overview

| Workflow | Trigger | What it does |
|----------|---------|--------------|
| [CI](.github/workflows/ci.yml) | Push/PR to `main`, `develop` | Lint, test, build (Bun/Node if `package.json` exists) |
| [Run Tests](.github/workflows/run-tests.yml) | Review requested / `ci-testing` label | Extra test run on demand |
| [Start Pull Request](.github/workflows/start-pull-request.yml) | Issue assigned | Creates branch + draft PR from issue |
| [Prepare Release](.github/workflows/prepare-release.yml) | Push to `main` | Opens `main` → `release` PR via git-pr-release |
| [Release](.github/workflows/release.yml) | Release PR merged | Publishes CalVer GitHub Release |
| [Apply Rulesets](.github/workflows/apply-rulesets.yml) | Manual | Sync rulesets from JSON to GitHub |

### Deployment (optional)

Not active by default. Copy from [`.github/examples/workflows/`](.github/examples/workflows/) when you have an app + host:

| Example workflow | Trigger (once copied) | What it does |
|------------------|----------------------|--------------|
| [deploy-cloudflare.yml](.github/examples/workflows/deploy-cloudflare.yml) | Push `main`, release, manual | Wrangler deploy |
| [deploy-vercel.yml](.github/examples/workflows/deploy-vercel.yml) | Push `main`, PR, release, manual | Vercel deploy + PR preview |
| [deploy-hetzner.yml](.github/examples/workflows/deploy-hetzner.yml) | Push `main`, release, manual | Docker → SSH deploy |

→ [`.github/examples/README.md`](.github/examples/README.md)

## Rulesets

Rulesets are **not** auto-applied from files (unlike Actions workflows). JSON definitions live in [`.github/rulesets/`](.github/rulesets/) and are reusable in three ways:

| Method | Best for |
|--------|----------|
| **Org rulesets** (`org/*.json`) | One policy for all repos (`~ALL` or name patterns) |
| **Repo rulesets** (`repo/*.json`) | Single-repo projects from this template |
| **Import / script** | UI import or `./scripts/apply-rulesets.sh repo` |

```bash
./scripts/apply-rulesets.sh repo --evaluate   # test without blocking
./scripts/apply-rulesets.sh repo              # apply (upserts by name)
./scripts/apply-rulesets.sh org               # org-wide (org admin required)
```

After applying, add **GitHub Actions** to each branch ruleset's bypass list so release/PR automation can push. Full details: [`.github/rulesets/README.md`](.github/rulesets/README.md).

## Release flow (CalVer)

Releases use **Calendar Versioning** in Malaysia timezone (`Asia/Kuala_Lumpur`):

```
YYYY.MM.weekN.releaseM
```

Example: `2026.05.week4.release1` → release name `2026-05 Week 4（Release No.1）`

1. Merge PRs into `main`.
2. **Prepare Release** opens a PR from `main` → `release` (label: `release-candidate`).
3. Review and merge the release PR.
4. **Release** workflow publishes the GitHub Release and tag.
5. Production deploy runs when you copy deploy workflows from `examples/` and merge a release.

## Deployment (optional)

Deploy workflows live in [`.github/examples/workflows/`](.github/examples/workflows/) and **do not run on push** until copied to `.github/workflows/`. See [`.github/examples/README.md`](.github/examples/README.md).

## Issue → PR flow

1. Open an issue using a template (`addition`, `fix`, `modification`, etc.).
2. Assign yourself (or a teammate).
3. **Start Pull Request** creates a branch like `fix/i42-20260523-1430` and opens a PR.
4. Fill in the PR checklist and attach evidence before requesting review.

Issue types `idea`, `epic`, and `agenda` are excluded from auto-PR creation.

## Required secrets

Set in **Settings → Secrets and variables → Actions** (only when deploy workflows are enabled).

### Cloudflare (`examples/workflows/deploy-cloudflare.yml`)

| Secret | Description |
|--------|-------------|
| `CLOUDFLARE_API_TOKEN` | API token with Workers/Pages deploy scope |
| `CLOUDFLARE_ACCOUNT_ID` | Cloudflare account ID |

### Vercel (`examples/workflows/deploy-vercel.yml`)

| Secret | Description |
|--------|-------------|
| `VERCEL_TOKEN` | Vercel personal/team token |
| `VERCEL_ORG_ID` | Team or user ID |
| `VERCEL_PROJECT_ID` | Project ID |

### Hetzner / VPS (`examples/workflows/deploy-hetzner.yml`)

| Secret | Description |
|--------|-------------|
| `SSH_PRIVATE_KEY` | Private key for deploy user |
| `DEPLOY_HOST` | Server IP or hostname |
| `DEPLOY_USER` | SSH username |
| `DEPLOY_PORT` | Optional — default `22` |
| `DEPLOY_PATH` | Optional — default `/opt/app` |

Images are pushed to `ghcr.io/<owner>/app:<sha>` using `GITHUB_TOKEN`.

For **private** GHCR packages, add a `GHCR_PULL_TOKEN` secret (PAT with `read:packages`) so the server can pull the image. Alternatively, make the package public under GitHub Packages settings.

### CI security (optional)

| Secret | Description |
|--------|-------------|
| `SNYK_TOKEN` | Snyk vulnerability scanning |

## GitHub environments

Create two environments under **Settings → Environments**:

- **staging** — auto-deploy from `main`
- **production** — deploy on release; add required reviewers for safety

Deploy workflows reference these environment names when copied from `examples/`.

## Project structure

```
.
├── .github/
│   ├── workflows/          # Active CI, release, automation
│   ├── examples/           # Optional deploy workflows + infra
│   ├── rulesets/
│   ├── ISSUE_TEMPLATE/
│   └── release-drafter-config.yml
├── scripts/
│   └── apply-rulesets.sh
├── .env.example
└── .gitignore
```

## Customization checklist

- [ ] Update Discussions URL in `.github/ISSUE_TEMPLATE/config.yml`
- [ ] Add `package.json` (or remove Bun-specific CI steps)
- [ ] Configure GitHub environments + secrets (when using deploy)
- [ ] Apply rulesets (UI import or `./scripts/apply-rulesets.sh repo`)
- [ ] Copy deploy from `.github/examples/` when you have an app + host (optional)

## License

Apache 2.0 — see [LICENSE](LICENSE).
