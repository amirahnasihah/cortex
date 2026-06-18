# Nuxt — State Management

## useState

SSR-friendly reactive shared state.

```ts
const count = useState('counter', () => 0)
```

- Key identifies the state across components
- Initial value is a factory function (SSR safety)
- Shared across all components using the same key

### Example

```vue
<script setup>
const count = useState('counter', () => 0)

function increment() {
  count.value++
}
</script>

<template>
  <button @click="increment">{{ count }}</button>
</template>
```

### With Composables

```ts
// composables/useCounter.ts
export function useCounter() {
  const count = useState('counter', () => 0)
  const increment = () => count.value++
  const decrement = () => count.value--
  return { count, increment, decrement }
}
```

## clearNuxtState

```ts
clearNuxtState('counter')    // clear specific key
clearNuxtState()             // clear all state
```

Nuxt 4: resets to initial value (not `undefined`).

## clearNuxtState with Options

```ts
clearNuxtState('counter', { reset: false })  // set to undefined
```

## useNuxtData

Access cached data from `useAsyncData`/`useFetch` without refetching:

```ts
const { data } = useNuxtData('myKey')
```

## Pinia (External)

For complex state management, use Pinia:

```bash
npm install @pinia/nuxt
```

```ts
// nuxt.config.ts
export default defineNuxtConfig({ modules: ['@pinia/nuxt'] })
```

```ts
// stores/counter.ts
export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const increment = () => count.value++
  return { count, increment }
})
```

## State Patterns

### Global State

```ts
// Shared across all components
const theme = useState('theme', () => 'light')
```

### Per-Page State

```ts
// composables/usePageData.ts
export function usePageData(id: string) {
  return useState(`page-${id}`, () => null)
}
```

### Persistent State

```ts
// Use useCookie for persistence
const token = useCookie('auth-token')
```
