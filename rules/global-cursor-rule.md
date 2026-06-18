# Global Cursor Rule — Frontend Dev for International Clients

**Paste the content below into Cursor Settings → Rules → Global rules** so every chat gets this context.

---

## Role
Frontend developer working with international clients (Japan, Germany, Malaysia, etc.). Stack: **Nuxt 4, Vue 3, Tailwind, TypeScript**.

---

## Key Principles

### 1. **Always assume i18n**
- Multi-locale from day one (en, ja, de, etc.)
- Use `@nuxtjs/i18n` for locale routing (`/`, `/ja`, `/de`)
- Locale JSON files in `i18n/locales/{locale}.json`
- Key naming: `pageName.sectionName.property` (e.g., `about.vision.title`)
- Translations: **formal tone for corporate clients** (JP: です・ます, DE: Sie), casual for startups (ask if unsure)

### 2. **Custom design per project**
- **No assumption of shadcn, MUI, or design system libraries** unless explicitly stated
- Each client has custom Tailwind (colors, fonts, spacing from Figma or brand)
- When adding new components: **mirror existing component patterns** (section layout, card structure, etc.)
- Use the project-specific design spec for colors, fonts, spacing

### 3. **SEO + i18n layout pattern**
Default pattern (unless project overrides):
- `app/layouts/default.vue` sets:
  - Canonical URL from `route.path` (no query params to avoid duplicate content)
  - Hreflang for all active locales
  - `lang` attribute from current locale
- Pages use `useSeoMeta` + `useHead` for title, description, og*, twitter
- Schema.org JSON-LD where applicable: Organization, WebSite, Article, ItemList, BreadcrumbList

### 4. **Code style**
- **Type-driven:** use `shared/types` for reusable types; prefer `unknown` over `any`
- **Functional:** prefer `map`, `filter`, `find` over `for` loops
- **No switch:** use objects/maps for lookup instead
- **Single source of truth:** composables in `app/composables`, no duplicated exports

### 5. **Naming**
- **Variables, functions, composables:** lowerCamelCase (e.g. `firstName`, `heroTitleClasses`)
- **TypeScript classes, types, component names:** PascalCase (e.g. `ArticleItem`, `VisionSection`)
- **File and folder names:** kebab-case (e.g. `locale-switcher.vue`, `use-article-helpers.ts`, folder `content/`, `locale-switcher/`)
- **CSS in template:** Tailwind or kebab-case; TS/JS classes stay PascalCase  
  For full conventions (folder structure, modules, per-project choices), use the project’s **conventions.md** or **docs/conventions.md** if present; otherwise see dotclaude **docs/conventions.md**.

### 6. **Workflow checklist**
When generating new components or pages:
1. **Check existing patterns:** ask which component to mirror (e.g., "same section pattern as VisionSection")
2. **Add i18n keys** for all active locales
3. **Use Tailwind classes** matching the project's design spec
4. **Add SEO meta** if it's a page (useSeoMeta, schema if applicable)

---

## Stack Defaults (override per project)
- **Framework:** Nuxt 4 (app/, server/ at root)
- **i18n:** @nuxtjs/i18n with path prefix (`/`, `/ja`, etc.)
- **Styling:** Tailwind v4 (custom config per project)
- **SEO:** @nuxtjs/sitemap, useSeoMeta, canonical + hreflang in layout
- **CMS:** varies per client (microCMS, Contentful, or static JSON)
- **Animation:** GSAP + ScrollTrigger where needed

---

## What to ask before generating
1. **Locale(s):** which languages for this task? (en, ja, de, etc.)
2. **Design:** custom Tailwind or a design system? If custom, which existing component to mirror?
3. **SEO:** is this a page (needs meta) or a component?
4. **Tone:** formal or casual for copy/translations?

---

## Project-specific rules
- If the project has `.cursor/rules/` or `CLAUDE.md`, **follow those** for stack, locales, conventions, and source-of-truth components.
- When in doubt, ask or follow the structure of existing files in the repo.
