# Stack docs — frameworks, package managers, design libs

Curated official-docs links. The design system is **stack-agnostic**; this maps
where to look when the *port* (framework / package manager) changes.

## llms.txt — what it is

A standard ([llmstxt.org](https://llmstxt.org)) where a site publishes an
LLM-friendly docs file:
- **`/llms.txt`** — curated index of key docs (a map).
- **`/llms-full.txt`** — all docs concatenated into one file.

**Don't vendor these into the repo** — they're huge and go stale. `WebFetch`
them on demand. For libraries, prefer the **context7 MCP** (live, versioned
docs) over any static link.

> ✓ = verified live (HTTP 200). `—` = no llms.txt at the standard path; link the
> normal docs or use context7 instead. Re-check periodically — sites add/move these.

## Frameworks

| Stack | Docs | llms.txt |
| --- | --- | --- |
| Nuxt 4 | https://nuxt.com/docs · modules: https://nuxt.com/modules | ✓ https://nuxt.com/llms.txt · https://nuxt.com/llms-full.txt |
| Next.js | https://nextjs.org/docs | ✓ https://nextjs.org/docs/llms-full.txt |
| Astro | https://docs.astro.build | — (no llms.txt — link docs / context7) |
| SvelteKit | https://svelte.dev/docs/kit | ✓ https://svelte.dev/llms.txt · https://svelte.dev/llms-full.txt |

## Package managers

| PM | Docs | Install cmd | llms.txt |
| --- | --- | --- | --- |
| pnpm | https://pnpm.io | `pnpm add` | — (link docs) |
| bun | https://bun.sh/docs | `bun add` | ✓ https://bun.sh/llms-full.txt |
| npm | https://docs.npmjs.com | `npm i` | — |
| yarn | https://yarnpkg.com | `yarn add` | — |

No `llms.txt`? Just link the normal docs / use context7 — don't manufacture one.

## Design libraries (prefer context7 MCP)

| Lib | Docs |
| --- | --- |
| Tailwind CSS v4 | https://tailwindcss.com/docs |
| shadcn/ui (React) | https://ui.shadcn.com |
| shadcn-vue | https://www.shadcn-vue.com |
| shadcn-svelte | https://www.shadcn-svelte.com |
| tweakcn (theme editor) | https://tweakcn.com |
| class-variance-authority | https://cva.style |
| GSAP / ScrollTrigger | https://gsap.com/docs |
| Lenis (smooth scroll) | https://lenis.darkroom.engineering |
| Lucide (icons) | https://lucide.dev |

> **Tailwind v4** has no `/llms.txt` at root (404). A curated **offline copy** is
> vendored at `tailwind-v4/` (md only, incl. its own `llms.txt`) — the lone
> intentional exception to *don't vendor*, since Tailwind is core and stable.

## How an agent should use this

1. **Framework behavior** → `WebFetch` the stack's `llms.txt` (index) or
   `llms-full.txt` (everything).
2. **Library API / snippets** → context7: `resolve-library-id` → `query-docs`.
3. **Never** copy these files into the repo — link + fetch on demand.
