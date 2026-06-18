# Nuxt — Modules & Integrations

## What Are Modules

Extend Nuxt with custom features and third-party integrations. 313+ modules in ecosystem.

## Adding Modules

```bash
npx nuxi@latest module add <module-name>
```

Or manually:

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  modules: ['@nuxtjs/tailwindcss', '@nuxt/image'],
})
```

## Key Official Modules

### @nuxt/ui (v4.9.0)

UI library — Reka UI + Tailwind CSS. 110+ components.

```bash
pnpm add @nuxt/ui tailwindcss
```

```ts
export default defineNuxtConfig({ modules: ['@nuxt/ui'] })
```

### @nuxt/image (v2.0.0)

Image optimization. 20+ providers (Cloudinary, Imgix, etc.).

```bash
npx nuxi@latest module add image
```

### @nuxt/content (v3.14.0)

File-based CMS — Markdown, YAML, JSON. MDC syntax (Vue in Markdown).

```bash
npx nuxi@latest module add content
```

### @nuxt/scripts

Third-party script management without perf sacrifice.

### @nuxt/fonts

Web font optimization.

### @nuxt/icon

200K+ icons via Iconify.

### @nuxt/eslint

ESLint integration with flat config support.

### @nuxt/test-utils

Testing utilities.

### @nuxt/hints

Performance and security hints.

### @nuxt/a11y

Real-time accessibility feedback.

## SEO Modules — Nuxt SEO Ecosystem (nuxtseo.com)

The `@nuxtjs/seo` meta-module bundles the entire SEO ecosystem into one install.

```bash
npx nuxi@latest module add seo
```

Or install modules individually for version pinning.

### Site Config (`nuxt-site-config`)

Shared config across all SEO modules. Install automatically with any SEO module.

```ts
export default defineNuxtConfig({
  siteConfig: {
    url: 'https://mysite.com',
    name: 'My Site',
    description: 'Site description',
    ogImage: '/og.png',
    titleSeparator: ' | ',
    titleTemplate: '%s - My Site',
  },
})
```

### @nuxtjs/sitemap (v8.2.1)

XML sitemap generation. Auto-discovers pages, SWR caching, multi-sitemap support.

```bash
npx nuxi@latest module add sitemap
```

- Single `/sitemap.xml` or chunked multi-sitemaps
- Dynamic URL endpoints (CMS, databases)
- Integrates with Nuxt Content and Nuxt I18n
- DevTools integration for debugging
- Zero-runtime mode available

### @nuxtjs/robots (v6.x)

Robot.txt management with best-practice defaults.

- Dev disallows by default (safe)
- Per-page indexing control via `definePageMeta`
- Bot detection with client-side fingerprinting
- AI directives (Content-Usage, Content-Signal)
- Route rules for dynamic config
- Integrates with I18n and Nuxt Content

```ts
export default defineNuxtConfig({
  robots: {
    allow: '/admin',
    disallow: '/private',
  },
})
```

### nuxt-og-image (v6.x)

Generate OG images from Vue components or screenshots.

- Vue template-based OG images
- 3 renderers: **Takumi** (recommended, 2-10x faster), Satori, Browser
- Custom fonts, emojis, Tailwind CSS support
- Edge runtime compatible (Cloudflare, Vercel Edge)
- DevTools playground with HMR

```bash
npx nuxt-og-image enable takumi
npx nuxt-og-image create  # scaffold first template
```

### @nuxt/schema-org

Automatic Schema.org structured data graphs.

- Type-safe composables
- Identity setup for site-wide schemas
- Integrates with Nuxt Content
- I18n support

### nuxt-seo-utils

SEO utilities — canonical URLs, breadcrumbs, share links, fallback titles.

- `useBreadcrumbItems()` — breadcrumb navigation
- `useFallbackTitle()` — enhanced page titles
- `useShareLinks()` — social share URLs
- Default meta tags, app icons, route rules

### nuxt-link-checker

Find and fix broken links affecting SEO.

- Real-time DevTools inspection
- Build-time scans for CI
- ESLint integration
- Reports generation

### nuxt-ai-ready

AI & LLM discoverability.

- Generates `llms.txt` and `llms-full.txt`
- MCP server for AI agents
- IndexNow integration
- Runtime sync for dynamic content

## UI / CSS Modules

| Module | Purpose |
|--------|---------|
| `@nuxtjs/tailwindcss` | Tailwind CSS |
| `@unocss/nuxt` | UnoCSS atomic CSS |
| `@nuxtjs/color-mode` | Dark/light mode |
| `@nuxtjs/google-fonts` | Google Fonts |
| `@vueuse/nuxt` | VueUse composables |

## i18n

```bash
npx nuxi@latest module add i18n
```

## Authentication

| Module | Purpose |
|--------|---------|
| `@logto/nuxt` | Logto auth |
| `@nuxtjs/kinde` | Kinde auth |
| `@sidebase/nuxt-auth` | NextAuth/AuthJS |
| `nuxt-auth-utils` | Auth utilities |

## CMS

| Module | Purpose |
|--------|---------|
| `@nuxt/content` | File-based CMS |
| `@nuxtjs/sanity` | Sanity CMS |
| `@storyblok/nuxt` | Storyblok |

## Creating Custom Modules

See [Nuxt Module Guide](https://nuxt.com/docs/guide/modules).

```ts
// my-module/src/module.ts
import { defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  meta: { name: 'my-module' },
  setup(options, nuxt) {
    // Module logic
  },
})
```

## Third-Party Scripts

```ts
export default defineNuxtConfig({
  scripts: {
    analytics: {
      googleAnalytics: { id: 'G-XXXXXXXXXX' },
    },
  },
})
```
