# Nuxt — SEO & Meta

## useHead

```ts
useHead({
  title: 'My Page',
  meta: [
    { name: 'description', content: 'Page description' },
    { property: 'og:title', content: 'My Page' },
  ],
  link: [{ rel: 'icon', href: '/favicon.ico' }],
})
```

## useSeoMeta

Flat object with full TypeScript support:

```ts
useSeoMeta({
  title: 'My Page',
  ogTitle: 'My Page',
  description: 'Page description',
  ogDescription: 'Page description',
  ogImage: '/og-image.png',
  twitterCard: 'summary_large_image',
})
```

## useServerSeoMeta

Same as `useSeoMeta` but only rendered server-side:

```ts
useServerSeoMeta({
  title: 'My Page',
  description: 'Only on server',
})
```

## <NuxtSeo> (via @nuxtjs/seo)

```vue
<SeoKit />
```

Or individual tags:

```vue
<Head>
  <Title>My Site</Title>
  <Meta name="description" content="..." />
  <Link rel="icon" href="/favicon.ico" />
</Head>
```

## Title Template

```ts
useHead({
  title: 'My Page',
  titleTemplate: '%s - My Site',
})
```

## Robots

```ts
export default defineNuxtConfig({
  app: {
    head: {
      meta: [{ name: 'robots', content: 'noindex, nofollow' }],
    },
  },
})
```

Or via `@nuxtjs/seo` module for full control.

## Canonical URL

```ts
useHead({
  link: [{ rel: 'canonical', href: 'https://mysite.com/current-page' }],
})
```

## Open Graph / Twitter

```ts
useSeoMeta({
  ogType: 'website',
  ogLocale: 'en_US',
  ogSiteName: 'My Site',
  ogUrl: 'https://mysite.com',
  twitterSite: '@myhandle',
  twitterCreator: '@myhandle',
})
```

## Sitemap

Use `@nuxtjs/sitemap`:

```bash
npx nuxi@latest module add sitemap
```

Auto-generates XML sitemap from your routes.

## Structured Data (JSON-LD)

```ts
useHead({
  script: [{
    type: 'application/ld+json',
    innerHTML: JSON.stringify({
      '@context': 'https://schema.org',
      '@type': 'WebSite',
      name: 'My Site',
    }),
  }],
})
```
