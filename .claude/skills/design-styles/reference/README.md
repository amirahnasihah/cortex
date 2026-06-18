# design-styles — reference

Concrete artifacts + sources for the design system. `SKILL.md` is the abstract
spec; these files are the canonical detail. **Markdown only** — no loose,
machine-coupled `.ts`/`.json` files (snippets are inlined), so the skill stays
portable and shareable.

**Reusable by design:** the base system is constant; per project only the token
*values* (color, typography, radius) and the component *port* (stack + package
manager) change. Token *names* stay fixed so components never change to re-theme.

## Map

| Path | What | Layer |
| --- | --- | --- |
| `theme/theme.css` | Canonical oklch token set (light + `.dark` + `@theme inline`) | **stack-agnostic base** |
| `theme/token-reference.md` | Semantic token table → utilities | base |
| `theme/hex-to-oklch.md` | Figma hex → oklch + audit trail | base |
| `shadcn/manual-install.md` | Manual setup (PM- & stack-agnostic; `cn()` + optional `components.json` inline) | port |
| `shadcn/dependencies.md` | Packages + framework ports | port |
| `shadcn/shadcn-patterns.md` | Strict manual `ui/` primitive conventions (cva, `data-slot`, `asChild`, square corners) | port |
| `shadcn/registries.md` | Where to mine components (+ shadcn MCP) | sources |
| `anti-slop.md` | What AI slop looks like + how to escape it (pairs with `/impeccable`, `/taste-skill`) | taste |
| `inspo/design-refs.md` | Taste & motion profile, visual references | taste |
| `typography/` | Offline typography guidance — pairing, readability, accessible/responsive type (Google Fonts + NN/g + web.dev) | taste |
| `examples/button.example.vue` | cva variant pattern (example) | port |
| `animation/gsap-and-lenis.md` | GSAP + ScrollTrigger; Lenis setup (optional) | motion |
| `animation/motion-patterns.md` | Awwwards-tier motion toolkit (GSAP scrub/pin/parallax/text-reveal + Motion/Framer) | motion |
| `assets.md` | Gen-AI image/video pipeline + MCP (generate → optimize → integrate) | sources |
| `design-spec.md` | Pointer to per-client design spec template | per-client |
| `stack-docs.md` | Official docs per framework / PM / design lib | sources |
| `tailwind-v4/` | Offline Tailwind v4 docs (vendored — core + stable) | sources |

## When to read what

- Theme / Figma colors → `theme/*`
- Install shadcn → `shadcn/manual-install.md` (+ `dependencies.md`, `shadcn-patterns.md`)
- Pick a stack / look up docs → `stack-docs.md`
- Avoid the generic AI look → `anti-slop.md`
- Taste / motion direction → `inspo/design-refs.md`, `shadcn/registries.md`
- Motion / animation → `animation/gsap-and-lenis.md`, `animation/motion-patterns.md`
- Typography / fonts → `typography/`, `inspo/design-refs.md`
- Images / video assets → `assets.md`
- Start a client → `design-spec.md`

## Rules

- **oklch always.** Convert Figma hex at the boundary; keep hex as a comment.
- **Reference tokens, never hardcode** — `bg-primary`, not raw oklch.
- **Own the components.** shadcn is copied in and edited, not a black-box dep.
- **Per client:** tune values in `:root` / `.dark`; token *names* stay constant.
- **Per stack/PM:** paths and install command vary; the token layer does not.
