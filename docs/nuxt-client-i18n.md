# nuxt-client-i18n — internal framework definition

**Not public. Not open source. Your professional backbone.**

This doc defines what nuxt-client-i18n is, what it is not, and how it evolves. Lock this. Do not change per project unless absolutely necessary. Changes are versioned (v1, v2).

---

## What it is NOT

- A starter template
- A copied previous project
- A random boilerplate

---

## What it IS

> **A controlled, opinionated Nuxt architecture system for all OSBR projects.**

Once this is defined, you stop copying old projects forever.

---

## Stack (locked)

- Nuxt 4
- TypeScript (strict)
- microCMS
- @nuxtjs/seo (nuxtseo)
- @nuxt/fonts (nuxtfont)
- @nuxtjs/i18n (nuxti18n)
- Tailwind (modern projects)
- GSAP (optional; isolated module)

---

## Folder structure (locked)

Do not change per project unless absolutely necessary.

```
nuxt-client-i18n/
├── app/
│   ├── components/
│   │   ├── content/
│   │   ├── layout/
│   │   └── ui/
│   ├── composables/
│   │   ├── useMicrocms.ts
│   │   ├── useSeo.ts
│   │   ├── useLocalePath.ts
│   │   └── useGsap.ts
│   ├── layouts/
│   ├── pages/
│   ├── plugins/
│   ├── utils/
│   ├── types/
│   └── constants/
├── server/
│   └── api/
├── shared/
│   └── types/
├── assets/
├── public/
├── nuxt.config.ts
└── tsconfig.json
```

When i18n is used: `i18n/locales/` (e.g. `en.json`, `ja.json`). English default (no `/en`), Japanese `/ja`.

---

## Naming conventions (locked policy)

Lock this across ALL projects built on nuxt-client-i18n.

### Variables

- **lowerCamelCase**  
  Example: `const firstName = ""`, `const siteTitle = ""`

### Types / interfaces / classes

- **PascalCase**  
  Example: `interface NewsItem {}`, `type CmsPage = {}`, `class SeoManager {}`

### Vue components

- **PascalCase** (file names)  
  Example: `HeroSection.vue`, `VisionStatementSection.vue`, `SeoMetaHead.vue`

### Composables

- **lowerCamelCase**, file name starts with `use`  
  Example: `useMicrocms.ts`, `useSeo.ts`, `useGsapIntro.ts`

### Folders

- **lowercase only**
- **No kebab** in folder names
- **No PascalCase** folder names  
  Example: `components/`, `composables/`, `layouts/`, `pages/`, `utils/`, `types/`, `constants/`, `content/`, `layout/`, `ui/`

---

## Core systems (locked)

### 1. Standard microCMS layer

- **Only ONE composable allowed:** `useMicrocms()`
- No direct fetch inside components
- No duplicate API logic
- All projects use the same pattern

### 2. Standard SEO layer

- **One composable:** `useSeo()`
- Handles: canonical, og:image, hreflang, locale-aware routing, title template
- No custom SEO per page unless passed as param

### 3. i18n strategy (locked)

- English default (no `/en` in path)
- Japanese `/ja`
- Canonical aware of locale
- No duplicated head logic (single place in layout / useSeo)

### 4. GSAP pattern (optional)

- Provide `useGsap.ts`
- Register plugin in plugin file
- Keep animation isolated
- Never mix animation logic with layout logic

---

## Versioning and evolution

- If nuxt-client-i18n changes, it changes **versioned**: `nuxt-client-i18n v1`, `nuxt-client-i18n v2`.
- Do NOT:
  - Improve structure randomly per project
  - Add modules differently per project
  - Change naming convention mid-way

Controlled evolution only.

---

## Future MCP (Level 3, only when stable)

When the architecture is stable, a hosted MCP may support:

1. **osbr.getProjectStandard** — Returns naming + folder rules.
2. **microcms.getSchema(projectKey)** — For different clients.
3. **microcms.generateTypes(projectKey, endpoint)** — Type generation from microCMS.

Do not build more until needed.

---

## Where v1 lives

- **Template:** `templates/nuxt/nuxt-client-i18n/` in this repo (dotclaude).
- **New client project:** Clone or copy from `templates/nuxt/nuxt-client-i18n/`; then only project-specific content and config (site name, domain, microCMS keys) change. Structure and naming stay locked.
