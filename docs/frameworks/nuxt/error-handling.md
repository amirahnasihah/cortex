# Nuxt — Error Handling

## createError

```ts
import { createError } from 'h3'

// In server API
export default defineEventHandler(() => {
  throw createError({ statusCode: 401, message: 'Unauthorized' })
})
```

## showError

Display full-screen error page:

```ts
showError({ statusCode: 404, message: 'Page not found' })
```

## clearError

```ts
const error = useError()
clearError()  // clears and redirects to / (or as configured)
clearError({ redirect: '/dashboard' })
```

## useError

Access current error in error.vue:

```vue
<script setup>
const error = useError()
</script>

<template>
  <div>
    <h1>{{ error.statusCode }}</h1>
    <p>{{ error.message }}</p>
  </div>
</template>
```

## Custom error.vue

```vue
<!-- app/error.vue -->
<script setup>
defineProps({ error: Object })

function handleError() {
  clearError({ redirect: '/' })
}
</script>

<template>
  <div class="error-page">
    <h1>{{ error.statusCode }}</h1>
    <p>{{ error.message }}</p>
    <button @click="handleError">Go home</button>
  </div>
</template>
```

## <NuxtErrorBoundary>

Catch client-side errors in components:

```vue
<NuxtErrorBoundary @error="logError">
  <RiskyComponent />
  <template #error="{ error }">
    <p>Component failed: {{ error.message }}</p>
  </template>
</NuxtErrorBoundary>
```

## Abort Navigation

```ts
export default defineNuxtRouteMiddleware((to, from) => {
  if (!authorized) {
    return abortNavigation({ statusCode: 403, message: 'Forbidden' })
  }
})
```
