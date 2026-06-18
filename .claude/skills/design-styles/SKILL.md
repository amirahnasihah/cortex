---
name: design-styles
description: Apply a reusable design system — Tailwind v4 token theme + shadcn
  reusable UI components (manual install, owned in-repo), themed via tweakcn-style
  oklch CSS variables. The token/theme layer is stack-agnostic; the shadcn port
  follows the framework (React/Vue/Svelte). Use when styling UI, setting up a
  theme, adding reusable components, translating Figma to tokens, or when the
  user asks to follow "our design rules" / "our design system".
---

# Design system — Tailwind + shadcn + tweakcn

Two layers:
1. **Design system / theme** — Tailwind v4 CSS-variable tokens in **oklch**,
   generated/edited tweakcn-style. **Stack-agnostic** — same tokens everywhere.
2. **Reusable UI** — **shadcn components, manually installed** (copied into the
   repo, owned and customized — not a black-box dependency). The port depends on
   the framework: React → shadcn/ui, Vue/Nuxt → shadcn-vue, Svelte → shadcn-svelte.

Full design reference lives in the repo's `docs/` (`conventions.md` colors,
`design-spec-template.md`). Drive the look from a per-client design spec.
Concrete artifacts (theme, shadcn setup, stack docs, taste refs) live in
`reference/` — see `reference/README.md`.

**Reusable by design:** the base system is constant across projects; only the
*values* change per client (color, typography, radius) and the *port* changes
per stack (Nuxt / Next / Astro …) and package manager (pnpm / bun / npm / yarn).

**Goal — anti-slop.** Aim for distinctive, modern, awwwards-tier, motion-forward
work — not templated AI defaults. See `reference/anti-slop.md` (+ the `impeccable`
/ `taste-skill` skills for taste judgment) and `reference/animation/motion-patterns.md`.

## When invoked (`/design-styles`)

Set up (or restyle) the design system in the current project:

1. **Detect the stack** from the repo before asking — `package.json` +
   config/lockfile: Nuxt / Next / Astro / SvelteKit, and the package manager
   (`pnpm-lock.yaml` → pnpm, `bun.lockb` → bun, `yarn.lock` → yarn, else npm).
2. **Theme source:**
   - **User pasted a tweakcn export** (a `:root` / `.dark` / `@theme inline`
     block)? → that **is** the theme. Drop it **verbatim** into the global
     stylesheet after `@import "tailwindcss";`. Don't rewrite the values.
   - Otherwise → start from `reference/theme/theme.css` (neutral default) and
     tune, or generate at tweakcn.com and paste back.
3. **Ask only what's unresolved** (keep it to a few):
   - Stack / package manager (if not detected)
   - Dark mode? (include `.dark` + `@custom-variant dark`)
   - Animation? (GSAP for motion; Lenis smooth-scroll only if asked)
   - i18n? (Nuxt, optional)
4. **Install** per `reference/shadcn/manual-install.md`: deps (chosen PM) →
   `cn()` util → theme CSS into the global stylesheet → shadcn components into
   the ui dir (framework port).
5. **Verify:** `bg-background` / `text-foreground` resolve; dark toggle works.

A pasted tweakcn block is the source of truth — it may also carry `sidebar-*`,
`shadow-*` (+ `--shadow-x/y/blur/…`), `--tracking-*`, `--spacing`,
`@custom-variant dark`, and an `@layer base` reset. **Keep them all** and map
any extras in `@theme inline`.

## Theme tokens (the stack-agnostic constant)

Use the shadcn **semantic token** set as CSS variables, values in **oklch**,
with light + `.dark` blocks. Generate/tune with **tweakcn**, then paste into the
project's global stylesheet. In Tailwind v4, map vars to utilities with
`@theme inline`.

```css
:root {
  --background: oklch(1 0 0);
  --foreground: oklch(0.145 0 0);
  --primary: oklch(0.62 0.19 27);          /* Figma brand #E5484D */
  --primary-foreground: oklch(0.985 0 0);
  --muted: oklch(0.97 0 0);
  --muted-foreground: oklch(0.556 0 0);
  --border: oklch(0.922 0 0);
  --ring: oklch(0.62 0.19 27);
  --radius: 0.625rem;
  /* typography = per-project placeholder; swap families, keep names (a slot, not a rule) */
  --font-sans: ui-sans-serif, system-ui, sans-serif;
  --font-serif: ui-serif, Georgia, serif;
  --font-mono: ui-monospace, monospace;
  /* ...card, popover, secondary, accent, destructive, input, chart-1..5 */
}
.dark {
  --background: oklch(0.145 0 0);
  --foreground: oklch(0.985 0 0);
  /* ...dark values */
}

@theme inline {
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --color-primary: var(--primary);
  --color-primary-foreground: var(--primary-foreground);
  /* ...map the rest → enables bg-primary, text-muted-foreground, etc. */
  --font-sans: var(--font-sans);           /* → font-sans / font-serif / font-mono */
  --font-serif: var(--font-serif);
  --font-mono: var(--font-mono);
  --radius-lg: var(--radius);
}
```

Rules:
- **oklch always.** tweakcn outputs oklch; keep it. If a Figma var arrives as
  hex, convert at the boundary and leave the hex as a comment (audit trail).
- **Reference tokens, never hardcode** — use `bg-primary`, `text-foreground`,
  `border-border`; no raw oklch/hex in components.
- **Customize the palette per client** in `:root` / `.dark`; the token *names*
  stay constant so components don't change.

## shadcn — manual installation

Stack- and PM-agnostic. Install deps with the project's package manager (`pnpm`
/ `bun` / `npm` / `yarn`). Use the CLI to scaffold then own the output, or go
fully manual (CLI-free, no `components.json`).

1. **Deps:** `clsx`, `tailwind-merge`, `class-variance-authority`, an icon set
   (e.g. `lucide-*`). Optionally the Tailwind v4 animation helper
   (`tw-animate-css`).
2. **`cn()` util** in your utils module — `twMerge(clsx(...))`.
3. **Theme CSS** — paste the tweakcn tokens + `@theme inline` mapping (above)
   into the project's global stylesheet.
4. **Components** — copy source into the ui components dir. You **own** them:
   edit variants (via cva), spacing, radius to match the client design.
5. **`components.json`** *(optional)* — only when driving the CLI.

Use the framework's port for component source (shadcn / shadcn-vue /
shadcn-svelte) — the theme layer above is identical across all of them. Paths
vary by stack (Nuxt `app/`, Next `app/`/`src/`, Astro `src/`); see
`reference/shadcn/manual-install.md` and `reference/stack-docs.md`.

## Conventions

- **Tailwind-first.** If Tailwind can do it, use Tailwind utilities — avoid pure
  CSS. Reach for hand-written CSS only when Tailwind genuinely can't express it.
- Reusable, composable primitives in `components/ui/`; compose feature
  components on top.
- Promote repeated utility patterns into cva variants or tokens. Any unavoidable
  custom CSS class: kebab-case.
- Keep `--radius`, spacing, and typography as tokens so the whole system
  re-themes from one place.

## Animation

- **GSAP** (+ ScrollTrigger) is the animation plugin, paired with Tailwind for
  static styling. Drive motion with GSAP; keep layout/styles in Tailwind.
- **Lenis** for smooth scroll — **optional, only when the client/design asks**.
  Don't add it by default.
- **Awwwards-tier toolkit** (scroll scrub/pin/parallax, split-text reveal, page
  transitions; GSAP + Motion/Framer) → `reference/animation/motion-patterns.md`.

## Guardrails (design-scoped)

- **oklch always.** Paste tweakcn output verbatim; convert Figma hex at the
  boundary and keep the hex as a comment. Don't hand-tune oklch you didn't generate.
- **Reference tokens, never hardcode** — `bg-primary`, `text-muted-foreground`,
  `border-border`. No raw oklch/hex or literal `bg-gray-100` in components.
- **Semantic tokens only in reusable `ui/` primitives** so they survive `.dark`
  / re-theming. Literal brand-chrome colors only in fixed-identity pages.
- **Tailwind-first.** No hand-written CSS rulesets or inline `style` for anything
  Tailwind can express; keyframes go in `@theme`, used via `animate-*`.
- **Own the components** (manual shadcn). A registry is a research source —
  rewrite what you pull to these tokens; don't paste foreign tokens/radii in.
- **Per client/stack:** change token *values* and paths — never token *names*.
- **Don't vendor docs** (link / context7) — the offline `tailwind-v4/` copy is
  the one intentional exception.

**Out of scope:** general engineering rules (TS strict, JSDoc, secrets, dev
workflow, AGENTS.md generation) don't belong here — they live in the project's
conventions / AGENTS.md, not in this design skill.

## Note

This **supersedes** the repo's old "no shadcn" stance for projects that follow
this skill — shadcn is used here, manually installed and owned. If a client
brief forbids it, fall back to custom Tailwind with the same token theme.
