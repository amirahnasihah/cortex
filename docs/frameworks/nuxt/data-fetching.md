# Nuxt — Data Fetching

## useFetch

Simple wrapper around `$fetch` + `useAsyncData`.

```vue
<script setup>
const { data, pending, error, refresh, status } = await useFetch('/api/users')
</script>
```

### Options

```ts
useFetch('/api/users', {
  method: 'POST',
  body: { name: 'John' },
  query: { page: 1 },
  headers: { Authorization: 'Bearer token' },
  transform: (data) => data.users,
  default: () => [],
  watch: [someRef],
  immediate: true,
  deep: false,
})
```

### Reactive URL/Options

```ts
const id = ref('123')
const { data } = await useFetch(`/api/users/${id}`)
// Re-fetches when id changes
```

## useAsyncData

More control — you provide the fetch function.

```ts
const { data, pending, error, refresh } = await useAsyncData('users', () => {
  return $fetch('/api/users')
})
```

### Options

```ts
useAsyncData('key', fetchFunction, {
  transform: (data) => data.results,
  default: () => [],
  getCachedData: (key, nuxtApp, ctx) => {
    // ctx.cause: 'initial' | 'refresh:hook' | 'refresh:manual' | 'watch'
    return cachedData[key]
  },
  deep: false,
  watch: [someRef],
  immediate: true,
})
```

## Lazy Variants

`useLazyFetch` / `useLazyAsyncData` — don't block navigation.

```ts
const { data, pending } = useLazyFetch('/api/data')
// pending is true while loading, navigation continues
```

## Nuxt 4 Data Fetching Changes

1. **Shared refs** — same key = shared `data`/`error`/`status`
2. **Reactive keys** — computed/ref/getter as key auto-refetches
3. **`getCachedData` context** — `ctx.cause` tells you why fetch happened
4. **Data cleanup** — auto-removed when last consumer unmounts
5. **`shallowRef` by default** — `data` is shallow (pass `deep: true` for deep reactivity)
6. **`pending` alignment** — only `true` when `status` is pending

## clearNuxtData / refreshNuxtData

```ts
clearNuxtData('key')       // clear specific
clearNuxtData()            // clear all
refreshNuxtData('key')     // refresh specific
refreshNuxtData()          // refresh all
```

## useNuxtData

Read cached data without refetching:

```ts
const { data } = useNuxtData('key')
```

## $fetch (utility)

Global helper for HTTP requests (uses `ofetch`):

```ts
const data = await $fetch('/api/users')
const data = await $fetch('/api/users', { method: 'POST', body: { name: 'John' } })
```
