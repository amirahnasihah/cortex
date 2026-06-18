# cortex — portable AI engineering harness

Personal workflow harness: skills, conventions, design tokens, and AI tool config that travel across projects and frameworks.

## What cortex IS

A **portable AI harness** — not a template repo. Call skills from any project directory, any framework (Next.js, Nuxt, Astro, Svelte, etc.), and the AI follows your conventions. The harness travels with you; the project doesn't need to know about it.

**Domains** (current and planned):
- **Frontend & Design** — Tailwind v4 oklch tokens, shadcn, design specs, typography
- **Cloud** — Cloudflare Workers, AWS (expanding)
- **Backend** — Node/Bun, Hono, Drizzle (expanding)
- **IoT** — ESP32, MQTT, embedded (expanding)

## How to use

From any repo:
1. Call `/design-styles` — applies oklch tokens, Tailwind v4 theme, shadcn conventions
2. Call `/code-rules` — applies TypeScript conventions, AGENTS.md scaffold
3. AI reads your conventions and generates the right structure for the framework you're using

No template cloning. No folder copying. The skills ARE the template.

## .claude

- **.claude/settings.json** — Shared project settings (committed). Edit to add allowed permissions or MCPs for the whole repo.
- **.claude/settings.local.json** — Local-only settings (gitignored). Use for machine-specific MCPs (e.g. Figma, microCMS) or extra permissions.

## Skills

Custom skills live in `.agents/skills/` (cross-platform — works with Claude Code, Cursor, Copilot, Gemini CLI).

**Custom skills** (committed in repo, `.agents/skills/`):
- **design-styles** — Tailwind v4 oklch token theme + shadcn, stack-agnostic
- **code-rules** — TypeScript/engineering conventions + AGENTS.md scaffold

**Third-party skills** (not bundled, install via `bash install-skills.sh`):
- impeccable, taste-skill
- Browse more at [skills.sh](https://www.skills.sh/)

## Docs

- **docs/conventions.md** — Naming conventions (camelCase / PascalCase / kebab-case), folder structure patterns, design system tokens. Single source of truth across projects.
- **docs/design-spec-template.md** — One-pager design spec to copy per project; fill from Figma or brief.
- **docs/ai-tool-stack-and-mcp.md** — MCP philosophy and AI-aware dev environment reference.
- **docs/tailwind-v4/** — Tailwind v4 reference docs (framework-agnostic).
- **docs/frameworks/** — Per-framework llms.txt summaries (Next, Nuxt, Astro). Regenerate with scripts in `scripts/frameworks/`.
- **docs/cloud/** — Cloud certification study materials (AWS, Azure, GCP, K8s).
- **docs/languages/** — Language and tooling references.

## MCP Servers

Project-scope MCP configs go in `.mcp.json` (gitignored — copy from `.mcp.json.example`).

Recommended MCPs for this harness:
- **Chrome DevTools** — browser debugging, screenshots, DOM inspection
- **Playwright** — browser automation, testing, form filling
- **Supabase** — database, auth, edge functions
- **Sanity** — headless CMS content management
- **Figma** — design-to-code, component sync
- **Context7** — live library/framework docs lookup
- **Cloudflare** — Workers, Pages, KV, D1, R2, AI, DNS, and platform API management
