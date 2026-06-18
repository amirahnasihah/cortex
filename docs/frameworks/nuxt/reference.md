# Nuxt — Quick Reference

## Key Composables

| Composable | Purpose |
|------------|---------|
| `useRoute()` | Current route info |
| `useRouter()` | Router instance |
| `useFetch()` | SSR-friendly fetch |
| `useAsyncData()` | Custom async data |
| `useLazyFetch()` | Fetch without blocking nav |
| `useLazyAsyncData()` | Async data without blocking nav |
| `useState()` | Reactive SSR-safe state |
| `useRuntimeConfig()` | Access runtime config |
| `useAppConfig()` | Access app config |
| `useCookie()` | Read/write cookies |
| `useHead()` | Manage `<head>` tags |
| `useSeoMeta()` | SEO meta tags (flat) |
| `useNuxtApp()` | Runtime app context |
| `useError()` | Current error |
| `useRequestHeaders()` | Server request headers |
| `useRequestURL()` | Server request URL |
| `useRequestEvent()` | Server request event |

## Key Components

| Component | Purpose |
|-----------|---------|
| `<NuxtPage>` | Render current page |
| `<NuxtLayout>` | Apply layout |
| `<NuxtLink>` | Navigation link (auto-prefetch) |
| `<NuxtLoadingIndicator>` | Progress bar |
| `<NuxtErrorBoundary>` | Error catching |
| `<ClientOnly>` | Client-side only rendering |
| `<DevOnly>` | Dev-only rendering |
| `<NuxtImg>` | Optimized images (via @nuxt/image) |
| `<NuxtPicture>` | Responsive pictures |
| `<NuxtSeo>` | SEO tags (via @nuxtjs/seo) |

## Key Utilities

| Utility | Purpose |
|---------|---------|
| `definePageMeta()` | Page metadata (layout, middleware, etc.) |
| `defineNuxtRouteMiddleware()` | Create route middleware |
| `defineEventHandler()` | Create server event handler |
| `defineNitroPlugin()` | Create Nitro plugin |
| `defineNuxtPlugin()` | Create Nuxt plugin |
| `defineAppConfig()` | App configuration |
| `navigateTo()` | Programmatic navigation |
| `abortNavigation()` | Stop navigation |
| `$fetch()` | HTTP requests (ofetch) |
| `clearNuxtData()` | Clear cached data |
| `refreshNuxtData()` | Refresh cached data |
| `clearNuxtState()` | Clear useState values |
| `createError()` | Create error object |
| `showError()` | Show error page |
| `clearError()` | Clear error state |
| `callOnce()` | Run code once (SSR/CSR) |
| `preloadComponents()` | Preload components |
| `prefetchComponents()` | Prefetch components |
| `preloadRouteComponents()` | Preload route components |

## Key Directories

| Directory | Purpose |
|-----------|---------|
| `app/pages/` | File-based routes |
| `app/components/` | Auto-imported components |
| `app/composables/` | Auto-imported composables |
| `app/layouts/` | Page layouts |
| `app/middleware/` | Route middleware |
| `app/plugins/` | Nuxt plugins |
| `app/assets/` | Processed assets |
| `app/utils/` | Auto-imported utilities |
| `server/api/` | API routes |
| `server/middleware/` | Server middleware |
| `server/plugins/` | Nitro plugins |
| `server/utils/` | Server utilities |
| `public/` | Static assets |
| `shared/` | Code shared between app and server |
| `content/` | File-based CMS (Nuxt Content) |
| `layers/` | Nuxt layers |

## CLI Commands

| Command | Purpose |
|---------|---------|
| `npx nuxi init` | Create new project |
| `npx nuxi dev` | Start dev server |
| `npx nuxi build` | Build for production |
| `npx nuxi generate` | Static site generation |
| `npx nuxi preview` | Preview production build |
| `npx nuxi typecheck` | Run type checking |
| `npx nuxi test` | Run tests |
| `npx nuxi module add` | Add a module |
| `npx nuxi upgrade` | Upgrade Nuxt |
| `npx nuxi prepare` | Generate types |
| `npx nuxi info` | Project info |
| `npx nuxi analyze` | Bundle analysis |
| `npx nuxi devtools` | Toggle devtools |

## Common Config Options

```ts
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [],
  css: [],
  runtimeConfig: { public: {} },
  app: { head: {}, pageTransition: {} },
  routeRules: {},
  vite: {},
  postcss: {},
  typescript: {},
  nitro: {},
  experimental: {},
})
```

## Nuxt Module Ecosystem

### Top Modules by Category

| Category | Modules |
|----------|---------|
| **UI** | `@nuxt/ui`, `nuxt-icon`, `@nuxt/fonts` |
| **CSS** | `@nuxtjs/tailwindcss`, `@unocss/nuxt` |
| **SEO** | `@nuxtjs/seo`, `@nuxtjs/sitemap`, `@nuxtjs/robots` |
| **Images** | `@nuxt/image`, `nuxt-cloudinary` |
| **CMS** | `@nuxt/content`, `@nuxtjs/sanity` |
| **Auth** | `@logto/nuxt`, `@nuxtjs/kinde`, `@sidebase/nuxt-auth` |
| **Analytics** | `@vercel/analytics`, `@nuxtjs/google-analytics` |
| **Testing** | `@nuxt/test-utils` |
| **DevTools** | `@nuxt/devtools` |
| **Performance** | `@nuxt/scripts`, `nuxt-prefetch` |

## Useful Links

- Docs: https://nuxt.com/docs
- Modules: https://nuxt.com/modules
- GitHub: https://github.com/nuxt/nuxt
- Discord: https://chat.nuxt.dev
- LLMs: https://nuxt.com/llms.txt
- Full docs (for LLMs): https://nuxt.com/llms-full.txt
