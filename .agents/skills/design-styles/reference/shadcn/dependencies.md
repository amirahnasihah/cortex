# Dependencies

Install with the **project's package manager** — `pnpm add` · `bun add` ·
`npm i` · `yarn add`. Below are the **packages**, not commands.

## Core (all ports)

| Package | Role |
|---------|------|
| `clsx` | Conditional class strings |
| `tailwind-merge` | Dedupe conflicting Tailwind utilities |
| `class-variance-authority` | Typed component variants (cva) |
| `tw-animate-css` | *Optional* — Tailwind v4 animation helper |
| `lucide-*` | Icons — `lucide-vue-next` / `lucide-react` / `lucide-svelte` |

## Component port (pick one)

| Stack | Port | Icons | Primitive dep |
|-------|------|-------|---------------|
| Nuxt / Vue | shadcn-vue | `lucide-vue-next` | `reka-ui` |
| React / Next | shadcn/ui | `lucide-react` | `@radix-ui/*` |
| Svelte | shadcn-svelte | `lucide-svelte` | `bits-ui` |

## Animation stylesheet

If you use `tw-animate-css`, import it in the global stylesheet:

```css
@import "tailwindcss";
@import "tw-animate-css";
```

See `../stack-docs.md` for docs links.
