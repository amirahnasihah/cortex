---
name: code-rules
description: Engineering conventions + AGENTS.md scaffolding for a project — TypeScript strict rules, JSDoc blocks, kebab-case naming + folder structure, secrets handling, and dev workflow. Generates or updates AGENTS.md and points it at the design-styles guidelines. Use when bootstrapping a project's agent guidance, writing/updating AGENTS.md or CLAUDE.md, or enforcing code conventions. Pairs with the design-styles skill (which owns the design layer only).
---

# Code rules — engineering conventions + AGENTS.md

Stack-agnostic engineering conventions and the AGENTS.md that carries them.
**Design is out of scope** — tokens, shadcn, taste live in the `design-styles`
skill. This skill owns code rules + the agent-guidance file.

## When invoked

1. **Detect** stack + package manager from the repo (lockfile/config) — don't
   ask if obvious.
2. **Generate or update `AGENTS.md`** from `reference/agents-md-template.md` —
   fill stack / PM / dev commands; point the Design section at the project's
   `guidelines/` (populated by `design-styles`).
3. **Apply** the rules below to new/edited code.
4. **Verify**: typecheck/build clean, no errors, tests pass if present.

## TypeScript

- `strict` mode on.
- **Boundaries take `unknown`, not `any`** — validate/parse into a typed shape
  (schema → `z.infer`, or a type guard). Past the boundary, everything is typed.
  *Parse, don't validate.*
- **Derive types, don't duplicate** — `z.infer`, `typeof`, `keyof`, `ReturnType`.
  One source of truth.
- **Make illegal states unrepresentable** — discriminated unions over
  optional/boolean soup.
- **`satisfies` over `as`**; no `!` non-null, no `as any` — narrow instead.
- `as const` + union literals over `enum`. Explicit return types on exported fns.
- Prefer arrow functions.

Detail + examples: `reference/typescript.md`.

## Code style

- Small, composable, functional components.
- Respect the formatter (biome / prettier) — don't fight it.
- Useful comments for complex logic; no generic noise.
- **JSDoc block at the top of every** component / page / util / hook — see
  `reference/jsdoc.md`.
- Less dependency; smaller chunks; update README/AGENTS.md on new package/script.

## Code design

- **Guard clauses / early return** over nested conditionals.
- **Pure core, side-effects at the edges** — isolate IO.
- **Immutable data; derive, don't sync** — no duplicated state that can drift.
- **Rule of three** before extracting an abstraction — avoid premature DRY.
- **No floating promises** — `await` or explicit `void`; `Promise.all` for
  independent work.
- **Never swallow errors** — no empty `catch`; `catch (e: unknown)` then narrow.
- **Test behavior, not implementation** — tests double as docs.
- Name by intent; booleans `isX` / `hasX` / `shouldX`.

## Naming & structure

- **kebab-case** for files and folders.
- `cva` variants **colocated** in each `ui/` component — no central `styles.ts`.

```
/components
  /ui          # primitives (button, input, badge, select…)
  /layout      # header, nav, footer, sidebar…
  /page        # per-page section components (top, about, contact…)
  /icon        # inline svg icon components
/layouts       # default.{vue,tsx,astro}
/composables   # or /hooks — use-custom-fetch.ts
/libs          # utils.ts → cn() + helpers
/types         # user.ts, product.ts
/data          # static / mock data
```

## Secrets & safety

- Never print secrets; never ask the user to paste them.
- Avoid commands that dump env/keys broadly; redact in any displayed output.
- Prefer existing authenticated CLIs.

## Dev workflow

- Clarify unclear instructions before coding.
- After changes: typecheck/build, ensure no errors, run tests if provided.

## Relationship to other docs

- **design-styles** — the design layer (tokens, shadcn, taste). This skill never
  duplicates it; AGENTS.md just links to it.
- **dotclaude `docs/conventions.md`** — Nuxt-client stack/naming specifics. Reuse
  it for Nuxt projects; this skill is the stack-agnostic superset.
