# Nuxt — Routing & Navigation

## File-Based Routing

Every `.vue` file in `app/pages/` creates a route. Uses `vue-router` under the hood.

```
pages/
  index.vue        → /
  about.vue        → /about
  posts/
    [id].vue       → /posts/:id
```

### Nested Routes

```
pages/
  users/
    index.vue      → /users
    [id].vue       → /users/:id
    [id]/
      posts.vue    → /users/:id/posts
```

### Dynamic Catch-All

```
pages/
  [...slug].vue    → /anything/here
```

## Navigation

### `<NuxtLink>`

```vue
<NuxtLink to="/about">About</NuxtLink>
<NuxtLink :to="{ path: '/posts', query: { sort: 'date' } }">Posts</NuxtLink>
```

- Auto-prefetches linked pages when they enter viewport
- Client-side navigation (no full page reload)
- Renders `<a>` tag with proper `href`

### Programmatic Navigation

```ts
const router = useRouter()

await router.push('/about')
await router.replace('/dashboard')
await router.back()
```

### `navigateTo`

```ts
navigateTo('/login')
navigateTo({ path: '/search', query: { q: 'nuxt' } })
```

## Route Parameters

```vue
<script setup>
const route = useRoute()
// /posts/1 → route.params.id === '1'
</script>
```

## Route Middleware

Runs before navigating to a route. Three types:

### 1. Inline (per-page)

```vue
<script setup>
definePageMeta({ middleware: 'auth' })
</script>
```

### 2. Named

`app/middleware/auth.ts`:

```ts
export default defineNuxtRouteMiddleware((to, from) => {
  if (!isAuthenticated()) return navigateTo('/login')
})
```

### 3. Global

`app/middleware/auth.global.ts` — runs on every route change.

**Note:** Route middleware runs in Vue context, not Nitro. For server routes use `server/middleware/`.

## Route Validation

```vue
<script setup>
definePageMeta({
  validate: async (route) => {
    return /^\d+$/.test(route.params.id)
  },
})
</script>
```

## Route Rules (Hybrid Rendering)

```ts
export default defineNuxtConfig({
  routeRules: {
    '/': { prerender: true },
    '/admin/**': { ssr: false },
    '/api/**': { cors: true, cache: { maxAge: 60 } },
    '/blog/**': { isr: 3600 },
  },
})
```

Per-page via `defineRouteRules`:

```ts
defineRouteRules({ prerender: true })
```

## KeepAlive

```vue
<NuxtPage :keepalive="{ max: 10 }" />
```

Or per-page:

```vue
<script setup>
definePageMeta({ keepalive: true })
</script>
```
