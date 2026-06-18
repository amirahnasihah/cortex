# Nuxt SEO — Full Reference

> Source: https://nuxtseo.com · Scraped June 2026

Nuxt SEO is a collection of hand-crafted Nuxt modules for technical SEO and AI discoverability.

## Installation

```bash
npx nuxi@latest module add seo
```

This installs `@nuxtjs/seo` which bundles all core modules. Or install individually:

```bash
npx nuxi@latest module add sitemap
npx nuxi@latest module add robots
npx nuxi@latest module add schema-org
# etc.
```

`nuxt-site-config` installs automatically with any SEO module.

---

## Modules Overview

| Module | Purpose |
|--------|---------|
| `nuxt-site-config` | Shared site URL, name, metadata across all modules |
| `@nuxtjs/sitemap` | XML sitemap generation |
| `@nuxtjs/robots` | robots.txt management |
| `nuxt-og-image` | OG image generation from Vue templates |
| `@nuxt/schema-org` | Schema.org structured data |
| `nuxt-seo-utils` | SEO utilities (breadcrumbs, share links, etc.) |
| `nuxt-link-checker` | Find/fix broken links |
| `nuxt-ai-ready` | AI/LLM discoverability (llms.txt, MCP) |
| `nuxt-skew-protection` | Version skew protection |

---

## Site Config

Set once, use everywhere:

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

Access at runtime:

```ts
const config = useSiteConfig()
// config.url, config.name, etc.
```

---

## @nuxtjs/sitemap

### Basic Setup

```ts
export default defineNuxtConfig({
  modules: ['@nuxtjs/sitemap'],
  siteConfig: { url: 'https://mysite.com' },
})
```

Visit `/sitemap.xml` to verify.

### Features

- Auto-discovers all pages
- Dynamic URL endpoints for CMS/database content
- Multi-sitemap splitting (10k+ pages)
- SWR caching
- Images, videos, news support
- `lastmod`, `priority`, `changefreq`
- I18n locale sitemaps
- Nuxt Content integration
- Zero-runtime build mode

### Dynamic URLs

```ts
// server/api/_sitemap-urls.ts
export default defineEventHandler(() => {
  return [
    { loc: '/blog/my-post', lastmod: new Date().toISOString() },
    // ...
  ]
})
```

### Multi-Sitemaps

```ts
export default defineNuxtConfig({
  sitemap: {
    sources: ['/api/__sitemap__/urls'],
    chunkSize: 10000,
  },
})
```

### Route Rules

```ts
export default defineNuxtConfig({
  routeRules: {
    '/admin/**': { sitemap: false },
  },
})
```

---

## @nuxtjs/robots

### Basic Setup

```ts
export default defineNuxtConfig({
  modules: ['robots'],
})
```

Generates `/robots.txt`. Dev = disallow all, prod = allow all.

### Configuration

```ts
export default defineNuxtConfig({
  robots: {
    allow: ['/'],
    disallow: ['/admin', '/private'],
    sitemap: 'https://mysite.com/sitemap.xml',
  },
})
```

### Per-Page Control

```vue
<script setup>
definePageMeta({ robots: { indexable: false } })
</script>
```

### Bot Detection

```ts
const { isBot } = useBotDetection()
```

### AI Directives

```ts
export default defineNuxtConfig({
  robots: {
    // Block AI training crawlers
    disallow: ['/api/'],
    // Allow AI search assistants
    allow: ['/docs/'],
  },
})
```

---

## nuxt-og-image

### Basic Setup

```bash
npx nuxt-og-image enable takumi  # recommended renderer
npx nuxt-og-image create          # scaffold first template
```

### Define OG Image

```vue
<script setup>
defineOgImage({
  title: 'My Page',
  description: 'Page description',
})
</script>
```

### Renderers

| Renderer | Speed | CSS Support | Edge |
|----------|-------|-------------|------|
| **Takumi** (recommended) | 2-10x faster | Full | Yes |
| Satori | Medium | Limited | Yes |
| Browser | Slow | Full | No (prerender only) |

### Custom Template

```vue
<!-- components/OgImage/Default.vue -->
<template>
  <div class="og-image">
    <h1>{{ title }}</h1>
    <p>{{ description }}</p>
  </div>
</template>

<script setup>
defineProps<{ title: string; description: string }>()
</script>
```

### Styling

Supports Tailwind CSS, UnoCSS, CSS variables, custom fonts.

---

## @nuxt/schema-org

### Basic Setup

```ts
export default defineNuxtConfig({
  modules: ['nuxt-schema-org'],
})
```

### Define Schema

```ts
useSchemaOrg([
  defineWebSite({ name: 'My Site', url: 'https://mysite.com' }),
  defineWebPage({ name: 'Home' }),
])
```

### Identity Setup

```ts
export default defineNuxtConfig({
  schemaOrg: {
    identity: {
      type: 'Organization',
      name: 'My Company',
      url: 'https://mycompany.com',
      logo: '/logo.png',
    },
  },
})
```

### Supported Nodes

- `defineWebSite`, `defineWebPage`, `defineArticle`
- `defineOrganization`, `definePerson`
- `defineProduct`, `defineFAQ`, `defineHowTo`
- `defineBreadcrumb`, `defineEvent`
- And many more...

---

## nuxt-seo-utils

### Composables

```ts
// Breadcrumbs
const items = useBreadcrumbItems()

// Fallback title
const title = useFallbackTitle('My Site')

// Share links
const links = useShareLinks({
  title: 'My Page',
  url: 'https://mysite.com/page',
})
// Returns: { twitter, facebook, linkedin, reddit, ... }
```

### Default Meta

Sets best-practice defaults for:
- Title template
- Canonical URL
- Open Graph tags
- Viewport meta
- Theme color

---

## nuxt-link-checker

```ts
export default defineNuxtConfig({
  modules: ['nuxt-link-checker'],
})
```

- Real-time link validation in DevTools
- Build-time scans for CI/CD
- ESLint integration
- Report generation

---

## nuxt-ai-ready

```ts
export default defineNuxtConfig({
  modules: ['nuxt-ai-ready'],
  aiReady: {
    siteUrl: 'https://mysite.com',
  },
})
```

### Features

- Generates `llms.txt` and `llms-full.txt`
- MCP server endpoint for AI agents
- IndexNow for instant search engine notification
- Runtime sync for dynamic content
- Markdown conversion of HTML pages

---

## Deployment Notes

- Sitemap URLs auto-update on deploy (no localhost in prod)
- OG images require absolute URLs (set `siteConfig.url`)
- Edge runtimes: use Takumi or Satori renderers
- Prerendering: sitemaps and OG images generated at build time

---

## Useful Links

- **Docs**: https://nuxtseo.com
- **GitHub**: https://github.com/harlan-zw/nuxt-seo
- **Sitemap docs**: https://nuxtseo.com/sitemap
- **Robots docs**: https://nuxtseo.com/robots
- **OG Image docs**: https://nuxtseo.com/og-image
- **Schema.org docs**: https://nuxtseo.com/schema-org
- **SEO Learning**: https://nuxtseo.com/learn-seo
