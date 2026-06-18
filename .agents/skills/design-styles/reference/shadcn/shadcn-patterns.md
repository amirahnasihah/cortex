# shadcn patterns — building `ui/` primitives

> Read before creating or modifying any `ui/` primitive. Long-form of the design
> system's shadcn rules; `SKILL.md` is the summary.

Manual shadcn install (<https://ui.shadcn.com/docs/installation/manual>): we
**own the source**. No reliance on the CLI at build time — copy the *idea*
(cva + `cn()` + `data-slot` + `asChild`), not a black-box dependency. Pulling a
component from a registry is design-time research (see `registries.md`); what
lands in your `ui/` dir is hand-owned and re-typed to these conventions.

Examples below are TSX (React). **The pattern is identical** in Vue
(`<script setup>`) and Svelte — only syntax and the `Slot`/icon import differ.

## 1. Folder layout

```
<root>/
  lib/utils.ts        → cn() = twMerge(clsx(...))   — every className composes through this
  components/ui/
    button.tsx        one primitive family per file, kebab-case
    input.tsx
    index.ts          barrel — re-exports each primitive + its variants
```

Root varies by stack (Nuxt `app/`, Next `src/` or `app/`, Astro `src/`). Import
via the alias (`@/components/ui`). After changing tsconfig paths, restart the
editor's TS server — trust the build over a stale editor squiggle.

## 2. Anatomy of a primitive

Five parts, in order. `button` is the reference:

```tsx
/**
 * Component: Button
 * @file <ui>/button.tsx
 * @description Action primitive — paints with semantic tokens, re-skins under theme.
 * @module ui
 */
import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"
import { Slot } from "@/lib/slot"
import { cn } from "@/lib/utils"

const buttonVariants = cva(
  "inline-flex items-center justify-center …",        // base: shared classes
  {
    variants: {
      variant: { default: "…", outline: "…", ghost: "…" },
      size:    { default: "…", sm: "…", icon: "…" },
    },
    defaultVariants: { variant: "default", size: "default" },
  },
)

function Button({ className, variant, size, asChild = false, ...props }
  : React.ComponentProps<"button"> & VariantProps<typeof buttonVariants> & { asChild?: boolean }) {
  const Comp = asChild ? Slot : "button"
  return (
    <Comp
      data-slot="button"
      className={cn(buttonVariants({ variant, size }), className)}
      {...props}
    />
  )
}

export { Button, buttonVariants }
```

Then register it in `index.ts`:

```ts
export { Button, buttonVariants } from "@/components/ui/button"
```

## 3. cva conventions

- Define `cva` **in the component file**, export as `<name>Variants`. No central
  `styles.ts`.
- **Base string** = classes shared by every instance. **`variants`** = the axes
  (usually `variant` for fill/chrome, `size` for dimensions). Always set
  `defaultVariants`.
- Type props as `ComponentProps<"el"> & VariantProps<typeof xVariants>` — that's
  what gives you `onClick`, `disabled`, `aria-*`, `type` for free.
- Stamp `data-slot="<name>"` on the root; add `data-variant` / `data-state` where
  a consumer or test might target it.

## 4. cn() + tailwind-merge — the gotchas

`cn()` = `twMerge(clsx(...))`. `clsx` resolves conditionals; `twMerge` dedupes
conflicting Tailwind utilities so the **last one wins** — that's what makes
call-site `className` overrides work.

- **Same-property group → last wins.** `transition-colors` (base) +
  `transition-transform` (call site) → only the call-site one survives.
- **Neutral default in base, override in variant** — e.g. `bg-transparent` in the
  base, `bg-background` in a variant.
- **svg-size rule:** a base like `[&_svg:not([class*='size-'])]:size-4` forces
  icons to `size-4` unless they carry a `size-` class. Write `<X className="size-5" />`
  (not `h-5 w-5`) to opt out.

Tailwind v4 spacing is dynamic (`h-13` → `calc(var(--spacing) * 13)`); don't add a
redundant `style={{ height: 52 }}` next to it.

## 5. asChild + Slot

Polymorphism without forking the primitive:

```tsx
<Button asChild><a href="/about">About</a></Button>   // renders <a>, keeps Button's classes
```

`Comp = asChild ? Slot : "button"`. The `Slot` source is port-specific —
`@radix-ui/react-slot` (React), `reka-ui` (Vue), or a local dependency-free Slot.
Any primitive that may render as a link/label takes `asChild` rather than growing
a `link` variant or a second component.

## 6. Two token tiers — the one hard rule

1. **Raw palette** — the literal brand colors, declared in the global stylesheet's
   `@theme`. Use only in **brand chrome that never re-themes** (fixed-identity
   pages, logo, sidebar shell).
2. **Semantic tokens** (shadcn naming) — the swappable layer; `:root` maps each to
   a raw value, and a theme overrides them under `.dark` / `[data-theme]`.

**THE RULE: reusable `ui/` primitives use ONLY semantic tokens** (`bg-primary`,
`text-muted-foreground`, `border-border`) — never a raw palette token or a literal
`bg-gray-100`. That's what lets the same component re-skin under a different theme.
Reaching for a raw token inside a primitive breaks theme-portability — the one
hard "don't".

## 7. Extend vs bypass vs inline

When something "doesn't fit the primitive", in order of preference:

1. **Extend the primitive** — add a variant or size. Almost always right.
   (A round FAB → `size="fab"`, not a raw `<button>`. A borderless field →
   `variant="bare"`, not a raw `<input>`.) Principle: **variant/size = identity
   (shape, fill, states); `className` = placement** (fixed/inset/shadow/scale at
   the call site).
2. **Leave it inline** — only for a genuine one-off the primitive can't express
   (a semantic `<ul>`/`<section>` grid). Still use tokens; no hardcoded colors.
3. **Never** leave a raw `<button>`/`<input>`/`<img>` in a page just because the
   primitive needs a small extension. Extend it.

**Extraction threshold:** pull a pattern into `ui/` when it repeats ~3×+ or is a
clear primitive. Don't pre-extract a one-off.

## 8. Images & links

Never a bare `<img>` — wrap in an `Image` primitive (required meaningful `alt`;
lazy/async baked in). Internal route → the framework's `<Link>`; external URL →
`<a target="_blank" rel="noreferrer">`. A primitive that renders as a link uses
`asChild`.

## 9. Checklist — adding a primitive

1. `<ui>/<kebab>.tsx` (or `.vue` / `.svelte`) with the JSDoc header.
2. `cva` exported as `<name>Variants`; base + variants + `defaultVariants`.
3. Props = `ComponentProps<"el"> & VariantProps<…>` (+ `asChild?` if polymorphic).
4. `data-slot` on the root; classes through `cn(xVariants(...), className)`.
5. **Semantic tokens only** (unless it's brand chrome).
6. Corners per the theme's `--radius` (square if the design calls for it).
7. Add to the `index.ts` barrel.
8. Typecheck/build green — trust the build, not a stale editor squiggle.

## 10. Common mistakes

- Raw `<button>`/`<input>`/`<img>` left inline because "it's a one-off" — extend,
  don't bypass.
- Redundant `style={{ width: 52 }}` duplicating an `h-13 w-13` class.
- `alt=""` on a meaningful image.
- A raw palette token inside a re-themeable primitive — breaks `.dark` / `[data-theme]`.
- Trusting the editor squiggle over the build after a tsconfig/barrel change.
