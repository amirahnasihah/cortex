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

## SEO Modules

### @nuxtjs/seo (v5.3.0)

Complete SEO solution. Bundles multiple SEO modules.

```bash
npx nuxi@latest module add seo
```

### @nuxtjs/sitemap (v8.2.1)

XML sitemap generation with SWR caching.

```bash
npx nuxi@latest module add sitemap
```

### @nuxtjs/robots

Robot.txt management.

### @nuxtjs/google-ads

Google Ads integration.

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
