# shadcn — manual install

Stack- and package-manager-agnostic. Components are **copied into the repo and
owned** (edited freely) — not a black-box dep. Use the CLI to scaffold then own
the output, or go fully manual (CLI-free, no `components.json` — see
`shadcn-patterns.md` for the strict variant).

The **theme layer is identical** across ports; only component source differs:
React → shadcn/ui · Vue/Nuxt → shadcn-vue · Svelte → shadcn-svelte.

## Steps

1. **Deps** — install with the project's package manager (`pnpm` / `bun` /
   `npm` / `yarn`). Packages: see `dependencies.md`.

2. **`cn()` util** — add to your utils module (`lib/utils`, `src/lib/utils`, …):

   ```ts
   import { type ClassValue, clsx } from "clsx"
   import { twMerge } from "tailwind-merge"

   export function cn(...inputs: ClassValue[]) {
     return twMerge(clsx(inputs))
   }
   ```

3. **Theme CSS** — paste `../theme/theme.css` into the project's global
   stylesheet, after `@import "tailwindcss";`. Includes the `@theme inline` map.

4. **Components** — copy source into the ui components dir (path varies by
   stack, below). You own them: edit cva variants, spacing, radius to match the
   client design. See `../examples/button.example.vue`.

5. **`components.json`** *(optional)* — only if you drive the CLI. Skip it for a
   fully-manual setup. Minimal shape:

   ```json
   {
     "$schema": "https://ui.shadcn.com/schema.json",
     "style": "new-york",
     "tailwind": { "css": "<global stylesheet>", "baseColor": "neutral", "cssVariables": true },
     "aliases": { "ui": "@/components/ui", "utils": "@/lib/utils" },
     "iconLibrary": "lucide"
   }
   ```

## Per-stack paths

| Stack | Global stylesheet | UI components | Utils |
| --- | --- | --- | --- |
| Nuxt | `app/assets/css/tailwind.css` | `app/components/ui/` | `app/lib/utils.ts` |
| Next | `app/globals.css` | `components/ui/` or `src/components/ui/` | `lib/utils.ts` |
| Astro | `src/styles/global.css` | `src/components/ui/` | `src/lib/utils.ts` |

See `../stack-docs.md` for official docs per stack.

## Ownership

Once copied, components are project code. Re-theming happens in `theme.css`
(token values) — components shouldn't need edits to change the palette.
