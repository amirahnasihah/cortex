# cortex — portable AI harness

Personal workflow harness: conventions, templates, AI tool config, and custom skills for AI-powered development.

## .claude

- **.claude/settings.json** — Shared project settings (committed). Edit to add allowed permissions or MCPs for the whole repo.
- **.claude/settings.local.json** — Local-only settings (add to .gitignore). Use for your machine-specific MCPs (e.g. Figma, microCMS) or extra permissions.

## What lives here

- **rules/global-cursor-rule.md** — Paste this into Cursor Settings → Rules → Global (role, i18n, custom design, no shadcn assumption).
- **docs/design-spec-template.md** — One-pager design spec to copy per project; fill from Figma or brief, then paste into Cursor when generating components.
- **templates/** — Reusable Nuxt 4 boilerplates: `nuxt-client-base/` (no i18n), `nuxt-client-i18n/` (multi-locale). Clone the one that fits each new client.
- **docs/** — Design spec template, **conventions** (`docs/conventions.md`), **nuxt-client-i18n** definition (`docs/nuxt-client-i18n.md`), **nuxt-client-i18n v2 project rules** (`docs/rules.md` — structure, naming, dependency direction, CMS/SEO/i18n/animation rules; follow when editing `templates/nuxt/nuxt-client-i18n/` or projects built from it), AI tool stack & MCP reference (`docs/ai-tool-stack-and-mcp.md`), doc links checklist (`docs/doc-links-checklist.md`).
- **rules/nuxt-client-conventions.mdc** — Copy into client projects’ `.cursor/rules/` so AI follows the same naming and structure.

## Conventions

- **Single source of truth:** **docs/conventions.md** — stack (Nuxt, TS, microCMS, Tailwind-first CSS, shadcn, optional i18n/GSAP/Lenis), naming (camelCase / PascalCase / kebab-case for files and folders), folder structure, modules, per-project choices. Reuse for new projects, other devs, and AI rules.
- Stack: Nuxt 4, Tailwind v4 (**Tailwind-first** — avoid pure CSS when Tailwind can do it), @nuxtjs/seo; i18n optional per template; custom design per client; **shadcn manual install** (owned in-repo) + tweakcn oklch theme.
- When editing templates, follow **docs/conventions.md** and Nuxt 4 default folder structure. For **nuxt-client-i18n** (and projects built from it), follow **docs/rules.md** (v2 project rules) — no structural or dependency drift.
- For full workflow (phases 1–4, prompt patterns), see the AI workflow upgrade plan.

## Skills

Custom skills live in `.agents/skills/` (cross-platform — works with Claude Code, Cursor, Copilot, Gemini CLI).

**Custom skills** (committed in repo, `.agents/skills/`):
- **design-styles** — Tailwind v4 oklch token theme + shadcn, stack-agnostic
- **code-rules** — TypeScript/engineering conventions + AGENTS.md scaffold

**Third-party skills** (not bundled, install via `bash install-skills.sh`):
- impeccable, taste-skill
- Browse more at [skills.sh](https://www.skills.sh/)

## MCP Servers

Project-scope MCP configs go in `.mcp.json` (gitignored — copy from `.mcp.json.example`).

Recommended MCPs for this harness:
- **Chrome DevTools** — browser debugging, screenshots, DOM inspection
- **Playwright** — browser automation, testing, form filling
- **Supabase** — database, auth, edge functions
- **Sanity** — headless CMS content management
- **Figma** — design-to-code, component sync
- **Context7** — live library/framework docs lookup
