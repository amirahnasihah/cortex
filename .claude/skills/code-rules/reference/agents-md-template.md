# AGENTS.md template

Copy to the project root as `AGENTS.md`; fill the `[placeholders]`. Keep it
short — **link out** to the design guidelines and conventions rather than
inlining them, so there's one source of truth.

---

```md
# Agent guidance — [PROJECT_NAME]

## Design

Before generating/modifying any UI, component, or animation, read:

- `guidelines/design-refs.md` — taste profile, motion language, inspiration
- `guidelines/shadcn-patterns.md` — how `ui/` primitives are built
- `guidelines/registries.md` — where to mine component patterns

(These come from the `design-styles` skill.)

## Stack

- Framework: [Nuxt 4 / Next / Astro / SvelteKit]
- Package manager: [pnpm / bun / npm / yarn]
- Dev port: [3000]

```bash
[pm] install     # install deps
[pm] dev         # dev server
[pm] build       # production build (also typecheck)
[pm] preview     # preview build
[pm] format      # format + lint
```

## Conventions

TypeScript strict; no `any` (use `unknown`); avoid `as`; arrow functions.
JSDoc block atop every component/page/util/hook. kebab-case files/folders.
Full rules: the `code-rules` skill.

## Secrets

Never print or request secrets; redact in output; use authenticated CLIs.

## Workflow

Clarify unclear instructions. After changes: typecheck/build, no errors, tests
pass. Update README/AGENTS.md on new package/script.
```
