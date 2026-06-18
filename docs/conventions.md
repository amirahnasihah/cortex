# Nuxt project conventions — reuse across projects and devs

**Single source of truth** for stack, naming, folder structure, and modules. Keep this in a template repo (e.g. dotclaude) and **copy into each new project** so the repo documents its own conventions. Use the same doc for onboarding, PR review, and AI rules (Cursor / Claude).

---

## Stack (typical)

- **Framework:** Nuxt 4, TypeScript
- **API / CMS:** microCMS (most projects)
- **CSS:** Tailwind v4 + custom Figma design. **Tailwind-first** — if Tailwind can do it, use Tailwind; avoid pure CSS. Pure CSS only as a fallback when Tailwind genuinely can't (or legacy projects).
- **UI components:** shadcn — **manual install**, copied into the repo and owned/customized (port follows the framework: shadcn/ui, shadcn-vue, shadcn-svelte). Theme via tweakcn-style oklch tokens.
- **Animations:** GSAP (+ ScrollTrigger) as the animation plugin, paired with Tailwind. **Lenis** for smooth scroll — **optional, only when the client/design asks for it**.
- **Optional:** @nuxtjs/i18n, @nuxtjs/seo, @nuxt/fonts, @nuxt/image, Pinia, VeeValidate

---

## Naming

| Thing | Convention | Example |
|-------|------------|--------|
| **Variables, functions, composables** | lowerCamelCase | `firstName`, `heroTitleClasses`, `isCompactHeaderVisible` |
| **TypeScript / JS classes, types, interfaces** | PascalCase (UpperCamelCase) | `ArticleItem`, `FirstName`, `MicroCmsArticle` |
| **Vue component names (in template)** | PascalCase | `<VisionSection />`, `<TitleLogo />`, `<LocaleSwitcher />` |
| **File names** | kebab-case | `intro.client.vue`, `locale-switcher.vue`, `modal-news.vue`, `use-article-helpers.ts` |
| **Folder names** | lowercase, kebab-case | `content`, `layout`, `locale-switcher`, `header` |
| **Component files** | Prefer kebab-case for consistency | `vision-section.vue`, `locale-switcher.vue` — Nuxt auto-imports as `VisionSection`, `LocaleSwitcher` |
| **CSS class names (in HTML/Template)** | Tailwind utilities or kebab-case for custom | `text-xl`, `font-bold`, `card-title` |
| **TS/JS class names** | PascalCase | (as above) |

**Rule of thumb:** camelCase for variables/functions, PascalCase for types/classes/component names, kebab-case for files and folders.

---

## Design system — Tailwind tokens + shadcn + tweakcn

Two layers, stack-aware:

- **Theme / tokens** — Tailwind v4 CSS-variable tokens in **oklch**, generated/tuned tweakcn-style. **Stack-agnostic** — same token set everywhere.
- **Reusable UI** — **shadcn, manually installed** (copied into the repo, owned and customized — not a black-box dep). Port follows the framework: React → shadcn/ui, Vue/Nuxt → shadcn-vue, Svelte → shadcn-svelte. The theme layer is identical across ports.

### Color tokens (Figma hex → oklch)

Figma color variables are authored in **hex** (Figma's picker has no oklch mode); tweakcn and Tailwind v4 work in **oklch**. Convert at the boundary: keep hex as the design source of truth, store **oklch** in tokens, leave the original hex as a comment for an auditable map.

- Use the shadcn **semantic token** set (`--background`, `--foreground`, `--primary`, `--muted`, `--border`, `--ring`, `--radius`, …) with light + `.dark` blocks.
- **Reference tokens, never hardcode** — `bg-primary`, `text-foreground`, `border-border`; no raw oklch/hex in components.
- **Why oklch:** perceptually uniform `L` makes tint/shade/hover steps predictable (adjust `L`, keep chroma/hue) and unlocks wider-gamut (P3) colors.
- **Per client:** tune values in `:root` / `.dark`; token *names* stay constant so components don't change.
- **Exception:** if the client brand guide is strict about exact hex, keep the hex comment as the reference/sign-off value.

```css
:root {
  --primary: oklch(0.62 0.19 27);          /* Figma brand #E5484D */
  --primary-foreground: oklch(0.985 0 0);
  --radius: 0.625rem;
  /* ...background, foreground, muted, border, ring, chart-1..5 */
}
.dark { /* ...dark values */ }

@theme inline {
  --color-primary: var(--primary);
  --color-primary-foreground: var(--primary-foreground);
  /* ...map the rest → enables bg-primary, text-muted-foreground, etc. */
}
```

### shadcn manual install

Deps (`clsx`, `tailwind-merge`, `class-variance-authority`, icon set, Tailwind v4 animation helper) → `components.json` → `cn()` in `lib/utils` → paste tweakcn theme + `@theme inline` map → copy components into `components/ui/`. Own them: edit cva variants, spacing, radius to match the client design.

---

## Folder structure

Same “almost same” layout across Nuxt + microCMS projects. Omit or add only what the project needs (e.g. no `i18n/` if single locale).

```
app/
  app.config.ts
  app.vue
  error.vue
  assets/
    css/                    # tailwind.css or global pure CSS
  components/               # by domain / feature
    about/
    button/
    card/
    content/
    layout/
      footer/
      header/
        parts/
    link/
    modal/
    news/
    svg/
    title/
    ui/
  composables/
  constants/
  data/                     # static/dummy data, nav links
  layouts/
    default.vue
  pages/
  plugins/
server/
  api/
  middleware/
shared/
  stores/
  types/                    # microCMS, articles, blocks, etc.
  utils/
i18n/                       # only when project uses i18n
  locales/
    en.json
    ja.json
public/
```

- **Components:** Group by domain (about, card, content, layout, news, ui, …). Use subfolders for parts (e.g. `layout/header/parts/`).
- **Composables:** One file per concern, kebab-case filename, e.g. `use-article-helpers.ts`, `use-header-state.ts`.
- **Types:** Shared in `shared/types/` (microCMS schema, blocks, articles, etc.); import in app and server.
- **Server:** `server/api/` for routes (e.g. microCMS proxy), `server/middleware/` for redirects or locale.

---

## Modules (use when needed)

| Need | Module | When |
|------|--------|------|
| i18n | @nuxtjs/i18n | Multi-locale (en, ja, de, …) |
| SEO | @nuxtjs/seo, @nuxtjs/sitemap | Canonical, hreflang, sitemap |
| Fonts | @nuxt/fonts | Custom fonts from Figma |
| Image | @nuxt/image | microCMS or other image domains |
| State | Pinia | When global state is needed |
| Forms | VeeValidate | When form validation is needed |
| UI components | shadcn (manual install) | Reusable primitives in `components/ui/`, owned + customized; tweakcn theme |
| **No** | MUI, Bootstrap, etc. | Use shadcn + custom Tailwind; pure CSS only when Tailwind can't |

---

## Per-project choices

Tick what applies when starting or documenting a project:

- **i18n:** Yes → add `i18n/`, @nuxtjs/i18n, locale in layout (canonical, hreflang). No → skip.
- **CSS:** “Tailwind + Figma” (default, Tailwind-first). Pure CSS only for legacy or when Tailwind genuinely can’t do it.
- **Animations:** GSAP (+ ScrollTrigger) + Tailwind when design requires; else minimal or none. Smooth scroll via **Lenis** only if the client/design asks for it.
- **Modules:** nuxtseo, nuxtfont, nuxti18n as needed; microCMS + Nuxt + TS are the common base.

Folder structure stays the same; only config and optional folders (e.g. `i18n/`) change.

---

## New project checklist

- [ ] Clone template (nuxt-client-base or nuxt-client-i18n) or copy this folder structure.
- [ ] Copy **conventions.md** (this file) into the new repo so the project documents its own conventions.
- [ ] Set nuxt.config: Tailwind (default, Tailwind-first), optional i18n, SEO, fonts, image.
- [ ] microCMS: `server/api/`, `shared/types/`, env vars.
- [ ] If i18n: `i18n/locales/`, layout canonical/hreflang, locale switcher.
- [ ] If animations: GSAP (+ ScrollTrigger) plugin + Tailwind. Add Lenis smooth scroll only if the client/design asks for it.
- [ ] Add design spec (from `docs/design-spec-template.md`) and, if using Cursor, project rule that references this conventions doc.

---

## Reuse for other devs and AI

- **Onboarding:** “We use this stack and naming; see `conventions.md` (or `docs/conventions.md`).”
- **PR review:** Check variables camelCase, files/folders kebab-case, structure matches this doc.
- **AI (Cursor):** Add a project rule that says: “Follow this project’s conventions: see `conventions.md` — camelCase variables, PascalCase for types/classes/component names, kebab-case for file and folder names, and the folder structure described there.”
- **AI (Claude):** Pin or reference this file in project instructions so generated code matches.
