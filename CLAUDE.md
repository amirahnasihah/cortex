# dotclaude — portable AI harness

Personal workflow harness: conventions, templates, AI tool config, and skills manifest for frontend work (expanding to backend, cloud, IoT).

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

Skills are **not bundled** in this repo — install on demand via `skills.sh`.

```bash
bash skills.sh          # install all
bash skills.sh design   # design & frontend only
bash skills.sh dev      # dev tools only
bash skills.sh util     # utilities only
```

Available skill categories:
- **design**: impeccable, taste-skill, frontend-design, web-design-guidelines
- **dev**: remotion-best-practices, remotion-render
- **util**: find-skills, skill-creator

If a skill is missing when invoked, run `bash skills.sh <category>` to install it.
